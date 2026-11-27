---
# qou-zo8u
title: '[DEFERRED per owner] Public release 1c: Repo README & site index links + bean further public-prep options'
status: in-progress
type: task
priority: deferred
tags:
    - held-public-release
created_at: 2026-11-23T21:31:07Z
updated_at: 2026-11-27T14:30:00Z
parent: qou-5bkr
---

DEFERRED per owner directive 2026-11-23 ('dont work public release'; related: qou-hksc). Scope when unheld: update repo README.md and site index landing page to link web view, monograph PDF, rendered Lean library (folio-assistant-sci lean-html-docs), QA report, CONTRIBUTING.md, and CC BY 4.0 / Apache-2.0 license; list further public-release preparation options for owner and bean them.

## 2026-11-24 — in progress (litlfred/qou#9383; owner requested directly, overriding the deferral)

Landing links built from declarations by `scripts/build-site-landing.py`: web view (cat-harness/folio/<paper>/), PDF (papers/<paper>/<paper>.pdf), other documents, every coverage.visualiser in qou.json (Accuracy, QA, Work plan, Lean), Source, CONTRIBUTING.md, LICENSE (CC BY 4.0). README Workplan row now links the rendered board. Whether the root becomes the dth-hrh-style just-the-docs Documents landing is the open owner decision on #9383 (see qou-w5av).


## 2026-11-27 — site state re-measured (thread "Get QOU site running on harness", PR #9440)
The gh-pages site is NOT deprecated any more: since #9396 (owner ruling 2026-11-24, "1 qou is platform later") the root is the platform Documents landing built by cat-harness-tools build-instance-site.ts. Live on 2026-11-27: landing, 5 papers under en/, /accuracy/, /lean/ load; /qa/ and /beans/ absent (cat-harness-tools #2511/#2512 still draft; site-step.sh skips them). Last publish 2026-11-25 17:18Z by publish-main-local.sh from 9686001, 3 commits behind main. PR #9440 makes site-publish.yml the canonical caller (publish on push to main, owner decision pending) and fixes Paper PDF (0/100 green: latexpand missing, exit 127 after a clean 1064-page build).
