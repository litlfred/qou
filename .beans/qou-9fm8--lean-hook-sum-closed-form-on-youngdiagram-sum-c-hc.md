---
# qou-9fm8
title: 'Lean: hook-sum closed form on YoungDiagram — Sum_c h(c) = Sum_i C(lambda_i,2) + Sum_j C(lambda-conj_j,2) + n'
status: completed
type: task
priority: normal
created_at: 2026-08-30T07:15:16Z
updated_at: 2026-08-30T07:16:04Z
---

`QOU/BraidKnot/HookSumClosedForm.lean` — the linear hook sum in closed form on
Mathlib's `YoungDiagram`, over the integers, on `PieceAGeneral`'s own
`armZ`/`legZ`/`hookZ`.

Sorry-free; `#print axioms` on every theorem gives exactly
`[propext, Classical.choice, Quot.sound]`. Verified by direct `lean` invocation
(v4.24.0) against the restored Mathlib olean cache — no `lake build`, which
would evict it (trace coverage is 0%).

Theorems:
- `sum_cells_eq_sum_rows` — cells-to-rows decomposition, for any `N` with
  `mu.colLen 0 <= N`. Built on `Finset.sum_fiberwise_of_maps_to` plus
  `YoungDiagram.row_eq_prod`; Mathlib has no `cells_eq_biUnion_rows`.
- `two_mul_sum_snd` / `two_mul_sum_fst` — the two coordinate sums; the second
  by transpose through `PieceA.sum_swap_transpose`.
- `sum_hookZ_eq` — hook sum = the two coordinate sums + n, from
  `PieceA.sum_armZ_generic` / `sum_legZ_generic` at F = id.
- `two_mul_sum_hookZ` — the binomial form, doubled to stay in the integers.
- `two_mul_sum_hookZ_eq_sum_sq` — `2 Sum_h = p2(lambda) + p2(lambda-conj)`, the
  conjugation-symmetric form. This is the input to the A1 argument (parent
  qou-470y): free cumulants have parity `R_k(conj) = (-1)^k R_k`, so a
  conjugation-invariant element of Lambda-star carries no odd-degree part,
  while Sum_h grows like n^(3/2).
- `sum_hookZ_eq_bStat` — the same identity in the `b(conj) + b(lambda) + n`
  shape, stated so it reads term-for-term against the prior art below.

Independently checked numerically: all 271 partitions of n = 1..12, both forms
exact, 0 failures.

PRIOR ART, found during this work and not before it:
`QOU.Common.HookSumComplete.hookSum_eq` already proves this identity,
sorry-free, over a sorted list of naturals with its own shadow
`colLen`/`bStat`/`armPart`/`legPart`/`hookSum` (truncated subtraction) and an
explicit sortedness hypothesis. It is disconnected from `YoungDiagram` and from
the corpus's `hookZ`, so it composes with nothing else in `QOU.BraidKnot`. That
is why this restatement exists, and the module docstring says so. Bridging the
two registers is a separate bean.

Wired into `QOU/BraidKnot.lean` so it is not an import orphan. The three
`QOU.Common.HookSum*` modules remain pre-existing orphans (qou-kljb,
owner-scoped), untouched here.


Parent (the A1 result this feeds): qou-470y — beans refuses a task-to-task
parent link, so it is recorded here rather than in the parent field.
Follow-up: qou-8r18 (bridge the list register to the YoungDiagram register).
