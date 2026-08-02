import Mathlib.Data.Nat.Choose.Vandermonde
import Mathlib.Data.Nat.Choose.Central
import Mathlib.Algebra.BigOperators.NatAntidiagonal
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# Binomial-square sums and the hook-shape bracket collapse

The classical moment sums of the **squared binomial** weight `C(m,k)²`, in division-free form,
together with the algebraic collapse they produce in the (TAIL) first-instance computation of the
covariance-kernel epic.

## Why these sums

The carrier lemma (`YoungDiagramKernelPincer.hookShape_of_hookLen_eq_sum` + its converse) confines
the top hook statistic `N_n` to the corner cells of the `n` **hook shapes** `(a, 1^c)`, and the
hook-shape data (`sytDim_hookShape`: `f^{(a,1^c)} = C(n−1, a−1)`; `contentSq_hookShape`) turns the
covariance `ν_n = Cov_Planch(N_n, ω₃)` into a single classical sum over `k = a − 1`:

`n! · ν_n = Σ_{k ≤ m} C(m,k)² · [Q(k) + Q(m−k) − C(n,2)]`,  `m = n − 1`,

with `Q(x) = Σ_{t ≤ x} t²`. Expanding the bracket, the **cubic terms cancel identically** between
the arm and the leg contributions:

`6·[Q(k) + Q(m−k) − C(n,2)] = 2(m+1)·(3k² − 3mk + m(m−1))`,

so only the zeroth, first and second `C(m,k)²`-moments are needed — a simplification of the
five-step derivation recorded in
`docs/audits/2026-07-26-covariance-kernel-A2-tail-first-instance.md`, whose step 4 lists the cubic
sum as well. (`two_mul_sum_cube_mul_choose_sq` below records the cubic sum anyway: it completes the
moment family and makes the cancellation claim checkable.)

## The moments

Each is stated **division-free** (odd moments carry an explicit factor `2`), over `ℕ`:

| moment | value |
|---|---|
| `Σ_{k≤m} C(m,k)²` | `C(2m, m)` (Vandermonde + symmetry) |
| `2·Σ_{k≤m} k·C(m,k)²` | `m·C(2m, m)` (reflection `k ↦ m − k`) |
| `Σ_{k≤m+1} k²·C(m+1,k)²` | `(m+1)²·C(2m, m)` (absorption `k·C(m+1,k) = (m+1)·C(m,k−1)`) |
| `2·Σ_{k≤m+1} k³·C(m+1,k)²` | `(m+1)²(m+2)·C(2m, m)` (absorption + reflection) |

and the payoff `bracket_sum_collapse` is the step-5 algebra: the bracket sum collapses to
`(m−1)(m−2)·C(2m−2, m−1)`, whose factor `(m−2) = (n−3)` is the exact source of the `n = 3` zero in
the closed form `ν_n = n(n−2)(n−3)·C(2n−4, n−2)/(3·n!)`.
-/

namespace QOU.BraidsAndKnots.BinomialSquareSums

open Finset

/-! ## The zeroth moment: Vandermonde convolution at the centre -/

/-- **Vandermonde square sum**: `Σ_{k ≤ m} C(m,k)² = C(2m, m)`. The central Vandermonde
convolution `C(m+m, m) = Σ_{i+j=m} C(m,i)·C(m,j)` with the symmetry `C(m, m−k) = C(m, k)`. -/
theorem sum_choose_sq (m : ℕ) :
    ∑ k ∈ range (m + 1), (m.choose k) ^ 2 = (2 * m).choose m := by
  rw [two_mul, Nat.add_choose_eq, Finset.Nat.sum_antidiagonal_eq_sum_range_succ_mk]
  refine Finset.sum_congr rfl fun k hk => ?_
  rw [Nat.choose_symm (Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)), sq]

/-! ## The first moment: reflection -/

/-- **First moment (division-free)**: `2·Σ_{k ≤ m} k·C(m,k)² = m·C(2m, m)`. Reflecting
`k ↦ m − k` leaves the weight invariant, so summing the two orderings replaces `k` by
`k + (m − k) = m`. -/
theorem two_mul_sum_mul_choose_sq (m : ℕ) :
    2 * ∑ k ∈ range (m + 1), k * (m.choose k) ^ 2 = m * ((2 * m).choose m) := by
  have hB : ∑ j ∈ range (m + 1), (m - j) * (m.choose j) ^ 2
      = ∑ j ∈ range (m + 1), j * (m.choose j) ^ 2 := by
    have hrefl := Finset.sum_range_reflect (fun k => k * (m.choose k) ^ 2) (m + 1)
    simp only [Nat.add_sub_cancel] at hrefl
    rw [← hrefl]
    refine Finset.sum_congr rfl fun j hj => ?_
    rw [Nat.choose_symm (Nat.lt_succ_iff.mp (Finset.mem_range.mp hj))]
  have hsum : ∑ j ∈ range (m + 1), j * (m.choose j) ^ 2
      + ∑ j ∈ range (m + 1), (m - j) * (m.choose j) ^ 2 = m * ((2 * m).choose m) := by
    rw [← Finset.sum_add_distrib, ← sum_choose_sq m, Finset.mul_sum]
    refine Finset.sum_congr rfl fun j hj => ?_
    have hjm : j ≤ m := Nat.lt_succ_iff.mp (Finset.mem_range.mp hj)
    rw [← Nat.add_mul]
    congr 1
    omega
  rw [hB] at hsum
  omega

/-! ## The absorption identity and the second moment -/

/-- **Absorption**: `(k+1)·C(m+1, k+1) = (m+1)·C(m, k)` — the standard index-shift that turns a
`k`-weighted binomial into an unweighted one at one lower order. -/
theorem succ_mul_choose_succ (m k : ℕ) :
    (k + 1) * ((m + 1).choose (k + 1)) = (m + 1) * (m.choose k) := by
  rw [Nat.mul_comm (k + 1) ((m + 1).choose (k + 1)), ← Nat.succ_mul_choose_eq]

/-- **Second moment**: `Σ_{k ≤ m+1} k²·C(m+1, k)² = (m+1)²·C(2m, m)`. The `k = 0` term vanishes;
absorption turns each remaining term into `(m+1)²·C(m, k−1)²`, and the zeroth moment finishes. -/
theorem sum_sq_mul_choose_sq (m : ℕ) :
    ∑ k ∈ range (m + 2), k ^ 2 * ((m + 1).choose k) ^ 2
      = (m + 1) ^ 2 * ((2 * m).choose m) := by
  have hterm : ∀ j ∈ range (m + 1),
      (j + 1) ^ 2 * ((m + 1).choose (j + 1)) ^ 2 = (m + 1) ^ 2 * (m.choose j) ^ 2 := by
    intro j _
    calc (j + 1) ^ 2 * ((m + 1).choose (j + 1)) ^ 2
        = ((j + 1) * ((m + 1).choose (j + 1))) ^ 2 := by ring
      _ = ((m + 1) * (m.choose j)) ^ 2 := by rw [succ_mul_choose_succ]
      _ = (m + 1) ^ 2 * (m.choose j) ^ 2 := by ring
  rw [Finset.sum_range_succ', Finset.sum_congr rfl hterm, ← Finset.mul_sum, sum_choose_sq]
  simp

/-- **Third moment (division-free)**: `2·Σ_{k ≤ m+1} k³·C(m+1, k)² = (m+1)²(m+2)·C(2m, m)`.
Absorption reduces the cube to `(k+1)·[(m+1)·C(m,k)]²`, then the first and zeroth moments at
order `m` finish. Recorded for completeness of the moment family: the cubic terms **cancel** in
the hook-shape bracket (see `bracket_sum_collapse`), so this moment is not consumed there. -/
theorem two_mul_sum_cube_mul_choose_sq (m : ℕ) :
    2 * ∑ k ∈ range (m + 2), k ^ 3 * ((m + 1).choose k) ^ 2
      = (m + 1) ^ 2 * (m + 2) * ((2 * m).choose m) := by
  have hterm : ∀ j ∈ range (m + 1),
      (j + 1) ^ 3 * ((m + 1).choose (j + 1)) ^ 2
        = (m + 1) ^ 2 * (j * (m.choose j) ^ 2) + (m + 1) ^ 2 * (m.choose j) ^ 2 := by
    intro j _
    have habs : ((j + 1) * ((m + 1).choose (j + 1))) ^ 2 = ((m + 1) * (m.choose j)) ^ 2 := by
      rw [succ_mul_choose_succ]
    calc (j + 1) ^ 3 * ((m + 1).choose (j + 1)) ^ 2
        = (j + 1) * ((j + 1) * ((m + 1).choose (j + 1))) ^ 2 := by ring
      _ = (j + 1) * ((m + 1) * (m.choose j)) ^ 2 := by rw [habs]
      _ = (m + 1) ^ 2 * (j * (m.choose j) ^ 2) + (m + 1) ^ 2 * (m.choose j) ^ 2 := by ring
  rw [Finset.sum_range_succ', Finset.sum_congr rfl hterm, Finset.sum_add_distrib,
      ← Finset.mul_sum, ← Finset.mul_sum, sum_choose_sq]
  have h1 := two_mul_sum_mul_choose_sq m
  have hz : (0 : ℕ) ^ 3 * ((m + 1).choose 0) ^ 2 = 0 := by norm_num
  rw [hz, Nat.add_zero]
  set S := ∑ k ∈ range (m + 1), k * (m.choose k) ^ 2 with hS
  set C := (2 * m).choose m with hC
  have hexp : 2 * ((m + 1) ^ 2 * S + (m + 1) ^ 2 * C)
      = (m + 1) ^ 2 * (2 * S) + 2 * ((m + 1) ^ 2 * C) := by ring
  rw [hexp, h1]
  ring

/-! ## The central-binomial step and the collapse -/

/-- **Central-binomial step**: `(m+1)·C(2m+2, m+1) = 2(2m+1)·C(2m, m)` — the ratio of successive
central binomial coefficients, in division-free form (`Nat.succ_mul_centralBinom_succ`). -/
theorem succ_mul_central_succ (m : ℕ) :
    (m + 1) * ((2 * (m + 1)).choose (m + 1)) = 2 * (2 * m + 1) * ((2 * m).choose m) := by
  have h := Nat.succ_mul_centralBinom_succ m
  simpa [Nat.centralBinom] using h

/-- **The step-5 collapse.** With `m = r + 1`, the hook-shape bracket sum collapses:

`Σ_{k ≤ m} C(m,k)²·(3k² − 3mk + m(m−1)) = (m−1)(m−2)·C(2m−2, m−1)`.

Stated over `ℤ` at `m = r + 1` (so the subtractions are genuine): the left side is the bracket
sum, the right side `r(r−1)·C(2r, r)`. The factor `(r − 1) = (m − 2) = (n − 3)` is the exact
source of the `n = 3` zero of `ν_n`.

Proof: substitute the three moments (`sum_sq_mul_choose_sq`, `two_mul_sum_mul_choose_sq`,
`sum_choose_sq`), eliminate `C(2r+2, r+1)` via `succ_mul_central_succ`, and collapse the
polynomial coefficient `6(r+1)² − 2(2r+1)(r+3) = 2r(r−1)`. -/
theorem bracket_sum_collapse (r : ℕ) :
    ∑ k ∈ range (r + 2), (((r + 1).choose k : ℤ)) ^ 2 *
        (3 * (k : ℤ) ^ 2 - 3 * ((r : ℤ) + 1) * (k : ℤ) + ((r : ℤ) + 1) * (r : ℤ))
      = (r : ℤ) * ((r : ℤ) - 1) * (((2 * r).choose r : ℤ)) := by
  -- Split the bracket sum into the three moments.
  have hsplit : ∑ k ∈ range (r + 2), (((r + 1).choose k : ℤ)) ^ 2 *
        (3 * (k : ℤ) ^ 2 - 3 * ((r : ℤ) + 1) * (k : ℤ) + ((r : ℤ) + 1) * (r : ℤ))
      = 3 * (∑ k ∈ range (r + 2), ((k : ℤ) ^ 2 * (((r + 1).choose k : ℤ)) ^ 2))
        - 3 * ((r : ℤ) + 1) * (∑ k ∈ range (r + 2), ((k : ℤ) * (((r + 1).choose k : ℤ)) ^ 2))
        + ((r : ℤ) + 1) * (r : ℤ) * (∑ k ∈ range (r + 2), (((r + 1).choose k : ℤ)) ^ 2) := by
    rw [Finset.mul_sum, Finset.mul_sum, Finset.mul_sum, ← Finset.sum_sub_distrib,
        ← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun k _ => by ring
  rw [hsplit]
  -- The three ℕ moments, cast to ℤ.
  have m2 : (∑ k ∈ range (r + 2), ((k : ℤ) ^ 2 * (((r + 1).choose k : ℤ)) ^ 2))
      = ((r : ℤ) + 1) ^ 2 * (((2 * r).choose r : ℤ)) := by
    have h := sum_sq_mul_choose_sq r
    have := congrArg (fun n : ℕ => (n : ℤ)) h
    push_cast at this
    exact this
  have m1 : 2 * (∑ k ∈ range (r + 2), ((k : ℤ) * (((r + 1).choose k : ℤ)) ^ 2))
      = ((r : ℤ) + 1) * (((2 * (r + 1)).choose (r + 1) : ℤ)) := by
    have h := two_mul_sum_mul_choose_sq (r + 1)
    have := congrArg (fun n : ℕ => (n : ℤ)) h
    push_cast at this
    convert this using 2
  have m0 : (∑ k ∈ range (r + 2), (((r + 1).choose k : ℤ)) ^ 2)
      = (((2 * (r + 1)).choose (r + 1) : ℤ)) := by
    have h := sum_choose_sq (r + 1)
    have := congrArg (fun n : ℕ => (n : ℤ)) h
    push_cast at this
    exact this
  have hcent : ((r : ℤ) + 1) * (((2 * (r + 1)).choose (r + 1) : ℤ))
      = 2 * (2 * (r : ℤ) + 1) * (((2 * r).choose r : ℤ)) := by
    have h := succ_mul_central_succ r
    have := congrArg (fun n : ℕ => (n : ℤ)) h
    push_cast at this
    exact this
  rw [m2, m0]
  -- Multiply through by 2 to use the division-free first moment.
  have key : 2 * (3 * (((r : ℤ) + 1) ^ 2 * (((2 * r).choose r : ℤ)))
        - 3 * ((r : ℤ) + 1) * (∑ k ∈ range (r + 2), ((k : ℤ) * (((r + 1).choose k : ℤ)) ^ 2))
        + ((r : ℤ) + 1) * (r : ℤ) * (((2 * (r + 1)).choose (r + 1) : ℤ)))
      = 2 * ((r : ℤ) * ((r : ℤ) - 1) * (((2 * r).choose r : ℤ))) := by
    have hm1 : 3 * ((r : ℤ) + 1) *
        (2 * (∑ k ∈ range (r + 2), ((k : ℤ) * (((r + 1).choose k : ℤ)) ^ 2)))
        = 3 * ((r : ℤ) + 1) * (((r : ℤ) + 1) * (((2 * (r + 1)).choose (r + 1) : ℤ))) := by
      rw [m1]
    have hc2 : ((r : ℤ) + 1) * (((r : ℤ) + 1) * (((2 * (r + 1)).choose (r + 1) : ℤ)))
        = ((r : ℤ) + 1) * (2 * (2 * (r : ℤ) + 1) * (((2 * r).choose r : ℤ))) := by
      rw [hcent]
    have hc3 : (r : ℤ) * (((r : ℤ) + 1) * (((2 * (r + 1)).choose (r + 1) : ℤ)))
        = (r : ℤ) * (2 * (2 * (r : ℤ) + 1) * (((2 * r).choose r : ℤ))) := by
      rw [hcent]
    linarith [hm1, hc2, hc3]
  linarith [key]

end QOU.BraidsAndKnots.BinomialSquareSums
