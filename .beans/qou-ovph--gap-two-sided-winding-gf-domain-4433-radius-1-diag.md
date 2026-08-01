---
# qou-ovph
title: 'GAP: two-sided winding GF domain — #4433 radius-1 diagnostic was pre-asymptotic (e<=28); lead(e)~e^2/8 forces eventual super-exponential decay of I(0,e)(q~) => GF may be entire on C* (no continuation needed, direct deep-window summation instead). W1 A2 red at ALL |w| (O(35-60)) because the +-40 window sits in the pre-asymptotic zone where the negative-e side blows up off |w|=1. Decay-onset probe at e=40..100 running; if confirmed: re-scope #4433 annulus claim (scope-(a) correction), re-run A2 with E~150/dps~120, and W2 becomes direct evaluation at the corpus sheet.'
status: completed
type: task
priority: normal
created_at: 2026-08-01T15:14:28Z
updated_at: 2026-08-01T20:22:47Z
---


## 2026-08-01 decay-onset CONFIRMED + entirety Lean-proved

Measured I(0,e)(q~): e=40: 1.98e-5; e=60: -2.1e-16; e=80: -3.5e-32;
e=100: 1.9e-53 — super-exponential, tracking the quadratic lead e^2/8
(each within ~1e4-1e5 of bare q~^lead). The #4433 radius-1 diagnostic
sampled only the pre-asymptotic plateau (e <= 28).

Lean (WindingGFTransform.lean, sorry-free): summable_winding_of_sq_dominated
(entire on C*) + gf_three_term_of_sq_dominated (functional equation holds
among tsums at EVERY w != 0 — HasSum discharged by entirety).

Remaining in this bean: (1) scope-(a) correction note in the merged #4433
audit + witness data row; (2) A2 rerun at |w| ~ 0.8 with E_GF=60 (peak
term analysis: at |w|=0.8 the negative-side hump peaks at only ~0.26 so
dps 50 suffices; at |w|=0.3 the hump reaches 1e17 and needs dps>=80 —
why both prior A2 configurations failed); (3) W2 = direct two-sided
summation at the corpus sheet w = q0^2 e^{2i theta} (converged by e~60)
+ the -4.0751 comparison.
