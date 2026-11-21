import QOU.MassTheory.CoCasimirTau0NotDescend
import QOU.SchurWeyl.OcneanuMarkovTraceEveryZ
import QOU.SchurWeyl.OcneanuTraceFaithful

/-!
# Among Markov traces, descent to the surviving blocks forces `z_D`

`CoCasimirTau0NotDescend` shows that the symmetrising trace `τ₀` does not pass to the
convention-D surviving blocks, while every Markov trace at `z_D = q³/(q²+1)` does. This file
asks the converse question: which Markov traces pass to the surviving blocks?

**Answer: only the one at `z_D`.** Let `T` be a Markov trace family on the Hecke tower with an
arbitrary parameter `z`. On `H_3(q)` suppose that

* `T` vanishes on every element supported off the surviving blocks (it passes to the
  surviving-block algebra), and
* `T` is nonzero on a primitive idempotent of every surviving block (it is nondegenerate there).

Then `z = q³/(q²+1)` (`markov_descends_forces_zD`). The converse holds as well, so this is an
iff (`markov_descends_iff_zD`).

Proof sketch. Every Markov trace at `z` is the `ocneanuWeight q z`-weighted seminormal trace
(`eq_ocneanuWtrace_of_markov`), so `T(e_{λ,i}) = w_λ(z)`. The column block `(1³)` is
supported off the surviving blocks, so `w_{(1³)}(z) = 0`. Its numerator is the product of the
cell factors `q^{2i}(q² − 1 − qz) + qz` for `i = 0, 1, 2`. These equal `q² − 1`,
`q(q² − 1)(q − z)` and `q(q² − 1)(q³ − (q² + 1)z)`. So `z = q` or `z = z_D`. At `z = q` the
factor of the cell `(1, 0)` vanishes, which kills every two-row block, contradicting
nondegeneracy. Hence `z = z_D`.

## Why the Markov condition is needed

The surviving-block algebra is a product of matrix algebras, one per surviving block, so its
traces form a space with one free scalar per block. A trace of the surviving-block algebra that
is not a Markov trace can therefore assign each block any per-simple weight. The uniqueness here
comes from the Markov tower condition (`tr_incl`, `tr_markov`), not from descent alone.

## What this gives for Term 4

Together with `quantumDim_primIdem_twoRow`: among Markov traces on the Hecke tower, exactly one
passes to the surviving blocks and is nondegenerate there. Its per-simple weight on a two-row
block `(m, k)` is the `sl₂` dimension `[m − k + 1]_q`. The hook `dim_q` is the weight of `τ₀`,
which is not a trace of the surviving-block algebra. Whether Term 4 must be built from a Markov
trace of the surviving-block algebra is the modelling ruling on issue #8109; this file does not
decide it.

## Base ring (§7c)

Generic `[Field K]`, `q ≠ 0`, `q` not a root of unity. No ordering, no `ℝ`.

LaTeX label: `thm:cocasimir-markov-descent-forces-zd`
-/

namespace QOU.MassTheory.CoCasimirHecke

open Finset QOU.SchurWeyl QOU.MassTheory.CoCasimirSurviving
open QOU.Mathlib (StandardYoungTableau partitionShape)

noncomputable section

open Classical

/-- The two-row partition `(2, 1)` of `3`. -/
def partitionTwoOne : Nat.Partition 3 where
  parts := {2, 1}
  parts_pos := fun h => by
    simp only [Multiset.insert_eq_cons, Multiset.mem_cons, Multiset.mem_singleton] at h
    omega
  parts_sum := by decide

theorem colLen_zero_partitionTwoOne : (partitionShape partitionTwoOne).colLen 0 = 2 := by
  rw [colLen_zero_partitionShape]
  rfl

variable {K : Type*} [Field K]
variable (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)

/-- **Every Markov trace at `z` gives a primitive idempotent its Ocneanu weight.** -/
theorem markovZ_primIdem {z : K} (T : HeckeCoset.MarkovTraceFamily K q q⁻¹ z) (n : ℕ)
    (lam : Nat.Partition (n + 1)) (i : Fin (dim n lam)) :
    T.tr n (primIdem q hq0 hq2 n lam i) = ocneanuWeight q z (partitionShape lam) := by
  rw [SeminormalRep.eq_ocneanuWtrace_of_markov q hq0 hq2 (gen_of_notRootOfUnity hq2) z T,
    wtraceW_primIdem]

/-- A diagram with three cells and three rows is the column `{(0,0), (1,0), (2,0)}`. -/
theorem cells_eq_column_of_three {μ : YoungDiagram} (hcard : μ.cells.card = 3)
    (hrows : μ.colLen 0 = 3) :
    μ.cells = {(0, 0), (1, 0), (2, 0)} := by
  have hsub : ({(0, 0), (1, 0), (2, 0)} : Finset (ℕ × ℕ)) ⊆ μ.cells := by
    intro c hc
    simp only [Finset.mem_insert, Finset.mem_singleton] at hc
    rw [YoungDiagram.mem_cells]
    rcases hc with rfl | rfl | rfl <;> rw [YoungDiagram.mem_iff_lt_colLen] <;> omega
  exact (Finset.eq_of_subset_of_card_le hsub (by rw [hcard]; decide)).symm

include hq0 hq2 in
/-- **Descent plus nondegeneracy forces `z_D`.** A Markov trace family at parameter `z` that
vanishes on `H_3(q)` off the surviving blocks, and is nonzero on a primitive idempotent of
every surviving block of `H_3(q)`, has `z = q³/(q²+1)`. -/
theorem markov_descends_forces_zD {z : K} (T : HeckeCoset.MarkovTraceFamily K q q⁻¹ z)
    (hdesc : ∀ x : Hecke K q q⁻¹ 2, OffSurviving q hq0 hq2 2 x → T.tr 2 x = 0)
    (hfaith : ∀ (lam : Nat.Partition 3), (partitionShape lam).colLen 0 ≤ 2 →
      ∀ i : Fin (dim 2 lam), T.tr 2 (primIdem q hq0 hq2 2 lam i) ≠ 0) :
    z = q ^ 3 / (q ^ 2 + 1) := by
  have hsq : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr (GenericParameter.sq_ne_one hq2)
  have hq21 : q ^ 2 + 1 ≠ 0 := GenericParameter.sq_add_one_ne_zero hq2
  have hgen := gen_of_notRootOfUnity hq2
  -- the column block `(1³)` is killed
  set col := columnPartition 3
  have hcol3 : (partitionShape col).colLen 0 = 3 := colLen_zero_columnPartition 3
  have i0 : Fin (dim 2 col) := ⟨0, dim_pos 2 col⟩
  have hzero := hdesc _ (primIdem_offSurviving q hq0 hq2 2 col i0 (by omega))
  rw [markovZ_primIdem] at hzero
  rw [ocneanuWeight, div_eq_zero_iff] at hzero
  rcases hzero with hnum | hden
  swap
  · exact absurd hden (ocneanuDen_ne_zero hgen _)
  rw [cells_eq_column_of_three (QOU.Mathlib.partitionShape_card col) hcol3] at hnum
  rw [Finset.prod_insert (by decide), Finset.prod_insert (by decide),
    Finset.prod_singleton] at hnum
  rcases mul_eq_zero.mp hnum with h0 | h12
  rotate_left
  rcases mul_eq_zero.mp h12 with h1 | h2
  rotate_left 2
  · -- cell (0,0): the factor is `q² − 1`
    exact absurd (by linear_combination h0) hsq
  · -- cell (1,0): `z = q`, which kills the two-row block `(2,1)`
    have hz : z = q := by
      have h' : q * (q ^ 2 - 1) * (q - z) = 0 := by linear_combination h1
      rcases mul_eq_zero.mp h' with h'' | h''
      · exact absurd h'' (mul_ne_zero hq0 hsq)
      · exact (sub_eq_zero.mp h'').symm
    exfalso
    set lam := partitionTwoOne
    have j0 : Fin (dim 2 lam) := ⟨0, dim_pos 2 lam⟩
    apply hfaith lam (by rw [colLen_zero_partitionTwoOne]) j0
    rw [markovZ_primIdem, ocneanuWeight, hz]
    refine div_eq_zero_iff.mpr (Or.inl (Finset.prod_eq_zero (i := (1, 0)) ?_ ?_))
    · rw [YoungDiagram.mem_cells, YoungDiagram.mem_iff_lt_colLen, colLen_zero_partitionTwoOne]
      omega
    · ring
  · -- cell (2,0): `z = z_D`
    have h' : q * (q ^ 2 - 1) * (q ^ 3 - (q ^ 2 + 1) * z) = 0 := by linear_combination h2
    rcases mul_eq_zero.mp h' with h'' | h''
    · exact absurd h'' (mul_ne_zero hq0 hsq)
    · field_simp
      linear_combination -h''

include hq0 hq2 in
/-- **The iff.** A Markov trace family at parameter `z` passes to the surviving blocks of
`H_3(q)` and is nondegenerate there exactly when `z = q³/(q²+1)`. -/
theorem markov_descends_iff_zD {z : K} (T : HeckeCoset.MarkovTraceFamily K q q⁻¹ z) :
    ((∀ x : Hecke K q q⁻¹ 2, OffSurviving q hq0 hq2 2 x → T.tr 2 x = 0)
      ∧ ∀ (lam : Nat.Partition 3), (partitionShape lam).colLen 0 ≤ 2 →
        ∀ i : Fin (dim 2 lam), T.tr 2 (primIdem q hq0 hq2 2 lam i) ≠ 0)
      ↔ z = q ^ 3 / (q ^ 2 + 1) := by
  constructor
  · rintro ⟨hdesc, hfaith⟩
    exact markov_descends_forces_zD q hq0 hq2 T hdesc hfaith
  · rintro rfl
    have hq21 := GenericParameter.sq_add_one_ne_zero hq2
    have hgen := gen_of_notRootOfUnity hq2
    refine ⟨fun x hx => markov_eq_zero_of_offSurviving q hq0 hq2 2 T x hx, ?_⟩
    intro lam hlam i
    rw [markov_primIdem]
    exact (wD_ne_zero_iff q hq0 2 hq21 hgen lam).mpr hlam

end

end QOU.MassTheory.CoCasimirHecke
