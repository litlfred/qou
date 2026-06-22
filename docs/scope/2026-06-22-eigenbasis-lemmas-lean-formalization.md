# Lean formalization of the eigenbasis structural lemmas L1–L3

**Branch:** `claude/eigenbasis-lemmas-lean-2026-06-22`
**Follows:** merged PR #2502 (eigenbasis structural lemmas, verified exact-symbolic)

## Context

PR #2502 added `computations/probes/eigenbasis_structural_lemmas_probe.py`,
which verifies three structural lemmas **exact-symbolic** and records a
`lean_followup` in its witness:

> formalize L1–L3 as lemmas in `QOU/BraidKnot` (L1, L2) and as a one-line
> corollary of `RibbonTwistEigenvalue` (L3).

This branch turns the verified-symbolic facts into **Lean theorems**, the
genuine gap-closure (the probe verifies; Lean proves).

## Approach — the abstract-structural pattern

Follow the existing
[`QOU/BraidKnot/ChiralityWritheRibbon.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/ChiralityWritheRibbon.lean):
model the categorical inputs as abstract structures
(`WedderburnChannel { kappa, weight }`, `HeckeCharValue { val }`) and the
ribbon-twist eigenvalue θ_λ = q^{2κ_λ} as the axiom class
`RibbonTwistEigenvalue`. State each lemma as a **sorry-free** theorem,
conditional on that class where the categorical input is needed (§3b-cond
conditional-class discipline) — never a vacuous self-assuming projection.

New file: `QOU/BraidKnot/EigenbasisStructuralLemmas.lean`.

| Lemma | Statement | Plan | Risk |
|---|---|---|---|
| **L3** framing GF | `Σ_m t^m χ_λ(β·Δ^{2m}) = χ_λ(β)/(1 − t·q^{2c(λ)})` | framing by Δ^{2m} scales χ_λ by θ_λ^m (from `RibbonTwistEigenvalue` + `q^{2mκ}=(q^{2κ})^m`); finite geometric closed form `(1−tθ)·Σ_{m<N} (tθ)^m χ = χ(1−(tθ)^N)`. | low — clean corollary, infra exists |
| **L1** order-parity | χ_λ(β) Laurent exponents ≡ L (mod 2), ∀λ | abstract odd-Laurent-degree crossing factors ⇒ length-L product (and its trace) has degree ≡ L (mod 2). | medium — parity bookkeeping |
| **L2** bar-involution | χ_λ(1/q) = ε_λ χ_{λ'}(q), ε_λ ∈ {±1} | the q↔−q⁻¹ seminormal eigenvalue swap = V_λ≅V_{λ'} intertwiner. | high — must be derived, not axiomatized, to avoid a vacuous projection |

## Discipline

- **Sorry-free** where a theorem is claimed proved; verified `lean`-direct
  against the restored `lake-cache/qou-v4-24-0` oleans.
- **Conditional-on-class** where a categorical axiom is genuinely needed
  (L3 takes `[RibbonTwistEigenvalue q]`), with the explicit-hypothesis
  banner per AGENTS.md §3b-cond.
- **No overclaim** — if L2 cannot be made non-vacuous this session, it lands
  as an honest conditional-class statement or is scoped to a follow-up,
  not a `: True := trivial` stub.
