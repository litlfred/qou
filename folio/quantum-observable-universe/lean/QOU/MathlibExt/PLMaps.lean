/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Topology.Algebra.ContinuousAffineMap
import Mathlib.Topology.LocallyFinite
import Mathlib.Analysis.Normed.Module.FiniteDimension

set_option autoImplicit false

/-!
# Piecewise-linear maps (issue #8902, stage 2, part 7)

The PL category used to compare Δ-equivalence with PL isotopy.

## What is a DEFINITION here

* `IsPolyhedron K` — `K` is a finite intersection of closed half-spaces `{x | φ x ≤ r}`
  (`φ` continuous linear). Bounded or not.
* `IsPL f` — `f` is affine on each of finitely many polyhedra that cover the whole space.

## What is a THEOREM here

* Polyhedra: `univ`, half-spaces, intersections and affine preimages are polyhedra; polyhedra are
  closed.
* `IsPL.affine`, `IsPL.id`, `IsPL.comp`, `IsPL.continuous`.
* `IsPL.of_leftInverse` — in finite dimension, **the inverse of a PL bijection is PL.** Pieces
  without interior are discarded (a finite union of closed sets with empty interior has empty
  interior); on the others the affine map is injective, hence invertible.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E F G : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [NormedAddCommGroup G] [NormedSpace ℝ G]

/-- **A polyhedron**: a finite intersection of closed half-spaces. -/
def IsPolyhedron (K : Set E) : Prop :=
  ∃ (ι : Type) (_ : Fintype ι) (φ : ι → E →L[ℝ] ℝ) (r : ι → ℝ), K = {x | ∀ i, φ i x ≤ r i}

namespace IsPolyhedron

lemma univ : IsPolyhedron (Set.univ : Set E) :=
  ⟨Empty, inferInstance, Empty.elim, Empty.elim, by ext; simp⟩

lemma halfspace (φ : E →L[ℝ] ℝ) (r : ℝ) : IsPolyhedron {x | φ x ≤ r} :=
  ⟨Unit, inferInstance, fun _ => φ, fun _ => r, by ext; simp⟩

lemma inter {K L : Set E} (hK : IsPolyhedron K) (hL : IsPolyhedron L) :
    IsPolyhedron (K ∩ L) := by
  obtain ⟨ι, _, φ, r, rfl⟩ := hK
  obtain ⟨κ, _, ψ, s, rfl⟩ := hL
  refine ⟨ι ⊕ κ, inferInstance, Sum.elim φ ψ, Sum.elim r s, ?_⟩
  ext x
  simp [Sum.forall]

/-- An affine map is its linear part plus its value at `0`. -/
lemma _root_.QOU.MathlibExt.PL.affine_apply_eq (A : E →ᴬ[ℝ] F) (x : E) :
    A x = A.contLinear x + A 0 := by
  have := A.map_vadd 0 x
  simpa using this

lemma preimage {K : Set F} (hK : IsPolyhedron K) (A : E →ᴬ[ℝ] F) :
    IsPolyhedron (A ⁻¹' K) := by
  obtain ⟨ι, _, φ, r, rfl⟩ := hK
  refine ⟨ι, inferInstance, fun i => (φ i).comp A.contLinear, fun i => r i - φ i (A 0), ?_⟩
  ext x
  simp only [mem_preimage, mem_setOf_eq, ContinuousLinearMap.comp_apply, affine_apply_eq A x,
    map_add, le_sub_iff_add_le]

lemma isClosed {K : Set E} (hK : IsPolyhedron K) : IsClosed K := by
  obtain ⟨ι, _, φ, r, rfl⟩ := hK
  simp only [setOf_forall]
  exact isClosed_iInter fun i => isClosed_le (φ i).continuous continuous_const

end IsPolyhedron

/-- **A PL map**: affine on each of finitely many polyhedra covering the space. -/
def IsPL (f : E → F) : Prop :=
  ∃ (ι : Type) (_ : Fintype ι) (K : ι → Set E) (A : ι → E →ᴬ[ℝ] F),
    (∀ i, IsPolyhedron (K i)) ∧ (⋃ i, K i) = Set.univ ∧ ∀ i, EqOn f (A i) (K i)

namespace IsPL

lemma affine (A : E →ᴬ[ℝ] F) : IsPL A :=
  ⟨Unit, inferInstance, fun _ => Set.univ, fun _ => A, fun _ => IsPolyhedron.univ, iUnion_const _,
    fun _ => eqOn_refl _ _⟩

lemma id : IsPL (id : E → E) := by
  have := affine (ContinuousLinearMap.id ℝ E).toContinuousAffineMap
  simpa using this

lemma comp {g : F → G} {f : E → F} (hg : IsPL g) (hf : IsPL f) : IsPL (g ∘ f) := by
  obtain ⟨ι, _, K, A, hK, hKu, hfA⟩ := hf
  obtain ⟨κ, _, L, B, hL, hLu, hgB⟩ := hg
  refine ⟨ι × κ, inferInstance, fun p => K p.1 ∩ A p.1 ⁻¹' L p.2,
    fun p => (B p.2).comp (A p.1), fun p => (hK p.1).inter ((hL p.2).preimage _), ?_, ?_⟩
  · refine eq_univ_of_forall fun x => ?_
    obtain ⟨i, hi⟩ := mem_iUnion.mp (hKu ▸ mem_univ x)
    obtain ⟨j, hj⟩ := mem_iUnion.mp (hLu ▸ mem_univ (A i x))
    exact mem_iUnion.mpr ⟨(i, j), hi, hj⟩
  · rintro ⟨i, j⟩ x ⟨hi, hj⟩
    simp only [Function.comp_apply, ContinuousAffineMap.comp_apply, hfA i hi]
    exact hgB j hj

protected lemma continuous {f : E → F} (hf : IsPL f) : Continuous f := by
  obtain ⟨ι, _, K, A, hK, hKu, hfA⟩ := hf
  exact LocallyFinite.continuous (locallyFinite_of_finite K) hKu (fun i => (hK i).isClosed)
    (fun i => (A i).continuous.continuousOn.congr (hfA i))

end IsPL

omit [NormedSpace ℝ E] in
/-- A finite union of closed sets with empty interior has empty interior. -/
lemma interior_biUnion_eq_empty {ι : Type*} (s : Finset ι) (K : ι → Set E)
    (hc : ∀ i ∈ s, IsClosed (K i)) (he : ∀ i ∈ s, interior (K i) = ∅) :
    interior (⋃ i ∈ s, K i) = ∅ := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | insert j s hj ih =>
    have hcl : IsClosed (⋃ i ∈ s, K i) :=
      s.finite_toSet.isClosed_biUnion fun i hi => hc i (Finset.mem_insert_of_mem hi)
    rw [Finset.set_biUnion_insert, union_comm,
      interior_union_isClosed_of_interior_empty hcl (he j (Finset.mem_insert_self _ _))]
    exact ih (fun i hi => hc i (Finset.mem_insert_of_mem hi))
      (fun i hi => he i (Finset.mem_insert_of_mem hi))

/-- **The inverse of a PL bijection is PL** (finite dimension). -/
theorem IsPL.of_leftInverse [FiniteDimensional ℝ E] {f g : E → E} (hf : IsPL f)
    (hgf : Function.LeftInverse g f) (hfg : Function.RightInverse g f) : IsPL g := by
  classical
  obtain ⟨ι, _, K, A, hK, hKu, hfA⟩ := hf
  have hfinj : Function.Injective f := hgf.injective
  -- pieces with interior cover
  have hcover : ∀ x, ∃ i, (interior (K i)).Nonempty ∧ x ∈ K i := by
    by_contra h
    push_neg at h
    obtain ⟨x, hx⟩ := h
    set S := Finset.univ.filter (fun i => (interior (K i)).Nonempty)
    set T := Finset.univ.filter (fun i => ¬ (interior (K i)).Nonempty)
    have hSc : IsClosed (⋃ i ∈ S, K i) :=
      S.finite_toSet.isClosed_biUnion fun i _ => (hK i).isClosed
    have hxV : x ∈ (⋃ i ∈ S, K i)ᶜ := by
      simp only [mem_compl_iff, mem_iUnion, not_exists]
      intro i hi hxi
      exact hx i (Finset.mem_filter.mp hi).2 hxi
    have hsub : (⋃ i ∈ S, K i)ᶜ ⊆ ⋃ i ∈ T, K i := by
      intro y hy
      obtain ⟨i, hi⟩ := mem_iUnion.mp (hKu ▸ mem_univ y)
      by_cases hfat : (interior (K i)).Nonempty
      · exact absurd (mem_iUnion₂.mpr ⟨i, Finset.mem_filter.mpr ⟨Finset.mem_univ _, hfat⟩, hi⟩) hy
      · exact mem_iUnion₂.mpr ⟨i, Finset.mem_filter.mpr ⟨Finset.mem_univ _, hfat⟩, hi⟩
    have hT := interior_biUnion_eq_empty T K (fun i _ => (hK i).isClosed)
      (fun i hi => not_nonempty_iff_eq_empty.mp (Finset.mem_filter.mp hi).2)
    have : x ∈ interior (⋃ i ∈ T, K i) :=
      interior_mono hsub (hSc.isOpen_compl.interior_eq.symm ▸ hxV)
    rw [hT] at this
    exact this
  -- on a piece with interior the linear part is injective
  have hinj : ∀ i, (interior (K i)).Nonempty → Function.Injective (A i).contLinear := by
    rintro i ⟨p, hp⟩
    refine (injective_iff_map_eq_zero _).mpr fun v hv => ?_
    obtain ⟨ε, hε, hball⟩ := Metric.isOpen_iff.mp isOpen_interior p hp
    set t := ε / (2 * (‖v‖ + 1))
    have ht : 0 < t := by positivity
    have hq : p + t • v ∈ K i := by
      refine interior_subset (hball ?_)
      rw [Metric.mem_ball, dist_eq_norm, add_sub_cancel_left, norm_smul,
        Real.norm_of_nonneg ht.le]
      calc t * ‖v‖ ≤ t * (‖v‖ + 1) := by nlinarith [norm_nonneg v]
        _ = ε / 2 := by simp only [t]; field_simp
        _ < ε := half_lt_self hε
    have hpK : p ∈ K i := interior_subset hp
    have heq : f (p + t • v) = f p := by
      rw [hfA i hq, hfA i hpK, affine_apply_eq (A i) (p + t • v), affine_apply_eq (A i) p,
        map_add, map_smul, hv, smul_zero, add_zero]
    have h1 : t • v = 0 := by
      have := hfinj heq
      rwa [add_eq_left] at this
    exact (smul_eq_zero.mp h1).resolve_left ht.ne'
  -- the inverse affine pieces
  let Linv : ∀ i, (interior (K i)).Nonempty → E →L[ℝ] E := fun i hi =>
    LinearMap.toContinuousLinearMap
      (LinearEquiv.ofInjectiveEndo ((A i).contLinear : E →ₗ[ℝ] E) (hinj i hi)).symm.toLinearMap
  have hLinv1 : ∀ i hi (y : E), (A i).contLinear (Linv i hi y) = y := fun i hi y =>
    (LinearEquiv.ofInjectiveEndo ((A i).contLinear : E →ₗ[ℝ] E) (hinj i hi)).apply_symm_apply y
  have hLinv2 : ∀ i hi (x : E), Linv i hi ((A i).contLinear x) = x := fun i hi x =>
    (LinearEquiv.ofInjectiveEndo ((A i).contLinear : E →ₗ[ℝ] E) (hinj i hi)).symm_apply_apply x
  let B : ∀ i, (interior (K i)).Nonempty → E →ᴬ[ℝ] E := fun i hi =>
    (Linv i hi).toContinuousAffineMap + ContinuousAffineMap.const ℝ E (-(Linv i hi (A i 0)))
  have hB : ∀ i hi (y : E), B i hi y = Linv i hi y - Linv i hi (A i 0) := by
    intro i hi y
    simp [B, sub_eq_add_neg]
  have hAB : ∀ i hi (y : E), A i (B i hi y) = y := by
    intro i hi y
    rw [affine_apply_eq, hB i hi, map_sub, hLinv1 i hi, hLinv1 i hi, sub_add_cancel]
  have hBA : ∀ i hi (x : E), B i hi (A i x) = x := by
    intro i hi x
    rw [hB i hi, affine_apply_eq (A i) x, map_add, hLinv2 i hi, add_sub_cancel_right]
  refine ⟨{i // (interior (K i)).Nonempty}, inferInstance, fun j => B j.1 j.2 ⁻¹' K j.1,
    fun j => B j.1 j.2, fun j => (hK j.1).preimage _, ?_, ?_⟩
  · refine eq_univ_of_forall fun y => ?_
    obtain ⟨i, hi, hx⟩ := hcover (g y)
    refine mem_iUnion.mpr ⟨⟨i, hi⟩, ?_⟩
    show B i hi y ∈ K i
    have : y = A i (g y) := by rw [← hfA i hx, hfg y]
    rw [this, hBA i hi]
    exact hx
  · rintro ⟨i, hi⟩ y hy
    change B i hi y ∈ K i at hy
    show g y = B i hi y
    have : f (B i hi y) = y := by rw [hfA i hy, hAB i hi]
    conv_lhs => rw [← this]
    exact hgf _

end QOU.MathlibExt.PL
