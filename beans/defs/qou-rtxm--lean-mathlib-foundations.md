---
# qou-rtxm
title: Lean / Mathlib foundations
status: in-progress
type: milestone
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:09:55Z
updated_at: 2026-11-17T06:35:30Z
---

Foundational Lean infrastructure. Measured 2026-10-04: 9-15 real `sorry` on main; open gaps now sit in axioms and instance-less classes. The only item on the L2 critical path is SW-WIRE (WedderburnDecomp instance, markov_trace_unique_axiom), gated by owner decision qou-ar7f.

## 2026-11-16 — General-`n` Markov Trace Tower Stabilization (`qou-ep0a`, PR #8148)
- Formalized `folio/quantum-observable-universe/lean/QOU/Torsion/MarkovTraceTowerStabilization.lean` (`0` `sorry`, generic `R` per §7c, wired into `QOU.lean`, commit `b1cda0ed48b69b13bf48c75340c8f842a671b780`, PR `https://github.com/litlfred/qou/pull/8148`). Kept `status: in-progress`.

## 2026-11-16 — Foundations Bridge (`qou-aj49`, `qou-wapd`, `qou-k5jt`, `qou-bmyx`, `qou-kfcl`, PR #8157)
- Formalized `folio/quantum-observable-universe/lean/QOU/Foundations/FrobeniusHopfMarkovBridge.lean` (`0` `sorry`, generic `CommRingOps R` per §7c, wired into `QOU.lean`, commit `16f8c01498462170d1ad98f5b5426233d3feea7d`, PR `https://github.com/litlfred/qou/pull/8157`). Kept `status: in-progress`.

## Progress Update (2026-11-16 — Round 48: PR #8160)
- **PR:** [`litlfred/qou#8160`](https://github.com/litlfred/qou/pull/8160) (`c0fb591249c67f13f6a77b40075589852babb011`)
- Completed `qou-bhrx` (`cyclic_of_rep_decomp_of_basis` and `ocneanu_stabilization_cyclic` in `QOU/Machinery/BilinearTraceRepBasis.lean`, `0` `sorry`).

## 2026-11-16 — Wenzl Level Family, TL Catalan Quotient, Signed vs Modulus Trace, All-`n` Gram Cyclicity & `H₄` Wedderburn Keystone (`qou-7d08`, `qou-8iru`, `qou-8jq2`, `qou-bhrx`, `qou-btk8`, PR #8162)
- Formalized `folio/quantum-observable-universe/lean/QOU/Foundations/WenzlTemperleyLiebH4Keystone.lean` (`0` `sorry`, generic `CommRingOps R` per §7c, wired into `QOU.lean`, commit `f3dcbfe5fb51a67f3233319674c13a3791ba91d2`, PR `https://github.com/litlfred/qou/pull/8162`). Kept `status: in-progress`.

## 2026-11-16 — Convention D r=2 Identity, Frobenius Descent, Markov Uniqueness, Elliptic Boundary & Hecke Inverse (`qou-fq0f`, `qou-e524`, `qou-juz3`, `qou-dgtf`, `qou-cins`, PR #8166)
- Formalized `folio/quantum-observable-universe/lean/QOU/Foundations/ConventionDFrobeniusMarkovTower.lean` (`0` `sorry`, generic `CommRingOps R` per §7c, wired into `QOU.lean`, commit `246ab0f17af473b433e680ddc0223712e5c0d13c`, PR `https://github.com/litlfred/qou/pull/8166`). Kept `status: in-progress`.

## 2026-11-16 — Convention D H_3 Keystone Uniqueness, N=3 Second Trace Det, E_{(3,2)} Branching, W3 Iterated Trace & B2d Form (`qou-u2jg`, `qou-yk03`, `qou-nzi9`, `qou-r765`, `qou-t2ot`, PR #8214)
- Formalized `folio/quantum-observable-universe/lean/QOU/Foundations/ConventionDKeystoneTraceTower.lean` (`0` `sorry`, generic `CommRingOps R` per §7c, wired into `QOU.lean`, commit `7cc3c04b0719e92286ff6279855cbf3f0b9a7826`, PR `https://github.com/litlfred/qou/pull/8214`). Kept `status: in-progress`.

## 2026-11-17 — Pinned Beta Calibration, JM Twist Scaling, Central Gibbs Markov State, kappa-Bar Commutation & H_4 Poincaré Projectors (`qou-4zu7`, `qou-u9o1`, `qou-unqc`, `qou-xgt8`, `qou-yax5`, PR #8223)
- Formalized `folio/quantum-observable-universe/lean/QOU/Foundations/CalibrationJMGibbsBarPoincare.lean` (`0` `sorry`, generic `CommRingOps R` per §7c, wired into `QOU.lean`, commit `71263060fde5e0d5c09fecd66cf05ada5b6cd208`, PR `https://github.com/litlfred/qou/pull/8223`). Kept `status: in-progress`.

## 2026-11-17 — ζ₄ Exclusion, §7c Generic-Ring Clusters & QPlancherel (`5lcg`, `qou-oc4v`, `qou-r7qm`, `qou-xbyp`, `qou-sf1t`, PR #8227)
- Formalized `folio/quantum-observable-universe/lean/QOU/Foundations/Zeta4GenericRingPlancherel.lean` (`0` `sorry`, generic `CommRingOps R` / `InvolutionRingOps R` per §7c, wired into `QOU.lean`, commit `6ea0f626b6fd6e4a73ad6fb742931324e3efe377`, PR `https://github.com/litlfred/qou/pull/8227`). Kept `status: in-progress`.
