---
# qou-ywh9
title: 'Degree-N volume form: does anything in axioms 1-4 supply degree 3?'
status: completed
type: task
priority: high
created_at: 2026-09-04T02:10:09Z
updated_at: 2026-09-04T02:45:39Z
parent: qou-8lxd
---


## Result 2026-09-04 (branch claude/w-derived-from-axioms-2026-09-04). Sibling of qou-j3w6.

Audit: docs/audits/2026-09-04-w-derived-not-postulated-degree-of-the-volume-form.md
Lean:  QOU/QuantumObservableUniverse/VolumeFormDegree.lean (11 decls, sorry-free,
       lean-direct exit 0, axioms at most [propext, Quot.sound])

PROVED. A volume form of degree N forces rank N, and the complementary power
Lambda^{N-1} equals Lambda^1 iff N = 2. So SELF-DUALITY OF V IS A DEGREE-2
ACCIDENT, not a separate axiom: at N=3 the same input gives W^dual = Lambda^2 W,
the SU(3) relation 3bar = Lambda^2 3 -- exactly the complex type that
gate_forces_complex_of_dim_three demands. V and W are the same construction at
different degrees, so W need not be postulated. This answers the owner's
objection that V is derived from axioms and W should be too.

OPEN (this bean's question). Does anything in axioms 1-4 supply degree 3?
Lead, recorded and NOT asserted: axiom 4's c_1(Ad(A)) = 0 is, in the usual
reading, triviality of the top exterior power of Ad(A) -- a volume form of
degree rank(Ad(A)). No Lean carrier for categorical Chern classes exists, and
the corpus says nothing about rank(Ad(A)).

Avenues measured this pass.
- (1) "i arises like q": REAL and located (rem:commutative-crossing-energy,
  rem:affine-chart-origin-of-i-and-q) but PROSE-tier; the Lean takes i^2 = -1 as
  a HYPOTHESIS, so the template itself is undischarged.
- (4) tetraplectic: degree 4 (psi^m), not 3. Its only degree-3 object is a
  3-VECTOR field on Sp(1) = S^3. The corpus layer derives one thing, the su(2)
  bracket. qou-8p1f / qou-8p1g already close the routes out.
- (5) affine-W compactifies to S^3: REFUTED scope-(b) -- the parallel volume form
  has infinite mass and does not extend across infinity; and complexification of
  a real rep is self-conjugate, so no real 3-manifold carries complex type.
- UNTOUCHED: groupoid, derived categories.

Where the negatives point: complex from the start -- a holomorphic (3,0)-form,
SL(3,C) contains SU(3). Real dimension 6, so S^6 = G2/SU(3), not S^3. The corpus
has that door open in three unjoined places (eightfold item 3; qou-8p1f's
constructive half at 3-forms in dim 7; qou-ko4g's note that G2/SO(4) is absent).

Two corpus defects found on the way, framed in the audit, not fixed here:
the ambient-S3 contradiction (rem:markov-trace-ambient-s3 vs the 2026-06-28
audit), and W overloaded (rank-2 Hodge plane vs 3-dim eightfold object).

**CLOSED 2026-09-04.** `CategoricalCoordinateForced.lean` (10 decls, sorry-free, arbitrary `CommRing`) discharges "the categorical structure forces R[i]": Cayley-Hamilton at rank 2 with `det` normalised by the volume form turns (tr=0, det=1) into f^2 = -1. No square root assumed. Also settles the CRT defect (C[i]/(i^2+1) is not C). Front B's separate finding -- c_1(Ad(A)) is defined by deferral to a tau landing in R-Mod, where every Chern class is trivially zero -- retires the c_1 lead on two independent grounds; see the PR #6546 comment.
