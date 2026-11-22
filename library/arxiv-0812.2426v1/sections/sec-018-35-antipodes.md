---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-018-35-antipodes
section_title: "Antipodes"
section_number: 3.5
pages: 12-13
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
toc_source: inferred
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
If C is left autonomous, then a left antipode for T is a natural transformation
sl = {sl
X : T (∨T (X)) →∨X}X∈Ob(C) satisfying:
T0T (evX)T (∨ηX ⊗idX) = evT (X)(sl
T (X)T (∨µX) ⊗idT (X))T2(∨T (X), X);
(ηX ⊗id∨X)coevXT0 = (µX ⊗sl
X)T2(T (X), ∨T (X))T (coevT (X)).
Likewise, if C is right autonomous, then a right antipode for T is a natural
transformation sr = {sr
X : T (T (X)∨) →X∨}X∈Ob(C) satisfying:
T0T ( eevX)T (idX ⊗η∨
X) = eevT (X)(idT (X) ⊗sr
T (X)T (µ∨
X))T2(X, T (X)∨);
(idX∨⊗ηX) g
coevXT0 = (sr
X ⊗µX)T2(T (X)∨, T (X))T ( g
coevT (X)).
As in the classical case, left and right antipodes are ‘anti-(co)multiplicative’,
see [BV07, Theorem 3.7].
Note that if a left (resp. right) antipode exists, then it is unique. Furthermore,
when they exist, the left antipode sl and the right antipode sr are ‘inverse’ to
each other in the sense that idT (X) = sr
∨T (X)T ((sl
X)
∨) = sl
T (X)∨T (∨(sr
X)) for any
object X of C.
3This is not standard terminology: pairs (M, r) are usually called T-algebras in the literature.
However pairs (M, r) are considered here as the analogues of modules over an algebra, and so the
term ‘algebra’ would be awkward in this context.
4This notion of bimonad coincides exactly with the notion of ‘Hopf monad’ introduced in
[Moe02].
However, by analogy with the notions of bialgebra and Hopf algebra, we prefer to
reserve the term ‘Hopf monad’ for bimonads with antipodes (see Section 3.6)
CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS
