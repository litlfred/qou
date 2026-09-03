---
# qou-c8p8
title: 'Mathlib infra: close class field debt'
status: in-progress
type: milestone
priority: normal
created_at: 2026-08-24T06:35:32Z
updated_at: 2026-09-03T14:53:24Z
---

Epic to close conjectural class fields that are standard math (not manuscript claims). Three axes: LP/SDP duality, parallelogram contour, RSK combinatorics.

This is the same triage first filed as `qou-bi00`, which I created without running the exact-title existence check `AGENTS.md` requires. `qou-bi00` is scrapped in favour of this entry; the check would have found this bean, whose three named axes already include "parallelogram contour".

The `#6491` audit found 491 uninhabited classes, 38 of them in the Mathlib-shaped directories (`Mathlib`, `MathlibExt`, `Machinery`) — the subset where "build the Mathlib infra" is the right response rather than "do the physics". This triages that subset by the only question that decides it: **does the pinned Mathlib v4.24.0 actually carry the thing the carrier needs?**

## Measured, against `.lake/packages/mathlib/Mathlib`

| carrier | Mathlib support | verdict |
|---|---|---|
| `Mathlib/EllipticDivisorDegree.lean:212 HasArgumentPrinciple` | **nothing** (`argumentPrinciple`, `argument_principle` occur nowhere) | genuine gap |
| `MathlibExt/SphericalCategory.lean:79 SphericalCategory` | **nothing** — no `PivotalCategory` either | genuine gap |
| `MathlibExt/FrechetShohat.lean:210,235 CarlemanDeterminacyStieltjes / FrechetShohatStieltjes` | **nothing** (`Carleman`, `moment_problem` occur nowhere) | genuine gap |
| `Mathlib/HadamardFactorization.lean:300 HasHadamardFactorization` | a **DIFFERENT** Hadamard theorem | see below |
| `Mathlib/PermutationEnumeration.lean:353 CoxeterSwapFormulaHolds` | real API (`GroupTheory/Coxeter/{Basic,Length}.lean`) | **the one wiring candidate** — but see the overlap note |

## The Hadamard hit is a name collision, and it is Mathlib's

`Analysis/Complex/Hadamard.lean` exists and is the **three-lines theorem** — a bound on `‖f‖` across a vertical strip. `HasHadamardFactorization` needs the **factorization theorem**, `f(z) = exp(g(z))·∏ₙ Eₚ(z/aₙ)`. Different statements, different proofs, sharing only a surname. A keyword probe scores it as supported; it is not.

Worth noting the corpus file here is exemplary and should not be "fixed": the carrier is stated in full strength, its docstring explains why the product equation already forces the zero enumeration to be complete, and `hadamard_factorization_needs_nonneg_order` **proves** that dropping `0 ≤ ρ` makes the statement false. It names its own requirements — Jensen's formula, zero-counting, Weierstrass/Borel–Carathéodory growth. That is a genuine multi-session build, honestly labelled.

## Coxeter: do not take it without coordinating

`GroupTheory/Coxeter/Length.lean` is real and `CoxeterSwapFormulaHolds` is plausibly a wiring job against it. But `main` landed `fec0f466dd lean(qou-phir): length additivity iff no inversion is undone` on 2026-09-03 — active sibling work in exactly this API. Per `AGENTS.md`, measured research-overlap is permitted for **open-outcome** questions; wiring an existing Mathlib API is **mechanical** and has one owner. Coordinate on `qou-phir` before touching it.

## Consequence for `ParallelogramContour.lean`, landed alongside

`windingNumber` occurs **nowhere** in Mathlib, and there is no residue theorem (the only `residue` hits are p-adic and local-field ring homs — an unrelated sense). So both classical routes to `parallelogramIntegral_inv_sub_eq_two_pi_i` are absent upstream.

**That axiom is genuinely blocked; the Cauchy one next to it never was.** The file carried one shared "Goursat is infeasible" argument for both, and it was right about the pole integral and wrong about Cauchy — Cauchy for an *entire* function needs only a primitive, which is why `#6491` proved it in one pass. The discriminator is the pole, not the parallelogram. The stale clause "requires the Cauchy-Goursat theorem for parallelograms (which is blocked above)" is corrected in the same commit: that theorem is proved and is above.

## The honest bottom line

**The tractable Mathlib-infra tier is exhausted.** Of 38 Mathlib-shaped carriers, one (`StandardYoungCount`, `#6491`) was a leaf and is closed; one axiom (Cauchy, `#6491`) was a mis-diagnosis and is proved; one candidate (Coxeter) is a real wiring job owned by a sibling; the rest need mathematics Mathlib does not have. Continuing this line means building argument-principle / pivotal-category / moment-problem theory upstream, which is a project, not a drain.

The `96` Prop-valued fields are the separate and larger surface, and `qou-ar7f` re-scopes them: three of the four in `QOU/Mathlib/HeckeAlgebra.lean` are shadows of a concrete development, and the owner decision there (retire vs re-point) is still open.
