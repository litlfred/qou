---
# qou-n226
title: GeometricShape's shape_ne_zero and shape_ne_one are redundant given im_pos
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:06:00Z
updated_at: 2026-10-04T15:20:37Z
parent: 08a2
---

MINOR, recorded not changed. shared-denominator-cusp-holonomy.lean:92 declares

    structure GeometricShape (z : C) : Prop where
      shape_ne_zero : z != 0
      shape_ne_one  : z != 1
      im_pos        : 0 < z.im

The third field implies the other two - both 0 and 1 are real, and no point with positive imaginary part is real. Proved on branch claude/lean-prove-assertions-2026-09-04 as QOU.QPochhammer.shape_ne_zero_ne_one, which is why the retyped alg-geom class could use Mathlib's UpperHalfPlane (definitionally {z : C // 0 < z.im}) rather than a bespoke structure.

NOT A DEFECT. The redundant fields are true and document intent (Thurston's two degeneracies). Left alone because that is a separate conjecture block whose author revised it deliberately on 2026-08-31 (bean qou-z9ws). Fold them into im_pos only if that file is being touched anyway.
