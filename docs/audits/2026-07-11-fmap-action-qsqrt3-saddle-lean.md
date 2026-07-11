# The even-channel action's arithmetic home is ℚ(√3) — Lean-certified saddle arithmetic

**Date:** 2026-07-11 · **Axis:** z→c_k f-map keystone (even channel) · **Tier:**
proved-lean (saddle arithmetic) · **Discipline:** no fit, no c_k / action value
claimed, no wiring, no tier change. Follow-up to
[`2026-07-11-fmap-action-qsqrt3-saddle-entropy-block.md`](2026-07-11-fmap-action-qsqrt3-saddle-entropy-block.md)
(#3571: the *numerical* PSLQ route to the ℚ(√−3) arithmetic is entropy-blocked).

## What #3571 left, and what this closes

#3571 established that ℚ(√−3) (the 4₁ invariant trace field) is the arithmetic
*home* of the even-channel resurgence expansion, but that PSLQ on the numerical
Kashaev-ladder coefficients cannot reach the exact arithmetic (divergent series +
fit contamination). The exact route is the saddle recursion — and its leading
data are now computed **exactly and Lean-certified**.

The 4₁ Kashaev sum localises at the saddle `x* = 5/6` (where `2 sin(5π/6)=1`, so
`G'(x*)=log 1 = 0`). The Taylor derivatives of `log(2 sin πx)` there are exact
`ℚ(√3)·π^k` elements:

```
G''(x*) = −√3·π          G'''(x*) = −4π²         G⁴(x*) = −8√3π³
G⁵(x*)  = −80π⁴          G⁶(x*)  = −352√3π⁵      G⁷(x*) = −5824π⁶
```

(even orders carry √3, odd orders are rational — the ℚ(√3) arithmetic). The
leading saddle-Laplace perturbative coefficient is exactly

```
b₁ = g₄/(8 g₂²) + 5 g₃²/(24 |g₂|³) = √3·π/54 ∈ ℚ(√3)·π
```

using the exponent (`2G`) data `(g₂,g₃,g₄) = (−2√3π, −8π², −16√3π³)`.

## Lean (sorry-free, lean-direct EXIT 0)

[`QOU/QBeta/Qsqrt3SaddleArithmetic.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/Qsqrt3SaddleArithmetic.lean)
(v4.24.0 + restored `lake-cache/qou-v4-24-0`; wired into `QOU.lean`):

| theorem | statement |
|---|---|
| `sin_saddle` / `grad_saddle_zero` | `2 sin(5π/6)=1`; `G'(x*)=log(2 sin 5π/6)=0` (critical point) |
| `cos_saddle` / `cot_saddle` | `cos(5π/6)=−√3/2`; `cot(5π/6)=−√3` |
| `hessian_eq` | `G''(x*) = π·cot(5π/6) = −√3·π` |
| `laplaceB1_at_saddle` | `b₁ = √3·π/54` (exact) |
| `laplaceB1_saddle_mem_qsqrt3` | `∃ r∈ℚ, b₁ = r·√3π` (the ℚ(√3)·π membership) |

Even-channel counterpart of the odd-channel
[`HopfCubicOddCarrier`](../../content/quantum-observable-universe/lean/QOU/QBeta/HopfCubicOddCarrier.lean)
(KC20, the bar-odd carrier over the prime-19 cubic field).

## Honest scope (anti-laundering) — arithmetic *home*, NOT the observable action

`b₁ = √3π/54 ≈ 0.101` is the **naive integral-Laplace** coefficient; it does **not**
equal the observable action coefficient `c₁ ≈ 0.554` (#3571). The observable needs
the full state-integral normalisation (the `N^{3/2}` power, Euler–Maclaurin
sum-vs-integral and boundary terms) absent from the naive saddle — research-grade,
and the observable's *exact* form remains unknown. **No action value is claimed or
wired.** A numeric `b₁ < ½ < c₁` inequality would need π-bounds from
`Mathlib…Trigonometric.Bounds`, outside this file's cached dependency surface; the
value-gap is recorded in the module docstring rather than lemma-ised.

Net: the even channel's arithmetic home is ℚ(√3), now proved from the exact
saddle Taylor data — the exact-arithmetic complement to #3571's numerical
entropy-block, closing the "which arithmetic" question without laundering a
closed-form action.

## Cross-references

- Numerical entropy-block (#3571): [`2026-07-11-fmap-action-qsqrt3-saddle-entropy-block.md`](2026-07-11-fmap-action-qsqrt3-saddle-entropy-block.md)
- Action real/amphichiral (#3508): [`2026-07-11-fmap-action-pin-and-hexagonal-prune.md`](2026-07-11-fmap-action-pin-and-hexagonal-prune.md)
- Odd-channel carrier (KC20): [`HopfCubicOddCarrier.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/HopfCubicOddCarrier.lean)
