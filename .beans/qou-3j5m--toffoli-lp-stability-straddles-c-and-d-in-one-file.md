---
# qou-3j5m
title: 'toffoli-lp-stability straddles C and D in one file: D Gram, C-frame Phi and P_77 feeding the witness'
status: todo
type: task
priority: normal
created_at: 2026-08-29T16:33:50Z
updated_at: 2026-08-29T17:40:47Z
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


## Two follow-ons from tracing the other phi appearances

I said the corpus's other golden-ratio appearances were "different construction,
not examined" and that checking was cheap. Checked. One is a defect, one is not
mine to claim.

### (A) fivefold-sheets-golden-ratio names the WRONG polynomial — measured

The block reads: "The q-AND polynomial P_{7,6}(q) has a zero at q = 1/phi^2".

    P_77(1/phi^2) = 0.0            <- zero, this is the DIAGONAL
    P_76(1/phi^2) = 0.038196601    <- NOT zero
    P_76's actual zero            = 0.465571231876768027, root of q^{3/2}+q^{1/2}-1

So the zero belongs to the Toffoli diagonal P_77, not to the q-AND amplitude
P_76 = Phi. A plain wrong-symbol defect, independent of any convention question,
and it is in the paper. Corrected in place, and the C-frame scope added rather
than leaving a C-frame identification stated unconditionally.

### (B) golden-ratio-degeneration-brings is a SEPARATE construction — NOT claimed

Its (s^2 + s - 1) comes from the Descartes/Bring Weierstrass coefficient
(descartes-elliptic-curve.md: 5(s^2+s-1)(4s^4-s^3-4s^2+s+4)/(27 s^3)), not from
the z*c + d recipe. Same quadratic in s = sqrt(q), different origin.

So the same quadratic surfaces in two independent places, and only ONE of them is
proved z_C-derived. Whether the elliptic curve's s is the same sqrt(q) and whether
ITS phi is convention-dependent is a separate question I have NOT answered, and I
am not asserting it. Recording the coincidence because it is the obvious next
thing to check and because assuming it either way would be wrong.

The beans qou-84in / qou-r4hg / qou-zpgk (golden window, SubstrateRegime.lean)
were not examined at all.


## DERIVED 2026-08-29 — and my own "a z-swap is not a migration" caveat was too strong HERE

Probe: computations/probes/toffoli_qand_convention_d_derivation.py (3/3 pass)

I declined the swap on the c_k-ladder precedent. That precedent is right in general
and does not apply to Phi, for a reason the proof block supplies itself.

`toffoli-transfer-matrix-proof.md` gives the chain:

    V_1 = z*c + d,  Delta_1 = 0 for a target flip,
    P_flip = V_1 * Delta_0,  V_0 = z*a_0 + b_0
    => Phi = z*(z*Delta_a0 + Delta_b0) = Delta_a0 * z^2 + Delta_b0 * z

So Phi is a QUADRATIC IN z whose coefficients are properties of the chain. And the
decomposition is UNIQUE: z_C = sqrt(q)/(q+1) is not in Q(q), so {1, z_C} is a
Q(q)-basis of Q(q)(sqrt q) and matching rational vs sqrt parts pins A and B.
Splitting the published Phi by parity in s = sqrt(q):

    A = Delta_a0 = (q-1)^2 (q+1)^2 / (2q)         BOTH RATIONAL IN q
    B = Delta_b0 = (q-1)(q^2+q+1) / (2(q+1))      hence frame-independent

and A*z_C^2 + B*z_C - Phi_published = 0 SYMBOLICALLY, not numerically.

The convention therefore enters through z ALONE. Evaluating the same A, B at the
canonical z_D is the framework's own construction at the canonical parameter, not a
substitution into a foreign closed form.

    Phi_D(q) = q^3 (q-1) (q^6 + 2q^5 + q^4 - q^3 + q^2 + q + 1)
               -------------------------------------------------
                          2 (q+1) (q^2+1)^2

THE CONSEQUENCE, and it is a content-level one. The sextic has NO REAL ROOTS
(sympy real_roots = []), so Phi_D vanishes on (0, inf) at **q = 1 only** — the
classical limit the block already states as item 5. Convention C additionally had
the root of q^{3/2}+q^{1/2}-1 at q = 0.465571231876768027, which
`toffoli-q-and.md` publishes as a threshold "below which the q-AND changes sign,
imparting a phase reversal to the target", and which
`toffoli-lp-stability-proof.md` solves for as q_Phi ~ 0.4656.

**That second threshold does not exist under the canonical convention.**
Phi_D(0.4656) = -0.0209, not zero.

At q0 both are positive (Phi_C = 0.0495, Phi_D = 0.0625, ratio 1.261), so the
q-GoL STABILITY VERDICT survives. What does not survive is the phase-reversal
threshold and every magnitude.

STILL NOT DERIVED: the diagonal P_77. The same uniqueness gives P_77 = z +
(q-1)/(q+1) as the unique z-linear form, but the proof block does not state that
the diagonal HAS that shape — its V_1 table gives d = 0 for the pp pair — so the
D-frame diagonal is conditional on that shape, not derived. Which means the
1/phi^2 golden-ratio threshold is established as C-frame (previous entry) but its
D replacement is NOT yet known.
