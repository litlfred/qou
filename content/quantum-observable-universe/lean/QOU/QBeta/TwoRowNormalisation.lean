import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Ring
import QOU.QBeta.TemperleyLiebTower

/-!
# The level sum is invariant, so the two-row weights normalise at every `n`

**Bean `qou-f1qs`.** Companion to `QOU.QBeta.TemperleyLiebTower`, which already
proves the analytic content at general `n`:

* `qint_three_term` — `[m+2]_q + [m]_q = [2]_q · [m+1]_q`
* `yw_branching`    — `yw (n+1) (m+2) + yw (n+1) m = yw n (m+1)`

both sorry-free, both for **all** `n` and `m`. What that file does *not* have,
and what this one supplies, is the step that turns the branching identity into a
statement about a whole level of the tower:

> `Σ_λ dim_λ · y_λ` does not depend on `n`.

Together with its value at the bottom of the tower that is the normalisation
`tr(1) = 1`, which until now existed only as the two explicit identities
`qdim_normalisation_three` (`[2]³ = [4] + 2[2]`) and `qdim_normalisation_four`.
Everything else was numerical — sympy, `n = 2 … 8`, PR #4928.

## The shape of the argument

Two-row shapes of `n` are indexed by `k`, with `λ = (n−k, k)`, weight
`yw q n (n−2k+1)` and dimension the ballot number
`d(n,k) = C(n,k) − C(n,k−1)`. Two facts drive everything:

* **dimensions satisfy Pascal**, `d(n+1,k) = d(n,k) + d(n,k−1)`, because
  `d(n,k) + d(n,k−1) = C(n,k) − C(n,k−2)` and `d(n+1,k)` is the same after
  applying Pascal twice;
* **weights branch**, and in this index `yw_branching` reads exactly "add a box
  to row 1" plus "add a box to row 2", with the three-row option contributing
  `0` — which is not an omission but the *definition* of convention D.

Feeding the first into the second and reindexing collapses the level sum at
`n+1` to the one at `n`.

## Why the core lemma is abstract

`level_sum_step` below is stated for arbitrary families `d`, `d'`, `f`, `g`
satisfying the two recursions, not for `Nat.choose` and `yw`. That is
deliberate. The arithmetic is pure reindexing and has nothing to do with
q-integers; stating it concretely would tangle the summation bookkeeping with
`qint` rewriting, and the bookkeeping is where the difficulty actually is.

## The boundary hypothesis is load-bearing, not a technicality

`level_sum_step` assumes `d N * f (N + 1) = 0`. It cannot be dropped: the
reindexed sum genuinely differs from the target by exactly that term. It is the
formal content of "there is no shape past the end of the row", and it is where
a naive treatment goes wrong.

Concretely — recorded because it is an easy trap. Defining `d(n,k)` as
`Nat.choose n k - Nat.choose n (k-1)` in **ℕ** looks attractive, because
truncating subtraction sends `d` to `0` exactly when `(n−k, k)` fails to be a
partition. But the Pascal rule then breaks at the boundary: for `n` even and
`k = n/2 + 1`, the rule would give `d(n+1,k) = 0 + d(n,n/2) ≠ 0`, while the
shape `(n+1−k, k)` needs `n+1 ≥ 2k = n+2` and does not exist. Truncated-ℕ
dimensions and the Pascal rule are not simultaneously usable. Carry the
dimensions in `R`.
-/

namespace QOU.QBeta.TwoRowNormalisation

open Finset

variable {R : Type*} [Field R]

/-- **The level sum is unchanged by one step of branching.**

`d'` is the dimension family one level up, obtained from `d` by Pascal; `f` is
the weight family one level up and `g` the one at the current level, related by
the branching `g k = f k + f (k+1)`.

The two sums are then equal. Read right to left: every shape at the lower level
distributes its dimension over the two shapes above it, and each upper shape
collects contributions from the (at most two) shapes below it — so the total is
carried up unchanged.

`hbdry` says the last dimension meets no shape above it. Without it the claim is
false, not merely unprovable: the reindexed sum exceeds the target by exactly
`d N * f (N + 1)`.

**`hd` and `hg` are range-local, and must be.** They were universally
quantified in the first version, which is unusable at the intended instance.
The weight family is `f k = yw q (n+1) (n − 2k + 2)`, and `hg` is exactly
`yw_branching` at `m = n − 2k` — but only while `n − 2k` is the intended
integer. Past `k = n/2` the **ℕ** subtraction `n − 2k` truncates to `0`, so the
universally-quantified hypothesis would assert
`yw (n+1) 2 + yw (n+1) 0 = yw n 1` for every large `k`, which is a different
(and false) claim about q-integers rather than a vacuous one. Off-shape indices
have to be excluded by the range, not by hoping the arithmetic degenerates
harmlessly. -/
theorem level_sum_step (N : ℕ) (d d' f g : ℕ → R)
    (hd0 : d' 0 = d 0)
    (hd : ∀ k ∈ range N, d' (k + 1) = d (k + 1) + d k)
    (hg : ∀ k ∈ range (N + 1), g k = f k + f (k + 1))
    (hbdry : d N * f (N + 1) = 0) :
    ∑ k ∈ range (N + 1), d' k * f k = ∑ k ∈ range (N + 1), d k * g k := by
  -- Right-hand side: split the branching, then peel the last term of the
  -- shifted sum so both sides run over `range N`.
  have hrhs : ∑ k ∈ range (N + 1), d k * g k
      = (∑ k ∈ range (N + 1), d k * f k)
        + ((∑ k ∈ range N, d k * f (k + 1)) + d N * f (N + 1)) := by
    rw [← Finset.sum_range_succ (fun k => d k * f (k + 1)) N, ← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun k hk => by rw [hg k hk]; ring
  -- Left-hand side: peel the FIRST term, so `hd` applies to every remaining one.
  have hlhs : ∑ k ∈ range (N + 1), d' k * f k
      = (∑ k ∈ range (N + 1), d k * f k) + ∑ k ∈ range N, d k * f (k + 1) := by
    rw [Finset.sum_range_succ' (fun k => d' k * f k) N,
        Finset.sum_range_succ' (fun k => d k * f k) N]
    have : ∀ k ∈ range N, d' (k + 1) * f (k + 1)
        = d (k + 1) * f (k + 1) + d k * f (k + 1) := by
      intro k hk; rw [hd k hk]; ring
    rw [Finset.sum_congr rfl this, Finset.sum_add_distrib, hd0]
    ring
  rw [hlhs, hrhs, hbdry, add_zero]

/-! ### The two ingredients `hbdry` needs

The boundary term `d N * f (N + 1)` dies for a *different* reason in each
parity, and both reasons are supplied here. See the bean `qou-f1qs` note: with
`N = ⌊(n+1)/2⌋` (the **upper** level's shape count),

* `n` odd — the lower level stops one shape earlier, so `d N = 0`;
* `n` even — `d N ≠ 0` but the weight above it is `yw q (n+1) 0`, which
  vanishes because `[0]_q = 0`.

Picking `N = ⌊n/2⌋` instead makes `hbdry` false for odd `n`. -/

/-- **`[0]_q = 0`**, hence the weight at argument `0` vanishes. This is what
kills the boundary term in the even case. -/
theorem qint_zero (q : R) : TemperleyLiebTower.qint q 0 = 0 := by
  simp [TemperleyLiebTower.qint]

/-- **`yw q n 0 = 0`.** The shape "one past the end of the row" carries no
weight, which is what `hbdry` asserts when `n` is even. -/
theorem yw_zero (q : R) (n : ℕ) : TemperleyLiebTower.yw q n 0 = 0 := by
  simp [TemperleyLiebTower.yw, qint_zero]

/-- The ballot / Catalan-triangle number `d(n,k) = dim` of the two-row irrep
`(n−k, k)`, carried in `R`.

Defined by cases on `k` rather than as `C(n,k) − C(n,k−1)` with truncating
subtraction: at `k = 0` that expression would read `C(n,0) − C(n,0) = 0`,
because `0 - 1 = 0` in `ℕ`, where the true dimension is `1`. -/
noncomputable def ballot (n : ℕ) : ℕ → R
  | 0 => 1
  | (k + 1) => (n.choose (k + 1) : R) - (n.choose k : R)

/-- **Pascal for the ballot numbers**, `d(n+1,k+1) = d(n,k+1) + d(n,k)`.

Two applications of Pascal's rule for binomials, and the `k = 0` case works out
because the two `−C(n,0)` terms cancel against the `+1` of `ballot n 0`. This
is the dimension half of `level_sum_step`'s `hd`. -/
theorem ballot_pascal (n k : ℕ) :
    ballot (n + 1) (k + 1) = ballot n (k + 1) + (ballot n k : R) := by
  cases k with
  | zero =>
      simp [ballot, Nat.choose_one_right]
  | succ j =>
      simp only [ballot, Nat.choose_succ_succ n (j + 1), Nat.choose_succ_succ n j]
      push_cast
      ring

end QOU.QBeta.TwoRowNormalisation
