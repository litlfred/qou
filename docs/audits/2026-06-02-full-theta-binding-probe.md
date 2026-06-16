# Full-order θ_λ binding — the carrier is right, but y_λ is the wrong measure for A≥3 absolute

**Date:** 2026-06-02
**Probe:** [`probe_full_theta_binding.py`](../../computations/probe_full_theta_binding.py)
→ `probe-full-theta-binding.witness.json`
**Status:** EXPLORATORY; asserts the refutation. A≥3-absolute binding remains an
open gate — but **sharply narrowed** by this result.

## What was tested

The prior probe ([`2026-06-02-theta-carry-binding-probe.md`](2026-06-02-theta-carry-binding-probe.md))
showed the rotation-only phase `|Δθ|` is too flat for absolute binding. The
diagnosis was that the extensive part lives in the GROWTH channels (`|χ/d|>1`).
This probe carries the **full-order** `θ_λ = arccos(χ^λ/d_λ) ∈ ℂ`
(Re = rotation phase, Im = growth/volume = `arccosh|χ/d|`) and tests every
component of `B = E·Σ_λ y_λ |Δθ_λ^{c}|`, `c ∈ {abs, re, im}`, on D/T/³He/⁴He.

## Result — none close; and WHY (the useful part)

| component | global scale | worst \|err\| | T/³He diff err |
|---|---|---|---|
| `|Δθ.abs|` | 50.0 | 198.8 % | −102.7 % |
| `|Δθ.re|` | 52.3 | 185.7 % | −75.9 % |
| `|Δθ.im|` (growth) | 213.2 | 257.8 % | −262.9 % |

All three share one signature: **D over-predicts (+186 … +258 %), and
T/³He/⁴He under-predict (−71 … −99 %), with ⁴He worst (≈ −98 %).** The
Markov-weighted phase sum is:

| isotope | `Σ y_λ |Δθ_λ|` (abs) | AME binding (MeV) |
|---|---|---|
| D | 0.133 | 2.22 |
| T | 0.033 | 8.48 |
| ³He | 0.034 | 7.72 |
| ⁴He | **0.006** | **28.30** |

**`Σ y_λ |Δθ_λ|` anti-correlates with A** (it shrinks ~20× from D to ⁴He) while
binding **grows ~13×**. Including the growth (Im) channels does not fix it —
`y_λ` *suppresses* them: ⁴He has a huge free growth-mass (1504, per
`binding_reeb_phase_decomposition.py`) but the `y_λ`-weighted contribution is
tiny, because `y_λ` is the **Markov/Plancherel measure for the TRACE (mass)** —
it concentrates on low-content blocks, exactly the opposite of where the
extensive binding sits.

## The narrowed gap

- ✅ **Carrier confirmed**: the per-block `θ_λ` (full-order, complex) is the right
  per-λ object; differences work (prior probe, +8 % no fit).
- 🔴 **Measure is wrong**: `y_λ` (the trace measure) is **not** the binding
  measure. Absolute A≥3 binding needs a per-block weight that **emphasises the
  growth channels** `y_λ` suppresses — a *binding-specific* measure, distinct
  from the mass/trace `y_λ`.

This is the refined open item: **find the per-block binding measure `w_λ^{bind}`
(≠ `y_λ`) such that `Σ_λ w_λ^{bind} |Δθ_λ|` tracks the extensive A-growth.** It is
the natural job of the **operator-valued combiner (#1698)** — which can apply a
weight other than the scalar-trace `y_λ`. The per-λ `θ_λ` vector it needs is now
emitted by `binding_reeb_phase_decomposition.py` (`by_partition`); what's missing
is the binding measure, not the carrier. Cross-ref cheat-sheet §9.3.
