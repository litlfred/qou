# Volume-Wedderburn Δ_λ — cheap geometric proxies refuted; q-6j saddle remains

**Date:** 2026-06-02
**Probe:** [`probe_volume_wedderburn_delta_lambda.py`](../../folio-assistant/computations/probe_volume_wedderburn_delta_lambda.py)
→ `probe-volume-wedderburn-delta-lambda.witness.json`
**Status:** EXPLORATORY (per `production-vs-exploratory-discipline`); asserts the
refutation. Δ_λ remains an open gate (GAP-A-3/A-4).

## The hypothesis (owner, 2026-06-02)

Close the per-partition binding density Δ_λ via a **per-Wedderburn-block
q-hyperbolic volume**: treat the Hecke energy as a representation that
Wedderburn-decomposes, and set

$$B(K) = m_e \sum_{\lambda \vdash 3A} y_\lambda(q_0)\,\chi^\lambda(\beta_K)\,\mathrm{Vol}_\lambda,$$

with `Vol_λ` a **parameter-free** function of the partition λ (computed from
geometry, not fit to binding). The motivating object is the quantum-6j /
volume-conjecture per-block ideal-tetrahedron volume (Costantino–Murakami).
If a single `Vol_λ` rule reproduces D / T / ³He / ⁴He simultaneously with no
per-isotope refit, the 1-equation/11-unknowns underdetermination is broken
and Δ_λ is closed.

## What was tested

Cached canonical-q₀ per-partition `(y_λ, χ_λ)` for all four light isotopes
(`chi-{deuteron,tritium,helium-3,helium-4}-…-at-q0-50dps.witness.json`)
against five parameter-free `Vol_λ` rules:

| rule | basis | params |
|---|---|---|
| `clausen_content` | `Σ_cells |Λ(π·content/n)|` (Lobachevsky volume) | 0 (volume units) |
| `clausen_hook` | `Σ_cells |Λ(π·hook/(n+1))|` | 0 (volume units) |
| `content_sq` | `Σ_cells content²` | 1 global scale |
| `abs_content` | `Σ_cells |content|` | 1 global scale |
| `uniform` | `Vol_λ = 1` (scalar Path-C) | 1 global scale |

`Λ(θ) = ½ Im Li₂(e^{2iθ})` is the ideal-hyperbolic-tetrahedron volume.

## Result — refuted

No rule closes all four within 5 % (worst |err| per rule: 99.7 %, 99.6 %,
324 %, 380 %, 313 %). The zero-parameter Clausen volumes **undershoot like the
bare `tr_M`** (D −85 % ≈ the −83 % bare-formula miss in
`binding-energy-categorical-deuteron`), i.e. content/hook-angle volumes are too
flat to supply the per-block structure the binding needs. The dimensionless
rules with a single global scale scatter wildly across isotopes (D +300 % while
T lands near −7 %), the signature of a non-categorical shape.

## Verdict & next step

The cheap geometric proxies are **out**. This is a clean narrowing, not a dead
end: it isolates the remaining candidate to the genuine **q-6j saddle-point
volume** — the asymptotic of the SU(2)_q 6j-symbol per Wedderburn block
(volume conjecture for 6j-symbols), which is *not* a content/hook shortcut and
must be computed directly. That is the next probe.

The structural case for the direction is unchanged and still strong (corpus
search: never tried; aligns with GAP-A-3/A-4; see
[`2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md)
and the Option E programme PR #1697). What this probe establishes is that the
*easy* version of `Vol_λ` does not work — the per-block volume must carry real
6j-asymptotic content.
