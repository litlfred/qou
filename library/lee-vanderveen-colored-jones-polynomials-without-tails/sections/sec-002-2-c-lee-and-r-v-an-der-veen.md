---
doc_id: lee-vanderveen-colored-jones-polynomials-without-tails
doc_title: "COLORED JONES POLYNOMIALS WITHOUT TAILS"
section_id: sec-002-2-c-lee-and-r-v-an-der-veen
section_title: "C. LEE AND R. V AN DER VEEN"
section_number: 2
pages: 2-2
source_pdf: lee-vanderveen-colored-jones-polynomials-without-tails.pdf
source_sha256: fcc45aebd34e25dc
doc_brief: "COLORED JONES POLYNOMIALS WITHOUT TAILS — We exhibit an in nite family of knots with the property that the rst coecient of the n-colored Jones polynomial grows linearly with n."
---
2. Colored Jones polynomial
The colored Jones polynomial is usually considered as a knot invariant but from our point of view it
is more natural to consider its extension to knotted framed graphs. A good thing about this deﬁnition
of the colored Jones polynomial is that it is less dependent on knot diagrams and a little more eﬃcient
for computations. The technical reason behind its success is that we diagonalize the R-matrix.
De
nition 2.1. Knotted trivalent graphs (KTG)
(1) A framed graph is a 1-dimensional simplicial complex Γ together with an embedding Γ →Σ
of Γ into a surface with boundary Σ as a spine.
(2) A coloring of Γ is a map  :E(Γ)→N.
(3) A Knotted Trivalent Graph (KTG) is a trivalent framed graph embedded (as a surface) into
R3, considered up to isotopy.
Framed knots and links are special cases of KTGs. We prefer the more general set of KTGs here
because there are natural 3-dimensional operations that can be used to generate the whole theory
from the tetrahedron.
Figure 2. Operations on Knotted Trivalent Graphs: framing change Fe
±, unzip Ue
and triangle move Aw applied to an edge e and vertex w shown in the middle.
More precisely it was shown by D. Thurston [15] and [17] that the following three moves suﬃce to
generate any KTG from the planar theta graph. The ﬁrst operation Fe
±cuts the surface Σ transversal
to an edge, rotates one side by  and reglues. This is called framing change or connected sum with a
M¨ obius band. The second operation is called unzip,Ue. It doubles a chosen edge along its framing,
deletes its end-vertices and joins the result as shown. The ﬁnal move is called Aw and expands a
vertexw into a triangle. All three moves are as shown in Figure 2.
Deﬁne [k] = v2k−v−2k
v2−v−2 and [k]! = [1][2]::: [k] for k∈N and [k]! = 0 if k =∈N. Let

a1 +a2 +···+ar
a1;a 2;:::;a r

= [a1 +a2 +···+ar]!
[a1]!::: [ar]!
The building blocks of the Jones polynomial are the following Laurent polynomials. For each we
explicitly state the term of maximal degree for later use.
f(a) =i−av
−a(a+2)
