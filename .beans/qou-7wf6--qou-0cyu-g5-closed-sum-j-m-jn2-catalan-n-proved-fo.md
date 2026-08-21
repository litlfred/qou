---
# qou-7wf6
title: 'qou-0cyu G5 CLOSED: sum_j m_j(n)^2 = catalan n proved for general n by reflection + Vandermonde'
status: completed
type: task
created_at: 2026-08-21T15:41:24Z
updated_at: 2026-08-21T15:41:24Z
---

Branch `claude/tl-all-n-corank-2026-08-21`, PR #5360.

## What closed

`Σ_j m_j(n)² = catalan n` — bean `qou-0cyu` item **G5** — is proved for
general `n`, sorry-free, against Mathlib's own `catalan`.
`QOU.Mathlib.ballot_sq_sum_catalan` in
`content/quantum-observable-universe/lean/QOU/Mathlib/BallotNumbers.lean`.

Wired through actual hook-length SYT dimensions in the new
`QOU/Mathlib/TwoRowDimCatalan.lean` (`dimHLF_two_row_sq_sum`), and to the
corank statement as `QOU.QBeta.MarkovGramDegenerate.corank_general`, which
supersedes `corank_three` / `_four` / `_five` (those wrote their two-row block
dimensions out by hand and did not reach n = 6).

22 new declarations, all `[propext, Classical.choice, Quot.sound]`, no
`sorryAx`. `lean`-direct exit 0 against the real import cone; no `lake build`.

## Why both of qou-0cyu's prices for G5 were wrong

The bean priced G5 first as "pure combinatorics, easy" (`qou-u2jg`), then
corrected itself to "by RSK, and Mathlib has neither RSK nor pattern
avoidance — LARGE", offering a direct induction on `ballot_succ_succ` as
route (b) to try first.

Route (b) does not close. The ballot recursion is LINEAR; the Catalan
recursion is a CONVOLUTION; squaring the first leaves cross terms
`2 Σ_j m_j m_{j-1}` the second has no slot for. That is exactly why G2 —
linear in the `m_j` — does succumb to the same recursion and G5 does not.

What closes it is a third route the bean did not consider: reflection plus
Vandermonde, no induction, no tableau.

  1. run the sum over the FULL range k = 0..n+1, where Vandermonde
     (`Nat.add_choose_eq`) evaluates all three pieces:
     `Σ_k m_k(n)² = 2·C(2n,n) − 2·C(2n,n+1)`
  2. `catalan n = C(2n,n) − C(2n,n+1)` from
     `succ_mul_catalan_eq_centralBinom` + `Nat.choose_succ_right_eq`
  3. `m_{n+1−k}(n) = −m_k(n)` folds the full sum to twice the half sum

The fold's fixed point is at odd `n`, and the summand vanishes there — which
is `ballot_boundary_zero`, already proved for G2's parity split. One lemma
resolves both.

Every ingredient was already in Mathlib at the pinned rev. Nothing needed
adding.

## Two things the corpus already had

Recording these because in both cases the framing I was given assumed work
that was already done:

1. **The two-row reduction is proved, not merely checkable.**
   `QOU/Mathlib/SYTDimHLFPair.lean:29` — `dimHLF_pair` — proves
   `dimHLF [a,b] = C(a+b,b) − C(a+b,b−1)` sorry-free, with a docstring saying
   so. The numerical check I ran (`two_row_ballot_catalan_reduction.py`,
   n ≤ 14) still earns its place as an independent control, but the wiring is
   unconditional rather than numerically-supported.

2. **n = 7 and n = 8 were already computed.**
   `computations/probes/wenzl_level_two_vanishing.py` loops `range(1,9)` and
   `range(3,9)`. Re-ran it: exit 0, witness byte-identical,
   `[1, 10, 78, 588, 4611, 38890]`, with `y_λ = 0 ⟺ ℓ(λ) ≥ 3` verified
   symbolically over ℚ(q) for n = 1..8.

## What did NOT close, and what I would NOT claim

No Gram-rank measurement exists past n = 6. `corank_seven_value` /
`corank_eight_value` say "prediction" in their docstrings; do not cite them as
measurements. The n = 7 rank is 5040×5040 exact on an `O(n!²)`-to-build matrix.

Full record: `docs/audits/2026-08-21-all-n-corank-catalan.md`.
