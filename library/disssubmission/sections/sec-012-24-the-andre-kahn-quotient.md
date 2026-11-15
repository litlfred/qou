---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-012-24-the-andre-kahn-quotient
section_title: "The Andr´e-Kahn quotient"
section_number: 2.4
pages: 40-43
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
For the Tannakian arguments to be given below, we want to work with
rigid symmetric monoidal categories which are at the same time semisimple
abelian categories. To obtain such a category D that is as close as possible
to the triangulated category D, we will apply a general quotient construction
introduced by Andr´e and Kahn in [1]. In what follows we always assume
that axioms (D1) – (D4) from the previous section, i.e. all axioms except
for the hard Lefschetz axiom, are satisﬁed.
The construction of Andr´e and Kahn works as follows. By rigidity we
have for each K ∈D an isomorphism HomD(K,K)
∼
−→HomD(1,K ∗K∨)
which in what follows we denote by f 7→f ♯. We then deﬁne the categorical
trace tr(f) ∈EndD(1) = Λ of an endomorphism f ∈HomD(K,K) to be the
composite morphism
tr(f) :
1
f ♯
/ K ∗K∨
SK,K∨/ K∨∗K
evK
/ 1
where as usual SK,K∨denotes the symmetry constraint and evK denotes the
evaluation morphism. Following section 7.1 of loc. cit. we then deﬁne the
Andr´e-Kahn radical ND on objects K,L ∈D by
ND(K,L) =

f ∈HomD(K,L) | ∀g ∈HomD(L,K) : tr(g◦f) = 0
	
.
This is an ideal of D in the sense that for all objects K,K′,L,L′ ∈D and all
morphisms h1 ∈HomD(K′,K), h2 ∈HomD(L,L′) one can show
h2 ◦ND(K,L)◦h1 ⊆ND(K′,L′).
2.4. The Andr´e-Kahn quotient
33
For any ideal one has the notion of the corresponding quotient category. By
deﬁnition, the quotient
D = D/ND
has the same objects as D, but the morphisms in D between two objects K,L
are deﬁned by
HomD(K,L) = HomD(K,L)/ND(K,L).
We have a natural quotient functor q : D −→D that is given by the identity
on objects and by the quotient map on morphisms, and in what follows we
denote by P the essential image of P under this quotient functor. Recall that
ultimately we want to construct a semisimple abelian category; as a ﬁrst
step towards this goal we have
LEMMA 2.6. The quotient functor q : D −→D preserves direct sums,
and the category P is pseudo-abelian in the sense that every idempotent
morphism in it splits as the projection onto a direct summand.
Proof. The functor q preserves direct sums since it is Λ-linear. To see
that idempotents in P split, let P be an object of P. Since P is an abelian
category and hence in particular pseudo-abelian, it sufﬁces to show that
every idempotent in
EndP(P) = EndP(P)/ND(P,P)
lifts to an idempotent in EndP(P). Since P is semisimple by axiom (D4),
passing to isotypic components we can assume P = Q⊕r for some simple
object Q of P and r ∈N. Then EndP(P) is the ring of r×r matrices over the
skew ﬁeld EndP(Q). Since matrix rings over skew ﬁelds do not have proper
two-sided ideals, it follows that either ND(P,P) = 0 or ND(P,P) = EndP(P),
and in both cases the lifting of idempotents is obvious.
□
It turns out that this is already enough to conclude that the quotient
category D has the desired properties:
PROPOSITION 2.7. The quotient category D is a semisimple abelian
Λ-linear rigid symmetric monoidal category.
Proof. By [1, lemma 7.1.1] the Andr´e-Kahn radical ND is a monoidal
ideal in the sense that idM ∗ND(K,L) ⊆ND(M∗K,M∗L) for all K,L,M ∈D,
hence by sorite 6.1.4 of loc. cit. the quotient D = D/ND inherits from D
the structure of a Λ-linear rigid symmetric monoidal category whose unit
element satisﬁes EndD(1) = Λ.
The main part of the proof is to check that the category D is semisimple
abelian. For this we ﬁrst claim that
(⋆)
HomD(P[m],Q[n]) = 0
for all objects P,Q in P and m̸ = n.
34
Chapter 2 – Proof of the vanishing theorem(s)
Indeed, for m > n we even have HomD(P[m],Q[n]) = 0 since under the
faithful functor rat this Hom-group injects into
HomDbc (X,Λ)(rat(P)[m],rat(Q)[n]) = Extn−m
Perv(X,Λ)(rat(P),rat(Q))
which vanishes for m > n (for the above identiﬁcation as an Ext-group recall
that Db
c (X,Λ) is the derived category of Perv(X,Λ)). On the other hand, in
the case m < n we have HomD(Q[n],P[m]) = 0, and then the deﬁnition of
the Andr´e-Kahn radical implies that
HomD(P[m],Q[n]) = ND(P[m],Q[n])
which is mapped to zero under the quotient functor q : D −→D. In both
cases the claim (⋆) follows.
Now by the perverse decomposition axiom (D3) every object K of D
can be written as K = L
n∈Z Kn[n] with certain Kn in P. For such K the
vanishing in (⋆) implies
(⋆⋆)
EndD(K) =
M
n∈Z
EndD(Kn[n]) =
M
n∈Z
EndP(Kn).
In particular, every idempotent endomorphism of K in the category D is a
direct sum of idempotent endomorphisms of the summands Kn[n], and by
lemma 2.6 it follows that D is pseudo-abelian. Hence to show that D is a
semisimple abelian category, it will sufﬁce by [1, A.2.10] to show that it is
a semisimple Λ-linear category in the sense of section 2.1.1 in loc. cit. For
this we use the following general result [2, th. 1].
Let F be a ﬁeld and A an F-linear rigid symmetric monoidal category
with EndA(1) = F. Suppose there exists an F-linear tensor functor ACU
from A to an abelian F-linear rigid symmetric monoidal category V such
that dimΛ(HomV(V1,V2)) < ∞for all V1,V2 ∈V. Then the quotient of A by
its Andr´e-Kahn radical NA is a semisimple F-linear category, and NA is the
unique monoidal ideal of A with this property.
In our case this applies for F = Λ, A = D and for the functor H•(X,−)
from D to the abelian category V of super vector spaces over Λ.
□
COROLLARY 2.8. The functors P →P and P ,→D are exact functors
between semisimple abelian categories. The image of a simple object P ∈P
inside P is either simple or isomorphic to zero, and if Λ is algebraically
closed, then the latter case occurs if and only if χ(P) = 0.
Proof. By proposition 2.7, D is a semisimple abelian category, and it
also follows from the proof of the proposition that P is a semisimple abelian
subcategory of D. Since the considered functors are additive, they are exact
by semisimplicity. If P is a simple object of P, then EndP(P) is a skew ﬁeld,
