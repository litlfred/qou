import QOU.SchurWeyl.SchurPrincipalBranching
import QOU.SchurWeyl.WenzlWeightLevelR

/-!
# QOU.SchurWeyl.BranchingGenericity — the four side conditions, from one hypothesis

`schurPrincipal_addCell_eq` carries four non-vanishing hypotheses, and the headline sum needs a
fifth (injectivity of the nodes) plus a row-count bound.  **They are all the same hypothesis**:
`Q` is not a root of unity, in the exact form `QBeta.WenzlWeight.schurPrincipal_eq_zero_iff` already
states it,

`hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1`.

Deriving them here, once, keeps that condition from appearing five times over in every downstream
signature.

| | |
|---|---|
| `one_sub_pow_ne_zero` | `1 − Qⁿ ≠ 0` for `n ≠ 0` — the primitive all four rest on |
| `descFactF_ne_zero`, `levelConst_ne_zero` | the `μ`-independent constant is invertible |
| `rowColProd_ne_zero` | the row-`a` and column-`a` factors are invertible |
| `hookProd_ne_zero` | the hook product is invertible (hooks are `≥ 1`) |
| `betaR_pow_injOn` | `i ↦ Q^{β_i}` is injective on the `r` rows |
| `colLen_zero_addCell_le` | adding a box at row `a` keeps the row count `≤ max(colLen, a+1)` |
| `sum_schurPrincipal_addCellOrSelf` | **`∑_a s_{μ+□ at a} = [r]_Q · s_μ`** — general-`r` branching |
| `sum_wenzlWeight_addCellOrSelf` | the same for the **normalised** weight: `∑_a w_{μ+□ at a} = w_μ` |

The last is not a genericity fact at all — it is the shape bound that keeps `μ + □` inside the
`≤ r`-row hypothesis — but it belongs with the others because it is the remaining side condition.

## Base ring (§7c)

Generic `[Field F]`; `colLen_zero_addCell_le` is pure combinatorics.  No ordering, no `ℝ`.

LaTeX label: `lem:branching-genericity`
-/

namespace QOU.SchurWeyl

open YoungDiagram Finset QOU.Mathlib QOU.Mathlib.SYTBeta

variable {F : Type*} [Field F]

/-- **The primitive.**  At a non-root-of-unity `Q`, `1 − Qⁿ` vanishes only at `n = 0`. -/
theorem one_sub_pow_ne_zero {Q : F} (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) {n : ℕ} (hn : n ≠ 0) :
    (1 : F) - Q ^ n ≠ 0 := by
  intro h
  have h1 : (Q : F) ^ n = 1 := by linear_combination -h
  refine hgen (n : ℤ) (by exact_mod_cast hn) ?_
  rw [zpow_natCast]
  exact h1

theorem descFactF_ne_zero {Q : F} (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (m : ℕ) :
    descFactF (fun n => 1 - Q ^ n) m ≠ 0 := by
  rw [descFactF]
  refine Finset.prod_ne_zero_iff.mpr fun j hj => ?_
  rw [Finset.mem_range] at hj
  exact one_sub_pow_ne_zero hgen (by omega)

theorem levelConst_ne_zero {Q : F} (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (r : ℕ) :
    levelConst Q r ≠ 0 :=
  Finset.prod_ne_zero_iff.mpr fun _ _ => descFactF_ne_zero hgen _

theorem rowColProd_ne_zero {Q : F} (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) {r a : ℕ}
    (ha : a < r) (μ : YoungDiagram) : rowColProd Q r a μ ≠ 0 := by
  rw [rowColProd]
  refine mul_ne_zero (Finset.prod_ne_zero_iff.mpr fun j hj => ?_)
    (Finset.prod_ne_zero_iff.mpr fun i hi => ?_)
  · rw [Finset.mem_Ico] at hj
    exact one_sub_pow_ne_zero hgen
      (by have := betaR_lt (μ := μ) (r := r) (by omega : a < j) hj.2; omega)
  · rw [Finset.mem_range] at hi
    exact one_sub_pow_ne_zero hgen
      (by have := betaR_lt (μ := μ) (r := r) hi ha; omega)

theorem hookProd_ne_zero {Q : F} (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (μ : YoungDiagram) :
    (∏ c ∈ μ.cells, (1 - Q ^ QOU.QBeta.WenzlWeight.hook μ c)) ≠ 0 :=
  Finset.prod_ne_zero_iff.mpr fun c hc =>
    one_sub_pow_ne_zero hgen (by have := QOU.QBeta.WenzlWeight.one_le_hook hc; omega)

/-- **The nodes are distinct.**  `β` is strictly decreasing, and at a non-root-of-unity `Q` distinct
exponents give distinct powers. -/
theorem betaR_pow_injOn {Q : F} (hQ : Q ≠ 0) (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1)
    (r : ℕ) (μ : YoungDiagram) :
    Set.InjOn (fun i => Q ^ betaR r μ i) (Finset.range r) := by
  have key : ∀ i j : ℕ, i < j → j < r → (Q : F) ^ betaR r μ i ≠ Q ^ betaR r μ j := by
    intro i j hij hj hEq
    have hlt : betaR r μ j < betaR r μ i := betaR_lt hij hj
    have hfac : (Q : F) ^ betaR r μ i = Q ^ betaR r μ j * Q ^ (betaR r μ i - betaR r μ j) := by
      rw [← pow_add]; congr 1; omega
    rw [hfac] at hEq
    have hQj : (Q : F) ^ betaR r μ j ≠ 0 := pow_ne_zero _ hQ
    have hone : (Q : F) ^ (betaR r μ i - betaR r μ j) = 1 := by
      refine mul_left_cancel₀ hQj ?_
      rw [mul_one]
      exact hEq
    exact one_sub_pow_ne_zero hgen (n := betaR r μ i - betaR r μ j) (by omega)
      (by rw [hone, sub_self])
  intro i hi j hj hEq
  simp only [Finset.coe_range, Set.mem_Iio] at hi hj
  rcases Nat.lt_trichotomy i j with h | h | h
  · exact absurd hEq (key i j h hj)
  · exact h
  · exact absurd hEq.symm (key j i h hi)

/-- **Adding a box does not raise the row count past `max(colLen 0, a+1)`.** -/
theorem colLen_zero_addCell_le {μ : YoungDiagram} {s : ℕ × ℕ} (hs : IsAddableCell μ s) :
    (addCell μ s hs).colLen 0 ≤ max (μ.colLen 0) (s.1 + 1) := by
  by_contra hcon
  push_neg at hcon
  have hmem : ((max (μ.colLen 0) (s.1 + 1), 0) : ℕ × ℕ) ∈ addCell μ s hs :=
    mem_iff_lt_colLen.mpr hcon
  rcases (mem_addCell s hs _).mp hmem with heq | hmemμ
  · have hfst : max (μ.colLen 0) (s.1 + 1) = s.1 := congrArg Prod.fst heq
    omega
  · have := mem_iff_lt_colLen.mp hmemμ
    omega

/-! ## General-`r` branching for `schurPrincipal` -/

/-- **General-`r` branching for the corpus weight.**

`∑_{a < r} s_{μ + □ at row a}(1, Q, …, Q^{r−1}) = (1 + Q + ⋯ + Q^{r−1}) · s_μ(1, Q, …, Q^{r−1})`,

the sum running over all `r` rows with the non-addable ones contributing `0`.

This is what #5575 proves at `r = 2` by way of `schurPrincipal_twoRow`'s telescoping closed form —
now at every level, for `QBeta.WenzlWeight.schurPrincipal` itself.  The single hypothesis `hgen` is
the same root-of-unity genericity `schurPrincipal_eq_zero_iff` carries; everything else is derived
above.

The summand is total (`addCellOrSelf` guarded by the decidable `IsAddableCell`) rather than indexed
by addability proofs, which is what `qratio_prod_eq_zero_of_not_addable` buys: on a row that cannot
take a box the `q`-ratio is already zero, so the guarded sum and a sum over addable rows agree. -/
theorem sum_schurPrincipal_addCellOrSelf (Q : F) (hQ0 : Q ≠ 0) (hQ1 : Q ≠ 1)
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) {r : ℕ} {μ : YoungDiagram} (hrμ : μ.colLen 0 ≤ r) :
    (∑ a ∈ Finset.range r,
        (if IsAddableCell μ (a, μ.rowLen a) then
          QOU.QBeta.WenzlWeight.schurPrincipal r Q (addCellOrSelf μ (a, μ.rowLen a)) else 0))
      = (∑ k ∈ Finset.range r, Q ^ k) * QOU.QBeta.WenzlWeight.schurPrincipal r Q μ := by
  classical
  have hkey := QOU.Mathlib.sum_eq_bracket_mul_of_qratio_scaling
    (s := Finset.range r) (v := fun i => Q ^ betaR r μ i)
    (betaR_pow_injOn hQ0 hgen r μ) (fun i _ => pow_ne_zero _ hQ0) hQ0 hQ1
    (fun a => if IsAddableCell μ (a, μ.rowLen a) then
      QOU.QBeta.WenzlWeight.schurPrincipal r Q (addCellOrSelf μ (a, μ.rowLen a)) else 0)
    (QOU.QBeta.WenzlWeight.schurPrincipal r Q μ) ?_
  · rwa [Finset.card_range] at hkey
  · intro a hi
    rw [Finset.mem_range] at hi
    dsimp only
    by_cases hadd : IsAddableCell μ (a, μ.rowLen a)
    · rw [if_pos hadd, addCellOrSelf_of hadd]
      have hrν : (addCell μ (a, μ.rowLen a) hadd).colLen 0 ≤ r :=
        le_trans (colLen_zero_addCell_le hadd) (by simp only [max_le_iff]; omega)
      exact schurPrincipal_addCell_eq Q hQ0 hadd hi hrμ hrν
        (hookProd_ne_zero hgen μ) (hookProd_ne_zero hgen _)
        (levelConst_ne_zero hgen r) (rowColProd_ne_zero hgen hi μ)
    · rw [if_neg hadd]
      obtain ⟨hpos, heq⟩ := not_isAddableCell_rowEnd μ hadd
      rw [Finset.prod_div_distrib, qratio_prod_eq_zero_of_not_addable Q hpos hi heq,
        zero_div, zero_mul]

theorem card_addCell {μ : YoungDiagram} {s : ℕ × ℕ} (hs : IsAddableCell μ s) :
    (addCell μ s hs).cells.card = μ.cells.card + 1 := by
  have hnot : s ∉ μ.cells := fun h => hs.1 (by simpa using h)
  have hcells : (addCell μ s hs).cells = insert s μ.cells := by
    ext c
    simp only [YoungDiagram.mem_cells, mem_addCell, Finset.mem_insert]
  rw [hcells, Finset.card_insert_of_notMem hnot]

/-- **Branching for the normalised weight**: `∑_{a<r} w_{μ + □ at row a} = w_μ`.

The normalisation `w_μ = s_μ / [r]_Q^{|μ|}` is chosen so that the `[r]_Q` produced by
`sum_schurPrincipal_addCellOrSelf` is exactly absorbed by the one extra cell each summand carries.
This is the "weights are consistent under restriction" half of "these are the Ocneanu weights" —
`MarkovNormalisation.ocneanuWeight_addable_sum` at `r = 2`, now at every level. -/
theorem sum_wenzlWeight_addCellOrSelf (Q : F) (hQ0 : Q ≠ 0) (hQ1 : Q ≠ 1)
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) {r : ℕ} {μ : YoungDiagram} (hrμ : μ.colLen 0 ≤ r)
    (hbr : levelBracket r Q ≠ 0) :
    (∑ a ∈ Finset.range r,
        (if IsAddableCell μ (a, μ.rowLen a) then
          wenzlWeight r Q (addCellOrSelf μ (a, μ.rowLen a)) else 0))
      = wenzlWeight r Q μ := by
  have hrw : ∀ a ∈ Finset.range r,
      (if IsAddableCell μ (a, μ.rowLen a) then
          wenzlWeight r Q (addCellOrSelf μ (a, μ.rowLen a)) else 0)
        = (if IsAddableCell μ (a, μ.rowLen a) then
            QOU.QBeta.WenzlWeight.schurPrincipal r Q (addCellOrSelf μ (a, μ.rowLen a)) else 0)
          / levelBracket r Q ^ (μ.cells.card + 1) := by
    intro a _
    by_cases h : IsAddableCell μ (a, μ.rowLen a)
    · rw [if_pos h, if_pos h, wenzlWeight, addCellOrSelf_of h, card_addCell h]
    · rw [if_neg h, if_neg h, zero_div]
  rw [Finset.sum_congr rfl hrw, ← Finset.sum_div,
    sum_schurPrincipal_addCellOrSelf Q hQ0 hQ1 hgen hrμ,
    show (∑ k ∈ Finset.range r, Q ^ k) = levelBracket r Q from rfl, wenzlWeight, pow_succ]
  field_simp

end QOU.SchurWeyl
