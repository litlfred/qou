---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-028-45-proof-of-the-main-theorem
section_title: "Proof of the main theorem"
section_number: 4.5
pages: 93-96
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
85
of a smooth non-hyperelliptic curve. As in lemma 4.11 the singular loci of
the relative theta divisor ΘS and of the ﬁbre Θs satisfy
Sing(ΘS) ⊆Sing(Θs),
so it follows from corollary 4.10 that the specialization sp(δΘη) admits the
simple perverse sheaf δΘs as a subquotient. Then the same holds for the
nearby cycles Ψ(δΘη) as well, and this proves our claim since by the result
for Jacobian varieties in [106], the Brill-Noether sheaf δΘs corresponds to
the g −1st fundamental representation of its Tannaka group which in the
non-hyperelliptic case is G(δΘs) = Sl2g−2(Λ)/µg−1.
□
4.5. Proof of the main theorem
Let X be a complex ppav of dimension g and Θ ⊂X a symmetric theta
divisor deﬁning the polarization. Consider the Tannaka group G = G(δΘ)
and its representation
V = ω(δΘ) ∈RepC(G)
which corresponds to the perverse intersection cohomology sheaf δΘ un-
der the equivalence ω : ⟨δΘ⟩−→RepC(G) in corollary 3.10. The Tannaka
group does not have to be connected, but fortunately it is not very far from
being connected either. Indeed we have the following
LEMMA 4.13. If the theta divisor is irreducible, then V restricts to an
irreducible representation V|G0 of the connected component G0 ⊆G.
Proof. The irreducibility of the theta divisor implies that δΘ is a simple
perverse sheaf, and accordingly V is an irreducible representation of the
Tannaka group G. But by the fundamental result of [109] the group G/G0
is abelian, hence if the claim of our lemma were not true, then by lemma B.4
in the appendix we would have an isomorphism V ⊗χ ∼= V for a suitable
non-trivial character χ : G −→C∗. The classiﬁcation of perverse sheaves
with Euler characteristic one in proposition 1.6 shows that χ corresponds
to a skyscraper sheaf δx of rank one, supported in some closed point x̸ = 0
of the ppav X. Hence the above isomorphism would on the geometric side
correspond to an isomorphism
δΘ ∗δx ∼= δΘ,
meaning that tx(Θ) = Θ for the translation tx : X →X,y 7→y+x. But this is
impossible for any point x̸ = 0, indeed the morphism
X −→Pic0(X),
x 7→

OX(Θ−tx(Θ))

is an isomorphism since the theta divisor gives a principal polarization.
□
86
Chapter 4 – The Tannaka group of the theta divisor
Now suppose that X is a general ppav. By lemma 4.6 the corresponding
Tannaka group admits an embedding
G = G(δΘ) ,→G(g) =
(
Spg!(C)
for even g,
SOg!(C)
for odd g,
and the representation V = ω(δΘ) arises as the restriction of the standard
representation of the classical group on the right hand side. For the proof
of theorem 4.2 we will show that for a general ppav the group G must be
as large as possible, using the lower bounds in proposition 4.12. We begin
with the following observation.
LEMMA 4.14. For a general ppav X with Tannaka group G = G(δΘ),
the connected component G0 ⊆G is simple modulo its center.
Proof. Let us ﬁrst introduce some notations. For any reductive complex
algebraic group H consider the derived group H0
der = [H0,H0]. This is a
connected semisimple group, and we denote by
˜H ↠H0
der
its simply connected cover. The covering group ˜H is a product of simply
connected covers of simple algebraic groups. Furthermore, since by the
theory of reductive groups [100, cor. 8.1.6] the connected component H0 is
the product of its derived group and its center (with ﬁnite intersection), any
irreducible representation of H0 is also irreducible under ˜H.
We now return to the Tannaka group G = G(δΘ) for a general ppav. To
prove the lemma we argue by contradiction. If the claim of the lemma is not
true, then the simply connected cover of this Tannaka group can be written
in the form
˜G = G1 ×G2
for certain non-trivial simply connected groups G1 and G2. Furthermore,
for the representation V = ω(δΘ) we have seen in lemma 4.13 that V|G0 is
irreducible. Hence by the above remarks also ˜G = G1 ×G2 acts irreducibly
on V so that we can write
V| ˜G = V1 ⊗V2
with certain irreducible representations Vi ∈RepC(Gi). Note that since V is
a faithful representation of G, it follows from the deﬁnition of the simply
connected covering group that the representations Vi are non-trivial and in
particular that dim(Vi) > 1. Now consider a connected subgroup H ,→G as
in part (2) of proposition 4.12 so that
V|H = W ⊕
(
1⊕1
if g is even,
1
if g is odd,
4.5. Proof of the main theorem
87
where W is some irreducible representation of the group H. Then via the
commutative diagram
˜H
∃
/

˜G
/

Gl(V1)×Gl(V2)

H  
/ G  
/ Gl(V)
Gl(V1 ⊗V2)
we can consider the restrictions of V1 and V2 to the covering group ˜H, and
by construction we have
V1| ˜H ⊗V2| ˜H = V| ˜H = W| ˜H ⊕
(
1⊕1
if g is even,
1
if g is odd,
where W| ˜H is irreducible by the general remarks from the beginning of the
proof. This implies that both Vi| ˜H are irreducible because otherwise more
than one non-trivial direct summand would occur. But then, since
Hom ˜H(1, V1| ˜H ⊗V2| ˜H)̸ = 0,
adjunction shows V1| ˜H is isomorphic to the dual of V2| ˜H. In particular V1
and V2 have the same dimension. This is impossible since dim(V) = g! is
not the square of a natural number for g > 1.
For g = 4 we can alternatively argue as follows, using only part (3) of
proposition 4.12. Here both V1 and V2 have dimension at most 12 since
their dimensions must be non-trivial divisors of dim(V) = 24. So if instead
of our previous choice we now take the subgroup H ,→G to be isogenous
to Sl2g−2(C) = Sl6(C) with the property in part (3) of the proposition, then
by the classiﬁcation of small representations in [3] each Vi| ˜H can contain
only trivial representations and 6-dimensional standard representations as
irreducible constituents. In particular, looking at V1| ˜H ⊗V2| ˜H one sees that
the third fundamental representation of Sl6(C) cannot occur as a constituent
of V|H, and this contradicts our choice of the subgroup H.
□
Now recall that the Tannaka group G = G(δΘ) of a general ppav is in
any case a subgroup of the symplectic or special orthogonal group G(g),
hence to prove theorem 4.2 it will be enough to show that the connected
component G0 must be the full group G(g). Note that by lemma 4.13 this
connected component is an irreducible subgroup of G(g) in the sense that
for the standard representation V ∈RepC(G(g)), the restriction V|G0 is still
irreducible. So we are in the situation of the following general lemma.
88
Chapter 4 – The Tannaka group of the theta divisor
LEMMA 4.15. Let H be an irreducible connected subgroup of G(g)
which is simple modulo its center. Then
dim(H) ≤g!
or
H = G(g).
Proof. Let V denote the standard representation of the symplectic or
special orthogonal group G(g), and suppose dim(H) > g! = dim(V). Then
by irreducibility the restriction of V to H must be one of the representations
in table 1 of [3]. Since dim(V) is the factorial of a natural number, one of
the following cases must occur for some r ∈N.
(a) The group H is of type Ar, Cr or Dr and acts on V via its standard
representation.
(b) The group H is of type Ar and acts on V via the symmetric or via
the alternating square of its standard representation.
Case (a) can only occur for H = G(g) since G(g) is itself the symplectic
or special orthogonal group with V as its standard representation. To deal
with case (b), note that by the criterion in [46, th. 3.2.14] the symmetric
square of the standard representation of Ar is self-dual only if r = 1, but
then it has dimension 3̸ = dim(V). In the same vein, the alternating square
of the standard representation of Ar is self-dual of dimension g! only in the
case (r,g) = (3,3) where H = G(g) = SO6(C) for dimension reasons.
□
To complete the proof of theorem 4.2, all that remains to be done is to
show that on a general ppav X we have
dim(G) > g!
for the group G = G(δΘ) attached to the theta divisor. But this follows by
induction on the dimension g = dim(X). Indeed, we already know that the
theorem holds for g ≤3, so we can assume g ≥4. To start the induction,
for g = 4 we can use the subgroup in part (3) of proposition 4.12 since in
that case dim(Sl2g−2(C)) = 35 > g! = 24. This being settled, the induction
step from dimension g −1 to dimension g is provided by part (1) of the
proposition because dim(G(g−1)) > g! for g ≥5. This ﬁnishes the proof of
the theorem. Going through the above arguments, one furthermore checks
that for g = 4 all we need is part (3) of proposition 4.12. Hence theorem 4.3
follows with the same proof.
