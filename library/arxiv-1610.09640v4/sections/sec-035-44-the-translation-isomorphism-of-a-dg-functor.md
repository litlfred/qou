---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-035-44-the-translation-isomorphism-of-a-dg-functor
section_title: "The Translation Isomorphism of a DG Functor"
section_number: 4.4
pages: 84-85
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
belian categories M and N, and DG ringsA and B. The translation functor of the
DG category C(A, M) will be denoted here byTA,M. For an objectM∈C(A, M),
we have the little t operator
tM∈HomA,M
(
M, TA,M(M)
{−1
.
This is an isomorphism in the DG categoryC(A, M). Likewise for the DG category
C(B, N).
Deﬁnition 4.4.1.Let F : C(A, M)→C(B, N) be a DG functor. For an object
M∈C(A, M), let
τF,M :F (TA,M(M))→TB,N(F (M))
be the degree0 isomorphism
τF,M := tF(M)◦F (tM)−1
in C(B, N), called thetranslation isomorphismof the functorF at the objectM.
The isomorphismτF,M sits in the following commutative diagram
F (TA,M(M))
τF,M // TB,N(F (M))
F (M)
F(tM)
OO
tF(M)
66
of isomorphisms in the categoryC(B, N).
Proposition 4.4.2. τF,M is an isomorphism inCstr(B, N).
Proof. We know thatτF,M is an isomorphism inC(B, N). It suﬃces to prove that
bothτF,M and its inverseτ−1
F,M are strict morphisms. Now by Proposition 4.1.5,tM
and t−1
M are cocycles. Therefore,F (tM) and F (tM)−1 =F (t−1
M ) are cocycles. For
the same reason,tF(M) and t−1
F(M) are cocycles. ButτF,M = tF(M)◦F (tM)−1, and
τ−1
F,M =F (tM)◦t−1
F(M). □
Theorem 4.4.3.LetF : C(A, M)→C(B, N) be a DG functor. Then the collection
τF :={τF,M}M∈C(A,M)
is an isomorphism
τF :F◦TA,M
≃
− →TB,N◦F
of functors Cstr(A, M)→Cstr(B, N).
The slogan summarizing this theorem is “A DG functor commutes with transla-
tions”.
Proof. In view of Proposition 4.4.2, all we need to prove is thatτF is a morphism
of functors (i.e. it is a natural transformation).
Letφ:M0→M1 be a morphism inCstr(A, M). We must prove that the diagram
(F◦TA,M)(M0)
τF,M0 //
(F◦TA,M)(φ)

(TB,N◦F )(M0)
(TB,N◦F)(φ)

(F◦TA,M)(M1)
τF,M1 // (TB,N◦F )(M1)
84
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in Cstr(B, N) is commutative. This will be true if the next diagram
(F◦TA,M)(M0)
(F◦TA,M)(φ)

F (M0)
F(tM0)oo
tF(M0)
//
F(φ)

(TB,N◦F )(M0)
(TB,N◦F)(φ)

(F◦TA,M)(M1) F (M1)
F(tM1)oo
tF(M1)
// (TB,N◦F )(M1)
in C(B, N), whose horizontal arrows are isomorphisms, is commutative. For this to
be true, it is enough to prove that both squares in this diagram are commutative.
This is true by Theorem 4.1.8(2). □
Recall that the translationT and all its powers are DG functors. To ﬁnish this
subsection, we calculate their translation isomorphisms.
Proposition 4.4.4. For every integerk, the translation isomorphism of the DG
functor Tk is τTk = (−1)k·idTk+1, where idTk+1 is the identity automorphism of
the functor Tk+1.
Proof. By Deﬁnition 4.4.1 and Proposition 4.1.11(1), fork = 1 the formula is
τT,M = tT(M)◦T(tM)−1 =−idT2(M), where idT2(M) is the identity automorphism
of the DG moduleT2(M). HenceτT =−idT2. For other integersk the calculation
is similar. □
