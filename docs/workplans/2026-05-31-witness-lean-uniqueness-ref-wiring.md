# Witness `lean_uniqueness_ref` wiring workplan

> **⚠ SUPERSEDED 2026-06-09** — folded into Phase 3 of
> [`2026-06-09-overall-strategy-update.md`](2026-06-09-overall-strategy-update.md).
> Consult the overall strategy doc first for "what's next" routing.
> This document remains on-disk for historical reference; the per-producer
> status table below is still the authoritative source for the wiring
> campaign's per-script status.

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

## Status accounting

| Layer | Wired | Total | Coverage |
|---|---:|---:|---:|
| Lean modules → atlas | 1 / 1 | 1 | 100% (this PR) |
| Atlas .ts manifest | 1 / 1 | 1 | 100% (this PR) |
| Per-nucleus witnesses | 1 / ~15 | 15 | ~7% (Phase 1+2 in flight) |
| Per-atom witnesses | 0 / ~20 | 20 | 0% (Phase 3 queued) |
| Compute-integration-watcher | 0 / 1 | 1 | 0% (separate PR queued) |

Total infrastructure wiring: ~10% complete. The wiring pattern is
established by this PR; subsequent PRs apply it systematically.
