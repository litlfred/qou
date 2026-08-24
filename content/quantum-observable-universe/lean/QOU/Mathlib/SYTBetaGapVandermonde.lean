import QOU.Mathlib.SYTHookFormulaBetaProdMonoid

/-!
# QOU.Mathlib.SYTBetaGapVandermonde — the β-gap product is the Vandermonde pair product

`SYTHookFormulaBetaProdMonoid` proves the divisor-free Frame–Robinson–Thrall hook product with the
denominator carried as a **nested recursion**, `∏_i betaGapProdF f (l[i]) (l.drop (i+1))`.  The
consumer wants it as a **pair product** `∏_{i<j} f(β_i − β_j)` — the Vandermonde shape, which at
`f n = 1 − Qⁿ` and `x_i = Q^{β_i}` is `∏_{i<j}(x_i − x_j)` up to a monomial.

This file is that reindexing.  It is bookkeeping, not a new identity: `betaGapProdF`'s recursion
advances `a` by one per step precisely because `β` decreases by one per row beyond the part, so the
`k`-th factor of row `i` is already `f(β_i − β_{i+1+k})`.

| | |
|---|---|
| `betaNum l i` | `β_i = l[i] + (|l| − 1 − i)` |
| `betaGapProdF_eq_prod_range` | the recursion as a `Finset.range` product |
| `betaGap_eq_betaNum_sub` | the `k`-th factor's argument **is** `β_i − β_{i+1+k}` |
| `prod_betaGapProdF_eq_pair_prod` | `∏_i betaGapProdF … = ∏_{i<j} f(β_i − β_j)` |
| `prodHooksF_mul_pair_prod` | the FRT hook product with the Vandermonde denominator |
| `prodHooksF_one_sub_pow_pair` | the same at `f n = 1 − Qⁿ` |

The last row completes sub-brick (a) of the general-`r` branching route (bean `qou-j7ln`): the
q-analogue of `∏_c h_λ(c) = (∏_i β_i!)/∏_{i<j}(β_i − β_j)`, cleared of its denominator and with that
denominator in pair form.

## Base ring (§7c)

Generic `[CommMonoid M]`; the q-instance is over `[CommRing R]`.  Arguments stay in `ℕ`.

LaTeX label: `lem:beta-gap-vandermonde`
-/

namespace QOU.Mathlib.SYTBeta

open QOU.BraidKnot.IdentityI (prodHooks)

variable {M : Type*} [CommMonoid M]

/-- The β-number of row `i`: `β_i = l[i] + (|l| − 1 − i)`.  Strictly decreasing in `i` for a
weakly-decreasing `l`. -/
def betaNum (l : List ℕ) (i : ℕ) : ℕ := l.getD i 0 + (l.length - 1 - i)

/-- The β-gap recursion, unrolled into a `Finset.range` product: the `k`-th factor is
`f(a + (k+1) − t[k])`. -/
theorem betaGapProdF_eq_prod_range (f : ℕ → M) (a : ℕ) (t : List ℕ) :
    betaGapProdF f a t = ∏ k ∈ Finset.range t.length, f (a + (k + 1) - t.getD k 0) := by
  induction t generalizing a with
  | nil => simp
  | cons c r ih =>
    rw [betaGapProdF_cons, ih (a + 1), List.length_cons, Finset.prod_range_succ']
    simp only [List.getD_cons_zero, List.getD_cons_succ]
    rw [mul_comm]
    congr 1
    refine Finset.prod_congr rfl fun k _ => ?_
    congr 1
    omega

theorem getD_drop (l : List ℕ) (i k : ℕ) : (l.drop i).getD k 0 = l.getD (i + k) 0 := by
  rw [List.getD_eq_getElem?_getD, List.getD_eq_getElem?_getD, List.getElem?_drop]

/-- Row `i`'s β-gap product, indexed by the offset `k` into the rows below. -/
theorem betaGapProdF_drop_eq (f : ℕ → M) (l : List ℕ) (i : ℕ) :
    betaGapProdF f (l.getD i 0) (l.drop (i + 1))
      = ∏ k ∈ Finset.range (l.length - (i + 1)),
          f (l.getD i 0 + (k + 1) - l.getD (i + 1 + k) 0) := by
  rw [betaGapProdF_eq_prod_range, List.length_drop]
  refine Finset.prod_congr rfl fun k _ => ?_
  rw [getD_drop]

/-- **The `k`-th β-gap factor of row `i` is `β_i − β_{i+1+k}`.**

`β_i − β_j = (l[i] − l[j]) + (j − i)` for `j > i`, and the recursion's `a + (k+1) − t[k]` is exactly
that with `j = i+1+k`.  Needs `l[j] ≤ l[i]`, i.e. that `l` is weakly decreasing — without it the two
truncated subtractions part company. -/
theorem betaGap_eq_betaNum_sub (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (i k : ℕ)
    (h : i + 1 + k < l.length) :
    l.getD i 0 + (k + 1) - l.getD (i + 1 + k) 0 = betaNum l i - betaNum l (i + 1 + k) := by
  have hanti : l.getD (i + 1 + k) 0 ≤ l.getD i 0 :=
    QOU.BraidKnot.IdentityI.getD_antitone l hl (by omega)
  unfold betaNum
  omega

/-- **The β-gap product in Vandermonde pair form.** -/
theorem prod_betaGapProdF_eq_pair_prod (f : ℕ → M) (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) :
    ((List.range l.length).map
        (fun i => betaGapProdF f (l.getD i 0) (l.drop (i + 1)))).prod
      = ∏ i ∈ Finset.range l.length, ∏ k ∈ Finset.range (l.length - (i + 1)),
          f (betaNum l i - betaNum l (i + 1 + k)) := by
  rw [list_range_map_prod']
  refine Finset.prod_congr rfl fun i hi => ?_
  rw [Finset.mem_range] at hi
  rw [betaGapProdF_drop_eq]
  refine Finset.prod_congr rfl fun k hk => ?_
  rw [Finset.mem_range] at hk
  rw [betaGap_eq_betaNum_sub l hl i k (by omega)]

/-- **The divisor-free FRT hook product with a Vandermonde denominator, any commutative monoid.**

`∏_c f(h_λ(c)) · ∏_{i<j} f(β_i − β_j) = ∏_i descFactF f β_i`. -/
theorem prodHooksF_mul_pair_prod (f : ℕ → M) (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) :
    prodHooksF f l *
        (∏ i ∈ Finset.range l.length, ∏ k ∈ Finset.range (l.length - (i + 1)),
          f (betaNum l i - betaNum l (i + 1 + k)))
      = ((List.range l.length).map
          (fun i => descFactF f (l.getD i 0 + (l.drop (i + 1)).length))).prod := by
  rw [← prod_betaGapProdF_eq_pair_prod f l hl]
  exact prodHooksF_mul_betaGapProdF f l hl

/-- **The q-analogue, in Vandermonde-ready form.**

`∏_c (1 − Q^{h_λ(c)}) · ∏_{i<j} (1 − Q^{β_i − β_j}) = ∏_i ∏_{k=1}^{β_i} (1 − Q^k)`.

This is the hook-length input that
`QOU.Mathlib.LagrangeCoeffSum.sum_eq_bracket_mul_of_qratio_scaling` needs, cleared of division.
With `x_i = Q^{β_i}` the middle factor is `∏_{i<j}(x_i − x_j)` up to the monomial `∏_{i<j} x_j`. -/
theorem prodHooksF_one_sub_pow_pair {R : Type*} [CommRing R] (Q : R) (l : List ℕ)
    (hl : List.Sorted (· ≥ ·) l) :
    prodHooksF (fun n => 1 - Q ^ n) l *
        (∏ i ∈ Finset.range l.length, ∏ k ∈ Finset.range (l.length - (i + 1)),
          (1 - Q ^ (betaNum l i - betaNum l (i + 1 + k))))
      = ((List.range l.length).map
          (fun i => descFactF (fun n => 1 - Q ^ n)
            (l.getD i 0 + (l.drop (i + 1)).length))).prod :=
  prodHooksF_mul_pair_prod (fun n => 1 - Q ^ n) l hl

end QOU.Mathlib.SYTBeta
