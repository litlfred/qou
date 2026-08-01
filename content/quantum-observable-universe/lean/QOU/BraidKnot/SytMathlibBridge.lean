import QOU.BraidKnot.SytRowSuperstandard
import QOU.BraidKnot.StandardYoungTableau

/-!
# Bridge `QOU.Mathlib.StandardYoungTableau μ → QOU.BraidKnot.StandardYoungTableau μ`

Two standard-Young-tableau types live in this development:

* `QOU.Mathlib.StandardYoungTableau μ` — a refinement of Mathlib's
  `SemistandardYoungTableau`, whose entry map is a `Set.BijOn` onto `{1, …, |μ|}`
  (entries `1..|μ|`).  The row-superstandard witness `rowSuperstandardStd` and the
  `Nonempty` instance built in `SytRowSuperstandard.lean` are of this type.
* `QOU.BraidKnot.StandardYoungTableau μ` — the bespoke entry-based structure
  (`entry`, `lt_card`, `zero_off`, `inj_on`, `row_strict`, `col_strict`) with
  entries `0..|μ|-1`, used by the Jucys–Murphy / Okounkov–Vershik seminormal
  machinery (`JucysMurphy.lean`: `tableauCellEquiv`, `AdjacentSwapStep`,
  `syt_all_connect_to_some`).

This file is the **one-line-down conversion** `toBraidKnot` between them: shift
every entry down by one (`entry i j - 1`).  Off the diagram Mathlib's SSYT is
pinned to `0` (`zeros'`), and `0 - 1 = 0` in `ℕ`, so `zero_off` holds for free;
on the diagram the `Set.BijOn` bound `1 ≤ entry ≤ |μ|` makes the truncated
subtraction faithful (`omega`).  Consequently the JM/OV code has a concrete
`Nonempty (QOU.BraidKnot.StandardYoungTableau μ)` (`rowSuperstandardBraidKnot`),
supplying the base tableau `T₀` its exchange argument needs.

Scope: pure combinatorics on `ℕ`; §7c-clean (no `ℝ`, no ordering on `q`); no fit.
-/

namespace QOU.BraidKnot

open YoungDiagram

variable {μ : YoungDiagram}

/-- **The one-down conversion** `QOU.Mathlib.StandardYoungTableau μ →
`QOU.BraidKnot.StandardYoungTableau μ`: shift each entry down by one so the range
becomes `0..|μ|-1`.  Off-diagram entries (`= 0` by `zeros'`) stay `0`. -/
noncomputable def _root_.QOU.Mathlib.StandardYoungTableau.toBraidKnot
    (T : QOU.Mathlib.StandardYoungTableau μ) : QOU.BraidKnot.StandardYoungTableau μ where
  entry i j := T.entry i j - 1
  lt_card i j hij := by
    have hmap : T.entry i j ∈ Set.Icc 1 μ.cells.card :=
      T.mapsTo_cells (QOU.Mathlib.StandardYoungTableau.mem_coe_cells hij)
    rw [Set.mem_Icc] at hmap
    show T.entry i j - 1 < μ.cells.card
    omega
  zero_off i j hij := by
    show T.entry i j - 1 = 0
    have h0 : T.entry i j = 0 := T.toSsyt.zeros hij
    rw [h0]
  inj_on i j i' j' hij hij' heq := by
    have h1 : T.entry i j ∈ Set.Icc 1 μ.cells.card :=
      T.mapsTo_cells (QOU.Mathlib.StandardYoungTableau.mem_coe_cells hij)
    have h2 : T.entry i' j' ∈ Set.Icc 1 μ.cells.card :=
      T.mapsTo_cells (QOU.Mathlib.StandardYoungTableau.mem_coe_cells hij')
    rw [Set.mem_Icc] at h1 h2
    have heq' : T.entry i j = T.entry i' j' := by
      show T.entry i j = T.entry i' j'
      omega
    have hcell := T.injOn_cells (QOU.Mathlib.StandardYoungTableau.mem_coe_cells hij)
      (QOU.Mathlib.StandardYoungTableau.mem_coe_cells hij') heq'
    exact ⟨congrArg Prod.fst hcell, congrArg Prod.snd hcell⟩
  row_strict i j hcell := by
    have hij : (i, j) ∈ μ := μ.up_left_mem (le_refl i) (Nat.le_succ j) hcell
    have hlt : T.entry i j < T.entry i (j + 1) := T.row_strict (Nat.lt_succ_self j) hcell
    have hmap : T.entry i j ∈ Set.Icc 1 μ.cells.card :=
      T.mapsTo_cells (QOU.Mathlib.StandardYoungTableau.mem_coe_cells hij)
    rw [Set.mem_Icc] at hmap
    show T.entry i j - 1 < T.entry i (j + 1) - 1
    omega
  col_strict i j hcell := by
    have hij : (i, j) ∈ μ := μ.up_left_mem (Nat.le_succ i) (le_refl j) hcell
    have hlt : T.entry i j < T.entry (i + 1) j := T.toSsyt.col_strict (Nat.lt_succ_self i) hcell
    have hmap : T.entry i j ∈ Set.Icc 1 μ.cells.card :=
      T.mapsTo_cells (QOU.Mathlib.StandardYoungTableau.mem_coe_cells hij)
    rw [Set.mem_Icc] at hmap
    show T.entry i j - 1 < T.entry (i + 1) j - 1
    omega

/-- **The row-superstandard tableau as a `QOU.BraidKnot.StandardYoungTableau`** —
the base tableau `T₀` the Okounkov–Vershik exchange argument
(`syt_all_connect_to_some`) walks every SYT toward, in the exact type that
argument consumes. -/
noncomputable def rowSuperstandardBraidKnot (μ : YoungDiagram) :
    QOU.BraidKnot.StandardYoungTableau μ :=
  (rowSuperstandardStd μ).toBraidKnot

/-- **`QOU.BraidKnot.StandardYoungTableau μ` is nonempty (sorry-free).** Via the
bridge from the row-superstandard Mathlib SYT. -/
instance instNonemptyBraidKnotStandardYoungTableau :
    Nonempty (QOU.BraidKnot.StandardYoungTableau μ) :=
  ⟨rowSuperstandardBraidKnot μ⟩

/-! ### Reverse bridge `BraidKnot → Mathlib` and the card equiv (sp09 part 2)

The custom SYT carries only *consecutive* strictness; the Mathlib SSYT wants
*arbitrary-gap* weak rows / strict columns.  `row_mono`/`col_mono` bridge that. -/

/-- Arbitrary-gap row strictness from the consecutive `row_strict`. -/
theorem row_mono (S : QOU.BraidKnot.StandardYoungTableau μ) (i : ℕ) :
    ∀ {j1 j2 : ℕ}, j1 < j2 → (i, j2) ∈ μ → S.entry i j1 < S.entry i j2 := by
  intro j1 j2
  induction j2 with
  | zero => intro h _; omega
  | succ k ih =>
    intro h hcell
    rcases eq_or_lt_of_le (Nat.lt_succ_iff.mp h) with heq | hlt
    · subst heq; exact S.row_strict i j1 hcell
    · have hk : (i, k) ∈ μ := μ.up_left_mem (le_refl i) (Nat.le_succ k) hcell
      exact lt_trans (ih hlt hk) (S.row_strict i k hcell)

/-- Arbitrary-gap column strictness from the consecutive `col_strict`. -/
theorem col_mono (S : QOU.BraidKnot.StandardYoungTableau μ) (j : ℕ) :
    ∀ {i1 i2 : ℕ}, i1 < i2 → (i2, j) ∈ μ → S.entry i1 j < S.entry i2 j := by
  intro i1 i2
  induction i2 with
  | zero => intro h _; omega
  | succ k ih =>
    intro h hcell
    rcases eq_or_lt_of_le (Nat.lt_succ_iff.mp h) with heq | hlt
    · subst heq; exact S.col_strict i1 j hcell
    · have hk : (k, j) ∈ μ := μ.up_left_mem (Nat.le_succ k) (le_refl j) hcell
      exact lt_trans (ih hlt hk) (S.col_strict k j hcell)

open scoped Classical in
/-- **The one-up conversion** `QOU.BraidKnot.StandardYoungTableau μ →
QOU.Mathlib.StandardYoungTableau μ`: shift each on-cell entry up by one (range
`1..|μ|`), pin off-cell entries to `0`.  Inverse of `toBraidKnot`. -/
noncomputable def _root_.QOU.BraidKnot.StandardYoungTableau.toMathlib
    (S : QOU.BraidKnot.StandardYoungTableau μ) : QOU.Mathlib.StandardYoungTableau μ where
  toSsyt :=
    { entry := fun i j => if (i, j) ∈ μ then S.entry i j + 1 else 0
      row_weak' := by
        intro i j1 j2 hlt hcell
        have hc1 : (i, j1) ∈ μ := μ.up_left_mem (le_refl i) (le_of_lt hlt) hcell
        rw [if_pos hc1, if_pos hcell]
        have := row_mono S i hlt hcell
        omega
      col_strict' := by
        intro i1 i2 j hlt hcell
        have hc1 : (i1, j) ∈ μ := μ.up_left_mem (le_of_lt hlt) (le_refl j) hcell
        rw [if_pos hc1, if_pos hcell]
        have := col_mono S j hlt hcell
        omega
      zeros' := by intro i j hij; rw [if_neg hij] }
  bijOn := by
    classical
    have hmapsTo : Set.MapsTo (fun c : ℕ × ℕ => if (c.1, c.2) ∈ μ then S.entry c.1 c.2 + 1 else 0)
        (μ.cells : Set (ℕ × ℕ)) (Set.Icc 1 μ.cells.card) := by
      intro c hc
      rw [Finset.mem_coe, YoungDiagram.mem_cells] at hc
      simp only [if_pos hc, Set.mem_Icc]
      have hlt := S.lt_card c.1 c.2 hc
      have hcard : μ.card = μ.cells.card := rfl
      omega
    have hinjOn : Set.InjOn (fun c : ℕ × ℕ => if (c.1, c.2) ∈ μ then S.entry c.1 c.2 + 1 else 0)
        (μ.cells : Set (ℕ × ℕ)) := by
      intro a ha b hb hEq
      rw [Finset.mem_coe, YoungDiagram.mem_cells] at ha hb
      simp only [if_pos ha, if_pos hb] at hEq
      have hea : S.entry a.1 a.2 = S.entry b.1 b.2 := by omega
      have := S.inj_on a.1 a.2 b.1 b.2 ha hb hea
      exact Prod.ext this.1 this.2
    refine ⟨hmapsTo, hinjOn, ?_⟩
    -- surjOn from injOn + mapsTo + equal finite card (Finset lemma; coe `Icc`)
    rw [show (Set.Icc 1 μ.cells.card) = (↑(Finset.Icc 1 μ.cells.card) : Set ℕ) from
      (Finset.coe_Icc 1 μ.cells.card).symm]
    refine Finset.surjOn_of_injOn_of_card_le _ ?_ hinjOn ?_
    · rw [Finset.coe_Icc]; exact hmapsTo
    · rw [Nat.card_Icc]; omega

/-- Left inverse `toBraidKnot ∘ toMathlib = id`. -/
theorem toBraidKnot_toMathlib (S : QOU.BraidKnot.StandardYoungTableau μ) :
    (S.toMathlib).toBraidKnot = S := by
  ext i j
  show (if (i, j) ∈ μ then S.entry i j + 1 else 0) - 1 = S.entry i j
  by_cases h : (i, j) ∈ μ
  · rw [if_pos h]; omega
  · rw [if_neg h, S.zero_off i j h]

/-- Mathlib SYT equality reduces to SSYT equality (`bijOn` is a `Prop`). -/
theorem mathlibSYT_ext {T1 T2 : QOU.Mathlib.StandardYoungTableau μ}
    (h : T1.toSsyt = T2.toSsyt) : T1 = T2 := by
  cases T1; cases T2; cases h; rfl

/-- Right inverse `toMathlib ∘ toBraidKnot = id`. -/
theorem toMathlib_toBraidKnot (T : QOU.Mathlib.StandardYoungTableau μ) :
    (T.toBraidKnot).toMathlib = T := by
  apply mathlibSYT_ext
  apply SemistandardYoungTableau.ext
  intro i j
  show (if (i, j) ∈ μ then (T.entry i j - 1) + 1 else 0) = T.toSsyt.entry i j
  by_cases h : (i, j) ∈ μ
  · rw [if_pos h]
    have hmap : T.entry i j ∈ Set.Icc 1 μ.cells.card :=
      T.mapsTo_cells (QOU.Mathlib.StandardYoungTableau.mem_coe_cells h)
    rw [Set.mem_Icc] at hmap
    have h1 : 1 ≤ T.toSsyt.entry i j := hmap.1
    show (T.toSsyt.entry i j - 1) + 1 = T.toSsyt.entry i j
    omega
  · rw [if_neg h]; exact (T.toSsyt.zeros h).symm

/-- **sp09 part 2 — the SYT-count equiv.** `numSYT μ = numStandardYoungTableaux μ`:
the bespoke 0-based SYT count equals the Mathlib-SSYT-based count, via the `±1`
shift bijection `toMathlib`/`toBraidKnot`. -/
theorem numSYT_eq_numStandardYoungTableaux (μ : YoungDiagram) :
    QOU.BraidKnot.numSYT μ = QOU.Mathlib.numStandardYoungTableaux μ :=
  Nat.card_congr
    ⟨QOU.BraidKnot.StandardYoungTableau.toMathlib,
      QOU.Mathlib.StandardYoungTableau.toBraidKnot,
      toBraidKnot_toMathlib, toMathlib_toBraidKnot⟩

end QOU.BraidKnot
