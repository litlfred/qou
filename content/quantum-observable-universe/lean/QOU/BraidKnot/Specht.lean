import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.GroupTheory.Perm.Sign
import Mathlib.GroupTheory.GroupAction.Defs
import Mathlib.Algebra.MonoidAlgebra.Basic
import Mathlib.LinearAlgebra.Finsupp.LSum
import Mathlib.RepresentationTheory.Basic
import QOU.BraidKnot.StandardYoungTableau

/-!
# QOU.BraidKnot.Specht — brick 2 of the Okounkov–Vershik tower

The classical **Specht-module** construction `S^μ` for a `YoungDiagram μ` with
`n = μ.card`, following Sagan, *The Symmetric Group* (§2.3–2.5) and James,
*The Representation Theory of the Symmetric Groups*.

This is "brick 2" of the QOU OV-tower; it builds on brick 1
(`QOU.BraidKnot.StandardYoungTableau`, the SYT count `numSYT`, imported above).

## What is sorry-free here

The whole *definitional* foundation is verified, `sorry`-free:

* `Tableau μ` — general (bijective) `Fin n`-fillings of `μ`'s cells.
* the `S_n`-action on tableaux (`Tableau.smul`, a `MulAction`).
* `rowPattern` / `colPattern` — the row/column membership data of a tableau,
  together with the `S_n`-action on them (`MulAction (Perm (Fin n)) (Fin n → ℕ)`).
* `rowStab` / `colStab` — row/column stabilizers as honest `Subgroup`s
  (literally `MulAction.stabilizer` of the patterns).
* `Tabloid μ` — the row-equivalence quotient, with `Fintype`/`DecidableEq`.
* `Mtab μ` — the permutation module `Tabloid μ →₀ k`, with its `S_n`
  representation `Mtab.rep` (a `Representation k (Perm (Fin n)) (Mtab μ)`).
* `polytabloid` and `SpechtSubmodule μ` (the latter is a `Submodule` *by
  construction*, being a `Submodule.span`).

## What is stated with `sorry` + `-- Ref:` (the genuine theorems)

* `specht_isSimple` — `S^μ` is irreducible over a char-0 field
  (`-- Ref: [james1984representation]`).
* `specht_finrank_eq_numSYT` — `dim S^μ = #SYT(μ)` (the standard-basis theorem)
  (`-- Ref: [sagan2001]`, Thm 2.5.2 / the standard polytabloid basis).

Both are textbook-famous theorems whose Lean proofs are out of scope for one
brick; they are honestly stubbed per AGENTS.md §1.

This module is intentionally **not** imported by the `QOU.BraidKnot` umbrella:
it carries two honest `sorry` targets (the deep theorems above), so wiring it
into the CI build would taint the umbrella's sorry-free surface.  It is verified
to compile standalone via `lean`-direct against the pinned v4.24.0 oleans.

## Conventions

Following brick 1, `μ : YoungDiagram` and a cell is `(i, j) : ℕ × ℕ` with
`(i, j) ∈ μ`.  We work over a base type `k` that is a field where simplicity is
discussed, and a generic `[CommRing k]` for the module-level construction
(nothing archimedean — §7c: no `ℝ`, no ordering, no `Real.*`).

## References
- [sagan2001] Sagan, *The Symmetric Group*, §2.3–2.5 (tabloids, polytabloids,
  Specht modules, the standard basis Thm 2.5.2).
- [james1984representation] James, *The Representation Theory of the Symmetric
  Groups* (Specht modules, irreducibility in char 0).
- [fulton1997] Fulton, *Young Tableaux* (tableaux / tabloids).
-/

open scoped BigOperators

namespace QOU.BraidKnot.Specht

variable {k : Type} [CommRing k]

/-- `nOf μ` is the number of cells of `μ`, i.e. the rank of the symmetric group
acting on tableaux of shape `μ`.  Abbreviation for `μ.card`. -/
abbrev nOf (μ : YoungDiagram) : ℕ := μ.card

/-! ## 1. General tableaux -/

/-- A **(general) `μ`-tableau** is a bijective filling of the cells of `μ` by the
labels `Fin n` (`n = μ.card`).  We carry it as an equivalence `Fin n ≃ μ.cells`:
`t l` is the cell holding label `l`.  Unlike `StandardYoungTableau` (brick 1)
these fillings are **arbitrary** bijections — no monotonicity is imposed.

Marked `@[reducible]` (the standard idiom for a free-construction wrapper) so
that `t l`, the `Equiv` operations, and the `Fintype`/`DecidableEq` instances on
`Fin n ≃ μ.cells` are transparently available. -/
@[reducible] def Tableau (μ : YoungDiagram) : Type :=
  Fin (nOf μ) ≃ μ.cells

namespace Tableau

/-- The `S_n`-action on `μ`-tableaux: `σ • t` relabels label `l` to the cell
that `t` assigned to `σ⁻¹ l`, i.e. precomposition by `σ⁻¹`.  Concretely
`(σ • t) = t ∘ σ⁻¹` as an `Equiv`. -/
instance instMulAction (μ : YoungDiagram) :
    MulAction (Equiv.Perm (Fin (nOf μ))) (Tableau μ) where
  smul σ t := (σ.symm.trans t : Fin (nOf μ) ≃ μ.cells)
  one_smul t := Equiv.ext fun l => rfl
  mul_smul σ τ t := Equiv.ext fun l => by
    show t ((σ * τ).symm l) = t (τ.symm (σ.symm l))
    rw [Equiv.Perm.mul_def, Equiv.symm_trans_apply]

@[simp] theorem smul_apply (μ : YoungDiagram) (σ : Equiv.Perm (Fin (nOf μ)))
    (t : Tableau μ) (l : Fin (nOf μ)) :
    (σ • t) l = t (σ.symm l) := rfl

end Tableau

/-! ## 2. Row / column patterns and stabilizers -/

/-- The **row pattern** of a tableau: `rowPattern t l` is the row index `(t l).1.1`
of the cell holding label `l`.  Two tableaux are row-equivalent iff they have the
same row pattern (up to within-row reshuffling), and the row stabilizer is the
stabilizer of this pattern. -/
def rowPattern {μ : YoungDiagram} (t : Tableau μ) : Fin (nOf μ) → ℕ :=
  fun l => (t l : ℕ × ℕ).1

/-- The **column pattern** of a tableau: `colPattern t l` is the column index
`(t l).1.2` of the cell holding label `l`. -/
def colPattern {μ : YoungDiagram} (t : Tableau μ) : Fin (nOf μ) → ℕ :=
  fun l => (t l : ℕ × ℕ).2

/-- The `S_n`-action on label-indexed data `Fin n → ℕ` by relabelling
(`σ • f = f ∘ σ⁻¹`).  This is the action whose stabilizers are the Young
row/column subgroups. -/
instance instArrowMulAction (μ : YoungDiagram) :
    MulAction (Equiv.Perm (Fin (nOf μ))) (Fin (nOf μ) → ℕ) where
  smul σ f := fun l => f (σ.symm l)
  one_smul f := by funext l; rfl
  mul_smul σ τ f := by
    funext l
    show f ((σ * τ).symm l) = f (τ.symm (σ.symm l))
    rw [Equiv.Perm.mul_def, Equiv.symm_trans_apply]

@[simp] theorem arrow_smul_apply (μ : YoungDiagram) (σ : Equiv.Perm (Fin (nOf μ)))
    (f : Fin (nOf μ) → ℕ) (l : Fin (nOf μ)) :
    (σ • f) l = f (σ.symm l) := rfl

/-- `rowPattern` is equivariant: `rowPattern (σ • t) = σ • rowPattern t`. -/
@[simp] theorem rowPattern_smul {μ : YoungDiagram} (σ : Equiv.Perm (Fin (nOf μ)))
    (t : Tableau μ) : rowPattern (σ • t) = σ • rowPattern t := by
  funext l; simp [rowPattern]

/-- `colPattern` is equivariant: `colPattern (σ • t) = σ • colPattern t`. -/
@[simp] theorem colPattern_smul {μ : YoungDiagram} (σ : Equiv.Perm (Fin (nOf μ)))
    (t : Tableau μ) : colPattern (σ • t) = σ • colPattern t := by
  funext l; simp [colPattern]

/-- The **row stabilizer** `R_t` of a tableau `t`: the subgroup of `S_n`
preserving the rows of `t` setwise.  Defined as the `MulAction.stabilizer` of the
row pattern, hence automatically a `Subgroup`. -/
def rowStab {μ : YoungDiagram} (t : Tableau μ) : Subgroup (Equiv.Perm (Fin (nOf μ))) :=
  MulAction.stabilizer (Equiv.Perm (Fin (nOf μ))) (rowPattern t)

/-- The **column stabilizer** `C_t` of a tableau `t`: the subgroup of `S_n`
preserving the columns of `t` setwise.  Defined as the `MulAction.stabilizer` of
the column pattern. -/
def colStab {μ : YoungDiagram} (t : Tableau μ) : Subgroup (Equiv.Perm (Fin (nOf μ))) :=
  MulAction.stabilizer (Equiv.Perm (Fin (nOf μ))) (colPattern t)

/-- Membership in the row stabilizer is exactly "fixes the row pattern". -/
theorem mem_rowStab {μ : YoungDiagram} {t : Tableau μ}
    {σ : Equiv.Perm (Fin (nOf μ))} : σ ∈ rowStab t ↔ σ • rowPattern t = rowPattern t :=
  Iff.rfl

/-- Membership in the column stabilizer is exactly "fixes the column pattern". -/
theorem mem_colStab {μ : YoungDiagram} {t : Tableau μ}
    {σ : Equiv.Perm (Fin (nOf μ))} : σ ∈ colStab t ↔ σ • colPattern t = colPattern t :=
  Iff.rfl

/-- Stabilizer membership is decidable (equality of two `Fin n → ℕ` patterns),
so `rowStab t` / `colStab t` carry a `Fintype` on their underlying subtype — which
is what makes the polytabloid sum below well-formed without `Set.toFinset` plumbing. -/
instance instDecidableMemRowStab {μ : YoungDiagram} (t : Tableau μ) :
    DecidablePred (· ∈ rowStab t) := fun _ =>
  decidable_of_iff _ mem_rowStab.symm

instance instDecidableMemColStab {μ : YoungDiagram} (t : Tableau μ) :
    DecidablePred (· ∈ colStab t) := fun _ =>
  decidable_of_iff _ mem_colStab.symm

/-! ## 3. Tabloids -/

/-- Two tableaux are **row-equivalent** when they have the same row pattern
(i.e. each label sits in the same row).  This is the setoid whose quotient is the
set of tabloids. -/
def rowEquiv (μ : YoungDiagram) : Setoid (Tableau μ) where
  r s t := rowPattern s = rowPattern t
  iseqv :=
    { refl := fun _ => rfl
      symm := fun h => h.symm
      trans := fun h₁ h₂ => h₁.trans h₂ }

@[simp] theorem rowEquiv_iff {μ : YoungDiagram} {s t : Tableau μ} :
    (rowEquiv μ).r s t ↔ rowPattern s = rowPattern t := Iff.rfl

/-- Row-equivalence is decidable (equality of two functions out of a `Fintype`
into `ℕ`), which makes the quotient `Tabloid` carry `DecidableEq`/`Fintype`. -/
instance instDecidableRowEquiv (μ : YoungDiagram) :
    DecidableRel (rowEquiv μ).r := fun s t =>
  decidable_of_iff (rowPattern s = rowPattern t) Iff.rfl

/-- A **tabloid** `{t}` of shape `μ` is a row-equivalence class of `μ`-tableaux:
the data of "which row each label lives in", forgetting the order within rows. -/
def Tabloid (μ : YoungDiagram) : Type := Quotient (rowEquiv μ)

namespace Tabloid

/-- The tabloid of a tableau (its row-equivalence class). -/
def mk {μ : YoungDiagram} (t : Tableau μ) : Tabloid μ := Quotient.mk (rowEquiv μ) t

instance instDecidableEq (μ : YoungDiagram) : DecidableEq (Tabloid μ) :=
  @Quotient.decidableEq _ (rowEquiv μ) (instDecidableRowEquiv μ)

instance instFintype (μ : YoungDiagram) : Fintype (Tabloid μ) :=
  @Quotient.fintype _ _ (rowEquiv μ) (instDecidableRowEquiv μ)

/-- The `S_n`-action descends to tabloids: `σ • {t} = {σ • t}`.  Well-defined
because the action is equivariant for the row pattern (`rowPattern_smul`). -/
instance instMulAction (μ : YoungDiagram) :
    MulAction (Equiv.Perm (Fin (nOf μ))) (Tabloid μ) where
  smul σ := Quotient.map (σ • ·) (by
    intro s t (h : rowPattern s = rowPattern t)
    show rowPattern (σ • s) = rowPattern (σ • t)
    simp [h])
  one_smul := by
    refine Quotient.ind (fun t => ?_)
    show Quotient.mk _ ((1 : Equiv.Perm (Fin (nOf μ))) • t) = Quotient.mk _ t
    rw [one_smul]
  mul_smul σ τ := by
    refine Quotient.ind (fun t => ?_)
    show Quotient.mk _ ((σ * τ) • t) = Quotient.mk _ (σ • (τ • t))
    rw [mul_smul]

@[simp] theorem smul_mk {μ : YoungDiagram} (σ : Equiv.Perm (Fin (nOf μ)))
    (t : Tableau μ) : σ • (Tabloid.mk t) = Tabloid.mk (σ • t) := rfl

end Tabloid

/-! ## 4. The permutation module `M^μ` -/

/-- The **permutation module** `M^μ` = the free `k`-module on tabloids of shape
`μ`.  The `S_n`-action permutes the basis of tabloids.

Marked `@[reducible]` so the `AddCommGroup`/`Module k` instances on
`Tabloid μ →₀ k` are transparently inherited. -/
@[reducible] def Mtab (μ : YoungDiagram) : Type := Tabloid μ →₀ k

namespace Mtab

/-- The basis tabloid vector `⟦t⟧ ∈ M^μ` (the `Finsupp.single` at the tabloid of
`t`, coefficient `1`). -/
noncomputable def of {μ : YoungDiagram} (t : Tableau μ) : Mtab (k := k) μ :=
  Finsupp.single (Tabloid.mk t) (1 : k)

/-- The `S_n`-representation on `M^μ`: each `σ` acts by the linear permutation of
basis tabloids `domLCongr (Tabloid.mulAction σ)`.  Implemented as a
`Representation k (Perm (Fin n)) (Mtab μ)` (i.e. a monoid hom into the linear
automorphisms), so it is wired for the `MonoidAlgebra k (Perm (Fin n))`-module
structure. -/
noncomputable def rep (μ : YoungDiagram) :
    Representation k (Equiv.Perm (Fin (nOf μ))) (Mtab (k := k) μ) where
  toFun σ := Finsupp.lmapDomain k k (fun d => σ • d)
  map_one' := by
    ext d t
    simp [Finsupp.lmapDomain_apply, one_smul]
  map_mul' σ τ := by
    ext d t
    simp [Finsupp.lmapDomain_apply, Finsupp.mapDomain_single, mul_smul]

@[simp] theorem rep_single {μ : YoungDiagram} (σ : Equiv.Perm (Fin (nOf μ)))
    (d : Tabloid μ) (c : k) :
    rep μ σ (Finsupp.single d c) = Finsupp.single (σ • d) c := by
  simp [rep, Finsupp.lmapDomain_apply, Finsupp.mapDomain_single]

@[simp] theorem rep_of {μ : YoungDiagram} (σ : Equiv.Perm (Fin (nOf μ)))
    (t : Tableau μ) : rep μ σ (of (k := k) t) = of (k := k) (σ • t) := by
  rw [of, rep_single, Tabloid.smul_mk, of]

end Mtab

/-! ## 5. Polytabloids and the Specht module -/

open Equiv (Perm)

/-- The **polytabloid** `e_t = Σ_{π ∈ C_t} sgn(π) · {π • t}` associated to a
tableau `t`: the signed sum over the column stabilizer of the tabloids of the
column-permuted tableaux.  This is the canonical spanning vector of the Specht
module. -/
noncomputable def polytabloid {μ : YoungDiagram} (t : Tableau μ) : Mtab (k := k) μ :=
  ∑ π : colStab t, (Equiv.Perm.sign (π : Equiv.Perm (Fin (nOf μ))) : ℤ) •
    Mtab.of (k := k) ((π : Equiv.Perm (Fin (nOf μ))) • t)

/-- The **Specht module** `S^μ ≤ M^μ`: the `k`-submodule spanned by all
polytabloids.  As a `Submodule.span` it is a submodule **by construction**
(`sorry`-free). -/
noncomputable def SpechtSubmodule (μ : YoungDiagram) : Submodule k (Mtab (k := k) μ) :=
  Submodule.span k (Set.range (polytabloid (k := k) (μ := μ)))

/-- Every polytabloid lies in the Specht module (immediate from the span). -/
theorem polytabloid_mem_specht {μ : YoungDiagram} (t : Tableau μ) :
    polytabloid (k := k) t ∈ SpechtSubmodule (k := k) μ :=
  Submodule.subset_span ⟨t, rfl⟩

/-! ## 6. The deep theorems (stated, `sorry` + `-- Ref:`) -/

/-- **Standard basis theorem.** The dimension of the Specht module `S^μ` equals
the number of standard Young tableaux of shape `μ`:
`dim_k S^μ = #SYT(μ) = f^μ`.  The standard polytabloids `{e_t : t ∈ SYT(μ)}` form
a `k`-basis. -/
theorem specht_finrank_eq_numSYT {k : Type} [Field k] (μ : YoungDiagram) :
    Module.finrank k (SpechtSubmodule (k := k) μ) = QOU.BraidKnot.numSYT μ := by
  -- Ref: [sagan2001] Thm 2.5.2 (the standard polytabloids form a basis of S^μ);
  -- brick-2 target.
  sorry

/-- **Irreducibility (char 0).** Over a field of characteristic zero, the Specht
module `S^μ` is a simple `MonoidAlgebra k (Perm (Fin n))`-module — the
irreducible representation of `S_n` indexed by `μ`.  We phrase simplicity as: the
only `S_n`-stable `k`-submodules of `S^μ` are `0` and `S^μ` (stated here at the
level of the representation `Mtab.rep` restricted to `S^μ`). -/
theorem specht_isSimple {k : Type} [Field k] [CharZero k] (μ : YoungDiagram)
    (hμ : μ.card ≠ 0) :  -- nonempty diagram; ℕ-nonemptiness, not ring ordering (§7c-clean)
    ∀ N : Submodule k (Mtab (k := k) μ),
      N ≤ SpechtSubmodule (k := k) μ →
      (∀ σ : Equiv.Perm (Fin (nOf μ)), ∀ x ∈ N, Mtab.rep μ σ x ∈ N) →
      N = ⊥ ∨ N = SpechtSubmodule (k := k) μ := by
  -- Ref: [james1984representation] (Specht modules are irreducible in char 0,
  -- via the standard-basis / Garnir / James submodule theorem); brick-2 target.
  sorry

end QOU.BraidKnot.Specht
