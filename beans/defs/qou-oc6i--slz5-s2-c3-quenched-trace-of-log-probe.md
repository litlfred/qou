---
# qou-oc6i
title: 'slz5 S2: C3 quenched (trace-of-log) bond functional, probe'
status: in-progress
type: task
priority: normal
created_at: 2026-10-10T15:10:00Z
updated_at: 2026-10-10T15:10:00Z
parent: qou-slz5
---

Stepping stone 2. Measurement done; the question it serves (what B should be on the faithful window) stays OPEN, so this bean stays open.

**Functional.** B_C3 = -alpha sum_lambda mu_lambda (1/f^lambda) log|det rho_lambda(W_atom)/det rho_lambda(W_free)|. Per bond it collapses to
g(d; z) = p+ log|q + d| + p- log|1/q - d|, p+ = (z + 1/q)/(q + 1/q).
Closed form checked against explicit Ocneanu block sums n = 3..7 (diff 2.5e-72).

**Results** (computations/deltalambda/c3_quenched_bond_logdet_probe.py, 5/5, units of alpha, B per bond):
- pp = -nn at EVERY z (sigma and sigma^-1 have reciprocal eigenvalues). Exact.
- pp = nn = 0 exactly at the self-dual point z = h/2, and only there.
- pn is always weakly ANTI-bound: about -0.00543 alpha across the whole window; colour-blind pn is z-independent.
- Magnitudes are about 50x smaller than B_log at convention D.

**Reading (judgement).** C3 is real everywhere, but its isospin structure is the letters' structure: whatever sign pp has, nn has the opposite. It cannot give nn, pp both unbound with pn bound. This points back at the letters (S3, S4), not at the functional. Scope (a): candidate measured, not adopted, no AME comparison.
