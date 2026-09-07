import Mathlib.Combinatorics.Young.YoungDiagram
import QOU.Mathlib.TwoRowDimCatalan

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

**Proved at `n = 3, 4, 5, 6` only:** that the two families have equal
*dimension* sums, and that the transposed pairs have equal dimension
(`dim_eq_dim_transpose_three_to_six`, `sq_sum_agree_three`, `sq_sum_agree_six`).
Every value there is computed by `decide` from `dimHLF`'s definition, so the
`Σ dim² = 5` column above is a theorem at that size rather than hand arithmetic.

**Not proved at general `n`:** `dim λ = dim λ'` — invariance of the
standard-tableau count under conjugation. `QOU.Mathlib.TwoRowDimCatalan` proves
`Σ dim² = catalan n` for the ≤ 2-**row** family at every `n`, via
`dimHLF_two_row_eq_ballot`; there is no ≤ 2-column counterpart, so the column
family's total is known only at the sizes decided above. Naming that one lemma is
deliberate: it is the entire remaining gap between the two halves of the corpus,
and it is a Mathlib-shaped statement rather than a QOU-shaped one.

The route is not mysterious, and is recorded so the next attempt does not start
cold. Both hook products factor into the *same three* products. For the two-row
shape `(a, b)` with `a = k + m`, `b = k`, and its transpose `2^k 1^m`:

    two-row:     ∏_{j<b}(a−j+1) · ∏_{b≤j<a}(a−j) · ∏_{j<b}(b−j)
    two-column:  ∏_{i<k}(k+m−i+1) · ∏_{k≤i<k+m}(k+m−i) · ∏_{i<k}(k−i)

which are termwise identical under `a = k+m`, `b = k`. So `prodHooks` agrees and
therefore so does `n!/prodHooks` — no factorial manipulation is needed, only the
`colLen` evaluation on `List.replicate k 2 ++ List.replicate m 1` and a
`List.range` split. Tracked as a bean; not attempted here.

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

section Dimensions

/-! ## The dimension half — and it lives in a *different encoding*

Everything above is about `YoungDiagram`. The corpus's standard-tableau count,
`QOU.BraidKnot.IdentityI.dimHLF` (Frame–Robinson–Thrall, `n!/∏ h_c`), is about
`List ℕ`. That is a third encoding alongside `Nat.Partition`, and the gap between
them is part of why the two conventions were never related: the transpose is
cheap on `YoungDiagram` (Mathlib has it) and the dimensions are cheap on
`List ℕ` (this corpus has them), and no file held both.

What follows is the dimension side, on lists, at the sizes where the trap
actually bites — `n = 3` is `A = 1` in the mass channel, which indexes at
`n = 3A`. Every value is **computed by `decide`** from `dimHLF`'s definition, not
quoted from a table: a transcription slip cannot survive.

These are finite decidable checks, not the general theorem. The general theorem
is `dimHLF λ = dimHLF λ'`, and it is **not proved anywhere in this corpus** — see
the file header. What these establish is that the trap is real at the sizes in
use, which is what a reader needs before wiring anything.
-/

open QOU.BraidKnot.IdentityI (dimHLF)

/-- **Transposed shapes have equal dimension at `n = 3, 4, 5, 6`.**

Left column: the ≤ 2-row shapes. Right column: their transposes, which are
exactly the ≤ 2-column shapes. Each pair is one instance of the unproved general
`dim λ = dim λ'`.

Note `(2,1)` at `n = 3` and `(2,2)` at `n = 4` are **self**-conjugate — they lie in
*both* families. That is why the two shape sets overlap rather than being
disjoint, and it is what makes the collision hard to notice by inspection. -/
theorem dim_eq_dim_transpose_three_to_six :
    (dimHLF [3] = dimHLF [1, 1, 1] ∧ dimHLF [2, 1] = dimHLF [2, 1]) ∧
    (dimHLF [4] = dimHLF [1, 1, 1, 1] ∧ dimHLF [3, 1] = dimHLF [2, 1, 1] ∧
      dimHLF [2, 2] = dimHLF [2, 2]) ∧
    (dimHLF [5] = dimHLF [1, 1, 1, 1, 1] ∧ dimHLF [4, 1] = dimHLF [2, 1, 1, 1] ∧
      dimHLF [3, 2] = dimHLF [2, 2, 1]) ∧
    (dimHLF [6] = dimHLF [1, 1, 1, 1, 1, 1] ∧ dimHLF [5, 1] = dimHLF [2, 1, 1, 1, 1] ∧
      dimHLF [4, 2] = dimHLF [2, 2, 1, 1] ∧ dimHLF [3, 3] = dimHLF [2, 2, 2]) := by
  decide

/-- **Both readings give `catalan n`, over different shape sets** — `n = 3`.

`catalan 3 = 5` is Mathlib's `catalan_three`; the two sums are computed. The
row family is `{(3), (2,1)}` and the column family `{(2,1), (1,1,1)}`: they share
only `(2,1)`, and both total `5`. A check that compares totals therefore passes
under either reading, which is the whole trap. -/
theorem sq_sum_agree_three :
    dimHLF [3] ^ 2 + dimHLF [2, 1] ^ 2 = catalan 3 ∧
    dimHLF [2, 1] ^ 2 + dimHLF [1, 1, 1] ^ 2 = catalan 3 := by
  rw [catalan_three]
  exact ⟨by decide, by decide⟩

/-- The same at `n = 6`, i.e. `A = 2` in the mass channel: both total
`catalan 6 = 132` over shape sets sharing **nothing at all** — at even `n` the
self-conjugate shape can be absent, and here the two families are disjoint.
Totals still agree. -/
theorem sq_sum_agree_six :
    dimHLF [6] ^ 2 + dimHLF [5, 1] ^ 2 + dimHLF [4, 2] ^ 2 + dimHLF [3, 3] ^ 2
        = catalan 6 ∧
    dimHLF [1, 1, 1, 1, 1, 1] ^ 2 + dimHLF [2, 1, 1, 1, 1] ^ 2
        + dimHLF [2, 2, 1, 1] ^ 2 + dimHLF [2, 2, 2] ^ 2 = catalan 6 := by
  have hc : catalan 6 = 132 := by
    norm_num [catalan_eq_centralBinom_div, Nat.centralBinom, Nat.choose, Nat.factorial]
  rw [hc]
  exact ⟨by decide, by decide⟩

/-- **The shape sets are different**, as lists, at `n = 3` and `n = 6`.

Trivial to check and worth stating next to the equal totals: it is the
conjunction of "different sets" with "same total" that is dangerous, and a
theorem asserting only one half of it invites the reader to supply the wrong
other half. -/
theorem shape_sets_differ :
    ([[3], [2, 1]] : List (List ℕ)) ≠ [[2, 1], [1, 1, 1]] ∧
    ([[6], [5, 1], [4, 2], [3, 3]] : List (List ℕ))
      ≠ [[1, 1, 1, 1, 1, 1], [2, 1, 1, 1, 1], [2, 2, 1, 1], [2, 2, 2]] := by
  exact ⟨by decide, by decide⟩

end Dimensions

end QOU.MassTheory.TwoRowTwoColumn
