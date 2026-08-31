import QOU.BraidKnot.Specht

/-!
# QOU.BraidKnot.RowStandardTableau — the index set Murphy's straightening runs over

Mathas' Lemma 3.14, the one remaining input to the Murphy basis
(`HeckeMurphyYoung.basisOfSpanning`), is a statement about **row-standard** tableaux: for `s, t`
row-standard of shape `λ`, `m_{st}` is a combination of `m_{uv}` with `u, v` **standard** of
shape `ν`, where either `ν ⊳ λ`, or `ν = λ` and `u ⊵ s`, `v ⊵ t`.

The corpus had no row-standard notion, and that absence is what blocks the spanning leg rather
than any difficulty in the argument. The gap is quantitative and it is large:

| shape | row-standard `μ`-tableaux | standard `μ`-tableaux |
|---|---|---|
| general `μ ⊢ n` | `n! / ∏ᵢ μᵢ!` | `f^μ` |
| one column `(1ⁿ)` | **`n!`** | **`1`** |

`HeckeMurphyYoung.span_murphySum_one_conjugates_eq_top` (step 2 of spanning) is exactly the
one-column row: every `T_w` is a Murphy element there, because `x_{(1ⁿ)} = 1` and every filling
of a single column is row-standard. Against the *standard* family that shape contributes a
single element, so the statement cannot be made there at all — hence this file.

## Why a predicate and not a new structure

`Specht.Tableau μ = Fin (nOf μ) ≃ μ.cells` is already the *arbitrary* bijective filling, and it
is what `HeckeMurphyYoung.dOf`, `dAt` and `murphyM` consume. Row-standardness is a condition on
such a filling — labels increase along each row — so it is a predicate, and a row-standard
tableau is a subtype. Nothing downstream has to be re-plumbed. (`BraidKnot.StandardYoungTableau`
is a different, `entry`-based structure carrying both `row_strict` and `col_strict`; the
row-standard condition is that structure minus the column half, but expressed on the filling
type the Hecke side already speaks.)

## References
- [mathas1999] Mathas, *Iwahori–Hecke Algebras and Schur Algebras of the Symmetric Group*,
  §3 (the Murphy basis; Lemmas 3.9, 3.12, 3.13, 3.14).
- [sagan2001] Sagan, *The Symmetric Group*, §2.6 (Garnir relations, the `q = 1` template).
-/

namespace QOU.BraidKnot.RowStandardTableau

open QOU.BraidKnot.Specht

variable {μ : YoungDiagram}

/-- **Row-standard**: within any one row, label order agrees with column order.

Stated as the single implication `same row → earlier column → smaller label`. The converse
follows from it (both patterns are determined by the filling, which is a bijection), so this is
the convenient form to *use*: a hypothesis about columns discharges a goal about labels. -/
def IsRowStandard (t : Tableau μ) : Prop :=
  ∀ l l' : Fin (nOf μ), rowPattern t l = rowPattern t l' →
    colPattern t l < colPattern t l' → l < l'

/-- A **row-standard tableau** of shape `μ`. -/
def _root_.QOU.BraidKnot.RowStandardTab (μ : YoungDiagram) : Type :=
  {t : Tableau μ // IsRowStandard t}

instance : CoeOut (QOU.BraidKnot.RowStandardTab μ) (Tableau μ) := ⟨Subtype.val⟩

instance instDecidableIsRowStandard (t : Tableau μ) : Decidable (IsRowStandard t) := by
  unfold IsRowStandard; infer_instance

instance : Fintype (QOU.BraidKnot.RowStandardTab μ) := by
  unfold QOU.BraidKnot.RowStandardTab; infer_instance

/-! ## The one-column shape

A shape with no cell in column `1` has every row of length at most one, so no two distinct
labels share a row and the row-standard condition is **vacuous**: every filling qualifies.
`YoungDiagram` is closed under moving up and left, so `(0,1) ∉ μ` is the whole hypothesis. -/

/-- **Every filling of a one-column shape is row-standard.** -/
theorem isRowStandard_of_no_second_column (hμ : ((0 : ℕ), (1 : ℕ)) ∉ μ) (t : Tableau μ) :
    IsRowStandard t := by
  intro l l' _hrow hcol
  exfalso
  -- put the cell in explicit `(i, j)` form so `up_left_mem` can unify its indices
  have hmem : (((t l' : ℕ × ℕ).1), ((t l' : ℕ × ℕ).2)) ∈ μ := by
    simp
  have hj : 1 ≤ (t l' : ℕ × ℕ).2 := by
    simp only [colPattern] at hcol; omega
  exact hμ (μ.up_left_mem (Nat.zero_le _) hj hmem)

/-- On a one-column shape the row-standard tableaux are **all** the fillings. -/
noncomputable def equivTableauOfNoSecondColumn (hμ : ((0 : ℕ), (1 : ℕ)) ∉ μ) :
    QOU.BraidKnot.RowStandardTab μ ≃ Tableau μ where
  toFun := Subtype.val
  invFun t := ⟨t, isRowStandard_of_no_second_column hμ t⟩
  left_inv _ := rfl
  right_inv _ := rfl

/-- **`n!` row-standard tableaux on a one-column shape** — against exactly one standard tableau.

This is the quantitative form of the gap the module docstring names: it is why Mathas' Lemma
3.14 cannot be stated against the standard-pair index set `HeckeMurphyYoung.MurphyIndex`, and
why `span_murphySum_one_conjugates_eq_top` had to be phrased over conjugating permutations
instead of over tableaux. -/
theorem card_eq_factorial_of_no_second_column (hμ : ((0 : ℕ), (1 : ℕ)) ∉ μ) :
    Fintype.card (QOU.BraidKnot.RowStandardTab μ) = (nOf μ).factorial := by
  classical
  have hc : Fintype.card μ.cells = nOf μ := by
    simp [nOf, YoungDiagram.card]
  have e : Fin (nOf μ) ≃ μ.cells := (Fintype.equivFinOfCardEq hc).symm
  rw [Fintype.card_congr (equivTableauOfNoSecondColumn hμ)]
  show Fintype.card (Fin (nOf μ) ≃ μ.cells) = _
  rw [Fintype.card_equiv e, Fintype.card_fin]

end QOU.BraidKnot.RowStandardTableau
