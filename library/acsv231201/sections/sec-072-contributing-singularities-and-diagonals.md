---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-072-contributing-singularities-and-diagonals
section_title: "Contributing singularities and diagonals"
section_number: null
pages: 442-444
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Let F(z) be the generating function of a sequence (ar). Theorems 7.20 and 7.35
represent ar as an integer sum of saddle point integrals near critical points of
F, which can be analyzed to determine asymptotics of ar. Unfortunately, iden-
tifying the integer coeﬃcients in this sum seems to be extremely diﬃcult, if
not undecidable. Even identifying the contributing singularities of F, which
are the critical points of highest height with non-zero coeﬃcients, is currently
only possible in general for minimal critical points, in two dimensions, or when
F is the product of linear factors.
Being able to identify the contributing singularities of a general rational
function would be an important theoretical breakthrough for ACSV. One (topo-
logical) approach is to generalize the two-dimensional algorithm discussed in
Section 9.3 to higher dimensions. Another (computational) approach is to use
software for D-ﬁnite functions. Recall from Section 8.4.2 that for any ﬁxed
r ∈Zd the r-diagonal of a multivariate rational function is D-ﬁnite, and the
methods of creative telescoping produce a D-ﬁnite equation satisﬁed by the
diagonal. Thus, it is possible to study rational diagonals using both ACSV and
techniques for D-ﬁnite functions. In fact, these methods are complementary:
ACSV often determines asymptotics up to unknown integers that are diﬃ-
cult to determine, while D-ﬁnite techniques often determine asymptotics up
424
13.1 Contributing singularities and diagonals
425
to unknown complex numbers that can be rigorously approximated. The com-
bination of these two representations was used in Example 11.50 to determine
asymptotics for a multivariate generating function with cone singularities, and
it is natural to ask how far this combined method can be pushed – both to
characterize the behavior of multivariate rational diagonals, and to attack the
connection problem for the asymptotics of sequences with D-ﬁnite generating
functions.
Problem 13.1. Classify the types of rational functions for which this hybrid
ACSV and D-ﬁnite numeric method applies.
Remark 13.1. The diagonal of any bivariate rational function is algebraic,
so asymptotics in any ﬁxed direction can always be decided by computing the
minimal polynomial for the diagonal and applying univariate techniques. How-
ever, the complexity of the computation to reduce to the one-dimensional case
can increase with the size of the integers representing a direction of interest,
and does not work for general direction. Thus, it is interesting to study even
bivariate rational diagonals using multivariate methods.
Example 13.2. The (a, b)-diagonal of the bivariate generating function
F(x, y) =
1
1 −x −y −xy
for the Delannoy numbers has the representation
G(x) =
h
t0i
F

x1/a/tb, ta
= 1
2πi
Z
γx
F

x1/a/tb, ta
t
dt
= 1
2πi
Z
γx
tb−1
tb −x1/a −ta+b −x1/ata dt ,
for x suﬃciently close to the origin and γx a circle around the origin that ap-
proaches the origin as x →0. This integrand has a single pole t = s(x) satisfy-
ing limx→0 s(x) = 0, which is a pole of order b, so
G(x) = Res
t=s(x) F

x1/a/tb, ta
/t
= lim
t→s(x)
1
(b −1)!∂b−1
t

(t −s(x))bF

x1/a/tb, ta
/t

.
The product rule gives this limit as an algebraic expression in s(x), which can
be combined with the deﬁning algebraic equation for s(x) to give an algebraic
equation satisﬁed by G, however this expression is extremely unwieldy for
large a and b, and the complexity of the operations grows with a and b. In
426
Challenges and extensions
contrast, asymptotics of the Delannoy numbers in all diagonal directions was
given in Example 9.11 using ACSV.
◁
