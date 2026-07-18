# α_EM per-loop measure `1/(8π)` — consolidated status (what is forced, what remains: one named conjecture)

**Date:** 2026-07-18 · **Axis:** α_EM per-loop measure (the single load-bearing
wall of the α_EM derivation) · **Tier:** status consolidation (no new result;
records the crystallized state) · **Discipline:** `1/(8π)` stays a **phase-4
identification** (R1 canonical); no fit; nothing wired.

## Purpose

The per-loop measure `1/(8π)` has been attacked from many angles across the
Front-3 cluster and the follow-on probes. This document consolidates the state:
**everything decomposable is decomposed; the wall has crystallized to a single
named conjecture.** It supersedes the scattered "still open" phrasing — the open
item is now *precise*, not diffuse.

## What is FORCED (the derived skeleton)

| ingredient | value | status | source |
|---|---|---|---|
| **count** = real harmonic-1-form count `b₁ = 2g = 8` (not holomorphic `g = 4`) | `8` | **forced** (Lean sorry-free) | #3920 (real Δ₁ ζ-index + real gauge field) |
| **π-power** = archimedean 2d heat-kernel `(4πs)^{−d/2}\|_{d=2}`, exponent `−1` | `1/(4π)` | **forced** | #3909 (three-way π adjudication) |
| **covolume** of the photon moduli `Vol(J) = √\|det Q\|` (unimodular) | `1` | **forced** | #3925 (Poincaré-duality unimodularity) |
| **the `2`** = Hecke channel count `e₊/e₋` (quadratic Hecke relation) | `2` | **derived** | sibling conjecture-statement F1 |
| **channel-swap involution** = `q ↦ −q⁻¹` (bar `q↦q⁻¹` FIXES the channels); carries the global `−` sign (`[2]_q ↦ −[2]_q`) | — | **exact `ℚ(q)`** | #3936 |
| **GB geometrization** = `a₀ = 1/(4π) = \|χ\|/(2·Area)`; genus-independent | — | **proved (Lean)** | main `ba606720e`/`2b562bc7d` |

Consequence (the derived object): the 1-loop measure on the unimodular Jacobian
is the bare heat-kernel unit `a₀ = 1/(4π)`. The data measure `1/(8π) = ½·a₀`.
The entire underived residual is a single factor `½` (#3925), whose "2" is the
Hecke channel multiplicity (derived count), placed in the **classical-limit
normalization**, not in q-dependent weights (sibling F2/F3).

## What REMAINS — one named conjecture (three equivalent statements)

The wall is a single correspondence, stated equivalently as:

1. **(classical-limit normalization)** the `q→1` one-loop total of the α_EM loop
   tower equals `a₀·α` (the universal heat-kernel unit) — sibling F3;
2. **(τ-functor unification)** the τ-functor identifies the Hecke channel-swap
   `q ↦ −q⁻¹` with the Hodge conjugation `H^{1,0} ↔ H^{0,1}` (#3920) — the "2"s
   are the same doubling;
3. **(categorical 1-loop propagator)** the RT shadow-world 1-loop determinant on
   the genus-4 Jacobian normalizes the measure to `½·a₀` — derivability map's
   "multi-week item".

### Sharpening of statement 2 (this cluster's contribution)

- The unifying involution is `q ↦ −q⁻¹` (the eigenvalue exchange), **not** the
  bar involution `q ↦ q⁻¹` (which FIXES the channels) — #3936.
- Under the standard nome `q = e^{2πiτ}`, `q ↦ −q⁻¹ ≙ τ ↦ ½ − τ`, a
  **holomorphic** modular involution — whereas Hodge conjugation is
  `τ ↦ −τ̄`, **anti-holomorphic**. So a holomorphic τ-functor cannot identify
  them directly: the unification requires the **fibre-level** complex-`q`
  reality structure (per the AGENTS.md Im(q) banner) to supply the
  anti-holomorphic ingredient — the correspondence is a fibre-level statement,
  not an observable-`q₀` one. (`2026-07-18-alpha-em-tau-correspondence.md`.)

## Honest forecast (outside view)

Statements 1–3 are one open conjecture. Closing it needs the categorical→
archimedean bridge (the τ-functor `q₀↔period` dictionary, or the RT 1-loop
determinant) — genuinely open, multi-session, uncertain payoff. Further *bounded*
probes will **refine the framing** (as #3920/#3925/#3936/the τ-correspondence
did) but will **not close** it. The per-loop measure is therefore best recorded
as **"honestly characterized: a proved skeleton `½·a₀` modulo one named
fibre-level correspondence"** — a phase-4 identification with a precise, single
open input, not diffuse numerology.

## Scope discipline (anti-laundering)

No CODATA read anywhere in the cluster; no convention tuned toward `8π`; every
forced row cites a proved invariant or exact algebra; the remaining conjecture is
stated as one named open input. No `α_k` wired; no fit; no tier change; `1/(8π)`
stays a phase-4 identification (R1 canonical status).

## Cross-references (the cluster)

- Count real-`b₁`: [`2026-07-18-alpha-em-multiplicity2-realcomplex-count.md`](2026-07-18-alpha-em-multiplicity2-realcomplex-count.md) (#3920)
- π-power adjudication: [`2026-07-18-alpha-em-pi-origin-adjudication.md`](2026-07-18-alpha-em-pi-origin-adjudication.md) (#3909)
- Reciprocal-form / Vol(J)=1 / located ½: [`2026-07-18-alpha-em-reciprocal-form-consolidation.md`](2026-07-18-alpha-em-reciprocal-form-consolidation.md) (#3925)
- Two-clause conjecture + three readings of the `2`: [`2026-07-18-alpha-em-perloop-conjecture-statement.md`](2026-07-18-alpha-em-perloop-conjecture-statement.md)
- Channel-swap involution `q↦−q⁻¹`: [`2026-07-18-alpha-em-channel-swap-involution.md`](2026-07-18-alpha-em-channel-swap-involution.md) (#3936)
- τ-correspondence holo-vs-anti-holo obstruction: [`2026-07-18-alpha-em-tau-correspondence.md`](2026-07-18-alpha-em-tau-correspondence.md)
- Derivability map (the wall): [`2026-07-14-alpha-em-2loop-derivability-map.md`](2026-07-14-alpha-em-2loop-derivability-map.md)
- Ledger: [`../coordination/alpha-em.md`](../coordination/alpha-em.md)
