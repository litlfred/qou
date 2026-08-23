---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-020-63-normalized-twisted-reidemeister-torsion-and-t
section_title: "Normalized twisted Reidemeister torsion and the free genus of a knot"
section_number: 6.3
pages: 23-24
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexand er polynomials of a 3–manifold associated to a representation of its fundam ental group."
---
K ⊂S3 a knot and let γ :π1(S3 \νK ) → GL(k,R ) be a representation with R a Noetherian
UFD. Letǫ = det(γ(µ )) whereµ denotes a meridian of K. Kitayama [Kiy08a] introduced an
invariant ˜∆ K,γ ∈Q(R(ǫ
1
2 )[t± 1
2 ]) which is a normalized version of the twisted Reidemeister
torsion τ (K,γ ), i.e. τ (K,γ ) has no indeterminacy and up to multiplication by an element
of the form ǫrt
s
2 it is a representative of the twisted Reidemeister torsion. (The invariant
˜∆ K,γ should not be confused with the torsion polynomial introduc ed in Section 5.4.)
Kitayama [Kiy08a, Theorem 6.3] studies the invariant ˜∆ K,γ for ﬁbered knots, obtaining
a reﬁned version of the ﬁbering obstruction which we stated i n Theorem 6.2. Furthermore
[Kiy08a, Theorem 5.8] proves a duality theorem for ˜∆ K,γ, reﬁning Proposition 3.6.
In the following we say that S is a free Seifert surface forK ifπ1(S3 \S) is a free group.
Note that Seifert’s algorithm produces free Seifert surfac es, in particular any knot has a
free Seifert surface. Given K the free genus is now deﬁned as
free-genus(K) = min {genus(S) |S free Seifert surface for K}.
Clearly we have free-genus( K) ≥ genus(K). In order to state the lower bound on the
free genus coming from ˜∆ K,γ we have to make a few more deﬁnitions. Given a Laurent
polynomial p = ∑ l
i=kaiti ∈ R[t± 1
2 ] with ak ⁄= 0,al ⁄= 0 we write l-deg( p) = k (‘lowest
degree’) and h-deg(p) = l (‘highest degree’). Furthermore givenf ∈Q(R[t± 1
2 ]) we deﬁne
h-deg(f ) = h-deg(p) − h-deg(q)
where we pick p,q ∈ R[t± 1
2 ] with f = p
q . Kitayama [Kiy08a, Proposition 6.6] proved the
following theorem:
Theorem 6.8. Given a knot K ⊂ S3 and a representation γ : π1(S3 \νK ) → GL(k,R )
with R a Noetherian UFD we have
2kfree-genus(K) ≥ 2 h-deg( ˜∆ K,γ ) +k.
Note that if h-deg( ˜∆ K,γ ) = − l-deg( ˜∆ K,γ) (which is the case for unitary representations)
then the bound in the theorem is implied by the bound given in T heorem 6.6. It is a very
interesting question whether Kitayama’s bound can detect t he diﬀerence between the genus
and the free genus.
Recall that Lin’s original deﬁnition of the twisted Alexand er polynomial is in terms of
regular Seifert surfaces, it might be worthwhile to explore the possibility that an appropriate
version of Lin’s twisted Alexander polynomial gives lower b ounds on the ‘regular genus’ of
a knot which can tell the regular genus apart from the free gen us.
24 STEF AN FRIEDL AND STEF ANO VIDUSSI
