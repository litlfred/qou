import QOU.Mathlib.SYTBetaGapVandermonde

/-!
# QOU.Mathlib.QHookVandermonde — the q-hook product against a genuine Vandermonde

`SYTBetaGapVandermonde.prodHooksF_one_sub_pow_pair` proves the q-analogue of Frame–Robinson–Thrall
in **`(1 − Q^{β_i − β_j})` form**:

    ∏_c (1 − Q^{h(c)}) · ∏_{i<j} (1 − Q^{β_i − β_j})  =  ∏_i ∏_{m=1}^{β_i} (1 − Q^m).

Its own docstring names what is left: *"with `x_i = Q^{β_i}` the middle factor is `∏_{i<j}(x_i − x_j)`
up to the monomial `∏_{i<j} x_j`."* This file does that conversion, so the identity is available
against a genuine Vandermonde in the node coordinates `x_i = Q^{β_i}` — which is the shape every
consumer in the `LagrangeCoeffSum` family takes, `sum_prod_qratio_corner` included.

The conversion is termwise and needs no sign or exponent bookkeeping:

    x_i − x_j  =  (−x_j) · (1 − Q^{β_i − β_j})        (β_j ≤ β_i)

so the whole monomial-and-sign correction is just `∏_{i<j} (−x_j)`, left in product form rather than
evaluated to `(−1)^{\binom k 2} Q^{\sum_j j·β_j}`. Leaving it unevaluated is deliberate: the
evaluated form is what a hand derivation reaches for and it is where the sign errors live, and no
consumer needs it — the correction cancels against itself on both sides of every ratio.

The only mathematical input is that `β` is **strictly** decreasing on a weakly-decreasing shape,
which is `getD_antitone` plus the `(length − 1 − i)` staircase.

## Base ring (§7c)

Generic `[CommRing R]`. No ordering, no `ℝ`, nothing archimedean; the arguments stay in `ℕ`.

LaTeX label: `lem:q-hook-vandermonde`
-/

namespace QOU.Mathlib.SYTBeta

open Finset

variable {R : Type*} [CommRing R]

/-- **`β` is strictly decreasing.** On a weakly-decreasing shape the parts are antitone and the
`(length − 1 − i)` staircase is strictly antitone, so their sum is strictly antitone. -/
theorem betaNum_lt_betaNum (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (i k : ℕ)
    (h : i + 1 + k < l.length) : betaNum l (i + 1 + k) < betaNum l i := by
  have hanti : l.getD (i + 1 + k) 0 ≤ l.getD i 0 :=
    QOU.BraidKnot.IdentityI.getD_antitone l hl (by omega)
  unfold betaNum
  omega

/-- **The termwise conversion.** `x_i − x_j = (−x_j)·(1 − Q^{β_i − β_j})` at `x_i = Q^{β_i}`.

This is where the `ℕ`-subtraction is discharged: `β_j ≤ β_i` lets `Q^{β_i}` split as
`Q^{β_j} · Q^{β_i − β_j}`, and the rest is `ring`. -/
theorem qPow_betaNum_sub (Q : R) (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (i k : ℕ)
    (h : i + 1 + k < l.length) :
    Q ^ betaNum l i - Q ^ betaNum l (i + 1 + k)
      = (-(Q ^ betaNum l (i + 1 + k)))
          * (1 - Q ^ (betaNum l i - betaNum l (i + 1 + k))) := by
  have hle : betaNum l (i + 1 + k) ≤ betaNum l i :=
    le_of_lt (betaNum_lt_betaNum l hl i k h)
  have hsplit : Q ^ betaNum l i
      = Q ^ betaNum l (i + 1 + k) * Q ^ (betaNum l i - betaNum l (i + 1 + k)) := by
    rw [← pow_add]
    congr 1
    omega
  rw [hsplit]
  ring

/-- **The Vandermonde pair product, in terms of the `(1 − Q^…)` pair product.**

`∏_{i<j} (x_i − x_j) = (∏_{i<j} (−x_j)) · ∏_{i<j} (1 − Q^{β_i − β_j})`, at `x_i = Q^{β_i}`. -/
theorem vandermonde_pair_prod (Q : R) (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) :
    (∏ i ∈ range l.length, ∏ k ∈ range (l.length - (i + 1)),
        (Q ^ betaNum l i - Q ^ betaNum l (i + 1 + k)))
      = (∏ i ∈ range l.length, ∏ k ∈ range (l.length - (i + 1)),
            (-(Q ^ betaNum l (i + 1 + k))))
        * ∏ i ∈ range l.length, ∏ k ∈ range (l.length - (i + 1)),
            (1 - Q ^ (betaNum l i - betaNum l (i + 1 + k))) := by
  rw [← Finset.prod_mul_distrib]
  refine Finset.prod_congr rfl fun i hi => ?_
  rw [← Finset.prod_mul_distrib]
  refine Finset.prod_congr rfl fun k hk => ?_
  rw [mem_range] at hi hk
  exact qPow_betaNum_sub Q l hl i k (by omega)

/-- **The q-hook product against a genuine Vandermonde (divisor-free).**

`∏_c (1 − Q^{h_λ(c)}) · ∏_{i<j} (x_i − x_j) = (∏_{i<j} (−x_j)) · ∏_i ∏_{m=1}^{β_i} (1 − Q^m)`,
at `x_i = Q^{β_i}`.

This is `prodHooksF_one_sub_pow_pair` in the node coordinates the `LagrangeCoeffSum` family uses.
The monomial-and-sign factor `∏_{i<j}(−x_j)` sits on the right rather than being evaluated; it is
the same factor on both sides of any ratio of two such products, so it cancels wherever this is
consumed. -/
theorem prodHooksF_one_sub_pow_vandermonde (Q : R) (l : List ℕ)
    (hl : List.Sorted (· ≥ ·) l) :
    prodHooksF (fun n => 1 - Q ^ n) l *
        (∏ i ∈ range l.length, ∏ k ∈ range (l.length - (i + 1)),
          (Q ^ betaNum l i - Q ^ betaNum l (i + 1 + k)))
      = (∏ i ∈ range l.length, ∏ k ∈ range (l.length - (i + 1)),
            (-(Q ^ betaNum l (i + 1 + k))))
        * ((List.range l.length).map
            (fun i => descFactF (fun n => 1 - Q ^ n)
              (l.getD i 0 + (l.drop (i + 1)).length))).prod := by
  rw [vandermonde_pair_prod Q l hl, ← mul_assoc, mul_comm (prodHooksF _ l), mul_assoc,
    prodHooksF_one_sub_pow_pair Q l hl]

end QOU.Mathlib.SYTBeta
