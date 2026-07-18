# μ̄-idempotent for the mixed-multibond channel — the common-weight form fails Milnor integrality

**Date:** 2026-07-18 · **Branch:** `claude/h4-exponents-value-screen-96501m` ·
**Probe:** [`computations/deltalambda/mixed_multibond_mubar_integrality_probe.py`](../../computations/deltalambda/mixed_multibond_mubar_integrality_probe.py)
(+ witness) · **Scope:** (a); EXPLORATORY; no fit; nothing wired; no tier change.
**Owner steer (2026-07-18):** "work on derived μ̄-idempotent / SDP-knot-ID invariant."

## What this settles

The mixed-multibond miss (Model G open trio;
[`2026-07-14-mixed-multibond-interface-derive-or-refute.md`](2026-07-14-mixed-multibond-interface-derive-or-refute.md))
is a shared, sub-additive channel. That audit's next-step #1: *"one |μ̄|-idempotent
per light cluster, not per bond"* — the shared channel is the Milnor triple-linking
(μ̄_ijk) content of the light cluster bridging `m` α's. This probe tests the
**simplest** such form and refutes it, using the corpus's own Magnus μ̄ machinery
([`binding_mn_milnor_linking.py`](../../computations/binding_mn_milnor_linking.py)).

## The test — Milnor integrality vs the t-series

A light cluster `X` bridging `m` α's carries `C(m,2)` potential Borromean triples
`(αᵢ, αⱼ, X)`. **Milnor μ̄_ijk is an integer** — the coefficient in a Magnus
expansion of the longitudes (verified in the probe: Borromean μ̄₁₂₃ = 1, chain
μ̄₁₂₃ = 0). So the simplest μ̄-idempotent — a **common scalar weight** `w` times the
(signed) integer count of triples — predicts `channel(m) = w · S(m)` with
`S(m) ∈ ℤ`, `|S(m)| ≤ C(m,2)`.

Taking the single triple at `m=2` as the unit (`w = channel(2) = 6.44 MeV`), the
pure t-series (⁷Li, ¹¹B, ¹⁵N, ¹⁹F) shared channel is:

| iso | m | C(m,2) | channel (MeV) | channel/w | nearest ℤ | off (triples) |
|---|--:|--:|--:|--:|--:|--:|
| ⁷Li | 1 | 0 | 0.12 | (≈0) | 0 | — |
| ¹¹B | 2 | 1 | 6.44 | 1.00 | 1 | 0 (unit) |
| ¹⁵N | 3 | 3 | 7.84 | **1.22** | 1 | 0.22 |
| ¹⁹F | 4 | 6 | 2.26 | **0.35** | 0 | 0.35 |

¹⁵N wants 1.22 triples and ¹⁹F wants 0.35 — **neither is an integer**, and ¹⁹F's
2.26 MeV cannot be the "0 triples" its nearest integer would demand. **Robust to
±5% (b,g)** across all four sign corners (¹⁵N stays 1.15–1.28, ¹⁹F 0.17–0.52 — never
integer).

## Verdict (scope-(a), NOT (b))

The μ̄-idempotent with a **common scalar weight and an integer Borromean-triple
count** does **not** reproduce the mixed-multibond t-series. Cited invariant:
**μ̄_ijk ∈ ℤ** (Milnor 1954; Magnus integrality).

This is **construction-limited (a)**, not a structural exclusion of the
μ̄-idempotent ingredient:

- A **q-weighted per-triple magnitude** — each triple dressed by its own per-block
  weight `a_D^{(2)}·w_2` / Hoefsmit block (the Part-6 dressing of
  [`binding_production_link_milnor.py`](../../computations/binding_production_link_milnor.py))
  — is **not tested here and survives**. The non-integer ratios 1.22 / 0.35 are
  exactly what a per-triple **q-weight** (non-common, block-dependent) would supply.
- That dressing **is** the confinement-SDP per-block weight — the environment-blocked
  9b piece (SDP active set → bond graph → per-block weights; needs cvxpy/Clarabel +
  the Hecke operator data, absent in this sandbox).

## What it narrows the invariant to

The derivation reduces to a precise, named target: the shared channel is **not** a
bare topological Borromean count. It is `Σ_triples w_triple · μ̄_triple` with a
**q-weighted, block-dependent** `w_triple` — so closing it requires the
**SDP-derived per-block weights**, not merely the link topology. The μ̄ topology
(computable in-sandbox, integer) fixes *which* triples are active; the *magnitude*
that makes the t-series non-integer must come from the per-block q-dimension the
SDP dual selects. This is the concrete complement to the audit's cone prune: the
cone prune excluded additive non-negative countings; this excludes the
common-weight integer-μ̄ count, leaving the **q-weighted** μ̄-idempotent as the
surviving form and locating its missing input (the SDP per-block weight).

## Coordination

Complements #3808 (Model-G rounds 8–11 / mixed-multibond) — this prunes the
bare-integer μ̄ reading of their next-step #1 without touching the
saturating-channel / t-series scope. Intent to post on #3808.

## Provenance

Magnus μ̄ machinery replicated from `binding_mn_milnor_linking.py` (pure integer
arithmetic — no SnapPy/cvxpy). AME2020 via `codata_constants._ame_binding_mev`;
`b = 0.78192`, `g = 2.4155` from the committed Model-G ledger. mpmath 40-dps;
exact rational binding differences. Witness assertion gates on integrality +
non-integer-multiple + ±5% robustness.
