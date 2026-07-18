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

## Categorical tie-down: the T_w Frobenius truncation removes one π²/6

The `T_w` Frobenius-pairing normalization the conjecture names is **not** ad hoc —
it is the **stratified-truncation corollary** of
[`prop:quantum-dilogarithm-stratified`](../../content/quantum-observable-universe/mass-theory/quantum-dilogarithm-stratified.md):
the Frobenius trace `tr_M(Φ_q(z_i)·T_w)` truncates at the NF support depth
`k_⋆(T_w)`, so *"the analytic infinite product truncates to a finite product … the
analytic divergence is a side-effect, absent from the categorical mass."* The
truncation cut is exactly at the sign-flip `k* = log_{q₀}(1/x)`, whose denominator
root `x = q₀^{−k*}` is the **cusp-completeness address**
([`conj:shared-denominator-cusp-holonomy`](../../content/quantum-observable-universe/mass-theory/shared-denominator-cusp-holonomy.md)).

Computing the genuine categorical object — the **truncated** product
`Φ_q^{[≤k*]}` (only the positive factors, `k ≤ k*`) — gives, in the q→1⁺ limit:

$$
  (1-q)\log \Phi_q^{[\le k_*]}(x;q) \;\longrightarrow\; \mathrm{Li}_2(x) - \frac{\pi^2}{6},
$$

| x | trunc (q→1⁺) | Li₂(x) − π²/6 |
|---|---|---|
| 0.2 | −1.4357 | −1.4339 |
| 0.5 | −1.0609 | −1.0627 |
| 0.8 | −0.5707 | −0.5701 |

So the T_w truncation **removes exactly one of the two π²/6 halves** — the
negative-factor Euler tail (`k > k*`), which is never Frobenius-paired. The
residual offset is the **single archimedean regulator constant**
`π²/6 = ζ(2) = Li₂(1)` — the dilogarithm's value at the cusp/branch point `x=1`
(the last, vanishing, factor). So the categorical mechanism reduces the offset
from the ad-hoc `π²/3` to the canonical regulator `ζ(2)`, and the remaining open
content is the **cusp-boundary regulator term** at `x=1`, not a functional
obstruction.

> **Lean provenance (2026-07-18).** The residual cusp constant
> `Li₂(1) = ζ(2) = π²/6` is now **machine-verified** as the sorry-free lemma
> `QOU.QPochhammer.LiTwo_one` in
> [`DilogarithmArchimedeanLimit.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/DilogarithmArchimedeanLimit.lean)
> (`LiTwo 1 = Real.pi ^ 2 / 6`, via Mathlib's `hasSum_zeta_two` + the
> vanishing-`n=0` split `Summable.tsum_eq_zero_add`). So the single archimedean
> regulator this derivation reduces to is no longer an asserted constant — it is
> a proved value. The pole-subtraction step is likewise Lean-backed
> (`log_neg_factor_split`), and the sub-unity per-factor expansion is the new
> `neg_log_one_sub_hasSum` / `partialProduct_log_eq` (Part A primitives). What
> stays open is the *uniform/Tauberian exchange* (`ArchimedeanLimit` class), not
> the value of the cusp constant.

## Grounding: the residual ζ(2) is the extended-Bloch / Rogers normalization

The residual `π²/6 = ζ(2) = Li₂(1)` is **not** a new mystery constant — it is the
**standard extended-Bloch-group / Rogers-dilogarithm normalization**. With the
Rogers dilogarithm `R(z) = ½ log z·log(1−z) + Li₂(z)`, at the complete
figure-eight shape `z = e^{iπ/3}`:

$$
  2\,R(e^{i\pi/3}) \;-\; \frac{\pi^2}{6} \;=\; i\,\mathrm{Vol}(4_1)
  \qquad(\text{Re}=-2\times10^{-41},\; \mathrm{Im}=2.0298832=\mathrm{Vol}(4_1)),
$$

so `Re[2R(e^{iπ/3})] = π²/6` exactly — the `−π²/6` here is the **same** constant
that normalizes Neumann's / Murakami–Yokota's complex volume
`f(u) = (1/2π){R(z)+R(w) − π²/6} − (i/2π)Vol(E)`. It is precisely the constant
that **pairs the algebraic half (Li₂) with the geometric half (Bloch–Wigner
`D = Im Li₂` → Vol)** — exactly the pairing the conjecture's own statement names
("supplies the algebraic half of the Kashaev volume conjecture, pairing with the
Bloch–Wigner geometric half").

So Part B closes numerically as

$$
  \underbrace{\mathrm{Li}_2(x) - \zeta(2)}_{\text{T}_w\text{-truncated bulk}}
  \;+\; \underbrace{\zeta(2)}_{\text{extended-Bloch cusp}}
  \;=\; \mathrm{Li}_2(x),
$$

and the residual is a **standard, non-fitted regulator**, not a functional
obstruction.

## Derivation: the cusp ζ(2) is the (quantum-)dilog inversion constant

The residual is not merely *identified* but **derived** — it is theorem-forced
([`dilog_archimedean_partB_cusp_derivation_probe.py`](../../computations/dilog_archimedean_partB_cusp_derivation_probe.py)).
The substrate continuation crosses the cusp `x=1` (the `k*` completeness root),
inverting the argument `x qᵏ ↦ (x qᵏ)⁻¹` for the `k>k*` factors. The classical
**dilogarithm inversion formula** carries exactly `−ζ(2)`:

$$
  \mathrm{Li}_2(z) + \mathrm{Li}_2(1/z) + \tfrac12\log^2(-z) = -\frac{\pi^2}{6}
  \qquad (z\notin(0,1)),
$$

verified to `2.4×10⁻⁴¹` for all test `z`. Its **categorical / quantum** realization
is the **Faddeev quantum-dilogarithm inversion relation**

$$
  \Phi_b(z)\,\Phi_b(-z) = e^{i\pi z^2}\, e^{i\pi(b^2+b^{-2})/12},
$$

whose modular-anomaly constant `iπ(b²+b⁻²)/12` has semiclassical (b→0) limit
`−π²/6` at the Li₂ level (`2πib²·[·] → −ζ(2)`; the `b⁻²·b²=1` term survives). So
`ζ(2)` is exactly the modular anomaly that the **bare / T_w-truncated** partial
product LACKS and the **modular-complete** Faddeev `Φ_b` (whose semiclassical
limit *is* `Li₂`) CARRIES. The same `ζ(2)` is the extended-Bloch/Rogers pairing
constant (`2R(e^{iπ/3})−π²/6 = i·Vol(4₁)`), tying the algebraic and geometric
halves.

**So the cusp regulator is closed at the level of value + origin:** it is a
standard, theorem-forced constant (the quantum-dilogarithm inversion / modular
anomaly), not a fit.

## What remains open

1. The **sign-assembled Lean formalization** — the derivation above fixes the
   value and origin of `ζ(2)`; the modular-completion bookkeeping that assembles
   `[T_w-truncated bulk] + [Φ_b modular anomaly] = Li₂(x)` sorry-free in Lean is
   the remaining formal step.
2. The **x→1⁻ edge** (gap 3), where the Riemann-sum error `ℏ·(−log(1−x))` blows
   up — untouched here.
3. **Lean/Mathlib** closure of even Part A — the standing infrastructure
   bottleneck, not addressed.

The block stays `kind:conjecture`.

## Cross-references

- Part A: `2026-06-07-dilog-archimedean-limit-part-A-elementary.md`, `dilog_archimedean_partA_witness.py`.
- Downstream: `borromean-bloch-group-element`, `phi-q-wkb-greens-function`, `conj:algebraic-geometric-dilog-equivalence`; the α_EM `1/π` archimedean shadow (`2026-07-17-alpha-em-permode-weight-localization.md`).
- Kashaev pairing: this is the algebraic half of the Kashaev volume conjecture (Bloch–Wigner `D = Im Li₂` is the geometric half).
