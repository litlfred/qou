import QOU.Mass.KZHolonomy.FlatTransport

/-!
# Flat transport in two real variables

A two-variable linear system `∂_a S = Ωa S`, `∂_b S = Ωb S` on a subset of `ℝ × ℝ`
(`IsSol2`).  Three facts used for the KZ pentagon:

* `exists_eq_mul_of_isSol2` — on an open rectangle two solutions, one pointwise invertible,
  differ by a constant on the right;
* `exists_reference2` — a flat connection `fa da + fb db` on an open star-shaped domain has an
  invertible fundamental solution normalised at the centre (radial transport);
* `isSol2_comp` — pulling such a solution back along a map `ψ` gives a solution of the
  pulled-back system (chain rule).

-- Ref: [leitner2026] docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md §2 Step 1
-/

set_option autoImplicit false

namespace QOU.KZ.Flat2D

open Set Filter Topology QOU.Mass.KZHolonomy

variable {R : Type*} [NormedRing R] [NormedAlgebra ℝ R] [CompleteSpace R]

/-- `S` solves `∂_a S = Ωa S`, `∂_b S = Ωb S` at every point of `D`. -/
def IsSol2 (Ωa Ωb S : ℝ × ℝ → R) (D : Set (ℝ × ℝ)) : Prop :=
  ∀ p ∈ D, HasDerivAt (fun a => S (a, p.2)) (Ωa p * S p) p.1 ∧
           HasDerivAt (fun b => S (p.1, b)) (Ωb p * S p) p.2

/-- The connection form `v ↦ v.1 • fa p + v.2 • fb p`. -/
noncomputable def form (fa fb : ℝ × ℝ → R) (p : ℝ × ℝ) : ℝ × ℝ →L[ℝ] R :=
  (ContinuousLinearMap.fst ℝ ℝ ℝ).smulRight (fa p) +
    (ContinuousLinearMap.snd ℝ ℝ ℝ).smulRight (fb p)

omit [CompleteSpace R] in
@[simp] theorem form_apply (fa fb : ℝ × ℝ → R) (p v : ℝ × ℝ) :
    form fa fb p v = v.1 • fa p + v.2 • fb p := rfl

/-! ### Small helpers -/

omit [CompleteSpace R] in
theorem IsSol2.mul_const {Ωa Ωb S : ℝ × ℝ → R} {D : Set (ℝ × ℝ)} (hS : IsSol2 Ωa Ωb S D)
    (α : R) : IsSol2 Ωa Ωb (fun p => S p * α) D := fun p hp => by
  refine ⟨?_, ?_⟩
  · simpa [mul_assoc] using (hS p hp).1.mul_const α
  · simpa [mul_assoc] using (hS p hp).2.mul_const α

omit [CompleteSpace R] in
theorem IsSol2.congr {Ωa Ωb Ga Gb S : ℝ × ℝ → R} {D : Set (ℝ × ℝ)} (hS : IsSol2 Ωa Ωb S D)
    (ha : ∀ p ∈ D, Ga p = Ωa p) (hb : ∀ p ∈ D, Gb p = Ωb p) : IsSol2 Ga Gb S D :=
  fun p hp => by rw [ha p hp, hb p hp]; exact hS p hp

/-! ### Pullback along a chart -/

omit [CompleteSpace R] in
/-- **Chain rule.** A solution `N` of the flat system `dN = (fa da + fb db) N` pulls back along
`ψ` to a solution of the pulled-back two-variable system. -/
theorem isSol2_comp {fa fb N : ℝ × ℝ → R} {D : Set (ℝ × ℝ)}
    (hN : ∀ p ∈ D, HasFDerivAt N ((ContinuousLinearMap.mul ℝ R).flip (N p) ∘L form fa fb p) p)
    {ψ : ℝ × ℝ → ℝ × ℝ} {ψa ψb : ℝ × ℝ → ℝ × ℝ} {T : Set (ℝ × ℝ)} (hT : ∀ q ∈ T, ψ q ∈ D)
    (hψa : ∀ q ∈ T, HasDerivAt (fun a => ψ (a, q.2)) (ψa q) q.1)
    (hψb : ∀ q ∈ T, HasDerivAt (fun b => ψ (q.1, b)) (ψb q) q.2) :
    IsSol2 (fun q => (ψa q).1 • fa (ψ q) + (ψa q).2 • fb (ψ q))
      (fun q => (ψb q).1 • fa (ψ q) + (ψb q).2 • fb (ψ q)) (N ∘ ψ) T := fun q hq => by
  refine ⟨?_, ?_⟩
  · have h := (hN (ψ q) (hT q hq)).comp_hasDerivAt q.1 (hψa q hq)
    simpa [Function.comp_def, add_mul, smul_mul_assoc] using h
  · have h := (hN (ψ q) (hT q hq)).comp_hasDerivAt q.2 (hψb q hq)
    simpa [Function.comp_def, add_mul, smul_mul_assoc] using h

omit [CompleteSpace R] in
/-- `isSol2_comp` with the pulled-back coefficients supplied as given functions. -/
theorem isSol2_comp_of_eq {fa fb N Ga Gb : ℝ × ℝ → R} {D : Set (ℝ × ℝ)}
    (hN : ∀ p ∈ D, HasFDerivAt N ((ContinuousLinearMap.mul ℝ R).flip (N p) ∘L form fa fb p) p)
    {ψ : ℝ × ℝ → ℝ × ℝ} {ψa ψb : ℝ × ℝ → ℝ × ℝ} {T : Set (ℝ × ℝ)} (hT : ∀ q ∈ T, ψ q ∈ D)
    (hψa : ∀ q ∈ T, HasDerivAt (fun a => ψ (a, q.2)) (ψa q) q.1)
    (hψb : ∀ q ∈ T, HasDerivAt (fun b => ψ (q.1, b)) (ψb q) q.2)
    (hGa : ∀ q ∈ T, Ga q = (ψa q).1 • fa (ψ q) + (ψa q).2 • fb (ψ q))
    (hGb : ∀ q ∈ T, Gb q = (ψb q).1 • fa (ψ q) + (ψb q).2 • fb (ψ q)) :
    IsSol2 Ga Gb (N ∘ ψ) T :=
  (isSol2_comp hN hT hψa hψb).congr hGa hGb

/-! ### Reference solution of a flat two-component connection -/

/-- `smulRight` against the first coordinate, as a continuous linear map. -/
noncomputable def sR1 : R →L[ℝ] (ℝ × ℝ →L[ℝ] R) :=
  ContinuousLinearMap.smulRightL ℝ (ℝ × ℝ) R (ContinuousLinearMap.fst ℝ ℝ ℝ)

/-- `smulRight` against the second coordinate, as a continuous linear map. -/
noncomputable def sR2 : R →L[ℝ] (ℝ × ℝ →L[ℝ] R) :=
  ContinuousLinearMap.smulRightL ℝ (ℝ × ℝ) R (ContinuousLinearMap.snd ℝ ℝ ℝ)

omit [CompleteSpace R] in
@[simp] theorem sR1_apply (x : R) (v : ℝ × ℝ) : sR1 x v = v.1 • x := rfl

omit [CompleteSpace R] in
@[simp] theorem sR2_apply (x : R) (v : ℝ × ℝ) : sR2 x v = v.2 • x := rfl

omit [CompleteSpace R] in
theorem form_eq (fa fb : ℝ × ℝ → R) : form fa fb = ⇑sR1 ∘ fa + ⇑sR2 ∘ fb := by
  funext p; ext <;> simp

omit [CompleteSpace R] in
theorem clm_decomp (L : ℝ × ℝ →L[ℝ] R) (a : ℝ × ℝ) :
    L a = a.1 • L (1, 0) + a.2 • L (0, 1) := by
  rw [← map_smul, ← map_smul, ← map_add]
  congr 1
  ext <;> simp

omit [CompleteSpace R] in
/-- Flatness of the two-component form reduces to the single `(1,0),(0,1)` identity. -/
theorem isFlatOn_form {fa fb : ℝ × ℝ → R} {fa' fb' : ℝ × ℝ → (ℝ × ℝ →L[ℝ] R)}
    {D : Set (ℝ × ℝ)}
    (hfa : ∀ p ∈ D, HasFDerivAt fa (fa' p) p) (hfb : ∀ p ∈ D, HasFDerivAt fb (fb' p) p)
    (hca : ContinuousOn fa' D) (hcb : ContinuousOn fb' D)
    (hflat : ∀ p ∈ D, fb' p (1, 0) - fa' p (0, 1) = fa p * fb p - fb p * fa p) :
    IsFlatOn (form fa fb) (fun p => sR1 ∘L fa' p + sR2 ∘L fb' p) D := by
  refine ⟨fun y hy => ?_, ?_, fun y hy a b => ?_⟩
  · have h := (sR1.hasFDerivAt.comp y (hfa y hy)).add (sR2.hasFDerivAt.comp y (hfb y hy))
    rw [form_eq]
    exact h
  · exact (continuousOn_const.clm_comp hca).add (continuousOn_const.clm_comp hcb)
  · have hf := hflat y hy
    simp only [ContinuousLinearMap.add_apply, ContinuousLinearMap.comp_apply, sR1_apply,
      sR2_apply, form_apply]
    rw [clm_decomp (fa' y) a, clm_decomp (fa' y) b, clm_decomp (fb' y) a, clm_decomp (fb' y) b]
    have e : fb' y (1, 0) = fa' y (0, 1) + (fa y * fb y - fb y * fa y) := by
      rw [← hf]; abel
    rw [e]
    simp only [add_mul, mul_add, smul_mul_assoc, mul_smul_comm, smul_add, smul_sub, smul_smul]
    module

/-- **Reference solution.** A flat connection `fa da + fb db` (continuous derivatives) on an
open domain star-shaped about `c` has a fundamental solution `N`, `dN = (fa da + fb db) N`,
invertible on `D` and with `N c = 1` (radial transport). -/
theorem exists_reference2 {fa fb : ℝ × ℝ → R} {fa' fb' : ℝ × ℝ → (ℝ × ℝ →L[ℝ] R)}
    {D : Set (ℝ × ℝ)} {c : ℝ × ℝ}
    (hD : IsOpen D) (hstar : StarConvex ℝ c D)
    (hfa : ∀ p ∈ D, HasFDerivAt fa (fa' p) p) (hfb : ∀ p ∈ D, HasFDerivAt fb (fb' p) p)
    (hca : ContinuousOn fa' D) (hcb : ContinuousOn fb' D)
    (hflat : ∀ p ∈ D, fb' p (1, 0) - fa' p (0, 1) = fa p * fb p - fb p * fa p) :
    ∃ N : ℝ × ℝ → R,
      (∀ p ∈ D, HasFDerivAt N ((ContinuousLinearMap.mul ℝ R).flip (N p) ∘L form fa fb p) p) ∧
      (∀ p ∈ D, IsUnit (N p)) ∧ N c = 1 := by
  have hfl := isFlatOn_form hfa hfb hca hcb hflat
  refine ⟨radialTransport (form fa fb) c, fun p hp => ?_,
    fun p hp => isUnit_radialTransport hstar hfl hp, ?_⟩
  · exact hasFDerivAt_radialTransport hD hfl (fun t ht => seg_mem_of_starConvex hstar hp ht)
  · have hX : ContinuousOn (radialX (form fa fb) c c) (Icc 0 1) := by
      unfold radialX; simp only [sub_self, map_zero]; exact continuousOn_const
    have hU : IsFundSol (radialX (form fa fb) c c) (fun _ => (1 : R)) := by
      refine ⟨rfl, fun t _ => ?_⟩
      unfold radialX; simp only [sub_self, map_zero, zero_mul]
      exact hasDerivWithinAt_const _ _ _
    rw [radialTransport_eq hX hU]

/-- `exists_reference2` in the form of `IsSol2`. -/
theorem exists_reference2_isSol2 {fa fb : ℝ × ℝ → R} {fa' fb' : ℝ × ℝ → (ℝ × ℝ →L[ℝ] R)}
    {D : Set (ℝ × ℝ)} {c : ℝ × ℝ}
    (hD : IsOpen D) (hstar : StarConvex ℝ c D)
    (hfa : ∀ p ∈ D, HasFDerivAt fa (fa' p) p) (hfb : ∀ p ∈ D, HasFDerivAt fb (fb' p) p)
    (hca : ContinuousOn fa' D) (hcb : ContinuousOn fb' D)
    (hflat : ∀ p ∈ D, fb' p (1, 0) - fa' p (0, 1) = fa p * fb p - fb p * fa p) :
    ∃ N : ℝ × ℝ → R, IsSol2 fa fb N D ∧ (∀ p ∈ D, IsUnit (N p)) ∧ N c = 1 := by
  obtain ⟨N, hN, hu, hc⟩ := exists_reference2 hD hstar hfa hfb hca hcb hflat
  refine ⟨N, ?_, hu, hc⟩
  have h := isSol2_comp (ψ := id) (ψa := fun _ => (1, 0)) (ψb := fun _ => (0, 1)) hN
    (fun q hq => hq) (fun q _ => (hasDerivAt_id q.1).prodMk (hasDerivAt_const q.1 q.2))
    (fun q _ => (hasDerivAt_const q.2 q.1).prodMk (hasDerivAt_id q.2))
  simpa using h

/-! ### Uniqueness on an open rectangle -/

/-- If `f' = Ω f`, `g' = Ω g` at `x` and `f x` is a unit, then `f⁻¹ g` is stationary at `x`. -/
theorem hasDerivAt_inverse_mul {f g : ℝ → R} {x : ℝ} {Ω : R}
    (hf : HasDerivAt f (Ω * f x) x) (hg : HasDerivAt g (Ω * g x) x) (hu : IsUnit (f x)) :
    HasDerivAt (fun t => Ring.inverse (f t) * g t) 0 x := by
  obtain ⟨u, hu⟩ := hu
  have hI : HasFDerivAt Ring.inverse (-ContinuousLinearMap.mulLeftRight ℝ R ↑u⁻¹ ↑u⁻¹) (f x) := by
    rw [← hu]; exact hasFDerivAt_ringInverse u
  have h := (hI.comp_hasDerivAt x hf).mul hg
  convert h using 1
  simp only [ContinuousLinearMap.neg_apply, ContinuousLinearMap.mulLeftRight_apply,
    Function.comp_apply, neg_mul]
  rw [← hu]
  simp [mul_assoc]

omit [CompleteSpace R] in
theorem eq_of_hasDerivAt_zero_Ioo {h : ℝ → R} {a b : ℝ}
    (hh : ∀ x ∈ Ioo a b, HasDerivAt h 0 x) {x y : ℝ} (hx : x ∈ Ioo a b) (hy : y ∈ Ioo a b) :
    h x = h y :=
  isOpen_Ioo.is_const_of_deriv_eq_zero isPreconnected_Ioo
    (fun z hz => (hh z hz).differentiableAt.differentiableWithinAt)
    (fun z hz => (hh z hz).deriv) hx hy

/-- **Uniqueness.** On an open rectangle, a solution `S` of the two-variable system is a
constant right multiple of a pointwise invertible solution `N`. -/
theorem exists_eq_mul_of_isSol2 {Ωa Ωb S N : ℝ × ℝ → R} {a b c d : ℝ}
    (hS : IsSol2 Ωa Ωb S (Set.Ioo a b ×ˢ Set.Ioo c d))
    (hN : IsSol2 Ωa Ωb N (Set.Ioo a b ×ˢ Set.Ioo c d))
    (hu : ∀ p ∈ Set.Ioo a b ×ˢ Set.Ioo c d, IsUnit (N p)) :
    ∃ α : R, ∀ p ∈ Set.Ioo a b ×ˢ Set.Ioo c d, S p = N p * α := by
  by_cases hne : (Set.Ioo a b ×ˢ Set.Ioo c d).Nonempty
  · obtain ⟨p0, hp0⟩ := hne
    set g : ℝ × ℝ → R := fun p => Ring.inverse (N p) * S p with hg
    refine ⟨g p0, fun p hp => ?_⟩
    have hv : g p = g (p.1, p0.2) :=
      eq_of_hasDerivAt_zero_Ioo (h := fun y => g (p.1, y))
        (fun y hy => hasDerivAt_inverse_mul (hN (p.1, y) ⟨hp.1, hy⟩).2
          (hS (p.1, y) ⟨hp.1, hy⟩).2 (hu _ ⟨hp.1, hy⟩)) hp.2 hp0.2
    have hh : g (p.1, p0.2) = g p0 :=
      eq_of_hasDerivAt_zero_Ioo (h := fun x => g (x, p0.2))
        (fun x hx => hasDerivAt_inverse_mul (hN (x, p0.2) ⟨hx, hp0.2⟩).1
          (hS (x, p0.2) ⟨hx, hp0.2⟩).1 (hu _ ⟨hx, hp0.2⟩)) hp.1 hp0.1
    rw [← hh, ← hv, hg, ← mul_assoc, Ring.mul_inverse_cancel _ (hu p hp), one_mul]
  · exact ⟨0, fun p hp => (hne ⟨p, hp⟩).elim⟩

end QOU.KZ.Flat2D
