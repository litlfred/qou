---
# qou-yvly
title: 'GAP: per-element JM eigenvalue L_k -> q^{2*cellContent} (Ram Thm 4.1) — the last input to barSymJMSum_block_eigenvalue'
status: todo
type: task
priority: normal
created_at: 2026-08-19T08:13:31Z
updated_at: 2026-08-19T08:16:49Z
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


## Do this FIRST, before investing sessions in the general proof

**Validate the target statement on the concrete (2,1) case.** `seminormalRep21` (`HoefsmitRep.lean`,
λ = (2,1), N = 3, d_λ = 2) is already sorry-free, and the two SYT of shape (2,1) are
`[[1,2],[3]]` and `[[1,3],[2]]`. Compute `ρ(L_0)`, `ρ(L_1)`, `ρ(L_2)` there and check against

    ρ(L_k) = diagonal (fun T => q^{2·cellContent (cellOf T (k+1))})

Expected, if the indexing in the narrowed GAP note is right:
* `L_0 = 1` → both entries `q^0 = 1` (entry 1 at (0,0), content 0).
* `L_1 = σ_0²` → entries at the cell of entry 2: `(0,1)` content **+1** for `[[1,2],[3]]`,
  `(1,0)` content **−1** for `[[1,3],[2]]` — i.e. `diag(q², q^{-2})`.
* `L_2` → cell of entry 3: `(1,0)` content −1, resp. `(0,1)` content +1 — i.e. `diag(q^{-2}, q²)`.

Note `L_1 + L_2` is then `diag(q²+q^{-2}, q^{-2}+q²)` — already scalar, and summing with
`L_0 + L_0⁻¹ = 2` gives `Σ_{c∈λ}(q^{2c}+q^{-2c})` for λ=(2,1) whose contents are {0, +1, −1}. That
is the whole identity in the smallest non-trivial case.

**Why do this first:** it is a few hours at most, and it independently checks the two things most
likely to be silently wrong in the general statement — the `L_k` ↔ entry-`k+1` offset, and the sign
convention on `cellContent = col − row`. If either is off, the general proof would be chasing a
false target. `content_cellOf_one` already pins the base case; this pins the step.

Note `QOU/SchurWeyl/QJucysMurphy.lean` already has `qJM_rhoTriv : ρ_triv(L_k) = q^{2k}` sorry-free —
the **one-dimensional** shape, where the single SYT has entry `k+1` in cell `(0,k)` of content `k`,
so `q^{2·content} = q^{2k}` ✓. That is a second, already-proved consistency point for the same
formula, and it is evidence the exponent convention is right — but it is a 1×1 case, so it does NOT
test the off-diagonal behaviour that makes the general theorem hard.
