---
# qou-h5aw
title: Project Yekutieli B3 Action onto the Local (2,1) Bond
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-20T01:57:24Z
updated_at: 2026-11-16T19:19:00Z
parent: qou-wp3h
---

## Progress Update (2026-11-16 — PR #8164)
- **PR:** [`litlfred/qou#8164`](https://github.com/litlfred/qou/pull/8164) (`47da262e4f487a8f51de58f3577a63d5b17e6d6a`)
- **Resolution:**
  - Formalized in `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/BorromeanChiPerRep.lean` (`0` `sorry`, `0` self-assuming audit hits) the projection of the Yekutieli $B_3 = (T_1 T_2^{-1})^3$ action onto the 2-dimensional standard Hook representation $V_{(2,1)}$ (the local $(2,1)$ bond):
    - `yekutieliBond21Trace h := -1 - h^2` and `yekutieliBond21Trace_qform_unit q := 1 - q^2 - q^{-2}` (`yekutieliBond21Trace_qform_unit_eq_poly`).
    - `chebyshevCubicTrace t := t^3 - 3 * t`, `yekutieli_b3_local_21_bond_projection : chebyshevCubicTrace (yekutieliBond21Trace h) = chi21_borromean h`, `yekutieli_b3_local_21_bond_qform_unit`, and `chebyshevCubicTrace_stationary_at_neg_one` (explaining why the $O(h^2)$ term cancels identically at $t_0 = -1$ since $T_3'(-1) = 0$).
  - Verified to 50+ dps (`< 1e-70` residual) in `computations/probes/na_stokes_bar_parity_local_bond_probe.py` (`na-stokes-bar-parity-local-bond.witness.json`, `scriptCommitSha: "0460230ed949f9048ab3fee481d3038ba5d0ec59"`).
  - Status kept at `in-progress` pending PR #8164 merge and owner verification.
