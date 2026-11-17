---
# qou-f1qs
title: 'Lean: general-n normalisation and indexing for the two-row weights (yw_branching is done)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T17:54:39Z
updated_at: 2026-11-17T12:24:25Z
parent: qou-0cyu
---


## State of play — check this before re-deriving anything

`QOU/QBeta/TemperleyLiebTower.lean` already contains, sorry-free:

| decl | what it gives | scope |
|---|---|---|
| `qint q m` | `[m]_q = (qᵐ − q⁻ᵐ)/(q − q⁻¹)` | def |
| `yw q n m` | `[m]_q / [2]_qⁿ`, the two-row weight with `m = n − 2k + 1` | def |
| `qint_three_term` | `[m+2] + [m] = [2]·[m+1]` | **all m** |
| `yw_branching` | `yw(n+1)(m+2) + yw(n+1)(m) = yw(n)(m+1)` | **all n, m** |
| `yw_pos`, `yw_nonneg` | positivity | all n, m |
| `conventionD_kills_antisymmetriser` | `z = z_D` iff the antisymmetriser dies | **n = 3 only** (scalar args `y₃ y₂₁ y₁₃`) |
| `qdim_normalisation_three` / `_four` | `[2]³ = [4] + 2[2]`, and the n=4 analogue | **n = 3, 4 only** |

So the *mathematical* content of the branching recursion is done at general `n`.
The file's own docstring says what remains: *"the indexing: relating
`yw q (n+1) (m+2)` and `yw q (n+1) m` to the two ways of adding a box to a
two-row diagram … a bookkeeping step between `m = n − 2k + 1` and the `covers`
Finset, not a new mathematical fact."*

**Do not re-derive `yw_branching` by hand.** It was re-derived from scratch in
PR #4928 before anyone checked, and it was already there.

## What is genuinely missing

1. **General-`n` normalisation.** `Σ_{λ⊢n} dim_λ · y_λ = 1` exists only as the
   explicit `n = 3` and `n = 4` identities. Everything else is numerical
   (`n = 2..8`, sympy, PR #4928).
2. **The partition-indexing layer.** No `Finset` of two-row shapes, no
   box-addition map, no `dim`. Nothing connects `yw q n m` to a partition.
3. **General-`n` vanishing at `z_D`.** That every `ℓ(λ) ≥ 3` weight dies is
   proved at `n = 3` and *asserted* beyond it from the TL identification —
   which is itself measured (`qou-8iru`, n = 2..7, residual 1.34e-51), not
   proved.

## Proof strategy for (1) — worked out, just needs writing

Two-row shapes of `n` indexed by `k`, `λ = (n−k, k)`, weight `yw q n (n−2k+1)`,
dimension `d(n,k) = C(n,k) − C(n,k−1)` (the ballot / Catalan-triangle number).

**Dimension Pascal rule.** `d(n+1,k) = d(n,k) + d(n,k−1)`, since
`d(n,k) + d(n,k−1) = C(n,k) − C(n,k−2)` and
`d(n+1,k) = C(n+1,k) − C(n+1,k−1) = C(n,k) − C(n,k−2)` by Pascal twice.

**Weight branching, in the same index.** With `m = n − 2k`, `yw_branching` reads

    yw (n+1) (n−2k+2) + yw (n+1) (n−2k) = yw n (n−2k+1)

which is exactly "add a box to row 1" plus "add a box to row 2", the three-row
option contributing `0` by convention D.

**The induction.** Let `S(n) = Σ_k d(n,k) · yw q n (n−2k+1)`.

    S(n+1) = Σ_k [d(n,k) + d(n,k−1)] · yw(n+1)(n−2k+2)
           = Σ_k d(n,k)·yw(n+1)(n−2k+2)  +  Σ_k d(n,k)·yw(n+1)(n−2k)   [reindex k→k+1]
           = Σ_k d(n,k)·[ yw(n+1)(n−2k+2) + yw(n+1)(n−2k) ]
           = Σ_k d(n,k)·yw(n)(n−2k+1)                                   [yw_branching]
           = S(n)

so `S` is constant, and `S(1) = 1`. Uses nothing but `yw_branching` and Pascal.

## Known trap in the indexing

`d(n,k) = C(n,k) − C(n,k−1)` in **ℕ** truncates to `0` exactly when `(n−k,k)` is
not a partition, which is convenient — but the Pascal rule then FAILS at the
boundary. Worked counterexample: for `n` even and `k = n/2 + 1`,
`d(n+1,k) = d(n,k) + d(n,k−1) = 0 + d(n,n/2) ≠ 0`, while the shape
`(n+1−k, k)` needs `n+1 ≥ 2k = n+2` and does not exist. So the truncated-ℕ
definition and the Pascal rule cannot both be used naively; carry the
dimensions in `ℤ` (or cast to `R`) and bound the summation range explicitly, or
define the ballot numbers by their own recursion with the boundary built in.

## Close condition

`Σ_{λ⊢n} dim_λ · y_λ = 1` proved in Lean for all `n`, sorry-free, with the
two-row shapes and their dimensions indexed properly; and the `ℓ(λ) ≥ 3`
vanishing at `z_D` either proved for general `n` or explicitly downgraded to a
conditional class with the TL identification as its named hypothesis (§3b-cond),
rather than left as an unstated assumption.

---

## Progress (PR #4928)

`QOU/QBeta/TwoRowNormalisation.lean` — `level_sum_step`, sorry-free,
`#print axioms` = `[propext, Classical.choice, Quot.sound]`, verified with
`lean`-direct against its real import cone. It is the arithmetic core: given
Pascal for the dimensions and branching for the weights, the two level sums
agree.

Hypotheses `hd` and `hg` are **range-local**. They were universal in the first
draft and that is unusable — see the docstring; past `k = n/2` the ℕ
subtraction `n − 2k` truncates and a universal `hg` asserts a false q-integer
identity rather than a vacuous one.

## The parity split, worked out — this is what the instantiation turns on

The two sums in `level_sum_step` run over the **same** `range (N + 1)`, but
levels `n` and `n + 1` do not always carry the same number of two-row shapes:
level `n` has `⌊n/2⌋ + 1`, level `n+1` has `⌊(n+1)/2⌋ + 1`, and those differ
exactly when `n` is odd.

Take **`N := ⌊(n+1)/2⌋`**, the upper level's count. Then `hbdry`,
`d N * f (N + 1) = 0`, holds in both parities but *for different reasons*:

* **`n` odd.** `N = (n+1)/2` while the lower level stops at `(n−1)/2 = N − 1`,
  so `d N = 0` — there is no such shape downstairs. The boundary term dies on
  the dimension.
* **`n` even.** `N = n/2` and `d N ≠ 0`, so the weight must vanish instead:
  `f (N + 1) = yw q (n+1) (n − 2N) = yw q (n+1) 0`, and `[0]_q = 0` gives
  `yw q m 0 = 0`. The boundary term dies on the q-integer.

Both cases are already available: `qint` at `0` is definitionally `0`, and the
dimension vanishing is the statement that `(n−k, k)` is not a partition once
`2k > n`. Neither needs new mathematics — but the proof does need the case
split, and picking `N = ⌊n/2⌋` instead makes `hbdry` FALSE for odd `n`.

## Remaining, in order

1. Ballot dimensions as `ℕ → ℕ → R` (in `R`, per the truncation trap above),
   with Pascal proved on the valid range.
2. `hbdry` by the parity split above.
3. Instantiate `level_sum_step` with `f k = yw q (n+1) (n − 2k + 2)`,
   `g k = yw q n (n − 2k + 1)`, `hg` discharged by `yw_branching`.
4. Base case and induction to `Σ_λ dim_λ · y_λ = 1` for all `n`.
5. Separately: general-`n` vanishing for `ℓ(λ) ≥ 3` at `z_D`.

## Progress 2026-11-17 (Round 66 — PR #8340)

- Formalized in `folio/quantum-observable-universe/lean/QOU/Foundations/AddableCellRatioFakeDegreeTwoRowBallotWeightTensorPowerCharacterOrbitTrace.lean` (Lean 4.24.0, `0` `sorry`, `0` `axiom`, `0` warnings, `0` directory-mode static vacuity & borrowed-name advisories).
- 80-dps `mpmath` numerical witness stamped in `computations/probes/addable-cell-ratio-fake-degree-two-row-ballot-weight-tensor-power-character-orbit-trace.witness.json` (`scriptHash = 0309390e769d`, `scriptCommitSha = c43b700db42337a2547c8ff1e2a1665156dd27ea`, `HEAD = d46ecc77d14e0e9528cfc49310e88f4e88eb306a`).
- PR: https://github.com/litlfred/qou/pull/8340 (`ready: d46ecc77d14e0e9528cfc49310e88f4e88eb306a`).
