/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLHomeo
import Mathlib.Topology.Algebra.ConstMulAction

set_option autoImplicit false

/-!
# The PL Alexander trick (issue #8902, Moise build part A)

A homeomorphism `h` of a finite-dimensional space that is PL and equal to the identity outside a
bounded set is PL isotopic to the identity, through `H t x = t • h (t⁻¹ • x)` (`H 0 = id`).

## Why the track is PL

On a piece `K` of `h`, where `h y = M y + b`, the track is `t • h (t⁻¹ • x) = M x + t • b`: affine
in `(t, x)`. The set where it applies, `{(t, x) | t⁻¹ • x ∈ K}`, is cut out by `φ x ≤ t * r` for the
half-spaces `φ ≤ r` of `K`: again a polyhedron. To make the pieces close up at `t = 0` they are
intersected with the cone `|c k x| ≤ t * R` over a box `|c k| ≤ R` outside which `h = id`; off that
cone the track is `x`. At `t = 0` the box cone is `{0}`.

## What is a DEFINITION here

* `alexFun f s x` — `x` if `s = 0`, else `s • f (s⁻¹ • x)`.
* `alexH h s` — the same, as a homeomorphism of `E`.

## What is a THEOREM here

* `IsPolyhedron.iInter` — a finite intersection of polyhedra is a polyhedron.
* `isPL_alexTrack` — for `f` PL with `f y = y` whenever some `|c k y| ≥ R` (`c` a separating
  finite family of functionals), the track `(t, x) ↦ alexFun f (clamp t) x` is PL.
* `plIsotopicToId_of_eq_outside` — **the PL Alexander trick**: in finite dimension, a
  homeomorphism that is PL in both directions and the identity outside a ball is PL isotopic to
  the identity.
* `PLAmbientIsotopic.of_eq_outside` — such a homeomorphism carrying `L` onto `L'` gives a PL
  ambient isotopy, with no further hypothesis.

## Literature

J. W. Alexander, *On the deformation of an n-cell*, Proc. Nat. Acad. Sci. 9 (1923) 406–407.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E F : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F]

lemma IsPolyhedron.iInter {κ : Type} [Fintype κ] {K : κ → Set E} (h : ∀ k, IsPolyhedron (K k)) :
    IsPolyhedron (⋂ k, K k) := by
  choose ι hι φ r hK using h
  haveI : ∀ k, Fintype (ι k) := hι
  refine ⟨Σ k, ι k, inferInstance, fun p => φ p.1 p.2, fun p => r p.1 p.2, ?_⟩
  ext x
  simp only [mem_iInter, mem_setOf_eq, Sigma.forall]
  constructor
  · intro hx k i
    have := hx k
    rw [hK k] at this
    exact this i
  · intro hx k
    rw [hK k]
    exact fun i => hx k i

lemma IsPolyhedron.of_iff (ψ : F →L[ℝ] ℝ) (a : ℝ) {P : F → Prop} (h : ∀ x, P x ↔ ψ x ≤ a) :
    IsPolyhedron {x | P x} := by
  have : {x | P x} = {x | ψ x ≤ a} := by ext x; exact h x
  rw [this]
  exact .halfspace ψ a

/-! ## The Alexander family -/

/-- The Alexander family as a function: `x` at `s = 0`, else `s • f (s⁻¹ • x)`. -/
noncomputable def alexFun (f : E → E) (s : ℝ) (x : E) : E :=
  if s = 0 then x else s • f (s⁻¹ • x)

lemma alexFun_zero (f : E → E) (x : E) : alexFun f 0 x = x := by simp [alexFun]

lemma alexFun_one (f : E → E) (x : E) : alexFun f 1 x = f x := by simp [alexFun]

lemma alexFun_of_ne (f : E → E) {s : ℝ} (hs : s ≠ 0) (x : E) :
    alexFun f s x = s • f (s⁻¹ • x) := by simp [alexFun, hs]

/-- The Alexander family as homeomorphisms: `x ↦ s • h (s⁻¹ • x)`, the identity at `s = 0`. -/
noncomputable def alexH (h : E ≃ₜ E) (s : ℝ) : E ≃ₜ E :=
  if hs : s = 0 then Homeomorph.refl E else
    ((Homeomorph.smulOfNeZero s⁻¹ (inv_ne_zero hs)).trans h).trans (Homeomorph.smulOfNeZero s hs)

lemma alexH_apply (h : E ≃ₜ E) (s : ℝ) (x : E) : alexH h s x = alexFun h s x := by
  by_cases hs : s = 0
  · simp [alexH, alexFun, hs]
  · simp [alexH, alexFun, hs]

lemma alexH_symm_apply (h : E ≃ₜ E) (s : ℝ) (x : E) :
    (alexH h s).symm x = alexFun h.symm s x := by
  by_cases hs : s = 0
  · simp [alexH, alexFun, hs]
  · simp [alexH, alexFun, hs, Homeomorph.smulOfNeZero, Units.smul_def]

/-! ## The track is PL -/

lemma clamp01_coe (t : ℝ) : (clamp01 t : ℝ) = max 0 (min 1 t) := by
  simp [clamp01, coe_projIcc]

lemma clamp01_of_nonpos {t : ℝ} (ht : t ≤ 0) : (clamp01 t : ℝ) = 0 := by
  rw [clamp01_coe]; rw [min_eq_right (by linarith)]; exact max_eq_left ht

lemma clamp01_of_one_le {t : ℝ} (ht : 1 ≤ t) : (clamp01 t : ℝ) = 1 := by
  rw [clamp01_coe, min_eq_left ht]; exact max_eq_right zero_le_one

lemma clamp01_of_mem {t : ℝ} (h0 : 0 ≤ t) (h1 : t ≤ 1) : (clamp01 t : ℝ) = t := by
  rw [clamp01_coe, min_eq_right h1]; exact max_eq_right h0

section track

variable {n : ℕ} (c : Fin n → E →L[ℝ] ℝ) (R : ℝ)

local notation "π₁" => ContinuousLinearMap.fst ℝ ℝ E
local notation "π₂" => ContinuousLinearMap.snd ℝ ℝ E

/-- `t ≤ 0`. -/
def lowSet : Set (ℝ × E) := {p | p.1 ≤ 0}

/-- `t ≥ 1` and `x ∈ K`. -/
def highSet (K : Set E) : Set (ℝ × E) := {p | 1 ≤ p.1 ∧ p.2 ∈ K}

/-- `0 ≤ t ≤ 1`, `φ i x ≤ t * r i` for all `i`, and `|c k x| ≤ t * R` for all `k`. -/
def coneSet {κ : Type} (φ : κ → E →L[ℝ] ℝ) (r : κ → ℝ) : Set (ℝ × E) :=
  {p | 0 ≤ p.1 ∧ p.1 ≤ 1 ∧ (∀ i, φ i p.2 ≤ p.1 * r i) ∧
    ∀ k, c k p.2 ≤ p.1 * R ∧ -c k p.2 ≤ p.1 * R}

/-- `0 ≤ t ≤ 1` and `t * R ≤ ψ x`. -/
def outSet (ψ : E →L[ℝ] ℝ) : Set (ℝ × E) := {p | 0 ≤ p.1 ∧ p.1 ≤ 1 ∧ p.1 * R ≤ ψ p.2}

lemma isPolyhedron_lowSet : IsPolyhedron (lowSet (E := E)) :=
  IsPolyhedron.of_iff π₁ 0 fun p => by simp

lemma isPolyhedron_highSet {K : Set E} (hK : IsPolyhedron K) : IsPolyhedron (highSet K) := by
  have : highSet K = {p : ℝ × E | 1 ≤ p.1} ∩ (π₂ : ℝ × E →L[ℝ] E).toContinuousAffineMap ⁻¹' K := by
    ext p; simp [highSet]
  rw [this]
  exact (IsPolyhedron.of_iff (-π₁) (-1) fun p => by simp).inter (hK.preimage _)

lemma isPolyhedron_slab : IsPolyhedron {p : ℝ × E | 0 ≤ p.1 ∧ p.1 ≤ 1} := by
  rw [setOf_and]
  exact (IsPolyhedron.of_iff (-π₁) 0 fun p => by simp).inter
    (IsPolyhedron.of_iff π₁ 1 fun p => by simp)

lemma isPolyhedron_coneSet {κ : Type} [Fintype κ] (φ : κ → E →L[ℝ] ℝ) (r : κ → ℝ) :
    IsPolyhedron (coneSet c R φ r) := by
  have : coneSet c R φ r = {p : ℝ × E | 0 ≤ p.1 ∧ p.1 ≤ 1} ∩
      ((⋂ i, {p : ℝ × E | φ i p.2 ≤ p.1 * r i}) ∩
        ⋂ k, ({p : ℝ × E | c k p.2 ≤ p.1 * R} ∩ {p : ℝ × E | -c k p.2 ≤ p.1 * R})) := by
    ext p; simp [coneSet, and_assoc]
  rw [this]
  refine isPolyhedron_slab.inter ((IsPolyhedron.iInter fun i => ?_).inter
    (IsPolyhedron.iInter fun k => (?_ : IsPolyhedron _).inter ?_))
  · exact IsPolyhedron.of_iff ((φ i).comp π₂ - r i • π₁) 0 fun p => by
      simp; constructor <;> intro h <;> linarith
  · exact IsPolyhedron.of_iff ((c k).comp π₂ - R • π₁) 0 fun p => by
      simp; constructor <;> intro h <;> linarith
  · exact IsPolyhedron.of_iff (-(c k).comp π₂ - R • π₁) 0 fun p => by
      simp; constructor <;> intro h <;> linarith

lemma isPolyhedron_outSet (ψ : E →L[ℝ] ℝ) : IsPolyhedron (outSet R ψ) := by
  have : outSet R ψ = {p : ℝ × E | 0 ≤ p.1 ∧ p.1 ≤ 1} ∩ {p | p.1 * R ≤ ψ p.2} := by
    ext p; simp [outSet, and_assoc]
  rw [this]
  exact isPolyhedron_slab.inter (IsPolyhedron.of_iff (R • π₁ - ψ.comp π₂) 0 fun p => by
    simp; constructor <;> intro h <;> linarith)

/-- **The Alexander track is PL.** `c` is a finite family of functionals with no common zero
but `0`, and `f` is the identity wherever some `|c k y| ≥ R`. -/
theorem isPL_alexTrack (hc : ∀ y, (∀ k, c k y = 0) → y = 0) {f : E → E} (hf : IsPL f)
    (hR : ∀ y, (∃ k, R ≤ |c k y|) → f y = y) :
    IsPL fun p : ℝ × E => alexFun f (clamp01 p.1 : ℝ) p.2 := by
  classical
  obtain ⟨ι, _, K, A, hK, hKu, hfA⟩ := hf
  choose κ hκ φ r hKeq using hK
  haveI : ∀ j, Fintype (κ j) := hκ
  -- the pieces
  let P : Unit ⊕ ι ⊕ ι ⊕ (Fin n ⊕ Fin n) → Set (ℝ × E) :=
    Sum.elim (fun _ => lowSet) (Sum.elim (fun j => highSet (K j))
      (Sum.elim (fun j => coneSet c R (φ j) (r j))
        (Sum.elim (fun k => outSet R (c k)) (fun k => outSet R (-c k)))))
  let B : Unit ⊕ ι ⊕ ι ⊕ (Fin n ⊕ Fin n) → ℝ × E →ᴬ[ℝ] E :=
    Sum.elim (fun _ => (π₂ : ℝ × E →L[ℝ] E).toContinuousAffineMap)
      (Sum.elim (fun j => (A j).comp (π₂ : ℝ × E →L[ℝ] E).toContinuousAffineMap)
        (Sum.elim (fun j => ((A j).contLinear.comp π₂ + (ContinuousLinearMap.fst ℝ ℝ E).smulRight (A j 0)).toContinuousAffineMap)
          (fun _ => (π₂ : ℝ × E →L[ℝ] E).toContinuousAffineMap)))
  refine ⟨_, inferInstance, P, B, ?_, ?_, ?_⟩
  · rintro (_ | j | j | k | k)
    · exact isPolyhedron_lowSet
    · exact isPolyhedron_highSet ⟨κ j, hκ j, φ j, r j, hKeq j⟩
    · exact isPolyhedron_coneSet c R (φ j) (r j)
    · exact isPolyhedron_outSet R (c k)
    · exact isPolyhedron_outSet R (-c k)
  · refine eq_univ_of_forall fun p => ?_
    obtain ⟨t, x⟩ := p
    simp only [mem_iUnion]
    rcases le_or_gt t 0 with ht0 | ht0
    · refine ⟨Sum.inl (), ?_⟩
      simp only [P, Sum.elim_inl, lowSet, mem_setOf_eq]
      exact ht0
    rcases le_or_gt 1 t with ht1 | ht1
    · obtain ⟨j, hj⟩ := mem_iUnion.mp (hKu ▸ mem_univ x)
      refine ⟨Sum.inr (Sum.inl j), ?_⟩
      simp only [P, Sum.elim_inl, Sum.elim_inr, highSet, mem_setOf_eq]
      exact ⟨ht1, hj⟩
    by_cases hp : ∃ k, t * R ≤ c k x
    · obtain ⟨k, hk⟩ := hp
      refine ⟨Sum.inr (Sum.inr (Sum.inr (Sum.inl k))), ?_⟩
      simp only [P, Sum.elim_inr, outSet]
      exact ⟨ht0.le, ht1.le, hk⟩
    by_cases hm : ∃ k, t * R ≤ -c k x
    · obtain ⟨k, hk⟩ := hm
      refine ⟨Sum.inr (Sum.inr (Sum.inr (Sum.inr k))), ?_⟩
      simp only [P, Sum.elim_inr, outSet, mem_setOf_eq]
      exact ⟨ht0.le, ht1.le, by simpa using hk⟩
    push_neg at hp hm
    obtain ⟨j, hj⟩ := mem_iUnion.mp (hKu ▸ mem_univ (t⁻¹ • x))
    rw [hKeq j, mem_setOf_eq] at hj
    refine ⟨Sum.inr (Sum.inr (Sum.inl j)), ?_⟩
    simp only [P, Sum.elim_inl, Sum.elim_inr, coneSet, mem_setOf_eq]
    refine ⟨ht0.le, ht1.le, fun i => ?_, fun k => ⟨(hp k).le, (hm k).le⟩⟩
    have := hj i
    rw [map_smul, smul_eq_mul, inv_mul_le_iff₀ ht0] at this
    exact this
  · rintro (_ | j | j | k | k) ⟨t, x⟩ hp
    · simp only [P, Sum.elim_inl, lowSet, mem_setOf_eq] at hp
      simp only [B, Sum.elim_inl]
      rw [clamp01_of_nonpos hp, alexFun_zero]
      simp
    · simp only [P, Sum.elim_inl, Sum.elim_inr, highSet, mem_setOf_eq] at hp
      simp only [B, Sum.elim_inr]
      rw [clamp01_of_one_le hp.1, alexFun_one]
      simp [hfA j hp.2]
    · simp only [P, Sum.elim_inl, Sum.elim_inr, coneSet, mem_setOf_eq] at hp
      simp only [B, Sum.elim_inr]
      obtain ⟨h0, h1, hφ, hck⟩ := hp
      rw [clamp01_of_mem h0 h1]
      rcases h0.eq_or_lt with rfl | ht
      · have hx : x = 0 := hc x fun k => by
          have := hck k
          simp only [zero_mul] at this
          linarith [this.1, this.2]
        subst hx
        simp [alexFun_zero]
      · rw [alexFun_of_ne _ ht.ne']
        have hmem : t⁻¹ • x ∈ K j := by
          rw [hKeq j, mem_setOf_eq]
          intro i
          rw [map_smul, smul_eq_mul, inv_mul_le_iff₀ ht]
          exact hφ i
        rw [hfA j hmem, affine_apply_eq (A j)]
        simp [smul_add, smul_smul, ht.ne']
    · simp only [P, Sum.elim_inr, outSet] at hp
      simp only [B, Sum.elim_inr]
      obtain ⟨h0, h1, hk⟩ := hp
      rw [clamp01_of_mem h0 h1]
      rcases h0.eq_or_lt with rfl | ht
      · simp [alexFun_zero]
      · rw [alexFun_of_ne _ ht.ne']
        have hfix : f (t⁻¹ • x) = t⁻¹ • x := by
          refine hR _ ⟨k, le_trans ?_ (le_abs_self _)⟩
          rw [map_smul, smul_eq_mul, le_inv_mul_iff₀ ht]
          exact hk
        rw [hfix, smul_smul, mul_inv_cancel₀ ht.ne', one_smul]
        simp
    · simp only [P, Sum.elim_inr, outSet, mem_setOf_eq] at hp
      simp only [B, Sum.elim_inr]
      obtain ⟨h0, h1, hk⟩ := hp
      rw [clamp01_of_mem h0 h1]
      rcases h0.eq_or_lt with rfl | ht
      · simp [alexFun_zero]
      · rw [alexFun_of_ne _ ht.ne']
        have hfix : f (t⁻¹ • x) = t⁻¹ • x := by
          refine hR _ ⟨k, le_trans ?_ (neg_le_abs _)⟩
          rw [map_smul, smul_eq_mul, ← mul_neg, le_inv_mul_iff₀ ht]
          simpa using hk
        rw [hfix, smul_smul, mul_inv_cancel₀ ht.ne', one_smul]
        simp

end track

/-! ## The Alexander trick -/

/-- **From PL Alexander tracks to a PL isotopy.** If the tracks of `h` and of `h⁻¹` are PL, then
`s ↦ alexH h s` is a PL isotopy from the identity to `h`. -/
theorem PLIsotopicToId.of_alexTrack (h : E ≃ₜ E)
    (hT : IsPL fun p : ℝ × E => alexFun h (clamp01 p.1 : ℝ) p.2)
    (hTs : IsPL fun p : ℝ × E => alexFun h.symm (clamp01 p.1 : ℝ) p.2) : PLIsotopicToId h := by
  have hval : ∀ s : unitInterval, (clamp01 (s : ℝ) : ℝ) = s := fun s => by
    rw [clamp01_of_mem s.2.1 s.2.2]
  have hemb : Continuous fun p : unitInterval × E => ((p.1 : ℝ), p.2) :=
    (continuous_subtype_val.comp continuous_fst).prodMk continuous_snd
  refine ⟨{ H := fun s => alexH h s
            continuous := ?_
            continuous_symm := ?_
            start := fun x => by simp [alexH_apply, alexFun_zero]
            finish := fun x => by simp [alexH_apply, alexFun_one]
            isPL := ?_ }⟩
  · convert hT.continuous.comp hemb using 1
    funext p
    simp only [Function.comp_apply, alexH_apply, hval]
  · convert hTs.continuous.comp hemb using 1
    funext p
    simp only [Function.comp_apply, alexH_symm_apply, hval]
  · convert hT using 1
    funext p
    exact alexH_apply _ _ _

/-- **The PL Alexander trick.** In finite dimension, a homeomorphism that is PL and the identity
outside a ball is PL isotopic to the identity. -/
theorem plIsotopicToId_of_eq_outside [FiniteDimensional ℝ E] (h : E ≃ₜ E) (hPL : IsPL h)
    (R : ℝ) (hR : ∀ y, R ≤ ‖y‖ → h y = y) : PLIsotopicToId h := by
  classical
  let b := Module.finBasis ℝ E
  let c : Fin (Module.finrank ℝ E) → E →L[ℝ] ℝ := fun k =>
    LinearMap.toContinuousLinearMap (b.coord k)
  have hc : ∀ y, (∀ k, c k y = 0) → y = 0 := fun y hy =>
    b.ext_elem fun k => by simpa [c] using hy k
  set S : ℝ := ∑ k, ‖c k‖ + 1 with hS
  have hSpos : 0 < S := by positivity
  have hR' : ∀ y, (∃ k, R * S ≤ |c k y|) → h y = y := by
    rintro y ⟨k, hk⟩
    apply hR
    by_contra hlt
    push_neg at hlt
    have hck : ‖c k‖ ≤ S := by
      rw [hS]
      have := Finset.single_le_sum (f := fun k => ‖c k‖) (fun k _ => norm_nonneg _)
        (Finset.mem_univ k)
      linarith
    have h1 : |c k y| ≤ ‖c k‖ * ‖y‖ := by
      rw [← Real.norm_eq_abs]; exact (c k).le_opNorm y
    have h2 : ‖c k‖ * ‖y‖ ≤ S * ‖y‖ := mul_le_mul_of_nonneg_right hck (norm_nonneg _)
    have h3 : S * ‖y‖ < S * R := mul_lt_mul_of_pos_left hlt hSpos
    linarith [mul_comm R S]
  have hR'' : ∀ y, (∃ k, R * S ≤ |c k y|) → h.symm y = y := fun y hy =>
    h.symm_apply_eq.mpr (hR' y hy).symm
  have hPLs : IsPL h.symm :=
    IsPL.of_leftInverse hPL (fun x => h.symm_apply_apply x) (fun y => h.apply_symm_apply y)
  have hT := isPL_alexTrack c (R * S) hc hPL hR'
  have hTs := isPL_alexTrack c (R * S) hc hPLs hR''
  have hval : ∀ s : unitInterval, (clamp01 (s : ℝ) : ℝ) = s := fun s => by
    rw [clamp01_of_mem s.2.1 s.2.2]
  refine ⟨{ H := fun s => alexH h s
            continuous := ?_
            continuous_symm := ?_
            start := fun x => by simp [alexH_apply, alexFun_zero]
            finish := fun x => by simp [alexH_apply, alexFun_one]
            isPL := ?_ }⟩
  · have hemb : Continuous fun p : unitInterval × E => ((p.1 : ℝ), p.2) :=
      (continuous_subtype_val.comp continuous_fst).prodMk continuous_snd
    have := hT.continuous.comp hemb
    convert this using 1
    funext p
    simp only [Function.comp_apply, alexH_apply, hval]
  · have hemb : Continuous fun p : unitInterval × E => ((p.1 : ℝ), p.2) :=
      (continuous_subtype_val.comp continuous_fst).prodMk continuous_snd
    have := hTs.continuous.comp hemb
    convert this using 1
    funext p
    simp only [Function.comp_apply, alexH_symm_apply, hval]
  · convert hT using 1
    funext p
    exact alexH_apply _ _ _

/-- **A compactly supported PL homeomorphism carrying `L` onto `L'` gives a PL ambient
isotopy.** No hypothesis beyond finite dimension. -/
theorem PLAmbientIsotopic.of_eq_outside [FiniteDimensional ℝ E] {L L' : PolygonalLink E}
    (h : E ≃ₜ E) (hPL : IsPL h) (R : ℝ) (hR : ∀ y, R ≤ ‖y‖ → h y = y)
    (e : Fin L.k ≃ Fin L'.k)
    (hfin : ∀ i, ∃ φ : ℝ → ℝ, OrientedReparam φ ∧
      ∀ t, h ((L.comp i).param t) = (L'.comp (e i)).param (φ t)) :
    PLAmbientIsotopic L L' :=
  PLAmbientIsotopic.of_plIsotopy (plIsotopicToId_of_eq_outside h hPL R hR).some e hfin

end QOU.MathlibExt.PL
