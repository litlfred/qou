---
# qou-l155
title: Pin lambda_SW so the Picard-Lefschetz thimble action is computable
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T09:30:03Z
updated_at: 2026-10-04T15:22:05Z
parent: qou-wp3h
---


## ANSWERED / RE-SCOPED (2026-09-06) — by an existing result, not by me

`2026-09-03-enclosed-pole-set-E-is-not-identifiable.md` (bean `qou-qx7j`) proves,
Lean, sorry-free, `[propext]` only: **every residue of `λ_SW^(n)` vanishes at
every branch point for every `n ≥ 1`, independently of the Puiseux data**
(`ddz_residue_slot_eq_zero`). Parity, not cancellation — the `t^{−2}` slot of a
`z`-derivative can only be fed by a constant term, which differentiation kills.
Non-vacuity established there.

**Consequence for this bean.** On the classical-jet prolongation there is no
nonzero thimble action, so `ξ = 1/√2` cannot be a `z_c` saddle's action there —
and pinning `λ_SW` yields zero however it is pinned. **Both beans are the wrong
question as posed.** The live question is *which prolongation*; the q-difference
one is untouched, and `RamificationParityMonodromy` locates the gap as
q-jet-bundle / q-D-module symbol calculus, **absent from Mathlib and the
corpus**.

Judgement, not finding: the Borel side independently says the plane is q-Borel
(Gevrey-1/2, q-Gevrey at `q₀`). Two negatives agreeing that the classical object
is wrong and the q-deformed one carries the content is the strongest signal in
the arc — but the machinery it points at has to be built.

**Do not spend on these two as written.** Re-scope to the q-difference
prolongation or close them.



## 🛑 Correction (2026-09-06, bean `qou-p6m1`)

The wall quoted above — "q-jet-bundle / q-D-module symbol calculus, **absent from
Mathlib and the corpus**" — bundles two objects, and I repeated it without
measuring it.

- **q-D-module symbol calculus: PRESENT.** `QOU.Machinery.QuantumTorusSymbol`
  (QDM-1/2, 19 decls, sorry-free, on `main` by 2026-07-24) and
  `QOU.Mathlib.RamifiedShiftCalculus` (the same calculus at the ramified pole
  `z = z_c + t²`, sorry-free, 2026-09-03). The latter **imports**
  `RamificationParityMonodromy`, the file carrying the denial.
- **q-jet bundle over `Σ`: ABSENT**, and **W1 stands.**

Nothing in this correction changes this bean's own verdict — the classical-jet
period is still Lean-proved zero. Only the description of what infrastructure
is missing was wrong.

## Progress Update (PR litlfred/qou#8244)
- **Status**: `in-progress` (awaiting PR merge)
- **PR**: https://github.com/litlfred/qou/pull/8244 (`457d28e500f11a4249f57fd33fcd18112faef23b`, scriptCommitSha `1086b0ae6f630df61ca513a195514ef5d6137b5c`)
- **Summary**: Added `disc_at_pm_one_and_wCubic_vals` and `ddz_linear_comb_residue_slot_eq_zero` in `QOU/Brings/ColourCubicBranchLocus.lean`, verified by 80-dps mpmath probe `frust_cubic_tower_jhopf_whitehead_probe.py`.
