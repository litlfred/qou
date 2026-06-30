import Mathlib.RingTheory.SimpleModule.WedderburnArtin
import Mathlib.RingTheory.SimpleModule.IsAlgClosed
import Mathlib.LinearAlgebra.Pi
import Mathlib.LinearAlgebra.Projection
import Mathlib.LinearAlgebra.Trace
import Mathlib.LinearAlgebra.Dimension.Finrank
import Mathlib.LinearAlgebra.FreeModule.Finite.Matrix
import Mathlib.Algebra.Algebra.Equiv
import Mathlib.Algebra.Algebra.Pi
import QOU.BraidKnot.WedderburnSn
import QOU.BraidKnot.SpechtClassification
import QOU.BraidKnot.RegularRepBlockTrace

/-!
# QOU.BraidKnot.SnWedderburnPartitionBridge — the partition-indexed isotypic projection family

The OV capstone (`OVTopAssembly.snBlocks`) needs a **partition-indexed** projection family of the
symmetric-group algebra `R[S_n]` over a general characteristic-zero field `R`: a family of
projections `proj i` (`i : SpechtClassification.PartitionIndex n`) onto blocks `p i` of
`R`-dimension `(dim Sᵘ)²`, summing to the identity. In `OVTopAssembly` this is a single opaque cited
`sorry` (`snBlocks`). This file **de-abstracts** that gap: it isolates the *one*
`S_n`-representation-theory fact genuinely absent from the pinned Mathlib, and discharges
**everything else** — the entire passage from a Wedderburn `∏ Matrix` algebra-equivalence to the
projection bundle — by sorry-free linear algebra.

This mirrors the merged `SpechtDominanceCore` / `exists_linearOrder_of_partialOrder` lever pattern:
a precisely-named structural core, with all the surrounding plumbing proved.

## What is sorry-free here

* **The mechanical extraction `snBlocks_of_algEquiv`** (the payoff). Given *any* `R`-algebra
  isomorphism `e : R[S_n] ≃ₐ[R] ∏ᵢ Matrix(Fin dᵢ) R`, it produces the full `snBlocks` bundle: the
  coordinate idempotents pulled back along `e` are projections (`IsProj`) onto blocks of
  `R`-dimension `dᵢ²`, and they sum to the identity. This is the bulk of the gap and it is pure
  linear algebra — `transProj_*` + `coordProj_*` + `finrank_range_*` below.
* **The assembled bridge `snBridge`** — the `snBlocks`-shaped existence theorem, sorry-free *modulo*
  the single named core. This is exactly what `OVTopAssembly.snBlocks` consumes.

## The one named core (the genuine `S_n`-rep-theory gap)

* `sn_rational_specht_split` — over a characteristic-zero field `R`, the **rational, OV-labelled**
  Wedderburn decomposition of `R[S_n]`:
  `R[S_n] ≃ₐ[R] ∏_{i:PartitionIndex n} Matrix(Fin (dim S^{λ_i})) R`,
  with block `i` the `S^{λ_i}`-isotypic component (matrix size `= dim_R S^{λ_i}`). This single
  statement folds in the three pieces of content absent from the pinned Mathlib:
  - **(a) ℚ-rationality / absolute irreducibility.** The division rings collapse to `R` itself —
    `S_n`-representations are defined over `ℚ`, so no genuine division-ring factors appear. Mathlib
    has the matrix-product form only for an **algebraically closed** base
    (`WedderburnSn.sn_wedderburnArtin_algClosed`); the char-0 (Maschke + rationality) descent is the
    missing input.
  - **(b) the partition labelling** of the block set (`SpechtClassification.PartitionIndex n`).
  - **(c) the Okounkov–Vershik identification** of block `i` with `S^{λ_i}` — matrix size
    `= dim_R S^{λ_i} = #SYT(λ_i)`.
  `-- Ref: [james1984representation], [sagan2001]`.

> **Why one core, not two (over-generality note).** An earlier shape split this into
> `sn_absolutelyIrreducible_charZero` (a partition-indexed split with *abstract* sizes `d`) plus
> `sn_block_dim_eq_specht` (`d i = dim S^{λ_i}`). The second is **false as a ∀-over-splits claim**:
> the index→block assignment of an arbitrary partition-indexed split is fixed only up to a
> permutation (Wedderburn determines the *multiset* of block sizes, not the labelling), so a
> relabeled split can have `d i ≠ dim S^{λ_i}` (e.g. at `n = 6`, swap the size-1 and size-5 blocks).
> Folding the alignment into the single existential `sn_rational_specht_split` — which asserts the
> *aligned* split exists, a true statement — is the honest disposition; it avoids planting an
> over-general cited `sorry` (cf. the `DominanceData.dom_colStab` / `seminormalVectors_span`
> over-generality fixes).

## Whether Mathlib offers any `S_n`-rationality support

It does **not**. Mathlib (pinned v4.24.0) provides the *abstract* Wedderburn–Artin theorem
(`IsSemisimpleRing.exists_ringEquiv_pi_matrix_divisionRing`) and its algebraically-closed
specialisation (`…_of_isAlgClosed`, where division rings collapse to the base field by Schur +
algebraic closure), but **nothing** about the rationality of the symmetric group's representations —
no statement that `S_n`-irreducibles are defined over `ℚ`, no Specht-module ↔ Wedderburn-block
identification, no `dim(λ) = #SYT(λ)` at the block level. The core is therefore genuine.

## Base ring (§7c)

`variable {R : Type} [Field R] [CharZero R]` for the rep-theory layer: `Field` is what the Wedderburn
decomposition needs; `CharZero` is what the char-0 rationality (Maschke) and the brick-3
classification need. The mechanical §1 is over a generic `[CommRing R]` / `[Field R]` — pure linear
algebra. No `ℝ`, no `Real.*`, no ordering on `R`: the construction is algebraic.

## References
- [james1984representation] James, *The Representation Theory of the Symmetric Groups* (Specht
  modules; rationality / absolute irreducibility over ℚ).
- [sagan2001] Sagan, *The Symmetric Group*, §2.4 (the Specht modules are a complete set of simple
  `k[S_n]`-modules in char 0; the partition labelling; `dim S^λ = #SYT(λ)`).
- [manuscript] content/.../BraidKnot/OVTopAssembly.lean (`snBlocks`, the gap this file fills).
-/

open scoped BigOperators

namespace QOU.BraidKnot.SnWedderburnPartitionBridge

open QOU.BraidKnot

-- Several mechanical lemmas carry section typeclasses (`[Fintype ι]`, `Module.Finite`/`Free`,
-- `[CharZero R]`) that document the intended use-site but are not all used by every individual
-- declaration; keep them (they match the shared `variable` blocks and the capstone interface) and
-- silence the unused-section-variable linter for the file rather than fragmenting the binders.
set_option linter.unusedSectionVars false

/-! ## 1. Mechanical extraction: projections from an algebra `∏ Matrix` decomposition

Everything in this section is **pure linear algebra over a commutative ring** (no `S_n`, no
char-0): from an `R`-linear isomorphism `e : A ≃ₗ[R] ∏ⱼ Bⱼ`, the coordinate idempotents on the
product pull back to a complete family of projections on `A`, with the right ranks. -/

section Mechanical

variable {R : Type} [CommRing R] {ι : Type} [Fintype ι] [DecidableEq ι]
  {B : ι → Type} [∀ i, AddCommGroup (B i)] [∀ i, Module R (B i)]

/-- The `i`-th **coordinate idempotent** on `∏ⱼ Bⱼ`: zero out every coordinate but `i`. -/
noncomputable def coordProj (i : ι) : (∀ j, B j) →ₗ[R] (∀ j, B j) :=
  (LinearMap.single R B i) ∘ₗ (LinearMap.proj i)

theorem coordProj_idem (i : ι) :
    (coordProj (R := R) (B := B) i) ∘ₗ (coordProj (R := R) (B := B) i)
      = coordProj (R := R) (B := B) i := by
  ext x j; simp [coordProj]

theorem coordProj_sum : (∑ i, coordProj (R := R) (B := B) i) = LinearMap.id := by
  ext x j; simp [coordProj]

theorem range_coordProj (i : ι) :
    LinearMap.range (coordProj (R := R) (B := B) i) = LinearMap.range (LinearMap.single R B i) := by
  apply le_antisymm
  · rintro x ⟨y, rfl⟩
    exact ⟨(LinearMap.proj i) y, rfl⟩
  · rintro x ⟨b, rfl⟩
    refine ⟨LinearMap.single R B i b, ?_⟩
    simp only [coordProj, LinearMap.comp_apply, LinearMap.proj_apply, LinearMap.single_apply,
      Pi.single_eq_same]

/-- `LinearMap.single R B i` is injective (it is a section of `proj i`). -/
theorem single_inj (i : ι) : Function.Injective (LinearMap.single R B i) := by
  intro a b h
  have h2 := congrFun (congrArg (fun f => f) h) i
  simpa [LinearMap.single_apply] using h2

section Field

variable {R : Type} [Field R] {ι : Type} [Fintype ι] [DecidableEq ι]
  {B : ι → Type} [∀ i, AddCommGroup (B i)] [∀ i, Module R (B i)]
  [∀ i, Module.Finite R (B i)] [∀ i, Module.Free R (B i)]
  {A : Type} [AddCommGroup A] [Module R A]

theorem finrank_range_coordProj (i : ι) :
    Module.finrank R (LinearMap.range (coordProj (R := R) (B := B) i)) = Module.finrank R (B i) := by
  rw [range_coordProj, LinearMap.finrank_range_of_inj (single_inj i)]

/-- **The pulled-back idempotent** `e.symm ∘ coordProj i ∘ e : A →ₗ[R] A`. -/
noncomputable def transProj (e : A ≃ₗ[R] (∀ j, B j)) (i : ι) : A →ₗ[R] A :=
  (e.symm : (∀ j, B j) →ₗ[R] A) ∘ₗ (coordProj (R := R) (B := B) i) ∘ₗ (e : A →ₗ[R] (∀ j, B j))

theorem transProj_idem (e : A ≃ₗ[R] (∀ j, B j)) (i : ι) :
    (transProj e i) ∘ₗ (transProj e i) = transProj e i := by
  ext x
  simp only [transProj, LinearMap.comp_apply, LinearEquiv.coe_coe, LinearEquiv.apply_symm_apply]
  congr 1
  have hidem : (coordProj (R := R) (B := B) i) ∘ₗ (coordProj (R := R) (B := B) i)
      = coordProj (R := R) (B := B) i := coordProj_idem i
  have : (coordProj (R := R) (B := B) i ∘ₗ coordProj (R := R) (B := B) i) (e x)
      = coordProj (R := R) (B := B) i (e x) := by rw [hidem]
  simpa [LinearMap.comp_apply] using this

/-- The pulled-back idempotent is a **projection** onto its range. -/
theorem transProj_isProj (e : A ≃ₗ[R] (∀ j, B j)) (i : ι) :
    LinearMap.IsProj (LinearMap.range (transProj e i)) (transProj e i) := by
  refine ⟨fun x => ⟨x, rfl⟩, ?_⟩
  intro x hx
  obtain ⟨y, rfl⟩ := hx
  have h2 : (transProj e i ∘ₗ transProj e i) y = transProj e i y := by rw [transProj_idem e i]
  simpa using h2

/-- The pulled-back projections **sum to the identity** (the blocks exhaust `A`). -/
theorem transProj_sum (e : A ≃ₗ[R] (∀ j, B j)) :
    (∑ i, transProj e i) = LinearMap.id := by
  have hsum : (∑ i, coordProj (R := R) (B := B) i) = LinearMap.id := coordProj_sum
  ext x
  simp only [LinearMap.coeFn_sum, Finset.sum_apply, transProj, LinearMap.comp_apply,
    LinearEquiv.coe_coe, LinearMap.id_coe, id_eq]
  rw [← map_sum]
  have : (∑ i, coordProj (R := R) (B := B) i (e x)) = (∑ i, coordProj (R := R) (B := B) i) (e x) := by
    rw [LinearMap.coeFn_sum, Finset.sum_apply]
  rw [this, hsum]
  simp

/-- **The `R`-dimension of the `i`-th pulled-back block** equals `finrank R (B i)`: conjugation by a
linear equiv preserves rank, and the coordinate-block range is `≃ₗ B i`. -/
theorem finrank_range_transProj (e : A ≃ₗ[R] (∀ j, B j)) (i : ι) :
    Module.finrank R (LinearMap.range (transProj e i)) = Module.finrank R (B i) := by
  -- range(e.symm ∘ coordProj ∘ e) = map e.symm (range (coordProj ∘ e)) = map e.symm (range coordProj)
  rw [transProj, LinearMap.range_comp, LinearMap.range_comp, LinearEquiv.range, Submodule.map_top]
  -- `map e.symm (range coordProj) ≃ₗ range coordProj` (e.symm injective) preserves finrank, then
  -- `finrank (range coordProj) = finrank (B i)`.
  refine Eq.trans ?_ (finrank_range_coordProj (R := R) (B := B) i)
  exact (Submodule.equivMapOfInjective (e.symm : (∀ j, B j) →ₗ[R] A) e.symm.injective
    (LinearMap.range (coordProj (R := R) (B := B) i))).symm.finrank_eq

end Field

end Mechanical

/-! ## 2. The single `S_n`-rep-theory core -/

variable {R : Type} [Field R] [CharZero R]

/-- **Named core (the genuine `S_n`-rep-theory gap).** Over a characteristic-zero field `R`, the
**rational, OV-labelled** Wedderburn decomposition of `R[S_n]`, indexed by the partitions of `n`,
with block `i` of matrix size exactly `dim_R S^{λ_i}`:
`R[S_n] ≃ₐ[R] ∏_{i:PartitionIndex n} Matrix(Fin (dim S^{λ_i})) R`.

This one existential folds in the three pieces of content absent from the pinned Mathlib:
(a) the division rings collapse to `R` — `S_n` is split over `ℚ` (absolute irreducibility), so no
genuine division-ring factors appear (Mathlib has the matrix product only for an algebraically
closed base, `WedderburnSn.sn_wedderburnArtin_algClosed`); (b) the block set is the partitions of
`n`; (c) block `i` is the `S^{λ_i}`-isotypic component, whose matrix size is `dim_R S^{λ_i}` (the
Okounkov–Vershik labelling). It is stated as the *aligned* split (sizes `= dim S^{λ_i}` pointwise),
not "some split with abstract sizes `d`", precisely so that no over-general `∀`-over-splits
side-claim is needed (see the file header). -/
theorem sn_rational_specht_split (n : ℕ) :
    Nonempty (MonoidAlgebra R (Equiv.Perm (Fin n)) ≃ₐ[R]
      (∀ i : SpechtClassification.PartitionIndex n,
        Matrix (Fin (Module.finrank R (Specht.SpechtSubmodule (k := R) i.diagram)))
               (Fin (Module.finrank R (Specht.SpechtSubmodule (k := R) i.diagram))) R)) := by
  -- Ref: [james1984representation] (the irreducible representations of S_n are defined over ℚ, hence
  --   absolutely irreducible: ℚ[S_n] — and a fortiori R[S_n] for any char-0 R — splits as a product
  --   of full matrix algebras ∏ Matrix(Fin dᵢ) R, with NO non-commutative division-ring factors;
  --   Mathlib gives the matrix product only over an algebraically closed field) +
  --   [sagan2001] §2.4 (the blocks are indexed by partitions of n, and block λ is the S^λ-isotypic
  --   component of matrix size dim_R S^λ = #SYT(λ) — the Okounkov–Vershik labelling).
  sorry

/-! ## 3. The mechanical payoff: `snBlocks` from any partition-indexed algebra split -/

/-- **The full `snBlocks` bundle from an algebra `∏ Matrix` decomposition (sorry-free).** Given *any*
`R`-algebra isomorphism `e : R[S_n] ≃ₐ[R] ∏_{i:PartitionIndex n} Matrix(Fin dᵢ) R`, the coordinate
idempotents pulled back along `e` form a complete family of projections onto blocks of `R`-dimension
`dᵢ²`. This is the entire content of `OVTopAssembly.snBlocks` *except* the choice of `e` (with
`dᵢ = dim S^{λ_i}`) — i.e. the bulk of the gap, discharged by pure linear algebra. -/
theorem snBlocks_of_algEquiv (n : ℕ)
    (d : SpechtClassification.PartitionIndex n → ℕ)
    (e : MonoidAlgebra R (Equiv.Perm (Fin n)) ≃ₐ[R]
      (∀ i : SpechtClassification.PartitionIndex n, Matrix (Fin (d i)) (Fin (d i)) R)) :
    ∃ (p : SpechtClassification.PartitionIndex n →
          Submodule R (MonoidAlgebra R (Equiv.Perm (Fin n))))
      (proj : SpechtClassification.PartitionIndex n →
          Module.End R (MonoidAlgebra R (Equiv.Perm (Fin n)))),
      (∀ i, LinearMap.IsProj (p i) (proj i)) ∧
      (∀ i, Module.finrank R (p i) = (d i) ^ 2) ∧
      (∑ i, proj i = LinearMap.id) := by
  classical
  -- The R-linear part of the algebra equivalence.
  let eL : MonoidAlgebra R (Equiv.Perm (Fin n)) ≃ₗ[R]
      (∀ i : SpechtClassification.PartitionIndex n, Matrix (Fin (d i)) (Fin (d i)) R) :=
    e.toLinearEquiv
  refine ⟨fun i => LinearMap.range (transProj (B := fun i => Matrix (Fin (d i)) (Fin (d i)) R) eL i),
          fun i => transProj (B := fun i => Matrix (Fin (d i)) (Fin (d i)) R) eL i, ?_, ?_, ?_⟩
  · -- isProj
    intro i; exact transProj_isProj eL i
  · -- finrank of block i = (d i)^2
    intro i
    rw [finrank_range_transProj eL i]
    rw [Module.finrank_matrix, Module.finrank_self, mul_one, Fintype.card_fin, sq]
  · -- Σ proj = id
    exact transProj_sum eL

/-! ## 4. The assembled bridge — `OVTopAssembly.snBlocks`-shaped, sorry-free modulo the one core -/

/-- **THE BRIDGE.** The partition-indexed isotypic projection family of `R[S_n]` over a
characteristic-zero field `R`: projections `proj i` onto blocks `p i` of `R`-dimension
`(dim S^{λ_i})²`, summing to the identity. Stated **exactly** as `OVTopAssembly.snBlocks`, so that
the capstone can replace its opaque cited `sorry` by `exact … snBridge n`.

**Sorry-free modulo the one named core** `sn_rational_specht_split` (the rational + OV-labelled
split): that split is fed to the sorry-free mechanical extraction `snBlocks_of_algEquiv`, whose
`finrank` output `(dim S^{λ_i})²` is already the `snBlocks` block size. -/
theorem snBridge (n : ℕ) :
    ∃ (p : SpechtClassification.PartitionIndex n →
          Submodule R (MonoidAlgebra R (Equiv.Perm (Fin n))))
      (proj : SpechtClassification.PartitionIndex n →
          Module.End R (MonoidAlgebra R (Equiv.Perm (Fin n)))),
      (∀ i, LinearMap.IsProj (p i) (proj i)) ∧
      (∀ i, Module.finrank R (p i)
          = (Module.finrank R (Specht.SpechtSubmodule (k := R) i.diagram)) ^ 2) ∧
      (∑ i, proj i = LinearMap.id) := by
  obtain ⟨e⟩ := sn_rational_specht_split (R := R) n
  exact snBlocks_of_algEquiv (R := R) n
    (fun i => Module.finrank R (Specht.SpechtSubmodule (k := R) i.diagram)) e

end QOU.BraidKnot.SnWedderburnPartitionBridge
