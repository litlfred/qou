---
doc_id: arxiv-q-alg-9709040v1
doc_title: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I"
section_id: sec-037-5-conﬁguration-spaces-and-their-compactiﬁcations
section_title: "Conﬁguration spaces and their compactiﬁcations"
section_number: 5
pages: 18-19
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
doc_brief: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I — 83 sections: Front matter; Introduction; Deformation quantization"
---
5.1. Deﬁnitions
Let n,m be non-negative integers satisfying the inequality 2 n +m≥ 2. We denote by Conf n,m the
product of the conﬁguration space of the upper half-plane wi th the conﬁguration space of the real line:
Conf n,m ={(p1,...,p n;q1,...,q m)|pi∈H, qj∈ R, pi1⁄=pi2 for i1⁄=i2, q j1⁄=qj2 for j1⁄=j2} .
Conf n,m is a smooth manifold of dimension 2 n +m. The group G(1) of holomorphic transformations
of CP 1 preserving the upper half-plane and the point ∞, acts on Conf n,m . This group is a 2-dimensional
connected Lie group, isomorphic to the group of orientation -preserving aﬃne transformations of the real line:
G(1) ={z↦→az +b|a,b∈ R, a> 0} .
It follows from the condition 2 n +m≥ 2 that the action of G(1) onConf n,m is free. The quotient space
Cn,m := Conf n,m/G(1) is a manifold of dimension 2 n +m− 2. If P = (p1,...,p n;q1,...,q m) is a point of
Conf n,m then we denote by [ P ] the corresponding point of Cn,m .
Analogously, we introduce simpler spaces Conf n and Cn for any n≥ 2:
Conf n :={(p1,...,p n)|pi∈ C, pi⁄=pj for i⁄=j},
Cn =Conf n/G(2), dim(Cn) = 2n− 3,
18
where G(2) is a 3-dimensional Lie group,
G(2) ={z↦→az +b|a∈ R,b∈ C, a> 0} .
We will construct compactiﬁcations Cn,m ofCn,m ( and compactiﬁcations Cn ofCn) which are smooth
manifolds with corners.
We remind that a manifold with corners (of dimension d) is deﬁned analogously to a usual manifold
with boundary, with the only diﬀerence that the manifold wit h corners looks locally as an open part of closed
simplicial cone ( R≥0)d. For example, the closed hypercube [0 , 1]d is a manifold with corners. There is a
natural smooth stratiﬁcation by faces of any manifold with c orners.
First of all, we give one of possible formal deﬁnitions of the compactiﬁcation Cn,m in the case n≥ 1.
With any point [( p1,...,p n;q1,...,q m)] of Cn,m we associate a collection of 2 n(n− 1) + nm angles with
values in R/2πZ:
(
Arg(pi−pj),Arg (pi−pj),Arg (pi−qj)
)
.
It is easy to see that we obtain an embedding of Cn,m into the torus ( R/2πZ)2n(n−1)+nm. The space Cn,m
is deﬁned as the compactiﬁcation of the image of this embeddi ng. Analogously, the compactiﬁcation C n is
obtained using angles Arg(pi−pj).
One can show that open strata of Cn,m are naturally isomorphic to products of manifolds of type Cn′,m ′
and Cn′ . In the next subsection we will describe explicitly Cn,m as a manifold with corners.
There is a natural action of the permutation group Σ n on Cn, and also of Σ n× Σ m on Cn,m . This
gives us a possibility to deﬁne spaces CA andCA,B for ﬁnite sets A,B such that #A≥ 2 or 2#A + #B≥ 2
respectively. If A′֒→A and B′֒→B are inclusions of sets then there are natural ﬁbrations (for getting maps)
CA−→CA′ and CA,B−→CA′,B ′.
