---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT"
section_id: sec-007-invariance-under-m1
section_title: "Invariance under M1"
section_number: null
pages: 20-21
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
doc_brief: "TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invarian ts, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
and M3, we can transform an open book with any number of pages to one with
only one page (see Figure 20). Thus, it suﬃces to prove invariance u nder M1 in
this special case. Drawing the dual graph in the vicinity of the verte x, invariance
under M1 is equivalent to the following equality:
1
D2
∑
j,k ∈Irr(C)
djdk ϕ ϕ ∗
... ...
V1 Vn Vn V1
Xj
Xk
=
∑
i∈Irr(C)
di ϕ ϕ ∗
... ...
V1 Vn Vn V1
Xi
Note the normalizing factor 1
D2 which comes from the fact that we are removing a
vertex.
TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT 21
add edge to each page
− − − − − − − − − − − − − − →
add faces between new edges
− − − − − − − − − − − − − − − − − − →
remove all pages but one
− − − − − − − − − − − − − − − →
Figure 20. Decomposing an open book into a single page book
Using semisimplicity of C, it is easy to see that it suﬃces to show this equality
in the special case when V =V1 ⊗ · · · ⊗Vn is simple:
1
D2
∑
j,k ∈Irr(C)
djdk ϕ ϕ ∗
V V
Xj
Xk
=
∑
i∈Irr(C)
di ϕ ϕ ∗
V V
Xi
By Lemma 1.1, the right-hand side is equal to coev V : 1 →V ⊗V ∗. Since Hom( 1,V ⊗
V ∗) is one-dimensional, the left-hand side is also a multiple of coev V . Composing
it with the evaluation morphism ev V , we get
1
D2
∑
j,k
djdkN V jk
1 = 1
D2
∑
j,k
N V j
k∗ dkdj
= 1
D2
∑
j
(∑
k
N V j
k∗ dk
)
dj = 1
D2
∑
j
(dVdj)dj =dV,
which proves that the left-hand side is equal to coev V .
