---
# qou-wv8g
title: 'Salvage review: 12 Lean modules exist only on 7 unlanded branches'
status: todo
type: task
tags:
    - reorg-2026-10-04
    - orphan-census
    - needs-owner
created_at: 2026-10-04T15:31:24Z
updated_at: 2026-10-12T19:36:53Z
parent: qou-trd0
---

Sample of the 60 newest unlanded branches: 27 carry content not on main. Branch-only modules include ModularDoubleLocusSeparation, TLCarrierBridge, BondCutSymmetryFibreTower(+Bound), CyclotomicEvaluationRingHom, SingleCrossingChainFactorizes and six Casimir/Wenzl files on p-neq-np-gaps-n8dxxl. All use pre-move content/ paths. Full census: 461 branches marked salvage-review; none may be deleted.

Found by the orphaned-content census 2026-10-04 (inventory: 3,383 rows). Report only: no math or physics content is to be changed; this item links, builds or places existing content.

## 2026-10-12 — one of the twelve landed: CyclotomicEvaluationRingHom

Salvaged from `claude/habiro-cyclotomic-binding-2026-09-12` (PR #7225, never
merged) onto `folio/quantum-observable-universe/lean/QOU/Habiro/`, within this
bean's own scope — *"this item links, builds or places existing content"*. No
mathematics was changed.

**Verified rather than assumed**, because the olean cache is a month-old
snapshot and both of this file's QOU dependencies were stale against it
(`QOU.Common.CyclotomicValueTruncates` and `QOU.Habiro.CyclotomicEvaluation`:
oleans 2026-08-30, sources 2026-09-27). The whole three-module cone was rebuilt
**from today's source** with `lean -DautoImplicit=false -s 65536`, exit 0; all
**21** declarations print `[propext, Classical.choice, Quot.sound]`, no
`sorryAx`; `check-sidecars.sh` reports the file §7c-clean ("no ℝ, generic OK").

Two salvage notes for whoever takes the other eleven:

1. **Repathing the file is not the whole job.** This one's docstring cited
   `QOU.Habiro.CyclotomicEvaluationAtSubstrate`, which has never existed — and
   could not, since §4 of the same file proves there is nothing at the substrate
   pin to instantiate. Check a branch-only module's *internal* references, not
   just its path.
2. **`lean`-direct against the restored cache would have been a false green
   here.** The deps were stale by a month; only the from-source rebuild of the
   cone is evidence about `main`.

Bean stays `todo`: eleven modules remain, and the census decision is tagged
`needs-owner`.
