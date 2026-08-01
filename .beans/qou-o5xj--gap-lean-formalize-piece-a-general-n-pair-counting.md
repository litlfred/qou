---
# qou-o5xj
title: 'GAP: Lean-formalize Piece A general-n (pair-counting identity Sal+Sij=D)'
status: todo
type: task
created_at: 2026-08-01T16:58:01Z
updated_at: 2026-08-01T16:58:01Z
---


## Concrete Lean plan (API validated 2026-08-01, PieceAGeneral.lean Stage 1)

Setting: Mathlib `YoungDiagram` (down-closed `Finset (ℕ×ℕ)`). Validated API:
`rowLen`, `colLen`, `mem_iff_lt_rowLen`, `mem_iff_lt_colLen`, `transpose`,
`rowLen_transpose`/`colLen_transpose`, `mem_transpose`, `Finset.sum_range_reflect`,
`Finset.sum_bij'`.

Stage 1 DONE (sorry-free): `armZ/legZ/hookZ/contentZ`, `hookZ_eq`
(`hook = rowLen i + colLen j − i − j − 1`), `armZ_nonneg`, `legZ_nonneg`.

Remaining stages:
1. **Reflection** `Σ_c armZ = Σ_c (c.2:ℤ)` and `Σ_c armZ² = Σ_c (c.2:ℤ)²` via
   `Finset.sum_bij'` with the involution `φ(i,j)=(i, rowLen i−1−j)` on `μ.cells`
   (needs `Nat.cast_sub` from `j < rowLen i`). Legs: apply the same to `μ.transpose`
   and transport by `swap` (`legZ μ c = armZ μ.transpose c.swap`).
2. **Separable reduction** (pure `ring` once the reflections give
   `Σa²=Σj², Σl²=Σi², Σa=Σj=A, Σl=Σi=L`): `Σh² − Σc² = n + 2A + 2L + 2Σ(a·l) + 2Σ(i·j)`.
3. **Pair-counting** `Σ_c armZ·legZ = #{(p,q)∈cells² : p.1<q.1 ∧ p.2>q.2}` and
   `Σ_c (c.1)·(c.2) = #{(p,q) : p.1<q.1 ∧ p.2<q.2}` via `Finset.card` bijections
   (arm-cell × leg-cell ↔ UR/LL pair with corner `(p.1,q.2)`; above×left ↔ UL/LR
   pair with corner = the cell). Then `Σal+Σij = D = C(n,2)−A−L` since cell pairs
   split into same-row (A) + same-col (L) + distinct-both (D).
4. Assemble Piece A. Math proof: `docs/audits/2026-08-01-keystone-identity-I-piece-A-general-proof.md`.

Best done with the Lean LSP up (blind lean-direct iteration is ~3 min/compile).
