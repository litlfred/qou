---
doc_id: arxiv-1304.0323v3
doc_title: "SYMMETRIC QUIVER HECKE ALGEBRAS R-MATRICES OF QUANTUM AFFINE ALGEBRAS"
section_id: sec-026-a7-graded-case
section_title: "A.7. Graded case"
section_number: null
pages: 75-78
source_pdf: 1304.0323v3.pdf
source_sha256: 92e2b9dc876e1a52
doc_brief: "SYMMETRIC QUIVER HECKE ALGEBRAS R-MATRICES OF QUANTUM AFFINE ALGEBRAS — Let J be a set of pairs consisting of good U ′ q(g)-modules and invertible elements in the base ﬁeld C(q)."
---
L-graded ifT has a decomposition T = ⨁
λ∈LTλ such that ⊗ induces a bifunctor
Tλ×Tµ→T λ+µ for any λ,µ∈L and that 1∈T 0.
Let{(Pi,RPi)}i∈I be a commuting family of central objects of T such that Pi∈T λi
for λi∈ L,i ∈ I. Let ℓ : Z⊕I→ L be a homomorphism given by ℓ(ei) = λi (i∈ I).
Hence Pα belongs toTℓ(α) for any α∈ Z⊕I
≥0.
Now we assume that ℓ : Z⊕I→ L is injective. We will deﬁne a tensor category T′
and a tensor functor
Ω :T →T′
such that Ω( Pi)≃ 1 for i∈I. We take Ob(T′) = Ob(T ) and
HomT ′(X,Y ) = lim −→
α,β∈Z⊕I
≥0,
λ+ℓ(α)=µ+ℓ(β)
HomT (X⊗Pα,Y ⊗Pβ)
forX∈T λ andY∈T µ. If λ−µ is not in the image of ℓ : Z⊕I→L, then we understand
that HomT ′(X,Y ) = 0. The tensor product of X,Y ∈T ′ is the same as the one in T .
Then·⊗· becomes a bifunctor on T′ as in the case of ~T =T [P⊗− 1
i |i∈I].
Note that the category T′ has a decomposition T′ = ⨁
a∈Coker(ℓ)
T′
a . We write T′ =
T [Pi≃ 1|i∈I].
Lemma A.7.1. LetT be an abelian L-graded tensor category and {(Pi,RPi)}i∈I be a
commuting family of central objects in T as above. Assume that the functor T ∋X↦→
Pi⊗X is an exact functor for all i∈I. Then the following statements hold.
(i) The functor Ω :T →T[Pi≃ 1|i∈I] is exact.
(ii) Ω( Pi) is isomorphic to 1 for any i∈I.
(iii) Every exact sequence in T [Pi≃ 1|i∈I] is isomorphic to the image of an exact
sequence inT .
(iv) The functor Ω is decomposed into
T
Υ
−→T[P⊗− 1
i |i∈I]
Ξ
− →T[Pi≃ 1|i∈I],
where Ξ(X,α ) = X for X∈T ,α∈ Z⊕I.
We have the similar results to the one in Proposition A.6.2 for the category T′ =
T [Pi≃ 1|i∈I] and the functor Ω : T →T′.
Proposition A.7.2. Let (T,⊗) and{(Pi,RPi)}i∈I be as in Lemma A.7.1. Consider
the following conditions.
(a)T is an abelian category.
(b)⊗ is an exact bifunctor.
(c) Every object of T has ﬁnite length.
(d) If X is a simple object of T , then X⊗Pi is a simple object for all i∈I.
76 S.-J. KANG, M. KASHIW ARA, M. KIM
SetT′ =T [Pi≃ 1|i∈I]. Then the following statements hold.
(i) If (T,⊗) satisﬁes (a) and (b), then T′ is an abelian category and the functor
Ω :T →T′ is exact.
(ii) If (T,⊗) satisﬁes (a)–(d), then (T′,⊗) satisﬁes (a)–(c), and the functor Ω :T →
T′ sends simple objects to simple objects. Conversely, every s imple object of T′
is the image of a simple object of T under Ω .
The following proposition gives a characterization of T [Pi≃ 1|i∈I].
Proposition A.7.3. LetT be a tensor category and let {(Pi,RPi)}i∈I be a commuting
family of central objects of T as in Lemma
A.7.1. LetC be another tensor category and
Ψ : T →C a tensor functor. Assume that, for any i∈I, there exists an isomorphism
gi : Ψ( Pi)∼−→1 such that the following diagrams are commutative for any X∈T :
Ψ(Pi⊗X)
Ψ(RPi (X))
/d15/d15
∼ /d47/d47 Ψ(Pi)⊗ Ψ(X)
gi⊗ Ψ(X) /d47/d47 1⊗ Ψ(X)
/d40/d40◗◗◗◗◗◗◗◗◗◗◗◗◗
Ψ(X⊗Pi)
∼ /d47/d47 Ψ(X)⊗ Ψ(Pi)
Ψ(X)⊗gi /d47/d47 Ψ(X)⊗ 1 /d47/d47 Ψ(X).
(A.7.1)
Then Ψ factors as T
Ω
− →T[Pi≃ 1|i∈I]
Ψ ′
− − →Cwith a tensor functor Ψ′. Moreover,
such a Ψ′ is unique up to a unique isomorphism.
Proof. Let ({Pα}α∈Z⊕I
≥0
,{fα,β}α,β∈Z⊕I
≥0
) be as in §
A.4. Taking X = Pj in ( A.7.1), the
diagram
Ψ(Pi⊗Pj)
∼ /d47/d47
Ψ(RPi (Pj ))
/d15/d15
Ψ(Pi)⊗ Ψ(Pj)
gi⊗gj /d47/d47 1⊗ 1
id
/d15/d15
Ψ(Pj⊗Pi)
∼ /d47/d47 Ψ(Pj)⊗ Ψ(Pi)
gj⊗gi /d47/d47 1⊗ 1
is commutative. Hence, Lemma A.4.2 implies that there exists a family of morphisms
gα : Ψ( Pα)∼−→1 (α∈ Z⊕I
≥0) such that the following diagram commutes:
Ψ(Pα⊗Pβ)
∼ /d47/d47
Ψ(fα,β)
/d15/d15
Ψ(Pα)⊗ Ψ(Pβ)
gα⊗gβ /d47/d47 1⊗ 1
∼
/d15/d15
Ψ(Pα+β)
gα+β /d47/d47 1.
(A.7.2)
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 77
We can also check that the diagram
Ψ(Pα⊗X)
Ψ(RP α (X))
/d15/d15
∼ /d47/d47 Ψ(Pα)⊗ Ψ(X)
gα⊗ Ψ(X) /d47/d47 1⊗ Ψ(X)
/d40/d40◗◗◗◗◗◗◗◗◗◗◗◗◗
Ψ(X⊗Pα)
∼ /d47/d47 Ψ(X)⊗ Ψ(Pα)
Ψ(X)⊗gα /d47/d47 Ψ(X)⊗ 1 /d47/d47 Ψ(X)
(A.7.3)
is commutative for any X∈T and α∈ Z⊕I
≥0.
We shall deﬁne the functor Ψ ′ :T′ :=T [Pi ≃ 1| i∈ I]−−→ Cas follows. For
X∈T , we set Ψ ′(X) = Ψ( X). For X∈T λ and Y ∈T µ, we deﬁne Hom T ′(X,Y )→
HomC(Ψ′(X), Ψ′(Y )) as the inductive limit of
HomT (X⊗Pα,Y ⊗Pβ)→ HomC
(
Ψ(X⊗Pα), Ψ(Y⊗Pβ)
)
≃ HomC
(
Ψ(X)⊗ Ψ(Pα), Ψ(Y )⊗ Ψ(Pβ)
) ∼−→HomC
(
Ψ(X)⊗ 1, Ψ(Y )⊗ 1
)
.
Here the limit is taken over α,β ∈ Z⊕I
≥0 such that λ +ℓ(α) = µ +ℓ(β). It is easy to
verify that Ψ ′ is a well-deﬁned functor. For X,Y ∈T , we have an isomorphism
Ψ′(X⊗Y ) = Ψ( X⊗Y )∼−→Ψ(X)⊗ Ψ(Y ) = Ψ ′(X)⊗ Ψ′(Y ).
Let us show that it is an isomorphism of functors. In order to see th is, it is enough
to show that for X ∈ Tλ, Y ∈ Tµ X′ ∈ Tλ′, Y′ ∈ Tµ′, and f ∈ HomT ′(X,X′),
g∈ HomT ′(Y,Y ′), the diagram
Ψ′(X⊗Y )
Ψ ′(f⊗g) /d47/d47
∼
/d15/d15
Ψ′(X′⊗Y′)
∼
/d15/d15
Ψ′(X)⊗ Ψ′(Y )
Ψ ′(f )⊗ Ψ ′(g) /d47/d47 Ψ′(X′)⊗ Ψ′(Y′)
(A.7.4)
is commutative.
Assume that f is given by ˜f ∈ HomT (X⊗Pα,X′⊗Pα′
) and g is given by ˜g ∈
HomT (Y⊗Pβ,Y ′⊗Pβ′
). We have two sequences of isomorphisms
Ψ(X⊗Pα⊗Y⊗Pβ) ∼−−−−→RP α (Y ) Ψ(X⊗Y⊗Pα⊗Pβ)∼−→Ψ(X⊗Y⊗Pα+β)
∼−→Ψ(X⊗Y )⊗ Ψ(Pα+β)∼−→Ψ(X⊗Y )
and
Ψ(X⊗Pα⊗Y⊗Pβ)∼−→Ψ(X)⊗ Ψ(Pα)⊗ Ψ(Y )⊗ Ψ(Pβ)
∼−→Ψ(X)⊗ 1⊗ Ψ(Y )⊗ 1∼−→Ψ(X)⊗ Ψ(Y ).
78 S.-J. KANG, M. KASHIW ARA, M. KIM
We denote the ﬁrst composition by ϕ : Ψ( X⊗Pα⊗Y⊗Pβ) ∼−→Ψ′(X⊗Y ) and the
second one by ψ : Ψ( X⊗Pα⊗Y⊗Pβ)∼−→Ψ′(X)⊗ Ψ′(Y ).
Similarly, we have two isomorphismsϕ′ : Ψ( X′⊗Pα′
⊗Y′⊗Pβ′
)∼−→Ψ′(X′⊗Y′) and
ψ′ : Ψ( X′⊗Pα′
⊗Y′⊗Pβ′
)∼−→Ψ′(X′)⊗ Ψ′(Y′). We can easily see that the following
diagram is commutative:
Ψ′(X⊗Y )
Ψ ′(f⊗g)
/d15/d15
Ψ(X⊗Pα⊗Y⊗Pβ)
∼
ψ
/d47/d47∼
ϕ
/d111/d111
Ψ( ˜f⊗ ˜g)
/d15/d15
Ψ′(X)⊗ Ψ′(Y )
Ψ ′(f )⊗ Ψ ′(g)
/d15/d15
Ψ′(X′⊗Y′) Ψ( X′⊗Pα′
⊗Y′⊗Pβ′
)
∼
ψ′
/d47/d47∼
ϕ′
/d111/d111 Ψ′(X′)⊗ Ψ′(Y′).
On the other hand, ( A.7.2) and ( A.7.3) imply that ψ coincides with the composition
Ψ(X⊗Pα⊗Y⊗Pβ) ∼−→ϕ Ψ(X⊗Y )∼−→Ψ(X)⊗ Ψ(Y ), and a similar relation holds for
ϕ′ and ψ′. Hence we obtain the commutativity of ( A.7.4). □
Lemma A.7.4. Under the conditions in the above proposition, we further as sume that
C is an abelian category and Ψ is an exact functor. Then the functor Ψ′ :T [Pi≃ 1|
i∈I]→C is exact.
Remark A.7.5. The commutativity of ( A.7.1) does not depend on the choice of an
isomorphism gi (i∈I). Indeed, in a tensor category T , the diagram
X⊗ 1
∼ /d47/d47
X⊗ϕ
/d15/d15
X
∼ /d47/d47 1⊗X
ϕ⊗X
/d15/d15
X⊗ 1
∼ /d47/d47X
∼ /d47/d47 1⊗X
is commutative for any ϕ∈ EndT (1).
