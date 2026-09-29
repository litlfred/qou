---
# cjo1
title: 'Test hypothesis: two AJ saddles emit c_2=-1 (bar-odd) and c_2=-8 (bar-even) [may not match — honest]'
status: todo
type: task
parent: b9cj
created_at: 2026-06-30T20:35:58Z
updated_at: 2026-07-06T18:18:13Z
---

SCOPING (2026-07-06, PR #3434 — probe NOT run, deliberately):

1. The bar-even target is NOT the integer -8: it is the MEASURED,
   NORMALIZATION-DEPENDENT rung c2^even = -8.00641 (net route; see
   docs/audits/2026-07-03-u-tilde-bar-weight-normalization.md — rung
   values change with the u-normalization). A saddle computation
   "emitting -8" would still miss the measured value by 6.4e-3; the
   hypothesis as titled glosses this.
2. Exact reproduction of c2^even/c3^even is the stability gate of bean
   8we6 (H4 Hoefsmit c4^even build), and bean aciw's standing gate says
   NO anchor-adjacent sweeps before that build. cjo1 is anchor-adjacent.
3. Formalize-first gap: no corpus map exists from the AJ saddle series
   of Â_{4_1} to the Q_beta ladder Π(1 + c_k u^k) — constructing that
   map IS the hypothesis. Without it, a numeric scan is shape-probing
   in the flip-flop minefield (production-vs-exploratory discipline).
   The invariant to formalize first: the bar-parity split of the saddle
   expansion (P-C15/aciw already supplies the fibre-side half: the 4_1
   qZeilberger Casoratian ratio is exactly bar-self-reciprocal).

GATED NEXT: after 8we6 lands c4^even + the u-tilde normalization is
pinned, restate cjo1 as "does the root-of-unity/real saddle split of
Â_{4_1} reproduce the bar-odd/bar-even RUNG SPLIT (not the values)" and
formalize the parity invariant before any evaluation.
