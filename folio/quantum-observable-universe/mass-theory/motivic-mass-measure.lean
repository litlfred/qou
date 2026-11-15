-- Ref: [kontsevich1995] M. Kontsevich, Lecture at Orsay, Dec. 1995 (motivic integration).
-- Ref: [denef-loeser2001] J. Denef, F. Loeser, Geometry on Arc Spaces of Algebraic Varieties.
-- Motivic mass measure on the QOU brane arc space.
--
-- Canonical declaration lives in: lean/QOU/MotivesArchimedean.lean
-- This sibling is a documentation-mirror of the QOU library declaration.

import Mathlib.Tactic

namespace QOU.BraidsKnots

/-- Abstract Grothendieck ring of varieties K_0(Var_k).

    Carries the Lefschetz motive L = [A^1] and admits the
    localization M = K_0(Var)[L^{-1}] used by motivic integration. -/
structure GrothendieckRingOfVarieties where
  /-- Underlying ring. -/
  Ring : Type*
  /-- The Lefschetz motive L = [A^1] in the ring. -/
  lefschetz : Ring
  /-- Class map [·] : Var → Ring sending a variety to its motive. -/
  classOf : (X : Type*) → Ring

/-- The **motivic mass measure** μ on the arc space L(X).

    Measures cylindrical subsets of L(X) and returns a class in the
    dimension-completion M̂ of K_0(Var)[L^{-1}]. The total measure
    equals the sum ∑ [E_i°] L^{-d_i} over exceptional divisors of the
    Gröbner-Shirshov reduction (Kontsevich change-of-variables). -/
structure MotivicMassMeasure (X : Type*) where
  /-- Ambient Grothendieck ring (target of the measure). -/
  K0 : GrothendieckRingOfVarieties
  /-- The measure of the whole arc space (= total motivic mass). -/
  totalMass : K0.Ring
  /-- Number of exceptional divisors produced by the reduction. -/
  numDivisors : Nat
  /-- The class [E_i°] of the smooth open part of each exceptional divisor. -/
  divisorClass : Fin numDivisors → K0.Ring
  /-- Codimension/weight d_i of each exceptional divisor. -/
  divisorWeight : Fin numDivisors → Nat

end QOU.BraidsKnots
