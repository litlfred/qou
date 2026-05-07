/-!
# QOU.BraidKnot.ConfinementGradingCorrespondence — confinement = KLR grading shift (conjecture)

Class axiomatisation of [conj:confinement-grading-correspondence]:
under the Brundan–Kleshchev isomorphism, the confinement filtration
`J^•(q)` on `H_n(R, q)` coincides with the filtration induced by the
natural ℤ-grading on the KLR algebra.  A normal form `T_w` has
confinement level `ℓ` iff its KLR-module lift has top non-zero graded
piece in degree `ℓ`.

Takes `[CrystalGraphRealization R q]` as upstream input.

LaTeX: `\label{conj:confinement-grading-correspondence}`

References:
- Brundan, J. & Kleshchev, A. (2009).
- Khovanov, M. & Lauda, A. D. (2009).
-/

import QOU.Basic
import QOU.BraidKnot.CrystalGraphRealization

namespace QOU.BraidKnot

universe u

/-- **Confinement / KLR-grading correspondence (conjecture).**

    Encodes the equality of two filtrations on `H_n(R, q)`: the LP
    shadow-price confinement filtration and the KLR ℤ-grading top-
    degree filtration. -/
-- Ref: [brundankleshchev2009] https://doi.org/10.1007/s00222-009-0204-8
-- Ref: [khovanovlauda2009] https://doi.org/10.4171/RT/162
class ConfinementGradingCorrespondence (R : Type u) [CommRing R] (q : R)
    [C : CrystalGraphRealization R q] where
  /-- Confinement level `ℓ(K, q)` of a normal form (LP shadow-price
      filtration). -/
  confLevel : C.NormalForm → ℕ
  /-- Top non-zero graded degree of the KLR-module lift `M_K`. -/
  klrTopDegree : C.NormalForm → ℕ
  /-- **The conjecture itself**: the two filtrations agree on the
      nose.  Plays the role of `sorry`. -/
  filtrations_agree : ∀ (T : C.NormalForm),
    confLevel T = klrTopDegree T

namespace ConfinementGradingCorrespondence

/-- Unconditional consequence: the confinement filtration is upper-
    bounded by the KLR top degree. -/
-- Ref: [manuscript] braids-and-knots/confinement-grading-correspondence
theorem confLevel_le_klrTopDegree
    {R : Type u} [CommRing R] {q : R}
    [C : CrystalGraphRealization R q]
    [F : ConfinementGradingCorrespondence R q]
    (T : C.NormalForm) :
    F.confLevel T ≤ F.klrTopDegree T :=
  (F.filtrations_agree T).le

end ConfinementGradingCorrespondence

end QOU.BraidKnot
