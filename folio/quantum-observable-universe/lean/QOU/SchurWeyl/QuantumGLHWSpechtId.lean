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

* `hwCharStatement_all`: `tr(z | HW_μ) = χ^{λ(μ)}(z)` for every dominant `μ`.
* `exists_linearEquiv_of_trace_eq`: two surjective representations with equal traces and equal
  nonzero dimension are isomorphic.
* `exists_hwSpace_equiv_specht`: `HW_μ ≅ S_{λ(μ)}` as `H_{m+1}(q)`-modules.

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

section Small

theorem zero_mem_of_card_pos (D : YoungDiagram) (h : 0 < D.cells.card) : (0, 0) ∈ D := by
  obtain ⟨⟨a, b⟩, hc⟩ := Finset.card_pos.mp h
  exact D.up_left_mem (Nat.zero_le a) (Nat.zero_le b) ((YoungDiagram.mem_cells _).1 hc)

theorem eq_of_card_one {D D' : YoungDiagram} (h : D.cells.card = 1) (h' : D'.cells.card = 1) :
    D = D' := by
  have key : ∀ E : YoungDiagram, E.cells.card = 1 → E.cells = {(0, 0)} := fun E hE => by
    obtain ⟨c, hc⟩ := Finset.card_eq_one.mp hE
    have h0 : (0, 0) ∈ E.cells := (YoungDiagram.mem_cells _).2 (zero_mem_of_card_pos E (by omega))
    rw [hc, Finset.mem_singleton] at h0
    rw [hc, ← h0]
  exact YoungDiagram.ext ((key D h).trans (key D' h').symm)

/-- A two-cell diagram is the row or the column. -/
theorem cells_of_card_two (D : YoungDiagram) (h : D.cells.card = 2) :
    D.cells = {(0, 0), (0, 1)} ∨ D.cells = {(0, 0), (1, 0)} := by
  have h0 : (0, 0) ∈ D := zero_mem_of_card_pos D (by omega)
  obtain ⟨c, hc, hne⟩ := Finset.exists_mem_ne (show 1 < D.cells.card by omega) (0, 0)
  have hcD : c ∈ D := (YoungDiagram.mem_cells _).1 hc
  have sub : ∀ e : ℕ × ℕ, e ∈ D → e ≠ (0, 0) → D.cells = {(0, 0), e} := fun e he hne' => by
    symm
    refine Finset.eq_of_subset_of_card_le ?_ ?_
    · intro x hx
      rw [Finset.mem_insert, Finset.mem_singleton] at hx
      rcases hx with rfl | rfl <;> exact (YoungDiagram.mem_cells _).2 ‹_›
    · rw [h, Finset.card_pair (Ne.symm hne')]
  by_cases h2 : 1 ≤ c.2
  · left; exact sub _ (D.up_left_mem (Nat.zero_le _) h2 hcD) (by simp)
  · right
    have h1 : 1 ≤ c.1 := by
      by_contra h1; apply hne; ext <;> simp <;> omega
    exact sub _ (D.up_left_mem h1 (Nat.zero_le _) hcD) (by simp)

end Small

section SmallTrace

variable {L : Type*} [Field L]

/-- In a two-cell diagram `{(0,0), c}`, if `T` puts the smaller entry at the corner, the
axial distance of `σ_1` is `axialDistance (0,0) c`. -/
theorem axialDist_one_of_pair {D : YoungDiagram} (hN : D.cells.card = 2) {c : ℕ × ℕ}
    (hc : D.cells = {(0, 0), c}) (T : StandardYoungTableau D)
    (hlt : T.entry 0 0 < T.entry c.1 c.2) :
    TableauCells.axialDist T 1 = QOU.SchurWeyl.axialDistance (0, 0) c := by
  have h0 : (0, 0) ∈ D.cells := by rw [hc]; simp
  have h1 : c ∈ D.cells := by rw [hc]; simp
  have r0 := T.mapsTo_cells (by simpa using h0)
  have r1 := T.mapsTo_cells (by simpa using h1)
  simp only [Set.mem_Icc, hN] at r0 r1
  have e0 : T.entry 0 0 = 1 := by omega
  have e1 : T.entry c.1 c.2 = 2 := by omega
  unfold TableauCells.axialDist
  rw [TableauCells.cellOf_unique T h0 e0, TableauCells.cellOf_unique T h1 e1]


/-- On the column `{(0,0),(1,0)}` every tableau has axial distance `-1` at `σ_1`. -/
theorem axialDist_one_col {D : YoungDiagram} (hN : D.cells.card = 2)
    (hc : D.cells = {(0, 0), (1, 0)}) (T : StandardYoungTableau D) :
    TableauCells.axialDist T 1 = -1 := by
  have h1 : (1, 0) ∈ D := (YoungDiagram.mem_cells _).1 (by rw [hc]; simp)
  rw [axialDist_one_of_pair hN hc T (T.toSsyt.col_strict (i1 := 0) Nat.zero_lt_one h1)]
  rfl

/-- On the row `{(0,0),(0,1)}` every tableau has axial distance `1` at `σ_1`. -/
theorem axialDist_one_row {D : YoungDiagram} (hN : D.cells.card = 2)
    (hc : D.cells = {(0, 0), (0, 1)}) (T : StandardYoungTableau D) :
    TableauCells.axialDist T 1 = 1 := by
  have h0 : (0, 0) ∈ D.cells := by rw [hc]; simp
  have h1 : (0, 1) ∈ D.cells := by rw [hc]; simp
  have hle : T.entry 0 0 ≤ T.entry 0 1 :=
    T.toSsyt.row_weak (j1 := 0) Nat.zero_lt_one ((YoungDiagram.mem_cells _).1 h1)
  have hne : T.entry 0 0 ≠ T.entry 0 1 := fun h => by
    have := T.injOn_cells (by simpa using h0) (by simpa using h1) h
    simp at this
  rw [axialDist_one_of_pair hN hc T (lt_of_le_of_ne hle hne)]
  rfl

/-- **The trace of `σ_0` on a two-cell shape** when every tableau has the same axial
distance `a`: it is `#SYT · seminormalParam a`. -/
theorem trace_seminormalRep_σ_zero (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q)
    {D : YoungDiagram} (hN : D.cells.card = 1 + 1) (a : ℤ)
    (ha : ∀ T : StandardYoungTableau D, TableauCells.axialDist T 1 = a) :
    (seminormalRep q hq hgen 1 hN (Hecke.σ L q q⁻¹ 1 0)).trace
      = (Fintype.card (StandardYoungTableau D) : L) * Seminormal.seminormalParam q a := by
  rw [seminormalRep_σ]
  simp only [Matrix.trace, Matrix.diag, seminormalGen]
  simp [ha, Finset.sum_const, Finset.card_univ]

end SmallTrace

section RowWeight

open QOU.IwahoriHecke.TensorEmbedGL
open scoped Matrix

variable {L : Type*} [Field L] {d : ℕ}

/-- A two-letter word of content `μ` with `μ t = 2` is the constant word `t`. -/
theorem eq_const_of_content {μ : Fin d → ℕ} {t : Fin d} (ht : μ t = 2) {a : Fin 2 → Fin d}
    (ha : content a = μ) : a = fun _ => t := by
  classical
  have h2 : (Finset.univ.filter fun k => a k = t).card = (Finset.univ : Finset (Fin 2)).card := by
    have := congrFun ha t
    simp only [content] at this
    rw [this, ht]; rfl
  funext k
  have hk : k ∈ Finset.univ.filter fun k => a k = t := by
    rw [Finset.eq_univ_of_card _ h2]; exact Finset.mem_univ k
  exact (Finset.mem_filter.mp hk).2

/-- **`σ_0` acts by `q` on `HW_μ` when `μ` is a single row of length two.** -/
theorem jimbo_σ_zero_mulVec_of_double (q : L) (hq : q ≠ 0) {μ : Fin d → ℕ} {t : Fin d}
    (ht : μ t = 2) {v : (Fin 2 → Fin d) → L} (hv : v ∈ hwSpace q 1 μ) :
    jimbo d q hq 1 (Hecke.σ L q q⁻¹ 1 0) *ᵥ v = q • v := by
  classical
  set c : Fin 2 → Fin d := fun _ => t
  have hsupp : ∀ b, b ≠ c → v b = 0 := fun b hb => by
    have h1 := congrFun hv.1 b
    rw [weightProj_mulVec_apply] at h1
    split_ifs at h1 with hcb
    · exact absurd (eq_const_of_content ht hcb) hb
    · exact h1.symm
  funext a
  rw [jimbo_σ]
  change (∑ b, strandBraid (d := d) q q⁻¹ (0 : Fin 1) a b * v b) = _
  rw [Finset.sum_eq_single c
    (fun b _ hb => by rw [hsupp b hb, mul_zero]) (by simp)]
  simp only [strandBraid, braidAt, embedPair_apply, rCheckN_apply, Pi.smul_apply, smul_eq_mul]
  have hvac : ∀ k : Fin 2, k ≠ (0 : Fin 1).castSucc → k ≠ (0 : Fin 1).succ → a k = c k := by
    intro k h0 h1; fin_cases k <;> simp_all
  rw [if_pos hvac]
  by_cases hac : a = c
  · subst hac; simp [c]
  · have hne : (a (0 : Fin 1).castSucc, a (0 : Fin 1).succ) ≠ (c (0 : Fin 1).castSucc, c (0 : Fin 1).succ) := by
      intro h
      apply hac
      funext k
      fin_cases k
      · exact (Prod.ext_iff.mp h).1
      · exact (Prod.ext_iff.mp h).2
    rw [if_neg hne, hsupp a hac]
    simp [c] at hne ⊢
    intro h0 h1; exact absurd h1 (hne h0)

end RowWeight


section Base

open scoped Matrix

variable {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L] {d : ℕ} [NeZero d]

omit [LinearOrder L] [IsStrictOrderedRing L] [NeZero d] in
theorem hwTrace_one (q : L) (hq : q ≠ 0) (m : ℕ) (μ : Fin d → ℕ) :
    hwTrace q hq m μ 1 = (Module.finrank L (hwSpace q m μ) : L) := by
  rw [hwTrace_eq_trace_hwAct, map_one, LinearMap.trace_one]

omit [LinearOrder L] [IsStrictOrderedRing L] [NeZero d] in
theorem hwTrace_σ_zero_of_double (q : L) (hq : q ≠ 0) {μ : Fin d → ℕ} {t : Fin d}
    (ht : μ t = 2) :
    hwTrace q hq 1 μ (Hecke.σ L q q⁻¹ 1 0) = q * (Module.finrank L (hwSpace q 1 μ) : L) := by
  rw [hwTrace_eq_trace_hwAct]
  have h : hwAct (d := d) q hq 1 μ (Hecke.σ L q q⁻¹ 1 0) = q • 1 :=
    LinearMap.ext fun v => Subtype.ext (jimbo_σ_zero_mulVec_of_double q hq ht v.2)
  rw [h, map_smul, LinearMap.trace_one, smul_eq_mul]

theorem hwSpace_ne_bot_of_dom (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q)
    (m : ℕ) {μ : Fin d → ℕ} (hμ : IsDom μ) (hs : ∑ y, μ y = m + 1) : hwSpace q m μ ≠ ⊥ := by
  intro h
  have := finrank_hwSpace_eq_numSYT q hq hgen m μ hμ hs
  rw [h, finrank_bot] at this
  exact (numStandardYoungTableaux_pos _).ne this

/-- Each dominant `μ` of total weight `m + 1` carries the character of *some* shape. -/
theorem exists_shape (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q) (m : ℕ)
    {μ : Fin d → ℕ} (hμ : IsDom μ) (hs : ∑ y, μ y = m + 1) :
    ∃ (P : YoungDiagram) (hP : P.cells.card = m + 1),
      ∀ z, hwTrace q hq m μ z = (seminormalRep q hq hgen m hP z).trace := by
  obtain ⟨π, hπ⟩ := exists_hwTrace_eq_trace q hq hgen m μ (hwSpace_ne_bot_of_dom q hq hgen m hμ hs)
  exact ⟨_, partitionShape_card_succ π, hπ⟩

/-- **Distinct nonzero highest-weight spaces have distinct characters**, by density. -/
theorem exists_hwTrace_ne (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q)
    (m : ℕ) {μ ν : Fin d → ℕ} (hμ : hwSpace q m μ ≠ ⊥) (hν : hwSpace q m ν ≠ ⊥) (hne : μ ≠ ν) :
    ∃ z, hwTrace q hq m μ z ≠ hwTrace q hq m ν z := by
  obtain ⟨x, hx, hx0⟩ := exists_jimbo_restrict_eq q hq hgen m
    ⟨μ, mem_occWeights_of_ne_bot hμ⟩ LinearMap.id
  have h1 : hwAct (d := d) q hq m μ x = 1 :=
    LinearMap.ext fun v => Subtype.ext (hx v.1 v.2 v.2)
  have h0 : hwAct (d := d) q hq m ν x = 0 :=
    LinearMap.ext fun w => Subtype.ext (hx0 ⟨ν, mem_occWeights_of_ne_bot hν⟩
      (fun h => hne (congrArg Subtype.val h).symm) w.1 w.2)
  refine ⟨x, ?_⟩
  rw [hwTrace_eq_trace_hwAct, hwTrace_eq_trace_hwAct, h1, h0, map_zero, LinearMap.trace_one]
  exact Nat.cast_ne_zero.mpr fun h => hμ (Submodule.finrank_eq_zero.mp h)

/-- A double row weight never carries the column character. -/
theorem cells_ne_col_of_double (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q)
    {μ : Fin d → ℕ} (hμ : IsDom μ) (hs : ∑ y, μ y = 1 + 1) {t : Fin d} (ht : μ t = 2)
    (P : YoungDiagram) (hP : P.cells.card = 1 + 1)
    (hPtr : ∀ z, hwTrace q hq 1 μ z = (seminormalRep q hq hgen 1 hP z).trace) :
    P.cells ≠ {(0, 0), (1, 0)} := by
  intro hc
  have hq2 := sub_inv_ne_zero_of_notRootOfUnity hq hgen
  have hsq : q ^ 2 ≠ 1 := by
    intro h; apply hq2
    have : q⁻¹ = q := inv_eq_of_mul_eq_one_right (by rw [← sq]; exact h)
    rw [this, sub_self]
  have e1 := hPtr 1
  rw [hwTrace_one, map_one, Matrix.trace_one] at e1
  have eσ := hPtr (Hecke.σ L q q⁻¹ 1 0)
  rw [hwTrace_σ_zero_of_double q hq ht,
    trace_seminormalRep_σ_zero q hq hgen hP (-1) (axialDist_one_col hP hc),
    Seminormal.seminormalParam_neg_one q hq hsq, ← e1] at eσ
  have hn : (Module.finrank L (hwSpace q 1 μ) : L) ≠ 0 :=
    Nat.cast_ne_zero.mpr fun h =>
      hwSpace_ne_bot_of_dom q hq hgen 1 hμ hs (Submodule.finrank_eq_zero.mp h)
  have h' := mul_right_cancel₀ hn (eσ.trans (mul_comm _ _))
  field_simp at h'
  nlinarith [sq_nonneg q]

end Base


section Ident

variable {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L] {d : ℕ} [NeZero d]

/-- The statement at level `m`: every dominant `μ ⊨ m + 1` carries `χ^{λ(μ)}`. -/
def HWCharStatement (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    Prop :=
  ∀ (μ : Fin d → ℕ) (hμ : IsDom μ) (hs : ∑ y, μ y = m + 1) (z : Hecke L q q⁻¹ m),
    hwTrace q hq m μ z = (seminormalRep q hq hgen m ((card_rowDiagram μ hμ).trans hs) z).trace

omit [LinearOrder L] [IsStrictOrderedRing L] [NeZero d] in
theorem hwCharStatement_of_eq (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q)
    (m : ℕ) {μ : Fin d → ℕ} (hμ : IsDom μ) (hs : ∑ y, μ y = m + 1) (P : YoungDiagram)
    (hP : P.cells.card = m + 1)
    (hPtr : ∀ z, hwTrace q hq m μ z = (seminormalRep q hq hgen m hP z).trace)
    (h : P = rowDiagram μ hμ) (z : Hecke L q q⁻¹ m) :
    hwTrace q hq m μ z
      = (seminormalRep q hq hgen m ((card_rowDiagram μ hμ).trans hs) z).trace := by
  rw [hPtr z]; exact trace_seminormalRep_congr q hq hgen m h _ _ z

theorem hwCharStatement_zero (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q) :
    HWCharStatement (d := d) q hq hgen 0 := by
  intro μ hμ hs z
  obtain ⟨P, hP, hPtr⟩ := exists_shape q hq hgen 0 hμ hs
  exact hwCharStatement_of_eq q hq hgen 0 hμ hs P hP hPtr
    (eq_of_card_one hP ((card_rowDiagram μ hμ).trans hs)) z

omit [NeZero d] in
theorem exists_double_of_row {μ : Fin d → ℕ} (hμ : IsDom μ) (hs : ∑ y, μ y = 1 + 1)
    (h : (0, 1) ∈ rowDiagram μ hμ) : ∃ t, μ t = 2 := by
  classical
  obtain ⟨y, -, hy⟩ := (mem_rowDiagram μ hμ _).1 h
  refine ⟨y, le_antisymm ?_ hy⟩
  have := Finset.single_le_sum (f := μ) (fun _ _ => Nat.zero_le _) (Finset.mem_univ y)
  omega

theorem hwCharStatement_one (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q) :
    HWCharStatement (d := d) q hq hgen 1 := by
  classical
  intro μ hμ hs z
  obtain ⟨P, hP, hPtr⟩ := exists_shape q hq hgen 1 hμ hs
  have hΛ : (rowDiagram μ hμ).cells.card = 2 := (card_rowDiagram μ hμ).trans hs
  refine hwCharStatement_of_eq q hq hgen 1 hμ hs P hP hPtr ?_ z
  rcases cells_of_card_two _ hΛ with hrow | hcol
  · -- `λ(μ)` is the row: `μ` is a double row, and `P` cannot be the column
    obtain ⟨t, ht⟩ := exists_double_of_row hμ hs
      ((YoungDiagram.mem_cells _).1 (by rw [hrow]; simp))
    rcases cells_of_card_two P hP with hP' | hP'
    · exact YoungDiagram.ext (hP'.trans hrow.symm)
    · exact absurd hP' (cells_ne_col_of_double q hq hgen hμ hs ht P hP hPtr)
  · rcases cells_of_card_two P hP with hP' | hP'
    · exfalso
      -- the double row weight `ν` at the last letter also carries the row character
      obtain ⟨y, hy1, -⟩ := (mem_rowDiagram μ hμ _).1
        ((YoungDiagram.mem_cells _).1 (show ((1 : ℕ), (0 : ℕ)) ∈ _ by rw [hcol]; simp))
      have hd : 2 ≤ d := by have := y.isLt; simp at hy1; omega
      set t : Fin d := ⟨d - 1, by omega⟩
      set ν : Fin d → ℕ := Pi.single t 2
      have hνt : ν t = 2 := by simp [ν]
      have hν : IsDom ν := by
        intro i j hij
        have hi : i ≠ t := fun h => by
          have := j.isLt; rw [h] at hij; simp [t] at hij; omega
        simp [ν, Pi.single_apply, hi]
      have hνs : ∑ y, ν y = 1 + 1 := by simp [ν]
      obtain ⟨P', hP'c, hP'tr⟩ := exists_shape q hq hgen 1 hν hνs
      have hP'row : P'.cells = {(0, 0), (0, 1)} := by
        rcases cells_of_card_two P' hP'c with h | h
        · exact h
        · exact absurd h (cells_ne_col_of_double q hq hgen hν hνs hνt P' hP'c hP'tr)
      have hPP : P' = P := YoungDiagram.ext (hP'row.trans hP'.symm)
      have hne : ν ≠ μ := by
        intro h
        have h01 : ((0 : ℕ), (1 : ℕ)) ∈ (rowDiagram μ hμ).cells :=
          (YoungDiagram.mem_cells _).2 ((mem_rowDiagram μ hμ _).2
            ⟨t, by simp [t], by rw [← h, hνt]; norm_num⟩)
        rw [hcol] at h01; simp at h01
      obtain ⟨w, hw⟩ := exists_hwTrace_ne q hq hgen 1 (hwSpace_ne_bot_of_dom q hq hgen 1 hν hνs)
        (hwSpace_ne_bot_of_dom q hq hgen 1 hμ hs) hne
      apply hw
      rw [hP'tr w, hPtr w]
      exact trace_seminormalRep_congr q hq hgen 1 hPP _ _ w
    · exact YoungDiagram.ext (hP'.trans hcol.symm)

/-- **The induction step**, above size two: the corner counting identity and the
reconstruction lemma force the shape of `HW_μ` to be `λ(μ)`. -/
theorem hwCharStatement_succ (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (hm : 1 ≤ m) (ih : HWCharStatement (d := d) q hq hgen m) :
    HWCharStatement (d := d) q hq hgen (m + 1) := by
  classical
  intro μ hμ hsum z
  obtain ⟨P, hP, hPtr⟩ := exists_shape q hq hgen (m + 1) hμ hsum
  refine hwCharStatement_of_eq q hq hgen (m + 1) hμ hsum P hP hPtr ?_ z
  have hΛ : (rowDiagram μ hμ).cells.card = m + 2 := (card_rowDiagram μ hμ).trans hsum
  have key := card_erase_eq q hq hgen m μ hμ hsum P hP hPtr (fun ν hν hs z => ih ν hν hs z)
  refine eq_of_eraseCorner_iff P _ (hP.trans hΛ.symm) (by omega) ?_ ?_
  · intro p hp
    set ν : Partition (m + 1) :=
      (partitionShapeEquiv (m + 1)).symm ⟨eraseCorner P p hp, card_eraseCorner_of_card p hp hP⟩
    have hν : partitionShape ν = eraseCorner P p hp := by
      rw [← partitionShapeEquiv_apply, Equiv.apply_symm_apply]
    have hpos := key ν
    have hl : 0 < (Finset.univ.filter fun c : {c : ℕ × ℕ // IsCornerCell P c} =>
        eraseCorner P c.1 c.2 = partitionShape ν).card :=
      Finset.card_pos.mpr ⟨⟨p, hp⟩, by simp [hν]⟩
    rw [hpos] at hl
    obtain ⟨x, hx⟩ := Finset.card_pos.mp hl
    obtain ⟨h, hx⟩ := (Finset.mem_filter.mp hx).2
    exact ⟨cornerOf μ x, isCornerCell_cornerOf hμ h.1 h.2, by
      rw [eraseCorner_cornerOf hμ h.1 h.2, hx, hν]⟩
  · intro c hc
    obtain ⟨x, hx0, hxd, rfl⟩ := exists_cornerOf hμ hc
    have hcard : (rowDiagram _ hxd).cells.card = m + 1 := by
      rw [card_rowDiagram]; have := sum_sub_single (μ := μ) hx0; omega
    set ν : Partition (m + 1) := (partitionShapeEquiv (m + 1)).symm ⟨rowDiagram _ hxd, hcard⟩
    have hν : partitionShape ν = rowDiagram _ hxd := by
      rw [← partitionShapeEquiv_apply, Equiv.apply_symm_apply]
    have hr : 0 < (Finset.univ.filter fun x : Fin d =>
        ∃ h : 0 < μ x ∧ IsDom (μ - Pi.single x 1), rowDiagram _ h.2 = partitionShape ν).card :=
      Finset.card_pos.mpr ⟨x, Finset.mem_filter.mpr ⟨Finset.mem_univ _, ⟨hx0, hxd⟩, hν.symm⟩⟩
    rw [← key ν] at hr
    obtain ⟨p, hp⟩ := Finset.card_pos.mp hr
    refine ⟨p.1, p.2, ?_⟩
    rw [eraseCorner_cornerOf hμ hx0 hxd, (Finset.mem_filter.mp hp).2, hν]

/-- **`tr(z | HW_μ) = χ^{λ(μ)}(z)`** for every dominant `μ`, at every level. -/
theorem hwCharStatement_all (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q)
    (m : ℕ) : HWCharStatement (d := d) q hq hgen m := by
  induction m with
  | zero => exact hwCharStatement_zero q hq hgen
  | succ k ih =>
    rcases Nat.eq_zero_or_pos k with rfl | hk
    · exact hwCharStatement_one q hq hgen
    · exact hwCharStatement_succ q hq hgen k hk ih

end Ident

section AbstractIso

variable {L A V W : Type*} [Field L] [Ring A] [Algebra L A]
  [AddCommGroup V] [Module L V] [FiniteDimensional L V]
  [AddCommGroup W] [Module L W] [FiniteDimensional L W]

/-- A nonzero vector has a functional taking it to `1`. -/
theorem exists_dual_eq_one {v : V} (hv : v ≠ 0) : ∃ f : Module.Dual L V, f v = 1 := by
  obtain ⟨f, hf⟩ : ∃ f : Module.Dual L V, f v ≠ 0 := by
    by_contra h; push_neg at h; exact hv ((Module.forall_dual_apply_eq_zero_iff L v).1 h)
  exact ⟨(f v)⁻¹ • f, by simp [hf]⟩

/-- The trace form on `End W` is nondegenerate. -/
theorem eq_zero_of_trace_mul_eq_zero (X : Module.End L W)
    (h : ∀ M : Module.End L W, LinearMap.trace L W (X * M) = 0) : X = 0 := by
  ext w
  by_contra hw
  obtain ⟨f, hf⟩ := exists_dual_eq_one (L := L) hw
  have := h (f.smulRight w)
  rw [show X * f.smulRight w = f.smulRight (X w) by ext; simp, LinearMap.trace_smulRight] at this
  simp [this] at hf

/-- **Two surjective representations with equal traces are isomorphic.**  If
`ρ₁ : A → End V` and `ρ₂ : A → End W` are onto, `dim V = dim W > 0`, and
`tr ρ₁(z) = tr ρ₂(z)` for every `z`, then there is a linear isomorphism `V ≃ W` intertwining
them. -/
theorem exists_linearEquiv_of_trace_eq (ρ₁ : A →ₐ[L] Module.End L V)
    (ρ₂ : A →ₐ[L] Module.End L W) (h₁ : Function.Surjective ρ₁) (h₂ : Function.Surjective ρ₂)
    (hdim : Module.finrank L V = Module.finrank L W) (hV : 0 < Module.finrank L V)
    (htr : ∀ z, LinearMap.trace L V (ρ₁ z) = LinearMap.trace L W (ρ₂ z)) :
    ∃ e : V ≃ₗ[L] W, ∀ z v, e (ρ₁ z v) = ρ₂ z (e v) := by
  classical
  haveI := Module.nontrivial_of_finrank_pos hV
  have hker : ∀ z, ρ₁ z = 0 → ρ₂ z = 0 := by
    intro z hz
    apply eq_zero_of_trace_mul_eq_zero
    intro M
    obtain ⟨y, rfl⟩ := h₂ M
    rw [← map_mul, ← htr, map_mul, hz, zero_mul, map_zero]
  obtain ⟨s, hs⟩ := LinearMap.exists_rightInverse_of_surjective ρ₁.toLinearMap
    (LinearMap.range_eq_top.2 h₁)
  have hs' : ∀ X, ρ₁ (s X) = X := fun X => LinearMap.congr_fun hs X
  have hψ : ∀ z, ρ₂ (s (ρ₁ z)) = ρ₂ z := by
    intro z
    have h0 := hker (s (ρ₁ z) - z) (by rw [map_sub, hs', sub_self])
    rwa [map_sub, sub_eq_zero] at h0
  obtain ⟨v₀, hv₀⟩ := exists_ne (0 : V)
  obtain ⟨f₀, hf₀⟩ := exists_dual_eq_one (L := L) hv₀
  have hP : ρ₂ (s (f₀.smulRight v₀)) ≠ 0 := by
    intro h0
    have := htr (s (f₀.smulRight v₀))
    rw [hs', h0, LinearMap.trace_smulRight, hf₀, map_zero] at this
    exact one_ne_zero this
  obtain ⟨w₀, hw₀⟩ : ∃ w, ρ₂ (s (f₀.smulRight v₀)) w ≠ 0 := by
    by_contra h; push_neg at h; exact hP (LinearMap.ext h)
  have hR_add : ∀ v v' : V, f₀.smulRight (v + v') = f₀.smulRight v + f₀.smulRight v' := by
    intro v v'; ext; simp [smul_add]
  have hR_smul : ∀ (c : L) (v : V), f₀.smulRight (c • v) = c • f₀.smulRight v := by
    intro c v; ext; simp [smul_comm c]
  let φ : V →ₗ[L] W :=
    { toFun := fun v => ρ₂ (s (f₀.smulRight v)) w₀
      map_add' := fun v v' => by simp [hR_add]
      map_smul' := fun c v => by simp [hR_smul] }
  have hφ : ∀ z v, φ (ρ₁ z v) = ρ₂ z (φ v) := by
    intro z v
    have : f₀.smulRight (ρ₁ z v) = ρ₁ (z * s (f₀.smulRight v)) := by
      rw [map_mul, hs']; ext; simp
    show ρ₂ (s (f₀.smulRight (ρ₁ z v))) w₀ = ρ₂ z (ρ₂ (s (f₀.smulRight v)) w₀)
    rw [this, hψ, map_mul, Module.End.mul_apply]
  have hsurj : Function.Surjective φ := by
    intro w
    obtain ⟨g, hg⟩ := exists_dual_eq_one (L := L) (show φ v₀ ≠ 0 from hw₀)
    obtain ⟨z, hz⟩ := h₂ (g.smulRight w)
    exact ⟨ρ₁ z v₀, by rw [hφ, hz]; simp [hg]⟩
  have hinj : Function.Injective φ :=
    (LinearMap.injective_iff_surjective_of_finrank_eq_finrank hdim).2 hsurj
  exact ⟨LinearEquiv.ofBijective φ ⟨hinj, hsurj⟩, fun z v => hφ z v⟩

end AbstractIso

section ModuleIso

open QOU.Mathlib QOU.SchurWeyl.SeminormalRep
open scoped Matrix

variable {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L] {d : ℕ} [NeZero d]

/-- **`HW_μ ≅ S_{λ(μ)}` as `H_{m+1}(q)`-modules.**  For a dominant weight `μ` of total weight
`m + 1`, the highest-weight space `HW_μ` is isomorphic, as a module over the Hecke algebra, to the
seminormal (Specht) representation of the row diagram `λ(μ)`. -/
theorem exists_hwSpace_equiv_specht (q : L) (hq : q ≠ 0)
    (hgen : GenericParameter.NotRootOfUnity q) (m : ℕ) (μ : Fin d → ℕ) (hμ : IsDom μ)
    (hs : ∑ y, μ y = m + 1) :
    ∃ e : hwSpace q m μ ≃ₗ[L] (StandardYoungTableau (rowDiagram μ hμ) → L),
      ∀ (z : Hecke L q q⁻¹ m) (v : hwSpace q m μ),
        e (hwAct q hq m μ z v)
          = seminormalRep q hq hgen m ((card_rowDiagram μ hμ).trans hs) z *ᵥ e v := by
  classical
  set ρ := seminormalRep q hq hgen m ((card_rowDiagram μ hμ).trans hs)
  let ρ₂ := (Matrix.toLinAlgEquiv' (R := L)
    (n := StandardYoungTableau (rowDiagram μ hμ))).toAlgHom.comp ρ
  have hocc := mem_occWeights_of_ne_bot (hwSpace_ne_bot_of_dom q hq hgen m hμ hs)
  have hdim : Module.finrank L (hwSpace q m μ)
      = Module.finrank L (StandardYoungTableau (rowDiagram μ hμ) → L) := by
    rw [finrank_hwSpace_eq_numSYT q hq hgen m μ hμ hs, Module.finrank_fintype_fun_eq_card,
      numStandardYoungTableaux, Nat.card_eq_fintype_card]
  have h₂ : Function.Surjective ρ₂ := by
    intro M
    have : LinearMap.toMatrix' M ∈ ρ.range := by
      rw [seminormalRep_range_eq_top]; trivial
    obtain ⟨z, hz⟩ := this
    refine ⟨z, ?_⟩
    change Matrix.toLin' (ρ z) = M
    rw [show ρ z = LinearMap.toMatrix' M from hz, Matrix.toLin'_toMatrix']
  have htr : ∀ z, LinearMap.trace L _ (hwAct q hq m μ z) = LinearMap.trace L _ (ρ₂ z) := by
    intro z
    rw [← hwTrace_eq_trace_hwAct, hwCharStatement_all q hq hgen m μ hμ hs z]
    simp only [ρ₂, LinearMap.trace_eq_matrix_trace L (Pi.basisFun L _),
      LinearMap.toMatrix_eq_toMatrix']
    change _ = (LinearMap.toMatrix' (Matrix.toLin' (ρ z))).trace
    rw [LinearMap.toMatrix'_toLin']
  obtain ⟨e, he⟩ := exists_linearEquiv_of_trace_eq (hwAct q hq m μ) ρ₂
    (hwAct_surjective q hq hgen m hocc) h₂ hdim
    (by rw [finrank_hwSpace_eq_numSYT q hq hgen m μ hμ hs]; exact numStandardYoungTableaux_pos _)
    htr
  exact ⟨e, fun z v => by rw [he]; simp [ρ₂]⟩

end ModuleIso

end QOU.SchurWeyl.QuantumGL
