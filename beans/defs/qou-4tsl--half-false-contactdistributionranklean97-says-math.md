---
# qou-4tsl
title: 'HALF-FALSE: ContactDistributionRank.lean:97 says Mathlib has no exterior-power-of-an-object API — it has ⋀[R]^n M and ModuleCat; the abstract-monoidal case is the real gap'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:08:25Z
updated_at: 2026-11-17T10:08:09Z
parent: qou-c8p8
---

**HALF-FALSE CLAIM — and the wrong half is the one that matters for the file's route.**

`QOU/Eightfold/ContactDistributionRank.lean:97-98`:

> "Mathlib has **no exterior-power-of-an-object API** and **no differential forms on
> manifolds at all**, so every declaration below is about `ℕ`."

Measured 2026-09-04 against pinned mathlib `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`:

**(a) "No exterior-power-of-an-object API" — FALSE as stated.** Mathlib has

    LinearAlgebra/ExteriorPower/Basic.lean     -- ⋀[R]^n M, ιMulti, map,
                                                  alternatingMapLinearEquiv, presentation
    LinearAlgebra/ExteriorPower/Pairing.lean
    LinearAlgebra/ExteriorAlgebra/{Basic,Grading,OfAlternating}.lean
    LinearAlgebra/Alternating/{Basic,Curry,DomCoprod}.lean
    Algebra/Category/ModuleCat/ExteriorPower.lean

What is genuinely absent is `Λ^k` of an **object of an abstract monoidal category** —
which is the file's actual subject and is what the sentence should say. Note also that
a wedge *product* `Λ^p × Λ^q → Λ^{p+q}` is not a named operation anywhere
(`grep -rn 'wedge' LinearAlgebra/Alternating/*.lean` → nothing), which is a separate
and real gap the sentence does not mention.

**(b) "No differential forms on manifolds at all" — TRUE as scoped, but incomplete.**
Mathlib has forms and the exterior derivative on a **normed space**
(`Analysis/Calculus/DifferentialForm/Basic.lean`: `extDeriv`, `extDerivWithin`,
linearity, and `extDeriv_extDeriv` = `d∘d=0`). Manifolds are explicitly future work in
Mathlib's own TODO. So the *manifold* claim holds; the omission matters because the
file's model case is `dim M = 3` and `M = ℝⁿ` is a normed space.

**Corrected form:**

> "Mathlib has exterior powers of **modules** (`⋀[R]^n M`) and of `ModuleCat`, but no
> `Λ^k` of an **object of an abstract monoidal category** and no wedge product as a
> named operation; and it has differential forms with `extDeriv` on a **normed space**
> (`Analysis/Calculus/DifferentialForm/Basic.lean`) but none on **manifolds** — so every
> declaration below is about `ℕ`."

**Nothing proved in the file changes.** `contactDim`, `distributionRealRank`,
`degree_three_but_rank_one` and `dim_seven_two_distributions` are `Nat.choose`
arithmetic, correct, and sorry-free. This is a provenance fix only. The same
"every declaration is about `ℕ`" framing appears in the sibling
`Eightfold/HyperbolicVolumeFormType.lean` and should be checked at the same time.

Source: `docs/audits/2026-09-04-mathlib-infrastructure-inventory.md` §F7, §H2, §H5.

### Progress Update (2026-11-17, Round 59 — lane-e667)
- **PR:** `litlfred/qou#8291` (`https://github.com/litlfred/qou/pull/8291`), head `97f9ffaed50b1b3971470d9bc651293cd4f935e3` (`COMMIT1 = 9f95671d31537da41246588ea9801b300607f995`), labeled `ready-to-merge` + `release`, `ready: 97f9ffaed50b1b3971470d9bc651293cd4f935e3` (`https://github.com/litlfred/qou/pull/8291#issuecomment-6944908884`).
- **Lean 4.24.0 Module:** `folio/quantum-observable-universe/lean/QOU/Foundations/HyperbolicScalingDescartesCubicFarkasDuality.lean` (wired into `QOU.lean`; `0` `sorry`, `0` `axiom`, `0` warnings, `0` CRITICAL/major/advisory across all 6 static vacuity & borrowed-name audits):
  - `qou-322e`: `chordal_step_symmetry_diagonal_and_concatenation` over `CommRingCarrier R`.
  - `qou-4tsl`: `alternating_two_wedge_antisym_and_three_wedge_vanishing` and `alternating_two_wedge_ring_antisym_and_diag` over `Int` and `CommRingCarrier R`.
  - `qou-5gai`: `dilation_cube_jacobian_density_cancellation` over `CommRingCarrier R`.
  - `qou-7y3g`: `classical_av4_cubic_factorization_and_complex_roots` over `Int`.
  - `qou-9h4t`: `primal_dual_slack_gap_and_complementary_slackness` over `Int`.
- **80-dps Probe & 2-Commit Witness:** `computations/probes/hyperbolic_scaling_descartes_cubic_farkas_duality_probe.py` + `computations/probes/hyperbolic-scaling-descartes-cubic-farkas-duality.witness.json` (`scriptHash = 9b07010b5e8c`, `scriptCommitSha = 9f95671d31537da41246588ea9801b300607f995`, `allPassed = True`).
- **Adversarial Cross-Review (Round 59):** Verified `litlfred/qou#8276` (`1909a7bd3bec6ebbdc594cc42f836c8a59fb6451`, `0` advisories) and remediated `3 major, 2 advisory` borrowed-name findings on sibling PR `litlfred/qou#8261`, pushing `77aeb5c622eb2876245d1628c2f107b5f85999f8` and posting `ready: 77aeb5c622eb2876245d1628c2f107b5f85999f8` (`https://github.com/litlfred/qou/pull/8261#issuecomment-6942739479`).
- **Status:** Kept at `in-progress` pending Merge Manager verification and merge.
