# Δ_λ magnitude: it's the graded trace `tr(g_ρ)` — a classical (q=1) dimension, not the substrate q₀

**Date:** 2026-07-11 · **Axis:** Δ_λ closure (strong sector), magnitude ·
**Follows:** the sign capstone [`2026-07-11-deltalambda-sign-pivotal-grading-capstone.md`](2026-07-11-deltalambda-sign-pivotal-grading-capstone.md) (#3529) ·
**Gate:** Track-A / Subgoal-2 — **owner-reversed** for this *reduction* (no fit, no wiring) ·
**Tier:** symbolic-exact + mpmath (parameter-free).

## Scope of the reversal

The owner authorised opening the gated Δ_λ **magnitude** question. This audit records a
**formalize-first reduction**, not a derivation: it shows the magnitude is not a seventh
weight-ansatz and prunes the substrate q-dimension, reducing the whole closure to one
object. It **does not** construct that object from the drivers — per "Axiomatization is
NOT a Proof," the binding compute stays blocked until a driver-level construction exists.

Probe [`deltalambda_magnitude_graded_trace_probe.py`](../../computations/deltalambda/deltalambda_magnitude_graded_trace_probe.py)
→ [witness](../../computations/deltalambda/deltalambda-magnitude-graded-trace.witness.json) (3/3).

## The reduction

The sign is the principal grading `g_ρ` at ζ₄ (`g_ρ|_{V_λ} = (−1)^{n(λ)}·id`; #3529).
Since `Δ_λ = sgn(w₀^{S_{λ'}})·dim(λ)`:

- **(1) Δ_λ = tr_{V_λ}(g_ρ) = (−1)^{n(λ)}·dim(λ).** The magnitude `|Δ_λ| = dim(λ)` is the
  ordinary dimension carried by the **same** object whose trace gives the sign. So the
  magnitude is **not a separate weight to fit** — the six failed ansätze (co-Casimir,
  Demazure, LP×2, crystal, Wenzl) were constructing Δ_λ as a *direct weight*; the
  graded-trace form says the closure is "construct `g_ρ`, take its trace."
- **(2) The magnitude is the classical q=1 dimension, not the substrate q₀
  quantum-dimension.** The q-hook-length quantum dimension `dim_q(λ; q₀) = [n]_q!/∏[h]_q`
  at `q₀ ≈ 1.11` differs from the integer `dim(λ)` by up to **4.41%** (e.g. [3,2]:
  `5.22` vs `5`). `|Δ_λ|` is exactly the integer — so the magnitude anchor is **q=1**,
  not q₀. This **prunes** the substrate q-dimension as the magnitude source.
- **(3) Δ_λ is a two-anchor object.** Magnitude at **q=1** (classical dimension) ⊗ sign at
  **ζ₄** (grading). The substrate `q₀ ≈ 1.11` (real, > 1) is **neither** anchor —
  consistent with the whole session's fibre-vs-archimedean theme.

## What this buys, and what it does not

- **Buys:** the magnitude is demystified (it's the ordinary dimension = graded trace),
  the substrate q-dimension is pruned, and the entire six-ansatz closure problem collapses
  to a **single** object: the principal grading `g_ρ`.
- **Does not buy:** a derivation of `g_ρ`. Constructing the `q^{2ρ}`-type principal
  grading (classical q=1 dimension ⊗ ζ₄ sign) as a canonical categorical morphism from
  the **13 drivers** is the **reduced open problem** — formalize-first, not yet done. This
  reduction unlocks **no** downstream binding compute (Anti-Laundering / "Axiomatization
  is NOT a Proof").

## Reduced open problem (for the record)

> Construct `g_ρ` — the principal (ρ) grading realizing `(−1)^{n(λ)}` at ζ₄ with the
> classical q=1 dimension — as a canonical morphism from the 13 categorical drivers.
> Then `Δ_λ = tr(g_ρ)` closes the per-isotope binding formula `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ`.

## Cross-references

- Sign capstone: [`2026-07-11-deltalambda-sign-pivotal-grading-capstone.md`](2026-07-11-deltalambda-sign-pivotal-grading-capstone.md) (#3529)
- Narrowing: [`2026-07-11-deltalambda-sign-operator-narrowing.md`](2026-07-11-deltalambda-sign-operator-narrowing.md) (#3523)
- Selection-rule engine (on main): `QOU/SelectionRules.lean`
