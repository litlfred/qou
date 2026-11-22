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

-- Ref: [leitner2026] bean `qou-argp` — the converse theta zero locus.
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

section Factorisation

/-- **`θ_P` is strictly positive on the positive real axis.**

Every term of `∑ P^{−n(n+1)} wⁿ` is positive when `w > 0`, so the sum is. This is
the cheapest proof that `θ_P` is not identically zero — which is what the
identity theorem needs before it will produce a divisor at all, and what the
`hne` hypotheses below ultimately rest on. -/
theorem qTheta_pos_of_pos (P w : ℝ) (hP : 1 < P) (hw : 0 < w) : 0 < qTheta P w := by
  have hP0 : (0:ℝ) < P := lt_trans zero_lt_one hP
  have hsum : Summable (fun n : ℤ => qThetaTerm P w n) := summable_qThetaTerm P w hP hw.ne'
  refine hsum.tsum_pos (fun n => ?_) 0 ?_
  · rw [qThetaTerm]
    exact le_of_lt (mul_pos (zpow_pos hP0 _) (zpow_pos hw _))
  · rw [qThetaTerm]
    norm_num

/-- `θ_P` is nonzero at every positive real, read in `ℂ`. -/
theorem qThetaC_ne_zero_of_pos (P w : ℝ) (hP : 1 < P) (hw : 0 < w) :
    qThetaC P (w : ℂ) ≠ 0 := by
  rw [qThetaC_ofReal]
  exact_mod_cast (qTheta_pos_of_pos P w hP hw).ne'

/-- **`θ_P` factorises over its zeros on any open annulus.**

`exists_finset_factorisation` with `V` the open annulus and `K` the closed one
around it; `qTheta_pos_of_pos` supplies the non-vanishing point the identity
theorem needs, so this carries no hypothesis beyond `0 < c < d`. -/
theorem qThetaC_factorisation_annulus (P : ℝ) (hP : 1 < P) (c d : ℝ) (hc : 0 < c) (hcd : c < d) :
    ∃ (S : Finset ℂ) (m : ℂ → ℕ) (g : ℂ → ℂ),
      AnalyticOnNhd ℂ g {z : ℂ | c < ‖z‖ ∧ ‖z‖ < d} ∧
      (∀ z : ℂ, c < ‖z‖ → ‖z‖ < d → g z ≠ 0) ∧
      (∀ a ∈ S, 0 < m a) ∧ (∀ a ∈ S, c < ‖a‖ ∧ ‖a‖ < d) ∧
      Set.EqOn (qThetaC P) (fun z => (∏ a ∈ S, (z - a) ^ (m a)) * g z)
        {z : ℂ | c < ‖z‖ ∧ ‖z‖ < d} := by
  classical
  set V : Set ℂ := {z : ℂ | c < ‖z‖ ∧ ‖z‖ < d} with hVdef
  set K : Set ℂ := closedBall (0:ℂ) d \ ball (0:ℂ) c with hKdef
  have hVopen : IsOpen V := isOpen_openAnnulus
  have hVconn : IsPreconnected V := isPreconnected_openAnnulus hc hcd
  -- the midpoint of the annulus on the positive real axis, where `θ_P > 0`
  have hmid0 : 0 < (c + d) / 2 := by linarith
  have hnormmid : ‖(((c + d) / 2 : ℝ) : ℂ)‖ = (c + d) / 2 := by
    rw [Complex.norm_real, Real.norm_eq_abs, abs_of_pos hmid0]
  have hmidV : (((c + d) / 2 : ℝ) : ℂ) ∈ V := by
    rw [hVdef]
    exact ⟨by rw [hnormmid]; linarith, by rw [hnormmid]; linarith⟩
  have hVne : V.Nonempty := ⟨_, hmidV⟩
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
  have hmidne : qThetaC P (((c + d) / 2 : ℝ) : ℂ) ≠ 0 :=
    qThetaC_ne_zero_of_pos P _ hP hmid0
  -- `θ_P` is not locally zero anywhere on `V`: it is nonzero at the midpoint,
  -- and `V` is connected, so the identity theorem forbids a zero neighbourhood
  have hord : ∀ u : V, meromorphicOrderAt (qThetaC P) u ≠ ⊤ := by
    rintro ⟨u, hu⟩ hcon
    rw [(hfV u hu).meromorphicOrderAt_eq, ENat.map_eq_top_iff, analyticOrderAt_eq_top] at hcon
    have := hfV.eqOn_zero_of_preconnected_of_eventuallyEq_zero hVconn hu hcon hmidV
    exact hmidne (by simpa using this)
  obtain ⟨S, m, g, hg, hgne, hmpos, hSV, hEq⟩ :=
    QOU.Mathlib.exists_finset_factorisation hVopen hVconn hVne hK hVK hf hord
  refine ⟨S, m, g, hg, fun z h1 h2 => hgne ⟨z, ?_⟩, hmpos, fun a ha => ?_, hEq⟩
  · rw [hVdef]; exact ⟨h1, h2⟩
  · have := hSV a ha; rw [hVdef] at this; exact this

/-- **The zeros of `θ_P` in an open annulus are a finite set** — and the
factorisation names it: `a ∈ S` and `θ_P a = 0` are the same statement there,
because the multiplicities are positive and the cofactor never vanishes. -/
theorem qThetaC_zeros_iff_annulus (P : ℝ) (hP : 1 < P) (c d : ℝ) (hc : 0 < c) (hcd : c < d) :
    ∃ S : Finset ℂ, (∀ a ∈ S, c < ‖a‖ ∧ ‖a‖ < d) ∧
      ∀ z : ℂ, c < ‖z‖ → ‖z‖ < d → (qThetaC P z = 0 ↔ z ∈ S) := by
  classical
  obtain ⟨S, m, g, _, hgV, hmpos, hSb, hEq⟩ :=
    qThetaC_factorisation_annulus P hP c d hc hcd
  refine ⟨S, hSb, fun z hz1 hz2 => ⟨fun hzero => ?_, fun hzS => ?_⟩⟩
  · have hval : qThetaC P z = (∏ b ∈ S, (z - b) ^ (m b)) * g z := hEq ⟨hz1, hz2⟩
    rw [hzero] at hval
    have hprod : (∏ b ∈ S, (z - b) ^ (m b)) = 0 :=
      (mul_eq_zero.1 hval.symm).resolve_right (hgV z hz1 hz2)
    obtain ⟨b, hbS, hb⟩ := Finset.prod_eq_zero_iff.1 hprod
    rwa [sub_eq_zero.1 ((pow_eq_zero_iff (hmpos b hbS).ne').1 hb)]
  · have hval : qThetaC P z = (∏ b ∈ S, (z - b) ^ (m b)) * g z := hEq ⟨hz1, hz2⟩
    have hprod : (∏ b ∈ S, (z - b) ^ (m b)) = 0 :=
      Finset.prod_eq_zero hzS (by rw [sub_self, zero_pow (hmpos z hzS).ne'])
    rw [hval, hprod, zero_mul]

end Factorisation

section CleanRadius

/-- **Every open interval of radii contains one on which `θ_P` does not vanish.**

Only finitely many radii carry a zero — the zeros in an annulus are finite — and
an interval of reals is infinite.

This is what makes the "no zero on `‖z‖ = ρ`" hypothesis of `qTheta_winding_step`
and everything downstream a choice rather than a restriction: given any point one
wants to reason about, a clean contour can always be placed on either side of
it. -/
theorem exists_clean_radius (P : ℝ) (hP : 1 < P) (c d : ℝ) (hc : 0 < c) (hcd : c < d) :
    ∃ ρ : ℝ, c < ρ ∧ ρ < d ∧ ∀ z : ℂ, ‖z‖ = ρ → qThetaC P z ≠ 0 := by
  classical
  obtain ⟨S, _, hS⟩ := qThetaC_zeros_iff_annulus P hP c d hc hcd
  have hMfin : ((fun z : ℂ => ‖z‖) '' (S : Set ℂ)).Finite := S.finite_toSet.image _
  obtain ⟨ρ, hρ, hρM⟩ := ((Set.Ioo_infinite hcd).diff hMfin).nonempty
  refine ⟨ρ, hρ.1, hρ.2, fun z hz hzero => hρM ⟨z, ?_, hz⟩⟩
  exact (hS z (by rw [hz]; exact hρ.1) (by rw [hz]; exact hρ.2)).1 hzero

end CleanRadius

section ZeroCount

/-- **The zeros of `θ_P` between two clean circles, and the winding number that
counts them.**

If `θ_P` vanishes nowhere on `‖z‖ = r` or on `‖z‖ = R`, its zeros in the open
annulus form a finite set `S` with strictly positive multiplicities `m`, and

    ∮_{|z|=R} θ'/θ  −  ∮_{|z|=r} θ'/θ  =  (∑ a ∈ S, m a) · 2πi.

The factorisation is taken on an annulus strictly larger than the contours — it
must be, since the argument principle needs the non-vanishing cofactor on a
*neighbourhood* of the closed contour annulus — and
`argumentPrinciple_annulus_filter` counts only the factors in between.

Nothing here mentions `−P^{2ℤ}`: which points the zeros are is arithmetic, and
is the caller's job. -/
theorem qThetaC_zeros_annulus (P : ℝ) (hP : 1 < P) (r R : ℝ) (hr : 0 < r) (hrR : r < R)
    (hnr : ∀ z : ℂ, ‖z‖ = r → qThetaC P z ≠ 0)
    (hnR : ∀ z : ℂ, ‖z‖ = R → qThetaC P z ≠ 0) :
    ∃ (S : Finset ℂ) (m : ℂ → ℕ),
      (∀ a ∈ S, r < ‖a‖ ∧ ‖a‖ < R) ∧ (∀ a ∈ S, 0 < m a) ∧
      (∀ a ∈ S, analyticOrderAt (qThetaC P) a = m a) ∧
      (∀ z : ℂ, r < ‖z‖ → ‖z‖ < R → (qThetaC P z = 0 ↔ z ∈ S)) ∧
      (∮ z in C((0:ℂ), R), deriv (qThetaC P) z / qThetaC P z)
        - (∮ z in C((0:ℂ), r), deriv (qThetaC P) z / qThetaC P z)
        = (∑ a ∈ S, (m a : ℂ)) * (2 * Real.pi * Complex.I) := by
  classical
  have hR : (0:ℝ) < R := lt_trans hr hrR
  obtain ⟨S, m, g, hg, hgV', hmpos, hSb, hEq⟩ :=
    qThetaC_factorisation_annulus P hP (r / 2) (2 * R) (by linarith) (by linarith)
  -- the working annulus, strictly larger than the contours on both sides
  set V : Set ℂ := {z : ℂ | r / 2 < ‖z‖ ∧ ‖z‖ < 2 * R} with hVdef
  have hVopen : IsOpen V := isOpen_openAnnulus
  have hgV : ∀ z ∈ V, g z ≠ 0 := by
    intro z hz; rw [hVdef] at hz; exact hgV' z hz.1 hz.2
  have hSVmem : ∀ a ∈ S, a ∈ V := by
    intro a ha; rw [hVdef]; exact hSb a ha
  -- every factor is a zero of `θ_P` …
  have hSzero : ∀ a ∈ S, qThetaC P a = 0 := by
    intro a ha
    have hval : qThetaC P a = (∏ b ∈ S, (a - b) ^ (m b)) * g a := hEq (hSb a ha)
    have hprod : (∏ b ∈ S, (a - b) ^ (m b)) = 0 :=
      Finset.prod_eq_zero ha (by rw [sub_self, zero_pow (hmpos a ha).ne'])
    rw [hval, hprod, zero_mul]
  -- … so no factor sits on either contour
  have hSne : ∀ a ∈ S, ‖a‖ ≠ r ∧ ‖a‖ ≠ R :=
    fun a ha => ⟨fun h => hnr a h (hSzero a ha), fun h => hnR a h (hSzero a ha)⟩
  refine ⟨S.filter (fun a => r < ‖a‖ ∧ ‖a‖ < R), m, fun a ha => (Finset.mem_filter.1 ha).2,
    fun a ha => hmpos a (Finset.mem_filter.1 ha).1,
    fun a ha => QOU.Mathlib.analyticOrderAt_eq_of_finset_factorisation hVopen hg hgV hSVmem hEq
      (Finset.mem_filter.1 ha).1, ?_, ?_⟩
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

section FundamentalAnnulus

/-- `2πi ≠ 0`, so the winding count can be cancelled. -/
private theorem two_pi_I_ne_zero : (2 * (Real.pi : ℂ) * Complex.I) ≠ 0 :=
  mul_ne_zero (mul_ne_zero two_ne_zero (by exact_mod_cast Real.pi_ne_zero)) Complex.I_ne_zero

/-- **`θ_P` has exactly one zero in each fundamental annulus.**

The converse of `qTheta_neg_zpow_eq_zero`, and the statement that makes the C1
pole divisor exact rather than `⊇`.

`qTheta_winding_step` puts the winding difference across `ρ < ‖z‖ < P²ρ` at
exactly `2πi`; `qThetaC_zeros_annulus` reads that difference as
`(∑ m)·2πi`, so `∑ m = 1`; every multiplicity is at least `1`, so the index set
is a single point.

The one hypothesis — no zero on the inner circle — is `qTheta_winding_step`'s
own, and is unavoidable rather than restrictive: the integrand `θ'/θ` is not
defined on a circle through a zero, and the radius is ours to choose. -/
theorem qThetaC_unique_zero_fundamental_annulus (P : ℝ) (hP : 1 < P) (ρ : ℝ) (hρ : 0 < ρ)
    (hne : ∀ z : ℂ, ‖z‖ = ρ → qThetaC P z ≠ 0) :
    ∃ a : ℂ, ρ < ‖a‖ ∧ ‖a‖ < P ^ 2 * ρ ∧ analyticOrderAt (qThetaC P) a = 1 ∧
      ∀ z : ℂ, ρ < ‖z‖ → ‖z‖ < P ^ 2 * ρ → (qThetaC P z = 0 ↔ z = a) := by
  classical
  have hP2 : (1:ℝ) < P ^ 2 := by nlinarith
  have hrR : ρ < P ^ 2 * ρ := by nlinarith
  obtain ⟨S, m, hSb, hmpos, hmord, hSzero, hwind⟩ :=
    qThetaC_zeros_annulus P hP ρ (P ^ 2 * ρ) hρ hrR hne (qThetaC_ne_zero_outer P hP ρ hρ hne)
  rw [qTheta_winding_step P hP ρ hρ hne] at hwind
  -- the contour identity pins the count at one
  have key : (1 : ℂ) * (2 * (Real.pi : ℂ) * Complex.I)
      = (∑ a ∈ S, (m a : ℂ)) * (2 * (Real.pi : ℂ) * Complex.I) := by
    rw [← hwind]; ring
  have hsum1 : (1 : ℂ) = ∑ a ∈ S, (m a : ℂ) := mul_right_cancel₀ two_pi_I_ne_zero key
  have hsumN : (∑ a ∈ S, m a) = 1 := by
    have hcast : ((∑ a ∈ S, m a : ℕ) : ℂ) = 1 := by push_cast; exact hsum1.symm
    exact_mod_cast hcast
  -- positive multiplicities summing to one ⇒ a single point
  have hle : S.card ≤ ∑ a ∈ S, m a := by
    simpa using Finset.card_nsmul_le_sum S m 1 (fun x hx => hmpos x hx)
  have hSne : S.Nonempty := by
    rcases Finset.eq_empty_or_nonempty S with h | h
    · rw [h] at hsumN; simp at hsumN
    · exact h
  have hcard : S.card = 1 := le_antisymm (hsumN ▸ hle) (Finset.card_pos.2 hSne)
  obtain ⟨a, ha⟩ := Finset.card_eq_one.1 hcard
  have haS : a ∈ S := by rw [ha]; exact Finset.mem_singleton_self a
  refine ⟨a, (hSb a haS).1, (hSb a haS).2, ?_, ?_⟩
  · -- the single multiplicity carries the whole sum, so it is `1`
    have hma : m a = 1 := by rw [ha, Finset.sum_singleton] at hsumN; exact hsumN
    rw [hmord a haS, hma, Nat.cast_one]
  · intro z hz1 hz2
    rw [hSzero z hz1 hz2, ha, Finset.mem_singleton]

/-- **The converse zero locus on a fundamental annulus.**

If a lattice point `−P^{2k}` lies in the annulus, it *is* the unique zero — so
on that annulus the zero set of `θ_P` is exactly `{−P^{2k}}`, which is the
converse the C1 pole divisor needs.

Choosing the `k` is arithmetic on `Real.log`, not analysis, and is left to the
caller: the annulus has ratio `P²` and the lattice spacing is `P²`, so an *open*
fundamental annulus carries one lattice point or none, depending on where `ρ`
falls. -/
theorem qThetaC_zero_locus_fundamental_annulus (P : ℝ) (hP : 1 < P) (ρ : ℝ) (hρ : 0 < ρ)
    (hne : ∀ z : ℂ, ‖z‖ = ρ → qThetaC P z ≠ 0) (k : ℤ)
    (hk1 : ρ < P ^ (2 * k)) (hk2 : P ^ (2 * k) < P ^ 2 * ρ) :
    analyticOrderAt (qThetaC P) (-((P ^ (2 * k) : ℝ) : ℂ)) = 1 ∧
      ∀ z : ℂ, ρ < ‖z‖ → ‖z‖ < P ^ 2 * ρ →
        (qThetaC P z = 0 ↔ z = -((P ^ (2 * k) : ℝ) : ℂ)) := by
  have hP0 : (0:ℝ) < P := lt_trans zero_lt_one hP
  obtain ⟨a, _, _, haord, hchar⟩ := qThetaC_unique_zero_fundamental_annulus P hP ρ hρ hne
  -- the lattice point is a zero, and it sits in the annulus, so it is *the* zero
  have hlat : ‖(-((P ^ (2 * k) : ℝ) : ℂ))‖ = P ^ (2 * k) := by
    rw [norm_neg, Complex.norm_real, Real.norm_eq_abs, abs_of_pos (zpow_pos hP0 _)]
  have hlatzero : qThetaC P (-((P ^ (2 * k) : ℝ) : ℂ)) = 0 := by
    rw [← Complex.ofReal_neg, qThetaC_ofReal, qTheta_neg_zpow_eq_zero P hP0 k,
      Complex.ofReal_zero]
  have hlateq : -((P ^ (2 * k) : ℝ) : ℂ) = a :=
    (hchar _ (by rw [hlat]; exact hk1) (by rw [hlat]; exact hk2)).1 hlatzero
  refine ⟨by rw [hlateq]; exact haord, fun z hz1 hz2 => ?_⟩
  rw [hchar z hz1 hz2, hlateq]

end FundamentalAnnulus

section Global

/-- **The zero locus of `θ_P`, in full: `θ_P(w) = 0 ↔ w ∈ −P^{2ℤ}`.**

The converse of `qTheta_neg_zpow_eq_zero`, with no hypothesis beyond `w ≠ 0` —
and `0` is excluded only because it is an essential singularity, where `θ_P` is
not an analytic object at all. With `p = P²` this is the classical statement
that the zero set of `θ_p` is exactly `−p^ℤ`, each zero simple.

The argument is the fundamental-annulus result plus arithmetic:
`⌊logb (P²) ‖w‖⌋` names the annulus `P^{2k} ≤ ‖w‖ < P^{2k+2}` holding `w`;
`exists_clean_radius` places a clean contour `ρ` in `(‖w‖/P², P^{2k})`, an
interval that is nonempty *because* `‖w‖ < P^{2k+2}`; and `(ρ, P²ρ)` then
contains both `w` and `−P^{2k}`, which
`qThetaC_zero_locus_fundamental_annulus` identifies.

This is what makes the C1 pole divisor exact rather than a containment: every
locus in the table at the top of `C1ConnectionPoles.lean` is a single `p`-orbit
of this set, with nothing else in it. -/
theorem qThetaC_eq_zero_iff (P : ℝ) (hP : 1 < P) (w : ℂ) (hw : w ≠ 0) :
    qThetaC P w = 0 ↔ ∃ k : ℤ, w = -((P ^ (2 * k) : ℝ) : ℂ) := by
  have hP0 : (0:ℝ) < P := lt_trans zero_lt_one hP
  have hP2 : (1:ℝ) < P ^ 2 := by nlinarith
  have hP2' : (0:ℝ) < P ^ 2 := by positivity
  have hzpow : ∀ j : ℤ, ((P:ℝ) ^ 2) ^ j = P ^ (2 * j) := by
    intro j
    rw [← zpow_natCast P 2, ← zpow_mul]
    norm_num
  refine ⟨fun hzero => ?_, ?_⟩
  · have hs : (0:ℝ) < ‖w‖ := norm_pos_iff.mpr hw
    -- the fundamental annulus containing `w`
    set k : ℤ := ⌊Real.logb (P ^ 2) ‖w‖⌋ with hkdef
    have hkle : (P:ℝ) ^ (2 * k) ≤ ‖w‖ := by
      rw [← hzpow k]
      calc ((P:ℝ) ^ 2) ^ k = ((P:ℝ) ^ 2) ^ ((k : ℤ) : ℝ) := (Real.rpow_intCast _ k).symm
        _ ≤ ((P:ℝ) ^ 2) ^ Real.logb (P ^ 2) ‖w‖ :=
            (Real.rpow_le_rpow_left_iff hP2).2 (Int.floor_le _)
        _ = ‖w‖ := Real.rpow_logb hP2' hP2.ne' hs
    have hklt : ‖w‖ < ((P:ℝ) ^ 2) ^ (k + 1) := by
      calc ‖w‖ = ((P:ℝ) ^ 2) ^ Real.logb (P ^ 2) ‖w‖ := (Real.rpow_logb hP2' hP2.ne' hs).symm
        _ < ((P:ℝ) ^ 2) ^ ((k : ℝ) + 1) :=
            (Real.rpow_lt_rpow_left_iff hP2).2 (Int.lt_floor_add_one _)
        _ = ((P:ℝ) ^ 2) ^ (k + 1) := by
            rw [← Real.rpow_intCast ((P:ℝ) ^ 2) (k + 1)]; norm_cast
    -- a clean contour just below the lattice point, which exists precisely
    -- because `w` is in that annulus and not the next one out
    have hlow : ‖w‖ / P ^ 2 < P ^ (2 * k) := by
      rw [div_lt_iff₀ hP2', ← hzpow k, ← zpow_add_one₀ hP2'.ne' k]
      exact hklt
    obtain ⟨ρ, hρ1, hρ2, hclean⟩ :=
      exists_clean_radius P hP (‖w‖ / P ^ 2) (P ^ (2 * k)) (by positivity) hlow
    have hρ1' : ‖w‖ < ρ * P ^ 2 := (div_lt_iff₀ hP2').1 hρ1
    have hρ0 : 0 < ρ := lt_trans (by positivity) hρ1
    have hk2 : (P:ℝ) ^ (2 * k) < P ^ 2 * ρ := by
      calc (P:ℝ) ^ (2 * k) ≤ ‖w‖ := hkle
        _ < ρ * P ^ 2 := hρ1'
        _ = P ^ 2 * ρ := by ring
    have hw2 : ‖w‖ < P ^ 2 * ρ := by rw [mul_comm]; exact hρ1'
    exact ⟨k, ((qThetaC_zero_locus_fundamental_annulus P hP ρ hρ0 hclean k hρ2 hk2).2
      w (lt_of_lt_of_le hρ2 hkle) hw2).1 hzero⟩
  · rintro ⟨k, rfl⟩
    rw [← Complex.ofReal_neg, qThetaC_ofReal, qTheta_neg_zpow_eq_zero P hP0 k,
      Complex.ofReal_zero]

/-- **Every zero of `θ_P` is simple.**

Together with `qThetaC_eq_zero_iff` this is the entire divisor of `θ_P` on
`ℂ*`: the orbit `−P^{2ℤ}`, reduced. It is what makes the C1 pole divisor
*determined* rather than merely supported — a containment of zero sets fixes
where the poles can be, but not with what multiplicity. -/
theorem qThetaC_analyticOrderAt_neg_zpow (P : ℝ) (hP : 1 < P) (k : ℤ) :
    analyticOrderAt (qThetaC P) (-((P ^ (2 * k) : ℝ) : ℂ)) = 1 := by
  have hP0 : (0:ℝ) < P := lt_trans zero_lt_one hP
  have hP2 : (1:ℝ) < P ^ 2 := by nlinarith
  have hP2' : (0:ℝ) < P ^ 2 := by positivity
  have hpos : (0:ℝ) < P ^ (2 * k) := zpow_pos hP0 _
  obtain ⟨ρ, hρ1, hρ2, hclean⟩ :=
    exists_clean_radius P hP (P ^ (2 * k) / P ^ 2) (P ^ (2 * k)) (by positivity)
      (div_lt_self hpos hP2)
  have hρ0 : 0 < ρ := lt_trans (by positivity) hρ1
  have hk2 : (P:ℝ) ^ (2 * k) < P ^ 2 * ρ :=
    calc (P:ℝ) ^ (2 * k) < ρ * P ^ 2 := (div_lt_iff₀ hP2').1 hρ1
      _ = P ^ 2 * ρ := mul_comm _ _
  exact (qThetaC_zero_locus_fundamental_annulus P hP ρ hρ0 hclean k hρ2 hk2).1

end Global

end QOU.QBeta.C1Poles
