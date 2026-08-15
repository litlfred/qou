---
# glhi
title: 'Lean gluing proofs: degrees 7–14, cusp equations, and wiring to SatisfiesEdgeEquations'
status: todo
type: task
priority: normal
tags:
    - lean
    - hyperbolic-volume
    - gluing-equations
    - codegen
parent: m015
created_at: 2026-08-10T07:00:00Z
updated_at: 2026-08-10T07:00:00Z
---

The successor to `glnl`, which delivered 312 Lean theorems across 19 manifolds at shape
field degrees 2–6 and is **completed** for that scope. Three things it deliberately did
not do.

## 1. Degrees 7–14

Route 75 verifies these exactly in Python; Lean has nothing for them:

| manifold | degree |
|---|---|
| 9₂ | 7 |
| 10₁, 7₅, 8₂, 8₃ | 8 |
| 7₆ | 9 |
| t12000 | 13 |
| 10₁₀₀ | 14 |

`scripts/gen-gluing-lean.py` handles them in principle — the method does not care about
degree. What grows is the **cofactor size**: each edge equation's certificate is
`(LHS − RHS)/P`, and at degree 14 with 16 equations the emitted `linear_combination`
terms get large. Measure before committing to it; a file that takes an hour to compile is
worse than no file.

## 2. Cusp equations

`glnl` covered **edge** equations only, because those have non-negative exponents and
clear to a polynomial identity. Cusp equations carry **negative** exponents — 5₂'s are
`[-1,0,0, 0,0,1, 0,0,0]` and `[2,0,-3, 1,0,-2, 0,0,1]` — so they need each parameter's
inverse as an explicit polynomial in `θ` (available: the parameters are units in
`ℚ(θ)`, and `sympy.invert` already computes exactly this for the Bézout certificates),
plus `zpow` handling in the statement.

Route 75 verifies all cusp equations symbolically in Python. Lean does not.

## 3. Wire the generated theorems to `SatisfiesEdgeEquations`

`glnl`'s own bean asked for this and it was not done: the generated theorems are
**standalone**, when `QOU/MathlibExt/IdealTriangulation.lean` already has `GluingData n e`
and `SatisfiesEdgeEquations`. Landing them as instances of that structure turns the
generated file from a parallel pile of identities into **certification of the corpus's
existing triangulation objects**, which is what makes it compose with
`FiveTwoVolumeConstant`, `FigureEightTriangulation` and the volume functor.

Note the flat-shape generalisation from `m015`: `SatisfiesEdgeEquations` currently lives
on `IdealTriangulation`, which carries `im_pos`. `QOU/Knot/FlatTetrahedra.lean` added
`ShapedTriangulation.SatisfiesEdgeEquations` over possibly-flat shapes. Wiring should
target the **weaker** one — the generated identities hold for an arbitrary root of the
minimal polynomial, which is exactly the flat-tolerant setting, and pinning them to
`im_pos` would re-import a hypothesis the proofs do not use.

## Method, unchanged and known to work

Verbatim from `glnl`, because it held up: state each identity for an **arbitrary root** of
the minimal polynomial (the verification lives in `ℚ[x]/(P)`, so it holds at every root,
which sidesteps root selection); prove non-vanishing by Bézout certificate; prove each
cleared edge equation by one `linear_combination` with a cofactor from exact polynomial
division. **Do not reach for `field_simp`** — its normal form is unpredictable and cannot
be code-generated.
