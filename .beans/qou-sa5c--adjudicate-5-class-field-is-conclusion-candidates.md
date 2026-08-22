---
# qou-sa5c
title: 'Adjudicate the 5 class-field-is-conclusion candidates the fixed self-assuming detector surfaced'
status: todo
type: task
priority: normal
created_at: 2026-08-22T21:20:00Z
updated_at: 2026-08-22T21:20:00Z
---

`scripts/lean-self-assuming-audit.py` was blind to the class-instance self-assuming variant
(bean qou-24m2, fixed 2026-08-22). With the fix it goes 0 -> 5 candidates on `content`. These are
CANDIDATES for agent inspection, not verdicts -- the script's own docstring is explicit about that.
Each has a class field whose DECLARED TYPE is syntactically the theorem's conclusion, projected as
the entire proof, which is the shape AGENTS.md 3b-cond rule 5 calls degenerate:

1. QOU/Archimedean/MassTowerOpenProblemsClasses.lean:71  term7_structural
   hT.alpha5_derived : exists a : R, a < 0 and a = alpha5_value
2. QOU/Archimedean/QHookBound.lean:608  qFact_ratio_bound
   hi.bound : |qFactReal q k / k! - 1| <= (q - q^-1)^2 * k * (k+1) * (2k+1) / 36
3. QOU/BraidKnot/LpDualityHypothesisClass.lean:158  theorem_3_via_class
   hyp.dualityGapZero : lp.duality_gap = 0
4. QOU/Infra/Polylogarithm.lean:157  beta3_via_class
   h.value_at_4 : imLi3ZetaPredicted 4 = beta3
5. molecular-construction/h2s-angle-s3-braid-holonomy.lean:39  opening_eq_holonomy_of_conj
   h.angle_eq_holonomy : d.angleOpeningDeg = d.s3BraidHolonomyDeg

Spot-checked #3 and it is a KNOWN, DOCUMENTED case, not a false positive: the file argues at
L140-152 that carrying the instance for a *specific* `lp` is the correct 3b-cond pattern, and it
already beans the real modelling fix as qou-7t1n ("OperatorSelectionLP needs its constraint data
plus feasibility/boundedness/optimality predicates, and the duality result should be conditional on
those"). So the detector is finding the genuine shape and the corpus already knows about at least
one of them.

The remaining four are UNADJUDICATED. For each, the 3b-cond rule-5 test is whether the class
axiomatises the theorem's *hypotheses* (legitimate) or its *conclusion* (degenerate -- the theorem
merely projects it). Do not assume degenerate from the detector hit alone; read the file, and where
it is genuinely conditional check whether the class carries real sub-hypotheses the theorem then
composes.
