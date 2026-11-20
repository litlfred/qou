---
# qou-ozdk
title: 'N5 [Higher-Order GPMT Ideal & H_12(q) Cabled (3^4) Singlet Bridge]: Formalize (z - z_D)^m Filtration & Bridge H_12(q) supset H_3(q)^4 to H_4(q) Alpha Cell'
status: todo
type: task
priority: high
created_at: 2026-11-19T11:13:48Z
updated_at: 2026-11-20T16:40:00Z
parent: qou-8ffl
---

Parent Epic: `qou-8ffl`. Deduplicates and extends `qou-xsmr` (*General-K 1st-order GPMT*) and `qou-br4t` (*4x4 Hankel/Cauchy SU(4) q-Plancherel*), building directly on `N1` (`qou-ki22`).

## Scope (Lane N5 — Higher-Order GPMT Ideal Filtration on `H_12(q)` / `H_{3A}(q)` & Cabled `(3^4)` Singlet Bridge)

1. **80-dps Diagnostic Finding from `N1` (`h4-fulltwist-alpha-and-carbon12-groebner.witness.json`):**
   - Among the `77` partitions of `12` in `H_12(q)` (`3A = 12` color strands for `^4He`), `7` have `ell(lambda) <= 2` (`z - z_D` multiplicity `m = 0`), `53` have a simple zero (`m = 1`), `16` have a double zero (`m = 2`), and `1` has a triple zero (`m = 3`).
   - Crucially, the rectangular 4-row cabled singlet `(3,3,3,3)` (`d = 462`, `kappa = -6`) contains TWO cells of content `-2` (`(2,0)` and `(3,1)`), so `w_(3,3,3,3)(q, z)` vanishes to **second order** `(z - z_D)^2` at Convention D (`w / (z - z_D)^2 |_{z_D} > 0`) and is invisible to first-order GPMT `d/dz |_{z_D}`.
2. **Deliverables (Lean 4 + 80-dps Compute):**
   - Formalize the `m`-th order GPMT tensor-ideal filtration `I_{>=3}^{(m)}` (`m = |{(r,c) in lambda : r - c = 2}|`) and the second-order modified quantum dimension `d_mod^{(2)}((3,3,3,3))` in Lean 4 (`0 sorry`, `0 axiom`).
   - Bridge the cabled `H_12(q) supset H_3(q)^{otimes 4}` Littlewood-Richardson / Schur-Weyl embedding to the nucleon-strand `H_4(q)` GPMT cumulants `dMod211`, `dMod1111` at 80 dps (`0` float64, zero fitting).



## Completed (2026-11-19)
Completed & Red-Team PASSED (`0` blockers): `folio/quantum-observable-universe/lean/QOU/Nuclear/SecondOrderGPMTCabledAlphaAndCarbon12.lean` (`1,015` lines, wired in `QOU.lean`) + 80-dps zero-float64 probe `computations/probes/second_order_gpmt_h12_carbon12_and_o16_probe.py` (`scriptHash = 1ef65a65eeca`).

## Reopened (owner instruction 2026-11-20, via W12)
This bean was set to completed by local commits on `cat/cat-harness/beans` (e223ed1 / 4fcd2cb / 89bb5e0, 2026-11-19, `litlfred@fenugreek.home`, no session trailer). The Lean / probe / witness files its resolution names are not on main, on any branch, or in any PR found by the bean id (measured 2026-11-20). See GAP bean qou-w12g.
