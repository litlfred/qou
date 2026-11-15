---
# qou-o41q
title: 'GAP: complex Bloch-Suslin hypotheses (BlochWignerFiveTerm, BlochSuslinRigidity) have no instance'
status: todo
type: task
created_at: 2026-11-15T18:12:20Z
updated_at: 2026-11-15T18:12:20Z
parent: qou-r9ih
---

Issue #7942, PR #7946. The real BlochSuslinUniqueness is equivalent to D = 0 (proved: the file's PentagonCoherent has its last two arguments inverted vs Suslin, and with antisymmetry y=1/x gives f(x^2)=2f(x)-2f(-x)). The corrected statement is QOU/Archimedean/BlochSuslinComplex.lean over C with Suslin's orientation. Open: (1) an instance BlochWignerFiveTerm for the Bloch-Wigner function (Mathlib lacks the complex dilogarithm five-term relation); (2) BlochSuslinRigidity (uniqueness of continuous five-term solutions up to scale; Bloch/Suslin K3 rigidity, not in Mathlib). With both, figure8_from_rigidity gives the figure-8 calibration. These are open conjecture classes; do not close this bean until an instance is proved.
