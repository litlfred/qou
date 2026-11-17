---
# qou-i2q5
title: 13 references to computations/_deprecated/hecke_core_legacy.py — a path that never existed, from a split blocked on owner OK since 2026-05-24
status: in-progress
pr: 8307
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T14:51:30Z
updated_at: 2026-11-17T10:37:00Z
parent: qou-5vkl
---

## The path 13 sites point at does not exist

`computations/_deprecated/hecke_core_legacy.py` is referenced in **13 places
across 8 files** and has never existed. The live file is
`computations/hecke_core_legacy.py`.

The cause is not rot — it is a **stalled plan documented as though it had
landed**. From
[`docs/coordination/2026-05-24-library-reuse-production-readiness.md:46`](docs/coordination/2026-05-24-library-reuse-production-readiness.md):

> **PR #1072 hecke_core split implementation** — the audit is done; the actual
> move-to-`_deprecated/hecke_core_legacy.py` for 29 EXPLORATORY + 12
> utility-of-exploratory functions is the next branch
> (`claude/hecke-core-split-2026-05-24` or similar). **Blocked on owner OK of
> the classification table.**

Dated 2026-05-24. Three months on, the move has not happened and the block has
not been lifted.

## The two halves need different treatment — do not sweep them together

| where | n | status |
|---|---|---|
| `docs/audits`, `docs/coordination`, `docs/workplans` | 5 | **historically accurate** — they describe a proposed destination. Leave them. |
| `tools/pyhecke/python/pyhecke/{partition,tower,trace,wedderburn}.py`, `computations/{hecke_core_legacy,phase5/phase3_triton_binding_convention_b}.py` | 8 | **wrong as of now** — shipped package docstrings and producer comments name a destination as if the move were done |

The `pyhecke` ones are the ones that matter: that is the **current Layer-2b
package**, and a reader following its docstring lands nowhere.

## Why this blocks nothing but misleads everything

`hecke_core_legacy` is **not legacy in practice**. Measured:

- **9 real importers** (`^\s*(from|import)\s+hecke_core_legacy`, excluding
  worktrees, `_deprecated`, and the file itself) — **three of them inside the
  shipped `pyhecke` package**: `partition.py:15`, `tower.py:19`, `trace.py:16`.
- `wedderburn.py` mentions it only in comments — I nearly counted that as a
  dependency, which is the prose-vs-code error this corpus keeps re-learning.

## What this settles for `qou-n7ue`

That bean floats *"the cheapest fix may be retargeting the consumer rather than
repairing the legacy path."* **That option does not exist.** `binding_energy`
(:2314) and `classify_nuclear_knot` (:165) are defined **only** in
`hecke_core_legacy`; neither `computations/substrate/hecke_core.py` nor the
generated `qou-mass/_internal/hecke_core.py` has them. There is nothing to
retarget to, and repairing the path — which is what landed — was the only
route.

## Do NOT just do the move

It is blocked on **owner OK of a classification table**, not on someone finding
the time. The tractable, unblocked piece is the 8 code-side references: correct
them to `computations/hecke_core_legacy.py` so the shipped package stops
pointing at a file that does not exist. That is a documentation fix and does not
touch the classification question.


## Round 55 Update (2026-11-17, PR #8307)

Updated the module docstrings and comments in `tools/pyhecke/python/pyhecke/{partition,tower,trace,wedderburn}.py` from the nonexistent `_deprecated/hecke_core_legacy.py` path to `computations/hecke_core_legacy.py` (PR #8307, commit `cf8ca11962518083f27bc0a2ce60447359b28381`).
