import QOU.BraidKnot.StandardYoungTableau
import QOU.Mathlib.StandardYoungTableau
import QOU.Mathlib.SYTEnumerationFintype

/-!
# QOU.BraidKnot.NumSYTBridge — encoding bridge `numSYT = numSYTenum ∘ rowLens`

The Frame–Robinson–Thrall wiring (`numSYT_mul_hookProduct`) and the Burnside identity
(`DeltaLambdaSignRule.burnside`) both need the repo's two **standard-Young-tableau counts** to agree:

* `QOU.BraidKnot.numSYT μ = Nat.card (QOU.BraidKnot.StandardYoungTableau μ)` — the 0-indexed
  tableau type (`entry : ℕ → ℕ → ℕ`, `lt_card`/`zero_off`/`inj_on`/`row_strict`/`col_strict`);
* `QOU.Mathlib.numStandardYoungTableaux μ = Nat.card (QOU.Mathlib.StandardYoungTableau μ)` — the
  SSYT-wrapper type (a `SemistandardYoungTableau` whose entry map bijects the cells onto
  `Set.Icc 1 μ.cells.card`, i.e. 1-indexed).

These are **different structures**; this file builds the explicit equivalence between them (an
index shift by `1` on the cells, wrapping/unwrapping the semistandard tableau) and derives the
count equality `numSYT μ = numStandardYoungTableaux μ`.  Combined with the already-proved list
bridge `QOU.Mathlib.SYTEnum.numSYTenum_eq_numStandardYoungTableaux` and the round-trip
`YoungDiagram.ofRowLens_to_rowLens_eq_self`, this yields

    numSYT μ = numSYTenum μ.rowLens                        (`numSYT_eq_numSYTenum_rowLens`)

— the encoding needed to feed the GNW hook-walk `numSYTenum_mul_prodHooks` into
`numSYT_mul_hookProduct`.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.  Verified standalone via `lean`-direct
against the pinned v4.24.0 oleans; it carries no `sorry`.

## References
- [sagan2001] Sagan, *The Symmetric Group*, §3.1 (standard Young tableaux; the 0/1-indexing is a
  cosmetic normalisation of the same filling).
-/

open Classical

namespace QOU.BraidKnot

variable {μ : YoungDiagram}

/-! ## General strictness for the BraidKnot tableau (chaining the adjacent field axioms) -/

/-- Auxiliary: chain the adjacent `row_strict` over a gap `d`. -/
theorem StandardYoungTableau.row_lt_aux (T : StandardYoungTableau μ) (i j1 : ℕ) :
    ∀ d, (i, j1 + d + 1) ∈ μ → T.entry i j1 < T.entry i (j1 + d + 1) := by
  intro d
  induction d with
  | zero => intro h; simpa using T.row_strict i j1 (by simpa using h)
  | succ k ih =>
    intro h
    have hmid : (i, j1 + k + 1) ∈ μ := μ.up_left_mem (le_refl i) (by omega) h
    have step2 : T.entry i (j1 + k + 1) < T.entry i (j1 + (k + 1) + 1) :=
      T.row_strict i (j1 + k + 1) h
    exact lt_trans (ih hmid) step2

/-- **General row strictness**: `T.entry i j1 < T.entry i j2` for `j1 < j2` (cell `(i, j2)`). -/
theorem StandardYoungTableau.row_lt (T : StandardYoungTableau μ) {i j1 j2 : ℕ}
    (hcell : (i, j2) ∈ μ) (hlt : j1 < j2) : T.entry i j1 < T.entry i j2 := by
  obtain ⟨d, rfl⟩ : ∃ d, j2 = j1 + d + 1 := ⟨j2 - j1 - 1, by omega⟩
  exact T.row_lt_aux i j1 d hcell

/-- Auxiliary: chain the adjacent `col_strict` over a gap `d`. -/
theorem StandardYoungTableau.col_lt_aux (T : StandardYoungTableau μ) (i1 j : ℕ) :
    ∀ d, (i1 + d + 1, j) ∈ μ → T.entry i1 j < T.entry (i1 + d + 1) j := by
  intro d
  induction d with
  | zero => intro h; simpa using T.col_strict i1 j (by simpa using h)
  | succ k ih =>
    intro h
    have hmid : (i1 + k + 1, j) ∈ μ := μ.up_left_mem (by omega) (le_refl j) h
    have step2 : T.entry (i1 + k + 1) j < T.entry (i1 + (k + 1) + 1) j :=
      T.col_strict (i1 + k + 1) j h
    exact lt_trans (ih hmid) step2

/-- **General column strictness**: `T.entry i1 j < T.entry i2 j` for `i1 < i2` (cell `(i2, j)`). -/
theorem StandardYoungTableau.col_lt (T : StandardYoungTableau μ) {i1 i2 j : ℕ}
    (hcell : (i2, j) ∈ μ) (hlt : i1 < i2) : T.entry i1 j < T.entry i2 j := by
  obtain ⟨d, rfl⟩ : ∃ d, i2 = i1 + d + 1 := ⟨i2 - i1 - 1, by omega⟩
  exact T.col_lt_aux i1 j d hcell

/-! ## Entry bounds on the Mathlib (1-indexed) tableau -/

/-- On a cell, a Mathlib standard tableau's entry lies in `[1, |μ|]`. -/
theorem mathlibEntry_bounds (S : QOU.Mathlib.StandardYoungTableau μ) {i j : ℕ} (h : (i, j) ∈ μ) :
    1 ≤ S.entry i j ∧ S.entry i j ≤ μ.cells.card := by
  have hmt := S.mapsTo_cells (QOU.Mathlib.StandardYoungTableau.mem_coe_cells h)
  rwa [Set.mem_Icc] at hmt

/-! ## The two directions of the equivalence -/

/-- **Forward map** (BraidKnot 0-indexed ⟶ Mathlib 1-indexed): shift entries up by `1` on cells. -/
noncomputable def toMathlibSYT (T : StandardYoungTableau μ) : QOU.Mathlib.StandardYoungTableau μ where
  toSsyt :=
    { entry := fun i j => if (i, j) ∈ μ then T.entry i j + 1 else 0
      row_weak' := by
        intro i j1 j2 hlt hcell
        have hc1 : (i, j1) ∈ μ := μ.up_left_mem (le_refl i) (le_of_lt hlt) hcell
        rw [if_pos hc1, if_pos hcell]
        have := T.row_lt hcell hlt
        omega
      col_strict' := by
        intro i1 i2 j hlt hcell
        have hc1 : (i1, j) ∈ μ := μ.up_left_mem (le_of_lt hlt) (le_refl j) hcell
        rw [if_pos hc1, if_pos hcell]
        have := T.col_lt hcell hlt
        omega
      zeros' := by intro i j h; rw [if_neg h] }
  bijOn := by
    have hcard : μ.card = μ.cells.card := rfl
    set f : ℕ × ℕ → ℕ := fun c => if (c.1, c.2) ∈ μ then T.entry c.1 c.2 + 1 else 0 with hf
    have hmaps : Set.MapsTo f (μ.cells : Set (ℕ × ℕ)) (Set.Icc 1 μ.cells.card) := by
      intro c hc
      rw [Finset.mem_coe, YoungDiagram.mem_cells] at hc
      rw [Set.mem_Icc, hf]
      simp only [if_pos hc]
      have := T.lt_card c.1 c.2 hc
      rw [hcard] at this
      omega
    have hinj : Set.InjOn f (μ.cells : Set (ℕ × ℕ)) := by
      intro c1 hc1 c2 hc2 heq
      rw [Finset.mem_coe, YoungDiagram.mem_cells] at hc1 hc2
      rw [hf] at heq
      simp only [if_pos hc1, if_pos hc2] at heq
      have he : T.entry c1.1 c1.2 = T.entry c2.1 c2.2 := by omega
      obtain ⟨h1, h2⟩ := T.inj_on c1.1 c1.2 c2.1 c2.2 hc1 hc2 he
      exact Prod.ext h1 h2
    have hsurj : Set.SurjOn f (μ.cells : Set (ℕ × ℕ)) (Set.Icc 1 μ.cells.card) := by
      rw [show (Set.Icc 1 μ.cells.card) = (↑(Finset.Icc 1 μ.cells.card) : Set ℕ) by
        simp [Finset.coe_Icc]]
      intro b hb
      simp only [Finset.coe_Icc, Set.mem_Icc] at hb
      have hmaps' : ∀ c ∈ μ.cells, f c ∈ Finset.Icc 1 μ.cells.card := by
        intro c hc
        have := hmaps (by rw [Finset.mem_coe]; exact hc)
        rw [Set.mem_Icc] at this
        simp only [Finset.mem_Icc]; exact this
      have hinj' : ∀ c1 ∈ μ.cells, ∀ c2 ∈ μ.cells, f c1 = f c2 → c1 = c2 := by
        intro c1 hc1 c2 hc2 heq
        exact hinj (by rw [Finset.mem_coe]; exact hc1) (by rw [Finset.mem_coe]; exact hc2) heq
      have hcardle : (Finset.Icc 1 μ.cells.card).card ≤ μ.cells.card := by rw [Nat.card_Icc]; omega
      have := Finset.surj_on_of_inj_on_of_card_le (s := μ.cells)
        (t := Finset.Icc 1 μ.cells.card) (fun c _ => f c) (fun c hc => hmaps' c hc)
        (fun c1 c2 h1 h2 he => hinj' c1 h1 c2 h2 he) hcardle b (by
          simp only [Finset.mem_Icc]; exact hb)
      obtain ⟨c, hc, hce⟩ := this
      exact ⟨c, by rw [Finset.mem_coe]; exact hc, hce.symm⟩
    exact ⟨hmaps, hinj, hsurj⟩

/-- **Backward map** (Mathlib 1-indexed ⟶ BraidKnot 0-indexed): shift entries down by `1` on cells. -/
noncomputable def toBraidKnotSYT (S : QOU.Mathlib.StandardYoungTableau μ) : StandardYoungTableau μ where
  entry := fun i j => if (i, j) ∈ μ then S.entry i j - 1 else 0
  lt_card := by
    intro i j h
    rw [if_pos h]
    obtain ⟨h1, h2⟩ := mathlibEntry_bounds S h
    show S.entry i j - 1 < μ.cells.card
    omega
  zero_off := by intro i j h; rw [if_neg h]
  inj_on := by
    intro i j i' j' hc hc' heq
    rw [if_pos hc, if_pos hc'] at heq
    obtain ⟨h1, _⟩ := mathlibEntry_bounds S hc
    obtain ⟨h1', _⟩ := mathlibEntry_bounds S hc'
    have he : S.entry i j = S.entry i' j' := by omega
    have := S.injOn_cells (QOU.Mathlib.StandardYoungTableau.mem_coe_cells hc)
      (QOU.Mathlib.StandardYoungTableau.mem_coe_cells hc') he
    exact ⟨congrArg Prod.fst this, congrArg Prod.snd this⟩
  row_strict := by
    intro i j hcell
    have hc0 : (i, j) ∈ μ := μ.up_left_mem (le_refl i) (by omega) hcell
    rw [if_pos hc0, if_pos hcell]
    have hlt : S.entry i j < S.entry i (j + 1) := S.row_strict (by omega) hcell
    obtain ⟨h1, _⟩ := mathlibEntry_bounds S hc0
    obtain ⟨h1', _⟩ := mathlibEntry_bounds S hcell
    omega
  col_strict := by
    intro i j hcell
    have hc0 : (i, j) ∈ μ := μ.up_left_mem (by omega) (le_refl j) hcell
    rw [if_pos hc0, if_pos hcell]
    have hlt : S.entry i j < S.entry (i + 1) j := S.toSsyt.col_strict' (by omega) hcell
    obtain ⟨h1, _⟩ := mathlibEntry_bounds S hc0
    obtain ⟨h1', _⟩ := mathlibEntry_bounds S hcell
    omega

/-- **The SYT-type equivalence** `BraidKnot.StandardYoungTableau μ ≃ Mathlib.StandardYoungTableau μ`
(index shift by `1` on the cells; wrap/unwrap the semistandard tableau). -/
noncomputable def sytEquiv (μ : YoungDiagram) :
    StandardYoungTableau μ ≃ QOU.Mathlib.StandardYoungTableau μ where
  toFun := toMathlibSYT
  invFun := toBraidKnotSYT
  left_inv T := by
    ext i j
    simp only [toBraidKnotSYT, toMathlibSYT, QOU.Mathlib.StandardYoungTableau.entry]
    by_cases h : (i, j) ∈ μ
    · rw [if_pos h, if_pos h]; omega
    · rw [if_neg h]; exact (T.zero_off i j h).symm
  right_inv S := by
    apply QOU.Mathlib.SYTEnum.StandardYoungTableau.ext_toSsyt
    apply SemistandardYoungTableau.ext
    intro i j
    show (if (i, j) ∈ μ then (if (i, j) ∈ μ then S.toSsyt.entry i j - 1 else 0) + 1 else 0)
        = S.toSsyt.entry i j
    by_cases h : (i, j) ∈ μ
    · rw [if_pos h, if_pos h]
      have h1 : 1 ≤ S.toSsyt.entry i j := (mathlibEntry_bounds S h).1
      omega
    · rw [if_neg h]
      exact (S.toSsyt.zeros' h).symm

/-! ## The count equalities -/

/-- **Bridge (count).** The two standard-tableau counts agree: `numSYT μ = numStandardYoungTableaux μ`. -/
theorem numSYT_eq_numStandardYoungTableaux (μ : YoungDiagram) :
    numSYT μ = QOU.Mathlib.numStandardYoungTableaux μ := by
  unfold numSYT QOU.Mathlib.numStandardYoungTableaux
  exact Nat.card_congr (sytEquiv μ)

/-- **The encoding bridge (bean qou-v986).** `numSYT μ = numSYTenum μ.rowLens`. Composes the count
equality above with the already-proved list bridge `numSYTenum_eq_numStandardYoungTableaux` and the
round-trip `ofRowLens_to_rowLens_eq_self`. -/
theorem numSYT_eq_numSYTenum_rowLens (μ : YoungDiagram) :
    numSYT μ = QOU.Mathlib.SYTEnum.numSYTenum μ.rowLens := by
  have h1 : numSYT μ = QOU.Mathlib.numStandardYoungTableaux μ :=
    numSYT_eq_numStandardYoungTableaux μ
  have h2 := QOU.Mathlib.SYTEnum.numSYTenum_eq_numStandardYoungTableaux μ.rowLens μ.rowLens_sorted
  rw [YoungDiagram.ofRowLens_to_rowLens_eq_self] at h2
  rw [h1, ← h2]

end QOU.BraidKnot
