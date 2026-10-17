---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
toc_source: outline
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polynomial and the boundary slopes of knots under the operation of cabling."
---
1.1. The Slope Conjecture. For a knot K ⊂S3, let n(K) denote a tubular neighbor-
hood of K and let MK := S3 \ n(K) denote the exterior of K. Let ⟨µ, λ⟩be the canonical
meridian–longitude basis of H1(∂n(K)). An element a/b ∈Q ∪{1/0} is called a boundary
slope of K if there is a properly embedded essential surface (S, ∂S) ⊂(MK, ∂n(K)), such
that ∂S represents aµ + bλ ∈H1(∂n(K)). Hatcher showed that every knot K ⊂S3 has
ﬁnitely many boundary slopes [15]. We will use bsK to denote the set of boundary slopes
of K.
For a positive integer n, let JK(n) ∈Z[v±1/2] be the n-th colored Jones polynomial of
K with framing 0 [18, 27], normalized so that
Junknot(n) = vn/2 −v−n/2
v1/2 −v−1/2 .
Here v = A−4, where A is the variable in the Kauﬀman bracket [20].
For a sequence {xn}, let {xn}′ denote the set of its cluster points. Let d+[JK(n)] denote
the highest degree of JK(n) in v, and let d−[JK(n)] denote the lowest degree. Elements of
September 8, 2015.
E. K. was partially supported in part by NSF grants DMS–1105843 and DMS–1404754.
1
2
the sets
jsK :=

4n−2d+[JK(n)]
	′
and
js∗
K :=

4n−2d−[JK(n)]
	′
are called Jones slopes of K. Garoufalidis [9] showed that every knot has ﬁnitely many
Jones slopes. Furthermore, he formulated the following conjecture and he veriﬁed it for
alternating knots, non-alternating knots with up to nine crossings, torus knots, and for
the family (−2, 3, p) of 3-string pretzel knots [10].
Conjecture 1.1 (Slope Conjecture). For every knot K ⊂S3 we have
(jsK ∪js∗
K) ⊂bsK.
Futer, Kalfagianni and Purcell [4] veriﬁed the conjecture for adequate knots (see Deﬁ-
nition 3.5 for terminology). The works of Garoufalidis and Dunﬁeld [3] and Garoufalidis
and van der Veen [11] veriﬁed the conjecture for a certain 2-parameter family of closed
3-braids, called 2-fusion knots. More recently, Lee and van der Veen [23] have proved the
conjecture for several more 3-string pretzel knots.
In this paper we study the behavior of the boundary slopes and the Jones slopes of
knots under the operation of cabling and prove the Slope Conjecture for cables of several
classes of knots. We also formulate, and verify for several classes of knots, conjectures
providing topological interpretations of the linear terms of the degree of the colored Jones
polynomial (Conjectures 1.6 and 5.1). To state our results we need some preparation.
