import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.Nat.Choose.Vandermonde
import Mathlib.Combinatorics.Enumerative.Catalan
import Mathlib.Algebra.BigOperators.NatAntidiagonal
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# Ballot numbers `m_j(n) = C(n,j) − C(n,j−1)`

**Bean `qou-0cyu`, items G1/G2/G5.** Mathlib infrastructure: at the pinned rev
Mathlib has `Nat.choose` and `catalan` but no ballot numbers, no
pattern-avoidance theory, and no RSK. This file supplies the piece that both
open identities need.

## Why this number

`m_j(n)` is the number of standard Young tableaux of the two-row shape
`(n − j, j)`. It is the multiplicity with which the irreducible `(n − j, j)`
occurs in the `n`-fold tensor power of the 2-dimensional representation, and the
two open statements in `qou-0cyu` are both statements about it:

* **G2** `[2]_qⁿ = Σ_j m_j(n) · [n − 2j + 1]_q` — the `q`-dimension of `V^⊗n`.
* **G5** `Σ_j m_j(n)² = catalan n` — by RSK, "321-avoiding permutations are
  Catalan". **Proved for general `n` below** (`ballot_sq_sum_catalan`), and not
  by RSK: see the section heading before `choose_sq_sum` for why the induction
  route does not close and what replaces it.

## The engine, and why it is the whole content

Everything reduces to one recursion:

    m_{j+1}(n+1) = m_{j+1}(n) + m_j(n)

This is Pascal applied twice, and it is *exactly* the shape needed to run the
induction for G2 against the `q`-integer three-term recursion
`[m+2] + [m] = [2]·[m+1]` already proved in
`QOU.QBeta.TemperleyLiebTower.qint_three_term`. Matching the two recursions term
by term is what makes G2 an induction rather than a computation:

    [2]ⁿ⁺¹ = [2]·Σ_j m_j(n)[n−2j+1] = Σ_j m_j(n)([n−2j+2] + [n−2j])

and collecting the coefficient of `[n−2j+2]` on the right gives
`m_j(n) + m_{j−1}(n)`, which `ballot_succ_succ` says is `m_j(n+1)`. The two
recursions are the same recursion.

## Indexing

`ballot n 0 = 1` by definition rather than by the formula, because the formula
would need `C(n, −1) = 0` and `ℕ` subtraction silently gives `C(n, 0)` instead —
the classic off-by-one that makes `m_0` come out `0` rather than `1`. Values are
`ℤ` so that `m_j(n)` can be written as a difference without truncation, even
though every value in range is a nonnegative integer.
-/

namespace QOU.Mathlib

/-- **Ballot number** `m_j(n) = C(n,j) − C(n,j−1)`, the number of standard Young
tableaux of shape `(n − j, j)`.

The `j = 0` case is given directly rather than by the difference: `C(n, 0−1)`
would be `C(n, 0)` under `ℕ` subtraction, making `m_0(n) = 0` instead of `1`. -/
def ballot (n : ℕ) : ℕ → ℤ
  | 0 => 1
  | (j + 1) => (n.choose (j + 1) : ℤ) - (n.choose j : ℤ)

@[simp] theorem ballot_zero (n : ℕ) : ballot n 0 = 1 := rfl

@[simp] theorem ballot_succ (n j : ℕ) :
    ballot n (j + 1) = (n.choose (j + 1) : ℤ) - (n.choose j : ℤ) := rfl

/-- **The ballot recursion — the engine.** `m_{j+1}(n+1) = m_{j+1}(n) + m_j(n)`.

Two cases, each Pascal. The `j = 0` case is the one that would break under a
naive uniform definition: `m_1(n+1) = n` while `m_1(n) + m_0(n) = (C(n,1) − 1) + 1`,
and those agree only because `m_0` was pinned to `1` rather than computed. -/
theorem ballot_succ_succ (n j : ℕ) :
    ballot (n + 1) (j + 1) = ballot n (j + 1) + ballot n j := by
  cases j with
  | zero =>
      -- `Nat.choose_one_right` does not fire under `simp only` here: the term is
      -- `(1 + n).choose 1`, not `(n + 1).choose 1`. Full `simp` normalises it.
      simp [ballot, Nat.choose_one_right]
  | succ k =>
      simp only [ballot_succ]
      push_cast [Nat.choose_succ_succ n (k + 1), Nat.choose_succ_succ n k]
      ring

/-- **The boundary vanishing: `m_{j+1}(2j+1) = 0`.**

`C(2j+1, j+1) = C(2j+1, j)` by binomial symmetry, so the ballot number just past
the diagonal is zero. Small, and it is precisely what makes G2's induction close
in the even case.

**Why it is the crux.** Running `[2]ⁿ⁺¹ = [2]·Σ_j m_j(n)[n−2j+1]` through the
three-term recursion and reindexing produces a sum over `j = 0 … ⌊n/2⌋ + 1`,
while the target for `n+1` runs to `⌊(n+1)/2⌋`. Those agree when `n` is odd. When
`n` is even, say `n = 2m`, the derived sum has one term too many — at
`j = m + 1`, with coefficient `m_{m+1}(2m+1)`. This lemma says that coefficient
is `0`, so the extra term disappears and the two sums coincide.

So the parity split in G2 is not an artefact of a clumsy index choice; it is
real, and this is the fact that resolves it. -/
theorem ballot_boundary_zero (j : ℕ) : ballot (2 * j + 1) (j + 1) = 0 := by
  have hle : j + 1 ≤ 2 * j + 1 := by omega
  have hsub : 2 * j + 1 - (j + 1) = j := by omega
  have hsymm : (2 * j + 1).choose j = (2 * j + 1).choose (j + 1) := by
    have h := Nat.choose_symm hle
    rwa [hsub] at h
  simp [ballot_succ, hsymm]

/-- The first column is all ones: `m_0(n) = 1`, the single tableau of shape `(n)`. -/
theorem ballot_zero_eq_one (n : ℕ) : ballot n 0 = 1 := rfl

/-- `m_1(n) = n − 1` for `n ≥ 1`: the shape `(n−1, 1)` has `n − 1` standard
fillings. Stated on `ℤ` so the `n = 0` case needs no side condition. -/
theorem ballot_one (n : ℕ) : ballot n 1 = (n : ℤ) - 1 := by
  simp [ballot, Nat.choose_one_right]

/-- **The row sums that the folio actually uses**, checked against the values
`qou-8iru` measured: the two-row Specht dimensions at `n = 3, 4, 5` are
`(1,2)`, `(1,3,2)` and `(1,4,5)`, whose squares sum to `5`, `14` and `42`. -/
theorem ballot_values_three : ballot 3 0 = 1 ∧ ballot 3 1 = 2 := by
  refine ⟨rfl, ?_⟩; decide

theorem ballot_values_four :
    ballot 4 0 = 1 ∧ ballot 4 1 = 3 ∧ ballot 4 2 = 2 := by
  refine ⟨rfl, ?_, ?_⟩ <;> decide

theorem ballot_values_five :
    ballot 5 0 = 1 ∧ ballot 5 1 = 4 ∧ ballot 5 2 = 5 := by
  refine ⟨rfl, ?_, ?_⟩ <;> decide

/-- **G5 at the levels the folio has measured.** `Σ_j m_j(n)² = catalan n` for
`n = 3, 4, 5`, against Mathlib's own `catalan` rather than a table in this repo.

These three are now **corollaries** of `ballot_sq_sum_catalan` below, which
proves the identity for general `n`. They are kept, and kept proved by
`norm_num` on the literal values rather than by specialising the general
theorem, precisely so that they remain an independent check on it: a sign or
index error in the general proof would have to reproduce these three numbers by
coincidence to survive.

Historical note, since the pricing was wrong twice. `qou-u2jg` called this "pure
combinatorics, no q", as though easy; `qou-0cyu` corrected that to "by RSK, and
Mathlib has neither RSK nor pattern avoidance — LARGE", offering a direct
induction on `ballot_succ_succ` as route (b). Route (b) does not close either
(the ballot recursion is linear, the Catalan recursion is a convolution). What
closes it is reflection plus Vandermonde, with no induction and no tableau. -/
theorem ballot_sq_sum_catalan_small :
    ballot 3 0 ^ 2 + ballot 3 1 ^ 2 = (catalan 3 : ℤ) ∧
    ballot 4 0 ^ 2 + ballot 4 1 ^ 2 + ballot 4 2 ^ 2 = (catalan 4 : ℤ) ∧
    ballot 5 0 ^ 2 + ballot 5 1 ^ 2 + ballot 5 2 ^ 2 = (catalan 5 : ℤ) := by
  refine ⟨?_, ?_, ?_⟩ <;>
    norm_num [ballot, catalan_eq_centralBinom_div, Nat.centralBinom, Nat.choose]

/-! ## G5 for general `n`: `Σ_j m_j(n)² = catalan n`

**Bean `qou-0cyu` item G5, closed.** The bean priced this as needing RSK
("321-avoiding permutations are Catalan"), noted that Mathlib has neither RSK
nor pattern avoidance, and offered two routes: (a) formalise enough RSK —
LARGE; (b) a direct induction on `ballot_succ_succ`.

Neither is what closes it. Route (b) does not in fact close: the ballot
recursion `m_{j+1}(n+1) = m_{j+1}(n) + m_j(n)` is *linear*, while the Catalan
recursion `C_{n+1} = Σ_i C_i C_{n-i}` is a *convolution*, and squaring the
former produces cross terms `2 Σ_j m_j m_{j-1}` that the latter has no place
for. The two recursions do not match, which is exactly why G2 (linear in the
`m_j`) succumbs to induction and G5 does not.

What closes it is a **third route with no induction at all**: reflection plus
Vandermonde. The three moving parts:

1. **Run the sum over the full range** `k = 0 … n+1` rather than `k = 0 … ⌊n/2⌋`.
   Over the full range the summand is a difference of two binomials, and
   Vandermonde evaluates each of the three resulting sums in closed form:
   `Σ_k m_k(n)² = 2·C(2n,n) − 2·C(2n,n+1)` (`ballot_sq_sum_full`).

2. **`catalan n = C(2n,n) − C(2n,n+1)`** (`catalan_eq_choose_sub`), from
   Mathlib's `succ_mul_catalan_eq_centralBinom` together with
   `Nat.choose_succ_right_eq`, by cancelling `n+1`.

3. **Fold the full range in half.** `m_{n+1−k}(n) = −m_k(n)`
   (`ballot_reflect`), so the squares are symmetric about `k = (n+1)/2` and the
   full sum is exactly twice the half sum (`ballot_sq_sum_fold`). The fold has a
   fixed point precisely when `n` is odd, and there the summand vanishes — which
   is `ballot_boundary_zero` above, already proved for G2's parity split. The
   same lemma resolves both.

So G5 is a finite binomial identity, not a combinatorial bijection, and every
ingredient is in Mathlib at the pinned rev. Nothing here needs a tableau.

**Why this matters downstream.** The Gram form of the Markov trace is diagonal
in the Wedderburn basis with entries proportional to `y_λ`, and `y_λ = 0 ↔
ℓ(λ) > r` at Wenzl level `r`. Convention D is level `r = 2`, so

    dim radical = n! − Σ_{ℓ(λ) ≤ 2} (dim V_λ)²

and the two-row Specht dimension is `f^{(n-k,k)} = C(n,k) − C(n,k−1) = m_k(n)`.
`ballot_sq_sum_catalan` therefore turns `corank(n) = n! − catalan n` from four
measured values (`n = 3,4,5,6 → 1, 10, 78, 588`) into a general-`n` statement.
See `QOU.QBeta.MarkovGramDegenerate` for the wiring, and
`computations/probes/two_row_ballot_catalan_reduction.py` for the numerical
check of the reduction (`n ≤ 14`, hook length formula against full partition
enumeration).
-/

/-- **Vandermonde, range form.** `Σ_{k ≤ n} C(n,k)² = C(2n,n)`.

`Nat.add_choose_eq` gives this over `Finset.antidiagonal`; the work is
transporting it to `Finset.range` and applying `Nat.choose_symm` to turn
`C(n, n−k)` into `C(n,k)`. -/
theorem choose_sq_sum (n : ℕ) :
    ∑ k ∈ Finset.range (n + 1), n.choose k * n.choose k = (2 * n).choose n := by
  have h : (2 * n) = n + n := by ring
  rw [h, Nat.add_choose_eq, Finset.Nat.sum_antidiagonal_eq_sum_range_succ_mk]
  refine Finset.sum_congr rfl ?_
  intro k hk
  have hkn : k ≤ n := by
    simpa [Nat.lt_succ_iff] using Finset.mem_range.mp hk
  rw [Nat.choose_symm hkn]

/-- **Vandermonde, off-diagonal range form.** `Σ_{j ≤ n} C(n,j+1)·C(n,j) = C(2n,n+1)`.

Same transport as `choose_sq_sum`, with one extra step: the `k = 0` term of the
antidiagonal sum is `C(n,0)·C(n,n+1) = 0`, and peeling it is what shifts the
index so that `C(n, n+1−k)` becomes `C(n, j)` against `C(n, j+1)`. -/
theorem choose_mul_succ_sum (n : ℕ) :
    ∑ j ∈ Finset.range (n + 1), n.choose (j + 1) * n.choose j = (2 * n).choose (n + 1) := by
  have h : (2 * n) = n + n := by ring
  rw [h, Nat.add_choose_eq, Finset.Nat.sum_antidiagonal_eq_sum_range_succ_mk]
  conv_rhs => rw [Nat.succ_eq_add_one, Finset.sum_range_succ']
  have hlast : n.choose 0 * n.choose (n + 1 - 0) = 0 := by
    simp [Nat.choose_succ_self]
  rw [hlast, add_zero]
  refine Finset.sum_congr rfl ?_
  intro i hi
  have hin : i ≤ n := by
    simpa [Nat.lt_succ_iff] using Finset.mem_range.mp hi
  have hidx : n + 1 - (i + 1) = n - i := by omega
  rw [hidx, Nat.choose_symm hin]

/-- **The shifted square-sum**, `Σ_{j ≤ n} C(n,j+1)² + 1 = C(2n,n)`.

Both sides are the same range-`(n+2)` sum read two ways: peeling the *last*
term (`C(n,n+1)² = 0`) reduces it to `choose_sq_sum`, and peeling the *first*
(`C(n,0)² = 1`) reduces it to the shifted sum. Stated in `ℕ` with the `+ 1` on
the left so that no truncated subtraction appears. -/
theorem choose_sq_sum_shift (n : ℕ) :
    (∑ j ∈ Finset.range (n + 1), n.choose (j + 1) * n.choose (j + 1)) + 1
      = (2 * n).choose n := by
  have hbig : ∑ k ∈ Finset.range (n + 2), n.choose k * n.choose k = (2 * n).choose n := by
    rw [Finset.sum_range_succ, choose_sq_sum]
    simp [Nat.choose_succ_self]
  rw [← hbig, Finset.sum_range_succ' (fun k => n.choose k * n.choose k) (n + 1)]
  simp

/-- **`catalan n = C(2n,n) − C(2n,n+1)`**, over `ℤ`.

Written with `C(2n, n+1)` rather than the more familiar `C(2n, n−1)`. The two
are equal by binomial symmetry, but `n+1` involves no truncated `ℕ`
subtraction, so this form is correct at `n = 0` as well (`1 − 0 = 1 = catalan 0`)
and needs no side condition. The `n−1` spelling would give `C(0,0) − C(0,0) = 0`
there — the same off-by-one that `ballot` itself is defined to avoid.

Proof: `(n+1)·catalan n = C(2n,n)` is Mathlib's
`succ_mul_catalan_eq_centralBinom`, and `(n+1)·C(2n,n+1) = n·C(2n,n)` is
`Nat.choose_succ_right_eq` at `k = n`. Subtract and cancel `n+1 ≠ 0`. -/
theorem catalan_eq_choose_sub (n : ℕ) :
    (catalan n : ℤ) = ((2 * n).choose n : ℤ) - ((2 * n).choose (n + 1) : ℤ) := by
  have hc : ((n : ℤ) + 1) * (catalan n : ℤ) = ((2 * n).choose n : ℤ) := by
    have := succ_mul_catalan_eq_centralBinom n
    have h2 : Nat.centralBinom n = (2 * n).choose n := rfl
    rw [h2] at this
    exact_mod_cast congrArg (fun m : ℕ => (m : ℤ)) this
  have hstep : ((2 * n).choose (n + 1) : ℤ) * ((n : ℤ) + 1)
      = ((2 * n).choose n : ℤ) * (n : ℤ) := by
    have := Nat.choose_succ_right_eq (2 * n) n
    have h2 : 2 * n - n = n := by omega
    rw [h2] at this
    exact_mod_cast congrArg (fun m : ℕ => (m : ℤ)) this
  have hne : ((n : ℤ) + 1) ≠ 0 := by positivity
  apply mul_left_cancel₀ hne
  rw [hc]
  ring_nf
  ring_nf at hstep
  linarith

/-- **The full-range square-sum: `Σ_{k=0}^{n+1} m_k(n)² = 2·catalan n`.**

This is the step that makes G5 a closed-form evaluation rather than an
induction. Over the *full* range the summand expands as
`C(n,k+1)² − 2·C(n,k+1)·C(n,k) + C(n,k)²`, and Vandermonde evaluates all three
pieces: `C(2n,n) − 1`, `C(2n,n+1)`, and `C(2n,n)`. The stray `−1` is cancelled
exactly by the `k = 0` term `m_0(n)² = 1`, which is peeled off separately
because `m_0` is pinned rather than computed. What remains is
`2·(C(2n,n) − C(2n,n+1))`, and `catalan_eq_choose_sub` identifies that as
`2·catalan n`. -/
theorem ballot_sq_sum_full (n : ℕ) :
    ∑ k ∈ Finset.range (n + 2), (ballot n k) ^ 2 = 2 * (catalan n : ℤ) := by
  have h1 : ∑ j ∈ Finset.range (n + 1), ((n.choose j : ℤ)) ^ 2
      = ((2 * n).choose n : ℤ) := by
    have hc := congrArg (fun m : ℕ => (m : ℤ)) (choose_sq_sum n)
    push_cast at hc
    simpa [sq] using hc
  have h2 : ∑ j ∈ Finset.range (n + 1), ((n.choose (j + 1) : ℤ)) ^ 2
      = ((2 * n).choose n : ℤ) - 1 := by
    have hc := congrArg (fun m : ℕ => (m : ℤ)) (choose_sq_sum_shift n)
    push_cast at hc
    have hsum : ∑ j ∈ Finset.range (n + 1), ((n.choose (j + 1) : ℤ)) ^ 2 + 1
        = ((2 * n).choose n : ℤ) := by simpa [sq] using hc
    linarith
  have h3 : ∑ j ∈ Finset.range (n + 1), ((n.choose (j + 1) : ℤ)) * (n.choose j : ℤ)
      = ((2 * n).choose (n + 1) : ℤ) := by
    have hc := congrArg (fun m : ℕ => (m : ℤ)) (choose_mul_succ_sum n)
    push_cast at hc
    simpa using hc
  have key : ∑ j ∈ Finset.range (n + 1), (ballot n (j + 1)) ^ 2
      = (∑ j ∈ Finset.range (n + 1), ((n.choose (j + 1) : ℤ)) ^ 2)
        - 2 * (∑ j ∈ Finset.range (n + 1), ((n.choose (j + 1) : ℤ)) * (n.choose j : ℤ))
        + (∑ j ∈ Finset.range (n + 1), ((n.choose j : ℤ)) ^ 2) := by
    rw [Finset.mul_sum, ← Finset.sum_sub_distrib, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl ?_
    intro j _
    rw [ballot_succ]
    ring
  rw [Finset.sum_range_succ' (fun k => (ballot n k) ^ 2) (n + 1), key, h1, h2, h3,
    catalan_eq_choose_sub]
  simp only [ballot_zero]
  ring

/-- **The reflection: `m_{n+1−k}(n) = −m_k(n)` for `k ≤ n+1`.**

Binomial symmetry, read on the difference: `C(n,n+1−k) − C(n,n−k)` is
`C(n,k−1) − C(n,k)`. The two boundary cases are the ones the uniform argument
misses — `k = 0` (where `m_0 = 1` is pinned and `m_{n+1} = −C(n,n) = −1` is
computed) and `k = n+1` (the mirror of the same pair) — so both are discharged
separately.

This is what halves the full-range sum. It also explains the shape of
`ballot_boundary_zero`: an odd `n` puts a fixed point at `k = (n+1)/2`, where
the reflection forces `m_k = −m_k`. -/
theorem ballot_reflect (n k : ℕ) (hk : k ≤ n + 1) :
    ballot n (n + 1 - k) = - ballot n k := by
  cases k with
  | zero =>
      have hz : n + 1 - 0 = n + 1 := by omega
      rw [hz, ballot_succ, ballot_zero]
      simp [Nat.choose_succ_self, Nat.choose_self]
  | succ j =>
      have hjn : j ≤ n := by omega
      have hidx : n + 1 - (j + 1) = n - j := by omega
      rw [hidx]
      rcases Nat.eq_or_lt_of_le hjn with heq | hlt
      · subst heq
        have h0 : j - j = 0 := by omega
        rw [h0, ballot_zero, ballot_succ]
        simp [Nat.choose_succ_self, Nat.choose_self]
      · obtain ⟨m, hm⟩ : ∃ m, n - j = m + 1 := ⟨n - j - 1, by omega⟩
        rw [hm, ballot_succ, ballot_succ]
        have e1 : n.choose (m + 1) = n.choose j := by
          have hmj : m + 1 = n - j := hm.symm
          rw [hmj, Nat.choose_symm hjn]
        have e2 : n.choose m = n.choose (j + 1) := by
          have hj1 : j + 1 ≤ n := by omega
          have hmj : m = n - (j + 1) := by omega
          rw [hmj, Nat.choose_symm hj1]
        rw [e1, e2]
        ring

/-- **The fold: the full-range sum is exactly twice the half-range sum.**

Split `range (n+2)` at `⌊n/2⌋ + 1`, reindex the tail to start at `0`, reverse
it with `Finset.sum_range_reflect`, and apply `ballot_reflect` term by term: the
tail becomes `Σ_{j < n+1−⌊n/2⌋} m_j(n)²`, a *head* sum again.

The parity split is where the two cases genuinely differ, and it is not an
artefact of the index choice:

* `n = 2m`: the tail has length `m + 1 = ⌊n/2⌋ + 1`, matching the head exactly.
* `n = 2m+1`: the tail has length `m + 2`, one term too long. The excess term is
  `m_{m+1}(2m+1)²`, and `ballot_boundary_zero` says it vanishes.

So both cases give tail = head, hence full = 2·head. -/
theorem ballot_sq_sum_fold (n : ℕ) :
    ∑ k ∈ Finset.range (n + 2), (ballot n k) ^ 2
      = 2 * ∑ k ∈ Finset.range (n / 2 + 1), (ballot n k) ^ 2 := by
  set h := n / 2 with hh
  have hhn : h ≤ n := by omega
  have hsplit : (∑ k ∈ Finset.Ico 0 (h + 1), (ballot n k) ^ 2)
      + (∑ k ∈ Finset.Ico (h + 1) (n + 2), (ballot n k) ^ 2)
      = ∑ k ∈ Finset.Ico 0 (n + 2), (ballot n k) ^ 2 :=
    Finset.sum_Ico_consecutive _ (Nat.zero_le _) (by omega)
  rw [← Finset.range_eq_Ico] at hsplit
  have htail : ∑ k ∈ Finset.Ico (h + 1) (n + 2), (ballot n k) ^ 2
      = ∑ j ∈ Finset.range (n + 1 - h), (ballot n j) ^ 2 := by
    rw [Finset.sum_Ico_eq_sum_range]
    have hL : n + 2 - (h + 1) = n + 1 - h := by omega
    rw [hL]
    rw [← Finset.sum_range_reflect (fun j => (ballot n (h + 1 + j)) ^ 2) (n + 1 - h)]
    refine Finset.sum_congr rfl ?_
    intro j hj
    have hjr : j < n + 1 - h := Finset.mem_range.mp hj
    have hidx : h + 1 + (n + 1 - h - 1 - j) = n + 1 - j := by omega
    rw [hidx, ballot_reflect n j (by omega)]
    ring
  rw [htail] at hsplit
  rw [← hsplit]
  rcases Nat.even_or_odd n with he | ho
  · obtain ⟨m, hm⟩ := he
    have hhm : h = m := by omega
    have hlen : n + 1 - h = h + 1 := by omega
    rw [hlen]
    ring
  · obtain ⟨m, hm⟩ := ho
    have hhm : h = m := by omega
    have hlen : n + 1 - h = h + 1 + 1 := by omega
    rw [hlen, Finset.sum_range_succ (fun j => (ballot n j) ^ 2) (h + 1)]
    have hzero : ballot n (h + 1) = 0 := by
      rw [hhm, hm]
      exact ballot_boundary_zero m
    rw [hzero]
    ring

/-- **G5, general `n`: `Σ_{j ≤ ⌊n/2⌋} m_j(n)² = catalan n`.**

The two-row Specht dimensions squared sum to the Catalan number, for every `n`,
against Mathlib's own `catalan`. Equivalently — though the proof never uses the
equivalence — 321-avoiding permutations of `n` are counted by `C_n`.

Combined with the Wedderburn diagonalisation of the Markov-trace Gram form and
the Wenzl vanishing `y_λ = 0 ↔ ℓ(λ) > 2` in convention D, this gives
`corank(n) = n! − catalan n` for all `n`, superseding the four measured values.
The corank statement itself remains conditional on the Wenzl weight
identification, which is carried as a Lean class and is therefore invisible to
`#print axioms` (bean `qou-fpjy`); *this* theorem is unconditional. -/
theorem ballot_sq_sum_catalan (n : ℕ) :
    ∑ k ∈ Finset.range (n / 2 + 1), (ballot n k) ^ 2 = (catalan n : ℤ) := by
  have h := ballot_sq_sum_full n
  rw [ballot_sq_sum_fold n] at h
  linarith

end QOU.Mathlib
