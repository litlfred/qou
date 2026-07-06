---
# n920
title: 'Borromean AJ: cross-check Borromean cyclotomic c_k against Habiro [H1] (simple links, RIMS Kokyuroku 1172) — NOT Masbaum math/0306345 (twist knots only); ref unavailable, DEFERRED'
status: in-progress
type: task
created_at: 2026-07-04T10:42:30Z
updated_at: 2026-07-06T21:58:19Z
---

UNBLOCKED 2026-07-06: owner uploaded uploads/0508100v6.pdf (GL2011).
Habiro's Borromean formula transcribed + verified in
computations/habiro_borromean_colored_jones.py (4/4 anchors: n=1
exactness, bar-symmetry n<=6, Laurent polynomiality, independent TL_3
Kauffman-bracket cross-check at n=2). Remaining for this bean: the
actual c_k cross-check against the corpus's Borromean cyclotomic
values, + the (novel) recurrence hunt on the diagonal tower.
EXISTENCE CERTIFICATE 2026-07-06 (borromean_diagonal_recurrence_hunt.py):
a q-difference operator annihilating the diagonal tower J_{B,n} EXISTS
at order r=5, m-window W=13 (nullity 2; 9/9 (p,s) mod-p samples, each
surviving 30 beyond-fit-range check rows; orders <=4 excluded for
W<=14). Phase 2 = symbolic reconstruction over Z[q^{±1}] + exact
symbolic annihilation + q->1 specialization (candidate Borromean
A-ideal generator, diagonal restriction).
