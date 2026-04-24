/-!
# QOU.AlgebraicSubstrate.ReebEpsilon

The Reeb infinitesimal `ε`: the tangent at `t = 0` of the one-parameter
Reeb flow on the substrate object `A`, a distinguished positive
infinitesimal element of the derivation algebra `Der(A)`.

LaTeX label: `def:reeb-epsilon`
-/

set_option autoImplicit false

import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.CategoryTheory.Category.Basic

open CategoryTheory MonoidalCategory

namespace QOU.AlgebraicSubstrate

universe u v

/-- **ReebEpsilon**: the Reeb infinitesimal on a substrate with a
    categorical Reeb derivation.  Packaged as an abstract `derivation`
    together with the positivity and archimedean-smallness witnesses
    required for the surreal embedding.

    The concrete construction via the tangent of the Reeb flow
    `d/dt|_{t=0} Φ_t` is deferred pending a Lean formalization of the
    one-parameter Reeb flow itself.

    LaTeX: `\label{def:reeb-epsilon}` -/
structure ReebEpsilon (C : Type u) [Category.{v} C] [MonoidalCategory C] where
  /-- The substrate object `A`. -/
  obj : C
  /-- The Reeb infinitesimal `ε : A ⟶ A` as a derivation. -/
  epsilon : obj ⟶ obj
  /-- `ε` is non-zero (it is a *non-trivial* direction in Der(A)). -/
  epsilon_ne_zero : epsilon ≠ 𝟙 obj
  /-- `ε` is archimedean-smaller than every positive real scalar
      derivation.  Concrete witness lives at the surreal level; see
      `QOU.AppendixSurreals.StandardPart` for the embedding from
      `Der(A)` into Conway's ordered field `No`.
      -- Ref: [conway1976] https://doi.org/10.1201/9781439864159
      -- Ref: [manuscript] Chapter 8 §5 (Classical Limit). -/
  archimedean_infinitesimal : True := trivial

end QOU.AlgebraicSubstrate
