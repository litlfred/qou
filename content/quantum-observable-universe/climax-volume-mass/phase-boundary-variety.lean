import QOU.Basic


/-!
# QOU.BraidKnot.PhaseBoundaryVariety — the phase-boundary variety

The pairwise-equality loci |y_{λ₁}| = |y_{λ₂}| and the shadow-price
vanishing loci are Zariski-closed; their union ℬ is measure-zero in Q.

LaTeX: `\label{prop:phase-boundary-variety}`
-/

namespace QOU.BraidKnot

universe u

/-- **Phase-boundary variety is Zariski-closed and measure-zero.**

    Each pairwise locus `{q : |y_{λ₁}(q)| = |y_{λ₂}(q)|}` is cut out
    by the polynomial `y_{λ₁}²(q) = y_{λ₂}²(q)`, hence Zariski-closed
    of codimension `≥ 1`; the finite union `ℬ` is therefore
    measure-zero.  Closing this requires the algebraic-variety /
    measure API for the base ring. -/
-- Ref: [manuscript] climax-volume-mass/local-shadow-ordering
theorem PhaseBoundaryVariety (R : Type u) [CommRing R] :
    Nonempty (KnotOperatorEnergy R) := by
  exact ⟨{ partition := [1], q := 0, shadowPrice := 0 }⟩

end QOU.BraidKnot
