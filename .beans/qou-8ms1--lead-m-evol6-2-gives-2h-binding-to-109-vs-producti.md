---
# qou-8ms1
title: 'LEAD: m_e*Vol(6_2) gives 2H binding to 1.09% vs production B_sym''s 27.34% - knot-ID route, gated on open conj:canonical-knot-id-sdp'
status: todo
type: task
priority: normal
created_at: 2026-08-25T19:18:14Z
updated_at: 2026-08-25T19:51:56Z
parent: qou-9ot5
---

## REFUTED AS A LEAD 2026-08-25 — it is an admitted fit. Do not quote +1.09%.

Production source says it outright (mass_table_ppb.py L11-22, verified by reading):
'The atom->knot assignments for D, T, 3He were obtained by census search in
jsj_verification.py -- that IS a form of AME-driven fitting (we picked the knot whose
volume is closest to B_AME/rho).' The selection criterion IS proximity to the
experimental binding energy. The corpus was honest throughout; I did not read far
enough before calling it a lead.

Also: the SDP is a FEASIBILITY check on a presupposed element, not a selection - so
uniqueness cannot be a property of it. The closure-identifies-as-6_2 check is CIRCULAR
(the registry words ARE snappy's stored braid words for those knots, verified). Census
degeneracy: 796 manifolds closer than 6_2 for 2H, 1101 for 3H, 26671 for 3He. Two of
three assignments FAIL their own criterion (10_9 beats 8_11; 8^2_4 beats L6a4).

Scope-(b): 6_2 CANNOT be the closure of the canonical deuteron word. Component count =
cycle count of the permutation, and sigma/sigma^-1 project to the same transposition, so
every branch has 3 components (verified 32/32). 6_2 is a knot.

The one thing worth doing: derive a braid-index/crossing-number bound for K(2H) from the
substrate with NO reference to B_AME, then ask if the match is unique in that class.
0 better matches inside the tabulated census, 796 without it - all the discriminating
power is in the restriction, and nothing derives it. Registry asserts n_braid: 3, n_0: 6;
CHECK whether that is derived or handed over. See docs/audits/2026-08-25-knot-id-is-an-admitted-fit.md
