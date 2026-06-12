# Witness `lean_uniqueness_ref` wiring workplan

**Date:** 2026-05-31
**Branch:** `claude/atlas-sdp-uniqueness-full-wiring-2026-05-31`
**Goal:** wire every per-nucleus / per-atom witness JSON to its
corresponding SDP-uniqueness Lean theorem from PRs #1537, #1542.

## Context

The parameterised SDP-uniqueness infrastructure landed in PR #1537
(generic module + 10 QOU isotopes + 118 elements) and PR #1542
(252 stable isotopes) is currently **not consumed** by the
computation-side witnesses. This workplan tracks the wiring
campaign to close that gap.

## Wiring pattern

Each per-nucleus / per-atom witness producer should add a
`lean_uniqueness_ref` field via `WitnessBuilder.add_data`:

```python
w.add_data("lean_uniqueness_ref", {
    "<nucleus>": "qou:QOU.BraidKnot.<wrapper>_uniqueness_closed",
    "framework_doc":
        "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
    "note": "...",
})
```

The reference uses the named wrapper at the most-specific
granularity available:
- Per-isotope wrapper if the nucleus is QOU R5-full-tracked
- `<element>_uniqueness_closed` from `PeriodicTableUniqueness` for
  AME2020 reference isotope
- `<element><A>_uniqueness_closed` from `StableIsotopeUniqueness` for
  stable nuclides
- `@nucleus_uniqueness_closed (3*A)` generic fallback

## Producers to wire

### Phase 1 — high-priority core producers

| Producer | Witness | Status |
|---|---|---|
| `m_p_substrate_identity_50dps.py` | `m-p-substrate-identity-50dps.witness.json` | ✅ wired (this PR) |
| `m_p_borromean_verification_50dps.py` | `m-p-borromean-verification-50dps.witness.json` | queued |
| `m_p_spectral_corrected_50dps.py` | `m-p-spectral-corrected-50dps.witness.json` | queued |
| `proton_mass_codata_50dps.py` | `proton-mass-codata-50dps.witness.json` | queued |
| `proton_mass_full_tower_50dps.py` | `proton-mass-full-tower-50dps.witness.json` | queued |

### Phase 2 — per-nucleus probes

| Producer | Witness | Status |
|---|---|---|
| `deuteron_tr_M_symbolic.py` | `deuteron_tr_M_symbolic.witness.json` | queued |
| `tritium_8_11_jones_markov_probe.py` | `tritium-8-11-jones-markov-probe.witness.json` | queued |
| `tritium_interface_decomposition.py` | `tritium-interface-decomposition.witness.json` | queued |
| `m_p_m_e_li2q.py` | `m-p-m-e-li2q.witness.json` | queued |

### Phase 3 — atom-binding probes

| Producer | Witness | Status |
|---|---|---|
| Helium-4 binding | various | queued |
| Lithium-6 binding | various | queued |
| Carbon-12 binding | various | queued |
| ... | various | queued |

## Cross-checks

- **Compute-integration-watcher** (`audit-wiring.ts`, item 4 of
  the user's wiring picks) should be extended to validate that
  every per-nucleus computation has a `lean_uniqueness_ref` field
  pointing to a real Lean wrapper. Audit run flags missing fields.
- **Atlas wiring** — `recursive-atom-knot-atlas.ts` now declares
  `conj:canonical-knot-id-sdp` in `uses[]` (this PR), tying the
  atlas content block to the underlying SDP-uniqueness conjecture
  (which the parameterised theorems prove the abstract version of).
- **Atlas Lean stub** replaced with real consumer module
  `QOU.BraidsAndKnots.recursive_atom_knot_atlas` (this PR) that
  imports the per-isotope wrappers and provides per-atlas-entry
  named theorems (`atlas_deuteron_uniqueness`, etc.).

## Status accounting (closing — 2026-06-12)

The campaign ran as batches 1–5 (#2190, #2193, #2196, plus the
batch-4/5 commits) and closes here. Two **distinct** completion
measures must not be conflated:

| Measure | State | Notes |
|---|---|---|
| **Producer-side wiring** (code) | **exhausted** | 75 producers call `lean_uniqueness_ref(...)`. An authoritative scan (every witness-*writing* producer whose constructed witness name matches the per-nucleus heuristic) reports **0** remaining unwired. The final 3 near-miss siblings (`probe_4_li6_rectangular_conjecture.py`, `probe_4d_li6_aggressive_scan.py`, `sublemma_2_1_h12_he4_branching.py` — basename-suffix variants the batch-5 codemod skipped) are wired in this PR. |
| **On-disk witness coverage** (audit) | 12 / 114 (10.5%) | This lags producer-side because the field is written **at producer runtime**; the on-disk `*.witness.json` files only gain the field when CI regenerates them. CI witness regeneration is currently billing-blocked, so this number will rise on the next green witness-pipeline run — **no further code change is required** for it to climb. |

### Genuine remainder (NOT code-wirable)

- **~28 orphaned-legacy witnesses** carry no `scriptFile` (pre-`WitnessBuilder`
  era) or name a deleted producer (e.g. `chi-helium-4-h12-at-q0-50dps`,
  `tau-hat-n-proton-level-1-empty`). These cannot be wired by editing a
  producer — they need migration triage (regenerate via a current producer,
  or accept as frozen legacy). Tracked as a follow-up, not part of this
  wiring campaign.
- **χ-evaluation / cache witnesses** (`chi-*`, `y_lambda-*`, `vol-density-*`)
  whose producers *do* write per-nucleus names are already wired where the
  producer is live (`delta_lambda_empirical_tabulation.py`,
  `chi_4he_via_rust_lossless.py`). No separate scope decision was needed:
  the SDP-uniqueness ref rides the producer, and a live producer either
  already carries it or was caught by the authoritative scan above.

**Bottom line:** the producer-side pool is exhausted; the wiring pattern
is fully propagated. Remaining audit "misses" are CI-regeneration lag
(self-clearing) plus orphaned-legacy witnesses (migration triage).
