/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLPrismPush

set_option autoImplicit false

/-!
# A Δ-move is a PL ambient isotopy (issue #8902, stage 2, part 11)

The ball hull of `PLDeltaIsotopy.lean` is not a polyhedron. This file puts a polyhedral body
inside it, so that the prism push of `PLPrismPush.lean` realizes the Δ-move.

## What is a DEFINITION here

* `crossφ B sp sm` — for a basis `B` indexed by `κ` and scales `sp k, sm k > 0`, the `2^κ`
  linear functionals `y ↦ ∑ₖ (±) (B.repr y k) / s±(k)` (sign chosen by `σ : κ → Bool`). Their
  polyhedron `polySet (crossφ B sp sm) 1` is the **skew cross-polytope** with vertices
  `sp k • B k` and `-(sm k) • B k`.

## What is a THEOREM here

* `polySet_cross_subset` — the skew cross-polytope lies in every convex set that contains `0`
  and its vertices.
* `exists_polyBody` — in finite dimension, for the Δ-triangle `a, b, c` there is a polyhedral
  body around `midpoint a b`, inside the ball hull, with `a`, `b` in it and `c` in its interior.
  The basis starts with `b - m` (and `c - m`, when it is not on the line of `a, b`).
* `deltaPushProvider_PL` — the prism push is a Δ-move provider with a **PL track**.
* `Move.plAmbientIsotopic`, `DeltaEquiv.plAmbientIsotopic` — **Δ-equivalent polygonal links
  are PL ambient isotopic** (finite dimension).

## What is NOT proved here

* The converse, PL ambient isotopy implies Δ-equivalence.
-/

namespace QOU.MathlibExt.PL

open Set Metric Module

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

section Cross

variable {κ : Type} [Fintype κ]

/-- The coefficient of coordinate `k` in the functional of sign pattern `σ`. -/
noncomputable def crossCoef (sp sm : κ → ℝ) (σ : κ → Bool) (k : κ) : ℝ :=
  if σ k then (sp k)⁻¹ else -(sm k)⁻¹

variable [FiniteDimensional ℝ E]

/-- The functionals of the skew cross-polytope. -/
noncomputable def crossφ (B : Basis κ ℝ E) (sp sm : κ → ℝ) (σ : κ → Bool) : E →L[ℝ] ℝ :=
  LinearMap.toContinuousLinearMap (∑ k, crossCoef sp sm σ k • B.coord k)

variable (B : Basis κ ℝ E) (sp sm : κ → ℝ)

lemma crossφ_apply (σ : κ → Bool) (y : E) :
    crossφ B sp sm σ y = ∑ k, crossCoef sp sm σ k * B.repr y k := by
  simp [crossφ]

lemma crossφ_smul_basis (σ : κ → Bool) (t : ℝ) (j : κ) :
    crossφ B sp sm σ (t • B j) = t * crossCoef sp sm σ j := by
  classical
  rw [crossφ_apply]
  simp [Finsupp.single_apply, mul_comm]

/-- **The skew cross-polytope lies in every convex set containing `0` and its vertices.** -/
lemma polySet_cross_subset (hsp : ∀ k, 0 < sp k) (hsm : ∀ k, 0 < sm k) {D : Set E}
    (hD : Convex ℝ D) (h0 : (0 : E) ∈ D) (hp : ∀ k, sp k • B k ∈ D)
    (hm : ∀ k, (-sm k) • B k ∈ D) : polySet (crossφ B sp sm) (fun _ => 1) ⊆ D := by
  classical
  intro y hy
  set μ : κ → ℝ := fun k => B.repr y k with hμ
  set σ : κ → Bool := fun k => decide (0 ≤ μ k) with hσ
  set w : κ → E := fun k => if σ k then sp k • B k else (-sm k) • B k with hw
  set t : κ → ℝ := fun k => crossCoef sp sm σ k * μ k with ht
  have ht0 : ∀ k, 0 ≤ t k := by
    intro k
    simp only [ht, hσ, crossCoef]
    by_cases h : 0 ≤ μ k
    · simp only [h, decide_true, ↓reduceIte]
      exact mul_nonneg (inv_nonneg.mpr (hsp k).le) h
    · simp only [h, decide_false, Bool.false_eq_true, ↓reduceIte]
      exact mul_nonneg_of_nonpos_of_nonpos (neg_nonpos.mpr (inv_nonneg.mpr (hsm k).le))
        (not_le.mp h).le
  have hT : ∑ k, t k ≤ 1 := by
    have := hy σ
    rwa [crossφ_apply] at this
  have hy' : y = ∑ k, t k • w k := by
    conv_lhs => rw [← B.sum_repr y]
    refine Finset.sum_congr rfl fun k _ => ?_
    simp only [ht, hw, crossCoef]
    split_ifs
    · rw [smul_smul]
      congr 1
      simp only [hμ]
      field_simp [(hsp k).ne']
    · rw [smul_smul]
      congr 1
      simp only [hμ]
      field_simp [(hsm k).ne']
  have hwD : ∀ k, w k ∈ D := by
    intro k
    simp only [hw]
    split_ifs
    · exact hp k
    · exact hm k
  by_cases hT0 : ∑ k, t k = 0
  · have hz : ∀ k, t k = 0 := fun k =>
      (Finset.sum_eq_zero_iff_of_nonneg fun k _ => ht0 k).mp hT0 k (Finset.mem_univ _)
    rw [hy']
    simpa [hz] using h0
  · have hTpos : 0 < ∑ k, t k := lt_of_le_of_ne (Finset.sum_nonneg fun k _ => ht0 k) (Ne.symm hT0)
    have hz : ∑ k, ((∑ k, t k)⁻¹ * t k) • w k ∈ D :=
      hD.sum_mem (fun k _ => mul_nonneg (inv_nonneg.mpr hTpos.le) (ht0 k))
        (by rw [← Finset.mul_sum, inv_mul_cancel₀ hT0]) (fun k _ => hwD k)
    have := hD.smul_mem_of_zero_mem h0 hz ⟨hTpos.le, hT⟩
    convert this using 1
    rw [Finset.smul_sum, hy']
    refine Finset.sum_congr rfl fun k _ => ?_
    rw [smul_smul, ← mul_assoc, mul_inv_cancel₀ hT0, one_mul]

end Cross

section Body

lemma mem_deltaBody_of_mid {a b c x : E} {ρ : ℝ} (hx : x ∈ closedBall (midpoint ℝ a b) ρ) :
    x ∈ deltaBody a b c ρ :=
  subset_convexHull ℝ _ (Or.inl (Or.inr hx))

lemma mem_deltaBody_of_apex {a b c x : E} {ρ : ℝ} (hx : x ∈ closedBall c ρ) :
    x ∈ deltaBody a b c ρ :=
  subset_convexHull ℝ _ (Or.inr hx)

lemma right_mem_deltaBody' {a b c : E} {ρ : ℝ} : b ∈ deltaBody a b c ρ :=
  subset_convexHull ℝ _ (by simp)

variable [FiniteDimensional ℝ E]

/-- A linearly independent set extends to a finite basis indexed by a type in `Type`. -/
lemma exists_basis_of_linearIndepOn {s : Set E} (hs : LinearIndepOn ℝ id s) :
    ∃ (κ : Type) (_ : Fintype κ) (B : Basis κ ℝ E), ∀ x ∈ s, ∃ k, B k = x := by
  classical
  let B0 := Basis.extend hs
  haveI : Finite (hs.extend (subset_univ s)) := Module.Finite.finite_basis B0
  let e := Finite.equivFin (hs.extend (subset_univ s))
  refine ⟨Fin (Nat.card (hs.extend (subset_univ s))), inferInstance, B0.reindex e,
    fun x hx => ⟨e ⟨x, Basis.subset_extend hs hx⟩, ?_⟩⟩
  simp [B0, Basis.reindex_apply, Basis.coe_extend]

/-- **A polyhedral body inside the ball hull of the Δ-triangle**, with `a`, `b` in it, `c` in its
interior, and the rays and the far part of the link outside it. -/
theorem exists_polyBody {a b c wa wb : E} {R' : Set E}
    (hsa : ∀ θ ∈ Icc (0 : ℝ) 1, (1 - θ) • (midpoint ℝ a b - a) + θ • (c - a) ≠ 0)
    (hsb : ∀ θ ∈ Icc (0 : ℝ) 1, (1 - θ) • (midpoint ℝ b a - b) + θ • (c - b) ≠ 0)
    (hta : ∀ t : ℝ, 0 < t → t ≤ 1 → a + t • wa ∉ convexHull ℝ {a, b, c})
    (htb : ∀ t : ℝ, 0 < t → t ≤ 1 → b + t • wb ∉ convexHull ℝ {a, b, c})
    (hR' : IsCompact R') (hdisj : Disjoint R' (convexHull ℝ {a, b, c})) :
    ∃ (ι : Type) (_ : Fintype ι) (φ : ι → E →L[ℝ] ℝ) (r : ι → ℝ), (∀ i, 0 < r i) ∧
      a - midpoint ℝ a b ∈ polySet φ r ∧ b - midpoint ℝ a b ∈ polySet φ r ∧
      (∀ i, φ i (c - midpoint ℝ a b) < r i) ∧
      (∀ t : ℝ, 0 < t → a + t • wa ∉ {x | x - midpoint ℝ a b ∈ polySet φ r}) ∧
      (∀ t : ℝ, 0 < t → b + t • wb ∉ {x | x - midpoint ℝ a b ∈ polySet φ r}) ∧
      Disjoint R' {x | x - midpoint ℝ a b ∈ polySet φ r} := by
  classical
  obtain ⟨ρ, hρ, hA, hB, hR⟩ := exists_deltaBody hsa hsb hta htb hR' hdisj
  rw [midpoint_comm b a] at hsb
  set m := midpoint ℝ a b with hm
  set u := b - m with hu
  set v := c - m with hv
  have hma : m - a = u := sub_eq_sub_iff_add_eq_add.mpr (by rw [hm, midpoint_add_self, add_comm])
  have hmb : m - b = -u := by rw [hu, neg_sub]
  have hca : c - a = v + u := by rw [← hma, hv, sub_add_sub_cancel]
  have hcb : c - b = v - u := by rw [hu, hv, sub_sub_sub_cancel_right]
  have hu0 : u ≠ 0 := by
    intro h0
    exact hsa 0 ⟨le_rfl, zero_le_one⟩ (by simp [hma, h0])
  have hbm : m + u = b := by rw [hu]; abel
  have ham : m + (-1 : ℝ) • u = a := by rw [← hma]; simp
  set δ : E → ℝ := fun x => ρ / (‖x‖ + 1) with hδ
  have hδ0 : ∀ x, 0 < δ x := fun x => div_pos hρ (by positivity)
  have hδx : ∀ x, ‖δ x • x‖ ≤ ρ := by
    intro x
    rw [norm_smul, Real.norm_of_nonneg (hδ0 x).le, hδ, div_mul_eq_mul_div,
      div_le_iff₀ (by positivity)]
    nlinarith [norm_nonneg x]
  have hball : ∀ (s : ℝ) (x : E), |s| ≤ δ x → m + s • x ∈ deltaBody a b c ρ := by
    intro s x hs
    refine mem_deltaBody_of_mid ?_
    rw [mem_closedBall, dist_eq_norm, add_sub_cancel_left, norm_smul, Real.norm_eq_abs]
    calc |s| * ‖x‖ ≤ δ x * ‖x‖ := mul_le_mul_of_nonneg_right hs (norm_nonneg x)
      _ = ‖δ x • x‖ := by rw [norm_smul, Real.norm_of_nonneg (hδ0 x).le]
      _ ≤ ρ := hδx x
  suffices key : ∃ (κ : Type) (_ : Fintype κ) (B : Basis κ ℝ E) (sp sm : κ → ℝ),
      (∀ k, 0 < sp k) ∧ (∀ k, 0 < sm k) ∧ (∀ k, m + sp k • B k ∈ deltaBody a b c ρ) ∧
      (∀ k, m + (-sm k) • B k ∈ deltaBody a b c ρ) ∧ (∀ σ, crossφ B sp sm σ u ≤ 1) ∧
      (∀ σ, crossφ B sp sm σ (-u) ≤ 1) ∧ (∀ σ, crossφ B sp sm σ v < 1) by
    obtain ⟨κ, _, B, sp, sm, hsp, hsm, hp, hn, hu1, hnu1, hv1⟩ := key
    have hsub : ∀ x, x - m ∈ polySet (crossφ B sp sm) (fun _ => 1) → x ∈ deltaBody a b c ρ := by
      intro x hx
      have h := polySet_cross_subset B sp sm hsp hsm (D := (fun y => m + y) ⁻¹' deltaBody a b c ρ)
        (convex_deltaBody.translate_preimage_right m)
        (by simpa using mem_deltaBody_of_mid (c := c) (mem_closedBall_self hρ.le)) hp hn hx
      simpa using h
    refine ⟨κ → Bool, inferInstance, crossφ B sp sm, fun _ => 1, fun _ => one_pos,
      fun σ => ?_, fun σ => hu1 σ, fun σ => hv1 σ, fun t ht h => hA t ht (hsub _ h),
      fun t ht h => hB t ht (hsub _ h), hR.mono_right fun x hx => hsub x hx⟩
    rw [show a - m = -u by rw [← hma, neg_sub]]
    exact hnu1 σ
  by_cases hdeg : ∃ γ : ℝ, γ • u = v
  · obtain ⟨γ, hγ⟩ := hdeg
    have hγ1 : γ < 1 := by
      by_contra h
      push_neg at h
      have hγ0 : 0 < γ := by linarith
      refine hsb (1 / γ) ⟨by positivity, by rw [div_le_one hγ0]; exact h⟩ ?_
      rw [hmb, hcb, ← hγ]
      have : (1 - 1 / γ) • -u + (1 / γ) • (γ • u - u) = (1 / γ * γ - 1) • u := by module
      rw [this, one_div_mul_cancel hγ0.ne', sub_self, zero_smul]
    have hγ2 : -1 < γ := by
      by_contra h
      push_neg at h
      have hγ0 : γ < 0 := by linarith
      refine hsa (-1 / γ) ⟨div_nonneg_of_nonpos (by norm_num) hγ0.le, ?_⟩ ?_
      · rw [div_le_one_of_neg hγ0]; exact h
      rw [hma, hca, ← hγ]
      have : (1 - -1 / γ) • u + (-1 / γ) • (γ • u + u) = (1 + -1 / γ * γ) • u := by module
      rw [this, div_mul_cancel₀ _ hγ0.ne]
      simp
    obtain ⟨κ, _, B, hB⟩ := exists_basis_of_linearIndepOn (LinearIndepOn.id_singleton ℝ hu0)
    obtain ⟨iu, hiu⟩ := hB u (mem_singleton u)
    set sp : κ → ℝ := fun k => if k = iu then 1 else δ (B k) with hsp
    have hpos : ∀ k, 0 < sp k := fun k => by
      simp only [hsp]; split_ifs
      · exact one_pos
      · exact hδ0 _
    have hc1 : ∀ σ, crossCoef sp sp σ iu = 1 ∨ crossCoef sp sp σ iu = -1 := by
      intro σ; simp only [crossCoef, hsp, if_pos rfl, inv_one]; cases σ iu <;> simp
    have hφ : ∀ σ (t : ℝ), crossφ B sp sp σ (t • u) = t * crossCoef sp sp σ iu := by
      intro σ t; rw [← hiu, crossφ_smul_basis]
    refine ⟨κ, inferInstance, B, sp, sp, hpos, hpos, fun k => ?_, fun k => ?_, fun σ => ?_,
      fun σ => ?_, fun σ => ?_⟩
    · by_cases hk : k = iu
      · simp only [hsp, hk, if_pos rfl, one_smul, hiu, hbm]; exact right_mem_deltaBody'
      · simp only [hsp, if_neg hk]; exact hball _ _ (by rw [abs_of_pos (hδ0 _)])
    · by_cases hk : k = iu
      · simp only [hsp, hk, if_pos rfl, hiu, ham]; exact left_mem_deltaBody
      · simp only [hsp, if_neg hk]; exact hball _ _ (by rw [abs_neg, abs_of_pos (hδ0 _)])
    · have := hφ σ 1; rw [one_smul] at this; rw [this]
      rcases hc1 σ with h | h <;> rw [h] <;> norm_num
    · have := hφ σ (-1); rw [neg_one_smul] at this; rw [this]
      rcases hc1 σ with h | h <;> rw [h] <;> norm_num
    · rw [← hγ, hφ]
      rcases hc1 σ with h | h <;> rw [h] <;> linarith
  · push_neg at hdeg
    obtain ⟨κ, _, B, hB⟩ :=
      exists_basis_of_linearIndepOn (linearIndepOn_id_pair hu0 hdeg)
    obtain ⟨iu, hiu⟩ := hB u (by simp)
    obtain ⟨iv, hiv⟩ := hB v (by simp)
    have hne : iv ≠ iu := by
      intro h; apply hdeg 1; rw [one_smul, ← hiu, ← hiv, h]
    set sp : κ → ℝ := fun k => if k = iu then 1 else if k = iv then 1 + δ v else δ (B k)
      with hsp
    set sm : κ → ℝ := fun k => if k = iu then 1 else δ (B k) with hsm
    have hp0 : ∀ k, 0 < sp k := fun k => by
      simp only [hsp]; split_ifs
      · exact one_pos
      · linarith [hδ0 v]
      · exact hδ0 _
    have hm0 : ∀ k, 0 < sm k := fun k => by
      simp only [hsm]; split_ifs
      · exact one_pos
      · exact hδ0 _
    have hc1 : ∀ σ, crossCoef sp sm σ iu = 1 ∨ crossCoef sp sm σ iu = -1 := by
      intro σ; simp only [crossCoef, hsp, hsm, if_pos rfl, inv_one]; cases σ iu <;> simp
    have hφu : ∀ σ (t : ℝ), crossφ B sp sm σ (t • u) = t * crossCoef sp sm σ iu := by
      intro σ t; rw [← hiu, crossφ_smul_basis]
    refine ⟨κ, inferInstance, B, sp, sm, hp0, hm0, fun k => ?_, fun k => ?_, fun σ => ?_,
      fun σ => ?_, fun σ => ?_⟩
    · by_cases hk : k = iu
      · simp only [hsp, hk, if_pos rfl, one_smul, hiu, hbm]; exact right_mem_deltaBody'
      by_cases hk' : k = iv
      · subst hk'
        simp only [hsp, if_neg hne, if_true, hiv]
        refine mem_deltaBody_of_apex ?_
        rw [mem_closedBall, dist_eq_norm,
          show m + (1 + δ v) • v - c = δ v • v by rw [hv]; module]
        exact hδx v
      · simp only [hsp, if_neg hk, if_neg hk']; exact hball _ _ (by rw [abs_of_pos (hδ0 _)])
    · by_cases hk : k = iu
      · simp only [hsm, hk, if_pos rfl, hiu, ham]; exact left_mem_deltaBody
      · simp only [hsm, if_neg hk]; exact hball _ _ (by rw [abs_neg, abs_of_pos (hδ0 _)])
    · have := hφu σ 1; rw [one_smul] at this; rw [this]
      rcases hc1 σ with h | h <;> rw [h] <;> norm_num
    · have := hφu σ (-1); rw [neg_one_smul] at this; rw [this]
      rcases hc1 σ with h | h <;> rw [h] <;> norm_num
    · have := crossφ_smul_basis B sp sm σ 1 iv
      rw [one_smul, hiv] at this
      rw [this, one_mul]
      simp only [crossCoef, hsp, hsm, if_neg hne]
      have hδv := hδ0 v
      cases σ iv
      · simp only [Bool.false_eq_true, ↓reduceIte]
        have : 0 < (δ (B iv))⁻¹ := inv_pos.mpr (hδ0 _)
        linarith
      · simp only [↓reduceIte]
        rw [inv_lt_one₀ (by linarith)]
        linarith

/-- **The prism push is a Δ-move provider with a PL track** (finite dimension). -/
theorem deltaPushProvider_PL (a b c : E) : DeltaPushProvider HasPLTrack a b c := by
  intro wa wb R' hsa hsb hta htb hR' hdisj
  obtain ⟨ι, _, φ, r, hr, ha, hb, hc, hA, hB, hR⟩ := exists_polyBody hsa hsb hta htb hR' hdisj
  exact pushData_of_polyBody φ r hr ha hb hc hA hB hR

/-- **A Δ-move is a PL ambient isotopy.** -/
theorem plAmbientIsotopic_of_delta (L L' : PolygonalLink E) (e : Fin L.k ≃ Fin L'.k)
    (m : Fin L.k) (c : E) (hother : ∀ i, i ≠ m → L'.comp (e i) = L.comp i)
    (hm : L'.comp (e m) = (L.comp m).subdivideLast c)
    (htri : convexHull ℝ {(L.comp m).v (Fin.last _), (L.comp m).v 0, c} ∩ L.carrier =
      segment ℝ ((L.comp m).v (Fin.last _)) ((L.comp m).v 0)) : PLAmbientIsotopic L L' :=
  exists_ambientIsotopy_of_delta HasPLTrack L L' e m c hother hm htri (deltaPushProvider_PL _ _ c)

/-- **Every move is a PL ambient isotopy.** -/
theorem Move.plAmbientIsotopic {L L' : PolygonalLink E} (h : Move L L') :
    PLAmbientIsotopic L L' := by
  cases h with
  | relabel e r h =>
    refine ⟨AmbientIsotopy.ofRelabel e r h, ?_⟩
    have : (AmbientIsotopy.ofRelabel e r h).track = Prod.snd := funext fun _ => rfl
    rw [this]
    exact IsPL.snd
  | delta e m c hother hm htri => exact plAmbientIsotopic_of_delta L L' e m c hother hm htri

/-- **Δ-equivalent polygonal links are PL ambient isotopic** (finite dimension). -/
theorem DeltaEquiv.plAmbientIsotopic {L L' : PolygonalLink E} (h : DeltaEquiv L L') :
    PLAmbientIsotopic L L' := by
  induction h with
  | rel _ _ h => exact h.plAmbientIsotopic
  | refl L => exact PLAmbientIsotopic.refl L
  | symm _ _ _ ih => exact ih.symm
  | trans _ _ _ _ _ ih₁ ih₂ => exact ih₁.trans ih₂

end Body

end QOU.MathlibExt.PL
