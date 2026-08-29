---
# qou-3j5m
title: 'toffoli-lp-stability straddles C and D in one file: D Gram, C-frame Phi and P_77 feeding the witness'
status: todo
type: task
priority: normal
created_at: 2026-08-29T16:33:50Z
updated_at: 2026-08-29T16:39:15Z
---

FOUND 2026-08-29 while reviewing what landed on main for the y_lambda/convention-D
arc (qou-qdtk, qou-ulxr, both now closed). This is the SAME CLASS in a different
chapter, reached by a different accessor -- which is why the y_lambda-keyed audit
(computations/audits/ylambda_threerow_frame_audit.py) never saw it.

MEASURED, in computations/toffoli-lp-stability.py:

  line 136  gram_matrix()        z = q**3 / (q**2 + 1)   # convention D  <- labelled
  line  74  toffoli_diagonal()   (q + mp.sqrt(q) - 1) / (q + 1)
  line  81  q_and_amplitude()    (q-1)(q*s+s-1)(q*s+q+1) / (2*(q+1)**2), s = sqrt(q)

Both closed forms are LIVE -- 7 uses each -- and both reach the witness:

  line 196  "P_77":      toffoli_diagonal(q)
  line 197  "Phi_qAND":  q_and_amplitude(q)
  line 241  "physical_q0_stable": toffoli_diagonal(Q0) > 0 and q_and_amplitude(Q0) > 0

So the q-GoL block's HEADLINE STABILITY CLAIM is computed entirely from the two
C-frame forms, in a file whose Gram matrix is explicitly convention D.

WHY THEY ARE CONVENTION C, structurally rather than by pattern-match: half-integer
powers of q cannot arise from a rational function of q. z_D = q^3/(q^2+1) is
rational; z_C = sqrt(q)/(q+1) is not. The `(q+1)^2` denominator is the C
fingerprint and `(q^2+1)` is D's -- the same discriminator AGENTS.md records for
the Markov peel ("(q^2+1) divides the denominator" as a complete convention test).

AND Phi IS z-DERIVED, so this is not an incidental sqrt: content/quantum-observable-
universe/information-theory/toffoli-transfer-matrix.md item 2 states the traced
volume as `V_1 = z(q)*c + d`. A quantity built from z(q) inherits the convention.

BLAST RADIUS, in the paper rather than the call graph. Every block quoting Phi or
P_77 is quoting a C-frame number:
  information-theory/q-game-of-life.md              (the q-AND amplitude; the
                                                     stability condition; "q0 ~ 1.110
                                                     lies safely inside the stable
                                                     regime")
  information-theory/toffoli-transfer-matrix.md      (defines Phi)
  information-theory/toffoli-transfer-matrix-interpretation.md
  information-theory/toffoli-q-and.md                (the q ~ 0.466 sign-change
                                                     threshold)
  information-theory/toffoli-lp-stability-proof.md   (solves Phi(q) = 0; q_Phi ~ 0.4656)
  information-theory/toffoli-lp-stability-table{1,2}-data.md

NOT ESTABLISHED, and deliberately not guessed:
  * what Phi is under D. The derivation chain from z to Phi is content-side and I
    did not reconstruct it. Substituting z_D into the existing closed form is NOT
    a migration -- the same rule AGENTS.md states for the c_k ladder.
  * how far the numbers move, hence whether the stability verdict survives. The
    C-frame threshold q_Phi ~ 0.4656 is a root of (q^{3/2} + q^{1/2} - 1); under D
    the corresponding object is a different function with a different root set, so
    the quoted MARGIN between q0 and the threshold is C-frame too.

SCOPE: (a). This says the file computes two conventions at once and that the
published stability numbers are C's. It does NOT say the stability conclusion is
wrong -- that needs the D derivation, which is the actual work here.


## PROVED 2026-08-29, not inferred — and the golden ratio is a C artifact

The `sqrt(q)` was suggestive, not proof: a square root can enter from a framing
factor with nothing to do with z. So I RECONSTRUCTED the published closed form
from the transfer-matrix block's own recipe instead.

Probe: computations/probes/toffoli_diagonal_convention_frame_probe.py
Witness: toffoli-diagonal-convention-frame.witness.json (3 assertions, all passed)
mpmath 50 dps, no float64.

RESULT 1 — the frame is identified, exactly.

    P_77 published  ==  z_C(q) + (q-1)/(q+1)

over 7 values of q, worst |difference| **1.34e-51**. Against z_D the SMALLEST
|difference| over the same values is 0.113 — never close. So the published
diagonal IS the `V_1 = z*c + d` recipe at c = 1, d = (q-1)/(q+1), with z = z_C.

RESULT 2 — the golden-ratio threshold does not survive the convention.

    1/phi^2                        0.3819660112501051518
    P_77(1/phi^2), published (C)   0.0            <- vanishes exactly
    same recipe with z_D there    -0.398580917583 <- does not vanish
    its root instead               0.66313789836736143447   (+73.6%)

The content block's "vanishes exactly at the golden ratio threshold q = 1/phi^2"
is a property of the C-frame closed form, not of the gate.

RESULT 3 — at q0 the VERDICT survives; the NUMBER does not.

    published (C)      0.551443414318   positive
    same recipe, z_D   0.664811117281   positive     gap +20.6%

So "q0 lies safely inside the stable regime" is unaffected. What is affected is
every quoted magnitude and every quoted threshold.

SCOPE, and the boundary is the point. Substituting z_D into a closed form derived
under C is NOT a migration — AGENTS.md states this for the c_k ladder and it
applies verbatim. The z_D column does NOT say what the convention-D Toffoli
diagonal is. It says the golden-ratio root is NOT FRAME-INVARIANT, hence cannot
be quoted unconditionally. Deriving the D-frame diagonal is the open work.

WORTH FLAGGING TO WHOEVER PICKS THIS UP: the golden ratio recurs across the corpus
(beans qou-84in, qou-r4hg, qou-zpgk are golden-window items; there is also
brings-surface/fivefold-sheets-golden-ratio and golden-ratio-degeneration-brings).
This result says NOTHING about those — they are a different construction and I did
not look at them. But an appearance of phi that traces back to a z_C closed form is
now a known failure mode, and checking is cheap: reconstruct from the recipe and
swap z.
