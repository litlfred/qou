# α_EM B2 lift — the vertex-local τ model over ℂ (2026-07-18)

**Bean:** `qou-tq20` (B2 lift), second tranche — after #3985 opened the
Mathlib gate and pinned the lift as the content-bearing class
`TauRhoHodgeLift` (no instance).

**Lean (this PR):** [`QOU/Archimedean/VertexLocalTauModel.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/VertexLocalTauModel.lean)
— sorry-free, `lean`-direct exit 0 with Mathlib (lint-clean).

**Scope guard (STRICT):** no axiom; no instance fabricated; nothing wired;
`1/(8π)` stays phase-4.

## What this tranche adds

The original `qou-tq20` target is the **vertex-local τ statement**: τ sends
the `H₂(i)`-module to the vertex tangent module where `dU` acts by the
multiplier `i` (the #3942 geometric carrier), intertwining ρ with
conjugation. This module formalizes the **ℂ-level model on both sides** of
that statement — upgrading the merged GInt shadow to the analytic type where
the obstruction actually lives (B1 #3955: the whole issue is ℂ-linear vs
ℂ-anti-linear; nome-independent per #3949; the GInt shadow could only mirror
that combinatorially).

Proved sorry-free over genuine ℂ:

| Theorem | Content |
|---|---|
| `hecke_relation_at_i` | the concrete Jordan block `σ = !![i,1;0,i]` satisfies `σ² = 2i·σ + 1` — the Hecke relation at `q = i` (`q − q⁻¹ = 2i`): the block **is** an `H₂(i)`-module |
| `jordan_nilpotent`, `not_semisimple` | `(σ − i·1)² = 0`, `σ ≠ i·1` — the degenerate confluence: eigenvalues coincide, the module is a genuine nontrivial Jordan block, and only its **semisimplification** acts by the scalar `i` = the vertex multiplier `dU\|_V` |
| `rho_carries_module` | `σ.map(starRingEnd ℂ) = σ̄` (the `q = −i` block) — the **genuinely anti-linear** statement of ρ's action on the module pair |
| `hecke_relation_conj` | `σ̄² = −2i·σ̄ + 1` — the conjugated Hecke relation at `q = −i` |
| `shadow_unique_complex` | the #3960 forced-assignment theorem transported to ℂ conjugation (`Complex.conj_I` carries the exchange) |
| `multiplier_order_four` | `i⁴ = 1`, `i² = −1` — the #3942 order-4 eigendata at scalar level |

## Why it matters for the lift

The `TauRhoHodgeLift` discharge requires constructing the loop weights from
the categorical side. The categorical side's degenerate-locus data is now
formalized over ℂ: the non-semisimple `H₂(i)` Jordan module whose
semisimplification is the scalar `i`, with ρ carrying it anti-linearly to
the `q = −i` partner — exactly matching the geometric carrier's multiplier
pair. Both endpoints of the lift are now stated in the same language
(`Matrix _ _ ℂ`, `starRingEnd ℂ`) as the interface class.

## Open remainder (unchanged)

The functor itself: exhibiting the `TauRhoHodgeLift` instance for the actual
α_EM loop weights. The model supplies both endpoints; it does not construct
the functor between them.
