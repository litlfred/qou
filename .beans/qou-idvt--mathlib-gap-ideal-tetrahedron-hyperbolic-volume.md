---
# qou-idvt
title: 'MATHLIB GAP: ideal-tetrahedron hyperbolic volume theory (blocks qou-krvm (iv) + qou-7y3g)'
status: todo
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
