import QOU.Basic


/-!
# QOU.BraidKnot.CemeteryGroup — cemetery group as ker τ on KLR modules

Light axiomatization of the cemetery group of `H_n(R, q)`: the localising
Serre subcategory of graded projective Khovanov–Lauda–Rouquier modules
annihilated by the observation functor τ (graded Euler characteristic).

Used by the GS reduction engine as a homological "kill switch": branches
whose KLR lift lands in this subcategory map to zero under τ and are
pruned without further polynomial cancellation.

LaTeX: `\label{def:cemetery-group}`

References:
- Khovanov, M. & Lauda, A. D. (2009). A diagrammatic approach to
  categorification of quantum groups I. Representation Theory 13.
- Brundan, J. & Kleshchev, A. (2009). Blocks of cyclotomic Hecke algebras
  and Khovanov–Lauda algebras. Inventiones mathematicae 178(3).
-/

namespace QOU.BraidKnot

universe u

/-- **Cemetery group** of `H_n(R, q)`: the localising Serre subcategory
    of graded projective KLR modules annihilated by the observation
    functor τ.

    This is a light axiomatic wrapper — the KLR/Hecke equivalence used to
    realise the cemetery group concretely is the Brundan–Kleshchev
    isomorphism, which is not yet formalised in Mathlib. The structure
    records the data needed by downstream blocks (the strand count, the
    substrate parameter, and the predicate witnessing membership). -/
structure CemeteryGroup (R : Type u) [CommRing R] where
  /-- Number of braid strands `n` of the ambient `H_n(R, q)`. -/
  nStrands : ℕ
  /-- Substrate parameter. -/
  q : R
  /-- Predicate: a state index `i` lies in the cemetery group iff its
      KLR lift has vanishing graded Euler characteristic. -/
  inCemetery : ℕ → Prop

namespace CemeteryGroup

/-- The trivial state (zero index) is by convention not in the cemetery
    group: it is the unit of the algebra. -/
-- Ref: [manuscript] Ch. particle-interactions, def:cemetery-group (unit/zero-index state excluded from cemetery group)
axiom zero_not_in_cemetery {R : Type u} [CommRing R] (Z : CemeteryGroup R) :
    ¬ Z.inCemetery 0

end CemeteryGroup

end QOU.BraidKnot
