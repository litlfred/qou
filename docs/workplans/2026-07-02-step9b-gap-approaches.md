# Workplan — Step 9b per-isotope binding: approach selection across the four sub-gaps

**Branch**: `claude/canonical-derivation-gaps-vuu01v`
**Date**: 2026-07-02
**Status**: survey in progress (this stub will be filled with the corpus-state
summary and the chosen approach per sub-gap).

## Scope

Step 9b of the canonical derivation chain
([cheat sheet §0](../canonical-derivation-cheat-sheet.md)) — the 🔴 open gate —
decomposed into four sub-gaps:

1. **q₀^(10A−5) residual** — trace-canonical `Δ_λ(K) ≈ q₀^(10A−5)`
   (D exact to 0.01 q₀-units, ³He off −1.40, Z-dependent). Task:
   derive-or-refute the exponent from W_free vs W_atom crossing/jet
   bookkeeping (formalize-first).
2. **Per-depth α_k assignment rule** — tower coefficients structural
   (z² Markov at k=2, m_e·8G plateau at k≥4) but the depth-assignment is
   empirical; tower undershoots D −73% … ⁴He −50%.
3. **Many-body series not closed** — pairwise bond-sum captures 26% of
   ⁴He; canonical link-volume assignment per nucleus, the ρ·A scale rule,
   and 2/3/4-body reconciliation all open.
4. **Brane-tower normalization** (PR #3016) — Borromean single pipeline
   converges ∀Z with the right shape, wrong normalization: the missing
   per-λ weight.

## Method

Per the formalize-first probe discipline (AGENTS.md): survey the corpus
first (three parallel sweep agents over audits/computations/coordination
ledgers), then for each sub-gap identify the structural invariant that
prunes the hypothesis class before running any probe. Findings and the
per-gap approach decision land here.
