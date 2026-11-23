/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Data.Finset.Sort
import Mathlib.Data.Finsupp.Basic
import Mathlib.Data.PNat.Basic
import Mathlib.Algebra.BigOperators.Group.List.Basic

/-!
# Increasing words and multi-indices

When every block of the splay is one-dimensional (the basis of `Aᵢ` is `bᵢ(n)`, `n ∈ ℕ`,
with `bᵢ(0) = 1`), a PBW normal monomial is a word `⟨i₁, n₁⟩ ⋯ ⟨iₖ, nₖ⟩` with
`i₁ < ⋯ < iₖ` and `nⱼ > 0`. This file proves that such words are in bijection with
multi-indices `J : I →₀ ℕ`:

* `toWord J` lists `⟨i, J i⟩` over the `i` with `J i ≠ 0`, in increasing order;
* `ofWord w` reads the multi-index back;
* `wordEquiv : {w // IsIncr w} ≃ (I →₀ ℕ)`.

No `sorry`, no axiom beyond Lean's three.
-/

set_option linter.unusedSectionVars false

namespace QOU.FormalGroups.PBW

variable {I : Type*} [LinearOrder I] [Fintype I]

/-- A word whose blocks strictly increase. -/
def IsIncr (w : List (Σ _ : I, ℕ+)) : Prop := w.IsChain fun a c => a.1 < c.1

theorem isIncr_iff_pairwise (w : List (Σ _ : I, ℕ+)) :
    IsIncr w ↔ w.Pairwise fun a c => a.1 < c.1 := by
  haveI : IsTrans (Σ _ : I, ℕ+) fun a c => a.1 < c.1 := ⟨fun _ _ _ h1 h2 => h1.trans h2⟩
  exact List.isChain_iff_pairwise

/-- The letter of `i` in `J`, if `J i ≠ 0`. -/
def letterOf (J : I →₀ ℕ) (i : I) : Option (Σ _ : I, ℕ+) :=
  if h : J i = 0 then none else some ⟨i, ⟨J i, Nat.pos_of_ne_zero h⟩⟩

/-- The increasing word of a multi-index. -/
noncomputable def toWord (J : I →₀ ℕ) : List (Σ _ : I, ℕ+) :=
  (Finset.univ.sort (· ≤ ·)).filterMap (letterOf J)

/-- The multi-index of a word. -/
noncomputable def ofWord (w : List (Σ _ : I, ℕ+)) : I →₀ ℕ :=
  (w.map fun g => Finsupp.single g.1 (g.2 : ℕ)).sum

theorem ofWord_nil : ofWord ([] : List (Σ _ : I, ℕ+)) = 0 := rfl

theorem ofWord_cons (g : Σ _ : I, ℕ+) (w : List (Σ _ : I, ℕ+)) :
    ofWord (g :: w) = Finsupp.single g.1 (g.2 : ℕ) + ofWord w := by
  simp [ofWord]

theorem mem_toWord (J : I →₀ ℕ) (g : Σ _ : I, ℕ+) : g ∈ toWord J ↔ (g.2 : ℕ) = J g.1 := by
  obtain ⟨i, n⟩ := g
  simp only [toWord, List.mem_filterMap, Finset.mem_sort, Finset.mem_univ, true_and, letterOf]
  constructor
  · rintro ⟨j, hj⟩
    split_ifs at hj with h
    cases hj; rfl
  · intro h
    refine ⟨i, ?_⟩
    rw [dif_neg (by rw [← h]; exact n.ne_zero)]
    congr; exact h.symm

theorem toWord_pairwise (J : I →₀ ℕ) : (toWord J).Pairwise fun a c => a.1 < c.1 := by
  unfold toWord
  rw [List.pairwise_filterMap]
  refine (Finset.sort_sorted_lt _).imp ?_
  intro a c hac b hb b' hb'
  simp only [letterOf] at hb hb'
  split_ifs at hb hb'
  cases hb; cases hb'; exact hac

theorem toWord_isIncr (J : I →₀ ℕ) : IsIncr (toWord J) :=
  (isIncr_iff_pairwise _).2 (toWord_pairwise J)

theorem ofWord_apply_of_forall_ne (w : List (Σ _ : I, ℕ+)) (i : I) (h : ∀ g ∈ w, g.1 ≠ i) :
    ofWord w i = 0 := by
  induction w with
  | nil => rfl
  | cons g w ih =>
    rw [ofWord_cons, Finsupp.add_apply, Finsupp.single_eq_of_ne (h g (by simp)).symm,
      ih fun g' hg' => h g' (by simp [hg']), add_zero]

theorem ofWord_apply_of_mem (w : List (Σ _ : I, ℕ+)) (hw : w.Pairwise fun a c => a.1 < c.1)
    (g : Σ _ : I, ℕ+) (hg : g ∈ w) : ofWord w g.1 = g.2 := by
  induction w with
  | nil => simp at hg
  | cons g' w ih =>
    rw [List.pairwise_cons] at hw
    rw [ofWord_cons, Finsupp.add_apply]
    rcases List.mem_cons.1 hg with rfl | hg
    · rw [Finsupp.single_eq_same, ofWord_apply_of_forall_ne w _
        fun g'' hg'' => (ne_of_lt (hw.1 g'' hg'')).symm, add_zero]
    · rw [Finsupp.single_eq_of_ne (ne_of_lt (hw.1 g hg)).symm, zero_add, ih hw.2 hg]

theorem ofWord_toWord (J : I →₀ ℕ) : ofWord (toWord J) = J := by
  ext i
  by_cases h : J i = 0
  · rw [h, ofWord_apply_of_forall_ne]
    intro g hg hgi
    rw [mem_toWord, hgi, h] at hg
    exact g.2.ne_zero hg
  · have hm : (⟨i, ⟨J i, Nat.pos_of_ne_zero h⟩⟩ : Σ _ : I, ℕ+) ∈ toWord J := by
      rw [mem_toWord]; rfl
    exact ofWord_apply_of_mem _ (toWord_pairwise J) _ hm

theorem mem_iff_of_pairwise (w : List (Σ _ : I, ℕ+)) (hw : w.Pairwise fun a c => a.1 < c.1)
    (g : Σ _ : I, ℕ+) : g ∈ w ↔ (g.2 : ℕ) = ofWord w g.1 := by
  constructor
  · intro hg; exact (ofWord_apply_of_mem w hw g hg).symm
  · intro h
    by_contra hg
    by_cases hex : ∃ g' ∈ w, g'.1 = g.1
    · obtain ⟨g', hg', he⟩ := hex
      have h' := ofWord_apply_of_mem w hw g' hg'
      rw [he, ← h] at h'
      obtain ⟨i, n⟩ := g
      obtain ⟨i', n'⟩ := g'
      simp only at he h'
      subst he
      exact hg (by rw [PNat.eq h']; exact hg')
    · push_neg at hex
      rw [ofWord_apply_of_forall_ne w _ hex] at h
      exact g.2.ne_zero h

theorem toWord_ofWord (w : List (Σ _ : I, ℕ+)) (hw : IsIncr w) : toWord (ofWord w) = w := by
  rw [isIncr_iff_pairwise] at hw
  haveI : IsAntisymm (Σ _ : I, ℕ+) fun a c => a.1 < c.1 :=
    ⟨fun _ _ h1 h2 => absurd (h1.trans h2) (lt_irrefl _)⟩
  haveI : IsIrrefl (Σ _ : I, ℕ+) fun a c => a.1 < c.1 := ⟨fun _ h => lt_irrefl _ h⟩
  refine List.Sorted.eq_of_mem_iff (toWord_pairwise _) hw fun g => ?_
  rw [mem_toWord, mem_iff_of_pairwise w hw]

/-- Increasing words are multi-indices. -/
noncomputable def wordEquiv : {w : List (Σ _ : I, ℕ+) // IsIncr w} ≃ (I →₀ ℕ) where
  toFun w := ofWord w.1
  invFun J := ⟨toWord J, toWord_isIncr J⟩
  left_inv w := Subtype.ext (toWord_ofWord w.1 w.2)
  right_inv J := ofWord_toWord J

/-- The product of `f` over the increasing word of `J`, in terms of an ordered list of all
indices: `∏_{i ∈ l} e i (J i)` when `e i 0 = 1` and `e i n = f ⟨i, n⟩` for `n > 0`. -/
theorem prod_toWord {M : Type*} [Monoid M] (e : I → ℕ → M) (he0 : ∀ i, e i 0 = 1)
    (J : I →₀ ℕ) :
    ((toWord J).map fun g => e g.1 g.2).prod =
      ((Finset.univ.sort (· ≤ ·)).map fun i => e i (J i)).prod := by
  unfold toWord
  induction (Finset.univ.sort (· ≤ ·) : List I) with
  | nil => rfl
  | cons i l ih =>
    by_cases h : J i = 0
    · have hn : letterOf J i = none := by simp [letterOf, h]
      rw [List.filterMap_cons_none hn, ih, List.map_cons, List.prod_cons, h, he0, one_mul]
    · have hs : letterOf J i = some ⟨i, ⟨J i, Nat.pos_of_ne_zero h⟩⟩ := by simp [letterOf, h]
      rw [List.filterMap_cons_some hs, List.map_cons, List.prod_cons, ih, List.map_cons,
        List.prod_cons]
      rfl

end QOU.FormalGroups.PBW
