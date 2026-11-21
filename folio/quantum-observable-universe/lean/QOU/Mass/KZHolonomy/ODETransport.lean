import QOU.Mass.KZHolonomy.FlatGauge

/-!
# Cocycle transport along a smooth path is ODE transport

Let `ω` be a flat connection form on an open set `D ⊆ E`.  The local cocycle `flatCocycle hD hfl`
(`FlatCocycle`) transports along every continuous path in `D` by lifting it to the associated
covering space (`QOU.MathlibExt.LocalCocycleTransport`).  For a `C¹` path `γ` this transport is
the value at `1` of the fundamental solution of `U' = ω(γ)(γ') U`, `U 0 = 1`
(`transport_flatCocycle_eq`).

So the monodromy of the covering-space construction is the ODE monodromy used to define
`kzBraidRep`, and the gauge of `FlatGauge` intertwines the ODE transports of the two connections.

The proof: on a convex ball `B` on which `ω` is flat, `Φ_c(γ t)⁻¹ · U t` is constant in `t`
(`radialTransport` from a centre `c ∈ B`), because both factors solve the same linear ODE.  This
gives the local form of the lift, which `LocalCocycle.transport_eq_of_local` recognises.
-/

set_option autoImplicit false
set_option linter.unusedSectionVars false

namespace QOU.Mass.KZHolonomy

open Set Metric QOU.MathlibExt

variable {E A : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedRing A] [NormedAlgebra ℝ A] [CompleteSpace A]

/-- **Transport against radial transport.**  On a convex open set `B` on which `ω` is flat,
`Φ_c(γ t)⁻¹ · U t` takes the same value at both ends of any interval `[a, b] ⊆ [0,1]` on which
`γ` stays in `B`. -/
theorem inverse_radial_mul_transport_eq {ω : E → E →L[ℝ] A} {ω' : E → E →L[ℝ] E →L[ℝ] A}
    {B : Set E} (hB : IsOpen B) (hconv : Convex ℝ B) (hfl : IsFlatOn ω ω' B) {c : E}
    (hc : c ∈ B) {γ γ' : ℝ → E}
    (hγd : ∀ t ∈ Icc (0:ℝ) 1, HasDerivWithinAt γ (γ' t) (Icc 0 1) t)
    {U : ℝ → A} (hU : IsTransport ω γ γ' U) {a b : ℝ} (ha : 0 ≤ a) (hab : a ≤ b) (hb : b ≤ 1)
    (hγB : ∀ t ∈ Icc a b, γ t ∈ B) :
    Ring.inverse (radialTransport ω c (γ b)) * U b =
      Ring.inverse (radialTransport ω c (γ a)) * U a := by
  set Z : ℝ → A := fun t => Ring.inverse (radialTransport ω c (γ t)) * U t with hZ
  have hsub : Icc a b ⊆ Icc (0:ℝ) 1 := Icc_subset_Icc ha hb
  have hd : ∀ t ∈ Icc a b, HasDerivWithinAt Z 0 (Icc 0 1) t := by
    intro t ht
    have ht01 := hsub ht
    have hseg : ∀ s ∈ Icc (0:ℝ) 1, c + s • (γ t - c) ∈ B := fun s hs =>
      seg_mem_of_starConvex (hconv.starConvex hc) (hγB t ht) hs
    have hΦ : HasDerivWithinAt (fun s => radialTransport ω c (γ s))
        (ω (γ t) (γ' t) * radialTransport ω c (γ t)) (Icc 0 1) t := by
      have := (hasFDerivAt_radialTransport hB hfl hseg).comp_hasDerivWithinAt t (hγd t ht01)
      simpa only [ContinuousLinearMap.comp_apply, ContinuousLinearMap.flip_apply,
        ContinuousLinearMap.mul_apply'] using this
    obtain ⟨u, hu⟩ := isUnit_radialTransport_of_convex hconv hfl hc (hγB t ht)
    have hinv : HasFDerivAt (Ring.inverse : A → A)
        (-ContinuousLinearMap.mulLeftRight ℝ A ↑u⁻¹ ↑u⁻¹) (radialTransport ω c (γ t)) := by
      rw [← hu]; exact hasFDerivAt_ringInverse u
    have hprod := (hinv.comp_hasDerivWithinAt t hΦ).mul (hU.2 t ht01)
    convert hprod using 1
    simp only [Function.comp_apply, ContinuousLinearMap.neg_apply,
      ContinuousLinearMap.mulLeftRight_apply, ← hu, Ring.inverse_unit]
    simp only [mul_assoc, Units.mul_inv, mul_one, neg_mul]
    abel
  have hcont : ContinuousOn Z (Icc a b) := fun t ht =>
    ((hd t ht).continuousWithinAt).mono hsub
  have hconst := constant_of_has_deriv_right_zero hcont (fun t ht =>
    hasDerivWithinAt_Ici_of_Icc ⟨(hsub (Ico_subset_Icc_self ht)).1, lt_of_lt_of_le ht.2 hb⟩
      (hd t (Ico_subset_Icc_self ht))) b ⟨hab, le_rfl⟩
  exact hconst

/-- A unit of `A`, viewed in `Aˣᵐᵒᵖ` (and `1` for a non-unit). -/
noncomputable def opUnit (a : A) : Aˣᵐᵒᵖ := by
  classical
  exact if h : IsUnit a then MulOpposite.op h.unit else 1

theorem opUnit_val {a : A} (h : IsUnit a) : ((opUnit a).unop : A) = a := by
  rw [opUnit, dif_pos h]; rfl

variable {ω : E → E →L[ℝ] A} {ω' : E → E →L[ℝ] E →L[ℝ] A} {D : Set E}

/-- **Cocycle transport along a `C¹` path is ODE transport.**  If `p` is a path in `D` whose
underlying map is the `C¹` path `γ`, its transport by the flat cocycle of `ω` is `U 1`, where `U`
is the fundamental solution of `U' = ω(γ)(γ') U`. -/
theorem transport_flatCocycle_eq (hD : IsOpen D) (hfl : IsFlatOn ω ω' D) {γ γ' : ℝ → E}
    (hγd : ∀ t ∈ Icc (0:ℝ) 1, HasDerivWithinAt γ (γ' t) (Icc 0 1) t)
    (hγ'c : ContinuousOn γ' (Icc 0 1)) {U : ℝ → A} (hU : IsTransport ω γ γ' U)
    {a b : D} (p : Path a b) (hp : ∀ t : unitInterval, (p t : E) = γ t) :
    (((flatCocycle hD hfl).transport p).unop : A) = U 1 := by
  have hγD : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ D := fun t ht => by
    rw [← hp ⟨t, ht⟩]; exact (p ⟨t, ht⟩).2
  have hXc : ContinuousOn (fun t => ω (γ t) (γ' t)) (Icc 0 1) :=
    continuousOn_transportCoeff (fun t ht => (hfl.hasFDerivAt _ (hγD t ht)).continuousAt)
      (fun t ht => (hγd t ht).continuousWithinAt) hγ'c
  have hunit : ∀ t ∈ Icc (0:ℝ) 1, IsUnit (U t) := hU.isUnit hXc
  set v : unitInterval → Aˣᵐᵒᵖ := fun t => opUnit (U t) with hv
  have hvval : ∀ t : unitInterval, ((v t).unop : A) = U t := fun t => opUnit_val (hunit t t.2)
  have hv0 : v 0 = 1 := by
    apply MulOpposite.unop_injective; apply Units.ext
    rw [hvval]; exact hU.1
  have hloc : ∀ t₀, ∀ᶠ t in nhds t₀,
      v t = v t₀ * (flatCocycle hD hfl).P (p t₀) (p t) := by
    intro t₀
    set y₀ := p t₀
    set r := ballRadius hD y₀
    have hopen : IsOpen (p ⁻¹' (flatCocycle hD hfl).U y₀) :=
      ((flatCocycle hD hfl).isOpen_U y₀).preimage p.continuous
    obtain ⟨ε, hε, hball⟩ := Metric.isOpen_iff.mp hopen t₀ ((flatCocycle hD hfl).mem_U y₀)
    filter_upwards [Metric.ball_mem_nhds t₀ hε] with t ht
    have hin : ∀ s ∈ Icc (0:ℝ) 1, |s - t₀| < ε → γ s ∈ ball y₀.1 r := by
      intro s hs hst
      have := hball (show (⟨s, hs⟩ : unitInterval) ∈ ball t₀ ε by
        rw [mem_ball, Subtype.dist_eq, Real.dist_eq]; exact hst)
      rw [← hp ⟨s, hs⟩]; exact this
    have hdist : |(t : ℝ) - t₀| < ε := by
      rw [mem_ball, Subtype.dist_eq, Real.dist_eq] at ht; exact ht
    have hB := hfl.mono' (ball_subset hD y₀)
    have hy₀ : y₀.1 ∈ ball y₀.1 r := mem_ball_self (ballRadius_pos hD y₀)
    have hZ : Ring.inverse (radialTransport ω y₀.1 (γ t)) * U t =
        Ring.inverse (radialTransport ω y₀.1 (γ t₀)) * U t₀ := by
      rcases le_total (t₀ : ℝ) t with h | h
      · exact inverse_radial_mul_transport_eq isOpen_ball (convex_ball _ _) hB hy₀ hγd hU
          t₀.2.1 h t.2.2 fun s hs => hin s ⟨t₀.2.1.trans hs.1, hs.2.trans t.2.2⟩
            (by rw [abs_of_nonneg (by linarith [hs.1])]
                rw [abs_of_nonneg (by linarith)] at hdist; linarith [hs.2])
      · exact (inverse_radial_mul_transport_eq isOpen_ball (convex_ball _ _) hB hy₀ hγd hU
          t.2.1 h t₀.2.2 fun s hs => hin s ⟨t.2.1.trans hs.1, hs.2.trans t₀.2.2⟩
            (by rw [abs_of_nonpos (by linarith [hs.2])]
                rw [abs_of_nonpos (by linarith)] at hdist; linarith [hs.1])).symm
    have hself : radialTransport ω y₀.1 (γ t₀) = 1 := by
      rw [← hp t₀]; exact radialTransport_self_of_mem hD hfl y₀
    rw [hself, Ring.inverse_one, one_mul] at hZ
    have htB : γ t ∈ ball y₀.1 r := hin t t.2 hdist
    have hu := isUnit_radialTransport_of_convex (convex_ball y₀.1 r) hB hy₀ htB
    apply MulOpposite.unop_injective; apply Units.ext
    rw [MulOpposite.unop_mul, Units.val_mul, flatCocycle_P, hvval, hvval, hp t,
      radialUnit_val hu, ← hZ, ← mul_assoc,
      Ring.mul_inverse_cancel _ hu, one_mul]
  rw [(flatCocycle hD hfl).transport_eq_of_local p v hv0 hloc, hvval]
  rfl

end QOU.Mass.KZHolonomy
