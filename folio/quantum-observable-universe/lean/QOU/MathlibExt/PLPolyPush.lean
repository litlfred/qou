/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLMaps
import QOU.MathlibExt.PLIsotopy
import QOU.MathlibExt.PLPush

set_option autoImplicit false

/-!
# The push of a polyhedral body is PL (issue #8902, stage 2, part 9)

For the Δ-move to be a **PL** isotopy, the body pushed across the triangle must be a polyhedron
and its gauge must be PL.

## What is a DEFINITION here

* `polySet φ r = {y | ∀ i, φ i y ≤ r i}` — a polyhedron given by finitely many linear
  inequalities with right-hand sides `r i > 0`, so `0` is interior.
* `polyGauge φ r y = max 0 (maxᵢ φ i y / r i)` (a `Finset.fold max 0`).

## What is a THEOREM here

* `gauge_polySet` — **the gauge of `polySet φ r` is `polyGauge φ r`.**
* `IsPL.max`, `IsPL.fold_max`, `IsPL.smul_const` — more closure of PL maps.
* `isPL_polyGauge`, `isPL_push_polySet` — the gauge and the push `x ↦ x + max 0 (1 - g x) • w`
  of a polyhedral body are PL.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E F : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F]

namespace IsPolyhedron

/-- A closed half-space bounded by an affine function. -/
lemma affine_le (A B : E →ᴬ[ℝ] ℝ) : IsPolyhedron {x | A x ≤ B x} := by
  have h := halfspace (A.contLinear - B.contLinear) (B 0 - A 0)
  convert h using 1
  ext x
  simp only [mem_setOf_eq, ContinuousLinearMap.sub_apply]
  rw [affine_apply_eq A x, affine_apply_eq B x]
  constructor <;> intro h <;> linarith

end IsPolyhedron

namespace IsPL

/-- **The maximum of two real PL functions is PL.** -/
lemma max {f g : E → ℝ} (hf : IsPL f) (hg : IsPL g) : IsPL (fun x => Max.max (f x) (g x)) := by
  obtain ⟨ι, _, K, A, hK, hKu, hfA⟩ := hf
  obtain ⟨κ, _, L, B, hL, hLu, hgB⟩ := hg
  refine ⟨ι × κ × Bool, inferInstance,
    fun p => K p.1 ∩ L p.2.1 ∩ (if p.2.2 then {x | B p.2.1 x ≤ A p.1 x} else {x | A p.1 x ≤ B p.2.1 x}),
    fun p => if p.2.2 then A p.1 else B p.2.1, fun p => ?_, ?_, ?_⟩
  · refine ((hK p.1).inter (hL p.2.1)).inter ?_
    split_ifs
    · exact IsPolyhedron.affine_le _ _
    · exact IsPolyhedron.affine_le _ _
  · refine eq_univ_of_forall fun x => ?_
    obtain ⟨i, hi⟩ := mem_iUnion.mp (hKu ▸ mem_univ x)
    obtain ⟨j, hj⟩ := mem_iUnion.mp (hLu ▸ mem_univ x)
    rcases le_total (B j x) (A i x) with h | h
    · exact mem_iUnion.mpr ⟨(i, j, true), ⟨hi, hj⟩, by simpa using h⟩
    · exact mem_iUnion.mpr ⟨(i, j, false), ⟨hi, hj⟩, by simpa using h⟩
  · rintro ⟨i, j, b⟩ x ⟨⟨hi, hj⟩, hb⟩
    cases b
    · simp only [Bool.false_eq_true, ↓reduceIte, mem_setOf_eq] at hb ⊢
      rw [hfA i hi, hgB j hj]
      exact max_eq_right hb
    · simp only [↓reduceIte, mem_setOf_eq] at hb ⊢
      rw [hfA i hi, hgB j hj]
      exact max_eq_left hb

/-- A finite `fold max` of real PL functions is PL. -/
lemma fold_max {ι : Type*} (s : Finset ι) (c : ℝ) {h : ι → E → ℝ} (hh : ∀ i, IsPL (h i)) :
    IsPL (fun x => s.fold Max.max c (fun i => h i x)) := by
  classical
  induction s using Finset.induction_on with
  | empty => simpa using IsPL.const (E := E) c
  | insert a s ha ih =>
    simp only [Finset.fold_insert ha]
    exact (hh a).max ih

/-- A real PL function times a fixed vector is PL. -/
lemma smul_const {f : E → ℝ} (hf : IsPL f) (w : F) : IsPL (fun x => f x • w) := by
  have h := (affine ((ContinuousLinearMap.id ℝ ℝ).smulRight w).toContinuousAffineMap).comp hf
  simpa [Function.comp_def] using h

lemma sub {f g : E → F} (hf : IsPL f) (hg : IsPL g) : IsPL (fun x => f x - g x) := by
  simpa [sub_eq_add_neg] using hf.add hg.neg

lemma clm (φ : E →L[ℝ] F) : IsPL φ := by
  simpa using affine φ.toContinuousAffineMap

end IsPL

variable {ι : Type} [Fintype ι] (φ : ι → E →L[ℝ] ℝ) (r : ι → ℝ)

/-- The polyhedron `{y | ∀ i, φ i y ≤ r i}`. -/
def polySet : Set E := {y | ∀ i, φ i y ≤ r i}

/-- `max 0 (maxᵢ φ i y / r i)`. -/
noncomputable def polyGauge (y : E) : ℝ := Finset.univ.fold Max.max 0 (fun i => φ i y / r i)

variable {φ r}

lemma isPolyhedron_polySet : IsPolyhedron (polySet φ r) :=
  ⟨ι, inferInstance, φ, r, rfl⟩

lemma polySet_mem_nhds (hr : ∀ i, 0 < r i) : polySet φ r ∈ nhds (0 : E) := by
  refine Filter.mem_of_superset ((isOpen_iInter_of_finite (s := fun i => {y : E | φ i y < r i})
    fun i => isOpen_lt (φ i).continuous continuous_const).mem_nhds ?_) ?_
  · simp only [mem_iInter, mem_setOf_eq, map_zero]
    exact hr
  · intro y hy
    simp only [mem_iInter, mem_setOf_eq] at hy
    exact fun i => (hy i).le

omit [Fintype ι] in
lemma convex_polySet [Finite ι] : Convex ℝ (polySet φ r) := by
  have : polySet φ r = ⋂ i, {y | φ i y ≤ r i} := by ext; simp [polySet]
  rw [this]
  exact convex_iInter fun i => convex_halfSpace_le (φ i).isLinear _

/-- **The gauge of a polyhedral body.** -/
theorem gauge_polySet (hr : ∀ i, 0 < r i) (y : E) : gauge (polySet φ r) y = polyGauge φ r y := by
  apply le_antisymm
  · refine le_of_forall_pos_le_add fun ε hε => ?_
    have hF : 0 ≤ polyGauge φ r y := (Finset.le_fold_max _).mpr (Or.inl le_rfl)
    set t := polyGauge φ r y + ε
    have ht : 0 < t := by positivity
    refine gauge_le_of_mem ht.le ⟨t⁻¹ • y, fun i => ?_, by simp [ht.ne']⟩
    have hi : φ i y / r i ≤ polyGauge φ r y :=
      (Finset.le_fold_max _).mpr (Or.inr ⟨i, Finset.mem_univ _, le_rfl⟩)
    rw [map_smul, smul_eq_mul, inv_mul_le_iff₀ ht]
    rw [div_le_iff₀ (hr i)] at hi
    nlinarith [hr i]
  · refine (Finset.fold_max_le _).mpr ⟨gauge_nonneg _, fun i _ => ?_⟩
    by_contra hlt
    push_neg at hlt
    obtain ⟨b, hb, hba, z, hz, rfl⟩ :=
      exists_lt_of_gauge_lt (absorbent_nhds_zero (polySet_mem_nhds hr)) hlt
    have := hz i
    rw [map_smul, smul_eq_mul, lt_div_iff₀ (hr i)] at hba
    nlinarith [hr i]

theorem isPL_polyGauge : IsPL (polyGauge φ r) :=
  IsPL.fold_max _ _ fun i => by
    convert IsPL.clm ((r i)⁻¹ • φ i) using 1
    funext x
    simp [div_eq_inv_mul]

/-- **The push of a polyhedral body is PL.** -/
theorem isPL_push_polySet (hr : ∀ i, 0 < r i) (w : E) : IsPL (push (polySet φ r) w) := by
  have hg : gauge (polySet φ r) = polyGauge φ r := funext (gauge_polySet hr)
  have h : IsPL (fun x => x + Max.max 0 (1 - polyGauge φ r x) • w) :=
    IsPL.id.add (((IsPL.const 0).max ((IsPL.const 1).sub isPL_polyGauge)).smul_const w)
  convert h using 1
  funext x
  simp only [push, pushCoef, hg]

end QOU.MathlibExt.PL
