---
doc_id: arxiv-math-0410233v4
doc_title: "Cusp shapes under cone deformation"
section_id: sec-020-64-example-2bridge-knots
section_title: "Example: 2–bridge knots"
section_number: 6.4
pages: 41-44
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
doc_brief: "Cusp shapes under cone deformation — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp sh ape."
---
there be at least 116 crossings per twist region was based on t he worst
case analysis. This came from Proposition 6.5, in which we sh owed that in
the worst possible case, the normalized length of a slope was at least the
square root of the number of crossings. When we are dealing wi th particular
classes of knots, we can often make signiﬁcantly better esti mates, and reduce
the number of crossings required. In this section, we presen t a particular
example of such a class of knots: 2–bridge knots.
We will determine the circle packing obtained from the proof of Theorem
6.1 for a 2–bridge knot. A 2–bridge knot with an even number of twist
regions will have a corresponding augmented link L of the form of Figure
14, except possibly with single crossings added at some cros sing circles. The
picture for an odd number of twist regions is similar.
In any case, the link will correspond to a trivalent graph Γ of the form
shown in Figure 15. Note each region of the graph complement g ives a circle
in the circle packing, with tangencies across edges. Thus ea ch circle will be
42 JESSICA S. PURCELL
· · ·
· · ·
· · ·
· · ·
Figure 14. Augmented link of a 2–bridge knot with an even
number of twist regions, and an even number of crossings per
region.
D
B1
C1
C2
· · ·
· · ·
· · ·
· · ·
A
Cn−2
B2
Cn−3
Figure 15. Trivalent graph associated with a 2–bridge knot.
D
A
B1 C1
C2
.
.
.
Cn−1B2
Figure 16. Circle packing associated with a 2–bridge knot.
tangent to the circles corresponding to regions A and D. The circle packing
associated with this graph is of the form in Figure 16.
Recall that the shape of cusps can be determined by analyzing the rect-
angles we get from taking points of tangency of the circles in Figure 16 to
inﬁnity. In particular, we are interested in the cusp shapes which correspond
to crossing circles in the link L. The rectangles tiling these cusps come from
CUSP SHAPES UNDER CONE DEFORMATION 43
the tangencies of circle A with certain of the Bi and Ci, and from tangen-
cies of D with certain of the Bi and Ci. Thus we ﬁnd the general shape of
rectangles of this form.
When we take a point of tangency between A and Bi to inﬁnity, i = 1
or 2, the two circles tangent to both A and Bi are D and a Cj. These are
tangent to each other. Thus our rectangle in this case is a squ are. Similarly
for points of tangency between D and Bi.
A crossing circle coming from one of these points of tangency will therefore
be tiled by two squares, with a longitude running across two s haded sides.
Then the slope si along which Dehn ﬁlling is performed will have normalized
length
√
1 + c2
i /
√
2. Note this is larger than I(0.6624), implying that the
results of Theorem 1.8 apply, provided ci ≥ 16. It is larger than I(1.0),
implying the results of Corollary 6.7 hold, when ci ≥ 17. Thus the number
of crossings in our theorem has gone from 116 to 16, and 145 to 1 7.
When we take a point of tangency between A and Ci, or between D and
Ci to inﬁnity, we get a 1 by 2 rectangle. This is because the circl es A and
Ci are tangent to two distinct circles Ci−1 and Ci+1, or possibly a Bi, which
are each tangent to D. Since D is also tangent to A and Ci, in the picture
at inﬁnity we have two parallel lines, A and Ci, with three full sized circles
tangent to each other and also to the lines A and Ci.
In this case, the crossing circle is tiled by two 1 by 2 rectang les, stacked
to form a square. The slope si will have normalized length
√
4 + c2
i /
√
4.
It will be larger than I(0.6624) provided ci ≥ 22, and larger than I(1.0)
provided ci ≥ 24.
We can also make improvements on the initial normalized heig ht, i.e. the
value h(X) of Theorem 1.4. To compute h(X), we determine the shape
of the rectangles tiling the cusp corresponding to the knot s trand. These
include all rectangles obtained by taking a point of tangenc y of the circle
packing of Figure 16 to inﬁnity, except those tangencies cor responding to
crossing circle cusps.
Each circle tangency of the form C2k tangent to D will give a rectangle
on the knot strand cusp. Similarly, those tangencies of circ les C2k+1 tangent
to A will give rectangles on the knot strand cusp. As we saw above, these
rectangles will each have dimensions 1 by 2. The side of lengt h 2 will con-
tribute to the height. There will be ( n − 2) of these rectangles, since each
Cj contributes one. Thus these rectangles contribute 2 n − 4 to the height.
Each circle tangency Ci tangent to Ci+1 also gives a rectangle on the
knot strand cusp, as do the tangencies B1 with C1 and Cn−2 with B2. Each
of these rectangles is a square, contributing 1 to the height , and there are
(n − 1) such rectangles.
The tangencies of B1 and D and of B2 and A (or D if n is odd) also
contribute rectangles of dimension 1 by 1 to the knot strand. Finally, the
44 JESSICA S. PURCELL
tangency of A to D gives a rectangle with dimensions 1 by ( n − 1), con-
tributing ( n − 1) to the height. Thus the total height of the cusp is
(2n − 4) + (n − 1) + 2 + (n − 1) = 4 n − 4.
(When n = 2 this argument needs to be modiﬁed slightly: there are no
Ci’s, but B1 and B2 are tangent. Tangencies of A and B2, D and B1, and A
and D also contribute to the height. These all give 1 by 1 rectangle s, hence
the height is 4 = 4 n − 4 in this case as well.)
A meridian runs along the widths of two rectangles in the cusp tiling.
Hence it has length 2. Thus the normalized height h(X) is given by:
h(X) = 4n − 4
√
(4n − 4)(2)
=
√
2(n − 1).
This information will show:
Proposition 6.8. Let K be a 2–bridge knot in S3 which admits a prime,
twist reduced diagram with n ≥ 2 twist regions and at least c ≥ 24 crossings
in each twist region. In a hyperbolic structure on S3 − K, normalized such
that the meridian has length 1, the height of the cusp of S3 − K satisﬁes:
( √
2(n − 1) − √n(0.18456)
) 2
≤ H ≤
( √
2(n − 1) + √n(0.18456)
) 2
.
Proof. Let L be the augmented link corresponding to K. Provided we have
at least n ≥ 2 twist regions, Theorem 6.1 implies S3 − L is hyperbolic. We
have seen in the above discussion that, provided we have at le ast c ≥ 24
crossings in each twist region, the slope on each crossing ci rcle of L on
which we perform Dehn ﬁlling has normalized length at least I(1.0). This
implies that a cone deformation exists from S3 − L to S3 − K for which the
tube radius is at least R1 = 1.0 throughout. Then Theorem 1.4 implies the
normalized height of the cusp of S3 − K satisﬁes:
−
√n(2π)2√
C(1.0)
(1 − e−2.0) ≤ hτ −
√
2(n − 1) ≤
√n(2π)2√
C(1.0)
(1 − e−2.0) .
Using the formulas for C(1.0) from the proof of Lemma 4.3, we ﬁnd
√
2(n − 1) − √n(0.18456) ≤ hτ ≤
√
2(n − 1) + √n(0.18456).
We obtain the ﬁnal result by noting if we scale such that the me ridian has
length 1, then the height is at least ( hτ )2. □
