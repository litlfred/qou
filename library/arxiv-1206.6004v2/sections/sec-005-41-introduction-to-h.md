---
doc_id: arxiv-1206.6004v2
doc_title: ""
section_id: sec-005-41-introduction-to-h
section_title: "Introduction to H"
section_number: 4.1
pages: 6-9
source_pdf: 1206.6004v2.pdf
source_sha256: b490672c8c3557dd
doc_brief: "Bring’s Curve: its Period Matrix and the Vector of Riemann Constants ⋆ — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
duplicate_of: "sigma12-065"
---
Riera and Rodr´ ıguez, in [17], give Bring’s curve as a quotient,H, of the hyperbolic disc. They
then proceed to calculate a period matrix taking account of the symmetries of the curve.
The essential features of the model can be seen in Fig. 2. The surface is seen to be a 20-
gon with edges identified as shown in the table below the figure. (We refer, for example, to
the identified edges 2 and 9 as 2 /9.) This leads to the polygon’s vertices falling into three
equivalence classes, also annotated in the figure. Naturally, this surface has genus 4.
For future calculations it will also be very useful to know the conformal structure (or equiva-
lently, the local holomorphic coordinate) about the points P1, P2 and P3. This can be recon-
structed quite easily from Fig. 2. For example, start near P1 in the bottom right quadrant
on edge 2/9. Make a small arc around P1 proceeding anticlockwise and you will next reach
Bring’s Curve: its Period Matrix and the Vector of Riemann Constants 7
y ∼
√
2x−1/2
y ∼ 21/3x1/3
y ∼ −
√
2x−1/2
y ∼ x−3
y ∼ −x3/4
y ∼ x3/4
γ− γ+ γ0
x = 0
x = ∞
Figure 1. Real paths on the Hulek–Craig curve as a branched cover of P1.
edge 1/14. Repeating at edge 14 tells us that we next meet 6 /13. If this procedure is continued
we obtain Fig. 3.
The polygon can be tiled by 120 double triangles (one can take a sector of the central pentagon
as a fundamental domain). Now consider the automorphism group. Let d be a rotation of π
2
about a vertex of the central pentagon andc be a rotation ofπ about the midpoint of an adjacent
pentagon edge. Then clearly c2 =d4 = 1. But it is also easy to see that cd is a rotation of 2π
5
about the centre and hence ( cd)5 = 1. The rotations c and d are thus the classical generators
of S5 and this describes the entire automorphism group of Bring’s curve.
Riera and Rodr´ ıguez give the homology basis for this model by prescribing which edges of
the polygon to traverse. We are going to construct an equivalent basis for the HK curve by
understanding an isomorphism
f : H→
{
(x,y,z )∈ C3 :C(x,y,z ) = 0
}
(4.1)
well enough to determine the precise values to which each edge of the polygon in Fig. 2 maps.
Once this is achieved, converting the homology basis will be a purely mechanical affair as
illustrated in [2] for Klein’s curve. Along the way we will gain some understanding of how f
acts on the automorphism group by push-forwards.
4.2 Riera and Rodr´ ıguez basis
We start by recapitulating the hyperbolic basis of interest. Riera and Rodr´ ıguez begin with a
simple non-canonical basis. They first define
α1 = 1 + 2, α 2 = 3 + 4
(in edge traversal notation, see [16, 17]) and then act on these cycles by rotations of 2πk
5 to
obtain their initial basis. So essentially
αi = (2i− 1) + (2i).
8 H.W. Braden and T.P. Northover
C
P1
P2
P3
P2
P1
P2
P3
P2
P1 P2
P3
P2
P1
P2
P3
P2
P1
P2
P3P2
R
1
2
3
4
5
6
7
8
910
11
12
13
14
15
16
17
18
19 20
Edge identifications
1 ↔ 14 5 ↔ 18 9 ↔ 2 13 ↔ 6 17 ↔ 10
3 ↔ 12 7 ↔ 16 11 ↔ 20 15 ↔ 4 19 ↔ 8
Figure 2. Riera and Rodr´ ıguez hyperbolic model,H, of Bring’s curve.
Next they specify (by fiat) a matrix which transforms these αi into a canonical basis and
proceed to derive further basis change to make use of the symmetries. The end result is the
following basis-change matrix (implicit in [17])


1 0 0 0 −2 0 1 0
1 −1 0 −1 −1 1 1 1
1 −1 0 0 −1 2 1 −1
0 −1 0 0 1 2 0 0
1 −1 1 0 −1 1 −1 −1
1 −1 1 −1 0 0 −1 1
1 −1 1 −1 0 1 0 1
0 −1 0 −1 1 1 1 2


, (4.2)
which sends the initialα1,...,α 8 homology basis to another{ai, bi}4
i=1, that is not only canonical
but behaves well with respect to the symmetry group of the curve. Now the symmetries relate
the periods Aij =
∫
ai
vj andBij =
∫
bi
vj (for any basis of holomorphic differentials vi). As
a consequence, the period matrixτ =BA−1 can be written as (1.1), whereτ0≈− 0.5+0.185576i
is defined in terms of Klein’s j-invariants5 by
j(τ0) =−293× 5
25 , j (5τ0) =−25
2 . (4.3)
5Riera and Rodr´ ıguez swap these two equations. However, we believe this to be a typographical error.
Bring’s Curve: its Period Matrix and the Vector of Riemann Constants 9
P1
1/14
6/13
5/18 10/17
2/9
P3
3/12
11/20
8/19 7/16
4/15
P2
4/15
1/14
11/20
10/7
7/16 6/13 3/12
2/9
8/19
5/18
Figure 3. Conformal structure of P1, P2 and P3.
