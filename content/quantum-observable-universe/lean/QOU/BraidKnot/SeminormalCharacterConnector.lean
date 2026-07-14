/-
# Seminormal character connector — standard tableaux → the `χ_λ(σ) = c_λ·h` core

Infra 4→5 connector (beans `qou-9vvr` done / `qou-tqab`) of the YT seminormal-sum
program. The algebraic core is proved in
[`SeminormalWeight`](SeminormalWeight.lean) (`fullCharacter_two_mul`:
`2·χ_λ(σ) = (2|R_row| + |S_off|)·h`) and
[`TableauContent`](TableauContent.lean) (content / axial distance). This file
**reuses the canonical `QOU.Mathlib.StandardYoungTableau`** (the `BijOn`-filled
standard tableau — *not* a re-definition) and builds the connector that supplies
that core's `(cellOf, ρ)` data per tableau:

* `cellOf T k` — the cell of `μ` holding entry `k` (the inverse of the bijective
  filling), the position map the character sum ranges over;
* `generatorRho T i` — the axial distance `ρ` of the generator pair `(i, i+1)`,
  i.e. `axialDistance (cellOf T i) (cellOf T (i+1))`, the `ρ` feeding `a_ρ`.

Remaining to *discharge* `symbolic_character_table` (bean `qou-tqab`, coordinate
with #3719 per `docs/coordination/yt-seminormal-infra.md`): the partition of the
SYT set into same-row / same-column / off-diagonal classes for the σ₁ generator,
the conjugate-transpose bijection giving `|R_row| = |R_col|` for a self-conjugate
`μ`, and the wire into that block's abstract `chiSigma`.

-- Ref: [sagan2001] The Symmetric Group, §3.3 (Young's seminormal form)
-/
import QOU.BraidKnot.TableauContent
import QOU.Mathlib.StandardYoungTableau

namespace QOU.BraidKnot.SeminormalCharacterConnector

open QOU.Mathlib QOU.BraidKnot.TableauContent

variable {μ : YoungDiagram}

open Classical in
/-- **The cell holding entry `k`** — the inverse of the bijective filling. For `k`
    in the value range `{1,…,|μ|}` the filling's surjectivity gives a (unique) cell;
    off-range it defaults to `(0,0)`. Noncomputable (choice on surjectivity). -/
noncomputable def cellOf (T : StandardYoungTableau μ) (k : ℕ) : ℕ × ℕ :=
  if h : ∃ c ∈ μ.cells, T.entry c.1 c.2 = k then h.choose else (0, 0)

/-- **Generator axial distance** `ρ = c(cell of i+1) − c(cell of i)`: the axial
    distance of the generator pair `(i, i+1)` in `T`, the `ρ` of the seminormal
    weight `a_ρ` that the character sum ranges over (`TableauContent.axialDistance`). -/
noncomputable def generatorRho (T : StandardYoungTableau μ) (i : ℕ) : ℤ :=
  axialDistance (cellOf T i) (cellOf T (i + 1))

/-- When `k` is actually an entry of `T` (some cell of `μ` maps to it), `cellOf T k`
    is a cell of `μ` and carries entry `k`. -/
theorem cellOf_spec (T : StandardYoungTableau μ) {k : ℕ}
    (hk : ∃ c ∈ μ.cells, T.entry c.1 c.2 = k) :
    cellOf T k ∈ μ.cells ∧ T.entry (cellOf T k).1 (cellOf T k).2 = k := by
  classical
  rw [cellOf, dif_pos hk]
  exact ⟨hk.choose_spec.1, hk.choose_spec.2⟩

/-- The generator axial distance is antisymmetric in the two entries:
    `ρ(i, i+1) = −ρ(i+1, i)` (via `TableauContent.axialDistance_antisymm`) — the
    cell-geometry root of the seminormal ρ ↔ −ρ pairing that makes the reduced-weight
    sum an integer `c_λ` (`SeminormalWeight.two_mul_reducedSum_eq_card`). -/
theorem generatorRho_swap (T : StandardYoungTableau μ) (i : ℕ) :
    axialDistance (cellOf T i) (cellOf T (i + 1))
      = -axialDistance (cellOf T (i + 1)) (cellOf T i) :=
  axialDistance_antisymm _ _

/-- **The `|R_row| = |R_col|` structural core (self-conjugacy ⇒ equal counts).**
    Given a self-inverse map `f` on the standard-tableau index set that carries the
    **same-row** class `Rrow` (`1, 2` in the same row) into the **same-column**
    class `Rcol` and back, the two classes have equal cardinality. The
    **conjugate transpose** `T ↦ Tᵀ` is exactly such an `f` for a self-conjugate
    `μ` (`μ = μᵀ`): it maps `SYT(μ)` to itself, is an involution, and swaps
    same-row ↔ same-column for the pair `1, 2`.

    This is the structural half of the σ₁-character closure: with `|Rrow| = |Rcol|`
    the diagonal contribution `|Rrow|·q + |Rcol|·(−q⁻¹) = |Rrow|·h` is an integer
    multiple of `h`, feeding `SeminormalWeight.fullCharacter_two_mul` (with the
    off-diagonal class empty for the single generator σ₁). Robust `Finset.image`
    proof — no heavy tableau machinery here; the remaining piece (bean `qou-tqab`)
    is *constructing* the transpose involution on the canonical
    `StandardYoungTableau` and discharging its three hypotheses. -/
theorem card_row_eq_card_col {ι : Type*} [DecidableEq ι]
    (Rrow Rcol : Finset ι) (f : ι → ι)
    (hf_row : ∀ t ∈ Rrow, f t ∈ Rcol) (hf_col : ∀ t ∈ Rcol, f t ∈ Rrow)
    (hff : ∀ t, f (f t) = t) :
    Rrow.card = Rcol.card := by
  have hinj : Set.InjOn f (Rrow : Set ι) := fun a _ b _ h => by
    have h2 := congrArg f h; rwa [hff, hff] at h2
  have himg : Rrow.image f = Rcol := by
    apply Finset.Subset.antisymm
    · intro b hb
      rw [Finset.mem_image] at hb
      obtain ⟨a, ha, rfl⟩ := hb
      exact hf_row a ha
    · intro b hb
      rw [Finset.mem_image]
      exact ⟨f b, hf_col b hb, hff b⟩
  rw [← himg, Finset.card_image_of_injOn hinj]

/-! ## The conjugate transpose (bean `qou-tqab`) -/

/-- **Cell membership in the transpose**: `(i, j) ∈ μᵀ ↔ (j, i) ∈ μ`. The transpose
    cell set is the `Prod.swap`-image of `μ`'s cells (`YoungDiagram.transpose`). -/
theorem mem_transpose_iff {i j : ℕ} : (i, j) ∈ μ.transpose ↔ (j, i) ∈ μ :=
  YoungDiagram.mem_transpose

/-- **The conjugate transpose of a standard tableau, as a semistandard tableau of
    `μᵀ`** — the mathematical heart of the row↔column swap: `entry (i,j) := T.entry
    (j,i)`. Weak rows of the transpose come from `T`'s **strict columns**
    (`col_strict`); strict columns come from `T`'s **strict rows** (`row_strict`,
    which holds for a *standard* tableau by bijectivity). The residual off-diagram
    zeros transport through `mem_transpose_iff`. -/
def transposeSsyt (T : StandardYoungTableau μ) : SemistandardYoungTableau μ.transpose where
  entry i j := T.entry j i
  zeros' := fun h => T.toSsyt.zeros (fun hc => h (mem_transpose_iff.mpr hc))
  row_weak' := fun hj hcell =>
    le_of_lt (T.toSsyt.col_strict hj (mem_transpose_iff.mp hcell))
  col_strict' := fun hi hcell =>
    T.row_strict hi (mem_transpose_iff.mp hcell)

/-- **`Prod.swap` is a bijection of cell sets** `μᵀ.cells ↔ μ.cells`. The transpose
    cell set is the swap-image of `μ`'s (`mem_transpose_iff`), so swapping coordinates
    carries one onto the other and is its own inverse (`Prod.swap_swap`). -/
theorem swap_bijOn_cells (μ : YoungDiagram) :
    Set.BijOn Prod.swap (μ.transpose.cells : Set (ℕ × ℕ)) (μ.cells : Set (ℕ × ℕ)) := by
  refine ⟨fun c hc => ?_, Prod.swap_injective.injOn, fun c hc => ?_⟩
  · simp only [Finset.mem_coe, YoungDiagram.mem_cells] at hc ⊢
    exact mem_transpose_iff.mp hc
  · simp only [Finset.mem_coe, YoungDiagram.mem_cells] at hc
    refine ⟨Prod.swap c, ?_, Prod.swap_swap c⟩
    simp only [Finset.mem_coe, YoungDiagram.mem_cells]
    exact mem_transpose_iff.mpr hc

/-- **Transpose preserves the cell count** `|μᵀ| = |μ|`: the cell set is a `Prod.swap`
    reindex of `μ`'s (`Finset.card_map`). -/
theorem transpose_cells_card (μ : YoungDiagram) :
    μ.transpose.cells.card = μ.cells.card := by
  have hmap : μ.transpose.cells = μ.cells.map (Equiv.prodComm ℕ ℕ).toEmbedding := by
    simp [YoungDiagram.transpose, Equiv.finsetCongr_apply]
  rw [hmap, Finset.card_map]

/-- **The conjugate transpose of a standard tableau** `T ↦ Tᵀ`, as a full
    `StandardYoungTableau μᵀ`. The semistandard content is `transposeSsyt`; the
    bijectivity of the filling is `T`'s own filling bijection **precomposed with the
    `Prod.swap` cell bijection** (`swap_bijOn_cells`), the value range shifted by the
    cardinality identity `|μᵀ| = |μ|` (`transpose_cells_card`).

    This is the concrete construction the σ₁-character closure needs: for a
    self-conjugate `μ` (`μ = μᵀ`) it is an **involution on `SYT(μ)`** that swaps the
    same-row and same-column classes of the pair `1, 2`, discharging the three
    hypotheses of `card_row_eq_card_col` and hence `|R_row| = |R_col|`. -/
def transpose (T : StandardYoungTableau μ) : StandardYoungTableau μ.transpose where
  toSsyt := transposeSsyt T
  bijOn := by
    have hfun : (fun c : ℕ × ℕ => (transposeSsyt T).entry c.1 c.2)
        = (fun c : ℕ × ℕ => T.toSsyt.entry c.1 c.2) ∘ Prod.swap := by
      funext c; rfl
    rw [hfun, transpose_cells_card]
    exact T.bijOn.comp (swap_bijOn_cells μ)

/-- **The double transpose recovers the filling** at the entry level: `Tᵀᵀ` has the
    same entry map as `T` (`entry (i,j) = T.entry (i,j)`). Definitional — the entry
    of `transpose` is the coordinate-swapped entry of its argument, and swapping
    twice is the identity. This is the involution-of-transpose statement in the form
    the character sum consumes (entry-level), independent of the
    `μᵀᵀ = μ` diagram identification. -/
theorem transpose_transpose_entry (T : StandardYoungTableau μ) (i j : ℕ) :
    (transpose (transpose T)).entry i j = T.entry i j := rfl

/-! ## The self-conjugate involution (bean `qou-tqab`) -/

/-- **Transport preserves the entry map**: casting a standard tableau along a diagram
    equality `μ = ν` leaves each entry value unchanged (the entry map is
    `ℕ → ℕ → ℕ`, independent of the diagram). Proved with fresh `ν` so the transport
    `subst`s cleanly — the self-referential `μᵀ = μ` case is recovered by
    instantiation. -/
theorem entry_cast {μ ν : YoungDiagram} (h : μ = ν) (S : StandardYoungTableau μ)
    (i j : ℕ) : (h ▸ S).entry i j = S.entry i j := by
  cases h; rfl

/-- **The self-conjugate transpose** — for a **self-conjugate** shape (`μᵀ = μ`), the
    conjugate transpose is an endomorphism `SYT(μ) → SYT(μ)`, obtained by transporting
    `transpose T : SYT(μᵀ)` back across `μᵀ = μ`. This is the `f` that
    `card_row_eq_card_col` consumes: for the generator pair `1, 2` it swaps the
    same-row and same-column classes. -/
noncomputable def selfTranspose (h : μ.transpose = μ) (T : StandardYoungTableau μ) :
    StandardYoungTableau μ :=
  h ▸ transpose T

/-- The self-conjugate transpose swaps coordinates at the entry level:
    `(selfTranspose h T).entry (i,j) = T.entry (j,i)`. -/
theorem selfTranspose_entry (h : μ.transpose = μ) (T : StandardYoungTableau μ)
    (i j : ℕ) : (selfTranspose h T).entry i j = T.entry j i := by
  rw [selfTranspose, entry_cast]
  rfl

/-- **`selfTranspose` is an involution** (entry level): applying the self-conjugate
    transpose twice recovers `T`'s filling. This is the involutivity hypothesis
    `card_row_eq_card_col` needs, in the entry form the class Finsets are cut out by. -/
theorem selfTranspose_involutive (h : μ.transpose = μ) (T : StandardYoungTableau μ)
    (i j : ℕ) : (selfTranspose h (selfTranspose h T)).entry i j = T.entry i j := by
  rw [selfTranspose_entry, selfTranspose_entry]

/-! ## The `cellOf`-swap bridge (bean `qou-tqab`) -/

/-- **`cellOf` is pinned by any witnessing cell** — the inverse of the filling is
    unique. If `c` is a cell of `μ` carrying entry `k`, then `cellOf T k = c`
    (filling injectivity, `injOn_cells`). This is the uniqueness the choice-based
    `cellOf` needs to compose with a coordinate swap. -/
theorem cellOf_eq_of_entry (T : StandardYoungTableau μ) {k : ℕ} {c : ℕ × ℕ}
    (hc : c ∈ μ.cells) (hk : T.entry c.1 c.2 = k) : cellOf T k = c := by
  obtain ⟨hmem, hval⟩ := cellOf_spec T ⟨c, hc, hk⟩
  exact T.injOn_cells (Finset.mem_coe.mpr hmem) (Finset.mem_coe.mpr hc)
    (hval.trans hk.symm)

/-- **The self-conjugate transpose swaps cells**:
    `cellOf (selfTranspose h T) k = Prod.swap (cellOf T k)`. The cell holding `k` in
    `Tᵀ` is the coordinate swap of the cell holding `k` in `T` — the entry-level
    coordinate swap (`selfTranspose_entry`) lifted through the pinned inverse
    (`cellOf_eq_of_entry`), the swapped cell staying in `μ` by
    `swap_bijOn_cells` + self-conjugacy. This is the **same-row ↔ same-column
    class swap** for the generator pair `1, 2`: whichever of `(cellOf T 1),
    (cellOf T 2)` shared a row now shares a column, discharging the
    class-exchange hypotheses of `card_row_eq_card_col`. -/
theorem cellOf_selfTranspose (h : μ.transpose = μ) (T : StandardYoungTableau μ) {k : ℕ}
    (hk : ∃ c ∈ μ.cells, T.entry c.1 c.2 = k) :
    cellOf (selfTranspose h T) k = Prod.swap (cellOf T k) := by
  obtain ⟨hmem, hval⟩ := cellOf_spec T hk
  apply cellOf_eq_of_entry
  · have h1 : cellOf T k ∈ (μ.transpose.cells : Set (ℕ × ℕ)) := by
      rw [h]; exact Finset.mem_coe.mpr hmem
    exact Finset.mem_coe.mp ((swap_bijOn_cells μ).mapsTo h1)
  · rw [selfTranspose_entry]; exact hval

/-! ## The σ₁ class-count identity `|R_row| = |R_col|` (bean `qou-tqab`)

The concrete `Finset.card` payload: for a **self-conjugate** shape with `≥ 2`
cells, the same-row and same-column classes of the pair `1, 2` are equinumerous.
`SYT(μ)` is a `Fintype` (via the `encode` injection already in
`StandardYoungTableau`), the classes are `Finset.filter`s, and `selfTranspose`
is the bijection between them (`cellOf_selfTranspose` swaps row ↔ column,
`selfTranspose_selfTranspose` is the involution). -/

/-- **Surjectivity of the filling**: every value in `{1,…,|μ|}` is the entry of some
    cell (`bijOn.surjOn`). -/
theorem exists_cell_entry (T : StandardYoungTableau μ) {k : ℕ}
    (hk : k ∈ Set.Icc 1 μ.cells.card) : ∃ c ∈ μ.cells, T.entry c.1 c.2 = k := by
  obtain ⟨c, hc, hce⟩ := T.bijOn.surjOn hk
  exact ⟨c, Finset.mem_coe.mp hc, hce⟩

/-- **The self-conjugate transpose is a structural involution** on `SYT(μ)`:
    `selfTranspose h (selfTranspose h T) = T` (full equality, not just entry level —
    lifted through the `encode` injection). -/
theorem selfTranspose_selfTranspose (h : μ.transpose = μ) (T : StandardYoungTableau μ) :
    selfTranspose h (selfTranspose h T) = T := by
  apply StandardYoungTableau.encode_injective
  funext c
  apply Fin.ext
  exact selfTranspose_involutive h T c.1.1 c.1.2

section Closure
open scoped Classical

/-- `SYT(μ)` is a `Fintype` (the `encode` injection into a finite function space,
    already proved injective in `StandardYoungTableau`). Noncomputable — the count is
    what matters, not an enumeration algorithm. -/
noncomputable instance instFintypeSYT (μ : YoungDiagram) :
    Fintype (StandardYoungTableau μ) :=
  Fintype.ofInjective StandardYoungTableau.encode StandardYoungTableau.encode_injective

/-- **Same-row class predicate** for the generator pair `1, 2`: the cells holding
    `1` and `2` share a row. -/
def sameRow12 (T : StandardYoungTableau μ) : Prop := (cellOf T 1).1 = (cellOf T 2).1

/-- **Same-column class predicate** for the pair `1, 2`. -/
def sameCol12 (T : StandardYoungTableau μ) : Prop := (cellOf T 1).2 = (cellOf T 2).2

/-- The **same-row class** `R_row ⊆ SYT(μ)`. -/
noncomputable def rowClass (μ : YoungDiagram) : Finset (StandardYoungTableau μ) :=
  Finset.univ.filter (fun T => sameRow12 T)

/-- The **same-column class** `R_col ⊆ SYT(μ)`. -/
noncomputable def colClass (μ : YoungDiagram) : Finset (StandardYoungTableau μ) :=
  Finset.univ.filter (fun T => sameCol12 T)

/-- `selfTranspose` carries the same-row class to the same-column class: for `≥ 2`
    cells and self-conjugate `μ`, `sameRow12 (selfTranspose h T) ↔ sameCol12 T`
    (`cellOf_selfTranspose` swaps the row/column coordinate). -/
theorem sameRow12_selfTranspose (h : μ.transpose = μ) (hn : 2 ≤ μ.cells.card)
    (T : StandardYoungTableau μ) : sameRow12 (selfTranspose h T) ↔ sameCol12 T := by
  have e1 : (1 : ℕ) ∈ Set.Icc 1 μ.cells.card := Set.mem_Icc.mpr ⟨le_refl 1, by omega⟩
  have e2 : (2 : ℕ) ∈ Set.Icc 1 μ.cells.card := Set.mem_Icc.mpr ⟨by norm_num, by omega⟩
  have c1 := cellOf_selfTranspose h T (exists_cell_entry T e1)
  have c2 := cellOf_selfTranspose h T (exists_cell_entry T e2)
  unfold sameRow12 sameCol12
  rw [c1, c2]
  simp only [Prod.fst_swap]

/-- `selfTranspose` carries the same-column class to the same-row class. -/
theorem sameCol12_selfTranspose (h : μ.transpose = μ) (hn : 2 ≤ μ.cells.card)
    (T : StandardYoungTableau μ) : sameCol12 (selfTranspose h T) ↔ sameRow12 T := by
  have e1 : (1 : ℕ) ∈ Set.Icc 1 μ.cells.card := Set.mem_Icc.mpr ⟨le_refl 1, by omega⟩
  have e2 : (2 : ℕ) ∈ Set.Icc 1 μ.cells.card := Set.mem_Icc.mpr ⟨by norm_num, by omega⟩
  have c1 := cellOf_selfTranspose h T (exists_cell_entry T e1)
  have c2 := cellOf_selfTranspose h T (exists_cell_entry T e2)
  unfold sameCol12 sameRow12
  rw [c1, c2]
  simp only [Prod.snd_swap]

/-- **The σ₁ class-count identity** `|R_row| = |R_col|`. For a self-conjugate shape
    with `≥ 2` cells, the same-row and same-column classes of the generator pair
    `1, 2` are equinumerous — `selfTranspose` is the explicit bijection between them
    (row ↔ column swap + involution), fed to `card_row_eq_card_col`. This is the
    concrete `Finset.card` heart of the σ₁ seminormal character `χ_λ(σ₁) = c_λ·h`. -/
theorem card_rowClass_eq_colClass (h : μ.transpose = μ) (hn : 2 ≤ μ.cells.card) :
    (rowClass μ).card = (colClass μ).card := by
  apply card_row_eq_card_col (rowClass μ) (colClass μ) (selfTranspose h)
  · intro T hT
    rw [rowClass, Finset.mem_filter] at hT
    rw [colClass, Finset.mem_filter]
    exact ⟨Finset.mem_univ _, (sameCol12_selfTranspose h hn T).mpr hT.2⟩
  · intro T hT
    rw [colClass, Finset.mem_filter] at hT
    rw [rowClass, Finset.mem_filter]
    exact ⟨Finset.mem_univ _, (sameRow12_selfTranspose h hn T).mpr hT.2⟩
  · exact selfTranspose_selfTranspose h

end Closure

end QOU.BraidKnot.SeminormalCharacterConnector
