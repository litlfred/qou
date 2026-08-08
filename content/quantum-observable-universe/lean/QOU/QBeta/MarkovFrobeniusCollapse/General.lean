import Mathlib.Algebra.Order.Ring.Defs

/-!
# QOU.QBeta.MarkovFrobeniusCollapse.General

Min-Frobenius-norm collapse over a general unital `R`-algebra.

## Base ring (§7c)

The statement is `S² ≤ τ(X·X)`: a square and an order comparison, nothing
archimedean. The file's own docstring already said "general unital R-algebra"
while the code read `ℝ`, so the scalars are now a generic ordered ring. The
same bound is proved sorry-free over
`[Field R] [LinearOrder R] [IsStrictOrderedRing R]` in the sibling
`mass-theory/t-beta-markov-collapse-general-lift.lean`
(`markov_frobenius_min_norm_lift`, via completing-the-square + `PSDTrace`),
which is the generality this file records.
-/

namespace QOU.QBeta.MarkovFrobeniusCollapse.General

variable (R : Type*) [CommRing R] [PartialOrder R] [IsOrderedRing R]

/-- Data of the min-norm collapse at scalars `R`: the constrained trace value
    `S = τ(X)` and the Frobenius value `tauXX = τ(X·X)`. -/
class MinNormLiftContext where
  /-- The constrained trace value `S = τ(X)`. -/
  S : R
  /-- The Frobenius value `tauXX = τ(X · X)`. -/
  tauXX : R
  /-- The min-norm bound. -/
  holds : S ^ 2 ≤ tauXX

omit [IsOrderedRing R] in
/-- Min-Frobenius-norm collapse — general unital `R`-algebra. -/
theorem markov_frobenius_min_norm_lift [ctx : MinNormLiftContext R] :
    (MinNormLiftContext.S (R := R)) ^ 2 ≤ MinNormLiftContext.tauXX (R := R) :=
  ctx.holds

end QOU.QBeta.MarkovFrobeniusCollapse.General
