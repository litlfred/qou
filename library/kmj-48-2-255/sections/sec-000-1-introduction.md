---
doc_id: kmj-48-2-255
doc_title: "A Formula for the Colored Jones Polynomial of 2-Bridge Knots Toshie Takata"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: KMJ-48-2-255.pdf
source_sha256: 720279042c6d762b
doc_brief: "A Formula for the Colored Jones Polynomial of 2-Bridge Knots Toshie Takata — We derive a formula for the colored Jones polynomial of 2-bridge knots."
---
For a positive integer n, the n-colored Jones polynomial is a Laurent polyno-
mial invariant in q of a knot colored with n-dimensional irreducible representation
of Uq(sl2). We denote by JK(n) the n-colored Jones polynomial of a knot K, which
is normalized so that the colored Jones polynomial of the trivial knot is 1. Then,
JK (2) coincides with the original Jones polynomial of a knot K deﬁned by V. F.
R. Jones [3]. K. Habiro [2] and T. T. Q. Le gave explicit formulas for the n-colored
Jones polynomials of the trefoil knot and the ﬁgure eight knot. Moreover, a formula
for the colored Jones polynomials of twist knots was given by G. Masbaum [7], using
skein theory.
In this paper, we give a formula for the colored Jones polynomial of the 2-bridge
knot S(p, t), using a formula obtained by R. Lawrence and O. Ron in [5]. As an
application of our formula, we obtain a relation between the degree of the colored
Jones polynomial and the crossing number for the 2-bridge knots S(4p + 1, 2p + 1)
and S(4p − 1, 2p − 1).
Let p and t be coprime odd integers with p > t > 1. We denote by S(p, t)
the 2-bridge knot of type ( p, t) using Schubert notation. We explain how to draw
a diagram of the 2-bridge knot S(p, t)(see [1], [4]). Drawn two disjoint vertical
segments w1 = AB and w2 = CD , divide each segments into p segments, and
number from 0 to 2 p − 1 in both sides of the dividing points of each segment as
pictured in Figure 1. The points B and D are numbered 0, and the points A and
C numbered p. Next draw two disjoint simple curves v1 from B to C and v2 from
D to A, which underpass the segments w1 and w2. Along the curve v1, one starts
Received June 29, 2006.
2000 Mathematics Subject Classiﬁcation: 57M27.
Key words and phrases: Knots, Jones polynomial.
This research is partially supported by Grant-in-Aid for Scientiﬁc Research (C)
255
256 Toshie Takata
from 0, i.e. B of the segments w1, and meets w2 at t, and next meets w1 at 2 t,
and then meets w2 at 3 t. This is to be repeated until one reaches p (= C) of w2.
Similarly, along the curve v2, one starts from 0(= D) of w2, and meets w1 at t,
and next meets w2 at 2 t, and then meets w1 at 3 t. This is to be repeated until one
reaches p (= A) of w1. Here we take it mod 2 p. This regular projection is called
Schubert’s normal form. For example, Schubert’s normal form for the S(5, 3) (the
ﬁgure eight knot) is as in Figure 1.
0
1
2
3
4
5
6
7
8
9
0
1
2
3
4
5
6
7
8
9
S(5,3)
A
B
C
D
Figure 1.
We will prepare with some notations. Let us put p′ = p − 1
2 . For 1 ≤ j ≤ p′,
deﬁne integers r(j) so that r(j) ≡ (2j − 1)t mod 2 p and −p < r (j) < p . We put
σj := r(j)
|r(j)| , r′(j) := |r(j)| + 1
2 and ir′(j) = j. Note that σj = ( −1)[(2j−1)t/p],
where [ x] denotes the greatest integer less than or equal to x. For an integer i,
sign(i) is the sign of i. We put m = (m1, · · · , mp′ ), m0 = 0. We will also deﬁne for
σ = ±1
(qσ)k = (qσ − 1)((qσ)2 − 1) · · · ((qσ)k − 1),
{
n
m
}
σ
= (qσ)n
(qσ)m(qσ)n−m
.
We obtain
Theorem 1. A formula for the n-colored Jones polynomial of the 2-bridge knot
A Formula for the Colored Jones Polynomial of 2-Bridge Knots 257
S(p, t) is given by
(1) JS(p,t)(n) =
∑
0≤mj−1≤mj ≤n−1
qa(m)n+b1(m)+b2(m) X(m),
where
a(m) = − 1
2
p′
∑
j=1


p′
∑
k=r′(j)
(σik + σip′+1−k )

 (mj − mj−1) − 1
2
p′−1∑
j=1
(σj+1 + σp′+1−j)mj
− 1
