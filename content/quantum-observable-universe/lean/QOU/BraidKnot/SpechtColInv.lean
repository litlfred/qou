import QOU.BraidKnot.Specht

/-!
# QOU.BraidKnot.SpechtColInv — the column-inversion count and its swap-decrease law

A `μ`-tableau is **column-monotone** when, in each column, the labels increase
going down the rows.  This file provides the `ℕ`-measure that detects and
strictly decreases towards column-monotonicity under a single same-column swap:
the **column-inversion count**

> `colInv t = #{ (l, l') : l < l', l, l' in the same column, but row l' < row l }`.

These are exactly the ordered label-pairs sitting in one column "out of order"
(the smaller-indexed label sits in a *lower* row, i.e. has a larger row index).

## What is proved sorry-free here

* `colInv t` — the column-inversion count.
* `colInv_eq_zero_iff_colMono` — `colInv t = 0` iff `t` is column-monotone.
* `exists_colInv_of_ne_zero` — a nonzero count exhibits a genuine inverted pair.
* `swap_mem_colStab_of_sameCol` — swapping two same-column labels preserves the
  column pattern, hence lies in `colStab t`.
* `eq_of_rowCol_eq` / `rowPattern_ne_of_sameCol` — cells are pinned by
  `(row, column)`; distinct same-column labels occupy distinct rows.
* `colInv_swap_lt` — **the key lemma.** Swapping a same-column inverted pair
  `(a, b)` occupying *adjacent rows* strictly decreases `colInv`:
  `colInv (Equiv.swap a b • t) < colInv t`.

### On the key lemma's hypotheses

The key lemma takes four hypotheses on the pair `(a, b)`:

* `colPattern t a = colPattern t b` — same column;
* `(a : ℕ) < (b : ℕ)` — index order;
* `rowPattern t b < rowPattern t a` — an inversion (smaller label sits lower);
* `rowPattern t a = rowPattern t b + 1` — **adjacent rows**.

The adjacency hypothesis is genuinely needed (and is what a column bubble-sort
caller always supplies).  Without it, a swap of a *non-adjacent* same-column
inverted pair can *create* new inversions against the labels lying between the two
swapped rows, and `colInv` need not decrease.  Adjacency keeps every third
same-column label's row outside the swapped two-row block `{row b, row b + 1}`
(rows in a column are injective, `rowPattern_ne_of_sameCol`), so no third pair is
reordered: the swap removes exactly the one inversion `(a, b)` and creates none.
The proof packages this as the set identity
`colInvSet t = insert (a, b) (colInvSet s)` (with `(a, b) ∉ colInvSet s`), whence
`colInv t = colInv s + 1`.

All sorry-free; reuses only the proved `Specht` tableau API.

## References
- [sagan2001] Sagan, *The Symmetric Group*, §2.5 (column-standardisation /
  straightening of tableaux).
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtColInv

open QOU.BraidKnot.Specht

variable {μ : YoungDiagram}

/-! ## 1. The column-inversion count -/

/-- The set of **column inversions** of `t`: ordered pairs `(p, q)` of labels with
`p < q`, in the same column (`colPattern t p = colPattern t q`), whose rows are
*out of order* (`rowPattern t q < rowPattern t p`, i.e. the smaller label `p`
sits in a strictly lower row than the larger label `q`). -/
def colInvSet (t : Tableau μ) : Finset (Fin (nOf μ) × Fin (nOf μ)) :=
  Finset.univ.filter (fun p : Fin (nOf μ) × Fin (nOf μ) =>
    (p.1 : ℕ) < (p.2 : ℕ) ∧ colPattern t p.1 = colPattern t p.2 ∧
      rowPattern t p.2 < rowPattern t p.1)

/-- **The column-inversion count.** `colInv t` is the number of column-inverted
ordered label pairs of `t`. -/
def colInv (t : Tableau μ) : ℕ := (colInvSet t).card

@[simp] theorem mem_colInvSet {t : Tableau μ} {p : Fin (nOf μ) × Fin (nOf μ)} :
    p ∈ colInvSet t ↔
      (p.1 : ℕ) < (p.2 : ℕ) ∧ colPattern t p.1 = colPattern t p.2 ∧
        rowPattern t p.2 < rowPattern t p.1 := by
  simp [colInvSet]

/-! ## 2. Column-monotonicity ⟺ no inversions -/

/-- A tableau is **column-monotone** when, within each column, labels increase
down the rows: for any two same-column labels, the smaller-indexed one sits in a
strictly higher (smaller-index) row. -/
def ColMono (t : Tableau μ) : Prop :=
  ∀ l l' : Fin (nOf μ), colPattern t l = colPattern t l' → (l : ℕ) < (l' : ℕ) →
    rowPattern t l < rowPattern t l'

/-- **Column-monotone ⟺ no column inversions.** A tableau has zero column
inversions iff it is column-monotone. -/
theorem colInv_eq_zero_iff_colMono (t : Tableau μ) :
    colInv t = 0 ↔ ColMono t := by
  classical
  rw [colInv, Finset.card_eq_zero, colInvSet, Finset.filter_eq_empty_iff]
  constructor
  · intro hempty l l' hcol hlt
    -- No inversion `(l, l')`; since rows along a column are distinct, conclude `<`.
    by_contra hge
    push_neg at hge
    -- `rowPattern t l' ≤ rowPattern t l`.  Two distinct labels in the same column
    -- have distinct rows, so in fact `rowPattern t l' < rowPattern t l` — an
    -- inversion, contradicting emptiness.
    have hrowne : rowPattern t l ≠ rowPattern t l' := by
      intro hrow
      -- Same row AND same column ⟹ same cell ⟹ same label (t injective), contra l<l'.
      have hcell : (t l : ℕ × ℕ) = (t l' : ℕ × ℕ) :=
        Prod.ext (hrow : (t l : ℕ × ℕ).1 = (t l' : ℕ × ℕ).1)
          (hcol : (t l : ℕ × ℕ).2 = (t l' : ℕ × ℕ).2)
      have hsub : t l = t l' := Subtype.ext hcell
      have : l = l' := t.injective hsub
      omega
    have hstrict : rowPattern t l' < rowPattern t l := lt_of_le_of_ne hge (Ne.symm hrowne)
    exact hempty (x := (l, l')) (Finset.mem_univ _) ⟨hlt, hcol, hstrict⟩
  · intro hmono p _ hinv
    obtain ⟨hlt, hcol, hrow⟩ := hinv
    exact absurd (hmono p.1 p.2 hcol hlt) (not_lt.mpr (le_of_lt hrow))

/-- **An inversion exists when the count is nonzero.** If `colInv t ≠ 0` then there
is a genuine column-inverted pair `(l, l')`. -/
theorem exists_colInv_of_ne_zero {t : Tableau μ} (h : colInv t ≠ 0) :
    ∃ l l' : Fin (nOf μ), colPattern t l = colPattern t l' ∧ (l : ℕ) < (l' : ℕ) ∧
      rowPattern t l' < rowPattern t l := by
  classical
  have hpos : 0 < (colInvSet t).card := Nat.pos_of_ne_zero h
  obtain ⟨p, hp⟩ := Finset.card_pos.mp hpos
  rw [mem_colInvSet] at hp
  exact ⟨p.1, p.2, hp.2.1, hp.1, hp.2.2⟩

/-! ## 3. Swapping a same-column pair stays in the column stabilizer -/

/-- **Swapping two same-column labels preserves the column pattern.** If `a` and
`b` lie in the same column of `t`, then `Equiv.swap a b ∈ colStab t`. -/
theorem swap_mem_colStab_of_sameCol {t : Tableau μ} {a b : Fin (nOf μ)}
    (hcol : colPattern t a = colPattern t b) :
    Equiv.swap a b ∈ colStab t := by
  rw [mem_colStab]
  funext l
  rw [arrow_smul_apply, Equiv.symm_swap]
  rcases eq_or_ne l a with rfl | hla
  · rw [Equiv.swap_apply_left]; exact hcol.symm
  · rcases eq_or_ne l b with rfl | hlb
    · rw [Equiv.swap_apply_right]; exact hcol
    · rw [Equiv.swap_apply_of_ne_of_ne hla hlb]

/-! ## 4. Pattern behaviour under a same-column swap -/

/-- **Row pattern after a swap.** `rowPattern (Equiv.swap a b • t) l =
rowPattern t ((Equiv.swap a b) l)` — the swap is an involution so `.symm`
equals itself. -/
theorem rowPattern_swap_smul (t : Tableau μ) (a b l : Fin (nOf μ)) :
    rowPattern (Equiv.swap a b • t) l = rowPattern t (Equiv.swap a b l) := by
  rw [rowPattern, Tableau.smul_apply, Equiv.symm_swap, rowPattern]

/-- **Column pattern after a swap.** Same statement, for the column. -/
theorem colPattern_swap_smul (t : Tableau μ) (a b l : Fin (nOf μ)) :
    colPattern (Equiv.swap a b • t) l = colPattern t (Equiv.swap a b l) := by
  rw [colPattern, Tableau.smul_apply, Equiv.symm_swap, colPattern]

/-! ## 5. Distinct same-column labels have distinct rows -/

/-- **Cells are determined by (row, column).** Two labels with equal row *and*
column patterns are equal — both sit in the same cell, and `t` is a bijection. -/
theorem eq_of_rowCol_eq {t : Tableau μ} {x y : Fin (nOf μ)}
    (hrow : rowPattern t x = rowPattern t y) (hcol : colPattern t x = colPattern t y) :
    x = y := by
  have hcell : (t x : ℕ × ℕ) = (t y : ℕ × ℕ) :=
    Prod.ext (hrow : (t x : ℕ × ℕ).1 = (t y : ℕ × ℕ).1)
      (hcol : (t x : ℕ × ℕ).2 = (t y : ℕ × ℕ).2)
  exact t.injective (Subtype.ext hcell)

/-- **Distinct same-column labels occupy distinct rows.** -/
theorem rowPattern_ne_of_sameCol {t : Tableau μ} {x y : Fin (nOf μ)}
    (hcol : colPattern t x = colPattern t y) (hxy : x ≠ y) :
    rowPattern t x ≠ rowPattern t y :=
  fun hrow => hxy (eq_of_rowCol_eq hrow hcol)

/-! ## 6. The key lemma: an adjacent same-column swap strictly decreases `colInv` -/

/-- **The key lemma.** Let `a < b` be a same-column inverted pair of `t` occupying
*adjacent* rows (`colPattern t a = colPattern t b`, `(a : ℕ) < b`,
`rowPattern t b < rowPattern t a`, and `rowPattern t a = rowPattern t b + 1`).
Then swapping `a` and `b` strictly decreases the column-inversion count:

`colInv (Equiv.swap a b • t) < colInv t`.

The proof shows the set identity `colInvSet t = insert (a, b) (colInvSet s)` with
`(a, b) ∉ colInvSet s`, whence `colInv t = colInv s + 1`.  Concretely, for every
ordered pair `(x, y)`:

* a pair disjoint from `{a, b}` has identical row/column data in `s` and `t`, so
  its inversion status is unchanged;
* a pair `{a, l}` or `{b, l}` (third label `l` in the column) is unchanged because
  `l`'s row lies *outside* the two-row block `{row b, row b + 1}` occupied by
  `a, b` (rows in a column are injective), so swapping those two rows does not
  reorder `l` against either `a` or `b`;
* the pair `(a, b)` itself is an inversion of `t` (`hrow`) but **not** of `s`
  (its rows are exchanged): it is the single element by which the two sets differ.

The adjacency hypothesis is exactly what keeps every third label's row outside
the swapped block, guaranteeing *no new inversions* are created. -/
theorem colInv_swap_lt {t : Tableau μ} {a b : Fin (nOf μ)}
    (hcol : colPattern t a = colPattern t b)
    (hab : (a : ℕ) < (b : ℕ))
    (hrow : rowPattern t b < rowPattern t a)
    (hadj : rowPattern t a = rowPattern t b + 1) :
    colInv (Equiv.swap a b • t) < colInv t := by
  classical
  set κ := Equiv.swap a b with hκ
  set s := κ • t with hs
  -- Patterns of `s` expressed through `κ` and `t`.
  have hcolS : ∀ l, colPattern s l = colPattern t (κ l) := fun l => by
    rw [hs]; exact colPattern_swap_smul t a b l
  have hrowS : ∀ l, rowPattern s l = rowPattern t (κ l) := fun l => by
    rw [hs]; exact rowPattern_swap_smul t a b l
  -- `κ` swaps `a, b` and fixes everything else.
  have hκa : κ a = b := by rw [hκ]; exact Equiv.swap_apply_left a b
  have hκb : κ b = a := by rw [hκ]; exact Equiv.swap_apply_right a b
  have hκfix : ∀ l, l ≠ a → l ≠ b → κ l = l := fun l hla hlb => by
    rw [hκ]; exact Equiv.swap_apply_of_ne_of_ne hla hlb
  have hne : a ≠ b := fun h => by rw [h] at hab; exact (lt_irrefl _ hab)
  -- Rename the two adjacent rows: `R = row b`, `R + 1 = row a`.
  set R := rowPattern t b with hR
  have hrowa : rowPattern t a = R + 1 := hadj
  -- A third label in the column avoids both rows `R` and `R + 1`.
  have hthirdRow : ∀ l, colPattern t l = colPattern t a → l ≠ a → l ≠ b →
      rowPattern t l ≠ R ∧ rowPattern t l ≠ R + 1 := by
    intro l hlc hla hlb
    have hbc : colPattern t l = colPattern t b := hlc.trans hcol
    refine ⟨?_, ?_⟩
    · -- `≠ R = row b`
      have := rowPattern_ne_of_sameCol hbc hlb
      simpa [hR] using this
    · -- `≠ R + 1 = row a`
      have := rowPattern_ne_of_sameCol hlc hla
      rw [hrowa] at this; exact this
  -- `(a, b)` is an inversion of `t`.
  have habT : (a, b) ∈ colInvSet t := by rw [mem_colInvSet]; exact ⟨hab, hcol, hrow⟩
  -- `(a, b)` is NOT an inversion of `s`: its rows are exchanged.
  have hab_not_s : (a, b) ∉ colInvSet s := by
    rw [mem_colInvSet]; rintro ⟨_, _, hrs⟩
    rw [hrowS, hrowS, hκa, hκb] at hrs  -- rowPattern t a < rowPattern t b
    omega
  -- Per-pair transport.  For a fixed ordered pair `(x, y)` with `x < y`, the `t`-
  -- and `s`-inversion predicates agree, EXCEPT the pair `(a, b)` (inversion of `t`,
  -- not of `s`).  We package this as the membership equivalence
  -- `colInvSet t = insert (a, b) (colInvSet s)`.
  have hset : colInvSet t = insert (a, b) (colInvSet s) := by
    ext p
    obtain ⟨x, y⟩ := p
    rw [Finset.mem_insert, mem_colInvSet, mem_colInvSet]
    simp only [hcolS, hrowS]
    -- Abbreviations: the `t`-predicate `Pt` and `s`-predicate `Ps` beyond the index.
    -- We split on which of `x, y` are in `{a, b}`.  In every "third-label" sub-case
    -- the involved label's row avoids `{R, R+1}`, so `omega` finishes the row part.
    -- `a, b` are kept as canonical names; case-equalities are pushed by `rw`, not
    -- `subst`, so that `κ = swap a b` and the lemmas `hκa, hκb, hcol, …` stay valid.
    constructor
    · rintro ⟨hxy, hcxy, hrxy⟩
      by_cases hxa : x = a
      · -- x = a (so y ≠ a as a < y).
        rw [hxa] at hxy hcxy hrxy ⊢
        have hya : y ≠ a := fun h => by rw [h] at hxy; exact (lt_irrefl _ hxy)
        by_cases hyb : y = b
        · -- (a, b): left disjunct.
          rw [hyb]; exact Or.inl rfl
        · -- (a, third): survives in `s`.  κ a = b, κ y = y.
          have hyc : colPattern t y = colPattern t a := hcxy.symm
          obtain ⟨hyR, hyR1⟩ := hthirdRow y hyc hya hyb
          refine Or.inr ⟨hxy, ?_, ?_⟩
          · rw [hκa, hκfix y hya hyb, ← hcol]; exact hcxy
          · rw [hκa, hκfix y hya hyb]
            -- goal: rowPattern t y < rowPattern t b = R; from hrxy: y < rowPattern t a = R+1
            rw [hrowa] at hrxy; rw [← hR]; omega
      · by_cases hxb : x = b
        · -- x = b (so y ≠ b, y ≠ a since a < b < y).
          rw [hxb] at hxy hcxy hrxy ⊢
          have hyb : y ≠ b := fun h => by rw [h] at hxy; exact (lt_irrefl _ hxy)
          have hya : y ≠ a := fun h => by rw [h] at hxy; omega
          -- hcxy : colPattern t b = colPattern t y.
          have hyc : colPattern t y = colPattern t a := (hcol.trans hcxy).symm
          obtain ⟨hyR, hyR1⟩ := hthirdRow y hyc hya hyb
          refine Or.inr ⟨hxy, ?_, ?_⟩
          · rw [hκb, hκfix y hya hyb]; exact hcol.trans hcxy
          · rw [hκb, hκfix y hya hyb]; rw [← hR] at hrxy; rw [hrowa]; omega
        · -- x ∉ {a, b}: κ x = x.
          refine Or.inr ⟨hxy, ?_, ?_⟩
          · by_cases hya : y = a
            · rw [hya] at hcxy ⊢; rw [hκfix x hxa hxb, hκa, ← hcol]; exact hcxy
            · by_cases hyb : y = b
              · rw [hyb] at hcxy ⊢; rw [hκfix x hxa hxb, hκb]; exact hcxy.trans hcol.symm
              · rw [hκfix x hxa hxb, hκfix y hya hyb]; exact hcxy
          · -- row part.
            by_cases hya : y = a
            · rw [hya] at hcxy hrxy ⊢
              have hxc : colPattern t x = colPattern t a := hcxy
              obtain ⟨hxR, hxR1⟩ := hthirdRow x hxc hxa hxb
              rw [hκfix x hxa hxb, hκa]; rw [hrowa] at hrxy; rw [← hR]; omega
            · by_cases hyb : y = b
              · rw [hyb] at hcxy hrxy ⊢
                have hxc : colPattern t x = colPattern t a := by rw [hcol]; exact hcxy
                obtain ⟨hxR, hxR1⟩ := hthirdRow x hxc hxa hxb
                rw [hκfix x hxa hxb, hκb]; rw [← hR] at hrxy; rw [hrowa]; omega
              · -- both third: κ trivial, predicate identical; row goal is `hrxy`.
                rw [hκfix x hxa hxb, hκfix y hya hyb]; exact hrxy
    · rintro (hpe | ⟨hxy, hcxy, hrxy⟩)
      · rw [Prod.mk.injEq] at hpe
        obtain ⟨rfl, rfl⟩ := hpe
        exact ⟨hab, hcol, hrow⟩
      · refine ⟨hxy, ?_, ?_⟩
        · -- column, back through κ.
          by_cases hxa : x = a
          · rw [hxa] at hxy hcxy ⊢
            have hya : y ≠ a := fun h => by rw [h] at hxy; exact (lt_irrefl _ hxy)
            by_cases hyb : y = b
            · rw [hyb]; exact hcol
            · rw [hκa, hκfix y hya hyb, ← hcol] at hcxy; exact hcxy
          · by_cases hxb : x = b
            · rw [hxb] at hxy hcxy ⊢
              have hyb : y ≠ b := fun h => by rw [h] at hxy; exact (lt_irrefl _ hxy)
              have hya : y ≠ a := fun h => by rw [h] at hxy; omega
              rw [hκb, hκfix y hya hyb] at hcxy; rw [← hcol]; exact hcxy
            · by_cases hya : y = a
              · rw [hya] at hcxy ⊢; rw [hκfix x hxa hxb, hκa] at hcxy; rw [hcol]; exact hcxy
              · by_cases hyb : y = b
                · rw [hyb] at hcxy ⊢; rw [hκfix x hxa hxb, hκb] at hcxy
                  exact hcxy.trans hcol
                · rw [hκfix x hxa hxb, hκfix y hya hyb] at hcxy; exact hcxy
        · -- row, back through κ.
          by_cases hxa : x = a
          · rw [hxa] at hxy hcxy hrxy ⊢
            have hya : y ≠ a := fun h => by rw [h] at hxy; exact (lt_irrefl _ hxy)
            by_cases hyb : y = b
            · rw [hyb]; exact hrow
            · have hyc : colPattern t y = colPattern t a := by
                rw [hκa, hκfix y hya hyb, ← hcol] at hcxy; exact hcxy.symm
              obtain ⟨hyR, hyR1⟩ := hthirdRow y hyc hya hyb
              rw [hκa, hκfix y hya hyb, ← hR] at hrxy; rw [hrowa]; omega
          · by_cases hxb : x = b
            · rw [hxb] at hxy hcxy hrxy ⊢
              have hyb : y ≠ b := fun h => by rw [h] at hxy; exact (lt_irrefl _ hxy)
              have hya : y ≠ a := fun h => by rw [h] at hxy; omega
              have hyc : colPattern t y = colPattern t a := by
                rw [hκb, hκfix y hya hyb] at hcxy; exact hcxy.symm
              obtain ⟨hyR, hyR1⟩ := hthirdRow y hyc hya hyb
              rw [hκb, hκfix y hya hyb, hrowa] at hrxy; rw [← hR]; omega
            · by_cases hya : y = a
              · rw [hya] at hcxy hrxy ⊢
                have hxc : colPattern t x = colPattern t a := by
                  rw [hκfix x hxa hxb, hκa] at hcxy; exact hcxy.trans hcol.symm
                obtain ⟨hxR, hxR1⟩ := hthirdRow x hxc hxa hxb
                -- hrxy : rowPattern t b < rowPattern t x;  goal : rowPattern t a < rowPattern t x
                rw [hκfix x hxa hxb, hκa, ← hR] at hrxy; rw [hrowa]; omega
              · by_cases hyb : y = b
                · rw [hyb] at hcxy hrxy ⊢
                  have hxc : colPattern t x = colPattern t a := by
                    rw [hκfix x hxa hxb, hκb] at hcxy; exact hcxy
                  obtain ⟨hxR, hxR1⟩ := hthirdRow x hxc hxa hxb
                  -- hrxy : rowPattern t a < rowPattern t x;  goal : rowPattern t b < rowPattern t x
                  rw [hκfix x hxa hxb, hκb, hrowa] at hrxy; rw [← hR]; omega
                · rw [hκfix x hxa hxb, hκfix y hya hyb] at hrxy; exact hrxy
  -- Conclude the count identity.
  rw [colInv, colInv, hset, Finset.card_insert_of_notMem hab_not_s]
  exact Nat.lt_succ_self _

end QOU.BraidKnot.SpechtColInv
