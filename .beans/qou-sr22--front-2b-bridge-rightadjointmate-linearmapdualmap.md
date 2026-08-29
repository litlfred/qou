---
# qou-sr22
title: 'Front 2b: bridge rightAdjointMate = LinearMap.dualMap in FGModuleCat'
status: scrapped
type: task
priority: normal
created_at: 2026-08-26T16:22:42Z
updated_at: 2026-08-26T16:38:08Z
---

SCRAPPED for the same reason as qou-gsdb: the instance it was a step toward landed
via qou-knsx, and this bridge is not needed for it.

Still a genuine Mathlib gap: (rightAdjointMate f).hom = LinearMap.dualMap f.hom is
nowhere in Algebra/Category/FGModuleCat/. The statement typechecks (the carriers
unify -- Vdual.obj is defeq to Module.Dual K V) and simp [rightAdjointMate] reduces
it to the five-step mate composite before stalling on qou-gsdb's wall.
