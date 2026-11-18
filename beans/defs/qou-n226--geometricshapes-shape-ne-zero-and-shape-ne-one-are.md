---
# qou-n226
title: GeometricShape's shape_ne_zero and shape_ne_one are redundant given im_pos
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:06:00Z
updated_at: 2026-11-18T11:12:15Z
parent: 08a2
---

MINOR, recorded not changed. shared-denominator-cusp-holonomy.lean:92 declares

    structure GeometricShape (z : C) : Prop where
      shape_ne_zero : z != 0
      shape_ne_one  : z != 1
      im_pos        : 0 < z.im

The third field implies the other two - both 0 and 1 are real, and no point with positive imaginary part is real. Proved on branch claude/lean-prove-assertions-2026-09-04 as QOU.QPochhammer.shape_ne_zero_ne_one, which is why the retyped alg-geom class could use Mathlib's UpperHalfPlane (definitionally {z : C // 0 < z.im}) rather than a bespoke structure.

NOT A DEFECT. The redundant fields are true and document intent (Thurston's two degeneracies). Left alone because that is a separate conjecture block whose author revised it deliberately on 2026-08-31 (bean qou-z9ws). Fold them into im_pos only if that file is being touched anyway.

- Round 82 (`lane-e667`): Formalized `qou-71ma`, `qou-n226`, `qou-oilr`, `qou-omuz`, `qou-wxmm` in `QOU.Foundations.ValuationGradeSelectionUpperHalfPlaneNonDegeneracyTwistedPairCohomologyDimensionLaurentRingUnitDivisionLinearDualityCertificate` with 80-dps `mpmath` 2-commit witness stamp (`84401456f07c58b1279d96f566c292313ce4c028` -> `0c9aa2b99fc76a7fc726e889fc36119e8f63d65c`, `scriptHash=f07174204f482f7a01972e149c17324ec39a978434a088c3f7d45077e7857c97`) in PR `litlfred/qou#8441` (`status: in-progress`).
