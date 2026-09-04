# Bounding the positive majorant: both columns reduce; one lossy shortcut fails (qou-o6ov)

**Date:** 2026-09-04
**Scope:** scope-(a); two derived positives + one narrow negative; nothing wired.
**Correction (same day):** an earlier version of this doc, and PR #6587's first body, framed
the two-row column as failing. That was **too pessimistic and is retracted** — the two-row
reduction holds and is monotone; only the lossy shortcut (S) fails. Section 2 is rewritten.
**Probes:** [`magnus_hook_majorant_monotone_probe.py`](../../computations/deltalambda/magnus_hook_majorant_monotone_probe.py),
[`magnus_tworow_majorant_sector_probe.py`](../../computations/deltalambda/magnus_tworow_majorant_sector_probe.py)
**Follows:** #6573 (bound (B) for `Σ|eig|`), #6556 (the positive majorant `tr_λ(X*X)` and its hook closed form), #6525 (two-row sectors).

## 1. Hook column — the chain closes

Composing pieces each already derived:

```
Σ|eig(M_hook)|/dim ≤ √(B''_j/dim),   B''_j = c²·q^{T(1−j)}·Σ_{a,b} Σ_± e_j(|μ(word)|),  T = 2L+4
```

with **`B''_j/dim` strictly decreasing in `j = b(λ)` at A = 2 and A = 3**. Inputs: (B) by
Cauchy–Schwarz + Schur (#6573); the closed form by the common-twist expansion (#6556); `B''_j` by
`|e_j(μ)| ≤ e_j(|μ|)`, Lean-proved in `MagnusHookDecayBound`. Bound holds at every `j`; per-dim
tightness 0.159–0.238 (A=2), 0.0623–0.121 (A=3) — 4–16× loose, valid, monotone.

**Still input, not theorem:** the Burau moduli are measured. The chain *reduces* the hook decay to
them.

### Two errors of mine here, both caught by the probe's own output

- **A units bug.** My tightness column compared the *total* `Σ|eig|` against the *per-dim* bound,
  printing ratios up to 2.38 — which reads as a bound **violation** where there is none. The check
  now asserts `≤ 1` so the same slip fails loudly.
- **A wrong prediction.** I asserted the crude spectral-radius bound "will not do it". **It does**
  decay per dimension: the binomial divides back out, since `dim = C(n−1,j)` on a hook. Crude and
  sharp differ in *tightness* (3× at `j=1` to ~2000× at `j=8`), not monotonicity. I had carried
  #6520's precedent across, but that is about **raw** monotonicity — a different quantity.

## 2. Two-row column — the reduction holds and is monotone; only the shortcut fails

#6525 showed two-row irreps are carried exactly by up-spin sectors: for **any** algebra element,
`tr_{(n−k,k)}(g) = tr_{W_k}(g) − tr_{W_{k−1}}(g)`, and noted the *difference* structure blocks a
bound for the signed trace (a per-sector triangle inequality re-imports the previous sector).

**The majorant seemed to escape that.** `tr_λ(X*X) ≥ 0` for every λ, so every term of
`tr_{W_k}(X*X) = Σ_{k'≤k} tr_{(n−k',k')}(X*X)` is non-negative and the subtracted sector can be
dropped outright — no triangle inequality, no cancellation:

```
0 ≤ tr_{(n−k,k)}(X* X) = tr_{W_k}(X*X) − tr_{W_{k−1}}(X*X) ≤ tr_{W_k}(X* X)          (S)
```

**Confirmed, and cheap:** `Ř` is symmetric (measured, `max|R − Rᵀ| = 0.0`), so the sector matrices
are too and `tr_{W_k}(X*X) = ‖X|_{W_k}‖_F²` — a sum of squared entries on a `C(n,k)`-dim block of
the fixed 4×4 `Ř`, no eigenvalues, no seminormal construction. The sector identity holds for `X*X`
to `6.1e-139`, and **(S) holds at every `k`**.

**But it does not decay.** Per dimension:

| A | k = 1 | 2 | 3 | 4 | slack (bound ÷ actual) |
|---|---|---|---|---|---|
| 2 | 320.8 | 281.4 | **560.0** | — | 1.0, 2.73, 10.46 |
| 3 | 4718.6 | 4191.2 | 3856.1 | **5388.2** | 1.0, 1.50, 2.57, 5.49 |

`bound/dim_λ` **rises** at the last `k` at both sizes, and the slack grows monotonically — dropping
`tr_{W_{k−1}}` discards more and more as `k` climbs, because the lower sectors accumulate. So (S)
is a valid bound that is useless: positivity makes dropping the term *legal*, not *affordable*.

**But the reduction itself is fine, and this is the result.** Keep the difference and the two-row
column has exactly what the hook column has — an exact expression in the fixed 4×4 `Ř`, monotone
per dimension:

```
tr_{(n−k,k)}(X* X) = tr_{W_k}(X*X) − tr_{W_{k−1}}(X*X) = ‖X|_{W_k}‖_F² − ‖X|_{W_{k−1}}‖_F²
```

verified to `6.1e-139`, and **strictly decreasing per dimension in `k = b(λ)` at both sizes**:

| A | k = 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 2 | 320.78 | 103.15 | 53.56 | — |
| 3 | 4718.6 | 2793.1 | 1498.6 | 981.2 |

No seminormal construction, no eigenvalues — two Frobenius norms on `C(n,k)`-dim blocks. Keeping
the difference **costs nothing**, since it is exactly computable; the only thing lost is the
cosmetic simplification of dropping a term.

**Scope-(a):** the narrow negative is that the drop-the-subtracted-sector shortcut does not decay.
It says nothing against the two-row reduction, which holds.

## Honest limits

A = 2 and 3 throughout. The hook monotonicity and the two-row non-monotonicity are both measured on
those two sizes, not proved. `Ř` symmetry and the sector identity for `X*X` are exact algebra facts
at the sizes checked. Nothing wired; no witness.

## Bottom line

The positive majorant `tr_λ(X*X)` reduces **both** columns to small `n`-independent objects,
monotone per dimension in `b(λ)`: the **hook** column to the reduced Burau (`B''_j/dim` decreasing,
bound 4–16× loose), and the **two-row** column to a difference of two sector Frobenius norms of the
fixed 4×4 `Ř` (exact, decreasing). The one negative is narrow: dropping the subtracted sector to
simplify (S) is legal by positivity but too lossy (slack 1.0 → 10.5), so the difference must be
kept — which costs nothing.
