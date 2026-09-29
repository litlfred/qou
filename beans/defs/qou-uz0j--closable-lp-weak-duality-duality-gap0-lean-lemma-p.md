---
# qou-uz0j
title: 'CLOSABLE: LP weak duality + duality_gap>=0 Lean lemma (proved backing for every LP/SDP-dual witness)'
status: completed
type: task
priority: high
created_at: 2026-08-15T15:57:50Z
updated_at: 2026-08-15T20:45:18Z
parent: qou-5lm6
---

Rivin Thm 3.2 weak half: for primal-feasible x (Ax=a,x>=0) and dual-feasible lambda (lambda^T A <= c), c^T x >= a^T lambda; hence primal_obj>=dual_obj, duality_gap = primal_obj-dual_obj >= 0. Short proof over LinearOrderedField, NO geometry. Gives a PROVED backing to the ubiquitous AGENTS.md LP/SDP-dual witness assertion (lp_dual_solver.py, y0*/y*/duality_gap). Highest cross-cutting leverage. formalize-first, sorry-free target.
