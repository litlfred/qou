---
# qou-5w53
title: 'GAP: Δ_λ binding magnitude via extended Bloch group'
status: todo
type: task
priority: normal
created_at: 2026-08-16T13:22:26Z
updated_at: 2026-08-16T13:42:50Z
---

WALL REPORT (PR #5242). No Delta_lambda number proposed; nothing inverted from CODATA.

W1 PROVED, scope-(b): the VOLUME leg of the extended-Bloch regulator is identically zero at
   the deuteron, at ANY tetrahedron count, flattening-independent.
   Invariant: Bloch-Wigner is conjugation-odd, D(zbar) = -D(z); a real is its own conjugate.
   The committed triangulation has BOTH shapes real (0.5, 2.0), so Vol = 0 by symmetry alone.
   Count-independence is the sharp part: every summand is individually zero, so the quantity
   that was supposed to grow like A does not grow at all. Flattening shifts the IMAGINARY
   part, so the move that distinguishes this route from a fit is powerless on this leg.
   Lean: QOU.MassTheory.BlochVolumeLeg, sorry-free, #print axioms clean.

W2 MEASURED (pure geometry, zero experimental input): census-frame volumes are non-monotone
   in A.  A=2 6_2 4.400833 | A=3 8_11 8.286317 | A=4 L6a4 7.327725.
   Vol(A=4) < Vol(A=3). The 4He term's extensivity comes from an explicit A factor written
   into B_4 = 2*m_e*A*Vol(L6a4), not from the geometry.

W3 BLOCKING -> bean qou-e5jf. Three inconsistent deuteron knot assignments differing by the
   whole of Vol(6_2). Cannot derive a knot invariant while the knot is undetermined.

W4 SURVIVING: the CS leg. Untouched by W1, and flattening is load-bearing there. But
   admissible_correction (FiveTwoSaddleSumRule.lean 7g) gives R-hat valued in C/pi^2 Z, so CS
   is determined only mod pi^2. An additive MeV term needs a definite real. Fixing that branch
   by what matches AME is the forbidden fit.
   OPEN QUESTION: can CS be pinned to a definite real by the gluing and parity equations alone?

BRIEF CORRECTIONS: bean qou-wojw does not exist (real one is qou-985x, todo);
docs/coordination/2026-08-08-main-review-workplan.md never existed (meant
2026-08-07-l2-volume-binding-cluster.md); PR #4798's O(100x) gauge freedom is ALREADY CLOSED
by #4848 with answer zero, Lean-proved -- it was offered as the live hook and is not live.

CHEAPEST NEXT FOOTHOLD: bean qou-fl4t (restore the DG flattening monomial dropped in
whitehead_c_sigma_torsion.py). Not a per-lambda ansatz, so it escapes #5234's scaling wall,
and one-loop-triangulation-invariance.witness.json:248 records that the c=1 calibration used
to justify dropping it cannot detect its absence.
