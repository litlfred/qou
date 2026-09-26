---
# qou-cgrc
title: 'DONE — fully proved, input-independent chirality obstruction (no transcription dependency): ChiralityGradedCount.lean'
status: completed
type: task
priority: high
tags:
    - g3-aomega
    - route-c
created_at: 2026-08-11T10:50:00Z
updated_at: 2026-09-26T11:03:16Z
parent: qou-rtec
---

Answers the owner's "work on making fully proved theorem". QOU/QBeta/ChiralityGradedCount.lean
(core Int, no Mathlib, lean-direct exit 0) proves the structural content for ARBITRARY integers,
so it has ZERO dependence on any transcribed literature value:

  mirror_involutive, barEven_mirror (+1 eigenvector), barOdd_mirror (-1 eigenvector)
  barGrading_faithful_general      2a = even+odd, 2b = even-odd  (no information lost)
  chiral_iff_odd_ne_zero           chiral <-> bar-odd part nonzero
  amphichiral_collapse             a=b  =>  odd=0 and the pair is its own mirror
  symmetric_scalar_cannot_separate ANY symmetric g agrees on (a,b) and (b,a)  [THE obstruction]
  symmetric_scalar_loses_chirality chiral => g blind while odd != 0
  amphichiral_cannot_witness_obstruction  <-- methodological payload: PROOF that a single
        amphichiral knot (4_1) is structurally incapable of separating scalar from graded, so
        the cross-knot gate is a LOGICAL NECESSITY, not a stylistic preference.

The knot numbers (4,3)/(3,3) appear ONLY as instances (dtSplit52/dtSplit41), never as
hypotheses. This is the clean separation the transcription problem demanded: general theorem
proved outright; literature values quarantined into instances.
