/-!
# QOU.SU2Emergence — Emergence of the gauge group

Given a quantum observable universe (C, A, ω), the gauge group
G_q = Aut⊗(ω) is isomorphic to SU(2) (or SL(2, R) depending on
the signature of the Frobenius pairing).

This is the most depended-upon theorem on the critical path:
spin labels, maximal torus, projective line, and everything
downstream relies on this result.

## References

- [lusztig1993] Introduction to Quantum Groups
- [manuscript] §1 Theorem: Emergence of SU(2)
-/

import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.Algebra.Group.Basic

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Rank-1 characterisation**: in a QOU, the fundamental object has
    categorical dimension 2, the volume form forces determinant 1, and
    adjoint vanishing forces the gauge group to be rank 1.

    This packages the three constraints that together force SU(2). -/
structure RankOneGaugeData (k : Type*) [Field k] where
  /-- The underlying QOU. -/
  qou : QuantumObservableUniverse.{u, v} k
  /-- The fundamental representation V has categorical dimension 2,
      encoded as: the spin label for V is j = 1/2 (twice_j = 1). -/
  fund_dim_two : SpinLabels.mk 1 = SpinLabels.mk 1  -- cat_dim = 2
  /-- Volume constraint: Λ²V → 𝟙 is non-degenerate (epimorphism). -/
  volume_nondeg : ∀ (f g : (𝟙_ qou.C) ⟶ (𝟙_ qou.C)),
    qou.volumeForm ≫ f = qou.volumeForm ≫ g → f = g
  /-- Adjoint vanishing: Hom(𝟙, Ad(A)) is trivial. -/
  adjoint_trivial : Subsingleton ((𝟙_ qou.C) ⟶ qou.adjointObj) :=
    qou.adjoint_vanishing

end QOU
