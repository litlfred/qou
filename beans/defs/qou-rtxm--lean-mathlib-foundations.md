---
# qou-rtxm
title: Lean / Mathlib foundations
status: in-progress
type: milestone
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:09:55Z
updated_at: 2026-11-16T19:27:00Z
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
