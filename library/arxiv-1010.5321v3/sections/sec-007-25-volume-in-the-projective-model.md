---
doc_id: arxiv-1010.5321v3
doc_title: "Formulas on hyperbolic volume"
section_id: sec-007-25-volume-in-the-projective-model
section_title: "Volume in the projective model"
section_number: 2.5
pages: 6-6
source_pdf: 1010.5321v3.pdf
source_sha256: c6bb20926b1f291f
doc_brief: "Formulas on hyperbolic volume — This paper collects some important formulas on hyperbolic volume."
---
At the origin of the projective (Kayley-Clein) model we cons ider a Cartesian system of coor-
dinates. Regarding the factor k we assume that the radius of the sphere is k. The considered
system is an orthogonal coordinate system both of the embedd ing Euclidean and the modeled
hyperbolic space.
Rn
x
X
x
X
x X
1
1
2
2
n n
P
k th n =Rn
O
r_
k
Figure 5: Coordinates in the Cayley-Klein model
We connect the hyperbolic spherical coordinates and the euc lidean spherical ones by the
system of equations:
rn =k tanh−1Rn
k , φ i =θi, i = 1, · · ·,n − 1.
Since the Jacobian is 1
1 −
(Rn
k
)2,
and
(
sinhrn
k
)n−1
=
(
sinh
(
1
2 ln 1 + Rn
k
1 − Rn
k
))n−1
=


Rn
k√
1 −
(Rn
k
)2


n−1
the volume is:
v(D) =
∫
D
Rn−1
n
√
1 −
(Rn
k
)2n+1 sinn−2θn−1 · · ·sinθ2dθ1 · · ·dθn−1dRn.
Transforming it into the usual Cartesian coordinates ( X1, · · ·,X n) the new formula is:
v(D) =
∫
D
1
(
1 −
( n∑
i=1
(
Xi
k
)2))n+1
2
dX1 · · ·dXn−1dXn.
