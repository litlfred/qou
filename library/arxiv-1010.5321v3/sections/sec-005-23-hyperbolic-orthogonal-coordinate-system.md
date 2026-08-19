---
doc_id: arxiv-1010.5321v3
doc_title: "Formulas on hyperbolic volume ∗ ´A.G.Horv´ ath Department of Geometry"
section_id: sec-005-23-hyperbolic-orthogonal-coordinate-system
section_title: "Hyperbolic orthogonal coordinate system"
section_number: 2.3
pages: 4-5
source_pdf: 1010.5321v3.pdf
source_sha256: c6bb20926b1f291f
doc_brief: "Formulas on hyperbolic volume ∗ Á.G.Horváth Department of Geometry — This paper collects some important formulas on hyperbolic volume."
---
Put an orthogonal system of axes to paracycle coordinate sys tem such that, the new half-axes
let the tangent half-lines at the origin of the old one. (We ca n see it on Fig.3.) To determine
the new coordinates of the point P we project P orthogonally to the hyperplane spanned by the
axes x1,x 2, · · ·,x n−2,x n. The getting point is Pn−1. Then we project orthogonally Pn−1 onto
the (n − 2)-space spanned by x1,x 2, · · ·,x n−3,x n. The new point is Pn−2. Now the ( n − 1)th
coordinate is the distance of P and Pn−1, the ( n − 2)th is the distance of Pn−1 and Pn−2 and
so on ... In the last step we get the nth coordinate which is the distance of the point P1 from
the origin O. Since the connection between the distance 2 d of two points of a paracycle and the
P
P
P
n-1
n-2
x
x
x
1
n-1
nxx
xn-1
n-2
n
Figure 3: Coordinate system based on orthogonal axes.
arclength of the connecting paracycle arc 2 s is
s =k sinhd
k
thus the distance z of the respective halving points can be calculated as:
z =k ln coshd
k.
Now elementary calculation shows that the connection betwe en the coordinates with respect to
the two system of coordinates is:
ξn−1 = e
ξn
k k sinhxn−1
k
ξn−2 = e
ξn
k +ln cosh
xn−1
k k sinhxn−2
k
.
.
.
ξ1 = e
ξn
k +ln cosh
xn−1
k +···+ln cosh x2
k k sinhx1
k
xn = ξn +k ln coshxn−1
k + · · · +k ln coshx2
k +k ln coshx1
k .
From this we get a new one, corresponding point (ξ1,ξ 2, · · ·,ξ n)T ∈ Hn to point (u1, · · ·un)T ∈
Rn as in our ﬁrst calculation. The corresponding system of equa tion is:
4
u1 = k coshx2
k · · · coshxn−1
k sinhx1
k
.
.
.
un−1 = k sinhxn−1
k
un = xn −k ln coshx1
k − · · · −k ln coshxn−1
k
The Jacobian of this transformation is
(
coshx1
k
)(
coshx2
k
)2
· · ·
(
coshxn−1
k
)n−1
,
and we get our third formula on the volume:
v(D) =
∫
D
(
coshxn−1
k
)n−1
· · ·
(
coshx2
k
)2(
coshx1
k
)
dx1 · · ·dxn.
Here we use hyperbolic orthogonal coordinates.
