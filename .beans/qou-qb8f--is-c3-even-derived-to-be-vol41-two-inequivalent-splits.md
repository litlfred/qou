---
# qou-qb8f
title: 'Is c_3^even DERIVED to be -Vol(4_1)? Two inequivalent splits live in the corpus'
status: todo
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
