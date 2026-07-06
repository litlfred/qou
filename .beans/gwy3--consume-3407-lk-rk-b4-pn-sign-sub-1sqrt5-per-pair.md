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
