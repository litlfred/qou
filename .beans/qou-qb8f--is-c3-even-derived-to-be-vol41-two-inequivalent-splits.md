---
# qou-qb8f
title: 'Is c_3^even DERIVED to be -Vol(4_1)? Two inequivalent splits live in the corpus'
status: completed
type: task
priority: high
created_at: 2026-08-08T10:45:00Z
updated_at: 2026-08-08T10:45:00Z
---

Raised (not adjudicated) from PR #4724 after retracting an S_leak-based filter.
This is for the c_3 owners (#4725 / the ck-dk registry maintainers) to settle.

`SLeakZeroCrossing.lean:11` defines
    S_leak(q0) := c_3(q0) + Vol(4_1)
and calls it "the bar-odd residual of c_3 after removing the bar-even
amphichiral -Vol(4_1) face". That reading requires c_3^even = -Vol(4_1)
EXACTLY. Three problems found; none is a claim the Lean is wrong.

1. NOT EMPIRICALLY ACCESSIBLE. c_3^even(q) = (c_3(q) + c_3(1/q))/2 needs c_3 at
   q ~ 0.901. Both anchors sit at q ~ 1.10998. No anchor data can determine the
   bar-split; it must come from an assumed structural form.

2. THE SIGN FLIP IS OFFSET-GENERIC. S_leak(mu) > 0 > S_leak(p) holds for ANY
   constant V strictly in (-c_3(mu), -c_3(p)) = (2.02020024, 2.06934258), a
   window of width 0.0491. Verified: Vol(4_1), 2+1/36, 2+1/30, 2+1/25, 2+1/24,
   63/31, e^0.708 -- 7/7 give the SAME flip
   (computations/qbeta/sleak_offset_genericity_check.py). So the flip restates
   "c_3 differs between anchors"; it is not evidence about Vol(4_1).

3. TWO INEQUIVALENT SPLITS IN THE CORPUS.
   - 2026-07-07-c3-even-solved-s-complex-volume-rigidity.md (the audit cited for
     "c_3^even is solved"): bar-even channel = exact Q(sqrt3) u-ladder,
     e_1 = 3sqrt3/4, projection rung ~ +86.66; bar-odd scalar S = Q_beta/E_0
     ~ 908, which does NOT sign-flip (S_p/S_mu ~ 1.024).
   - S_leak framing: even part = -Vol(4_1) ~ -2.03, odd residual ~ 0.0097.
   These are not the same decomposition. SLeakZeroCrossing.lean guards the
   SYMBOL collision between the two S's, but that guard does not reconcile the
   two EVEN parts. And the 2026-07-07 audit tiers the V_q identification
   "exploratory" in its own header.

NOT A CLAIM THE LEAN IS WRONG: sleak_zero_between_anchors and
sign_definite_carrier_excluded are stated for a GENERIC continuous function
with the anchor signs as hypotheses, and are fine as stated. What is
unsupported is the interpretive step that S_leak IS c_3's bar-odd part.

Questions to settle:
(a) Is there a derivation of c_3^even = -Vol(4_1), or is it a near-match?
    (D(z)+D(w) = Vol(4_1) to 4e-18 is the volume of 4_1 -- that identity is
    real, but it does not by itself say c_3^even equals it.)
(b) If yes, which of the two even-part claims is canonical, and should the
    other be re-scoped?
(c) Should the registry's c_3 row carry a pointer either way?

Generic guard added so this class does not recur: AGENTS.md
"Defined residual != derived decomposition (STRICT, 2026-08-08)".

---

# ANSWERED (2026-08-08, PR #4742): (H1) is NOT derived — it CONTRADICTS the
# canonical split. Scope-(a).

Probe: computations/qbeta/c3_even_canonical_split_contradiction.py (7/7).
Audit: docs/audits/2026-08-08-c3-even-vol41-contradicts-canonical-split.md.

## (a) Is c_3^even = -Vol(4_1) derived?  NO — and worse than underived.

The bar-split is not measurable from anchor data (needs c_3 at q ~ 0.901; both
anchors sit at q ~ 1.10998), so it was tested for CONSISTENCY against the
corpus's derived split instead.

2026-07-07 audit §2 gives c_3^odd = kappa_(2,1)(q)*S with the DERIVED bar-odd
carrier kappa_(2,1) = (q-1)^3(q+1)/q^2 (verified kappa(1/q) = -kappa(q)
symbolically) and the archimedean scalar S = Q_beta/E_0, quoted INDEPENDENTLY
as S_p ~ 908.4, S_mu ~ 886.8, S_p/S_mu ~ 1.024.

Inverting c_3 = -kappa*S under the hypothesis c_3^even = 0:

  proton  S_recon = 908.3624831   vs audit 908.4   rel dev 4.1e-5
  muon    S_recon = 886.7905751   vs audit 886.8   rel dev 1.1e-5
  S_p/S_mu = 1.02432582           vs audit 1.024

So the canonical decomposition has c_3 essentially PURELY BAR-ODD:
c_3^even ~ 0, NOT -2.03. Separation = 98.09% of |c_3|. The two readings are
INCOMPATIBLE, not merely distinct.

## What S_leak actually is: a 209x cancellation artifact

  proton  c_3 = -2.06934258 + Vol(4_1) -> -0.039459367   (98.093% cancelled)
  muon    c_3 = -2.02020024 + Vol(4_1) -> +0.0096829728  (99.521% cancelled)

  anchor swing of c_3     2.4325%
  anchor swing of S_leak  507.51%
  amplification           208.63x

c_3's own 2.4% swing is REAL (the dc_3/dq ~ 4.6e6 obstruction stands). The extra
209x is arithmetic. Any argument reading S_leak's RELATIVE swing as structural
sensitivity is reading the cancellation.

## (b) Which even-part claim is canonical?  The kappa*S split.

## CORRECTION to this bean's own framing (recorded, not deleted)

This bean said "two inequivalent SPLITS", citing c_3^even ~ +86.66. Imprecise
twice:
 1. +86.66 is a PROJECTION ARTIFACT — the 2026-07-07 audit says so itself
    ("the honest rungs are the e_k"; e_1 = 3sqrt3/4, margin 9, residuals 0).
 2. It is a DIFFERENT OBJECT — the k=3 rung of the bar-even channel of log R,
    not the bar-even PART of the c_3 Taylor coefficient. Same glyph, two
    referents (the overloaded-symbol trap, AGENTS.md conditional-proved rule 4).

Sharp statement: (H1) contradicts the derived kappa*S split. Not "rival values".

## NOT refuted (scope-(a) boundary)

Vol(4_1) as an ingredient elsewhere; 4_1's amphichirality; and EVERY theorem in
SLeakZeroCrossing.lean / SLeakMagnitude{Offset,Taylor}Ratio.lean — all generic
and hypothesis-carrying, all stand. Only the interpretive sentence is affected.
No Lean edited; the docstring fix belongs to those files' owners (#4734 notified).

## (c) Registry pointer — UNANSWERED, left to the registry maintainers.

## Follow-on

c_3^even ~ 0, if right, is itself a structural claim worth PROVING rather than
inferring from a 1e-5 two-anchor cross-check. Filed as a note here, not a bean,
pending the owners' read.
