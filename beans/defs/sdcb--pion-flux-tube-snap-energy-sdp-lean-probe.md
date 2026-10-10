---
# sdcb
title: 'probe: pion flux-tube snapping energy ≡ SDP solution — Lean sense-check'
status: completed
type: task
priority: normal
created_at: 2026-08-02T17:40:00Z
updated_at: 2026-08-02T18:05:00Z
---

## Problem

Does it make sense / is it probable in Lean that the pion "flux-tube snapping"
energy equals the SDP solution (from prop:operator-selection-lp /
prop:confinement-sdp)?

## Context

- In QCD, flux-tube snapping = string breaking; the snap energy ≈ m_π ≈ 139.57 MeV.
- In QOU, the SDP (confinement-operator-selection.py) minimises the Frobenius
  action and picks the canonical T_w ∈ H_n(q_0); its crossing_energy is in
  units of m_e.
- The pion braid is σ₁σ₂^{-1} (half-figure-eight) per pion-half-figure-eight.ts.
- prop:operator-selection-lp selects the minimum-action Wedderburn block;
  its dual gives shadow prices = binding shadow energies.

## Tasks

- [x] Units audit: what are the units of E_cross in confinement-operator-selection.witness.json?
- [x] Identify the SDP optimal value vs pion mass ratio.
- [x] Check whether pion braid (σ₁σ₂^{-1}) is a candidate in the SDP.
- [x] Assess Lean formalizability: is there a path to a sorry-free Lean proposition?
- [x] Write up the verdict: probable / not-probable / scope-limited-negative.

## Findings

### Units audit

`E_CROSS = ½(q - q⁻¹) = ½HA ≈ 0.10453` (dimensionless, defined in
`qou_substrate/constants.py` line 99). In MeV: `E_CROSS × m_e ≈ 0.0534 MeV`.

`crossing_energy(vec) = Σ |vec[i]| × degrees[i] × E_CROSS` so the SDP
crossing energies for all candidates are in the range **0.05–0.27 m_e**
(≈ 0.026–0.14 MeV).

### Pion mass vs SDP scale

| Quantity | Value |
|---|---|
| m_π (CODATA) | 139.57 MeV |
| E_CROSS × m_e | 0.0534 MeV |
| L+ (σ₀σ₁) crossing energy | 0.0775 MeV |
| Proton B₃ crossing energy | 0.0737 MeV |
| m_π / (E_CROSS × m_e) | **~2613×** |

The SDP crossing energy scale is **~2613× smaller** than m_π. The claim
"pion snap energy = SDP solution" is wrong by three orders of magnitude.

### Pion in the SDP candidates

The pion braid L+ = σ₀σ₁ is present as a candidate in the SDP with
`n_demand=0` (no confinement demand; it's a free channel, not a bound state).
It is NOT the SDP minimum-action winner — that is B₃ (proton/neutron).

### Structural role conflict

- The SDP objective is the **confinement-operator selection**: picks the
  Hecke element T_w that minimises the Frobenius action under confinement
  demand constraints. It selects the **bound-state operator**, not a decay scale.
- Pion "flux-tube snapping" is a **meson pair-production / decay** channel —
  structurally the *bar-odd sinh* partner (`Q_β ≈ 0.784 MeV`), not the
  bar-even meson scale.
- m_π is **CAL-3** in QOU (an input calibration), not derived from the SDP.

### LP dual fields

The confinement witness has `y0_star = null`, `dual_obj = null`, etc.
(stubs — not yet populated via `lp_dual_solver.py`). Even if the dual
were populated, the shadow price y0* (= Lagrange multiplier per net demand
unit) would not equal m_π dimensionally.

### Lean formalizability

**NOT probable as stated.** There is no structural path in the current
framework from `prop:operator-selection-lp` to a statement like
`E_snap_pion = y0_star`. Specifically:
- The scale mismatch is ~2613× — not a unit-normalisation issue.
- The SDP selects a **confinement operator** (bound state), not a decay energy.
- m_π is a calibration input (CAL-3), not a prediction in the current framework.
- The Lean proof state (confinement-nf-partial-proof.md): T₁+T₃ proved,
  T₂ conditional on `conj:crystal-graph-realization`; no sorry-free path
  to a pion-mass identification.

### Scope classification (AGENTS.md §"Before declaring refuted")

**(a) Scope-limited negative:** "The SDP crossing_energy functional, evaluated
on the pion braid L+, does not reproduce m_π as-is. The scale is wrong by
~2613×."

A *structural* path that might connect the two:
- If the SDP dual shadow price y0* (not yet computed, dual stubs are null)
  is interpreted as an energy per Frobenius demand unit, and if the demand
  normalization absorbs the m_e→m_π factor (~273), a relationship could
  exist dimensionally — but this would require a separate derivation, not
  the current SDP setup.

## Verdict

**NOT probable in Lean as stated.** The identification requires a framework
extension (populating the LP dual, reinterpreting the shadow price in pion
mass units) that does not exist in the corpus. The current SDP infrastructure
selects the confinement operator; it does not predict m_π. Follow-up
direction: investigate whether the LP dual y0* (once populated) has any
ratio relationship to m_π / m_e = 273.
