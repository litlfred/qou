---
# qou-7xt3
title: 'Orbit-size classification: the 3-cell configuration to size map (1/2/3/6) with the size-2 hook'
status: todo
type: task
created_at: 2026-08-15T02:59:25Z
updated_at: 2026-08-15T02:59:25Z
---


## The map (exact enumeration, 2026-08-15)

Orbit size = number of standard fillings of the 3-cell configuration holding k, k+1, k+2.
Determined by the comparability relation among the three cells (a <= b iff same row with
a left of b, or same column with a above b):

  total order on all 3 (a chain)        -> 1   e.g. 3-in-a-row, 3-in-a-column,
                                                (0,0)(0,1)(1,1)
  exactly one INCOMPARABLE pair (hook)  -> 2   e.g. (0,0)(0,1)(1,0)
  exactly one COMPARABLE pair           -> 3   e.g. any two sharing a row/column
                                                (adjacent or not) + one unrelated
  antichain (no comparable pair)        -> 6

So the orbit size is 6/|number of linear extensions|... precisely: it IS the number of
linear extensions of the induced poset on the three cells.

USE: this is the classification step (ii) needs. The identities are already proved for
every size — 1 (scalars), 2 (seminormalBlock), 3 (Orbit3Braid), 6 (Orbit6Braid).

DESIGN NOTE, and the real blocker: there is NO Lean object for "the orbit" yet. The
s_k-action (swapTableau) is partial — defined only under SwapAdmissible — so the orbit is
a connected component under partial moves, not a group orbit. Options before writing the
classification:
  (a) define the orbit as a Finset (SYT lam) closed under the available moves;
  (b) index by the linear extensions of the 3-cell poset and build the correspondence
      directly, skipping a general orbit notion;
  (c) sidestep orbits: define rho on ALL of SYT lam by the trichotomy (axialDist_trichotomy
      already gives the per-generator case split) and prove the relations globally, with the
      orbit-local identities used only as the algebraic content.

(c) is probably the shortest route to discharging hoefsmit_seminormal_rep, since the
per-orbit basis correspondence — the thing that makes Orbit3Braid/Orbit6Braid's explicit
index orderings usable — is exactly what (a) and (b) force one to build.
