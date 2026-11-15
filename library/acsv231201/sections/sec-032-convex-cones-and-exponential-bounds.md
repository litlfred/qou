---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-032-convex-cones-and-exponential-bounds
section_title: "Convex cones and exponential bounds"
section_number: null
pages: 165-171
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
147
bounded component has the (convergent) inﬁnite series representation
[xNyN]F(x, y) = −
X
k≥0
4−2N+3k+3 (2N + 3k + 2)!
k! (N + k + 1)!2 .
Give as simple a formula as you can for the coeﬃcient of xNyN in this Laurent
expansion when N < 0.
6.3 Convex cones and exponential bounds
Let f(z) = P
r∈Zd arzr be any convergent Laurent series with domain of con-
vergence D = Relog−1(B). The coarsest asymptotic information about the co-
eﬃcients {ar} is their exponential rate of growth (or decay) when r →∞in
diﬀerent directions. Recall the notation |r| = |r1| + · · · + |rd|.
Deﬁnition 6.19. A sequence {rn} = r1, r2, . . . in Zd goes to inﬁnity in the
direction ˆr if |rn| →∞and rn/|rn| →ˆr. We often drop the subscript n,
writing r →∞to denote a sequence going to inﬁnity and using shorthand like
limr→∞p(r) for an expression limn→∞p(rn) involving a function p : Rd →R.
In the univariate case one can only move forwards or backwards on the real
line, however in multivariate cases there are many directions to study. Typi-
cally the asymptotic behavior of ar changes in a predictable manner with the
direction of a limit r →∞, however this is not always the case. It can there-
fore be useful to consider both the exponential growth in a ﬁxed direction, and
a smoothed version that can be easier to compute.
Deﬁnition 6.20. The (limsup logarithmic) growth rate of a sequence ai in the
direction ˆr is the quantity
β( ˆr) := lim sup
s→∞
s/|s|= ˆr
1
|s| log |as|,
while the (limsup logarithmic) neighborhood growth rate of ai in the direction
ˆr is
β( ˆr) := lim sup
s→∞
s/|s|→ˆr
1
|s| log |as|.
The (neighborhood) growth rate of a generating function is the (neighborhood)
growth rate of its coeﬃcient sequence.
148
Laurent series, amoebas, and convex geometry
Example 6.21. The growth rate of the power series expansion of
f(x, y) =
x −y
1 −x −y =
X
r,s≥0
" r + s −1
s
!
−
 r + s −1
r
!#
xrys
in the direction ˆr = (1, 1) is −∞, because an,n = 0 for all n ≥0, however the
neighborhood growth rate in the direction ˆr is log 2. For instance, |an,n+k|1/n →
2 as n →∞whenever k , 0 is a ﬁxed integer.
◁
Computing the growth rate of a multidimensional sequence can be diﬃcult,
however it is possible to bound the growth rate using the behavior of f on
its domain of convergence D. For any w ∈D, bounding the Cauchy integral
expression
|ar| =

 1
2πi
!d Z
T(w)
f(z)z−r−1 dz

by the maximum modulus of its integrand times the surface area of its domain
of integration gives
|ar| ≤|w−r| · max
z∈T(w) | f(z)|.
(6.4)
The dual rate of f over D (or B) is the quantity
β∗( ˆr) := inf
z∈D −ˆr · Relog(z) = inf
x∈B −ˆr · x .
(6.5)
Optimizing (6.4) over w ∈D implies
lim sup
r→∞
|ar|1/|r| ≤inf
w∈D |w|−ˆr ,
(6.6)
so that
β( ˆr) ≤β( ˆr) ≤β∗( ˆr)
(6.7)
for any direction ˆr.
Remark 6.22. Equation (6.7) is the multivariate analogue of relationship (3.5)
between the radius of convergence of a univariate power series and exponential
growth, however in the multivariate case we get an inequality instead of an
equality. The dual rate is an example of a Legendre transform (see the notes at
the end of this chapter).
Remark 6.23. To compute β∗( ˆr) it is suﬃcient to minimize the function |z| ˆr
on the closure D. Writing z = x + iy for real variables x and y implies
|z|2v = (x2
1 + y2
1)v1 · · · (x2
1 + y2
d)vd for any v ∈Rd. Thus, if ˆr has positive rational
coordinates and f represents a rational function then (potentially after taking
powers of some variables to remove fractional powers) we can represent the
6.3 Convex cones and exponential bounds
149
problem of minimizing |z| ˆr on D as a polynomial optimization problem over
a semialgebraic domain. Computing such a minimizer can be done algorithmi-
cally, although in general it is extremely expensive. See [Las15] for a detailed
account of such optimization problems, and computationally feasible relax-
ations.
Because B is an open convex set in Rd, either β∗( ˆr) = −∞or the inﬁmum
in (6.5) is achieved by taking x to a point on the boundary ∂B. In the rest of this
section we examine what happens when β∗( ˆr) = −∞, while the next section
studies the case when β∗( ˆr) is ﬁnite.
Proposition 6.24. Let f(z) = P(z)/Q(z) be a ratio of polynomials P and Q.
If r1, r2, . . . is a sequence of vectors in Zd going to inﬁnity in the direction
ˆr ∈Rd and the set {−ˆr · x : x ∈B} is unbounded from below then arn = 0 for
all but ﬁnitely many n.
Proof
If the linear function −ˆr · x is unbounded from below on B then, since
P and Q are polynomials, we can ﬁnd a sequence of points {xk} in B and a
polynomial p(x) such that −ˆr · x ≤−k and
| f(z)| ≤p(ek) on Relog−1(xk).
Because rn/|rn| = ˆr + o(1) we have |z−rn| = |e−x·rn| ≤e−k(|rn|+o(|rn|)) when
z ∈Relog−1(x), so the maximum modulus bound (6.4) implies
|arn| ≤p(ek) exp
h
−k(|rn| + o(|rn|))
i
.
If n is suﬃciently large then |rn|+o(|rn|) is positive and the upper bound on the
right-hand side goes to zero as k →∞. Since this bound holds for all k ∈N, it
follows that arn is zero for all suﬃciently large n.
□
Remark 6.25. If f(z) is a ratio of analytic functions with a Laurent series
converging on D = Relog−1(B) and −ˆr · x is unbounded from below on B
then the function p giving an upper bound on |f(z)| may no longer be poly-
nomial, and thus the coeﬃcients arn may not eventually be zero. However,
our argument still proves that the coeﬃcients decay faster than any exponen-
tial function in n. The methods of ACSV we develop are not concerned with
this super-exponential regime, and if the reader encounters such a situation we
recommend trying direct application of the multivariate saddle point methods
described in Chapter 5.
Proposition 6.24 describes the extreme behavior that occurs when {−ˆr · x :
x ∈B} is unbounded from below, and it is natural to wonder when such behav-
ior can occur. Serendipitously, the connection between the Newton polytope
150
Laurent series, amoebas, and convex geometry
Figure 6.4 A convex set (light gray) with three selected boundary points. Parts
of the corresponding tangent cones (facing into the set) and normal cones (facing
away from the set) are displayed. Note that the rightmost normal cone is a one-
dimensional line. The recession cone of this set is {0} since the set is bounded.
of Q and the components of amoeba(Q)c described in Theorem 6.18 above
can be strengthened to help provide such information. In order to state this
relationship we need some additional terminology.
Deﬁnition 6.26. Let B be a convex set. A convex cone is a subset of Rd that is
closed under addition and closed under multiplication by positive scalars. The
recession cone of B is the set of vectors {v ∈Rd : x+v ∈B for all x ∈B} and
the (open) tangent cone to B at x ∈B is
tanx(B) = {s ∈Rd : x + εs ∈B for all suﬃciently small ε > 0}.
The tangent cone is a generalization of the tangent space of a manifold to
spaces with singularities. The (closed) normal cone to B at x ∈B is
normalx(B) = {s ∈Rd : s · x ≥s · b for all b ∈B} .
See Figure 6.4 for an illustration of these concepts.
Exercise 6.8. If K is an open convex cone in Rd then its dual cone K∗⊂Rd
is the set of vectors {s ∈Rd : s · x ≥0 for all x ∈K}. Prove the following
statements.
a) The recession cone, tangent cone, and normal cone are convex cones.
b) Let K and L be open convex cones. Then (K ∩L)∗= hull(K∗∪L∗) and if
K ⊂L then K∗⊃L∗.
6.3 Convex cones and exponential bounds
151
c) Every open convex cone is the intersection of all open half-spaces that con-
tain it.
d) After a translation by x, the tangent cone to B at x is the interior of the
intersection of all halfspaces that contain B and have x on their boundary.
e) If x is an interior point of B then normalx(B) = {0}.
f) The normal cone is the dual cone to the negative of the tangent cone,
normalx(B) = (−tanx(B))∗.
The result we need comes from the following correspondence.
Proposition 6.27. Let f be a Laurent polynomial and let x be a point in a
component B of amoeba( f)c. Then the recession cone of B equals the normal
cone of N f at ν(x).
Proof
Let s ∈Zd \ {0}. By deﬁnition, the ray {x + ts : t > 0} stays in B
if and only if all zeros of f(p1ws1, . . . , pdwsd) lie inside |w| = 1 for all p ∈
Relog−1(x), and Lemma 6.14 implies this occurs if and only if s · ν(x) equals
the total number of zeros of as(w) = f(ex1ws1, . . . , exdwsd) in the complex plane
minus the order of the pole of as(w) at the origin. Since as(w) has degree
maxn∈N f (s · n), it follows that
s is in the recession cone of B
if and only if {x + ts : t > 0} ⊂B for all x ∈B
if and only if s · ν(x) = max
n∈N f(s · n) for all x ∈B
if and only if s ∈normalν(p)

N f

,
proving the desired equivalence.
□
Exercise 6.9. Prove that the order of any bounded component of amoeba( f)c
is an interior point of N f , then prove that the recession cone of a component
of amoeba( f)c has nonempty interior if and only if its order is a vertex of N f .
Proposition 6.27 allows us to read oﬀproperties of the components of the
complement amoeba( f)c directly from the Newton polytope of f. It also has
strong implications for the asymptotic behavior of sequences with multivariate
rational generating functions.
Corollary 6.28. Assume the hypotheses of Proposition 6.24 and let x ∈B. If
the ray {ν(x)+t ˆr : t > 0} does not intersect N Q then arn = 0 for all but ﬁnitely
many n.
Proof
See Exercise 6.17.
□
152
Laurent series, amoebas, and convex geometry
Figure 6.5 Left: The Newton polytope of 1 −x −y with the normal cones at each
vertex. Right: A drawing of amoeba(1 −x −y) with the recession cones of each
component of the complement added.
Corollary 6.29. Let f(z) be a rational function and let {rn} be a sequence of
vectors in Zd going to inﬁnity in the non-zero direction ˆr ∈Rd. Then there
is a component B of amoeba( f)c such that the convergent Laurent expansion
f(z) = P
r∈Zd arzr with domain of convergence D = Relog−1(B) has arn = 0
for all but ﬁnitely many n.
Proof
For any non-zero vector ˆr ∈Rd there exists a vertex n ∈N f such
that {n + t ˆr : t > 0} does not intersect N f (any of the vertices of N f on
the hyperplane touching the boundary of N f with outward normal ˆr have this
property). The desired result then follows from Corollary 6.28 where B is the
component of amoeba( f)c with order n, whose existence is guaranteed by The-
orem 6.18.
□
Corollary 6.29 turns out to be crucial to our framework for ACSV. Roughly,
we represent a sequence of interest as a Cauchy integral then move the point
x in the domain of integration Relog−1(x) from its starting component of
amoeba( f)c to another component, picking up a residue integral over an in-
tersection cycle along the way. By moving x into a component where series
coeﬃcients are eventually zero, we only need to approximate the residue in-
tegral, which can be done using saddle point techniques. Fully describing this
argument takes up the majority of Chapter 7.
