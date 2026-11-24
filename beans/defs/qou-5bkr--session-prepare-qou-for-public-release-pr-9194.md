---
# qou-5bkr
title: 'Session: prepare qou for public release (PR #9194)'
status: in-progress
type: epic
priority: normal
created_at: 2026-11-23T21:14:50Z
updated_at: 2026-11-24T17:54:38Z
---

EXTERNAL AGENT ACTIVE (HANDS-OFF FOR SWARM, 2026-11-23):
- PR #9194 rebase-merged onto main (21:36Z).
- External agent actively working on:
  1. Scan full git history for secrets, emails, private paths;
  2. Build site + Lean + PDF locally (no deploy);
  3. Add Read-the-work links to the site home page;
  4. Add CITATION.cff (no Zenodo release yet).
STRICT SWARM DECONFLICTION: Do NOT touch CITATION.cff, site home_page / index landing page, README.md, CONTRIBUTING.md, CONTRIBUTORS.md, authors-note, build-site.sh, publish-main-local.sh, or run gh-pages deploy while external agent owns this track.

## 2026-11-24 — fence crossed on owner's direct request (litlfred/qou#9383)

The owner asked directly (2026-11-24, "2y 3y 4y" and follow-ups) for the site landing, the work-plan page and the QA wiring. #9383 edits `scripts/build-site.sh`, `scripts/publish-main-local.sh` and one README row (links only), which this bean fences to the public-release agent. Recorded here so that agent sees it.
