---
doc_id: modularqholonomicmodules
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-008-22-an-algorithm-for-a-fundamental-matrix
section_title: "An algorithm for a fundamental matrix"
section_number: 2.2
pages: 13-14
source_pdf: modular.qholonomic.modules.pdf
source_sha256: 640303a68dd75453
toc_source: outline
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
---
obtain a fundamental matrix solution to a q-holonomic module given by Dreyfus [20] using
the q-Borel and the q-Laplace transform. Let us describe the main steps here.
• Choose a cyclic vector to present a q-holonomic module in the form of a linear q-diﬀerence
equation
r
X
j=0
ajσjf = 0
(53)
14
STAVROS GAROUFALIDIS AND CAMPBELL WHEELER
where f = f(t, q), (σf)(t, q) = f(qt, q) and aj(t, q) ∈Q(q)[t±1], with ar̸ = 0. The rest of the
algorithm depends on (53) alone.
• The lower Newton polygon of (53) is the lower convex hull of the points (j, v0(aj)) for
j = 0, . . . , r, where v0(p) denotes the minimum t-exponent of a Laurent polynomial p(t)
(with the convention that v0(0) = ∞). The boundary of the lower Newton polygon is a
ﬁnite sequence of edges with increasing slopes.
• For each edge of the lower Newton polygon, we replace our function by a ratio of theta
functions times a new function, so that the corresponding edge is now horizontal, and then
apply the Frobenius method to get t-formal power series solutions, once for each root of the
indicial polynomial of the edge. If κ is the slope of the edge and an integer, the solutions
have the form
θ(t; q)κ
∞
X
k=0
αk(q)tk θ(ρ−1t; q)
θ(t; q)
(54)
where ρ is determined by the roots of the indicial polynomial of the edge. A special feature
in the equations that we study is that the roots of the indicial polynomials are roots of unity
times a fractional power of q times a monomial in any additional variables.
• If a solution is not convergent at t = 0, apply a q-Borel transform, followed by an iterated
q-Laplace transform (deﬁned below), to construct a fundamental matrix U(t, q) of analytic
solutions at t = 0. The q-Borel and q-Laplace transforms preserve linear q-diﬀerence equa-
tions and change their Newton polygons by an aﬃne linear transformation.
• Repeat the above steps using the upper Newton polygon of (53), that is the upper convex
hull of the points (j, v∞(aj)) for j = 0, . . . , r, where v∞(p) denotes the maximum t-exponent
of a Laurent polynomial p(t) (with the convention that v∞(0) = −∞). Call the corresponding
fundamental matrix V (t, q).
The ratio M = V −1U is a matrix of elliptic functions. These functions depend on addi-
tional elliptic parameters that come from the q-Laplace transform, a feature of q-diﬀerence
equations which is absent in the world of linear diﬀerential equations. The connection prob-
lem, i.e., the determination of this matrix, is largely unsolved, with partial success for the
case of many q-hypergeometric diﬀerence equations; see Ohyama, Morita [55, 56, 57, 58].
