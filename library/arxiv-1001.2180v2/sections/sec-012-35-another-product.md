---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-012-35-another-product
section_title: "Another product"
section_number: 3.5
pages: 11-12
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
[
Śni06]), which will be useful in section 5. It is enough to give the value of the product of two elements
of the basis Σρ:
Σµ • Σν = Σµ∪ν.
If we look at the description of the classical product on the Σµ given at the previous paragraph, taking
the product • consists in keeping in the result the terms indexed by famili es of disjoint indices. This
remark can be generalized to expression of the kind:
X G
i1,...,ir =
∑
∀j, A j ∈A(n,ij )
G(ai,j )∈G
C(A1) · · · C(Ar),
where G(ai,j ) is, as in the previous paragraph, the graph describing which of the ai,j’s are equal and G
a collection of admissible graphs. The following lemma will be useful in subsection 5.1:
Lemma 8. The disjoint product of two such expressions is given by:
X G
i1,...,ir • X G′
i′
1,...,i′
r
= X G⊔G ′
i1,...,ir ,i′
1,...,i′
r
,
where G ⊔ G ′ is the collection of all graphs obtained by the disjoint unio n of a graph of G and a graph of
G′. In other words, the disjoint product of two expressions as ab ove is obtained by keeping in the usual
product only terms such that the two families of indices are di sjoint.
Proof. As in the previous paragraph, the summation over sequences o f indices corresponding to a given
graph gives a term Σρ. Therefore:
X G
i1,...,ir =
∑
G∈G
Σρ(G)
12 V ALENTIN FÉRAY AND PIERRE-LOÏC MÉLIOT
and we have
X G
i1,...,ir • X G′
i′
1,...,i′
r
=
∑
G∈G
∑
G′∈G′
Σρ(G),ρ(G′);
= X G⊔G ′
i1,...,ir ,i′
1,...,i′
r
. □
