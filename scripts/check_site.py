"""Check static pages, local links and assets without network access."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.refs = []
        self.errors = []
        self.h1_count = 0
        self.has_title = False
        self.has_description = False
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                self.errors.append(f"Duplicate ID: {attrs['id']}")
            self.ids.add(attrs["id"])
        self.h1_count += tag == "h1"
        self.has_title |= tag == "title"
        self.has_description |= tag == "meta" and attrs.get("name") == "description"
        if tag == "img" and "alt" not in attrs:
            self.errors.append("Image missing alt attribute")
        for attr in ("href", "src"):
            if attr in attrs:
                self.refs.append(attrs[attr])


def check(root):
    root = root.resolve()
    files = list(root.glob("*.html")) + list((root / "systems").glob("*.html"))
    pages = {p.resolve(): Page(p) for p in files}
    errors = []
    for path, page in pages.items():
        for error in page.errors:
            errors.append(f"{path.relative_to(root)}: {error}")
        if page.h1_count != 1 or not page.has_title or not page.has_description:
            errors.append(f"{path.name}: expected one h1, title and description")
        for ref in page.refs:
            url = urlsplit(ref)
            if url.scheme in ("https", "http", "mailto", "tel"):
                continue
            if url.scheme or url.netloc or url.path.startswith("/"):
                errors.append(f"{path.name}: unsupported or root-relative reference {ref}")
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.is_relative_to(root):
                errors.append(f"{path.name}: reference escapes site: {ref}")
            elif not target.is_file():
                errors.append(f"{path.name}: missing target {ref}")
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f"{path.name}: missing fragment {ref}")
    if not (root / "index.html").is_file() or len(pages) < 2:
        errors.append("Missing homepage or system pages")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Checked {len(pages)} HTML pages: local links, fragments, assets and page metadata pass.")


if __name__ == "__main__":
    check(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1])
