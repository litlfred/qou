/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.QuantumGLHWBranching
import QOU.Mathlib.SYTBranchingRule
import QOU.Mathlib.NumSYTPos

/-!
# `dim HW_λ ≤ f^λ`

G3.4c (bean `qou-gl343`), part 2.

A dominant weight `μ : Fin d → ℕ` (`μ 0 ≤ μ 1 ≤ … ≤ μ (d−1)`, see `QuantumGLDominance`) is read as a
Young diagram `rowDiagram μ` whose row `r` has length `μ (d − 1 − r)`.  Removing one box from row
`d − 1 − x` is `μ ↦ μ − e_x`, and this is a removable corner exactly when `μ − e_x` is still
dominant (`isCornerCell_cornerOf`, `eraseCorner_cornerOf`).

`finrank_hwSpace_le_numSYT`: for every dominant `μ`,
`dim HW_μ ≤ #SYT(rowDiagram μ)`, by induction on the length, from
* the branching bound `finrank_hwSpace_succ_le` (`QuantumGLHWBranching`),
* dominance `le_of_mem_hwSpace` (non-dominant terms vanish),
* the weight-sum constraint `hwSpace_eq_bot_of_sum_ne`, and
* the SYT branching rule `numStandardYoungTableaux_branching`.

This is the inequality `(★)` needed by the double-centraliser argument of G3.4 (PR #7864).

## Base ring (§7c)

Any field; `q` not a root of unity (used only through dominance).

-- Ref: [kassel1995] C. Kassel, *Quantum Groups*, GTM 155, Ch. VII.
-/

namespace QOU.SchurWeyl.QuantumGL

open QOU.IwahoriHecke.TensorEmbedGL Matrix QOU.Mathlib

section Diagram

variable {d : ℕ}

/-- Dominance in the index convention of `QuantumGLDominance`: `μ i ≤ μ (i+1)`. -/
def IsDom (μ : Fin d → ℕ) : Prop := ∀ i j : Fin d, (j : ℕ) = i + 1 → μ i ≤ μ j

theorem IsDom.monotone {μ : Fin d → ℕ} (h : IsDom μ) : Monotone μ := by
  intro a b hab
  rw [Fin.le_def] at hab
  obtain ⟨k, hk⟩ : ∃ k, (b : ℕ) = a + k := ⟨b - a, by omega⟩
  induction k generalizing b with
  | zero => rw [show a = b from Fin.ext (by omega)]
  | succ k ih =>
      have hb' : (b : ℕ) - 1 < d := by omega
      have hb1 : ((⟨b - 1, hb'⟩ : Fin d) : ℕ) = b - 1 := rfl
      exact (ih (b := ⟨b - 1, hb'⟩) (by rw [hb1]; omega) (by rw [hb1]; omega)).trans
        (h ⟨b - 1, hb'⟩ b (by rw [hb1]; omega))

/-- The cells: row `d − 1 − y` has length `μ y`. -/
def rowCells (μ : Fin d → ℕ) : Finset (ℕ × ℕ) :=
  Finset.univ.biUnion fun y : Fin d => (Finset.range (μ y)).image fun c => (d - 1 - (y : ℕ), c)

theorem mem_rowCells (μ : Fin d → ℕ) (p : ℕ × ℕ) :
    p ∈ rowCells μ ↔ ∃ y : Fin d, p.1 = d - 1 - y ∧ p.2 < μ y := by
  simp only [rowCells, Finset.mem_biUnion, Finset.mem_univ, true_and, Finset.mem_image,
    Finset.mem_range]
  constructor
  · rintro ⟨y, c, hc, rfl⟩; exact ⟨y, rfl, hc⟩
  · rintro ⟨y, h1, h2⟩; exact ⟨y, p.2, h2, by rw [← h1]⟩

/-- The Young diagram of a dominant weight. -/
def rowDiagram (μ : Fin d → ℕ) (hμ : IsDom μ) : YoungDiagram where
  cells := rowCells μ
  isLowerSet := by
    intro a b hba ha
    rw [Finset.mem_coe, mem_rowCells] at ha ⊢
    obtain ⟨y, h1, h2⟩ := ha
    have hy := y.isLt
    refine ⟨⟨d - 1 - b.1, by omega⟩, by simp; have := hba.1; omega, ?_⟩
    have hle : y ≤ (⟨d - 1 - b.1, by omega⟩ : Fin d) := by
      rw [Fin.le_def]; simp; have := hba.1; omega
    exact lt_of_le_of_lt hba.2 (lt_of_lt_of_le h2 (hμ.monotone hle))

theorem mem_rowDiagram (μ : Fin d → ℕ) (hμ : IsDom μ) (p : ℕ × ℕ) :
    p ∈ rowDiagram μ hμ ↔ ∃ y : Fin d, p.1 = d - 1 - y ∧ p.2 < μ y :=
  mem_rowCells μ p

/-- The last box of row `d − 1 − x`. -/
def cornerOf (μ : Fin d → ℕ) (x : Fin d) : ℕ × ℕ := (d - 1 - x, μ x - 1)

theorem cornerOf_injective (μ : Fin d → ℕ) : Function.Injective (cornerOf μ) := by
  intro x y h
  have := congrArg Prod.fst h
  simp only [cornerOf] at this
  have := x.isLt; have := y.isLt
  exact Fin.ext (by omega)

theorem isDom_sub_lt {μ : Fin d → ℕ} {x : Fin d} (hx : 0 < μ x)
    (h : IsDom (μ - Pi.single x 1)) (y : Fin d) (hy : (x : ℕ) = y + 1) : μ y < μ x := by
  have := h y x hy
  have hyx : y ≠ x := fun e => by rw [e] at hy; omega
  simp only [Pi.sub_apply, Pi.single_eq_same, Pi.single_eq_of_ne hyx] at this
  omega

theorem isCornerCell_cornerOf {μ : Fin d → ℕ} (hμ : IsDom μ) {x : Fin d} (hx : 0 < μ x)
    (h : IsDom (μ - Pi.single x 1)) : IsCornerCell (rowDiagram μ hμ) (cornerOf μ x) := by
  have hxd := x.isLt
  refine ⟨(mem_rowDiagram μ hμ _).mpr ⟨x, rfl, by simp [cornerOf]; omega⟩, ?_, ?_⟩
  · rw [mem_rowDiagram]
    rintro ⟨y, h1, h2⟩
    simp only [cornerOf] at h1 h2
    have hyd := y.isLt
    have := isDom_sub_lt hx h y (by omega)
    omega
  · rw [mem_rowDiagram]
    rintro ⟨y, h1, h2⟩
    simp only [cornerOf] at h1 h2
    have hyd := y.isLt
    have : y = x := Fin.ext (by omega)
    subst this
    omega

theorem eraseCorner_cornerOf {μ : Fin d → ℕ} (hμ : IsDom μ) {x : Fin d} (hx : 0 < μ x)
    (h : IsDom (μ - Pi.single x 1)) :
    eraseCorner (rowDiagram μ hμ) (cornerOf μ x) (isCornerCell_cornerOf hμ hx h)
      = rowDiagram (μ - Pi.single x 1) h := by
  ext p
  show p ∈ eraseCorner _ _ _ ↔ p ∈ rowDiagram _ h
  rw [mem_eraseCorner, mem_rowDiagram, mem_rowDiagram]
  have hxd := x.isLt
  constructor
  · rintro ⟨⟨y, h1, h2⟩, hne⟩
    refine ⟨y, h1, ?_⟩
    by_cases hyx : y = x
    · subst hyx
      simp only [Pi.sub_apply, Pi.single_eq_same]
      have : p.2 ≠ μ y - 1 := fun e => hne (Prod.ext h1 e)
      omega
    · simpa [Pi.single_eq_of_ne hyx] using h2
  · rintro ⟨y, h1, h2⟩
    by_cases hyx : y = x
    · subst hyx
      simp only [Pi.sub_apply, Pi.single_eq_same] at h2
      refine ⟨⟨y, h1, by omega⟩, fun e => ?_⟩
      rw [e] at h2; simp [cornerOf] at h2
    · simp only [Pi.sub_apply, Pi.single_eq_of_ne hyx, tsub_zero] at h2
      refine ⟨⟨y, h1, h2⟩, fun e => ?_⟩
      have := y.isLt
      rw [e] at h1; simp [cornerOf] at h1
      exact hyx (Fin.ext (by omega))

end Diagram

section Bound

variable {K : Type*} [Field K] {d : ℕ}

theorem sum_content {n : ℕ} (a : Fin n → Fin d) : ∑ y, content a y = n := by
  classical
  simp only [content]
  rw [← Finset.card_eq_sum_card_fiberwise (fun k _ => Finset.mem_univ (a k))]
  simp

/-- A highest-weight space of the wrong total weight is zero. -/
theorem hwSpace_eq_bot_of_sum_ne (q : K) (m : ℕ) (μ : Fin d → ℕ) (h : ∑ y, μ y ≠ m + 1) :
    hwSpace q m μ = ⊥ := by
  rw [Submodule.eq_bot_iff]
  rintro v ⟨hv, -⟩
  funext a
  have := congrFun hv a
  rw [weightProj_mulVec_apply, if_neg] at this
  · exact this.symm
  · intro hc; apply h; rw [← hc, sum_content]

theorem isDom_of_ne_bot (q : K) (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0)
    (hgen : GenericParameter.NotRootOfUnity q) (m : ℕ) (μ : Fin d → ℕ)
    (h : hwSpace q m μ ≠ ⊥) : IsDom μ := by
  obtain ⟨v, hv, hv0⟩ := (Submodule.ne_bot_iff _).mp h
  exact fun i j hij => le_of_mem_hwSpace q hq hq2 hgen m μ hv hv0 hij

/-- On one site a highest-weight space has dimension at most `1`. -/
theorem finrank_hwSpace_zero_le_one (q : K) (μ : Fin d → ℕ) :
    Module.finrank K (hwSpace q 0 μ) ≤ 1 := by
  by_cases hb : hwSpace q 0 μ = ⊥
  · rw [hb, finrank_bot]; exact Nat.zero_le _
  obtain ⟨v, hv, hv0⟩ := (Submodule.ne_bot_iff _).mp hb
  obtain ⟨a, ha⟩ : ∃ a, v a ≠ 0 := by
    by_contra hc; push_neg at hc; exact hv0 (funext hc)
  have hca : content a = μ := by
    by_contra hc
    have := congrFun hv.1 a
    rw [weightProj_mulVec_apply, if_neg hc] at this
    exact ha this.symm
  have hsupp : ∀ w ∈ hwSpace q 0 μ, ∀ b, b ≠ a → w b = 0 := by
    intro w hw b hba
    have := congrFun hw.1 b
    rw [weightProj_mulVec_apply, if_neg] at this
    · exact this.symm
    · intro hcb
      apply hba
      funext k
      have hk : k = 0 := Fin.ext (by have := k.isLt; omega)
      subst hk
      have h1 : content a (b 0) = 1 := by
        rw [hca, ← hcb, content_eq_sum, Fin.sum_univ_one, if_pos rfl]
      rw [content_eq_sum, Fin.sum_univ_one] at h1
      by_contra hne
      rw [if_neg (Ne.symm hne)] at h1
      exact absurd h1 (by norm_num)
  let f : hwSpace q 0 μ →ₗ[K] K :=
    { toFun := fun w => w.1 a
      map_add' := fun _ _ => rfl
      map_smul' := fun _ _ => rfl }
  have hf : Function.Injective f := by
    intro w w' h
    apply Subtype.ext
    funext b
    by_cases hba : b = a
    · subst hba; exact h
    · rw [hsupp _ w.2 b hba, hsupp _ w'.2 b hba]
  have := LinearMap.finrank_le_finrank_of_injective hf
  simpa using this

/-- **`dim HW_μ ≤ f^μ`** for every dominant weight `μ`. -/
theorem finrank_hwSpace_le_numSYT (q : K) (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0)
    (hgen : GenericParameter.NotRootOfUnity q) :
    ∀ (m : ℕ) (μ : Fin d → ℕ) (hμ : IsDom μ),
      Module.finrank K (hwSpace q m μ) ≤ numStandardYoungTableaux (rowDiagram μ hμ) := by
  classical
  intro m
  induction m with
  | zero =>
      intro μ hμ
      exact (finrank_hwSpace_zero_le_one q μ).trans (numStandardYoungTableaux_pos _)
  | succ m ih =>
      intro μ hμ
      by_cases hb : hwSpace q (m + 1) μ = ⊥
      · rw [hb, finrank_bot]; exact Nat.zero_le _
      have hsum : ∑ y, μ y = m + 2 := by
        by_contra hc; exact hb (hwSpace_eq_bot_of_sum_ne q (m + 1) μ hc)
      set D := rowDiagram μ hμ
      let F : ℕ × ℕ → ℕ := fun c =>
        if hc : IsCornerCell D c then numStandardYoungTableaux (eraseCorner D c hc) else 0
      let good : Finset (Fin d) :=
        Finset.univ.filter fun x => 0 < μ x ∧ IsDom (μ - Pi.single x 1)
      -- each term of the branching bound
      have hterm : ∀ x : Fin d, Module.finrank K (hwSpace q m (μ - Pi.single x 1))
          ≤ if x ∈ good then F (cornerOf μ x) else 0 := by
        intro x
        by_cases hgx : x ∈ good
        · rw [if_pos hgx]
          obtain ⟨hx, hd⟩ := (Finset.mem_filter.mp hgx).2
          have hc := isCornerCell_cornerOf hμ hx hd
          have : F (cornerOf μ x) = numStandardYoungTableaux (rowDiagram _ hd) := by
            simp only [F, dif_pos hc, D]
            rw [eraseCorner_cornerOf hμ hx hd]
          rw [this]
          exact ih _ hd
        · rw [if_neg hgx]
          have hz : hwSpace q m (μ - Pi.single x 1) = ⊥ := by
            by_contra hne
            have hd := isDom_of_ne_bot q hq hq2 hgen m _ hne
            have hx : 0 < μ x := by
              by_contra h0
              push_neg at h0
              have h0' : μ x = 0 := by omega
              apply hne
              apply hwSpace_eq_bot_of_sum_ne
              have : μ - Pi.single x 1 = μ := by
                funext y
                by_cases hyx : y = x
                · subst hyx; simp [h0']
                · simp [Pi.single_eq_of_ne hyx]
              rw [this, hsum]; omega
            exact hgx (Finset.mem_filter.mpr ⟨Finset.mem_univ _, hx, hd⟩)
          rw [hz, finrank_bot]
      have h1 := (finrank_hwSpace_succ_le q hq m μ).trans (Finset.sum_le_sum fun x _ => hterm x)
      refine h1.trans ?_
      rw [← Finset.sum_filter,
        show (Finset.univ.filter fun x : Fin d => x ∈ good) = good by ext; simp]
      rw [← Finset.sum_image (f := F) (fun x _ y _ h => cornerOf_injective μ h)]
      have hsub : good.image (cornerOf μ) ⊆ D.cells.filter (IsCornerCell D) := by
        intro c hc
        obtain ⟨x, hgx, rfl⟩ := Finset.mem_image.mp hc
        obtain ⟨hx, hd⟩ := (Finset.mem_filter.mp hgx).2
        have hcc := isCornerCell_cornerOf hμ hx hd
        exact Finset.mem_filter.mpr ⟨hcc.1, hcc⟩
      refine (Finset.sum_le_sum_of_subset (f := F) hsub).trans ?_
      rw [Finset.sum_subtype (D.cells.filter (IsCornerCell D))
        (p := IsCornerCell D) (fun c => by simp only [Finset.mem_filter]; exact ⟨fun h => h.2,
          fun h => ⟨h.1, h⟩⟩)]
      by_cases hD : 0 < D.cells.card
      · rw [numStandardYoungTableaux_branching hD]
        exact le_of_eq (Finset.sum_congr rfl fun c _ => by simp only [F, dif_pos c.2])
      · have hDe : D.cells = ∅ := Finset.card_eq_zero.mp (by omega)
        haveI hemp : IsEmpty {c : ℕ × ℕ // IsCornerCell D c} :=
          ⟨fun c => by
            have h : c.1 ∈ D.cells := c.2.1
            rw [hDe] at h; simp at h⟩
        rw [Finset.univ_eq_empty, Finset.sum_empty]; exact Nat.zero_le _

end Bound

end QOU.SchurWeyl.QuantumGL
