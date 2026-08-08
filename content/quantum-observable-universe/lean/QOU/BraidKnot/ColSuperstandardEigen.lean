import QOU.BraidKnot.ColSuperstandardTableau

/-!
# QOU.BraidKnot.ColSuperstandardEigen — the OV eigen-equation, reduced to the annihilation

Assembles the Okounkov–Vershik eigen-equation for the **column-superstandard** tableau
`T₀`, reducing `JucysMurphy.seminormalVector_base_exists` (bean `sv8b`) to the single
remaining debt: the per-column Garnir **annihilation**.

`OVBaseSeminormalVector.jm_polytabloid_split` writes the JM action as

    X_s · e_t = (same-column count) · (−e_t) + (off-column Garnir sum).

Both summands are settled here for `T₀`:

* **`−i` half** — `ColSuperstandardTableau.sameColumn_count`: the same-column count is
  the **row index** of `s`'s cell.
* **`+j` half** — `offColumn_sum` (this file): the off-column sum is the **column index**
  of `s`'s cell times `e_{T₀}`.

giving `X_s · e_{T₀} = (col − row) · e_{T₀}` — and `col − row` is exactly the content of
`s`'s cell, which is the OV eigenvalue.

## What the `+j` half rests on

The off-column labels `{j < s : (j s) ∉ colStab T₀}` are, under column-major order,
exactly the labels of the columns strictly left of `s`'s (`offColumn_filter_eq`). For each
such column `c`, `OVBaseSeminormalVector.colGarnir_single_column_of_annihilation` collapses
the sum over that column's labels to a single `e_{T₀}` — **given** the full-group
annihilation `∑_{σ ∈ S_{C∪{s}}} sgn(σ)·σ·e_{T₀} = 0`. Summing over the `col(s)` columns
gives `col(s) · e_{T₀}`.

Two side conditions that the Garnir lemma needs are discharged outright here:
`s ∉ colLabels μ c` (its column differs), and `permFixingOutside_colLabels_le_colStab`
(permutations supported on one column preserve the column pattern).

## The remaining debt — stated honestly

`offColumn_sum` and `jm_eigen_colSuperstandard` **carry the annihilation as an explicit
hypothesis**; they are conditional theorems, not closures. Nothing here proves the
annihilation. Per bean `sv8b` that reduces to a *row collision*: for every
`ρ ∈ colStab T₀`, two distinct labels of `C ∪ {s}` share a row in `ρ • T₀`. The route is
`sum_sign_rep_polytabloid_eq_zero_of_family` + `mtab_sum_sign_smul_of_eq_zero`, and it is
being worked on PR #4702.

What this file buys: the annihilation is now the **only** thing between the corpus and the
base seminormal vector — the counting, the column decomposition, the stabiliser side
conditions and the assembly are all discharged.

-- Ref: [vershik-kerov1977] Vershik–Kerov, Young's seminormal form
-- Ref: [sagan2001] Sagan, The Symmetric Group §2.6 (Garnir relations), §3.1
-/

namespace QOU.BraidKnot.ColSuperstandardEigen

open QOU.BraidKnot QOU.BraidKnot.ColSuperstandardTableau

/-- The labels sitting in column `c` of the column-superstandard tableau. -/
noncomputable def colLabels (μ : YoungDiagram) (c : ℕ) : Finset (Fin (Specht.nOf μ)) :=
  Finset.univ.filter (fun l => (colSuperstandard μ l : ℕ × ℕ).2 = c)

theorem mem_colLabels (μ : YoungDiagram) (c : ℕ) (m : Fin (Specht.nOf μ)) :
    m ∈ colLabels μ c ↔ (colSuperstandard μ m : ℕ × ℕ).2 = c := by
  simp [colLabels]

/-- **The off-column labels are exactly those in strictly earlier columns.**

`j < s` splits by `lt_iff_colRow` into "earlier column" or "same column, earlier row";
`(j s) ∉ colStab` rules out the second by `swap_mem_colStab_iff`. -/
theorem offColumn_filter_eq (μ : YoungDiagram) (s : Fin (Specht.nOf μ)) :
    Finset.univ.filter (fun j : Fin (Specht.nOf μ) =>
        j.val < s.val ∧ Equiv.swap j s ∉ Specht.colStab (colSuperstandard μ))
      = (Finset.range ((colSuperstandard μ s : ℕ × ℕ).2)).biUnion (colLabels μ) := by
  ext j
  simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_biUnion,
    Finset.mem_range, colLabels]
  rw [swap_mem_colStab_iff, colPattern_colSuperstandard, colPattern_colSuperstandard]
  constructor
  · rintro ⟨hlt, hne⟩
    rcases (lt_iff_colRow μ j s).mp (Fin.lt_def.mpr hlt) with h | ⟨h, _⟩
    · exact ⟨_, h, rfl⟩
    · exact absurd h hne
  · rintro ⟨c, hc, hj⟩
    subst hj
    exact ⟨Fin.lt_def.mp ((lt_iff_colRow μ j s).mpr (Or.inl hc)), Nat.ne_of_lt hc⟩

/-- **Permutations supported on one column stabilise the column pattern.** This is the
`hCcol` side condition of `colGarnir_single_column_of_annihilation`.

A permutation fixing everything outside `colLabels μ c` maps that set into itself (by
injectivity), and every member has column value `c`, so the pattern is unchanged. -/
theorem permFixingOutside_colLabels_le_colStab (μ : YoungDiagram) (c : ℕ) :
    ∀ π ∈ OVBaseSeminormalVector.permFixingOutside (μ := μ) (colLabels μ c),
      π ∈ Specht.colStab (colSuperstandard μ) := by
  intro π hπ
  rw [Specht.mem_colStab]
  funext l
  rw [Specht.arrow_smul_apply]
  by_cases hl : l ∈ colLabels μ c
  · have hinv : π.symm l ∈ colLabels μ c := by
      by_contra hcon
      have hfix := (OVBaseSeminormalVector.mem_permFixingOutside.mp hπ) (π.symm l) hcon
      rw [Equiv.apply_symm_apply] at hfix
      exact hcon (hfix ▸ hl)
    rw [colPattern_colSuperstandard, colPattern_colSuperstandard,
      (mem_colLabels μ c _).mp hinv, (mem_colLabels μ c _).mp hl]
  · have hfix := (OVBaseSeminormalVector.mem_permFixingOutside.mp hπ) l hl
    have hinv : π.symm l = l := by
      calc π.symm l = π.symm (π l) := by rw [hfix]
      _ = l := Equiv.symm_apply_apply π l
    rw [hinv]

variable {k : Type} [Field k] [CharZero k]

/-- **The off-column (Garnir) collapse — the `+j` half**, conditional on the per-column
annihilation: the off-column sum is `col(s) · e_{T₀}`.

Decompose the off-column labels by column (`offColumn_filter_eq`), collapse each column
with `colGarnir_single_column_of_annihilation`, and sum the `col(s)` resulting copies of
`e_{T₀}`. -/
theorem offColumn_sum (μ : YoungDiagram) (s : Fin (Specht.nOf μ))
    (hann : ∀ c, c < (colSuperstandard μ s : ℕ × ℕ).2 →
      ∑ σ ∈ OVBaseSeminormalVector.permFixingOutside (μ := μ) (insert s (colLabels μ c)),
          (Equiv.Perm.sign σ : ℤ) •
            Specht.Mtab.rep (k := k) μ σ (Specht.polytabloid (k := k) (colSuperstandard μ)) = 0) :
    ∑ j ∈ Finset.univ.filter (fun j : Fin (Specht.nOf μ) =>
        j.val < s.val ∧ Equiv.swap j s ∉ Specht.colStab (colSuperstandard μ)),
          Specht.polytabloid (k := k) ((Equiv.swap j s) • (colSuperstandard μ))
      = ((colSuperstandard μ s : ℕ × ℕ).2) • Specht.polytabloid (k := k) (colSuperstandard μ) := by
  classical
  rw [offColumn_filter_eq]
  rw [Finset.sum_biUnion (by
    intro a _ b _ hab
    simp only [Function.onFun, Finset.disjoint_left]
    intro x hxa hxb
    exact hab (((mem_colLabels μ a x).mp hxa).symm.trans ((mem_colLabels μ b x).mp hxb)))]
  have hstep : ∀ c ∈ Finset.range ((colSuperstandard μ s : ℕ × ℕ).2),
      ∑ j ∈ colLabels μ c, Specht.polytabloid (k := k) ((Equiv.swap j s) • (colSuperstandard μ))
        = Specht.polytabloid (k := k) (colSuperstandard μ) := by
    intro c hc
    rw [Finset.mem_range] at hc
    refine OVBaseSeminormalVector.colGarnir_single_column_of_annihilation
      (k := k) (colSuperstandard μ) (colLabels μ c) s ?_ ?_ (hann c hc)
    · rw [mem_colLabels]; exact Nat.ne_of_gt hc
    · exact permFixingOutside_colLabels_le_colStab μ c
  rw [Finset.sum_congr rfl hstep, Finset.sum_const, Finset.card_range]

/-- **The Okounkov–Vershik eigen-equation for the column-superstandard tableau**,
conditional only on the per-column Garnir annihilation:

    X_s · e_{T₀} = col(s) · e_{T₀} − row(s) · e_{T₀}

Since the content of cell `(i, j)` is `j − i`, the right-hand side is `content · e_{T₀}` —
the OV eigenvalue. Stated as a difference of `ℕ`-smuls rather than a `ℤ`-smul because the
content is negative below the diagonal and the `ℕ` subtraction would truncate. -/
theorem jm_eigen_colSuperstandard (μ : YoungDiagram) (s : Fin (Specht.nOf μ))
    (hann : ∀ c, c < (colSuperstandard μ s : ℕ × ℕ).2 →
      ∑ σ ∈ OVBaseSeminormalVector.permFixingOutside (μ := μ) (insert s (colLabels μ c)),
          (Equiv.Perm.sign σ : ℤ) •
            Specht.Mtab.rep (k := k) μ σ (Specht.polytabloid (k := k) (colSuperstandard μ)) = 0) :
    (Specht.Mtab.rep (k := k) μ).asAlgebraHom
        (QOU.BraidKnot.JucysMurphy.jucysMurphy (k := k) (Specht.nOf μ) s)
        (Specht.polytabloid (k := k) (colSuperstandard μ))
      = ((colSuperstandard μ s : ℕ × ℕ).2) • Specht.polytabloid (k := k) (colSuperstandard μ)
        - ((colSuperstandard μ s : ℕ × ℕ).1)
            • Specht.polytabloid (k := k) (colSuperstandard μ) := by
  rw [OVBaseSeminormalVector.jm_polytabloid_split, sameColumn_count, offColumn_sum μ s hann]
  rw [smul_neg]
  abel

end QOU.BraidKnot.ColSuperstandardEigen
