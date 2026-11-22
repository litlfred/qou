/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLAlexander
import QOU.MathlibExt.PLLipschitzPiecewise
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

## What is a THEOREM here

* `rcone_cover`, `coneMap_eq` — the cone map is well defined (uses `IsPL.exists_lipschitz`).
* `isPL_scalTrack` — `(t, x) ↦ scalFun f (coneMap …) (clamp t) x` is PL.
* `coneMap_eq_self_of_bounded` — at bounded distance from the identity the cone map is `id`.
* `plIsotopicToId_of_bounded` — in finite dimension, a homeomorphism that is PL and at bounded
  distance from the identity is PL isotopic to the identity.
* `PLIsotopicToId.exists_bound` — conversely a PL track is Lipschitz, so the end map is at bounded
  distance from the identity. Together: `plIsotopicToId_iff_bounded`.
* `not_plIsotopicToId_two_smul` — `x ↦ 2 • x` is not PL isotopic to the identity.
* `PLAmbientIsotopic.of_bounded` — a bounded-displacement PL homeomorphism carrying `L` onto `L'`
  gives a PL ambient isotopy, with no further hypothesis.

## Correction (2026-11-22)

An earlier version of this file stated `ConePLIsotopyToId E` and `PLHomeo.lean` stated
`PLIsotopyToId E` ("every orientation-preserving PL homeomorphism is PL isotopic to the
identity") as named gaps. Both are **false** here: a PL track has finitely many affine pieces on
`ℝ × E`, hence is Lipschitz, hence moves every point by a bounded amount, and `x ↦ 2 • x` does
not (`not_plIsotopicToId_two_smul`). They have been removed. The Moise assembly needs a PL
homeomorphism at bounded distance from the identity (for example compactly supported).
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

lemma clamp01_zero : (clamp01 0 : ℝ) = 0 := clamp01_of_nonpos le_rfl

/-- **At bounded distance from the identity, the cone map is the identity.** -/
theorem coneMap_eq_self_of_bounded {ι : Type} [Fintype ι] {κ : ι → Type}
    {φ : (j : ι) → κ j → E →L[ℝ] ℝ} {r : (j : ι) → κ j → ℝ} (A : ι → E →ᴬ[ℝ] E) {f : E → E}
    (hcov : ∀ x, ∃ j, x ∈ piece φ r j) (hfA : ∀ j, EqOn f (A j) (piece φ r j)) {B : ℝ}
    (hb : ∀ x, ‖f x - x‖ ≤ B) (x : E) : coneMap A hcov x = x := by
  obtain ⟨⟨y, hy⟩, hx⟩ := (rcone_cover hcov x).choose_spec
  set j := (rcone_cover hcov x).choose
  show (A j).contLinear x = x
  set d := (A j).contLinear x - x
  have hbound : ∀ n : ℕ, (n : ℝ) * ‖d‖ ≤ B + ‖A j y - y‖ := by
    intro n
    have hy' := add_smul_mem_piece hy hx (Nat.cast_nonneg n)
    have h := hb (y + (n : ℝ) • x)
    rw [hfA j hy', affine_apply_eq (A j), map_add, map_smul] at h
    have e : (A j).contLinear y + (n : ℝ) • (A j).contLinear x + A j 0 - (y + (n : ℝ) • x) =
        (A j y - y) + (n : ℝ) • d := by
      simp only [d, affine_apply_eq (A j) y, smul_sub]
      abel
    rw [e] at h
    have h3 : ‖(n : ℝ) • d‖ ≤ ‖(A j y - y) + (n : ℝ) • d‖ + ‖A j y - y‖ := by
      have := norm_sub_le ((A j y - y) + (n : ℝ) • d) (A j y - y)
      rwa [add_sub_cancel_left] at this
    rw [norm_smul, Real.norm_natCast] at h3
    linarith
  have hd : ‖d‖ = 0 := by
    by_contra hne
    have hpos : 0 < ‖d‖ := lt_of_le_of_ne (norm_nonneg _) (Ne.symm hne)
    obtain ⟨n, hn⟩ := exists_nat_gt ((B + ‖A j y - y‖) / ‖d‖)
    rw [div_lt_iff₀ hpos] at hn
    linarith [hbound n]
  exact sub_eq_zero.mp (norm_eq_zero.mp hd)

/-- **The Alexander track of a PL map at bounded distance from the identity is PL.** -/
theorem isPL_alexTrack_of_bounded {f : E → E} (hf : IsPL f) {B : ℝ}
    (hb : ∀ x, ‖f x - x‖ ≤ B) :
    IsPL fun p : ℝ × E => alexFun f (clamp01 p.1 : ℝ) p.2 := by
  obtain ⟨ι, _, κ, _, φ, r, A, hcov, hfA⟩ := hf.exists_pres
  obtain ⟨C, -, hC⟩ := hf.exists_lipschitz
  have hT := isPL_scalTrack A hcov hfA hC
  convert hT using 1
  funext p
  by_cases hs : (clamp01 p.1 : ℝ) = 0
  · rw [hs, alexFun_zero, scalFun_zero, coneMap_eq_self_of_bounded A hcov hfA hb]
  · rw [alexFun_of_ne _ hs, scalFun_of_ne _ _ hs]

/-- **A homeomorphism, PL and at bounded distance from the identity, is PL isotopic to the
identity** (finite dimension), through `t • h (t⁻¹ • x)`. -/
theorem plIsotopicToId_of_bounded [FiniteDimensional ℝ E] (h : E ≃ₜ E) (hPL : IsPL h) {B : ℝ}
    (hb : ∀ x, ‖h x - x‖ ≤ B) : PLIsotopicToId h := by
  have hPLs : IsPL h.symm :=
    IsPL.of_leftInverse hPL (fun x => h.symm_apply_apply x) (fun y => h.apply_symm_apply y)
  have hbs : ∀ y, ‖h.symm y - y‖ ≤ B := fun y => by
    have := hb (h.symm y)
    rwa [h.apply_symm_apply, norm_sub_rev] at this
  exact PLIsotopicToId.of_alexTrack h (isPL_alexTrack_of_bounded hPL hb)
    (isPL_alexTrack_of_bounded hPLs hbs)

/-- **A homeomorphism PL isotopic to the identity is at bounded distance from it**: the track is
Lipschitz on `ℝ × E`. -/
theorem PLIsotopicToId.exists_bound {h : E ≃ₜ E} (hh : PLIsotopicToId h) :
    ∃ B, ∀ x, ‖h x - x‖ ≤ B := by
  obtain ⟨I⟩ := hh
  obtain ⟨C, -, hC⟩ := I.isPL.exists_lipschitz
  refine ⟨C, fun x => ?_⟩
  have h1 : clamp01 1 = 1 := Subtype.ext (clamp01_of_one_le le_rfl)
  have h0 : clamp01 0 = 0 := Subtype.ext clamp01_zero
  have := hC ((0 : ℝ), x) ((1 : ℝ), x)
  simp only [h1, h0, I.start, I.finish] at this
  have hn : ‖((1 : ℝ), x) - ((0 : ℝ), x)‖ = 1 := by simp
  rwa [hn, mul_one] at this

/-- **PL isotopy to the identity is bounded displacement** (finite dimension). -/
theorem plIsotopicToId_iff_bounded [FiniteDimensional ℝ E] (h : E ≃ₜ E) (hPL : IsPL h) :
    PLIsotopicToId h ↔ ∃ B, ∀ x, ‖h x - x‖ ≤ B :=
  ⟨PLIsotopicToId.exists_bound, fun ⟨_, hb⟩ => plIsotopicToId_of_bounded h hPL hb⟩

/-- **`x ↦ 2 • x` is not PL isotopic to the identity**, although it is linear, PL both ways and
orientation preserving: its displacement `‖x‖` is unbounded. So "every orientation-preserving PL
homeomorphism is PL isotopic to the identity" is false for the finitely-many-pieces PL tracks used
here. -/
theorem not_plIsotopicToId_two_smul [Nontrivial E] :
    ¬ PLIsotopicToId (Homeomorph.smulOfNeZero (2 : ℝ) two_ne_zero : E ≃ₜ E) := by
  intro hh
  obtain ⟨B, hB⟩ := hh.exists_bound
  obtain ⟨v, hv⟩ := exists_ne (0 : E)
  have hvpos : 0 < ‖v‖ := norm_pos_iff.mpr hv
  set c : ℝ := (|B| + 1) / ‖v‖
  have hc : 0 < c := by positivity
  have := hB (c • v)
  simp only [Homeomorph.smulOfNeZero_apply, smul_smul] at this
  rw [show (2 : ℝ) * c = c + c by ring, add_smul, add_sub_cancel_right, norm_smul,
    Real.norm_of_nonneg hc.le, div_mul_cancel₀ _ hvpos.ne'] at this
  linarith [le_abs_self B]

/-- **A PL homeomorphism at bounded distance from the identity carrying `L` onto `L'` gives a PL
ambient isotopy.** No gap. -/
theorem PLAmbientIsotopic.of_bounded [FiniteDimensional ℝ E] {L L' : PolygonalLink E}
    (h : E ≃ₜ E) (hPL : IsPL h) {B : ℝ} (hb : ∀ x, ‖h x - x‖ ≤ B) (e : Fin L.k ≃ Fin L'.k)
    (hfin : ∀ i, ∃ φ : ℝ → ℝ, OrientedReparam φ ∧
      ∀ t, h ((L.comp i).param t) = (L'.comp (e i)).param (φ t)) :
    PLAmbientIsotopic L L' :=
  PLAmbientIsotopic.of_plIsotopy (plIsotopicToId_of_bounded h hPL hb).some e hfin

end main

end QOU.MathlibExt.PL
