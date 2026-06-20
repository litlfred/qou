/-!
# QOU.AlgebraicSubstrate.ReebEpsilon — The Reeb infinitesimal `ε`

The Reeb infinitesimal `ε` is the tangent at `t = 0` of the
one-parameter Reeb flow `Φ_t : A → A` on the substrate object `A`.
It is the *categorical* origin of the substrate parameter, preceding
any choice of scalar `q`: the paper's `q = 1 + ε` is derived from
`ε`, not vice versa.

Two properties pick out `ε` as a positive infinitesimal:
- **Positivity**: `⟨v, ε·v⟩ > 0` for every non-zero state `v` under
  the Frobenius pairing.
- **Archimedean smallness**: for every standard real `λ > 0` and
  every `n ∈ ℕ`, `n · ε < λ` in the operator order on `End(A)`.

These properties match Conway's definition of a positive infinitesimal
in `𝐍𝐨`, under the embedding `ε ↦ 1/ω` developed in
`QOU.AppendixSurreals.StandardPart`.

LaTeX label: `def:reeb-epsilon`

## References

- [conway1976] Conway, *On Numbers and Games*, Academic Press.
- [manuscript] Chapter 8 §5 (Classical Limit and Macroscopic Continuum).
-/

set_option autoImplicit false

import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic

open CategoryTheory MonoidalCategory

namespace QOU.AlgebraicSubstrate

universe u v

/-- **ReebEpsilon**: the Reeb infinitesimal on a substrate with a
    categorical Reeb derivation.

    Encoded as a bundled structure rather than a field, because the
    concrete construction via `d/dt|_{t=0} Φ_t` requires the
    one-parameter Reeb flow, which is not yet formalised at the
    categorical level.  We record the abstract properties
    (non-triviality + archimedean-infinitesimal) as typeclass data
    that downstream modules may assume.

    LaTeX: `\label{def:reeb-epsilon}` -/
-- Ref: [conway1976] On Numbers and Games
-- Ref: [manuscript] Chapter 8 §5 (Classical Limit)
structure ReebEpsilon (C : Type u) [Category.{v} C] [MonoidalCategory C]
    where
  /-- The substrate object `A`. -/
  obj : C
  /-- The Reeb infinitesimal `ε : A ⟶ A` as an endomorphism. -/
  epsilon : obj ⟶ obj
  /-- `ε` is non-trivial: distinct from the identity. -/
  epsilon_ne_id : epsilon ≠ 𝟙 obj

/-- The archimedean-infinitesimal property of `ε`: for every
    positive standard-real scalar `λ > 0` and every `n : ℕ`, the
    iterate `n · ε` is dominated by `λ · id`.

    Stated abstractly as a class rather than a field, because the
    operator order on `End(A)` requires the Frobenius pairing, which
    lives at a different layer.  Downstream modules that construct a
    specific `ReebEpsilon` instance will (conjecturally) provide an
    `ArchimedeanInfinitesimal` instance.

    The connection to the surreal `1/ω` is made in
    `QOU.AppendixSurreals.StandardPart`.

    Encoded as an empty marker `Prop` class per AGENTS.md §3b: the
    archimedean-smallness statement `n · ε < λ · 𝟙` requires the
    Frobenius-pairing operator order on `End(A)`, which lives at a
    different layer of the formalisation.  Downstream theorems
    that assume this class hypothesis prove conditional results
    whose only unproved input is the (eventual) archimedean
    witness.  An instance is the conjecture. -/
-- Ref: [conway1976] On Numbers and Games §0 (Archimedean property)
class ArchimedeanInfinitesimal
    {C : Type u} [Category.{v} C] [MonoidalCategory C]
    (R : ReebEpsilon C) : Prop

end QOU.AlgebraicSubstrate
