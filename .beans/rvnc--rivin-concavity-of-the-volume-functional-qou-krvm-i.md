---
# rvnc
title: Rivin concavity of the volume functional — qou-krvm (iv), the last untouched hypothesis
status: completed
type: task
priority: high
tags:
    - lean
    - hyperbolic-volume
    - angle-structures
created_at: 2026-08-09T19:15:46Z
updated_at: 2026-09-03T04:38:06Z
parent: krvm
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

---
**2026-08-09 — the algebraic half is DONE.** `QOU/Knot/RivinConcavity.lean`,
sorry-free, axioms `[propext, Classical.choice, Quot.sound]`, `lake build` exit 0
at 3089 jobs with the `.olean` deleted first, zero warnings.

* `sos_identity` — the sum-of-squares identity as pure algebra (no trig, no
  angles): `field_simp; ring`. Verified symbolically in sympy (exact, residual 0)
  before being written, which is why it went in first try.
* `cot_quadratic_pos` — **the Hessian fact**: for `α,β,γ > 0` summing to `π` and
  `u+v+w = 0` not all zero, `cot α·u² + cot β·v² + cot γ·w² > 0`. No case split
  on which angle is obtuse — the SOS absorbs it.

That is the negative-definiteness of the Hessian of `Λ(α)+Λ(β)+Λ(γ)` on the
tangent space of the constraint, i.e. the mathematical content of Rivin
concavity for one tetrahedron.

**2026-08-09 later — the ANALYTIC half is done too** (`mlgp` Gap 2 closed), in
the same file:

* `hasDerivAt_Lob` — `Λ′(t) = −log(2 sin t)` on `(0, π)`, by chain rule on
  `Λ(t) = Cl₂(2t)/2` through the corpus's `QOU.Knot.hasDerivAt_Cl_2_series`.
  The inner factor `2` cancels the `/2` in the normalisation — which is why
  that normalisation is the standard one.
* `hasDerivAt_deriv_Lob` — **`Λ″(t) = −cot t`** on `(0, π)`.
* `deriv_deriv_Lob` — the same as a `deriv` equation.

So the quadratic form in `cot_quadratic_pos` really **is** the Hessian, not a
form asserted to be one. Verified: `lake build` exit 0 / 3157 jobs with the
`.olean` deleted first; `#print axioms` standard on all of
`hasDerivAt_Lob`, `hasDerivAt_deriv_Lob`, `deriv_deriv_Lob`,
`cot_quadratic_pos` — **and on the corpus inputs I leaned on**,
`QOU.Knot.hasDerivAt_Cl_2_series` and `QOU.Knot.clausen_eq_series`, which I
checked rather than took from their docstrings.

**What is STILL owed, and it is now Gap 3 not Gap 2.** The step from "Hessian
negative definite on the tangent space, pointwise" to "strictly concave on the
angle-structure polytope". That wants a lemma about concavity on an affine
slice; check `Mathlib.Analysis.Convex.*` before writing one. Remember the bound
is pointwise and degenerates at the boundary, so anything wanting a uniform
modulus will not apply.

So `qou-krvm` (iv) is **not** discharged — but what remains is assembly, not the
mathematical content, which is done.

CLAIMED 2026-09-03 (session back-to-math). Plan: formalize single-ideal-tetrahedron concavity — Hessian on the slice gamma=pi-alpha-beta is [[-cotA-cotG,-cotG],[-cotG,-cotB-cotG]]; det = cotA cotB + cotB cotG + cotG cotA = 1 (triangle cotangent identity for A+B+G=pi), diagonal -cotA-cotG = -sinB/(sinA sinG) < 0 => negative definite. Then block-diagonal over tets + restriction to gluing slice preserves NSD. Verifying against M004AngleStructure hypothesis (iv) + BlochWignerLobachevsky (has Lob, Cl_2, tetAngle).

── UPDATE 2026-09-03 (session back-to-math), corpus-grep before writing new Lean ──

(iv)'s CONCAVITY is ALREADY DISCHARGED in the corpus — this bean was stale. The
qou-7425 / qou-idvt cluster did the multi-tet lift while this bean still called
(iv) 'untouched':

 • QOU.Archimedean.tetVol_strictConcaveOn — single ideal tet, the real Lobachevsky
   volume, StrictConcaveOn on the 2-D tetSimplex. Independent of my line-route
   RivinConcavity.strictConcaveOn_tetVolLine (SOS Hessian). TWO proofs of the core.
 • MultiTetVolumeConcave.totalVol_strictConcaveOn — block-diagonal sum over tets on
   any convex block-in-simplex polytope (exactly this bean's planned lift).
 • MultiTetVolumeConcave.m004Vol_maximizer_unique / convex_m004Polytope — concrete
   figure-eight: unique volume maximiser. Uniqueness needs NO symmetry (strict
   concavity alone), so (iv)'s 'invariant' half is not required to close m004.

All verified sorry-free this session via lean-direct + #print axioms
([propext, Classical.choice, Quot.sound]) against the restored v4-24-0 cache.

WHAT I ADDED (not a re-derivation — the wiring/hygiene the bean's plan called for):
 • MultiTetVolumeConcave.m004Vol_concaveOn : ConcaveOn ℝ m004Polytope totalVol —
   the concrete (iv)-concave-half in the exact form SymmetricOptimum.optima_coincide
   consumes as hf₂, greppable by the hypothesis framing. sorry-free.
 • Narrowed the two stale '(iv) is untouched' notes in M004AngleStructure.lean to
   point at the cluster and name the corpus's own tetVol volume theory.

WHAT GENUINELY REMAINS OPEN (NOT concavity — do not re-attack that): the GEOMETRIC
IDENTIFICATION that the analytic totalVol IS the hyperbolic volume of the ideal
simplex (Mostow/Thurston; Mathlib has no ideal-tet geometry). That is beans
qou-7y3g / qou-idvt T2, a large geometric-realization item, out of rvnc's scope.
rvnc (the Rivin CONCAVITY) is done.
