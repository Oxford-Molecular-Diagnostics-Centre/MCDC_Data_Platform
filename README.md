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

The configured remote is `Oxford-Molecular-Diagnostics-Centre/MCDC_Data_Platform`. Local edits and a staged build do not publish changes; deployment requires a push through the configured publishing workflow.

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


## Feedback applied on 12 November 2026

The latest message from Helene Dreau in the supplied `RE Request for 1-2 slides.msg` guides this update. Earlier requests in the quoted chain concern presentation slides and are background, not additional deliverables.

- Use the same five workflow labels in the hero diagram, lifecycle and detailed sections: clinical cohort and study metadata; sample management; laboratory operations and analytical testing; biomarker data and analytical results; reporting and collaboration.
- Keep data generation and analysis together. Show IT, storage, resource management and quality management as infrastructure supporting all stages. Preserve existing section anchors, including `#laboratory`, `#analysis`, `#storage` and `#quality`.
- Group the directory by the cross-cutting OPS, QMS and IT functions marked on the email screenshots. Show all three spanning the entire five-stage workflow. The directory features 12 systems; sample-sheet checks sit within WebNGS, with the existing comparison detail page retained for supporting information and legacy links.
- Use Histopathology Services as the current display name while retaining the established service URL. Include molecular and cellular outputs in the overview and results descriptions.
- Context: the supplied `MCDC - SRF 2026 (Presentation).pptx`, including its integrated pathway and laboratory capabilities, and the Oxford Cancer MCDC webpage supplied by the user. Its indexed MCDC content was accessible under `https://www.cancer.ox.ac.uk/support/omdc`; direct page retrieval was unavailable.

**Coordination still required:** Konstantin and Sara need to agree the plans and destination for the Project Initiation Document (PID) form on the Cancer Centre website. The existing “Discuss a project” email link remains in place until that destination is agreed. No message has been sent to Sara and no form migration has been performed.

Source email, presentation and review notes are excluded from the public `_site` build by the explicit publishing list in `scripts/build_site.py`.


### Follow-up visual revisions

- OPS groups study capture, LIMS, MCDC Sample Tracker, stock and booking. QMS groups EQA and the shared quality controls. IT groups WebNGS, Illumina, WebIGV, local systems and AWS. These are functional groupings; QMS and IT support operational systems as well.
- Every system detail page returns to its OPS, QMS or IT overview. Existing workflow section anchors remain available.
- Screenshot images render at their natural proportions without fixed-height clipping or hover enlargement. The existing source image files are retained.
- Capability cards, laboratory services, directory groups and infrastructure cards now have images. Python and Illumina wordmarks are unmodified; the other new illustrations use locally cached Lucide icons. Sources and licenses are included in `assets/illustrations/SOURCES.txt`, `LUCIDE-LICENSE.txt` and `FEATHER-LICENSE.txt`.
- The image sources are [Lucide](https://lucide.dev/license), the [Python Software Foundation](https://www.python.org/community/logos/) and the [Illumina wordmark file on Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Illumina_logo.svg). No external asset requests are needed when viewing the website.
