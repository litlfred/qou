---
# qou-xip2
title: 'EPIC: Continuous Repo Backlog Drain (Beans, Legacy PRs #5402..#9159, & Open Issues #2472..#9158)'
status: in-progress
type: epic
priority: high
created_at: 2026-11-23T20:54:33Z
updated_at: 2026-11-24T00:50:04Z
parent: qou-hksc
---

Umbrella epic exposing the complete 2026-11-23 evidence-backed repository backlog triage in `beans` CLI so any internal or external agent can claim and drain batches without collisions.

### Structure
1. **Bean Drain Epics (`Q-Drain-1` .. `Q-Drain-10`):** 10 themed child epics covering `126` prioritized critical/high/normal beans (strictly respecting Rule 13a on `815` zero-instance Lean classes).
2. **Legacy PR Salvage/Close Tasks (`PR-Drain-1` .. `PR-Drain-5` + `A2` Gated PRs):** Exact PR numbers, branch names, file counts, queue overlaps, and rebase/salvage/close workflows for all `170` `HAS_UNMERGED_POTENTIAL_DELTA` PRs (`#5402..#9159`) plus the `12` `(A2)` PRs gated on `#9189/#9191/#9200`. **NEVER pass `--delete-branch` or `-d` when closing any PR!**
3. **GitHub Issue Resolution Tasks (`Issues-Cluster-1` .. `Issues-Cluster-8`):** All `90` `STILL_OPEN_ACTIONABLE` GitHub issues grouped into 8 domain clusters (`#9154` guarded until both BHK `references.ts` and Chester–Arsiwalla–Kauffman 2025 library sections land).


## 2026-11-23 — Batch 1 (`qou-1scg`, `qou-l7cy`, `qou-9f1c`) Progress (Worker 31)
- **`qou-1scg` (`Q-Drain-1`):** Audited all 13 child beans against `origin/main` (`e330ab6aa04`); completed **1** (`qou-j540`, PR `#8048` `47627a8a27b`) and narrowed **12** with exact `origin/main` measurements & `owner-rulings.md` rescopes (Rule 13a preserved).
- **`qou-l7cy` (`PR-Drain-1`):** Opened consolidated salvage PR **#9237** (`claude/backlog-drain-batch1-20261123`, `3328685b1ae`) porting clean deliverables from **7 of 9** PRs (`#9159, #9157, #9045, #8741, #8896, #9105, #8751` + `#8560` Parts B & D), turning **5 of 6** blocking precision-gate reds **GREEN** and draining `q0-anchor refill` `NEW: 63 -> 21`; documented blockers on `#9095` (owner-approval hold) and `#8560` Part C (47 unfinished witness re-runs + 14 conflicts). Zero legacy PRs prematurely closed; zero branches deleted.
- **`qou-9f1c` (`Issues-Cluster-1`):** Audited `#9104, #8895, #8010, #7589` (+ guarded `#9154`) against `origin/main`; posted tracking-bean & PR #9237 linkage comments on all 4 issues (`#8895` and `#9158` set to auto-close when PR #9237 merges).
