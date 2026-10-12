import QOU.Mathlib.MajFormula
import QOU.Mathlib.StandardYoungTableau

/-!
# QOU.Mathlib.MajSYTBridge — `SYTe` is the corpus's standard Young tableau

`QOU.Mathlib.MajStandardization.SYTe μ` presents a standard tableau as an ordering of the cells
(`e : Cell μ ≃ Fin |μ|`, increasing along rows and down columns, entries `0, …, |μ|−1`).
`QOU.Mathlib.StandardYoungTableau μ` presents it as a semistandard tableau whose entry map is a
bijection of the cells onto `{1, …, |μ|}`.

**Theorem** (`sytEquiv`).  The two types are equivalent: shift entries by one.

Consequences:

* `card_SYTe : Fintype.card (SYTe μ) = numStandardYoungTableaux μ`;
* `fmaj_eval_one : (fmaj μ).eval 1 = numStandardYoungTableaux μ` — the `maj` generating function
  `∑_{T ∈ SYT(μ)} q^{maj T}` of `QOU.Mathlib.MajFormula` specialises at `q = 1` to `#SYT(μ)`.

Pure finite combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.MajSYTBridge

open Finset YoungDiagram Polynomial QOU.Mathlib.MajStandardization QOU.Mathlib.MajFormula

variable {μ : YoungDiagram}

/-- The `1`-indexed entry map of an `SYTe` (junk `0` off the diagram). -/
def entryOf (S : SYTe μ) (i j : ℕ) : ℕ :=
  if h : (i, j) ∈ μ.cells then (S.e ⟨(i, j), h⟩ : ℕ) + 1 else 0

theorem entryOf_mem (S : SYTe μ) {i j : ℕ} (h : (i, j) ∈ μ.cells) :
    entryOf S i j = (S.e ⟨(i, j), h⟩ : ℕ) + 1 := dif_pos h

/-- An `SYTe` as a semistandard tableau (entries shifted to `1, …, |μ|`). -/
def toSsyt (S : SYTe μ) : SemistandardYoungTableau μ where
  entry := entryOf S
  row_weak' := by
    intro i j1 j2 hj hc
    have hc2 : (i, j2) ∈ μ.cells := (mem_cells _).mpr hc
    have hc1 : (i, j1) ∈ μ.cells := (mem_cells _).mpr (μ.up_left_mem le_rfl hj.le hc)
    rw [entryOf_mem S hc1, entryOf_mem S hc2]
    have := Fin.lt_def.mp (S.row_lt ⟨(i, j1), hc1⟩ ⟨(i, j2), hc2⟩ rfl hj)
    omega
  col_strict' := by
    intro i1 i2 j hi hc
    have hc2 : (i2, j) ∈ μ.cells := (mem_cells _).mpr hc
    have hc1 : (i1, j) ∈ μ.cells := (mem_cells _).mpr (μ.up_left_mem hi.le le_rfl hc)
    rw [entryOf_mem S hc1, entryOf_mem S hc2]
    have := Fin.lt_def.mp (S.col_lt ⟨(i1, j), hc1⟩ ⟨(i2, j), hc2⟩ rfl hi)
    omega
  zeros' := by
    intro i j h
    exact dif_neg (fun h' => h ((mem_cells _).mp h'))

/-- An `SYTe` as a standard Young tableau. -/
def toSYT (S : SYTe μ) : StandardYoungTableau μ where
  toSsyt := toSsyt S
  bijOn := by
    refine ⟨?_, ?_, ?_⟩
    · intro c hc
      have hc' : (c.1, c.2) ∈ μ.cells := hc
      show entryOf S c.1 c.2 ∈ Set.Icc 1 μ.cells.card
      rw [entryOf_mem S hc']
      exact ⟨by omega, (S.e ⟨(c.1, c.2), hc'⟩).2⟩
    · intro c hc d hd h
      have hc' : (c.1, c.2) ∈ μ.cells := hc
      have hd' : (d.1, d.2) ∈ μ.cells := hd
      have h' : entryOf S c.1 c.2 = entryOf S d.1 d.2 := h
      rw [entryOf_mem S hc', entryOf_mem S hd'] at h'
      have := S.e.injective (Fin.ext (by omega : (S.e ⟨(c.1, c.2), hc'⟩ : ℕ) = S.e ⟨(d.1, d.2), hd'⟩))
      exact congrArg Subtype.val this
    · intro k hk
      obtain ⟨hk1, hk2⟩ := hk
      let x := S.e.symm ⟨k - 1, by omega⟩
      refine ⟨x.1, x.2, ?_⟩
      show entryOf S x.1.1 x.1.2 = k
      rw [entryOf_mem S x.2]
      have : S.e ⟨(x.1.1, x.1.2), x.2⟩ = ⟨k - 1, by omega⟩ := by
        simp [x]
      rw [this]; simp only; omega

theorem entry_pos (T : StandardYoungTableau μ) (c : Cell μ) : 1 ≤ T.entry c.1.1 c.1.2 :=
  (T.mapsTo_cells (by rw [Finset.mem_coe]; exact c.2)).1

theorem entry_le (T : StandardYoungTableau μ) (c : Cell μ) : T.entry c.1.1 c.1.2 ≤ μ.cells.card :=
  (T.mapsTo_cells (by rw [Finset.mem_coe]; exact c.2)).2

/-- The `0`-indexed cell ordering of a standard tableau, as a function. -/
def eFun (T : StandardYoungTableau μ) (c : Cell μ) : Fin μ.cells.card :=
  ⟨T.entry c.1.1 c.1.2 - 1, by have := entry_pos T c; have := entry_le T c; omega⟩

theorem eFun_bijective (T : StandardYoungTableau μ) : Function.Bijective (eFun T) := by
  constructor
  · intro c d h
    have h' := congrArg Fin.val h
    simp only [eFun] at h'
    have := entry_pos T c; have := entry_pos T d
    have hcd : T.entry c.1.1 c.1.2 = T.entry d.1.1 d.1.2 := by omega
    exact Subtype.ext (T.injOn_cells (by rw [Finset.mem_coe]; exact c.2)
      (by rw [Finset.mem_coe]; exact d.2) hcd)
  · intro k
    obtain ⟨c, hc, hck⟩ := T.bijOn.surjOn (show (k : ℕ) + 1 ∈ Set.Icc 1 μ.cells.card from
      ⟨by omega, k.2⟩)
    refine ⟨⟨c, hc⟩, Fin.ext ?_⟩
    simp only [eFun]
    have hck' : T.entry c.1 c.2 = k + 1 := hck
    rw [hck']; omega

theorem syt_ext {T1 T2 : StandardYoungTableau μ} (h : T1.toSsyt = T2.toSsyt) : T1 = T2 := by
  cases T1; cases T2; cases h; rfl

/-- A standard Young tableau as an `SYTe`. -/
noncomputable def ofSYT (T : StandardYoungTableau μ) : SYTe μ where
  e := Equiv.ofBijective _ (eFun_bijective T)
  row_lt := by
    intro c c' hr hc
    show eFun T c < eFun T c'
    rw [Fin.lt_def]; simp only [eFun]
    have hp := entry_pos T c
    obtain ⟨⟨a, b⟩, ha⟩ := c; obtain ⟨⟨a', b'⟩, ha'⟩ := c'
    simp only at hr hc hp ⊢; subst hr
    have h := T.row_strict hc ((mem_cells _).mp ha')
    omega
  col_lt := by
    intro c c' hcol hr
    show eFun T c < eFun T c'
    rw [Fin.lt_def]; simp only [eFun]
    have hp := entry_pos T c
    obtain ⟨⟨a, b⟩, ha⟩ := c; obtain ⟨⟨a', b'⟩, ha'⟩ := c'
    simp only at hcol hr hp ⊢; subst hcol
    have h : T.toSsyt.entry a b < T.toSsyt.entry a' b := T.toSsyt.col_strict hr ((mem_cells _).mp ha')
    simp only [StandardYoungTableau.entry] at hp ⊢
    omega

/-- **`SYTe μ ≃ StandardYoungTableau μ`** — shift the entries by one. -/
noncomputable def sytEquiv (μ : YoungDiagram) : SYTe μ ≃ StandardYoungTableau μ where
  toFun := toSYT
  invFun := ofSYT
  left_inv S := by
    apply SYTe.ext'
    ext c
    show (eFun (toSYT S) c : ℕ) = S.e c
    simp only [eFun]
    show entryOf S c.1.1 c.1.2 - 1 = S.e c
    rw [entryOf_mem S c.2]
    simp
  right_inv T := by
    have hall : ∀ i j, (toSYT (ofSYT T)).toSsyt.entry i j = T.toSsyt.entry i j := by
      intro i j
      show entryOf (ofSYT T) i j = T.toSsyt.entry i j
      by_cases hij : (i, j) ∈ μ.cells
      · rw [entryOf_mem _ hij]
        show (eFun T ⟨(i, j), hij⟩ : ℕ) + 1 = _
        simp only [eFun]
        have := entry_pos T ⟨(i, j), hij⟩
        dsimp only at this
        show T.entry i j - 1 + 1 = T.toSsyt.entry i j
        simp only [StandardYoungTableau.entry] at this ⊢
        omega
      · rw [entryOf, dif_neg hij]
        exact (T.toSsyt.zeros (fun h => hij ((mem_cells _).mpr h))).symm
    have hssyt : (toSYT (ofSYT T)).toSsyt = T.toSsyt := SemistandardYoungTableau.ext hall
    exact syt_ext hssyt

/-- The number of `SYTe μ` is the corpus's `#SYT(μ)`. -/
theorem card_SYTe (μ : YoungDiagram) :
    Fintype.card (SYTe μ) = numStandardYoungTableaux μ := by
  rw [numStandardYoungTableaux, ← Nat.card_eq_fintype_card]
  exact Nat.card_congr (sytEquiv μ)

/-- **`maj` generating function at `q = 1`:** `∑_{T ∈ SYT(μ)} 1^{maj T} = #SYT(μ)`. -/
theorem fmaj_eval_one (μ : YoungDiagram) :
    (fmaj μ).eval 1 = (numStandardYoungTableaux μ : ℤ) := by
  rw [fmaj, eval_finset_sum]
  simp only [eval_pow, eval_X, one_pow, sum_const, card_univ, nsmul_eq_mul, mul_one]
  rw [card_SYTe]

end QOU.Mathlib.MajSYTBridge
