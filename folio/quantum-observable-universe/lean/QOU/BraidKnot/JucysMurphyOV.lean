/-
  Okounkov–Vershik layer of the Jucys–Murphy development.

  Split out of `JucysMurphy.lean` so that `seminormalVector_base_exists` can be
  *proved* rather than cited.  The proof runs through
  `ColSuperstandardEigen.jm_eigen_colSuperstandard'`, and the import chain is

    JucysMurphy → OVBaseSeminormalVector → ColSuperstandardTableau
                → ColSuperstandardEigen → SeminormalBaseExists

  so in the old single-file layout the statement sat strictly upstream of its own
  proof and had to carry a `sorry`.  Everything here is the unchanged tail of
  `JucysMurphy.lean` (declarations from `seminormalVector_base_exists` onward),
  reopening the same namespace; the only edit is that the `sorry` is gone.

  The split point was chosen by measurement: no declaration below it is
  referenced by `OVBaseSeminormalVector` / `ColSuperstandardTableau` /
  `ColSuperstandardEigen` (docstring mentions only), so the cut introduces no
  cycle.
-/

import QOU.BraidKnot.SeminormalBaseExists

open scoped BigOperators
open MonoidAlgebra

namespace QOU.BraidKnot.JucysMurphy

variable {k : Type} [CommRing k]

/-- **OV existence core 1 (base seminormal vector — the residual cited debt).** For *some*
standard tableau `T₀` of shape `μ` there is a nonzero simultaneous JM eigenvector in `S^λ`
with the content tuple of `T₀`.  Classically this is the explicit seminormal vector of the
column-superstandard tableau (or, in Okounkov–Vershik, the highest weight of the GZ chain).

**Status note (corrected).** An earlier version of this docstring said the construction "needs
the polytabloid straightening machinery not yet built here". That is **stale**: this file
imports `QOU.BraidKnot.SpechtStandardBasis`, and the straightening machinery
(`standardPolytabloid_straightening`, `standardPolytabloid_span`, and the Garnir core
`straightening_step_colMax`) is now **proved sorry-free** there — `#print axioms` on each gives
exactly `[propext, Classical.choice, Quot.sound]`. So the cited blocker no longer applies; what
remains is the eigen-computation itself, not missing infrastructure.

The reduction is set up in `QOU.BraidKnot.OVBaseSeminormalVector` (sorry-free, imports this
file — hence the residual must be discharged there or in a leaf, not in place). Its
`jm_polytabloid_split` gives, for any tableau `t`,

  `X_s · e_t = #{j < s : (j s) ∈ colStab t} · (−e_t) + Σ_{j < s, (j s) ∉ colStab t} e_{(j s)·t}`.

For the column-superstandard `T₀` with `s` at cell `(i, j)` the same-column count is `i`, so the
first term is `−i · e_{T₀}`; since `content(i,j) = j − i`, the **sole remaining obligation** is
the off-column (Garnir) collapse

  `Σ_{j' < s, (j' s) ∉ colStab T₀} e_{(j' s)·T₀} = j · e_{T₀}`,

i.e. the off-column sum contributes exactly the number of cells strictly left of `s` in its row.
Numerically confirmed in
`docs/audits/2026-07-19-ov-base-vector-column-superstandard-verification.md`.

Strictly
smaller than the previous all-`T` existence core: existence for a *single* tableau, with the
propagation to every `T` now machine-checked (`seminormalVector_data_step` +
`syt_adjacentSwap_connected`).

**Base ring `[Field k] [CharZero k]`** — see `seminormalVector_data_exists`. -/
theorem seminormalVector_base_exists {k : Type} [Field k] [CharZero k] (μ : YoungDiagram) :
    ∃ T₀ : QOU.BraidKnot.StandardYoungTableau μ,
      ∃ v : Specht.Mtab (k := k) μ,
        v ∈ Specht.SpechtSubmodule (k := k) μ ∧ v ≠ 0 ∧
          ∀ s : Fin (Specht.nOf μ),
            (Specht.Mtab.rep μ).asAlgebraHom (jucysMurphy (k := k) (Specht.nOf μ) s) v
              = (cellContent ((tableauCellEquiv μ T₀ s : ℕ × ℕ))) • v := by
  -- Proved (no longer cited): the column-superstandard tableau is the distinguished `T₀`, and
  -- its polytabloid is the eigenvector.  See `SeminormalBaseExists`, whose ingredients are
  -- `jm_eigen_colSuperstandard'` (the OV eigen-equation, unconditional since
  -- `colGarnir_annihilation`), `polytabloid_mem_specht`, and the nonvanishing that falls out of
  -- `standardPolytabloid_linearIndependent`.
  -- Ref: [vershik-kerov1977] (Young's seminormal form; the OV highest weight of the
  -- Gelfand–Zetlin chain).
  exact QOU.BraidKnot.SeminormalBaseExists.seminormalVector_base_exists' (k := k) μ

/-- **`AdjacentSwapStep` is symmetric (sorry-free).** Swapping `a, a+1` back in `T'` returns `T`:
the content-swap conditions are visibly symmetric in `T ↔ T'`, and the content gap only changes
*sign* under the swap (`c'_b − c'_a = c_a − c_b = −(c_b − c_a)`), so the admissibility conditions
`d ≠ 0` and `d² ≠ 1` survive (`omega` / `(a−b)² = (b−a)²`). -/
theorem adjacentSwapStep_symm (μ : YoungDiagram)
    {T T' : QOU.BraidKnot.StandardYoungTableau μ}
    (h : AdjacentSwapStep μ T T') : AdjacentSwapStep μ T' T := by
  obtain ⟨a, b, hab, hTa, hTb, hoff, hne, hsq⟩ := h
  refine ⟨a, b, hab, hTb.symm, hTa.symm, fun s hsa hsb => (hoff s hsa hsb).symm, ?_, ?_⟩
  · rw [hTb, hTa]; omega
  · rw [hTb, hTa]
    have hflip :
        (cellContent ((tableauCellEquiv μ T a : ℕ × ℕ))
            - cellContent ((tableauCellEquiv μ T b : ℕ × ℕ))) ^ 2
          = (cellContent ((tableauCellEquiv μ T b : ℕ × ℕ))
              - cellContent ((tableauCellEquiv μ T a : ℕ × ℕ))) ^ 2 := by ring
    rw [hflip]; exact hsq

/-- **The admissible-adjacent-swap chain relation is symmetric (sorry-free).** Immediate from
`adjacentSwapStep_symm` by induction on the chain (reverse each step). Hence
`Relation.ReflTransGen (AdjacentSwapStep μ)` is an equivalence relation on `SYT(μ)`. -/
theorem reflTransGen_adjacentSwap_symm (μ : YoungDiagram)
    {T T' : QOU.BraidKnot.StandardYoungTableau μ}
    (h : Relation.ReflTransGen (AdjacentSwapStep μ) T T') :
    Relation.ReflTransGen (AdjacentSwapStep μ) T' T := by
  induction h with
  | refl => exact Relation.ReflTransGen.refl
  | tail _ hstep ih => exact Relation.ReflTransGen.head (adjacentSwapStep_symm μ hstep) ih

lemma cellLabel_tableauCellEquiv {μ : YoungDiagram}
    (T : QOU.BraidKnot.StandardYoungTableau μ) (s : Fin (Specht.nOf μ)) :
    QOU.BraidKnot.SpechtStandardBasis.cellLabel T (tableauCellEquiv μ T s) = s :=
  Equiv.apply_symm_apply
    (Equiv.ofBijective _ (QOU.BraidKnot.SpechtStandardBasis.cellLabel_bijective T)) s

lemma tableauCellEquiv_cellLabel {μ : YoungDiagram}
    (T : QOU.BraidKnot.StandardYoungTableau μ) (c : μ.cells) :
    tableauCellEquiv μ T (QOU.BraidKnot.SpechtStandardBasis.cellLabel T c) = c :=
  Equiv.symm_apply_apply
    (Equiv.ofBijective _ (QOU.BraidKnot.SpechtStandardBasis.cellLabel_bijective T)) c

/-- The entry at the cell of label `s` is `s` itself. -/
lemma entry_tableauCellEquiv {μ : YoungDiagram}
    (T : QOU.BraidKnot.StandardYoungTableau μ) (s : Fin (Specht.nOf μ)) :
    T.entry ((tableauCellEquiv μ T s : ℕ × ℕ)).1 ((tableauCellEquiv μ T s : ℕ × ℕ)).2
      = s.val := by
  have h := congrArg Fin.val (cellLabel_tableauCellEquiv T s)
  simpa [QOU.BraidKnot.SpechtStandardBasis.cellLabel] using h

lemma tableauCellEquiv_mem {μ : YoungDiagram}
    (T : QOU.BraidKnot.StandardYoungTableau μ) (s : Fin (Specht.nOf μ)) :
    ((tableauCellEquiv μ T s : ℕ × ℕ)) ∈ μ := by
  have := (tableauCellEquiv μ T s).2
  rwa [YoungDiagram.mem_cells] at this

/-- **Realization of an admissible adjacent swap (sorry-free).** For adjacent labels `a, a+1`
whose cells in `T` lie in different rows and columns, the consecutive-label cell-swap tableau
`swapCellsSYT` realizes an `AdjacentSwapStep μ T ·`. -/
theorem adjacentSwapStep_swapCells {μ : YoungDiagram}
    (T : QOU.BraidKnot.StandardYoungTableau μ) (a b : Fin (Specht.nOf μ))
    (hab : (a : ℕ) + 1 = (b : ℕ))
    (hrow : ((tableauCellEquiv μ T a : ℕ × ℕ)).1 ≠ ((tableauCellEquiv μ T b : ℕ × ℕ)).1)
    (hcol : ((tableauCellEquiv μ T a : ℕ × ℕ)).2 ≠ ((tableauCellEquiv μ T b : ℕ × ℕ)).2) :
    AdjacentSwapStep μ T
      (QOU.BraidKnot.swapCellsSYT T (tableauCellEquiv μ T a) (tableauCellEquiv μ T b)
        (tableauCellEquiv_mem T a) (tableauCellEquiv_mem T b)
        (by rw [entry_tableauCellEquiv, entry_tableauCellEquiv]; omega) hrow hcol) := by
  set T' := QOU.BraidKnot.swapCellsSYT T (tableauCellEquiv μ T a) (tableauCellEquiv μ T b)
    (tableauCellEquiv_mem T a) (tableauCellEquiv_mem T b)
    (by rw [entry_tableauCellEquiv, entry_tableauCellEquiv]; omega) hrow hcol with hT'_def
  have cell_ne : ∀ s t : Fin (Specht.nOf μ), s ≠ t →
      ((tableauCellEquiv μ T s : ℕ × ℕ).1, (tableauCellEquiv μ T s : ℕ × ℕ).2)
        ≠ (tableauCellEquiv μ T t : ℕ × ℕ) := by
    intro s t hst h
    rw [Prod.mk.eta] at h
    exact hst ((tableauCellEquiv μ T).injective (Subtype.ext h))
  have hcell_a : tableauCellEquiv μ T' a = tableauCellEquiv μ T b := by
    have hlab : QOU.BraidKnot.SpechtStandardBasis.cellLabel T' (tableauCellEquiv μ T b) = a := by
      apply Fin.ext
      show T'.entry (tableauCellEquiv μ T b : ℕ × ℕ).1 (tableauCellEquiv μ T b : ℕ × ℕ).2 = (a : ℕ)
      rw [hT'_def, QOU.BraidKnot.swapCellsSYT_entry_at_q, entry_tableauCellEquiv]
    rw [← hlab, tableauCellEquiv_cellLabel]
  have hcell_b : tableauCellEquiv μ T' b = tableauCellEquiv μ T a := by
    have hlab : QOU.BraidKnot.SpechtStandardBasis.cellLabel T' (tableauCellEquiv μ T a) = b := by
      apply Fin.ext
      show T'.entry (tableauCellEquiv μ T a : ℕ × ℕ).1 (tableauCellEquiv μ T a : ℕ × ℕ).2 = (b : ℕ)
      rw [hT'_def, QOU.BraidKnot.swapCellsSYT_entry_at_p, entry_tableauCellEquiv]
    rw [← hlab, tableauCellEquiv_cellLabel]
  have hcell_other : ∀ s : Fin (Specht.nOf μ), s ≠ a → s ≠ b →
      tableauCellEquiv μ T' s = tableauCellEquiv μ T s := by
    intro s hsa hsb
    have hlab : QOU.BraidKnot.SpechtStandardBasis.cellLabel T' (tableauCellEquiv μ T s) = s := by
      apply Fin.ext
      show T'.entry (tableauCellEquiv μ T s : ℕ × ℕ).1 (tableauCellEquiv μ T s : ℕ × ℕ).2 = (s : ℕ)
      rw [hT'_def, QOU.BraidKnot.swapCellsSYT_entry_other
        (by rw [Prod.mk.eta]; exact tableauCellEquiv_mem T s) (cell_ne s a hsa) (cell_ne s b hsb),
        entry_tableauCellEquiv]
    conv_lhs => rw [← hlab]
    rw [tableauCellEquiv_cellLabel]
  refine ⟨a, b, hab, ?_, ?_, ?_, ?_, ?_⟩
  · rw [hcell_a]
  · rw [hcell_b]
  · intro s hsa hsb; rw [hcell_other s hsa hsb]
  · have hne := QOU.BraidKnot.content_ne_of_succ T (tableauCellEquiv_mem T a)
      (tableauCellEquiv_mem T b) (by rw [entry_tableauCellEquiv, entry_tableauCellEquiv]; omega)
    simp only [cellContent]; omega
  · have hsq := QOU.BraidKnot.sq_content_gap_ne_one T (tableauCellEquiv_mem T a)
      (tableauCellEquiv_mem T b) (by rw [entry_tableauCellEquiv, entry_tableauCellEquiv]; omega)
      hrow hcol
    simpa only [cellContent] using hsq

/-! ### Inversion-measure walk to the row-superstandard base (closes `syt_all_connect_to_some`) -/

/-- The base tableau for the exchange walk: the row-superstandard tableau. -/
noncomputable def baseTableau (μ : YoungDiagram) : QOU.BraidKnot.StandardYoungTableau μ :=
  QOU.BraidKnot.rowSuperstandardBraidKnot μ

/-- The permutation `π_T = cellLabel_{T₀} ∘ tableauCellEquiv_T` of `Fin (nOf μ)`; `= 1` at `T₀`. -/
noncomputable def permOf (μ : YoungDiagram) (T : QOU.BraidKnot.StandardYoungTableau μ) :
    Equiv.Perm (Fin (Specht.nOf μ)) :=
  (tableauCellEquiv μ T).trans
    (Equiv.ofBijective (QOU.BraidKnot.SpechtStandardBasis.cellLabel (baseTableau μ))
      (QOU.BraidKnot.SpechtStandardBasis.cellLabel_bijective (baseTableau μ)))

lemma permOf_apply {μ : YoungDiagram} (T : QOU.BraidKnot.StandardYoungTableau μ)
    (s : Fin (Specht.nOf μ)) :
    permOf μ T s
      = QOU.BraidKnot.SpechtStandardBasis.cellLabel (baseTableau μ) (tableauCellEquiv μ T s) :=
  rfl

lemma permOf_val {μ : YoungDiagram} (T : QOU.BraidKnot.StandardYoungTableau μ)
    (s : Fin (Specht.nOf μ)) :
    (permOf μ T s : ℕ)
      = (baseTableau μ).entry (tableauCellEquiv μ T s : ℕ × ℕ).1
          (tableauCellEquiv μ T s : ℕ × ℕ).2 :=
  rfl

theorem permOf_base (μ : YoungDiagram) : permOf μ (baseTableau μ) = 1 := by
  apply Equiv.ext; intro s
  rw [permOf_apply]
  exact cellLabel_tableauCellEquiv (baseTableau μ) s

/-- A standard tableau is determined by its label→cell bijection. -/
theorem eq_of_tableauCellEquiv_eq {μ : YoungDiagram}
    {T T' : QOU.BraidKnot.StandardYoungTableau μ}
    (h : ∀ s, tableauCellEquiv μ T s = tableauCellEquiv μ T' s) : T = T' := by
  apply QOU.BraidKnot.StandardYoungTableau.ext
  funext i j
  by_cases hij : (i, j) ∈ μ
  · have hc : ((i, j) : ℕ × ℕ) ∈ μ.cells := (YoungDiagram.mem_cells _).mpr hij
    set s := QOU.BraidKnot.SpechtStandardBasis.cellLabel T ⟨(i, j), hc⟩ with hsdef
    have hTc : tableauCellEquiv μ T s = ⟨(i, j), hc⟩ := tableauCellEquiv_cellLabel T ⟨(i, j), hc⟩
    have hT'c : tableauCellEquiv μ T' s = ⟨(i, j), hc⟩ := by rw [← h s]; exact hTc
    have eT := entry_tableauCellEquiv T s
    have eT' := entry_tableauCellEquiv T' s
    rw [hTc] at eT; rw [hT'c] at eT'
    exact eT.trans eT'.symm
  · rw [T.zero_off i j hij, T'.zero_off i j hij]

/-- A descent of `π_T` at adjacent labels forces the two cells into different rows. -/
theorem descent_ne_row (μ : YoungDiagram) (T : QOU.BraidKnot.StandardYoungTableau μ)
    (a b : Fin (Specht.nOf μ)) (hab : (a : ℕ) + 1 = (b : ℕ))
    (hdesc : permOf μ T b < permOf μ T a) :
    ((tableauCellEquiv μ T a : ℕ × ℕ)).1 ≠ ((tableauCellEquiv μ T b : ℕ × ℕ)).1 := by
  intro hsame
  have hmemA := tableauCellEquiv_mem T a
  have hmemB := tableauCellEquiv_mem T b
  have heA := entry_tableauCellEquiv T a
  have heB := entry_tableauCellEquiv T b
  have hdv : (permOf μ T b : ℕ) < (permOf μ T a : ℕ) := hdesc
  rw [permOf_val, permOf_val] at hdv
  have hlt : (tableauCellEquiv μ T a : ℕ × ℕ).2 < (tableauCellEquiv μ T b : ℕ × ℕ).2 := by
    rcases lt_trichotomy (tableauCellEquiv μ T a : ℕ × ℕ).2 (tableauCellEquiv μ T b : ℕ × ℕ).2
      with h | h | h
    · exact h
    · exfalso
      have hcell : (tableauCellEquiv μ T a : ℕ × ℕ) = (tableauCellEquiv μ T b : ℕ × ℕ) :=
        Prod.ext hsame h
      have := (tableauCellEquiv μ T).injective (Subtype.ext hcell)
      omega
    · exfalso
      have hstep := QOU.BraidKnot.entryLtRow T
        (by rw [Prod.mk.eta]; exact hmemA) h
      rw [heA, hsame, heB] at hstep
      omega
  have hasc : (baseTableau μ).entry (tableauCellEquiv μ T a : ℕ × ℕ).1
        (tableauCellEquiv μ T a : ℕ × ℕ).2
      < (baseTableau μ).entry (tableauCellEquiv μ T b : ℕ × ℕ).1
          (tableauCellEquiv μ T b : ℕ × ℕ).2 := by
    rw [← hsame]
    exact QOU.BraidKnot.entryLtRow (baseTableau μ) (by rw [hsame, Prod.mk.eta]; exact hmemB) hlt
  omega

/-- A descent of `π_T` at adjacent labels forces the two cells into different columns. -/
theorem descent_ne_col (μ : YoungDiagram) (T : QOU.BraidKnot.StandardYoungTableau μ)
    (a b : Fin (Specht.nOf μ)) (hab : (a : ℕ) + 1 = (b : ℕ))
    (hdesc : permOf μ T b < permOf μ T a) :
    ((tableauCellEquiv μ T a : ℕ × ℕ)).2 ≠ ((tableauCellEquiv μ T b : ℕ × ℕ)).2 := by
  intro hsame
  have hmemA := tableauCellEquiv_mem T a
  have hmemB := tableauCellEquiv_mem T b
  have heA := entry_tableauCellEquiv T a
  have heB := entry_tableauCellEquiv T b
  have hdv : (permOf μ T b : ℕ) < (permOf μ T a : ℕ) := hdesc
  rw [permOf_val, permOf_val] at hdv
  have hlt : (tableauCellEquiv μ T a : ℕ × ℕ).1 < (tableauCellEquiv μ T b : ℕ × ℕ).1 := by
    rcases lt_trichotomy (tableauCellEquiv μ T a : ℕ × ℕ).1 (tableauCellEquiv μ T b : ℕ × ℕ).1
      with h | h | h
    · exact h
    · exfalso
      have hcell : (tableauCellEquiv μ T a : ℕ × ℕ) = (tableauCellEquiv μ T b : ℕ × ℕ) :=
        Prod.ext h hsame
      have := (tableauCellEquiv μ T).injective (Subtype.ext hcell)
      omega
    · exfalso
      have hstep := QOU.BraidKnot.entryLtCol T
        (by rw [Prod.mk.eta]; exact hmemA) h
      rw [heA, hsame, heB] at hstep
      omega
  have hasc : (baseTableau μ).entry (tableauCellEquiv μ T a : ℕ × ℕ).1
        (tableauCellEquiv μ T a : ℕ × ℕ).2
      < (baseTableau μ).entry (tableauCellEquiv μ T b : ℕ × ℕ).1
          (tableauCellEquiv μ T b : ℕ × ℕ).2 := by
    rw [← hsame]
    exact QOU.BraidKnot.entryLtCol (baseTableau μ) (by rw [hsame, Prod.mk.eta]; exact hmemB) hlt
  omega

/-- The swap of two adjacent-label cells right-multiplies `π_T` by `swap a b`. -/
theorem permOf_swapCells (μ : YoungDiagram) (T : QOU.BraidKnot.StandardYoungTableau μ)
    (a b : Fin (Specht.nOf μ)) (hab : (a : ℕ) + 1 = (b : ℕ))
    (hrow : ((tableauCellEquiv μ T a : ℕ × ℕ)).1 ≠ ((tableauCellEquiv μ T b : ℕ × ℕ)).1)
    (hcol : ((tableauCellEquiv μ T a : ℕ × ℕ)).2 ≠ ((tableauCellEquiv μ T b : ℕ × ℕ)).2) :
    permOf μ (QOU.BraidKnot.swapCellsSYT T (tableauCellEquiv μ T a) (tableauCellEquiv μ T b)
        (tableauCellEquiv_mem T a) (tableauCellEquiv_mem T b)
        (by rw [entry_tableauCellEquiv, entry_tableauCellEquiv]; omega) hrow hcol)
      = permOf μ T * Equiv.swap a b := by
  set T' := QOU.BraidKnot.swapCellsSYT T (tableauCellEquiv μ T a) (tableauCellEquiv μ T b)
    (tableauCellEquiv_mem T a) (tableauCellEquiv_mem T b)
    (by rw [entry_tableauCellEquiv, entry_tableauCellEquiv]; omega) hrow hcol with hT'_def
  have cell_ne : ∀ s t : Fin (Specht.nOf μ), s ≠ t →
      ((tableauCellEquiv μ T s : ℕ × ℕ).1, (tableauCellEquiv μ T s : ℕ × ℕ).2)
        ≠ (tableauCellEquiv μ T t : ℕ × ℕ) := by
    intro s t hst h
    rw [Prod.mk.eta] at h
    exact hst ((tableauCellEquiv μ T).injective (Subtype.ext h))
  have hcell_a : tableauCellEquiv μ T' a = tableauCellEquiv μ T b := by
    have hlab : QOU.BraidKnot.SpechtStandardBasis.cellLabel T' (tableauCellEquiv μ T b) = a := by
      apply Fin.ext
      show T'.entry (tableauCellEquiv μ T b : ℕ × ℕ).1 (tableauCellEquiv μ T b : ℕ × ℕ).2 = (a : ℕ)
      rw [hT'_def, QOU.BraidKnot.swapCellsSYT_entry_at_q, entry_tableauCellEquiv]
    rw [← hlab, tableauCellEquiv_cellLabel]
  have hcell_b : tableauCellEquiv μ T' b = tableauCellEquiv μ T a := by
    have hlab : QOU.BraidKnot.SpechtStandardBasis.cellLabel T' (tableauCellEquiv μ T a) = b := by
      apply Fin.ext
      show T'.entry (tableauCellEquiv μ T a : ℕ × ℕ).1 (tableauCellEquiv μ T a : ℕ × ℕ).2 = (b : ℕ)
      rw [hT'_def, QOU.BraidKnot.swapCellsSYT_entry_at_p, entry_tableauCellEquiv]
    rw [← hlab, tableauCellEquiv_cellLabel]
  have hcell_other : ∀ s : Fin (Specht.nOf μ), s ≠ a → s ≠ b →
      tableauCellEquiv μ T' s = tableauCellEquiv μ T s := by
    intro s hsa hsb
    have hlab : QOU.BraidKnot.SpechtStandardBasis.cellLabel T' (tableauCellEquiv μ T s) = s := by
      apply Fin.ext
      show T'.entry (tableauCellEquiv μ T s : ℕ × ℕ).1 (tableauCellEquiv μ T s : ℕ × ℕ).2 = (s : ℕ)
      rw [hT'_def, QOU.BraidKnot.swapCellsSYT_entry_other
        (by rw [Prod.mk.eta]; exact tableauCellEquiv_mem T s) (cell_ne s a hsa) (cell_ne s b hsb),
        entry_tableauCellEquiv]
    conv_lhs => rw [← hlab]
    rw [tableauCellEquiv_cellLabel]
  apply Equiv.ext
  intro s
  rw [Equiv.Perm.mul_apply, permOf_apply, permOf_apply]
  congr 1
  rcases eq_or_ne s a with rfl | hsa
  · rw [hcell_a, Equiv.swap_apply_left]
  · rcases eq_or_ne s b with rfl | hsb
    · rw [hcell_b, Equiv.swap_apply_right]
    · rw [hcell_other s hsa hsb, Equiv.swap_apply_of_ne_of_ne hsa hsb]

/-- **OV existence core 2 — every standard tableau walks to the row-superstandard base
(sorry-free).** Well-founded induction on the inversion count of `π_T`: at `0` inversions `π_T = 1`
so `T = T₀`; otherwise an adjacent descent of `π_T` yields (`descent_ne_row`/`descent_ne_col`) an
admissible swap (`adjacentSwapStep_swapCells`) whose result has strictly smaller inversion count
(`permOf_swapCells` + `invCount_mul_swap_lt`), so the induction closes the walk. Every descent is
admissible because same-row / same-column consecutive labels map to *ascents* under
`cellLabel_{T₀}`, and consecutive labels never share a diagonal. -/
theorem syt_all_connect_to_some (μ : YoungDiagram) :
    ∃ T₀ : QOU.BraidKnot.StandardYoungTableau μ,
      ∀ T : QOU.BraidKnot.StandardYoungTableau μ,
        Relation.ReflTransGen (AdjacentSwapStep μ) T T₀ := by
  refine ⟨baseTableau μ, ?_⟩
  suffices H : ∀ m : ℕ, ∀ T : QOU.BraidKnot.StandardYoungTableau μ,
      QOU.Mathlib.invCount (permOf μ T) = m →
      Relation.ReflTransGen (AdjacentSwapStep μ) T (baseTableau μ) by
    exact fun T => H _ T rfl
  intro m
  induction m using Nat.strong_induction_on with
  | _ m IH =>
    intro T hm
    by_cases h0 : QOU.Mathlib.invCount (permOf μ T) = 0
    · have hp1 : permOf μ T = 1 := QOU.Mathlib.eq_one_of_invCount_eq_zero h0
      have hTeq : T = baseTableau μ := by
        apply eq_of_tableauCellEquiv_eq
        intro s
        have h1 : QOU.BraidKnot.SpechtStandardBasis.cellLabel (baseTableau μ)
            (tableauCellEquiv μ T s) = s := by rw [← permOf_apply, hp1]; rfl
        have h2 := cellLabel_tableauCellEquiv (baseTableau μ) s
        exact (QOU.BraidKnot.SpechtStandardBasis.cellLabel_bijective (baseTableau μ)).injective
          (h1.trans h2.symm)
      rw [hTeq]
    · have hne : permOf μ T ≠ 1 := by
        intro h
        apply h0
        rw [h, QOU.Mathlib.invCount, Finset.card_eq_zero, Finset.filter_eq_empty_iff]
        rintro p -
        rintro ⟨h1, h2⟩
        exact absurd (h1.trans h2) (lt_irrefl _)
      obtain ⟨a, b, hba, hdesc⟩ := QOU.Mathlib.exists_adjacent_descent_of_ne_one hne
      have hab : (a : ℕ) + 1 = (b : ℕ) := hba.symm
      have hrow := descent_ne_row μ T a b hab hdesc
      have hcol := descent_ne_col μ T a b hab hdesc
      have hstep := adjacentSwapStep_swapCells T a b hab hrow hcol
      have hmeasure : QOU.Mathlib.invCount (permOf μ
          (QOU.BraidKnot.swapCellsSYT T (tableauCellEquiv μ T a) (tableauCellEquiv μ T b)
            (tableauCellEquiv_mem T a) (tableauCellEquiv_mem T b)
            (by rw [entry_tableauCellEquiv, entry_tableauCellEquiv]; omega) hrow hcol))
          < QOU.Mathlib.invCount (permOf μ T) := by
        rw [permOf_swapCells μ T a b hab hrow hcol]
        exact QOU.Mathlib.invCount_mul_swap_lt (permOf μ T) hba hdesc
      exact Relation.ReflTransGen.head hstep
        (IH _ (by rw [← hm]; exact hmeasure) _ rfl)

/-- **OV existence core 2 (adjacent-swap connectivity of standard tableaux — combinatorial).**
Any two standard Young tableaux of the same shape are connected by a chain of admissible
adjacent swaps (`AdjacentSwapStep`).

**De-abstraction (this proof is sorry-free).** Both `T` and `T'` connect to the common base `T₀`
(`syt_all_connect_to_some`, core 2); reverse the second leg by symmetry
(`reflTransGen_adjacentSwap_symm`) and compose (`T ⤳* T₀ ⤳* T'`). The residual cited debt is thus
the strictly smaller one-directional base walk, with the two-directional plumbing proved here. -/
theorem syt_adjacentSwap_connected (μ : YoungDiagram)
    (T T' : QOU.BraidKnot.StandardYoungTableau μ) :
    Relation.ReflTransGen (AdjacentSwapStep μ) T T' := by
  obtain ⟨T₀, hbase⟩ := syt_all_connect_to_some μ
  exact (hbase T).trans (reflTransGen_adjacentSwap_symm μ (hbase T'))

/-- **The Okounkov–Vershik existence theorem (Young's seminormal vector), de-abstracted.** For
every standard Young tableau `T` of shape `μ`, there exists a nonzero vector `v` in the Specht
submodule `S^λ` on which **each** Jucys–Murphy element `X_s` acts diagonally with eigenvalue
`cellContent (c)`, where `c = tableauCellEquiv μ T s` is the cell of `μ` holding label `s` in `T`.

**De-abstraction (this proof is sorry-free; its inputs are the two named cores).** Take the base
seminormal vector (`seminormalVector_base_exists`, core 1), walk the admissible-adjacent-swap
chain from its tableau to `T` (`syt_adjacentSwap_connected`, core 2), transporting the
eigenvector along each step by the machine-checked classical 2×2 seminormal block
(`seminormalVector_data_step`: the JM recursion `s·X_a·s = X_b − s` + the eigenvalue-swap /
fixed-operator / non-vanishing linear algebra + `S^λ`-invariance — all sorry-free).  The cited
debt is thus reduced from "all-`T` eigenvector existence" to {base-tableau existence,
adjacent-swap connectivity} — each strictly more atomic.

**Base ring `[Field k] [CharZero k]` (§7c over-generality fix).** Stated over a char-0 field, NOT
the file-wide `[CommRing k]`: over a general commutative ring the integer cell-contents can collide
modulo the characteristic (e.g. `ℤ/pℤ` with `c_i ≡ c_j` but `c_i ≠ c_j`), so the cast JM eigenvalues
`↑c_s` stop being distinct, the eigenspaces merge, and a simultaneous eigenvector with the
*prescribed* content tuple need not exist in `S^λ` — the `[CommRing k]` form is over-general (false at
`ℤ/pℤ`).  Young's seminormal form is genuinely a char-0 fact (it inverts the content differences
`c_i − c_j`, exactly as the transport step does). -/
theorem seminormalVector_data_exists {k : Type} [Field k] [CharZero k] (μ : YoungDiagram)
    (T : QOU.BraidKnot.StandardYoungTableau μ) :
    ∃ v : Specht.Mtab (k := k) μ,
      v ∈ Specht.SpechtSubmodule (k := k) μ ∧ v ≠ 0 ∧
        ∀ s : Fin (Specht.nOf μ),
          (Specht.Mtab.rep μ).asAlgebraHom (jucysMurphy (k := k) (Specht.nOf μ) s) v
            = (cellContent ((tableauCellEquiv μ T s : ℕ × ℕ))) • v := by
  obtain ⟨T₀, hbase⟩ := seminormalVector_base_exists (k := k) μ
  have hchain : Relation.ReflTransGen (AdjacentSwapStep μ) T₀ T :=
    syt_adjacentSwap_connected μ T₀ T
  induction hchain with
  | refl => exact hbase
  | tail _ hstep ih => exact seminormalVector_data_step μ hstep ih

/-- **Jucys–Murphy eigenvalue theorem (Okounkov–Vershik).** The Specht module `S^λ` admits a
Gelfand–Zetlin / seminormal basis indexed by the standard Young tableaux of shape `μ`, on which
every JM element `X_k` acts **diagonally** with eigenvalue `cellContent (cell of k in T)`.

We state this as: for every standard tableau `T` of shape `μ`, there is a seminormal eigenvector
`sv` whose indexing tableau is `T`.  The eigenproperty itself is recorded as the `isEig` field of
`SeminormalVector` (each `X_k` acts by the content of `k`'s cell); the *content* of the theorem is
the **existence** of such vectors for every `T`, i.e. that the GZ basis exists and diagonalises the
JM elements.  Together with `jucysMurphy_commute`, this is the heart of the OV approach.

**Reduction (sorry-free here, modulo the named eigenvector core).** This theorem no longer carries
the `sorry` directly.  Its `cellOf` field is *constructed* from `T` by the sorry-free brick-4
bijection `tableauCellEquiv μ T` (= `sytToTableau T`), and the eigenvector data `(v, mem, nz, isEig)`
is supplied by `seminormalVector_data_exists` — the single cited core that isolates exactly Young's
seminormal-vector existence.  `sv.T = T` then holds by `rfl`.  So the genuine OV debt is now named
precisely (`seminormalVector_data_exists`) and the *bijection* part — historically bundled into the
same `sorry` — is genuinely closed.

**Base ring `[Field k] [CharZero k]`** — inherited from `seminormalVector_data_exists` (the
seminormal eigenvector is a char-0 fact; the `[CommRing k]` form is over-general, false at `ℤ/pℤ`). -/
theorem jucysMurphy_eigenvalue {k : Type} [Field k] [CharZero k] (μ : YoungDiagram)
    (T : QOU.BraidKnot.StandardYoungTableau μ) :
    ∃ sv : SeminormalVector (k := k) μ, sv.T = T := by
  obtain ⟨v, hmem, hnz, hisEig⟩ := seminormalVector_data_exists (k := k) μ T
  exact ⟨{ T := T
           v := v
           mem := hmem
           nz := hnz
           cellOf := tableauCellEquiv μ T
           isEig := hisEig }, rfl⟩

/-- The span of the seminormal vectors, as a submodule of `M^λ` (local abbreviation; the public
`seminormalVectors_span` below uses the inline `Submodule.span …` form for splice-compatibility). -/
noncomputable abbrev seminormalSpan {k : Type} [Field k] (μ : YoungDiagram) :
    Submodule k (Specht.Mtab (k := k) μ) :=
  Submodule.span k (Set.range (fun sv : SeminormalVector (k := k) μ => sv.v))

/-- **Easy direction (sorry-free).** The seminormal span sits inside `S^λ` — every seminormal vector
lies in `S^λ` (the `mem` field of `SeminormalVector`). -/
theorem seminormalSpan_le {k : Type} [Field k] (μ : YoungDiagram) :
    seminormalSpan (k := k) μ ≤ Specht.SpechtSubmodule (k := k) μ := by
  rw [seminormalSpan, Submodule.span_le]
  rintro _ ⟨sv, rfl⟩
  exact sv.mem

/-- **(L1) Joint eigenvectors with pairwise-distinct eigenvalue tuples are linearly independent.**
Generic linear algebra (no tableau/Specht content, sorry-free): a family `v : ι → V` of nonzero
vectors, each a simultaneous eigenvector of every operator `A s` with eigenvalue tuple
`c i : S → k`; if the tuple map `c` is injective, the family is independent.

Proof: `linearIndependent_iff'` + strong induction on the support `t` of a finite dependency.  For
`j ∈ t`: if `t = {j}`, then `g j • v j = 0` forces `g j = 0` (`v j ≠ 0`); otherwise pick `i₀ ∈ t`
with `i₀ ≠ j` and a separator `s₀` with `c i₀ s₀ ≠ c j s₀` (tuple injectivity), apply `A s₀` and
subtract `c i₀ s₀ ·` the original relation — the `i₀` term dies, and the inductive hypothesis on
`t.erase i₀` gives `g j · (c j s₀ − c i₀ s₀) = 0`, whence `g j = 0`.

Note the operators need **not** commute and no diagonalisability is assumed — only the given
family's eigen-structure is used.  This is the entire linear-algebra content of the OV
"distinct content-tuples ⇒ independent" step, factored out of the citation. -/
theorem linearIndependent_of_joint_eigenvectors {k : Type} [Field k]
    {V : Type*} [AddCommGroup V] [Module k V] {ι S : Type*}
    (A : S → V →ₗ[k] V) (v : ι → V) (c : ι → S → k)
    (hnz : ∀ i, v i ≠ 0)
    (heig : ∀ i s, A s (v i) = c i s • v i)
    (hinj : Function.Injective c) :
    LinearIndependent k v := by
  classical
  rw [linearIndependent_iff']
  intro t
  induction t using Finset.strongInduction with
  | _ t IH =>
    intro g hrel j hj
    by_cases hcard : t.card ≤ 1
    · -- singleton support: g j • v j = 0 with v j ≠ 0
      have ht : t = {j} := Finset.eq_singleton_iff_unique_mem.mpr
        ⟨hj, fun x hx => Finset.card_le_one.mp hcard x hx j hj⟩
      rw [ht, Finset.sum_singleton] at hrel
      exact (smul_eq_zero.mp hrel).resolve_right (hnz j)
    · push_neg at hcard
      -- a second support element i₀ ≠ j
      obtain ⟨i₀, hi₀t, hi₀j⟩ : ∃ i₀ ∈ t, i₀ ≠ j := by
        obtain ⟨a, ha, b, hb, hab⟩ := Finset.one_lt_card.mp hcard
        rcases eq_or_ne a j with rfl | haj
        · exact ⟨b, hb, fun h => hab h.symm⟩
        · exact ⟨a, ha, haj⟩
      -- a separating operator index
      obtain ⟨s₀, hs₀⟩ := Function.ne_iff.mp (fun h : c i₀ = c j => hi₀j (hinj h))
      -- apply A s₀ to the relation
      have h1 : ∑ i ∈ t, (g i * c i s₀) • v i = 0 := by
        have h := congrArg (A s₀) hrel
        rw [map_sum, map_zero] at h
        calc ∑ i ∈ t, (g i * c i s₀) • v i
            = ∑ i ∈ t, A s₀ (g i • v i) := by
              refine Finset.sum_congr rfl fun i _ => ?_
              rw [map_smul, heig, smul_smul]
          _ = 0 := h
      -- scale the relation by c i₀ s₀
      have h2 : ∑ i ∈ t, (g i * c i₀ s₀) • v i = 0 := by
        calc ∑ i ∈ t, (g i * c i₀ s₀) • v i
            = c i₀ s₀ • ∑ i ∈ t, g i • v i := by
              rw [Finset.smul_sum]
              refine Finset.sum_congr rfl fun i _ => ?_
              rw [smul_smul, mul_comm]
          _ = 0 := by rw [hrel, smul_zero]
      -- subtract: the i₀ coefficient is killed
      have hrel2 : ∑ i ∈ t, (g i * (c i s₀ - c i₀ s₀)) • v i = 0 := by
        calc ∑ i ∈ t, (g i * (c i s₀ - c i₀ s₀)) • v i
            = ∑ i ∈ t, ((g i * c i s₀) • v i - (g i * c i₀ s₀) • v i) := by
              refine Finset.sum_congr rfl fun i _ => ?_
              rw [mul_sub, sub_smul]
          _ = (∑ i ∈ t, (g i * c i s₀) • v i) - ∑ i ∈ t, (g i * c i₀ s₀) • v i :=
              Finset.sum_sub_distrib _ _
          _ = 0 := by rw [h1, h2, sub_zero]
      have hrel3 : ∑ i ∈ t.erase i₀, (g i * (c i s₀ - c i₀ s₀)) • v i = 0 := by
        have h := Finset.add_sum_erase t (fun i => (g i * (c i s₀ - c i₀ s₀)) • v i) hi₀t
        rw [hrel2] at h
        simpa [sub_self] using h
      -- inductive hypothesis on the smaller support, read off at j
      have hIH := IH (t.erase i₀) (Finset.erase_ssubset hi₀t)
        (fun i => g i * (c i s₀ - c i₀ s₀)) hrel3 j
        (Finset.mem_erase.mpr ⟨Ne.symm hi₀j, hj⟩)
      rcases mul_eq_zero.mp hIH with h | h
      · exact h
      · exact absurd (sub_eq_zero.mp h).symm hs₀

/-! #### L2 helpers: entries strictly increase along diagonals; the row-count formula

The proof of L2 below avoids diagram-removal entirely.  In a standard tableau the entries
strictly increase along each **diagonal** (`row_strict` + `col_strict` + up-left-closedness), the
diagonal-`d` cells of `μ` form a contiguous row range starting at row `(−d)⁺`, and therefore

  `row(s) = (−content s)⁺ + #{s' < s with the same content}`

— the row of a label is determined by the content **tuple** alone.  Two tableaux with the same
content tuple then agree cell-by-cell (columns follow from rows + contents), hence are equal. -/

private lemma entry_lt_diag_succ {μ : YoungDiagram}
    (T : QOU.BraidKnot.StandardYoungTableau μ) {i j : ℕ}
    (hmem : (i + 1, j + 1) ∈ μ) : T.entry i j < T.entry (i + 1) (j + 1) :=
  lt_trans
    (T.row_strict i j (μ.up_left_mem (Nat.le_succ i) le_rfl hmem))
    (T.col_strict i (j + 1) hmem)

/-- Entries strictly increase along a diagonal: same content, strictly smaller row ⇒ strictly
smaller entry.  Induction on the row of the lower cell, stepping through the diagonal
predecessor `(y₁ − 1, y₂ − 1)` (in `μ` by up-left-closedness). -/
private lemma entry_lt_of_diag_row_lt {μ : YoungDiagram}
    (T : QOU.BraidKnot.StandardYoungTableau μ) :
    ∀ (r : ℕ) {x y : ℕ × ℕ}, x ∈ μ → y ∈ μ → y.1 = r →
      (x.2 : ℤ) - (x.1 : ℤ) = (y.2 : ℤ) - (y.1 : ℤ) → x.1 < y.1 →
      T.entry x.1 x.2 < T.entry y.1 y.2 := by
  intro r
  induction r with
  | zero => intro x y _ _ hy1 _ hlt; omega
  | succ r IH =>
    rintro ⟨x1, x2⟩ ⟨y1, y2⟩ hx hy hy1 hd hlt
    simp only at hy1 hd hlt ⊢
    subst hy1
    rcases eq_or_lt_of_le (Nat.lt_succ_iff.mp hlt) with heq | hlt'
    · -- x is the immediate diagonal predecessor: y = (x1+1, x2+1)
      subst heq
      have hy2 : y2 = x2 + 1 := by omega
      subst hy2
      exact entry_lt_diag_succ T hy
    · -- step through z = (r, y2 − 1)
      have hzmem : (r, y2 - 1) ∈ μ :=
        μ.up_left_mem (Nat.le_succ r) (Nat.sub_le y2 1) hy
      have hstep : T.entry r (y2 - 1) < T.entry (r + 1) y2 := by
        have h1 : y2 - 1 + 1 = y2 := by omega
        have := entry_lt_diag_succ T (i := r) (j := y2 - 1) (by rw [h1]; exact hy)
        rwa [h1] at this
      refine lt_trans (IH (x := (x1, x2)) (y := (r, y2 - 1)) hx hzmem rfl ?_ hlt') hstep
      have : ((y2 - 1 : ℕ) : ℤ) = (y2 : ℤ) - 1 := by omega
      simp only [this]
      omega

/-- **The row-count formula.** The row of the cell holding label `s` equals
`(−content)⁺ + #{s' < s with the same content}` — determined by the content tuple alone. -/
private lemma row_eq_offset_add_count {μ : YoungDiagram}
    (T : QOU.BraidKnot.StandardYoungTableau μ) (s : Fin (Specht.nOf μ)) :
    ((tableauCellEquiv μ T s : ℕ × ℕ)).1
      = (-(cellContent ((tableauCellEquiv μ T s : ℕ × ℕ)))).toNat
        + (Finset.univ.filter (fun s' : Fin (Specht.nOf μ) =>
            cellContent ((tableauCellEquiv μ T s' : ℕ × ℕ))
              = cellContent ((tableauCellEquiv μ T s : ℕ × ℕ)) ∧ s' < s)).card := by
  classical
  set x : ℕ × ℕ := ((tableauCellEquiv μ T s : ℕ × ℕ)) with hxdef
  have hxmem : x ∈ μ := tableauCellEquiv_mem T s
  set d : ℤ := cellContent x
  have hd : d = (x.2 : ℤ) - (x.1 : ℤ) := rfl
  -- the count is the size of the row range [(−d)⁺, x.1)
  have hcard : (Finset.univ.filter (fun s' : Fin (Specht.nOf μ) =>
        cellContent ((tableauCellEquiv μ T s' : ℕ × ℕ)) = d ∧ s' < s)).card
      = (Finset.Ico (-d).toNat x.1).card := by
    refine Finset.card_bij'
      (fun s' _ => ((tableauCellEquiv μ T s' : ℕ × ℕ)).1)
      (fun i hi => QOU.BraidKnot.SpechtStandardBasis.cellLabel T
        ⟨(i, ((i : ℤ) + d).toNat), by
          rw [YoungDiagram.mem_cells]
          rw [Finset.mem_Ico] at hi
          have hx' : (x.1, x.2) ∈ μ := by rwa [Prod.mk.eta]
          refine μ.up_left_mem (le_of_lt hi.2) ?_ hx'
          rw [Int.toNat_le]
          omega⟩)
      ?_ ?_ ?_ ?_
    · -- forward well-defined: row(s') ∈ Ico (−d)⁺ x.1
      intro s' hs'
      obtain ⟨-, hc, hlt⟩ := Finset.mem_filter.mp hs'
      have hymem : ((tableauCellEquiv μ T s' : ℕ × ℕ)) ∈ μ := tableauCellEquiv_mem T s'
      have hcy : ((((tableauCellEquiv μ T s' : ℕ × ℕ)).2 : ℤ))
          - (((tableauCellEquiv μ T s' : ℕ × ℕ)).1 : ℤ) = d := by
        simpa [cellContent] using hc
      show ((tableauCellEquiv μ T s' : ℕ × ℕ)).1 ∈ Finset.Ico (-d).toNat x.1
      rw [Finset.mem_Ico]
      constructor
      · -- (−d)⁺ ≤ row(s') since the column is a natural number
        rw [Int.toNat_le]
        omega
      · -- row(s') < x.1: not equal (else same cell ⇒ s' = s), not greater (entry monotone)
        rcases lt_trichotomy ((tableauCellEquiv μ T s' : ℕ × ℕ)).1 x.1 with h | h | h
        · exact h
        · -- same row + same content ⇒ same cell ⇒ s' = s, contra s' < s
          exfalso
          have hy2 : ((tableauCellEquiv μ T s' : ℕ × ℕ)).2 = x.2 := by omega
          have hcell : (tableauCellEquiv μ T s') = (tableauCellEquiv μ T s) := by
            apply Subtype.ext
            rw [← hxdef]
            exact Prod.ext h hy2
          have hss := congrArg (QOU.BraidKnot.SpechtStandardBasis.cellLabel T) hcell
          rw [cellLabel_tableauCellEquiv, cellLabel_tableauCellEquiv] at hss
          exact absurd hss (ne_of_lt hlt)
        · -- row(s') > x.1 ⇒ entry x < entry(s'-cell) ⇒ s < s', contra
          exfalso
          have hmono := entry_lt_of_diag_row_lt T ((tableauCellEquiv μ T s' : ℕ × ℕ)).1
            hxmem hymem rfl (by omega) h
          rw [hxdef] at hmono
          rw [entry_tableauCellEquiv, entry_tableauCellEquiv] at hmono
          exact absurd (Fin.lt_def.mpr hmono) (not_lt.mpr (le_of_lt hlt))
    · -- backward well-defined: the constructed label is in the filter
      intro i hi
      rw [Finset.mem_Ico] at hi
      have h0 : (0 : ℤ) ≤ (i : ℤ) + d := by
        have h1 := hi.1
        rw [Int.toNat_le] at h1
        omega
      rw [Finset.mem_filter]
      refine ⟨Finset.mem_univ _, ?_, ?_⟩
      · -- content of its cell = d
        rw [tableauCellEquiv_cellLabel]
        show ((((i : ℤ) + d).toNat : ℤ)) - (i : ℤ) = d
        rw [Int.toNat_of_nonneg h0]
        ring
      · -- the constructed label < s: its entry is on the diagonal at a smaller row
        have hcmem : ((i, ((i : ℤ) + d).toNat) : ℕ × ℕ) ∈ μ := by
          have hx' : (x.1, x.2) ∈ μ := by rwa [Prod.mk.eta]
          refine μ.up_left_mem (le_of_lt hi.2) ?_ hx'
          rw [Int.toNat_le]
          omega
        have hmono := entry_lt_of_diag_row_lt T x.1
          (x := (i, ((i : ℤ) + d).toNat)) (y := x) hcmem hxmem rfl
          (by
            show ((((i : ℤ) + d).toNat : ℤ)) - (i : ℤ) = (x.2 : ℤ) - (x.1 : ℤ)
            rw [Int.toNat_of_nonneg h0]
            omega) hi.2
        rw [Fin.lt_def]
        show T.entry i (((i : ℤ) + d).toNat) < s.val
        rw [← entry_tableauCellEquiv T s, ← hxdef]
        exact hmono
    · -- left inverse: reconstructing from the row gives back s'
      intro s' hs'
      obtain ⟨-, hc, -⟩ := Finset.mem_filter.mp hs'
      have hcy : ((((tableauCellEquiv μ T s' : ℕ × ℕ)).2 : ℤ))
          - (((tableauCellEquiv μ T s' : ℕ × ℕ)).1 : ℤ) = d := by
        simpa [cellContent] using hc
      have key : ∀ (c : μ.cells), (c : ℕ × ℕ) = ((tableauCellEquiv μ T s' : ℕ × ℕ)) →
          QOU.BraidKnot.SpechtStandardBasis.cellLabel T c = s' := by
        intro c hcv
        rw [Subtype.ext hcv, cellLabel_tableauCellEquiv]
      apply key
      refine Prod.ext rfl ?_
      show (((((tableauCellEquiv μ T s' : ℕ × ℕ)).1 : ℤ) + d).toNat)
          = ((tableauCellEquiv μ T s' : ℕ × ℕ)).2
      omega
    · -- right inverse: the row of the constructed cell is i
      intro i hi
      simp only [tableauCellEquiv_cellLabel]
  rw [hcard, Nat.card_Ico]
  -- x.1 ≥ (−d)⁺ since the column is a natural number
  have hle : (-d).toNat ≤ x.1 := by
    rw [Int.toNat_le]
    omega
  omega

/-- **(L2) The seminormal simple-spectrum core (combinatorial): the content tuple determines the
standard tableau — PROVED.** If two standard Young tableaux of shape `μ` assign the same
cell-content to every label, they are equal.

Proof (no diagram-removal): entries strictly increase along each diagonal
(`entry_lt_of_diag_row_lt`), so the **row** of the cell holding label `s` is
`(−content s)⁺ + #{s' < s with the same content}` (`row_eq_offset_add_count`) — a function of the
content tuple alone, hence shared by `T` and `T'`.  The **column** then follows from
row + content, so the label→cell maps coincide; inverting, the cell→label maps (`cellLabel`)
coincide, i.e. all entries agree on `μ` (and off `μ` both are pinned to `0`), so `T = T'`. -/
theorem syt_content_tuple_injective (μ : YoungDiagram)
    (T T' : QOU.BraidKnot.StandardYoungTableau μ)
    (h : ∀ s : Fin (Specht.nOf μ),
      cellContent ((tableauCellEquiv μ T s : ℕ × ℕ))
        = cellContent ((tableauCellEquiv μ T' s : ℕ × ℕ))) :
    T = T' := by
  classical
  -- the label→cell maps agree
  have hcell : ∀ s : Fin (Specht.nOf μ),
      ((tableauCellEquiv μ T s : ℕ × ℕ)) = ((tableauCellEquiv μ T' s : ℕ × ℕ)) := by
    intro s
    have hrow : ((tableauCellEquiv μ T s : ℕ × ℕ)).1
        = ((tableauCellEquiv μ T' s : ℕ × ℕ)).1 := by
      rw [row_eq_offset_add_count T s, row_eq_offset_add_count T' s, h s]
      congr 2
      apply Finset.filter_congr
      intro s' _
      rw [h s']
    refine Prod.ext hrow ?_
    -- columns: (col : ℤ) = row + content on both sides
    have h1 : ((((tableauCellEquiv μ T s : ℕ × ℕ)).2 : ℤ))
        - (((tableauCellEquiv μ T s : ℕ × ℕ)).1 : ℤ)
        = ((((tableauCellEquiv μ T' s : ℕ × ℕ)).2 : ℤ))
        - (((tableauCellEquiv μ T' s : ℕ × ℕ)).1 : ℤ) := by
      simpa [cellContent] using h s
    omega
  -- hence the cell→label maps agree, i.e. the entries agree on μ
  ext i j
  by_cases hij : (i, j) ∈ μ
  · have hc : ((i, j) : ℕ × ℕ) ∈ μ.cells := (YoungDiagram.mem_cells _).mpr hij
    set c : μ.cells := ⟨(i, j), hc⟩
    set s : Fin (Specht.nOf μ) := QOU.BraidKnot.SpechtStandardBasis.cellLabel T c with hsdef
    have h1 : (tableauCellEquiv μ T s : ℕ × ℕ) = ((i, j) : ℕ × ℕ) := by
      rw [hsdef, tableauCellEquiv_cellLabel]
    have h2 : (tableauCellEquiv μ T' s : ℕ × ℕ) = ((i, j) : ℕ × ℕ) := by
      rw [← hcell s, h1]
    -- entries at (i,j): both equal s.val
    have e1 : T.entry i j = s.val := by
      have := entry_tableauCellEquiv T s
      rw [h1] at this
      exact this
    have e2 : T'.entry i j = s.val := by
      have := entry_tableauCellEquiv T' s
      rw [h2] at this
      exact this
    rw [e1, e2]
  · rw [T.zero_off i j hij, T'.zero_off i j hij]

/-- **The atomic OV completeness core (Young's seminormal form, independence half) — now assembled,
not cited.** The seminormal (Gelfand–Zetlin) vectors form a **linearly independent** family indexed
by **all** standard Young tableaux of shape `μ` — i.e. `#SYT(μ) = dim S^λ`-many independent
simultaneous JM-eigenvectors.

**De-abstraction (this proof is sorry-free; its only cited input is the existence core).** The
family is built by choice from `seminormalVector_data_exists` (the eigenvector existence core);
independence is the generic joint-eigenvalue argument `linearIndependent_of_joint_eigenvectors`
(L1, proved) applied to the operators `ρ(X_s)` with eigenvalue tuples the cast content vectors
`s ↦ ((cellContent (cell of s in T) : ℤ) : k)`, whose injectivity is `Int.cast_injective`
(`CharZero`) + the combinatorial simple-spectrum fact `syt_content_tuple_injective` (L2 —
**proved**, via the diagonal row-count formula).  So the entire cited debt of this statement is
`seminormalVector_data_exists` — both the linear algebra and the spectrum combinatorics are
machine-checked.

This is strictly more atomic than the old `seminormalVectors_span` cited `sorry`: that cited the
whole inclusion `S^λ ⊆ span`; the *spanning* is a sorry-free dimension corollary
(`seminormalVectors_span` below), and the independence is now itself assembled from more atomic
parts.

**Base ring `[Field k] [CharZero k]`** (not over-general): in positive characteristic the cell
contents collide mod `p`, merging eigenspaces and breaking distinctness, so the `[CommRing k]` form
would be false at its generality. -/
theorem exists_indep_seminormal_family {k : Type} [Field k] [CharZero k] (μ : YoungDiagram) :
    ∃ b : QOU.BraidKnot.StandardYoungTableau μ → SeminormalVector (k := k) μ,
      LinearIndependent k (fun T => (b T).v) := by
  -- build the family by choice from the existence core
  choose v hmem hnz hisEig using
    fun T : QOU.BraidKnot.StandardYoungTableau μ => seminormalVector_data_exists (k := k) μ T
  refine ⟨fun T => { T := T, v := v T, mem := hmem T, nz := hnz T,
                     cellOf := tableauCellEquiv μ T, isEig := hisEig T }, ?_⟩
  -- independence via L1: operators ρ(X_s), tuples the cast content vectors
  refine linearIndependent_of_joint_eigenvectors
    (fun s : Fin (Specht.nOf μ) =>
      (Specht.Mtab.rep μ).asAlgebraHom (jucysMurphy (k := k) (Specht.nOf μ) s))
    (fun T => v T)
    (fun T s => ((cellContent ((tableauCellEquiv μ T s : ℕ × ℕ)) : ℤ) : k))
    hnz ?_ ?_
  · intro T s
    rw [hisEig T s]
    exact (Int.cast_smul_eq_zsmul k _ _).symm
  · intro T T' hTT'
    apply syt_content_tuple_injective μ T T'
    intro s
    have hs : ((cellContent ((tableauCellEquiv μ T s : ℕ × ℕ)) : ℤ) : k)
        = ((cellContent ((tableauCellEquiv μ T' s : ℕ × ℕ)) : ℤ) : k) := congrFun hTT' s
    exact_mod_cast hs

/-- **Plumbing (sorry-free): `#SYT(μ) ≤ dim_k(span)`.** The span of the independent `#SYT(μ)`-family
already has dimension `#SYT(μ)` (`finrank_span_eq_card`), and it is contained in `seminormalSpan`
(`Submodule.finrank_mono`). -/
theorem numSYT_le_finrank_seminormalSpan {k : Type} [Field k] [CharZero k] (μ : YoungDiagram) :
    numSYT μ ≤ Module.finrank k (seminormalSpan (k := k) μ) := by
  obtain ⟨b, hb⟩ := exists_indep_seminormal_family (k := k) μ
  have hsub : Submodule.span k (Set.range (fun T => (b T).v)) ≤ seminormalSpan (k := k) μ := by
    rw [seminormalSpan]
    apply Submodule.span_mono
    rintro _ ⟨T, rfl⟩
    exact ⟨b T, rfl⟩
  have hcard : Module.finrank k (Submodule.span k (Set.range (fun T => (b T).v)))
      = Fintype.card (QOU.BraidKnot.StandardYoungTableau μ) := finrank_span_eq_card hb
  have hnum : numSYT μ = Fintype.card (QOU.BraidKnot.StandardYoungTableau μ) := by
    rw [numSYT, Nat.card_eq_fintype_card]
  rw [hnum, ← hcard]
  exact Submodule.finrank_mono hsub

/-- **Seminormal vectors span the Specht module (Okounkov–Vershik) — sorry-free modulo the single
independence core `exists_indep_seminormal_family`.** The Specht submodule `S^λ ≤ M^λ` is contained in
the span of the seminormal (Gelfand–Zetlin) vectors; with the automatic reverse inclusion
`seminormalSpan_le`, the GZ vectors span `S^λ`.  This is the OV completeness consumed by the punchline
`centralC2_acts_by_contentSqSum` (the scalar action propagates from the spanning vectors by
`Submodule.span_induction`).

**De-abstraction.** `span ≤ S^λ` (`seminormalSpan_le`) plus `dim S^λ = #SYT(μ) ≤ dim(span)` (the
counting plumbing over the independence core) force `span = S^λ` on the finite-dimensional `M^λ`
(`Submodule.eq_of_le_of_finrank_le`); take `.ge`.  So the cited debt is now *independence of the
seminormal family* only — strictly more atomic than the old whole-inclusion `sorry`.

**Base ring — `[Field k] [CharZero k]` (§7c over-generality fix).** Completeness is false over `ℤ`
(seminormal vectors carry denominators ⇒ the integral vectors span only a proper finite-index
sublattice) and the independence is false in positive characteristic (contents collide mod `p`), so
the char-0 field is the honest generality.  The `[CommRing k]` form would be an over-general cited
claim — the same anti-pattern as `DominanceData.dom_colStab`; the capstone consumes the punchline at a
char-0 field `R`, so the restriction costs nothing downstream. -/
theorem seminormalVectors_span {k : Type} [Field k] [CharZero k] (μ : YoungDiagram) :
    Specht.SpechtSubmodule (k := k) μ
      ≤ Submodule.span k (Set.range (fun sv : SeminormalVector (k := k) μ => sv.v)) := by
  have hle : seminormalSpan (k := k) μ ≤ Specht.SpechtSubmodule (k := k) μ :=
    seminormalSpan_le μ
  have hfr : Module.finrank k (Specht.SpechtSubmodule (k := k) μ)
      ≤ Module.finrank k (seminormalSpan (k := k) μ) := by
    rw [SpechtFinrankWired.specht_finrank_eq_numSYT_wired]
    exact numSYT_le_finrank_seminormalSpan μ
  exact (Submodule.eq_of_le_of_finrank_le hle hfr).ge

/-- **Punchline — `C₂` acts by `Σ_{c∈λ} c(c)²` on `S^λ`.** The Jucys–Murphy central element
`C₂ = ∑_k X_k²` acts on the Specht module `S^λ ≤ M^λ` (via `Specht.Mtab.rep` extended to the group
algebra) as the **scalar** `contentSqSum μ`.  That is, for every `x ∈ S^λ`,
`ρ(C₂) · x = (contentSqSum μ) • x`.

This is the central element acting by a single eigenvalue on the irreducible `S^λ` (Schur's lemma
made explicit): since each `X_k` acts on the seminormal vector for `T` by `c(cell of k)`, the
central `∑_k X_k²` acts by `∑_k c(cell of k)² = ∑_{c∈λ} c(c)²` — independent of `T`, hence a
scalar on all of `S^λ`.  **This integer scalar `contentSqSum μ` is exactly the `ω = Σc²` field of
the keystone's `SnWedderburnSpectralData`** (`QOU.BraidKnot.RegularRepBlockTrace`); discharging
this theorem discharges that field's content for the Specht-module block.

**Sorry-free modulo the two cited OV cores.** The proof is a `Submodule.span_induction`:
the seminormal vectors span `S^λ` (`seminormalVectors_span`), `C₂` acts on each by `contentSqSum μ`
(the sorry-free `centralC2_smul_seminormal`), and the scalar action extends through `+`, `0`, and
`k`-scaling because both `ρ(C₂)` and `(contentSqSum μ) • ·` are `k`-linear.  No `sorry`, no `ℝ`,
no `native_decide`.

**Base ring `[Field k] [CharZero k]`** — inherited from `seminormalVectors_span` (the completeness it
consumes is false over `ℤ`; see that lemma).  The capstone uses this at `k := R` with
`[Field R] [CharZero R]`. -/
theorem centralC2_acts_by_contentSqSum {k : Type} [Field k] [CharZero k] (μ : YoungDiagram) :
    ∀ x ∈ Specht.SpechtSubmodule (k := k) μ,
      (Specht.Mtab.rep μ).asAlgebraHom (centralC2 (k := k) (Specht.nOf μ)) x
        = (contentSqSum μ) • x := by
  intro x hx
  -- the seminormal vectors span S^λ, so x lies in their span
  have hxspan : x ∈ Submodule.span k
      (Set.range (fun sv : SeminormalVector (k := k) μ => sv.v)) :=
    seminormalVectors_span μ hx
  -- propagate the scalar action `ρ(C₂) w = ω • w` from the spanning vectors to x by linearity,
  -- with a motive that depends *only* on span-membership (so no spurious S^λ side-goals appear)
  refine Submodule.span_induction
    (p := fun w _ => (Specht.Mtab.rep μ).asAlgebraHom (centralC2 (k := k) (Specht.nOf μ)) w
      = (contentSqSum μ) • w)
    ?_ ?_ ?_ ?_ hxspan
  · rintro w ⟨sv, rfl⟩
    exact centralC2_smul_seminormal μ sv
  · simp
  · intro a b _ _ ha hb; rw [map_add, ha, hb, smul_add]
  · intro r a _ ha; rw [map_smul, ha, smul_comm]

end QOU.BraidKnot.JucysMurphy
