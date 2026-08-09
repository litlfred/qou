/-
  Rivin concavity — the Hessian of the volume functional on an angle structure.

  Bean `qou-rvnc`, parent `qou-krvm` (iv): "the volume functional is concave and
  invariant (Rivin; not in Mathlib)" — the last of the four hypotheses of
  `SymmetricOptimum.optima_coincide` left untouched, and the gate on the
  Casson–Rivin route to hyperbolic volume.

  ═══ WHAT THIS FILE PROVES, AND WHAT IT DELIBERATELY DOES NOT ═══

  The volume of an ideal tetrahedron with dihedral angles `α, β, γ` (summing to
  `π`) is `Λ(α) + Λ(β) + Λ(γ)`, with `Λ` the Lobachevsky function.  Rivin's
  theorem is that the total volume is *strictly concave* on the space of angle
  structures.

  ⚠ **`Λ` is NOT concave.**  `Λ″(θ) = −cot θ`, so `Λ` is concave on `(0, π/2)`
  and **convex** on `(π/2, π)`.  Any attempt to prove Rivin's theorem by
  concavity of `Λ` termwise is doomed; that is the trap this file exists to
  avoid.  What is true is concavity of the *sum* on the simplex, and the
  constraint `α + β + γ = π` is exactly what makes it work.

  The Hessian of `Λ(α) + Λ(β) + Λ(γ)` is `diag(−cot α, −cot β, −cot γ)`.
  Restricted to the tangent space `{u + v + w = 0}` of the constraint, negative
  definiteness is precisely `cotQuadratic > 0`, which is `cot_quadratic_pos`
  below.  **That is the mathematical content of Rivin concavity for one
  tetrahedron, and it is what this file delivers.**

  It is delivered *without any analysis*: the proof is an exact sum-of-squares
  identity (`sos_identity`), verified symbolically before being written.  With
  `a = cot α`, `b = cot β` and `w = −(u+v)`,

      (a + b) · (a·u² + b·v² + cot γ·w²)  =  (a·u − b·v)²  +  (u + v)²

  and `a + b = sin γ / (sin α · sin β) > 0`.  At most one of the three angles
  can exceed `π/2`, so at most one cotangent is negative — the identity is how
  that gets used, and no case split on which angle is obtuse is needed.

  **Not claimed here:** that `Λ″ = −cot` (that is the analytic half, and needs
  a second derivative of `Cl₂`; `QOU/Knot/Clausen.lean` has the first,
  `hasDerivAt_clausen`).  Nothing here mentions `Λ`, so nothing here depends on
  it.  The quadratic-form fact is the reusable piece and is stated on its own.

  ⚠ **The bound is NOT uniform.**  Strict positivity holds pointwise on the open
  simplex and degenerates at the boundary: numerically the normalised minimum
  over 300k samples at 30 dps is `9.3e-4`, approached only as `α → π`.  Any
  downstream argument that wants a uniform constant will fail; keep it
  pointwise.

  -- Ref: [rivin1994] Euclidean structures on simplicial surfaces and hyperbolic
  --      volume, Ann. of Math. 139 (1994)
  -- Ref: [futer-gueritaud2011] From angled triangulations to hyperbolic
  --      structures, https://arxiv.org/abs/1004.0440
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic

namespace QOU.Knot.Rivin

open Real

/-! ### The sum-of-squares identity, as pure algebra

No trigonometry and no angles: `sa, ca, sb, cb` are formal stand-ins for
`sin α, cos α, sin β, cos β`, and the third angle's cotangent enters as
`(sa·sb − ca·cb)/(sa·cb + ca·sb)`, which is what `cot(π − α − β)` expands to.
Keeping this step trig-free is what makes it a one-line `field_simp; ring`
instead of a fight with `sin_add`/`cos_add` under a `field_simp`. -/

/-- **The identity.**  Clearing the denominators of

    `cot α·u² + cot β·v² + cot γ·w²`   (with `γ = π − α − β`, `w = −(u+v)`)

turns it into a sum of two squares.  Verified symbolically (sympy, exact) before
being stated. -/
theorem sos_identity (sa ca sb cb u v : ℝ) (hsa : sa ≠ 0) (hsb : sb ≠ 0)
    (hsg : sa * cb + ca * sb ≠ 0) :
    (ca / sa * u ^ 2 + cb / sb * v ^ 2
        + (sa * sb - ca * cb) / (sa * cb + ca * sb) * (-(u + v)) ^ 2)
      * (sa * sb * (sa * cb + ca * sb))
      = (ca * sb * u - sa * cb * v) ^ 2 + (sa * sb) ^ 2 * (u + v) ^ 2 := by
  field_simp
  ring

/-! ### The trigonometric form -/

/-- Every angle of a "triangle" (three positive reals summing to `π`) is `< π`,
so its sine is positive.  Stated for the first slot; apply with the arguments
permuted for the others. -/
theorem sin_pos_of_sum_pi {α β γ : ℝ} (hα : 0 < α) (hβ : 0 < β) (hγ : 0 < γ)
    (hsum : α + β + γ = π) : 0 < Real.sin α :=
  Real.sin_pos_of_pos_of_lt_pi hα (by linarith)

/-- The quadratic form appearing as `−(Hessian)` of the tetrahedron volume,
restricted to the tangent space of `α + β + γ = π`. -/
noncomputable def cotQuadratic (α β γ u v w : ℝ) : ℝ :=
  Real.cos α / Real.sin α * u ^ 2 + Real.cos β / Real.sin β * v ^ 2
    + Real.cos γ / Real.sin γ * w ^ 2

/-- **Rivin concavity for one ideal tetrahedron** — the Hessian of
`Λ(α)+Λ(β)+Λ(γ)` is negative definite on the tangent space of the constraint.

Given positive angles summing to `π` and a tangent vector `u + v + w = 0` that
is not zero,

    `cot α·u² + cot β·v² + cot γ·w²  >  0`.

Note the hypothesis is `¬(u = 0 ∧ v = 0)`, which under `u + v + w = 0` is
exactly `(u, v, w) ≠ 0`.

No case analysis on which angle is obtuse: the sum-of-squares identity absorbs
it. -/
theorem cot_quadratic_pos {α β γ u v w : ℝ}
    (hα : 0 < α) (hβ : 0 < β) (hγ : 0 < γ) (hsum : α + β + γ = π)
    (htan : u + v + w = 0) (hne : ¬(u = 0 ∧ v = 0)) :
    0 < cotQuadratic α β γ u v w := by
  -- the three sines are positive
  have hsa : 0 < Real.sin α := sin_pos_of_sum_pi hα hβ hγ hsum
  have hsb : 0 < Real.sin β := sin_pos_of_sum_pi hβ hα hγ (by linarith)
  have hsg : 0 < Real.sin γ := sin_pos_of_sum_pi hγ hα hβ (by linarith)
  -- expand `sin γ` and `cos γ` through `γ = π − (α + β)`
  have hγeq : γ = π - (α + β) := by linarith
  have hsgx : Real.sin γ = Real.sin α * Real.cos β + Real.cos α * Real.sin β := by
    rw [hγeq, Real.sin_pi_sub, Real.sin_add]
  have hcgx : Real.cos γ = Real.sin α * Real.sin β - Real.cos α * Real.cos β := by
    rw [hγeq, Real.cos_pi_sub, Real.cos_add]; ring
  have hw : w = -(u + v) := by linarith
  -- the identity
  have hid : cotQuadratic α β γ u v w
      * (Real.sin α * Real.sin β * Real.sin γ)
      = (Real.cos α * Real.sin β * u - Real.sin α * Real.cos β * v) ^ 2
        + (Real.sin α * Real.sin β) ^ 2 * (u + v) ^ 2 := by
    unfold cotQuadratic
    rw [hw, hsgx, hcgx]
    exact sos_identity _ _ _ _ _ _ hsa.ne' hsb.ne' (by rw [← hsgx]; exact hsg.ne')
  -- the numerator is strictly positive
  have hnum : 0 < (Real.cos α * Real.sin β * u - Real.sin α * Real.cos β * v) ^ 2
      + (Real.sin α * Real.sin β) ^ 2 * (u + v) ^ 2 := by
    rcases eq_or_lt_of_le (by positivity :
        (0:ℝ) ≤ (Real.cos α * Real.sin β * u - Real.sin α * Real.cos β * v) ^ 2
          + (Real.sin α * Real.sin β) ^ 2 * (u + v) ^ 2) with h | h
    · -- if it vanished, both squares vanish and `(u, v) = 0`
      exfalso
      have h1 : (Real.cos α * Real.sin β * u - Real.sin α * Real.cos β * v) ^ 2 = 0 := by
        nlinarith [sq_nonneg (Real.cos α * Real.sin β * u - Real.sin α * Real.cos β * v),
          sq_nonneg (u + v), mul_pos hsa hsb, sq_nonneg (Real.sin α * Real.sin β)]
      have h2 : (Real.sin α * Real.sin β) ^ 2 * (u + v) ^ 2 = 0 := by
        nlinarith [sq_nonneg (Real.cos α * Real.sin β * u - Real.sin α * Real.cos β * v),
          sq_nonneg (u + v), sq_nonneg (Real.sin α * Real.sin β)]
      have huv : u + v = 0 := by
        have hab : (Real.sin α * Real.sin β) ^ 2 ≠ 0 := by positivity
        have := mul_eq_zero.mp h2
        rcases this with h' | h'
        · exact absurd h' hab
        · exact pow_eq_zero_iff (n := 2) (by norm_num) |>.mp h'
      have hv : v = -u := by linarith
      have h1' : Real.cos α * Real.sin β * u - Real.sin α * Real.cos β * v = 0 :=
        pow_eq_zero_iff (n := 2) (by norm_num) |>.mp h1
      rw [hv] at h1'
      -- `u · sin γ = 0`
      have : u * Real.sin γ = 0 := by rw [hsgx]; linarith [h1']
      have hu : u = 0 := by
        rcases mul_eq_zero.mp this with h' | h'
        · exact h'
        · exact absurd h' hsg.ne'
      exact hne ⟨hu, by rw [hv, hu]; ring⟩
    · exact h
  -- divide
  have hden : 0 < Real.sin α * Real.sin β * Real.sin γ := by positivity
  nlinarith [hid, hnum, hden]

end QOU.Knot.Rivin
