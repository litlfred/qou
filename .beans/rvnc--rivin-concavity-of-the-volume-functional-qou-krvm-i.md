---
# rvnc
title: 'Rivin concavity of the volume functional — qou-krvm (iv), the last untouched hypothesis'
status: todo
type: task
priority: high
tags:
    - lean
    - hyperbolic-volume
    - angle-structures
parent: krvm
created_at: 2026-08-09T19:15:46Z
updated_at: 2026-08-09T19:15:46Z
---

`M004AngleStructure.lean` lists four hypotheses of `SymmetricOptimum.optima_coincide`
that bean `qou-krvm` needs discharged. (i) is settled for m004, (ii) was **refuted
as stated** and repaired, (iii) is done. **(iv) is untouched**: "the volume functional
is concave and invariant (Rivin; not in Mathlib)".

This is the single gate on the Casson–Rivin route to `Vol(5₂) = 3·D(y₁)` — and it is
not knot-specific, so discharging it unblocks m004, L6a4, m015 and every future anchor
at once. Highest leverage item in the volume lane.

**Why it is more tractable than its reputation.** It is not an analysis problem; it is
a Hessian sign. The volume functional on an angle structure is `Σ Λ(θᵢ)` with `Λ` the
Lobachevsky function, and `Λ″(θ) = −cot θ`. On the *linear* affine slice cut out by the
gluing equations, concavity is the statement that a specific quadratic form is negative
semidefinite. That reduces to algebra plus the sign of `cot` on `(0, π)`.

**The corpus already has the pieces** — contrary to the note in `M004AngleStructure.lean`
that "Mathlib has no ideal-tetrahedron volume theory". True of Mathlib, false of QOU:
`QOU/Archimedean/BlochWignerLobachevsky.lean` has `Cl_2`, `Lob`, `tetAngle₁/₂/₃`,
`tetAngles_sum_eq_pi`, `BlochWigner_lob`, and `Vol(S(z)) = Λ(α)+Λ(β)+Λ(γ) = D(z)` as a
theorem. That note should be narrowed when this lands — the missing piece is concavity,
not the volume theory.

**The exact statement, checked numerically 2026-08-09 before this bean was written.**
`Λ` is **NOT** globally concave on `(0, π)`: `Λ″(θ) = −cot θ`, so `Λ` is concave on
`(0, π/2)` and **convex** on `(π/2, π)`. Do not state or attempt the global claim.

What is true is concavity of the *sum* on the simplex. With `α+β+γ = π`, the Hessian of
`Λ(α)+Λ(β)+Λ(γ)` is `diag(−cot α, −cot β, −cot γ)` restricted to the tangent space
`{u+v+w = 0}`, so the target is exactly

    u + v + w = 0,  α + β + γ = π,  α,β,γ ∈ (0,π),  (u,v,w) ≠ 0
      ⟹   cot α·u² + cot β·v² + cot γ·w²  >  0

At most one angle can be `≥ π/2`, so at most one `cot` is `≤ 0` — that is the whole
mechanism, and it is a `nlinarith`-shaped fact, not analysis.

Sanity check: 300k random samples of `(α,β,γ,u,v)` at 30 dps give normalised
`Q = 0.00093…` as the minimum, strictly positive, approached only at the degenerate
corner `α → π`. Note the corollary for formalisation: strict concavity holds pointwise
on the **open** simplex but the bound is **not uniform** — it degenerates at the
boundary. Any proof that wants a uniform constant will fail; keep it pointwise.

**Control.** The trefoil `3₁` is not hyperbolic (`KnotRegistry.trefoil_volume_zero`,
`Vol_q(β_{3₁}) = 0`). Any concavity/optimum machinery must yield *no positively-oriented
solution* for `3₁`. If a route hands the trefoil a volume, the route is wrong.
