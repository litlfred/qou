---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-044-53-some-properties-of-triangulated-categories
section_title: "Some Properties of Triangulated Categories"
section_number: 5.3
pages: 96-102
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
a few general results on triangulated categories. Recall that all triangulated cate-
gories, and all triangulated functors between them, are (implicitly) K-linear.
Proposition 5.3.1. Let K be a triangulated category. If L
α−→M
β−→N
γ−→T(L) is
a distinguished triangle in K, then β ◦α = 0.
Proof. By axioms (TR1) and (TR3) we have a commutative diagram
L
idL
/
idL

L
/
α

0
/

T(L)
T(idL)

L
α
/ M
β
/ N
γ
/ T(L) .
We see that β ◦α factors through 0.
□
96
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Proposition 5.3.2. Let K be a triangulated category, and let
L
α
/
φ

M
β
/
ψ

N
γ
/
χ

T(L)
T(φ)

L′
α′
/ M ′
β′
/ N ′
γ′
/ T(L′) .
be a morphism of distinguished triangles. If φ and ψ are isomorphisms, then χ is
also an isomorphism.
Proof. Take an arbitrary P ∈K, and let F := HomK(P, −). We get a commutative
diagram
F(L)
F (α) /
F (φ)

F(M)
F (β)
/
F (ψ)

F(N)
F (γ) /
F (χ)

F(T(L))
F (T(φ))

F (T(α)) / F(T(M))
F (T(ψ))

F(L′)
F (α′) / F(M ′)
F (β′) / F(N ′)
F (γ′) / F(T(L′))
F (T(α′))/ F(T(M ′))
in Mod K. By Proposition 5.2.7 the rows in the diagram are exact sequences. Since
the other vertical arrows are isomorphisms, it follows that
F(χ) : HomK(P, N) →HomK(P, N ′)
is an isomorphism of abelian groups. By forgetting structure, we see that F(χ) is
an isomorphism of sets.
Consider the Yoneda functor YK : K →Fun(Kop, Set) from Subsection 1.7. There
is a morphism YK(χ) : YK(N) →YK(N ′) in Fun(Kop, Set). For every object P ∈K,
letting F := HomK(P, −) as above, we have YK(N)(P) = F(N) and YK(N ′)(P) =
F(N ′). The calculation above shows that
F(χ) = YK(χ)(P) : YK(N)(P) →YK(N ′)(P)
is an isomorphism in Set. Therefore YK(χ) is an isomorphism in Fun(Kop, Set).
According to Yoneda Lemma (Theorem 1.7.4) the morphism χ : N →N ′ in K is
an isomorphism.
□
Exercise 5.3.3. Try to prove the last proposition without the Yoneda Lemma.
Recall that if η : F →G is a morphism of functors K →L, then for an object
M ∈K we denote by ηM : F(M) →G(M) the corresponding morphism in L.
Corollary 5.3.4. Suppose F, G : K →L are triangulated functors between trian-
gulated categories, and η : F →G is a morphism of triangulated functors. Let
L
α−→M
β−→N
γ−→T(L) be a distinguished triangle in K. If ηL and ηM are isomor-
phisms, then ηN is an isomorphism.
Proof. After applying the functors F and G, and the morphisms of functors τF , τG
and η, we obtain a commutative diagram
F(L)
F (α) /
ηL

F(M)
F (β)
/
ηM

F(N)
τF,L◦F (γ)
/
ηN

TL(F(L))
TL(ηL)

G(L)
G(α) / G(M)
G(β)
/ G(N)
τG,L◦G(γ)
/ TL(G(L))
in L in which the rows are distinguished triangles. According to Proposition 5.3.2
the morphism ηN is an isomorphism.
□
97
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Corollary 5.3.5. Let K be a triangulated category, and let L
α−→M −→N
△
−−→be a
distinguished triangle in it. The two conditions below are equivalent.
(i) α : L →M is an isomorphism.
(ii) N ∼= 0.
Exercise 5.3.6. Prove Corollary 5.3.5. (Hint: Use Proposition 5.3.2 and axiom
(TR1)(c).)
Deﬁnition 5.3.7. Let K be a triangulated category, and let α : L →M be a
morphism in K. By axiom (TR1)(b) there exists a distinguished triangle
(†)
L
α−→M
β−→N
γ−→T(L)
in K. The object N is called a cone of α, and the distinguished triangle (†) is called
a distinguished triangle built on α.
Corollary 5.3.8. In the situation of Deﬁnition 5.3.7, the object N and the distin-
guished triangle (†) are unique up to isomorphism.
Proof. Suppose
(†′)
L
α−→M
β′
−→N ′
γ′
−→T(L)
is another distinguished triangle built on α. By axiom (TR3) there is a commutative
diagram
L
α
/
idL

M
β
/
idM

N
γ
/
χ

T(L)
T(idL)

L
α
/ M
β′
/ N ′
γ′
/ T(L) .
in K. Proposition 5.3.2 says that χ is an isomorphism.
□
Remark 5.3.9. In general the isomorphism χ in the corollary above is not unique,
and thus the cone of α is not functorial in the morphism α. However, in some
special cases χ is unique – see Remark 5.3.26 below.
Note also that the standard cones and triangles in the DG category C(A, M) are
functorial, by Proposition 4.2.6. This implies that in the triangulated categories
K(A, M) and D(A, M) we can sometimes arrange to have functorial cones.
Proposition 5.3.10. Let K be a triangulated category, and let L
α−→M
β−→N
γ−→
T(L) be a distinguished triangle in it. The two conditions below are equivalent.
(i) The morphism γ is zero.
(ii) There exists a morphism τ : M →L such that τ ◦α = idL.
Proof.
(i) ⇒(ii): By Propositions 5.2.7 the contravariant functor HomK(−, L) is coho-
mological. Applying it to the given distinguished triangle, and using Proposition
5.2.6, we get an exact sequence of K-modules
HomK(M, L)
Hom(α,idL)
−−−−−−−→HomK(L, L)
Hom(T−1(γ),idL)
−−−−−−−−−−−→HomK(T−1(N), L).
Since the homomorphism HomK(T−1(γ), idL) is zero, there exists some morphism
τ ∈HomK(M, L) such that idL = HomK(α, idL)(τ) = τ ◦α.
98
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(ii) ⇒(i): Let us examine the commutative diagram
HomK(N, N)
Hom(id,γ)

HomK(N, T(L))
Hom(id,T(α))

Hom(id,id)
$
HomK(N, T(M))
Hom(id,T(τ)) / HomK(N, T(L))
in Mod K. Because the homomorphism HomK(id, id) is bijective, it follows that
HomK(id, T(α)) is injective.
But the column is an exact sequence (by Proposi-
tions 5.2.7 and 5.2.6), and therefore HomK(idN, γ) = 0. We conclude that γ =
HomK(idN, γ)(idN) = 0.
□
Lemma 5.3.11. Let M, M ′ be objects in a triangulated category K. Consider the
canonical morphisms
M
e−→M ⊕M ′
p−→M
and
M ′
e′
−→M ⊕M ′
p′
−→M ′.
Then
M
e−→M ⊕M ′
p′
−→M ′
0−→T(M)
is a distinguished triangle in K.
Proof. By axiom (TR1)(c) and axiom (TR2) there is a distinguished triangle 0
0−→
M ′
idM′
−−−→M ′
0−→0. By axiom (TR1)(b) there is a distinguished triangle
(5.3.12)
M
e−→M ⊕M ′
β−→N
γ−→T(M)
in K, for some object N. Because p ◦e = idM, Proposition 5.3.10 says that γ = 0.
Next, since p′ ◦e = 0, axiom (TR3) produces a morphism of triangles
(5.3.13)
M
e
/
0

M ⊕M ′
β
/
p′

N
γ=0
/
ψ

T(M)
0

0
0
/ M ′
idM′
/ M ′
0
/ 0
We claim that ψ is an isomorphism. This is proved indirectly. For every object
L ∈K there is a commutative diagram
(5.3.14)
HomK(L, M)
/ HomK(L, M ⊕M ′)
/
Hom(idL,p′)

HomK(L, N)
/
Hom(idL,ψ)

0
0
/ HomK(L, M ′)
id
/ HomK(L, M ′)
/ 0
in Mod K, that’s gotten by applying the functor HomK(L, −) to the left part of
diagram (5.3.13). The rows in (5.3.14) are exact sequences. Because
HomK(L, M ⊕M ′) ∼= HomK(L, M) ⊕HomK(L, M ′)
we can replace (5.3.14) with the next commutative diagram
(5.3.15)
0
/ HomK(L, M ′)
/
Hom(idL,idM′)

HomK(L, N)
/
Hom(idL,ψ)

0
0
/ HomK(L, M ′)
id / HomK(L, M ′)
/ 0
99
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
with exact rows. We see that Hom(idL, ψ) is an isomorphism of K-modules. Hence
it is a bijection of sets. Using the Yoneda Lemma, like in the proof of Proposition
5.3.2, we conclude that ψ is an isomorphism in K.
Finally, from the commutative diagram (5.3.13) we know that ψ ◦β = p′. So we
have this isomorphism of triangles:
(5.3.16)
M
e
/
id

M ⊕M ′
β
/
id

N
γ=0 /
ψ
∼
=

T(M)
id

M
e
/ M ⊕M ′
p′
/ M ′
0
/ T(M)
The ﬁrst triangle is distinguished. By axiom (TR1)(a) the second triangle is also
distinguished.
□
Deﬁnition 5.3.17. Let K be a linear category, and let M, N ∈K.
(1) The object M is called a retract of N if there are morphisms M
e−→N
p−→M
such that p ◦e = idM. The morphism e : M →N is called an embedding.
(2) The object M is called a direct summand of N if there is an object M ′ ∈K
and an isomorphism M ⊕M ′ ∼= N. The corresponding morphism e : M →
N is called an embedding.
Note that in both items above the embedding e : M →N is a monomorphism
in K.
Theorem 5.3.18. Let K be a triangulated category, and let e : M →N be a
morphism in K. The following two conditions are equivalent:
(i) There is a morphism e′ : M ′ →N in K such that
(e, e′) : M ⊕M ′ →N
is an isomorphism. In other words, M is a direct summand of N, with
embedding e : M →N.
(ii) There is a morphism p : N →M in K such that p ◦e = idM. In other
words, M is a retract of N, with embedding e : M →N.
Proof.
(i) ⇒(ii): This is trivial (and only requires K to be a linear category).
(ii) ⇒(i): Let M
e−→N
β−→M ′
γ−→T(M) be a distinguished triangle in K built
on e. By Proposition 5.3.10 we know that γ = 0. According to Lemma 5.3.11,
M
ϵ−→M ⊕M ′
π′
−→M ′
0−→T(M) is also the distinguished triangle in K; here ϵ is the
embedding and π′ is the projection. Turning these two distinguished triangles and
using axiom (TR3) we get a morphism θ such that the diagram
T−1(M ′)
0
/
id

M
ϵ
/
id

M ⊕M ′
π′
/
θ

M ′
id

T−1(M ′)
0
/ M
e
/ N
β
/ M ′
is commutative.
By Proposition 5.3.2, θ is an isomorphism.
Finally we deﬁne
e′ := θ ◦ϵ′, where ϵ′ : M ′ →M ⊕M ′ is the embedding.
□
Deﬁnition 5.3.19. Let K be a triangulated category. A saturated full triangulated
subcategory of K is a full triangulated subcategory K′ ⊆K (Deﬁnition 5.2.2) which
is closed in K under taking direct summands and under isomorphisms.
100
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Deﬁnition 5.3.20. Let K be a triangulated category and let Z ⊆Ob(K) be a set
of objects. The saturated full triangulated subcategory of K generated by Z is the
smallest saturated full triangulated subcategory K′ ⊆K such that Z ⊆Ob(K′).
Proposition 5.3.21. Let K be a triangulated category, let Z ⊆Ob(K) be a set of
objects, and let K′ ⊆K be the saturated full triangulated subcategory of K generated
by Z. An object M ∈K belongs to K′ if and only if there is a sequence M0, . . . , Mr
of objects of K, such that Mr = M, and for every i ≤r at least one of the following
conditions holds:
(a) Mi ∈Z.
(b) There is an isomorphism Mi ∼= Tp(Mj) in K for some j < i and p ∈Z.
(c) There is a distinguished triangle Mj →Mk →Mi
△
−−→in K for some
j, k < i.
(d) Mi is a direct summand of Mj in K for some j < i.
Proposition 5.3.22. Let K and L be triangulated categories, let F, G : K →L be
triangulated functors, and let ζ : F →G be a morphism of triangulated functors.
Denote by K′ the full subcategory of K on the objects M such that ζM : F(M) →
G(M) is an isomorphism in L. Then K′ is a saturated full triangulated subcategory
of K.
Corollary 5.3.23. Let K and L be triangulated categories, let F : K →L be a
triangulated functor, and let K′ be the kernel of F, i.e. K′ ⊆K is the full subcategory
on the objects M ∈K such that F(M) = 0. Then K′ is a saturated full triangulated
subcategory of K.
Exercise 5.3.24. Prove Proposition 5.3.21, Proposition 5.3.22 and Corollary
5.3.23.
We end this subsection with two remarks.
Remark 5.3.25. The story of the concept “saturated full triangulated subcate-
gory” is convoluted. In the text [155] from 1977, J.-L. Verdier introduced épaisse
full triangulated subcategories (a rather messy deﬁnition).
However, J. Rickard
proved (see [125, Proposition 1.3], published in 1989) that épaisse is equivalent to
saturated, as deﬁned above. Rickard did not give a name for this new and useful
property.
Verdier died in 1989.
A few years later, in 1996, G. Maltsiniotis published
Verdier’s thesis [156]. In this thesis the word “épaisse” is absent, and instead we
ﬁnd the deﬁnition of saturated categories, identical to Deﬁnition 5.3.19. Maltsiniotis
notes that Verdier was aware (although this is only implicit in his writing) of the
equivalence between épaisse and saturated; indeed, these are precisely the categories
that occur as kernels of triangulated functors (see Corollary 5.3.23 above, and
Remark 7.1.14 on Verdier quotients and saturated denominator sets of morphisms).
Remark 5.3.26. As mentioned above, in Remark 5.3.9, the cone of a morphism
α : L →M in a triangulated category D is usually not functorial. However, if D
is endowed with a t-structure, then some cones can be made functorial. Here is a
quick explanation.
The concept of t-structure was introduced by A.A. Beilinson, J. Bernstein and
P. Deligne in the book [16]. A t-structure on a triangulated category D consists of
a pair (D≤0, D≥0) of full subcategories of D, that satisfy a few axioms (see e.g. [75,
Chapter X] or [187, Deﬁnition 4.1]). The prototypical example is the standard t-
structure on D := D(M), the derived category of an abelian category M (see Section
7 of the book). Here D≤0 is the full subcategory of D(M) on the complexes M with
nonpositive cohomology, and D≥0 is the full subcategory of D(M) on the complexes
101
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
M with nonnegative cohomology. Other t-structures on D = D(M) are often called
perverse t-structures.
The heart of the t-structure (D≤0, D≥0) is the category D0 := D≤0 ∩D≥0. In
the prototypical example above, the heart is the category of complexes M with
cohomology concentrated in degree 0, so it is equivalent to M. Something similar
happens in general: the heart D0 is always an abelian category, and there is a
cohomological functor H0 : D →D0. The short exact sequences 0 →L
α−→M
β−→
N →0 in D0 are the distinguished triangles L
α−→M
β−→N
△
−−→in D such that
L, M, N ∈D0.
Here is how a t-structure (D≤0, D≥0) aﬀects functoriality of cones. Axiom (TR3)
guarantees that for a pair of distinguished triangles and morphism φ, ψ as in the
solid diagram below, there is at least one morphism χ (the dashed arrow) making
the whole diagram commutative.
L
α
/
φ

M
β
/
ψ

N
γ
/
χ

T(L)
T(φ)

L′
α′
/ M ′
β′
/ N ′
γ′
/ T(L′)
According to [16, Proposition 1.1.9] (see also [187, Lemma 4.10]), if L ∈D≤0 and
T(N ′) ∈D≥0, then this morphism χ is unique.
The idea of a t-structure emerged in the study of algebraic topology, microlocal
analysis and representations of Lie algebras. In that context the triangulated cat-
egory D was the full subcategory of D(KX) on complexes with suitable ﬁniteness
and constructibility conditions. The base ring K was either a ﬁeld or the l-adic
integers bZl. The space (or site) X was either a topological space with a classical
metric topology, or a scheme with its étale topology. The objects of the heart where
called perverse sheaves. This theory is explained in the original book [16], and also
in [27] and in [75, Chapter X]. In algebraic geometry one can also consider perverse
coherent sheaves; see [187] and [4].
