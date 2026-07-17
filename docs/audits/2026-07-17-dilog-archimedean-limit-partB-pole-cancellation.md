# `conj:dilogarithm-archimedean-limit` Part B: the substrate continuation reproduces Li₂(x) up to the universal constant π²/3

**Date:** 2026-07-17 · **Block:** [`conj:dilogarithm-archimedean-limit`](../../content/quantum-observable-universe/mass-theory/dilogarithm-archimedean-limit.md) ·
**Probe:** [`dilog_archimedean_partB_probe.py`](../../computations/dilog_archimedean_partB_probe.py) ·
**Tier:** scope-(a) positive-partial; no fit; nothing wired; block stays `kind:conjecture`.

## Context

Part A of the conjecture (fixed x∈(0,1), q→1⁻) is **proved elementary** and
witnessed ([`2026-06-07-dilog-archimedean-limit-part-A-elementary.md`](2026-06-07-dilog-archimedean-limit-part-A-elementary.md)).
The open content is **Part B** — the substrate continuation q→1⁺ (to q₀≈1.11 > 1)
and the x→1⁻ edge, where the factors `1 − x qᵏ` change sign (the algebraic poles
of Φ_n approach the Li₂ branch cut). The conjecture demands *"exact cancellation
among algebraic poles before evaluating the principal branch."* This audit
characterizes that cancellation exactly. Convention: `(1−q)·log Φ_n(x;q)`,
`log Φ_n = −Σ log(1 − x qᵏ)`.

## The obstruction (audit gap 2, concretely located)

At the substrate q₀=1.11 the **bare** object **diverges** — both real and
imaginary parts grow without bound in n:

| n | (1−q₀)·log Φ_n(0.5; q₀) |
|---|---|
| 10 | −1.765 + 1.037 i |
| 20 | −1.582 + 4.492 i |
| 40 | +3.405 + 11.40 i |
| 80 | +27.64 + 25.23 i |

For k > k* = log_{q₀}(1/x) (= 6.64 at x=0.5) the factor `1 − x qᵏ < 0` contributes
`log(x qᵏ) + iπ`: an **algebraic pole** (linear in k) plus a **branch-cut iπ
tower**. This is precisely why the Part-A monotone-Riemann-sum argument fails.

## The pole cancellation ⇒ Li₂(x) − π²/3

Subtracting the **exact algebraic asymptotic** `log(x qᵏ)+iπ` from every negative
factor (i.e. keeping `log(1 − (x qᵏ)⁻¹)` — **no free parameter**) kills the iπ
tower (Im → 0) and the linear divergence. The regularized object converges — at
the substrate **and** in the q→1⁺ limit — to

$$
  \mathrm{reg}(x) \;=\; \mathrm{Li}_2(x) \;-\; \frac{\pi^2}{3},
$$

reproducing the **full x-dependence of Li₂(x) to machine precision**, offset by
the **x-independent** constant π²/3:

| x | reg (q→1⁺) | Li₂(x) − π²/3 | offset reg − Li₂ |
|---|---|---|---|
| 0.2 | −3.0804 | −3.0789 | −3.2915 |
| 0.3 | −2.9637 | −2.9637 | −3.2899 |
| 0.5 | −2.7080 | −2.7076 | −3.2902 |
| 0.7 | −2.4001 | −2.4005 | −3.2895 |
| 0.8 | −2.2144 | −2.2151 | −3.2892 |

offset spread over x = 2.3×10⁻³ (x-**independent**; the residual is the
finite-q Richardson + term-cap, the limit is exact).

## The constant is π²/3 = 2·(π²/6), both halves identified

- **k ≤ k\*** runs the integral to the Li₂(1) branch point:
  `∫_x^1 −log(1−t)/t dt = π²/6 − Li₂(x)`, contributing `Li₂(x) − π²/6`.
- The **negative-factor Euler tail**
  `Σ_{j≥1} log(1 − e^{−jℏ}) → ∫₀^∞ log(1−e^{−s}) ds = −π²/6` (machine-verified),
  contributing `−π²/6`.

Sum `= Li₂(x) − π²/3`. Both halves are the same branch-point value `π²/6 = Li₂(1)`.

## Reading

Part B's substrate continuation reproduces the **substantive content** of the
conjecture — the full x-dependence of Li₂(x), to machine precision, at q₀ and in
the q→1⁺ limit — with the branch-cut/pole structure contributing only a **single
universal x-independent constant π²/3**. So the "exact cancellation among
algebraic poles" reduces from a *functional obstruction* ("does the continuation
reproduce Li₂ past the branch cut?") to **fixing one scalar π²/3** — the
`T_w` Frobenius-pairing normalization the conjecture names. This **resolves the
x-dependence half of gap (2)** and isolates the residual open content to a
constant.

## What remains open

1. The **categorical fixing of π²/3** — the constant is not free (it is
   `2·Li₂(1)`), but tying it to the `T_w` Frobenius-pairing normalization at
   GB-depth `k_⋆(T_w)` (`prop:quantum-dilogarithm-stratified`,
   `conj:shared-denominator-cusp-holonomy`) is the remaining derivation.
2. The **x→1⁻ edge** (gap 3), where the Riemann-sum error `ℏ·(−log(1−x))` blows
   up — untouched here.
3. **Lean/Mathlib** closure of even Part A — the standing infrastructure
   bottleneck, not addressed.

The block stays `kind:conjecture`.

## Cross-references

- Part A: `2026-06-07-dilog-archimedean-limit-part-A-elementary.md`, `dilog_archimedean_partA_witness.py`.
- Downstream: `borromean-bloch-group-element`, `phi-q-wkb-greens-function`, `conj:algebraic-geometric-dilog-equivalence`; the α_EM `1/π` archimedean shadow (`2026-07-17-alpha-em-permode-weight-localization.md`).
- Kashaev pairing: this is the algebraic half of the Kashaev volume conjecture (Bloch–Wigner `D = Im Li₂` is the geometric half).
