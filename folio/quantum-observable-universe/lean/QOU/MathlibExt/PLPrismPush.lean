/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLPolyPush
import QOU.MathlibExt.PLDeltaMove

set_option autoImplicit false

/-!
# The prism push: a PL isotopy across a polyhedral body (issue #8902, stage 2, part 10)

The family `s ↦ push S (s • v)` is not PL in `(s, x)` jointly: its coefficient is `s` times a
PL function. Instead, push the centre of the **prism** `S' = [-1, 1] × S ⊆ ℝ × E` in the
direction `(0, v)`. The gauge of `S'` is `max |τ| (gauge S y)`, so the push of `S'` is PL, it
preserves the first coordinate, and its slice at `τ = s - 1` is a homeomorphism `H s` of `E`
with `H 0 = id` and `H 1 = push S v`.

## What is a DEFINITION here

* `prismφ`, `prismr` — the inequalities of `S'` (`±τ ≤ 1`, `φ i y ≤ r i`).
* `prismIso m s` — the slice homeomorphism, conjugated by the translation to `m`.

## What is a THEOREM here

* `gauge_prism` — the gauge of `S'` is `max |τ| (gauge S y)`.
* `prismIso_apply`, `prismIso_zero`, `prismIso_one`, `continuous_prismIso`,
  `continuous_prismIso_symm` — `prismIso` is an isotopy from the identity to
  `x ↦ m + push S v (x - m)`.
* `isPL_prismIso_track` — **its track `(t, x) ↦ prismIso m (clamp t) x` is PL.**
* `pushData_of_polyBody` — a polyhedral body around the Δ-triangle with `a`, `b` on its
  boundary, `c` inside, missing the edge rays and the rest of the link, gives a push provider
  whose isotopy has a PL track.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

namespace IsPL

lemma min {f g : E → ℝ} (hf : IsPL f) (hg : IsPL g) : IsPL (fun x => Min.min (f x) (g x)) := by
  have h := (hf.neg.max hg.neg).neg
  convert h using 1
  funext x
  simp only [max_neg_neg, neg_neg]


/-- The clamp of `ℝ` onto `[0, 1]`, as a real function, is PL. -/
lemma clamp01 : IsPL (fun t : ℝ => ((clamp01 t : unitInterval) : ℝ)) := by
  have h := (IsPL.const (E := ℝ) (0 : ℝ)).max ((IsPL.const 1).min IsPL.id)
  convert h using 1

end IsPL

variable {ι : Type} [Fintype ι] {φ : ι → E →L[ℝ] ℝ} {r : ι → ℝ}

/-- The inequalities of the prism `[-1, 1] × polySet φ r`. -/
noncomputable def prismφ (φ : ι → E →L[ℝ] ℝ) : Bool ⊕ ι → (ℝ × E) →L[ℝ] ℝ
  | .inl true => ContinuousLinearMap.fst ℝ ℝ E
  | .inl false => -ContinuousLinearMap.fst ℝ ℝ E
  | .inr i => (φ i).comp (ContinuousLinearMap.snd ℝ ℝ E)

/-- Right-hand sides of the prism. -/
def prismr (r : ι → ℝ) : Bool ⊕ ι → ℝ
  | .inl _ => 1
  | .inr i => r i

omit [Fintype ι] in
lemma prismr_pos (hr : ∀ i, 0 < r i) (j : Bool ⊕ ι) : 0 < prismr r j := by
  cases j with
  | inl b => exact one_pos
  | inr i => exact hr i

/-- **The gauge of the prism.** -/
theorem gauge_prism (hr : ∀ i, 0 < r i) (τ : ℝ) (y : E) :
    gauge (polySet (prismφ φ) (prismr r)) (τ, y) = Max.max |τ| (gauge (polySet φ r) y) := by
  rw [gauge_polySet (prismr_pos hr), gauge_polySet hr]
  apply le_antisymm
  · refine (Finset.fold_max_le _).mpr ⟨le_max_of_le_left (abs_nonneg τ), fun j _ => ?_⟩
    rcases j with (_ | _) | i
    · simp only [prismφ, prismr, ContinuousLinearMap.neg_apply, ContinuousLinearMap.coe_fst',
        div_one]
      exact le_max_of_le_left (neg_le_abs τ)
    · simp only [prismφ, prismr, ContinuousLinearMap.coe_fst', div_one]
      exact le_max_of_le_left (le_abs_self τ)
    · simp only [prismφ, prismr, ContinuousLinearMap.coe_comp', Function.comp_apply,
        ContinuousLinearMap.coe_snd']
      exact le_max_of_le_right ((Finset.le_fold_max _).mpr (Or.inr ⟨i, Finset.mem_univ _, le_rfl⟩))
  · refine max_le ?_ ((Finset.fold_max_le _).mpr ⟨(Finset.le_fold_max _).mpr (Or.inl le_rfl),
      fun i _ => (Finset.le_fold_max _).mpr (Or.inr ⟨.inr i, Finset.mem_univ _, ?_⟩)⟩)
    · rcases le_total 0 τ with h | h
      · refine (Finset.le_fold_max _).mpr (Or.inr ⟨.inl true, Finset.mem_univ _, ?_⟩)
        simp [prismφ, prismr, abs_of_nonneg h]
      · refine (Finset.le_fold_max _).mpr (Or.inr ⟨.inl false, Finset.mem_univ _, ?_⟩)
        simp [prismφ, prismr, abs_of_nonpos h]
    · simp [prismφ, prismr]

section Prism

variable (hr : ∀ i, 0 < r i) {v : E} (hv : gauge (polySet φ r) v < 1)
include hr hv

lemma gauge_prism_dir : gauge (polySet (prismφ φ) (prismr r)) ((0 : ℝ), v) < 1 := by
  rw [gauge_prism hr, abs_zero, max_eq_right (gauge_nonneg _)]
  exact hv

/-- The push of the prism, a homeomorphism of `ℝ × E`. -/
noncomputable def prismPush : ℝ × E ≃ₜ ℝ × E :=
  pushHomeomorph convex_polySet (polySet_mem_nhds (prismr_pos hr)) (gauge_prism_dir hr hv)

lemma prismPush_apply (τ : ℝ) (y : E) : prismPush hr hv (τ, y) =
    (τ, y + pushCoef (polySet (prismφ φ) (prismr r)) (τ, y) • v) := by
  simp [prismPush, pushHomeomorph_apply, push]

lemma prismPush_fst (p : ℝ × E) : (prismPush hr hv p).1 = p.1 := by
  obtain ⟨τ, y⟩ := p
  rw [prismPush_apply]

lemma prismPush_symm_fst (p : ℝ × E) : ((prismPush hr hv).symm p).1 = p.1 := by
  conv_rhs => rw [← (prismPush hr hv).apply_symm_apply p]
  rw [prismPush_fst]

/-- The slice of the prism push at height `τ`. -/
noncomputable def prismSlice (τ : ℝ) : E ≃ₜ E where
  toFun y := (prismPush hr hv (τ, y)).2
  invFun y := ((prismPush hr hv).symm (τ, y)).2
  left_inv y := by
    have e : (τ, (prismPush hr hv (τ, y)).2) = prismPush hr hv (τ, y) :=
      Prod.ext (prismPush_fst hr hv (τ, y)).symm rfl
    simp only
    rw [e, Homeomorph.symm_apply_apply]
  right_inv y := by
    have e : (τ, ((prismPush hr hv).symm (τ, y)).2) = (prismPush hr hv).symm (τ, y) :=
      Prod.ext (prismPush_symm_fst hr hv (τ, y)).symm rfl
    simp only
    rw [e, Homeomorph.apply_symm_apply]
  continuous_toFun := continuous_snd.comp ((prismPush hr hv).continuous.comp
    (continuous_const.prodMk continuous_id))
  continuous_invFun := continuous_snd.comp ((prismPush hr hv).symm.continuous.comp
    (continuous_const.prodMk continuous_id))

/-- **The prism isotopy** around `m`: at time `s`, the slice at height `s - 1`. -/
noncomputable def prismIso (m : E) (s : unitInterval) : E ≃ₜ E :=
  (Homeomorph.subRight m).trans ((prismSlice hr hv ((s : ℝ) - 1)).trans (Homeomorph.addLeft m))

lemma prismIso_apply (m : E) (s : unitInterval) (x : E) :
    prismIso hr hv m s x = m + (prismPush hr hv ((s : ℝ) - 1, x - m)).2 := rfl

lemma prismIso_symm_apply (m : E) (s : unitInterval) (y : E) :
    (prismIso hr hv m s).symm y = m + ((prismPush hr hv).symm ((s : ℝ) - 1, y - m)).2 := by
  simp [prismIso, prismSlice, Homeomorph.addLeft_symm, add_comm, ← sub_eq_add_neg]

lemma prismIso_zero (m : E) (x : E) : prismIso hr hv m 0 x = x := by
  rw [prismIso_apply, prismPush_apply]
  have : pushCoef (polySet (prismφ φ) (prismr r)) (((0 : unitInterval) : ℝ) - 1, x - m) = 0 := by
    apply pushCoef_of_one_le_gauge
    rw [gauge_prism hr]
    simp
  rw [this]
  simp

lemma prismIso_one (m : E) (x : E) : prismIso hr hv m 1 x = m + push (polySet φ r) v (x - m) := by
  rw [prismIso_apply, prismPush_apply]
  simp only [Set.Icc.coe_one, sub_self, push, pushCoef]
  rw [gauge_prism hr, abs_zero, max_eq_right (gauge_nonneg _)]

lemma continuous_prismIso (m : E) :
    Continuous fun p : unitInterval × E => prismIso hr hv m p.1 p.2 := by
  simp only [prismIso_apply]
  exact continuous_const.add (continuous_snd.comp ((prismPush hr hv).continuous.comp
    (((continuous_subtype_val.comp continuous_fst).sub continuous_const).prodMk
      (continuous_snd.sub continuous_const))))

lemma continuous_prismIso_symm (m : E) :
    Continuous fun p : unitInterval × E => (prismIso hr hv m p.1).symm p.2 := by
  simp only [prismIso_symm_apply]
  exact continuous_const.add (continuous_snd.comp ((prismPush hr hv).symm.continuous.comp
    (((continuous_subtype_val.comp continuous_fst).sub continuous_const).prodMk
      (continuous_snd.sub continuous_const))))

/-- **The track of the prism isotopy is PL.** -/
theorem isPL_prismIso_track (m : E) :
    IsPL (fun p : ℝ × E => prismIso hr hv m (clamp01 p.1) p.2) := by
  have hpush : IsPL (prismPush hr hv) := by
    have := isPL_push_polySet (prismr_pos hr) (((0 : ℝ), v) : ℝ × E) (φ := prismφ φ)
    convert this using 1
  have hin : IsPL (fun p : ℝ × E => (((clamp01 p.1 : unitInterval) : ℝ) - 1, p.2 - m)) :=
    (IsPL.clamp01.comp IsPL.fst |>.sub (IsPL.const 1)).prodMk (IsPL.snd.sub (IsPL.const m))
  have h := (IsPL.const m).add (IsPL.snd.comp (hpush.comp hin))
  convert h using 1

end Prism

/-- The track property used for PL isotopies. -/
def HasPLTrack (H : unitInterval → E ≃ₜ E) : Prop := IsPL fun p : ℝ × E => H (clamp01 p.1) p.2

/-- **A polyhedral body around the Δ-triangle gives a push provider with a PL track.** The body
is `m + polySet φ r` with `m` the midpoint of `[a, b]`; `a`, `b` lie in it, `c` strictly inside
every inequality, and it misses the two edge rays and `R'`. -/
theorem pushData_of_polyBody {a b c wa wb : E} {R' : Set E} (φ : ι → E →L[ℝ] ℝ) (r : ι → ℝ)
    (hr : ∀ i, 0 < r i) (ha : a - midpoint ℝ a b ∈ polySet φ r)
    (hb : b - midpoint ℝ a b ∈ polySet φ r) (hc : ∀ i, φ i (c - midpoint ℝ a b) < r i)
    (hA : ∀ t : ℝ, 0 < t → a + t • wa ∉ {x | x - midpoint ℝ a b ∈ polySet φ r})
    (hB : ∀ t : ℝ, 0 < t → b + t • wb ∉ {x | x - midpoint ℝ a b ∈ polySet φ r})
    (hR : Disjoint R' {x | x - midpoint ℝ a b ∈ polySet φ r}) :
    ∃ (K : Set E) (H : unitInterval → E ≃ₜ E),
      (∀ t : ℝ, 0 < t → a + t • wa ∉ K) ∧ (∀ t : ℝ, 0 < t → b + t • wb ∉ K) ∧ Disjoint R' K ∧
      (Continuous fun p : unitInterval × E => H p.1 p.2) ∧
      (Continuous fun p : unitInterval × E => (H p.1).symm p.2) ∧ (∀ x, H 0 x = x) ∧
      (∀ x, x ∉ interior K → H 1 x = x) ∧
      (∀ u : ℝ, 0 ≤ u → u ≤ 1 / 2 → H 1 ((1 - u) • a + u • b) = (1 - 2 * u) • a + (2 * u) • c) ∧
      (∀ u : ℝ, 1 / 2 ≤ u → u ≤ 1 →
        H 1 ((1 - u) • a + u • b) = (2 - 2 * u) • c + (2 * u - 1) • b) ∧ HasPLTrack H := by
  set m := midpoint ℝ a b
  set S := polySet φ r
  set K : Set E := {x | x - m ∈ S}
  have hcS : Convex ℝ S := convex_polySet
  have h0S : S ∈ nhds (0 : E) := polySet_mem_nhds hr
  have hv : gauge S (c - m) < 1 := by
    rw [gauge_polySet hr]
    refine (Finset.fold_max_lt _).mpr ⟨one_pos, fun i _ => ?_⟩
    rw [div_lt_one (hr i)]
    exact hc i
  have hint : ∀ x, gauge S (x - m) < 1 → x ∈ interior K := by
    intro x hx
    rw [gauge_lt_one_iff_mem_interior hcS h0S] at hx
    exact preimage_interior_subset_interior_preimage (continuous_id.sub continuous_const) hx
  have hgK : ∀ x, x ∉ interior K → 1 ≤ gauge S (x - m) := fun x hx =>
    not_lt.mp fun h => hx (hint x h)
  have hga : gauge S (a - m) = 1 :=
    le_antisymm (gauge_le_one_of_mem ha) (hgK a (not_mem_interior_of_ray hA))
  have hgb : gauge S (b - m) = 1 :=
    le_antisymm (gauge_le_one_of_mem hb) (hgK b (not_mem_interior_of_ray hB))
  refine ⟨K, prismIso hr hv m, hA, hB, hR, continuous_prismIso hr hv m,
    continuous_prismIso_symm hr hv m, prismIso_zero hr hv m, fun x hx => ?_, fun u hu0 hu1 => ?_,
    fun u hu0 hu1 => ?_, isPL_prismIso_track hr hv m⟩
  · rw [prismIso_one, push_of_one_le_gauge _ (hgK x hx)]
    abel
  · have hx : (1 - u) • a + u • b - m = (1 - 2 * u) • (a - m) := by
      simp only [m, midpoint_eq_smul_add, invOf_eq_inv]; module
    rw [prismIso_one, hx, push_smul_of_gauge_eq_one _ hga (by linarith) (by linarith)]
    simp only [m, midpoint_eq_smul_add, invOf_eq_inv]; module
  · have hx : (1 - u) • a + u • b - m = (2 * u - 1) • (b - m) := by
      simp only [m, midpoint_eq_smul_add, invOf_eq_inv]; module
    rw [prismIso_one, hx, push_smul_of_gauge_eq_one _ hgb (by linarith) (by linarith)]
    simp only [m, midpoint_eq_smul_add, invOf_eq_inv]; module

end QOU.MathlibExt.PL
