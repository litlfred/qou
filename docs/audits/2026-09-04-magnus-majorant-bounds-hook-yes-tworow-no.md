# Bounding the positive majorant: the hook column closes, the two-row route does not (qou-o6ov)

**Date:** 2026-09-04
**Scope:** scope-(a); one derived positive + one clean negative; nothing wired.
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

## 2. Two-row column — positivity gives a valid bound that is useless

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
is a **valid bound that is useless for the decay theorem**, and the difference structure #6525
identified remains the obstacle after all: positivity makes dropping the term *legal*, not
*affordable*.

**Scope-(a):** this excludes the drop-the-subtracted-sector route as stated. It does not exclude a
two-row bound that keeps the difference (e.g. via the sl₂ lowering intertwiner `W_{k−1} ↪ W_k`, so
the difference is a trace on the cokernel) — that is untried.

## Honest limits

A = 2 and 3 throughout. The hook monotonicity and the two-row non-monotonicity are both measured on
those two sizes, not proved. `Ř` symmetry and the sector identity for `X*X` are exact algebra facts
at the sizes checked. Nothing wired; no witness.

## Bottom line

The positive majorant `tr_λ(X*X)` closes the **hook** column: a derived, monotone, per-dimension
bound reducing the decay to the Burau moduli. It does **not** close the **two-row** column by the
obvious route — positivity legalises dropping the subtracted sector, but the resulting bound stops
decaying (slack 1.0 → 10.5) because the lower sectors accumulate. The two-row obstacle is still the
difference structure, and a bound that keeps it is the open route.
