import Mathlib.Combinatorics.Young.YoungDiagram
import QOU.Mathlib.TwoRowDimCatalan
import Mathlib.Algebra.BigOperators.Intervals

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

**Proved, at general `n`:** the dimension half as well. `dimHLF_two_col_eq_two_row`
gives `dim λ' = dim λ` for exactly this family — the two-column shape
`2^k 1^{n−2k}` has the same Frame–Robinson–Thrall dimension as the two-row shape
`(n−k, k)` it transposes to — and `dimHLF_two_col_sq_sum` carries
`Σ dim² = catalan n` across to the column family, which
`QOU.Mathlib.TwoRowDimCatalan` had only for the row family.

So the `Σ dim² = 5` column of the table above is a theorem, at every `n`, not
hand arithmetic. The proof needs **no factorials**: both hook products factor
into the *same three* products, termwise. For `(a, b)` with `a = k+m`, `b = k`,
against its transpose `2^k 1^m`,

    two-row:     ∏_{j<b}(a−j+1) · ∏_{b≤j<a}(a−j) · ∏_{j<b}(b−j)
    two-column:  ∏_{i<k}(k+m−i+1) · ∏_{k≤i<k+m}(k+m−i) · ∏_{i<k}(k−i)

are the same three factors in a different association, so `prodHooks` agrees on
the nose and `n!/prodHooks` follows. That is why this is ~120 lines rather than a
hook-length development.

**Still not proved:** `dim λ = dim λ'` for a *general* partition. Nothing here
touches shapes with three or more rows and three or more columns; the argument
above is specific to this family and does not generalise as written. That is a
Mathlib-shaped statement and remains open — but it is no longer what stands
between the two halves of this corpus.

-- Ref: [leitner2026] rem:hecke-radical-is-temperley-lieb — the block this
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
cheap on `YoungDiagram` (Mathlib has it), the dimensions are cheap on `List ℕ`
(this corpus has them), and no file held both.
-/

open QOU.BraidKnot.IdentityI (dimHLF prodHooks sz)

/-! `colLen` is deliberately **not** opened. `YoungDiagram.colLen` and
`QOU.BraidKnot.IdentityI.colLen` are both in scope in this file and Lean reports
the bare name as ambiguous — the encoding straddle described above, biting inside
the file that documents it. Written out in full below rather than disambiguated by
an alias, so the reader can see which of the two is meant at every use. -/

/-- The two-column shape `2^k 1^m`: `k` rows of two cells, then `m` rows of one.
It is the transpose of the two-row shape `(k+m, k)`. -/
def twoCol (k m : ℕ) : List ℕ := List.replicate k 2 ++ List.replicate m 1

@[simp] theorem twoCol_length (k m : ℕ) : (twoCol k m).length = k + m := by
  simp [twoCol]

/-- Column `0` of `2^k 1^m` meets every row. -/
theorem twoCol_colLen_zero (k m : ℕ) : QOU.BraidKnot.IdentityI.colLen (twoCol k m) 0 = k + m := by
  simp [QOU.BraidKnot.IdentityI.colLen, twoCol]

/-- Column `1` meets only the rows of length two. -/
theorem twoCol_colLen_one (k m : ℕ) : QOU.BraidKnot.IdentityI.colLen (twoCol k m) 1 = k := by
  simp [QOU.BraidKnot.IdentityI.colLen, twoCol]

theorem twoCol_getD_lt (k m i : ℕ) (h : i < k) : (twoCol k m).getD i 0 = 2 := by
  have hlen : i < (List.replicate k (2 : ℕ)).length := by simpa using h
  rw [twoCol, List.getD_eq_getElem?_getD, List.getElem?_append_left hlen,
    List.getElem?_replicate]
  simp [h]

theorem twoCol_getD_ge (k m i : ℕ) (h1 : k ≤ i) (h2 : i < k + m) :
    (twoCol k m).getD i 0 = 1 := by
  have hlen : (List.replicate k (2 : ℕ)).length ≤ i := by simpa using h1
  rw [twoCol, List.getD_eq_getElem?_getD, List.getElem?_append_right hlen,
    List.length_replicate, List.getElem?_replicate]
  have : i - k < m := by omega
  simp [this]

/-- Column lengths of the two-row shape `(a, b)`: column `j` meets row `0` when
`j < a` and row `1` when `j < b`. Unconditional — `b ≤ a` is not needed. -/
theorem twoRow_colLen (a b j : ℕ) :
    QOU.BraidKnot.IdentityI.colLen [a, b] j = (if j < a then 1 else 0) + (if j < b then 1 else 0) := by
  by_cases h1 : j < a <;> by_cases h2 : j < b <;> simp [QOU.BraidKnot.IdentityI.colLen, h1, h2]

/-- `prodHooks` as a `Finset` product. Definitionally the same object; the
`Finset` form is what the interval-splitting API works on. -/
theorem prodHooks_eq (l : List ℕ) :
    prodHooks l = ∏ i ∈ Finset.range l.length,
      (∏ j ∈ Finset.range (l.getD i 0), ((l.getD i 0 - j) + (QOU.BraidKnot.IdentityI.colLen l j - i) - 1)) := rfl

/-- **The hook product of the two-column shape**, split at the row where the
rows of length two run out. -/
theorem prodHooks_twoCol (k m : ℕ) :
    prodHooks (twoCol k m)
      = ((∏ i ∈ Finset.range k, (k + m - i + 1)) * ∏ i ∈ Finset.range k, (k - i))
        * ∏ i ∈ Finset.Ico k (k + m), (k + m - i) := by
  rw [prodHooks_eq, twoCol_length,
    ← Finset.prod_range_mul_prod_Ico _ (Nat.le_add_right k m)]
  congr 1
  · rw [← Finset.prod_mul_distrib]
    refine Finset.prod_congr rfl fun i hi => ?_
    have hik : i < k := Finset.mem_range.mp hi
    rw [twoCol_getD_lt k m i hik, show (2 : ℕ) = 1 + 1 from rfl,
      Finset.prod_range_succ, Finset.prod_range_one,
      twoCol_colLen_zero, twoCol_colLen_one]
    congr 1 <;> omega
  · refine Finset.prod_congr rfl fun i hi => ?_
    obtain ⟨h1, h2⟩ := Finset.mem_Ico.mp hi
    rw [twoCol_getD_ge k m i h1 h2, Finset.prod_range_one, twoCol_colLen_zero]
    omega

/-- **The hook product of the two-row shape**, split at the column where the
second row runs out. -/
theorem prodHooks_twoRow (a b : ℕ) (hab : b ≤ a) :
    prodHooks [a, b]
      = ((∏ j ∈ Finset.range b, (a - j + 1)) * ∏ j ∈ Finset.Ico b a, (a - j))
        * ∏ j ∈ Finset.range b, (b - j) := by
  rw [prodHooks_eq, show ([a, b] : List ℕ).length = 2 from rfl,
    show (2 : ℕ) = 1 + 1 from rfl, Finset.prod_range_succ, Finset.prod_range_one,
    show ([a, b] : List ℕ).getD 0 0 = a from rfl,
    show ([a, b] : List ℕ).getD 1 0 = b from rfl]
  congr 1
  · rw [← Finset.prod_range_mul_prod_Ico _ hab]
    congr 1
    · refine Finset.prod_congr rfl fun j hj => ?_
      have hjb : j < b := Finset.mem_range.mp hj
      rw [twoRow_colLen a b j]
      simp only [if_pos (lt_of_lt_of_le hjb hab), if_pos hjb]
      omega
    · refine Finset.prod_congr rfl fun j hj => ?_
      obtain ⟨hbj, hja⟩ := Finset.mem_Ico.mp hj
      rw [twoRow_colLen a b j]
      simp only [if_pos hja, if_neg (by omega : ¬ j < b)]
      omega
  · refine Finset.prod_congr rfl fun j hj => ?_
    have hjb : j < b := Finset.mem_range.mp hj
    rw [twoRow_colLen a b j]
    simp only [if_pos (lt_of_lt_of_le hjb hab), if_pos hjb]
    omega

/-- **The two hook products are equal.**

Not by a factorial computation on each side — the three factors of
`prodHooks_twoCol` and `prodHooks_twoRow` are *termwise the same*, under
`a = k+m`, `b = k`. Only the association differs, so `ring` closes it. This is
the whole reason the general statement is cheap. -/
theorem prodHooks_twoCol_eq_twoRow (k m : ℕ) :
    prodHooks (twoCol k m) = prodHooks [k + m, k] := by
  rw [prodHooks_twoCol, prodHooks_twoRow (k + m) k (Nat.le_add_right k m)]
  ring

theorem sz_twoCol (k m : ℕ) : sz (twoCol k m) = sz [k + m, k] := by
  simp [sz, twoCol, List.sum_append]
  omega

/-- **`dim (2^k 1^m) = dim (k+m, k)`** — the transposed shapes have equal
Frame–Robinson–Thrall dimension. -/
theorem dimHLF_twoCol (k m : ℕ) : dimHLF (twoCol k m) = dimHLF [k + m, k] := by
  unfold dimHLF
  rw [prodHooks_twoCol_eq_twoRow, sz_twoCol]

/-- **`dim λ' = dim λ` for the two-row/two-column family, at every `n`.**

This is the lemma the row half and the column half of the corpus needed in order
to be about each other. `QOU.MathlibExt.WenzlSchurElement` and
`QOU.MassTheory.SelfConjugateStratumVanishes` stratify by `μ.rowLen 0 ≤ 2` (at
most two columns); `QOU.QBeta.TemperleyLiebTower` and
`QOU.QBeta.TwoRowNormalisation` stratify by two rows. Combined with
`transposeEquiv` above — which matches the *shapes* — this matches the
*dimensions*, so a statement in either convention now transports.

It is **not** the general `dim λ = dim λ'`: nothing here touches shapes with
three or more rows *and* three or more columns. -/
theorem dimHLF_two_col_eq_two_row (n k : ℕ) (hk : 2 * k ≤ n) :
    dimHLF (List.replicate k 2 ++ List.replicate (n - 2 * k) 1) = dimHLF [n - k, k] := by
  have h : k + (n - 2 * k) = n - k := by omega
  have hd := dimHLF_twoCol k (n - 2 * k)
  rw [twoCol] at hd
  rw [hd, h]

/-- **`Σ dim² = catalan n` over the ≤ 2-COLUMN family, at every `n`.**

`QOU.Mathlib.TwoRowDimCatalan.dimHLF_two_row_sq_sum` had this for the ≤ 2-row
family only. The two families are different sets (`shape_sets_differ`) and this
says their squared-dimension totals agree at every `n`, not just where they were
decided — so the dimension check provably cannot separate the conventions, at
any size. That is the trap stated as a theorem instead of as a warning. -/
theorem dimHLF_two_col_sq_sum (n : ℕ) :
    ∑ k ∈ Finset.range (n / 2 + 1),
        ((dimHLF (List.replicate k 2 ++ List.replicate (n - 2 * k) 1) : ℕ) : ℤ) ^ 2
      = (catalan n : ℤ) := by
  rw [← QOU.Mathlib.dimHLF_two_row_sq_sum n]
  refine Finset.sum_congr rfl fun k hk => ?_
  have h2k : 2 * k ≤ n := by have := Finset.mem_range.mp hk; omega
  rw [dimHLF_two_col_eq_two_row n k h2k]

/-! ### Small cases, kept as corroboration

These predate the general theorems above and are retained deliberately: each is
computed by `decide` from `dimHLF`'s definition, so they are an independent check
that the general proof's `prodHooks` bookkeeping did not go wrong somewhere that
still typechecks. `dim_eq_dim_transpose_three_to_six` is
`dimHLF_two_col_eq_two_row` at twelve concrete shapes, arrived at a different
way. -/

/-- Transposed shapes have equal dimension at `n = 3, 4, 5, 6`, by evaluation.

Note `(2,1)` at `n = 3` and `(2,2)` at `n = 4` are **self**-conjugate — they lie
in *both* families. That is why the two shape sets overlap rather than being
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

/-- Both readings total `catalan 3 = 5`, over sets sharing only `(2,1)`. -/
theorem sq_sum_agree_three :
    dimHLF [3] ^ 2 + dimHLF [2, 1] ^ 2 = catalan 3 ∧
    dimHLF [2, 1] ^ 2 + dimHLF [1, 1, 1] ^ 2 = catalan 3 := by
  rw [catalan_three]
  exact ⟨by decide, by decide⟩

/-- The same at `n = 6` — `A = 2` in the mass channel — where the two families
share **nothing at all** and the totals still agree. The disjoint case is the
sharper one. -/
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

Worth stating next to the equal totals: it is the conjunction of "different sets"
with "same total" that is dangerous, and a theorem asserting only one half
invites the reader to supply the wrong other half. -/
theorem shape_sets_differ :
    ([[3], [2, 1]] : List (List ℕ)) ≠ [[2, 1], [1, 1, 1]] ∧
    ([[6], [5, 1], [4, 2], [3, 3]] : List (List ℕ))
      ≠ [[1, 1, 1, 1, 1, 1], [2, 1, 1, 1, 1], [2, 2, 1, 1], [2, 2, 2]] := by
  exact ⟨by decide, by decide⟩

/-- **Cross-check: the two routes meet.**

`twoCol k m` is *asserted* to be the transpose of `(k+m, k)`; that assertion is
where the general proof could silently be about the wrong shape while still
typechecking. These evaluate `twoCol` at the three sizes the decided cases cover
and confirm it produces exactly the lists those cases used — so
`dimHLF_twoCol 2 2 : dimHLF (twoCol 2 2) = dimHLF [4, 2]` and the decided
`dimHLF [4, 2] = dimHLF [2, 2, 1, 1]` are statements about one shape, not two. -/
theorem twoCol_agrees_with_decided_shapes :
    twoCol 1 1 = [2, 1] ∧ twoCol 2 2 = [2, 2, 1, 1] ∧
      twoCol 0 6 = [1, 1, 1, 1, 1, 1] ∧ twoCol 1 4 = [2, 1, 1, 1, 1] := by
  refine ⟨by decide, by decide, by decide, by decide⟩

end Dimensions

end QOU.MassTheory.TwoRowTwoColumn
