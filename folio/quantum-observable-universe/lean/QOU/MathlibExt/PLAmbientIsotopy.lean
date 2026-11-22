/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLPolygonalLink
import Mathlib.Topology.Algebra.Order.Floor
import Mathlib.Topology.Algebra.Module.Basic
import Mathlib.Topology.UnitInterval
import Mathlib.Topology.Homeomorph.Defs

set_option autoImplicit false

/-!
# Ambient isotopy of polygonal links (issue #8902, stage 2, part 3)

Owner ruling 2026-11-21: stage 2 compares Δ-equivalence with **topological** ambient isotopy
first; a PL version and the proof that the two agree come later.

## What is a DEFINITION here

* `hat x = max 0 (1 - |x|)` — the tent function.
* `Polygon.param P : ℝ → E` — the standard parametrization of a polygon, of period `1`:
  on `[k/N, (k+1)/N]` (`N = n + 1` vertices) it runs linearly from `v k` to `v (k+1)`. It is
  written as `∑ₖ hat (N · fract t - k) • w k` with `w = v 0, …, v n, v 0`, so continuity is a
  finite sum of continuous terms.
* `OrientedReparam φ` — `φ : ℝ → ℝ` continuous, strictly increasing, `φ (t + 1) = φ t + 1`:
  the lift of an orientation-preserving homeomorphism of the circle.
* `AmbientIsotopy L L'` — a family `H t` (`t ∈ [0, 1]`) of homeomorphisms of `E`, with
  `(t, x) ↦ H t x` and `(t, x) ↦ (H t)⁻¹ x` both continuous (a level-preserving homeomorphism
  of `[0, 1] × E`), `H 0 = id`, and a bijection `e` of components such that `H 1 ∘ param (L.comp i)` is an
  orientation-preserving reparametrization of `param (L'.comp (e i))`.
* `AmbientIsotopic L L'` — such an isotopy exists.

## What is a THEOREM here

* `continuous_hat`, `Polygon.continuous_param` — the parametrization is continuous.
* `Polygon.param_add_one`, `Polygon.param_zero` — it has period `1` and starts at `v 0`.
* `OrientedReparam.comp`, `.surjective`, `.symm` — oriented reparametrizations compose, are
  onto, and have oriented inverses.
* `AmbientIsotopic.refl`, `.symm`, `.trans` — ambient isotopy is an equivalence relation.
  Transitivity runs both isotopies at once, `t ↦ K t ∘ H t`; symmetry uses `t ↦ H (1 - t) ∘ (H 1)⁻¹`.

## What is NOT proved here

* That the image of `param` is the polygon's point set.
* Either direction of "Δ-equivalent ↔ ambient isotopic". These are the next steps of stage 2.
-/

namespace QOU.MathlibExt.PL

open Set Int

/-- The tent function `max 0 (1 - |x|)`. -/
noncomputable def hat (x : ℝ) : ℝ := max 0 (1 - |x|)

theorem continuous_hat : Continuous hat :=
  continuous_const.max (continuous_const.sub continuous_abs)

lemma hat_zero : hat 0 = 1 := by simp [hat]

lemma hat_of_one_le_abs {x : ℝ} (h : 1 ≤ |x|) : hat x = 0 := by
  simp only [hat]
  exact max_eq_left (by linarith)

variable {E : Type*} [AddCommGroup E] [Module ℝ E] [TopologicalSpace E]
  [IsTopologicalAddGroup E] [ContinuousSMul ℝ E]

namespace Polygon

variable (P : Polygon E)

/-- The closed vertex list `v 0, …, v n, v 0`. -/
def closedV : Fin (P.n + 2) → E := Fin.snoc (α := fun _ => E) P.v (P.v 0)

/-- The path on `[0, 1]`, extended to `ℝ` by the same formula. -/
noncomputable def pathRaw (s : ℝ) : E :=
  ∑ k : Fin (P.n + 2), hat ((P.n + 1 : ℝ) * s - k) • P.closedV k

/-- **The standard parametrization**, of period `1`. -/
noncomputable def param (t : ℝ) : E := P.pathRaw (fract t)

theorem continuous_pathRaw : Continuous P.pathRaw :=
  continuous_finset_sum _ fun _ _ =>
    (continuous_hat.comp ((continuous_const.mul continuous_id).sub continuous_const)).smul
      continuous_const

omit [TopologicalSpace E] [IsTopologicalAddGroup E] [ContinuousSMul ℝ E] in
lemma pathRaw_zero : P.pathRaw 0 = P.v 0 := by
  simp only [pathRaw, mul_zero, zero_sub]
  rw [Finset.sum_eq_single (0 : Fin (P.n + 2))]
  · simp [hat_zero, closedV]
  · intro k _ hk
    have hk1 : (1 : ℝ) ≤ k := by
      have : (1 : ℕ) ≤ k.val := Nat.one_le_iff_ne_zero.mpr fun h => hk (Fin.ext h)
      exact_mod_cast this
    rw [hat_of_one_le_abs (by rw [abs_neg, abs_of_nonneg (by linarith)]; exact hk1), zero_smul]
  · simp

omit [TopologicalSpace E] [IsTopologicalAddGroup E] [ContinuousSMul ℝ E] in
lemma pathRaw_one : P.pathRaw 1 = P.v 0 := by
  simp only [pathRaw, mul_one]
  rw [Finset.sum_eq_single (Fin.last (P.n + 1))]
  · simp [hat_zero, closedV]
  · intro k _ hk
    have hk1 : (k : ℝ) + 1 ≤ P.n + 1 := by
      have : k.val + 1 ≤ P.n + 1 := by
        have := k.isLt
        have : k.val ≠ P.n + 1 := fun h => hk (Fin.ext h)
        omega
      exact_mod_cast this
    rw [hat_of_one_le_abs (by rw [abs_of_nonneg (by linarith)]; linarith), zero_smul]
  · simp

theorem continuous_param : Continuous P.param :=
  ContinuousOn.comp_fract'' P.continuous_pathRaw.continuousOn
    (by rw [pathRaw_zero, pathRaw_one])

omit [TopologicalSpace E] [IsTopologicalAddGroup E] [ContinuousSMul ℝ E] in
theorem param_add_one (t : ℝ) : P.param (t + 1) = P.param t := by
  simp [param]

omit [TopologicalSpace E] [IsTopologicalAddGroup E] [ContinuousSMul ℝ E] in
theorem param_zero : P.param 0 = P.v 0 := by
  simp [param, pathRaw_zero]

end Polygon

/-- The lift of an orientation-preserving homeomorphism of the circle `ℝ / ℤ`. -/
structure OrientedReparam (φ : ℝ → ℝ) : Prop where
  continuous : Continuous φ
  strictMono : StrictMono φ
  add_one : ∀ t, φ (t + 1) = φ t + 1

namespace OrientedReparam

theorem id : OrientedReparam id :=
  ⟨continuous_id, strictMono_id, fun _ => rfl⟩

theorem comp {φ ψ : ℝ → ℝ} (hψ : OrientedReparam ψ) (hφ : OrientedReparam φ) :
    OrientedReparam (ψ ∘ φ) :=
  ⟨hψ.continuous.comp hφ.continuous, hψ.strictMono.comp hφ.strictMono,
    fun t => by simp [hφ.add_one, hψ.add_one]⟩

variable {φ : ℝ → ℝ} (h : OrientedReparam φ)
include h

lemma add_nat (t : ℝ) (n : ℕ) : φ (t + n) = φ t + n := by
  induction n with
  | zero => simp
  | succ n ih =>
    push_cast
    rw [← add_assoc, h.add_one, ih, add_assoc]

lemma sub_nat (t : ℝ) (n : ℕ) : φ (t - n) = φ t - n := by
  have := h.add_nat (t - n) n
  rw [sub_add_cancel] at this
  linarith

/-- An oriented reparametrization is onto. -/
theorem surjective : Function.Surjective φ := by
  intro y
  set n := ⌈|y - φ 0|⌉₊
  have hn : |y - φ 0| ≤ n := Nat.le_ceil _
  have h1 := h.sub_nat 0 n
  have h2 := h.add_nat 0 n
  rw [zero_sub] at h1
  rw [zero_add] at h2
  obtain ⟨hl, hr⟩ := abs_le.mp hn
  exact intermediate_value_univ (-(n : ℝ)) n h.continuous ⟨by linarith, by linarith⟩

/-- The order isomorphism `ℝ ≃o ℝ` defined by an oriented reparametrization. -/
noncomputable def toOrderIso : ℝ ≃o ℝ :=
  StrictMono.orderIsoOfSurjective φ h.strictMono h.surjective

/-- **The inverse of an oriented reparametrization is one.** -/
theorem symm : OrientedReparam h.toOrderIso.symm :=
  ⟨h.toOrderIso.symm.continuous, h.toOrderIso.symm.strictMono, fun t => by
    apply h.strictMono.injective
    have e1 : ∀ s, φ (h.toOrderIso.symm s) = s := fun s => h.toOrderIso.apply_symm_apply s
    rw [h.add_one, e1, e1]⟩

lemma apply_symm (s : ℝ) : φ (h.toOrderIso.symm s) = s := h.toOrderIso.apply_symm_apply s

end OrientedReparam

/-- **A topological ambient isotopy** carrying the oriented link `L` onto `L'`. -/
structure AmbientIsotopy (L L' : PolygonalLink E) where
  /-- The homeomorphism at time `t`. -/
  H : unitInterval → E ≃ₜ E
  /-- Joint continuity in time and space. -/
  continuous : Continuous fun p : unitInterval × E => H p.1 p.2
  /-- Joint continuity of the inverses. -/
  continuous_symm : Continuous fun p : unitInterval × E => (H p.1).symm p.2
  /-- The isotopy starts at the identity. -/
  start : ∀ x, H 0 x = x
  /-- How the components correspond. -/
  e : Fin L.k ≃ Fin L'.k
  /-- At time `1`, each component goes onto its partner, preserving orientation. -/
  finish : ∀ i, ∃ φ : ℝ → ℝ, OrientedReparam φ ∧
    ∀ t, H 1 ((L.comp i).param t) = (L'.comp (e i)).param (φ t)

/-- Two oriented polygonal links are **ambient isotopic**. -/
def AmbientIsotopic (L L' : PolygonalLink E) : Prop := Nonempty (AmbientIsotopy L L')

omit [IsTopologicalAddGroup E] [ContinuousSMul ℝ E] in
/-- **Every link is ambient isotopic to itself.** -/
theorem AmbientIsotopic.refl (L : PolygonalLink E) : AmbientIsotopic L L :=
  ⟨{ H := fun _ => Homeomorph.refl E
     continuous := continuous_snd
     continuous_symm := continuous_snd
     start := fun _ => rfl
     e := Equiv.refl _
     finish := fun _ => ⟨id, OrientedReparam.id, fun _ => rfl⟩ }⟩

omit [IsTopologicalAddGroup E] [ContinuousSMul ℝ E] in
/-- **Ambient isotopy is symmetric.** Run the isotopy backwards and undo its end. -/
theorem AmbientIsotopic.symm {L L' : PolygonalLink E} (h : AmbientIsotopic L L') :
    AmbientIsotopic L' L := by
  obtain ⟨I⟩ := h
  refine ⟨{ H := fun t => (I.H 1).symm.trans (I.H (unitInterval.symm t))
            continuous := ?_
            continuous_symm := ?_
            start := ?_
            e := I.e.symm
            finish := ?_ }⟩
  · exact I.continuous.comp ((unitInterval.continuous_symm.comp continuous_fst).prodMk
      ((I.H 1).symm.continuous.comp continuous_snd))
  · exact (I.H 1).continuous.comp (I.continuous_symm.comp
      ((unitInterval.continuous_symm.comp continuous_fst).prodMk continuous_snd))
  · intro x
    simp
  · intro j
    obtain ⟨φ, hφ, hH⟩ := I.finish (I.e.symm j)
    rw [Equiv.apply_symm_apply] at hH
    refine ⟨hφ.toOrderIso.symm, hφ.symm, fun t => ?_⟩
    have := hH (hφ.toOrderIso.symm t)
    rw [hφ.apply_symm] at this
    simp only [Homeomorph.trans_apply, unitInterval.symm_one, I.start]
    rw [← this, Homeomorph.symm_apply_apply]

omit [IsTopologicalAddGroup E] [ContinuousSMul ℝ E] in
/-- **Ambient isotopy is transitive.** Run both isotopies at once and compose. -/
theorem AmbientIsotopic.trans {L L' L'' : PolygonalLink E} (h : AmbientIsotopic L L')
    (h' : AmbientIsotopic L' L'') : AmbientIsotopic L L'' := by
  obtain ⟨I⟩ := h
  obtain ⟨J⟩ := h'
  refine ⟨{ H := fun t => (I.H t).trans (J.H t)
            continuous := ?_
            continuous_symm := ?_
            start := ?_
            e := I.e.trans J.e
            finish := ?_ }⟩
  · exact J.continuous.comp (continuous_fst.prodMk I.continuous)
  · exact I.continuous_symm.comp (continuous_fst.prodMk J.continuous_symm)
  · intro x
    simp [I.start, J.start]
  · intro i
    obtain ⟨φ, hφ, hH⟩ := I.finish i
    obtain ⟨ψ, hψ, hK⟩ := J.finish (I.e i)
    exact ⟨ψ ∘ φ, hψ.comp hφ, fun t => by
      simp only [Homeomorph.trans_apply, hH, hK, Equiv.trans_apply, Function.comp]⟩

end QOU.MathlibExt.PL
