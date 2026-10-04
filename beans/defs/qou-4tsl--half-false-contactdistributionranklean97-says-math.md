---
# qou-4tsl
title: 'HALF-FALSE: ContactDistributionRank.lean:97 says Mathlib has no exterior-power-of-an-object API — it has ⋀[R]^n M and ModuleCat; the abstract-monoidal case is the real gap'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:08:25Z
updated_at: 2026-10-04T15:20:42Z
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
