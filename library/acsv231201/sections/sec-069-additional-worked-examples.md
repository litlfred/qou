---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-069-additional-worked-examples
section_title: "Additional worked examples"
section_number: null
pages: 422-430
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
We now run through several other examples.
Example 12.22 (A constant coeﬃcient bivariate recurrence). Consider the
constant coeﬃcient linear recurrence
f(m, n) = f(m −1, n −1) + f(m −1, n −2) + 2 f(m −2, n −1)
(m, n ≥2)
with boundary conditions f(m, n) = 0 if m < 0 or n < 0 and f(m, n) = 1
when 0 ≤m ≤1 or 0 ≤n ≤1. Grau Ribas [Gra] asked for the limit
of f(n + 1, n + 1)/ f(n, n) which, based on numerical computations such as
f(100, 100)/ f(99, 99) = 2.70265 . . . , appears to exist and be close to e.
Introducing the generating function F(x, y) = P
m,n f(m, n)xmyn, the deﬁning
recurrence of f implies
F(x, y) =
1
Q(x, y)
with Q(x, y) = 1 −xy −xy2 −2x2y. Gr¨obner basis computations verify that V
is smooth, and the critical points in the main diagonal direction are the points
(x, 2x) where x is a root of 8x3 + 2x2 −1. If w = 0.85 . . . denotes the unique
real root of 8x3 + 2x2 −1 then Lemma 6.41 implies that (w, 2w) is minimal,
and it is the only critical point on the torus T(w, 2w). The limit
f(n + 1, n + 1)
f(n, n)
→
1
2w2
12.7 Additional worked examples
405
is algebraic, and therefore not equal to e. Reducing R = 1/(2w2) modulo the
minimal polynomial for w implies R is the unique positive root of the polyno-
mial 8 −R + 2R2 −R3.
◁
Example 12.23 (Horizontally Convex Polyominoes). The generating function
F(x, y) =
X
r,s≥0
arsxrys =
xy(1 −x)3
(1 −x)4 −xy(1 −x −x2 + x3 + x2y)
(12.16)
enumerates horizontally convex polyominoes (HCPs) [P´ol69; Odl95; Wil06;
Sta97] by total size r and number of rows s. Letting Q denote the denomi-
nator of F in (12.16), we know from Example 8.4 that V is smooth except
at the point (1, 0). By Proposition 6.38, there is a part of the graph of Q in
the ﬁrst quadrant consisting of minimal points, which are the points shown in
Figure 12.4 with x ≤1.
Figure 12.4 Minimal points of V in the positive real quadrant.
The only combinatorially interesting directions occur in Ξ = {(ˆr, ˆs) : 0 <
ˆs < 1/2}, because an HCP cannot have more rows than its size. As ˆr varies
over Ξ from the horizontal to the diagonal, the unique contributing point in
the direction ˆr moves along this graph from (1, 0) to (0, ∞). The numerator
P = xy(1 −x)3 of F in (12.16) is nonvanishing on this component and, using
Gr¨obner bases, we ﬁnd that the quantity Q in the asymptotic expansion (9.7)
does not vanish at any of these contributing points.
Since for each direction there are only ﬁnitely many critical points, and no
others lie on the same torus as the one we have identiﬁed, it follows from
Theorem 9.12 that asymptotics for ars are uniform as s/r varies over a compact
subset of the interval (0, 1) and have the form ars ∼Cx−ry−ss−1/2. Algebraic
406
Combinatorial applications
methods may then be used to determine x, y, and C as explicit functions of
λ = s/r, giving asymptotics for the number of HCPs that are uniform as long
as s/r remains in a compact subinterval of (0, 1). For instance, when λ = 1/2
the smooth critical points (x, y) satisfy 3x2 + 18x −5 and 75y2 −288y + 256,
with the contributing singularity occurring at
(x0, y0) =

r
32
3 −3, 48 −
√
512
25
≈(0.265986, 1.397442),
and a ﬂoating point computation gives an,n/2 ∼(0.2373 . . . )(3.1803 . . . )nn−1/2.
Note that the exponential growth of 3.1803 . . . in this case is only slightly less
than the exponential growth 3.2055 . . . for all HCPs – a reﬂection of the fact
that the exponential growth varies quadratically around its maximum.
We can also derive limit laws. For instance, let q(x) = Q(x, 1) = 1−5x+7x2−
4x3 and let a ≈0.3120 be the root of q with minimum modulus. Theorem 12.33
below, with the roles of x and y switched, proves that the number of rows k of
a uniformly chosen HCP of total size n satisﬁes k/n →m in probability, where
m = yQy(a, y)
aQx(a, y) =
5 −9a + 11a2
4(5 −14a + 12a2) =
1
2.207 . . ..
In other words, the average row size converges to a little over 2.2.
◁
Example 12.24 (Symmetric Eulerian numbers). The symmetric Eulerian num-
bers A(r, s) count the number of permutations of the set [r+s+1] = {1, 2, . . . , r+
s + 1} with precisely r descents, and admit the exponential generating function
F(x, y) =
ex −ey
xey −yex =
X
r,s≥0
A(r, s)
r! s! ,
(12.17)
see [Com74, page 246] and [GJ04, p. 2.4.21]. To represent the numerator and
denominator of F as analytic functions with no common divisor we factor out
a term x−y from each, writing F(x, y) = P(x, y)/Q(x, y) for P = (ex−ey)/(x−y)
and Q = (xey −yex)/(x −y). We know by its combinatorial deﬁnition that the
power series coeﬃcients of F are nonnegative, and the power series expansion
of Q is aperiodic, so the results of Section 6.4 imply that the minimal points of
F have positive coordinates. The graph of Q in this quadrant of R2 is monotone
decreasing with x and asymptotic to both axes; see Figure 12.5.
It can be veriﬁed by a direct computation that the singular variety of F is
smooth, and the quantity Q in the asymptotic expansion (9.7) does not vanish
at positive real points – in fact, Q(x, y) reaches its minimum value of e3/12 at
the point (1, 1). The logarithmic gradient of Q at any point (x, y) in the ﬁrst
12.7 Additional worked examples
407
Figure 12.5 The zero set of (xey −yex)/(x −y) in the ﬁrst quadrant.
quadrant is a non-zero multiple of (α, 1 −α), where
α =
xQx(x, y)
xQx(x, y) + yQy(x, y),
which simpliﬁes to
α = 1 −x
y −x
for points on V, except when (x, y) = (1, 1) and α = 1/2. Thus, Theorem 9.5
implies that asymptotics in the direction (α, 1−α) can be computed by solving
the system
α = 1 −x
y −x ,
xey = yex
for positive real values (x, y) and using the expansion (9.7). The result, recalling
that F is an exponential generating function, is that A(r, s) is asymptotically
estimated by
A(r, s) ∼Cα(r + s)−1/2γr+sr!s!
where γ = x−αyα−1 and Cα is a messy constant determined by (9.6) and (9.7).
◁
Example 12.25 (Number of successes in a coin-ﬂipping game). Consider a
single player game with biased coins, so that heads appears with probability
p = 2/3 for the ﬁrst n ﬂips and p = 1/3 thereafter. The player is told to get r
heads and s tails, and is allowed to choose n. On average, how many choices
of n ≤r + s will be winning choices?
408
Combinatorial applications
Decomposing the probability that n is a winning choice for the player by
how many heads are rolled in the ﬁrst n throws shows that the probability is
X
a+b=n
 n
a
!
(2/3)a(1/3)b
 r + s −n
r −a
!
(1/3)r−a(2/3)s−b .
If ars is the sum of the winning probability over all n, then the array {ars}
is the convolution of the arrays
r+s
r

(2/3)r(1/3)s and
r+s
r

(1/3)r(2/3)s, so the
generating function F(x, y) = P
rs arsxrys is the product
F(x, y) = P(x, y)
Q(x, y) =
1

1 −1
3 x −2
3y
 
1 −2
3 x −1
3y
 .
The complete intersection asymptotic results of Chapter 10 imply that ars =
3 plus an error term which is exponentially small as r, s →∞provided that
r/(r + s) stays in a compact subinterval of (1/3, 2/3). A purely combinatorial
analysis of the sum may be carried out to yield the leading term 3, but says
nothing about the error terms.
◁
Example 12.26 (Lattice paths constrained to a quadrant). Consider the class
of lattice paths on Z2 that start at the origin and must remain in the nonneg-
ative quadrant N2 while using the set {(1, 0), (1, −1), (−1, 0), (−1, 1)} of allow-
able steps. The kernel method [Mel21, Chapter 4] allows one to prove that the
generating function enumerating such walks by number of steps is the main
diagonal of
F(x, y, t) = (x + 1)(x−2 −y−1)(x −y)(x + y)
1 −xyt(x + xy−1 + yx−1 + x−1) .
This is a rational function with smooth singular variety, and minimal critical
points p1 = (1, 1, 1/4) and p2 = (−1, 1, 1/4). As the numerator of F has a
zero of order 2 at p1 and a zero of order 3 at p2, only p1 contributes to domi-
nant asymptotics. Computation with a computer algebra system shows that the
counting sequence for the number of walks on these steps satisﬁes
sn = 4n
n2 · 8
π + O
 4n
n3
!
.
ACSV provides a powerful framework to determine asymptotics of such lattice
path models [Mel21, Chapters 6 and 9].
◁
Example 12.27 (alignments). Fix a positive integer d. The (d, n)-alignments
are d × m binary matrices for some m, such that no columns are identically
zero and the ith row sum is ni. These structures have relevance to bioinformat-
ics [RT05; Wat95], and the generating function enumerating such alignments
12.7 Additional worked examples
409
by multi-index n is
F(z) =
1
2 −Qd
i=1 (1 + zi)
=
X
n∈Nd
anzn.
In the main diagonal direction, the symmetry of F and the combinatorial ape-
riodic nature of the problem combine with Lemma 6.41 to imply that there is
a single, strictly minimal, contributing point (z, . . . , z) in the positive orthant,
where z = 21/d −1. Theorem 9.5 then yields
an,...,n ∼
2(1−d2)/d
(21/d −1)
√
dπd−1 (21/d −1)−knn−d−1
2 ,
recovering a result of [Gri+90].
◁
Example 12.28 (integer solutions to linear equations). Let A be a d×m matrix
of nonnegative integers and, for r ∈Nd, let ar denote the number of nonnega-
tive integer solutions to Ax = r. The generating function for the array {ar} is
given by
F(z) =
X
r∈Nd
arzr =
m
Y
j=1
1
1 −zAeT
j ,
where ej is the jth elementary vector. This enumeration problem is discussed
at length in [DS03] (see also [Sta97, Section 4.6]) which uses the running
example
A =

1
0
0
1
1
0
1
0
1
0
0
0
1
0
1

with generating function
F(z) =
1
Q1Q2Q3Q4Q5
=
1
(1 −x)(1 −y)(1 −z)(1 −xy)(1 −xz) .
The divisors of F are all binomials of the form 1 −zα, and their zero sets all
intersect at (1, 1, 1). The logarithmic gradients of the divisors at (1, 1, 1) are the
columns of A.
Every triple of columns of A except for (1, 2, 4) and (1, 3, 5) forms a lin-
early independent set. The circuits of the matroid deﬁned by A are therefore
these triples and the only quadruple (2, 3, 4, 5) not containing either triple, so
the broken circuits are (1, 2), (1, 3), and (2, 3, 4), and the bases containing no
broken circuit are (1, 4, 5), (2, 3, 5), (2, 4, 5), and (3, 4, 5). By Theorem 10.33, a
410
Combinatorial applications
basis for rational functions with simple poles on VQ1, . . . , VQ5 is given by
(
1
Q1Q4Q5
,
1
Q2Q3Q5
,
1
Q2Q4Q5
,
1
Q3Q4Q5
)
.
To reduce F to the sum of terms whose support is in BC(F) we use relations
expressing Qi in terms of {Q j : j ∈C \ {i}}, where i is the greatest element in a
circuit. A little scratch work uncovers these relations for the respective circuits
(1, 2, 4), (1, 3, 5), and (2, 3, 4, 5), giving
Q4 = Q1 + Q2 −Q1Q2
(12.18a)
Q5 = Q1 + Q3 −Q1Q3
(12.18b)
Q5 = −y−1Q2 + y−1Q3 + xQ4 .
(12.18c)
The ﬁrst relation (12.18a) divided by QQ4 yields
1
Q =
1
Q2Q3Q2
4Q5
+
1
Q1Q3Q2
4Q5
−
1
Q3Q2
4Q5
.
(12.19)
We are ﬁnished manipulating the third term of (12.19), as its support {3, 4, 5}
is in BC(F). The second term of (12.19), after an application of (12.18b), be-
comes
1
Q3Q2
4Q2
5
+
1
Q1Q2
4Q2
5
−
1
Q2
4Q2
5
.
The ﬁrst term of (12.19), after an application of (12.18c), yields
−1/y
Q3Q2
4Q2
5
+
1/y
Q2Q2
4Q2
5
+
x
Q2Q3Q4Q2
5
and, using (12.18c) once again on the last of these three terms, replaces that
term by
−x/y
Q3Q4Q3
5
+
x/y
Q2Q4Q3
5
+
x2
Q2Q3Q3
5
.
Putting this all together gives the decomposition
F = −
1
Q3Q2
4Q5
+
1
Q3Q2
4Q2
5
+
1
Q1Q2
4Q2
5
−
1
Q2
4Q2
5
+
−1/y
Q3Q2
4Q2
5
+
1/y
Q2Q2
4Q2
5
+
−x/y
Q3Q4Q3
5
+
x/y
Q2Q4Q3
5
+
x2
Q2Q3Q3
5
,
and the techniques of Chapter 10 can now be applied to each term to determine
asymptotic behavior.
◁
12.7 Additional worked examples
411
Example 12.29 (Serial Dictatorship). The trivariate sequence
anjr =

(r−s
t−s)
( r
t−1)
if 1 ≤s ≤t ≤r
0
otherwise
arises in the study of the Serial Dictatorship algorithm for allocating indivisible
goods (it gives the probability, under IID uniform strict preferences of r agents
over r items, that the sth agent receives its tth most preferred item).
The generating function for the numerators brst =
r−s
t−s

is
F(x, y, z) =
X
r,s,t≥0
brstxryszt =
xyz
(1 −x −xz)(1 −xyz).
Let Q1(x, y, z) = 1 −z −xz and Q2(x, y, z) = 1 −xyz. Because Q1 is inde-
pendent of y, points on the stratum where Q1 vanishes but Q2 is non-zero can
only be critical points for directions (r, s, t) with s = 0. Similarly, the stratum
where Q1 is non-zero but Q2 vanishes contains only critical points in the main
diagonal direction (which results in a trivial sequence). Thus, all interesting
directions correspond to points where both factors vanish, which is the curve
parametrized by (x, 1/(1 −x), (1 −x)/x) for x , 0.
A point on this curve is a contributing point for asymptotics in the direction
(r, s, t) if and only if the direction lies in the lognormal cone at the point. This
means that (r, s, t) = λ(1, 0, 1 −x) + µ(1, 1, 1) for some λ, µ ≥0. Solving this
system gives the unique contributing point
 r −t
r −s, r −s
t −s , t −s
r −t

for any such direction, when r > t > s > 0. Each such point is minimal by
Corollary 6.39. Theorem 10.38 applies and yields the dominant asymptotic
behavior. We obtain the ﬁrst-order approximation for the numerator
brst ∼
(r −s)r−s+ 1
2
√
2π(r −t)r−t+ 1
2 (t −s)t−s+ 1
2 .
The relative error is less than 2% even for (r, s, t) = (20, 5, 10). Note that the
approximation is uniform in the union of the cones spanned by (1, 1, 1) and
(1, 0, 1 −x) as x ranges over any compact subset of (0, 1). The cones cover the
entire range of interest r > t > s > 0.
◁
Example 12.30 (Inﬁnite products: Quivers and Littlewood–Richardson coeﬃ-
cients). Consider the inﬁnite product generating function
F(x, y) =
∞
Y
i=1

1 −xi −yi−1
412
Combinatorial applications
arising both in the study of chiral operators in four-dimensional quiver gauge
theories [RWZ20] and in the enumeration of Littlewood–Richardson coeﬃ-
cients cλ
µν, since
F(x, y) =
X
λ,µ,ν

cλ
µν
2 x|µ|y|ν|
(see Harris and Willenbring [HW14] for a derivation and more on Littlewood–
Richardson coeﬃcients). Although F is meromorphic and not rational, its anal-
ysis is surprisingly simple. Write
F(x, y) =
P(x, y)
1 −x −y,
where P(x, y) = Q∞
i=2

1 −xi −yi−1. It is easy to compute that for a direction
(r, s) with positive coordinates the unique critical point on V1−x−y occurs at
w =
 r
r+s,
s
r+s

. Because the coordinates of w lie in (0, 1), the polynomial
1 −xi −yi does not vanish at (x, y) = w when i > 1 and w is a smooth
strictly minimal singularity of F where P does not vanish. Theorem 9.5 and
Equation (9.7) thus imply that
ar,s ∼
P
 r
r+s,
s
r+s

√
2π
(r + s)r+s+ 1
2
rrss √rs .
◁
