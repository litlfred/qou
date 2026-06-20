# W_λ partition-function defect Z(n): sign change at n=7 sharpens *and* tempers the q-Bessel lead

**Date:** 2026-06-20
**Branch:** `claude/fervent-noether-zssd1k`
**Status:** Structural narrowing — no fit, no correspondence chain
**Extends:** [`keystone_qbessel_plancherel_precheck.py`](scripts/keystone_qbessel_plancherel_precheck.py) (8d781b21, n=5 only)
**Script:** [`scripts/keystone_wlambda_Z_defect_n_scaling.py`](scripts/keystone_wlambda_Z_defect_n_scaling.py) (`ALL CHECKS PASS`, exit 0)
**Frontier:** q-Bessel/heat-kernel geometric realization of the Ocneanu weights `W_λ = d_q(λ)²/[n]_q!` (#2503 DG plan; #2488 scope handoff)

## What the precheck left open

The precheck (8d781b21) found the candidate weight `W_λ = d_q(λ)²/[n]_q!` is **not**
a probability measure at `q_0`: it is sub-normalized, with partition function
`Z(5) = Σ_{λ⊢5} W_λ = 0.98222`, defect `1 − Z(5) = 0.0178`. It named `1 − Z` as
"the geometric quantity to explain" (the heat-kernel trace any `S¹`-equivariant
index realization must reproduce) — **but computed it only at `n = 5`.**

This note extends that single number to a structural object, using **only**
balanced-q-integer arithmetic (`[m]_q = (qᵐ − q⁻ᵐ)/(q − q⁻¹)` and the q-hook-length
formula `d_q(λ) = [n]_q!/∏_cells [h]_q`). The `2I → E8 → Poincaré → Lawrence–Zagier`
correspondence chain is **never invoked** — this is a property of `W_λ` itself.

## Result

`Z(n) = Σ_{λ⊢n} d_q(λ)²/[n]_q!` at `q_0 = 1.10997858` (`h_0 = q_0 − q_0⁻¹ ≈ 0.2091`):

| n | Z(n) at q₀ | 1 − Z(n) |
|---|-----------|----------|
| 2 | 0.994581 | +0.005419 |
| 3 | 0.987440 | **+0.012560** |
| 4 | 0.982165 | +0.017835 (max) |
| 5 | 0.982224 | +0.017776 |
| 6 | 0.991080 | +0.008920 |
| 7 | **1.012426** | **−0.012426** |

**Small-h leading order** `1 − Z(n) = C(n)·h² + O(h⁴)` (verified bar-even: `C(n)`
is stable across `h = 10⁻³` and `10⁻⁴`). Empirical `24·C(n)` for `n = 2..8`:
`3, 7, 10, 10, 5, −7, −28`.

## Three findings

1. **`1 − Z(3) = 0.01256`** — the keystone generation blocks live at `n = 3`
   (the Borromean `H₃`), not `n = 5`. This value was previously un-computed.

2. **The defect is non-monotone and changes sign.** It rises to a max `≈ 0.0178`
   near `n = 4`, falls, and `Z(n)` **crosses 1 at `n = 7`** (defect goes negative).
   The leading `h²` coefficient `C(n)` itself flips sign there.

3. **Leading order is `h²` — bar-even** (invariant under `q → q⁻¹`). A bar-even
   quantity **cannot by itself** be the bar-odd 210 ppb muon shift, consistent
   with [44377f33](../coordination/s5-so3-keystone.md) (the frontier carries the
   `O(1)` generation skeleton, not the fine shift).

## Why it matters (sharpens **and** tempers the lead)

- **Sharpens:** the q-Bessel/heat-kernel realization (#2503) now has a sharp,
  falsifiable target — any `S¹`-equivariant index whose index measure is `W_λ`
  must reproduce a partition function `Z(n)` that is `< 1` for `2 ≤ n ≤ 6` **and
  `> 1` for `n ≥ 7`**. A geometric object with this `n`-profile is a strong
  constraint; one without it refutes the identification.

- **Tempers:** the framing "`1 − Z` is the mass defect" is **not** a clean
  monotone-positive heat-kernel-trace story once the sign change is included. A
  partition function / heat-kernel trace is conventionally positive and definite;
  a normalization constant that crosses 1 is more naturally read as `W_λ`
  simply not being the right (un-normalized) measure — the genuine q-Plancherel
  probability measure is `W_λ/Z(n)`, and `Z(n)` may be a normalization artifact
  rather than a geometric defect. The DG build (#2503 Step-1 gate) should treat
  the sign change as a discriminating test, not assume `1 − Z > 0`.

## What this does NOT do

- No closed form for `C(n)` is claimed. A hook-moment ansatz
  `C(n) = (1/n!)Σ_λ dim(λ)·Σ_cells h²` was **tested and refuted** (the script's
  self-check caught it); `C(n)` is reported empirically only.
- Manifold existence stays **owner-gated** (subgoal-2 differential geometry).
- **No physical claim** and **no fit**: `q_0` anchors the table; the 210 ppb
  target is referenced only to note the bar-parity mismatch (it tunes nothing).
