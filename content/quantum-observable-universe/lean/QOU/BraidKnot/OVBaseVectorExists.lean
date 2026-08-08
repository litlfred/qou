import QOU.BraidKnot.ColSuperstandardEigen
import QOU.BraidKnot.JucysMurphy

/-!
# QOU.BraidKnot.OVBaseVectorExists — the OV base seminormal vector, existence downstream

This leaf module proves, **sorry-free and fully downstream**, the statement of
`QOU.BraidKnot.JucysMurphy.seminormalVector_base_exists` (bean `sv8b`): for *some*
standard tableau `T₀` of shape `μ` there is a nonzero simultaneous JM eigenvector in
`S^λ` whose eigenvalue at strand `s` is the content of `T₀`'s cell holding `s`.

`JucysMurphy.seminormalVector_base_exists` (JucysMurphy.lean:865) carries a `sorry`
that **cannot** be discharged in place: it is consumed at JucysMurphy:1250, while the
eigen machinery that closes it — `ColSuperstandardEigen.jm_eigen_colSuperstandard'`
(the unconditional OV eigen-equation for the column-superstandard tableau) — lives
*downstream* of `JucysMurphy` (it imports it). That is a layering inversion; removing
the in-place `sorry` needs an owner-gated file split. This module demonstrates the full
closure without touching `JucysMurphy`, by re-stating the identical `∃`-statement as
`seminormalVector_base_exists'` and proving it from the downstream ingredients.

## What is assembled here

* **`colSuperstandardSYT`** — the bridge missing from the corpus: the
  `StandardYoungTableau μ` whose `sytToTableau` image is exactly `colSuperstandard μ`.
  Its entries read off `(colSuperstandard μ).symm`; the six SYT fields are discharged
  from the `Fin` bound, `dif_neg`, injectivity of an `Equiv`, and the column-major order
  `ColSuperstandardTableau.lt_iff_colRow` (rows/columns via Young down-left closure
  `YoungDiagram.up_left_mem`).
* **`sytToTableau_colSuperstandardSYT`** — the bridge identity
  `sytToTableau (colSuperstandardSYT μ) = colSuperstandard μ`.
* **`seminormalVector_base_exists'`** — the base-existence theorem, with
  `T₀ := colSuperstandardSYT μ`, `v := Specht.polytabloid (colSuperstandard μ)`:
  membership from `polytabloid_mem_specht`, non-vanishing from the standard-polytabloid
  linear independence, and the eigen-equation from `jm_eigen_colSuperstandard'` (the
  `col • v − row • v` shape reconciled with `content • v` by `sub_smul` + `natCast_zsmul`).

-- Ref: [vershik-kerov1977] Vershik–Kerov, Young's seminormal form
-- Ref: [sagan2001] Sagan, The Symmetric Group §2.5–§3.1
-/

namespace QOU.BraidKnot.OVBaseVectorExists

open QOU.BraidKnot QOU.BraidKnot.ColSuperstandardTableau QOU.BraidKnot.ColSuperstandardEigen

variable {k : Type} [Field k] [CharZero k] {μ : YoungDiagram}

/-- **The column-superstandard standard Young tableau.** Entry `(i, j)` is the label that
`colSuperstandard μ` assigns to the cell `(i, j)` — i.e. `(colSuperstandard μ).symm ⟨(i,j)⟩`
— on the cells of `μ`, and `0` off the diagram. This is the `StandardYoungTableau` whose
`sytToTableau` image is `colSuperstandard μ` (`sytToTableau_colSuperstandardSYT`). -/
noncomputable def colSuperstandardSYT (μ : YoungDiagram) : StandardYoungTableau μ where
  entry := fun i j =>
    if h : (i, j) ∈ μ then
      (((colSuperstandard μ).symm ⟨(i, j), (YoungDiagram.mem_cells _).2 h⟩ : Fin (Specht.nOf μ)) : ℕ)
    else 0
  lt_card := by
    intro i j hij
    rw [dif_pos hij]
    exact ((colSuperstandard μ).symm ⟨(i, j), (YoungDiagram.mem_cells _).2 hij⟩).2
  zero_off := by
    intro i j hij
    rw [dif_neg hij]
  inj_on := by
    intro i j i' j' hij hij' hval
    rw [dif_pos hij, dif_pos hij'] at hval
    have hFin :
        (colSuperstandard μ).symm ⟨(i, j), (YoungDiagram.mem_cells _).2 hij⟩
          = (colSuperstandard μ).symm ⟨(i', j'), (YoungDiagram.mem_cells _).2 hij'⟩ :=
      Fin.ext hval
    have hcell :
        (⟨(i, j), (YoungDiagram.mem_cells _).2 hij⟩ : {c // c ∈ μ.cells})
          = ⟨(i', j'), (YoungDiagram.mem_cells _).2 hij'⟩ :=
      (colSuperstandard μ).symm.injective hFin
    have hpair : ((i, j) : ℕ × ℕ) = (i', j') := congrArg Subtype.val hcell
    exact ⟨(Prod.ext_iff.mp hpair).1, (Prod.ext_iff.mp hpair).2⟩
  row_strict := by
    intro i j hij1
    have hij : (i, j) ∈ μ := μ.up_left_mem (le_refl i) (Nat.le_succ j) hij1
    rw [dif_pos hij, dif_pos hij1]
    have hlt :
        (colSuperstandard μ).symm ⟨(i, j), (YoungDiagram.mem_cells _).2 hij⟩
          < (colSuperstandard μ).symm ⟨(i, j + 1), (YoungDiagram.mem_cells _).2 hij1⟩ := by
      rw [lt_iff_colRow]
      refine Or.inl ?_
      rw [Equiv.apply_symm_apply, Equiv.apply_symm_apply]
      exact Nat.lt_succ_self j
    exact hlt
  col_strict := by
    intro i j hij1
    have hij : (i, j) ∈ μ := μ.up_left_mem (Nat.le_succ i) (le_refl j) hij1
    rw [dif_pos hij, dif_pos hij1]
    have hlt :
        (colSuperstandard μ).symm ⟨(i, j), (YoungDiagram.mem_cells _).2 hij⟩
          < (colSuperstandard μ).symm ⟨(i + 1, j), (YoungDiagram.mem_cells _).2 hij1⟩ := by
      rw [lt_iff_colRow]
      refine Or.inr ⟨?_, ?_⟩
      · rw [Equiv.apply_symm_apply, Equiv.apply_symm_apply]
      · rw [Equiv.apply_symm_apply, Equiv.apply_symm_apply]
        exact Nat.lt_succ_self i
    exact hlt

/-- On the cells of `μ` the label `l = (colSuperstandard μ).symm ⟨(i,j)⟩` and the tableau
entry agree — the two ways of reading the `Equiv.apply_symm_apply` roundtrip. -/
theorem cellLabel_colSuperstandardSYT (μ : YoungDiagram) :
    SpechtStandardBasis.cellLabel (colSuperstandardSYT μ) = ⇑(colSuperstandard μ).symm := by
  funext c
  obtain ⟨⟨i, j⟩, hc⟩ := c
  apply Fin.ext
  show (colSuperstandardSYT μ).entry i j = _
  have hij : (i, j) ∈ μ := (YoungDiagram.mem_cells _).1 hc
  show (dite ((i, j) ∈ μ) _ _ : ℕ) = _
  rw [dif_pos hij]

/-- **The bridge identity (sorry-free).** `sytToTableau (colSuperstandardSYT μ)` is exactly
`colSuperstandard μ`. Since `sytToTableau T = (Equiv.ofBijective (cellLabel T) …).symm` and
`cellLabel (colSuperstandardSYT μ) = (colSuperstandard μ).symm` as maps, the two `Equiv`s
agree by `Equiv.coe_fn_injective`; a `symm_symm` finishes. -/
theorem sytToTableau_colSuperstandardSYT (μ : YoungDiagram) :
    SpechtStandardBasis.sytToTableau (colSuperstandardSYT μ) = colSuperstandard μ := by
  have hX : (colSuperstandard μ).symm
      = Equiv.ofBijective (SpechtStandardBasis.cellLabel (colSuperstandardSYT μ))
          (SpechtStandardBasis.cellLabel_bijective _) :=
    Equiv.coe_fn_injective (cellLabel_colSuperstandardSYT μ).symm
  rw [SpechtStandardBasis.sytToTableau, ← hX, Equiv.symm_symm]

/-- **OV base seminormal vector — existence, sorry-free and downstream.**

This is the statement of `QOU.BraidKnot.JucysMurphy.seminormalVector_base_exists`
(JucysMurphy.lean:865), proved here rather than in place because the eigen machinery it
needs (`ColSuperstandardEigen.jm_eigen_colSuperstandard'`) is downstream of `JucysMurphy`.

`T₀ := colSuperstandardSYT μ`, `v := Specht.polytabloid (colSuperstandard μ)`:
membership is `polytabloid_mem_specht`; non-vanishing is the standard-polytabloid linear
independence; the eigen-equation is the unconditional column-superstandard eigen-equation,
with its `col • v − row • v` right-hand side reconciled with `content • v` via `sub_smul`
and `natCast_zsmul`. -/
theorem seminormalVector_base_exists' (μ : YoungDiagram) :
    ∃ T₀ : QOU.BraidKnot.StandardYoungTableau μ,
      ∃ v : Specht.Mtab (k := k) μ,
        v ∈ Specht.SpechtSubmodule (k := k) μ ∧ v ≠ 0 ∧
          ∀ s : Fin (Specht.nOf μ),
            (Specht.Mtab.rep μ).asAlgebraHom
                (QOU.BraidKnot.JucysMurphy.jucysMurphy (k := k) (Specht.nOf μ) s) v
              = (QOU.BraidKnot.JucysMurphy.cellContent
                    ((QOU.BraidKnot.JucysMurphy.tableauCellEquiv μ T₀ s : ℕ × ℕ))) • v := by
  classical
  -- non-vanishing: the standard polytabloid of `colSuperstandardSYT μ` is a nonzero basis
  -- vector; its underlying `Mtab` element is `polytabloid (colSuperstandard μ)`.
  have hv_ne : Specht.polytabloid (k := k) (colSuperstandard μ) ≠ 0 := by
    intro h
    refine (SpechtStandardBasis.standardPolytabloid_linearIndependent (k := k) (μ := μ)).ne_zero
      (colSuperstandardSYT μ) (Subtype.ext ?_)
    show SpechtStandardBasis.standardPolytabloid (k := k) (colSuperstandardSYT μ)
        = (0 : Specht.SpechtSubmodule (k := k) μ).val
    rw [SpechtStandardBasis.standardPolytabloid, sytToTableau_colSuperstandardSYT]
    exact h
  refine ⟨colSuperstandardSYT μ, Specht.polytabloid (k := k) (colSuperstandard μ),
    Specht.polytabloid_mem_specht _, hv_ne, ?_⟩
  intro s
  -- `tableauCellEquiv μ T₀ = sytToTableau T₀ = colSuperstandard μ`.
  rw [show QOU.BraidKnot.JucysMurphy.tableauCellEquiv μ (colSuperstandardSYT μ)
        = colSuperstandard μ from sytToTableau_colSuperstandardSYT μ]
  -- unfold the content into `col − row` (as `ℤ`), then match the `ℕ`-smul difference.
  rw [QOU.BraidKnot.JucysMurphy.cellContent, sub_smul, natCast_zsmul, natCast_zsmul]
  exact jm_eigen_colSuperstandard' μ s

end QOU.BraidKnot.OVBaseVectorExists
