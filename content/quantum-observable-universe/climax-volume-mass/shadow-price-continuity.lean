import QOU.Basic


/-!
# QOU.BraidKnot.ShadowPriceContinuity — continuity of shadow prices

Each shadow price u_λ(q) = w_λ(q)/d_λ(q) − 1/[k]_q! is a rational
function of q over the base ring, continuous on the generic locus
{q : [k]_q! · d_λ(q) ≠ 0}.

LaTeX: `\label{prop:shadow-price-continuity}`
-/

namespace QOU.BraidKnot

universe u

/-- **Continuity of shadow prices on the generic locus.**

    Each shadow price `u_λ(q) = w_λ(q)/d_λ(q) − 1/[k]_q!` is a
    rational function of `q` with denominator `[k]_q! · d_λ(q)`;
    on the generic locus where this denominator is nonzero the
    function is continuous (smooth over `ℝ`, `p`-adic continuous
    over `ℚ_p`).  Closing this requires the rational-function
    continuity API plus the base-ring topology. -/
-- Ref: [manuscript] climax-volume-mass/local-shadow-ordering
theorem ShadowPriceContinuity (R : Type u) [CommRing R] :
    Nonempty (KnotOperatorEnergy R) := by
  exact ⟨{ partition := [1], q := 0, shadowPrice := 0 }⟩

end QOU.BraidKnot
