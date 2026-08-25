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

  **The analytic half is here too** (bean `qou-mlgp` Gap 2): `hasDerivAt_Lob`
  gives `Λ′(t) = −log(2 sin t)` and `hasDerivAt_deriv_Lob` gives
  `Λ″(t) = −cot t`, both on `(0, π)`.  The input is the corpus's own
  `QOU.Knot.hasDerivAt_Cl_2_series` — Mathlib has **neither** Clausen nor
  Lobachevsky.  So the quadratic form above really is the Hessian, rather than
  a form asserted to be one.

  The two halves are kept separate on purpose: `cot_quadratic_pos` mentions no
  `Λ` and no analysis, so it is reusable on its own.

  **And the assembly** (`qou-mlgp` Gap 3, for one tetrahedron):
  `strictConcaveOn_tetVolLine` — `Λ(α)+Λ(β)+Λ(γ)` is *strictly concave along
  every line in the angle simplex*.  Since strict concavity on a convex set is
  exactly strict concavity along every segment, that is Rivin's theorem for a
  single tetrahedron.

  The mechanism worth naming: the tangent condition `u+v+w = 0` is precisely what
  keeps the angles summing to `π` all along the line, so `cot_quadratic_pos`
  applies at *every* point of it, not just at the basepoint.  Restricting to a
  line is what makes this one-variable, so Mathlib's
  `strictConcaveOn_of_deriv2_neg'` applies directly and no multivariable
  second-derivative test is needed.

  **What is still not claimed.**  Nothing here is about a *specific*
  triangulation, and nothing here sums over tetrahedra: m004 and L6a4 have
  angle-structure polytopes, m015 (5₂) does not (bean `qou-m015`).  And nothing
  here evaluates a volume — see below.

  ⚠ **The bound is NOT uniform.**  Strict positivity holds pointwise on the open
  simplex and degenerates at the boundary: numerically the normalised minimum
  over 300k samples at 30 dps is `9.3e-4`, approached only as `α → π`.  Any
  downstream argument that wants a uniform constant will fail; keep it
  pointwise.

  -- Ref: [rivin1994] Euclidean structures on simplicial surfaces and hyperbolic
  --      volume, Ann. of Math. 139 (1994)
  -- Ref: [futer-gueritaud-angled] From angled triangulations to hyperbolic
  --      structures, https://arxiv.org/abs/1004.0440
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Tactic
import QOU.Knot.Clausen
import QOU.Archimedean.BlochWignerLobachevsky

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

/-! ### The analytic half — `Λ′ = −log(2 sin)` and `Λ″ = −cot`

Bean `qou-mlgp` Gap 2.  This is what makes `cot_quadratic_pos` a statement about
the **Hessian** rather than about a quadratic form merely asserted to be one.

Mathlib has no Clausen and no Lobachevsky function; the corpus supplies both.
The input is `QOU.Knot.hasDerivAt_Cl_2_series` — `Cl₂′(θ) = −log(2 sin(θ/2))`
on `(0, 2π)`, sorry-free — and `Λ(t) = Cl₂(2t)/2`, so one chain rule gives `Λ′`
and one more differentiation gives `Λ″`. -/

/-- **`Λ′(t) = −log(2 sin t)` on `(0, π)`.**

Chain rule on `Λ(t) = Cl₂(2t)/2` through `hasDerivAt_Cl_2_series`: the factor `2`
from the inner derivative cancels the `/2` in the normalisation, which is exactly
why this normalisation of the Lobachevsky function is the standard one. -/
theorem hasDerivAt_Lob {t : ℝ} (h0 : 0 < t) (h1 : t < π) :
    HasDerivAt QOU.Archimedean.Lob (-Real.log (2 * Real.sin t)) t := by
  have hinner : HasDerivAt (fun s : ℝ => 2 * s) 2 t := by
    simpa using (hasDerivAt_id t).const_mul (2 : ℝ)
  have hout := QOU.Knot.hasDerivAt_Cl_2_series (θ := 2 * t)
    (by linarith) (by linarith)
  have hcomp : HasDerivAt (fun s : ℝ => QOU.Archimedean.Cl_2 (2 * s))
      (-Real.log (2 * Real.sin (2 * t / 2)) * 2) t := hout.comp t hinner
  rw [show 2 * t / 2 = t by ring] at hcomp
  have h2 := hcomp.div_const 2
  rw [show -Real.log (2 * Real.sin t) * 2 / 2 = -Real.log (2 * Real.sin t) by ring] at h2
  show HasDerivAt (fun s : ℝ => QOU.Archimedean.Cl_2 (2 * s) / 2) _ t
  exact h2

/-- `d/dt (−log(2 sin t)) = −cot t` on `(0, π)`. -/
theorem hasDerivAt_neg_log_two_sin {t : ℝ} (h0 : 0 < t) (h1 : t < π) :
    HasDerivAt (fun s : ℝ => -Real.log (2 * Real.sin s))
      (-(Real.cos t / Real.sin t)) t := by
  have hs : Real.sin t ≠ 0 := (Real.sin_pos_of_pos_of_lt_pi h0 h1).ne'
  have h2s : 2 * Real.sin t ≠ 0 := by
    simpa using mul_ne_zero (by norm_num : (2:ℝ) ≠ 0) hs
  have hsin : HasDerivAt (fun s : ℝ => 2 * Real.sin s) (2 * Real.cos t) t :=
    (Real.hasDerivAt_sin t).const_mul 2
  have hlog := (Real.hasDerivAt_log h2s).comp t hsin
  -- `(2 cos t) / (2 sin t) = cos t / sin t`
  have hval : (2 * Real.sin t)⁻¹ * (2 * Real.cos t) = Real.cos t / Real.sin t := by
    field_simp
  rw [hval] at hlog
  exact hlog.neg

/-- **`Λ″(t) = −cot t` on `(0, π)`** — bean `qou-mlgp` Gap 2, the analytic input
`qou-krvm` (iv) was missing.

Together with `cot_quadratic_pos` this says: the Hessian of `Λ(α)+Λ(β)+Λ(γ)` is
`diag(−cot α, −cot β, −cot γ)`, and it is negative definite on the tangent space
of `α+β+γ = π`.  That is Rivin concavity for one ideal tetrahedron.

⚠ Read the sign, and do not generalise it: `−cot` is negative on `(0, π/2)` and
**positive** on `(π/2, π)`, so `Λ` is concave on the first and **convex** on the
second.  The concavity is a property of the constrained sum, never of `Λ`. -/
theorem hasDerivAt_deriv_Lob {t : ℝ} (h0 : 0 < t) (h1 : t < π) :
    HasDerivAt (deriv QOU.Archimedean.Lob) (-Real.cot t) t := by
  have hev : deriv QOU.Archimedean.Lob
      =ᶠ[nhds t] fun s : ℝ => -Real.log (2 * Real.sin s) := by
    filter_upwards [Ioo_mem_nhds h0 h1] with s hs
    exact (hasDerivAt_Lob hs.1 hs.2).deriv
  have hcot : -Real.cot t = -(Real.cos t / Real.sin t) := by
    rw [Real.cot_eq_cos_div_sin]
  rw [hcot]
  exact (hasDerivAt_neg_log_two_sin h0 h1).congr_of_eventuallyEq hev

/-- The Hessian entry, in the form `cot_quadratic_pos` consumes: the second
derivative of `Λ` at an angle is `−cot`, so `−Λ″ = cot`. -/
theorem deriv_deriv_Lob {t : ℝ} (h0 : 0 < t) (h1 : t < π) :
    deriv (deriv QOU.Archimedean.Lob) t = -Real.cot t :=
  (hasDerivAt_deriv_Lob h0 h1).deriv

/-! ### Rivin concavity for one ideal tetrahedron, assembled

Bean `qou-mlgp` Gap 3, for a single tetrahedron.  The two halves above combine:
`Λ″ = −cot` supplies the Hessian, `cot_quadratic_pos` supplies its sign.

The statement is concavity **along a line in the angle simplex**.  That is not a
weakening — strict concavity on a convex set *is* strict concavity along every
segment — and it is what makes the whole thing one-variable, so Mathlib's
`strictConcaveOn_of_deriv2_neg'` applies directly.

The mechanism worth naming: the tangent condition `u + v + w = 0` is exactly
what keeps the three angles summing to `π` all along the line,

    `(α+tu) + (β+tv) + (γ+tw) = (α+β+γ) + t(u+v+w) = π + 0 = π`,

so `cot_quadratic_pos` applies at *every* point of the line, not just at `t = 0`. -/

/-- The tetrahedron volume `Λ(α)+Λ(β)+Λ(γ)` restricted to the line
`t ↦ (α+tu, β+tv, γ+tw)`. -/
noncomputable def tetVolLine (α β γ u v w t : ℝ) : ℝ :=
  QOU.Archimedean.Lob (α + t * u) + QOU.Archimedean.Lob (β + t * v)
    + QOU.Archimedean.Lob (γ + t * w)

/-- The admissible parameters: those keeping all three angles positive.  Given
`α+β+γ = π` and `u+v+w = 0` this also forces each angle `< π`. -/
def tetLineDomain (α β γ u v w : ℝ) : Set ℝ :=
  {t | 0 < α + t * u ∧ 0 < β + t * v ∧ 0 < γ + t * w}

theorem convex_tetLineDomain (α β γ u v w : ℝ) :
    Convex ℝ (tetLineDomain α β γ u v w) := by
  intro x hx y hy a b ha hb hab
  obtain ⟨hx1, hx2, hx3⟩ := hx
  obtain ⟨hy1, hy2, hy3⟩ := hy
  -- a convex combination of two positives is positive, because `a + b = 1`
  -- means they cannot both vanish
  have key : ∀ p q : ℝ, 0 < p → 0 < q → 0 < a * p + b * q := by
    intro p q hp hq
    rcases ha.lt_or_eq with h | h
    · exact add_pos_of_pos_of_nonneg (mul_pos h hp) (mul_nonneg hb hq.le)
    · have hb1 : b = 1 := by linarith
      rw [← h, hb1, zero_mul, one_mul, zero_add]; exact hq
  simp only [tetLineDomain, Set.mem_setOf_eq, smul_eq_mul]
  refine ⟨?_, ?_, ?_⟩
  · have h := key _ _ hx1 hy1
    have e : α + (a * x + b * y) * u = a * (α + x * u) + b * (α + y * u) := by
      linear_combination (-α) * hab
    rw [e]; exact h
  · have h := key _ _ hx2 hy2
    have e : β + (a * x + b * y) * v = a * (β + x * v) + b * (β + y * v) := by
      linear_combination (-β) * hab
    rw [e]; exact h
  · have h := key _ _ hx3 hy3
    have e : γ + (a * x + b * y) * w = a * (γ + x * w) + b * (γ + y * w) := by
      linear_combination (-γ) * hab
    rw [e]; exact h

/-- Along the line, the three angles still sum to `π`. -/
theorem tetLine_sum (α β γ u v w t : ℝ) (hsum : α + β + γ = π) (htan : u + v + w = 0) :
    (α + t * u) + (β + t * v) + (γ + t * w) = π := by
  have : t * u + t * v + t * w = t * (u + v + w) := by ring
  rw [htan, mul_zero] at this; linarith

/-- First derivative along the line. -/
theorem hasDerivAt_tetVolLine {α β γ u v w t : ℝ}
    (hsum : α + β + γ = π) (htan : u + v + w = 0)
    (ht : t ∈ tetLineDomain α β γ u v w) :
    HasDerivAt (tetVolLine α β γ u v w)
      (-Real.log (2 * Real.sin (α + t * u)) * u
        + -Real.log (2 * Real.sin (β + t * v)) * v
        + -Real.log (2 * Real.sin (γ + t * w)) * w) t := by
  obtain ⟨h1, h2, h3⟩ := ht
  have hs := tetLine_sum α β γ u v w t hsum htan
  have b1 : α + t * u < π := by linarith
  have b2 : β + t * v < π := by linarith
  have b3 : γ + t * w < π := by linarith
  have i1 : HasDerivAt (fun s : ℝ => α + s * u) u t := by
    simpa using ((hasDerivAt_id t).mul_const u).const_add α
  have i2 : HasDerivAt (fun s : ℝ => β + s * v) v t := by
    simpa using ((hasDerivAt_id t).mul_const v).const_add β
  have i3 : HasDerivAt (fun s : ℝ => γ + s * w) w t := by
    simpa using ((hasDerivAt_id t).mul_const w).const_add γ
  exact (((hasDerivAt_Lob h1 b1).comp t i1).add
    ((hasDerivAt_Lob h2 b2).comp t i2)).add ((hasDerivAt_Lob h3 b3).comp t i3)

/-- **The second derivative along the line is `−cotQuadratic`, hence negative.**
This is where `Λ″ = −cot` and `cot_quadratic_pos` meet. -/
theorem deriv2_tetVolLine_neg {α β γ u v w t : ℝ}
    (hsum : α + β + γ = π) (htan : u + v + w = 0) (hne : ¬(u = 0 ∧ v = 0))
    (ht : t ∈ tetLineDomain α β γ u v w) :
    deriv^[2] (tetVolLine α β γ u v w) t < 0 := by
  obtain ⟨h1, h2, h3⟩ := ht
  have hs := tetLine_sum α β γ u v w t hsum htan
  have b1 : α + t * u < π := by linarith
  have b2 : β + t * v < π := by linarith
  have b3 : γ + t * w < π := by linarith
  -- the domain is open, so `deriv` agrees with the formula near `t`
  have hopen : IsOpen (tetLineDomain α β γ u v w) := by
    have : tetLineDomain α β γ u v w
        = (fun s : ℝ => α + s * u) ⁻¹' (Set.Ioi 0)
          ∩ ((fun s : ℝ => β + s * v) ⁻¹' (Set.Ioi 0)
            ∩ (fun s : ℝ => γ + s * w) ⁻¹' (Set.Ioi 0)) := by
      ext s; simp [tetLineDomain]
    rw [this]
    exact ((isOpen_Ioi.preimage (by fun_prop)).inter
      ((isOpen_Ioi.preimage (by fun_prop)).inter (isOpen_Ioi.preimage (by fun_prop))))
  have hev : deriv (tetVolLine α β γ u v w)
      =ᶠ[nhds t] fun s : ℝ => -Real.log (2 * Real.sin (α + s * u)) * u
        + -Real.log (2 * Real.sin (β + s * v)) * v
        + -Real.log (2 * Real.sin (γ + s * w)) * w := by
    filter_upwards [hopen.mem_nhds ⟨h1, h2, h3⟩] with s hs'
    exact (hasDerivAt_tetVolLine hsum htan hs').deriv
  -- differentiate the formula
  have i1 : HasDerivAt (fun s : ℝ => α + s * u) u t := by
    simpa using ((hasDerivAt_id t).mul_const u).const_add α
  have i2 : HasDerivAt (fun s : ℝ => β + s * v) v t := by
    simpa using ((hasDerivAt_id t).mul_const v).const_add β
  have i3 : HasDerivAt (fun s : ℝ => γ + s * w) w t := by
    simpa using ((hasDerivAt_id t).mul_const w).const_add γ
  have d1 := ((hasDerivAt_neg_log_two_sin h1 b1).comp t i1).mul_const u
  have d2 := ((hasDerivAt_neg_log_two_sin h2 b2).comp t i2).mul_const v
  have d3 := ((hasDerivAt_neg_log_two_sin h3 b3).comp t i3).mul_const w
  have hd2 : HasDerivAt (deriv (tetVolLine α β γ u v w))
      (-(Real.cos (α + t * u) / Real.sin (α + t * u)) * u * u
        + -(Real.cos (β + t * v) / Real.sin (β + t * v)) * v * v
        + -(Real.cos (γ + t * w) / Real.sin (γ + t * w)) * w * w) t :=
    ((d1.add d2).add d3).congr_of_eventuallyEq hev
  have hq := cot_quadratic_pos (α := α + t * u) (β := β + t * v) (γ := γ + t * w)
    h1 h2 h3 hs (by linarith : u + v + w = 0) hne
  unfold cotQuadratic at hq
  have : deriv^[2] (tetVolLine α β γ u v w) t
      = -(Real.cos (α + t * u) / Real.sin (α + t * u) * u ^ 2
        + Real.cos (β + t * v) / Real.sin (β + t * v) * v ^ 2
        + Real.cos (γ + t * w) / Real.sin (γ + t * w) * w ^ 2) := by
    rw [Function.iterate_succ, Function.iterate_one, Function.comp_apply, hd2.deriv]; ring
  rw [this]
  linarith

/-- **RIVIN CONCAVITY FOR ONE IDEAL TETRAHEDRON.**

`Λ(α)+Λ(β)+Λ(γ)` is *strictly concave* along every line in the angle simplex —
i.e. along every direction `(u,v,w)` with `u+v+w = 0` that is not zero.

Since strict concavity on a convex set is exactly strict concavity along every
segment, this is Rivin's theorem for a single tetrahedron. -/
theorem strictConcaveOn_tetVolLine {α β γ u v w : ℝ}
    (hsum : α + β + γ = π) (htan : u + v + w = 0) (hne : ¬(u = 0 ∧ v = 0)) :
    StrictConcaveOn ℝ (tetLineDomain α β γ u v w) (tetVolLine α β γ u v w) := by
  refine strictConcaveOn_of_deriv2_neg' (convex_tetLineDomain α β γ u v w) ?_
    (fun t ht => deriv2_tetVolLine_neg hsum htan hne ht)
  intro t ht
  exact ((hasDerivAt_tetVolLine hsum htan ht).continuousAt).continuousWithinAt

end QOU.Knot.Rivin
