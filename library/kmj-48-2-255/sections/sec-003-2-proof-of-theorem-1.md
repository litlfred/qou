---
doc_id: kmj-48-2-255
doc_title: "A formula for the colored Jones polynomial of 2-bridge knots"
section_id: sec-003-2-proof-of-theorem-1
section_title: "Proof of Theorem 1"
section_number: 2
pages: 3-5
source_pdf: KMJ-48-2-255.pdf
source_sha256: 720279042c6d762b
doc_brief: "A formula for the colored Jones polynomial of 2-bridge knots — We derive a formula for the colored Jones polynomial of 2-bridge knots."
---
Firstly, we review a result in [5]. Let L be a knot in S3. We consider a 1-tangle
L′ whose closure is L. We assume that L′ is presented as a tangle diagram D in
258 Toshie Takata
generic position with respect to the height function with the end points at the top
and at the bottom. We orient D from the top to the bottom. Let c denote the
number of the crossings in a diagram D. There are eight crossing types given by
the orientations on the two strands and the sign of the crossing, two cap types,
and two cup types by the orientations on the strand in a tangle diagram. The two
crossoing types (1) and (2), the cap type (i), and the cup type (ii) as in Figure 2
are called leftpointing. We construct an enhanced Gauss diagram G for D, which is
a circle containing the combinatorial data which encodes D. We number crossings
by j = 1, · · · , c and denote by σj the sign of the j-th crossing. We mark the base
K -2
K 2
K 2
K 2
K -2 K -2
(1) (2) (i) (ii)
Figure 2.
A B
1b-
1a-
2b-
2a-
1c-
1d-
2c-
2d-
CD
1b + 1c + 2b + 2c +
2a + 2d + 1a + 1d +
K 2
K-2
K 2
K2
K2K2 K-2K-2
K-2
K
K-2 K-2
2
Figure 3.
point on a circle, which corresponds to the end at the top of D. As going around the
circle clockwise from the base point, with tracing the tangle strand according to its
orientation, we mark 2 c points indexed by i = 1, · · · , 2c, which correspond to points
passing crossings on the tangle strand. So, exactly two points of these 2 c points
except the base point correspond to one crossing, and one comes from the underpass
A Formula for the Colored Jones Polynomial of 2-Bridge Knots 259
and the other from the overpass. Join these two points on the circle by an oriented
chord from overpass to underpass, and assign the sign of the corresponding crossing.
Each i-th point on the circle is assigned with a pair ( j(i), εi), simply denoted by
j(i)εi, where j(i) is the number of the passing crossing, and εi is 1 for an overpass
and −1 for an underpass. Moreover, the circle is marked with blobs K ±2 placed
on the leftpointing crossings and cups and caps as in Figure 2. The result is an
enhanced Gauss diagram. For example, the enhanced Gauss diagram for Figure 1
is shown in Figure 3, where oriented chords are not drawn. We denote by i1, · · · , ib
the position of the blobs K ±2, where the a-th blob is placed between the ia-th and
(ia + 1)-th positions on the circle, with K 2δa .
We put
qj = 1
2
∑
i>j+
σi − 1
2
∑
i>j−
σi − 1
2
c∑
j=1
σj,
d(l) =
c∑
j=1
qjlj − 1
2
∑
a
δa − 1
2 σj,
C 0(l) = −d(l) −
∑
a
k≤ia
δaεklk − 1
2
∑
j
σjlj − 1
2
∑
i
k<i
σiεiliεklk
+
∑
j
σj(
∑
i<j−
εili)(
∑
k<j+
εklk).
Theorem 2([5]). A formula for the n-colored Jones polynomial of a 0-framed knot
L0 is given by
JL0(n) (2)
=
∞∑
lj =0
j=0,...,c
qCn(l)
c∏
j=1
{
s(j) + lj
lj
}
σj
(qσj (n−s(j)−1) − 1) · · · (qσj (n−s(j)−lj ) − 1),
where s(j) = − ∑
i<j− εilj(i), and C n(l) = d(l)n + C 0(l). Here i < j − means i < i 0
for i0 such that j = j(i0) and εi0 = −1.
We apply this formula to the 2-bridge knot S(p, t).
From Schubert’s normal form, we get a 1-tangle diagram as in Figure 4 and
