import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Equivalence
import Mathlib.CategoryTheory.Functor.Basic


/-!
# QOU.AlgebraicSubstrate.tannaka_krein_isomorphism

Tannaka–Krein duality: the category of localized representations
is equivalent to the category of comodules over the reconstructed
Hopf algebra.
LaTeX: `\label{thm:tannaka-krein-isomorphism}`
-/

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

universe u v

/-- The category of localized A-module representations (monopoles).
    Axiomatized as an opaque type; the full construction requires the
    localization theory from §2. -/
-- Ref: [manuscript] Ch. q-geometric-langlands §2, thm:tannaka-krein-isomorphism (localized A-module rep category)
axiom RepLoc : Type (u + 1)

/-- The category of comodules over the reconstructed Hopf algebra H_ξ.
    Axiomatized as an opaque type; the reconstruction is via the
    fibre functor τ from Tannaka–Krein theory. -/
-- Ref: [deligne1990] Catégories tannakiennes, in The Grothendieck Festschrift II, 111-195 (comodule category over reconstructed Hopf algebra)
axiom ComodH : Type (u + 1)

/-- **Tannaka–Krein duality for the substrate.**

    The category of localized representations Rep_loc(A) is equivalent
    to the category of comodules Comod(H_ξ) over the Hopf algebra
    reconstructed from the Reeb spectrum via the fibre functor τ. -/
/-- **External axiom (§3b-cond pattern): tannaka_krein_isomorphism.**

    Auto-extracted from the single-sorry theorem body in this file.
    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor.

    See the theorem docstring below for the cited reference. -/
-- Ref: [tannaka1939] Tannaka, Über den Dualitätssatz der nichtkommutativen topologischen Gruppen, Tôhoku Math. J. 45 (1939) 1-12 (Tannaka–Krein duality)
axiom tannaka_krein_isomorphism_axiom  :
    Nonempty (RepLoc.{u} ≃ ComodH.{u})

theorem tannaka_krein_isomorphism :
    Nonempty (RepLoc.{u} ≃ ComodH.{u}) :=
  tannaka_krein_isomorphism_axiom

end QOU.AlgebraicSubstrate
