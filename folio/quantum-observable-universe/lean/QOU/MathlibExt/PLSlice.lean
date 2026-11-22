/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLLipschitz
import QOU.MathlibExt.PLPrismPush

set_option autoImplicit false

/-!
# Time slices of a planar polyhedron (issue #8902, stage 2: PL isotopy ⇒ Δ-equivalence)

For one edge `[a, b]` of a link moved by a PL ambient isotopy, the map
`(t, s) ↦ H_t (a + s (b - a))` is PL on `ℝ × ℝ` (`AmbientIsotopy.isPL_edgeTrack`). So the square
`[0, 1]²` is covered by finitely many polyhedra on which it is affine. This file describes the
**time slice** of one such polyhedron inside the strip `0 ≤ s ≤ 1`: at time `t` it is the
interval `[sliceLo t, sliceHi t]`, cut out by finitely many time-only conditions, and both
endpoints are **PL functions of `t`**.

## What is a THEOREM here

* `AmbientIsotopy.isPL_edgeTrack` — the edge track is PL.
* `slice_mem_iff` — `(t, s) ∈ polySet φ r` with `0 ≤ s ≤ 1` iff the time-only conditions hold at
  `t` and `sliceLo t ≤ s ≤ sliceHi t`.
* `isPL_sliceLo`, `isPL_sliceHi` — the slice endpoints are PL in `t`.

## What is NOT proved here

* Finiteness of the times at which slice endpoints tie, and the exact-image polygons between such
  times. These are the next steps towards `PLAmbientIsotopic.deltaEquiv`.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

namespace AmbientIsotopy

variable {L L' : PolygonalLink E}

/-- **The edge track is PL**: `(t, s) ↦ H_t (a + s • (b - a))`. -/
theorem isPL_edgeTrack (I : AmbientIsotopy L L') (h : IsPL I.track) (a b : E) :
    IsPL (fun p : ℝ × ℝ => I.track (p.1, a + p.2 • (b - a))) := by
  have hin : IsPL (fun p : ℝ × ℝ => (p.1, a + p.2 • (b - a))) :=
    IsPL.fst.prodMk ((IsPL.const a).add (IsPL.snd.smul_const (b - a)))
  exact h.comp hin

end AmbientIsotopy

/-! ### Slices -/

variable {ι : Type} [Fintype ι] (φ : ι → ℝ × ℝ →L[ℝ] ℝ) (r : ι → ℝ)

/-- Time coefficient of a constraint. -/
def tc (i : ι) : ℝ := φ i (1, 0)

/-- Space coefficient of a constraint. -/
def sc (i : ι) : ℝ := φ i (0, 1)

omit [Fintype ι] in
lemma apply_eq (i : ι) (t s : ℝ) : φ i (t, s) = tc φ i * t + sc φ i * s := by
  have : ((t, s) : ℝ × ℝ) = t • ((1 : ℝ), (0 : ℝ)) + s • ((0 : ℝ), (1 : ℝ)) := by
    ext <;> simp
  rw [this, map_add, map_smul, map_smul, smul_eq_mul, smul_eq_mul, tc, sc, mul_comm t,
    mul_comm s]

/-- Lower bound coming from constraint `i` (`0` if it gives none). -/
noncomputable def loTerm (i : ι) (t : ℝ) : ℝ :=
  if sc φ i < 0 then (r i - tc φ i * t) / sc φ i else 0

/-- Upper bound coming from constraint `i` (`1` if it gives none). -/
noncomputable def hiTerm (i : ι) (t : ℝ) : ℝ :=
  if 0 < sc φ i then (r i - tc φ i * t) / sc φ i else 1

/-- **Lower slice endpoint** in the strip `0 ≤ s ≤ 1`. -/
noncomputable def sliceLo (t : ℝ) : ℝ := Finset.univ.fold max 0 (fun i => loTerm φ r i t)

/-- **Upper slice endpoint** in the strip `0 ≤ s ≤ 1`. -/
noncomputable def sliceHi (t : ℝ) : ℝ := Finset.univ.fold min 1 (fun i => hiTerm φ r i t)

/-- The time-only conditions (constraints not involving `s`). -/
def timeOK (t : ℝ) : Prop := ∀ i, sc φ i = 0 → tc φ i * t ≤ r i

omit [Fintype ι] in
lemma constraint_iff (i : ι) {t s : ℝ} (hs0 : 0 ≤ s) (hs1 : s ≤ 1) :
    φ i (t, s) ≤ r i ↔
      (sc φ i = 0 → tc φ i * t ≤ r i) ∧ loTerm φ r i t ≤ s ∧ s ≤ hiTerm φ r i t := by
  rw [apply_eq]
  unfold loTerm hiTerm
  rcases lt_trichotomy (sc φ i) 0 with hn | hz | hp
  · rw [if_pos hn, if_neg (not_lt.2 hn.le), div_le_iff_of_neg hn]
    constructor
    · intro h; exact ⟨fun h0 => absurd h0 hn.ne, by linarith, hs1⟩
    · rintro ⟨-, h, -⟩; linarith
  · simp only [hz, lt_irrefl, if_false, zero_mul, add_zero, forall_const]
    exact ⟨fun h => ⟨h, hs0, hs1⟩, fun h => h.1⟩
  · rw [if_neg (not_lt.2 hp.le), if_pos hp, le_div_iff₀ hp]
    constructor
    · intro h; exact ⟨fun h0 => absurd h0 hp.ne', hs0, by linarith⟩
    · rintro ⟨-, -, h⟩; linarith

/-- **The slice of a polyhedron in the strip.** -/
theorem slice_mem_iff (t s : ℝ) :
    ((t, s) ∈ polySet φ r ∧ 0 ≤ s ∧ s ≤ 1) ↔ timeOK φ r t ∧ sliceLo φ r t ≤ s ∧ s ≤ sliceHi φ r t := by
  unfold sliceLo sliceHi timeOK polySet
  rw [Finset.fold_max_le, Finset.le_fold_min]
  simp only [Finset.mem_univ, forall_const, mem_setOf_eq]
  constructor
  · rintro ⟨h, hs0, hs1⟩
    have hc := fun i => (constraint_iff φ r i hs0 hs1).1 (h i)
    exact ⟨fun i => (hc i).1, ⟨hs0, fun i => (hc i).2.1⟩, ⟨hs1, fun i => (hc i).2.2⟩⟩
  · rintro ⟨ht, ⟨hs0, hlo⟩, ⟨hs1, hhi⟩⟩
    exact ⟨fun i => (constraint_iff φ r i hs0 hs1).2 ⟨ht i, hlo i, hhi i⟩, hs0, hs1⟩

omit [Fintype ι] in
lemma isPL_ratio (i : ι) : IsPL (fun t : ℝ => (r i - tc φ i * t) / sc φ i) := by
  have h := (IsPL.const (E := ℝ) (r i / sc φ i)).add (IsPL.id.smul_const (-(tc φ i) / sc φ i))
  convert h using 1
  funext t
  simp only [id, smul_eq_mul]
  ring

/-- **The lower slice endpoint is PL in time.** -/
theorem isPL_sliceLo : IsPL (sliceLo φ r) := by
  refine IsPL.fold_max _ _ (fun i => ?_)
  unfold loTerm
  split_ifs
  · exact isPL_ratio φ r i
  · exact IsPL.const 0

omit [Fintype ι] in
/-- A finite `fold min` of real PL functions is PL. -/
lemma isPL_fold_min {κ : Type*} (S : Finset κ) (c : ℝ) {h : κ → ℝ → ℝ} (hh : ∀ i, IsPL (h i)) :
    IsPL (fun x => S.fold min c (fun i => h i x)) := by
  classical
  induction S using Finset.induction_on with
  | empty => simpa using IsPL.const (E := ℝ) c
  | insert a S ha ih =>
    simp only [Finset.fold_insert ha]
    exact (hh a).min ih

/-- **The upper slice endpoint is PL in time.** -/
theorem isPL_sliceHi : IsPL (sliceHi φ r) := by
  refine isPL_fold_min _ _ (fun i => ?_)
  unfold hiTerm
  split_ifs
  · exact isPL_ratio φ r i
  · exact IsPL.const 1

end QOU.MathlibExt.PL
