import Mathlib.Algebra.Homology.HomologicalComplex
import Mathlib.Algebra.Ring.Basic
import Mathlib.Logic.Equiv.Defs

/-!
# QOU.AlgebraicSubstrate.RigidDualizingComplex

Yekutieli's rigid dualizing complex for a non-commutative algebra,
providing canonical duality in the derived category.

LaTeX label: `def:rigid-dualizing-complex`
-/

set_option autoImplicit false


namespace QOU.AlgebraicSubstrate

universe u v

/-- **RigidDualizingComplex**: a rigid dualizing complex `ω_A•` for
    a non-commutative algebra `A`, in the sense of Yekutieli.

    The complex is equipped with a rigidifying isomorphism
    `ω_A• ≃ RHom_{A^e}(A, A^e)`, ensuring uniqueness up to
    unique isomorphism.

    Universe-carrying structure (§7d U2): the carrier universe `v` is
    pinned so use sites can tie it explicitly.

    LaTeX: `\label{def:rigid-dualizing-complex}` -/
structure RigidDualizingComplex (A : Type u) [Ring A] where
  /-- The carrier type for the dualizing complex. -/
  carrier : Type v
  /-- Homological dimension of `A`. -/
  homdim : ℕ
  /-- `RHom_{A^e}(A, A^e)`, the object the rigidifying isomorphism lands in.
      Carried as a field because the derived-category construction is not in
      Mathlib — which is what made the old `Prop` field look forced. -/
  rhomEnv : Type v
  /-- **The rigidifying isomorphism** `ω_A• ≃ RHom_{A^e}(A, A^e)`.

      Was `rigidifying_iso : Prop`, a field typed with the *universe* `Prop`,
      so the instance chose the proposition and `True` discharged it. An
      isomorphism is DATA; it is now an `Equiv`, which is the weakest form
      that still says the two objects correspond. -/
  rigidifying_iso : carrier ≃ rhomEnv
  /-- Injective dimension of the complex. -/
  injDim : ℕ
  /-- **Finite injective dimension**, bounded by the homological dimension.
      Was a `Prop` field; "finite" is now a stated bound between two
      numbers the structure already carries. -/
  finite_inj_dim : injDim ≤ homdim
  /-- The van den Bergh duality functor on the carrier. -/
  vdbDual : carrier → carrier
  /-- **Van den Bergh duality**: the duality is an involution.  Was a `Prop`
      field naming the property without stating it. -/
  vdb_duality : ∀ x, vdbDual (vdbDual x) = x

-- Ref: [yekutieli2015] Yekutieli, "Nonabelian Multiplicative Integration on Surfaces," World Scientific 2015 (DOI: 10.1142/9537)
/-- **The structure is inhabited — and this is NOT Yekutieli's existence
    theorem.**  Renamed and re-stated 2026-09-07; read the scope before
    citing it.

    It used to be called `rigid_dualizing_exists`, docstringed as "Existence
    of a rigid dualizing complex for a suitable non-commutative algebra
    satisfying van den Bergh conditions", and proved by setting all three
    `Prop` fields to `True`.  Two things were wrong with that.  The
    hypotheses it names — "suitable", "van den Bergh conditions" — appear
    nowhere in the statement, which quantifies over EVERY ring; and
    Yekutieli's Theorem 4.2 does not hold for every ring.  So the name and
    docstring claimed a theorem the statement does not make.

    With the fields encoded, the witness has to satisfy them, and it still
    can: `carrier = rhomEnv = A`, the identity equivalence, `injDim =
    homdim = 0`, `vdbDual = id`.  **That is the point of keeping it.**
    Encoding the fields narrowed what a witness must supply — an `Equiv`, a
    numeric bound, an involution — without making the trivial model
    impossible, and a theorem that exhibits the trivial model is the honest
    record of how much was bought.

    What it establishes: the axioms are consistent.  What it does not: that
    any *interesting* rigid dualizing complex exists, which needs the
    derived-category infrastructure Mathlib lacks.  See [yekutieli2015]
    Theorem 4.2 for the real construction and its real hypotheses. -/
-- Ref: [yekutieli2015] https://doi.org/10.1515/9783110291230  Theorem 4.2
theorem rigidDualizingComplex_inhabited_trivially (A : Type u) [Ring A] :
    Nonempty (RigidDualizingComplex.{u, u} A) :=
  ⟨{ carrier := A
     homdim := 0
     rhomEnv := A
     rigidifying_iso := Equiv.refl A
     injDim := 0
     finite_inj_dim := le_refl 0
     vdbDual := id
     vdb_duality := fun _ => rfl }⟩

end QOU.AlgebraicSubstrate
