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
harmlessly.

**`hg` is stated weighted, `d k * g k = d k * (f k + f (k+1))`, not as the bare
`g k = f k + f (k+1)`.** That is not stylistic. At the intended instance the bare
form is *false* at one index: when `2k = n+1` the branching identity degenerates
under ℕ truncation to `yw q n 0 = yw q (n+1) 1 + yw q (n+1) 0`, i.e. `0 = [1]_q /
[2]_q^{n+1}`, which is wrong rather than vacuous. What saves it is that the
dimension there is `0` — the shape `(n−k, k)` with `2k > n` does not exist — and
the lemma only ever uses the product. Weighting the hypothesis is exactly the
generality the proof already had. -/
theorem level_sum_step (N : ℕ) (d d' f g : ℕ → R)
    (hd0 : d' 0 = d 0)
    (hd : ∀ k ∈ range N, d' (k + 1) = d (k + 1) + d k)
    (hg : ∀ k ∈ range (N + 1), d k * g k = d k * (f k + f (k + 1)))
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

/-- **`yw q n 1 = yw q (n+1) 2`** — one level up, two steps along, same weight.

`[1]_q = 1` and `[2]_q` is exactly the factor each level of the tower divides
by, so the two cancel.

This is not decoration. In the `k`-indexing the branching hypothesis of
`level_sum_step` is `yw q n (n − 2k + 1) = yw q (n+1) (n − 2k + 2) + yw q (n+1) (n − 2k)`,
which is `yw_branching` at `m = n − 2k` **while `2k ≤ n`**. At the top index of
an odd level, `2k = n + 1` and the ℕ subtraction truncates `n − 2k` to `0`, so
the required identity degenerates to `yw q n 1 = yw q (n+1) 2 + yw q (n+1) 0`.
By `yw_zero` the second term drops, and this lemma says what is left is true —
so the hypothesis survives the truncation rather than being violated by it.

That is luck rather than design, and it is worth having as a named fact instead
of a coincidence rediscovered inside a proof. -/
theorem yw_one_succ (q : R) (hq : q - q⁻¹ ≠ 0) (hs : q + q⁻¹ ≠ 0) (n : ℕ) :
    TemperleyLiebTower.yw q n 1 = TemperleyLiebTower.yw q (n + 1) 2 := by
  -- `hq` is the denominator of `qint` and cannot be dropped: `[1]_q` is
  -- `(q − q⁻¹)/(q − q⁻¹)`, which is `1` only away from that zero.
  have h1 : TemperleyLiebTower.qint q 1 = 1 := by
    simp [TemperleyLiebTower.qint, div_self hq]
  have h2 : TemperleyLiebTower.qint q 2 = q + q⁻¹ := by
    unfold TemperleyLiebTower.qint
    rw [div_eq_iff hq]
    ring
  simp only [TemperleyLiebTower.yw, h1, h2]
  -- Deliberately NOT `field_simp`: under the variable exponent `n` it rewrites
  -- the base of `(q + q⁻¹) ^ n` and leaves two different bases at the same
  -- power, which `ring` cannot reconcile. TemperleyLiebTower says so at
  -- `mul_div_pow_succ`, which is the lemma to use instead.
  have h := TemperleyLiebTower.mul_div_pow_succ (q + q⁻¹) 1 hs n
  rw [mul_one] at h
  exact h.symm

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

/-- **`[1]_q = 1`.** The hypothesis cannot be dropped: `[1]_q` is literally
`(q − q⁻¹)/(q − q⁻¹)`. -/
theorem qint_one (q : R) (hq : q - q⁻¹ ≠ 0) : TemperleyLiebTower.qint q 1 = 1 := by
  simp [TemperleyLiebTower.qint, div_self hq]

/-- **The ballot number vanishes one past the end of the row**: `d(n,k) = 0`
whenever `2k = n + 1`.

For `n = 2j+1` the shape `(n−k, k)` with `k = j+1` would need `n ≥ 2k = n+1`, so
it does not exist, and the ballot number knows it: `C(n, j+1) = C(n, j)` by the
symmetry `n − (j+1) = j`, so the difference is zero.

This is the fact that rescues `hg` at the one index where the bare branching
identity fails — see `level_sum_step`. -/
theorem ballot_eq_zero_of_two_mul_eq_succ (n k : ℕ) (h : 2 * k = n + 1) :
    (ballot n k : R) = 0 := by
  obtain ⟨j, rfl⟩ : ∃ j, k = j + 1 := ⟨k - 1, by omega⟩
  have hn : n = 2 * j + 1 := by omega
  subst hn
  have hsymm := Nat.choose_symm (show j + 1 ≤ 2 * j + 1 by omega)
  rw [show 2 * j + 1 - (j + 1) = j from by omega] at hsymm
  simp [ballot, hsymm]

/-- **The level sum** `Σ_λ dim_λ · y_λ` over the two-row shapes of `n`.

Summed over the whole of `range (n + 1)` rather than over `k ≤ ⌊n/2⌋`, because
every off-shape term vanishes on its own — and this is what removes the parity
case-split the argument otherwise needs:

* at `2k = n + 1` the *dimension* is zero (`ballot_eq_zero_of_two_mul_eq_succ`);
* at `2k ≥ n + 2` the ℕ subtraction truncates the weight's argument to `0`, and
  the *weight* is zero (`yw_zero`).

Two different reasons, one uniform range. Taking instead the tight upper limit
`⌊(n+1)/2⌋` forces the two levels' shape counts apart whenever `n` is odd and
makes the boundary hypothesis hold for a different reason in each parity. -/
noncomputable def levelSum (q : R) (n : ℕ) : R :=
  ∑ k ∈ range (n + 1), ballot n k * TemperleyLiebTower.yw q n (n + 1 - 2 * k)

/-- **The level sum does not depend on the level.**

This is `level_sum_step` at `N = n + 1`, with the ballot numbers for the
dimensions and `yw` for the weights: Pascal supplies `hd`, `yw_branching`
supplies `hg`, and `yw_zero` supplies `hbdry`.

`hg` splits into exactly three cases, and only the first is mathematics:

* `2k ≤ n` — the branching identity itself, at `m = n − 2k`;
* `2k = n + 1` — the dimension is zero, so the (false) identity is never used;
* `2k ≥ n + 2` — every argument truncates to `0`, so all three weights vanish
  and the identity reads `0 = 0 + 0`. -/
theorem levelSum_succ (q : R) (hq : q ≠ 0) (hs : q + q⁻¹ ≠ 0) (n : ℕ) :
    levelSum q (n + 1) = levelSum q n := by
  have key := level_sum_step (R := R) (n + 1) (ballot n) (ballot (n + 1))
      (fun k => TemperleyLiebTower.yw q (n + 1) (n + 1 + 1 - 2 * k))
      (fun k => TemperleyLiebTower.yw q n (n + 1 - 2 * k))
      rfl
      (fun k _ => ballot_pascal n k)
      (fun k _ => by
        rcases lt_trichotomy (2 * k) (n + 1) with hlt | heq | hgt
        · -- `2k ≤ n`: the branching identity, at `m = n − 2k`.
          have h1 : n + 1 - 2 * k = (n - 2 * k) + 1 := by omega
          have h2 : n + 1 + 1 - 2 * k = (n - 2 * k) + 2 := by omega
          have h3 : n + 1 + 1 - 2 * (k + 1) = n - 2 * k := by omega
          simp only [h1, h2, h3]
          rw [TemperleyLiebTower.yw_branching q hq hs n (n - 2 * k)]
        · -- `2k = n + 1`: no such shape, so the dimension kills the term.
          rw [ballot_eq_zero_of_two_mul_eq_succ (R := R) n k heq]
          ring
        · -- `2k ≥ n + 2`: every argument truncates to `0`.
          have h1 : n + 1 - 2 * k = 0 := by omega
          have h2 : n + 1 + 1 - 2 * k = 0 := by omega
          have h3 : n + 1 + 1 - 2 * (k + 1) = 0 := by omega
          simp only [h1, h2, h3, yw_zero]
          ring)
      (by
        have h : n + 1 + 1 - 2 * (n + 1 + 1) = 0 := by omega
        simp only [h, yw_zero, mul_zero])
  -- The upper sum is `levelSum q (n+1)` on the nose; the lower one carries a
  -- single extra index `k = n+1`, whose weight argument truncates to `0`.
  rw [levelSum, levelSum, key, Finset.sum_range_succ]
  have h : n + 1 - 2 * (n + 1) = 0 := by omega
  simp only [h, yw_zero, mul_zero, add_zero]

/-- **The bottom of the tower.** One shape, dimension `1`, weight `[1]_q/[2]_q⁰`. -/
theorem levelSum_zero (q : R) (hq : q - q⁻¹ ≠ 0) : levelSum q 0 = 1 := by
  simp [levelSum, ballot, TemperleyLiebTower.yw, qint_one q hq]

/-- **`Σ_λ dim_λ · y_λ = 1` at every `n`** — the normalisation `tr(1) = 1` for
the two-row weights, at general `n`.

This is what the file was for. Until now the identity existed only as the two
explicit instances `qdim_normalisation_three` and `qdim_normalisation_four`, with
`n = 2 … 8` checked numerically in sympy; the general statement was asserted from
those. It is now proved, for every `n`, from `yw_branching` and Pascal.

The hypotheses are the standing non-degeneracy of the q-integers: `q ≠ 0`,
`q ≠ q⁻¹` (else `[m]_q` is `0/0`), and `q ≠ −q⁻¹` (else `[2]_q = 0` and the
tower divides by zero). At the substrate anchor `q₀ ≈ 1.11` all three hold. -/
theorem levelSum_eq_one (q : R) (hq : q ≠ 0) (hq' : q - q⁻¹ ≠ 0)
    (hs : q + q⁻¹ ≠ 0) (n : ℕ) : levelSum q n = 1 := by
  induction n with
  | zero => exact levelSum_zero q hq'
  | succ m ih => rw [levelSum_succ q hq hs m]; exact ih

end QOU.QBeta.TwoRowNormalisation
