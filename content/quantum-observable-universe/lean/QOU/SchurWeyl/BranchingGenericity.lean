import QOU.SchurWeyl.SchurPrincipalBranching

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

end QOU.SchurWeyl
