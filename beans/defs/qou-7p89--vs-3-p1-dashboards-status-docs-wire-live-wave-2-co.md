---
# qou-7p89
title: 'VS-3 (P1 Dashboards & Status Docs): Wire Live Wave-2 Compute and Liquid Variable Substitution Across Status Scorecards & Appendix Dashboards'
status: todo
type: task
priority: high
created_at: 2026-11-19T07:06:02Z
updated_at: 2026-11-19T07:06:02Z
parent: qou-v6so
---

## Audit Provenance

Grounded in `computations/audits/paper-status-variable-substitution-and-staleness-audit.witness.json` (`computations/audits/paper_status_variable_substitution_and_staleness_audit.py`), linked to `qou-v6so` and `qou-trd0`.

## Defects Identified by the End-to-End Audit

1. **Zero dynamic variable substitution across all 4 status scorecard documents (`0` Liquid `{{ qou... }}` and `0` `:val[...]`, with `400` hardcoded residual literals):**
   - `docs/precision-goals.md` (`218` hardcoded residual literals; narrative cites stale `-468 ppb` for $\alpha_{\mathrm{EM}}^{-1}$, `+23.4 ppb` for $m_K/m_\pi$, and `148 ppm` / `291x` for $m_n$).
   - `docs/observable-sector-tracker.md` (`99` hardcoded residual literals; narrative cites `0.00807` gap on $\alpha_{\mathrm{EM}}^{-1}$ and stale $B({}^2\mathrm{H}) = 2.861\text{ MeV}$).
   - `docs/prediction-validation-status.md` (`80` hardcoded residual literals across 36 observable rows).
   - `folio/quantum-observable-universe/appendix-qvalues/per-observable-100x-status-dashboard.md` (currently contains a custom `:::observable-dashboard` fence that `render-latex.ts` strips to **0 rows in the compiled PDF**, instead of a Liquid-bound table backed by `per-observable-100x-status.witness.json`!).
2. **Stale P1 Dashboard Producers:**
   - `computations/per_observable_100x_status.py` (`per-observable-100x-status.witness.json`): uses 1-term $m_p, m_n, Q_\beta$, CS-resummed $\alpha_{\mathrm{EM}}^{-1}$ (`-467.6 ppb`), and records `0` `upstream_witness_hashes` despite reading `7` upstream witnesses on disk (3 of which have drifted!).
   - `computations/onepb_status_dashboard.py` (`onepb-status-dashboard.witness.json`): `scriptHash` stale (`83ec456ff613` vs live `14a9b17cd29f`), records `0` `upstream_witness_hashes` across `6` file-read witnesses.
   - `computations/mass_binding_dashboard.py` (`mass-binding-dashboard.witness.json`): Tables 1–7 use 1-term float64 `proton_neutron_mass_mev()`, float64 `pyhecke` `E_HARTREE_EV` (lines 85, 296), truncated $M=0$ $E_0 = m_e/(q(q-1))$ (line 331), and unnormalized `W_lambda_float` (lines 175, 654, 671).
   - `computations/two_term_qed_isotope_and_nucleon_compute.py`: line 240 prose has inverted derivative sign (`d(m_p^QCD/m_e)/dq > 0`), line 306 uses unprojected $\alpha_D$, and lines 415/440 scale $B_{\mathrm{sym}}$ and GPMT by truncated $E_0^{(0)}$.
   - `computations/probes/electroweak_bring_schwinger_bridge_probe.py`: line 92 hardcodes CODATA `137.035999177` inside `schwinger_1loop_alpha_pi` instead of derived $\alpha_{\mathrm{EM}}^{-1}(q_0)$.

## Required Deliverables

1. Upgrade `per_observable_100x_status.py`, `onepb_status_dashboard.py`, `mass_binding_dashboard.py`, `two_term_qed_isotope_and_nucleon_compute.py`, and `electroweak_bring_schwinger_bridge_probe.py` to live Wave-2 compute (Form-B Bring–Schwinger $\alpha_{\mathrm{EM}}^{-1}$ at `-0.365 ppb`, 2-term QED nucleon/Coulomb/mirror splittings at $q_{2\mathrm{t}}$, mirror-projected $\alpha_D^{\mathrm{proj}}$, $E_0^{(\infty)}$, GPMT $d_{\mathrm{mod}}$, and 4-row Hankel $Z_{3A}^{(4)}(q_0)$) and record all `upstream_witness_hashes` via `WitnessBuilder`.
2. Replace `:::observable-dashboard` in `appendix-qvalues/per-observable-100x-status-dashboard.md` and hardcoded table cells in `docs/precision-goals.md`, `docs/observable-sector-tracker.md`, and `docs/prediction-validation-status.md` with Liquid `{{ qou.computations... }}` variable substitution.
