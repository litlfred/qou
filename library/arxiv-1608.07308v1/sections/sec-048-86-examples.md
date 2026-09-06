---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-048-86-examples
section_title: "Examples"
section_number: 8.6
pages: 64-66
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
describe the homology of categoriﬁed projectors on two and three strands.
Example 8.7. For theS2 projector, we have
Y =
(
0 0
1 0
)
.
The commutation relation implies thatX is of the form
X =
(
u1 0
u2 u1
)
.
One has deg(u1) =q, deg(u2) =q/t, so the Poincar´e series equals
P ( ˚AT ) = 1
(1−q)(1−q/t).
Example 8.8. For the Λ2 projector, we have
X =
(
x1 0
1 x2
)
,Y =
(
0 0
y21 0
)
,
and the commutation relation (x1−x2)y21 = 0. One has deg(x1) = deg(x2) = q, deg(y21) =
t/q, so the Poincar´e series equals
P ( ˚AT ) = 1−t
(1−q)2(1−t/q) = 1
(1−q)2 + t/q
(1−q)(1−t/q).
Example 8.9. For theS3 projector, we have
X =


x1 0 0
x2 x1 0
x3 x2 x1

,Y =


0 0 0
1 0 0
0 1 0

,
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY 65
One has deg(x1) =q, deg(x2) =q/t, degx3 =q/t2, so the Poincar´e series equals
P ( ˚AT ) = 1
(1−q)(1−q/t)(1−q/t2).
More generally, for theSn projector, we have
P ( ˚AT ) =
n∏
i=1
(1−qt1−i)−1.
Example 8.10. For the Λ3 projector, we have
X =


x1 0 0
1 x2 0
0 1 x3

,Y =


0 0 0
y21 0 0
y31 y32 0

,
and the commutation relations (x1−x2)y21 = (x2−x3)y32 = 0 and
y21−y32 = (x1−x3)y31.
Note that one can eliminate y32 using the last equation. One has deg(x1) = deg( x2) =
deg(x3) =q, deg(y21) = deg(y32) =t/q, deg(y31) =t/q2, so the Poincar´e series equals
P ( ˚AT ) = (1−t)2
(1−q)3(1−q/t)(1−q/t2).
More generally, for the Λn projector, we have
˚AT = C[x1,...,x n,yi,j]i>j
yi,j(xi−xj)− (yi−1,j−yi,j+1)
and
P ( ˚AT ) = (1−t)n−1
(1−q)n
n−1∏
i=1
(1−qt−i)−1.
(which can also be seen directly from Proposition 8.12.)
Example 8.11. For the hook-shaped projector with (z1,z 2,z 3) = (1,t,q ), we have
X =


x1 0 0
x21 x1 0
1 x32 x3

,Y =


0 0 0
1 0 0
0 y32 0

,
with commutation relations
x32 =x21y32, (x1−x3)y32 = 0,
In this case deg(x1) = deg(x3) = q, deg(x21) = q/t, deg(x32) = t, deg(y32) = t2/q, so the
Poincar´e series equals
P ( ˚AT ) = (1−t2)
(1−q)2(1−q/t)(1−t2/q).
For the other hook-shaped projector we have (z1,z 2,z 3) = (1,q,t ), so
X =


x1 0 0
1 x2 0
0 x32 x3

,Y =


0 0 0
y21 0 0
1 y32 0

,
with commutation relations (x1−x2)y21 = (x2−x3)y32 = 0 and
x1−x3 +y32 =x32y21.
66 EUGENE GORSKY, ANDREI NEGUT , , AND JACOB RASMUSSEN
In this case deg(x1) = deg(x2) = deg(x3) = q, deg(x32) = q2/t, deg(y21) = t/q, deg(y32) =
q, so the Poincar´e series equals
P ( ˚AT ) = (1−t)(1−q2)
(1−q)3(1−t/q)(1−q2/t).
