---
# qou-ev3a
title: 'D2: converse at v=n-1 — each of the three shapes achieves hookLen = n-1 at its stated cell'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T00:45:18Z
updated_at: 2026-11-16T18:02:18Z
parent: qou-wp3h
---

## Progress Update (2026-11-16 — Owner Ruling `Q-WP3H-1 = 1`, PR #8143)

- Formalized the reverse direction (converse) of the D2 depth-1 hook-length characterization at $v = n - 1$ in `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/HookArmLeg.lean` (`0` `sorry`, PR `litlfred/qou#8143`, commit `7df80d1c2e228518b2ca15ec1d314be46da8e524`):
  1. **Single row `[n]` ($n \ge 2$) at cell `(0, 1)`:** `sorted_singleRow`, `zero_one_mem_cells_singleRow`, `hookLen_singleRow_zero_one`, `hookLen_singleRow_zero_one_add_one` (`hookLen [n] 0 1 + 1 = [n].sum`).
  2. **Single column `List.replicate n 1` ($n \ge 2$) at cell `(1, 0)`:** `countP_pos_replicate_one`, `sorted_singleCol`, `one_zero_mem_cells_singleCol`, `hookLen_singleCol_one_zero`, `hookLen_singleCol_one_zero_add_one` (`hookLen (List.replicate n 1) 1 0 + 1 = (List.replicate n 1).sum`).
  3. **Two-corner shape `a :: 2 :: List.replicate c 1` ($a \ge 2$, size $n = a + c + 2$) at corner `(0, 0)`:** `sorted_twoCorner`, `sum_twoCorner`, `zero_zero_mem_cells_twoCorner`, `hookLen_twoCorner_zero_zero`, `hookLen_twoCorner_zero_zero_eq_sum_sub_one`, `hookLen_twoCorner_zero_zero_add_one` (`hookLen (a :: 2 :: List.replicate c 1) 0 0 + 1 = (a :: 2 :: List.replicate c 1).sum`).
  4. **Bundled converse theorem:** `depth1_three_shapes_achieve_hookLen_eq_sum_sub_one`.
- Kept at `status: in-progress` pending PR #8143 merge and owner verification.
