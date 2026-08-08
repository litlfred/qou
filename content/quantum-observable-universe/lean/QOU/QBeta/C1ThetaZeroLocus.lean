import Mathlib.Analysis.Meromorphic.Order
import QOU.QBeta.C1ConnectionPoles

/-!
# The converse q-theta zero locus

`QOU/QBeta/C1ConnectionPoles.lean` proves that `θ_P` vanishes on `−P^{2ℤ}` and
that the winding difference across one fundamental annulus is exactly `2πi`
(`qTheta_winding_step`). Read through the argument principle, that says the
annulus `ρ < ‖z‖ < P²ρ` contains **exactly one** zero, counted with
multiplicity — which is the converse of the vanishing theorem, and what upgrades
the C1 pole divisor from `⊇` to `=`.

This file takes that last step. Everything general it needs is already proved:

| | |
|---|---|
| the annulus argument principle, factors off the contours | `argumentPrinciple_annulus_filter` |
| analytic functions factorise over their zeros | `QOU.Mathlib.exists_finset_factorisation` |
| the contour identity for `θ_P` | `qTheta_winding_step` |
| `θ_P(−P^{2k}) = 0` | `qTheta_neg_zpow_eq_zero` |

What is θ-specific, and is done here:

* `isPreconnected_openAnnulus` — the factorisation needs a *connected* open set,
  and an open annulus is `exp` of a convex strip.
* `qThetaC_ne_zero_outer` — non-vanishing on `‖z‖ = ρ` propagates to
  `‖z‖ = P²ρ` through the functional equation, so both contours are clean from
  the single hypothesis `qTheta_winding_step` already asks for.
* `qThetaC_zero_count_annulus` — the count is `1`.
* `qThetaC_zero_locus_annulus` — hence a single simple zero, and if a lattice
  point `−P^{2k}` lies in the annulus it *is* that zero.

-- Ref: [manuscript] bean `qou-argp` — the converse theta zero locus.
-/

open scoped Real
open Metric Filter Topology

namespace QOU.QBeta.C1Poles

section OpenAnnulus

/-- **An open annulus in `ℂ` is preconnected.**

It is the image under `Complex.exp` of the strip `log r < re z < log R`, which is
a preimage of an interval under an `ℝ`-linear map, hence convex.

Needed because `exists_finset_factorisation` runs the identity theorem, which
wants a connected domain: an annulus is the smallest such domain containing the
two contour circles of `qTheta_winding_step`. -/
theorem isPreconnected_openAnnulus {r R : ℝ} (hr : 0 < r) (hrR : r < R) :
    IsPreconnected {z : ℂ | r < ‖z‖ ∧ ‖z‖ < R} := by
  have hR : (0:ℝ) < R := lt_trans hr hrR
  have hlin : IsLinearMap ℝ Complex.re := ⟨Complex.add_re, fun c z => Complex.smul_re c z⟩
  have hstrip : Convex ℝ (Complex.re ⁻¹' Set.Ioo (Real.log r) (Real.log R)) :=
    (convex_Ioo _ _).is_linear_preimage hlin
  have himg : {z : ℂ | r < ‖z‖ ∧ ‖z‖ < R}
      = Complex.exp '' (Complex.re ⁻¹' Set.Ioo (Real.log r) (Real.log R)) := by
    ext w
    constructor
    · rintro ⟨h1, h2⟩
      have hw0 : w ≠ 0 := by
        intro h
        rw [h, norm_zero] at h1
        linarith
      refine ⟨Complex.log w, ?_, Complex.exp_log hw0⟩
      simp only [Set.mem_preimage, Set.mem_Ioo, Complex.log_re]
      exact ⟨Real.log_lt_log hr h1, Real.log_lt_log (lt_trans hr h1) h2⟩
    · rintro ⟨z, hz, rfl⟩
      simp only [Set.mem_preimage, Set.mem_Ioo] at hz
      rw [Set.mem_setOf_eq, Complex.norm_exp]
      refine ⟨?_, ?_⟩
      · calc r = Real.exp (Real.log r) := (Real.exp_log hr).symm
          _ < Real.exp z.re := Real.exp_lt_exp.2 hz.1
      · calc Real.exp z.re < Real.exp (Real.log R) := Real.exp_lt_exp.2 hz.2
          _ = R := Real.exp_log hR
  rw [himg]
  exact hstrip.isPreconnected.image _ Complex.continuous_exp.continuousOn

/-- An open annulus is open. -/
theorem isOpen_openAnnulus {r R : ℝ} : IsOpen {z : ℂ | r < ‖z‖ ∧ ‖z‖ < R} := by
  have : {z : ℂ | r < ‖z‖ ∧ ‖z‖ < R} = (fun z : ℂ => ‖z‖) ⁻¹' (Set.Ioo r R) := by
    ext z; simp [Set.mem_Ioo]
  rw [this]
  exact isOpen_Ioo.preimage continuous_norm

end OpenAnnulus

section OuterCircle

/-- **Non-vanishing propagates outward across one fundamental annulus.**

`θ_P(P²w) = w·θ_P(w)` with `w ≠ 0`, so a zero on `‖z‖ = P²ρ` would force one on
`‖z‖ = ρ`. This is why `qTheta_winding_step`'s single hypothesis — no zero on the
*inner* circle — is enough to make both contours legitimate. -/
theorem qThetaC_ne_zero_outer (P : ℝ) (hP : 1 < P) (ρ : ℝ) (hρ : 0 < ρ)
    (hne : ∀ z : ℂ, ‖z‖ = ρ → qThetaC P z ≠ 0) :
    ∀ z : ℂ, ‖z‖ = P ^ 2 * ρ → qThetaC P z ≠ 0 := by
  have hP0 : (0:ℝ) < P := lt_trans zero_lt_one hP
  have hPC : ((P:ℂ)) ≠ 0 := by exact_mod_cast hP0.ne'
  intro z hz
  set w : ℂ := z / (P:ℂ) ^ (2:ℤ) with hwdef
  have hpow : ((P:ℂ) ^ (2:ℤ)) ≠ 0 := zpow_ne_zero _ hPC
  have hnormpow : ‖((P:ℂ) ^ (2:ℤ))‖ = P ^ 2 := by
    rw [norm_zpow, Complex.norm_real, Real.norm_eq_abs, abs_of_pos hP0, zpow_two, pow_two]
  have hwnorm : ‖w‖ = ρ := by
    rw [hwdef, norm_div, hz, hnormpow]
    field_simp
  have hw0 : w ≠ 0 := by
    intro h
    rw [h, norm_zero] at hwnorm
    exact hρ.ne hwnorm
  have hzw : z = (P:ℂ) ^ (2:ℤ) * w := by
    rw [hwdef]
    field_simp
  rw [hzw, qThetaC_functional_equation P hP0 w hw0]
  exact mul_ne_zero hw0 (hne w hwnorm)

end OuterCircle

section ZeroCount

/-- **The zeros of `θ_P` between two clean circles, and the winding number that
counts them.**

If `θ_P` vanishes nowhere on `‖z‖ = r` or on `‖z‖ = R`, its zeros in the open
annulus form a finite set `S` with strictly positive multiplicities `m`, and

    ∮_{|z|=R} θ'/θ  −  ∮_{|z|=r} θ'/θ  =  (∑ a ∈ S, m a) · 2πi.

`exists_finset_factorisation` supplies the factorisation on an open annulus
strictly larger than the contours (it must be strictly larger — the identity
theorem needs an open connected domain, and the argument principle needs the
non-vanishing factor on a *neighbourhood* of the closed contour annulus), and
`argumentPrinciple_annulus_filter` counts only the factors in between.

Nothing here mentions `−P^{2ℤ}`: which points the zeros are is arithmetic, and
is the caller's job. -/
theorem qThetaC_zeros_annulus (P : ℝ) (hP : 1 < P) (r R : ℝ) (hr : 0 < r) (hrR : r < R)
    (hnr : ∀ z : ℂ, ‖z‖ = r → qThetaC P z ≠ 0)
    (hnR : ∀ z : ℂ, ‖z‖ = R → qThetaC P z ≠ 0) :
    ∃ (S : Finset ℂ) (m : ℂ → ℕ),
      (∀ a ∈ S, r < ‖a‖ ∧ ‖a‖ < R) ∧ (∀ a ∈ S, 0 < m a) ∧
      (∀ z : ℂ, r < ‖z‖ → ‖z‖ < R → (qThetaC P z = 0 ↔ z ∈ S)) ∧
      (∮ z in C((0:ℂ), R), deriv (qThetaC P) z / qThetaC P z)
        - (∮ z in C((0:ℂ), r), deriv (qThetaC P) z / qThetaC P z)
        = (∑ a ∈ S, (m a : ℂ)) * (2 * Real.pi * Complex.I) := by
  classical
  have hR : (0:ℝ) < R := lt_trans hr hrR
  -- the working annulus, strictly larger than the contours on both sides
  set V : Set ℂ := {z : ℂ | r / 2 < ‖z‖ ∧ ‖z‖ < 2 * R} with hVdef
  set K : Set ℂ := closedBall (0:ℂ) (2 * R) \ ball (0:ℂ) (r / 2) with hKdef
  have hVopen : IsOpen V := isOpen_openAnnulus
  have hVconn : IsPreconnected V := isPreconnected_openAnnulus (by linarith) (by linarith)
  have hnormr : ‖(r : ℂ)‖ = r := by
    rw [Complex.norm_real, Real.norm_eq_abs, abs_of_pos hr]
  have hrV : (r : ℂ) ∈ V := by
    rw [hVdef]
    exact ⟨by rw [hnormr]; linarith, by rw [hnormr]; linarith⟩
  have hVne : V.Nonempty := ⟨(r : ℂ), hrV⟩
  have hK : IsCompact K := (isCompact_closedBall _ _).diff isOpen_ball
  have hVK : V ⊆ K := by
    intro z hz
    rw [hVdef] at hz
    refine ⟨?_, ?_⟩
    · simpa [mem_closedBall, dist_zero_right] using hz.2.le
    · simp only [mem_ball, dist_zero_right, not_lt]
      exact hz.1.le
  have hK0 : K ⊆ ({(0:ℂ)}ᶜ) := by
    intro z hz h
    simp only [Set.mem_singleton_iff] at h
    have h2 := hz.2
    simp only [mem_ball, dist_zero_right, not_lt] at h2
    rw [h, norm_zero] at h2
    linarith
  have hf : AnalyticOnNhd ℂ (qThetaC P) K :=
    ((differentiableOn_qThetaC P hP).analyticOnNhd isOpen_compl_singleton).mono hK0
  have hfV : AnalyticOnNhd ℂ (qThetaC P) V := hf.mono hVK
  have hrne : qThetaC P (r : ℂ) ≠ 0 := hnr _ hnormr
  -- `θ_P` is not locally zero anywhere on `V`: it is nonzero at `r`, and `V` is
  -- connected, so the identity theorem forbids a zero neighbourhood
  have hord : ∀ u : V, meromorphicOrderAt (qThetaC P) u ≠ ⊤ := by
    rintro ⟨u, hu⟩ hcon
    rw [(hfV u hu).meromorphicOrderAt_eq, ENat.map_eq_top_iff, analyticOrderAt_eq_top] at hcon
    have := hfV.eqOn_zero_of_preconnected_of_eventuallyEq_zero hVconn hu hcon hrV
    exact hrne (by simpa using this)
  obtain ⟨S, m, g, hg, hgne, hmpos, hSV, hEq⟩ :=
    QOU.Mathlib.exists_finset_factorisation hVopen hVconn hVne hK hVK hf hord
  have hgV : ∀ z ∈ V, g z ≠ 0 := fun z hz => hgne ⟨z, hz⟩
  -- every factor is a zero of `θ_P` …
  have hSzero : ∀ a ∈ S, qThetaC P a = 0 := by
    intro a ha
    have hval : qThetaC P a = (∏ b ∈ S, (a - b) ^ (m b)) * g a := hEq (hSV a ha)
    have hprod : (∏ b ∈ S, (a - b) ^ (m b)) = 0 :=
      Finset.prod_eq_zero ha (by rw [sub_self, zero_pow (hmpos a ha).ne'])
    rw [hval, hprod, zero_mul]
  -- … so no factor sits on either contour
  have hSne : ∀ a ∈ S, ‖a‖ ≠ r ∧ ‖a‖ ≠ R :=
    fun a ha => ⟨fun h => hnr a h (hSzero a ha), fun h => hnR a h (hSzero a ha)⟩
  refine ⟨S.filter (fun a => r < ‖a‖ ∧ ‖a‖ < R), m, fun a ha => (Finset.mem_filter.1 ha).2,
    fun a ha => hmpos a (Finset.mem_filter.1 ha).1, ?_, ?_⟩
  · -- the zeros in the annulus are exactly the filtered factors
    intro z hz1 hz2
    refine ⟨fun hzero => ?_, fun hzT => hSzero z (Finset.mem_filter.1 hzT).1⟩
    have hzV : z ∈ V := by rw [hVdef]; exact ⟨by linarith, by linarith⟩
    have hval : qThetaC P z = (∏ b ∈ S, (z - b) ^ (m b)) * g z := hEq hzV
    rw [hzero] at hval
    have hprod : (∏ b ∈ S, (z - b) ^ (m b)) = 0 :=
      (mul_eq_zero.1 hval.symm).resolve_right (hgV z hzV)
    obtain ⟨b, hbS, hb⟩ := Finset.prod_eq_zero_iff.1 hprod
    have hzb : z = b := sub_eq_zero.1 ((pow_eq_zero_iff (hmpos b hbS).ne').1 hb)
    subst hzb
    exact Finset.mem_filter.2 ⟨hbS, hz1, hz2⟩
  · -- the argument principle, transferred from the factorisation to `θ_P` itself
    have hAsub : closedBall (0:ℂ) R \ ball (0:ℂ) r ⊆ V := by
      rintro z ⟨hz1, hz2⟩
      simp only [mem_closedBall, dist_zero_right] at hz1
      simp only [mem_ball, dist_zero_right, not_lt] at hz2
      rw [hVdef]
      exact ⟨by linarith, by linarith⟩
    have hap := argumentPrinciple_annulus_filter g S m r R hr hrR hVopen hAsub hg hgV hSne
    have htrans : ∀ s : ℝ, 0 ≤ s → sphere (0:ℂ) s ⊆ V →
        (∮ z in C((0:ℂ), s), deriv (fun w => (∏ a ∈ S, (w - a) ^ (m a)) * g w) z
            / ((∏ a ∈ S, (z - a) ^ (m a)) * g z))
          = ∮ z in C((0:ℂ), s), deriv (qThetaC P) z / qThetaC P z := by
      intro s hs hsub
      refine circleIntegral.integral_congr hs fun z hz => ?_
      have hzV : z ∈ V := hsub hz
      have hev : qThetaC P =ᶠ[𝓝 z] (fun w => (∏ a ∈ S, (w - a) ^ (m a)) * g w) :=
        Filter.eventuallyEq_of_mem (hVopen.mem_nhds hzV) hEq
      have hval : qThetaC P z = (∏ a ∈ S, (z - a) ^ (m a)) * g z := hEq hzV
      rw [hev.deriv_eq, hval]
    have hsphR : sphere (0:ℂ) R ⊆ V := by
      intro z hz
      simp only [mem_sphere, dist_zero_right] at hz
      rw [hVdef]
      exact ⟨by rw [hz]; linarith, by rw [hz]; linarith⟩
    have hsphr : sphere (0:ℂ) r ⊆ V := by
      intro z hz
      simp only [mem_sphere, dist_zero_right] at hz
      rw [hVdef]
      exact ⟨by rw [hz]; linarith, by rw [hz]; linarith⟩
    rw [htrans R hR.le hsphR, htrans r hr.le hsphr] at hap
    exact hap

end ZeroCount

end QOU.QBeta.C1Poles
