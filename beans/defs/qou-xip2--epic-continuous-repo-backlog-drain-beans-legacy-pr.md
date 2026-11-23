---
# qou-xip2
title: 'EPIC: Continuous Repo Backlog Drain (Beans, Legacy PRs #5402..#9159, & Open Issues #2472..#9158)'
status: in-progress
type: epic
priority: high
created_at: 2026-11-23T20:54:33Z
updated_at: 2026-11-23T20:55:44Z
parent: qou-hksc
---

Umbrella epic exposing the complete 2026-11-23 evidence-backed repository backlog triage in `beans` CLI so any internal or external agent can claim and drain batches without collisions.

### Structure
1. **Bean Drain Epics (`Q-Drain-1` .. `Q-Drain-10`):** 10 themed child epics covering `126` prioritized critical/high/normal beans (strictly respecting Rule 13a on `815` zero-instance Lean classes).
2. **Legacy PR Salvage/Close Tasks (`PR-Drain-1` .. `PR-Drain-5` + `A2` Gated PRs):** Exact PR numbers, branch names, file counts, queue overlaps, and rebase/salvage/close workflows for all `170` `HAS_UNMERGED_POTENTIAL_DELTA` PRs (`#5402..#9159`) plus the `12` `(A2)` PRs gated on `#9189/#9191/#9200`. **NEVER pass `--delete-branch` or `-d` when closing any PR!**
3. **GitHub Issue Resolution Tasks (`Issues-Cluster-1` .. `Issues-Cluster-8`):** All `90` `STILL_OPEN_ACTIONABLE` GitHub issues grouped into 8 domain clusters (`#9154` guarded until both BHK `references.ts` and Chester–Arsiwalla–Kauffman 2025 library sections land).
