---
# qou-3j5m
title: 'toffoli-lp-stability straddles C and D in one file: D Gram, C-frame Phi and P_77 feeding the witness'
status: in-progress
type: task
priority: normal
created_at: 2026-08-29T16:33:50Z
updated_at: 2026-08-30T09:49:28Z
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


## RETRACTION 2026-08-29 — I claimed the diagonal was derived. It is not.

Commit 039910ce46 ("derive P_77 too") is WRONG on its central claim and this
supersedes it. What it got right: (q-1)/(q+1) == h*z_C^2 exactly, h = q - 1/q.
What does not follow: that P_77 = z + h z^2 is THE decomposition.

BOTH of these are exact at z_C:

    P_77 = z + (q-1)/(q+1)     constant + degree 1
    P_77 = z + h z^2           no constant, degree 2

and they DISAGREE at the canonical z. At q0: 0.664811117281 vs 0.691166478358.
The off-diagonal P_66 carries the same ambiguity — both c0 + c1 z and c1 z + c2 z^2
reproduce it exactly with coefficients rational in q.

THE REASON IS COUNTABLE. The parity split in s = sqrt(q) gives TWO equations (the
rational part, the sqrt part). A z-polynomial of degree <= 3 has FOUR unknowns.
Uniqueness needs the degree and the constant term fixed from outside the data.

WHY Phi SURVIVES AND THE DIAGONAL DOES NOT. `toffoli-transfer-matrix-proof.md`
STATES Phi's chain: P_flip = V_1 * Delta_0, V_0 = z a_0 + b_0. That forces no
constant term and degree exactly 2 — two unknowns, two equations, determined. The
corpus states no such chain for the diagonal. So the difference between "derived"
and "undetermined" here is a sentence of prose in one block, not a property of the
arithmetic. I mistook a consistent fit for a derivation, which is the exact error
class this arc exists to catch.

CONSEQUENCE FOR THE OWNER'S OPTION 1 (correct the blocks to the D forms):
**it is only half-completable today.** Phi can be corrected. The diagonal cannot,
so the q_star = 1/phi^2 golden-ratio threshold can be SCOPED as C-frame but not
replaced. The half-D chapter I named as Option 1's risk is unavoidable without new
input.

WHAT WOULD SETTLE IT: the Hecke element whose Markov trace is the diagonal. Every
element of H_3 traces to sum_w c_w z^{|w|} on the normal-form basis [(), (0,), (1,),
(0,1), (1,0), (0,1,0)], so the element gives all four coefficients at once and the
D form immediately. Reconstructing the 3-strand Toffoli transfer matrix from the
braid is the open work, and it is real work, not a sweep.


## UN-RETRACTION 2026-08-29 — the construction exists, and it settles the diagonal

My retraction was correct given only the published closed form, and over-cautious
given the corpus. `computations/_deprecated/toffoli-braid.py` records the
construction the content blocks report:

    V_i     = z*a_i + b_i     (a_i, b_i) from chain_reduce -- RATIONAL in q, no z
    P_{k,k} = prod_i V_i      over range(A-1); for A = 3, TWO factors

So the diagonal is (z a_0 + b_0)(z a_1 + b_1): degree exactly 2, and whether a
constant appears is DECIDED by the ordering, not assumed. Computing it for state
7 = |111> (all-pp, every crossing (c,d) = (1,0)):

    P_77 = z + h z^2,  h = q - 1/q,  CONSTANT TERM ZERO

and at z_C that reproduces the published (q + q^{1/2} - 1)/(q + 1) EXACTLY
(symbolic zero). So:

    P_77_D(q) = q^3 (q^4 + 1) / (q^2 + 1)^2,  positive for every q > 0

The rival z + (q-1)/(q+1) (0.6648 at q0 vs 0.6912) is excluded by the construction.

FOUR POSITIONS ON ONE QUESTION, recorded because the pattern is the lesson:
  v1 conditional     -- a fit with no backing. Right to be cautious.
  v2 derived         -- right answer, wrong reasoning (an identity at z_C does not
                        single out a decomposition).
  v3 undetermined    -- correct given ONLY the closed form; 2 equations, 4 unknowns.
  v4 derived         -- from the construction. A NEW SOURCE, not v2's argument again.

The general lesson: when a decomposition is underdetermined by the data, do not
stop at "undetermined" -- look for the construction. It was in the tree, in a
_deprecated file, and neither the content blocks nor the live producer cite it.

A DISCREPANCY I CANNOT RESOLVE, reported: the same construction does NOT reproduce
the published P_66 = (q^4 + q^{7/2} + 2q^{3/2} + q^{1/2} - 1)/(2(q+1)^2) for ANY of
the eight 3-strand orderings. Residual -0.186 at q0, -2.23 at q = 2 -- far outside
rounding. P_77 from the same code matches exactly, so the construction is the
credible side, but what the published P_66 IS remains open. Someone should look.

OPTION 1 IS NOW COMPLETABLE for both thresholds: q_Phi (via Phi_D) and q_star (via
P_77_D). P_66's interpretation-table entry needs the discrepancy settled first.


## 2026-08-29 — OPTION 1 IS BLOCKED, and P_66 was the smallest part of it

Chasing the P_66 discrepancy found that it is not a P_66 problem. Probe:
computations/probes/toffoli_published_vs_construction_audit.py (4/4).

The ONLY construction the corpus records is
`computations/_deprecated/toffoli-braid.py` — a file neither the content blocks
nor the live producer cite. An independent reconstruction of it (written from the
content block's prose) reproduces that producer EXACTLY, symbolic zero on both
diagonals. So the recipe is the framework's, not my paraphrase.

Against it, of the four published entries ONE matches, at q = 111/100:

    P_77   construction  0.5514527845   published  0.5514527845   MATCH
    P_66   construction  0.4153790120   published  0.6010         NO
    P_76   construction -0.1415316448   published +0.0495 (=Phi)  NO
    P_67   construction +0.1415316448   published -0.0495         NO

WORSE, THE PROOF BLOCK'S KEY LEMMA IS CONVENTION-DEPENDENT. "Target-flip
blindness of the control crossing", Delta_1 = 0, is what reduces the 1-jet to
P_flip = V_1 * Delta_0 and hence to c * Phi. chain_reduce pairs generator i with
every j > i, so generator 1 is the crossing (1,2) — control-control only if the
TARGET IS STRAND 0. The producer's toffoli_output flips `k & 1`, the LAST strand.

    target = last  (producer)       Delta_1 = -0.1045   NOT zero
    target = first (block's prose)  Delta_1 =  0        zero

AND EVEN UNDER THE BLOCK'S OWN CONVENTION the chain does not give the published
Phi: V_1^par * Delta_0 = -0.0466748 against Phi = +0.0495489, ratio -0.942 — 6% in
magnitude and a sign flip.

WHAT THIS DOES TO THE CONVENTION WORK. The Phi derivation upstream (A z^2 + B z,
A and B rational) is still correct AS ALGEBRA about the published closed form, and
P_77 is safe because it matches its construction. But for Phi, P_66 and P_67 the
prior question is now open: the published closed form is not what the recorded
construction produces, so migrating it to convention D would carry the discrepancy
to a new value and make it harder to see.

SO OPTION 1 SPLITS:
  * P_77 / q_star = 1/phi^2  -- CAN be corrected. Derived, matches its construction.
  * Phi / q_Phi = 0.4656     -- SHOULD NOT be, until the discrepancy is adjudicated.
  * P_66, P_67                -- same.

NOT CLAIMED: that the published forms are wrong. The construction is in a
_deprecated file and may itself be superseded by a derivation not in the tree.
What is established is that the two disagree on three of four entries, that the
key lemma is convention-dependent and false as the producer runs, and that the
corpus does not record which side is current. That is an owner call.


## WHICH OBJECT IS CURRENT — answered from the deprecation criteria themselves

`computations/_deprecated/README.md` states the criteria for that directory:

  "dead exploratory probes ... - no content block consumes them ... - no audit report
   cites them - the witness body itself contains no assertions"

So toffoli-braid.py was moved for being ORPHANED, not for being WRONG. That is a
WIRING judgement, not a correctness one, and it inverts the natural reading of
"deprecated".

And the live producer does not derive anything. `toffoli-lp-stability.py` defines
`toffoli_diagonal` and `q_and_amplitude` as HARD-CODED closed forms, evaluates them
on a q-grid, computes `gram_matrix(q)` alongside, and NEVER connects the two — the
Gram is used only for eigenvalues. So:

  * published closed forms  -- transcribed literals in the content blocks AND in the
                               live producer. NO derivation anywhere in the tree.
  * the construction        -- derives all 64 entries from crossing coefficients,
                               and its P_77 matches the published P_77 exactly.

VERDICT. Derivable: the construction, uniquely — it is the only thing in the tree
that computes these amplitudes from anything. Canonical: the construction has the
stronger claim (it derives, it agrees on the one entry that can be checked, and its
deprecation was about consumers). The three disagreements are most plausibly
TRANSCRIPTION DRIFT in hand-written content blocks that nothing re-derived — which
is also why the producer got orphaned: nothing consumed it, so nothing caught it.

Caveats kept: the construction is z_C-based and A = 3 only, and an unrecorded
derivation cannot be excluded. This is an owner call, not mine to close.

## THE GOLDEN THRESHOLD ITSELF SURVIVES — a scope correction to my own framing

I had been writing as though q_star = 1/phi^2 were C-frame. It is not. It has TWO
independent sources in the corpus:

  1. the root of s^2 + s - 1 in the Weierstrass coefficient of the Descartes curve
     E_q (descartes-elliptic-curve.md: 5(s^2+s-1)(4s^4-s^3-4s^2+s+4)/(27 s^3)) --
     NO z anywhere in it, hence convention-independent;
  2. the zero of the Toffoli diagonal P_77 -- z_C-derived, and gone under D.

So the threshold stands; the whole golden-ratio structure of the info-theory
chapter (golden-ratio-transport, golden-threshold-time-marker, julia-set-reeb,
golden-julia-dynamics) rests on (1) and is untouched. What convention D removes is
the COINCIDENCE that the Toffoli diagonal also vanishes there. That is a far more
contained claim than the one I was about to make, and getting it wrong would have
mis-scoped a dozen blocks.

## EXECUTED: the P_77 / q_star half of Option 1 (4 blocks)

  toffoli-transfer-matrix.md              item 6 + a Convention scope note with the
                                          derived P_77^D and the coincidence framing
  toffoli-lp-stability.md                 the "P_77 vanishes at q_star" threshold row
  fivefold-sheets-golden-ratio.md         replaced my earlier placeholder scope note
                                          with the derived form
  toffoli-transfer-matrix-interpretation  the P_77 table row, both frames

NOT touched, per the audit above: Phi, q_Phi, P_66, P_67.


## A FOURTH disagreement — and it WEAKENS my own "transcription drift" reading

Tested the block's UNIVERSALITY claim: P_flip = c_{k1k2} * Phi with c = 1 for every
control pair, so all three amplitudes equal Phi = +0.0495 (the interpretation
table lists all three as "1x"). Against the construction, target = last strand:

    pp      -0.1306159003
    mixed   -0.1176706540
    nn      -0.1070109882

Three DIFFERENT values, all negative where the table says +0.0495. So the
construction does not produce the universal factorization the block's Statement 1
asserts.

WHY THIS MATTERS FOR THE VERDICT. I wrote that the three disagreements were "most
plausibly transcription drift in hand-written blocks". That reading is now weaker:
a mistyped number cannot produce a STRUCTURAL claim. Universality is either a real
property of some derivation, or a mistake in one. So either

  (a) the published forms come from a different, unrecorded derivation that DOES
      have universality -- in which case the construction is not the current object
      despite being the only one in the tree that computes; or
  (b) that derivation is wrong.

I cannot distinguish these, and I should not have leaned as far toward drift as I
did. What stands unchanged: the construction is the ONLY thing in the tree that
derives anything here, it agrees with the published P_77 exactly, and its
deprecation was about consumers rather than correctness.

Running total: 4 independent disagreements (P_66 value, P_76/P_67 value AND sign,
the Delta_1 = 0 lemma, universality) against 1 agreement (P_77).


## 2026-08-29 — the adjudication material is complete; universality settles which branch is open

The investigation asked for (\"which of the two disagreeing objects is current
and derivable/canonical\") is done for the P_77 half and blocked-with-reason for
the other three. Summary of what is now measured
(computations/probes/toffoli_published_vs_construction_audit.py, 6/6):

**P_77 — SETTLED, published == construction.** The published closed form
(q + sqrt(q) - 1)/(q + 1) is exactly what _deprecated/toffoli-braid.py produces
(symbolic zero). It is convention C, it is derivable, and its convention-D
partner q^3(q^4+1)/(q^2+1)^2 is now derived and carried in the blocks. Done.

**Phi, P_66, P_67 — NOT settled, and now demonstrably NOT this construction.**

    P_66   construction 0.4153790120   published 0.6010017280
    P_76   construction -0.1415316448  published +0.0495489435 (claimed = Phi)
    P_67   construction +0.1415316448  published -0.0495489435

Two structural facts on top of the numeric gap:

1. The proof block's key lemma Delta_1 = 0 (\"target-flip blindness of the
   control crossing\") is convention-dependent. chain_reduce pairs generator i
   with every j > i, so generator 1 is the crossing (1,2) — control-control only
   if the target is strand 0. The producer's toffoli_output flips k & 1, the LAST
   strand. Measured: target = last, Delta_1 = -0.1045 (not zero); target = first,
   Delta_1 = 0.

2. **Universality fails under BOTH indexings.** The block asserts
   P_flip = c_{k1k2} * Phi with c = 1 for every control pair; the interpretation
   table lists all three as +0.0495 \"1x\". At q = 111/100:

       control   target = LAST   target = FIRST   first / Phi
       pp         -0.13061590     -0.04667483      -0.9420
       mixed      -0.11767065     -0.03258679      -0.6577
       nn         -0.10701099     -0.02078434      -0.4195

   Three amplitudes, not one — including in the target-FIRST reading, which is
   the block's own prose and the only one where its key lemma holds.

**Why (2) is the load-bearing one.** It closes a branch I could not close
before. A number that disagrees can be transcription drift; a structural
property that fails cannot be. So \"the published trio is this construction,
mis-copied\" is out. What remains is a branch this probe cannot test: an
unrecorded derivation absent from the tree. The construction lives in a
_deprecated file that neither the content blocks nor the live producer cite, so
that is a real possibility, not a formality.

**Consequence for the convention work.** Migrating Phi / P_66 / P_67 to
convention D would carry an unresolved disagreement to a new value, so it stays
blocked on the owner. P_77 is unaffected and is done. The straddle this bean
opened with — toffoli-lp-stability.py computing physical_q0_stable from two
C-frame closed forms inside a D-Gram file — is unchanged and still live; the
P_77 half of it is now at least derivable in both frames.

**Open, for the owner.** Which is the framework's object for Phi / P_66 / P_67:
the published closed forms, or _deprecated/toffoli-braid.py? Nothing in the tree
records it, and the two disagree in value AND in structure. I have deliberately
not edited those blocks.


## RESOLVED BY DERIVATION 2026-08-30 (owner: "no determination. we need to rederive/investigate/resolve")

`computations/probes/toffoli_trio_rederivation.py`, 6/6 assertions. Five results.

**R1. Φ is not in the construction's image AT ALL.** Exhaustive exact-rational
search — 32 objects (both generators × all 8 orderings, plus every
parent–daughter difference over both indexings) and all 528 pairwise products,
at six q where √q is rational, in `Fraction` arithmetic: **zero matches**, as a
single object or as a product of two.

The structural reason, and it is decisive: split Φ over the ℚ(q)-basis {1, √q}
and its z-coefficient is **(q³−1)/(2(q+1))** — a `(q+1)` in the DENOMINATOR.
Every `chain_reduce` object has denominators that are powers of q alone, because
the only source of one is `h = q − 1/q`. A `(q+1)` cannot arise. So
`P₇₆ = 1·Φ` is unrecoverable under ANY indexing or convention: the right-hand
side is not a quantity this construction produces.

**R2. The producer OVERWRITES its own entry, and the committed value is the
overwrite.** `build_matrix` loops k = 0..7 and, when the Toffoli output m ≠ k,
writes BOTH `M[m][k]` and `M[k][m]`. Only k = 6 and k = 7 qualify — and they are
each other's m, so both iterations write both cells and **k = 7, running last,
wins**. At q = 111/100:

    parent |110> (the docstring's convention)   -0.13061590026045
    parent |111> (the k=7 overwrite)            -0.14153164476025   <- the witness

**R3. And the overwrite is deliberate — it IMPOSES the antisymmetry.** The
second write is commented *"Reverse transition (use parent context for
antisymmetry)"* and uses `V_par` for both directions. With one shared context
`P₆₇ = −P₇₆` holds trivially. Derived honestly — each entry from its own input
column, as the docstring specifies — **antisymmetry is FALSE in both
conventions**. Block item 4 is not a result; it is an assumption implemented by
using the wrong parent for one of the two entries. Same shape as asserting a
value and proving it by `rfl`.

**R4. The block contradicts itself twice, without any external object.**
(a) Item 1 factors `P_flip = c·Φ` and its own table gives **c = 1 for all three
control pairs** — so item 1 asserts universality. But the same table's `d`
column differs per pair, and item 2 says `V̂₁ = zc + d` is "type-dependent". The
factorization drops `d`, which is where the type-dependence lives.
(b) The opening sentence fixes "target strand 3"; item 2's `Δ₁ = 0` requires the
target to be strand 1. `toffoli_output` flips `k & 1`, the LAST strand — so the
opening sentence is the framework's convention and item 2 is the false one.

**R5. What survives.** `P₇₇` reproduces the published closed form exactly
(symbolic zero), and block item 5 (all target-flip amplitudes vanish as q → 1)
**holds** — the derived `P₇₆` retains its `(q−1)` factor. Two of the block's
claims stand; three do not.

## The derived replacements

    convention C   P_76 = -(q-1)(q^2+3q+1) / (2q(q+1))        [rational in q]
    convention D   P_76 = -(q-1)(q+1)(q^6+q^4+2q^2+1) / (2q(q^2+1)^2)
    convention D   P_67 =  (q-1)(q+1)(2q^6+q^4+q^2+1) / (2q(q^2+1)^2)
    convention D   P_66 =  (q^4+1)(q^4+q^2+2) / (4q(q^2+1)^2)
    convention D   P_77 =  q^3(q^4+1) / (q^2+1)^2             [unchanged]

## What is NOT claimed

That the published forms are arbitrary. An unrecorded derivation could still
produce them and this probe cannot speak to one absent from the tree. What is
settled: the corpus's own recorded construction does not, under any indexing or
convention, and three of the block's four claims are false against it — two of
them by the block's own internal contradiction.

## Still to do

The content edits: `toffoli-transfer-matrix.md` items 1-4, and
`toffoli-q-and.md`, whose entire factor-anatomy section describes Φ's factors
`(q^{3/2}+q^{1/2}-1)` and `(q^{3/2}+q+1)` — including the q ≈ 0.466 sign-reversal
threshold, which belongs to a polynomial the construction does not produce.


## REOPENED 2026-08-30 — the straddle this bean OPENED on is now fixed, and it flips a headline claim

The bean's original scope — `computations/toffoli-lp-stability.py` computing its
Gram in convention **D** while `toffoli_diagonal()` and `q_and_amplitude()` were
hard-coded convention-**C** closed forms, both feeding `physical_q0_stable` —
was never fixed by the derivation tranche. Fixed now, and the result is not
cosmetic.

**Migrated:**
* `toffoli_diagonal` → `P₇₇^D = q³(q⁴+1)/(q²+1)²`. A straight frame change.
* `q_and_amplitude` → the **derived** `P₇₆^D = −(q−1)(q+1)(q⁶+q⁴+2q²+1)/(2q(q²+1)²)`.
  NOT a frame change: the published Φ is not in the construction's image.
* Both C forms retained as `*_HISTORICAL`, unwired, with the reason.

**`physical_q0_stable` now reports False, and that is the honest answer.**

    P_77 C (published)   +0.5514        P_77 D (derived)   +0.6912
    Phi  C (published)   +0.0495
    P_76 C (derived)     -0.1306        P_76 D (derived)   -0.1438

The block claims: *"P₇₇(q₀) ≈ 0.5514, Φ(q₀) ≈ 0.0495. **Both are strictly
positive.** The q-Toffoli is LP-stable at the physical substrate value."* The
positivity half fails.

**And it is NOT a convention artefact.** The derived q-AND is negative at q₀ in
convention **C** as well as D. The failure follows from replacing Φ with the
amplitude the construction actually produces, not from the frame change. A
migration alone would have left the claim standing.

**Both stability thresholds also vanish.** `stable_regime_lp` was "q > q⋆" and
`stable_regime_physical` was "(q⋆, q_Φ) ∪ (1, ∞)". Under the derived forms
`P₇₇^D` is strictly positive for **all** q > 0 (no q⋆ to be above), and the
derived q-AND's sextic `q⁶+q⁴+2q²+1` has **no positive real root** (no q_Φ) — so
its only sign change on q > 0 is at q = 1. Conclusions rewritten to what is
measured.

## THE DECISION, and it is the owner's

**Is positivity the right LP-stability criterion for the target-flip
amplitude, or is non-vanishing?**

* **What it means.** The gate tests `P₇₇(q₀) > 0 AND q_AND(q₀) > 0`. The
  diagonal passes. The q-AND is a *transition* amplitude; whether its sign
  carries physical meaning, or only its magnitude, is a modelling question the
  producer cannot settle. If non-vanishing is the criterion, the q-Toffoli is
  stable at q₀ after all (|P₇₆| = 0.1438 ≠ 0) and only the *wording* of the
  claim needs correcting.
* **What it costs.** Positivity: rewrite item 4 of `prop:toffoli-lp-stability`
  to its negation, and revisit item 1's "all Hecke amplitudes carry the correct
  sign". Non-vanishing: a one-line criterion change plus a corrected sentence.
* **What it risks.** Choosing non-vanishing *because it keeps the claim green*
  is exactly the move the anti-fit discipline forbids; it needs an independent
  reason. Choosing positivity retires a published stability result.
* **What it commits to.** Either way the block's quoted numbers (0.5514,
  0.0495) go — the first is C-frame, the second is not an object of the
  construction.
* **Default if nothing is done.** The witness reports `physical_q0_stable:
  False` with the criterion recorded beside it, and the content block still
  claims stability. That inconsistency is live and visible, which is better
  than a silently-weakened gate, but it should not stand for long.

**My judgement, not a finding:** I would NOT weaken the criterion. The block
states positivity as the LP-feasibility condition in item 1 as well as item 4,
so positivity is what the framework claims, and the honest correction is to
retire the claim rather than re-tune the test to survive it.

**Content block deliberately NOT edited** pending that call.


## 2026-08-30 — I ANSWERED MY OWN BLOCKING QUESTION FROM THE CORPUS, and nearly claimed something false on the way

I asked the owner: positivity or non-vanishing? Before asking again I ran the
corpus-grep I should have run first. It settles the question, and it caught a
wrong claim I was one step from making.

### The near-miss, recorded because it is the point

Reading `operator-selection-lp.md` I found the LP's feasibility conditions are
the net constraint, **Frobenius positivity `Σ_j G_ij x_j ≥ 0`** on the
Gram-weighted selection vector, and boundedness — none of which mentions a
transfer-matrix entry. And `toffoli-lp-stability.py` **solves no LP at all**: no
`linprog`, no selection vector, no net constraint, no dual. I was about to
conclude *"the stability gate is unconnected to the LP it is named for"*.

**That would have been wrong.** `toffoli-lp-stability-proof.md` states the link
explicitly:

> *"Positivity of `G·t(q)` therefore reduces to the positivity of the product
> `P_{7,7}(q)·W_std(q)` with the appropriate sign from `Φ(q)`."*

So there IS a stated reduction from LP feasibility to amplitude positivity. The
producer not solving an LP is by design — the reduction is what licenses the
sign test. **Checking the proof block before generalising from the producer is
what saved this.**

### The question is ANSWERED: positivity

The proof block makes amplitude positivity the LP-feasibility condition and
says so twice ("all amplitudes of the correct sign"; "The proof stands on the
two amplitude positivities"). So positivity is what the framework claims, not a
choice I get to make — my recommendation was right, but it is now settled by
the corpus rather than by my judgement. **The owner does not need to rule on
this.**

### But the proof block carries three claims the derivation retires — all measured

**Claim 1: "For q > 1: both P₇₇(q) > 0 and Φ(q) > 0."**

    q            1.1          1.5          2            5
    P_77 D    +0.6715      +1.9371      +5.4400     +115.75
    P_76 D    -0.1301      -0.8660      -2.6700      -57.873
    P_76 C    -0.1193      -0.5167      -0.9167       -2.7333

The derived q-AND is negative for **every** q > 1, in both conventions. FAILS.

**Claim 2: the two positivities "are convention-independent".** `P₇₇` has a
positive zero in C (`q⋆ = 1/φ² = 0.38197`) and its convention-D numerator
`q³(q⁴+1)` has **no** positive real root. FAILS.

**Claim 3: the thresholds.** `q⋆` comes from `x²+x−1`, the numerator of the
convention-C diagonal; `q_Φ ≈ 0.4656` from `x³+x−1`, a factor of Φ, which is
not in the construction's image. Both derive from retired objects.

### The residual gap — a finding, not a question

The reduction itself is asserted, not derived, and the unspecified part is
precisely the one that matters here: *"with the appropriate sign from `Φ(q)`"*.
Nothing in the source says what the appropriate sign IS or why. So even with
positivity established as the criterion, whether a **negative** target-flip
amplitude actually breaks `G·t ≥ 0` is not established by the corpus — it is
the missing step in a reduction the proof block states in one clause.

That is the honest residue, and it belongs in the proof block as an open note
rather than as a question to the owner.


## RESOLVED 2026-08-30 — PR #6095, four commits

The blocking question this bean carried — *is the LP-stability criterion
POSITIVITY or NON-VANISHING?* — was raised as an owner decision and **did
not need one.** `toffoli-lp-stability-proof.md` states the criterion twice
and both times it is positivity ("Positivity of G·t(q) therefore reduces to
the positivity of the product P_77·W_std"; "the proof stands on the two
amplitude positivities"), and `prop:operator-selection-lp` agrees at the LP
level — its Frobenius constraint is `Sum_j G_ij x_j >= 0`, an inequality.
So the recommendation I gave was right and is now settled by the source
rather than by my judgement. Question withdrawn from the PR.

WHAT THAT COSTS, narrowly. The proof reduces `G·t >= 0` to positivity of
`P_77 · W_std` "with the appropriate sign from Phi(q)". First half survives
untouched (`P_77·W_std = +0.4624` at q0, positive for all q > 0). Second
half is the retired one, and the qualifying clause now carrying the weight
is asserted in that one sub-clause and derived NOWHERE. So: the argument
for stability does not close. NOT that the gate is LP-unstable — no block
claims that, in either direction.

NINE BLOCKS corrected, not one. The retired objects (Phi, the golden-ratio
threshold q*, the antisymmetry P_67 = -P_76) had reached eight blocks
downstream of the one #6033 fixed:
toffoli-lp-stability{,-proof,-table1-data,-table2-data},
toffoli-transfer-matrix-{interpretation,proof},
tm-interactions{,-table2-data}, q-game-of-life{,-proof,-interpretation}.
Derived at q0 under D: P_77 +0.6912, P_66 +0.5407, P_67 +0.1572,
P_76 -0.1438.

TWO LEAN DEFECTS, both PRE-EXISTING and both found only because the
verification was actually run:

  1. toffoli-lp-stability.lean DID NOT COMPILE ON MAIN. `q_param` is
     unresolvable there — it lives in namespace QOU.GroundRing and the file
     imports only QOU.QuantumObservableUniverse. Confirmed by lean-direct
     against `git show origin/main:...`, same error, line 38. A content-block
     Lean sibling is covered by NO CI, so nothing would ever have caught it.
  2. `toffoli_shadow_bounded : exists k, 0 < k and k < 10 := <303/100,...>`
     removed. Vacuous (mentions no Toffoli, no Gram, no q) AND its constant
     is a number the content block retired on 2026-08-09. Zero consumers.

`toffoli_lp_stable` kept, proof untouched — `q > q* <-> q + sqrt q - 1 > 0`
is a true fact about a real function; only the docstring identifying that
function with a live amplitude is withdrawn.

VERIFIED: lean-direct exit 0 against the real 15-module import cone;
#print axioms clean on all six theorems, no sorryAx; render preflight clean
on all nine .md; qa-sweep re-run on 11 sidecars; re-verified after rebasing
onto main (124 commits), branch-only diff byte-identical across the rebase.


## CORRECTION 2026-08-30 — my "the corpus settles it" was an over-claim

The prepare-merge rebase surfaced sibling bean qou-nmqd, which reached the same
convention-D derivation independently and landed first. Its body states, of
positivity vs non-vanishing: "They are not the same condition and cannot both
be the criterion."

I had written that the corpus settles the question outright, in the PR body and
in the entry above. That is too strong and is corrected. What the corpus settles
is narrower, per-property:

  LP FEASIBILITY -> positivity.  prop:operator-selection-lp's Frobenius
                    constraint is the INEQUALITY sum_j G_ij x_j >= 0, and the
                    LP proof states the amplitude condition as positivity twice.
  UNIVERSALITY   -> non-vanishing.  rem:toffoli-q-and needs the flip channel to
                    FIRE, and says P_76(q) != 0 for every q != 1.  A NEGATIVE
                    amplitude fires; universality is untouched at q0.

So the two are not rivals -- each is right for its own property, which is where
I disagree with the sibling. But the sibling is right that something is still
open, and it is not what either of us first said it was: what is open is WHICH
OF THE TWO PROPERTIES the phrase "the evolution is well-defined" is asserting.
prop:q-game-of-life has historically meant both at once and they have now come
apart at the substrate.

Both readings are now stated in q-game-of-life.md with the open item named in
those terms, so the corpus is honest under either.

A SECOND GAP, upstream of the choice and surfaced by neither branch: the LP
proof reduces feasibility to positivity of P_77 * W_std "with the appropriate
sign from" the off-diagonal amplitude, and that clause is derived NOWHERE. The
first factor survives (P_77 * W_std = +0.4624 at q0, positive for all q > 0).
Deciding the property above does not close this; it is prior to it.

FILED SEPARATELY while running prepare-merge: qou-cr3v, two scratch_*.lean
files on main duplicating real modules (6 un-importable FQN collisions, gate at
63 vs baseline 57). Not this arc's, not this branch's regression.
