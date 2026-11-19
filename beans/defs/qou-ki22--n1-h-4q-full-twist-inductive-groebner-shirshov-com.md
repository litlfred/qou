---
# qou-ki22
title: 'N1 [H_4(q) Full-Twist & Inductive Groebner-Shirshov Compute + Lean]: H_4(q) Delta_4^2 Singlet Cell, Transfer-Matrix Reduction & Light/Medium Nuclear Compute (^2H..^40Ca)'
status: completed
type: task
priority: high
created_at: 2026-11-19T09:36:33Z
updated_at: 2026-11-19T12:46:10Z
parent: qou-8ffl
---

Parent Epic: `qou-8ffl`. Cross-links: `qou-v2om`, `qou-n0so`, `qou-xsmr`.

## Scope (Lane N1 — Active)

1. **Lean 4 Formalization (`folio/quantum-observable-universe/lean/QOU/Nuclear/H4FullTwistAlphaCellAndGroebnerBridge.lean`):**
   - Formalize the 5 partitions of `4` (`(4)`, `(3,1)`, `(2,2)`, `(2,1^2)`, `(1^4)`), their SYT dimensions `(1, 3, 2, 3, 1)` (`sum d_lambda^2 = 24 = 4!`), Young-diagram content sums `(+6, +2, 0, -2, -6)`, transpose conjugation duality, and Wigner-`SU(4)` `(4) <-> (1^4)` antisymmetrization pairing.
   - Construct explicit Laurent-polynomial Specht matrix representations for all 5 blocks of `H_4(q)`, prove all Hecke quadratic and braid relations and all 25 Markov conjugacy-class characters, and prove by matrix multiplication that the 4-strand full twist `Delta_4^2 = (T_1 T_2 T_3)^4` acts centrally on each block by scalar `q^(2 * kappa_lambda)` = `(q^12, q^4, 1, q^-4, q^-12)` (and `Delta_4^-2` by `(q^-12, q^-4, 1, q^4, q^12)`).
   - Prove exact closed-form rational expressions in `Q(q)` for the Convention-D 2-row full-twist traces `tr_D(Delta_4^+-2)` and Casimir `<2 kappa>_D = 12(q^4 + 1)/(q^2 + 1)^2`, and for the GPMT-completed `>= 3`-row full-twist traces and Casimir `<-2 kappa>_{GPMT,>=3}` combining `dMod211(q) < 0` and `dMod1111(q) > 0`.
   - Prove the inductive transfer-matrix Hecke reduction `C^2 = h C + 1 => C^k = a_k(h) C + b_k(h)` (`tm-general-form`, `periodic-table-demand-conjecture.md:51`), general `(c,d)` crossing transfer-matrix product compression, `X_nn = C - h` inverse quadratic, achiral `X_gg^2 = ((q^2+1)^2 / (4 q^2)) * 1` collapse, and `O(A^2)` block-ordered `markov_peel` factorization.
2. **80-dps Compute Probe (`computations/probes/h4_fulltwist_alpha_and_carbon12_groebner_probe.py` + `.witness.json`):**
   - Evaluate at 80 dps at both `q_0` and `q_2t` (with `q0Anchor: "comparison"`) across `^2H, ^3H, ^3He, ^4He, ^6Li, ^8Be, ^12C, ^16O, ^24Mg, ^40Ca`:
     * (a) 1-crossing pair trace (`alpha_simplex` baseline),
     * (b) Multi-crossing `H_4(Delta_4^+-2)` full-twist + GPMT `alpha`-cell energy + inter-cell transfer-matrix couplings (testing `^8Be` vs `2 * ^4He` threshold stability with Coulomb, and reporting `B(^12C)` & `M(^12C)`),
     * (c) Exact 80-dps `H_12(q)` 2-row Ocneanu + GPMT derivative comparison (`alpha_k_jones_markov_h12` upgrade without float64) and why `L1` stopped at `A <= 6`.



## Completed (Checkpoint 4 — 2026-11-19)
- Formalized `folio/quantum-observable-universe/lean/QOU/Nuclear/H4FullTwistAlphaCellAndGroebnerBridge.lean` (`0 sorry`, `0 axiom`, wired into `QOU.lean`) and `QOU/Nuclear/BallManifoldTriangulationAndSurfaceScaling.lean`.
- Generated 80-dps zero-float64 probes and witnesses: `computations/probes/h4_fulltwist_alpha_and_carbon12_groebner_probe.py` (`h4-fulltwist-alpha-and-carbon12-groebner.witness.json`, `scriptHash: 7daa156ec83a`) and `computations/probes/nuclear_3d_ball_manifold_triangulation_probe.py` (`nuclear-3d-ball-manifold-triangulation.witness.json`, `scriptHash: 835eb55fb324`).
