---
# cjo1
title: 'Test hypothesis: two AJ saddles emit c_2=-1 (bar-odd) and c_2=-8 (bar-even) [may not match — honest]'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-06-30T20:35:58Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
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


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: BLOCKED.** The two targets (−1 bar-odd, −8.006 bar-even) are convention-C rung values, so a saddle computation matching them would not bear on the D-frame ladder. Keep it gated on 8we6, and restate it against the D-frame rung split once qou-cds1 supplies one.

Evidence: Scoping-only bean: no probe was run, deliberately. Both targets are convention C. c2^even = −8.00641 comes from the KC21 net route on z_C. `qou-cds1`'s table says "c₂ = −1 is a C-frame statement" (implied D value −9.299 is a data inversion; the D-rebuilt c2 is OPEN). Gated on `8we6` (todo).

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
