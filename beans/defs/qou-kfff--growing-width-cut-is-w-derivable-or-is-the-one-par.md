---
# qou-kfff
title: 'Growing-width cut: is w derivable, or is the one-parameter family excluded?'
status: completed
type: task
priority: normal
created_at: 2026-08-26T21:36:15Z
updated_at: 2026-08-26T21:49:01Z
---

Closed in the NEGATIVE, without deriving w.

The move: do not ask what fixes w; ask whether ANY constant w works. Two measured facts say no.
  1. S(k)/k is strictly increasing over k=1..64, so g_w(A) = E0*S(floor(wA))/A is non-decreasing in A for every w (verified, 581 values of w on a 0.005 grid over [0.10,3.00]).
  2. B/A is NOT: it peaks at 4He (7.0739) and dips at 6Li (5.3323).
A monotone function times any positive constant stays monotone, so no member of the family -- nor any rescaling of it -- matches both. Failure is in the SHAPE, not the normalisation. Scope (b).

The extensivity that Addendum 23 read as the escape IS the exclusion: a volume law is constant per strand, and constant per strand is monotone per nucleon.

Two corrections to Addendum 23, both measured:
  * 'at w = 3 the cut is the entire system and the entropy is identically zero' is FALSE. S(3A) > 0 at every A (S(6)=2.8437, S(12)=6.6650). S is a TRACE-state entropy, never pure; it is not even symmetric under k <-> n-k, so no Schmidt argument and no 'balanced cut is the maximiser' justification for w=3/2 either.
  * Convergence to ln[2]_q is SLOW -- 6.57 % short at k=64 -- so the asymptotic E0*w*ln[2]_q per nucleon overstates the model everywhere the isotopes actually live.

Probe: computations/meson/growing_width_cut_shape_exclusion_probe.py, 7/7.
Lean: QOU/MassTheory/GrowingWidthCutShapeExclusion.lean, 6 decls, sorry-free.
Audit: Addendum 42. PR #5863.

Honest limitation: S(k)/k monotone is MEASURED on 1..64, not proved for all k; it enters the Lean as a hypothesis. Isotopes reach k <= 48, so the range covers the claim.

Method note worth carrying: an early draft asserted the tie-back to Addendum 23's table using digits I had invented beyond the four the source publishes. The assertion correctly failed. Compare to the precision the source actually carries.
