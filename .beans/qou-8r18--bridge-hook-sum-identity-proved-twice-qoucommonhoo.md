---
# qou-8r18
title: 'BRIDGE: hook-sum identity proved twice — QOU.Common.HookSum* (list register) vs QOU.BraidKnot.HookSum (YoungDiagram register)'
status: completed
type: task
priority: normal
created_at: 2026-08-30T07:15:54Z
updated_at: 2026-08-30T08:04:25Z
---

The hook-sum identity is now proved twice in this corpus, in two registers that
do not talk to each other:

1. `QOU.Common.HookSumComplete.hookSum_eq` (179 lines, sorry-free, orphan):
   over a sorted list of naturals, with hand-rolled `colLen` / `bStat` /
   `armPart` / `legPart` / `hookSum`, truncated subtraction, and an explicit
   sortedness hypothesis. Siblings `HookSumGeneral` (the arm half) and
   `HookSumIdentity` (`decide`-checked small shapes) are in the same register.
2. `QOU.BraidKnot.HookSum` (qou-9fm8, sorry-free, wired into the umbrella):
   over Mathlib `YoungDiagram`, in the integers, on `PieceAGeneral`'s
   `armZ`/`legZ`/`hookZ`, no sortedness hypothesis.

Neither is wrong and neither subsumes the other mechanically. `sum_hookZ_eq_bStat`
states (2) in (1)'s `b(conj) + b(lambda) + n` shape so a reader can match them
term for term, but that is a human reading, not a proof.

WHAT A BRIDGE NEEDS
- `mu.rowLens.getD i 0 = mu.rowLen i` and `HookSumComplete.colLen mu.rowLens j =
  mu.colLen j`. `YoungDiagram.rowLens`, `rowLens_sorted`, `pos_of_mem_rowLens`
  and `ofRowLens_to_rowLens_eq_self` all exist and are already used in
  `QOU/MathlibExt/MacdonaldTelescopeGeneralX.lean`.
- The naturals-to-integers cast, which is where the work is: (1) uses truncated
  subtraction cellwise (`l.getD i 0 - 1 - j`), so each cast needs the
  cell-membership bound that makes the truncation inert. `PieceA.armZ_nonneg`
  and `legZ_nonneg` are the corresponding facts on the other side.
- Then `HookSumComplete.hookSum mu.rowLens = (Sum_c hookZ mu c).toNat`, and
  `hookSum_eq` and `sum_hookZ_eq_bStat` become one theorem.

WHY IT IS WORTH DOING: it retires a duplicate rather than leaving two proofs to
drift, and it is the same shape as the migration `QOU.Common` needs generally —
several `Common` modules carry list-based shadow combinatorics predating the
`YoungDiagram` adoption.

NOT IN SCOPE HERE: wiring the three `QOU.Common.HookSum*` modules into an
umbrella. They are pre-existing import orphans and that is owner-scoped
(qou-kljb).


Claimed 2026-08-30 on branch claude/q407-self-assuming-projections-2026-08-21.


## Summary of Changes

`QOU/BraidKnot/HookSumRegisterBridge.lean` — sorry-free, nine theorems, all on
`[propext, Classical.choice, Quot.sound]` only. Verified by direct `lean`
v4.24.0 against the restored Mathlib cache (no `lake build`, which evicts it).

Data bridges: `rowLens_getD` (total, not just in-range — the list statements
index by `getD` over `range l.length` and carry no bound), `colLen_rowLens`,
`rowLens_sum_eq_card`. Hypothesis bridges: `rowLens_sorted'` and
`rowLens_le_rowLen_zero`, both from `YoungDiagram.rowLen_anti` — notably NOT via
`YoungDiagram.rowLens_sorted`, since `rowLen_anti` already has the shape
`hookSum_eq` wants.

`hookSum_rowLens` identifies the two hook sums. `sum_hookZ_eq_bStat_via_list`
re-derives the YoungDiagram closed form FROM `HookSumComplete.hookSum_eq`, and
`sum_hookZ_eq_bStat_via_reflections` states the identical proposition proved the
other way — so the two are demonstrably one theorem, not two that agree.

The work was where the bean predicted: the cast, and specifically that it is
CONDITIONAL. The list side writes an arm as truncated `l.getD i 0 - 1 - j`,
which agrees with `armZ`'s integer subtraction only ON a cell, so the cellwise
step carries `j < rowLen i` and derives `i < colLen j` from it before `omega`
may equate them. Off a cell the registers genuinely disagree.

One thing the bean did not anticipate: `ring` cannot finish the last step.
`colSum` is `Σ_j (colLen j) * j` and the YoungDiagram form is `Σ_j j * colLen j`;
`ring` cannot reach inside a binder, so it sees two unrelated atoms. An explicit
`Finset.sum_congr` with `mul_comm` closes it by `rfl`.

Cross-checked numerically: the List-register definitions replicated verbatim in
Python and compared against the YoungDiagram register over all 271 partitions of
n <= 12 — the bridge identity, `hookSum_eq` itself, both b-statistics, and
`length rowLens = colLen 0`. 0 failures.

Side effect worth knowing: `QOU.Common.HookSumComplete` is no longer an import
orphan, because the bridge imports it — so it is now visible to every tool that
walks imports. `HookSumGeneral` and `HookSumIdentity` remain orphans and were
not touched; wiring those is still owner-scoped (qou-kljb).

NOT done, and out of scope as filed: retiring either proof. Both stand; the
point was to make the duplication checked rather than latent.
