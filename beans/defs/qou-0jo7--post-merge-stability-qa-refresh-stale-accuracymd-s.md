---
# qou-0jo7
title: 'Post-merge stability QA: refresh stale ACCURACY.md scorecard + witnesses, fix JonesTractableOrders transcendental boundary, and shrink base-ring-audit'
status: in-progress
type: task
priority: high
tags:
    - stability
    - compute-accuracy
created_at: 2026-11-28T10:15:32Z
updated_at: 2026-11-28T10:15:32Z
parent: qou-s028
---

2026-11-28 (Antigravity coordinator 92bff8c9-777d-458a-a380-8dd5bf5cc0f3, sibling ws5-nov19-rebase -> branch claude/postmerge-qa-scorecard-boundary-20261128): Clear live post-merge QA reds on `origin/main` (2cc11f7f1c6): (1) fix `NEW QOU/InformationTheory/JonesTractableOrders.lean ['transcendental-function']` in `scripts/transcendental-boundary-audit.py --check` (and verify `qou-68a4` status) + `scripts/base-ring-audit.py --shrink`; (2) refresh import-cone-stale accuracy-scorecard witnesses at proton pin (two-step SHA stamp) and regenerate `ACCURACY.md` (`generate-accuracy-scorecard.py --write && --check` exit 0).
