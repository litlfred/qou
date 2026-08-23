---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-017-54-twisted-invariants-and-slice-links
section_title: "Twisted invariants and slice links"
section_number: 5.4
pages: 17-18
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexand er polynomials of a 3–manifold associated to a representation of its fundam ental group."
---
that if L is a slice link with more than one component, then the ordinar y Alexander module
is necessarily non–torsion, in particular the correspondi ng Reidemeister torsion is zero. We
will follow an idea of Turaev [Tu86, Section 5.1] to deﬁne a (t wisted) invariant for links
even if the (twisted) Alexander module is non–torsion. This invariant will then give rise to
a sliceness obstruction for links. We refer throughout this section to [CF10] and [Tu86] for
details.
Let L ⊂ S3 be an oriented m–component link. Let R ⊂ C be a subring and let α :
π(S3 \νL) → GL(k,R ) be a unitary representation. Suppose that ψ :π1(S3 \νL) →F is a
homomorphism to a free abelian group which is non–trivial on each meridian of L. Under
these assumptions we can endow H1(S3 \νL;Q(R[F ])k) and H2(S3 \νL;Q(R[F ])k) with
dual bases and using these bases we can deﬁne the Reidemeiste r torsion
˜τα⊗ψ(L) ∈Q(F )∗/N(Q(F )∗),
here N (Q(F )∗) denotes the subgroup of norms of the multiplicative group Q(F )∗, i.e.
N (Q(F )∗) = {qq |q ∈ Q(F )∗}. Reidemeister torsion ˜ τα⊗ψ(L) viewed as an element in
Q(F )∗/N(Q(F )∗) is well–deﬁned up to multiplication by an element of the for m ±df where
18 STEF AN FRIEDL AND STEF ANO VIDUSSI
d ∈ det(α(π1(S3 \νL))),f ∈F . The invariant τα⊗ψ(L) is the twisted version of an invariant
ﬁrst introduced by Turaev [Tu86, Section 5.1].
For example, if L is the m–component unlink in S3 with meridians µ 1,...,µ m, then given
α and ψ as above we have
˜τα⊗ψ(L) = ±df ·
m∏
i=1
det
(
id −ψ(µi)α(µi)
) −1 ∈Q(F )∗/N(Q(F )∗)
with d ∈ det(α(π1(S3 \νL))),f ∈F .
In [CF10] the ﬁrst author and Jae Choon Cha prove the followin g result.
Proposition 5.6. LetL be an m–component oriented slice link with meridians µ 1,...,µ m.
Let R ⊂ C be a subring closed under complex conjugation and let α : π1(S3 \νL) →
GL(k,R ) be a representation which factors through a ﬁnite group of pr ime power order. Let
ψ :H1(S3 \νL) →F be an epimorphism onto a free abelian group which is non–triv ial on
each meridian of L. Then
˜τα⊗ψ(L) = ±df ·
m∏
i=1
det
(
id −ψ(µi)α(µi)
) −1 ∈Q(F )∗/N(Q(F ))∗
for some d ∈ det(α(π1(S3 \νL))) and f ∈F .
If α is the trivial representation over Z, then it is shown in [Tu86, Theorem 5.1.1] that
the torsion is represented by the untwisted Alexander polyn omial of L corresponding to ψ.
Using this observation we see that Proposition 5.6 generali zes earlier results of Murasugi
[Mu67], Kawauchi [Ka77, Ka78] and Nakagawa [Na78]. The appr oach taken in [CF10] is
partly inspired by Turaev’s proof of the untwisted case (cf. [Tu86, Theorem 5.4.2]).
In [CF10] we will in particular use the obstruction of Propos ition 5.6 to reprove that the
Bing double of the Figure 8 knot is not slice. This had ﬁrst bee n shown by Cha [Ch09].
