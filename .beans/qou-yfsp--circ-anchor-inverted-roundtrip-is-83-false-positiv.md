---
# qou-yfsp
title: circ-anchor-inverted-roundtrip is ~83% false positives — docstring matching + no direction check
status: todo
type: bug
priority: high
created_at: 2026-08-07T20:54:55Z
updated_at: 2026-08-07T20:54:55Z
---

MEASURED FROM A FULL DRAIN. Adjudicating all 11 outstanding candidates in the
circular-anchor ledger (bean qou-i3yg, 2026-08-07) found the
`circ-anchor-inverted-roundtrip` criterion firing almost entirely on noise:

    5 of 6 anchor-inverted candidates were FALSE POSITIVES (~83%).

The one true positive (VOL_41 in computations/_deprecated/full-derivation-verified.py,
genuinely inverted to obtain q0) is in deprecated code.

TWO CONCRETE DEFECTS, both visible in the recorded evidence strings:

1. "CONFIRMATION LANGUAGE" IS MATCHED INSIDE DOCSTRINGS. Every false positive
   quotes its supposed confirmation from the module docstring, not from a
   reported check:
     - DPS:  "confirmation at line 23: 'ε − tr_M|z = h·(z − 1) ...'"  (a formula
             in the docstring)
     - Q0:   "confirmation at line 16: '...the three confirmed atoms...'"
     - P:    "confirmation at line 23 / line 16" (both docstring prose)
   FIX: strip docstrings and comments before scanning for confirmation
   language, the same way the Lean vacuity audit strips comments.

2. "INVERTED TO DEFINE" IS REALLY JUST "USED DOWNSTREAM". The detector reports
   `DPS = 50` as "inverted to define h" (DPS is an mpmath precision knob used on
   the very next line as `mp.mp.dps = DPS + 15`; it does not define h = q - 1/q
   at all), and `N_VERIFY_SYMBOLIC = 10` as "inverted to define stray_sqrt" (it
   is a loop bound). Even the plausible-looking `Q0 -> H` is wrong in DIRECTION:
   `H = Q0 - 1.0/Q0` is a FORWARD definition from Q0; nothing recovers Q0 from H.
   FIX: require the flagged constant to actually be RE-DERIVED from the quantity
   it defines (a genuine round-trip), not merely to appear upstream of it.
   Direction is the whole content of the criterion.

WHY THIS MATTERS RATHER THAN BEING COSMETIC: a criterion that is ~83% noise
trains agents to skim and clear it, which is exactly how the T4 circularity —
the case this whole axis was built for — would slip through a future sweep. A
high-recall detector is fine; a high-recall detector whose evidence strings are
visibly nonsense is worse than none, because it destroys the reviewer's prior.

SEPARATE, ALREADY APPLIED (2026-08-07): `circ-vacuous-check` now distinguishes a
hardcoded True from a hardcoded False. A literal False cannot manufacture a
passing claim — two of the five vacuous-check candidates were legitimate
recordings of negative results (a rejected tensor-product baseline, and a probe
whose filename ends `_negative`). Only always-PASSES is the hazard.

ALSO WORTH SCOPING: 2 of the 11 candidates are in computations/_deprecated/.
Consider excluding that directory, or reporting it in a separate bucket.
