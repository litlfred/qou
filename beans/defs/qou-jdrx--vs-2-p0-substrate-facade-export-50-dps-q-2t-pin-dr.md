---
# qou-jdrx
title: 'VS-2 (P0 Substrate & Facade): refresh stale muon-stamped q-pinning-50-digit.witness.json & align canonical_mass.py _from_witness'
status: todo
type: task
priority: high
created_at: 2026-11-19T07:06:02Z
updated_at: 2026-11-24T08:06:23Z
parent: qou-s028
---

## Audit Provenance

Grounded in `computations/audits/paper-status-variable-substitution-and-staleness-audit.witness.json` (`computations/audits/paper_status_variable_substitution_and_staleness_audit.py`), linked to `qou-v6so`, `qou-2002`, and `qou-9nnz`.

## Defects Identified by the End-to-End Audit

1. **`computations/substrate/q_parameter.py` & `computations/q_pinning_50_digit.py` (`P0-Substrate`):**
   - `Q_50_DIGIT_STR` is currently the 1-term proton root $q_{\mathrm{proton,1t}} = 1.1099785827513808075916690956107688798744991218736$.
   - The two-term Borromean QED proton self-energy $M_p^{\mathrm{QED}} = +220.077\text{ eV}$ shifts the proton-pinned root by $+11.1709\text{ ppb}$ to
     $$q_{2\mathrm{t}} = 1.1099785951508859990875652035986826212141034805412,$$
     closing $96.18\%$ of the $11.6141\text{ ppb}$ gap to the CODATA-2022 muon pin ($q_{\mu} = 1.1099785956427390466817951293800017527000655610290$, leaving only $0.443\text{ ppb}$).
   - Meanwhile, `computations/q-pinning-50-digit.witness.json` on disk is stale (`scriptHash` mismatch AND frozen at the muon anchor `q0Anchor: "muon"` while `q_pinning_50_digit.py` computes the 1-term proton anchor), and `28` manuscript Liquid bindings + `19` `ValueRegistry` entries read from `q-pinning-50-digit.witness.json`!
2. **`computations/canonical_mass.py` (`P0-Facade`):**
   - `proton_neutron_mass_mev()` defaults to 1-term float64 masses; `E_0` is truncated at $M=0$ ($E_0^{(0)} = m_e / (q(q-1)) = 4.185981\text{ MeV}$ instead of the closed-form tower $E_0^{(\infty)} = E_0^{(0)}/(1-\hbar_q^2) = m_e q / ((q-1)(2q-1)) = 4.227483\text{ MeV}$, a $+9914.5\text{ ppm}$ shift); `alpha_D` is unprojected ($-0.040486\text{ rad}$ vs mirror-projected $\alpha_D^{\mathrm{proj}} = \alpha_D - h^2/4 = -0.051412\text{ rad}$); and functions hardcode `Q_50_DIGIT_STR` instead of accepting `q: mpf | None = None`.
3. **`computations/coulomb_energy.py` (`P0-Facade`):**
   - `alpha_hbar_c_mev_fm()` uses the CS-resummed $\alpha_{\mathrm{EM}}^{-1} = 137.0359351$ (`-467.6 ppb`) at fixed `Q_50_DIGIT_STR` instead of accepting `q` and defaulting to the Form-B 1-loop Bring–Schwinger cubic root $\alpha_{\mathrm{EM}}^{-1} = 137.0359991270$ (`-0.3652 ppb`, $-2.38\,\sigma_{\mathrm{exp}}$).
4. **`computations/derived_masses.py` & `computations/substrate/hecke_core.py` (`P0-Facade`):**
   - `derived_masses.py` (`M_P_MEV`, `M_N_MEV`, `M_MU_MEV`, `M_TAU_MEV`, `Q_BETA_MEV`) and `hecke_core.py` expose 1-term float64 module constants without `q_2t`, two-term QED nucleon splittings, or `E_0^tower`.

## Required Deliverables

1. Export 50-dps `Q_2T_50_DIGIT_STR` and `q_two_term_at(dps)` in `substrate/q_parameter.py`, and regenerate `q-pinning-50-digit.witness.json` with explicit `proton_1term`, `proton_2term_borromean`, and `muon_codata2022` blocks so downstream Liquid bindings are anchor-unambiguous and fresh.
2. Upgrade `canonical_mass.py`, `coulomb_energy.py`, `derived_masses.py`, and `substrate/hecke_core.py` to pure `mpmath.mpf`, accepting `q: mpf | None = None`, exposing `E0_tower_mev(q)`, `alpha_D_mirror_projected(q)`, Form-B Bring–Schwinger $\alpha_{\mathrm{EM}}^{-1}(q)$, and 4-row Hankel-normalized $Z_{3A}^{(4)}(q)$.


## 2026-11-20 W13 (#8526, PR #8539)

Measured float64 surface: derived_masses 0, coulomb_energy 0, hecke_core 2 (inf sentinels), canonical_mass 1 real (_from_witness line 56; 20 importers; W2 scope, offered on #8526, not touched). q_2t pin + default changes = owner decision, framed ask on #8526. Stays todo.


## 2026-11-23 — Q-Drain-1 Applicability & Scope Narrowing against origin/main (`e330ab6aa04`) and owner-rulings.md
- **Measured on `origin/main` (`e330ab6aa04`):** `computations/q-pinning-50-digit.witness.json` is still stamped `q0Anchor: "muon"` with stale `scriptHash: 58f994b46a01` (vs live `q_pinning_50_digit.py` `e6f6426e55c7`), and `canonical_mass.py` retains 1 float64 site (`_from_witness`).
- **CRITICAL Applicability Rescope (`docs/coordination/owner-rulings.md`):**
  1. **Do NOT promote retired `KnKp` `q_2t`:** Owner ruled (#8554, #8591, 2026-11-20) that the one-term proton pin is canonical default, `q_2t` is a named comparison only, and under derived `K^{\otimes 3}/[2]_q^3` weighting the connected part vanishes on `V^3` (the `+11.17 ppb` / `96.18%` figure in this bean's original text was an artifact of the retired `1/3` `KnKp` normalisation).
  2. **Do NOT switch `coulomb_energy.py` default to Form-B:** Owner ruled (2026-11-21, `qou-aemx`) that consumers stay on the CS tower (labelled) and Form-B is a labelled comparison arm only.
  3. **Tower-summed `E_0`:** Canonical via `computations/qbeta/qbeta_e0.py` (#8590).
- **Surviving open sub-problem:** Resolve the muon/proton stamp & consumer straddle on `q-pinning-50-digit.witness.json` (28 Liquid bindings + 19 `ValueRegistry` entries, pending owner sign-off on #8526) and excise the remaining `_from_witness` float64 cast in `canonical_mass.py`.
