---
# qou-yvly
title: 'GAP: per-element JM eigenvalue L_k -> q^{2*cellContent} (Ram Thm 4.1) — the last input to barSymJMSum_block_eigenvalue'
status: todo
type: task
priority: normal
created_at: 2026-08-19T08:13:31Z
updated_at: 2026-08-19T08:14:11Z
---

## Scope, after the 2026-08-19 narrowing

`barSymJMSum_block_eigenvalue` (`QJucysMurphy.lean`) is the only remaining `sorry` in the
SchurWeyl general-λ cone. Its GAP note used to name **two** inputs; one has landed and the
scaffolding around the other is now proved, so the gap is exactly ONE statement:

    ρ(L_k + L_k⁻¹) = diagonal (fun T => q^{2c} + q^{-2c})   at   c = cellContent (cellOf T (k+1))

That is [ram1997] Theorem 4.1.

### Discharged around it (do NOT redo these)

* `hoefsmit_seminormal_rep` — PROVED, merged 45817bf516 (bean qou-im9l). No longer an input.
* the scalar's value — `cellContentCoshSum` + `cellContentCoshSum_eq_bracket`, already sorry-free.
* **diagonal ⟹ scalar** — `TableauCells.sum_diagonal_eq_scalar` (`JMBlockEigenvalue.lean`,
  sorry-free, axiom-clean). This is the step that makes the sum a scalar rather than merely
  diagonal, and it assumes NOTHING about the eigenvalue being `q^{2c}`: it holds for an arbitrary
  per-cell function, because `cellOf T` is a bijection `[1,|μ|] → cells`, so every column sums the
  same multiset of contents and the T-dependence cancels (`sum_comp_cellOf`).
* the index alignment `L_0 = 1` ↔ entry `1` at `(0,0)`, content `0` — `content_cellOf_one`.
  Checked rather than assumed: an off-by-one in the `L_k` ↔ entry pairing would range the two sums
  over different cell multisets, and the identity would be false while still type-checking.

### What remains, stated honestly

`L_k` is a product of `genMat`s under `L_{k+1} = σ_k L_k σ_k`. Showing that product is diagonal
with entries `q^{2·content}` is the substance of Ram's theorem, not packaging around it. The
plausible route is induction on `k`: `genMat` is block-diagonal over the `s_k`-orbits (1×1 and
2×2), so `M · D · M` is a per-orbit computation — the 2×2 case is where the content/axial-distance
relation has to do real work, and it is NOT known here to be as column-local as
`genMat_quadratic` was.

**NOT claimed: that this is close.** It is a research-grade item, comparable to `genMat_braid`,
which took a multi-session effort.
