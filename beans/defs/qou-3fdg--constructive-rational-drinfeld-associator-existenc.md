---
# qou-3fdg
title: 'Constructive: rational Drinfeld associator existence (Bar-Natan descent, then algebraic obstruction)'
status: in-progress
type: feature
priority: normal
created_at: 2026-11-27T17:52:55Z
updated_at: 2026-11-27T18:01:21Z
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

2026-11-27: stage 1 done -- PR #9539 (LowDegree.lean): pentagon/inversion all c, hexagon iff (c-1/24)[t12,t23]=0. Sorry-free, std axioms. Next: stage 2 linear descent.

2026-11-27: #9539 merged (e834d19e0a). Stage 2a descent lemma -> PR #9541.
Stage 3 design (for next session if this one ends): induction P(N): exists full K-associator Phi with Phi_<=N rational. Step: Phi_{N+1} solves L x = w(Phi_<=N), L = linearized op at phi=1 (rational, independent of Phi), w rational => rational x by exists_of_baseChange; y = x - Phi_{N+1} in ker L (x) K = grt_{N+1} (x) K. NEED: for y in grt_{N+1}(K), exists associator Phi' = Phi mod deg N+1 with Phi'_{N+1} = Phi_{N+1}+y: Drinfeld GRT_1 action (Drinfeld 1990 sec.5; Bar-Natan 1998 via Aut(PaCD)). Plan: model DK families abstractly (reuse QOU.QFTMath.InfPureBraid.IsInfPureBraid in StandardModel/InfinitesimalPureBraid.lean) + cabling lemmas (strand doubling preserves IsInfPureBraid), GRT_1 automorphisms of t_n, then action. Linearized kernel: Lie, f(A,B)=-f(B,A), f(t13,t12)+f(t23,t13)+f(t12,t23)=0, linearized pentagon.
