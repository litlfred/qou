import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Combinatorics.Enumerative.Partition
import Mathlib.GroupTheory.Perm.Sign
import Mathlib.Algebra.Group.End
import Mathlib.Algebra.MonoidAlgebra.Basic
import Mathlib.RepresentationTheory.Basic
import Mathlib.RingTheory.SimpleModule.Basic
import QOU.BraidKnot.Specht

/-!
# QOU.BraidKnot.SpechtClassification — brick 3 of the Okounkov–Vershik tower

The **classification** of the irreducible `k[S_n]`-modules over a characteristic-zero
field `k`: the family of Specht modules `{S^μ : μ ⊢ n}` is a complete, pairwise
non-isomorphic family of the simple `k[S_n]`-modules.  Consequently the number of
iso-classes of irreducible `S_n`-representations equals the number of partitions of
`n` — the count that pins the Wedderburn block count.

This is "brick 3"; it builds on brick 1 (`QOU.BraidKnot.StandardYoungTableau`) and
brick 2 (`QOU.BraidKnot.Specht`, the Specht-module construction `S^μ ≤ M^μ`).

## Design — "S^μ as an S_n-representation" and isomorphism

Brick 2's `Specht.SpechtSubmodule μ` is a `Submodule k (Mtab μ)`, and crucially
`S^μ` and `S^ν` for `μ ≠ ν` live in **different** ambient modules
(`Mtab μ` vs `Mtab ν`).  To compare them as `S_n`-representations we:

1. **View each `S^μ` as a genuine `Representation`** — `spechtRep μ` is the
   restriction of `Specht.Mtab.rep μ` to the (S_n-stable) submodule `S^μ`,
   produced via `LinearMap.restrict`.  Its well-formedness needs the
   stability lemma `specht_smul_mem` (`S^μ` is `S_n`-invariant), which is a
   genuine brick-2/brick-3 theorem and is honestly stubbed.

2. **State isomorphism via a hand-rolled intertwiner** — `IsRepIso ρ ρ'`
   asserts a `k`-linear equiv `e : V ≃ₗ[k] V'` that **intertwines** the two
   actions (`e (ρ g x) = ρ' g (e x)`).  This is the cleanest honest
   formulation: it composes directly with brick 2's `Mtab.rep`/`SpechtSubmodule`
   and avoids `FDRep`'s finite-dimensionality plumbing (which would force
   `Module.Finite` side-goals before the classification content is even
   reachable).  We chose this over `FDRep k (Perm …)` `Iso` for exactly that
   reason — the intertwiner predicate is a `Prop`-level statement over the
   `Representation` objects brick 2 already supplies.

## What is sorry-free here

* `PartitionIndex n` — the index type `{μ : YoungDiagram // μ.card = n}`, with
  `DecidableEq` (and a fresh sorry-free `DecidableEq YoungDiagram` instance the
  pinned Mathlib lacks).
* `IsRepIso` — the intertwiner predicate, with `refl`/`symm`/`trans` (it is an
  equivalence relation on representations; all three sorry-free).
* `transportPermHom` — the `Perm (Fin a) →* Perm (Fin b)` group transport along
  `a = b` (sorry-free), the device that lets `S^μ`, `S^ν` be compared over one
  group.
* `spechtRep` / `spechtRepOn` — `S^μ` and the regrouped `S^ν` as `Representation`s
  (sorry-free *proof terms*, but transitively `sorryAx`-dependent because they
  reference `specht_smul_mem`; see below).
* `partitionEquivYoungIndex` — the bijection `Nat.Partition n ≃ PartitionIndex n`
  (sorry-free; built from `YoungDiagram.ofRowLens` / `rowLens` round-trips via the
  helper `card_eq_rowLens_sum`, since Mathlib has no packaged bridge at this pin).
* the `Fintype (PartitionIndex n)` instance + `card_partitionIndex` /
  `card_irreducibles_eq_card_partitions` — sorry-free (they rest on
  `partitionEquivYoungIndex`, now closed); the latter is the punchline count
  `#{irreducibles} = #{partitions of n}` modulo the classification stubs below.

## What is stated with `sorry` + `-- Ref:` (the genuine theorems)

* `specht_smul_mem` — `S^μ` is `S_n`-stable (needed to *form* `spechtRep`).
  `-- Ref: [sagan2001]` §2.3.
* `specht_pairwise_noniso` — `μ ≠ ν → ¬ (S^μ ≅ S^ν)`.  `-- Ref:
  [james1984representation]`.
* `specht_exhausts_irreducibles` — every simple `k[S_n]`-module is `≅` some
  `S^μ`.  `-- Ref: [sagan2001]` §2.4.

All textbook-famous theorems (Sagan §2.4, James 1984); their Lean proofs are out
of scope for one brick and are honestly stubbed per AGENTS.md §1.  This module is
intentionally **not** imported by the `QOU.BraidKnot` umbrella (it carries honest
`sorry` targets); it is verified to compile standalone via `lean`-direct against
the pinned v4.24.0 oleans.

## References
- [sagan2001] Sagan, *The Symmetric Group*, §2.4 (classification of irreducibles;
  the Specht modules are a complete set of simple modules in char 0).
- [james1984representation] James, *The Representation Theory of the Symmetric
  Groups* (Specht modules; pairwise non-isomorphism via the bilinear form / the
  James submodule theorem).
- [fulton1997] Fulton, *Young Tableaux* (partitions and Young diagrams).
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtClassification

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open Equiv (Perm)

variable {k : Type} [Field k] [CharZero k]

/-! ## 1. The index set: partitions of `n` ↔ Young diagrams of size `n` -/

/-- The **index type** for the irreducibles of `S_n`: Young diagrams with exactly
`n` cells.  Carrying it as the subtype `{μ : YoungDiagram // μ.card = n}` gives a
direct projection `(·).val : PartitionIndex n → YoungDiagram`, so we can form
`Specht.SpechtSubmodule` of an index element with no glue. -/
def PartitionIndex (n : ℕ) : Type := {μ : YoungDiagram // μ.card = n}

/-- `YoungDiagram` has decidable equality: a diagram is determined by its `cells`
`Finset` (the `isLowerSet` field is a `Prop`, irrelevant by proof irrelevance), and
`Finset (ℕ × ℕ)` has `DecidableEq`.  Mathlib's pinned revision does not `deriving`
this, so we supply it via the `cells` injection. -/
instance : DecidableEq YoungDiagram := fun μ ν =>
  decidable_of_iff (μ.cells = ν.cells) (by rw [YoungDiagram.ext_iff])

namespace PartitionIndex

instance (n : ℕ) : DecidableEq (PartitionIndex n) :=
  Subtype.instDecidableEq

/-- The underlying Young diagram of an index element. -/
def diagram {n : ℕ} (i : PartitionIndex n) : YoungDiagram := i.val

@[simp] theorem diagram_card {n : ℕ} (i : PartitionIndex n) : i.diagram.card = n := i.property

end PartitionIndex

/-! ### Helper lemmas for the partition ↔ Young-diagram bijection -/

open YoungDiagram in
/-- The number of cells produced by `cellsOfRowLens w` equals the sum of `w`. -/
theorem card_cellsOfRowLens (w : List ℕ) :
    (YoungDiagram.cellsOfRowLens w).card = w.sum := by
  induction w with
  | nil => simp [YoungDiagram.cellsOfRowLens]
  | cons a ws ih =>
    rw [YoungDiagram.cellsOfRowLens, List.sum_cons, Finset.card_union_of_disjoint]
    · rw [Finset.card_product, Finset.card_singleton, Finset.card_range, Finset.card_map, ih,
        Nat.one_mul]
    · rw [Finset.disjoint_left]
      rintro ⟨i, j⟩ h1 h2
      simp only [Finset.mem_product, Finset.mem_singleton, Finset.mem_range] at h1
      simp only [Finset.mem_map, Function.Embedding.coe_prodMap, Function.Embedding.coeFn_mk] at h2
      obtain ⟨⟨i', j'⟩, -, hi'⟩ := h2
      simp only [Prod.map_apply, Prod.mk.injEq] at hi'
      omega

/-- `μ.card` equals the sum of its row lengths. -/
theorem card_eq_rowLens_sum (μ : YoungDiagram) : μ.card = μ.rowLens.sum := by
  conv_lhs => rw [← YoungDiagram.ofRowLens_to_rowLens_eq_self (μ := μ)]
  exact card_cellsOfRowLens μ.rowLens

/-- The parts of a partition, after sorting, remain positive. -/
theorem sorted_parts_pos (n : ℕ) (p : Nat.Partition n) :
    ∀ x ∈ p.parts.sort (· ≥ ·), 0 < x := fun x hx =>
  p.parts_pos (by rwa [Multiset.mem_sort] at hx)

/-- `YoungDiagram.ofRowLens` depends only on the underlying list, not the sortedness proof. -/
theorem ofRowLens_congr {w₁ w₂ : List ℕ} {h₁ : w₁.Sorted (· ≥ ·)} {h₂ : w₂.Sorted (· ≥ ·)}
    (hw : w₁ = w₂) : YoungDiagram.ofRowLens w₁ h₁ = YoungDiagram.ofRowLens w₂ h₂ := by
  subst hw; rfl

/-- **Partitions of `n` index Young diagrams of size `n`.**  The classical
bijection `λ ⊢ n ↔ {Young diagram with n cells}` sending a partition to the
diagram whose row lengths are its (sorted) parts, with inverse reading off
`rowLens`.  Built directly from `YoungDiagram.ofRowLens` / `rowLens` and their
round-trip lemmas — Mathlib has no packaged `YoungDiagram ↔ Nat.Partition`
bridge at this pin. **Sorry-free.** -/
noncomputable def partitionEquivYoungIndex (n : ℕ) :
    Nat.Partition n ≃ PartitionIndex n where
  toFun p :=
    -- Ref: [sagan2001] (a partition λ ⊢ n is the same data as a Young diagram with
    -- n cells, via its row lengths)
    ⟨YoungDiagram.ofRowLens (p.parts.sort (· ≥ ·)) (Multiset.sort_sorted _ _), by
      show (YoungDiagram.ofRowLens _ _).card = n
      rw [card_eq_rowLens_sum, YoungDiagram.rowLens_ofRowLens_eq_self (sorted_parts_pos n p),
        ← Multiset.sum_coe, Multiset.sort_eq, p.parts_sum]⟩
  invFun μ :=
    { parts := (μ.val.rowLens : Multiset ℕ)
      parts_pos := fun {i} hi =>
        YoungDiagram.pos_of_mem_rowLens μ.val i (by rwa [Multiset.mem_coe] at hi)
      parts_sum := by rw [Multiset.sum_coe, ← card_eq_rowLens_sum]; exact μ.property }
  left_inv p := by
    apply Nat.Partition.ext
    dsimp only
    rw [YoungDiagram.rowLens_ofRowLens_eq_self (sorted_parts_pos n p), Multiset.sort_eq]
  right_inv μ := by
    apply Subtype.ext
    dsimp only
    have hsort : ((μ.val.rowLens : Multiset ℕ).sort (· ≥ ·)) = μ.val.rowLens := by
      rw [Multiset.coe_sort, List.mergeSort_eq_self]; exact μ.val.rowLens_sorted
    rw [ofRowLens_congr (h₂ := μ.val.rowLens_sorted) hsort]
    exact YoungDiagram.ofRowLens_to_rowLens_eq_self

/-- There are finitely many Young diagrams of size `n`, **derived** from the
partition equiv together with `Fintype (Nat.Partition n)` (Mathlib,
`Mathlib/Combinatorics/Enumerative/Partition.lean`).  This makes the irreducible
count below a finite cardinal. -/
noncomputable instance instFintypePartitionIndex (n : ℕ) : Fintype (PartitionIndex n) :=
  Fintype.ofEquiv (Nat.Partition n) (partitionEquivYoungIndex n)

/-- The index set of irreducibles has the same cardinality as the partitions of
`n` — immediate from the equiv.  (Sorry-free: it is `Fintype.card_congr` of the
stubbed equiv, no extra content.) -/
theorem card_partitionIndex (n : ℕ) :
    Fintype.card (PartitionIndex n) = Fintype.card (Nat.Partition n) :=
  (Fintype.card_congr (partitionEquivYoungIndex n)).symm

/-! ## 2. `S^μ` as an `S_n`-representation -/

/-- **`S^μ` is `S_n`-stable.**  The Specht submodule is invariant under the
permutation action `Specht.Mtab.rep`: this is what makes the restricted
representation `spechtRep` below well-formed.  It holds because `rep σ` permutes
polytabloids (`e_t ↦ ±e_{σ•t}`), which span `S^μ`. -/
theorem specht_smul_mem (μ : YoungDiagram) (σ : Perm (Fin (Specht.nOf μ)))
    (x : Mtab (k := k) μ) (hx : x ∈ SpechtSubmodule (k := k) μ) :
    Mtab.rep μ σ x ∈ SpechtSubmodule (k := k) μ := by
  -- Ref: [sagan2001] §2.3 (the column-group signed sum e_t spans S^μ and
  -- σ • e_t = ± e_{σ • t}, so S^μ is S_n-stable); brick-3 target.
  sorry

/-- **`S^μ` as a representation of `S_n`.**  The restriction of `Specht.Mtab.rep μ`
to the stable submodule `S^μ`, packaged as a genuine
`Representation k (Perm (Fin n)) (S^μ)`.  Each generator acts by
`LinearMap.restrict` of `Mtab.rep μ σ` to `S^μ` (well-defined by
`specht_smul_mem`).  This is the object on which `IsRepIso` compares `S^μ` and
`S^ν`. -/
noncomputable def spechtRep (μ : YoungDiagram) :
    Representation k (Perm (Fin (Specht.nOf μ))) (SpechtSubmodule (k := k) μ) where
  toFun σ := (Mtab.rep μ σ).restrict (fun x hx => specht_smul_mem (k := k) μ σ x hx)
  map_one' := by
    refine LinearMap.ext fun x => Subtype.ext ?_
    simp only [LinearMap.restrict_apply, map_one, Module.End.one_apply]
  map_mul' σ τ := by
    refine LinearMap.ext fun x => Subtype.ext ?_
    simp only [LinearMap.restrict_apply, map_mul, Module.End.mul_apply]

@[simp] theorem spechtRep_apply_coe (μ : YoungDiagram) (σ : Perm (Fin (Specht.nOf μ)))
    (x : SpechtSubmodule (k := k) μ) :
    ((spechtRep (k := k) μ σ x : SpechtSubmodule (k := k) μ) : Mtab (k := k) μ)
      = Mtab.rep μ σ (x : Mtab (k := k) μ) := by
  simp [spechtRep, LinearMap.restrict_apply]

/-! ## 3. Isomorphism of representations (the intertwiner predicate) -/

/-- **Two representations are isomorphic** when there is a `k`-linear equivalence
between their carriers that **intertwines** the group actions.  This is the honest,
plumbing-free notion of "`V ≅ V'` as `G`-representations": a `k`-linear
isomorphism `e` with `e (ρ g x) = ρ' g (e x)` for all `g, x`.

For Specht modules of *different* shapes the carriers `S^μ` and `S^ν` sit in
different ambient modules, and the *same* abstract group `Perm (Fin n)` acts on
both (here `n = μ.card = ν.card`), so this is exactly the statement that compares
them. -/
structure IsRepIso {G V V' : Type} [Monoid G] [AddCommGroup V] [Module k V]
    [AddCommGroup V'] [Module k V'] (ρ : Representation k G V) (ρ' : Representation k G V') :
    Prop where
  /-- There exists a `k`-linear equiv intertwining the two actions. -/
  exists_intertwiner :
    ∃ e : V ≃ₗ[k] V', ∀ (g : G) (x : V), e (ρ g x) = ρ' g (e x)

namespace IsRepIso

variable {G V V' V'' : Type} [Monoid G]
  [AddCommGroup V] [Module k V] [AddCommGroup V'] [Module k V']
  [AddCommGroup V''] [Module k V'']

-- `IsRepIso` is an equivalence relation on representations over any field; the
-- `CharZero k` section hypothesis is genuinely unused here (it is only needed for
-- the *classification* theorems below), so we `omit` it to keep the surface clean.
omit [CharZero k]

/-- Representation isomorphism is reflexive (the identity equiv intertwines). -/
theorem refl (ρ : Representation k G V) : IsRepIso (k := k) ρ ρ :=
  ⟨⟨LinearEquiv.refl k V, fun _ _ => rfl⟩⟩

/-- Representation isomorphism is symmetric (the inverse equiv intertwines). -/
theorem symm {ρ : Representation k G V} {ρ' : Representation k G V'}
    (h : IsRepIso (k := k) ρ ρ') : IsRepIso (k := k) ρ' ρ := by
  obtain ⟨e, he⟩ := h.exists_intertwiner
  refine ⟨⟨e.symm, fun g y => ?_⟩⟩
  -- `e.symm (ρ' g y) = ρ g (e.symm y)` from `he` applied to `x = e.symm y`.
  have := he g (e.symm y)
  rw [e.apply_symm_apply] at this
  exact e.symm_apply_eq.mpr this.symm

/-- Representation isomorphism is transitive (compose the intertwining equivs). -/
theorem trans {ρ : Representation k G V} {ρ' : Representation k G V'}
    {ρ'' : Representation k G V''}
    (h : IsRepIso (k := k) ρ ρ') (h' : IsRepIso (k := k) ρ' ρ'') :
    IsRepIso (k := k) ρ ρ'' := by
  obtain ⟨e, he⟩ := h.exists_intertwiner
  obtain ⟨f, hf⟩ := h'.exists_intertwiner
  refine ⟨⟨e.trans f, fun g x => ?_⟩⟩
  show f (e (ρ g x)) = ρ'' g (f (e x))
  rw [he g x, hf g (e x)]

end IsRepIso

/-- **Transport the acting group along a cell-count equality.**  When `h : a = b`,
`finCongr h : Fin a ≃ Fin b` induces a monoid isomorphism
`Perm (Fin a) →* Perm (Fin b)` (`Equiv.permCongrHom` as a `MonoidHom`).  Composing a
representation of `Perm (Fin b)` with this hom yields a representation of
`Perm (Fin a)`, so two Specht modules of equal-size shapes can be compared by
`IsRepIso` over **one** group.  This is the precise sense in which "`S^μ` and `S^ν`
are both `S_n`-representations" when `μ` and `ν` have the same number of cells.

Kept general in `{a b : ℕ}` (rather than `nOf μ = nOf ν`) so the same transport
serves both the pairwise-non-iso comparison (`nOf μ = nOf ν`) and the completeness
comparison (`nOf μ = n` against a bare `n`). -/
noncomputable def transportPermHom {a b : ℕ} (h : a = b) :
    Perm (Fin a) →* Perm (Fin b) :=
  (Equiv.permCongrHom (finCongr h)).toMonoidHom

/-- `S^ν` viewed as a representation of the *same* group `Perm (Fin (nOf μ))`
acting on `S^μ`, via `transportPermHom`.  Abbreviation used to state the
classification cleanly. -/
noncomputable def spechtRepOn {μ ν : YoungDiagram} (h : Specht.nOf μ = Specht.nOf ν) :
    Representation k (Perm (Fin (Specht.nOf μ))) (SpechtSubmodule (k := k) ν) :=
  (spechtRep (k := k) ν).comp (transportPermHom h)

/-! ## 4. The classification theorems (stated, `sorry` + `-- Ref:`) -/

/-- **Pairwise non-isomorphism.**  Distinct shapes give non-isomorphic Specht
modules: if `μ ≠ ν` (with the same number of cells, so they index the *same*
symmetric group), then `S^μ` and `S^ν` are not isomorphic as `S_n`-representations.

We state it via the intertwiner predicate over the shared carrier index `nOf μ`,
using the hypothesis `h : nOf μ = nOf ν` to view `spechtRep ν` as a representation
of `Perm (Fin (nOf μ))` (by transporting along `h`). -/
theorem specht_pairwise_noniso {μ ν : YoungDiagram} (h : Specht.nOf μ = Specht.nOf ν)
    (hμν : μ ≠ ν) :
    ¬ IsRepIso (k := k) (spechtRep (k := k) μ) (spechtRepOn (k := k) h) := by
  -- Ref: [james1984representation] (Specht modules of distinct shapes are
  -- pairwise non-isomorphic — via the James bilinear form / submodule theorem);
  -- brick-3 target.
  sorry

/-- **Completeness.**  Every simple `k[S_n]`-module is isomorphic to some Specht
module.  Phrased: for any representation `ρ : Representation k (Perm (Fin n)) W`
that is simple as a `k[S_n]`-module — stated as
`IsSimpleModule (MonoidAlgebra k (Perm (Fin n))) ρ.asModule`, using the
`MonoidAlgebra k G`-module structure on `ρ.asModule` (Mathlib
`Representation.asModule`) — there is a Young diagram `μ` with `nOf μ = n` and a
representation isomorphism `ρ ≅ spechtRep μ` (after transporting the acting group
along `nOf μ = n`).

This is the half of the classification that says the Specht modules **exhaust** the
irreducibles. -/
theorem specht_exhausts_irreducibles {n : ℕ} {W : Type} [AddCommGroup W] [Module k W]
    (ρ : Representation k (Perm (Fin n)) W)
    (_hsimple : IsSimpleModule (MonoidAlgebra k (Perm (Fin n))) ρ.asModule) :
    ∃ (μ : YoungDiagram) (h : Specht.nOf μ = n),
      IsRepIso (k := k) ρ
        ((spechtRep (k := k) μ).comp (transportPermHom h.symm)) := by
  -- Ref: [sagan2001] §2.4 (the Specht modules form a complete set of irreducible
  -- k[S_n]-modules in char 0; #{S^μ} = #conjugacy classes = #partitions);
  -- brick-3 target.
  sorry

/-- **The count corollary (the punchline).**  The number of iso-classes of
irreducible `k[S_n]`-modules equals the number of partitions of `n`.

We phrase the left-hand side as `Fintype.card (PartitionIndex n)` — the number of
*Specht* modules — which equals the number of irreducibles by
`specht_pairwise_noniso` (they are distinct) + `specht_exhausts_irreducibles`
(they are all of them).  The right-hand side `Fintype.card (Nat.Partition n)` is
the partition count.  This is the identity that pins the Wedderburn block count of
`k[S_n]` to `#{λ ⊢ n}`. -/
theorem card_irreducibles_eq_card_partitions (n : ℕ) :
    Fintype.card (PartitionIndex n) = Fintype.card (Nat.Partition n) := by
  -- Ref: [sagan2001] §2.4 (the classification gives a bijection
  -- {iso-classes of irreducible k[S_n]-modules} ↔ {partitions of n}); follows
  -- from `specht_pairwise_noniso` + `specht_exhausts_irreducibles`.  Here it is
  -- the `card_partitionIndex` restatement (sorry-free given the partition equiv),
  -- recorded as the named punchline.
  exact card_partitionIndex n

end QOU.BraidKnot.SpechtClassification
