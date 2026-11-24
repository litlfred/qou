---
# qou-gen3
title: 'SM/Eightfold Worker Pkg 1 (Q-Gap-7): N_gen=3 Bring Zero-Mode Count, S_3⊂S_5 CKM/PMNS Overlap Textures, & Satellite Tau Carrier'
status: in-progress
type: feature
priority: high
created_at: 2026-11-23T20:06:00Z
updated_at: 2026-11-24T02:18:47Z
parent: qou-sm8w
---

## Scope & Linked Legacy Beans (`qou-x4qm`, `qou-xtcl`, `qou-htk4`, `qou-y0mq`)

1. **Derive `N_gen = 3` Structurally:** Test and formalize in Lean (`QOU/StandardModel/BringThreeGenerations.lean`) the Riemann-Roch / Hodge `h^0` (`g - 1 = 3` on `g = 4` Bring curve mod harmonic `b_9` composite quotient) zero-mode multiplicity of the chiral generation `Lambda^1 F oplus Lambda^2(F^*)`, resolving `qou-xtcl` (`T(2,9)` exclusion) and `qou-x4qm`.
2. **Construct Categorical Flavour Basis & CKM/PMNS Mixing Operator:** Build the overlap Gram matrix between the three conjugate `S_3 subset S_5` chiral fibre subgroups on Bring's surface (`color-confinement-observation.md:9`) vs. weak `T(3,5)` eigenmodes, testing parameter-free Cabibbo `theta_12` and PMNS tribimaximal-deformed mixing angles at 80 dps (`PREREGISTRATION.md` first, zero fitting!).
3. **Satellite / Inhomogeneous Loop Carrier for `m_tau` (`qou-htk4`):** Test Whitehead/cable satellite linking of `T(2,7)` with `4_1` (bypassing the 25-prime-knot direct-volume exclusion of `sm-params-lepton-masses.md:9`).

### Worker 22 Delivery (2026-11-23, branch `claude/sm8w-bring-ngen3-ckm-tau-20261123`)
- **GitHub Issue:** https://github.com/litlfred/qou/issues/9224
- **Ready PR (held for owner OK):** https://github.com/litlfred/qou/pull/9225 (head `54d4410bee4`)
- **Lean 4 Module (`0 sorry`, standard axioms only):** `folio/quantum-observable-universe/lean/QOU/StandardModel/BringGenerationSplitAndCKMTexture.lean` (wired into `QOU.lean`):
  - Honest `S_5 ⊃ S_4 ⊃ S_3` and `S_5 ⊃ S_3 × S_2` branching of 4D canonical differential space `V_std ≅ V_{(4,1)}` (`4 -> 3 + 1 -> 2 + 1 + 1` and `4 -> (2 ⊠ 1) + (1 ⊠ 1) + (1 ⊠ sgn)`), explicit idempotent projectors + 3-element root basis independence/span, Morgan-Voyce `b_9(h) = b_3(h)(h^6 + 6h^4 + 9h^2 + 1)` & Bezout coprimality of `(b_3, b_5)` and `(b_3, b_7)`, `bring_generation_filters_disagree` (`4 != 3 != 2`), and zero-instance Rule-13a `BringChiralGenerationSelectionHypothesis`.
  - Generic `[CommRing R]` (`QuadI R`) `3 x 3` Chau-Keung unitarity, Jarlskog plaquette closed form & domain vanishing iff, rational pentagon non-zero CP witness, and Cabibbo Hecke relation `([3]_q^2 + 4h^2) sin^2(2 theta_12) = 4h^2`.
  - Seifert-Torres / reduced-Burau factorisation for `(2, 2n+1)`-cabled figure-eight satellites, degree-10 palindromicity & `Delta_{C_{2,7}(4_1)}(-1) = 7`, and golden-ratio sign node across `phi^2`.
- **Pre-registered 80-dps Probe & Stamped Witness (`q0Anchor = "proton"`, `stale: False`, `14/14` assertions):** `computations/probes/sm8w_bring_ngen3_ckm_tau/` (`PREREGISTRATION.md` committed first in `b79c58b664d`).
  - Honest hits & misses: `PMNS-P1b` gives `sin^2(theta_13) = h^2/2 = 0.021853` (`-0.67%`), `sin^2(theta_12) = 0.297722` (`-3.02%`), `sin^2(theta_23) = 0.488829` (`-10.47%`); `CKM-C1a` gives `|V_us|` `-6.79%`, `|V_cb|` `+3.57%`, `|V_ub|` `-23.81%`, `J_CP` `-17.25%`; all parameter-free satellite `T(2,7)--4_1` and bare `5_2` / `T(2,7)` `tau/e` candidates miss CODATA `3477.23` (closest bare `Vol(5_2)/hbar_{q_0}^3 = 2907.49` at `-16.39%`, cabled Alexander ratio `2390.74` at `-31.25%`, `H_6(q_0)` cabled Markov bend `1.01703` vs observed `12.2952`), leaving `m_tau` and unconditional chiral selection open.

Follow-up Gap 3 primary derivation (qou-hlea) staged at ff3ae6c8158 on origin/claude/gap3-ngen3-bring-prym-riemann-roch-20261123.
