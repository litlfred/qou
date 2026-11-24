/-
  Concavity of the ideal-tetrahedron volume: the Hessian is negative definite.
  Bean `qou-idvt` T3 — the piece that unblocks `qou-krvm` hypothesis (iv).

  WHY THIS IS HERE.  `qou-krvm` (iv) asks for Rivin's theorem: the hyperbolic
  volume functional is concave on the angle-structure polytope.  `qou-7y3g` and
  `qou-idvt` both recorded this as a "large Mathlib gap" — no ideal-simplex
  volume, no Mostow rigidity, build hyperbolic geometry first.

  **It is not that hard, for the tetrahedron.**  Writing `Λ` for the Lobachevsky
  function, the ideal-tetrahedron volume is `Λ(α) + Λ(β) + Λ(γ)` on the simplex
  `α + β + γ = π`, and `Λ'' = -cot`.  Parametrising by `(α, β)` with
  `γ = π - α - β`, the Hessian is

      f_αα = -(cot α + cot γ)      f_αβ = -cot γ      f_ββ = -(cot β + cot γ)

  and the whole theorem reduces to two trigonometric identities, both proved
  below with no geometry whatsoever:

    * `cot_cyclic_sum_eq_one` — `cot α cot β + cot β cot γ + cot γ cot α = 1`
      whenever `α + β + γ = π`.  Hence `det H = 1 > 0`, EXACTLY — not merely
      positive, and not degenerating anywhere on the simplex.
    * `cot_add_cot_pos` — `cot α + cot γ = sin β / (sin α sin γ) > 0`.  Hence
      `f_αα < 0`.

  Negative definiteness follows (`hessian_neg_definite`).  Note this holds at
  EVERY interior point, including `(π/4, π/4, π/2)` — the regular ideal
  octahedron's triple, where `cot γ = 0` and the Hessian looks degenerate but
  `det` is still exactly `1`.  That point is the one `L6a4AngleStructure` proves
  is L6a4's unique symmetric point, so the awkward case is the one that matters.

  WHAT IS PROVED HERE, AND WHAT IS NOT.

  * PROVED, sorry-free: both identities, and that the Hessian matrix is negative
    definite at every interior point of the simplex.
  * NOT PROVED, and NOT claimed: that this implies `Λ(α)+Λ(β)+Λ(γ)` is strictly
    concave.  That is the standard second-derivative test, and taking it in Lean
    needs the `C²` / `ContDiff` machinery (bean `qou-idvt` T3-plumbing, open).
  * `Λ` therefore does NOT appear below.  Nothing here is stated in terms of a
    volume; the file is about a 2x2 matrix of cotangents.  That is deliberate —
    it is the honest scope, and it keeps the result usable the moment T2 lands.

  UPDATE 2026-08-08 — the `Λ` half of that note was stale and is corrected.
  It read "T1-T2, still open — the corpus has `Cl_2` in
  `ClausenFunctionMathlibFiller` but no `Λ`".  In fact `QOU.Archimedean.Lob`
  (`= Cl_2 (2*t)/2`) already existed in `BlochWignerLobachevsky`, and **T1 is now
  done**: `Λ'' = -cot` — the identity this docstring states in prose above and
  whose absence was the stated reason `Λ` could not appear — is proved in
  `QOU/Archimedean/LobachevskyDerivative.lean` (`deriv_deriv_Lob`, sorry-free).

  What that changes here: nothing in the statements below, deliberately.  What it
  changes for a reader: the cotangents in this file are now KNOWN to be `Λ''`,
  so the Hessian is the Hessian of the Lobachevsky volume sum rather than of an
  unnamed function.  The remaining gap to `qou-krvm` (iv) is T2 (the *geometric*
  identification `Vol = Λ(α)+Λ(β)+Λ(γ)`) and T3-plumbing (the second-derivative
  test) — NOT `Λ` or its second derivative.

  Also worth knowing before using `Λ'' = -cot` here: **`Λ` is not concave on
  `(0,π)`** — `Λ''` is positive on `(π/2,π)` (`deriv_deriv_Lob_pos`).  The
  concavity below comes from the SUM, via `cot_add_cot_pos`; the octahedral
  triple `(π/4,π/4,π/2)` sits exactly at that sign change.

  A shape-coordinate entry point now exists too:
  `IdealTetrahedronShapeBridge.AngleTriple.ofShape` builds an `AngleTriple` from
  any `z` with `Im z > 0`, so every theorem below applies at a shape parameter.

  So this does not close `qou-krvm` (iv).  It removes the part everyone assumed
  was the hard part.

  Archimedean (ℝ): trigonometry and ordering throughout — §7c.

  -- Ref: [rivin1994] https://doi.org/10.2307/2118572 (concavity of hyperbolic
  --      volume on the angle-structure polytope — the qou-krvm (iv) source)
  -- Ref: [leitner2026] beans qou-idvt (T3), qou-krvm (iv)
-/

import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic

namespace QOU.Archimedean.IdealTetrahedronConcavity

open Real

/-- The dihedral-angle triple of an ideal tetrahedron: three positive angles
summing to `π`.  (Positivity plus the sum forces each to lie in `(0, π)`.) -/
structure AngleTriple where
  α : ℝ
  β : ℝ
  γ : ℝ
  hα : 0 < α
  hβ : 0 < β
  hγ : 0 < γ
  sum : α + β + γ = Real.pi

namespace AngleTriple

variable (t : AngleTriple)

theorem α_lt_pi : t.α < Real.pi := by have := t.sum; linarith [t.hβ, t.hγ]
theorem β_lt_pi : t.β < Real.pi := by have := t.sum; linarith [t.hα, t.hγ]
theorem γ_lt_pi : t.γ < Real.pi := by have := t.sum; linarith [t.hα, t.hβ]

/-- Every angle has strictly positive sine — the workhorse. -/
theorem sin_α_pos : 0 < Real.sin t.α := Real.sin_pos_of_pos_of_lt_pi t.hα t.α_lt_pi
theorem sin_β_pos : 0 < Real.sin t.β := Real.sin_pos_of_pos_of_lt_pi t.hβ t.β_lt_pi
theorem sin_γ_pos : 0 < Real.sin t.γ := Real.sin_pos_of_pos_of_lt_pi t.hγ t.γ_lt_pi

end AngleTriple

/-! ## Identity 1 — the determinant is exactly 1 -/

/-- **`cot α cot β + cot β cot γ + cot γ cot α = 1` for `α + β + γ = π`.**

This is what makes `det H = 1` exactly, at every interior point.  Proved by
clearing denominators onto the sine addition formula: with
`sin(α+β) = sin γ` and `cos(α+β) = -cos γ`, the numerator collapses. -/
theorem cot_cyclic_sum_eq_one (t : AngleTriple) :
    Real.cos t.α / Real.sin t.α * (Real.cos t.β / Real.sin t.β)
      + Real.cos t.β / Real.sin t.β * (Real.cos t.γ / Real.sin t.γ)
      + Real.cos t.γ / Real.sin t.γ * (Real.cos t.α / Real.sin t.α) = 1 := by
  have sa := t.sin_α_pos; have sb := t.sin_β_pos; have sg := t.sin_γ_pos
  -- γ = π - (α + β), so sin γ = sin (α+β) and cos γ = -cos (α+β)
  have hγ : t.γ = Real.pi - (t.α + t.β) := by have := t.sum; linarith
  have hsin : Real.sin t.γ = Real.sin t.α * Real.cos t.β + Real.cos t.α * Real.sin t.β := by
    rw [hγ, Real.sin_pi_sub, Real.sin_add]
  have hcos : Real.cos t.γ = -(Real.cos t.α * Real.cos t.β - Real.sin t.α * Real.sin t.β) := by
    rw [hγ, Real.cos_pi_sub, Real.cos_add]
  field_simp
  rw [hsin, hcos]
  ring

/-! ## Identity 2 — the diagonal entries are negative -/

/-- **`cot α + cot γ = sin β / (sin α sin γ)`.**  Immediate from the sine
addition formula, since `α + γ = π - β`. -/
theorem cot_add_cot_eq (t : AngleTriple) :
    Real.cos t.α / Real.sin t.α + Real.cos t.γ / Real.sin t.γ
      = Real.sin t.β / (Real.sin t.α * Real.sin t.γ) := by
  have sa := t.sin_α_pos; have sg := t.sin_γ_pos
  have hβ : t.β = Real.pi - (t.α + t.γ) := by have := t.sum; linarith
  have hsin : Real.sin t.β = Real.sin t.α * Real.cos t.γ + Real.cos t.α * Real.sin t.γ := by
    rw [hβ, Real.sin_pi_sub, Real.sin_add]
  field_simp
  rw [hsin]; ring

/-- Hence `cot α + cot γ > 0`, so the Hessian's diagonal entries are negative. -/
theorem cot_add_cot_pos (t : AngleTriple) :
    0 < Real.cos t.α / Real.sin t.α + Real.cos t.γ / Real.sin t.γ := by
  rw [cot_add_cot_eq t]
  exact div_pos t.sin_β_pos (mul_pos t.sin_α_pos t.sin_γ_pos)

/-! ## Negative definiteness -/

/-- A symmetric `2x2` form with negative leading entry and positive determinant
is negative definite.  Completing the square: `A·Q = (A x + B y)² + (AC - B²) y²`,
and `A < 0` flips it. -/
theorem quadratic_neg_of_lead_neg_of_det_pos {A B C x y : ℝ}
    (hA : A < 0) (hdet : 0 < A * C - B ^ 2) (hxy : x ≠ 0 ∨ y ≠ 0) :
    A * x ^ 2 + 2 * B * x * y + C * y ^ 2 < 0 := by
  have key : A * (A * x ^ 2 + 2 * B * x * y + C * y ^ 2)
      = (A * x + B * y) ^ 2 + (A * C - B ^ 2) * y ^ 2 := by ring
  rcases eq_or_ne y 0 with rfl | hy
  · -- `y = 0`, so `x ≠ 0`: the form is `A x²` with `A < 0`.
    have hx : x ≠ 0 := by
      rcases hxy with h | h
      · exact h
      · exact absurd rfl h
    have hx2 : 0 < x ^ 2 := by positivity
    nlinarith
  · -- `y ≠ 0`: the completed square is strictly positive, and `A < 0` flips it.
    have hy2 : 0 < y ^ 2 := by positivity
    have hpos : 0 < (A * x + B * y) ^ 2 + (A * C - B ^ 2) * y ^ 2 := by
      have h1 := sq_nonneg (A * x + B * y)
      have h2 : 0 < (A * C - B ^ 2) * y ^ 2 := mul_pos hdet hy2
      linarith
    nlinarith [key, hpos]

/-- **The Hessian of the ideal-tetrahedron volume is negative definite.**

Entries `A = -(cot α + cot γ)`, `B = -cot γ`, `C = -(cot β + cot γ)`.  The proof
is the two identities: `A < 0` by `cot_add_cot_pos`, and `A·C - B² = 1` by
`cot_cyclic_sum_eq_one`.

Holds at every interior point of the simplex, the regular octahedral triple
`(π/4, π/4, π/2)` included — there `cot γ = 0` and the matrix looks degenerate,
but the determinant is still exactly `1`. -/
theorem hessian_neg_definite (t : AngleTriple) {x y : ℝ} (hxy : x ≠ 0 ∨ y ≠ 0) :
    (-(Real.cos t.α / Real.sin t.α + Real.cos t.γ / Real.sin t.γ)) * x ^ 2
      + 2 * (-(Real.cos t.γ / Real.sin t.γ)) * x * y
      + (-(Real.cos t.β / Real.sin t.β + Real.cos t.γ / Real.sin t.γ)) * y ^ 2 < 0 := by
  set ca := Real.cos t.α / Real.sin t.α
  set cb := Real.cos t.β / Real.sin t.β
  set cg := Real.cos t.γ / Real.sin t.γ
  have hA : -(ca + cg) < 0 := neg_neg_iff_pos.mpr (cot_add_cot_pos t)
  have hid : ca * cb + cb * cg + cg * ca = 1 := cot_cyclic_sum_eq_one t
  have hdet : 0 < (-(ca + cg)) * (-(cb + cg)) - (-cg) ^ 2 := by nlinarith [hid]
  exact quadratic_neg_of_lead_neg_of_det_pos hA hdet hxy

/-- The determinant, isolated: it is exactly `1` everywhere on the simplex — not
merely positive.  Recorded separately because the exactness is the surprising
part and is what keeps the octahedral point non-degenerate. -/
theorem hessian_det_eq_one (t : AngleTriple) :
    (-(Real.cos t.α / Real.sin t.α + Real.cos t.γ / Real.sin t.γ))
        * (-(Real.cos t.β / Real.sin t.β + Real.cos t.γ / Real.sin t.γ))
      - (-(Real.cos t.γ / Real.sin t.γ)) ^ 2 = 1 := by
  have hid := cot_cyclic_sum_eq_one t
  nlinarith [hid]

/-! ## Non-vacuity: the simplex is inhabited, including the awkward point

Every theorem above is universally quantified over `AngleTriple`.  If that
structure were empty they would all hold vacuously, so the two triples the corpus
actually cares about are exhibited. -/

/-- The regular ideal TETRAHEDRON triple — m004's Casson-Rivin optimum
(`M004AngleStructure.regular_unique_on_fixed_locus`), in radians. -/
noncomputable def regularTetrahedron : AngleTriple where
  α := Real.pi / 3
  β := Real.pi / 3
  γ := Real.pi / 3
  hα := by positivity
  hβ := by positivity
  hγ := by positivity
  sum := by ring

/-- The regular ideal OCTAHEDRON triple — L6a4's unique symmetric point
(`L6a4AngleStructure.unique_symmetric_point`), in radians.

This is the case worth having: `cot(π/2) = 0`, so the Hessian's off-diagonal
vanishes and the matrix *looks* degenerate. It is not — `hessian_det_eq_one`
gives determinant exactly `1` here too. -/
noncomputable def regularOctahedron : AngleTriple where
  α := Real.pi / 4
  β := Real.pi / 4
  γ := Real.pi / 2
  hα := by positivity
  hβ := by positivity
  hγ := by positivity
  sum := by ring

/-- The determinant is `1` at the octahedral point — the potentially degenerate
one — so negative definiteness is not lost there. -/
theorem det_eq_one_at_octahedron :
    (-(Real.cos regularOctahedron.α / Real.sin regularOctahedron.α
        + Real.cos regularOctahedron.γ / Real.sin regularOctahedron.γ))
      * (-(Real.cos regularOctahedron.β / Real.sin regularOctahedron.β
        + Real.cos regularOctahedron.γ / Real.sin regularOctahedron.γ))
      - (-(Real.cos regularOctahedron.γ / Real.sin regularOctahedron.γ)) ^ 2 = 1 :=
  hessian_det_eq_one regularOctahedron

end QOU.Archimedean.IdealTetrahedronConcavity
