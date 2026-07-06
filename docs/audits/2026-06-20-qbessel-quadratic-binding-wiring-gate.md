# Can the q-Bessel quadratic propagator improve mass/binding? Wiring gate: NO (not as-is)

**Date:** 2026-06-20
**Branch:** `claude/qbk2-binding-wiring-assessment-2026-06-20`
**Status:** Decisive wiring gate — derive-or-refute, no fit, **nothing wired**
**Bean:** [`qbk2`](../../.beans/qbk2--qbessel-2nd-kind-quadratic-action-binding-correction.md)
**Follows:** PR #2530 (gate), PR #2533 (off-shell resolvent)
**Script:** [`computations/qbeta/qbessel_quadratic_binding_wiring_gate.py`](../../computations/qbeta/qbessel_quadratic_binding_wiring_gate.py) (`GATE COMPLETE: DO NOT WIRE`)

## The owner's question

> "How would we use the q-Bessel quadratic propagator to improve mass/binding — and
> if we can Lean-prove it, wire it up?"

PRs #2530/#2533 established the admissible object: the coincidence-limit propagator
`G(w) = g₁(w)g₂(w)/D(w)` is finite/regular at the substrate origin (the 2nd kind
survives on-shell as a **bilinear**). The natural use is a one-loop / self-energy
correction to the binding sum:

```
δB  =  Σ_λ  y_λ · [ G(w_λ^atom) − G(w_λ^free) ],     one propagator per block, differenced.
```

This note runs the wiring gate **before** any wiring, on the real deuteron per-block
characters (`atom-chi-rust-d.witness.json`, n=6, 11 blocks).

## The gate: is the correction substrate-forced or a free knob?

A per-block correction needs two inputs per block λ. **The substrate fixes neither:**

| Input | What it is | Fixed by substrate? |
|-------|-----------|---------------------|
| `ν_λ` | the q-Bessel **order** on block λ | **No** — the Reeb/q-Bessel dictionary ties "order" to a rep level but pins no unique `ν_λ` per partition |
| `w_λ` | the q-Bessel **argument** | **No** — the block carries a Reeb phase `θ_λ = arccos/arccosh(χ_λ/dim_λ)`, but the map `θ → x → w=qx²` (`x=θ`? `x=sinθ`? `x=2sinh(θ/2)`?) is a functional **choice** |

If `δB` is stable across reasonable choices → forced → worth wiring. If it swings →
the map is a free knob → wiring it is the **forbidden 7th Δ_λ ansatz**.

## Result (deuteron, n=6)

| | Finding | Number |
|---|---------|--------|
| **Map-instability** | `S = Σ_λ[G(w_atom)−G(w_free)]` across 2 ν-rules × 3 argument maps | ranges **3.89 → 17.15**, relative spread **63%** |
| Cross-anchor | same `S` at q₀ vs the muon-anchor q | stable (~0.2%) — but irrelevant, swamped by map-instability |
| **Growth-sector share** | fraction of `|correction|` from growth blocks | **83%** — exactly the blocks that cancelled in the A≥3 scalar refutation |
| **Integer-order resonance** | physically-natural *integer* `ν` (rep levels) | **singular**: hits the Neumann log-resonance `q^k=q^ν` in `g₂` (`NaN`); only half-integer `SU_q(2)` spin labels are non-singular — and *which* is itself unforced |

## Verdict — DO NOT WIRE (four independent obstructions)

1. **Unforced argument map (decisive).** `δB` swings 63% in scale across equally-natural
   `(ν_λ, w_λ)` choices. The map is a free functional knob → a per-block propagator
   multiplier is a disguised **7th Δ_λ ansatz**, which the standing discipline forbids
   (AGENTS.md Δ_λ gate; six closures + GAP-A-4's 22 are CLOSED).
2. **Growth-sector cancellation.** 83% of the correction lives in the growth blocks —
   exactly those that cancelled in `|tr_free|−|tr_atom|` and refuted every A≥3 scalar
   observable (`binding_reeb_phase_decomposition.py`).
3. **Integer-order resonance.** The natural integer rep-levels are the singular
   logarithmic-Neumann case the power-series `g₂` does not cover.
4. **Mixed bar-parity** (PR #2533): `G`'s sector under `q→1/q` is ν-dependent — no
   definite parity for a clean mass term.

## What this means for "if we can Lean-prove it, wire it up"

- **The wireable Lean lemma is the q-Bessel Casoratian regularity** (`D` obeys q-Abel
  `D(qw)=q^{−ν}D(w)`; `G→1/(q^{−ν}−1)`). It is clean and provable — **but it is a
  q-Bessel FACT, not a binding claim.** Proving it does not make `δB` real, so it is
  **not** a production wiring (no `appendix-mass-binding-algorithms` change is warranted).
- **What would unblock a wiring** (the legitimate path, not taken here): an
  *independent substrate derivation* that **forces** the order `ν_λ` and argument map
  `w_λ` per block (so `δB` is parameter-free), surviving the free−atom difference with a
  definite bar-parity. Until that derivation exists, wiring is a fit.

The owner's "quadratic action" intuition is **structurally correct** — the propagator
is the right admissible object (PRs #2530/#2533) — but it does **not** yield a
parameter-free mass/binding correction without first deriving the order+argument map
from the substrate. No fit; nothing wired; `c_k`/`Δ_λ` stay cal-anchored. Owner closes
the bean (§4a).
