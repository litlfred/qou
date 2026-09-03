/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MassTheory.TwoRowCapDerived

/-!
# The self-conjugate stratum of the mass channel is empty past four cells

## What this explains

`computations/probes/gram_norm_binding_probe.py` decomposes the operator-space
Gram norm `G(W) = ∑_λ y_λ · tr(ρ_λ(W) ρ_λ(W^♯))` into per-block contributions
and reports the **self-conjugate share** — the fraction of `G` carried by the
bar-fixed blocks `λ = λ'`, since bar sends `e_λ ↦ e_λ'`
(`prop:hecke-baer-star-generic`).

That share prints as `0.0000` for every isotope the probe runs: ²H (`n = 6`),
³H and ³He (`n = 9`), ⁴He (`n = 12`). Read from a float64 probe alone that is
an *observation*, and a weak one — a share could be small for numerical
reasons, or zero by an accident of the particular braid words chosen. It is
neither. It is forced, for every `n ≥ 5`, by the two-row cap, and this file
proves it.

## The argument

Convention D caps the mass channel at two rows: a nonzero Wenzl/Ocneanu weight
forces `ℓ(λ) ≤ 2` (`TwoRowCap.colLen_le_two_of_massWeight_ne_zero_of_wenzl`,
itself derived from `schurPrincipal_eq_zero_iff` rather than posited).

A self-conjugate diagram has `rowLen 0 = colLen 0`. Capping the column length
at two therefore caps the *row* length at two as well, so the whole diagram is
confined to the `2 × 2` box and cannot hold more than four cells.

So for `n ≥ 5` there is no diagram that is both self-conjugate and carries a
nonzero weight, and the self-conjugate stratum of any weighted Wedderburn sum
is empty — not small, empty. The probe's `0.0000` is that emptiness.

## Sharpness

The bound is attained, so none of this is vacuous: `(2,2)` is self-conjugate,
has column length two, and has exactly four cells — the diagram the corpus
already singles out as the unique self-conjugate partition of four
(`QOU.Archimedean.EHartreeTraceRatio.unique_self_conjugate_partition_of_four`).
`selfConjugate_two_two` below exhibits it, so `card_le_four_…` is a statement
about a nonempty class with an extremal member, not an empty one.

## Scope

This constrains the **self-conjugate share** only. The probe's companion
`chiral_anti_share = 0.5000` is a *different* claim — it needs every nonzero
`c_λ` to share a sign — and is **not** proved here. Do not read this file as
covering it.
-/

namespace QOU.MassTheory.SelfConjugateStratum

open YoungDiagram

/-- A self-conjugate diagram has equal first row and first column lengths.
`μ.transpose.rowLen 0 = μ.colLen 0` always; self-conjugacy rewrites the left. -/
theorem rowLen_zero_eq_colLen_zero_of_selfConjugate
    (μ : YoungDiagram) (hsc : μ.transpose = μ) :
    μ.rowLen 0 = μ.colLen 0 := by
  conv_lhs => rw [← hsc]
  exact μ.rowLen_transpose 0

/-- A self-conjugate diagram capped at two rows sits inside the `2 × 2` box:
every cell has both coordinates `< 2`. -/
theorem cell_lt_two_of_selfConjugate_of_colLen_le_two
    (μ : YoungDiagram) (hsc : μ.transpose = μ) (hcol : μ.colLen 0 ≤ 2)
    (c : ℕ × ℕ) (hc : c ∈ μ.cells) :
    c.1 < 2 ∧ c.2 < 2 := by
  have hmem : (c.1, c.2) ∈ μ := by simpa using (mem_cells (μ := μ) c).mp hc
  constructor
  · -- the row index is bounded by the FIRST column's length (columns shrink)
    have h1 : c.1 < μ.colLen c.2 := mem_iff_lt_colLen.mp hmem
    have h2 : μ.colLen c.2 ≤ μ.colLen 0 := μ.colLen_anti 0 c.2 (Nat.zero_le _)
    omega
  · -- the column index is bounded by the FIRST row's length (rows shrink),
    -- and self-conjugacy turns that back into the column bound
    have h1 : c.2 < μ.rowLen c.1 := mem_iff_lt_rowLen.mp hmem
    have h2 : μ.rowLen c.1 ≤ μ.rowLen 0 := μ.rowLen_anti 0 c.1 (Nat.zero_le _)
    have h3 : μ.rowLen 0 = μ.colLen 0 :=
      rowLen_zero_eq_colLen_zero_of_selfConjugate μ hsc
    omega

/-- **Main bound.** A self-conjugate diagram surviving the two-row cap has at
most four cells. -/
theorem card_le_four_of_selfConjugate_of_colLen_le_two
    (μ : YoungDiagram) (hsc : μ.transpose = μ) (hcol : μ.colLen 0 ≤ 2) :
    μ.card ≤ 4 := by
  have hsub : μ.cells ⊆ (Finset.range 2) ×ˢ (Finset.range 2) := by
    intro c hc
    simp only [Finset.mem_product, Finset.mem_range]
    exact cell_lt_two_of_selfConjugate_of_colLen_le_two μ hsc hcol c hc
  calc μ.card = μ.cells.card := rfl
    _ ≤ ((Finset.range 2) ×ˢ (Finset.range 2)).card := Finset.card_le_card hsub
    _ = 4 := by simp

/-- Contrapositive, in the form the Wedderburn sums consume: past four cells a
two-row diagram is **never** self-conjugate. -/
theorem not_selfConjugate_of_colLen_le_two_of_five_le_card
    (μ : YoungDiagram) (hcol : μ.colLen 0 ≤ 2) (h5 : 5 ≤ μ.card) :
    μ.transpose ≠ μ := by
  intro hsc
  have := card_le_four_of_selfConjugate_of_colLen_le_two μ hsc hcol
  omega

/-- **The mass-channel statement.** For `n ≥ 5`, a self-conjugate diagram
carries weight exactly zero — so the self-conjugate stratum of `∑_λ y_λ · χ_λ`
contributes nothing at all. This is the probe's `selfconj_share = 0.0000` at
`n = 6, 9, 12`, and it holds for every `n ≥ 5`, not just those three. -/
theorem massWeight_eq_zero_of_selfConjugate_of_five_le_card
    {R : Type*} [Field R] {Q Z : R} (hQ0 : Q ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (hZ : Z ≠ 0) (μ : YoungDiagram)
    (hsc : μ.transpose = μ) (h5 : 5 ≤ μ.card) :
    QOU.QBeta.WenzlWeight.schurPrincipal 2 Q μ / Z = 0 := by
  by_contra hne
  have hcol : μ.colLen 0 ≤ 2 :=
    QOU.MassTheory.TwoRowCap.colLen_le_two_of_massWeight_ne_zero_of_wenzl
      hQ0 hQ hZ μ hne
  exact not_selfConjugate_of_colLen_le_two_of_five_le_card μ hcol h5 hsc

/-! ## Sharpness — the bound is attained, so nothing above is vacuous -/

/-- The `2 × 2` box — the diagram `(2,2)`, written as the box it is. -/
def box2 : YoungDiagram where
  cells := (Finset.range 2) ×ˢ (Finset.range 2)
  isLowerSet := by
    intro a b hba ha
    simp only [Finset.coe_product, Set.mem_prod, Finset.coe_range,
      Set.mem_Iio] at ha ⊢
    exact ⟨lt_of_le_of_lt hba.1 ha.1, lt_of_le_of_lt hba.2 ha.2⟩

theorem box2_transpose : box2.transpose = box2 := by
  ext c
  simp [box2, YoungDiagram.transpose, and_comm]

theorem box2_colLen_le_two : box2.colLen 0 ≤ 2 := by
  have hb : ∀ i, (i, 0) ∈ box2 ↔ i < 2 := by
    intro i; simp [box2, YoungDiagram.mem_mk]
  by_contra hc
  have h2 : (2, 0) ∈ box2 := mem_iff_lt_colLen.mpr (by omega)
  exact absurd ((hb 2).mp h2) (by omega)

theorem box2_card : box2.card = 4 := by simp [YoungDiagram.card, box2]

/-- `(2,2)` is self-conjugate, has column length two, and has four cells. It
is therefore an **extremal** witness for `card_le_four_…`: the bound is
attained and cannot be lowered to three, so that theorem is a statement about
a nonempty class rather than a vacuous one. -/
theorem selfConjugate_two_two :
    ∃ μ : YoungDiagram, μ.transpose = μ ∧ μ.colLen 0 ≤ 2 ∧ μ.card = 4 :=
  ⟨box2, box2_transpose, box2_colLen_le_two, box2_card⟩

end QOU.MassTheory.SelfConjugateStratum
