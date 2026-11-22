/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLAlexander
import QOU.MathlibExt.PLLipschitz
import Mathlib.Data.Fintype.Pigeonhole

set_option autoImplicit false

/-!
# The scaling isotopy: a PL homeomorphism is PL isotopic to its cone at infinity
(issue #8902, Moise build part A)

For a PL map `f` with pieces `K j = {φ j i ≤ r j i}` and affine maps `A j = M j + b j`, the family
`t • f (t⁻¹ • x)` is affine in `(t, x)` on `{φ j i x ≤ t * r j i}` (it is `M j x + t • b j`), and as
`t → 0` it tends to the **cone map** `x ↦ M j x` on the recession cone `{φ j i ≤ 0}` of `K j`. The
recession cones of the nonempty pieces cover `E`, and two of them give the same value where they
meet because `f` is Lipschitz.

## What is a DEFINITION here

* `piece φ r j`, `rcone φ r j` — `{φ j i ≤ r j i}` and its recession cone `{φ j i ≤ 0}`.
* `coneMap φ r A hcov` — the cone map at infinity.
* `scalFun f G s x` — `G x` at `s = 0`, else `s • f (s⁻¹ • x)`.
* `ConePLIsotopyToId E` — every orientation-preserving PL homeomorphism of `E` that is **conical**
  (`g (s • x) = s • g x` for `s ≥ 0`) is PL isotopic to the identity. **A `Prop`, stated, not
  proved here.**

## What is a THEOREM here

* `rcone_cover`, `coneMap_eq` — the cone map is well defined (uses `IsPL.exists_lipschitz`).
* `isPL_scalTrack` — `(t, x) ↦ scalFun f (coneMap …) (clamp t) x` is PL.
* `plIsotopyToId_of_cone` — in finite dimension, `ConePLIsotopyToId E → PLIsotopyToId E`. The
  homeomorphism `h` is joined to its cone map `G` by the scaling isotopy; `G` is a conical,
  orientation-preserving PL homeomorphism with inverse the cone map of `h⁻¹`.

So the PL isotopy-to-identity gap of `PLHomeo.lean` reduces to conical maps, that is, to
orientation-preserving PL homeomorphisms of the sphere.
-/

namespace QOU.MathlibExt.PL

open Set Filter Topology

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

section pres

variable {ι : Type} [Fintype ι] {κ : ι → Type} [∀ j, Fintype (κ j)]
  (φ : (j : ι) → κ j → E →L[ℝ] ℝ) (r : (j : ι) → κ j → ℝ)

/-- The piece `{φ j i ≤ r j i}`. -/
def piece (j : ι) : Set E := {x | ∀ i, φ j i x ≤ r j i}

/-- Its recession cone `{φ j i ≤ 0}`. -/
def rcone (j : ι) : Set E := {x | ∀ i, φ j i x ≤ 0}

variable {φ r}

omit [Fintype ι] [∀ j, Fintype (κ j)] in
lemma add_smul_mem_piece {j : ι} {y x : E} (hy : y ∈ piece φ r j) (hx : x ∈ rcone φ j)
    {s : ℝ} (hs : 0 ≤ s) : y + s • x ∈ piece φ r j := fun i => by
  have := mul_nonpos_of_nonneg_of_nonpos hs (hx i)
  simp only [map_add, map_smul, smul_eq_mul]
  linarith [hy i]

omit [Fintype ι] [∀ j, Fintype (κ j)] in
lemma smul_mem_rcone {j : ι} {x : E} (hx : x ∈ rcone φ j) {s : ℝ} (hs : 0 ≤ s) :
    s • x ∈ rcone φ j := fun i => by
  simp only [map_smul, smul_eq_mul]
  exact mul_nonpos_of_nonneg_of_nonpos hs (hx i)

omit [∀ j, Fintype (κ j)] in
/-- **The recession cones of the nonempty pieces cover.** -/
theorem rcone_cover (hcov : ∀ x, ∃ j, x ∈ piece φ r j) (x : E) :
    ∃ j, (piece φ r j).Nonempty ∧ x ∈ rcone φ j := by
  classical
  choose J hJ using fun n : ℕ => hcov ((n : ℝ) • x)
  haveI : Nonempty ι := ⟨J 0⟩
  obtain ⟨j, hj⟩ := Finite.exists_infinite_fiber J
  have hinf : (J ⁻¹' {j}).Infinite := Set.infinite_coe_iff.mp hj
  obtain ⟨n₀, hn₀, -⟩ := hinf.exists_gt 0
  refine ⟨j, ⟨_, (show J n₀ = j from hn₀) ▸ hJ n₀⟩, fun i => ?_⟩
  by_contra hpos
  push_neg at hpos
  obtain ⟨n, hn, hlt⟩ := hinf.exists_gt ⌈r j i / φ j i x⌉₊
  have hmem := (show J n = j from hn) ▸ hJ n
  have h1 := hmem i
  rw [map_smul, smul_eq_mul] at h1
  have h2 : r j i / φ j i x < n := by
    have := Nat.le_ceil (r j i / φ j i x)
    exact lt_of_le_of_lt this (by exact_mod_cast hlt)
  rw [div_lt_iff₀ hpos] at h2
  linarith

variable (A : ι → E →ᴬ[ℝ] E)

omit [Fintype ι] [∀ j, Fintype (κ j)] in
/-- **Two recession cones give the same linear part where they meet** (for a Lipschitz `f`). -/
theorem linear_eq_of_rcone {f : E → E} (hfA : ∀ j, EqOn f (A j) (piece φ r j)) {C : ℝ}
    (hC : ∀ a b, ‖f b - f a‖ ≤ C * ‖b - a‖) {j l : ι} (hj : (piece φ r j).Nonempty)
    (hl : (piece φ r l).Nonempty) {x : E} (hxj : x ∈ rcone φ j) (hxl : x ∈ rcone φ l) :
    (A j).contLinear x = (A l).contLinear x := by
  obtain ⟨y, hy⟩ := hj
  obtain ⟨z, hz⟩ := hl
  set d := (A j).contLinear x - (A l).contLinear x
  set D := A j y - A l z
  have hbound : ∀ n : ℕ, (n : ℝ) * ‖d‖ ≤ C * ‖y - z‖ + ‖D‖ := by
    intro n
    have hy' := add_smul_mem_piece hy hxj (Nat.cast_nonneg n)
    have hz' := add_smul_mem_piece hz hxl (Nat.cast_nonneg n)
    have h := hC (z + (n : ℝ) • x) (y + (n : ℝ) • x)
    rw [hfA j hy', hfA l hz', affine_apply_eq (A j), affine_apply_eq (A l), map_add, map_add,
      map_smul, map_smul] at h
    have e : (A j).contLinear y + (n : ℝ) • (A j).contLinear x + A j 0 -
        ((A l).contLinear z + (n : ℝ) • (A l).contLinear x + A l 0) = D + (n : ℝ) • d := by
      simp only [D, d, affine_apply_eq (A j) y, affine_apply_eq (A l) z, smul_sub]
      abel
    rw [e, show y + (n : ℝ) • x - (z + (n : ℝ) • x) = y - z by abel] at h
    have h3 : ‖(n : ℝ) • d‖ ≤ ‖D + (n : ℝ) • d‖ + ‖D‖ := by
      have := norm_sub_le (D + (n : ℝ) • d) D
      rwa [add_sub_cancel_left] at this
    rw [norm_smul, Real.norm_natCast] at h3
    linarith
  have hd : ‖d‖ = 0 := by
    by_contra hne
    have hpos : 0 < ‖d‖ := lt_of_le_of_ne (norm_nonneg _) (Ne.symm hne)
    obtain ⟨n, hn⟩ := exists_nat_gt ((C * ‖y - z‖ + ‖D‖) / ‖d‖)
    rw [div_lt_iff₀ hpos] at hn
    linarith [hbound n]
  exact sub_eq_zero.mp (norm_eq_zero.mp hd)

/-- **The cone map at infinity.** -/
noncomputable def coneMap (hcov : ∀ x, ∃ j, x ∈ piece φ r j) (x : E) : E :=
  (A (rcone_cover hcov x).choose).contLinear x

omit [∀ j, Fintype (κ j)] in
theorem coneMap_eq {f : E → E} (hfA : ∀ j, EqOn f (A j) (piece φ r j)) {C : ℝ}
    (hC : ∀ a b, ‖f b - f a‖ ≤ C * ‖b - a‖) (hcov : ∀ x, ∃ j, x ∈ piece φ r j) {j : ι}
    (hj : (piece φ r j).Nonempty) {x : E} (hx : x ∈ rcone φ j) :
    coneMap A hcov x = (A j).contLinear x :=
  linear_eq_of_rcone A hfA hC (rcone_cover hcov x).choose_spec.1 hj
    (rcone_cover hcov x).choose_spec.2 hx

end pres

/-- The scaling family: `G x` at `s = 0`, else `s • f (s⁻¹ • x)`. -/
noncomputable def scalFun (f G : E → E) (s : ℝ) (x : E) : E :=
  if s = 0 then G x else s • f (s⁻¹ • x)

lemma scalFun_zero (f G : E → E) (x : E) : scalFun f G 0 x = G x := by simp [scalFun]

lemma scalFun_of_ne (f G : E → E) {s : ℝ} (hs : s ≠ 0) (x : E) :
    scalFun f G s x = s • f (s⁻¹ • x) := by simp [scalFun, hs]

lemma scalFun_one (f G : E → E) (x : E) : scalFun f G 1 x = f x := by simp [scalFun]

section track

variable {ι : Type} [Fintype ι] {κ : ι → Type} [∀ j, Fintype (κ j)]
  {φ : (j : ι) → κ j → E →L[ℝ] ℝ} {r : (j : ι) → κ j → ℝ} (A : ι → E →ᴬ[ℝ] E)

local notation "π₁" => ContinuousLinearMap.fst ℝ ℝ E
local notation "π₂" => ContinuousLinearMap.snd ℝ ℝ E

/-- **The scaling track is PL.** -/
theorem isPL_scalTrack {f : E → E} (hcov : ∀ x, ∃ j, x ∈ piece φ r j)
    (hfA : ∀ j, EqOn f (A j) (piece φ r j)) {C : ℝ} (hC : ∀ a b, ‖f b - f a‖ ≤ C * ‖b - a‖) :
    IsPL fun p : ℝ × E => scalFun f (coneMap A hcov) (clamp01 p.1 : ℝ) p.2 := by
  classical
  let N := {j // (piece φ r j).Nonempty}
  let P : ι ⊕ N ⊕ N → Set (ℝ × E) :=
    Sum.elim (fun j => highSet (piece φ r j))
      (Sum.elim (fun j => {p | 0 ≤ p.1 ∧ p.1 ≤ 1 ∧ ∀ i, φ j.1 i p.2 ≤ p.1 * r j.1 i})
        (fun j => {p | p.1 ≤ 0 ∧ ∀ i, φ j.1 i p.2 ≤ 0}))
  let B : ι ⊕ N ⊕ N → ℝ × E →ᴬ[ℝ] E :=
    Sum.elim (fun j => (A j).comp (π₂ : ℝ × E →L[ℝ] E).toContinuousAffineMap)
      (Sum.elim (fun j => ((A j.1).contLinear.comp π₂ +
          (ContinuousLinearMap.fst ℝ ℝ E).smulRight (A j.1 0)).toContinuousAffineMap)
        (fun j => ((A j.1).contLinear.comp π₂).toContinuousAffineMap))
  refine ⟨_, inferInstance, P, B, ?_, ?_, ?_⟩
  · rintro (j | j | j)
    · exact isPolyhedron_highSet ⟨κ j, inferInstance, φ j, r j, rfl⟩
    · have : {p : ℝ × E | 0 ≤ p.1 ∧ p.1 ≤ 1 ∧ ∀ i, φ j.1 i p.2 ≤ p.1 * r j.1 i} =
          {p : ℝ × E | 0 ≤ p.1 ∧ p.1 ≤ 1} ∩ ⋂ i, {p : ℝ × E | φ j.1 i p.2 ≤ p.1 * r j.1 i} := by
        ext p; simp [and_assoc]
      show IsPolyhedron {p : ℝ × E | 0 ≤ p.1 ∧ p.1 ≤ 1 ∧ ∀ i, φ j.1 i p.2 ≤ p.1 * r j.1 i}
      rw [this]
      exact isPolyhedron_slab.inter (IsPolyhedron.iInter fun i =>
        IsPolyhedron.of_iff ((φ j.1 i).comp π₂ - r j.1 i • π₁) 0 fun p => by
          simp; constructor <;> intro h <;> linarith)
    · have : {p : ℝ × E | p.1 ≤ 0 ∧ ∀ i, φ j.1 i p.2 ≤ 0} =
          {p : ℝ × E | p.1 ≤ 0} ∩ ⋂ i, {p : ℝ × E | φ j.1 i p.2 ≤ 0} := by
        ext p; simp
      show IsPolyhedron {p : ℝ × E | p.1 ≤ 0 ∧ ∀ i, φ j.1 i p.2 ≤ 0}
      rw [this]
      exact isPolyhedron_lowSet.inter (IsPolyhedron.iInter fun i =>
        IsPolyhedron.of_iff ((φ j.1 i).comp π₂) 0 fun p => by simp)
  · refine eq_univ_of_forall fun p => ?_
    obtain ⟨t, x⟩ := p
    simp only [mem_iUnion]
    rcases le_or_gt t 0 with ht0 | ht0
    · obtain ⟨j, hj, hx⟩ := rcone_cover hcov x
      refine ⟨Sum.inr (Sum.inr ⟨j, hj⟩), ?_⟩
      simp only [P, Sum.elim_inr, mem_setOf_eq]
      exact ⟨ht0, hx⟩
    rcases le_or_gt 1 t with ht1 | ht1
    · obtain ⟨j, hj⟩ := hcov x
      refine ⟨Sum.inl j, ?_⟩
      simp only [P, Sum.elim_inl, highSet, mem_setOf_eq]
      exact ⟨ht1, hj⟩
    obtain ⟨j, hj⟩ := hcov (t⁻¹ • x)
    refine ⟨Sum.inr (Sum.inl ⟨j, _, hj⟩), ?_⟩
    simp only [P, Sum.elim_inr, Sum.elim_inl, mem_setOf_eq]
    refine ⟨ht0.le, ht1.le, fun i => ?_⟩
    have := hj i
    rw [map_smul, smul_eq_mul, inv_mul_le_iff₀ ht0] at this
    exact this
  · rintro (j | j | j) ⟨t, x⟩ hp
    · simp only [P, Sum.elim_inl, highSet, mem_setOf_eq] at hp
      simp only [B, Sum.elim_inl]
      rw [clamp01_of_one_le hp.1, scalFun_one]
      simp [hfA j hp.2]
    · simp only [P, Sum.elim_inr, Sum.elim_inl, mem_setOf_eq] at hp
      simp only [B, Sum.elim_inr, Sum.elim_inl]
      obtain ⟨h0, h1, hφ⟩ := hp
      rw [clamp01_of_mem h0 h1]
      rcases h0.eq_or_lt with rfl | ht
      · rw [scalFun_zero, coneMap_eq A hfA hC hcov j.2 (fun i => by simpa using hφ i)]
        simp
      · rw [scalFun_of_ne _ _ ht.ne']
        have hmem : t⁻¹ • x ∈ piece φ r j.1 := fun i => by
          rw [map_smul, smul_eq_mul, inv_mul_le_iff₀ ht]
          exact hφ i
        rw [hfA j.1 hmem, affine_apply_eq (A j.1)]
        simp [smul_add, smul_smul, ht.ne']
    · simp only [P, Sum.elim_inr, mem_setOf_eq] at hp
      simp only [B, Sum.elim_inr]
      rw [clamp01_of_nonpos hp.1, scalFun_zero, coneMap_eq A hfA hC hcov j.2 hp.2]
      simp

end track

section main

/-- A PL map with an explicit half-space presentation of its pieces. -/
lemma IsPL.exists_pres {f : E → E} (hf : IsPL f) :
    ∃ (ι : Type) (_ : Fintype ι) (κ : ι → Type) (_ : ∀ j, Fintype (κ j))
      (φ : (j : ι) → κ j → E →L[ℝ] ℝ) (r : (j : ι) → κ j → ℝ) (A : ι → E →ᴬ[ℝ] E),
      (∀ x, ∃ j, x ∈ piece φ r j) ∧ ∀ j, EqOn f (A j) (piece φ r j) := by
  obtain ⟨ι, hι, K, A, hK, hKu, hfA⟩ := hf
  choose κ hκ φ r hKeq using hK
  refine ⟨ι, hι, κ, hκ, φ, r, A, fun x => ?_, fun j => ?_⟩
  · obtain ⟨j, hj⟩ := mem_iUnion.mp (hKu ▸ mem_univ x)
    exact ⟨j, by rw [hKeq j] at hj; exact hj⟩
  · have := hfA j
    rwa [hKeq j] at this

/-- The same, keeping the determinant condition of an orientation-preserving map. -/
lemma IsPL.OrientationPreserving.exists_pres {f : E → E} (hf : IsPL.OrientationPreserving f) :
    ∃ (ι : Type) (_ : Fintype ι) (κ : ι → Type) (_ : ∀ j, Fintype (κ j))
      (φ : (j : ι) → κ j → E →L[ℝ] ℝ) (r : (j : ι) → κ j → ℝ) (A : ι → E →ᴬ[ℝ] E),
      (∀ x, ∃ j, x ∈ piece φ r j) ∧ (∀ j, EqOn f (A j) (piece φ r j)) ∧
      ∀ j, (interior (piece φ r j)).Nonempty →
        0 < LinearMap.det ((A j).contLinear : E →ₗ[ℝ] E) := by
  obtain ⟨ι, hι, K, A, hK, hKu, hfA, hdet⟩ := hf
  choose κ hκ φ r hKeq using hK
  refine ⟨ι, hι, κ, hκ, φ, r, A, fun x => ?_, fun j => ?_, fun j hj => hdet j ?_⟩
  · obtain ⟨j, hj⟩ := mem_iUnion.mp (hKu ▸ mem_univ x)
    exact ⟨j, by rw [hKeq j] at hj; exact hj⟩
  · have := hfA j
    rwa [hKeq j] at this
  · rw [hKeq j]; exact hj

variable (E) in
/-- **Conical PL isotopy to the identity (stated, not proved).** Every orientation-preserving
homeomorphism of `E`, PL in both directions and conical (`g (s • x) = s • g x` for `s ≥ 0`), is PL
isotopic to the identity. Such a `g` is the cone on a PL homeomorphism of the unit sphere; for
`finrank ℝ E = 3` the statement is that orientation-preserving PL homeomorphisms of the 2-sphere
are PL isotopic to the identity, which follows from the PL Schoenflies theorem in the plane and
the Alexander trick (Moise, *Geometric Topology in Dimensions 2 and 3*, GTM 47, 1977). -/
def ConePLIsotopyToId : Prop :=
  ∀ g : E ≃ₜ E, IsPL.OrientationPreserving g → IsPL g.symm →
    (∀ s : ℝ, 0 ≤ s → ∀ x, g (s • x) = s • g x) → PLIsotopicToId g

lemma clamp01_zero : (clamp01 0 : ℝ) = 0 := clamp01_of_nonpos le_rfl

/-- **Reduction to conical maps.** In finite dimension, if every conical orientation-preserving
PL homeomorphism is PL isotopic to the identity, so is every orientation-preserving PL
homeomorphism. -/
theorem plIsotopyToId_of_cone [FiniteDimensional ℝ E] (hcone : ConePLIsotopyToId E) :
    PLIsotopyToId E := by
  classical
  intro h hor hinv
  obtain ⟨ι, _, κ, _, φ, r, A, hcov, hfA, hdet⟩ := hor.exists_pres
  obtain ⟨ι', _, κ', _, φ', r', A', hcov', hfA'⟩ := hinv.exists_pres
  obtain ⟨C, -, hC⟩ := hor.isPL.exists_lipschitz
  obtain ⟨C', -, hC'⟩ := hinv.exists_lipschitz
  set G := coneMap A hcov with hGdef
  set G' := coneMap A' hcov' with hG'def
  have hT := isPL_scalTrack A hcov hfA hC
  have hT' := isPL_scalTrack A' hcov' hfA' hC'
  have hGpl : IsPL G := by
    have := hT.comp ((IsPL.const (0 : ℝ)).prodMk IsPL.id)
    convert this using 1
    funext x
    simp [scalFun_zero, G]
  have hG'pl : IsPL G' := by
    have := hT'.comp ((IsPL.const (0 : ℝ)).prodMk IsPL.id)
    convert this using 1
    funext x
    simp [scalFun_zero, G']
  have hcl : (0 : ℝ) ∈ closure (Ioc (0 : ℝ) 1) := by
    rw [closure_Ioc zero_ne_one]; exact ⟨le_rfl, zero_le_one⟩
  have hinv1 : ∀ x, G (G' x) = x := by
    intro x
    have hψc : Continuous fun t : ℝ =>
        scalFun h G (clamp01 t) (scalFun h.symm G' (clamp01 t) x) :=
      hT.continuous.comp (continuous_id.prodMk
        (hT'.continuous.comp (continuous_id.prodMk continuous_const)))
    have hsub : Ioc (0 : ℝ) 1 ⊆
        {t | scalFun h G (clamp01 t) (scalFun h.symm G' (clamp01 t) x) = x} := by
      intro t ht
      simp only [mem_setOf_eq, clamp01_of_mem ht.1.le ht.2, scalFun_of_ne _ _ ht.1.ne',
        smul_smul, inv_mul_cancel₀ ht.1.ne', one_smul, Homeomorph.apply_symm_apply,
        mul_inv_cancel₀ ht.1.ne']
    have := (isClosed_eq hψc continuous_const).closure_subset_iff.mpr hsub hcl
    simpa [clamp01_zero, scalFun_zero] using this
  have hinv2 : ∀ x, G' (G x) = x := by
    intro x
    have hψc : Continuous fun t : ℝ =>
        scalFun h.symm G' (clamp01 t) (scalFun h G (clamp01 t) x) :=
      hT'.continuous.comp (continuous_id.prodMk
        (hT.continuous.comp (continuous_id.prodMk continuous_const)))
    have hsub : Ioc (0 : ℝ) 1 ⊆
        {t | scalFun h.symm G' (clamp01 t) (scalFun h G (clamp01 t) x) = x} := by
      intro t ht
      simp only [mem_setOf_eq, clamp01_of_mem ht.1.le ht.2, scalFun_of_ne _ _ ht.1.ne',
        smul_smul, inv_mul_cancel₀ ht.1.ne', one_smul, Homeomorph.symm_apply_apply,
        mul_inv_cancel₀ ht.1.ne']
    have := (isClosed_eq hψc continuous_const).closure_subset_iff.mpr hsub hcl
    simpa [clamp01_zero, scalFun_zero] using this
  let gH : E ≃ₜ E :=
    { toFun := G
      invFun := G'
      left_inv := hinv2
      right_inv := hinv1
      continuous_toFun := hGpl.continuous
      continuous_invFun := hG'pl.continuous }
  -- `G` is conical and orientation preserving
  have hconic : ∀ s : ℝ, 0 ≤ s → ∀ x, gH (s • x) = s • gH x := by
    intro s hs x
    obtain ⟨j, hj, hx⟩ := rcone_cover hcov x
    show G (s • x) = s • G x
    rw [hGdef, coneMap_eq A hfA hC hcov hj (smul_mem_rcone hx hs),
      coneMap_eq A hfA hC hcov hj hx, map_smul]
  have hOP : IsPL.OrientationPreserving gH := by
    refine ⟨{j // (piece φ r j).Nonempty}, inferInstance, fun j => rcone φ j.1,
      fun j => (A j.1).contLinear.toContinuousAffineMap, fun j => ⟨κ j.1, inferInstance, φ j.1,
      fun _ => 0, rfl⟩, ?_, fun j x hx => ?_, fun j hj => hdet j.1 ?_⟩
    · refine eq_univ_of_forall fun x => ?_
      obtain ⟨j, hj, hx⟩ := rcone_cover hcov x
      exact mem_iUnion.mpr ⟨⟨j, hj⟩, hx⟩
    · show G x = _
      rw [hGdef, coneMap_eq A hfA hC hcov j.2 hx]
      rfl
    · obtain ⟨y, hy⟩ := j.2
      obtain ⟨z, hz⟩ := hj
      refine ⟨y + z, interior_maximal (t := (fun u => y + u) '' interior (rcone φ j.1)) ?_
        (isOpenMap_add_left y _ isOpen_interior) ⟨z, hz, rfl⟩⟩
      rintro _ ⟨u, hu, rfl⟩
      simpa using add_smul_mem_piece hy (interior_subset hu) zero_le_one
  have hGsymm : IsPL gH.symm := hG'pl
  obtain ⟨I₁⟩ := hcone gH hOP hGsymm hconic
  -- the scaling isotopy, precomposed with `G⁻¹`
  let Hs : ℝ → E ≃ₜ E := fun s => if s = 0 then gH else alexH h s
  have hHs : ∀ s x, Hs s x = scalFun h G s x := by
    intro s x
    by_cases hs : s = 0
    · simp [Hs, hs, scalFun_zero, gH]
    · simp [Hs, hs, alexH_apply, alexFun_of_ne _ hs, scalFun_of_ne _ _ hs]
  have hHsym : ∀ s x, (Hs s).symm x = scalFun h.symm G' s x := by
    intro s x
    by_cases hs : s = 0
    · simp [Hs, hs, scalFun_zero, gH]
    · simp [Hs, hs, alexH_symm_apply, alexFun_of_ne _ hs, scalFun_of_ne _ _ hs]
  have hval : ∀ s : unitInterval, (clamp01 (s : ℝ) : ℝ) = s := fun s =>
    clamp01_of_mem s.2.1 s.2.2
  have hemb : Continuous fun p : unitInterval × E => ((p.1 : ℝ), p.2) :=
    (continuous_subtype_val.comp continuous_fst).prodMk continuous_snd
  let I₂ : PLIsotopy (gH.symm.trans h) :=
    { H := fun s => gH.symm.trans (Hs s)
      continuous := by
        have hemb' : Continuous fun p : unitInterval × E => ((p.1 : ℝ), G' p.2) :=
          (continuous_subtype_val.comp continuous_fst).prodMk
            (hG'pl.continuous.comp continuous_snd)
        have := hT.continuous.comp hemb'
        convert this using 1
        funext p
        simp only [Homeomorph.trans_apply, Function.comp_apply, hHs, hval]
        rfl
      continuous_symm := by
        have := hGpl.continuous.comp (hT'.continuous.comp hemb)
        convert this using 1
        funext p
        simp only [Homeomorph.symm_trans_apply, Function.comp_apply, hHsym, hval]
        rfl
      start := fun x => by
        simp only [Homeomorph.trans_apply, hHs, Set.Icc.coe_zero, scalFun_zero]
        exact hinv1 x
      finish := fun x => by
        simp only [Homeomorph.trans_apply, hHs, Set.Icc.coe_one, scalFun_one]
      isPL := by
        have := hT.comp (IsPL.fst.prodMk (hG'pl.comp IsPL.snd))
        convert this using 1
        funext p
        simp only [Homeomorph.trans_apply, Function.comp_apply, hHs]
        rfl }
  have hfin : gH.trans (gH.symm.trans h) = h := by
    ext x; simp
  rw [← hfin]
  exact ⟨I₁.trans I₂⟩

/-- **Orientation-preserving PL homeomorphisms carrying `L` onto `L'` give PL ambient
isotopies**, conditional on the conical statement only. -/
theorem PLAmbientIsotopic.of_plHomeo_of_cone [FiniteDimensional ℝ E]
    (hcone : ConePLIsotopyToId E) {L L' : PolygonalLink E} (h : E ≃ₜ E)
    (hor : IsPL.OrientationPreserving h) (hinv : IsPL h.symm) (e : Fin L.k ≃ Fin L'.k)
    (hfin : ∀ i, ∃ φ : ℝ → ℝ, OrientedReparam φ ∧
      ∀ t, h ((L.comp i).param t) = (L'.comp (e i)).param (φ t)) :
    PLAmbientIsotopic L L' :=
  PLAmbientIsotopic.of_plHomeo (plIsotopyToId_of_cone hcone) h hor hinv e hfin

end main

end QOU.MathlibExt.PL
