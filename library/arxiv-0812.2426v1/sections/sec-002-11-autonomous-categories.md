---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-002-11-autonomous-categories
section_title: "Autonomous categories"
section_number: 1.1
pages: 3-4
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
toc_source: inferred
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
provide
examples of Hopf monads. If fact, any monoidal adjunction between autonomous
categories gives rise to a Hopf monad. It turns out that much of the theory of
ﬁnite-dimensional Hopf algebras extends to Hopf monads, see [BV07]. In Section 3,
we recall a few results on Hopf monads.
The whole point of introducing Hopf monads here is that they provide an al-
gebraic interpretation of the center construction [BV08].
If C is a centralizable
autonomous category, meaning that the coend Z(X) =
R Y ∈C ∨Y ⊗X ⊗Y exists
for any object X of C, then Z is a quasitriangular Hopf monad on C and the cen-
ter Z(C) coincides, as a braided category, with the category of Z-modules in C. In
addition, Drinfeld’s double construction extends naturally to Hopf monads. This
theory provides a description of the coend of Z(C). In Section 4, we recall a few
facts on the double of Hopf monads.
In Section 5, we apply the above results to spherical fusion categories. Firstly,
we obtain a generalization of M¨uger’s theorem on the modularity of the center of
a spherical fusion category C to the case where dim C is not necessarily invertible
and k is any commutative ring. Denoting by {Vi}i∈I a (ﬁnite) representative family
of scalar objects of C, we get:
Z(X) =
M
i∈I
∨Vi ⊗X ⊗Vi,
Moreover Z(C) is centralizable and dim Z(C) = (dim C)2. The underlying object of
the coend of Z(C) is:
C =
M
i,j∈I
∨Vi ⊗∨Vj ⊗∨∨Vi ⊗Vj ,
and all structural morphisms of C (including its integral Λ:
1 →C) can be written
down explicitly in C. Furthermore, Z(C) is always modular. When k is an alge-
braically closed ﬁeld and dim C is invertible, then Z(C) is a fusion category and
so we recover M¨uger’s theorem. However, when dim C is not invertible, Z(C) is a
non-semisimple ribbon category. Nevertheless, in this case, the version τZ(C)(M; Λ)
of the Lyubashenko invariant is still deﬁned and computable in terms of C.
1. Conventions and notations
1.1. Autonomous categories. Monoidal categories are assumed to be strict.
Recall that a duality in a monoidal category (C, ⊗,
1) is a quadruple (X, Y, e, d),
where X, Y are objects of C, e: X ⊗Y →
1 (the evaluation) and c:
1 →Y ⊗X
(the coevaluation) are morphisms in C, such that:
(e ⊗idX)(idX ⊗c) = idX
and
(idY ⊗e)(c ⊗idY ) = idY .
Then (X, e, c) is a left dual of Y , and (Y, e, c) is a right dual of X.
A left autonomous category is a monoidal category for which every object X
admits a left dual (∨X, evX, coevX). Likewise, a right autonomous category is a
monoidal category for which every object X admits a right dual (X∨, eevX, g
coevX).
4
A. BRUGUI`ERES AND A. VIRELIZIER
An autonomous category is a monoidal category which is left and right au-
tonomous. Note that in an autonomous category, there are canonical isomorphisms:
∨(X∨) ∼= X,
∨(X ⊗Y ) ∼= ∨Y ⊗∨X,
∨
1 ∼=
1,
(∨X)
∨∼= X,
(X ⊗Y )∨∼= Y ∨⊗X∨,
1∨∼=
1.
Subsequently, in formulae, we will often abstain (by abuse) from writing down these
isomorphisms.
