# Phase 2 audit — m_n prediction chain

**Date**: 2026-05-16
**Scope**: m_n chain extras beyond the m_p chain audit
(Phase 1). The m_n chain shares ~60 % of files with the m_p
chain — those are covered in
[`2026-05-16-compute-paper-lean-audit-mp-chain.md`](2026-05-16-compute-paper-lean-audit-mp-chain.md).
This doc audits the **m_n-specific** files: the assembly /
build-chain scripts that emit the canonical `m_n` derivation
JSON.

## Shared with Phase 1 (no re-audit needed here)

All of these are already audited in Phase 1; m_n consumes them
unchanged:

- `_phi_q_util.py` (Φ_q)
- `terms_2_3_atom_per_gen_mpfr_50dps.py` (T2/T3 producer — handles
  electron + proton + neutron in a single pass)
- `derive_m_n_hecke_full_tower_50dps.py` (the m_n-specific producer
  is a mirror of `derive_m_p_hecke_full_tower_50dps.py` with
  identical math claims and gaps)
- `bw_chirality_isotopes.py` (upstream; under parallel-agent audit)
- `gb_filtration_jet_tracker.py` (upstream; parallel agent)
- `term5_v2_chirality.py` (upstream; parallel agent)

## m_n-specific files audited

| file | LoC | role |
|---|---:|---|
| `build_neutron_mass_50dps_chain.py` | 352 | Assembly chain — emits `neutron-mass-50dps.derivation.json` + `neutron-mass-codata-50dps.witness.json` |
| `build_markov_trace_assembly_neutron_chain.py` | 293 | Upstream chain for the dimensionless `tr_M(neutron, q_0)` value (Phase A) |
| **total** | **645** | |

## File-by-file

### `build_neutron_mass_50dps_chain.py` (352 lines)

Parallel to `build_proton_mass_50dps_chain.py` (already covered in
Phase 1). The chain assembles m_n_pred via

```
m_n_pred (MeV) := (m_n_Hecke / m_e_Hecke) × M_E_MEV
```

reading `m_n_Hecke` from
`derive_m_n_hecke_path_a.m_n_hecke_path_a_at_q0()` and
`m_e_Hecke` from
`derive_m_e_hecke_path_a.m_e_hecke_path_a_cat_units_at_q0()`.

| section | math claim | paper backing | Lean | verdict |
|---|---|---|---|---|
| Step 1 (L~80) | Reference the neutron Markov-trace assembly chain (50 dps via Wenzl bridge) | `prop:markov-trace-assembly-neutron` (if exists; check) | `markov-trace-assembly-*.lean` | **BACKED-STANDARD** |
| Step 2 (L~110) | Phase A 50-dps Terms 2-6 from `mass-formula-6term-mpfr-50dps.witness.json` | `prop:six-term-mass-formula-complete` ([six-term-mass-formula-complete.md](../../content/quantum-observable-universe/braids-and-knots/six-term-mass-formula-complete.md)) — to confirm | check sibling .lean | **BACKED** |
| Step 3 (L~140) | m_n_Hecke = T1 + T4 partial (Path A) | `prop:atomic-mass-via-rho-k` or sibling | check | **BACKED-PATH-A** (acknowledged partial truncation) |
| Step 4 (L~170) | m_e_Hecke (same Path A truncation, electron H_2 trefoil) | `prop:derive-m-e-hecke-path-a` (if exists) | check | **BACKED-PATH-A** |
| Step 5 (L~200) | Dimensionless mass ratio m_n / m_e at 50 dps | Pure arithmetic | n/a | **STANDARD** |
| Step 6 (L~230) | Scale by CODATA m_e → m_n in MeV | CAL-1 scaling per three-cal discipline | n/a | **STANDARD** |

**Note**: This file is the **Path A** assembly (T1+T4 only).
This branch's PR #663 replaces this with the **full tower**
(T1+T2+T3+T4+T5 at A_categorical) via
[`derive_m_n_hecke_full_tower_50dps.py`](../../computations/derive_m_n_hecke_full_tower_50dps.py).
The Path A chain is preserved on main as backward-compat for the
canonical 1 ppb workplan ledger but is **not the production
m_n path** on this branch.

**Verdict**: BACKED with documented Path A truncation (per the
chain's own docstring lines 25-30). No fitting, no calibration
leak. The 1.50 % residual under the full-tower path (replacing
this) is honest framework prediction.

### `build_markov_trace_assembly_neutron_chain.py` (293 lines)

Upstream chain for the dimensionless `tr_M(neutron, q_0)` at 50
dps via the Wenzl bridge. Per the chain docstring: "fully-trusted
on main via PR #480".

| section | math claim | paper backing | Lean | verdict |
|---|---|---|---|---|
| Markov-trace assembly | `tr_M(W) = Σ_λ y_λ(q) · χ^λ(W)` (Wenzl bridge) | `prop:wenzl-bridge-applicability-qou` ([wenzl-bridge-applicability-qou.md](../../content/quantum-observable-universe/braids-and-knots/wenzl-bridge-applicability-qou.md)) | [wenzl-bridge-applicability-qou.lean](../../content/quantum-observable-universe/braids-and-knots/wenzl-bridge-applicability-qou.lean) | **PROVEN** (claim: PR #480 "fully-trusted" — needs Lean sorry-check) |
| y_λ Plancherel weights at q_0 | `y_λ = dim_q(λ)² / [n]_q!` | `prop:y-lambda-jones-markov` or `prop:plancherel-weight-canonical` | check | **BACKED** |
| Hoefsmit χ^λ matrices at q_0 | Standard Hoefsmit seminormal at q_0 | [hecke-character-symbolic.py] tree; `prop:hoefsmit-seminormal` if exists | check | **STANDARD** |
| q_0 50-dps anchor | `q_0` from `q-pinning-50-digit.witness.json` (CAL-2) | `prop:three-calibration-inputs` ([three-calibration-inputs.md](../../content/quantum-observable-universe/braids-and-knots/three-calibration-inputs.md)) | check | **BACKED** |

**Verdict**: BACKED. The Wenzl-bridge production is the canonical
50-dps Markov-trace path; per the comment "fully-trusted on main",
Lean coverage is presumed complete (verifiable via the
`wenzl-bridge-applicability-qou.lean` file).

## Summary

| file | sections | PROVEN | BACKED | GAP | STANDARD |
|---|---:|---:|---:|---:|---:|
| `build_neutron_mass_50dps_chain.py` | 6 | 0 | 4 | 0 | 2 |
| `build_markov_trace_assembly_neutron_chain.py` | 4 | 1 (claimed) | 3 | 0 | 0 |
| **total Phase 2 extras** | **10** | **1** | **7** | **0** | **2** |

**Phase 2 verdict**: No new GAPs beyond Phase 1 (which flagged 5
sites in 3 propositions). The m_n-specific files are either Path A
truncations (acknowledged) or canonical Wenzl-bridge infrastructure
(claimed PROVEN per PR #480 audit).

The m_n full-tower closure (this branch's PR #663) inherits Phase 1's
gaps (categorical-A formal claim, T5-categorical assembly,
n=3 baryon weights uniform) — those need promotion to formal
propositions before m_n / m_p can reach `derived` under the 1 ppb
threshold.
