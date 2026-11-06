"""Validate and stage only public site files for GitHub Pages."""
from pathlib import Path
import shutil

from check_site import check

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "_site"


def build():
    check(ROOT)
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir()
    for name in ("index.html", ".nojekyll"):
        shutil.copy2(ROOT / name, OUTPUT / name)
    for name in ("assets", "systems"):
        shutil.copytree(ROOT / name, OUTPUT / name)
    # Keep existing links to the supplied filename working without publishing
    # a duplicate content source.
    shutil.copy2(ROOT / "index.html", OUTPUT / "MCDC_Data_Platform.html")
    check(OUTPUT)
    print(f"Public site staged in {OUTPUT}")


if __name__ == "__main__":
    build()
