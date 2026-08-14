---
# qou-w4gn
title: 'GAP: eps_m per-ELEMENT representative at m>=3 — residue-level lattice model shown insufficient (Addendum 25)'
status: todo
type: task
created_at: 2026-08-11T11:21:33Z
updated_at: 2026-08-11T11:21:33Z
---


## Single-relation route: RULED OUT (2026-08-11, idle-window probe)

The cheapest route to a per-element representative is one five-term
relation seeded at the offending symbol. xi's symbols are the specific
elements z_1 (mult 2) and z_2 (mult 1), so per-element divisibility
m | n_j e(w_j) fails only where noted:

| m | z_2 needs fixing (m does not divide e(z_2)) | z_1 needs fixing (m does not divide 2 e(z_1)) |
|---|---|---|
| 2 | no | no |
| 3 | yes | no |
| 4, 8, 12, 24 | yes | yes |
| 6 | yes | no |

Fixing z_2 by subtracting a five-term relation seeded at (z_2, y)
cancels z_2 but introduces its other four arguments at multiplicity -1,
each then needing m | e(w). Swept over every admissible y in F_25
(alpha basis, alphabar^2 = 4 alphabar + 3):

    ZERO candidates at every m | 24.

So no single relation clears the obstruction. This does NOT close the
bean: multi-relation combinations (and relations seeded at other
positions, or acting on z_1 as well) are untested, and the search space
of coefficient vectors over the 506 relations is large. The negative is
scope-(a): one route, exhaustively excluded.

Convention note: this run measures e(z_1) = 15, e(z_2) = 22 against an
alpha-basis generator, where the merged probes report 9 and 2 against a
different generator. The dlogs differ by a unit rescaling; every
divisibility verdict agrees, as it must.
