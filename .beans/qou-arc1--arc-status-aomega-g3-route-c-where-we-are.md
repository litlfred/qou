---
# qou-arc1
title: 'ARC STATUS: A_omega / G3 / Route C — what is settled, what is open, and the four options at the decision point'
status: in-progress
type: milestone
priority: high
tags:
    - g3-aomega
    - route-c
    - arc-status
created_at: 2026-08-11T11:40:00Z
updated_at: 2026-08-11T11:40:00Z
---

Consolidated position after the 2026-08-11 session (PR #4972). Read this before opening any
new A_omega work — it supersedes the stale framing in qou-vr3q.

## SETTLED (proved or verified this arc)

 * A_omega = 3 is LANDED as a certified DT count, CONDITIONAL on conj:stokes-dt-bps-bridge
   (StokesQZeroDTCount, sorry-free). Non-degeneracy gate passed on the closed GPPV/GGM sector;
   the open-HOMFLY Gukov-Stosic sector (det(4_1)=5) correctly REJECTED.
 * Uniqueness leg CLOSED sorry-free (DoublyPeriodicLiouville + FaddeevPhiPhysical).
 * PROVENANCE: the 5_2 Stokes matrices are DERIVED from the eq-(98) DT array via GGM's
   elementary products, not transcribed (StokesMatrixProvenance.lean). The -9 is a product
   artifact. Residual exposure shrinks to one small integer array.
 * FULLY PROVED, INPUT-INDEPENDENT: ChiralityGradedCount.lean — no symmetric scalar can recover
   a chirality-split count; and amphichiral_cannot_witness_obstruction PROVES a single
   amphichiral knot (4_1) cannot separate scalar-from-graded, so the cross-knot gate is a
   logical necessity.
 * Scalar avenue PROVABLY EXHAUSTED (Driver14 no_scalar_matches_chirality_split_datum + the new
   general theorem). Route A's R1 (#connections = A-poly L-degree) was the best scalar ever
   found — hits the dtMax vector (3,4) — and it still falls.
 * M1 CONFIRMED + GGM eq-(200) q^1 ERRATUM identified by two independent routes (qou-m1fx).
 * q-Bessel/Askey blocks validated (qou-qbes). NOTE the convergence: the GGM holomorphic blocks
   ARE q-Hahn Bessel functions, so the Askey thread and the A_omega thread meet in one object.

## CORRECTIONS LANDED (the corpus was wrong)

 * qou-3ent: A_omega = 3 is the OFF-DIAGONAL Stokes constant; eq (21) is DIAGONAL-ONLY and that
   entry's q^0 is 1. "3 is a 3d-index coefficient" is NOT supported by any exact statement.
 * The 3 is NOT 4_1-specific: 3 = s(1) for s(x) = x+1+x^-1, and the SAME s(x) governs 5_2
   (s(1)=3, s(1)+1=4). Any 4_1-invariant explanation is refuted before it starts.
 * The trace-field disc(Q(sqrt-3)) = -3 reading: refuted (co-occurring 4).

## THE LOAD-BEARING OPEN ITEM (qou-q3np)

 A_omega -> S(muon)=+0.00968298 / S(proton)=-0.03945936 has NO literature support (329 uploads
 swept, all 7 keyword matches false positives) AND a structural obstruction: Stokes constants
 are INTEGERS (3, 9, 75, 642, 5580, ...) while the targets are small non-integer OPPOSITE-SIGNED
 reals. Nothing in the corpus addresses the sign asymmetry, the co-occurring 4, or the tower.

## THE FOUR OPTIONS AT THIS DECISION POINT

 O1. SCOPE HONESTLY (cheapest, recommended first). Record in the content blocks that A_omega -> S
     is a conjecture with no literature support; scope downstream claims. Costs nothing, removes
     a standing over-claim. Does not close anything.
 O2. ATTACK THE MECHANISM. Find/derive a map from an integer Stokes constant to a small signed
     real residual. Must explain the sign asymmetry, the co-occurring 4, and the tower. This is
     the only route that would make A_omega -> S a result rather than a hope. High risk, high
     value, genuinely open.
 O3. ROUTE C PROPER (M1 done -> M2/M3). Build the closed-sector (Q,W) and its BPS cohomology,
     then the Hecke->BPS bridge. M3 is literature-open (DT categorification) = research
     programme, not a session. M2 is a finite computation and IS tractable.
 O4. PIVOT AWAY. Bank the proved/verified results (they stand on their own: provenance, the
     chirality obstruction, the erratum) and stop investing in the A_omega periphery until O1/O2
     resolves. Explicitly permitted by the evidence.

 RECOMMENDATION: O1 now (it is nearly free and it is honest), then decide between O2 and O4.
 O3-M2 is worth doing only if O2 looks survivable — otherwise it elaborates a periphery whose
 connection to physics is unestablished.
