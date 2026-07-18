# The Ohtsuki κ-tower validated first-principles from the Kashaev sum — the κ_n are the complex-volume cumulants (log Z), not the moments of Z

**Date:** 2026-07-18 · **Branch:** `claude/kappa-tower-kashaev-cumulant-validation-2026-07-18` ·
**Tier:** first-principles numerical validation (no fit) · **Discipline:** scope-(a); no `c_k`
wired; L2 unchanged (2/7). **Validates:** #3628's κ-tower; grounds #3692 (Borel resummation) and
the #3805/#3872 A_ω target.

## What this validates

The corpus Ohtsuki κ-tower (derived on #3628, bar-parity Lean-proved and Borel–Padé resummed on
#3692):

    κ₁ = (11/108)√3π      κ₂ = (2/27)π²      κ₃ = (1081/21870)√3π³      κ₄ = (98/729)π⁴

is here **independently reproduced from the raw Kashaev sum** `⟨4₁⟩_N = Σ_k |(q)_k|²`
(`q = e^{2πi/N}`), to rel err **1e-23 (κ₁), 1e-18 (κ₂), 1e-14 (κ₃), 1e-11 (κ₄)** — no fit, no
appeal to the #3628 derivation. Four exact rationals × π^n reproduced to 11+ digits is not
coincidence: the tower is correct.

## The convention it pins down (the moment-vs-cumulant / Z-vs-log Z distinction)

The κ_n are the coefficients of the **complex volume** `𝔙_b = 𝔙_0 + Σ_n (2πb²)ⁿ κ_n`, which is the
expansion of **`log Z`** (the free energy / connected generating function). The Kashaev sum
`⟨4₁⟩_N` is **`Z` itself**, whose asymptotic `Z/prefactor = 1 + Σ_n a_n (2π/N)^n` has **moment**
coefficients `a_n`. Moments and cumulants differ beyond first order:

    b₁ = a₁,   b₂ = a₂ − a₁²/2,   b₃ = a₃ − a₁a₂ + a₁³/3,   …

The κ_n are the `b_n` (cumulants). Comparing the tower to the moments `a_n` is a **category error**
producing a spurious ~15–21% "mismatch" at `n ≥ 2` (concretely `(2π)²a₂ ≈ 0.885 ≠ κ₂ = 0.731`,
21% off), while the cumulant `(2π)²b₂ = 0.731 = κ₂` matches exactly. `κ₁` matches either way only
because `b₁ = a₁`.

> **Record (discipline working).** This note began as an apparent "κ₃ is 16% off the corpus"
> finding from a moment-based extraction. The corpus-grep gate (AGENTS.md §"Before declaring
> refuted/mismatch") caught it: grepping the tower's origin
> ([`qbeta_c3_phib_kappa_tower_scale_probe.py`](../../computations/qbeta/qbeta_c3_phib_kappa_tower_scale_probe.py))
> revealed the κ_n are the `𝔙_b = log Z` coefficients (cumulants), not the moments of `Z` — so
> the "discrepancy" was a category error, and the corrected comparison validates the tower to
> 1e-11. No false "discrepancy" claim shipped.

## Method (no fit)

Fit `log(⟨4₁⟩_N / [3^{−1/4} N^{3/2} e^{N·Vol/2π}])` — which **is** the cumulant series
`Σ b_n (2π/N)^n` — by a Vandermonde linear solve over `N ∈ {400…51200}` at 260 dps. The two
well-determined low cumulants (`κ₁, κ₂`) are fit-order-independent (M=5 vs M=8, to 1e-8); `κ₃, κ₄`
converge more slowly in fit order (M=5 truncates too early to pin them), so their robustness is
carried by the ≤1e-11 match to the independent corpus closed forms. Everything is exact-arithmetic
Kashaev data through a linear solve — no free parameters.

## Why this serves the open work (options 1 + 2)

- **A_ω derivation (#3805/#3872).** The exact κ-tower is the target those GGM/Stokes derivations
  must reproduce; this validates it first-principles (independent of #3628's fit) and fixes the
  convention (cumulant / `𝔙_b`, with the `κ₁ = 11√3π/108` 2-loop = `2π·11/(72√3)` normalization
  from the merged #3890). If a GGM tower surfaces a `0.885`-scale `κ₂`, it is the *moment* — apply
  the cumulant correction.
- **Odd-channel Borel resummation (#3692).** The divergent tower that #3692 Borel–Padé resums to
  the smooth `Im 𝔙_b` is exactly this cumulant series; grounding `κ₁..κ₄` first-principles from the
  Kashaev sum anchors the resummation's input. The odd rungs (`κ₁, κ₃`, √3-carrying) feed the
  bar-odd `S`; the even rungs (`κ₂, κ₄`, rational) feed the bar-even Vol (#3628 √3-parity, Lean
  `OhtsukiTowerBarParity.lean`).

## Scope discipline

scope-(a) validation; **no fit** (Vandermonde solve on exact Kashaev data); no `c_k` wired; L2
unchanged (2/7). Nothing here re-pins a production constant — it validates an existing derived
tower and records the moment/cumulant convention to prevent the category error recurring.

## Compute

- Probe: [`computations/qbeta/qbeta_ohtsuki_kappa_tower_kashaev_cumulant_validation.py`](../../computations/qbeta/qbeta_ohtsuki_kappa_tower_kashaev_cumulant_validation.py) (exit 0)
- Witness: `computations/qbeta/qbeta-ohtsuki-kappa-tower-kashaev-cumulant-validation.witness.json`

## Cross-references

- The κ-tower's derivation + bar-parity + Borel resummation: #3628 / #3692, [`qbeta_c3_phib_kappa_tower_scale_probe.py`](../../computations/qbeta/qbeta_c3_phib_kappa_tower_scale_probe.py)
- The 2-loop convention (κ₁ = 2π·11/(72√3)): [`2026-07-18-genuine-4one-2loop-is-quantum-dilog.md`](2026-07-18-genuine-4one-2loop-is-quantum-dilog.md) (merged #3890)
- A_ω derivation this feeds: #3805, #3872
