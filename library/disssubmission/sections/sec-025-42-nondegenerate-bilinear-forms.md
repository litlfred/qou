---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-025-42-nondegenerate-bilinear-forms
section_title: "Nondegenerate bilinear forms"
section_number: 4.2
pages: 81-82
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
73
4.2. Nondegenerate bilinear forms
In the introduction to this chapter we have remarked that conjecture 4.1
essentially says that for a smooth theta divisor the associated Tannaka group
is as large as possible. To justify this interpretation, let X be a complex ppav
of dimension g ≥2 and Θ ⊂X a symmetric theta divisor. For simplicity we
assume that the ppav X is indecomposable, in which case Θ is irreducible
and hence in particular normal by [36].
Then δΘ is a simple perverse sheaf, and by symmetry of the theta divisor
it is isomorphic to its adjoint dual (δΘ)∨= (−id)∗D(δΘ). On the Tannakian
side, if we denote by
ω :
⟨δΘ⟩
∼
−→RepC(G(δΘ))
the tensor functor in corollary 3.10, then it follows that V = ω(δΘ) is an
irreducible self-dual representation of G(δΘ). Any representation with these
properties is either orthogonal or symplectic, depending on whether the unit
object 1 = δ0 of our Tannakian category lies in the alternating square Λ2(V)
or in the symmetric square S2(V). To decide which of the two possibilities
occurs, consider the commutativity constraint
S = SδΘ,δΘ :
δΘ ∗δΘ
∼
−→δΘ ∗δΘ
as deﬁned in section 2.1. We claim that this constraint S acts by (−1)g−1
on the stalk cohomology group H 0(δΘ ∗δΘ)0 at the origin. Indeed we
have δΘ = ICΘ[g −1], so our claim amounts to the statement that S acts
trivially on the stalk cohomology group H 2g−2(ICΘ ∗ICΘ)0. For this latter
statement one can use that since by assumption the theta divisor is normal,
we have a natural identiﬁcation
H 2g−2(ICΘ ∗ICΘ)0 ∼= H 2g−2(CΘ ∗CΘ)0
which allows to replace the intersection cohomology sheaf with the constant
sheaf. Then our claim easily follows via base change.
For the representation V = ω(δΘ) it follows from the above that the
unit object 1 lies in the alternating square Λ2(V) if g is even, resp. in the
symmetric square S2(V) if g is odd. This implies
LEMMA 4.6. If the theta divisor Θ ⊂X is smooth, then there exists an
embedding
G(δΘ) ,→G(g) =
(
Spg!(C)
for even g
SOg!(C)
for odd g
such that ω(δΘ) is the restriction of the standard representation of G(g).
74
Chapter 4 – The Tannaka group of the theta divisor
Proof. Since Θ is smooth, the irreducible representation V = ω(δΘ) is
of dimension dimC(V) = χ(δΘ) = g! by the Gauss-Bonnet formula, and we
have noted above that V is a symplectic resp. orthogonal representation if g
is even resp. odd. This proves the lemma with the full orthogonal group in
place of the special orthogonal group. It remains to show that det(V) is the
trivial character of G(δΘ). If not, the character det(V) would by part (b) of
proposition 1.6 correspond to a skyscraper sheaf δx supported in a 2-torsion
point x ∈X(C)\{0}. For monodromy reasons it is impossible to select such
a 2-torsion point naturally on every ppav on an Zariski-open dense subset
of the moduli space Ag. So we can ﬁnish the proof by a specialization
argument, using that the Tannaka group deﬁnes a constructible stratiﬁcation
of the moduli space (see the remarks preceding proposition 4.12 below) and
that by theorem 3.15 it only becomes smaller on closed subsets.
□
