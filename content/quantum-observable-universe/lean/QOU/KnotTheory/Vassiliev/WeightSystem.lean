import QOU.KnotTheory.Vassiliev.FourTermRelation
import Mathlib.LinearAlgebra.Quotient.Basic
import Mathlib.Tactic

/-!
# Weight systems

The **reduced chord-diagram space** `𝒜 R n` is the free module on chord
diagrams modulo the one- and four-term relations (`FourTermRelation.lean`):

`𝒜 R n := CDModule R n ⧸ relationsSubmodule R`.

A **weight system of degree `n`** is an `R`-linear functional on `𝒜 R n`,
equivalently a functional on `CDModule R n` that vanishes on both the 1T and 4T
relators.  Weight systems are the targets of the *symbol* map of a finite-type
invariant (`FiniteTypeInvariant.lean`); the fundamental theorem that the symbol
of a finite-type invariant *is* a weight system, and Kontsevich's converse, are
stated as honest conjecture classes there / in `MilnorVassilievBridge.lean`.

All results here hold for an **arbitrary** relations submodule, so they are
independent of the exact 4T encoding (module docstring of
`FourTermRelation.lean`).

## References

* Bar-Natan, *On the Vassiliev knot invariants*, Topology 34 (1995) 423–472.
-/

namespace QOU.KnotTheory.Vassiliev

open scoped Classical

variable {R : Type*} [CommRing R] {n : ℕ}

/-- The reduced chord-diagram space of degree `n`: the free module on chord
diagrams modulo the one- and four-term relations. -/
abbrev AReduced (R : Type*) [CommRing R] (n : ℕ) :=
  CDModule R n ⧸ relationsSubmodule R

/-- The canonical projection from the free chord-diagram module onto the
reduced space `𝒜`. -/
noncomputable def AReduced.proj : CDModule R n →ₗ[R] AReduced R n :=
  (relationsSubmodule R).mkQ

/-- The class of a chord diagram in the reduced space. -/
noncomputable def AReduced.mk (D : ChordDiagram n) : AReduced R n :=
  AReduced.proj (CDModule.of D)

/-- A **weight system** of degree `n`: an `R`-linear functional on the reduced
chord-diagram space. -/
abbrev WeightSystem (R : Type*) [CommRing R] (n : ℕ) := AReduced R n →ₗ[R] R

namespace WeightSystem

/-- Framing independence: a weight system vanishes on any diagram carrying an
isolated (adjacent-endpoint) chord. -/
theorem apply_isolated_eq_zero (w : WeightSystem R n) {D : ChordDiagram n}
    (h : HasAdjacentChord D) : w (AReduced.mk D) = 0 := by
  have hmem : CDModule.of D ∈ relationsSubmodule (R := R) (n := n) :=
    of_mem_relations_of_hasAdjacentChord (R := R) h
  have : AReduced.mk (R := R) D = 0 := by
    unfold AReduced.mk AReduced.proj
    rw [Submodule.mkQ_apply, Submodule.Quotient.mk_eq_zero]
    exact hmem
  rw [this, map_zero]

/-- The four-term relation: a weight system annihilates every four-term
relator. -/
theorem apply_fourTerm_eq_zero (w : WeightSystem R n) (D : ChordDiagram n)
    (i j : Fin (2 * n)) :
    w (AReduced.proj (fourTermRelator R D i j)) = 0 := by
  have hmem : fourTermRelator R D i j ∈ relationsSubmodule (R := R) (n := n) :=
    fourTermRelator_mem_relations (R := R) D i j
  have : AReduced.proj (R := R) (fourTermRelator R D i j) = 0 := by
    unfold AReduced.proj
    rw [Submodule.mkQ_apply, Submodule.Quotient.mk_eq_zero]
    exact hmem
  rw [this, map_zero]

/-! ## Weight systems as functionals on the free module

Precomposing a weight system with the projection gives a functional on the
free chord-diagram module that vanishes on the relations; conversely any such
functional descends to a weight system.  This is the "vanishes on 1T and 4T"
characterization. -/

/-- The pullback of a weight system to a functional on the free module. -/
noncomputable def pullback (w : WeightSystem R n) : CDModule R n →ₗ[R] R :=
  w.comp AReduced.proj

/-- The pullback of a weight system vanishes on the relations submodule. -/
theorem pullback_vanishes (w : WeightSystem R n) :
    relationsSubmodule (R := R) (n := n) ≤ LinearMap.ker (pullback w) := by
  intro x hx
  simp only [LinearMap.mem_ker, pullback, LinearMap.comp_apply]
  have : AReduced.proj (R := R) x = 0 := by
    unfold AReduced.proj
    rw [Submodule.mkQ_apply, Submodule.Quotient.mk_eq_zero]
    exact hx
  rw [this, map_zero]

/-- Any functional on the free module that vanishes on the relations descends
to a weight system. -/
noncomputable def descend (f : CDModule R n →ₗ[R] R)
    (hf : relationsSubmodule (R := R) (n := n) ≤ LinearMap.ker f) :
    WeightSystem R n :=
  (relationsSubmodule R).liftQ f hf

/-- Descending a functional and then evaluating on a class recovers the
functional (the descent is a genuine factorization through the quotient). -/
@[simp] theorem descend_mk (f : CDModule R n →ₗ[R] R)
    (hf : relationsSubmodule (R := R) (n := n) ≤ LinearMap.ker f)
    (x : CDModule R n) :
    descend f hf (AReduced.proj x) = f x := by
  unfold descend AReduced.proj
  rw [Submodule.mkQ_apply, Submodule.liftQ_apply]

end WeightSystem

end QOU.KnotTheory.Vassiliev
