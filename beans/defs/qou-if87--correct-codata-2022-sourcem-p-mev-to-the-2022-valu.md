---
# qou-if87
title: Correct codata_2022_source.M_P_MEV to the 2022 value + re-score the L2 dashboard (follow-up to qou-2an8)
status: completed
type: task
priority: normal
created_at: 2026-08-09T10:53:26Z
updated_at: 2026-08-09T22:25:16Z
---

## Partial delivery (2026-08-09, PR #4860) — label fixed + guard added; VALUE STILL OPEN

Done (provable from repo contents, NO value change, zero blast radius):
- M_P_MEV docstring corrected: it is CODATA-2018, not 2022. Carries the
  inconsistency proof (127x the last printed digit) + neutron-leg ID.
- M_N_MEV_AME_DERIVED docstring: its ~1.5 ppb gap vs the direct neutron is
  explained by the stale proton; and it is NOT an independent measurement.
- NEW M_P_MEV_RATIO_CONSISTENT (+_ERR), explicitly DERIVED.
- NEW MASS_RATIO_P_E re-export SOURCED from qou_substrate (not a copy —
  a literal would make this a 4th registry). Fail-soft.
- NEW triple_consistency_ppb() / assert_triple_consistent() regression guard.

**STILL BLOCKED — the literal swap.** physics.nist.gov is egress-blocked in
the sandbox, so the true CODATA-2022 digits are unverified. Writing a DERIVED
number into a file whose stated purpose is vendoring NIST quotes would
reintroduce the provenance defect being documented. Needs either network or
an owner-supplied verified quote.

Once swapped: tighten KNOWN_TRIPLE_RESIDUAL_PPB from 1.4 to ~0.05, and
re-score the dashboard (m_n 420.1x -> 176.7x, Delta_pn 163.3x -> 151.3x,
Q_beta 164x -> 139x; m_p should become UNSCORED as a pin-anchor round-trip).
