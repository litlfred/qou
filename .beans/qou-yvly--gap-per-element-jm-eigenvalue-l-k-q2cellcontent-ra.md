---
# qou-yvly
title: 'GAP: per-element JM eigenvalue L_k -> q^{2*cellContent} (Ram Thm 4.1) — the last input to barSymJMSum_block_eigenvalue'
status: todo
type: task
priority: normal
created_at: 2026-08-19T08:13:31Z
updated_at: 2026-08-19T12:33:45Z
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


## The validation RAN, and it PASSES — 2026-08-19

Done, and proved in Lean rather than checked by hand: `JMBlockEigenvalue.lean` §Rep21Eigenvalue,
four theorems, sorry-free and axiom-clean.

    S0_sq_eq_diag        : S0² = diag(q², q^{-2})
    S1_S0sq_S1_eq_diag   : S1 · S0² · S1 = diag(q^{-2}, q²)          ← the informative one
    seminormalRep21_qJM_one : ρ(L_1) = diag(q², q^{-2})
    seminormalRep21_qJM_two : ρ(L_2) = diag(q^{-2}, q²)

**Both conventions are confirmed.** The prediction `L_k ↦ diagonal (q^{2·cellContent(cellOf T (k+1))})`
matches exactly on λ = (2,1):

| tableau | entry 2 cell / content | entry 3 cell / content |
|---|---|---|
| `[[1,2],[3]]` | (0,1), +1 → q² | (1,0), −1 → q^{-2} |
| `[[1,3],[2]]` | (1,0), −1 → q^{-2} | (0,1), +1 → q² |

So the `L_k` ↔ entry-`(k+1)` offset is right, and `cellContent = col − row` has the right sign.
The general target is NOT mis-stated — that was the thing this check existed to rule out.

### The mechanism, which is the part worth carrying into the general proof

`L_2` is the informative case: unlike `S0²` it is a genuine 2×2 product whose off-diagonal entries
must **cancel**, and they do, through a single identity

    a·q² + d·q^{-2} = 0,     a = −1/(q³+q)  (S1's top-left),  d = q³/(q²+1)  (S1's bottom-right)

i.e. the two diagonal entries of the seminormal block, weighted by the two contents, sum to zero.
That is the axial-distance relation doing exactly the work a general induction would need it to do
at each size-2 orbit: `M · D · M` stays diagonal precisely because the block's parameters are tied
to the contents this way.

**Suggested next step**, now that the target is validated: try to state and prove that cancellation
identity for the general `seminormalBlock q a` at a general axial distance — i.e. the size-2 orbit
step of the induction — rather than starting from the full theorem. `seminormalBlock` and
`seminormalBlock_quadratic` already exist and are generic over the field.

### Still NOT claimed

One shape, with one size-2 orbit. It does not prove the general theorem, and `d_λ = 2` is the
smallest case where the off-diagonal is non-trivial at all — a λ with several orbits, or orbits of
size 6, is not exercised. Ram Thm 4.1 remains open.


## 2026-08-19 — the size-2 orbit step is now PROVED (do not redo)

`JMBlockEigenvalue.lean` §OrbitStep, all sorry-free and axiom-clean
(propext / Classical.choice / Quot.sound only):

* `seminormalBlock_conj_diag_swap` (hq : q ≠ 0) (hδ : q^(2δ) ≠ 1) :
    seminormalBlock q (a δ) * diag(x, x·q^(2δ)) * seminormalBlock q (a δ)
      = diag(x·q^(2δ), x)
  Read with x = q^{2c} and δ = axialDistance, this IS σ_k L_k σ_k = L_{k+1}
  on a two-element orbit, with the two contents exchanged.
* `block_conj_diag` — the matrix half. Both off-diagonal entries of
  M·diag(x,y)·M carry the SAME factor a·x + d·y (d = (q−q⁻¹) − a), so a
  single scalar condition kills both. That is why one hypothesis suffices.
* `seminormalParam_weighted_sum_zero` — the scalar half. a(δ)·x +
  a(−δ)·(x·q^{2δ}) = 0. This is the only place the axial distance enters.

The bridge between the two halves is `seminormalParam_add_neg`, already
sorry-free: it identifies the block's lower-right entry (q−q⁻¹) − a(δ)
with a(−δ).

### Correcting my own earlier caveat on this bean

I wrote that the 2×2 case "is NOT known to be as column-local as
genMat_quadratic was — that is the thing that would make it tractable,
and I have not established it." That was too pessimistic. The step is
column-local in the relevant sense: the whole 2×2 computation reduces to
ONE scalar identity in q and δ, with no tableau data beyond the axial
distance. Cost was a few hours, not a genMat_braid-scale effort.

### What is actually left for Ram Thm 4.1

Orbit BOOKKEEPING, not the per-orbit algebra:

1. orbits of size > 2 under s_k (the 1×1 fixed-point case is trivial; the
   claim that every s_k-orbit on SYT(μ) has size ≤ 2 needs stating), and
2. assembly of the per-generator steps along a reduced word, i.e. the
   induction on k in L_{k+1} = σ_k L_k σ_k with genMat block-diagonal
   over orbits.

Neither needs new algebraic identities as far as I can see — but I have
not tried them, so treat that as a guess, not a result.


### Correction to the item above — orbit size ≤ 2 is NOT part of the gap

I listed "the claim that every s_k-orbit on SYT(μ) has size ≤ 2 needs
stating" as remaining work. Wrong: `TableauCells.swapTableau_involutive`
already proves it (merged well before this branch), and the size-1 case is
`SeminormalRep.genMat_of_not_admissible`. Both were in the corpus. I wrote
the item before grepping, which is the failure mode this bean's own notes
warn about.

Also landed: `genMat_submatrix_orbit` — restricted to the two rows and
columns {T, s_k·T}, `genMat` IS `seminormalBlock q (a δ)`. Hypothesis
`axialDist T k < 0` fixes the orientation, which is forced: genMat's two
off-diagonals are `offDiag q δ` and `offDiag q (−δ)` and those are
asymmetric (one is 1, the other 1 + a(δ)a(−δ)); only one ordering matches
seminormalBlock. The other orientation is the same lemma applied to s_k·T.
This makes seminormalBlock_conj_diag_swap a statement about the actual
representation rather than an abstract 2×2 identity.

So the remaining gap is exactly ONE thing: the induction on k in
L_{k+1} = σ_k L_k σ_k, decomposing the product orbit by orbit.
