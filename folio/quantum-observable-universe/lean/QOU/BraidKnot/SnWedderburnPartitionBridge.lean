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
import QOU.BraidKnot.RegularRepTrace
import QOU.BraidKnot.JucysMurphyOV
import Mathlib.Algebra.Algebra.Bilinear

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

* `sn_isotypic_specht_split` — over a characteristic-zero field `R`, the **isotypic, rational,
  OV-labelled** Wedderburn decomposition of `R[S_n]`:
  `R[S_n] ≃ₐ[R] ∏_{i:PartitionIndex n} Matrix(Fin (dim S^{λ_i})) R`,
  with block `i` the `S^{λ_i}`-isotypic component (matrix size `= dim_R S^{λ_i}`), carrying the
  central `C₂ = Σₖ Xₖ²` to the block-scalar family `fun i => contentSqSum λᵢ • 1`.  The plain
  rational split `sn_rational_specht_split` is now a **corollary** of it (forget the `C₂` clause),
  so the file has a **single** core, not two.  This statement folds in the pieces of content absent
  from the pinned Mathlib:
  - **(a) ℚ-rationality / absolute irreducibility.** The division rings collapse to `R` itself —
    `S_n`-representations are defined over `ℚ`, so no genuine division-ring factors appear. This is
    the genuinely missing input: the char-0 (Maschke + rationality) **descent**.
    *Correction (2026-08-09).* An earlier wording of this bullet said Mathlib "has the matrix-product
    form only for an algebraically closed base". That is inaccurate, and it contradicted
    §"Whether Mathlib offers…" two paragraphs below, which correctly cites the general
    division-ring form. Mathlib's `IsSemisimpleRing.exists_algEquiv_pi_matrix_divisionRing` gives the
    `∏ Matrix` decomposition as an **algebra** equivalence over *any* base — algebraic closure is
    needed only to collapse the `𝔇 i`, which is exactly (and only) what is missing here. That rung is
    now wired as `WedderburnSn.sn_wedderburnArtin_alg` (sorry-free), so what this core still owes on
    the (a) front is the collapse `𝔇 i ≃ R` alone, not the algebra-form split.
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
> Folding the alignment into the single existential core `sn_isotypic_specht_split` (from which the
> plain `sn_rational_specht_split` is derived) — which asserts the *aligned* split exists, a true
> statement — is the honest disposition; it avoids planting an over-general cited `sorry` (cf. the
> `DominanceData.dom_colStab` / `seminormalVectors_span` over-generality fixes).

## Whether Mathlib offers any `S_n`-rationality support

It does **not**. Mathlib (pinned v4.24.0) provides the *abstract* Wedderburn–Artin theorem in three
forms — ring (`IsSemisimpleRing.exists_ringEquiv_pi_matrix_divisionRing`), **algebra over an
arbitrary base** (`…exists_algEquiv_pi_matrix_divisionRing`), and the algebraically-closed
specialisation (`…_of_isAlgClosed`, where the division rings collapse to the base field by Schur +
algebraic closure) — but **nothing** about the rationality of the symmetric group's representations:
no statement that `S_n`-irreducibles are defined over `ℚ`, no Specht module at all (a name search
over the full import closure returns **0** hits for `Specht`), no Specht-module ↔ Wedderburn-block
identification, no `dim(λ) = #SYT(λ)` at the block level. The core is therefore genuine.

**Measured residual (2026-08-09).** With `WedderburnSn.sn_wedderburnArtin_alg` in place, the delta
between what Mathlib + this corpus supply and what `sn_isotypic_specht_split` asserts is exactly
four items, none of them the Wedderburn step itself:
1. the division-ring collapse `𝔇 i ≃ R` (ℚ is a splitting field for `S_n`);
2. the reindexing `Fin N ≃ SpechtClassification.PartitionIndex n`;
3. the size identification `𝔫 i = dim_R S^{λ_i}`;
4. the `C₂ = Σₖ Xₖ²` block-scalar alignment `↦ contentSqSum λᵢ • 1` (the isotypic clause).

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
set_option linter.unusedSimpArgs false

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
  rw [← LinearMap.comp_apply, coordProj_idem]

/-- The pulled-back idempotent is a **projection** onto its range. -/
theorem transProj_isProj (e : A ≃ₗ[R] (∀ j, B j)) (i : ι) :
    LinearMap.IsProj (LinearMap.range (transProj e i)) (transProj e i) := by
  refine ⟨fun x => ⟨x, rfl⟩, ?_⟩
  rintro x ⟨y, rfl⟩
  rw [← LinearMap.comp_apply, transProj_idem]

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

/-! ## 2. The single `S_n`-rep-theory core (isotypic split) + its rational corollary

The genuine gap is the **isotypic** core `sn_isotypic_specht_split` below; the plain rational
Wedderburn split `sn_rational_specht_split` is now a **corollary** of it (forget the carried-`C₂`
clause).  The two cited cores of the previous shape thus collapse to **one**. -/

variable {R : Type} [Field R] [CharZero R]

/-- **Named core (the genuine isotypic-aligned `S_n`-rep-theory gap).** Over a characteristic-zero
field `R`, a *rational, OV-labelled* Wedderburn algebra isomorphism
`R[S_n] ≃ₐ[R] ∏_{i:PartitionIndex n} Matrix(Fin (dim S^{λ_i})) R` with block `i` the
`S^{λ_i}`-**isotypic** component, **carrying** the central Jucys–Murphy element `C₂ = Σ_k X_k²` to the
block-scalar family `fun i => contentSqSum λ_i • 1`.

The carried-`C₂` clause *is* the isotypic alignment, made operational: by
`JucysMurphy.centralC2_acts_by_contentSqSum`, `C₂` acts on the `S^{λ_i}`-isotypic block by
`contentSqSum λ_i` (Schur per isotypic component), so an `e` whose block `i` *is* that component sends
`C₂` to `contentSqSum λ_i • 1` there.  Conversely the clause **forces** the alignment (a size-aligned
split need not be isotypic; `freeProjClaim_false` shows an unconstrained `proj` cannot satisfy the
decomposition), so bundling it into the existential is the honest, non-over-general disposition.
This is the **single** named core of the file: the plain rational split
`sn_rational_specht_split` is derived from it, and §5's `snBlocks_c2_aligned` consumes it directly.
Mathlib (pinned v4.24.0) lacks every piece this folds in: ℚ-rationality (collapsing division rings
to `R`; it has the matrix product only over an algebraically closed base), the partition labelling,
the OV identification block `i` ↔ `S^{λ_i}` of size `dim_R S^{λ_i}`, and the isotypic /
`C₂`-eigenvalue alignment.
`-- Ref: [vershik-kerov1977], [sagan2001], [james1984representation]`. -/
class SnIsotypicSpechtSplit (R : Type) [Field R] [CharZero R] : Prop where
  /-- Mathlib lacks char-0 rationality (Maschke) for S_n, Specht module alignment, and the isotypic/C₂ block alignment. -/
  exists_split (n : ℕ) :
    ∃ e : MonoidAlgebra R (Equiv.Perm (Fin n)) ≃ₐ[R]
      (∀ i : SpechtClassification.PartitionIndex n,
        Matrix (Fin (Module.finrank R (Specht.SpechtSubmodule (k := R) i.diagram)))
               (Fin (Module.finrank R (Specht.SpechtSubmodule (k := R) i.diagram))) R),
      e (RegularRepTrace.centralC2 n)
        = fun i : SpechtClassification.PartitionIndex n =>
            ((JucysMurphy.contentSqSum i.diagram : ℤ) : R) •
            (1 : Matrix (Fin (Module.finrank R (Specht.SpechtSubmodule (k := R) i.diagram)))
                        (Fin (Module.finrank R (Specht.SpechtSubmodule (k := R) i.diagram))) R)

theorem sn_isotypic_specht_split (n : ℕ) [SnIsotypicSpechtSplit R] :
    ∃ e : MonoidAlgebra R (Equiv.Perm (Fin n)) ≃ₐ[R]
      (∀ i : SpechtClassification.PartitionIndex n,
        Matrix (Fin (Module.finrank R (Specht.SpechtSubmodule (k := R) i.diagram)))
               (Fin (Module.finrank R (Specht.SpechtSubmodule (k := R) i.diagram))) R),
      e (RegularRepTrace.centralC2 n)
        = fun i : SpechtClassification.PartitionIndex n =>
            ((JucysMurphy.contentSqSum i.diagram : ℤ) : R) •
            (1 : Matrix (Fin (Module.finrank R (Specht.SpechtSubmodule (k := R) i.diagram)))
                        (Fin (Module.finrank R (Specht.SpechtSubmodule (k := R) i.diagram))) R) :=
  SnIsotypicSpechtSplit.exists_split n

/-- **Rational Wedderburn split — a corollary of the isotypic core.** Over a characteristic-zero
field `R`, the rational, OV-labelled Wedderburn decomposition of `R[S_n]`, indexed by the partitions
of `n`, with block `i` of matrix size exactly `dim_R S^{λ_i}`:
`R[S_n] ≃ₐ[R] ∏_{i:PartitionIndex n} Matrix(Fin (dim S^{λ_i})) R`.

**Sorry-free modulo the single core** `sn_isotypic_specht_split`: forgetting that theorem's
carried-`C₂` clause yields exactly this algebra iso (same `e`).  The isotypic split is strictly
stronger, so the previous shape's two independent cited cores collapse to one.
`-- Ref: [james1984representation], [sagan2001]`. -/
theorem sn_rational_specht_split (n : ℕ) [SnIsotypicSpechtSplit R] :
    Nonempty (MonoidAlgebra R (Equiv.Perm (Fin n)) ≃ₐ[R]
      (∀ i : SpechtClassification.PartitionIndex n,
        Matrix (Fin (Module.finrank R (Specht.SpechtSubmodule (k := R) i.diagram)))
               (Fin (Module.finrank R (Specht.SpechtSubmodule (k := R) i.diagram))) R)) :=
  ⟨(sn_isotypic_specht_split (R := R) n).choose⟩

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
theorem snBridge (n : ℕ) [SnIsotypicSpechtSplit R] :
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

/-! ## 5. The aligned bundle — isotypic projections + the `C₂` block-decomposition

`snBridge` above gives the `snBlocks` bundle from a **size-aligned** split (block `i` has the right
dimension `(dim S^{λ_i})²`).  The capstone's `decomp` field needs strictly more: the central
Jucys–Murphy element `C₂ = Σ_k X_k²` must be **block-diagonal** with eigenvalues `contentSqSum λ_i`,

  `mulLeft C₂ = ∑ i, contentSqSum λ_i • proj i`,

and that holds only when block `i` is the **`S^{λ_i}`-isotypic component** — an *isotypic*-alignment,
strictly stronger than size-alignment (distinct partitions can share `dim S^λ`, so a size-aligned
split need not be isotypic-aligned).  The decomp therefore **cannot** be layered on top of `snBridge`'s
size-aligned `proj`; the projection family and the eigen-decomposition must be produced together. -/

/-- The free-`proj` decomposition predicate: `mulLeft C₂ = ∑ i, contentSqSum λ_i • proj i` for an
**unconstrained** `proj`.  (The `decomp` field of `SnWedderburnSpectralData` is this equation for a
*specific aligned* `proj` — never a free one; see `freeProjClaim_false`.) -/
abbrev FreeProjClaim (K : Type) [Field K] [CharZero K] (n : ℕ) : Prop :=
  ∀ (proj : SpechtClassification.PartitionIndex n →
        Module.End K (MonoidAlgebra K (Equiv.Perm (Fin n)))),
    LinearMap.mulLeft K (RegularRepTrace.centralC2 n)
      = ∑ i, ((JucysMurphy.contentSqSum i.diagram : ℤ) : K) • proj i

/-- **The free-`proj` decomposition is FALSE** (machine-proved, no `sorry`).  At `n = 2` over `ℚ`,
instantiating at `proj ≡ 0` forces `mulLeft C₂ = 0`, hence (apply to `1`) `C₂ = 0`, contradicting
`C₂(1) = binom(2,2) = 1`.  Hence the `decomp` block-diagonalisation holds only for the *aligned*
isotypic family of `snBlocks_c2_aligned` below, not for an arbitrary `proj`.  Axioms
`[propext, Classical.choice, Quot.sound]`. -/
theorem freeProjClaim_false : ¬ FreeProjClaim ℚ 2 := by
  intro h
  have h0 := h (fun _ => 0)
  simp only [smul_zero, Finset.sum_const_zero] at h0
  have happ := congrArg
    (fun (f : Module.End ℚ (MonoidAlgebra ℚ (Equiv.Perm (Fin 2)))) => f 1) h0
  simp only [LinearMap.mulLeft_apply, mul_one, LinearMap.zero_apply] at happ
  have hc := RegularRepTrace.centralC2_coeff_one (R := ℚ) 2
  rw [happ] at hc
  simp at hc

/-! ### The C₂-decomposition machinery (sorry-free, pure linear algebra)

`mulLeft_blockScalar` + `mulLeft_eq_sum_transProj` discharge the entire passage from an isotypic
algebra iso to the `C₂` block-decomposition, so `snBlocks_c2_aligned` reduces to the single isotypic
split core `sn_isotypic_specht_split` below.  No "center of a product of matrix algebras" lemma is
needed: the block-scalar shape is supplied as a hypothesis (exactly the content the isotypic
alignment provides). -/

section C2Decomp
variable {R : Type} [CommRing R] {ι : Type} [Fintype ι] [DecidableEq ι]
  {B : ι → Type} [∀ i, Ring (B i)] [∀ i, Algebra R (B i)]

/-- On the product algebra `∏ⱼ Bⱼ`, left-multiplication by a **block-scalar** element
`fun i => γ i • 1` equals `∑ᵢ γ i • coordProj i`: on coordinate `i` it scales by `γ i`. Sorry-free. -/
theorem mulLeft_blockScalar (γ : ι → R) :
    LinearMap.mulLeft R (fun i => (γ i) • (1 : B i)) =
      ∑ i, (γ i) • (coordProj (R := R) (B := B) i) := by
  apply LinearMap.ext; intro v; funext k
  have hL : (LinearMap.mulLeft R (fun i => (γ i) • (1 : B i)) v) k = γ k • v k := by
    simp [LinearMap.mulLeft_apply, Pi.mul_apply]
  have hR : (∑ i, (γ i) • (coordProj (R := R) (B := B) i)) v k = γ k • v k := by
    rw [LinearMap.coeFn_sum, Finset.sum_apply, Finset.sum_apply]
    simp only [LinearMap.smul_apply, Pi.smul_apply, coordProj, LinearMap.comp_apply,
      LinearMap.single_apply, LinearMap.proj_apply]
    rw [Finset.sum_eq_single k]
    · simp
    · intro b _ hb; simp [Ne.symm hb]
    · intro hk; exact absurd (Finset.mem_univ k) hk
  rw [hL, hR]

end C2Decomp

section C2DecompField
variable {R : Type} [Field R] {ι : Type} [Fintype ι] [DecidableEq ι]
  {B : ι → Type} [∀ i, Ring (B i)] [∀ i, Algebra R (B i)]
  {A : Type} [Ring A] [Algebra R A]

/-- **The `mulLeft`-conjugation payoff (sorry-free).** If an algebra iso `e : A ≃ₐ ∏ⱼ Bⱼ` carries a
central element `z` to a block-scalar `fun i => γ i • 1`, then `mulLeft z` block-diagonalises:
`mulLeft z = ∑ᵢ γ i • transProj e.toLinearEquiv i`.  Conjugate `mulLeft` by `e` (algebra-hom
property), apply `mulLeft_blockScalar`, push the composition through the finite sum/scalar.  No
center-of-product lemma is required — the block-scalar shape is the hypothesis. -/
theorem mulLeft_eq_sum_transProj
    (e : A ≃ₐ[R] (∀ i, B i)) (z : A) (γ : ι → R)
    (hz : e z = fun i => (γ i) • (1 : B i)) :
    LinearMap.mulLeft R z = ∑ i, (γ i) • (transProj (e.toLinearEquiv) i) := by
  have hconj : LinearMap.mulLeft R z =
      (e.symm.toLinearMap) ∘ₗ (LinearMap.mulLeft R (e z)) ∘ₗ (e.toLinearMap) := by
    ext a
    simp only [LinearMap.comp_apply, AlgEquiv.toLinearMap_apply, LinearMap.mulLeft_apply]
    rw [← map_mul, AlgEquiv.symm_apply_apply]
  rw [hconj, hz, mulLeft_blockScalar]
  ext a
  simp only [LinearMap.comp_apply, LinearMap.coeFn_sum, Finset.sum_apply, LinearMap.smul_apply,
    AlgEquiv.toLinearMap_apply]
  rw [map_sum]
  apply Finset.sum_congr rfl
  intro i _
  rw [map_smul]
  simp only [transProj, LinearMap.comp_apply, LinearEquiv.coe_coe]
  rfl

end C2DecompField

/-! The single named core `sn_isotypic_specht_split` is stated in §2 above (with the rational
Wedderburn split `sn_rational_specht_split` derived from it as a corollary).  §5 here consumes it
through the sorry-free `C₂`-decomposition machinery. -/

/-- **The aligned isotypic projection family + `C₂` eigen-decomposition (the capstone core), now
sorry-free modulo the single isotypic split `sn_isotypic_specht_split`.** Over a characteristic-zero
field `R`, a partition-indexed family `proj i` onto blocks `p i` that is the `snBlocks` bundle
(`IsProj`, ranks `(dim S^{λ_i})²`, `∑ proj = id`) **and** block-diagonalises the central JM element:
`mulLeft C₂ = ∑ i, contentSqSum λ_i • proj i`.

The projection family is `transProj e i` for the isotypic `e` from `sn_isotypic_specht_split`;
conjuncts 1–3 reuse the sorry-free `transProj_isProj` / `finrank_range_transProj` / `transProj_sum`,
and conjunct 4 (the `C₂` block-diagonalisation) is the sorry-free `mulLeft_eq_sum_transProj` applied to
the core's carried-`C₂` clause.  The entire `C₂`-decomposition machinery is thus discharged sorry-free;
only the isotypic split itself remains cited. -/
theorem snBlocks_c2_aligned (n : ℕ) [SnIsotypicSpechtSplit R] :
    ∃ (p : SpechtClassification.PartitionIndex n →
          Submodule R (MonoidAlgebra R (Equiv.Perm (Fin n))))
      (proj : SpechtClassification.PartitionIndex n →
          Module.End R (MonoidAlgebra R (Equiv.Perm (Fin n)))),
      (∀ i, LinearMap.IsProj (p i) (proj i)) ∧
      (∀ i, Module.finrank R (p i)
          = (Module.finrank R (Specht.SpechtSubmodule (k := R) i.diagram)) ^ 2) ∧
      (∑ i, proj i = LinearMap.id) ∧
      LinearMap.mulLeft R (RegularRepTrace.centralC2 n)
        = ∑ i, ((JucysMurphy.contentSqSum i.diagram : ℤ) : R) • proj i := by
  classical
  obtain ⟨e, he⟩ := sn_isotypic_specht_split (R := R) n
  set Bi := fun i : SpechtClassification.PartitionIndex n =>
    Matrix (Fin (Module.finrank R (Specht.SpechtSubmodule (k := R) i.diagram)))
           (Fin (Module.finrank R (Specht.SpechtSubmodule (k := R) i.diagram))) R with hBi
  let eL := e.toLinearEquiv
  refine ⟨fun i => LinearMap.range (transProj (B := Bi) eL i),
          fun i => transProj (B := Bi) eL i, ?_, ?_, ?_, ?_⟩
  · intro i; exact transProj_isProj eL i
  · intro i
    rw [finrank_range_transProj eL i]
    rw [Module.finrank_matrix, Module.finrank_self, mul_one, Fintype.card_fin, sq]
  · exact transProj_sum eL
  · exact mulLeft_eq_sum_transProj e (RegularRepTrace.centralC2 n)
      (fun i => ((JucysMurphy.contentSqSum i.diagram : ℤ) : R)) he

end QOU.BraidKnot.SnWedderburnPartitionBridge
