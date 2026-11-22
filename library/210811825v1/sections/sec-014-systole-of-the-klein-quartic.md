---
doc_id: 210811825v1
doc_title: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups"
section_id: sec-014-systole-of-the-klein-quartic
section_title: "Systole of the Klein quartic"
section_number: null
pages: 98-100
source_pdf: 2108.11825v1.pdf
source_sha256: 1c2a4b317d6239c5
toc_source: outline
doc_brief: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups — 26 sections: Front matter; Introduction; Background"
---
Systole of the Klein quartic
The systole of the Klein quartic is described in Klein’s original paper [48] on the prop-
erties of the quartic curve, and is expounded upon in [44,80]. We will use K to denote
the surface. Consider a tessellation of K by heptagons (these can be barycentrically sub-
divided into 14 (2, 3, 7) triangles, see Figure 4.2). Starting with the central heptagon,
join the midpoints of two adjoining edges with a geodesic. Extend this geodesic in both
directions until it meets the boundary of the fundamental 14-gon. On its way, it passes
through the midpoints of a further 3 and a half heptagon midpoints in either direction; a
total of 8 midpoints. For this reason, Karcher and Weber coin it an “eight step geodesic”.
Note that the two boundary edges that it meets are actually the same edge once the side
associations are made; that is, we have a simple closed geodesic. In fact, the length of
this curve turns out to be the systole of the surface [44]. An order 7 rotation around the
centre of the 14-gon maps this geodesic onto six other copies.
We obtain two more geodesics of length equal to the systole by creating curves that
pass through adjoining edges of heptagons at varying distances from the centre; these
are shown in Figure 4.2. There are 7 heptagons surrounding the central heptagon. The
magenta curve passes through two edges of one of these. This time, when it reaches the
boundary, it does not form a closed curve since the two sides are not associated with
one another. We make the relevant side association and continue the geodesic from here,
following the pattern of passing through midpoints of heptagon edges, until the geodesic
is closed. Since we could have chosen any of the 7 heptagons, we get a further 7 closed
geodesics. The orange (and green) curves pass through two adjoining edges of a heptagon
in the second closest group from the centre. Again, there will be 7 of these. They follow
the same pattern through 8 heptagon edge midpoints, thus having the same length. The
multiplicity of the systole is 21.
88
Figure 4.1: Calculating 1
8 of the systole
b
c
a
We calculate the systole using basic hyperbolic trigonometry to give a closed formula
for one of the “steps”, and then multiply this by 8. Similar to the formulae in Theorem 2.30
for right-angled hyperbolic triangles, we have
sinh(a) = sin(α) sinh(c)
(4.1)
for a right-angled hyperbolic triangle where c is the length of the hypotenuse and α is
the angle opposite the side of length a [13]. Also recall from Section 2.2.3 that the side
of medium length in a (2, 3, 7) triangle has length
arccosh
1
2 csc
π
7

.
Consider the blue geodesic in Figure 4.2. We can zoom in on its centre “step” to get
the triangle shown in Figure 4.1. Since step is symmetric with respect to b, we can divide
the larger triangle into two smaller right-angled triangles. Note that the medium side of
a (2, 3, 7) triangle is the hypotenuse of the right-angled triangle in Figure 4.1. Let a be
half the length of the blue line, that is, the shortest side of the triangle on the left. We
calculate the length of a using Equation (4.1), where α is the angle opposite a and is
equal to π
7. We have
sinh (a) = sin
π
7

sinh

arccosh
1
2 csc
π
7

= sin
π
7
s
−1 + 1
2 csc
π
7
 
1 + 1
2 csc
π
7

= sin
π
7
 1
2
r
csc2
π
7

−4

.
Thus
l(a) = arcsinh
1
2
r
csc2
π
7

−4

sin
π
7

.
This is half of the length of one step of the geodesic, and there are eight steps altogether,
therefore
s(K) = 16 arcsinh
1
2
r
csc2
π
7

−4

sin
π
7

≈3.93594624883.
89
Remark 4.1 Note that there is more than one way to calculate a closed formula for the
systole; [72] came up with
8 arccosh
3
2 −2 sin2 π
7

≈3.93594624883.
Figure 4.2: Geodesics of length equal to the systole
Remark 4.2 Numerical calculations of the other values in the geodesic length spectrum of
the Klein quartic are given in the doctoral thesis of Vogeler [81], along with multiplicities.
Vogeler also gives similar length spectra calculations for many other Hurwitz surfaces,
including the Macbeath surface mentioned in the introduction to this work.
