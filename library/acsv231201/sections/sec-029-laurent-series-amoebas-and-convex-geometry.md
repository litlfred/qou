---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-029-laurent-series-amoebas-and-convex-geometry
section_title: "Laurent series, amoebas, and convex geometry"
section_number: null
pages: 152-153
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Laurent series, amoebas, and convex geometry
The theory of analytic combinatorics works by encoding a sequence of interest
as a convergent series and applying tools from complex analysis. Although
our results in previous chapters have focused on power series expansions that
converge near the origin, a single rational (or meromorphic) function can be
represented by multiple convergent series expansions over diﬀerent domains
in Cd.
Example 6.1. The function F(z) = 1/(1 −z) has the convergent power series
representation
F(z) =
X
n≥0
zn
when
|z| < 1
and also the convergent Laurent series representation
F(z) = −1/z
1 −1
z
= −
X
n≥0
z−n−1
when
|z| > 1.
◁
In this chapter we introduce several constructions that, in addition to be-
ing used in later arguments, expand our viewpoint and help motivate how to
make certain choices while computing on actual examples. The ﬁrst section of
this chapter develops the theory of convergent Laurent series, their domains of
convergence, and a generalization of the Cauchy Integral Formula. Not only do
Laurent series allow us to deal more naturally with generating functions that
are ratios of Laurent polynomials, which appear frequently in combinatorial
applications, they are also the natural level of generality with which to discuss
polynomial amoebas – algebro-geometric objects that allow us to visualize the
relationship between a rational function and its convergent series expansions.
Furthermore, the algebraic computations that we undertake in order to deter-
mine asymptotics of a series expansion of a rational (or meromorphic) function
134
