/-
  H4-4 (reduced form): the ORTHOSCHEME BASE INTEGRAL is `½Λ(ψ)`.

  This is `qou-w3eg` H4-4, in the one-dimensional form Milnor's computation
  actually reduces to, together with the bridge that makes `Λ` usable as an
  antiderivative at all.

  WHERE THIS SITS.  H4-2 (`HyperbolicVolumeFubini`) collapsed the solid to
  Milnor's two-dimensional base integral

      Vol(chimney T R)  =  ∫∫_T dA / (2(R² − x² − y²)).

  Milnor evaluates that by cutting the inscribed triangle at the circumcentre
  into six right triangles and integrating each in polar coordinates.  For the
  right triangle with angle `ψ` AT THE CIRCUMCENTRE, the radial integral
  `∫₀^{r(φ)} r dr / (2(1 − r²)) = −¼ log(1 − r(φ)²)` is elementary, and with
  `r(φ) = cos ψ / cos φ` the remaining angular integrand is

      −¼ · log( (cos²φ − cos²ψ) / cos²φ ).

  `integral_orthoscheme` below evaluates that integral and lands on `½Λ(ψ)` —
  the value Milnor's Appendix reports.  So this file is H4-4's analytic core,
  stated purely as a one-dimensional integral identity.

  WHAT IS STILL MISSING FOR H4-3, AND IT IS NOT SMALL.  The polar-coordinate
  reduction — that the two-dimensional integral over the right triangle IS this
  one-dimensional integral — is NOT proved here.  So this file does not close
  H4-3, and no theorem below mentions a region, a triangle, or a volume.  What
  is proved is an identity between a real integral and `Λ`.

  THE THREE PIECES.

  1. **`Λ` is the primitive of `−log(2 sin)`** (`integral_neg_log_two_sin`).
     `LobachevskyDerivative` (T1) proved `Λ' = −log(2 sin t)` POINTWISE on
     `(0,π)`; the integral form additionally needs (i) continuity of `Λ` on the
     CLOSED interval, so the fundamental theorem applies up to the endpoints
     where `Λ'` blows up, and (ii) honest integrability of `log(2 sin)` across
     those endpoints.  Mathlib supplies the latter unconditionally
     (`intervalIntegrable_log_sin`), so the log singularity at `0` and `π` — the
     one place this could have failed — costs an `a.e.` rewrite, not a proof.
     This is the statement `qou-idvt` T1 promised as "`Λ` is the primitive
     `Λ(x) = −∫₀ˣ log|2 sin t| dt`" but which existed only in derivative form.

  2. **The trig factorization** `cos²φ − cos²ψ = sin(ψ+φ)·sin(ψ−φ)`.  It is what
     turns the orthoscheme integrand into three `log sin` integrals — i.e. the
     reason `Λ` appears at all.

  3. **The evaluation** (`integral_orthoscheme`).  Three translated `log sin`
     integrals, then Milnor's duplication identity `Λ(2a) = 2Λ(a) + 2Λ(a+π/2)`
     (already proved in `LobachevskyMaximum`) collapses the result to `½Λ(ψ)`.
     Every `log 2` from the `2 sin` normalization cancels — which is the
     arithmetic check that the normalization was right.

  SCOPE — what is NOT claimed.

  * **No geometry.**  No region, no triangle, no tetrahedron, no dihedral angle,
    no hyperbolic volume.  `ψ` here is a real number in `(0, π/2)`, not "the
    angle at the circumcentre" — that identification is H4-3's job.
  * **No assembly.**  That six such pieces sum to `Λ(α)+Λ(β)+Λ(γ)` is H4-5 and
    is not proved.  The pairing is only meaningful once H4-3 says which `ψ` each
    piece carries.
  * **The obtuse case is untouched** and remains the flagged failure point of
    the tier: Milnor subdivides from the circumcentre only "if all three angles
    are acute", and otherwise a piece enters with a MINUS sign (`qou-w3eg`).
    The hypothesis `ψ < π/2` below is exactly where that restriction will bite —
    it is what makes `cos ψ > 0`, i.e. the circumcentre-to-edge foot land at
    positive distance on the correct side.
  * **Nothing wired, nothing axiomatised.**  The `qou-5gai` GUARD is intact:
    `volChart` stays *defined* as the Λ-sum and labelled analytic; no class
    stands in for H4.

  Archimedean (ℝ): `log`, `sin`, `cos`, Lebesgue integration, ordering — §7c.

  -- Ref: [milnor1982] Appendix (the orthoscheme computation, value `Λ(a)/2`)
  -- Ref: [thurston1978] Ch. 7 (computation of volume)
  -- Ref: [leitner2026] beans qou-w3eg (H4-4), qou-5gai (H4), qou-idvt (T1/T2)
-/

import QOU.Archimedean.LobachevskyDerivative
import QOU.Archimedean.LobachevskyMaximum
import Mathlib.Analysis.SpecialFunctions.Integrals.LogTrigonometric

namespace QOU.Archimedean.HyperbolicVolume

open Real MeasureTheory intervalIntegral Set
open QOU.Archimedean QOU.Archimedean.IdealTetrahedronConcavity

/-! ### 1. `Λ` is the primitive of `−log(2 sin)`

T1 gave `Λ' = −log(2 sin t)` pointwise on the OPEN interval `(0,π)`.  Getting the
integral form across the closed interval is not bookkeeping: `Λ'` is unbounded at
both endpoints, so the fundamental theorem is applied in its
`hasDeriv_right_of_le` form (continuity on `[a,b]`, derivative on `(a,b)` only),
and the integrand's integrability has to be established rather than inherited
from continuity. -/

/-- The zero set of `sin` is null — it is contained in the countable set `πℤ`. -/
theorem measure_sin_eq_zero : volume {t : ℝ | Real.sin t = 0} = 0 := by
  have hsub : {t : ℝ | Real.sin t = 0} ⊆ Set.range (fun n : ℤ => (n : ℝ) * π) := by
    intro t ht
    obtain ⟨n, hn⟩ := Real.sin_eq_zero_iff.mp ht
    exact ⟨n, hn⟩
  exact measure_mono_null hsub ((Set.countable_range _).measure_zero volume)

/-- Almost every real has `sin t ≠ 0`.  This is what lets `log (2 sin t)` be
split as `log 2 + log (sin t)` under an integral, even though the splitting fails
pointwise exactly where `sin` vanishes. -/
theorem ae_sin_ne_zero : ∀ᵐ t : ℝ, Real.sin t ≠ 0 := by
  rw [MeasureTheory.ae_iff]
  simpa using measure_sin_eq_zero

/-- `log (2 sin ·)` is interval-integrable on ANY interval.

The log singularities at the zeros of `sin` are integrable; Mathlib proves this
for `log ∘ sin` (`intervalIntegrable_log_sin`) with no hypothesis on the
endpoints, and the constant `log 2` splits off almost everywhere. -/
theorem intervalIntegrable_log_two_sin (a b : ℝ) :
    IntervalIntegrable (fun t => Real.log (2 * Real.sin t)) volume a b := by
  have hbase : IntervalIntegrable (fun t => Real.log 2 + Real.log (Real.sin t)) volume a b :=
    (intervalIntegral.intervalIntegrable_const).add intervalIntegrable_log_sin
  have hae : ∀ᵐ t : ℝ, Real.log 2 + Real.log (Real.sin t) = Real.log (2 * Real.sin t) := by
    filter_upwards [ae_sin_ne_zero] with t ht
    exact (Real.log_mul two_ne_zero ht).symm
  exact ⟨hbase.1.congr (ae_restrict_of_ae hae), hbase.2.congr (ae_restrict_of_ae hae)⟩

/-- **`Λ` is the primitive of `−log(2 sin)`:**

    ∫_a^b −log(2 sin t) dt = Λ(b) − Λ(a)   for  0 ≤ a ≤ b ≤ π.

This is the integral form of T1's `hasDerivAt_Lob`, and the form in which `Λ` is
classically *defined*.  The endpoints are included: `Λ'` blows up at `0` and `π`,
so the fundamental theorem is used with the derivative required only on the open
interval, and the integrability across the singularity is
`intervalIntegrable_log_two_sin`. -/
theorem integral_neg_log_two_sin {a b : ℝ} (h0 : 0 ≤ a) (hab : a ≤ b) (hbπ : b ≤ π) :
    ∫ t in a..b, -Real.log (2 * Real.sin t) = Lob b - Lob a := by
  refine integral_eq_sub_of_hasDeriv_right_of_le hab continuous_Lob.continuousOn
    (fun x hx => ?_) ((intervalIntegrable_log_two_sin a b).neg)
  exact (hasDerivAt_Lob (lt_of_le_of_lt h0 hx.1) (lt_of_lt_of_le hx.2 hbπ)).hasDerivWithinAt

/-- **`Λ(x) = −∫₀ˣ log(2 sin t) dt` on `[0, π]`** — the classical definition of
the Lobachevsky function, recovered as a theorem from the `Cl₂` series
definition rather than assumed. -/
theorem Lob_eq_integral {x : ℝ} (h0 : 0 ≤ x) (hπ : x ≤ π) :
    Lob x = ∫ t in (0:ℝ)..x, -Real.log (2 * Real.sin t) := by
  rw [integral_neg_log_two_sin le_rfl h0 hπ]
  simp

/-- The `log sin` form, with the `log 2` from the normalization made explicit.
This is the shape the orthoscheme computation consumes three times. -/
theorem integral_log_sin_eq {a b : ℝ} (h0 : 0 ≤ a) (hab : a ≤ b) (hbπ : b ≤ π) :
    ∫ t in a..b, Real.log (Real.sin t) = Lob a - Lob b - (b - a) * Real.log 2 := by
  have hls : IntervalIntegrable (fun t => Real.log (Real.sin t)) volume a b :=
    intervalIntegrable_log_sin
  have hneg := integral_neg_log_two_sin h0 hab hbπ
  rw [intervalIntegral.integral_neg] at hneg
  have hsplit : ∫ t in a..b, Real.log (2 * Real.sin t)
      = ∫ t in a..b, (Real.log 2 + Real.log (Real.sin t)) := by
    refine intervalIntegral.integral_congr_ae ?_
    filter_upwards [ae_sin_ne_zero] with t ht _
    exact Real.log_mul two_ne_zero ht
  have hsplit2 : ∫ t in a..b, (Real.log 2 + Real.log (Real.sin t))
      = (b - a) * Real.log 2 + ∫ t in a..b, Real.log (Real.sin t) := by
    rw [intervalIntegral.integral_add intervalIntegral.intervalIntegrable_const hls,
      intervalIntegral.integral_const, smul_eq_mul]
  linarith [hneg, hsplit, hsplit2]

/-! ### 2. The trig factorization

The identity that makes `Λ` appear: the orthoscheme integrand's numerator is a
product of two sines, so its log is a sum of two `log sin` terms. -/

/-- `cos²φ − cos²ψ = sin(ψ+φ)·sin(ψ−φ)`. -/
theorem cos_sq_sub_cos_sq (ψ φ : ℝ) :
    Real.cos φ ^ 2 - Real.cos ψ ^ 2 = Real.sin (ψ + φ) * Real.sin (ψ - φ) := by
  have hψ := Real.sin_sq_add_cos_sq ψ
  have hφ := Real.sin_sq_add_cos_sq φ
  rw [Real.sin_add, Real.sin_sub]
  linear_combination (-(Real.cos φ ^ 2)) * hψ + (Real.cos ψ ^ 2) * hφ

/-! ### 3. The orthoscheme value

Milnor's Appendix reports the value `Λ(a)/2` for the orthoscheme; this is that
computation, in the reduced one-dimensional form. -/

/-- **The three-log decomposition of the orthoscheme integrand**, valid pointwise
on the OPEN interval `0 ≤ φ < ψ < π/2`.

It fails at `φ = ψ` — there the left side is `log 0 = 0` by Lean's convention
while the right side is not — which is exactly why the integral identity below
needs an `a.e.` rewrite and why the integrability statement is about `Ioo`. -/
theorem log_orthoscheme_eq {ψ φ : ℝ} (hψ : ψ < π / 2) (hφ0 : 0 ≤ φ) (hφψ : φ < ψ) :
    Real.log ((Real.cos φ ^ 2 - Real.cos ψ ^ 2) / Real.cos φ ^ 2)
      = Real.log (Real.sin (ψ + φ)) + Real.log (Real.sin (ψ - φ))
        - 2 * Real.log (Real.cos φ) := by
  have hπ : 0 < π := Real.pi_pos
  have hcos : 0 < Real.cos φ := Real.cos_pos_of_mem_Ioo ⟨by linarith, by linarith⟩
  have hs1 : 0 < Real.sin (ψ + φ) :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  have hs2 : 0 < Real.sin (ψ - φ) :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  rw [cos_sq_sub_cos_sq ψ φ,
    Real.log_div (by positivity) (by positivity),
    Real.log_mul (ne_of_gt hs1) (ne_of_gt hs2),
    show Real.cos φ ^ 2 = Real.cos φ ^ (2 : ℕ) from rfl, Real.log_pow]
  push_cast
  ring

/-! The three translated integrands, and their integrability.  Each is a
translate or reflection of `log ∘ sin` or `log ∘ cos`, both of which Mathlib
integrates on any interval. -/

theorem intervalIntegrable_log_sin_add {ψ : ℝ} :
    IntervalIntegrable (fun φ => Real.log (Real.sin (ψ + φ))) volume 0 ψ := by
  have := (intervalIntegrable_log_sin (a := ψ) (b := 2 * ψ)).comp_add_left ψ
  simpa [Function.comp, two_mul] using this

theorem intervalIntegrable_log_sin_sub {ψ : ℝ} :
    IntervalIntegrable (fun φ => Real.log (Real.sin (ψ - φ))) volume 0 ψ := by
  have := (intervalIntegrable_log_sin (a := ψ) (b := 0)).comp_sub_left ψ
  simpa [Function.comp] using this

/-- **The orthoscheme integrand is integrable on the open interval `(0, ψ)`.**

Stated for `Ioo` rather than `Icc`/`Ioc` on purpose: the three-log decomposition
holds pointwise only where `φ < ψ` strictly, and `φ = ψ` is where the integrand
blows up.  This is what makes the improper integral in `integral_orthoscheme` a
real number rather than Lean's junk value. -/
theorem integrableOn_orthoscheme {ψ : ℝ} (hψ0 : 0 < ψ) (hψ : ψ < π / 2) :
    IntegrableOn
      (fun φ => (-(1/4 : ℝ)) * Real.log ((Real.cos φ ^ 2 - Real.cos ψ ^ 2) / Real.cos φ ^ 2))
      (Set.Ioo 0 ψ) volume := by
  have hthree : IntegrableOn (fun φ => (-(1/4 : ℝ)) *
      (Real.log (Real.sin (ψ + φ)) + Real.log (Real.sin (ψ - φ))
        - 2 * Real.log (Real.cos φ))) (Set.Ioo 0 ψ) volume := by
    have h : IntervalIntegrable (fun φ => (-(1/4 : ℝ)) *
        (Real.log (Real.sin (ψ + φ)) + Real.log (Real.sin (ψ - φ))
          - 2 * Real.log (Real.cos φ))) volume 0 ψ :=
      (((intervalIntegrable_log_sin_add.add intervalIntegrable_log_sin_sub).sub
        (intervalIntegrable_log_cos.const_mul 2)).const_mul _)
    exact ((intervalIntegrable_iff_integrableOn_Ioc_of_le hψ0.le).mp h).mono_set
      Set.Ioo_subset_Ioc_self
  refine hthree.congr_fun (fun φ hφ => ?_) measurableSet_Ioo
  rw [log_orthoscheme_eq hψ hφ.1.le hφ.2]

/-- **H4-4 (reduced) — the orthoscheme base integral is `½Λ(ψ)`:**

    ∫₀^ψ −¼ · log( (cos²φ − cos²ψ) / cos²φ ) dφ  =  ½ Λ(ψ)   for 0 < ψ < π/2.

The integrand is Milnor's angular integrand for the right triangle with angle
`ψ` at the circumcentre, after the elementary radial integration.  It is
unbounded at `φ = ψ` (where the base vertex meets the circle and the fibre mass
diverges — `fibreMass_eq_top`), so the identity is a genuine improper-integral
statement, and the integrability that makes it meaningful is
`intervalIntegrable_log_two_sin`, not continuity.

`ψ < π/2` is Milnor's acute hypothesis in local form: it is what puts `cos ψ > 0`
and therefore the foot of the circumcentre perpendicular at positive distance on
the correct side of the edge. -/
theorem integral_orthoscheme {ψ : ℝ} (hψ0 : 0 < ψ) (hψ : ψ < π / 2) :
    ∫ φ in (0:ℝ)..ψ,
        (-(1/4 : ℝ)) * Real.log ((Real.cos φ ^ 2 - Real.cos ψ ^ 2) / Real.cos φ ^ 2)
      = Lob ψ / 2 := by
  have hπ : 0 < π := Real.pi_pos
  have hA : IntervalIntegrable (fun φ => Real.log (Real.sin (ψ + φ))) volume 0 ψ :=
    intervalIntegrable_log_sin_add
  have hB : IntervalIntegrable (fun φ => Real.log (Real.sin (ψ - φ))) volume 0 ψ :=
    intervalIntegrable_log_sin_sub
  have hC : IntervalIntegrable (fun φ => Real.log (Real.cos φ)) volume 0 ψ :=
    intervalIntegrable_log_cos
  -- (a) rewrite the integrand as three log-sin/log-cos terms, valid off `φ = ψ`
  have hrw : ∫ φ in (0:ℝ)..ψ,
        (-(1/4 : ℝ)) * Real.log ((Real.cos φ ^ 2 - Real.cos ψ ^ 2) / Real.cos φ ^ 2)
      = ∫ φ in (0:ℝ)..ψ, (-(1/4 : ℝ)) *
          (Real.log (Real.sin (ψ + φ)) + Real.log (Real.sin (ψ - φ))
            - 2 * Real.log (Real.cos φ)) := by
    refine intervalIntegral.integral_congr_ae ?_
    have hne : ∀ᵐ φ : ℝ, φ ≠ ψ := by
      -- the exceptional point `φ = ψ` (where the base vertex meets the circle)
      -- is a single point, hence null
      rw [MeasureTheory.ae_iff]; simp
    filter_upwards [hne] with φ hφne hmem
    rw [Set.uIoc_of_le hψ0.le] at hmem
    obtain ⟨hφ0, hφψ⟩ := hmem
    rw [log_orthoscheme_eq hψ hφ0.le (lt_of_le_of_ne hφψ hφne)]
  rw [hrw, intervalIntegral.integral_const_mul,
    intervalIntegral.integral_sub (hA.add hB) (hC.const_mul 2),
    intervalIntegral.integral_add hA hB, intervalIntegral.integral_const_mul]
  -- (b) the three integrals, by translation/reflection onto `∫ log sin`
  have hA' : ∫ φ in (0:ℝ)..ψ, Real.log (Real.sin (ψ + φ))
      = Lob ψ - Lob (2 * ψ) - ψ * Real.log 2 := by
    have hshift : ∫ φ in (0:ℝ)..ψ, Real.log (Real.sin (ψ + φ))
        = ∫ u in (ψ)..(2 * ψ), Real.log (Real.sin u) := by
      have := intervalIntegral.integral_comp_add_left
        (fun u => Real.log (Real.sin u)) ψ (a := 0) (b := ψ)
      simpa [two_mul] using this
    rw [hshift, integral_log_sin_eq hψ0.le (by linarith) (by linarith)]
    ring
  have hB' : ∫ φ in (0:ℝ)..ψ, Real.log (Real.sin (ψ - φ))
      = -Lob ψ - ψ * Real.log 2 := by
    have hrefl : ∫ φ in (0:ℝ)..ψ, Real.log (Real.sin (ψ - φ))
        = ∫ u in (0:ℝ)..ψ, Real.log (Real.sin u) := by
      have := intervalIntegral.integral_comp_sub_left
        (fun u => Real.log (Real.sin u)) ψ (a := 0) (b := ψ)
      simpa using this
    rw [hrefl, integral_log_sin_eq le_rfl hψ0.le (by linarith)]
    simp
  have hC' : ∫ φ in (0:ℝ)..ψ, Real.log (Real.cos φ)
      = Lob (π / 2 - ψ) - ψ * Real.log 2 := by
    have hrefl : ∫ φ in (0:ℝ)..ψ, Real.log (Real.cos φ)
        = ∫ u in (π / 2 - ψ)..(π / 2), Real.log (Real.sin u) := by
      have := intervalIntegral.integral_comp_sub_left
        (fun u => Real.log (Real.sin u)) (π / 2) (a := 0) (b := ψ)
      simpa [Real.sin_pi_div_two_sub] using this
    rw [hrefl, integral_log_sin_eq (by linarith) (by linarith) (by linarith)]
    simp
  rw [hA', hB', hC']
  -- (c) Milnor's duplication identity collapses the result
  have hdup : Lob (2 * ψ) = 2 * Lob ψ + 2 * Lob (ψ + π / 2) := Lob_duplication ψ
  have hshift : Lob (ψ + π / 2) = -Lob (π / 2 - ψ) := by
    have h1 : Lob (ψ - π / 2 + π) = Lob (ψ - π / 2) := Lob_add_pi _
    have h2 : Lob (-(π / 2 - ψ)) = -Lob (π / 2 - ψ) := Lob_neg _
    rw [show ψ + π / 2 = ψ - π / 2 + π by ring, h1,
      show ψ - π / 2 = -(π / 2 - ψ) by ring, h2]
  rw [hshift] at hdup
  linarith

end QOU.Archimedean.HyperbolicVolume
