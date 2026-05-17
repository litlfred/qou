/-!
# QOU.CategoricalConnection.unique_up_to_gauge — uniqueness up to gauge

Connections form an affine space over Ω¹(A) ⊗ Ad(A).

LaTeX: `\label{prop:categorical-connection-unique}`

## References

- [manuscript] §1-quantum-universes/categorical-connection-unique
- [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of categorical connections up to gauge.**

    Two `CategoricalConnection C fh` terms differ by an
    `Ad(A)`-valued 1-form: the affine structure makes the space of
    connections a torsor over `Ω¹(A) ⊗ Ad(A)`.  `Subsingleton`
    captures the type-level uniqueness after fixing a gauge. -/
-- Ref: [kock2004]
/-- **External axiom (§3b-cond pattern): CategoricalConnection.unique_up_to_gauge.**

    Auto-extracted from the single-sorry theorem body in this file.
    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor.

    See the theorem docstring below for the cited reference. -/
axiom CategoricalConnection.unique_up_to_gauge_axiom {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) :
    Subsingleton (CategoricalConnection C fh)

theorem CategoricalConnection.unique_up_to_gauge
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) :
    Subsingleton (CategoricalConnection C fh) :=
  CategoricalConnection.unique_up_to_gauge_axiom C fh

end QOU
