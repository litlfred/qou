/-!
# QOU.AlgebraicSubstrate.tannaka_krein_isomorphism

Tannaka–Krein duality: the category of localized representations
is equivalent to the category of comodules over the reconstructed
Hopf algebra.
LaTeX: `\label{thm:tannaka-krein-isomorphism}`
-/

import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.CategoryTheory.Equivalence
import Mathlib.CategoryTheory.Functor.Basic

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

universe u v

/-- The category of localized A-module representations (monopoles).
    Axiomatized as an opaque type; the full construction requires the
    localization theory from §2. -/
axiom RepLoc : Type (u + 1)

/-- The category of comodules over the reconstructed Hopf algebra H_ξ.
    Axiomatized as an opaque type; the reconstruction is via the
    fibre functor τ from Tannaka–Krein theory. -/
axiom ComodH : Type (u + 1)

/-- **Tannaka–Krein duality for the substrate.**

    The category of localized representations Rep_loc(A) is equivalent
    to the category of comodules Comod(H_ξ) over the Hopf algebra
    reconstructed from the Reeb spectrum via the fibre functor τ. -/
theorem tannaka_krein_isomorphism :
    Nonempty (RepLoc.{u} ≃ ComodH.{u}) := by
  -- Ref: [reshetikhin1991] https://doi.org/10.1007/BF01239527
  sorry

end QOU.AlgebraicSubstrate
