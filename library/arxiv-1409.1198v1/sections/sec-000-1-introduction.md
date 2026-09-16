---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a high er categorical level."
---
1.1. What is categoriﬁcation? Categoriﬁcation is perhaps best explained by deﬁning decategoriﬁc a-
tion. Quite broadly, decategoriﬁcation is a rigorously deﬁned procedure for forgetting information and
reducing the complexity of a given mathematical structure. A bit mo re formally, a decategoriﬁcation
can be thought of as a map
(n − 1)-category n-categoryD/d111/d111
for simplifying an n-categorical structure into an ( n − 1)-categorical structure.
Categorifcation asks the question “given a speciﬁc ( n−1)-categoryA, ﬁnd an n-categoryB such that
A ∼= D(B)”. In this case, we say that A is the decategoriﬁcation of B and that B categoriﬁes A. Often
it is the case that the existence of a categoriﬁcation of A reveals new insights and hidden structure
that could not be seen without knowledge of B. For more introductory material on categoriﬁcation
see [2, 35, 38, 58].
An example when n = 1 can be obtained by considering the 1-category V ect
/CZ
of ﬁnite dimensional
/CZ -vector spaces. We can deﬁne a decategoriﬁcation
/C6
V ect
/CZ
D/d111/d111
from the 1-category V ect
/CZ
to the 0-category, or set, of natural numbers /C6 by setting D = dim.
In this example a natural number n is categoriﬁed by any vector space V with dim(V ) = n. This
categoriﬁcation lifts much of the structure of natural numbers, i.e. dim(V ⊕W ) = dim(V ) + dim(W )
and dim(V ⊗W ) = dim(V ) × dim(W ).
Generalizing the previous example, let gV ect
/CZ
denote the category of graded vector spaces V =
⊕k∈ /CI
Vk. One way to decategorify a graded vector space is to take its grad ed dimension
/C6 [q,q ]−1 gV ect
/CZ
D=dimq/d111/d111
where
dimqV :=
∑
k∈ /CI
qk dimVk.
Date: September 4, 2014.
1
2 ANNA BELIAKOV A, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. LA UDA
This example can be extended another direction by considering the c ategory Kom( gV ect
/CZ
) of com-
plexes of graded vector spaces. The graded Euler characteristic gives rise to a decategoriﬁcation map
taking a bounded complex of graded vector spaces into a Laurent p olynomialχ(C•) = ∑
i(−1)i dimqCi ∈
/CI [q,q −1]. While these examples may seem somewhat trivial, these elementary id eas resurface in more
sophisticated categoriﬁcations discussed below.
Several important observations are in order. A categoriﬁcation n eed not be unique, in the sense
that there may be two diﬀerent n-categories B and B′ with A = D(B) = D(B′). Furthermore, there
may be several diﬀerent ways to simplify a given n-categorical structure into an ( n − 1)-categorical
structure. That is to say, it may be possible to decategorify a given structure in more than one way. In
this article we will focus on two ways of decategorifying an (additive) category to produce an abelian
group. These are the “Grothendieck group” and “trace”.
