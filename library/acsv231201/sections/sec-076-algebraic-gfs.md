---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-076-algebraic-gfs
section_title: "Algebraic GFs"
section_number: null
pages: 448-450
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Section 12.6 showed how to study algebraic generating functions by embed-
ding them as diagonals of higher-dimensional rational functions. The simplest
embedding method, due to Furstenberg, is easy to apply when it works, but
does not apply to any algebraic generating function intersected by one of its
algebraic conjugates at the origin. There are several known methods for resolv-
ing singularities in such cases, for instance the algorithm of Safonov [Saf00]
mentioned in Theorem 2.41 and the less constructive procedure of Denef and
Lipshitz [DL87].
Example 13.6. Let f(x) = x/
√
1 −x be an algebraic function with minimal
polynomial P(x, y) = (1−x)y2 −x2. Because f(x) = x+O(x2) and its algebraic
conjugate −f(x) = −x+O(x2) intersect at the origin, the embedding method of
Furstenberg does not apply. Safonov’s procedure subtracts some initial terms
via the substitution y = xz+x, yielding a minimal polynomial (1−x)(z+1)2−1 to
which Proposition 2.34 now applies. Converting back to the original variables
then gives f as the main diagonal of
F(x, y) =

2 y3x + 3 y2x −2 y2 + 2 yx −3 y + x −2

yx
y2x + 2 yx −y + x −2
.
We remark that F has no aﬃne critical points in the main diagonal direction,
so it admits critical points at inﬁnity which determine asymptotic behavior,
making the analysis diﬃcult. An alternative embedding, following the method
of [DL87], is obtained through the much less obvious substitution y = x/(1−z),
expressing f(x) as the main diagonal of
G(x, y) =
2xy
1 −x −y.
In contrast to the diﬃcult behavior of F, the function G is combinatorial and
has a smooth contributing critical point at (1/2, 1/2), allowing for an easy
asymptotic analysis.
◁
13.5 Algebraic GFs
431
Problem 13.4. Give a complete analysis of algebraic generating functions f(x)
with quadratic minimal polynomials.
Problem 13.5. Can an algebraic series f(x) with nonnegative coeﬃcients al-
ways be embedded as the diagonal of a combinatorial rational function? Find
an eﬃcient algorithm that converts coeﬃcient extraction for algebraic func-
tions to coeﬃcient extraction for rational functions in a way that preserves the
combinatorial nature of the problem.
Recent work [Gre+22] develops software to analyze a variety of algebraic
generating functions, ultimately cataloguing 20 combinatorial examples. An
alternative approach being developed [BJP23] integrates algebraic generating
functions directly. If f is an algebraic function deﬁned by P(z, f) = 0 and
f(0) = c, with y = c a simple zero of P(0, y), coeﬃcients of the power series
expansion of f at the origin are given by
ar =
1
(2πi)d
Z
T
f(z)z−r−1 dz ,
(13.2)
where T is a torus about the origin, suﬃciently small so the polydisk with the
same radii contains no singularities of f. Because (0, c) is a simple zero of P,
there is a neighborhood N of (0, c) in Cd+1 such that projection π onto the ﬁrst
d coordinates of the hypersurface VP in Cd+1 restricted to this neighborhood
is a bi-analytic map to a neighborhood of the origin in Cd. Choosing T smaller
if necessary so as to be contained in this neighborhood of the origin, the set
C = π−1(T) is a small torus in VP and (13.2) becomes
ar =
1
(2πi)d
Z
C
yz−r−1 dz.
(13.3)
Aside from the high negative powers of z1, . . . , zd, the integrand y has no
denominator, however the coeﬃcients ar may be recovered the same way as
one recovers coeﬃcients of rational functions. In the absence of critical points
at inﬁnity, the d-dimensional complex variety V∗= VP ∩Cd
∗has a Morse the-
oretic decomposition into cycles attaining their maximum height near critical
points of the height function h( ˆr,0)(z) = Pd
j=1 rj log |zj|. One then resolves the
chain C in this basis. For instance, if the surface VP is smooth and there are
no CPAI for P in the direction ( ˆr, 0) then the asymptotics of ar are given by
some linear combination of Φw from (9.4) over critical points w of P in the
direction ( ˆr, 0).
Example 13.7. Let f(x) = 1−
√
1−4x
2x
be the Catalan generating function, with
minimal polynomial P(x, y) = xy2 −y + 1 = 0. The point (0, f(0)) = (0, 1) is
a smooth point of VP, and a small circle about (0, 1) in V∗projects by π to a
432
Challenges and extensions
small circle about the origin in C1. The smooth surface VP has precisely one
critical point p = (1/4, 2) in the direction (1, 0), deﬁned by the simultaneous
vanishing of P and Py. There is a critical point at inﬁnity because the value
of Py goes to zero as x →0, however the height function goes to inﬁnity as
x →0 so Morse theory tells us that the initial curve C can be deformed in
V∗to a smooth contour γ in P passing through p so that the minimum of
log |x| on γ occurs at p. A standard stationary phase integral for
R
γ x−n−1ydx
leads to an asymptotic series for the Catalan numbers. Because the amplitude
y is stationary at p, there will be one more negative power of n than the usual
n−1/2 obtained from a univariate saddle point integral. This recovers without
computation the fact that the nth Catalan number is Θ

n−3/24n
.
◁
Exercise 13.6 below explores what happens when (0, c) is not a simple pole
of P. We conclude with an exercise illustrating a multivariate algebraic func-
tion.
Exercise 13.2. Let
f(x, y) = 1 + x(y −1) −
p
1 −2x(y + 1) + x2(y −1)2
2
be the Narayana bivariate generating function from Example 2.37, deﬁned by
the minimal polynomial
P(x, y, w) = w2 −w 1 + x(y −1) + xy
and the fact that f(0, 0) = 0.
(a) Show that P is smooth.
(b) Find c = f(0, 0) and determine whether (0, 0, c) is a simple zero of P.
(c) Find the critical points for P in the direction (2, 1, 0).
(d) Among the critical points, which have ﬁnite height?
(e) Are there critical points at inﬁnity in the direction (2, 1, 0)?
(f) What asymptotics for a2n,n do you get from integrating
R
γ wx−2n−1y−n−1 dxdy
over an appropriate contour γ?
