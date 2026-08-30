---
# qou-hwtower
title: 'q-RH: Hasse-Weil now holds over every extension field, not just F_q'
status: completed
type: task
priority: medium
created_at: 2026-08-30T06:05:00Z
updated_at: 2026-08-30T06:05:00Z
---

The chapter proved `|∑ αᵢ| ≤ 2g√q` — the point-count bound over `𝔽_q` alone.
That is weaker than the theorem the chapter is named for. Hasse–Weil is a
statement about **every** finite extension: Frobenius on `𝔽_{q^r}` acts with
eigenvalues `αᵢ^r`, giving `| |ℬ(𝔽_{q^r})| − (q^r + 1) | ≤ 2g·q^{r/2}`.

Closed, because it is one or two lines from the magnitude bound already proved.
All in `hasse-weil-bound.lean`, all `#print axioms`
`[propext, Classical.choice, Quot.sound]`, file `lean`-direct exit 0:

- `norm_eigenvalue_pow` — `‖αᵢ^r‖ = (q^{1/2})^r`.
- `norm_sum_eigenvalue_pow_le` — `‖∑ αᵢ^r‖ ≤ 8·(q^{1/2})^r`.
- `sum_eigenvalue_pow_isReal` — the power sums are **real** at every level, via
  conjugation-closure (`conj` commutes with powers; the conjugation permutation
  reindexes the sum). Not decoration: `|ℬ(𝔽_{q^r})|` is an integer, so a power
  sum with a nonzero imaginary part would be an inconsistency, not a loose
  bound. `sum_eigenvalues_isReal` was the `r = 1` case.
- `norm_sum_eigenvalue_pow_tight` — **tightness, checked rather than assumed.**

## Why tightness needed its own check

A bound tight at `r = 1` can still be loose in the tower, and the *growth rate*
in `r` is the part of Hasse–Weil that does the work — a loose rate would leave
exactly that part unattested while the `r = 1` statement looked fine. Measured
on the supersingular witness (`q = 4`, all `αᵢ = 2`): power sum `8·2^r`, bound
`8·(4^{1/2})^r = 8·2^r`. Equality at every `r`.

## The r = 0 degeneracy, stated rather than excluded

At `r = 0` every `αᵢ^0 = 1`, the sum is `8`, the bound reads `8 ≤ 8`. True and
tight and carrying no arithmetic — `𝔽_{q^0}` is not a field. The theorems
quantify over all `r : ℕ` because excluding it buys nothing, but nothing
downstream should read the `r = 0` instance as a point count. Recorded at the
section docstring as well as here.

## What this is NOT

More of the **local** theory, which is the half that was never in doubt —
Hasse–Weil has held unconditionally at every place since 1948 while RH stayed
open. This does not move the arc toward RH; the adelic assembly step still
carries the whole distance (`conj:adelic-critical-line-persistence`). What it
closes is a gap between what the chapter proved and what it claimed the name of.
