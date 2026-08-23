---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-055-42-nondegenerate-bilinear-forms-73
section_title: "Nondegenerate bilinear forms 73"
section_number: 4.2
pages: 81-82
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
4.2. Nondegenerate bilinear forms
In the introduction to this chapter we have remarked that conjecture 4.1
essentially says that for a smooth theta divisor the associated Tannaka group
is as large as possible. To justify this interpretation, letX be a complex ppav
of dimensiong≥ 2 andΘ⊂ X a symmetric theta divisor. For simplicity we
assume that the ppavX is indecomposable, in which caseΘ is irreducible
and hence in particular normal by [36].
ThenδΘ is a simple perverse sheaf, and by symmetry of the theta divisor
it is isomorphic to its adjoint dual(δΘ)∨ = (−id)∗D(δΘ). On the Tannakian
side, if we denote by
ω : ⟨δΘ⟩ ∼−→RepC(G(δΘ))
the tensor functor in corollary 3.10, then it follows thatV = ω(δΘ) is an
irreducible self-dual representation ofG(δΘ). Any representation with these
properties is either orthogonal or symplectic, depending on whether the unit
object1 = δ0 of our Tannakian category lies in the alternating squareΛ2(V)
or in the symmetric squareS2(V). To decide which of the two possibilities
occurs, consider the commutativity constraint
S = SδΘ,δΘ : δΘ∗δΘ
∼−→ δΘ∗δΘ
as deﬁned in section 2.1. We claim that this constraintS acts by (−1)g−1
on the stalk cohomology groupH 0(δΘ∗ δΘ)0 at the origin. Indeed we
have δΘ = ICΘ[g−1], so our claim amounts to the statement thatS acts
trivially on the stalk cohomology groupH 2g−2(ICΘ∗ICΘ)0. For this latter
statement one can use that since by assumption the theta divisor is normal,
we have a natural identiﬁcation
H 2g−2(ICΘ∗ICΘ)0∼= H 2g−2(CΘ∗CΘ)0
which allows to replace the intersection cohomology sheaf with the constant
sheaf. Then our claim easily follows via base change.
For the representationV = ω(δΘ) it follows from the above that the
unit object1 lies in the alternating squareΛ2(V) if g is even, resp. in the
symmetric squareS2(V) if g is odd. This implies
LEMMA 4.6. If the theta divisorΘ⊂ X is smooth, then there exists an
embedding
G(δΘ) ↪→ G(g) =
{
Spg!(C) for even g
SOg!(C) for odd g
such thatω(δΘ) is the restriction of the standard representation of G(g).
74 Chapter 4 – The Tannaka group of the theta divisor
Proof. SinceΘ is smooth, the irreducible representationV = ω(δΘ) is
of dimension dimC(V) =χ(δΘ) =g! by the Gauss-Bonnet formula, and we
have noted above thatV is a symplectic resp. orthogonal representation ifg
is even resp. odd. This proves the lemma with the full orthogonal group in
place of the special orthogonal group. It remains to show that det(V) is the
trivial character ofG(δΘ). If not, the character det(V) would by part(b) of
proposition 1.6 correspond to a skyscraper sheafδx supported in a 2-torsion
pointx∈X(C)\{0}. For monodromy reasons it is impossible to select such
a 2-torsion point naturally on every ppav on an Zariski-open dense subset
of the moduli spaceAg. So we can ﬁnish the proof by a specialization
argument, using that the Tannaka group deﬁnes a constructible stratiﬁcation
of the moduli space (see the remarks preceding proposition 4.12 below) and
that by theorem 3.15 it only becomes smaller on closed subsets. □
