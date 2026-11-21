import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Data.Fintype.Pi
import Mathlib.Algebra.BigOperators.Fin

/-!
# Littlewood–Richardson coefficients

`lrCoeff λ μ ν` is the Littlewood–Richardson coefficient `c^ν_{λ μ}`, defined
combinatorially as the number of **LR tableaux** of skew shape `ν / λ` and
content `μ` (Macdonald, *Symmetric Functions and Hall Polynomials*, I.9;
Fulton, *Young Tableaux*, §5.2):

* a filling `T` of the cells of `ν \ λ` by row indices of `μ`
  (values in `Fin μ.card`, which is large enough for every row index);
* **semistandard**: weakly increasing along rows, strictly increasing down
  columns;
* **content `μ`**: the value `i` occurs exactly `μ.rowLen i` times
  (`(μ.row i).card` times);
* **lattice (Yamanouchi) reverse reading word**: reading the rows top to
  bottom, each row right to left, every prefix contains at least as many
  `i`s as `(i+1)`s.

The coefficient is set to `0` unless `λ ≤ ν`: a filling of `ν \ λ` when
`λ ⊄ ν` is not a skew tableau (e.g. `λ = (2)`, `ν = (1,1)`, `μ = (1)` would
otherwise count `1`; `lrCoeff_two_one_oneOne` checks the guard).

Everything is a decidable predicate on a `Fintype`, so small coefficients are
evaluated by `decide` in the kernel (no `native_decide`):
`c^{(3,2,1)}_{(2,1),(2,1)} = 2` is `lrCoeff_d21_d21_d321`.

## Main results

* `lrCoeff_eq_zero_of_not_le`, `card_eq_of_lrCoeff_ne_zero` — the support
  condition `λ ≤ ν`, `|ν| = |λ| + |μ|`.
* `lrCoeff_bot_right` — `c^ν_{λ ∅} = δ_{ν λ}`.
* `rowSum`, `lrCoeff_rowSum_pos` — `ν = λ + μ` (row lengths added) always
  occurs: `c^{λ+μ}_{λ μ} ≥ 1`, witnessed by the tableau filling row `i` with
  `i`.

## Not proved here

The symmetries `c^ν_{λμ} = c^ν_{μλ}` and `c^{ν'}_{λ'μ'} = c^ν_{λμ}` are
standard theorems of LR theory and are **not** formalised in this file.

-- Ref: [macdonald1995] Macdonald, Symmetric Functions and Hall Polynomials, 2nd ed., OUP 1995, I.9
-/

namespace QOU.Mathlib

open Finset

/-- The cells of the skew shape `ν / λ` (as a set difference; it is a skew
    shape when `λ ≤ ν`). -/
def skewCells (nu la : YoungDiagram) : Finset (ℕ × ℕ) := nu.cells \ la.cells

/-- A filling of `ν / λ` by row indices of `μ`. -/
abbrev LRFilling (la mu nu : YoungDiagram) : Type :=
  {c // c ∈ skewCells nu la} → Fin mu.card

/-- `readLE c d`: in the reverse reading order (rows top to bottom, each row
    right to left), `c` is read no later than `d`. -/
def readLE (c d : ℕ × ℕ) : Prop := c.1 < d.1 ∨ (c.1 = d.1 ∧ d.2 ≤ c.2)

instance : DecidableRel readLE := fun c d => by unfold readLE; infer_instance

/-- `T` is a **Littlewood–Richardson tableau** of shape `ν / λ` and content
    `μ`. -/
def IsLRTableau (la mu nu : YoungDiagram) (T : LRFilling la mu nu) : Prop :=
  -- rows weakly increase
  (∀ c d : {c // c ∈ skewCells nu la}, c.1.1 = d.1.1 → c.1.2 ≤ d.1.2 → T c ≤ T d) ∧
  -- columns strictly increase
  (∀ c d : {c // c ∈ skewCells nu la}, c.1.2 = d.1.2 → c.1.1 < d.1.1 → T c < T d) ∧
  -- content `μ`
  (∀ i : Fin mu.card, (univ.filter fun c => T c = i).card = (mu.row i).card) ∧
  -- the reverse reading word is a lattice word
  (∀ c : {c // c ∈ skewCells nu la}, ∀ i : Fin mu.card,
    (univ.filter fun d : {c // c ∈ skewCells nu la} =>
        readLE d.1 c.1 ∧ (T d : ℕ) = (i : ℕ) + 1).card ≤
      (univ.filter fun d : {c // c ∈ skewCells nu la} =>
        readLE d.1 c.1 ∧ (T d : ℕ) = (i : ℕ)).card)

instance (la mu nu : YoungDiagram) (T : LRFilling la mu nu) :
    Decidable (IsLRTableau la mu nu T) := by
  unfold IsLRTableau; infer_instance

/-- The **Littlewood–Richardson coefficient** `c^ν_{λ μ}`: the number of LR
    tableaux of shape `ν / λ` with content `μ`, and `0` unless `λ ≤ ν`. -/
def lrCoeff (la mu nu : YoungDiagram) : ℕ :=
  if la.cells ⊆ nu.cells then
    (univ.filter fun T : LRFilling la mu nu => IsLRTableau la mu nu T).card
  else 0

/-! ## Elementary facts about Young diagrams -/

/-- A cell's row index is below the number of cells. -/
theorem fst_lt_card {mu : YoungDiagram} {c : ℕ × ℕ} (hc : c ∈ mu) : c.1 < mu.card := by
  have hsub : (range (c.1 + 1)).image (fun k => (k, 0)) ⊆ mu.cells := by
    intro x hx
    simp only [mem_image, mem_range] at hx
    obtain ⟨k, hk, rfl⟩ := hx
    exact (YoungDiagram.mem_cells _).mpr
      (mu.up_left_mem (Nat.lt_succ_iff.mp hk) (Nat.zero_le _) hc)
  have := card_le_card hsub
  rw [card_image_of_injective _ (fun a b h => by simpa using h), card_range] at this
  exact this

/-- `(μ.row i).card = μ.rowLen i`. -/
theorem card_row (mu : YoungDiagram) (i : ℕ) : (mu.row i).card = mu.rowLen i := by
  rw [YoungDiagram.row_eq_prod, card_product, card_singleton, card_range, one_mul]

/-- The rows of `μ` partition its cells: `Σ_{i < |μ|} |row i| = |μ|`. -/
theorem sum_card_row (mu : YoungDiagram) :
    ∑ i : Fin mu.card, (mu.row i).card = mu.card := by
  rw [Fin.sum_univ_eq_sum_range (fun i => (mu.row i).card)]
  have h := card_eq_sum_card_fiberwise (s := mu.cells) (t := range mu.card)
    (f := fun c => c.1)
    (fun c hc => mem_range.mpr (fst_lt_card ((YoungDiagram.mem_cells _).mp hc)))
  simpa [YoungDiagram.row, YoungDiagram.card] using h.symm

/-- Rows of a nonempty diagram: `0 < μ.rowLen 0`. -/
theorem rowLen_zero_pos {mu : YoungDiagram} (h : 0 < mu.card) : 0 < mu.rowLen 0 := by
  obtain ⟨c, hc⟩ := card_pos.mp h
  have : ((0 : ℕ), (0 : ℕ)) ∈ mu :=
    mu.up_left_mem (Nat.zero_le _) (Nat.zero_le _) ((YoungDiagram.mem_cells _).mp hc)
  exact YoungDiagram.mem_iff_lt_rowLen.mp this

/-- `rowLen i ≤ |μ|`. -/
theorem rowLen_le_card (mu : YoungDiagram) (i : ℕ) : mu.rowLen i ≤ mu.card := by
  rw [← card_row]; exact card_le_card (filter_subset _ _)

/-- A nonempty row has index below the number of cells. -/
theorem lt_card_of_rowLen_pos {mu : YoungDiagram} {i : ℕ} (h : 0 < mu.rowLen i) :
    i < mu.card :=
  fst_lt_card (c := (i, 0)) (YoungDiagram.mem_iff_lt_rowLen.mpr h)

/-! ## Counting over subtypes -/

theorem card_filter_subtype {s : Finset (ℕ × ℕ)} (p : ℕ × ℕ → Prop) [DecidablePred p] :
    (univ.filter fun c : {c // c ∈ s} => p c.1).card = (s.filter p).card := by
  rw [← card_map (Function.Embedding.subtype _)]
  congr 1
  ext x
  constructor
  · intro hx
    obtain ⟨y, hy, rfl⟩ := mem_map.mp hx
    exact mem_filter.mpr ⟨y.2, (mem_filter.mp hy).2⟩
  · intro hx
    obtain ⟨h1, h2⟩ := mem_filter.mp hx
    exact mem_map.mpr ⟨⟨x, h1⟩, mem_filter.mpr ⟨mem_univ _, h2⟩, rfl⟩

/-! ## Support -/

/-- `c^ν_{λ μ} = 0` unless `λ ≤ ν`. -/
theorem lrCoeff_eq_zero_of_not_le {la mu nu : YoungDiagram} (h : ¬ la ≤ nu) :
    lrCoeff la mu nu = 0 := by
  rw [lrCoeff, if_neg (fun h' => h (YoungDiagram.cells_subset_iff.mp h'))]

/-- `c^ν_{λ μ} ≠ 0` forces `λ ≤ ν`. -/
theorem le_of_lrCoeff_ne_zero {la mu nu : YoungDiagram} (h : lrCoeff la mu nu ≠ 0) :
    la ≤ nu := by
  by_contra h'; exact h (lrCoeff_eq_zero_of_not_le h')

/-- An LR tableau of shape `ν / λ` and content `μ` forces `|ν| = |λ| + |μ|`. -/
theorem card_eq_of_isLRTableau {la mu nu : YoungDiagram} (hle : la.cells ⊆ nu.cells)
    (T : LRFilling la mu nu) (hT : IsLRTableau la mu nu T) :
    nu.card = la.card + mu.card := by
  have hfib := card_eq_sum_card_fiberwise (s := (univ : Finset {c // c ∈ skewCells nu la}))
    (t := (univ : Finset (Fin mu.card))) (f := T) (fun _ _ => mem_univ _)
  have hskew : (univ : Finset {c // c ∈ skewCells nu la}).card = nu.card - la.card := by
    rw [card_univ, Fintype.card_coe, skewCells, card_sdiff, inter_eq_left.mpr hle]
  have hsum : ∑ b : Fin mu.card,
      (univ.filter fun c : {c // c ∈ skewCells nu la} => T c = b).card = mu.card := by
    exact (sum_congr rfl (fun i _ => hT.2.2.1 i)).trans (sum_card_row mu)
  have hcard : la.card ≤ nu.card := card_le_card hle
  have : nu.card - la.card = mu.card := by rw [← hskew, hfib, hsum]
  omega

/-- `c^ν_{λ μ} ≠ 0` forces `|ν| = |λ| + |μ|`. -/
theorem card_eq_of_lrCoeff_ne_zero {la mu nu : YoungDiagram} (h : lrCoeff la mu nu ≠ 0) :
    nu.card = la.card + mu.card := by
  unfold lrCoeff at h
  split_ifs at h with hle
  · obtain ⟨T, hT⟩ := card_ne_zero.mp h
    exact card_eq_of_isLRTableau hle T (mem_filter.mp hT).2
  · exact absurd rfl h

/-- **Support of `c^ν_{λ μ}`**: it vanishes unless `λ ≤ ν` and
    `|ν| = |λ| + |μ|`. -/
theorem lrCoeff_eq_zero_of_not_support {la mu nu : YoungDiagram}
    (h : ¬ (la ≤ nu ∧ nu.card = la.card + mu.card)) : lrCoeff la mu nu = 0 := by
  by_contra h'
  exact h ⟨le_of_lrCoeff_ne_zero h', card_eq_of_lrCoeff_ne_zero h'⟩

/-! ## Empty content -/

theorem card_bot : (⊥ : YoungDiagram).card = 0 := by
  simp [YoungDiagram.card]

open scoped Classical in
/-- **`c^ν_{λ ∅} = δ_{ν λ}`.** -/
theorem lrCoeff_bot_right (la nu : YoungDiagram) :
    lrCoeff la ⊥ nu = if nu = la then 1 else 0 := by
  have hfin : (⊥ : YoungDiagram).card = 0 := card_bot
  by_cases hle : la.cells ⊆ nu.cells
  · by_cases heq : nu = la
    · subst heq
      rw [if_pos rfl, lrCoeff, if_pos hle]
      have hempty : ∀ c, c ∉ skewCells nu nu := fun c hc => by
        simp [skewCells] at hc
      have hall : ∀ T : LRFilling nu ⊥ nu, IsLRTableau nu ⊥ nu T := by
        intro T
        refine ⟨fun c => absurd c.2 (hempty _), fun c => absurd c.2 (hempty _),
          fun i => absurd i.2 (by omega), fun c => absurd c.2 (hempty _)⟩
      rw [filter_true_of_mem (fun T _ => hall T), card_univ, Fintype.card_fun]
      have : Fintype.card {c // c ∈ skewCells nu nu} = 0 :=
        Fintype.card_eq_zero_iff.mpr ⟨fun c => hempty _ c.2⟩
      rw [this, pow_zero]
    · rw [if_neg heq, lrCoeff, if_pos hle]
      have hne : (skewCells nu la).Nonempty := by
        rw [skewCells, sdiff_nonempty]
        intro hsub
        exact heq (YoungDiagram.ext (Subset.antisymm hsub hle))
      obtain ⟨c, hc⟩ := hne
      have : IsEmpty (LRFilling la ⊥ nu) :=
        ⟨fun T => absurd (T ⟨c, hc⟩).2 (by omega)⟩
      rw [univ_eq_empty, filter_empty, card_empty]
  · have heq : nu ≠ la := fun h => hle (h ▸ Subset.refl _)
    rw [if_neg heq, lrCoeff, if_neg hle]

/-! ## The row-sum constituent `λ + μ` -/

/-- The Young diagram `λ + μ` whose `i`-th row has length
    `λ.rowLen i + μ.rowLen i`. -/
def rowSum (la mu : YoungDiagram) : YoungDiagram where
  cells := ((range (la.card + mu.card)) ×ˢ (range (la.card + mu.card))).filter
    fun c => c.2 < la.rowLen c.1 + mu.rowLen c.1
  isLowerSet := by
    intro a b hba ha
    simp only [coe_filter, Set.mem_setOf_eq, mem_product, mem_range] at ha ⊢
    obtain ⟨⟨h1, h2⟩, h3⟩ := ha
    have hb1 : b.1 ≤ a.1 := hba.1
    have hb2 : b.2 ≤ a.2 := hba.2
    have := la.rowLen_anti _ _ hb1
    have := mu.rowLen_anti _ _ hb1
    refine ⟨⟨by omega, by omega⟩, by omega⟩

theorem mem_rowSum {la mu : YoungDiagram} {c : ℕ × ℕ} :
    c ∈ rowSum la mu ↔ c.2 < la.rowLen c.1 + mu.rowLen c.1 := by
  rw [← YoungDiagram.mem_cells]
  simp only [rowSum, mem_filter, mem_product, mem_range]
  constructor
  · exact fun h => h.2
  · intro h
    have h1 := rowLen_le_card la c.1
    have h2 := rowLen_le_card mu c.1
    refine ⟨⟨?_, by omega⟩, h⟩
    rcases Nat.eq_zero_or_pos (la.rowLen c.1) with h0 | h0
    · have : 0 < mu.rowLen c.1 := by omega
      have := lt_card_of_rowLen_pos this; omega
    · have := lt_card_of_rowLen_pos h0; omega

theorem rowLen_rowSum (la mu : YoungDiagram) (i : ℕ) :
    (rowSum la mu).rowLen i = la.rowLen i + mu.rowLen i :=
  eq_of_forall_lt_iff fun j => by
    rw [← YoungDiagram.mem_iff_lt_rowLen, mem_rowSum]

theorem le_rowSum (la mu : YoungDiagram) : la.cells ⊆ (rowSum la mu).cells := by
  intro c hc
  rw [YoungDiagram.mem_cells] at hc ⊢
  rw [mem_rowSum]
  have : c.2 < la.rowLen c.1 := YoungDiagram.mem_iff_lt_rowLen.mp hc
  omega

theorem mem_skewCells_rowSum {la mu : YoungDiagram} {c : ℕ × ℕ} :
    c ∈ skewCells (rowSum la mu) la ↔
      la.rowLen c.1 ≤ c.2 ∧ c.2 < la.rowLen c.1 + mu.rowLen c.1 := by
  rw [skewCells, mem_sdiff, YoungDiagram.mem_cells, YoungDiagram.mem_cells, mem_rowSum,
    YoungDiagram.mem_iff_lt_rowLen]
  omega

/-- The skew cells of `(λ + μ)/λ` in row `i` number `μ.rowLen i`. -/
theorem card_skewCells_rowSum_row (la mu : YoungDiagram) (i : ℕ) :
    ((skewCells (rowSum la mu) la).filter fun c => c.1 = i).card = mu.rowLen i := by
  have : ((skewCells (rowSum la mu) la).filter fun c => c.1 = i) =
      {i} ×ˢ Ico (la.rowLen i) (la.rowLen i + mu.rowLen i) := by
    ext ⟨a, b⟩
    simp only [mem_filter, mem_skewCells_rowSum, mem_product, mem_singleton, mem_Ico]
    constructor
    · rintro ⟨h, rfl⟩; exact ⟨rfl, h⟩
    · rintro ⟨rfl, h⟩; exact ⟨h, rfl⟩
  rw [this, card_product, card_singleton, Nat.card_Ico, one_mul]
  omega

/-- The **highest-weight tableau** of shape `(λ + μ)/λ`: each cell is filled
    with its row index. -/
def rowSumTableau (la mu : YoungDiagram) : LRFilling la mu (rowSum la mu) :=
  fun c => ⟨c.1.1, by
    have := (mem_skewCells_rowSum.mp c.2)
    exact lt_card_of_rowLen_pos (by omega)⟩

theorem isLRTableau_rowSumTableau (la mu : YoungDiagram) :
    IsLRTableau la mu (rowSum la mu) (rowSumTableau la mu) := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro c d h _
    exact Fin.le_iff_val_le_val.mpr (le_of_eq h)
  · intro c d _ h
    exact Fin.lt_iff_val_lt_val.mpr h
  · intro i
    rw [card_row]
    have := card_filter_subtype (s := skewCells (rowSum la mu) la) (fun c => c.1 = (i : ℕ))
    rw [← card_skewCells_rowSum_row la mu i, ← this]
    congr 1
    ext c
    simp [rowSumTableau, Fin.ext_iff]
  · intro c i
    simp only [rowSumTableau, Fin.val_mk]
    rw [card_filter_subtype (s := skewCells (rowSum la mu) la)
        (fun d => readLE d c.1 ∧ d.1 = (i : ℕ) + 1),
      card_filter_subtype (s := skewCells (rowSum la mu) la)
        (fun d => readLE d c.1 ∧ d.1 = (i : ℕ))]
    by_cases hci : c.1.1 ≤ (i : ℕ)
    · -- nothing in row `i + 1` is read before `c`
      have : ((skewCells (rowSum la mu) la).filter
          fun d => readLE d c.1 ∧ d.1 = (i : ℕ) + 1) = ∅ := by
        apply filter_false_of_mem
        rintro d _ ⟨hr, hd⟩
        rcases hr with hr | hr <;> omega
      rw [this, card_empty]; exact Nat.zero_le _
    · -- all of row `i` is read before `c`; row `i+1` has `μ_{i+1} ≤ μ_i` cells
      have hR : ((skewCells (rowSum la mu) la).filter
          fun d => readLE d c.1 ∧ d.1 = (i : ℕ)) =
          (skewCells (rowSum la mu) la).filter fun d => d.1 = (i : ℕ) := by
        apply filter_congr
        intro d _
        constructor
        · exact fun h => h.2
        · intro h; exact ⟨Or.inl (by omega), h⟩
      have hL : ((skewCells (rowSum la mu) la).filter
          fun d => readLE d c.1 ∧ d.1 = (i : ℕ) + 1) ⊆
          (skewCells (rowSum la mu) la).filter fun d => d.1 = (i : ℕ) + 1 :=
        monotone_filter_right _ (fun _ h => h.2)
      rw [hR]
      refine (card_le_card hL).trans ?_
      rw [card_skewCells_rowSum_row, card_skewCells_rowSum_row]
      exact mu.rowLen_anti _ _ (Nat.le_succ _)

/-- **`λ + μ` always occurs**: `c^{λ+μ}_{λ μ} ≥ 1`. -/
theorem lrCoeff_rowSum_pos (la mu : YoungDiagram) : 0 < lrCoeff la mu (rowSum la mu) := by
  rw [lrCoeff, if_pos (le_rowSum la mu)]
  exact card_pos.mpr ⟨rowSumTableau la mu,
    mem_filter.mpr ⟨mem_univ _, isLRTableau_rowSumTableau la mu⟩⟩

/-- `|λ + μ| = |λ| + |μ|`. -/
theorem card_rowSum (la mu : YoungDiagram) : (rowSum la mu).card = la.card + mu.card :=
  card_eq_of_lrCoeff_ne_zero (lrCoeff_rowSum_pos la mu).ne'

/-- For self-conjugate nonempty `λ`, `μ`, the diagram `λ + μ` is **not**
    self-conjugate: its first row has `λ₁ + μ₁` cells, its first column
    `max(λ₁, μ₁)` (since `λ' = λ`, the first column of `λ` has `λ₁` cells). -/
theorem rowSum_transpose_ne {la mu : YoungDiagram} (hla : la.transpose = la)
    (hmu : mu.transpose = mu) (hla0 : 0 < la.card) (hmu0 : 0 < mu.card) :
    (rowSum la mu).transpose ≠ rowSum la mu := by
  intro h
  have ha := rowLen_zero_pos hla0
  have hb := rowLen_zero_pos hmu0
  set k := la.rowLen 0 + mu.rowLen 0 - 1
  have hmem : ((0 : ℕ), k) ∈ rowSum la mu := by
    rw [mem_rowSum]; simp only; omega
  have h2 : (k, (0 : ℕ)) ∈ rowSum la mu := by
    rw [← h]; exact YoungDiagram.mem_transpose.mpr hmem
  have hk := mem_rowSum.mp h2
  simp only at hk
  have hcolLa : la.colLen 0 = la.rowLen 0 := by
    rw [← YoungDiagram.colLen_transpose, hla]
  have hcolMu : mu.colLen 0 = mu.rowLen 0 := by
    rw [← YoungDiagram.colLen_transpose, hmu]
  rcases Nat.eq_zero_or_pos (la.rowLen k) with h0 | h0
  · have hpos : 0 < mu.rowLen k := by omega
    have : k < mu.colLen 0 :=
      YoungDiagram.mem_iff_lt_colLen.mp (YoungDiagram.mem_iff_lt_rowLen.mpr hpos)
    omega
  · have : k < la.colLen 0 :=
      YoungDiagram.mem_iff_lt_colLen.mp (YoungDiagram.mem_iff_lt_rowLen.mpr h0)
    omega

/-! ## Concrete values (kernel `decide`) -/

/-- `(1)` -/
def yd1 : YoungDiagram := YoungDiagram.ofRowLens [1] (by decide)
/-- `(2)` -/
def yd2 : YoungDiagram := YoungDiagram.ofRowLens [2] (by decide)
/-- `(1,1)` -/
def yd11 : YoungDiagram := YoungDiagram.ofRowLens [1, 1] (by decide)
/-- `(2,1)` -/
def yd21 : YoungDiagram := YoungDiagram.ofRowLens [2, 1] (by decide)
/-- `(2,2)` -/
def yd22 : YoungDiagram := YoungDiagram.ofRowLens [2, 2] (by decide)
/-- `(3,2,1)` -/
def yd321 : YoungDiagram := YoungDiagram.ofRowLens [3, 2, 1] (by decide)

/-- `s₁ s₁ = s₂ + s₁₁`: `c^{(2)}_{(1)(1)} = 1`. -/
theorem lrCoeff_d1_d1_d2 : lrCoeff yd1 yd1 yd2 = 1 := by decide
/-- `c^{(1,1)}_{(1)(1)} = 1`. -/
theorem lrCoeff_d1_d1_d11 : lrCoeff yd1 yd1 yd11 = 1 := by decide
/-- Size mismatch: `c^{(2,1)}_{(1)(1)} = 0`. -/
theorem lrCoeff_d1_d1_d21 : lrCoeff yd1 yd1 yd21 = 0 := by decide
/-- `c^{(2,1)}_{(1)(1,1)} = 1`. -/
theorem lrCoeff_d1_d11_d21 : lrCoeff yd1 yd11 yd21 = 1 := by decide
/-- The lattice condition bites: `s₂ s₁₁ = s₃₁ + s₂₁₁`, so
    `c^{(2,2)}_{(2)(1,1)} = 0` (the only semistandard filling of
    `(2,2)/(2)` with content `(1,1)` reads `1 0`, not a lattice word). -/
theorem lrCoeff_d2_d11_d22 : lrCoeff yd2 yd11 yd22 = 0 := by decide
/-- `c^{(2,2)}_{(1,1)(1,1)} = 1`. -/
theorem lrCoeff_d11_d11_d22 : lrCoeff yd11 yd11 yd22 = 1 := by decide
/-- The `λ ≤ ν` guard bites: `c^{(1,1)}_{(2)(1)} = 0` although `(1,1) \ (2)`
    is a single cell that a content-`(1)` filling covers. -/
theorem lrCoeff_two_one_oneOne : lrCoeff yd2 yd1 yd11 = 0 := by decide
/-- **A coefficient above one**: `c^{(3,2,1)}_{(2,1)(2,1)} = 2`. -/
theorem lrCoeff_d21_d21_d321 : lrCoeff yd21 yd21 yd321 = 2 := by decide

end QOU.Mathlib
