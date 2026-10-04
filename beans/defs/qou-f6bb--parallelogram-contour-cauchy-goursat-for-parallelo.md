---
# qou-f6bb
title: 'Parallelogram contour: Cauchy-Goursat for parallelograms'
status: completed
type: task
priority: normal
tags:
    - mathlib
    - reorg-2026-10-04
created_at: 2026-08-24T06:35:58Z
updated_at: 2026-10-04T15:21:58Z
parent: qou-c8p8
---

Build: contour integral API for parallelograms. Mathlib has rectangles (integral_boundary_rect_eq_zero_of_differentiable_on_off_countable) but not parallelograms. Need: (1) parameterize parallelogram boundary, (2) prove Cauchy-Goursat for parallelograms, (3) bare pole integral over parallelogram = 2πi. ~400 lines.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [B c8p8] "Cauchy ... #6491 proved it in one pass"
