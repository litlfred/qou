---
doc_id: sigma12-065
doc_title: "Bring's Curve: its Period Matrix and the Vector of Riemann Constants"
section_id: sec-009-41-introduction-to-h
section_title: "Introduction to H"
section_number: 4.1
pages: 6-7
source_pdf: sigma12-065.pdf
source_sha256: a6e0e0da5cc5ff9b
toc_source: outline
doc_brief: "Bring's Curve: its Period Matrix and the Vector of Riemann Constants — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
---
Introduction to H
Riera and Rodr´ıguez, in [17], give Bring’s curve as a quotient, H, of the hyperbolic disc. They
then proceed to calculate a period matrix taking account of the symmetries of the curve.
The essential features of the model can be seen in Fig. 2. The surface is seen to be a 20-
gon with edges identified as shown in the table below the figure. (We refer, for example, to
the identified edges 2 and 9 as 2/9.)
This leads to the polygon’s vertices falling into three
equivalence classes, also annotated in the figure. Naturally, this surface has genus 4.
For future calculations it will also be very useful to know the conformal structure (or equiva-
lently, the local holomorphic coordinate) about the points P1, P2 and P3. This can be recon-
structed quite easily from Fig. 2. For example, start near P1 in the bottom right quadrant
on edge 2/9. Make a small arc around P1 proceeding anticlockwise and you will next reach
y ∼
√
2x−1/2
y ∼21/3x1/3
y ∼−
√
2x−1/2
y ∼x−3
y ∼−x3/4
y ∼x3/4
γ−
γ+
γ0
x = 0
x = ∞
Figure 1. Real paths on the Hulek–Craig curve as a branched cover of P1.
edge 1/14. Repeating at edge 14 tells us that we next meet 6/13. If this procedure is continued
we obtain Fig. 3.
The polygon can be tiled by 120 double triangles (one can take a sector of the central pentagon
as a fundamental domain). Now consider the automorphism group. Let d be a rotation of π
2
about a vertex of the central pentagon and c be a rotation of π about the midpoint of an adjacent
pentagon edge. Then clearly c2 = d4 = 1. But it is also easy to see that cd is a rotation of 2π
5
about the centre and hence (cd)5 = 1. The rotations c and d are thus the classical generators
of S5 and this describes the entire automorphism group of Bring’s curve.
Riera and Rodr´ıguez give the homology basis for this model by prescribing which edges of
the polygon to traverse. We are going to construct an equivalent basis for the HK curve by
understanding an isomorphism
f : H →

(x, y, z) ∈C3 : C(x, y, z) = 0
	
(4.1)
well enough to determine the precise values to which each edge of the polygon in Fig. 2 maps.
Once this is achieved, converting the homology basis will be a purely mechanical affair as
illustrated in [2] for Klein’s curve. Along the way we will gain some understanding of how f
acts on the automorphism group by push-forwards.
4.2
