---
# qou-xbl8
title: 'GAP: derive the tail-lemma per-row bracket bound in Lean (infinite gap-2 lattice cancellation)'
status: todo
type: task
priority: normal
created_at: 2026-10-11T08:20:00Z
updated_at: 2026-10-11T08:20:00Z
parent: qou-3e6w
---

`QOU/MassTheory/XbotBottomEdgeLemmas.lean` (PR #7715) formalises sorry-free the shift identity
(`frameObjective_shift`), the wall inequality (`frameObjective_bottom_raise_lt`, `frame_succ_le`),
and the structural half of the tail lemma: a move's gain is exactly `Σ_{j∈H} rowGain`
(`pairObjective_move_gain`), and if each high row's `rowGain ≤ β < 0` then the high part never
helps (`tail_never_helps`, `tail_move_lt_zero`).

**Open:** the hypothesis `hrow` itself — that every row at or above `N` contributes at most
`eps(b_N + 1) + cbar_N − (ln q0)/2`. Deriving it needs (i) the bi-infinite gap-2 lattice
cancellation (a convergent infinite sum; only the finite antisymmetric piece
`antisymm_double_sum_eq_zero` is in Lean), (ii) the comparison of this frame's rows below `N`
with that lattice, and (iii) monotonicity in `j` making row `N` the worst case. The sign
`bracket < 0` is still the numeric check M7 of `rev_e_infinity_xbot_lnatural_probe.py`, and
enters Lean only as the hypothesis `β < 0`. The L♮ optimality criterion (Murota 2003, Ch. 7)
is cited, not formalised.
