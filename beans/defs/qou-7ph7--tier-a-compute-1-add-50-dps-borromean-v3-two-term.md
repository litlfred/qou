---
# qou-7ph7
title: 'Tier A Compute 1: Add 50-dps Borromean V^3 Two-Term & Connected QED Helpers to qou_substrate (constants.py & __init__.py) and m_p_substrate_identity_50dps.py'
status: in-progress
type: task
priority: high
created_at: 2026-11-18T21:22:35Z
updated_at: 2026-11-18T21:22:35Z
parent: qou-7xl8
---

Implement Tier A non-breaking compute updates from Section 6.2.1 & 6.2.2 of `docs/audits/2026-11-18-two-term-qed-downstream-and-211ppb-audit.md`:
1. `tools/qou-substrate/python/qou_substrate/constants.py` & `__init__.py`:
   - Add 50-dps MPFR helpers `tr_borromean_v3_at(q=None, dps=50)`, `tr_e21_borromean_v3_at(q=None, dps=50)`, `tr_conn_borromean_p_at(q=None, dps=50)`, `tr_conn_borromean_n_at(q=None, dps=50)`, `tr_conn_borromean_diff_at(q=None, dps=50)`, and parallel diagnostic pin solver `q_two_term_borromean_at(dps=50, k_weighted=False)`.
   - Export all 6 helpers in `qou_substrate/__init__.py` `__all__` while keeping default `q_at(dps)` and `Q_50_DIGIT_STR` strictly unchanged.
2. `computations/m_p_substrate_identity_50dps.py` & `computations/m-p-substrate-identity-50dps.witness.json`:
   - Add `borromean_v3_connected_qed_traces(q)` and emit the additive JSON witness section `two_term_borromean_qed_diagnostics` + assertions `borromean_v3_e3_plus_e21_equals_full_trace` and `borromean_v3_conn_proton_closes_mup_gap_within_1sigma`.
   - Re-run `python3 computations/m_p_substrate_identity_50dps.py --write-witness` and verify all existing fields remain bit-identical.
