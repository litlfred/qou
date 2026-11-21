import Mathlib.Analysis.Meromorphic.Order
import Mathlib.Analysis.Analytic.IsolatedZeros
import Mathlib.Analysis.SpecialFunctions.Complex.Analytic
import Mathlib.Analysis.SpecialFunctions.Complex.LogDeriv
import Mathlib.Algebra.Ring.Periodic

/-!
# QOU.Mathlib.EllipticAnnulusDescent — step 1 of Liouville's third theorem

Bean `qou-z4jb` (owner ruling 2026-11-20 on #8526, option 3). The planned proof of
`QOU.Mathlib.EllipticDivisorDegree.elliptic_divisor_degree_zero` pulls an elliptic
function back along `w = exp (2πi z / ω₁)`, which turns the `ω₁`-periodicity into
single-valuedness on `ℂ*` and the `ω₂`-periodicity into invariance under the
dilation `w ↦ p w`, `p = exp (2πi ω₂/ω₁)`. The divisor sum over a fundamental cell
then becomes the zero-minus-pole count on the annulus `R < |w| < |p| R`, which the
annulus argument principle equates to a difference of two circle integrals of
`logDeriv`, and the dilation invariance makes that difference `0`.

This file is the **descent** half, all sorry-free:

* `meromorphicOrderAt_comp_of_deriv_ne_zero` — the meromorphic order is invariant
  under a local biholomorphism (`φ` analytic, `φ' x ≠ 0`). Mathlib v4.24.0 has
  `MeromorphicAt.comp_analyticAt` but no order statement; the corpus had only the
  translation case.
* `exists_local_log` — an analytic local logarithm at every `w₀ ≠ 0`.
* `annulusPullback`, with `annulusPullback_eventuallyEq` (branch independence for
  `ω₁`-periodic `f`), `annulusPullback_meromorphicAt_order` (meromorphy on `ℂ*` and
  `ord_{w₀} g = ord_{(ω₁/2πi) log w₀} f`), and `annulusPullback_mul`
  (`g (p w) = g w`).

Still to do (tracked on `qou-z4jb`): the annulus argument principle with `ℤ`
orders for a meromorphic function on a neighbourhood of a closed annulus; the
winding identity from `annulusPullback_mul` via `circleIntegral_scale`; and the
transfer of the divisor sum between the annulus and the fundamental parallelogram.
-/

open Filter Topology

namespace QOU.Mathlib.EllipticAnnulusDescent

/-- An analytic map `φ` with `φ' x ≠ 0` factors as `φ z - φ x = (z - x) * h z`
with `h` analytic at `x` and `h x = φ' x ≠ 0` (namely `h = dslope φ x`). -/
theorem exists_sub_eq_mul_of_deriv_ne_zero {φ : ℂ → ℂ} {x : ℂ}
    (hφ : AnalyticAt ℂ φ x) (hd : deriv φ x ≠ 0) :
    ∃ h : ℂ → ℂ, AnalyticAt ℂ h x ∧ h x ≠ 0 ∧ ∀ z, φ z - φ x = (z - x) * h z := by
  obtain ⟨p, hp⟩ := hφ
  refine ⟨dslope φ x, hp.has_fpower_series_dslope_fslope.analyticAt, ?_, ?_⟩
  · rwa [dslope_same]
  · intro z; rw [← smul_eq_mul, sub_smul_dslope]

/-- Such a `φ` maps a punctured neighbourhood of `x` into a punctured
neighbourhood of `φ x`. -/
theorem tendsto_nhdsNE_of_deriv_ne_zero {φ : ℂ → ℂ} {x : ℂ}
    (hφ : AnalyticAt ℂ φ x) (hd : deriv φ x ≠ 0) :
    Tendsto φ (𝓝[≠] x) (𝓝[≠] (φ x)) := by
  obtain ⟨h, han, hne, heq⟩ := exists_sub_eq_mul_of_deriv_ne_zero hφ hd
  refine tendsto_nhdsWithin_iff.mpr ⟨hφ.continuousAt.tendsto.mono_left nhdsWithin_le_nhds, ?_⟩
  have hev : ∀ᶠ z in 𝓝 x, h z ≠ 0 := han.continuousAt.eventually_ne hne
  filter_upwards [nhdsWithin_le_nhds hev, self_mem_nhdsWithin] with z hz hzx
  have : φ z - φ x ≠ 0 := by
    rw [heq z]; exact mul_ne_zero (sub_ne_zero.mpr hzx) hz
  exact sub_ne_zero.mp this

/-- **The meromorphic order is invariant under a local biholomorphism.** If `f`
is meromorphic at `φ x`, `φ` is analytic at `x` and `φ' x ≠ 0`, then
`ord_x (f ∘ φ) = ord_{φ x} f`. -/
theorem meromorphicOrderAt_comp_of_deriv_ne_zero {f φ : ℂ → ℂ} {x : ℂ}
    (hf : MeromorphicAt f (φ x)) (hφ : AnalyticAt ℂ φ x) (hd : deriv φ x ≠ 0) :
    meromorphicOrderAt (f ∘ φ) x = meromorphicOrderAt f (φ x) := by
  have hT := tendsto_nhdsNE_of_deriv_ne_zero hφ hd
  have hfc : MeromorphicAt (f ∘ φ) x := hf.comp_analyticAt hφ
  cases hn : meromorphicOrderAt f (φ x) with
  | top =>
    rw [meromorphicOrderAt_eq_top_iff] at hn ⊢
    exact hT.eventually hn
  | coe n =>
    obtain ⟨u, hu, hu0, hfu⟩ := (meromorphicOrderAt_eq_int_iff hf).mp hn
    obtain ⟨h, han, hne, heq⟩ := exists_sub_eq_mul_of_deriv_ne_zero hφ hd
    rw [meromorphicOrderAt_eq_int_iff hfc]
    refine ⟨fun z => h z ^ n * u (φ z), ?_, ?_, ?_⟩
    · exact (han.zpow hne).mul (hu.comp_of_eq hφ rfl)
    · exact mul_ne_zero (zpow_ne_zero _ hne) hu0
    · filter_upwards [hT.eventually hfu] with z hz
      simp only [Function.comp_apply, hz, heq z, smul_eq_mul, mul_zpow]
      ring

open Complex Real

/-- **A local logarithm at every nonzero point.** For `w₀ ≠ 0` there is `ℓ`,
analytic at `w₀` with `ℓ' w₀ = w₀⁻¹`, such that `exp (ℓ w) = w` near `w₀`.
On the slit plane `ℓ = log`; otherwise `ℓ w = log (-w) + π i`. -/
theorem exists_local_log {w₀ : ℂ} (hw₀ : w₀ ≠ 0) :
    ∃ ℓ : ℂ → ℂ, AnalyticAt ℂ ℓ w₀ ∧ HasDerivAt ℓ w₀⁻¹ w₀ ∧
      ∀ᶠ w in 𝓝 w₀, exp (ℓ w) = w := by
  have hev : ∀ᶠ w in 𝓝 w₀, w ≠ 0 := isOpen_ne.mem_nhds hw₀
  rcases mem_slitPlane_or_neg_mem_slitPlane hw₀ with h | h
  · refine ⟨log, analyticAt_clog h, hasDerivAt_log h, ?_⟩
    filter_upwards [hev] with w hw using exp_log hw
  · refine ⟨fun w => log (-w) + π * I, ?_, ?_, ?_⟩
    · exact ((analyticAt_clog h).comp_of_eq analyticAt_id.neg rfl).add analyticAt_const
    · have h1 : HasDerivAt (fun w : ℂ => -w) (-1) w₀ := (hasDerivAt_id w₀).neg
      have h2 := ((hasDerivAt_log h).comp w₀ h1).add_const (π * I : ℂ)
      convert h2 using 1
      field_simp
    · filter_upwards [hev] with w hw
      rw [Complex.exp_add, exp_log (neg_ne_zero.mpr hw), exp_pi_mul_I]; ring

/-- The annulus pull-back of `f` along `w = exp (2πi z / ω₁)`:
`annulusPullback f ω₁ w = f ((ω₁ / (2πi)) · log w)`. For `ω₁`-periodic `f`
this does not depend on the branch of `log` (`annulusPullback_eventuallyEq`). -/
noncomputable def annulusPullback (f : ℂ → ℂ) (ω₁ : ℂ) (w : ℂ) : ℂ :=
  f (ω₁ / (2 * π * I) * log w)

/-- **Branch independence.** Near any `w₀ ≠ 0`, for `ω₁`-periodic `f`, the
pull-back agrees with `f ∘ (c · ℓ)` for the local logarithm `ℓ` at `w₀`,
`c = ω₁ / (2πi)`. -/
theorem annulusPullback_eventuallyEq {f : ℂ → ℂ} {ω₁ : ℂ}
    (hper : Function.Periodic f ω₁) {ℓ : ℂ → ℂ} {w₀ : ℂ} (hw₀ : w₀ ≠ 0)
    (hℓ : ∀ᶠ w in 𝓝 w₀, exp (ℓ w) = w) :
    annulusPullback f ω₁ =ᶠ[𝓝 w₀] fun w => f (ω₁ / (2 * π * I) * ℓ w) := by
  have hev : ∀ᶠ w in 𝓝 w₀, w ≠ 0 := isOpen_ne.mem_nhds hw₀
  filter_upwards [hℓ, hev] with w hw hw0
  obtain ⟨n, hn⟩ := exp_eq_exp_iff_exists_int.mp ((exp_log hw0).trans hw.symm)
  have h2 : (2 * (π : ℂ) * I) ≠ 0 := by simp [Real.pi_ne_zero, I_ne_zero]
  have : ω₁ / (2 * π * I) * log w = ω₁ / (2 * π * I) * ℓ w + (n : ℤ) * ω₁ := by
    rw [hn]; field_simp
  rw [annulusPullback, this, (hper.int_mul n) _]

private theorem two_pi_I_ne_zero : (2 * (π : ℂ) * I) ≠ 0 := by
  simp [Real.pi_ne_zero, I_ne_zero]

/-- `c · log w₀` and `c · ℓ w₀` differ by an integer multiple of `ω₁` whenever
`exp (ℓ w₀) = w₀`, `c = ω₁ / (2πi)`. -/
theorem exists_int_log_eq {ω₁ w₀ : ℂ} {ℓ : ℂ → ℂ} (hw₀ : w₀ ≠ 0)
    (hℓ : exp (ℓ w₀) = w₀) :
    ∃ n : ℤ, ω₁ / (2 * π * I) * log w₀ = ω₁ / (2 * π * I) * ℓ w₀ + n * ω₁ := by
  obtain ⟨n, hn⟩ := exp_eq_exp_iff_exists_int.mp ((exp_log hw₀).trans hℓ.symm)
  have h2 := two_pi_I_ne_zero
  exact ⟨n, by rw [hn]; field_simp⟩

/-- **Meromorphy and order transfer to the annulus.** For `f` meromorphic on
`ℂ` and `ω₁`-periodic (`ω₁ ≠ 0`), the pull-back is meromorphic at every
`w₀ ≠ 0`, and its order there equals the order of `f` at `(ω₁/2πi) · log w₀`. -/
theorem annulusPullback_meromorphicAt_order {f : ℂ → ℂ} {ω₁ : ℂ} (hω : ω₁ ≠ 0)
    (hmero : ∀ z, MeromorphicAt f z) (hper : Function.Periodic f ω₁)
    {w₀ : ℂ} (hw₀ : w₀ ≠ 0) :
    MeromorphicAt (annulusPullback f ω₁) w₀ ∧
      meromorphicOrderAt (annulusPullback f ω₁) w₀
        = meromorphicOrderAt f (ω₁ / (2 * π * I) * log w₀) := by
  obtain ⟨ℓ, hℓan, hℓd, hℓexp⟩ := exists_local_log hw₀
  set c : ℂ := ω₁ / (2 * π * I) with hc
  have hc0 : c ≠ 0 := div_ne_zero hω two_pi_I_ne_zero
  set φ : ℂ → ℂ := fun w => c * ℓ w with hφdef
  have hφ : AnalyticAt ℂ φ w₀ := analyticAt_const.mul hℓan
  have hφd : deriv φ w₀ ≠ 0 := by
    rw [((hℓd.const_mul c)).deriv]
    exact mul_ne_zero hc0 (inv_ne_zero hw₀)
  have heq : annulusPullback f ω₁ =ᶠ[𝓝 w₀] f ∘ φ :=
    annulusPullback_eventuallyEq hper hw₀ hℓexp
  have hmc : MeromorphicAt (f ∘ φ) w₀ := (hmero _).comp_analyticAt hφ
  refine ⟨hmc.congr (heq.symm.filter_mono nhdsWithin_le_nhds), ?_⟩
  rw [meromorphicOrderAt_congr (heq.filter_mono nhdsWithin_le_nhds),
    meromorphicOrderAt_comp_of_deriv_ne_zero (hmero _) hφ hφd]
  obtain ⟨n, hn⟩ := exists_int_log_eq (ω₁ := ω₁) hw₀ hℓexp.self_of_nhds
  rw [hn]
  -- order is invariant under translation by a period
  have hfun : f ∘ (fun z => z + n * ω₁) = f := funext fun z => (hper.int_mul n) z
  have hd : deriv (fun z : ℂ => z + n * ω₁) (φ w₀) ≠ 0 := by
    rw [deriv_add_const, deriv_id'']; exact one_ne_zero
  have := meromorphicOrderAt_comp_of_deriv_ne_zero (φ := fun z : ℂ => z + n * ω₁)
    (x := φ w₀) (hmero (φ w₀ + n * ω₁)) (analyticAt_id.add analyticAt_const) hd
  rw [hfun] at this
  exact this

/-- **The second period becomes a dilation.** With `p = exp (2πi ω₂/ω₁)`,
the pull-back of a doubly periodic `f` satisfies `g (p w) = g w` for `w ≠ 0`. -/
theorem annulusPullback_mul {f : ℂ → ℂ} {ω₁ ω₂ : ℂ} (hω : ω₁ ≠ 0)
    (hper₁ : Function.Periodic f ω₁) (hper₂ : Function.Periodic f ω₂)
    {w : ℂ} (hw : w ≠ 0) :
    annulusPullback f ω₁ (exp (2 * π * I * (ω₂ / ω₁)) * w) = annulusPullback f ω₁ w := by
  have hpw : exp (2 * π * I * (ω₂ / ω₁)) * w ≠ 0 := mul_ne_zero (exp_ne_zero _) hw
  have hexp : exp (log (exp (2 * π * I * (ω₂ / ω₁)) * w))
      = exp (2 * π * I * (ω₂ / ω₁) + log w) := by
    rw [exp_log hpw, Complex.exp_add, exp_log hw]
  obtain ⟨n, hn⟩ := exp_eq_exp_iff_exists_int.mp hexp
  have h2 := two_pi_I_ne_zero
  have : ω₁ / (2 * π * I) * log (exp (2 * π * I * (ω₂ / ω₁)) * w)
      = ω₁ / (2 * π * I) * log w + ω₂ + n * ω₁ := by
    rw [hn]; field_simp; ring
  rw [annulusPullback, annulusPullback, this, (hper₁.int_mul n) _, hper₂]

end QOU.Mathlib.EllipticAnnulusDescent
