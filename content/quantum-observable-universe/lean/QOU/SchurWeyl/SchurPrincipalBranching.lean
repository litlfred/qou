import QOU.SchurWeyl.QRatioBetaFactors
import QOU.SchurWeyl.PairProductSplit
import QOU.Mathlib.VandermondeUpdateRatio

/-!
# QOU.SchurWeyl.SchurPrincipalBranching — the box-addition ratio for `schurPrincipal`

The last assembly.  `schurPrincipal_mul_const` writes

`s_μ · C(r) = Q^{n(μ)} · P_μ`,   `P_μ = ∏_{i<j<r}(1 − Q^{β_i−β_j})`,

with `C(r)` independent of `μ`.  Adding a box at row `a` changes `P` only in the pairs involving `a`,
and the two boundary factors are exactly the `q`-ratio's (`QRatioBetaFactors`).  Putting those
together gives the box-addition ratio.

| | |
|---|---|
| `betaPairProd Q r μ` | `P_μ`, in interval indexing |
| `levelConst Q r` | `C(r)`, the `μ`-independent constant |
| `rowColProd Q r a μ` | the row-`a` and column-`a` factors of `P_μ` |
| `betaPairProd_addCell` | `P_ν · (row·col)_μ = P_μ · (row·col)_ν` |
| `schurPrincipal_addCell_mul` | **the box-addition ratio, cross-multiplied** |
| `qratio_prod_eq_rowColProd` | the `q`-ratio **is** `Q^a · (row·col)_ν/(row·col)_μ` |
| `schurPrincipal_addCell_eq` | **`s_ν = (q-ratio) · s_μ`** — the branching hypothesis itself |

The headline is stated **division-free** on purpose: as a cross-multiplied equation it needs no
non-vanishing hypothesis beyond the two the closed form already carries, so it stays true at the
roots of unity where the quotient form is `0/0`.  The quotient form is a corollary for whoever
supplies the genericity.

## Base ring (§7c)

Generic `[Field F]` — `schurPrincipal` is a quotient.  No ordering, no `ℝ`.

LaTeX label: `thm:schur-principal-branching`
-/

namespace QOU.SchurWeyl

open YoungDiagram Finset QOU.Mathlib QOU.Mathlib.SYTBeta

/-- Offset indexing (`∏_{k < r−(i+1)}`) and interval indexing (`∏_{j ∈ Ico (i+1) r}`) agree. -/
theorem prod_offset_eq_prod_Ico {M : Type*} [CommMonoid M] (r : ℕ) (g : ℕ → ℕ → M) :
    (∏ i ∈ Finset.range r, ∏ k ∈ Finset.range (r - (i + 1)), g i (i + 1 + k))
      = ∏ i ∈ Finset.range r, ∏ j ∈ Finset.Ico (i + 1) r, g i j :=
  Finset.prod_congr rfl fun _ _ => (Finset.prod_Ico_eq_prod_range _ _ _).symm

variable {F : Type*} [Field F]

/-- `P_μ = ∏_{i<j<r} (1 − Q^{β_i − β_j})`. -/
noncomputable def betaPairProd (Q : F) (r : ℕ) (μ : YoungDiagram) : F :=
  ∏ i ∈ Finset.range r, ∏ j ∈ Finset.Ico (i + 1) r, (1 - Q ^ (betaR r μ i - betaR r μ j))

/-- `C(r)`, the `μ`-independent constant of the closed form. -/
noncomputable def levelConst (Q : F) (r : ℕ) : F :=
  ∏ i ∈ Finset.range r, descFactF (fun n => 1 - Q ^ n) (r - 1 - i)

/-- The row-`a` and column-`a` factors of `P_μ` — the ones a box at row `a` changes. -/
noncomputable def rowColProd (Q : F) (r a : ℕ) (μ : YoungDiagram) : F :=
  (∏ j ∈ Finset.Ico (a + 1) r, (1 - Q ^ (betaR r μ a - betaR r μ j)))
    * ∏ i ∈ Finset.range a, (1 - Q ^ (betaR r μ i - betaR r μ a))

/-- The closed form, in interval indexing. -/
theorem schurPrincipal_mul_levelConst (Q : F) {r : ℕ} {μ : YoungDiagram}
    (hr : μ.colLen 0 ≤ r)
    (hD : (∏ c ∈ μ.cells, (1 - Q ^ QOU.QBeta.WenzlWeight.hook μ c)) ≠ 0) :
    QOU.QBeta.WenzlWeight.schurPrincipal r Q μ * levelConst Q r
      = Q ^ QOU.QBeta.WenzlWeight.nPart μ * betaPairProd Q r μ := by
  rw [levelConst, betaPairProd, ← prod_offset_eq_prod_Ico]
  exact schurPrincipal_mul_const Q hr hD

/-- **Only the pairs involving `a` change.** -/
theorem betaPairProd_addCell (Q : F) {r : ℕ} {μ : YoungDiagram} {s : ℕ × ℕ}
    (hs : IsAddableCell μ s) (ha : s.1 < r) :
    betaPairProd Q r (addCell μ s hs) * rowColProd Q r s.1 μ
      = betaPairProd Q r μ * rowColProd Q r s.1 (addCell μ s hs) := by
  have hfix : ∀ i, i ≠ s.1 → betaR r (addCell μ s hs) i = betaR r μ i := fun i hi => by
    rw [betaR_addCell hs i, if_neg hi, Nat.add_zero]
  refine prod_pairs_split_ne ha
    (fun i j => 1 - Q ^ (betaR r μ i - betaR r μ j))
    (fun i j => 1 - Q ^ (betaR r (addCell μ s hs) i - betaR r (addCell μ s hs) j))
    (fun i j hi hj => by dsimp only; rw [hfix i (by omega), hfix j hj])
    (fun i j hi hj => by dsimp only; rw [hfix i (by omega), hfix j (by omega)])

/-- **The box-addition ratio for `schurPrincipal`, cross-multiplied.**

`s_ν · C · (row·col)_μ = Q^{a} · (row·col)_ν · s_μ · C`,   `ν = μ + □ at row `a`.

Dividing (where the factors are invertible) gives
`s_ν/s_μ = Q^a · (row·col)_ν/(row·col)_μ`, and `QRatioBetaFactors` identifies that right-hand side
with `∏_{j ≠ a}(Q·x_a − x_j)/(x_a − x_j)` at `x_i = Q^{β_i}` — the hypothesis
`QOU.Mathlib.sum_eq_bracket_mul_of_qratio_scaling` is waiting on. -/
theorem schurPrincipal_addCell_mul (Q : F) {r : ℕ} {μ : YoungDiagram} {s : ℕ × ℕ}
    (hs : IsAddableCell μ s) (ha : s.1 < r)
    (hrμ : μ.colLen 0 ≤ r) (hrν : (addCell μ s hs).colLen 0 ≤ r)
    (hDμ : (∏ c ∈ μ.cells, (1 - Q ^ QOU.QBeta.WenzlWeight.hook μ c)) ≠ 0)
    (hDν : (∏ c ∈ (addCell μ s hs).cells,
      (1 - Q ^ QOU.QBeta.WenzlWeight.hook (addCell μ s hs) c)) ≠ 0) :
    QOU.QBeta.WenzlWeight.schurPrincipal r Q (addCell μ s hs) * levelConst Q r
        * rowColProd Q r s.1 μ
      = Q ^ s.1 * rowColProd Q r s.1 (addCell μ s hs)
        * (QOU.QBeta.WenzlWeight.schurPrincipal r Q μ * levelConst Q r) := by
  have hν := schurPrincipal_mul_levelConst Q hrν hDν
  have hμ := schurPrincipal_mul_levelConst Q hrμ hDμ
  have hsplit := betaPairProd_addCell Q hs ha
  have hn : QOU.QBeta.WenzlWeight.nPart (addCell μ s hs)
      = QOU.QBeta.WenzlWeight.nPart μ + s.1 := nPart_addCell hs
  rw [hν, hμ, hn, pow_add]
  calc Q ^ QOU.QBeta.WenzlWeight.nPart μ * Q ^ s.1 * betaPairProd Q r (addCell μ s hs)
        * rowColProd Q r s.1 μ
      = Q ^ QOU.QBeta.WenzlWeight.nPart μ * Q ^ s.1
          * (betaPairProd Q r (addCell μ s hs) * rowColProd Q r s.1 μ) := by ring
    _ = Q ^ QOU.QBeta.WenzlWeight.nPart μ * Q ^ s.1
          * (betaPairProd Q r μ * rowColProd Q r s.1 (addCell μ s hs)) := by rw [hsplit]
    _ = Q ^ s.1 * rowColProd Q r s.1 (addCell μ s hs)
          * (Q ^ QOU.QBeta.WenzlWeight.nPart μ * betaPairProd Q r μ) := by ring

/-! ## The `q`-ratio, identified -/

/-- **The `q`-ratio is `Q^a` times the row-column ratio.**

`∏_{j ≠ a} (Q·x_a − x_j)/(x_a − x_j) = Q^a · (row·col)_ν / (row·col)_μ`,  `x_i = Q^{β_i}`.

Unconditional beyond `Q ≠ 0`: a product of quotients is the quotient of the products in any field,
and the two `QRatioBetaFactors` lemmas supply the factorwise identity — `j > a` exactly, `j < a`
with one `Q`.  The `a` copies of `Q` from the rows above are what becomes `Q^a`. -/
theorem qratio_prod_eq_rowColProd (Q : F) (hQ : Q ≠ 0) {r : ℕ} {μ : YoungDiagram} {s : ℕ × ℕ}
    (hs : IsAddableCell μ s) (ha : s.1 < r) :
    (∏ j ∈ (Finset.range r).erase s.1,
        (Q * Q ^ betaR r μ s.1 - Q ^ betaR r μ j) / (Q ^ betaR r μ s.1 - Q ^ betaR r μ j))
      = Q ^ s.1 * (rowColProd Q r s.1 (addCell μ s hs) / rowColProd Q r s.1 μ) := by
  have hνa : betaR r (addCell μ s hs) s.1 = betaR r μ s.1 + 1 := by
    rw [betaR_addCell hs, if_pos rfl]
  have hνj : ∀ j, j ≠ s.1 → betaR r (addCell μ s hs) j = betaR r μ j := fun j hj => by
    rw [betaR_addCell hs j, if_neg hj, Nat.add_zero]
  rw [QOU.Mathlib.prod_erase_range_split r s.1 ha]
  -- rows above `a`: one `Q` each
  have hup : ∀ j ∈ Finset.range s.1,
      (Q * Q ^ betaR r μ s.1 - Q ^ betaR r μ j) / (Q ^ betaR r μ s.1 - Q ^ betaR r μ j)
        = Q * ((1 - Q ^ (betaR r (addCell μ s hs) j - betaR r (addCell μ s hs) s.1))
            / (1 - Q ^ (betaR r μ j - betaR r μ s.1))) := by
    intro j hj
    rw [Finset.mem_range] at hj
    rw [qratio_factor_upper Q hQ _ _ (betaR_lt hj ha), hνa, hνj j (by omega), Nat.sub_sub]
  -- rows below `a`: exact
  have hdown : ∀ j ∈ Finset.Ico (s.1 + 1) r,
      (Q * Q ^ betaR r μ s.1 - Q ^ betaR r μ j) / (Q ^ betaR r μ s.1 - Q ^ betaR r μ j)
        = (1 - Q ^ (betaR r (addCell μ s hs) s.1 - betaR r (addCell μ s hs) j))
            / (1 - Q ^ (betaR r μ s.1 - betaR r μ j)) := by
    intro j hj
    rw [Finset.mem_Ico] at hj
    rw [qratio_factor_lower Q hQ _ _ (le_of_lt (betaR_lt (by omega) hj.2)), hνa,
      hνj j (by omega)]
  rw [Finset.prod_congr rfl hup, Finset.prod_congr rfl hdown, Finset.prod_mul_distrib,
    Finset.prod_const, Finset.card_range, Finset.prod_div_distrib, Finset.prod_div_distrib,
    rowColProd, rowColProd]
  field_simp

/-- **The box-addition ratio, in quotient form — the branching hypothesis itself.**

`s_{μ+□ at row a}(1,…,Q^{r−1}) = (∏_{j ≠ a} (Q·x_a − x_j)/(x_a − x_j)) · s_μ(1,…,Q^{r−1})`,
`x_i = Q^{β_i}`.

This is `hw` of `QOU.Mathlib.sum_eq_bracket_mul_of_qratio_scaling` for `schurPrincipal`, so with it
`∑_a s_{μ+□ at a} = [r]_Q · s_μ` — general-`r` branching for the corpus weight.

The two extra hypotheses over the cross-multiplied form are the price of dividing: `levelConst` and
the row-column product must be invertible.  Both are products of `1 − Q^k` at nonzero `k` (the
β-numbers are distinct by `betaR_lt`), so both hold under the same root-of-unity genericity that
`schurPrincipal_eq_zero_iff` already assumes. -/
theorem schurPrincipal_addCell_eq (Q : F) (hQ : Q ≠ 0) {r : ℕ} {μ : YoungDiagram} {s : ℕ × ℕ}
    (hs : IsAddableCell μ s) (ha : s.1 < r)
    (hrμ : μ.colLen 0 ≤ r) (hrν : (addCell μ s hs).colLen 0 ≤ r)
    (hDμ : (∏ c ∈ μ.cells, (1 - Q ^ QOU.QBeta.WenzlWeight.hook μ c)) ≠ 0)
    (hDν : (∏ c ∈ (addCell μ s hs).cells,
      (1 - Q ^ QOU.QBeta.WenzlWeight.hook (addCell μ s hs) c)) ≠ 0)
    (hC : levelConst Q r ≠ 0) (hRC : rowColProd Q r s.1 μ ≠ 0) :
    QOU.QBeta.WenzlWeight.schurPrincipal r Q (addCell μ s hs)
      = (∏ j ∈ (Finset.range r).erase s.1,
          (Q * Q ^ betaR r μ s.1 - Q ^ betaR r μ j) / (Q ^ betaR r μ s.1 - Q ^ betaR r μ j))
        * QOU.QBeta.WenzlWeight.schurPrincipal r Q μ := by
  have h := schurPrincipal_addCell_mul Q hs ha hrμ hrν hDμ hDν
  have h' : QOU.QBeta.WenzlWeight.schurPrincipal r Q (addCell μ s hs) * rowColProd Q r s.1 μ
      = Q ^ s.1 * rowColProd Q r s.1 (addCell μ s hs)
        * QOU.QBeta.WenzlWeight.schurPrincipal r Q μ := by
    refine mul_right_cancel₀ hC ?_
    linear_combination h
  rw [qratio_prod_eq_rowColProd Q hQ hs ha]
  field_simp
  linear_combination h'

end QOU.SchurWeyl
