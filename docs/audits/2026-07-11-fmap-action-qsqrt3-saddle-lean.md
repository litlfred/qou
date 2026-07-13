# The even-channel action: ℚ(√3) home + EXACT observable coefficient `κ₁ = 11√3π/108`

**Date:** 2026-07-11 · **Axis:** z→c_k f-map keystone (even channel) · **Tier:**
proved-lean (saddle arithmetic) + numerical-exact (κ₁ identification, 33-digit PSLQ)
· **Discipline:** no fit to QOU data, no Q_β c_k / action value wired, no tier change.
Follow-up to
[`2026-07-11-fmap-action-qsqrt3-saddle-entropy-block.md`](2026-07-11-fmap-action-qsqrt3-saddle-entropy-block.md)
(#3571: the *numerical* PSLQ route to the ℚ(√−3) arithmetic is entropy-blocked).

## What #3571 left, and what this closes

#3571 established that ℚ(√−3) — the *imaginary* quadratic invariant trace field of
4₁ — is the ambient arithmetic of the even-channel resurgence, but that PSLQ on the
numerical Kashaev-ladder coefficients cannot reach the exact arithmetic (divergent
series + fit contamination). The exact route is the saddle recursion — and its
leading data are now computed **exactly and Lean-certified**. Those real saddle data
live in the totally real quadratic field **ℚ(√3)**, a field *distinct* from the
imaginary quadratic trace field ℚ(√−3): both embed in the cyclotomic field ℚ(ζ₁₂),
and `√−3 = i·√3` relates their generators, but the two number fields are not equal
(one totally real, one imaginary). The certified content below is the ℚ(√3) real
saddle arithmetic that the ℚ(√−3) trace field refracts.

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

## The observable leading coefficient — EXACT: `κ₁ = 11√3π/108 = (11/2)·b₁`

The naive saddle `b₁ = √3π/54 ≈ 0.101` is the **integral**-Laplace coefficient; it
omits the Euler–Maclaurin sum-vs-integral correction of the discrete Kashaev *sum*.
The **observable** leading coefficient is `κ₁ = [1/N] log J_N(4₁) ≈ 0.5542164724…`
(the value #3571 could only fit; the naive saddle missed it, `κ₁/b₁ = 5.5`). A
targeted extraction closes it exactly:

- **Method** ([`qbeta_ohtsuki_kappa1_extract.py`](scripts/qbeta_ohtsuki_kappa1_extract.py)):
  strip the exact `(3/2)log N + N·Vol/2π` pieces from `log J_N`, then a 10-point
  Vandermonde fit in `1/N` (N ≤ 786432, dps 120) isolates `κ₁` to **≈23 confident
  digits** — the entropy-block of #3571 was on the *full ladder*, never the
  best-conditioned leading rung. #3571's failure to PSLQ was a basis-size artifact
  (10 elements at 15 digits is under the entropy bound), not a real block on κ₁.
- **Identification** (2-term PSLQ, **33-digit** agreement): `κ₁ = 11·√3·π/108 ∈ ℚ(√3)·π`.
- **Structure 1** — `κ₁ = (11/2)·b₁`: the Euler–Maclaurin sum-correction multiplies
  the naive saddle by exactly `11/2`.
- **Structure 2** — Ohtsuki's imaginary-coefficient form `κ_1^Oht = A/√−3` has the
  rational `A = 11/72` **exactly** — the classical figure-eight **2-loop numerator
  `11`**. (The imaginary `√−3` trace field ⇒ real observable via `κ₁ = 2π·A/√3`.)

Lean (`ohtsukiKappa1`, `ohtsukiKappa1_eq_eleven_halves_b1`, `ohtsukiKappa1_mem_qsqrt3`)
certifies the **algebra** `κ₁ = (11/2)·b₁` and the `ℚ(√3)·π` membership; the *value*
`κ₁ = 11√3π/108` is the numerical Ohtsuki identification (not proved from the sum).

## Honest scope (anti-laundering)

`κ₁` is a fact about the **4₁ Kashaev/Ohtsuki asymptotic** — a topological invariant
— **NOT** a Q_β production `c_k`. Identifying it wires **nothing**: the bridge from
the 4₁ resurgence action to the physical Q_β observable action is the open keystone.
Higher-order `[1/N^k]` coefficients remain entropy-blocked (#3571). **No Q_β action
value is claimed or wired; no tier changes.**

Net: the even channel's arithmetic home is ℚ(√3), and its observable **leading
coefficient is now exact** — `κ₁ = 11√3π/108`, the Ohtsuki 2-loop coefficient —
extending #3571's entropy-blocked numerical route and #3606's naive saddle to the
true observable value, without laundering the keystone bridge.

## Cross-references

- κ₁ extraction probe + witness: [`scripts/qbeta_ohtsuki_kappa1_extract.py`](scripts/qbeta_ohtsuki_kappa1_extract.py)
- Numerical entropy-block (#3571): [`2026-07-11-fmap-action-qsqrt3-saddle-entropy-block.md`](2026-07-11-fmap-action-qsqrt3-saddle-entropy-block.md)
- Action real/amphichiral (#3508): [`2026-07-11-fmap-action-pin-and-hexagonal-prune.md`](2026-07-11-fmap-action-pin-and-hexagonal-prune.md)
- Odd-channel carrier (KC20): [`HopfCubicOddCarrier.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/HopfCubicOddCarrier.lean)
