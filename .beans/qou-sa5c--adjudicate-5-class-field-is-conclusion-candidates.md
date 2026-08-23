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

## 2026-08-22 — ADJUDICATED (all 5). Shape alone is NOT the verdict; severity varies sharply.
Discriminator: field-type == conclusion establishes the SHAPE (that is what the regex matches);
what decides laundering is whether the class has a PROVED instance and whether the file documents
its posture. Measured per candidate:

| # | class | instance? | verdict |
|---|---|---|---|
| 1 | Term7ShellCorrectionClass (MassTowerOpenProblemsClasses:71) | YES (L85) but on the PLACEHOLDER `alpha5_value = -1` | NEEDS ATTENTION |
| 2 | QFactRatioBound (QHookBound:608) | **NONE** | NEEDS ATTENTION |
| 3 | HasFiniteLPDuality (LpDualityHypothesisClass:158) | NONE, deliberately | OK — known + documented |
| 4 | TheoremA.value_at_4 (Polylogarithm:157) | YES, discharged by sorry-free `beta3_from_jonquiere` | OK — honest |
| 5 | H2SAngleS3HolonomyConjecture (h2s-angle-s3-braid-holonomy:39) | NONE | OK — conjecture carrier |

* #4 is HONEST and is the important counterexample to reading a detector hit as a verdict.
  `beta3_from_jonquiere : imLi3ZetaPredicted 4 = beta3` is a real proof (`unfold; field_simp; ring`),
  the instance at L107 discharges `value_at_4` with it, and the file has ZERO sorries. So
  `beta3_via_class` is a redundant convenience wrapper over already-proved content, not laundering.
* #3 is the deliberate 3b-cond posture, documented in-file at L140-152: two false axioms were REMOVED
  and a caller must now supply the instance for their own LP; real modelling work already beaned as
  qou-7t1n. Nothing to do.
* #5 is an explicitly-named `...Conjecture` carrier whose theorem is its conditional form — the
  3b-tax dependent-conjecture pattern. The name states the epistemic status honestly.
* #1 has an instance, but the file itself calls it a "placeholder `alpha5_value = -1`" sign witness,
  so the unconditional content is the sign only, not the value. `term7_structural` derives nothing
  beyond projecting the field.
* #2 is the weakest: field IS the conclusion, NO instance anywhere in the corpus, and unlike #3 the
  posture is undocumented, so `qFact_ratio_bound` proves nothing standalone. Note a substantial
  `nlinarith` bound proof sits immediately above it (L590-606) — the material to inhabit the class
  may already exist, which would turn the theorem into an honest wrapper like #4. Worth checking.

Follow-up needed on #1 and #2 ONLY. Both turn on judgement about the framework's own math (what
`alpha5_value` should be; whether the neighbouring bound proof discharges `QFactRatioBound`), so they
are left for the owner / a targeted session rather than changed here.

Detector-precision result worth keeping: 5/5 hits were the genuine shape (no regex false positives),
but only 2/5 warrant action. That is evidence FOR the script's "candidates for inspection, not
verdicts" framing, not a complaint about it.
