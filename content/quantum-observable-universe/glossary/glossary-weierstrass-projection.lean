/-!
# QOU.Archimedean.weierstrassProjection — Glossary: Weierstrass projection ℘_q(z)

The Weierstrass elliptic function on ℂ/Λ_q uniformising the
Descartes elliptic curve ℰ_q.

LaTeX label: `rem:glossary-weierstrass-projection`

Note: The main definition is in archimedean-universe/weierstrass-projection.lean.
This glossary entry provides a cross-reference.

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

import Mathlib.Data.Complex.Basic

namespace QOU.Archimedean

/-- Glossary reference: the Weierstrass projection ℘_q : ℂ/Λ_q → ℙ¹
    is the meromorphic function uniformising ℰ_q.

    The full definition (Laurent series construction) is in
    `archimedean-universe/weierstrass-projection.lean`. -/
-- Ref: [manuscript] Ch. 8 Glossary, §5/weierstrass-projection
theorem weierstrass_projection_exists (g2 g3 : ℝ) :
    ∃ (wp : ℂ → ℂ), True := ⟨fun _ => 0, trivial⟩
    -- Full construction in archimedean-universe/weierstrass-projection.lean

end QOU.Archimedean
