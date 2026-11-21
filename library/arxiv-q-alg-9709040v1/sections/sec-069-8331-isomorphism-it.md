---
doc_id: arxiv-q-alg-9709040v1
doc_title: "Deformation quantization of Poisson manifolds"
section_id: sec-069-8331-isomorphism-it
section_title: "Isomorphism IT"
section_number: 8.3.3.1
pages: 41-43
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
toc_source: inferred
doc_brief: "Deformation quantization of Poisson manifolds — 75 sections: Front matter; Plans; Star-products"
---
The isomorphism IT is given by the sum over terms corresponding to admissible graphs Γ with no
vertices of the second type, one special vertex v of the ﬁrst type such that no edge start at v, and such that
at any other vertex start two edges and ends no more than one edge. Vertex v is the marked vertex where
we put an element of Sym(g) considered as an element of tangent cohomology. At other vertices we put the
Poisson-Kirillov bi-vector ﬁeld on g∗, i.e. the tensor of commutator operation in g. As the result we get
0-diﬀerential operator, i.e. an element of algebra Sym(g).
It is easy to see that any such graph is isomorphic to a union of copies of “wheels” Whn, n ≥2:
.
.
1
2
. . .
v
n
.
.
.
.
.
with identiﬁed central vertex v. The following picture shows a typical graph:
.
v
. . .
.
. .
. .
In the integration we may assume that the point corresponding to v is ﬁxed, say that it is i · 1 + 0 ∈H,
because group G(1) acts simply transitively on H. First of all, the operator Sym(g)−→Sym(g) corresponding
41
to the individual wheel Whn is the diﬀerential operator on g∗with constant coeﬃcients, and it corresponds
to the polynomial γ 7→T race (ad(γ)n) on g. The operator corresponding to the joint of several wheels is the
product of operators associated with individual wheels. Also, the integral corresponding to the joint is the
product of integrals. Thus, with the help of symmetry factors, we get that the total operator is equal to the
exponent of the sum of operators associated with wheels Whn, n ≥2 with weights equal to corresponding
integrals. By the symmetry argument used several times before (z 7→−z), we see that integrals corresponding
to wheels with odd n vanish. We proved the ﬁrst statement of our theorem.
Q.E.D.
8.3.3.2. Isomorphism Ialg ◦IP BW
The second case, for the operator Ialg ◦IP BW , is a bit more tricky. Let us write a formula for this map:
Ialg ◦IP BW : γn 7→γ ⋆γ ⋆γ . . . ⋆γ
(n copies of γ) .
This formula deﬁnes the map unambiguously because elements γn, γ ∈g, n ≥0 generate Sym(g) as a
vector space.
In order to multiply several (say, m, where m ≥2) elements of the quantized algebra we should put
these elements at m ﬁxed points in increasing order on R and take the sum over all possible graphs with
m vertices of the second type of corresponding expressions with appropriate weights. The result does not
depend on the position of ﬁxed points on R because the star-product is associative. Moreover, if we calculate
a power of a given element with respect to the ⋆-product, we can put all these points in arbitrary order.
It follows that we can take an average over conﬁgurations of m points on R where each point is random,
distributed independently from other points, with certain probability density on R. We choose a probability
distribution on R with a smooth symmetric (under transformation x 7→−x) density ρ(x). We assume also
that ρ(x)dx is the restriction to R ≃C1,1 of a smooth 1-form on C1,1 ≃{−∞}⊔R⊔{+∞}. With probability
1 our m points will be pairwise distinct. One can check easily that the interchanging of order of integration
(i.e. for the taking mean value from the probability theory side, and for the integration of diﬀerential forms
over conﬁguration spaces) is valid operation in our case.
The conclusion is that the m-th power of an element of quantized algebra can be calculated as a sum
over all graphs with m vertices of the second type, with weights equal to integrals over conﬁguration spaces
where we integrate products of forms dφ and 1-forms ρ(xi)dxi where xi are points moving along R.
The basic element of pictures in our case are “wheels without axles”:
. .
.
.
.
.
.
.
2
.
. .
.
n
1
and the Λ-graph (which gives 0 by symmetry reasons):
42
.
.
.
The typical total picture is something like (with m = 10):
. . . . . . .
.
. . .
.
.
.
.
.
.
.
Again, it is clear from all this that the operator Ialg ◦IP BW is a diﬀerential operator with constant
coeﬃcients on Sym(g), equal to the exponent of the sum of operators corresponding to individual wheels.
These operators are again proportional to operators associated with power series on g
γ−→T race (ad(γ)n) .
By the same symmetry reasons as above we see that integrals corresponding to odd n vanish. The second
part of the theorem is proven.
