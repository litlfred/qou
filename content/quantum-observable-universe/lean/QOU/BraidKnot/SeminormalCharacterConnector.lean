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

The σ₁ closure is now concrete and sorry-free: `sigmaOneCharacter_eq_card_mul`
proves `χ_λ(σ₁) = |R_row|·h` for self-conjugate `μ` (`c_λ = |R_row| ∈ ℤ`), via
the SYT `Fintype`, the same-row/same-column class `Finset`s
(`rowClass`/`colClass`), the conjugate-transpose bijection between them
(`card_rowClass_eq_colClass`), and `SeminormalWeight.fullCharacter_two_mul` at
`Soff = ∅`. What remains to reach the *tabulated* `c_λ ∈ {1, 3, 8, 10}` of
`symbolic_character_table` is the per-shape count `|R_row|` for each
self-conjugate partition; the block's abstract `chiSigma` field is an opaque
input, not dischargeable in place without restating that block.

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

/-! ### The concrete σ₁ seminormal character `χ_λ(σ₁) = c_λ·h`

For the single generator `σ₁`, values `1, 2` are always adjacent (`1` at the
corner), so the **off-diagonal class is empty** — the σ₁ character is purely
diagonal, `|R_row|·q + |R_col|·(h − q)`. Instantiating
`SeminormalWeight.fullCharacter_two_mul` at `Soff = ∅` with the class-count
identity `card_rowClass_eq_colClass` collapses it to an integer multiple of `h`.
This is the concrete, sorry-free realization of `prop:symbolic-character-table`'s
"self-conjugate ⇒ integer coefficient" — `c_λ = |R_row| ∈ ℤ` — for `σ₁`. -/

/-- The **concrete σ₁ seminormal character** on `S^λ`: purely diagonal (the
    off-diagonal class is empty for `σ₁`), `|R_row|·q + |R_col|·(h − q)`. -/
noncomputable def sigmaOneCharacter (μ : YoungDiagram) {R : Type*} [Field R] (q hh : R) : R :=
  ((rowClass μ).card : R) * q + ((colClass μ).card : R) * (hh - q)

/-- **`2·χ_λ(σ₁) = 2·|R_row|·h`** — fully general over any `[Field R]`. The σ₁
    character is an integer multiple of `h`; `fullCharacter_two_mul` at `Soff = ∅`
    plus `card_rowClass_eq_colClass`. -/
theorem two_mul_sigmaOneCharacter (h : μ.transpose = μ) (hn : 2 ≤ μ.cells.card)
    {R : Type*} [Field R] (q hh : R) (hq : q ≠ 0) :
    (2 : R) * sigmaOneCharacter μ q hh = ((2 * (rowClass μ).card : ℕ) : R) * hh := by
  have key := SeminormalWeight.fullCharacter_two_mul (ι := StandardYoungTableau μ)
    q hh (rowClass μ) (colClass μ) ∅ (fun _ => (0 : ℤ)) id
    (card_rowClass_eq_colClass h hn)
    (by intro t ht; exact absurd ht (Finset.notMem_empty t))
    (by intro t ht; exact absurd ht (Finset.notMem_empty t))
    (by intro t ht; exact absurd ht (Finset.notMem_empty t))
    hq
    (by intro t ht; exact absurd ht (Finset.notMem_empty t))
  rw [sigmaOneCharacter]
  simpa using key

/-- **`χ_λ(σ₁) = |R_row|·h`** (`c_λ = |R_row| ∈ ℤ`) — the proposition's factorisation
    for `σ₁`, over any field with `2 ≠ 0` (in particular `ℝ`). The remaining step to
    the tabulated `c_λ ∈ {1, 3, 8, 10}` is the per-shape count `|R_row|` for each
    self-conjugate `μ`. -/
theorem sigmaOneCharacter_eq_card_mul (h : μ.transpose = μ) (hn : 2 ≤ μ.cells.card)
    {R : Type*} [Field R] (q hh : R) (hq : q ≠ 0) (h2 : (2 : R) ≠ 0) :
    sigmaOneCharacter μ q hh = ((rowClass μ).card : R) * hh := by
  have key := two_mul_sigmaOneCharacter h hn q hh hq
  have hcast : ((2 * (rowClass μ).card : ℕ) : R) = 2 * ((rowClass μ).card : R) := by
    push_cast; ring
  rw [hcast, mul_assoc] at key
  exact mul_left_cancel₀ h2 key

/-! ### The per-shape count `c_λ = #SYT(μ)/2` (self-conjugate μ)

For `σ₁` the pair `1, 2` sits in the corner: `1` at `(0,0)` and `2` at the only
two addable cells `(0,1)` or `(1,0)`. Hence **every** standard tableau is in
exactly one of the two classes — `sameRow12 ∨ sameCol12` and never both — so
`rowClass ∪ colClass = univ` disjointly and `|R_row| + |R_col| = #SYT(μ)`. With
the conjugate-transpose identity `|R_row| = |R_col|`, this closes the per-shape
count with **no enumeration**: `2·|R_row| = #SYT(μ)`, i.e. `c_λ = #SYT(μ)/2`. -/

/-- **The `(0,0)` corner is minimal**: `T.entry 0 0 ≤ T.entry a b` for every cell
    `(a,b)` — weak rows to `(0,b)` then strict columns down to `(a,b)`. -/
theorem entry_le (T : StandardYoungTableau μ) {a b : ℕ} (hab : (a, b) ∈ μ) :
    T.entry 0 0 ≤ T.entry a b := by
  have h0b : (0, b) ∈ μ := μ.up_left_mem (Nat.zero_le a) (le_refl b) hab
  have h1 : T.entry 0 0 ≤ T.entry 0 b := by
    rcases Nat.eq_zero_or_pos b with hb | hb
    · subst hb; exact le_rfl
    · exact T.toSsyt.row_weak hb h0b
  have h2 : T.entry 0 b ≤ T.entry a b := by
    rcases Nat.eq_zero_or_pos a with ha | ha
    · subst ha; exact le_rfl
    · exact le_of_lt (T.toSsyt.col_strict ha hab)
  exact le_trans h1 h2

/-- **Entry `1` is at the corner**: `T.entry 0 0 = 1`. The corner is `≥ 1` (in the
    value range) and `≤` the cell carrying `1` (`entry_le`), so it *is* `1`. -/
theorem entry_zero_zero_eq_one (T : StandardYoungTableau μ) (hn : 1 ≤ μ.cells.card) :
    T.entry 0 0 = 1 := by
  obtain ⟨⟨a, b⟩, hcell, hval⟩ := exists_cell_entry T (Set.mem_Icc.mpr ⟨le_refl 1, hn⟩)
  have hval2 : T.entry a b = 1 := hval
  have hab : (a, b) ∈ μ := (YoungDiagram.mem_cells _).mp hcell
  have h00 : (0, 0) ∈ μ := μ.up_left_mem (Nat.zero_le a) (Nat.zero_le b) hab
  have hle : T.entry 0 0 ≤ T.entry a b := entry_le T hab
  rw [hval2] at hle
  have hge : 1 ≤ T.entry 0 0 :=
    (Set.mem_Icc.mp (T.mapsTo_cells (StandardYoungTableau.mem_coe_cells h00))).1
  omega

/-- **`(0,0) ∈ μ`** whenever `μ` has a cell (the diagram is a lower set). -/
theorem zero_zero_mem_cells (hn : 1 ≤ μ.cells.card) : (0, 0) ∈ μ.cells := by
  obtain ⟨⟨a, b⟩, hc⟩ := Finset.card_pos.mp (show 0 < μ.cells.card by omega)
  rw [YoungDiagram.mem_cells] at hc ⊢
  exact μ.up_left_mem (Nat.zero_le a) (Nat.zero_le b) hc

/-- **`cellOf T 1 = (0,0)`** — the entry `1` lives at the corner. -/
theorem cellOf_one (T : StandardYoungTableau μ) (hn : 1 ≤ μ.cells.card) :
    cellOf T 1 = (0, 0) :=
  cellOf_eq_of_entry T (zero_zero_mem_cells hn) (entry_zero_zero_eq_one T hn)

/-- **`cellOf T 2` sits on the corner row or column**: its row *or* column index is
    `0`. If both were `≥ 1`, its up-neighbour and left-neighbour would both carry an
    entry `< 2`, i.e. both `= 1` — two distinct cells with entry `1`, impossible by
    injectivity of the filling. -/
theorem cellOf_two_coord_zero (T : StandardYoungTableau μ) (hn : 2 ≤ μ.cells.card) :
    (cellOf T 2).1 = 0 ∨ (cellOf T 2).2 = 0 := by
  have h2range : (2 : ℕ) ∈ Set.Icc 1 μ.cells.card := Set.mem_Icc.mpr ⟨by norm_num, hn⟩
  obtain ⟨⟨a, b⟩, hcell, hval⟩ := exists_cell_entry T h2range
  have hpin : cellOf T 2 = (a, b) := cellOf_eq_of_entry T hcell hval
  rw [hpin]
  show a = 0 ∨ b = 0
  by_contra hcon
  push_neg at hcon
  obtain ⟨ha, hb⟩ := hcon
  have ha1 : 1 ≤ a := Nat.one_le_iff_ne_zero.mpr ha
  have hb1 : 1 ≤ b := Nat.one_le_iff_ne_zero.mpr hb
  have hval2 : T.entry a b = 2 := hval
  have hab : (a, b) ∈ μ := (YoungDiagram.mem_cells _).mp hcell
  have hn1_mem : (a - 1, b) ∈ μ := μ.up_left_mem (Nat.sub_le a 1) (le_refl b) hab
  have hn2_mem : (a, b - 1) ∈ μ := μ.up_left_mem (le_refl a) (Nat.sub_le b 1) hab
  have hlt1 : T.entry (a - 1) b < T.entry a b := T.toSsyt.col_strict (by omega) hab
  have hlt2 : T.entry a (b - 1) < T.entry a b := T.row_strict (by omega) hab
  have hge1 : 1 ≤ T.entry (a - 1) b :=
    (Set.mem_Icc.mp (T.mapsTo_cells (StandardYoungTableau.mem_coe_cells hn1_mem))).1
  have hge2 : 1 ≤ T.entry a (b - 1) :=
    (Set.mem_Icc.mp (T.mapsTo_cells (StandardYoungTableau.mem_coe_cells hn2_mem))).1
  have he1 : T.entry (a - 1) b = 1 := by rw [hval2] at hlt1; omega
  have he2 : T.entry a (b - 1) = 1 := by rw [hval2] at hlt2; omega
  have heq : (a - 1, b) = (a, b - 1) :=
    T.injOn_cells (StandardYoungTableau.mem_coe_cells hn1_mem)
      (StandardYoungTableau.mem_coe_cells hn2_mem)
      (by show T.entry (a - 1) b = T.entry a (b - 1); rw [he1, he2])
  have : a - 1 = a := congrArg Prod.fst heq
  omega

/-- **The σ₁ dichotomy**: for every standard tableau of a `≥ 2`-cell shape, `1` and
    `2` share a row *or* a column. -/
theorem sameRow12_or_sameCol12 (T : StandardYoungTableau μ) (hn : 2 ≤ μ.cells.card) :
    sameRow12 T ∨ sameCol12 T := by
  have h1 : cellOf T 1 = (0, 0) := cellOf_one T (by omega)
  rcases cellOf_two_coord_zero T hn with hi | hj
  · exact Or.inl (by unfold sameRow12; rw [h1]; exact hi.symm)
  · exact Or.inr (by unfold sameCol12; rw [h1]; exact hj.symm)

/-- **The σ₁ classes are disjoint**: `1` and `2` cannot share *both* a row and a
    column (they would occupy the same cell, but carry different entries). -/
theorem not_sameRow12_and_sameCol12 (T : StandardYoungTableau μ) (hn : 2 ≤ μ.cells.card) :
    ¬ (sameRow12 T ∧ sameCol12 T) := by
  rintro ⟨hr, hc⟩
  have hcell_eq : cellOf T 1 = cellOf T 2 := Prod.ext_iff.mpr ⟨hr, hc⟩
  have h1 : (1 : ℕ) ∈ Set.Icc 1 μ.cells.card := Set.mem_Icc.mpr ⟨le_refl 1, by omega⟩
  have h2 : (2 : ℕ) ∈ Set.Icc 1 μ.cells.card := Set.mem_Icc.mpr ⟨by norm_num, hn⟩
  obtain ⟨_, v1⟩ := cellOf_spec T (exists_cell_entry T h1)
  obtain ⟨_, v2⟩ := cellOf_spec T (exists_cell_entry T h2)
  rw [hcell_eq] at v1
  exact absurd (v1.symm.trans v2) (by norm_num)

/-- **`R_row ∪ R_col = SYT(μ)`** (as `Finset.univ`) — every tableau is in one class. -/
theorem rowClass_union_colClass (hn : 2 ≤ μ.cells.card) :
    rowClass μ ∪ colClass μ = Finset.univ := by
  rw [Finset.eq_univ_iff_forall]
  intro T
  rw [Finset.mem_union, rowClass, colClass, Finset.mem_filter, Finset.mem_filter]
  rcases sameRow12_or_sameCol12 T hn with h | h
  · exact Or.inl ⟨Finset.mem_univ _, h⟩
  · exact Or.inr ⟨Finset.mem_univ _, h⟩

/-- **`R_row` and `R_col` are disjoint** — no tableau is in both. -/
theorem disjoint_rowClass_colClass (hn : 2 ≤ μ.cells.card) :
    Disjoint (rowClass μ) (colClass μ) := by
  rw [Finset.disjoint_left]
  intro T hT1 hT2
  rw [rowClass, Finset.mem_filter] at hT1
  rw [colClass, Finset.mem_filter] at hT2
  exact not_sameRow12_and_sameCol12 T hn ⟨hT1.2, hT2.2⟩

/-- **The per-shape count** `2·|R_row| = #SYT(μ)` for a self-conjugate shape with
    `≥ 2` cells (`c_λ = #SYT(μ)/2`): the two σ₁ classes partition `SYT(μ)` and are
    equinumerous (`card_rowClass_eq_colClass`). No enumeration of tableaux. -/
theorem two_mul_card_rowClass_eq_card (h : μ.transpose = μ) (hn : 2 ≤ μ.cells.card) :
    2 * (rowClass μ).card = Fintype.card (StandardYoungTableau μ) := by
  have hsum : (rowClass μ).card + (colClass μ).card
      = Fintype.card (StandardYoungTableau μ) := by
    rw [← Finset.card_union_of_disjoint (disjoint_rowClass_colClass hn),
      rowClass_union_colClass hn, Finset.card_univ]
  rw [two_mul]
  nth_rewrite 2 [card_rowClass_eq_colClass h hn]
  exact hsum

/-- **`2·χ_λ(σ₁) = #SYT(μ)·h`** — the σ₁ seminormal character in closed form with the
    per-shape coefficient made explicit: `c_λ = #SYT(μ)/2`. Combines the character
    factorisation `2·χ = 2·|R_row|·h` with the count `2·|R_row| = #SYT(μ)`. Fully
    general over any `[Field R]`. -/
theorem two_mul_sigmaOneCharacter_eq_card (h : μ.transpose = μ) (hn : 2 ≤ μ.cells.card)
    {R : Type*} [Field R] (q hh : R) (hq : q ≠ 0) :
    (2 : R) * sigmaOneCharacter μ q hh
      = ((Fintype.card (StandardYoungTableau μ) : ℕ) : R) * hh := by
  rw [two_mul_sigmaOneCharacter h hn q hh hq, two_mul_card_rowClass_eq_card h hn]

/-! ### General generator `σ_i`: the diagonal class-count `|R_row^i| = |R_col^i|`

The `σ₁` results above hardcode the value pair `1, 2`. The diagonal half of
`fullCharacter_two_mul` — the equinumerosity of the same-row and same-column
classes — holds for **every** generator `σ_i` (value pair `i, i+1`), because
`cellOf_selfTranspose` swaps the row/column coordinate for *any* entry `k`, not
just `1, 2`. These generator-indexed versions supply the `hcard` hypothesis of
`fullCharacter_two_mul` for a general `σ_i` on a self-conjugate shape. -/

/-- Same-row predicate for the generator pair `(i, i+1)`. -/
def sameRowGen (i : ℕ) (T : StandardYoungTableau μ) : Prop :=
  (cellOf T i).1 = (cellOf T (i + 1)).1

/-- Same-column predicate for the generator pair `(i, i+1)`. -/
def sameColGen (i : ℕ) (T : StandardYoungTableau μ) : Prop :=
  (cellOf T i).2 = (cellOf T (i + 1)).2

/-- The same-row class `R_row^i ⊆ SYT(μ)` for generator `σ_i`. -/
noncomputable def rowClassGen (μ : YoungDiagram) (i : ℕ) :
    Finset (StandardYoungTableau μ) :=
  Finset.univ.filter (fun T => sameRowGen i T)

/-- The same-column class `R_col^i ⊆ SYT(μ)` for generator `σ_i`. -/
noncomputable def colClassGen (μ : YoungDiagram) (i : ℕ) :
    Finset (StandardYoungTableau μ) :=
  Finset.univ.filter (fun T => sameColGen i T)

/-- `selfTranspose` carries the same-row class of `σ_i` to the same-column class,
    provided `i, i+1` are both in the value range (`1 ≤ i`, `i+1 ≤ |μ|`). -/
theorem sameRowGen_selfTranspose (h : μ.transpose = μ) (i : ℕ)
    (hi : 1 ≤ i) (hi2 : i + 1 ≤ μ.cells.card) (T : StandardYoungTableau μ) :
    sameRowGen i (selfTranspose h T) ↔ sameColGen i T := by
  have ei : i ∈ Set.Icc 1 μ.cells.card := Set.mem_Icc.mpr ⟨hi, by omega⟩
  have ei1 : i + 1 ∈ Set.Icc 1 μ.cells.card := Set.mem_Icc.mpr ⟨by omega, hi2⟩
  have c1 := cellOf_selfTranspose h T (exists_cell_entry T ei)
  have c2 := cellOf_selfTranspose h T (exists_cell_entry T ei1)
  unfold sameRowGen sameColGen
  rw [c1, c2]
  simp only [Prod.fst_swap]

/-- `selfTranspose` carries the same-column class of `σ_i` to the same-row class. -/
theorem sameColGen_selfTranspose (h : μ.transpose = μ) (i : ℕ)
    (hi : 1 ≤ i) (hi2 : i + 1 ≤ μ.cells.card) (T : StandardYoungTableau μ) :
    sameColGen i (selfTranspose h T) ↔ sameRowGen i T := by
  have ei : i ∈ Set.Icc 1 μ.cells.card := Set.mem_Icc.mpr ⟨hi, by omega⟩
  have ei1 : i + 1 ∈ Set.Icc 1 μ.cells.card := Set.mem_Icc.mpr ⟨by omega, hi2⟩
  have c1 := cellOf_selfTranspose h T (exists_cell_entry T ei)
  have c2 := cellOf_selfTranspose h T (exists_cell_entry T ei1)
  unfold sameColGen sameRowGen
  rw [c1, c2]
  simp only [Prod.snd_swap]

/-- **The general-`σ_i` diagonal class-count identity** `|R_row^i| = |R_col^i|`.
    For a self-conjugate shape and any generator `σ_i` (`1 ≤ i`, `i+1 ≤ |μ|`), the
    same-row and same-column classes of the pair `i, i+1` are equinumerous — the
    conjugate transpose is the explicit bijection. This is the `hcard` input to
    `SeminormalWeight.fullCharacter_two_mul` for a general single generator. -/
theorem card_rowClassGen_eq_colClassGen (h : μ.transpose = μ) (i : ℕ)
    (hi : 1 ≤ i) (hi2 : i + 1 ≤ μ.cells.card) :
    (rowClassGen μ i).card = (colClassGen μ i).card := by
  apply card_row_eq_card_col (rowClassGen μ i) (colClassGen μ i) (selfTranspose h)
  · intro T hT
    rw [rowClassGen, Finset.mem_filter] at hT
    rw [colClassGen, Finset.mem_filter]
    exact ⟨Finset.mem_univ _, (sameColGen_selfTranspose h i hi hi2 T).mpr hT.2⟩
  · intro T hT
    rw [colClassGen, Finset.mem_filter] at hT
    rw [rowClassGen, Finset.mem_filter]
    exact ⟨Finset.mem_univ _, (sameRowGen_selfTranspose h i hi hi2 T).mpr hT.2⟩
  · exact selfTranspose_selfTranspose h

/-! ### General generator `σ_i`: the off-diagonal swap involution `τ`

The off-diagonal class `S_off^i` (`i, i+1` in different rows *and* different
columns) carries the fixed-point-free involution that `fullCharacter_two_mul`
consumes: the **value-swap** `i ↔ i+1`. Swapping the two values in a standard
tableau yields a standard tableau **iff** `i, i+1` are off-diagonal (the classical
elementary-transposition fact); the swap exchanges the cells of `i` and `i+1`, so
it negates the generator axial distance `ρ` (`axialDistance_antisymm`). -/

/-- The value transposition `i ↔ i+1` on `ℕ` (identity elsewhere). -/
def swapSucc (i k : ℕ) : ℕ := if k = i then i + 1 else if k = i + 1 then i else k

/-- `swapSucc i` is an involution. -/
theorem swapSucc_involutive (i k : ℕ) : swapSucc i (swapSucc i k) = k := by
  unfold swapSucc; split_ifs <;> omega

/-- `swapSucc i` preserves strict order except on the transposed pair: if `a < b`
    and `(a, b) ≠ (i, i+1)`, then `swapSucc i a < swapSucc i b`. -/
theorem swapSucc_lt (i : ℕ) {a b : ℕ} (hab : a < b) (hne : ¬(a = i ∧ b = i + 1)) :
    swapSucc i a < swapSucc i b := by
  unfold swapSucc; split_ifs <;> omega

/-- `swapSucc i` is a bijection of the value range `{1,…,n}` (it permutes `i, i+1`,
    both in range). -/
theorem swapSucc_bijOn_Icc (i n : ℕ) (hi : 1 ≤ i) (hi2 : i + 1 ≤ n) :
    Set.BijOn (swapSucc i) (Set.Icc 1 n) (Set.Icc 1 n) := by
  have hmaps : Set.MapsTo (swapSucc i) (Set.Icc 1 n) (Set.Icc 1 n) := by
    intro k hk
    rw [Set.mem_Icc] at hk ⊢
    unfold swapSucc; split_ifs <;> omega
  refine ⟨hmaps, ?_, ?_⟩
  · intro a _ b _ hab
    have := congrArg (swapSucc i) hab
    rwa [swapSucc_involutive, swapSucc_involutive] at this
  · intro k hk
    exact ⟨swapSucc i k, hmaps hk, swapSucc_involutive i k⟩

/-- **The value-swap `i ↔ i+1` as a semistandard tableau**, valid when `i, i+1` are
    off-diagonal. Weak rows / strict columns survive the swap because within any
    single row (resp. column) at most one of `i, i+1` appears (their cells differ in
    that coordinate), so the swap never inverts an adjacent comparison. -/
def swapSuccSsyt (T : StandardYoungTableau μ) (i : ℕ)
    (hrow : (cellOf T i).1 ≠ (cellOf T (i + 1)).1)
    (hcol : (cellOf T i).2 ≠ (cellOf T (i + 1)).2)
    (hi : 1 ≤ i) : SemistandardYoungTableau μ where
  entry a b := swapSucc i (T.entry a b)
  zeros' := fun {a b} h => by
    show swapSucc i (T.entry a b) = 0
    rw [show T.entry a b = 0 from T.toSsyt.zeros h]
    unfold swapSucc
    rw [if_neg (by omega : ¬ ((0 : ℕ) = i)), if_neg (by omega : ¬ ((0 : ℕ) = i + 1))]
  row_weak' := fun {r j1 j2} hj hcell => by
    show swapSucc i (T.entry r j1) ≤ swapSucc i (T.entry r j2)
    apply le_of_lt
    apply swapSucc_lt i (T.row_strict hj hcell)
    rintro ⟨e1, e2⟩
    have hj1cell : (r, j1) ∈ μ := μ.up_left_mem (le_refl r) (le_of_lt hj) hcell
    have hc1 : cellOf T i = (r, j1) :=
      cellOf_eq_of_entry T ((YoungDiagram.mem_cells _).mpr hj1cell) e1
    have hc2 : cellOf T (i + 1) = (r, j2) :=
      cellOf_eq_of_entry T ((YoungDiagram.mem_cells _).mpr hcell) e2
    exact absurd (by rw [hc1, hc2] : (cellOf T i).1 = (cellOf T (i + 1)).1) hrow
  col_strict' := fun {r1 r2 c} hr hcell => by
    show swapSucc i (T.entry r1 c) < swapSucc i (T.entry r2 c)
    apply swapSucc_lt i (T.toSsyt.col_strict hr hcell)
    rintro ⟨e1, e2⟩
    have hr1cell : (r1, c) ∈ μ := μ.up_left_mem (le_of_lt hr) (le_refl c) hcell
    have hc1 : cellOf T i = (r1, c) :=
      cellOf_eq_of_entry T ((YoungDiagram.mem_cells _).mpr hr1cell) e1
    have hc2 : cellOf T (i + 1) = (r2, c) :=
      cellOf_eq_of_entry T ((YoungDiagram.mem_cells _).mpr hcell) e2
    exact absurd (by rw [hc1, hc2] : (cellOf T i).2 = (cellOf T (i + 1)).2) hcol

/-- **The value-swap `i ↔ i+1` as a standard tableau** (off-diagonal `i, i+1`). The
    filling stays bijective: `swapSucc i` permutes the value range `{1,…,|μ|}`. -/
def swapSuccSYT (T : StandardYoungTableau μ) (i : ℕ)
    (hrow : (cellOf T i).1 ≠ (cellOf T (i + 1)).1)
    (hcol : (cellOf T i).2 ≠ (cellOf T (i + 1)).2)
    (hi : 1 ≤ i) (hi2 : i + 1 ≤ μ.cells.card) : StandardYoungTableau μ where
  toSsyt := swapSuccSsyt T i hrow hcol hi
  bijOn := by
    have hfun : (fun c : ℕ × ℕ => (swapSuccSsyt T i hrow hcol hi).entry c.1 c.2)
        = swapSucc i ∘ (fun c : ℕ × ℕ => T.toSsyt.entry c.1 c.2) := by funext c; rfl
    rw [hfun]
    exact (swapSucc_bijOn_Icc i μ.cells.card hi hi2).comp T.bijOn

/-- The value-swap sends the cell of `i` to the cell of `i+1`. -/
theorem cellOf_swapSuccSYT_i (T : StandardYoungTableau μ) (i : ℕ)
    (hrow : (cellOf T i).1 ≠ (cellOf T (i + 1)).1)
    (hcol : (cellOf T i).2 ≠ (cellOf T (i + 1)).2)
    (hi : 1 ≤ i) (hi2 : i + 1 ≤ μ.cells.card) :
    cellOf (swapSuccSYT T i hrow hcol hi hi2) i = cellOf T (i + 1) := by
  have ei1 : (i + 1) ∈ Set.Icc 1 μ.cells.card := Set.mem_Icc.mpr ⟨by omega, hi2⟩
  obtain ⟨hmem, hval⟩ := cellOf_spec T (exists_cell_entry T ei1)
  apply cellOf_eq_of_entry _ hmem
  show swapSucc i (T.entry (cellOf T (i + 1)).1 (cellOf T (i + 1)).2) = i
  rw [hval]; unfold swapSucc; split_ifs <;> omega

/-- The value-swap sends the cell of `i+1` to the cell of `i`. -/
theorem cellOf_swapSuccSYT_i1 (T : StandardYoungTableau μ) (i : ℕ)
    (hrow : (cellOf T i).1 ≠ (cellOf T (i + 1)).1)
    (hcol : (cellOf T i).2 ≠ (cellOf T (i + 1)).2)
    (hi : 1 ≤ i) (hi2 : i + 1 ≤ μ.cells.card) :
    cellOf (swapSuccSYT T i hrow hcol hi hi2) (i + 1) = cellOf T i := by
  have ei : i ∈ Set.Icc 1 μ.cells.card := Set.mem_Icc.mpr ⟨hi, by omega⟩
  obtain ⟨hmem, hval⟩ := cellOf_spec T (exists_cell_entry T ei)
  apply cellOf_eq_of_entry _ hmem
  show swapSucc i (T.entry (cellOf T i).1 (cellOf T i).2) = i + 1
  rw [hval]; unfold swapSucc; split_ifs <;> omega

/-- **The value-swap negates the generator axial distance** `ρ`: it exchanges the
    cells of `i` and `i+1`, and `axialDistance` is antisymmetric. This is the
    `ρ(τ t) = −ρ t` hypothesis of `SeminormalWeight.two_mul_characterSum_eq`. -/
theorem generatorRho_swapSuccSYT (T : StandardYoungTableau μ) (i : ℕ)
    (hrow : (cellOf T i).1 ≠ (cellOf T (i + 1)).1)
    (hcol : (cellOf T i).2 ≠ (cellOf T (i + 1)).2)
    (hi : 1 ≤ i) (hi2 : i + 1 ≤ μ.cells.card) :
    generatorRho (swapSuccSYT T i hrow hcol hi hi2) i = - generatorRho T i := by
  unfold generatorRho
  rw [cellOf_swapSuccSYT_i, cellOf_swapSuccSYT_i1]
  exact axialDistance_antisymm _ _

end Closure

end QOU.BraidKnot.SeminormalCharacterConnector
