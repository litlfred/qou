---
# qou-krvm
title: 'GAP: discharge optima_coincide''s hypotheses for the actual m004/L6a4 polytopes'
status: todo
type: task
priority: high
created_at: 2026-08-07T17:10:13Z
updated_at: 2026-08-07T17:10:13Z
---

THE GAP BETWEEN THE GENERAL THEOREM AND THE SPECIFIC MEASUREMENT.

PROVED (PR #4513, QOU/Knot/SymmetricOptimum.lean, sorry-free):
`optima_coincide` — two concave objectives on a symmetric convex feasible set,
each invariant under the symmetry and each with a unique maximiser, have the
SAME maximiser. So the offset between them is zero whatever they are.

NOT PROVED — the hypotheses have never been discharged for the actual anchors:
  (i)   that the m004 / L6a4 angle-structure polytopes are stable under a
        triangulation symmetry group acting linearly (a representation);
  (ii)  that the symmetric point is UNIQUE in each;
  (iii) that the Casson-Rivin minimum-angle objective is concave AND invariant
        there;
  (iv)  that the volume functional is concave AND invariant there (Rivin's
        theorem gives concavity in the literature; it is not in Mathlib).

So the measured ||x_geom - x_LP|| = 2.4e-16 / 5.0e-16 is explained by a proved
general theorem whose hypotheses are, for these two manifolds, only checked
numerically. The explanation is sound but the application is not formal.

WHAT WOULD CLOSE IT: (i)-(iii) are plausibly reachable — the symmetry group is
finite and explicit, the polytope is cut out by the integer edge/tet equations
already built in `ga_equalities`, and the minimum-angle objective is a min of
linear forms (concave, and invariant if the group permutes the forms). (iv) is
the hard one and overlaps the volume-theory gap in the sibling bean.

Partial credit is genuinely useful here: proving (i)-(iii) alone already forces
x_LP to the symmetric point, which is half the observed coincidence.
