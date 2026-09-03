---
# qou-rraz
title: 'V2 finding: the 3-body cumulant sign is threshold-forced (b3>0 needs fpn>2/3) — independent of edge set, like-pair typing and energy scale'
status: completed
type: task
priority: normal
created_at: 2026-08-30T02:46:55Z
updated_at: 2026-08-30T02:46:55Z
parent: qou-mhj9
---

PR #6059, commit dfcfa9c6. Lean: QOU/MassTheory/MayerThreeBodySign.lean
(sorry-free, lean-direct exit 0, #print axioms clean on all 5 decls).
Probe: computations/probes/mayer_threebody_sign_threshold_probe.py
(+ witness, allPassed=true, free_parameters=0, mpmath end-to-end).

QUESTION: the 08-29 probe found b3 wrong-signed (-2.744 vs AME +1.426) in all
four convention x typing combos. Is that structural to the Mayer assembly, or
an artifact of the bond typing / the arrangement DOF (qou-m07y)?

ANSWER: structural, and the bound is cheap. Under W = 1 - PROD f normalised at
the deuteron, in W-units b3 = 3*fpn - 2 - P3 with P3 the bond product over
whatever edge set the 3-body system carries. P3 >= 0 (positive bond factors),
so b3 <= 3*fpn - 2, hence

    b3 > 0  REQUIRES  fpn > 2/3.

P3 enters ONLY through positivity. Therefore the bound does not depend on:
  - the EDGE SET  => deriving the bond set (qou-h7mh / item 1) cannot fix the
    3-body sign while the assembly stays 1 - PROD f;
  - the LIKE-PAIR factors f_pp, f_nn (both live inside P3);
  - the ENERGY SCALE => alpha (qou-302y) is a magnitude question and cannot
    bear on this sign.

MEASURED (50 dps, proton pin) -- all four fpn below 2/3:
  D probe2 0.50823 (margin 0.15844) | D chi 0.61269 (0.05398)
  C probe2 0.39486 (0.27180)        | C chi 0.49932 (0.16735)
Edge-set sweep at A=3 (triangle + 3 chains x 2 typings x 2 conventions): b3<0
in all 16, all respecting the cap. Cross-check reproduces the 08-29 MeV b3
exactly (-2.7438574 / -2.02572 / -3.22385 / -2.66794).

SCOPE-(b) on the conjunction {multiplicative assembly, fpn <= 2/3}, invariant
= positivity of a product of positive bond factors. Does NOT exclude the bond
picture; does NOT close the magnitude.

CONSEQUENCE: the defect is UPSTREAM of any weight -- in the ASSEMBLY, not in
the body-order coefficients a_D^(n). This settles the two-locus question the
session opened with (weights vs assembly) in favour of assembly. Any
replacement must change the FUNCTIONAL FORM, or clear fpn > 2/3.
