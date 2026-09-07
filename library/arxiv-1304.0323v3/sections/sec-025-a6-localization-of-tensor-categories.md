---
doc_id: arxiv-1304.0323v3
doc_title: "SYMMETRIC QUIVER HECKE ALGEBRAS R-MATRICES OF QUANTUM AFFINE ALGEBRAS"
section_id: sec-025-a6-localization-of-tensor-categories
section_title: "A.6. Localization of tensor categories"
section_number: null
pages: 72-75
source_pdf: 1304.0323v3.pdf
source_sha256: 92e2b9dc876e1a52
doc_brief: "SYMMETRIC QUIVER HECKE ALGEBRAS R-MATRICES OF QUANTUM AFFINE ALGEBRAS — Let J be a set of pairs consisting of good U ′ q(g)-modules and invertible elements in the base ﬁeld C(q)."
---
{(Pi,RPi)}i∈I be a family of central objects in T . Set
Bi,j =RPi(Pj) :Pi⊗Pj ∼−→Pj⊗Pi
for i,j ∈ I. If ( {Pi}i∈I,{Bi,j}i,j∈I) is a commuting family of objects, we say that
{(Pi,RPi)}i∈I is a commuting family of central objects (see also [ 21] for its generaliza-
tion). Note that it means that {(Pi,RPi)}i∈I satisﬁes the conditions:
(a) for any i∈I, RPi satisﬁes ( A.3.1),
(b) RPj (Pi)◦RPi(Pj) = idPi⊗Pj for any i,j∈I,
(c) RPi(Pi) = idPi⊗Pi for any i∈I.
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 73
For a commuting family {(Pi,RPi)}i∈I of central objects, let Φ i∈ Fct(T,T ) be the
endofunctor deﬁned by X↦→X⊗Pi. We deﬁne the isomorphism BΦ
i,j : Φ iΦj ∼−→ΦjΦi
by
ΦiΦj(X) = X⊗Pj⊗Pi ∼−−→Bj,i
X⊗Pi⊗Pj = Φ jΦi(X).
Then it is easy to see that {Φi}i∈I becomes a commuting family of endofunctors.
Let ~T =T [P⊗− 1
i | i∈ I] be the localization of T by{Φi}i∈I. Hence we have
Ob( ~T ) = Ob(T )× Z⊕I and
Hom ~T ((X,α ), (Y,β )) = lim −→
γ+α,γ +β∈Z⊕I
≥0,
γ∈Z⊕I
≥0
HomT (X⊗Pα+γ,Y ⊗Pβ+γ).
For any α∈ Z⊕I
≥0, we can deﬁne an isomorphism which is functorial in X
Rα(X) :Pα⊗X ∼−→X⊗Pα
such that the following diagrams are commutative for any X,Y ∈T :
Pα⊗X⊗Y
Rα(X)⊗Y
/d47/d47
Rα(X⊗Y )
/d44/d44
X⊗Pα⊗Y
X⊗Rα(Y )
/d47/d47X⊗Y⊗Pα ,
Pα⊗Pβ⊗X
/d15/d15
P α⊗Rβ (X)
/d47/d47Pα⊗X⊗Pβ
Rα(X)⊗P β
/d47/d47X⊗Pα⊗Pβ
/d15/d15
Pα+β⊗X
Rα+β (X) /d47/d47X⊗Pα+β,
Pi⊗X
≀/d15/d15
RPi (X)
/d47/d47X⊗Pi
≀/d15/d15
Pei⊗X
Rei (X) /d47/d47X⊗Pei.
Moreover, such isomorphisms Rα are unique.
Indeed,{(Pi,RPi)}i∈I is a commuting family in the tensor category Tc of central
objects of T .
The category ~T has a structure of tensor category as follows.
Forα,β ∈ Z⊕I and X,Y ∈T , we deﬁne
(X,α )⊗(Y,β ) = (X⊗Y,α +β).
Forα′,β′∈ Z⊕I and X′,Y ′∈T , we deﬁne the map
Hom ~T
(
(X,α ), (X′,α′)
)
× Hom ~T
(
(Y,β ), (Y′,β′)
)
74 S.-J. KANG, M. KASHIW ARA, M. KIM
→ Hom ~T
(
(X⊗Y,α +β), (X′⊗Y′,α′ +β′)
)
by taking the inductive limit of the composition of the morphisms below w ith respect
to γ,γ′∈ Z⊕I
≥0
HomT (X⊗Pα+γ,X′⊗Pα′+γ)× HomT (Y⊗Pβ+γ′
,Y ′⊗Pβ′+γ′
)
→ HomT (X⊗Pα+γ⊗Y⊗Pβ+γ′
,X′⊗Pα′+γ⊗Y′⊗Pβ′+γ′
)
≃ HomT
(
X⊗Y⊗Pα+γ⊗Pβ+γ′
,X′⊗Y′⊗Pα′+γ⊗Pβ′+γ′)
≃ HomT
(
X⊗Y⊗Pα+α′+γ+γ′
,X′⊗Y′⊗Pα′+β′+γ+γ′)
→ Hom ~T
(
(X⊗Y,α +β), (X′⊗Y′,α′ +β′)
)
.
It is easy to verify that ~T becomes a tensor category. Moreover, X↦→(X, 0) gives a
tensor functor Υ : T →~T such that the image of Pi is an invertible object of ~T for any
i∈I. We write T [P⊗− 1
i |i∈I] for ~T .
Lemma A.6.1. LetT be a tensor category and let {(Pi,RPi)}i∈I be a commuting
family of central objects of T . Let C be another tensor category and Ψ : T → Ca
tensor functor. Assume that Ψ(Pi) is invertible for any i∈ I. Then the functor Ψ
factors throughT
Υ
−→T[P⊗− 1
i |i∈I]
Ψ ′
− − →Cwith a tensor functor Ψ′. Moreover, such
a Ψ′ is unique up to a unique isomorphism.
Proposition A.6.2. Let (T,⊗) be a tensor category and let {(Pi,RPi)}i∈I be a com-
muting family of central objects of T . Consider the following conditions.
(a)T is an abelian category.
(b)⊗ is an exact bifunctor.
(c) Any object of T has a ﬁnite length.
(d) If X is a simple object of T , then X⊗Pi is a simple object for any i∈I.
Set ~T =T [P⊗− 1
i |i∈I]. Then the following statements hold.
(i) If (T,⊗) satisﬁes (a) and (b), then ~T is an abelian category and the functor
Υ : T →~T is exact.
(ii) If (T,⊗) satisﬁes (a)–(d), then ( ~T,⊗) satisﬁes (a)–(c), and the functor Υ : T →
~T sends simple objects to simple objects. Conversely, every s imple object of ~T is
isomorphic to Υ(S)⊗Pα for some α∈ Z⊕I and a simple object S ofT .
For easy reference, we record the following lemma.
Lemma A.6.3. Let k be a ﬁeld and let C be a k-linear abelian category. Assume that
(a) any object of C has ﬁnite length,
(b) dim k HomC(S,S )<∞ for any simple object S inC.
Then we have dimk HomC(X,Y )<∞ for all X,Y ∈C .
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 75
