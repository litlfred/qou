import Mathlib.Combinatorics.Young.YoungDiagram

/-!
# ≤ 2 rows and ≤ 2 columns are different families, and nothing in this corpus said so

**Bean `qou-cds1`.** Two halves of the Lean corpus quantify over Temperley–Lieb
survivors in **opposite conventions**, and until this file nothing related them:

| module | survivor condition | in Mathlib terms |
|---|---|---|
| `QOU.QBeta.TemperleyLiebTower`, `QOU.QBeta.TwoRowNormalisation` | at most two **rows** | `μ.colLen 0 ≤ 2` |
| `QOU.MathlibExt.WenzlSchurElement`, `QOU.MassTheory.SelfConjugateStratumVanishes` | at most two **columns** | `μ.rowLen 0 ≤ 2` |

`WenzlSchurElement`'s own docstring warns that *"anyone wiring
`schurElement_tl_eq_zero_iff` to that block must transpose"*. This file supplies
the transposition as theorems, so that warning can be discharged rather than
merely read.

## Why it is a trap and not just a difference

The two families are **equinumerous** — `transposeEquiv` below is an explicit
bijection between them at every fixed size — while being **different sets**
(`atMostTwoRows_iff_atMostTwoCols_false`). At `n = 3`:

| convention | surviving shapes | `Σ dim²` |
|---|---|---|
| ≤ 2 rows | `(3)`, `(2,1)` | `1² + 2² = 5` |
| ≤ 2 columns | `(2,1)`, `(1,1,1)` | `2² + 1² = 5` |

Disjoint but for `(2,1)`, and both sum to `catalan 3 = 5`. So **every count-based
and dimension-based check agrees under either reading**, and a proof transported
from one to the other by matching numbers rather than by transposing is wrong
without ever producing a wrong number. That is the failure mode this file exists
to make impossible: `transposeEquiv` is the *only* honest transport, and it is
not the identity.

## Scope — what is proved here and what is not

**Proved:** the shape-level statements. The transpose is a size-preserving
involution, it carries each family onto the other, and the two families are
genuinely distinct.

**Not proved here:** that the two families have equal *dimension* sums. That
needs `dim λ = dim λ'` (invariance of the standard-tableau count under
conjugation), which this corpus does not have — `QOU.Mathlib.TwoRowDimCatalan`
proves `Σ dim² = catalan n` for the ≤ 2-**row** family only, via
`dimHLF_two_row_eq_ballot`, and there is no ≤ 2-column counterpart. So the
`Σ dim² = 5` column of the table above is arithmetic on hand-computed
dimensions, not a theorem, and it is stated as such. Naming that one missing
lemma is deliberate: it is the whole remaining gap between the two halves of the
corpus, and it is a Mathlib-shaped statement rather than a QOU-shaped one.

-- Ref: [manuscript] rem:hecke-radical-is-temperley-lieb — the block this
-- collision was found in; see also QOU.MathlibExt.WenzlSchurElement.
-/

namespace QOU.MassTheory.TwoRowTwoColumn

open YoungDiagram

/-- **At most two rows** — the convention of `TemperleyLiebTower`,
`TwoRowNormalisation`, and convention D's surviving Wedderburn blocks. The
number of rows of `μ` is the length of its zeroth column. -/
def AtMostTwoRows (μ : YoungDiagram) : Prop := μ.colLen 0 ≤ 2

/-- **At most two columns** — the convention of `WenzlSchurElement` and
`SelfConjugateStratumVanishes`. The number of columns of `μ` is the length of
its zeroth row. -/
def AtMostTwoCols (μ : YoungDiagram) : Prop := μ.rowLen 0 ≤ 2

instance (μ : YoungDiagram) : Decidable (AtMostTwoRows μ) := by
  unfold AtMostTwoRows; infer_instance

instance (μ : YoungDiagram) : Decidable (AtMostTwoCols μ) := by
  unfold AtMostTwoCols; infer_instance

section Bridge

/-- **Transposing sends the row condition to the column condition.**

This is the lemma `WenzlSchurElement`'s docstring asks for. A theorem proved for
`μ.rowLen 0 ≤ 2` applies to a two-row shape only after transposing it — not to
the two-row shape itself. -/
@[simp] theorem atMostTwoCols_transpose (μ : YoungDiagram) :
    AtMostTwoCols μ.transpose ↔ AtMostTwoRows μ := by
  simp [AtMostTwoCols, AtMostTwoRows, YoungDiagram.rowLen_transpose]

/-- **…and back.** The mirror of `atMostTwoCols_transpose`, so transport works in
both directions. -/
@[simp] theorem atMostTwoRows_transpose (μ : YoungDiagram) :
    AtMostTwoRows μ.transpose ↔ AtMostTwoCols μ := by
  simp [AtMostTwoRows, AtMostTwoCols, YoungDiagram.colLen_transpose]

/-- **Transposing preserves the number of cells**, so it is a bijection of
partitions of `n` and not merely of diagrams. Mathlib has `transpose` as an
order isomorphism but records nothing about `card`. -/
@[simp] theorem card_transpose (μ : YoungDiagram) : μ.transpose.card = μ.card := by
  simp [YoungDiagram.card, YoungDiagram.transpose]

end Bridge

section Equinumerous

/-- **The two families are in explicit bijection at every size.**

The map is transposition, and it is the *only* correct transport between the
conventions: it is a bijection, and — by `atMostTwoRows_iff_atMostTwoCols_false`
below — it is not the identity, so a family-level statement does not survive
being read in the other convention just because the counts match. -/
def transposeEquiv (n : ℕ) :
    {μ : YoungDiagram // AtMostTwoRows μ ∧ μ.card = n} ≃
      {μ : YoungDiagram // AtMostTwoCols μ ∧ μ.card = n} where
  toFun x :=
    ⟨x.1.transpose, (atMostTwoCols_transpose x.1).mpr x.2.1,
      (card_transpose x.1).trans x.2.2⟩
  invFun y :=
    ⟨y.1.transpose, (atMostTwoRows_transpose y.1).mpr y.2.1,
      (card_transpose y.1).trans y.2.2⟩
  left_inv x := Subtype.ext (YoungDiagram.transpose_transpose x.1)
  right_inv y := Subtype.ext (YoungDiagram.transpose_transpose y.1)

end Equinumerous

section Distinct

/-! ### …and yet they are different sets

A bijection is not an equality. The witness is the smallest one there is: the
single row `(3)`, which has one row and three columns. -/

/-- The single row `(3)`: three cells, all in row `0`. -/
def row3 : YoungDiagram where
  cells := Finset.range 1 ×ˢ Finset.range 3
  isLowerSet := by
    intro a b hba ha
    simp only [Finset.coe_product, Set.mem_prod, Finset.coe_range,
      Set.mem_Iio] at ha ⊢
    exact ⟨lt_of_le_of_lt hba.1 ha.1, lt_of_le_of_lt hba.2 ha.2⟩

theorem mem_row3 (i j : ℕ) : (i, j) ∈ row3 ↔ i < 1 ∧ j < 3 := by
  simp only [row3, YoungDiagram.mem_mk, Finset.mem_product,
    Finset.mem_range]

theorem row3_rowLen : row3.rowLen 0 = 3 := by
  have hin : ((0 : ℕ), (2 : ℕ)) ∈ row3 := (mem_row3 0 2).mpr ⟨by omega, by omega⟩
  have hout : ((0 : ℕ), (3 : ℕ)) ∉ row3 := by
    intro h; have := (mem_row3 0 3).mp h; omega
  have h1 := YoungDiagram.mem_iff_lt_rowLen.mp hin
  have h2 : ¬ (3 < row3.rowLen 0) := fun h =>
    hout (YoungDiagram.mem_iff_lt_rowLen.mpr h)
  omega

theorem row3_colLen : row3.colLen 0 = 1 := by
  have hin : ((0 : ℕ), (0 : ℕ)) ∈ row3 := (mem_row3 0 0).mpr ⟨by omega, by omega⟩
  have hout : ((1 : ℕ), (0 : ℕ)) ∉ row3 := by
    intro h; have := (mem_row3 1 0).mp h; omega
  have h1 := YoungDiagram.mem_iff_lt_colLen.mp hin
  have h2 : ¬ (1 < row3.colLen 0) := fun h =>
    hout (YoungDiagram.mem_iff_lt_colLen.mpr h)
  omega

theorem row3_card : row3.card = 3 := by simp [YoungDiagram.card, row3]

theorem row3_atMostTwoRows : AtMostTwoRows row3 := by
  simp [AtMostTwoRows, row3_colLen]

theorem row3_not_atMostTwoCols : ¬ AtMostTwoCols row3 := by
  simp [AtMostTwoCols, row3_rowLen]

/-- **The two conditions are not equivalent.**

Stated as the refutation of the universally quantified biconditional, because
that is the claim an agent transporting a theorem between the two halves of the
corpus is implicitly making. It is false, and `row3` is why. -/
theorem atMostTwoRows_iff_atMostTwoCols_false :
    ¬ (∀ μ : YoungDiagram, AtMostTwoRows μ ↔ AtMostTwoCols μ) := fun h =>
  row3_not_atMostTwoCols ((h row3).mp row3_atMostTwoRows)

/-- **The transposed witness**, `(1,1,1)`: at most two columns, more than two
rows. So neither family contains the other — the failure is symmetric, not an
artefact of which side the witness was built on. -/
theorem exists_atMostTwoCols_not_atMostTwoRows :
    ∃ μ : YoungDiagram, AtMostTwoCols μ ∧ ¬ AtMostTwoRows μ ∧ μ.card = 3 :=
  ⟨row3.transpose,
    (atMostTwoCols_transpose row3).mpr row3_atMostTwoRows,
    fun h => row3_not_atMostTwoCols ((atMostTwoRows_transpose row3).mp h),
    (card_transpose row3).trans row3_card⟩

/-- **Both facts in one statement**, at the smallest size where they differ:
there is a shape in each family that the other misses, and both have three
cells — so a size-graded argument cannot separate them either. -/
theorem families_differ_at_three :
    (∃ μ : YoungDiagram, AtMostTwoRows μ ∧ ¬ AtMostTwoCols μ ∧ μ.card = 3) ∧
    (∃ μ : YoungDiagram, AtMostTwoCols μ ∧ ¬ AtMostTwoRows μ ∧ μ.card = 3) :=
  ⟨⟨row3, row3_atMostTwoRows, row3_not_atMostTwoCols, row3_card⟩,
    exists_atMostTwoCols_not_atMostTwoRows⟩

end Distinct

end QOU.MassTheory.TwoRowTwoColumn
