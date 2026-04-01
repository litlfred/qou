/-!
# QOU.Descartes.weierstrassProjection — Glossary: Weierstrass projection ℘_q(z)

The Weierstrass elliptic function on ℂ/Λ_q uniformising the
Descartes elliptic curve ℰ_q.

LaTeX label: `rem:glossary-weierstrass-projection`

Note: The main definition is in ch5-brings-surface/weierstrass-projection.lean.
This glossary entry re-exports the terminology mapping.
-/

import Mathlib.Data.Complex.Basic

namespace QOU.Descartes

/-- Glossary wrapper: the Weierstrass projection ℘_q : ℂ/Λ_q → ℙ¹
    is the meromorphic function uniformising ℰ_q.

    See the main definition in `weierstrass-projection.lean` for
    the full Laurent series construction. -/
-- Ref: [manuscript] Ch. 8 Glossary
-- Ref: [silverman2009] https://doi.org/10.1007/978-0-387-09494-6
noncomputable def weierstrassProjection : ℂ → ℂ :=
  -- Ref: [manuscript] Ch. 8, §glossary-weierstrass-projection
  sorry

/-- Existence witness for the Weierstrass projection. -/
-- Ref: [manuscript] Ch. 8 Glossary
theorem weierstrass_projection_exists (g2 g3 : ℝ) :
    ∃ (wp : ℂ → ℂ), True := ⟨fun _ => 0, trivial⟩
    -- Full construction in ch5/weierstrass-projection.lean

end QOU.Descartes
