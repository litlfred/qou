import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Combinatorics.Enumerative.Partition
import Mathlib.GroupTheory.Perm.Sign
import Mathlib.Algebra.Group.End
import Mathlib.Algebra.MonoidAlgebra.Basic
import Mathlib.RepresentationTheory.Basic
import Mathlib.RingTheory.SimpleModule.Basic
import QOU.BraidKnot.Specht
import QOU.BraidKnot.SpechtCrossKappa
import QOU.MathlibExt.RepresentationCharacter

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
now-proved `partitionEquivYoungIndex`, no extra content.) -/
theorem card_partitionIndex (n : ℕ) :
    Fintype.card (PartitionIndex n) = Fintype.card (Nat.Partition n) :=
  (Fintype.card_congr (partitionEquivYoungIndex n)).symm

/-! ## 2. `S^μ` as an `S_n`-representation -/

/-! ### Helper lemmas for `specht_smul_mem` (the `S_n`-stability proof) -/

omit [CharZero k] in
/-- Conjugation `σ · σ⁻¹` carries `colStab t` into `colStab (σ • t)`. -/
theorem conj_mem_colStab_fwd {μ : YoungDiagram} (σ : Perm (Fin (Specht.nOf μ)))
    (t : Tableau μ) (π : Perm (Fin (Specht.nOf μ))) (hπ : π ∈ colStab t) :
    σ * π * σ⁻¹ ∈ colStab (σ • t) := by
  rw [mem_colStab] at hπ ⊢
  rw [colPattern_smul, mul_smul, mul_smul, inv_smul_smul, hπ]

omit [CharZero k] in
/-- Conjugation `σ⁻¹ · σ` carries `colStab (σ • t)` back into `colStab t`. -/
theorem conj_mem_colStab_bwd {μ : YoungDiagram} (σ : Perm (Fin (Specht.nOf μ)))
    (t : Tableau μ) (ρ : Perm (Fin (Specht.nOf μ))) (hρ : ρ ∈ colStab (σ • t)) :
    σ⁻¹ * ρ * σ ∈ colStab t := by
  rw [mem_colStab] at hρ ⊢
  rw [colPattern_smul] at hρ
  rw [mul_smul, mul_smul, hρ, inv_smul_smul]

/-- The conjugation bijection `C_t ≃ C_{σ•t}`, `π ↦ σπσ⁻¹`.  It witnesses that the
column stabilizers of `t` and `σ • t` are conjugate subgroups, the reindexing used
to push `rep σ` through a polytabloid. -/
noncomputable def conjStabEquiv {μ : YoungDiagram} (σ : Perm (Fin (Specht.nOf μ)))
    (t : Tableau μ) : (colStab t) ≃ (colStab (σ • t)) where
  toFun π := ⟨σ * (π : Perm (Fin (Specht.nOf μ))) * σ⁻¹, conj_mem_colStab_fwd σ t π π.2⟩
  invFun ρ := ⟨σ⁻¹ * (ρ : Perm (Fin (Specht.nOf μ))) * σ, conj_mem_colStab_bwd σ t ρ ρ.2⟩
  left_inv π := by
    apply Subtype.ext
    show σ⁻¹ * (σ * (π : Perm (Fin (Specht.nOf μ))) * σ⁻¹) * σ = (π : Perm (Fin (Specht.nOf μ)))
    rw [mul_assoc, mul_assoc, inv_mul_cancel, mul_one, ← mul_assoc, inv_mul_cancel, one_mul]
  right_inv ρ := by
    apply Subtype.ext
    show σ * (σ⁻¹ * (ρ : Perm (Fin (Specht.nOf μ))) * σ) * σ⁻¹ = (ρ : Perm (Fin (Specht.nOf μ)))
    rw [mul_assoc, mul_assoc, mul_inv_cancel, mul_one, ← mul_assoc, mul_inv_cancel, one_mul]

omit [CharZero k] in
/-- **`rep σ` permutes polytabloids: `σ · e_t = e_{σ•t}`.**  The linear action sends
the polytabloid of `t` to the polytabloid of `σ • t`, via `map_sum`/`map_zsmul`
(`rep` is `k`-linear) + `rep_of`, reindexing the column-stabilizer sum along the
conjugation bijection `conjStabEquiv` (sign is conjugation-invariant in `ℤˣ`, and
`(σπσ⁻¹) • (σ•t) = σ • (π•t)`).  This is the heart of `S_n`-stability. -/
theorem rep_polytabloid {μ : YoungDiagram} (σ : Perm (Fin (Specht.nOf μ)))
    (t : Tableau μ) :
    Mtab.rep (k := k) μ σ (polytabloid (k := k) t) = polytabloid (k := k) (σ • t) := by
  rw [polytabloid, map_sum]
  simp only [map_zsmul, Mtab.rep_of]
  rw [polytabloid]
  refine Fintype.sum_equiv (conjStabEquiv σ t) _ _ (fun π => ?_)
  show (Equiv.Perm.sign (π : Perm (Fin (Specht.nOf μ))) : ℤ)
        • Mtab.of (k := k) (σ • ((π : Perm (Fin (Specht.nOf μ))) • t))
      = (Equiv.Perm.sign ((conjStabEquiv σ t π : colStab (σ • t)) : Perm (Fin (Specht.nOf μ))) : ℤ)
        • Mtab.of (k := k)
            (((conjStabEquiv σ t π : colStab (σ • t)) : Perm (Fin (Specht.nOf μ))) • (σ • t))
  have hsign :
      Equiv.Perm.sign ((conjStabEquiv σ t π : colStab (σ • t)) : Perm (Fin (Specht.nOf μ)))
        = Equiv.Perm.sign (π : Perm (Fin (Specht.nOf μ))) := by
    show Equiv.Perm.sign (σ * (π : Perm (Fin (Specht.nOf μ))) * σ⁻¹)
        = Equiv.Perm.sign (π : Perm (Fin (Specht.nOf μ)))
    rw [map_mul, map_mul, map_inv,
        mul_comm (Equiv.Perm.sign σ) (Equiv.Perm.sign (π : Perm (Fin (Specht.nOf μ)))),
        mul_assoc, mul_inv_cancel, mul_one]
  have htab :
      ((conjStabEquiv σ t π : colStab (σ • t)) : Perm (Fin (Specht.nOf μ))) • (σ • t)
        = σ • ((π : Perm (Fin (Specht.nOf μ))) • t) := by
    show (σ * (π : Perm (Fin (Specht.nOf μ))) * σ⁻¹) • (σ • t)
        = σ • ((π : Perm (Fin (Specht.nOf μ))) • t)
    rw [mul_smul, mul_smul, inv_smul_smul, ← mul_smul]
  rw [hsign, htab]

omit [CharZero k] in
/-- **`S^μ` is `S_n`-stable.**  The Specht submodule is invariant under the
permutation action `Specht.Mtab.rep`: this is what makes the restricted
representation `spechtRep` below well-formed.  It holds because `rep σ` permutes
polytabloids (`e_t ↦ ±e_{σ•t}`), which span `S^μ`. -/
theorem specht_smul_mem (μ : YoungDiagram) (σ : Perm (Fin (Specht.nOf μ)))
    (x : Mtab (k := k) μ) (hx : x ∈ SpechtSubmodule (k := k) μ) :
    Mtab.rep μ σ x ∈ SpechtSubmodule (k := k) μ := by
  -- Ref: [sagan2001] §2.3 (the column-group signed sum e_t spans S^μ and
  -- σ • e_t = e_{σ • t} via colStab conjugation, so S^μ is S_n-stable).
  rw [SpechtSubmodule] at hx ⊢
  induction hx using Submodule.span_induction with
  | mem y hy =>
      obtain ⟨t, rfl⟩ := hy
      rw [rep_polytabloid]
      exact Submodule.subset_span ⟨σ • t, rfl⟩
  | zero => rw [map_zero]; exact Submodule.zero_mem _
  | add y z _ _ hy hz => rw [map_add]; exact Submodule.add_mem _ hy hz
  | smul a y _ hy => rw [map_smul]; exact Submodule.smul_mem _ a hy

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

omit [CharZero k] in
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

/-! ## 3.5  Dominance (majorization) order on Young diagrams

The reduction ingredient for §4's pairwise non-isomorphism: the majorization
order `partitionDom` and its **antisymmetry** (proved sorry-free).  Antisymmetry
is what turns "dominance both ways" into "equal shapes", factoring
`specht_pairwise_noniso` into the single James cross-shape core
`spechtIso_imp_dom_both` + this proved reduction.  Mathlib packages the
containment order on `YoungDiagram` but not the dominance order. -/

open scoped BigOperators in
/-- **Dominance (majorization) order on Young diagrams**: `μ` dominates `ν`
(`partitionDom μ ν`) iff every partial row-length sum of `μ` is at least the
corresponding partial sum of `ν`. -/
def partitionDom (μ ν : YoungDiagram) : Prop :=
  ∀ i, (∑ r ∈ Finset.range i, ν.rowLen r) ≤ (∑ r ∈ Finset.range i, μ.rowLen r)

/-- Dominance is reflexive. -/
theorem partitionDom_refl (μ : YoungDiagram) : partitionDom μ μ := fun _ => le_refl _

open scoped BigOperators in
/-- **Antisymmetry of dominance (sorry-free).** If `μ` dominates `ν` and `ν`
dominates `μ`, then `μ = ν`: equal partial sums for every `i` force equal
row lengths (`Finset.sum_range_succ` + `omega`), and equal row lengths force
equal cell sets (`YoungDiagram.ext` via `mem_iff_lt_rowLen`). -/
theorem partitionDom_antisymm (μ ν : YoungDiagram)
    (hμν : partitionDom μ ν) (hνμ : partitionDom ν μ) : μ = ν := by
  have heq : ∀ i, (∑ r ∈ Finset.range i, μ.rowLen r) = (∑ r ∈ Finset.range i, ν.rowLen r) :=
    fun i => le_antisymm (hνμ i) (hμν i)
  apply YoungDiagram.ext
  ext ⟨i, j⟩
  have hrow : μ.rowLen i = ν.rowLen i := by
    have h1 := heq (i + 1); have h2 := heq i
    rw [Finset.sum_range_succ, Finset.sum_range_succ] at h1
    omega
  simp only [YoungDiagram.mem_cells, YoungDiagram.mem_iff_lt_rowLen, hrow]

/-! ## 4. The classification theorems -/

/-! ### The cross-shape dominance argument (Sagan Thm 2.4.4)

An intertwiner `S^μ ≃ S^ν` forces `μ ⊵ ν`.  All the machinery is upstream:

* `SpechtCrossKappa.kapL_polytabloid` — `κ_t e_t = |C_t| · e_t`, which keeps the
  argument inside `S^μ` and so avoids extending the intertwiner to `M^μ`;
* `SpechtCrossKappa.kapCross` — `κ_t` acting on `M^ν`, and its vanishing on a
  clash;
* `SpechtCrossDominance.dominance_of_tableau_noclash` — Sagan Lemma 2.2.6.
-/

/-- Every diagram admits a tableau: `nOf μ` is by definition the number of
cells. -/
theorem nonempty_tableau (μ : YoungDiagram) : Nonempty (Specht.Tableau μ) :=
  ⟨(Fintype.equivFinOfCardEq (Fintype.card_coe μ.cells)).symm⟩

open scoped BigOperators in
/-- The `κ_t` computation at the heart of Sagan Thm 2.4.4 (the step that avoids
extending `θ` to `M^μ`): because `κ_t e_t = |C_t| e_t` stays inside `S^μ`,
equivariance of `θ` on `S^μ` alone gives `κ_t (θ e_t) = |C_t| · θ e_t ≠ 0`.
Expanding `θ e_t` in the `ν`-tabloid basis then produces a tabloid with
`κ_t {s} ≠ 0`, and Lemma 2.2.6 converts that into dominance: an equivariant
`θ : S^μ → M^ν` not killing the polytabloid `e_t` forces `μ ⊵ ν`. -/
theorem dom_of_kapCross {μ ν : YoungDiagram} (h : Specht.nOf μ = Specht.nOf ν)
    (t : Specht.Tableau μ)
    (θ : Specht.SpechtSubmodule (k := k) μ →ₗ[k] Specht.Mtab (k := k) ν)
    (hθ : ∀ (σ : Perm (Fin (Specht.nOf μ))) (x : Specht.SpechtSubmodule (k := k) μ),
      θ (spechtRep (k := k) μ σ x)
        = Specht.Mtab.rep ν (SpechtCrossKappa.transportPerm h σ) (θ x))
    (ht : θ ⟨Specht.polytabloid (k := k) t, Specht.polytabloid_mem_specht t⟩ ≠ 0) :
    partitionDom μ ν := by
  classical
  set y : Specht.SpechtSubmodule (k := k) μ :=
    ⟨Specht.polytabloid (k := k) t, Specht.polytabloid_mem_specht t⟩ with hy
  have heyne : θ y ≠ 0 := ht
  -- inside `S^μ`, the `C_t`-sum is `|C_t| • y`  (`κ_t e_t = |C_t| e_t`)
  have hsum : (∑ π : Specht.colStab t,
        (Equiv.Perm.sign (π : Perm (Fin (Specht.nOf μ))) : ℤ) •
          spechtRep (k := k) μ (π : Perm (Fin (Specht.nOf μ))) y)
      = (Fintype.card (Specht.colStab t)) • y := by
    refine Subtype.ext ?_
    have hL : (((∑ π : Specht.colStab t,
          (Equiv.Perm.sign (π : Perm (Fin (Specht.nOf μ))) : ℤ) •
            spechtRep (k := k) μ (π : Perm (Fin (Specht.nOf μ))) y) :
              Specht.SpechtSubmodule (k := k) μ) : Specht.Mtab (k := k) μ)
        = ∑ π : Specht.colStab t,
            (Equiv.Perm.sign (π : Perm (Fin (Specht.nOf μ))) : ℤ) •
              Specht.Mtab.rep μ (π : Perm (Fin (Specht.nOf μ)))
                (Specht.polytabloid (k := k) t) := by
      rw [Submodule.coe_sum]
      exact Finset.sum_congr rfl (fun π _ => rfl)
    rw [hL, ← SpechtIrreducible.kapL_apply, SpechtCrossKappa.kapL_polytabloid]
    simp [hy]
  -- therefore `κ_t (θ y) = |C_t| • θ y`
  have hkap : SpechtCrossKappa.kapCross (k := k) h t (θ y)
      = (Fintype.card (Specht.colStab t)) • θ y := by
    rw [SpechtCrossKappa.kapCross_apply]
    have hterm : ∀ π : Specht.colStab t,
        (Equiv.Perm.sign (π : Perm (Fin (Specht.nOf μ))) : ℤ) •
            Specht.Mtab.rep ν (SpechtCrossKappa.transportPerm h
              (π : Perm (Fin (Specht.nOf μ)))) (θ y)
          = θ ((Equiv.Perm.sign (π : Perm (Fin (Specht.nOf μ))) : ℤ) •
              spechtRep (k := k) μ (π : Perm (Fin (Specht.nOf μ))) y) := by
      intro π
      rw [map_zsmul, hθ]
    rw [Finset.sum_congr rfl (fun π _ => hterm π), ← map_sum, hsum, map_nsmul]
  -- `|C_t| ≠ 0` in char 0, so `κ_t` does not kill `θ y`
  have hne : SpechtCrossKappa.kapCross (k := k) h t (θ y) ≠ 0 := by
    rw [hkap]
    haveI : Nonempty (Specht.colStab t) := ⟨1⟩
    intro hzero
    rw [← Nat.cast_smul_eq_nsmul (R := k)] at hzero
    rcases smul_eq_zero.mp hzero with hc | hv
    · exact (Nat.cast_ne_zero.mpr Fintype.card_ne_zero) hc
    · exact heyne hv
  -- so some `ν`-tabloid survives `κ_t`; Lemma 2.2.6 turns that into dominance
  by_contra hdom
  refine hne ?_
  have hall : ∀ s : Specht.Tableau ν,
      SpechtCrossKappa.kapCross (k := k) h t (Specht.Mtab.of s) = 0 := by
    intro s
    by_contra hs
    exact hdom (SpechtCrossKappa.dominance_of_kapCross_ne_zero (k := k) h t s hs)
  have hzeroMap : SpechtCrossKappa.kapCross (k := k) h t = 0 := by
    refine Finsupp.lhom_ext (fun d c => ?_)
    obtain ⟨s, rfl⟩ := Quotient.exists_rep d
    show SpechtCrossKappa.kapCross (k := k) h t
        (Finsupp.single (Specht.Tabloid.mk s) c) = (0 : Specht.Mtab (k := k) ν →ₗ[k] _) _
    have hsingle : (Finsupp.single (Specht.Tabloid.mk s) c : Specht.Mtab (k := k) ν)
        = c • Specht.Mtab.of s := by
      rw [Specht.Mtab.of, Finsupp.smul_single, smul_eq_mul, mul_one]
    rw [hsingle, map_smul, hall s, smul_zero, LinearMap.zero_apply]
  rw [hzeroMap, LinearMap.zero_apply]

open scoped BigOperators in
/-- **Sagan Thm 2.4.4, hom form.**  A nonzero equivariant `θ : S^μ → M^ν` forces
`μ ⊵ ν`.  This is the general statement; the isomorphism version below is the
special case `θ = (inclusion) ∘ e`.

`θ ≠ 0` gives a polytabloid it does not kill, because the `e_t` span `S^μ`. -/
theorem dom_of_nonzero_hom {μ ν : YoungDiagram} (h : Specht.nOf μ = Specht.nOf ν)
    (θ : Specht.SpechtSubmodule (k := k) μ →ₗ[k] Specht.Mtab (k := k) ν)
    (hθ : ∀ (σ : Perm (Fin (Specht.nOf μ))) (x : Specht.SpechtSubmodule (k := k) μ),
      θ (spechtRep (k := k) μ σ x)
        = Specht.Mtab.rep ν (SpechtCrossKappa.transportPerm h σ) (θ x))
    (hne : θ ≠ 0) :
    partitionDom μ ν := by
  classical
  -- some polytabloid survives `θ`: they span `S^μ`
  obtain ⟨t, ht⟩ : ∃ t : Specht.Tableau μ,
      θ ⟨Specht.polytabloid (k := k) t, Specht.polytabloid_mem_specht t⟩ ≠ 0 := by
    by_contra hall
    push_neg at hall
    refine hne (LinearMap.ext (fun x => ?_))
    rw [LinearMap.zero_apply]
    obtain ⟨v, hv⟩ := x
    induction hv using Submodule.span_induction with
    | mem z hz =>
        obtain ⟨t, rfl⟩ := hz
        exact hall t
    | zero => exact map_zero θ
    | add z w hz hw ihz ihw =>
        have hsplit : (⟨z + w, Submodule.add_mem _ hz hw⟩ :
            Specht.SpechtSubmodule (k := k) μ) = ⟨z, hz⟩ + ⟨w, hw⟩ := rfl
        rw [hsplit, map_add, ihz, ihw, add_zero]
    | smul c z hz ihz =>
        have hsplit : (⟨c • z, Submodule.smul_mem _ c hz⟩ :
            Specht.SpechtSubmodule (k := k) μ) = c • ⟨z, hz⟩ := rfl
        rw [hsplit, map_smul, ihz, smul_zero]
  exact dom_of_kapCross h t θ hθ ht

open scoped BigOperators in
/-- **Sagan Thm 2.4.4 for an isomorphism.**  A `k`-linear intertwiner
`S^μ ≃ S^ν` (for `Perm (Fin (nOf μ))` acting on `S^ν` through `h`) forces `μ ⊵ ν`.
Immediate from `dom_of_nonzero_hom` applied to `e` followed by the inclusion
`S^ν ↪ M^ν`. -/
theorem dom_of_intertwiner {μ ν : YoungDiagram} (h : Specht.nOf μ = Specht.nOf ν)
    (e : Specht.SpechtSubmodule (k := k) μ ≃ₗ[k] Specht.SpechtSubmodule (k := k) ν)
    (he : ∀ (σ : Perm (Fin (Specht.nOf μ))) (x : Specht.SpechtSubmodule (k := k) μ),
      e (spechtRep (k := k) μ σ x) = spechtRepOn (k := k) h σ (e x)) :
    partitionDom μ ν := by
  classical
  refine dom_of_nonzero_hom h ((Specht.SpechtSubmodule (k := k) ν).subtype ∘ₗ (e : _ →ₗ[k] _))
    (fun σ x => ?_) ?_
  · show ((e (spechtRep (k := k) μ σ x) : Specht.SpechtSubmodule (k := k) ν) :
        Specht.Mtab (k := k) ν) = _
    rw [he]
    rfl
  · -- `e` is injective and `S^μ ≠ 0`, so the composite is nonzero
    obtain ⟨t⟩ := nonempty_tableau μ
    intro hzero
    set y : Specht.SpechtSubmodule (k := k) μ :=
      ⟨Specht.polytabloid (k := k) t, Specht.polytabloid_mem_specht t⟩ with hy
    have hyne : y ≠ 0 := fun hz =>
      SpechtCrossKappa.polytabloid_ne_zero (K := k) μ t (congrArg Subtype.val hz)
    refine hyne ?_
    have hcoe : ((e y : Specht.SpechtSubmodule (k := k) ν) :
        Specht.Mtab (k := k) ν) = 0 := by
      have hv := LinearMap.congr_fun hzero y
      simpa using hv
    have h0 : e y = 0 := Subtype.ext hcoe
    have hb := congrArg e.symm h0
    rwa [e.symm_apply_apply, map_zero] at hb

/-- **James/Sagan cross-shape dominance — PROVED.**  A representation isomorphism
`S^μ ≅ S^ν` (over the shared group via `h`) forces dominance both ways:
`partitionDom μ ν ∧ partitionDom ν μ`.

Sagan Thm 2.4.4.  Each direction is `dom_of_intertwiner` above; the reverse one
re-indexes the acting group through `transportPermHom h.symm`, using that the two
transports are mutually inverse.

Mathlib packages neither the cross-shape dominance bound nor the tableau
combinatorics it rests on; the ingredients are built in
`QOU.BraidKnot.SpechtCrossDominance` (Sagan Lemma 2.2.6) and
`QOU.BraidKnot.SpechtCrossKappa` (the cross-shape `κ_t`).

`#print axioms` reports `[propext, Classical.choice, Quot.sound]`. -/
theorem spechtIso_imp_dom_both {μ ν : YoungDiagram} (h : Specht.nOf μ = Specht.nOf ν)
    (hiso : IsRepIso (k := k) (spechtRep (k := k) μ) (spechtRepOn (k := k) h)) :
    partitionDom μ ν ∧ partitionDom ν μ := by
  -- Ref: [sagan2001] Thm 2.4.4 / [james1984representation] §II.
  obtain ⟨e, he⟩ := hiso.exists_intertwiner
  refine ⟨dom_of_intertwiner h e he, ?_⟩
  -- the reverse direction: invert the intertwiner and re-index the acting group
  refine dom_of_intertwiner h.symm e.symm (fun τ y => ?_)
  have hround : transportPermHom h (transportPermHom h.symm τ) = τ :=
    Equiv.ext (fun _ => Fin.ext rfl)
  have hkey := he (transportPermHom h.symm τ) (e.symm y)
  rw [e.apply_symm_apply] at hkey
  show e.symm (spechtRep (k := k) ν τ y)
      = spechtRep (k := k) μ (transportPermHom h.symm τ) (e.symm y)
  have : spechtRep (k := k) ν τ y
      = spechtRepOn (k := k) h (transportPermHom h.symm τ) y := by
    show _ = spechtRep (k := k) ν (transportPermHom h (transportPermHom h.symm τ)) y
    rw [hround]
  rw [this, ← hkey, e.symm_apply_apply]

/-- **Pairwise non-isomorphism.**  Distinct shapes give non-isomorphic Specht
modules: if `μ ≠ ν` (with the same number of cells, so they index the *same*
symmetric group), then `S^μ` and `S^ν` are not isomorphic as `S_n`-representations.

We state it via the intertwiner predicate over the shared carrier index `nOf μ`,
using the hypothesis `h : nOf μ = nOf ν` to view `spechtRep ν` as a representation
of `Perm (Fin (nOf μ))` (by transporting along `h`).

**Now sorry-free modulo the single James core** `spechtIso_imp_dom_both`: an
isomorphism gives dominance both ways, and the proved `partitionDom_antisymm`
turns that into `μ = ν`, contradicting `μ ≠ ν`. -/
theorem specht_pairwise_noniso {μ ν : YoungDiagram} (h : Specht.nOf μ = Specht.nOf ν)
    (hμν : μ ≠ ν) :
    ¬ IsRepIso (k := k) (spechtRep (k := k) μ) (spechtRepOn (k := k) h) := by
  intro hiso
  obtain ⟨hd1, hd2⟩ := spechtIso_imp_dom_both (k := k) h hiso
  exact hμν (partitionDom_antisymm μ ν hd1 hd2)

/-! ### Finiteness and simplicity of `S^μ`, in the form the character count wants

`RepresentationCharacter` states Schur with simplicity as "every stable subspace
is `⊥` or `⊤`" of the *carrier*, whereas `specht_isSimple` speaks of submodules
of `M^μ` contained in `S^μ`. These three lemmas bridge that and supply the
finiteness the character pairing needs. -/

instance spechtSubmodule_finite (μ : YoungDiagram) :
    Module.Finite k (Specht.SpechtSubmodule (k := k) μ) := by
  haveI : Module.Finite k (Specht.Mtab (k := k) μ) := by
    unfold Specht.Mtab; infer_instance
  infer_instance

instance spechtSubmodule_nontrivial (μ : YoungDiagram) :
    Nontrivial (Specht.SpechtSubmodule (k := k) μ) := by
  obtain ⟨t⟩ := nonempty_tableau μ
  exact ⟨⟨⟨Specht.polytabloid (k := k) t, Specht.polytabloid_mem_specht t⟩, 0, fun h =>
    SpechtCrossKappa.polytabloid_ne_zero (K := k) μ t (congrArg Subtype.val h)⟩⟩

/-- `specht_isSimple`, transported from submodules of `M^μ` inside `S^μ` to
submodules of the carrier `S^μ` itself. -/
theorem spechtRep_stable_eq_bot_or_top (μ : YoungDiagram)
    (p : Submodule k (Specht.SpechtSubmodule (k := k) μ))
    (hp : ∀ (g : Perm (Fin (Specht.nOf μ))) v, v ∈ p → spechtRep (k := k) μ g v ∈ p) :
    p = ⊥ ∨ p = ⊤ := by
  have hinj : Function.Injective (Specht.SpechtSubmodule (k := k) μ).subtype :=
    Submodule.subtype_injective _
  have hle : p.map (Specht.SpechtSubmodule (k := k) μ).subtype
      ≤ Specht.SpechtSubmodule (k := k) μ := by
    rintro _ ⟨x, -, rfl⟩; exact x.2
  have hstable : ∀ (σ : Perm (Fin (Specht.nOf μ))) x,
      x ∈ p.map (Specht.SpechtSubmodule (k := k) μ).subtype →
      Specht.Mtab.rep μ σ x ∈ p.map (Specht.SpechtSubmodule (k := k) μ).subtype := by
    rintro σ _ ⟨x, hx, rfl⟩
    exact ⟨spechtRep (k := k) μ σ x, hp σ x hx, rfl⟩
  rcases SpechtIrreducible.specht_isSimple (k := k) μ _ hle hstable with h | h
  · refine Or.inl (Submodule.map_injective_of_injective hinj ?_)
    rw [h, Submodule.map_bot]
  · refine Or.inr (Submodule.map_injective_of_injective hinj ?_)
    rw [h, Submodule.map_subtype_top]

/-! ### Transporting the acting group

The count runs over representations of the *same* group `Perm (Fin n)`, while
`spechtRep μ` acts through `Perm (Fin (nOf μ))`. `spechtRepAt` is the composite
appearing in `specht_exhausts_irreducibles`'s own statement; the two lemmas
below move simplicity and non-isomorphism across it, using only that the
transport is bijective. -/

theorem transportPermHom_surjective {a b : ℕ} (h : a = b) :
    Function.Surjective (transportPermHom h) := fun τ =>
  ⟨transportPermHom h.symm τ, Equiv.ext (fun _ => Fin.ext rfl)⟩

/-- `S^μ` as a representation of `Perm (Fin n)`, for `h : nOf μ = n`.  This is
the composite that `specht_exhausts_irreducibles` compares against. -/
noncomputable def spechtRepAt {n : ℕ} {μ : YoungDiagram} (h : Specht.nOf μ = n) :
    Representation k (Perm (Fin n)) (Specht.SpechtSubmodule (k := k) μ) :=
  (spechtRep (k := k) μ).comp (transportPermHom h.symm)

theorem spechtRepAt_stable {n : ℕ} {μ : YoungDiagram} (h : Specht.nOf μ = n)
    (p : Submodule k (Specht.SpechtSubmodule (k := k) μ))
    (hp : ∀ (g : Perm (Fin n)) v, v ∈ p → spechtRepAt (k := k) h g v ∈ p) :
    p = ⊥ ∨ p = ⊤ := by
  refine spechtRep_stable_eq_bot_or_top μ p (fun τ v hv => ?_)
  obtain ⟨g, rfl⟩ := transportPermHom_surjective h.symm τ
  exact hp g v hv

/-- Distinct shapes stay non-isomorphic after the transport. -/
theorem spechtRepAt_noniso {n : ℕ} {μ ν : YoungDiagram} (hμ : Specht.nOf μ = n)
    (hν : Specht.nOf ν = n) (hne : μ ≠ ν)
    (e : Specht.SpechtSubmodule (k := k) μ ≃ₗ[k] Specht.SpechtSubmodule (k := k) ν) :
    ¬ ∀ (g : Perm (Fin n)) (v : Specht.SpechtSubmodule (k := k) μ),
        e (spechtRepAt (k := k) hμ g v) = spechtRepAt (k := k) hν g (e v) := by
  intro he
  refine specht_pairwise_noniso (k := k) (hμ.trans hν.symm) hne ⟨e, fun τ x => ?_⟩
  obtain ⟨g, rfl⟩ := transportPermHom_surjective hμ.symm τ
  have hround : transportPermHom (hμ.trans hν.symm) (transportPermHom hμ.symm g)
      = transportPermHom hν.symm g := Equiv.ext (fun _ => Fin.ext rfl)
  show e (spechtRep (k := k) μ (transportPermHom hμ.symm g) x)
      = spechtRep (k := k) ν (transportPermHom (hμ.trans hν.symm)
          (transportPermHom hμ.symm g)) (e x)
  rw [hround]
  exact he g x

/-- **Completeness.**  Every simple `k[S_n]`-module is isomorphic to some Specht
module.  Phrased: for any representation `ρ : Representation k (Perm (Fin n)) W`
that is simple as a `k[S_n]`-module — stated as
`IsSimpleModule (MonoidAlgebra k (Perm (Fin n))) ρ.asModule`, using the
`MonoidAlgebra k G`-module structure on `ρ.asModule` (Mathlib
`Representation.asModule`) — there is a Young diagram `μ` with `nOf μ = n` and a
representation isomorphism `ρ ≅ spechtRep μ` (after transporting the acting group
along `nOf μ = n`).

This is the half of the classification that says the Specht modules **exhaust** the
irreducibles.

## Proved

The Specht modules are `#partitions` many pairwise non-isomorphic simples
(`specht_isSimple` + `specht_pairwise_noniso`), and there are no others. The
"no others" half is a **count**, every step of it a bound:

    #{pairwise non-isomorphic simples}
      ≤ dim_k {class functions on Sₙ}      characters are independent class functions
      ≤ #conj classes of Sₙ                a class function is its values on classes
      ≤ #partitions of n                   cycle type separates conjugacy classes

Assuming an extra simple `W` isomorphic to no `S^μ` gives `#partitions + 1`
pairwise non-isomorphic simples, contradicting the chain.

Independence of the characters comes from the pairing

    ⅟|G| • Σ_g χ_V(g⁻¹)·χ_W(g) = dim_k Hom_G(V, W)

(`RepresentationCharacter.charPairing_eq_finrank_homG`), which is **diagonal**
by Schur and has **nonzero diagonal** because the identity is equivariant. Note
what is *not* needed: `FDRep.char_orthonormal` normalises that diagonal to `1`
and carries `[IsAlgClosed k]` to do it, but a bound only needs the diagonal
nonzero — so the whole argument runs over an arbitrary characteristic-zero
field, `ℚ` included.

`#print axioms` reports `[propext, Classical.choice, Quot.sound]`.

## Supporting modules

| Module | Role |
|---|---|
| `QOU.MathlibExt.RepresentationCharacter` | character theory on `Representation`, off Mathlib's `FDRep` category layer; Schur; the count |
| `QOU.MathlibExt.GroupAlgebraCenter` | class functions and their dimension; conjugacy classes inject into partitions |
| `QOU.MathlibExt.GramNondegenerate` | a diagonal Gram matrix with nonzero diagonal gives linear independence |

Closes bean sp06. -/
theorem specht_exhausts_irreducibles {n : ℕ} {W : Type} [AddCommGroup W] [Module k W]
    (ρ : Representation k (Perm (Fin n)) W)
    (hsimple : IsSimpleModule (MonoidAlgebra k (Perm (Fin n))) ρ.asModule) :
    ∃ (μ : YoungDiagram) (h : Specht.nOf μ = n),
      IsRepIso (k := k) ρ
        ((spechtRep (k := k) μ).comp (transportPermHom h.symm)) := by
  classical
  by_contra hcon
  push_neg at hcon
  haveI := hsimple
  -- `W` is nonzero …
  haveI hWnt : Nontrivial W := by
    have hnt : Nontrivial ρ.asModule :=
      (Submodule.nontrivial_iff (MonoidAlgebra k (Perm (Fin n)))).mp inferInstance
    exact hnt
  obtain ⟨w, hw⟩ := exists_ne (0 : W)
  -- … and finite-dimensional: it is a quotient of the group algebra
  haveI hAfin : Module.Finite k (MonoidAlgebra k (Perm (Fin n))) := by
    unfold MonoidAlgebra; infer_instance
  haveI hWfin : Module.Finite k W := by
    refine Module.Finite.of_surjective
      ((LinearMap.applyₗ w).comp ρ.asAlgebraHom.toLinearMap) ?_
    refine LinearMap.range_eq_top.mp ?_
    refine (QOU.MathlibExt.RepresentationCharacter.stable_eq_bot_or_top ρ _ ?_).resolve_left ?_
    · rintro g _ ⟨r, rfl⟩
      refine ⟨MonoidAlgebra.single g 1 * r, ?_⟩
      show ρ.asAlgebraHom (MonoidAlgebra.single g 1 * r) w = ρ g (ρ.asAlgebraHom r w)
      rw [map_mul, Representation.asAlgebraHom_single_one]
      rfl
    · intro hbot
      refine hw ?_
      have : ((LinearMap.applyₗ w).comp ρ.asAlgebraHom.toLinearMap) 1 = 0 := by
        rw [← Submodule.mem_bot (R := k), ← hbot]
        exact LinearMap.mem_range_self _ _
      simpa using this
  haveI : Invertible ((Fintype.card (Perm (Fin n)) : k)) :=
    invertibleOfNonzero (Nat.cast_ne_zero.mpr Fintype.card_ne_zero)
  -- the characters of the Specht modules together with that of `ρ`
  set χ : Option (PartitionIndex n) → (Perm (Fin n) → k) := fun o =>
    Option.rec (QOU.MathlibExt.RepresentationCharacter.charOf ρ)
      (fun i => QOU.MathlibExt.RepresentationCharacter.charOf (spechtRepAt (k := k) i.property)) o with hχ
  -- simplicity, in the stable-subspace form Schur wants
  have hsimpW : ∀ p : Submodule k W, (∀ g v, v ∈ p → ρ g v ∈ p) → p = ⊥ ∨ p = ⊤ :=
    QOU.MathlibExt.RepresentationCharacter.stable_eq_bot_or_top ρ
  have hsimpS : ∀ i : PartitionIndex n,
      ∀ p : Submodule k (Specht.SpechtSubmodule (k := k) i.diagram),
        (∀ g v, v ∈ p → spechtRepAt (k := k) i.property g v ∈ p) → p = ⊥ ∨ p = ⊤ :=
    fun i => spechtRepAt_stable i.property
  -- off-diagonal: non-isomorphic simples have orthogonal characters
  have hoff : ∀ a b, a ≠ b →
      QOU.MathlibExt.RepresentationCharacter.charForm k (Perm (Fin n)) (χ a) (χ b) = 0 := by
    intro a b hab
    have key : ∀ {V₁ V₂ : Type} [AddCommGroup V₁] [Module k V₁] [Module.Finite k V₁]
        [AddCommGroup V₂] [Module k V₂] [Module.Finite k V₂]
        (ρ₁ : Representation k (Perm (Fin n)) V₁) (ρ₂ : Representation k (Perm (Fin n)) V₂),
        (∀ p : Submodule k V₁, (∀ g v, v ∈ p → ρ₁ g v ∈ p) → p = ⊥ ∨ p = ⊤) →
        (∀ p : Submodule k V₂, (∀ g v, v ∈ p → ρ₂ g v ∈ p) → p = ⊥ ∨ p = ⊤) →
        (∀ e : V₁ ≃ₗ[k] V₂, ¬ ∀ (g : Perm (Fin n)) (v : V₁), e (ρ₁ g v) = ρ₂ g (e v)) →
        QOU.MathlibExt.RepresentationCharacter.charForm k (Perm (Fin n))
          (QOU.MathlibExt.RepresentationCharacter.charOf ρ₁) (QOU.MathlibExt.RepresentationCharacter.charOf ρ₂) = 0 := by
      intro V₁ _ _ _ V₂ _ _ _ ρ₁ ρ₂ h₁ h₂ hno
      rw [QOU.MathlibExt.RepresentationCharacter.charForm_charOf,
        QOU.MathlibExt.RepresentationCharacter.homG_eq_bot h₁ h₂ hno]
      simp
    match a, b with
    | none, none => exact absurd rfl hab
    | none, some i =>
        exact key ρ _ hsimpW (hsimpS i)
          (fun e he => hcon i.diagram i.property ⟨e, fun g x => he g x⟩)
    | some i, none =>
        refine key _ ρ (hsimpS i) hsimpW (fun e he => ?_)
        refine hcon i.diagram i.property ⟨e.symm, fun g x => ?_⟩
        have := he g (e.symm x)
        rw [e.apply_symm_apply] at this
        exact (e.symm_apply_eq).mpr this.symm
    | some i, some j =>
        refine key _ _ (hsimpS i) (hsimpS j) (fun e => ?_)
        exact spechtRepAt_noniso i.property j.property
          (fun hd => hab (congrArg some (Subtype.ext hd))) e
  -- diagonal: the identity is equivariant, so `dim Hom_G ≥ 1`, nonzero in char 0
  have hdiag : ∀ a, QOU.MathlibExt.RepresentationCharacter.charForm k (Perm (Fin n)) (χ a) (χ a) ≠ 0 := by
    have key : ∀ {V₁ : Type} [AddCommGroup V₁] [Module k V₁] [Module.Finite k V₁]
        [Nontrivial V₁] (ρ₁ : Representation k (Perm (Fin n)) V₁),
        QOU.MathlibExt.RepresentationCharacter.charForm k (Perm (Fin n))
          (QOU.MathlibExt.RepresentationCharacter.charOf ρ₁) (QOU.MathlibExt.RepresentationCharacter.charOf ρ₁) ≠ 0 := by
      intro V₁ _ _ _ _ ρ₁
      rw [QOU.MathlibExt.RepresentationCharacter.charForm_charOf]
      exact Nat.cast_ne_zero.mpr
        (Nat.one_le_iff_ne_zero.mp
          (QOU.MathlibExt.RepresentationCharacter.one_le_finrank_homG_self ρ₁))
    intro a
    match a with
    | none => exact key ρ
    | some i => exact key _
  -- the count, against the number of partitions
  have hcard := QOU.MathlibExt.RepresentationCharacter.card_le_card_conjClasses_of_orthogonal χ
    (fun a => by
      match a with
      | none => exact fun g h => QOU.MathlibExt.RepresentationCharacter.charOf_conj ρ g h
      | some i => exact fun g h => QOU.MathlibExt.RepresentationCharacter.charOf_conj _ g h)
    hoff hdiag
  rw [Fintype.card_option, card_partitionIndex] at hcard
  have hle := QOU.MathlibExt.GroupAlgebraCenter.card_conjClasses_perm_fin_le n
  omega

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


/-! ### Removed 2026-08-30 — self-assuming projections

- `diagram_card` — body was `i.property`: the conclusion was the projected field
  verbatim, so the declaration restated its own hypothesis.

**Why removal.** The content stays in the class field each declaration
projected, which asserts the same proposition under the same hypotheses; only
the restatement goes. That is the vacuity ledger's recorded disposition for
this category — *"drop the pseudo-theorem and project the field at use sites"*
— and there were no use sites: each had **zero references anywhere in the
corpus**, including in this file. Bean `qou-z9ws`.
-/

end QOU.BraidKnot.SpechtClassification
