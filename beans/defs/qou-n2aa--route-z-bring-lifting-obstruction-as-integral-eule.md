---
# qou-n2aa
title: 'Route Z: Bring lifting obstruction as integral Euler class; derive kappa_0 = e'
status: todo
type: task
priority: high
created_at: 2026-10-12T19:30:20Z
updated_at: 2026-10-12T19:30:20Z
parent: qou-vo9t
---

Route 2 of qou-lx8f (owner, 2026-10-12: pursue in parallel; band deferred).

**Reading.** The obstruction is integral, kappa_0 = e(xi) = -6 in H^2(Sigma_4, Z) = Z. That is nonzero, so persistence is at least consistent.

**Problem.** An integral Euler class obstructs a nowhere-zero section (trivialising an SO(2)-bundle). It is NOT the obstruction to lifting through a central extension by a finite or discrete-abelian kernel. The natural central extension with Z kernel is Z -> R -> U(1) (or the universal cover). Making this a Yekutieli lifting problem needs that extension identified explicitly, and kappa_0 = e derived. Today kappa_0 = e is asserted (thm:qu-to-qou item 2, "via the Gysin sequence") and is a structure field in every Lean file (trace_map, kappa_zero_euler, hattori_stallings).

**Next honest step.** Identify the Z-kernel central extension the tower uses, then derive kappa_0 = e from it. Lean needs Euler classes, which Mathlib lacks; the group-level shadow is T1 with A = Z.
