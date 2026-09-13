---
doc_id: arxiv-1304.0323v3
doc_title: "SYMMETRIC QUIVER HECKE ALGEBRAS"
section_id: sec-030-b1-serre-category
section_title: "B.1. Serre category"
section_number: null
pages: 79-81
source_pdf: 1304.0323v3.pdf
source_sha256: 92e2b9dc876e1a52
doc_brief: "SYMMETRIC QUIVER HECKE ALGEBRAS — Let J be a set of pairs consisting of good U ′ q(g)-modules and invertible elements in the base ﬁeld C(q)."
---
of an abelian category by a subcategory. For more details, see [ 33, § 4.3]. Let A be an
abelian category and let S be a Serre subcategory ofA ; i.e.,
(i)S is a full subcategory of A,
(ii)S is stable under taking subobjects, quotients and extensions, nam ely, for any
exact sequence 0 →X′→X→X′′→ 0 inA, the middle term X is inS if and
only if X′ and X′′ are inS.
For two objects X and Y ofA, we have a directed set
L(X,Y ) ={(X′,Y ′)|X′⊂X,Y ′⊂Y,X/X′∈S ,Y ′∈S}
80 S.-J. KANG, M. KASHIW ARA, M. KIM
with the order given by
(X′
1,Y ′
1)≤ (X′,Y ′)⇔X′⊂X′
1,Y ′
1⊂Y′.
If (X′
1,Y ′
1)≤ (X′,Y ′), we have a canonical homomorphism of abelian groups
HomA(X′
1,Y/Y ′
1)→ HomA(X′,Y/Y ′).
The quotient categoryA/S is deﬁned as follows:
(1) The objects of A/S are the same as the objects of A.
(2) For two objects X, Y ofA/S, the morphisms are given by
HomA/S(X,Y ) := lim −→
(X ′,Y ′)∈L(X,Y )
HomA(X′,Y/Y ′).
(3) We refer the reader to [ 33, § 4.3] for the deﬁnition of the composition HomA/S(X,Y )×
HomA/S(Y,Z )→ HomA/S(X,Z ) for X,Y,Z ∈ Ob(A/S).
Then we can deﬁne the functor Q :A→A /S.
Theorem B.1.1 ([33, § 4.3]). LetS be a Serre subcategory of an abelian category A.
Then the following statements hold.
(i) The quotient category A/S is abelian.
(ii) For an object X∈A ,Q(X)≃ 0 if and only if X∈S .
(iii) The functorQ :A→A /S is exact.
(iv) Every exact sequence in A/S is isomorphic to the image of an exact sequence in
A underQ.
(v) LetB be an abelian category and let H :A→B be an exact functor such that
H(X)≃ 0 for all X inS. Then H factors through A/S with an exact functor
H :A/S→B . Moreover, such an H is unique up to isomorphism.
(vi) An additive functor G :A/S→B is exact if and only if G◦Q :A→B is exact.
As for simple objects in A/S, we have the following proposition.
Proposition B.1.2. LetS be a Serre subcategory of an abelian category A.
(i) If X is simple in A and X /∈S , then Q(X) is simple in A/S.
(ii) Assume that every object in A has ﬁnite length. Then every simple object Y in
A/S is isomorphic to Q(X) for a simple object X inA.
(iii) If X1 and X2 are simple objects of A andQ(X1)≃Q (X2)⁄≃0 inA/S, then
X1≃X2 inA.
Since the proofs are elementary, we omit them.
The following lemma is also elementary.
Lemma B.1.3. Let k be a ﬁeld and let A be a k-linear abelian category. Assume the
following conditions:
(a) dim k HomA(X,Y )<∞ for any X,Y ∈A ,
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 81
(b) any object of A has ﬁnite length.
Then, for any Serre subcategoryS ofA, the quotient categoryA/S is a k-linear abelian
category satisfying (a) and (b).
The following proposition is easy to verify.
Proposition B.1.4. LetA be an abelian tensor category such that ⊗ is an exact
bifunctor and let S be a Serre subcategory of A. Assume the following condition:
for any X∈A and Y∈S , X⊗Y and Y⊗X belong toS.(B.1.1)
ThenA/S has a structure of a tensor category such that Q :A→A /S is a tensor
functor.
