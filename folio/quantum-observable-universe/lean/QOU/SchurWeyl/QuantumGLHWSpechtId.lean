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


section Reconstruct

/-- Every cell lies below a corner. -/
theorem exists_corner_ge (P : YoungDiagram) {v : ℕ × ℕ} (hv : v ∈ P) :
    ∃ w, IsCornerCell P w ∧ v ≤ w := by
  classical
  obtain ⟨w, hwS, hmax⟩ := (P.cells.filter (v ≤ ·)).exists_max_image (fun w => w.1 + w.2)
    ⟨v, Finset.mem_filter.mpr ⟨hv, le_rfl⟩⟩
  obtain ⟨hwP, hvw⟩ := Finset.mem_filter.mp hwS
  refine ⟨w, ⟨hwP, fun h => ?_, fun h => ?_⟩, hvw⟩
  · have := hmax _ (Finset.mem_filter.mpr ⟨h, hvw.trans (Prod.mk_le_mk.mpr ⟨by omega, le_rfl⟩)⟩)
    simp at this
  · have := hmax _ (Finset.mem_filter.mpr ⟨h, hvw.trans (Prod.mk_le_mk.mpr ⟨le_rfl, by omega⟩)⟩)
    simp at this

/-- A diagram with a single corner `u` is the rectangle below `u`. -/
theorem mem_iff_le_of_unique_corner (P : YoungDiagram) {u : ℕ × ℕ} (hu : IsCornerCell P u)
    (huniq : ∀ w, IsCornerCell P w → w = u) (v : ℕ × ℕ) : v ∈ P ↔ v ≤ u := by
  constructor
  · intro hv
    obtain ⟨w, hw, hvw⟩ := exists_corner_ge P hv
    exact huniq w hw ▸ hvw
  · intro hvu; exact P.isLowerSet hvu hu.1

/-- The coordinate step of the rectangle comparison. -/
theorem fst_le_of_rect_erase {a b a' b' : ℕ} (ha : 2 ≤ a + b) (ha' : 2 ≤ a' + b')
    (hE : ∀ i j : ℕ, ((i ≤ a ∧ j ≤ b) ∧ (i, j) ≠ (a, b))
      ↔ ((i ≤ a' ∧ j ≤ b') ∧ (i, j) ≠ (a', b'))) : a ≤ a' := by
  by_contra hlt
  rcases Nat.eq_zero_or_pos b with hb | hb
  · have h1 := (hE (a - 1) 0).mp ⟨⟨by omega, by omega⟩, by simp; omega⟩
    have h2 := (hE 0 1).mpr ⟨⟨by omega, by simp at h1; omega⟩, by simp; omega⟩
    omega
  · have := (hE a (b - 1)).mp ⟨⟨le_rfl, by omega⟩, by simp; omega⟩
    omega

/-- A diagram with at least three cells and one corner `u` has `u.1 + u.2 ≥ 2`. -/
theorem two_le_of_unique_corner (P : YoungDiagram) (h3 : 3 ≤ P.cells.card) {u : ℕ × ℕ}
    (hu : IsCornerCell P u) (huniq : ∀ w, IsCornerCell P w → w = u) : 2 ≤ u.1 + u.2 := by
  classical
  by_contra hlt
  have hsub : P.cells ⊆ {(0, 0), u} := by
    intro v hv
    have := (mem_iff_le_of_unique_corner P hu huniq v).mp hv
    obtain ⟨h1, h2⟩ := Prod.mk_le_mk.mp (show (v.1, v.2) ≤ (u.1, u.2) from this)
    simp only [Finset.mem_insert, Finset.mem_singleton]
    by_cases hv0 : v = (0, 0)
    · exact Or.inl hv0
    · right; refine Prod.ext ?_ ?_ <;>
        · have : v.1 ≠ 0 ∨ v.2 ≠ 0 := by
            by_contra hh; push_neg at hh; exact hv0 (Prod.ext hh.1 hh.2)
          omega
  have := (Finset.card_le_card hsub).trans (Finset.card_le_two)
  omega

/-- **Young's lattice is reconstructible from its down-sets above size two.**  Two diagrams
with at least three cells whose corner erasures agree (in both directions) are equal. -/
theorem eq_of_eraseCorner_iff (P Λ : YoungDiagram) (hcard : P.cells.card = Λ.cells.card)
    (h3 : 3 ≤ P.cells.card)
    (hPΛ : ∀ p (hp : IsCornerCell P p), ∃ c, ∃ hc : IsCornerCell Λ c,
      eraseCorner P p hp = eraseCorner Λ c hc)
    (hΛP : ∀ c (hc : IsCornerCell Λ c), ∃ p, ∃ hp : IsCornerCell P p,
      eraseCorner Λ c hc = eraseCorner P p hp) : P = Λ := by
  classical
  -- two corners give an inclusion
  have incl : ∀ (A B : YoungDiagram) (hAB : ∀ p (hp : IsCornerCell A p), ∃ c,
      ∃ hc : IsCornerCell B c, eraseCorner A p hp = eraseCorner B c hc)
      (p₁ p₂ : ℕ × ℕ), IsCornerCell A p₁ → IsCornerCell A p₂ → p₁ ≠ p₂ →
      A.cells ⊆ B.cells := by
    intro A B hAB p₁ p₂ h₁ h₂ hne v hv
    by_cases hv1 : v = p₁
    · obtain ⟨c, hc, he⟩ := hAB p₂ h₂
      have : v ∈ eraseCorner A p₂ h₂ := (mem_eraseCorner _ _ _ _).mpr ⟨hv, hv1 ▸ hne⟩
      rw [he, mem_eraseCorner] at this; exact this.1
    · obtain ⟨c, hc, he⟩ := hAB p₁ h₁
      have : v ∈ eraseCorner A p₁ h₁ := (mem_eraseCorner _ _ _ _).mpr ⟨hv, hv1⟩
      rw [he, mem_eraseCorner] at this; exact this.1
  have hP0 : 0 < P.cells.card := by omega
  obtain ⟨v₀, hv₀⟩ := Finset.card_pos.mp hP0
  obtain ⟨u, hu, -⟩ := exists_corner_ge P hv₀
  obtain ⟨c, hc, hPu⟩ := hPΛ u hu
  by_cases hPu2 : ∃ w, IsCornerCell P w ∧ w ≠ u
  · obtain ⟨w, hw, hwu⟩ := hPu2
    exact YoungDiagram.ext (Finset.eq_of_subset_of_card_le
      (incl P Λ hPΛ w u hw hu hwu) hcard.ge)
  push_neg at hPu2
  by_cases hΛc2 : ∃ w, IsCornerCell Λ w ∧ w ≠ c
  · obtain ⟨w, hw, hwc⟩ := hΛc2
    exact (YoungDiagram.ext (Finset.eq_of_subset_of_card_le
      (incl Λ P hΛP w c hw hc hwc) hcard.le)).symm
  push_neg at hΛc2
  -- both are rectangles
  have hrP := mem_iff_le_of_unique_corner P hu hPu2
  have hrΛ := mem_iff_le_of_unique_corner Λ hc hΛc2
  have hE : ∀ v : ℕ × ℕ, (v ≤ u ∧ v ≠ u) ↔ (v ≤ c ∧ v ≠ c) := by
    intro v
    have := congrArg (fun D : YoungDiagram => v ∈ D) hPu
    simp only [mem_eraseCorner, hrP, hrΛ, eq_iff_iff] at this
    exact this
  have h2u := two_le_of_unique_corner P h3 hu hPu2
  have h2c := two_le_of_unique_corner Λ (hcard ▸ h3) hc hΛc2
  have hE' : ∀ i j : ℕ, ((i ≤ u.1 ∧ j ≤ u.2) ∧ (i, j) ≠ (u.1, u.2))
      ↔ ((i ≤ c.1 ∧ j ≤ c.2) ∧ (i, j) ≠ (c.1, c.2)) := fun i j => by
    simpa [Prod.mk_le_mk] using hE (i, j)
  have hE'' : ∀ i j : ℕ, ((i ≤ u.2 ∧ j ≤ u.1) ∧ (i, j) ≠ (u.2, u.1))
      ↔ ((i ≤ c.2 ∧ j ≤ c.1) ∧ (i, j) ≠ (c.2, c.1)) := fun i j => by
    have := hE' j i
    simp only [ne_eq, Prod.mk.injEq] at this ⊢
    tauto
  have e1 := fst_le_of_rect_erase h2u h2c hE'
  have e2 := fst_le_of_rect_erase h2c h2u fun i j => (hE' i j).symm
  have e3 := fst_le_of_rect_erase (by omega) (by omega) hE''
  have e4 := fst_le_of_rect_erase (by omega) (by omega) fun i j => (hE'' i j).symm
  have huc : u = c := Prod.ext (by omega) (by omega)
  ext v
  show v ∈ P ↔ v ∈ Λ
  rw [hrP, hrΛ, huc]

end Reconstruct

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
