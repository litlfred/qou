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

New file: `QOU/BraidKnot/EigenbasisStructuralLemmas.lean` (registered in the
`QOU.BraidKnot` aggregator).

| Lemma | Lean theorem(s) | Status |
|---|---|---|
| **L3** framing GF | `framing_gf_closed_form` (geometric closed form `(1−tθ)·Σ = c₀·(1−(tθ)^N)`, single pole at `t=θ⁻¹`) + `framing_eigenvalue_pow` (`q^{2mκ}=(q^{2κ})^m`) | ✅ **sorry-free** |
| **L1** order-parity | `character_qneg_parity` — `q↦−q` form: `χ(−q)=(−1)^L·χ(q)` (≡ Laurent exponents ≡ L mod 2, since `q^k↦(−1)^k q^k`) | ✅ **sorry-free** |
| **L2** bar-involution | `character_bar_conjugate` + `character_bar_conjugate_sign` — §3b-cond: factor-level seminormal bar↔conjugate relation (input) ⟹ derived `χ_λ(q⁻¹)=s^L·χ_{λ'}(q)`, `ε=s^L∈{±1}` | ✅ **sorry-free** |

All three verified `lean`-direct against the restored `lake-cache/qou-v4-24-0`
oleans (exit 0, no warnings, no `sorry`).

## Discipline

- **Sorry-free** where a theorem is claimed proved; verified `lean`-direct
  against the restored `lake-cache/qou-v4-24-0` oleans.
- **Conditional-on-class** where a categorical axiom is genuinely needed
  (L3 takes `[RibbonTwistEigenvalue q]`), with the explicit-hypothesis
  banner per AGENTS.md §3b-cond.
- **No overclaim** — if L2 cannot be made non-vacuous this session, it lands
  as an honest conditional-class statement or is scoped to a follow-up,
  not a `: True := trivial` stub.
