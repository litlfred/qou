---
# qou-idvt
title: 'MATHLIB GAP: ideal-tetrahedron hyperbolic volume theory (blocks qou-krvm (iv) + qou-7y3g)'
status: in-progress
type: task
priority: high
created_at: 2026-08-08T08:00:00Z
updated_at: 2026-08-08T08:00:00Z
---

Split out so two beans stop each carrying the same "large Mathlib gap" note.
**This one piece of infrastructure is the sole remaining blocker on both.**

## Who is blocked

  * `qou-krvm` hypothesis **(iv)** — the hyperbolic volume functional is CONCAVE
    and symmetry-INVARIANT on the angle-structure polytope (Rivin). With (i)-(iii)
    now Lean-proved for both anchors (PR #4513 m004, PR #4725 L6a4), (iv) is the
    ONLY thing between qou-krvm and closure.
  * `qou-7y3g` — `Vol(4_1) = 2*Cl_2(pi/3)` and `Vol(B_3) = 8*Catalan` are
    numerical only.

Both also feed `qou-skum`: if the volumes are FORCED by the cell decomposition
rather than measured, they reclassify from untraceable literals to `structural`
in the no-free-parameter certificate. That reclassification currently rests on
numerics.

## What Mathlib actually has (VERIFY before scoping — do not trust this list)

Mathlib has no ideal-simplex volume, no Mostow rigidity. What it may have, and
what makes the gap narrower than "build hyperbolic geometry":

  * `QOU.Archimedean.ClausenFunctionMathlibFiller` ALREADY EXISTS in this tree
    and is in the `FigureEightComplexVolume` import cone. **Start here.**
  * `Mathlib.Analysis.SpecialFunctions` — check for Clausen / Lobachevsky.
  * `FigureEightComplexVolume.V₄₁_zero_re` already states `V_41(0) = 2*Cl_2(pi/3)`
    EXACTLY at the Lean level (exact because `a_2` is purely imaginary).

So the corpus already has the closed FORM. What is missing is the bridge from
"this closed form" to "the hyperbolic volume of the manifold" — a much smaller,
much better-posed target than "hyperbolic volume theory".

## Suggested decomposition (tiered, so partial credit is real)

  T1  Lobachevsky function `Lambda(x) = -int_0^x log|2 sin t| dt` and its basic
      identities, on top of the existing Clausen filler.
  T2  Ideal-tetrahedron volume `Vol(alpha,beta,gamma) = Lambda(alpha)+Lambda(beta)+Lambda(gamma)`
      for a positive angle triple summing to pi.
  T3  **Concavity of T2 in the angles** — this alone discharges `qou-krvm` (iv)
      for the tetrahedral case, since invariance is immediate once the volume is
      a symmetric function of the angle triple. T3 IS THE PRIZE; T1-T2 are means.
  T4  The regular triple maximises T2 (gives `Vol(4_1) = 2*Lambda(pi/3)*...`
      forms and feeds `qou-7y3g`).

T3 is worth attempting on its own: concavity of a sum of `Lambda` over the
simplex `alpha+beta+gamma = pi` is a real-analysis statement, not a geometry one,
and does not need any manifold theory.

## GUARD — this bean exists BECAUSE of the laundering rule

Do NOT axiomatise "the volume functional is concave" as a Lean class and consume
it downstream to close `qou-krvm`. AGENTS.md: "Axiomatization is NOT a Proof."
A `class RivinConcavity` with a `sorry`-ed instance would make (iv) look
discharged while proving nothing. Either prove T3 or leave (iv) open and
labelled. `qou-7y3g` carries the same guard for the volume identity.

## Note on scale

This is infra-scale, not session-scale, as `qou-7y3g` says. But T3 alone may be
session-scale, and it is the piece that actually unblocks a downstream result.
Attack T3 first; do not start by building hyperbolic geometry.

---

## 2026-08-08 — T3's MATHEMATICAL CORE IS PROVED (sorry-free). Λ not needed.

`QOU/Archimedean/IdealTetrahedronConcavity.lean`. This bean assumed T3 needed
T1-T2 first (build Lobachevsky, then ideal-simplex volume, then concavity). **It
does not.** The concavity reduces to two trigonometric identities, and `Λ` does
not appear in the file at all.

Writing `f(α,β) = Λ(α)+Λ(β)+Λ(π−α−β)` with `Λ'' = −cot`, the Hessian is

    f_αα = −(cot α + cot γ)    f_αβ = −cot γ    f_ββ = −(cot β + cot γ)

and everything follows from:

  * `cot_cyclic_sum_eq_one` — `cot α cot β + cot β cot γ + cot γ cot α = 1`
    whenever `α+β+γ = π`. Hence `det H = 1` **exactly** (`hessian_det_eq_one`),
    not merely positive.
  * `cot_add_cot_pos` — `cot α + cot γ = sin β/(sin α sin γ) > 0`, so `f_αα < 0`.
  * `hessian_neg_definite` — negative definite at EVERY interior point.

Both identities are elementary (sine addition formula after clearing
denominators). No geometry, no manifold theory, no Rivin paper — the literature
was not needed.

**The awkward point is handled.** At `(π/4, π/4, π/2)` — L6a4's unique symmetric
point (`L6a4AngleStructure.unique_symmetric_point`) — `cot γ = 0`, the
off-diagonal vanishes, and the matrix looks degenerate. `det_eq_one_at_octahedron`
shows the determinant is still exactly 1 there. Since that is precisely the point
`qou-krvm` cares about, it is the case that had to work.

**Non-vacuity proved**: `regularTetrahedron` (m004's optimum) and
`regularOctahedron` (L6a4's) are exhibited, so `AngleTriple` is inhabited and the
universally-quantified theorems are not empty.

## WHAT THIS DOES NOT DO — read before citing

It does **not** close `qou-krvm` (iv), and the file says so. What is missing:

  1. `Λ` itself (T1) and `Vol = Λ(α)+Λ(β)+Λ(γ)` (T2). The corpus has `Cl_2` in
     `ClausenFunctionMathlibFiller` but no Lobachevsky function.
  2. `Λ'' = −cot`, which needs T1.
  3. The second-derivative test: "Hessian negative definite ⇒ strictly concave"
     needs Mathlib's `ContDiff`/`C²` machinery. Standard, but not free.

So the honest status is: **the part everyone assumed was hard is done; the
remaining part is plumbing.** T3 was mis-scoped in this bean as depending on
T1-T2 — it is the other way round for the *core*, though the plumbing does need
them.

Revised tiering: T1 (Lobachevsky on top of `Cl_2`) → T2 (`Vol` as the sum) →
**T3-core DONE** → T3-plumbing (second-derivative test) ⇒ `qou-krvm` (iv).
