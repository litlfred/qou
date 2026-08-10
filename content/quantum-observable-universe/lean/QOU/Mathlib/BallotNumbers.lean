import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Combinatorics.Enumerative.Catalan
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
  Catalan".

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

The general `n` is open and is *not* the easy combinatorial exercise
`qou-u2jg` first called it: by RSK it is the statement that 321-avoiding
permutations are counted by the Catalan numbers, and Mathlib has neither RSK nor
pattern avoidance. `ballot_succ_succ` above is the intended engine for a direct
induction that avoids RSK entirely — see `qou-0cyu` G5 route (b). -/
theorem ballot_sq_sum_catalan_small :
    ballot 3 0 ^ 2 + ballot 3 1 ^ 2 = (catalan 3 : ℤ) ∧
    ballot 4 0 ^ 2 + ballot 4 1 ^ 2 + ballot 4 2 ^ 2 = (catalan 4 : ℤ) ∧
    ballot 5 0 ^ 2 + ballot 5 1 ^ 2 + ballot 5 2 ^ 2 = (catalan 5 : ℤ) := by
  refine ⟨?_, ?_, ?_⟩ <;>
    norm_num [ballot, catalan_eq_centralBinom_div, Nat.centralBinom, Nat.choose]

end QOU.Mathlib
