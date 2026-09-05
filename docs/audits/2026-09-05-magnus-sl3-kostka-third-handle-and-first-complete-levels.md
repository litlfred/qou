# A third handle (`sl₃` weight sectors + Kostka inversion), and the first complete `b`-levels

**Date:** 2026-09-05 · **Bean:** `qou-o6ov` · **Scope:** (a) scope-limited — n = 6 and n = 9. Nothing wired, no witness, no fit.

## Why a third handle was needed — correcting my own stated plan

I had said the next step was to bound the envelope `max_{b(λ)=b} tr_λ(X*X)/dim_λ` from the two
closed forms already in hand (the reduced Burau on hooks, the sector difference on two-rows).
**That premise is false, and the data refuting it was already measured.** At A=3 the envelope is not
attained on a hook or a two-row at large `b`:

| b | envelope shape | per-dim | hook at same b | ratio |
|---|---|---|---|---|
| 6 | `(3,3,3)` | 211.56 | `(3,1⁶)` 14.319 | 15× |
| 7 | `(2,2,2,2,1)` | 31.56 | `(2,1⁷)` 0.4354 | 72× |

At large `b` the hook sits near the **minimum** of its level, not the maximum. So those two closed
forms cannot bound the envelope at all; a handle reaching the **fat** shapes is required.

## The construction, which subsumes both existing handles

`(ℂ^k)^⊗n = ⊕_λ S^λ(ℂ^k) ⊗ M^λ`, with the Hecke algebra acting only on `M^λ`. The `μ`-weight space
of `S^λ(ℂ^k)` has dimension `K_{λμ}` (Kostka), so for **any** algebra element `g`:

```
tr_{W_μ}(g) = Σ_λ K_{λμ} · χ_λ(g),        λ ⊢ n with at most k rows           (K)
```

`K` is unitriangular in dominance (`K_{λλ} = 1`, `K_{λμ} = 0` unless `λ ⊵ μ`), so (K) **inverts**:
every `χ_λ` with ≤ k rows follows from weight-sector traces.

#6525's two-row difference `tr_{(n−k,k)} = tr_{W_k} − tr_{W_{k−1}}` is exactly the **k=2 case** of
this inversion, not a separate device. The probe *demonstrates* that instead of asserting it, by
checking the k=3 route against the k=2 one on every two-row shape.

`Ř` still acts on adjacent pairs, so #6710's sparse column-wise kernel carries over with only the
local rule changed: `a==b → q`, `a<b → (q−q⁻¹)·same + swapped`, `a>b → swapped`.

## Two gates, deliberately sharing no code

**1. The Kostka matrix alone.** `multinomial(n; μ) = Σ_λ K_{λμ}·f^λ` — `dim W_μ` counted two ways,
touching **no trace code**. Exact at n = 6, 9 and 12. A bug in `K` therefore cannot hide behind a
bug in the kernel, or the reverse.

**2. n=6 is a complete gate** — all 7 of its ≤3-row shapes against the direct seminormal trace,
*plus* the Burau closed form on the 3 hooks and the `sl₂` sector difference on the 4 two-rows.
Worst `|Δ_rel| = 2.68e-63`; every per-dim value reproduces #6587's.

## n=9: five shapes never previously evaluated

| λ | dim | b | per-dim | |
|---|---|---|---|---|
| `(8,1)` | 8 | 1 | 4718.6197 | |
| `(7,1,1)` | 28 | 2 | 3478.2851 | |
| `(7,2)` | 27 | 2 | 2793.0993 | |
| `(6,2,1)` | 105 | 3 | **1572.9564** | new |
| `(6,3)` | 48 | 3 | 1498.5567 | |
| `(5,3,1)` | 162 | 4 | **836.89929** | new |
| `(5,2,2)` | 120 | 4 | **665.48861** | new |
| `(4,4,1)` | 84 | 5 | **605.58457** | new |
| `(4,3,2)` | 168 | 5 | **384.85787** | new |
| `(3,3,3)` | 42 | 6 | 211.56463 | reproduces the capped value exactly |

## The first complete levels in this arc

Every envelope figure in this arc has been a max over a **dim-capped subset** of its level, and a
max over a subset is a lower bound on the max, not the max. With the ≤3-row shapes plus the Burau
hooks, three levels at n=9 close outright:

| b | level size | known | complete | envelope max | attained by |
|---|---|---|---|---|---|
| 1 | 1 | 1 | yes | 4718.6197 | `(8,1)` |
| 2 | 2 | 2 | yes | 3478.2851 | `(7,1,1)` |
| 3 | 3 | 3 | **yes** | 1671.2349 | `(6,1,1,1)` |
| 4 | 5 | 4 | no | — | missing `(5,2,1,1)` |
| 5 | 6 | 3 | no | — | missing 3 |
| 6 | 7 | 2 | no | — | missing 5 |
| 7 | 4 | 1 | no | — | missing 3 |

`4718.62 > 3478.285 > 1671.235` — **strictly decreasing over the complete levels.** The probe
prints an envelope only for a complete level; a subset max is not reported as a maximum.

Worth recording because it might have gone the other way: the new `(6,2,1)` at 1572.96 lands
*between* the hook `(6,1,1,1)` (1671.23) and the two-row `(6,3)` (1498.56), so completing `b=3` did
**not** overturn its level max. The reason to complete the level was that it could have.

## Coverage, measured

Of the 30 partitions of 9: **12** have ≤3 rows (this handle), **12** have ≤3 columns (the same
handle applied to transposes), overlapping only in `(3,3,3)`, and hooks contribute **3** more —
**26 covered, 4 not**:

```
(5,2,1,1) dim 189   (4,3,1,1) dim 216   (4,2,2,1) dim 216   (4,2,1,1,1) dim 189
```

Those four have both ≥4 rows and ≥4 columns, so no `k=3` orientation reaches them, and `k=4` is
hopeless — its largest weight sector at n=9 is `multinomial(9; 3,2,2,2) = 7560`. **Direct seminormal
at dim ≤ 216 is the cheaper route for exactly those four**, comparable in cost to the runs here.

## What is NOT established

- **n = 6 and n = 9 only.** The gate is at n=6; it is the same algorithm at n=9, but that is an
  argument, not a measurement at that size.
- **This does not complete the envelope.** Four levels at n=9 remain incomplete, and no envelope is
  reported for them.
- **Nothing here bounds anything.** It computes traces of the positive element `X*X`.
- Whether the envelope stays monotone once `b = 4…7` are completed is **open** — and it is exactly
  the question the capped measurements could not answer.
