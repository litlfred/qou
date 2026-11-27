---
# qou-3fdg
title: 'Constructive: rational Drinfeld associator existence (Bar-Natan descent, then algebraic obstruction)'
status: in-progress
type: feature
created_at: 2026-11-27T17:52:55Z
updated_at: 2026-11-27T17:52:55Z
parent: qou-dk7p
---

Owner pick 2026-11-27 (card option 2): stages 1-5, then research attempt to drop the hypothesis.

Goal: Lean, sorry-free, algebraic: a group-like Phi in completed U(t_3) over Q satisfying pentagon + hexagons; discharge the Phi hypothesis of PR #9519 (QuasiYangBaxterFromHexagon).

Caveat: Bar-Natan 1998 (Selecta) and Drinfeld still need ONE associator over some field K containing Q (KZ over C). As far as known no purely algebraic proof of obstruction vanishing. Theorem formalized: associator over K => associator over Q; K-input is one named hypothesis, used in no proof. Coordinator asked whether it reduces to the shared Coev axiom: not evident (KZ needs completeness, Coev is coev=0 squeeze) -- open question, not claimed.

Stages:
1. truncated U(t_n) over Q-algebras, leg maps, group-like, pentagon/hexagon mod deg N; explicit Phi = exp((1/24)[t12,t23]) mod deg 3.
2. linear descent: degree-(n+1) part solves affine Q-linear system; solvable over K => over Q.
3. grt = kernel of linearized eqs; GRT action phi -> phi g(A, phi^-1 B phi) preserves pentagon/hexagon.
4. induction + limit: full rational Phi.
5. wire into #9519 via Casimir into Q[[h]] data.
R. research: algebraic obstruction vanishing (drop hypothesis).

Thread: Formalize rational associator existence.
