import QOU.MathlibExt.CauchyBinet
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.Basis.Basic
import Mathlib.LinearAlgebra.Dimension.Constructions

/-!
# Full row rank ⇒ some `r × r` minor is nonzero

For `M : Matrix (Fin r) (Fin n) K` over a field, linearly independent rows
force **some** `r × r` column selection to have nonzero determinant.

**Mathlib does not have this.** It has the square characterisation
(`Matrix.linearIndependent_rows_iff_isUnit`, `m × m` only) and the rank API
(`Matrix.rank`, `rank_eq_finrank_span_cols`), but nothing connecting rank to
minors of a *rectangular* matrix — there is no minor API outside
`Adjugate` and `PosDef`.

## Why it is wanted here

This is the missing hypothesis of `CauchyBinet.det_gram_map_ne_zero`, which
takes "one `r × r` minor of the integer matrix `M` is nonzero" and returns
"`det (N Nᵀ) ≠ 0` over every characteristic-zero field". Linear independence
of the rows is what a caller actually has; a nonzero minor is what the
Cauchy–Binet corollary wants. This file is the bridge, and
`det_gram_map_ne_zero_of_linearIndependent` at the bottom is the composite:

  `M : Matrix (Fin r) (Fin n) ℤ` with `ℚ`-independent rows
    ⟹ `det (N Nᵀ) ≠ 0` for `N = M.map (Int.cast : ℤ → k)`, any `[CharZero k]`.

## Proof route

Three moves, all at the level of *column indices* — never converting a set of
column vectors back into a set of indices, which is where this argument
usually gets painful in a proof assistant.

1. Independent rows ⇒ `M.rank = r` (`LinearIndependent.rank_matrix`) ⇒ the
   columns span `K^r`, since `rank` is also the dimension of the column span.
2. `exists_linearIndepOn_extension` extracts an **index set** `b ⊆ Fin n` whose
   columns are independent and still cover the rest. It is stated for
   `LinearIndepOn`, i.e. indexed by a set, so no vector-to-index step arises.
3. Independent + spanning ⇒ `b` is a basis ⇒ `b.card = r`; enumerate `b` in
   increasing order with `Finset.orderEmbOfFin` to get the `Selector`, and the
   resulting square submatrix has independent columns, hence is a unit.
-/

namespace QOU.MathlibExt.RankMinor

open Matrix Finset QOU.MathlibExt.CauchyBinet

variable {K : Type*} [Field K]

/-! ## Step 1 — full row rank makes the columns span -/

/-- **The columns of a full-row-rank matrix span `K^r`.** Row rank is column
rank, so the column span has dimension `r` inside an `r`-dimensional space. -/
theorem span_col_eq_top {r n : ℕ} (M : Matrix (Fin r) (Fin n) K)
    (hM : LinearIndependent K M.row) :
    Submodule.span K (Set.range M.col) = ⊤ := by
  have hrank : M.rank = r := by simpa using hM.rank_matrix
  refine Submodule.eq_top_of_finrank_eq ?_
  rw [← M.rank_eq_finrank_span_cols, hrank, Module.finrank_fin_fun]

/-! ## Step 2 — extract an independent spanning set of column *indices*

`exists_linearIndepOn_extension` is the lemma that keeps this argument in the
index world: it is stated for `LinearIndepOn K v b` with `b : Set ι`, so what
comes back is a set of column indices, not a set of column vectors. -/

/-- **An `r`-element set of columns forming a basis.** -/
theorem exists_finset_col_basis {r n : ℕ} (M : Matrix (Fin r) (Fin n) K)
    (hM : LinearIndependent K M.row) :
    ∃ S : Finset (Fin n), S.card = r ∧ LinearIndepOn K M.col (S : Set (Fin n)) := by
  obtain ⟨b, -, -, hcover, hind⟩ :=
    exists_linearIndepOn_extension (K := K) (v := M.col)
      (linearIndepOn_empty K M.col) (Set.empty_subset (Set.univ : Set (Fin n)))
  -- the covered image already spans, so `b`'s columns span too
  have hspan : Submodule.span K (M.col '' b) = ⊤ := by
    refine top_le_iff.mp ?_
    rw [← span_col_eq_top M hM, ← Set.image_univ]
    exact Submodule.span_le.mpr hcover
  -- independent + spanning = basis, and a basis of `K^r` has `r` elements
  haveI : Fintype b := Set.Finite.fintype (Set.toFinite b)
  -- `Basis` lives in `namespace Module` at this Mathlib revision
  have hbasis : Module.Basis b K (Fin r → K) := by
    refine Module.Basis.mk hind ?_
    rw [← Set.image_eq_range, hspan]
  have hcard : Fintype.card b = r := by
    have := Module.finrank_eq_card_basis hbasis
    rwa [Module.finrank_fin_fun, eq_comm] at this
  refine ⟨b.toFinset, ?_, ?_⟩
  · rwa [Set.toFinset_card]
  · rwa [Set.coe_toFinset]

/-! ## Step 3 — the selector, and the minor it names -/

/-- **Full row rank ⇒ a nonzero maximal minor.** Some strictly monotone
selection of `r` columns has invertible square submatrix.

This is the hypothesis `CauchyBinet.det_gram_map_ne_zero` asks for. -/
theorem exists_selector_det_ne_zero {r n : ℕ} (M : Matrix (Fin r) (Fin n) K)
    (hM : LinearIndependent K M.row) :
    ∃ f : Selector r n, (minorA M f).det ≠ 0 := by
  obtain ⟨S, hcard, hind⟩ := exists_finset_col_basis M hM
  -- enumerate `S` in increasing order: that is exactly a `Selector`
  set e := S.orderEmbOfFin hcard with he
  refine ⟨⟨e, e.strictMono⟩, ?_⟩
  -- the selected submatrix's columns are `M.col ∘ e`, independent because
  -- `e` is an injection of `Fin r` onto `S`
  have hmem : ∀ i, e i ∈ (S : Set (Fin n)) := fun i => S.orderEmbOfFin_mem hcard i
  have hcols : LinearIndependent K (minorA M ⟨e, e.strictMono⟩).col := by
    have : (minorA M ⟨e, e.strictMono⟩).col
        = (fun x : (S : Set (Fin n)) => M.col x) ∘ (fun i => ⟨e i, hmem i⟩) := rfl
    rw [this]
    refine hind.comp _ (fun i j hij => ?_)
    exact (S.orderEmbOfFin hcard).injective (congrArg Subtype.val hij)
  exact (Matrix.isUnit_iff_isUnit_det _).mp
    (Matrix.linearIndependent_cols_iff_isUnit.mp hcols) |>.ne_zero

/-! ## Composite — the statement a caller actually has hypotheses for

An integer matrix with `ℚ`-independent rows has a nonsingular Gram matrix over
*every* characteristic-zero field. Nothing here is ordered except `ℤ`, which is
the whole point: the conclusion travels to `ℂ` without the form ever being
positive definite there.

The rank argument runs over `ℚ` (a field, so §1–3 apply), the sum of squares
runs over `ℤ` (ordered, so Cauchy–Binet gives positivity), and only the final
`≠ 0` crosses into `k`. -/

/-- Casting commutes with taking a minor. -/
theorem map_minorA {r n : ℕ} {R S : Type*} [CommRing R] [CommRing S]
    (φ : R →+* S) (M : Matrix (Fin r) (Fin n) R) (f : Selector r n) :
    minorA (M.map φ) f = (minorA M f).map φ := rfl

/-- **The composite.** `M` integer with `ℚ`-linearly independent rows ⇒
`det (N Nᵀ) ≠ 0` where `N` is `M` cast into any characteristic-zero field. -/
theorem det_gram_map_ne_zero_of_linearIndependent {r n : ℕ} {k : Type*}
    [Field k] [CharZero k] (M : Matrix (Fin r) (Fin n) ℤ)
    (hM : LinearIndependent ℚ (M.map (Int.cast : ℤ → ℚ)).row) :
    ((M.map (Int.cast : ℤ → k)) * (M.map (Int.cast : ℤ → k))ᵀ).det ≠ 0 := by
  obtain ⟨f, hf⟩ := exists_selector_det_ne_zero _ hM
  -- a minor nonzero over ℚ is a minor nonzero over ℤ, `Int.cast` being injective
  refine det_gram_map_ne_zero M (f₀ := f) ?_
  intro hz
  refine hf ?_
  have hcast : minorA (M.map (Int.cast : ℤ → ℚ)) f = (minorA M f).map (Int.cast : ℤ → ℚ) :=
    map_minorA (Int.castRingHom ℚ) M f
  -- `RingHom.map_det` is stated with `mapMatrix`, which is `Matrix.map` on the
  -- nose but not syntactically; bridge it before rewriting
  have hmm : (Int.castRingHom ℚ).mapMatrix (minorA M f)
      = (minorA M f).map (Int.cast : ℤ → ℚ) := rfl
  have hdet := (Int.castRingHom ℚ).map_det (minorA M f)
  rw [hmm] at hdet
  rw [hcast, ← hdet, hz]
  simp

/-! ## The same, over arbitrary finite index types

`Selector r n` is `Fin`-indexed by construction (`StrictMono` needs an order),
so everything above is stated for `Matrix (Fin r) (Fin n)`. A caller's matrix
is usually indexed by whatever its data is indexed by — a set of tableaux, a
quotient — so it has to be reindexed through `Fintype.equivFin` first. That is
pure bookkeeping and belongs here, not at each call site. -/

/-- **Index-type-agnostic form.** Same statement as
`det_gram_map_ne_zero_of_linearIndependent`, with the row and column indices
arbitrary finite types. -/
theorem det_gram_map_ne_zero_of_linearIndependent' {ι κ : Type*} [Fintype ι] [Fintype κ]
    [DecidableEq ι] {k : Type*} [Field k] [CharZero k] (M : Matrix ι κ ℤ)
    (hM : LinearIndependent ℚ (M.map (Int.cast : ℤ → ℚ)).row) :
    ((M.map (Int.cast : ℤ → k)) * (M.map (Int.cast : ℤ → k))ᵀ).det ≠ 0 := by
  classical
  set eι := Fintype.equivFin ι with heι
  set eκ := Fintype.equivFin κ with heκ
  -- transport `M` to `Fin`-indices
  set M' : Matrix (Fin (Fintype.card ι)) (Fin (Fintype.card κ)) ℤ :=
    M.submatrix eι.symm eκ.symm with hM'
  -- independence survives: the rows are reindexed by a bijection *and* have
  -- their entries permuted, the latter being a linear equivalence of `κ → ℚ`
  have hM'ind : LinearIndependent ℚ (M'.map (Int.cast : ℤ → ℚ)).row := by
    have hrow : (M'.map (Int.cast : ℤ → ℚ)).row
        = (LinearEquiv.funCongrLeft ℚ ℚ eκ.symm) ∘
            ((M.map (Int.cast : ℤ → ℚ)).row ∘ eι.symm) := rfl
    rw [hrow]
    refine (hM.comp _ eι.symm.injective).map' _ (LinearMap.ker_eq_bot.mpr ?_)
    exact (LinearEquiv.funCongrLeft ℚ ℚ eκ.symm).injective
  have key := det_gram_map_ne_zero_of_linearIndependent (k := k) M' hM'ind
  -- and the Gram determinant is unchanged: the two reindexings cancel
  have hgram : (M'.map (Int.cast : ℤ → k)) * (M'.map (Int.cast : ℤ → k))ᵀ
      = ((M.map (Int.cast : ℤ → k)) * (M.map (Int.cast : ℤ → k))ᵀ).submatrix
          eι.symm eι.symm := by
    show ((M.map (Int.cast : ℤ → k)).submatrix eι.symm eκ.symm)
        * ((M.map (Int.cast : ℤ → k)).submatrix eι.symm eκ.symm)ᵀ = _
    rw [Matrix.transpose_submatrix, Matrix.submatrix_mul_equiv]
  rwa [hgram, Matrix.det_submatrix_equiv_self] at key

end QOU.MathlibExt.RankMinor
