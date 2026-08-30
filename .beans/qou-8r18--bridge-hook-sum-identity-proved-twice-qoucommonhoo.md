---
# qou-8r18
title: 'BRIDGE: hook-sum identity proved twice — QOU.Common.HookSum* (list register) vs QOU.BraidKnot.HookSum (YoungDiagram register)'
status: todo
type: task
created_at: 2026-08-30T07:15:54Z
updated_at: 2026-08-30T07:15:54Z
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
