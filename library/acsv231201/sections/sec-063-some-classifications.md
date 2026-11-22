---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-063-some-classifications
section_title: "Some classifications"
section_number: null
pages: 399-403
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
We begin with a guide to help users of ACSV ﬁnd examples similar to their
intended application, with some of the examples occurring in earlier chapters
and some in this chapter. We classify the examples by local geometry, by form
of generating function, and by intended application. We also point to some
examples where our standard hypotheses fail to hold. The website for this book
contains links to Sage worksheets computing many of the examples listed here.
381
382
Combinatorial applications
Local geometry of GF
Examples
Smooth nondegenerate; explicit critical
points
9.10, 9.11, 9.13, 9.14, 12.11, 12.13,
12.15, 12.27, 12.30
Smooth nondegenerate; implicit critical
points
12.5, 12.6, 12.9, 12.10, 12.17, 12.18,
12.20, 12.22, 12.23, 12.24, 12.25, 12.26
Smooth nondegenerate; periodicity
9.14, 12.11, 12.13
Smooth nondegenerate; torality
12.11, 12.13, 11.11
Smooth degenerate
9.32, 9.39
Multiple transverse n < d
12.29
Multiple transverse n = d
10.28, 10.27, 10.66
Multiple arrangement n > d
10.35, 10.47, 12.28
Multiple not arrangement
10.69, 13.3
Cone point
11.41, 11.43, 11.45, 11.47, 11.50
Table 12.1 Guide by local geometry (dimension d, number of local sheets n).
Classiﬁcation by geometry of contributing points
Table 12.1 collates examples arranged by local geometry. Because smoothness
is a generic property, smooth singular critical points dictate asymptotics in
many applications. Although the coordinates of critical points can be solved in
radicals for simple examples, such as Examples 9.10 and 9.11, this is usually
not the case. Thus, many examples use the algebraic techniques discussed in
Chapter 8 to work with critical points implicitly. A generating function with
more than one contributing point for a given direction leads to periodicity in
coeﬃcients – for instance, the rational function
F(x, y) =
1
1 −x2 −y2
has four contributing singularities in the main diagonal direction, reﬂecting
the fact that the only terms that appear in any series expansion of F are those
with even exponents. We may even have a continuum of critical points, such
as when F(x, y) = 1/(1 −xy), which can be handled under the strong torality
hypothesis discussed in Section 9.1 of Chapter 9. Although the vast majority
of our results require nondegenerate critical points, an example with cubic de-
generacy was studied in Example 9.39 of Chapter 9. Degeneracies of any order
can be handled in two dimensions using Theorem 9.38.
The diﬃculty of analyzing a multiple arrangement point w depends both on
the dimension of the problem and on the number of smooth sheets intersect-
ing at w. The simplest cases occur when there is a single sheet (which is the
smooth case) or when the number of sheets equals the dimension (where there
is a complete intersection). Arrangement points with more sheets than factors
are handled through an algebraic decomposition.
12.1 Some classiﬁcations
383
Form of GF
Examples
Denominator linear in a variable
9.10, 9.11, 9.13, 9.14, 9.39, 12.5, 12.6,
12.9, 12.10, 12.11, 12.13, 12.15, 12.17
Bivariate
9.10, 9.11, 9.13, 9.14, 9.32, 9.39, 10.28,
10.27, 10.35, 10.47, 10.66, 10.69,
11.11, 12.5, 12.6, 12.9, 12.15, 12.18,
12.22, 12.23, 12.25
Trivariate
11.41, 11.43, 11.45, 11.47, 11.50, 12.20,
12.26, 12.29
Higher/arbitrary dimension
12.10, 12.17, 12.27
Repeated factors, m < d
12.29
Repeated factors, m = d
10.28, 10.27, 10.66
Repeated factors, m > d
10.32, 10.35, 10.47, 12.28
Meromorphic, not rational
12.24, 12.30
Algebraic
12.18, 12.20
Non-combinatorial
9.32
Table 12.2 Guide by form of GF (dimension d, number of denominator
factors m).
Multiple points that are not arrangement points are tricky, and the general
theory has not been worked out. Two sheets that are tangent behave basically
like a single repeated sheet, as seen in Proposition 10.68 of Chapter 10, al-
though more complicated singularities can arise, as in Example 10.9. Chap-
ter 11 contains essentially all that we know for more complicated singularities,
with explicit results for cone points.
Classiﬁcation by form of generating function
Table 12.2 classiﬁes our examples by the algebraic form of the generating func-
tion F(z) = P(z)/Q(z). The simplest case occurs when Q is linear in one of
its variables, and the (perhaps surprising) ubiquity of examples of this form is
a reﬂection of the fact that the sequence construction on combinatorial classes
(described in Section 2.2 of Chapter 2) corresponds to the quasi-inverse map
f 7→1/(1 −f) on generating functions. The technique of Lagrange inversion
can also be incorporated into this framework. Sections 12.2 and 12.3 cover ap-
plications to Riordan arrays and Lagrange inversion, respectively. Section 12.4
discusses the transfer matrix method.
Our formulae are ﬂexible enough to work in any dimension, and even for
families with arbitrary dimension as a parameter, although computations are
often simpler in lower dimensions. Repeated denominator factors correspond
to higher order poles, and thus change asymptotic behavior, while multiple
distinct factors lead to multiple points.
384
Combinatorial applications
Structure/application
Typical type of GF
Examples
regular languages, words,
strings
Rational, smooth
12.6, 12.10, 12.17
lattice walks
Rational,
smooth/multiple
12.26
trees
Algebraic or Riordan
12.9
quantum walks
Rational, toral
12.11, 12.13
tilings
Rational, cone/nasty
11.43, 11.45, 11.47
sums of independent ran-
dom variables
Riordan
12.34
number triangles
Riordan
9.10, 9.11, 9.14, 12.15,
12.20, 12.24
constant coeﬃcient linear
recurrences
Rational,
smooth/multiple
12.22
partitions
Inﬁnite product
12.30
Table 12.3 Guide by application area.
Most of our generating functions are rational, but our asymptotic results hold
more generally for meromorphic functions. Some examples, such as F(x, y) =
1/(1 −ex −ey), require solving transcendental equations for critical points,
while others, such as
F(x, y) =
∞
Y
i=1
1
1 −xi −yi
can be reduced to cases with polynomial denominators. We can also ﬁnd asymp-
totics of algebraic generating functions by embedding them in rational series
of higher dimension.
Classiﬁcation by application
Many combinatorial families gives rise to multivariate generating functions
with the same type of behavior, which can be analyzed together, and Table 12.3
gives a rough guide for readers seeking to quickly ﬁnd a relevant application.
Note that some problems fall into multiple areas, due to bijections between
various combinatorial objects.
Examples where our standard hypotheses fail to hold
Most asymptotic expansions derived in this text hold for nondegenerate con-
tributing points, require intersections of multiple denominator factors to be
transverse, and occur in directions in the interior of cones where asymptotic
behavior transitions smoothly with direction. Furthermore, the ﬁrst-order terms
