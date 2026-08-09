/-
  The OV base seminormal vector — existence, sorry-free.

  `JucysMurphy.seminormalVector_base_exists` is the last cited `sorry` in
  `JucysMurphy.lean` (line 875).  Every ingredient for it now exists, but it
  cannot be discharged *in place*: the proof runs through
  `ColSuperstandardEigen.jm_eigen_colSuperstandard'`, and the import chain is

    JucysMurphy → OVBaseSeminormalVector → ColSuperstandardTableau
                → ColSuperstandardEigen

  so the statement sits strictly upstream of its own proof.  This file states
  and proves the same proposition downstream, where the eigen-equation is
  available.

  Base ring `[Field k] [CharZero k]` — inherited, and genuinely required: over a
  general `CommRing` the integer cell contents can collide modulo the
  characteristic, so the prescribed content tuple need not be realised.  Do not
  generalise (AGENTS.md §7c; the `[CommRing k]` form is false at `ℤ/pℤ`).

  Refs: prop:ov-seminormal-base-vector,
        [vershik-kerov1977] Vershik–Kerov, Young's seminormal form,
        [okounkov-vershik1996] Okounkov–Vershik, A new approach to the
                               representation theory of the symmetric groups.
-/

import QOU.BraidKnot.ColSuperstandardEigen
import QOU.BraidKnot.ColSuperstandardSYT

namespace QOU.BraidKnot.SeminormalBaseExists

open QOU.BraidKnot
open QOU.BraidKnot.ColSuperstandardTableau

variable {k : Type} [Field k] [CharZero k]

/-- **The OV base seminormal vector exists — sorry-free.**

Witnesses: the column-superstandard tableau `T₀` (as an honest
`StandardYoungTableau` via `colSuperstandardSYT`), and its polytabloid
`e_{T₀}` as the eigenvector.

* membership — `Specht.polytabloid_mem_specht`;
* the eigen-equation — `jm_eigen_colSuperstandard'`, whose right-hand side
  `col(s) • e − row(s) • e` is exactly `cellContent = col − row` acting on `e`
  once the two `ℕ`-scalars are pushed into `ℤ`;
* the cell indexing — `sytToTableau_colSuperstandardSYT`, which says the SYT
  packaging reads back as the original column-superstandard filling.

This is the statement of `JucysMurphy.seminormalVector_base_exists`, proved
here rather than there because the eigen-equation is downstream of it. -/
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
  have hbridge : QOU.BraidKnot.JucysMurphy.tableauCellEquiv μ (colSuperstandardSYT μ)
      = colSuperstandard μ := sytToTableau_colSuperstandardSYT μ
  refine ⟨colSuperstandardSYT μ, Specht.polytabloid (k := k) (colSuperstandard μ),
    Specht.polytabloid_mem_specht _, ?_, ?_⟩
  · -- `e_{T₀} ≠ 0`: the standard polytabloids are linearly independent, and a member
    -- of a linearly independent family is nonzero.
    have hne := (SpechtStandardBasis.standardPolytabloid_linearIndependent
      (k := k) (μ := μ)).ne_zero (colSuperstandardSYT μ)
    intro h0
    refine hne (Subtype.ext ?_)
    show SpechtStandardBasis.standardPolytabloid (k := k) (colSuperstandardSYT μ) = 0
    rw [SpechtStandardBasis.standardPolytabloid, sytToTableau_colSuperstandardSYT]
    exact h0
  · intro s
    rw [ColSuperstandardEigen.jm_eigen_colSuperstandard', hbridge]
    rw [QOU.BraidKnot.JucysMurphy.cellContent, sub_smul, natCast_zsmul, natCast_zsmul]

end QOU.BraidKnot.SeminormalBaseExists
