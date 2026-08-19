import QOU.SchurWeyl.QJucysMurphy
import QOU.SchurWeyl.SytAdmissible
import QOU.SchurWeyl.SeminormalParam

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

## What the `OrbitStep` section *does* prove

The inductive step of that theorem, on an orbit of size `2`:
`seminormalBlock_conj_diag_swap` shows `M · diag(x, x·q^{2δ}) · M = diag(x·q^{2δ}, x)` for
`M = seminormalBlock q (a δ)`.  Read with `x = q^{2c}` and `δ` the axial distance, this is exactly
`σ_k L_k σ_k = L_{k+1}` acting on a two-element orbit, with the two contents exchanged.

It factors into a matrix half and a scalar half, and the split is the point: `block_conj_diag`
shows *both* off-diagonal entries of `M · diag(x,y) · M` carry the same factor `a·x + d·y`, so a
single scalar condition kills both; `seminormalParam_weighted_sum_zero` shows that condition holds
precisely when `y = x·q^{2δ}`.  The axial distance is therefore the *only* place the tableau
combinatorics enters the step — everything else is `2 × 2` matrix algebra over `ℝ`.

What is still missing for Ram Thm 4.1 in general is the orbit *bookkeeping*: orbits of size `> 2`,
and the assembly of the per-generator steps along a reduced word.  The size-`2` step below is the
base case of that induction, not a proof of it.
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

/-! ## The target, verified on the smallest non-trivial shape

Bean `qou-yvly` records that the per-element eigenvalue should be checked on a concrete case before
anyone invests sessions in the general proof, because two conventions could be silently wrong — the
`L_k` ↔ entry-`(k+1)` offset, and the sign of `cellContent = col − row`. This section runs that
check on `λ = (2,1)` and it **passes exactly**, so the general target is the right one.

The two standard tableaux of shape `(2,1)`, in the order `S0 = diag(q, -q⁻¹)` indexes them:

| | entry `2` at | content | entry `3` at | content |
|---|---|---|---|---|
| `[[1,2],[3]]` | `(0,1)` | `+1` | `(1,0)` | `−1` |
| `[[1,3],[2]]` | `(1,0)` | `−1` | `(0,1)` | `+1` |

`L_1 = σ_0²` and `L_2 = σ_1 L_1 σ_1`, so the prediction `L_k ↦ diagonal (q^{2·content})` reads

* `ρ(L_1) = diag(q^{+2}, q^{−2})`,
* `ρ(L_2) = diag(q^{−2}, q^{+2})` — the *same two* values, exchanged, because `σ_1` swaps the
  tableaux.

Both hold. `L_1` is the easy one (`S0` is already diagonal); **`L_2` is the informative one** — it is
a genuine `2×2` product `S1 · S0² · S1` whose off-diagonal entries have to cancel, which is the
first test of anything the `1×1` shapes cannot see. They cancel through the single identity

  `a·q² + d·q^{−2} = 0`,  `a = −1/(q³+q)`, `d = q³/(q²+1)`

relating `S1`'s two diagonal entries to the two contents — the axial-distance relation doing exactly
the work the general induction would need it to do.

**Scope.** This is one shape, and it does not prove the general theorem; `d_λ = 2` with a single
size-`2` orbit is the smallest case where the off-diagonal is even non-trivial. What it does buy is
that the general statement in bean `qou-yvly` is not mis-stated. -/

section Rep21Eigenvalue

variable (q : ℝ)

private theorem sq_add_one_ne' : (q ^ 2 + 1) ≠ 0 := by positivity

private theorem cube_add_ne' (hq : q ≠ 0) : (q ^ 3 + q) ≠ 0 := by
  have h : q ^ 3 + q = q * (q ^ 2 + 1) := by ring
  rw [h]; exact mul_ne_zero hq (sq_add_one_ne' q)

/-- `S0² = diag(q², q^{−2})` — the `L_1` eigenvalues, at the contents `+1` and `−1` of entry `2`. -/
theorem S0_sq_eq_diag : S0 q * S0 q = !![q ^ 2, 0; 0, (q⁻¹) ^ 2] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [S0, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

/-- **`S1 · S0² · S1 = diag(q^{−2}, q²)`** — the `L_2` eigenvalues, at the contents `−1` and `+1`
of entry `3`.

The informative half of the check: unlike `S0²` this is a genuine `2×2` product, and the
off-diagonal entries cancel rather than being zero by construction. -/
theorem S1_S0sq_S1_eq_diag (hq : q ≠ 0) :
    S1 q * (S0 q * S0 q) * S1 q = !![(q⁻¹) ^ 2, 0; 0, q ^ 2] := by
  have h1 : (q ^ 2 + 1) ≠ 0 := sq_add_one_ne' q
  have h2 : (q ^ 3 + q) ≠ 0 := cube_add_ne' q hq
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [S0, S1, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- `ρ_{(2,1)}(L_1) = diag(q², q^{−2})`: the per-element eigenvalue, first instance. -/
theorem seminormalRep21_qJM_one (hq : q ≠ 0) :
    seminormalRep21 q hq (qJM ℝ q q⁻¹ 2 1) = !![q ^ 2, 0; 0, (q⁻¹) ^ 2] := by
  rw [qJM_one ℝ q q⁻¹ 2 (by norm_num), map_mul]
  have h0 : seminormalRep21 q hq (Hecke.σ ℝ q q⁻¹ 2 ⟨0, by norm_num⟩) = S0 q :=
    seminormalRep21_σ0 q hq
  rw [h0, S0_sq_eq_diag]

/-- `ρ_{(2,1)}(L_2) = diag(q^{−2}, q²)`: the per-element eigenvalue on the moved tableaux. -/
theorem seminormalRep21_qJM_two (hq : q ≠ 0) :
    seminormalRep21 q hq (qJM ℝ q q⁻¹ 2 2) = !![(q⁻¹) ^ 2, 0; 0, q ^ 2] := by
  rw [qJM_succ ℝ q q⁻¹ 2 (show 1 < 2 by norm_num), map_mul, map_mul]
  have h1 : seminormalRep21 q hq (Hecke.σ ℝ q q⁻¹ 2 ⟨1, by norm_num⟩) = S1 q :=
    seminormalRep21_σ1 q hq
  rw [h1, qJM_one ℝ q q⁻¹ 2 (by norm_num), map_mul]
  have h0 : seminormalRep21 q hq (Hecke.σ ℝ q q⁻¹ 2 ⟨0, by norm_num⟩) = S0 q :=
    seminormalRep21_σ0 q hq
  rw [h0, S1_S0sq_S1_eq_diag q hq]

end Rep21Eigenvalue

/-! ## The size-`2` orbit step, in general

The `(2,1)` check above works because of one scalar cancellation.  This section isolates that
cancellation for the **generic** `seminormalBlock` at a **general** axial distance, which is the
per-orbit step any induction proving [ram1997] Thm 4.1 has to run.

Two facts, and they separate cleanly:

* `block_conj_diag` is pure matrix algebra.  For any block of `seminormalBlock` shape (top-right
  `1`, trace `q − q⁻¹`, determinant `−1` — so the bottom-left is forced to `a·d + 1`) and any
  diagonal `diag(x, y)`, the conjugate `M · diag(x,y) · M` is diagonal **iff** `a·x + d·y = 0`, and
  then it is `diag(y, x)` — the two values **exchanged**, which is what a generator swapping the two
  tableaux of the orbit must do.  Both off-diagonal entries carry the *same* factor `a·x + d·y`, so
  one condition kills both.  No `q`, no contents, no seminormal parameters enter.

* `seminormalParam_weighted_sum_zero` is where the geometry enters: the condition `a·x + d·y = 0`
  holds for `a = a(δ)`, `d = a(−δ)` exactly when `y = x · q^{2δ}` — i.e. when the two eigenvalues
  differ by the axial distance between the two cells.  In content terms `c₂ = c₁ + δ`, which is what
  `axialDistance` *is*.

Together: at a size-`2` orbit the seminormal generator conjugates `diag(q^{2c₁}, q^{2c₂})` to
`diag(q^{2c₂}, q^{2c₁})` precisely when `δ = c₂ − c₁`.  The `(2,1)` instance above is this with
`δ = ±1`.

**What this is not.**  It is the *orbit step*, not the induction.  A full proof still needs the
size-`1` orbits, the assembly of `genMat` from its blocks, and the induction on `L_{k+1} = σ_k L_k σ_k`
that tracks which cell each entry occupies.  Those are not here. -/

section OrbitStep

open Seminormal

variable (q : ℝ)

/-- **The scalar cancellation.**  `a(δ)·x + a(−δ)·(x·q^{2δ}) = 0`: the seminormal parameters at
`±δ`, weighted by two eigenvalues differing by `q^{2δ}`, cancel.

This is the content half of the orbit step — the place the axial distance enters. -/
theorem seminormalParam_weighted_sum_zero (hq : q ≠ 0) (δ : ℤ) (hδ : q ^ (2 * δ) ≠ 1) (x : ℝ) :
    seminormalParam q δ * x + seminormalParam q (-δ) * (x * q ^ (2 * δ)) = 0 := by
  have h1 : q ^ ((-2 : ℤ) * δ) = (q ^ (2 * δ))⁻¹ := by
    rw [show (-2 : ℤ) * δ = -(2 * δ) by ring, zpow_neg]
  have h2 : q ^ ((-2 : ℤ) * (-δ)) = q ^ (2 * δ) := by congr 1; ring
  rw [seminormalParam, seminormalParam, h1, h2]
  set u := q ^ (2 * δ) with hu
  have hu0 : u ≠ 0 := zpow_ne_zero _ hq
  have hu1 : (1 : ℝ) - u ≠ 0 := sub_ne_zero.mpr (Ne.symm hδ)
  have hiu : (1 : ℝ) - u⁻¹ ≠ 0 := by
    intro hcon
    apply hδ
    have hinv : u⁻¹ = 1 := by linarith
    rw [← inv_inv u, hinv, inv_one]
  -- the bracket vanishes: `1/(1 − u⁻¹) = u/(u−1)` and `u/(1 − u) = −u/(u−1)`
  have hb : (1 - u⁻¹)⁻¹ + u * (1 - u)⁻¹ = 0 := by
    have hu1' : u - 1 ≠ 0 := fun h => hu1 (by linarith)
    have e : (1 : ℝ) - u⁻¹ = (u - 1) / u := by field_simp
    rw [e, inv_div]
    field_simp
    ring
  rw [div_eq_mul_inv, div_eq_mul_inv]
  have expand : (q - q⁻¹) * (1 - u⁻¹)⁻¹ * x + (q - q⁻¹) * (1 - u)⁻¹ * (x * u)
      = (q - q⁻¹) * x * ((1 - u⁻¹)⁻¹ + u * (1 - u)⁻¹) := by ring
  rw [expand, hb, mul_zero]

/-- **The matrix step.**  A `seminormalBlock` conjugating a diagonal matrix gives a diagonal matrix
with the two entries **exchanged** — provided the single condition `a·x + d·y = 0`, where
`d = (q − q⁻¹) − a` is the block's other diagonal entry.

Both off-diagonal entries of the product carry the same factor `a·x + d·y`, which is why one
hypothesis suffices for both. -/
theorem block_conj_diag (a x y : ℝ) (hcancel : a * x + ((q - q⁻¹) - a) * y = 0) :
    seminormalBlock q a * !![x, 0; 0, y] * seminormalBlock q a = !![y, 0; 0, x] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [seminormalBlock, Matrix.mul_apply, Fin.sum_univ_two]
  · linear_combination a * hcancel
  · linear_combination hcancel
  · linear_combination (a * (q - q⁻¹) - a ^ 2 + 1) * hcancel
  · linear_combination ((q - q⁻¹) - a) * hcancel

/-- **The orbit step.**  On a size-`2` orbit `{T, s_k T}` whose two swapped cells have contents
differing by `δ`, the seminormal generator `seminormalBlock q (a δ)` carries `diag(x, x·q^{2δ})` to
`diag(x·q^{2δ}, x)`.

Read with `x = q^{2c}` and `δ = axialDistance`: the two diagonal entries are `q^{2c}` and `q^{2c'}`,
and the conclusion is that `σ_k L_k σ_k` is again diagonal with the two contents **exchanged** —
the inductive step of [ram1997] Theorem 4.1 on an orbit of size `2`.

The only input beyond the two lemmas above is `seminormalParam_add_neg`, which identifies the
block's lower-right entry `(q − q⁻¹) − a(δ)` with `a(−δ)`.  So the whole step reduces to the
scalar cancellation: the axial distance is the *only* place the tableau combinatorics enters. -/
theorem seminormalBlock_conj_diag_swap (hq : q ≠ 0) (δ : ℤ) (hδ : q ^ (2 * δ) ≠ 1) (x : ℝ) :
    seminormalBlock q (seminormalParam q δ) * !![x, 0; 0, x * q ^ (2 * δ)]
        * seminormalBlock q (seminormalParam q δ)
      = !![x * q ^ (2 * δ), 0; 0, x] := by
  have hneg : q ^ ((-2 : ℤ) * δ) ≠ 1 := by
    rw [show (-2 : ℤ) * δ = -(2 * δ) by ring, zpow_neg]
    intro hcon
    exact hδ (by rw [← inv_inv (q ^ (2 * δ)), hcon, inv_one])
  have hd : (q - q⁻¹) - seminormalParam q δ = seminormalParam q (-δ) := by
    have := seminormalParam_add_neg q δ hq hneg
    linarith
  refine block_conj_diag q _ x (x * q ^ (2 * δ)) ?_
  rw [hd]
  exact seminormalParam_weighted_sum_zero q hq δ hδ x

end OrbitStep

end TableauCells

end QOU.SchurWeyl
