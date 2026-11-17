---
# qou-p443
title: 'Borel singularity vs Bring saddle: close the identification or refute it with the thimble action'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T09:30:03Z
updated_at: 2026-10-04T15:16:44Z
parent: qou-frzo
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

## Round 71 Progress (`litlfred/qou#8246`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/StrandNormalizationChiralityAndMagnusBridgeBrick.lean` (`ramified_puiseux_classical_jet_residue_parity_vanishing`)
- **Summary**: Proved ramified Puiseux quadratic coordinate `z = z_c + t^2` odd-parity pullback cancellation `(2 * c1 * t) + (2 * c1 * (-t)) = 0` vs non-vanishing `q`-difference shift `c1 * (p * t)^2 - c1 * t^2 = (p^2 - 1) * c1 * t^2 != 0`.
- **80-dps Probe & Witness**: `computations/probes/strand_normalization_chirality_and_magnus_bridge_brick_probe.py` -> `computations/probes/strand-normalization-chirality-and-magnus-bridge-brick.witness.json` (`scriptCommitSha: bf27f37259a48fea2b98340ccf2912cea35c83cc`, PR head `641d009e3ad3b5a36bfab308cf07ceb158eb2c62`)
- **PR**: https://github.com/litlfred/qou/pull/8246 (`status: in-progress` pending merge)
