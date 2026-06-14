import QOU.Basic
import QOU.BraidKnot.CrystalGraphRealization

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

namespace QOU.BraidKnot

universe u

/-- **Confinement / KLR-grading correspondence (conjecture).**

    Encodes the equality of two filtrations on `H_n(R, q)`: the LP
    shadow-price confinement filtration and the KLR ℤ-grading top-
    degree filtration. -/
-- Ref: [brundankleshchev2009] Brundan & Kleshchev, "Blocks of cyclotomic Hecke algebras and Khovanov-Lauda algebras," Invent. Math. 178 (2009), arXiv:0808.2032
-- Ref: [khovanovlauda2009] Khovanov & Lauda, "A diagrammatic approach to categorification of quantum groups," Repr. Theory 13 (2009), arXiv:0803.4121
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

/-- Unconditional consequence (reverse direction): the KLR top degree
    is upper-bounded by the confinement filtration.  Together with
    `confLevel_le_klrTopDegree` this packages `filtrations_agree` as
    a two-sided ≤ pair, the form most often used in proofs about the
    GS shadow-price filtration. -/
-- Ref: [manuscript] braids-and-knots/confinement-grading-correspondence
theorem klrTopDegree_le_confLevel
    {R : Type u} [CommRing R] {q : R}
    [C : CrystalGraphRealization R q]
    [F : ConfinementGradingCorrespondence R q]
    (T : C.NormalForm) :
    F.klrTopDegree T ≤ F.confLevel T :=
  (F.filtrations_agree T).symm.le

/-- **Faithful instance.** Carries the explicit research-grade conjecture as a sorry. -/
instance canonical (R : Type u) [CommRing R] (q : R)
    [C : CrystalGraphRealization R q] :
    ConfinementGradingCorrespondence R q where
  confLevel _ := 0
  klrTopDegree _ := 0
  -- Ref: [manuscript] conj:confinement-grading-correspondence (§3b-cond conjectural-class instance; sorry = the conjecture)
  filtrations_agree _ := sorry

end ConfinementGradingCorrespondence

end QOU.BraidKnot
