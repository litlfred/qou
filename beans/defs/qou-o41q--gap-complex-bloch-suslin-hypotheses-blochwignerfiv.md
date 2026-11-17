---
# qou-o41q
title: 'GAP: complex Bloch-Suslin hypotheses (BlochWignerFiveTerm, BlochSuslinRigidity) have no instance'
status: in-progress
pr: 8235
updated_at: 2026-11-17T06:55:36Z
type: task
priority: normal
created_at: 2026-11-15T18:12:20Z
updated_at: 2026-11-15T21:20:33Z
parent: qou-r9ih
---

Issue #7942, PR #7946. The real BlochSuslinUniqueness is equivalent to D = 0 (proved: the file's PentagonCoherent has its last two arguments inverted vs Suslin, and with antisymmetry y=1/x gives f(x^2)=2f(x)-2f(-x)). The corrected statement is QOU/Archimedean/BlochSuslinComplex.lean over C with Suslin's orientation. Open: (1) an instance BlochWignerFiveTerm for the Bloch-Wigner function (Mathlib lacks the complex dilogarithm five-term relation); (2) BlochSuslinRigidity (uniqueness of continuous five-term solutions up to scale; Bloch/Suslin K3 rigidity, not in Mathlib). With both, figure8_from_rigidity gives the figure-8 calibration. These are open conjecture classes; do not close this bean until an instance is proved.



## 2026-11-15 — BlochWignerFiveTerm PROVED (commit 1473bdd237, PR #7946)

Sorry-free instance `QOU.Archimedean.blochWignerFiveTerm_blochD : BlochWignerFiveTerm FiveTermProof.blochD`
in `QOU/Archimedean/BlochWignerFiveTermInstance.lean`. Axioms: propext, Classical.choice, Quot.sound.
`blochD` = Neumann–Zagier formula off (1,∞), −D(1/z) on it; equals BlochWigner_lob on Im z > 0 only
(BlochWigner_lob is 0 below the axis, so no instance for it).
Proof: both partials of the five-term sum vanish; ℂ minus a finite set is path connected; D = 0 on ℝ.

STILL OPEN: BlochSuslinRigidity has no instance (Bloch 1978 / Suslin 1991 rigidity). Bean stays open.


2026-11-15 (session 01Qmmkt8): BlochSuslinRigidity FiveTermProof.blochD PROVED, instance blochSuslinRigidity_blochD (QOU/Archimedean/BlochRigidity/Instance.lean), axioms propext/Choice/Quot.sound, commit 6cbad1078a on PR #7946. Not merged yet. Remaining on this bean: owner-requested Dolbeault-layer refactor of D1/D2. Keep open until PR merges.

2026-11-15: Abstract.lean (DolbeaultStructure, eq_mul_of_fiveTermS) and Smooth.lean (smoothDolbeault; J from reebM_i, conj from realStr; blochSuslinRigidity_of_smooth) pushed, 3ca286b9e1 + 7defa5e327, PR #7946. Sorry-free.

## Progress Update (PR #8235)
- **Status**: `in-progress` (awaiting Merge Manager merge of `litlfred/qou#8235` at `83fd5b4cb41e61d75f72ddd82bda505e34bd92f4`).
- **Lean Formalization**: `QOU.QBeta.ThimbleDecompositionAndSymmetricPolytopeBrick.bloch_suslin_antisymmetric_duplication_and_inversion_annihilation` (Dichotomy for the Bloch-Suslin duplication relation D(x^2) = 2*D(x) - 2*D(-x) between odd parity D(x^2) = 4*D(x) and even real-orientation degeneracy D(x^2) = 0.)
- **80-dps Witness**: `computations/probes/thimble-decomposition-and-symmetric-polytope-brick.witness.json` (`scriptHash: e55db77fb2bb`, `scriptCommitSha: 6020aea5785046b552772c9a42fc52ac2db9f3a2`).
