# MCDC Data Platform website

Static public website based on `MCDC_Data_Platform.html`, with an overview and 13 individual system pages. No application server, credentials, third-party fonts or JavaScript packages are needed.

## Preview and check

```bash
python3 scripts/build_site.py
python3 -m http.server 8080 --directory _site
```

Open <http://localhost:8080/>. The build validates local links, fragments, page metadata and referenced assets, then copies the public pages into `_site`. To check without staging, run `python3 scripts/check_site.py`.

## Publish on GitHub Pages

1. Add these files to the intended GitHub repository and push to its default branch.
2. In **Settings → Pages → Build and deployment**, select **GitHub Actions** as the source.
3. Run **Check and deploy GitHub Pages** from the Actions tab, or push a change to the default branch. The deployment job reports the published URL.

Pull requests and other branches run the build checks; only the default branch deploys. The workflow follows the [GitHub Pages custom workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

All site links and asset paths are relative, so the same files work on a `github.io/repository/` project site, an account site or a custom domain. No hostname is assumed. For a custom domain, configure it in the repository's Pages settings.

This workspace has no usable Git checkout or configured remote. No commit, push or live deployment has been performed.

## Editing

- `index.html`: platform overview, system directory and contact information.
- `systems/*.html`: system capabilities, workflow, outputs, scope and related systems.
- `assets/site.css` and `assets/site.js`: shared responsive styles, mobile menu and screenshot lightbox.
- `assets/*.png`: extracted images from the supplied overview; `booking.svg` is an illustrative calendar replacing a screenshot with a visible staff name.
- `scripts/build_site.py`: explicit publishing list. Only `index.html`, `systems/`, `assets/`, `.nojekyll` and a safe copy of the homepage at the original filename are published.

`MCDC_Data_Platform.html` is now a compatibility redirect to the overview. The build places a copy of the current homepage at that filename so legacy links and section anchors work in the deployed site. Use the staged `_site` artifact and the supplied workflow. The original standalone file was backed up locally to `/tmp/MCDC_Data_Platform.original.html` before replacement; it is not included in the repository or published artifact.

## Content evidence

The system descriptions were checked against these neighbouring repository files on 6 November 2026. These are local source references for maintainers, not public application links. No credentials, databases, patient records or internal resource identifiers were copied into the site.

| Pages | Local evidence | Scope reflected in public copy |
| --- | --- | --- |
| TriOx | `../TriOx/README.md` | Study forms, referrals, manifests, role-scoped reports |
| MCDC LIMS | `../lims/README.md`, `../LIMS2/README.md`, `../Tracker/README.md` | Legacy workflows, read-only snapshots and prototype kept distinct |
| Stock | `../Stock/ARCHITECTURE.md`, `../Stock/REQUIREMENTS_2_0_STATUS.md` | Inventory lifecycle; partial requirements do not imply completed validation |
| Booking | `../WebBOOKING/README.md` | Resource calendars, permissions and project/cost-centre attribution |
| WebNGS | `../WebNGS/README.md` | Run planning, QC, workers, analysis, reporting and tracking |
| Sample Sheet Validator | `../samplesheet/README.md` | CSV comparison and configured validation rules |
| WebIGV | `../WebIGV/README.md`, `../WebNGS/README.md` | Separate viewer and project-specific interpretation/reporting workflows |
| WebEQA | `../WebEQA/README.md` | Schemes, distributions, configurable workflows, audit and reminders |
| Sample Tracker | `../Tracker/README.md`, `../WebNGS/README.md` | Manifest receipt, storage, usage, handover and read-only LIMS views |
| REDCap, local systems, AWS, Illumina | Supplied overview; WebNGS README for configured S3/BaseSpace use | Project-dependent capabilities, with unverified live integrations explicitly qualified |

Repository documentation supports capability descriptions, not claims about current production deployment, certification or study approval. The public copy avoids release-specific status claims and routes availability questions to MCDC.
