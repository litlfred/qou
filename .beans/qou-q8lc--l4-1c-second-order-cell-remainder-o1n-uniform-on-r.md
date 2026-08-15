---
# qou-q8lc
title: 'L4-1c: second-order cell remainder O(1/N) uniform on r-compacts away from 5pi/6'
status: completed
type: task
created_at: 2026-08-11T01:06:41Z
updated_at: 2026-08-11T10:45:00Z
---


DONE (part i, the exact half): LogSineSingularPart.lean log_cell_telescope
sorry-free. STRUCTURAL FINDING: splitting the integrand at the singularity
puts ALL singular behaviour in a half that telescopes EXACTLY (evaluated by
L4-1b Stirling); Euler-Maclaurin is NOT needed for L4-1 (audit updated).
Part ii (the smooth C1 Riemann defect for phi = log(2 sin x/x)) split to its
own bean — the one genuinely-new estimate left, whose only hard point is a
Lipschitz bound across phi's removable singularity at 0 (phi' = cot x - 1/x,
each term singular, the difference regular).
