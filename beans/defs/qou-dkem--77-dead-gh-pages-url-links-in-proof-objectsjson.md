---
# qou-dkem
title: 77 dead gh_pages_url links in proof-objects.json
status: todo
type: task
created_at: 2026-11-17T23:08:25Z
updated_at: 2026-11-27T14:30:00Z
parent: qou-trd0
---

The gh-pages site is deprecated (owner 2026-09-27); 77 gh_pages_url fields point to pages that do not exist. Left: owner decides drop vs repoint.

Recorded 2026-11-17 from the stale-sibling-session sweep (table: /mnt/project-files/qou-sibling-consolidation/table.md). Source session archived; work not lost.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8411, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.


## 2026-11-27 — site state re-measured (thread "Get QOU site running on harness", PR #9440)
The gh-pages site is NOT deprecated any more: since #9396 (owner ruling 2026-11-24, "1 qou is platform later") the root is the platform Documents landing built by cat-harness-tools build-instance-site.ts. Live on 2026-11-27: landing, 5 papers under en/, /accuracy/, /lean/ load; /qa/ and /beans/ absent (cat-harness-tools #2511/#2512 still draft; site-step.sh skips them). Last publish 2026-11-25 17:18Z by publish-main-local.sh from 9686001, 3 commits behind main. PR #9440 makes site-publish.yml the canonical caller (publish on push to main, owner decision pending) and fixes Paper PDF (0/100 green: latexpand missing, exit 127 after a clean 1064-page build).
