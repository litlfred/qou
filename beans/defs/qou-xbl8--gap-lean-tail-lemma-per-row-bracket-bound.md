---
# qou-xbl8
title: 'GAP: derive the tail-lemma per-row bracket bound in Lean (infinite gap-2 lattice cancellation)'
status: in-progress
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

## Round 47 Implementation (PR #8153, `status: in-progress`)

- **Lean formalization (`folio/quantum-observable-universe/lean/QOU/MassTheory/XbotBottomEdgeLemmas.lean`, wired into `QOU.lean`, `0` `sorry`)**:
  - **(i) Gap-2 lattice cancellation**: `latticeKernel`, `latticeKernel_antisymm`, `latticeKernel_sum_self_eq_zero`, `latticeKernel_sum_sdiff_eq`, `symmetric_gap2_lattice_sum_eq_zero`, and `matched_lower_upper_sum_nonpos` formalize the signed lattice kernel cancellation and matched lower/upper gap-2 domination.
  - **(ii) Frame comparison below `N`**: `pminus`, `pplus`, `crossChange_framePsi_of_lt`, `crossChange_framePsi_of_gt`, `crossChange_moveBy_le_pminus`, `activeLowerRows`, `cbarAt`, `rowBracket`, `activeCross_le_cbarAt`, and `rowGain_le_rowBracket` prove `rowGain j ≤ rowBracket eps pe w c N j` at any zero-padded tail row `j ≥ N ≥ pe`.
  - **(iii) Monotonicity in `j ≥ N` and discharging `hrow`**: `rowBase_of_ge`, `rowBase_mono`, `rowBase_strictMono_of_ge`, `cbarAt_antitone`, `rowBracket_antitone`, `rowGain_le_rowBracket_N`, `frame_tail_never_helps`, and `frame_tail_move_lt_zero` prove that row `N` is the worst case (`rowBracket eps pe w c N j ≤ rowBracket eps pe w c N N`) and discharge `hrow` in `tail_never_helps` / `tail_move_lt_zero`.
- **L♮ optimality criterion**: proved in `QOU/BraidKnot/LNaturalOptimality.lean` (`global_of_local_boxDiffDomain`, PR #8044, bean `qou-r9a6`).
- **PR**: https://github.com/litlfred/qou/pull/8153 (`95e28f261d9c08b118bd02c63a82c44dafe6174c`).
