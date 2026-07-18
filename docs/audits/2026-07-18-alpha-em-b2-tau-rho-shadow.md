# α_EM τ-correspondence, bean B2 (shadow level) — the ρ↔Hodge dictionary is FORCED

**Date:** 2026-07-18 · **Axis:** the `1/π` correspondence wall (milestone `qou-b5qg`, bean
`qou-tq20`) · **Tier:** machine-verified shadow theorems (Lean core, sorry-free) + the
functorial lift honestly left open (Mathlib-gated) · **Derives no clause of the per-loop
conjecture; no fit; nothing wired; `1/(8π)` stays phase-4.**

Lean [`QOU/Archimedean/TauRhoHodgeShadow.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/TauRhoHodgeShadow.lean)
(`lean`-direct exit 0, sorry-free; imports the #3942 carrier module).

## The B2 statement and what is now proved

B2: *τ intertwines the fibre reality structure `ρ = conj` (B1, merged) with the Hodge
conjugation of `H¹(Bring)`.* At the degenerate locus this statement determines a unique
shadow, now machine-verified:

- **`hodgeShadow`** — the assignment `q=i ↦ H^{1,0}` (`true`), `q=−i ↦ H^{0,1}` (`false`).
- **`shadow_norm` / `shadow_intertwines`** — it satisfies the B1 dictionary (normalization
  + ρ-equivariance `hodgeOf(conj z) = ¬hodgeOf(z)` on the pair).
- **`shadow_unique`** — **any** assignment satisfying normalization + ρ-intertwining agrees
  with `hodgeShadow` on the whole pair: **the dictionary is forced — zero freedom at the
  shadow level.**
- **`shadow_multiplier_compat`** — the assignment matches the geometric carrier's `dU = J`
  eigendata at the vertices (`U·V = i·V`, `U·conj(V) = −i·conj(V)`; #3942).

## The honest open remainder of B2 (Mathlib-gated)

The **functorial lift**: that the categorical τ-functor itself carries `ρ` to the Hodge
conjugation — a statement about the actual functor between the braided category and the
geometric side, requiring category-theoretic apparatus not available in Lean core (and the
sandbox Mathlib build is network-blocked). The shadow theorems establish that the lift has
a **unique candidate and no consistency obstruction** at the degenerate locus. The bean
stays open for the lift; B3 (`qou-cncc`) can proceed conditionally on it.

## Scope guard (STRICT)

Shadow-level proofs only; the functorial claim is *not* asserted (no laundering — per
§"Axiomatization is NOT a Proof", no class/axiom stands in for the lift). No fit; nothing
wired.

## Cross-references

- Proof plan: milestone `qou-b5qg` — B1 merged (#3955), B2 shadow (this PR), B3–B5 queued
- B1: `2026-07-18-alpha-em-b1-fibre-reality-structure.md` (merged)
- Carrier: `QOU/Archimedean/SigmaJGeometricCarrier.lean` (#3942, merged)
