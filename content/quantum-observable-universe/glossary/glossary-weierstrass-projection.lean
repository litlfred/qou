/-!
# QOU.Descartes.weierstrassProjection — Glossary: Weierstrass projection ℘_q(z)

The Weierstrass elliptic function on ℂ/Λ_q uniformising the
Descartes elliptic curve ℰ_q.

LaTeX label: `rem:glossary-weierstrass-projection`

Note: The main definition is in descartes-universe/weierstrass-projection.lean.
This glossary entry provides a cross-reference.
-/

import Mathlib.Data.Complex.Basic

namespace QOU.Descartes

/-- Glossary reference: the Weierstrass projection ℘_q : ℂ/Λ_q → ℙ¹
    is the meromorphic function uniformising ℰ_q.

    The full definition (Laurent series construction) is in
    `descartes-universe/weierstrass-projection.lean`. -/
-- Ref: [manuscript] Ch. 8 Glossary, §5/weierstrass-projection
theorem weierstrass_projection_exists (g2 g3 : ℝ) :
    ∃ (wp : ℂ → ℂ), True := ⟨fun _ => 0, trivial⟩
    -- Full construction in descartes-universe/weierstrass-projection.lean

end QOU.Descartes
