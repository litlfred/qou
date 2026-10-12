---
# qou-ocof
title: 'NS rescue: explore honest reformulations of an NS-singularity statement on Bring'
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T20:26:55Z
updated_at: 2026-10-12T22:00:00Z
parent: qou-vo9t
---

Owner-directed (2026-10-12): after restating thm:ns-singularity-descartes as true topological facts (option B), keep exploring whether ANY honest reformulation could rescue an NS-singularity statement on Bring's surface.

Constraints: no fitting; do not re-house a claim into whatever group makes it true; every candidate must name the object the chain actually uses. Candidates to examine:
- dynamical: does the model's actual Reeb field vanish on the collision locus?
- 3-manifold setting: H^2 of the 3-dimensional M_S, rather than of the surface
- local cohomology on Sigma
- relative classes H^2(S, S minus Sigma)
- Kummer/arithmetic forms
- Atiyah/jet classes

Output: an audit doc with a per-candidate verdict.

## 2026-10-12 — exploration result (docs/audits/2026-10-12-ns-rescue-reformulations.md)

Verdict: no honest rescue among the five candidates. Per candidate:
- (1) Reeb field vanishes on Sigma: no, scope (b). The corpus's Reeb field generates a free U(1) action and Theta(R)=1, so it has no zeros.
- (2) H^2_Sigma(S,Z): true but vacuous. It is codimension 1, H^2_Sigma = Z, and the lift of e = -6 is unique and independent of the section. But it holds for every non-empty compact Sigma, so it says nothing about collisions.
- (3) M = UT(Sigma_4): e(contact) = 0; the -6 survives only as Z/6 torsion; the Reeb flow is periodic. Contact structure tight, Weinstein satisfied trivially. Neither gives a singularity statement.
- (4) Etnyre–Ghrist transfers exactly but points the other way. V is a Beltrami field for the left-invariant metric, so it is a steady Euler flow, and e^{-nu t} V is a globally smooth NS solution on M. 2D NS and Euler on the surface are globally regular.
- (5) Kummer: the fibre has order 6 in H_1(M). No dynamical content.

Two independent defects were found:
- the symbol 𝒮 is used as both a 2-surface and a contact 3-manifold;
- the computation (c).1 and the Levi chain (descartes-proof Step 3, levi-degeneracy (B)) take opposite branches.

The bean stays open: the 3D NS question on M remains the open Clay-type problem.
