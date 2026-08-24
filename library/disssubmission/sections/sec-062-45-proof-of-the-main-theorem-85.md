---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-062-45-proof-of-the-main-theorem-85
section_title: "Proof of the main theorem 85"
section_number: 4.5
pages: 93-95
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
of a smooth non-hyperelliptic curve. As in lemma 4.11 the singular loci of
the relative theta divisorΘS and of the ﬁbreΘs satisfy
Sing(ΘS)⊆ Sing(Θs),
so it follows from corollary 4.10 that the specializationsp(δΘη) admits the
simple perverse sheafδΘs as a subquotient. Then the same holds for the
nearby cyclesΨ(δΘη) as well, and this proves our claim since by the result
for Jacobian varieties in [106], the Brill-Noether sheafδΘs corresponds to
the g−1st fundamental representation of its Tannaka group which in the
non-hyperelliptic case isG(δΘs) =Sl2g−2(Λ)/µg−1. □
4.5. Proof of the main theorem
Let X be a complex ppav of dimensiong and Θ⊂ X a symmetric theta
divisor deﬁning the polarization. Consider the Tannaka groupG = G(δΘ)
and its representation
V = ω(δΘ)∈ RepC(G)
which corresponds to the perverse intersection cohomology sheafδΘ un-
der the equivalenceω :⟨δΘ⟩−→RepC(G) in corollary 3.10. The Tannaka
group does not have to be connected, but fortunately it is not very far from
being connected either. Indeed we have the following
LEMMA 4.13. If the theta divisor is irreducible, then V restricts to an
irreducible representation V|G0 of the connected component G0⊆ G.
Proof.The irreducibility of the theta divisor implies thatδΘ is a simple
perverse sheaf, and accordinglyV is an irreducible representation of the
Tannaka groupG. But by the fundamental result of [109] the groupG/G0
is abelian, hence if the claim of our lemma were not true, then by lemma B.4
in the appendix we would have an isomorphismV⊗ χ∼= V for a suitable
non-trivial characterχ : G−→C∗. The classiﬁcation of perverse sheaves
with Euler characteristic one in proposition 1.6 shows thatχ corresponds
to a skyscraper sheafδx of rank one, supported in some closed pointx⁄= 0
of the ppavX. Hence the above isomorphism would on the geometric side
correspond to an isomorphism
δΘ∗δx∼= δΘ,
meaning thattx(Θ) =Θ for the translationtx : X→X,y↦→y+x. But this is
impossible for any pointx⁄= 0, indeed the morphism
X−→Pic0(X), x↦→[OX(Θ−tx(Θ))]
is an isomorphism since the theta divisor gives a principal polarization.□
86 Chapter 4 – The Tannaka group of the theta divisor
Now suppose thatX is a general ppav. By lemma 4.6 the corresponding
Tannaka group admits an embedding
G = G(δΘ) ↪→ G(g) =
{
Spg!(C) for eveng,
SOg!(C) for oddg,
and the representationV = ω(δΘ) arises as the restriction of the standard
representation of the classical group on the right hand side. For the proof
of theorem 4.2 we will show that for a general ppav the groupG must be
as large as possible, using the lower bounds in proposition 4.12. We begin
with the following observation.
LEMMA 4.14. For a general ppav X with Tannaka group G= G(δΘ),
the connected component G0⊆ G is simple modulo its center.
Proof.Let us ﬁrst introduce some notations. For any reductive complex
algebraic groupH consider the derived groupH0
der = [H0,H0]. This is a
connected semisimple group, and we denote by
˜H↠ H0
der
its simply connected cover. The covering group˜H is a product of simply
connected covers of simple algebraic groups. Furthermore, since by the
theory of reductive groups [100, cor. 8.1.6] the connected componentH0 is
the product of its derived group and its center (with ﬁnite intersection), any
irreducible representation ofH0 is also irreducible under˜H.
We now return to the Tannaka groupG = G(δΘ) for a general ppav. To
prove the lemma we argue by contradiction. If the claim of the lemma is not
true, then the simply connected cover of this Tannaka group can be written
in the form
˜G = G1×G2
for certain non-trivial simply connected groupsG1 and G2. Furthermore,
for the representationV = ω(δΘ) we have seen in lemma 4.13 thatV|G0 is
irreducible. Hence by the above remarks also˜G = G1×G2 acts irreducibly
onV so that we can write
V| ˜G = V1⊗V2
with certain irreducible representationsVi∈ RepC(Gi). Note that sinceV is
a faithful representation ofG, it follows from the deﬁnition of the simply
connected covering group that the representationsVi are non-trivial and in
particular that dim(Vi) > 1. Now consider a connected subgroupH ↪→G as
in part (2) of proposition 4.12 so that
V|H = W⊕
{
1⊕1 if g is even,
1 if g is odd,
