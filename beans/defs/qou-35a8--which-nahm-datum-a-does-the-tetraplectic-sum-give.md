---
# qou-35a8
title: Which Nahm datum A does the tetraplectic sum give beyond 4_1?
status: todo
type: task
created_at: 2026-11-27T17:26:40Z
updated_at: 2026-11-27T17:26:40Z
---

Research path, opened 2026-11-27 (thread 'Reeb flow and tetraplectic structure', PR #9496 merged).

PR #9496 (QOU/MassTheory/NahmBlochBridge.lean, sorry-free) proves: for a symmetric integer matrix A, any solution of 1 - z_i = prod_j z_j^{A_ij} gives sum [z_i] in the Bloch group B(F). For the figure-eight knot 4_1 the datum is A = (-1) (Habiro q->1 ratio, habiro41_nahm_iff), and fig8Class is the Nahm class of A = -I.

OPEN: which Nahm datum A (if any) the tetraplectic sinh-lattice state sum gives for knots beyond 4_1. It must be DERIVED from the state sum's q->1 saddle equations, not chosen to match a volume (no-fit rule).

Next honest step: write the q->1 stationary-phase equations of the tetraplectic sum for a second hyperbolic knot (5_2 is the natural test, 3 tetrahedra) and read A off them; check A is symmetric, so nahmClass_mem_blochGroup applies.

Conjecture-tracking bean: do not close until the mathematics closes (AGENTS.md rule 13a).
