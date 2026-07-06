---
# gwy3
title: 'Consume #3407 Lk_R⁽ᵏ⁾: b₄ pn sign + sub-1/√5 per-pair magnitude (spec posted on #3407)'
status: in-progress
type: task
priority: normal
created_at: 2026-07-06T17:12:45Z
updated_at: 2026-07-06T17:32:03Z
parent: il97
---

2026-07-06 update: owner landed the pn magnitude directly on main
(8275655551 + 17264f2a9c): g = 1/√(5 + (q₀−1)²/q₀) ≈ 0.44673, just below
the 1/√5 ceiling; ²H tier switched to "reeb-flow", B = 5g ≈ 2.2336 MeV
(+0.41% vs AME 2.22457). Remaining scope: (1) verify the derivation of g
and the linear B = 5g form against the #3407 Lk_R⁽ᵏ⁾ spec (sign leg still
implicit); (2) the hardcoded err_pct: 0.0 in
categorical_q_decay_ba_low_isotopes.py:206 mis-reports the actual +0.41%;
(3) extend to the A=4 [1⁴] exchange matrix.
2026-07-06 (later): provenance + extension done on PR #3436 —
docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md
+ computations/probes/b4_1four_reeb_flow_magnitude.py (3/3 assertions).
Findings: 5 = |μ_min|² DERIVED; (q₀−1)²/q₀ term + linear B=5g ASSERTED
(no corpus derivation); det-form fails deuteron (−58%) ⇒ forms distinct;
[1⁴] mixed-sign at g_reeb = 26.596 MeV = 0.940× full B(⁴He) (2.877× b₄).
Remaining: derive g_reeb from Lk_R⁽ᵏ⁾ (#3407); reconcile linear-vs-det;
pin b₄ convention (connected excess vs full); pn sign.
2026-07-06 (round 3): #3407 turned out MERGED — its audit doc
(2026-07-05-reeb-linking-operation-attack.md) claims 3-route derivation of
g, but categorical_linking_reeb_flow_probe.py restates the formula in one
line (no Route A/B/C computation exists). Provenance table corrected in
2026-07-06-reeb-flow audit. Q3 added to b4_1four_reeb_flow_magnitude.py:
Ursell cumulants of the det form at g_reeb — b₂ 0.42×, b₃ 1.042× (4.2%!),
b₄ 1.63× vs AME. Convention pinned: 9.2431 = connected cumulant.
Remaining: substantiate Route A/B/C (or re-scope #3407 doc claim);
reconcile linear 5g law; pn sign.
