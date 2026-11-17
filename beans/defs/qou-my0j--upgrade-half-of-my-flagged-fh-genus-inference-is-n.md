---
# qou-my0j
title: 'UPGRADE: half of my flagged FH genus inference is now proved. em_linking_fh_link_bound_correction flagged the WHOLE step ''mu-bar_123 != 0 obstructs a genus-0 disk => genus >= 1 => ac >= 1'' as my inference. Main''s MilnorMagnusCoefficient.lean now DERIVES mu-bar(12..A) = +/-1 != 0 sorry-free via faithful nilpotent Magnus realization. So the non-vanishing is proved; the remaining gap is the single implication ''mu-bar != 0 => genus >= 1 in the complement''. Update the witness to cite the Lean fact and narrow the flag.'
status: in-progress
pr: 8248
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T15:04:34Z
updated_at: 2026-11-17T07:18:00Z
parent: qou-5vkl
---

## Progress (2026-11-17, PR #8248)

- [x] Update `computations/em_linking_fh_link_bound_correction.py` and its witness to cite `QOU/MassTheory/MilnorMagnusCoefficient.lean` (`milnorMagnusCoeff_eq`, `milnorMagnusCoeff_ne_zero`) for $\bar{\mu}(12\dots A) = \pm 1 \neq 0$ and narrow the unformalised inference flag to $\bar{\mu} \neq 0 \Rightarrow \text{genus} \ge 1$ in the complement (PR #8248, Commit 1 `d3dcd4c4757a988299ad0246ed502bd2358a90e4`, Commit 2 `b4185f1dac70a76b08299e291f3137fb9b60fe3c`).
- [ ] Merge PR #8248 (`claude/round53-trd0-9nnz-fixes`, HEAD `b4185f1dac70a76b08299e291f3137fb9b60fe3c`)
