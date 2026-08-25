---
doc_id: arxiv-1010.5321v3
doc_title: "Formulas on hyperbolic volume"
section_id: sec-003-21-coordinate-system-based-on-paracycles-horocyc
section_title: "Coordinate system based on paracycles (horocycles)"
section_number: 2.1
pages: 2-3
source_pdf: 1010.5321v3.pdf
source_sha256: c6bb20926b1f291f
doc_brief: "Formulas on hyperbolic volume — This paper collects some important formulas on hyperbolic volume."
---
P
T
p
t
Figure 1: coordinate system based on paracycles.
Consider a parasphere of dimension n − 1 and its pencil of rays of parallel lines. The last
coordinate axis let be one of these rays, the origin will be th e intersection of this line by the
parasphere. The further axes are pairwise orthogonal parac ycles. The coordinates of P are
(ξ1,ξ 2, · · ·,ξ n)T, where the last coordinate is the distance of P and the parasphere, while the
further coordinates are the coordinates of the orthogonal p rojectionT with respect to the Carte-
sian coordinate system giving by the mentioned paracycles.
In Rn we can correspond to P a point p (see on Fig.1) with ordinary Cartesian coordinates:
(x1,x 2, · · ·,x n)T =
(
e− ξn
k ξ1,e − ξn
k ξ2, · · ·,e − ξn
k ξn−1,ξ n
)T
.
By deﬁnition let the volume of a Jordan measurable set D be
v(D) := vn
∫
D⋆
dx1 · · ·dxn,
where D⋆ is the image of D by the above mapping and vn is a constant which we will choose
later. Our ﬁrst formula on the volume is:
v(D) = vn
∫
D
e−(n−1) ξn
k dξ1 · · ·dξn,
depending on the coordinates of the points of D, with the given system of coordinates. Let now
the domain D = [0,a 1] × · · · × [0,a n−1] be a sector of parallel segments of length an based on a
2
coordinate-brick of the corresponding parasphere, then
v(D) = vn
a1∫
0
· · ·
an∫
0
e−(n−1) ξn
k dξn · · ·dξ1 = kvn
n − 1
n−1∏
i=1
ai
[
−e−(n−1) an
k +e0
]
=
= kvn
n − 1
n−1∏
i=1
ai[1 −e−(n−1) an
k ].
If an tends to inﬁnity and ai = 1 for i = 1 · · · (n − 1), then the volume is equal to kvn
n−1 . Note
that J.Bolyai and N.I.Lobachevski used the value vn = 1 so in their calculations the value of the
volume is independent from the dimension but depends on the c onstantk which determine the
measure of the curvature of the space. We follows them we will determine the constant vn such
that for every ﬁxed k the value of the measure of a thin layer divided by its height t ends to the
value of the measure of the limit ﬁgure of lower dimension. No w the limit:
lim
an→∞
v(D)
an
= kvn
n − 1
n−1∏
i=1
ai lim
an→∞
[1 −e−(n−1) an
k ]
an
=vn
n−1∏
i=1
ai,
is equal to vn−1
n−1∏
i=1
ai showing that 1 = v1 =v2 =... =vn =... .
Thusvn = 1 as it used by earlier. On the other hand if for a ﬁxed n the number k tends to
inﬁnity the volume of a body tends to the euclidean volume of t he corresponding euclidean body.
In every dimension n we also have a k for which the corresponding hyperbolic n-space contains
a natural body with unit volume, if k is equal to n − 1 then the volume of the paraspheric sector
based on a unit cube of volume 1 is also 1.
So with respect to paracycle coordinate system our volume fu nction by deﬁnition is
v(D) =
∫
D
e−(n−1) ξn
k dξ1 · · · dξn.
