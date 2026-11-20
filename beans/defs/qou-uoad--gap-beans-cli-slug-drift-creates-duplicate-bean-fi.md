---
# qou-uoad
title: 'GAP: beans CLI slug drift creates duplicate bean files on --body-append'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T13:22:41Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-5vkl
---


## Measured, 2026-08-23 (found while unstalling PR #5531)

PR #5531 was a one-file bean change whose diff was **11 files**. The ten
extras were duplicates of beans that already exist on `main` under
near-identical filenames. Mechanism:

| this container's CLI | the CLI that wrote main's files |
|---|---|
| `placeholders-todos` | `placeholderstodos` |
| `s5-so3`             | `s5so3` |
| `n-2`                | `n2` |
| `qou-mass`           | `qoumass` |

The newer CLI maps separators (`/`, `=`, `-`) to `-`; the older dropped
them. `beans update <id> --body-append` therefore resolves to a filename
that does not exist and **writes a new file** instead of updating the
existing bean. The id is then claimed by two files.

**This is not branch-specific.** A fresh `scripts/install-beans.sh` in
this container produces the new-style slugs, so any agent doing a
`--body-append` against a bean created before the CLI change hits it.

**Blast radius is already visible on main.** Bean `qou-xqno` ("2 duplicate
bean ids") is a *symptom* of this, not an unrelated hygiene item; main's
`sp06` carries a 2026-08-23 recovery note about an empty-title duplicate,
and `qou-x4qm` had to be re-issued as `qou-5isd` to break a collision.
Those were fixed one at a time, by hand, without the cause being named.

**Not fixed here** — this is a bean-only finding from a PR-unstalling
pass. The honest next step is a `beans doctor`-style guard that resolves
by **id** rather than by filename, or a one-off pass that reconciles
old-slug and new-slug filenames. Neither is in scope for #5531 or #5494.

Risk if left: every duplicate silently starves the §4 idle-backlog policy
of signal (the 14,688-duplicate incident of 2026-08-04 is the precedent),
and re-landing a duplicate can *undo* a hand fix, as it nearly did here.

- **Round 95 PR (`litlfred/qou#8505`)**: Formalized `SlugDriftDuplicateReconciliationLedger`, `canonicalSlugDriftDuplicateReconciliationLedger`, `slug_drift_duplicate_excess_and_recovery`, and `slug_drift_cubic_factorization` in `QOU.Foundations.CyclicShiftExploratoryWitnessAuditInteriorMaximumConeObstructionAnchorScriptlessWitnessPartitionSlugDriftDuplicateReconciliationDualCrystalProgressLogging` with 80-dps witness (`HEAD = 420a7c37f74e9880c86f0d911e737f7383abb435`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8505, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
