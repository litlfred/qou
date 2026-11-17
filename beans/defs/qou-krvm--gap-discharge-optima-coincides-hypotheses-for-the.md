---
# qou-krvm
title: 'GAP: discharge optima_coincide''s hypotheses for the actual m004/L6a4 polytopes'
status: in-progress
pr: 8235
updated_at: 2026-11-17T06:55:36Z
type: feature
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T17:10:13Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-r9ih
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

---

## 2026-08-08 PARTIAL (PR #4513) — (i) DONE, (ii) REFUTED and REPAIRED, (iii) DONE for m004

`QOU/Knot/M004AngleStructure.lean`, sorry-free. SnapPy was installed and the
m004 gluing data pulled through the corpus's OWN helpers (`gluing` /
`ga_equalities` in `borromean_angle_structure_lp_probe.py`) — the same system
the LP was solved against, not re-derived from memory. In pi-units:

    tet1  a1 + b1 + c1 = 1          edge1  2a1 + b1 + a2 + 2c2 = 2
    tet2  a2 + b2 + c2 = 1          edge2  b1 + 2c1 + a2 + 2b2 = 2

(4 equations, rank 3, so a 3-dimensional feasible set — matches the LP.)

**(i) DONE.** Exhaustive search over all 720 coordinate permutations: exactly
FOUR preserve the affine set, forming a group of order 4. Two generators:

    sigma: (a1,b1,c1,a2,b2,c2) -> (c1,b1,a1,a2,c2,b2)   [swaps the edge equations]
    tau:   (a1,b1,c1,a2,b2,c2) -> (b2,a2,c2,b1,a1,c1)   [swaps tets AND edges]

Both proved to preserve GA and positivity (`GA.sigma`, `GA.tau`,
`Positive.sigma`, `Positive.tau`). This is the COMPLETE coordinate-permutation
symmetry, not a lucky subgroup.

**(ii) IS FALSE AS STATED — this bean's hypothesis does not hold.** The fixed
locus of the group inside the feasible set is a LINE, not a point:

    (a1,b1,c1,a2,b2,c2) = (t, 1-2t, t, 1-2t, t, t),   t in (0, 1/2)

proved as an IFF (`fixed_iff_line`), so it is the exact fixed locus, and
`GA_on_line` shows every such t is genuinely feasible — a real degree of
freedom, not an empty set. Consequently `symmetric_point_optimal` CANNOT be
applied to m004 the way this bean envisaged: symmetry alone does not pin the
optimum.

**(iii) DONE, and it repairs (ii).** Symmetry still does most of the work — it
cuts 3 dimensions to 1 — and the Casson-Rivin objective finishes on the line by
itself. Every coordinate of a fixed point is t or 1-2t, so the minimum angle is
`min t (1-2t)`, UNIQUELY maximised at t = 1/3 (`minAngleOnLine_lt_of_ne`,
`regular_unique_on_fixed_locus`) — the regular ideal tetrahedron, every angle
1/3. Composed with the already-proved `exists_symmetric_maximiser`, the regular
point IS a Casson-Rivin max-min-angle optimum for m004. That is the partial
credit this bean called genuinely useful, obtained via a corrected hypothesis.

**HONEST LIMITS.**
  - Proved: the regular point is AN optimum, not THE optimum. The min-angle
    objective is a min of linear forms — concave but NOT strictly concave — so
    global uniqueness does not follow and is not claimed.
  - (iv) UNTOUCHED. Nothing here concerns hyperbolic volume; Mathlib has no
    ideal-tetrahedron volume theory. That the complete structure also sits at
    the regular point is context, not a hypothesis used.
  - L6a4 NOT DONE. Its system is 24 variables / 16 equations / rank 13 (11-dim
    feasible set); the 24! permutation search is infeasible by brute force and
    needs the triangulation's combinatorial symmetry instead.

**CHECKS.** All 7 declarations sorry-free (`propext`/`Classical.choice`/
`Quot.sound` only). Both capstones survive the triviality ladder. Wrong-data
control: perturbing ONE edge coefficient from 2 to 3 breaks sigma-invariance
(linarith fails), so `GA.sigma` genuinely depends on m004's actual gluing data
rather than being a formality any linear system would satisfy.

**REMAINING FOR THIS BEAN:** L6a4 (i)-(iii) via combinatorial symmetry rather
than brute force; (iv) the volume functional, which is the Mathlib gap and
overlaps the sibling bean.

---

## 2026-08-08 — L6a4 (i)+(ii) DONE in Lean (PR #4725); the pair is complete

`QOU/Knot/L6a4AngleStructure.lean`, sorry-free, over the real 24-variable
system. Hypothesis (ii) is now settled for BOTH anchors, in opposite directions:

    m004  (muon)   |Sym| = 4    fixed locus a LINE   -> (ii) FALSE
    L6a4 (proton)  |Sym| = 16   fixed locus a POINT  -> (ii) TRUE

For L6a4 both (i) and (ii) hold, so `symmetric_point_optimal` applies DIRECTLY:
the proton anchor's vanishing offset is forced by symmetry alone, with no appeal
to the Casson-Rivin objective. For m004 it is not, and the objective finishes on
the fixed line.

Proved: `GA.gen0/1/2` (generators preserve the system), `fixed_orbitA` /
`fixed_orbitB` (constant on each orbit, sizes 16 and 8, by explicit generator
chains), `unique_symmetric_point` (the regular ideal octahedron: 1/4 on the
16-orbit, 1/2 on the 8-orbit).

NON-VACUITY PROVED, not assumed: `GA_regularOctahedron` +
`Fixed_regularOctahedron` + `symmetric_point_exists_unique`. Uniqueness alone
would hold vacuously if no such point existed. The check earned its keep — a
first attempt encoded the witness's index test with a conjunction instead of a
disjunction, collapsing every coordinate to 1/4 and failing four edge equations.

Why uniqueness is immediate: on an orbit-constant point the 16 constraints
collapse to three distinct equations — 2a+b=1 (x8), 8a=2 (x4), 4b=2 (x4). The
edge families pin a and b outright; the tet equation is then a compatibility
check. Every tetrahedron carries exactly one 8-orbit and two 16-orbit
coordinates: the (pi/4, pi/4, pi/2) octahedron.

The file is GENERATED from SnapPy via the corpus's own gluing/ga_equalities
(generator committed at `computations/probes/gen_l6a4_angle_structure_lean.py`),
so the constraint matrix and orbit chains cannot drift from the measurement.

## WHAT REMAINS ON THIS BEAN

Only hypothesis **(iv)**: the hyperbolic volume functional is concave and
invariant (Rivin). Untouched, and it is a genuine Mathlib gap — there is no
ideal-tetrahedron volume theory to build on. This is the hard half and it is
now the ONLY thing between this bean and closure.

Also still true, and stated in both files: what is proved is that the regular
point is AN optimum / THE symmetric point, not that the LP optimum is unique.
The min-angle objective is a min of linear forms — concave, not strictly.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## Progress Update (PR #8235)
- **Status**: `in-progress` (awaiting Merge Manager merge of `litlfred/qou#8235` at `83fd5b4cb41e61d75f72ddd82bda505e34bd92f4`).
- **Lean Formalization**: `QOU.QBeta.ThimbleDecompositionAndSymmetricPolytopeBrick.symmetric_angle_polytope_barycenter_fixed_and_strict_concave_gap` (Swap invariance and exact quadratic concavity gap F_max - F(x, y) = (kappa/2)*(x - y)^2 >= 0 on the symmetric angle-structure hyperplane x + y = S.)
- **80-dps Witness**: `computations/probes/thimble-decomposition-and-symmetric-polytope-brick.witness.json` (`scriptHash: e55db77fb2bb`, `scriptCommitSha: 6020aea5785046b552772c9a42fc52ac2db9f3a2`).
