---
# qou-oilr
title: Benard's adjoint-torsion LES of the pair (M,dM) is a dim-H1 machine — and Reidemeister torsion is genuinely ABSENT from the corpus
status: todo
type: task
priority: normal
created_at: 2026-08-24T17:34:25Z
updated_at: 2026-08-24T17:35:03Z
---

## The source

`library/2018sorus020/` — Léo Bénard, *Reidemeister torsion on character
varieties* (HAL tel-02108892, 110 pp, 78 sections). **Ingested and UNCITED.** It
is rank **3** in `docs/audits/2026-08-15-library-uncited-triage.md` (score 521.1,
92 extracted candidates) — the highest-scoring uncited source in the library.

Sections that carry the machinery:

- §1.2 Twisted cohomology (`sec-018`) — H^k(M,A) for a Z[Gamma]-module A
- §2.1 The twisted complex with adjoint action (`sec-036`)
- §2.1.2 Computation of the twisted cohomology (`sec-038`)
- §1.5 Reidemeister torsion, three definitions (`sec-033`..`sec-035`)
- §1.4 Alexander module and character varieties (`sec-029`..`sec-031`);
  `sec-031` is specifically the **figure-eight** component of irreducible chars

Verified present, not inferred from titles: the text carries "long exact sequence
of the pair (M, dM)" and "long exact sequence in cohomology : 0 -> H^0(Cone(phi))
-> H^1(M, Ad.rho)_v".

## The check that mattered — a symbol collision I nearly walked into

The corpus has a `QOU.Torsion.*` namespace, which makes "the corpus already has
torsion machinery" look obvious. **It is a different word.** `QOU/Torsion/`
contains BraneTower, Descent, GlobalGluing, MassIdentity, YekutieliTriple — the
gerbe / twisted-2-cocycle sense. And every corpus hit for "Reidemeister" is a
Reidemeister **MOVE** (R1/R2/R3), not Reidemeister **torsion**: `grep -rn
Reidemeister content/ computations/ docs/` outside `library/` returns moves,
`reidemeister-action-table`, `conj:reidemeister-mass-invariance` — zero torsion.

So Reidemeister torsion is genuinely absent from this corpus. That is the honest
version of the finding, and it is a cleaner one than the identification would
have been. (AGENTS.md: attributes do not transfer across overloaded symbols.)

## Why H^1(M, Ad.rho) is the interesting shape

The canonical chain rests on `H^1(Bring) = 2W` carrying exactly 3 real DOF, and
`calibration-cohomology-alignment` (`QOU.Mass.calibrations_eq_cohomology`) is
explicitly a **count/alignment** claim: 3 calibrations = 3 H^1 DOF. It counts;
it does not derive.

Bénard's LES of the pair (M, dM) with adjoint coefficients is a machine for
computing exactly that kind of number — dim H^1 with Ad.rho coefficients on a
knot complement — from the boundary torus data.

**NOT an identification.** H^1(Bring) (Bring's surface) and H^1(M, Ad.rho) (a
knot complement) are different spaces and I am not claiming they are the same
object, or that either dimension count transfers. What is claimed: the corpus's
central count has the same SHAPE as a quantity this thesis computes, and the
corpus currently has no derivation of it. Whether the shapes connect is the
open question, and answering "no" would be a real result too.

## The adjacent rung it may actually serve first

`qou-m3ad` (in-progress, high) reframed Route C's M3 from "build a CoHA" to
"derive the index set Omega", and landed `QOU/QBeta/AdjointIndexSetM3.lean`
sorry-free with **H_Ad, the sl_2 adjoint, as the knot-independent core**. That
is the same `Ad` representation Bénard's §2.1 computes cohomology of, for knot
complements including 4_1 — one of the two certified-DT knots (`qou-rtec`).

Coordinate with `qou-m3ad` before touching this; per AGENTS.md an open-outcome
research overlap is permitted but must declare its distinct angle.

Also worth noting from the same triage table: rank 4 is
`arxiv-1601.02479v5` *Cohomological Donaldson-Thomas theory of a quiver with
potential*, and rank 7 `arxiv-1511.00400v2` *Reidemeister torsion, hyperbolic
three-manifolds, and character varieties* — both uncited. `qou-rtec`'s D1 rung
is literally "construct the (Q,W)". The three top-ranked uncited sources are
the three things the open arcs need; that is worth someone's attention
independent of this bean.
