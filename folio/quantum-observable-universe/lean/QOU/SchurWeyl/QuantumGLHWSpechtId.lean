/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.QuantumGLHWSpecht
import QOU.SchurWeyl.QuantumGLHWDim

/-!
# `HW_μ` carries the Specht character of `λ(μ)`

G3.4c (bean `qou-gl343`), identification step E.

`exists_hwTrace_eq_trace` gives one partition `π` with `tr(z | HW_μ) = χ^π(z)`.  This file
pins `π` to the row diagram `λ(μ)`, by induction on the size, comparing the two branching
rules (`hwTrace_heckeIncl` and `trace_seminormalRep_heckeIncl`) through the Wedderburn
test elements `W⁻¹(1_ν)`.

## Base ring (§7c)

A linearly ordered field, `q` not a root of unity.
-/

namespace QOU.SchurWeyl.QuantumGL

open QOU.SchurWeyl.JimboGL QOU.SchurWeyl.HeckeInclusion QOU.Mathlib YoungDiagram
open QOU.SchurWeyl.SeminormalRep

section Test

variable {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L]

omit [LinearOrder L] [IsStrictOrderedRing L] in
/-- The seminormal character depends only on the diagram. -/
theorem trace_seminormalRep_congr (q : L) (hq : q ≠ 0)
    (hgen : GenericParameter.NotRootOfUnity q) (m : ℕ) {D D' : YoungDiagram} (h : D = D')
    (hN : D.cells.card = m + 1) (hN' : D'.cells.card = m + 1) (z : Hecke L q q⁻¹ m) :
    (seminormalRep q hq hgen m hN z).trace = (seminormalRep q hq hgen m hN' z).trace := by
  subst h; rfl

/-- **Test elements.**  On the Wedderburn block idempotent `W⁻¹(1_ν)`, the seminormal
character of a diagram `D` is `f^ν` if `D` is the shape of `ν` and `0` otherwise. -/
theorem trace_seminormalRep_test (q : L) (hq : q ≠ 0)
    (hgen : GenericParameter.NotRootOfUnity q) (m : ℕ) (D : YoungDiagram)
    (hN : D.cells.card = m + 1) (ν : Partition (m + 1)) :
    (seminormalRep q hq hgen m hN ((heckeWedderburn q hq hgen m).symm (Pi.single ν 1))).trace
      = if D = partitionShape ν then (numStandardYoungTableaux (partitionShape ν) : L)
        else 0 := by
  set lam := (partitionShapeEquiv (m + 1)).symm ⟨D, hN⟩
  have hlam : partitionShape lam = D := by
    rw [← partitionShapeEquiv_apply, Equiv.apply_symm_apply]
  rw [trace_seminormalRep_congr q hq hgen m hlam.symm hN (partitionShape_card_succ lam)]
  have hW : seminormalRep q hq hgen m (partitionShape_card_succ lam)
      ((heckeWedderburn q hq hgen m).symm (Pi.single ν 1))
      = (heckeWedderburn q hq hgen m ((heckeWedderburn q hq hgen m).symm (Pi.single ν 1))) lam :=
    rfl
  rw [hW, AlgEquiv.apply_symm_apply, ← hlam]
  by_cases h : lam = ν
  · subst h
    rw [Pi.single_eq_same, Matrix.trace_one, if_pos rfl, numStandardYoungTableaux,
      Nat.card_eq_fintype_card]
  · rw [Pi.single_eq_of_ne h, Matrix.trace_zero,
      if_neg fun e => h (partitionShape_injective e)]

end Test

section Corner

variable {d : ℕ}

/-- **Every corner of `λ(μ)` is the last box of a removable row.** -/
theorem exists_cornerOf {μ : Fin d → ℕ} (hμ : IsDom μ) {c : ℕ × ℕ}
    (hc : IsCornerCell (rowDiagram μ hμ) c) :
    ∃ x : Fin d, 0 < μ x ∧ IsDom (μ - Pi.single x 1) ∧ c = cornerOf μ x := by
  obtain ⟨hc0, hc1, hc2⟩ := hc
  obtain ⟨y, h1, h2⟩ := (mem_rowDiagram μ hμ c).mp hc0
  have hyd := y.isLt
  have hlast : c.2 + 1 = μ y := by
    by_contra hne
    exact hc2 ((mem_rowDiagram μ hμ _).mpr ⟨y, h1, by simp; omega⟩)
  refine ⟨y, by omega, fun i j hij => ?_, Prod.ext (by simp [cornerOf, h1]) (by
    simp [cornerOf]; omega)⟩
  simp only [Pi.sub_apply]
  have hi := i.isLt; have hj := j.isLt
  by_cases hjy : j = y
  · subst hjy
    have hiy : i ≠ j := fun e => by rw [e] at hij; omega
    rw [Pi.single_eq_same, Pi.single_eq_of_ne hiy]
    have : μ i ≤ c.2 := by
      by_contra hlt
      exact hc1 ((mem_rowDiagram μ hμ _).mpr ⟨i, by simp; omega, by omega⟩)
    omega
  · rw [Pi.single_eq_of_ne hjy]
    have := hμ i j hij
    by_cases hiy : i = y
    · subst hiy; rw [Pi.single_eq_same]; omega
    · rw [Pi.single_eq_of_ne hiy]; omega

end Corner


section Count

variable {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L] {d : ℕ} [NeZero d]

omit [NeZero d] in
theorem sum_sub_single {μ : Fin d → ℕ} {x : Fin d} (hx : 0 < μ x) :
    ∑ y, (μ - Pi.single x 1 : Fin d → ℕ) y + 1 = ∑ y, μ y := by
  classical
  rw [← Finset.add_sum_erase _ _ (Finset.mem_univ x), ← Finset.add_sum_erase _ _
    (Finset.mem_univ x)]
  have : ∑ y ∈ Finset.univ.erase x, (μ - Pi.single x 1 : Fin d → ℕ) y = ∑ y ∈ Finset.univ.erase x, μ y :=
    Finset.sum_congr rfl fun y hy => by
      simp [Pi.single_eq_of_ne (Finset.ne_of_mem_erase hy)]
  rw [this]; simp only [Pi.sub_apply, Pi.single_eq_same]; omega

omit [LinearOrder L] [IsStrictOrderedRing L] [NeZero d] in
theorem hwTrace_eq_zero_of_eq_bot {q : L} (hq : q ≠ 0) {m : ℕ} {μ : Fin d → ℕ}
    (h : hwSpace q m μ = ⊥) (z : Hecke L q q⁻¹ m) : hwTrace q hq m μ z = 0 := by
  haveI : Subsingleton (hwSpace q m μ) := by rw [h]; infer_instance
  rw [hwTrace_eq_trace_hwAct, Subsingleton.elim (hwAct q hq m μ z) 0, map_zero]

omit [LinearOrder L] [IsStrictOrderedRing L] [NeZero d] in
/-- A removed box that is not a removable row end kills the highest-weight space. -/
theorem hwSpace_sub_eq_bot (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q)
    (m : ℕ) {μ : Fin d → ℕ} (hsum : ∑ y, μ y = m + 2) {x : Fin d}
    (hg : ¬ (0 < μ x ∧ IsDom (μ - Pi.single x 1))) : hwSpace q m (μ - Pi.single x 1) = ⊥ := by
  by_contra hne
  have hd := isDom_of_ne_bot q hq (sub_inv_ne_zero_of_notRootOfUnity hq hgen) hgen m _ hne
  have hx : 0 < μ x := by
    by_contra h0
    apply hne
    apply hwSpace_eq_bot_of_sum_ne
    have : μ - Pi.single x 1 = μ := by
      funext y
      by_cases hyx : y = x
      · subst hyx; simp; omega
      · simp [Pi.single_eq_of_ne hyx]
    rw [this, hsum]; omega
  exact hg ⟨hx, hd⟩

/-- **The counting identity behind the induction step.**  If `HW_μ` (size `m + 2`) carries
`χ^P`, and every `HW_ν` of size `m + 1` carries `χ^{λ(ν)}`, then for each `ν ⊢ m + 1` the
corners of `P` and the removable row ends of `μ` with erasure `ν` are equally many. -/
theorem card_erase_eq (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (μ : Fin d → ℕ) (hμ : IsDom μ) (hsum : ∑ y, μ y = m + 2) (P : YoungDiagram)
    (hP : P.cells.card = m + 2)
    (hPtr : ∀ z, hwTrace q hq (m + 1) μ z = (seminormalRep q hq hgen (m + 1) hP z).trace)
    (ih : ∀ (ν : Fin d → ℕ) (hν : IsDom ν) (hs : ∑ y, ν y = m + 1) (z : Hecke L q q⁻¹ m),
      hwTrace q hq m ν z = (seminormalRep q hq hgen m
        ((card_rowDiagram ν hν).trans hs) z).trace)
    (ν : Partition (m + 1)) [DecidablePred fun c : {c : ℕ × ℕ // IsCornerCell P c} =>
      eraseCorner P c.1 c.2 = partitionShape ν]
    [DecidablePred fun x : Fin d => ∃ h : 0 < μ x ∧ IsDom (μ - Pi.single x 1),
      rowDiagram _ h.2 = partitionShape ν] :
    (Finset.univ.filter fun c : {c : ℕ × ℕ // IsCornerCell P c} =>
        eraseCorner P c.1 c.2 = partitionShape ν).card
      = (Finset.univ.filter fun x : Fin d => ∃ h : 0 < μ x ∧ IsDom (μ - Pi.single x 1),
        rowDiagram _ h.2 = partitionShape ν).card := by
  set e := (heckeWedderburn q hq hgen m).symm (Pi.single ν 1)
  set F : L := (numStandardYoungTableaux (partitionShape ν) : L)
  have hF : F ≠ 0 := by
    simp only [F, ne_eq, Nat.cast_eq_zero]
    exact (numStandardYoungTableaux_pos _).ne'
  have key := hPtr (heckeIncl L q q⁻¹ m e)
  rw [hwTrace_heckeIncl q hq hgen m μ hμ hsum, trace_seminormalRep_heckeIncl] at key
  have hl : ∀ x : Fin d, hwTrace q hq m (μ - Pi.single x 1) e
      = if ∃ h : 0 < μ x ∧ IsDom (μ - Pi.single x 1), rowDiagram _ h.2 = partitionShape ν
        then F else 0 := by
    intro x
    by_cases hg : 0 < μ x ∧ IsDom (μ - Pi.single x 1)
    · have hs : ∑ y, (μ - Pi.single x 1 : Fin d → ℕ) y = m + 1 := by
        have := sum_sub_single (μ := μ) hg.1; omega
      rw [ih _ hg.2 hs, trace_seminormalRep_test]
      exact if_congr ⟨fun h => ⟨hg, h⟩, fun ⟨_, h⟩ => h⟩ rfl rfl
    · rw [hwTrace_eq_zero_of_eq_bot hq (hwSpace_sub_eq_bot q hq hgen m hsum hg),
        if_neg fun ⟨h, _⟩ => hg h]
  have hr : ∀ c : {c : ℕ × ℕ // IsCornerCell P c},
      (seminormalRep q hq hgen m (card_eraseCorner_of_card c.1 c.2 hP) e).trace
        = if eraseCorner P c.1 c.2 = partitionShape ν then F else 0 := fun c => by
    convert trace_seminormalRep_test q hq hgen m _ (card_eraseCorner_of_card c.1 c.2 hP) ν
  simp only [hl, hr, Finset.sum_ite, Finset.sum_const_zero, add_zero, Finset.sum_const,
    nsmul_eq_mul] at key
  exact_mod_cast (mul_right_cancel₀ hF key).symm

end Count

end QOU.SchurWeyl.QuantumGL
