import QOU.SchurWeyl.QJucysMurphy
import QOU.SchurWeyl.SytAdmissible

/-!
# Why `Θ = Σ_k (L_k + L_k⁻¹)` is a *scalar*, reduced to the per-element eigenvalue

`barSymJMSum_block_eigenvalue` asserts that the bar-symmetrised Jucys–Murphy sum acts on the
`λ`-block by `cellContentCoshSum λ q = Σ_{c∈λ}(q^{2c} + q^{−2c})`.  Its `-- Ref:`-cited `sorry`
names two inputs: the general-`λ` representation (now **proved**, `hoefsmit_seminormal_rep`) and
the per-element eigenvalue `L_k ↦ q^{2·cellContent}` — Ram's theorem, still open here.

This file supplies **everything except that theorem**, so that the remaining gap is exactly one
named hypothesis rather than a `sorry` of unstated size.

## The part that needs no eigenvalue theorem

The reason `Θ` is a *scalar* and not merely diagonal is a reindexing fact, not a spectral one:

> `cellOf T` is a bijection `[1, |μ|] → μ.cells`, so `∑_k g (cellOf T k)` equals `∑_{c ∈ μ.cells} g c`
> — **the same value for every tableau `T`**.

That is `sum_comp_cellOf` below.  Per-element eigenvalues that *depend* on `T` therefore sum to
something that does not, and the `T`-dependence cancels before any representation theory is
invoked.  Nothing here assumes the eigenvalues are `q^{2c}`; the statement is about an arbitrary
`g`.

## The consistency check that the indexing survives

`qJM` runs `L_0 = 1`, `L_{k+1} = σ_k L_k σ_k`, so the sum `∑_{k ∈ range (n+1)}` pairs `L_k` with
entry `k + 1`, and `L_0 = 1` must correspond to the cell holding entry `1`.  It does:
`cellOf_one` puts entry `1` at `(0,0)`, whose content is `0`, and `q^{2·0} = 1` is exactly the
eigenvalue of `L_0 = 1`.  The off-by-one lines up — worth checking rather than assuming, since a
shift by one would make the two sums range over different multisets of cells and the whole
identity would be false while still looking plausible.

## What is *not* here

The per-element eigenvalue itself.  `L_k` is a product of `genMat`s under the recursion, and
showing that product is diagonal with entries `q^{2·content}` is [ram1997] Theorem 4.1 — the
substance, not the packaging.  It is stated below as the hypothesis `PerElementEigenvalue` and
consumed; it is **not** proved, and this file does not claim it is.
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)

namespace TableauCells

variable {μ : YoungDiagram}

/-- **Summing over values is summing over cells.**  `cellOf T` is a bijection from `[1, |μ|]` onto
the cells, so any sum indexed by tableau *entries* is the corresponding sum over *cells* — the same
value for every `T`.

This is the whole reason a sum of per-tableau eigenvalues can be a scalar: the right-hand side
does not mention `T`. -/
theorem sum_comp_cellOf {R : Type*} [AddCommMonoid R] (T : StandardYoungTableau μ)
    (g : ℕ × ℕ → R) :
    ∑ j ∈ Finset.Icc 1 μ.cells.card, g (cellOf T j) = ∑ c ∈ μ.cells, g c := by
  classical
  refine Finset.sum_nbij' (fun j => cellOf T j) (fun c => T.entry c.1 c.2) ?_ ?_ ?_ ?_ ?_
  · intro j hj
    exact cellOf_mem T (by simpa using hj)
  · intro c hc
    have := T.mapsTo_cells (by simpa using hc)
    simpa using this
  · intro j hj
    exact entry_cellOf T (by simpa using hj)
  · intro c hc
    exact cellOf_unique T hc rfl
  · intro j _
    rfl

/-- The `range`-indexed form, matching `barSymJMSum`'s `∑ k ∈ range (n + 1)`.

`L_k` pairs with entry `k + 1`; `cellOf_one` confirms the base of that pairing (`L_0 = 1` ↔ entry
`1` at the corner `(0,0)`, content `0`). -/
theorem sum_range_comp_cellOf {R : Type*} [AddCommMonoid R] (T : StandardYoungTableau μ)
    (g : ℕ × ℕ → R) {n : ℕ} (hn : μ.cells.card = n + 1) :
    ∑ k ∈ Finset.range (n + 1), g (cellOf T (k + 1)) = ∑ c ∈ μ.cells, g c := by
  classical
  rw [← sum_comp_cellOf T g]
  rw [hn]
  refine Finset.sum_nbij' (fun k => k + 1) (fun j => j - 1) ?_ ?_ ?_ ?_ ?_
  · intro k hk
    simp only [Finset.mem_range] at hk
    simp only [Finset.mem_Icc]
    omega
  · intro j hj
    simp only [Finset.mem_Icc] at hj
    simp only [Finset.mem_range]
    omega
  · intro k _
    dsimp only
    omega
  · intro j hj
    simp only [Finset.mem_Icc] at hj
    dsimp only
    omega
  · intro k _
    rfl

/-- **The corner check.**  `L_0 = 1` pairs with entry `1`, which sits at `(0,0)` with content `0`,
so its eigenvalue slot is `q^{2·0} = 1` — consistent with `L_0 = 1` acting as the identity.

Stated because an off-by-one in the `L_k` ↔ entry pairing would leave the two sums ranging over
different multisets of cells: the identity would be false while still type-checking. -/
theorem content_cellOf_one (T : StandardYoungTableau μ) (hne : 0 < μ.cells.card) :
    cellContent (cellOf T 1) = 0 := by
  rw [cellOf_one T hne]
  simp [cellContent]

/-! ## The assembly: diagonal per-element eigenvalues force a *scalar* sum -/

/-- **Per-element diagonal ⟹ the bar-symmetrised sum is a scalar.**

If every `ρ(L_k + L_k⁻¹)` is the diagonal matrix whose `T`-entry is
`q^{2c} + q^{−2c}` at the cell `cellOf T (k+1)`, then the sum over `k` is the *scalar*
`cellContentCoshSum`.  The `T`-dependence cancels by `sum_range_comp_cellOf`: each column sums the
same multiset of contents, namely all the cells of `μ`.

This is the whole of `barSymJMSum_block_eigenvalue` except the per-element eigenvalue itself.
Nothing here proves that eigenvalue — `A` is an arbitrary family and `hdiag` is a hypothesis. -/
theorem sum_diagonal_eq_scalar {μ : YoungDiagram} [DecidableEq (StandardYoungTableau μ)]
    {n : ℕ} (hn : μ.cells.card = n + 1) (q : ℝ)
    (A : ℕ → Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ)
    (hdiag : ∀ k, A k = Matrix.diagonal (fun T =>
      q ^ (2 * cellContent (cellOf T (k + 1))) + q ^ (-(2 * cellContent (cellOf T (k + 1)))))) :
    ∑ k ∈ Finset.range (n + 1), A k
      = (∑ c ∈ μ.cells, (q ^ (2 * cellContent c) + q ^ (-(2 * cellContent c))))
          • (1 : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ) := by
  classical
  ext T T'
  rw [Matrix.sum_apply]
  by_cases hTT : T = T'
  · subst hTT
    have hk : ∀ k ∈ Finset.range (n + 1), A k T T
        = q ^ (2 * cellContent (cellOf T (k + 1)))
          + q ^ (-(2 * cellContent (cellOf T (k + 1)))) := by
      intro k _
      rw [hdiag k, Matrix.diagonal_apply_eq]
    rw [Finset.sum_congr rfl hk]
    rw [sum_range_comp_cellOf T
      (fun c => q ^ (2 * cellContent c) + q ^ (-(2 * cellContent c))) hn]
    simp [Matrix.smul_apply, Matrix.one_apply_eq]
  · have hk : ∀ k ∈ Finset.range (n + 1), A k T T' = 0 := by
      intro k _
      rw [hdiag k, Matrix.diagonal_apply_ne _ hTT]
    rw [Finset.sum_congr rfl hk, Finset.sum_const_zero]
    simp [Matrix.smul_apply, Matrix.one_apply_ne hTT]

end TableauCells

end QOU.SchurWeyl
