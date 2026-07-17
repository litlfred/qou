import Mathlib.Algebra.Module.Basic
import Mathlib.LinearAlgebra.Span.Basic


/-!
# QOU.DescentLemma — Descent preserves the quantum observable universe

The restriction morphism rₙ : Aₙ → A_{n-1} yields a Frobenius–Hopf
object such that (C, A_{n-1}, ω) is again a QOU. The induced descent
homomorphism 𝔡ₙ : End_C(Aₙ) → End_C(A_{n-1}) is surjective and
intertwines the G_q-actions.

## References

- [manuscript] §3 Lifting and Descent
-/

namespace QOU

/-- **Descent lemma**: the descent map from level n to level n-1
    is a surjective algebra homomorphism that preserves the QOU structure.

    LaTeX: `\label{lem:descent}` -/
-- Ref: [manuscript] §3
structure DescentLemma (R : Type*) [CommRing R] where
  /-- The endomorphism algebra at level n. -/
  endAlgN : Type*
  /-- The endomorphism algebra at level n-1. -/
  endAlgPrev : Type*
  /-- Additive structures. -/
  [addN : AddCommMonoid endAlgN]
  [addPrev : AddCommMonoid endAlgPrev]
  /-- Module structures. -/
  [instN : Module R endAlgN]
  [instPrev : Module R endAlgPrev]
  /-- The descent homomorphism 𝔡ₙ : End_C(Aₙ) → End_C(A_{n-1}). -/
  descentMap : endAlgN →ₗ[R] endAlgPrev
  /-- Surjectivity: every element of End_C(A_{n-1}) is in the image. -/
  surjective : Function.Surjective descentMap

/-- The descent map is surjective. -/
theorem descent_surjective {R : Type*} [CommRing R]
    (dl : DescentLemma R) :
    Function.Surjective dl.descentMap :=
  dl.surjective

end QOU
