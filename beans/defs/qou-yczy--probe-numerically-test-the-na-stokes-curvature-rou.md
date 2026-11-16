---
# qou-yczy
title: 'Probe: numerically test the na-Stokes curvature route to -pi^2/3 (bar-even cosh / bar-odd sinh channel split; -pi^2/3 = -2*(pi^2/6) decomposition against the surface-ordering term).'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-26T12:23:36Z
updated_at: 2026-11-16T19:19:00Z
parent: qou-wp3h
---

## Progress Update (2026-11-16 — PR #8164)
- **PR:** [`litlfred/qou#8164`](https://github.com/litlfred/qou/pull/8164) (`47da262e4f487a8f51de58f3577a63d5b17e6d6a`)
- **Resolution:**
  - Formalized `naStokes_surface_ordering_double_half_plaquette` in `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/BorromeanChiPerRep.lean` (`0` `sorry`) and added the 50+ dps numerical probe `computations/probes/na_stokes_bar_parity_local_bond_probe.py` + `computations/probes/na-stokes-bar-parity-local-bond.witness.json` (`scriptCommitSha: "0460230ed949f9048ab3fee481d3038ba5d0ec59"`), testing the $-\pi^2/3 = -2(\pi^2/6)$ surface-ordering decomposition and bar-even $\cosh(\log q_0) - 1$ / bar-odd $\sinh(\log q_0)$ channel split.
  - Status kept at `in-progress` pending PR #8164 merge and owner verification.
