---
doc_id: arxiv-math-9909027v1
doc_title: "Planar Algebras, I"
section_id: sec-009-34-tensor-product
section_title: "Tensor product"
section_number: 3.4
pages: 79-80
source_pdf: 9909027v1.pdf
source_sha256: e6cd544cdc141d3b
toc_source: inferred
doc_brief: "Planar Algebras, I — We introduce a notion of planar algebra, the simplest example of which is a vector space of tensors, closed under planar contractions."
---
Let P 1 = ∪kP 1
k and P 2 = ∪kP 2
k be general planar algebras. We will
endow the ﬁltered algebra P 1 ⊗P 2 = ∪kP 1
k ⊗P 2
k with a general planar
algebra structure on the labelling set L = `
i≥1 P 1
i × P 2
i . Consider P 1 and
P 2 presented on themselves by Φ1 and Φ2 respectively. First deﬁne a linear
map L : P(L) →P(P1) ⊗P(P2) by L(T) = T1 ⊗T2 where T is a tangle
labelled by f : Boxes(T) →P1 × P2, Ti have the same unlabelled tangle as
T and they are labelled by f composed with the projection P1 × P2 →Pi,
i = 1, 2. This L is well deﬁned since the isotopy classes of labelled tangles
are a basis of P(L). Now deﬁne the presenting map ΦP1⊗P2 : P(L) →P1⊗P2
by
ΦP1⊗P2 = (Φ1 ⊗Φ2) ◦L .
This obviously gives a homomorphism of ﬁltered algebras. It is surjective
because we may consider the tangle
labelled by x × y for an arbitrary
79
pair (x, y) in P 1
k × P 2
k . This will be sent on to x ⊗y ∈P 1
k × P 2
k . Thus we
need only show the annular invariance of ker ΦP1⊗P2. But if A is an annular
tangle in A(L) then it is easy to see that L ◦πA = πA1 ⊗πA2 ◦L where A1
and A2 are the annular tangles having the same unlabelled tangle as A but
labelled by the ﬁrst and second components of the labels of A respectively.
So if
x ∈ker ∈ΦP1⊗P2 ,
ΦP1⊗P2πA(x) = Φ1 ⊗Φ2(πA1 ⊗πA2(L(x))) = πA1 ⊗πA2(Φ1 ⊗Φ2(L(x)))
= πA1 ⊗πA2(ΦP1⊗P2(x)) = 0
So P1 ⊗P2 is a general planar algebra.
It is clear that P1 ⊗P2 is connected iﬀboth P1 and P2 are and that
ZP1⊗P2 = ZP1ZP2 in the sense that a network labelled with P1 × P2 is the
same as two networks labelled with P1 and P2 respectively. Thus P1 ⊗P2
is a planar algebra if P1 and P2 are. Moreover, nondegeneracy, ∗structure,
positivity and sphericity are inherited by P1 ⊗P2 from P1 and P2. So the
tensor product of two C∗-planar algebras is a C∗-planar algebra.
Notes. (i) By representing elements of P1 and P2 by tangles, one may
think of the tensor product planar structure as being a copy of P1 and one of
P2 sitting in boxes on parallel planes, with no topological interaction between
them. This corresponds to presenting P1 ⊗P2 on the labelling set P(P1) ×
P(P2) in the obvious way.
(ii) It is clear that P1 ⊗P2 ≈P2 ⊗P1 as (general) planar algebras.
