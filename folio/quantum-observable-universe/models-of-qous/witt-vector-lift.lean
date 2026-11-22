import QOU.FormalGroups.FormalGroupLaw

/-!
# QOU.WittVectorLift

Content sibling for `def:witt-vector-lift`. A lift of a formal group law `H` over `S` along a
ring map `φ : R →+* S` is a formal group law `G` over `R` whose reduction along `φ` is `H`
(`QOU.FormalGroups.FormalGroupLaw.IsLift`). The Witt vector lift is the case
`φ : W(k) → k`, the reduction of the Witt vectors of a perfect field `k` of characteristic
`p` to `k`. Mathlib's Witt vectors are not in the olean cone used here, so the declaration is
stated for a general `φ`.

Nothing is asserted about existence. Until 2026-11-21 this file defined `WittVectorLift` as a
structure of natural numbers (prime, height, Lie dimension) and proved arithmetic facts about
them (`p ≠ 0`, `2 * 4 = 8`, `p < p²`) under Witt-vector names, and its docstring said the lift
is "obtained by integrating π_< in the sense of Fresse". The integration theorem it was
attributed to (arXiv:math/0602138, Thm. 3.7) is over a field of characteristic `p` and
constructs no lift.

-- Ref: [hazewinkel1978] M. Hazewinkel, *Formal Groups and Applications*, 1978.
-/

namespace QOU

open QOU.FormalGroups

/-- A lift of the formal group law `H` over `S` along `φ : R →+* S`. With `φ : W(k) → k` this
is a Witt vector lift. -/
abbrev WittVectorLift {R S : Type*} [CommRing R] [CommRing S] (φ : R →+* S) {ι : Type*}
    [Finite ι] (H : FormalGroupLaw S ι) : Type _ :=
  {G : FormalGroupLaw R ι // G.IsLift φ H}

/-- A commutative lift has a commutative reduction. -/
theorem WittVectorLift.isComm_of_isComm {R S : Type*} [CommRing R] [CommRing S] {φ : R →+* S}
    {ι : Type*} [Finite ι] {H : FormalGroupLaw S ι} (G : WittVectorLift φ H)
    (hG : G.1.IsComm) : H.IsComm :=
  G.2.isComm hG

end QOU
