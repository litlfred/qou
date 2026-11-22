---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-010-algebraic-generating-functions
section_title: "Algebraic generating functions"
section_number: null
pages: 48-58
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
A formal power series F(z) is called an algebraic power series if there ex-
ists a polynomial P(z, y) ∈C[z, y] such that P(z, F(z)) = 0. Algebraic series
2.3 Algebraic generating functions
31
are often considered to be the second simplest class of generating functions,
after rational series, to arise frequently in combinatorics. The main reason al-
gebraic series arise often is that a decomposition of the elements in a combi-
natorial class into products or disjoint unions involving smaller elements from
the same class yields an algebraic equation satisﬁed by the generating function
of the class. Perhaps the most famous example of a (non-rational) algebraic
generating function is the following.
Example 2.14 (binary trees and Catalan numbers). Let C be the class of planar
rooted binary trees, deﬁned recursively by saying that the empty tree lies in C
and every element of C with n ≥1 vertices is formed by a root vertex together
with a left subtree L ∈C and a right subtree R ∈C such that the number of
vertices in L and R sum to n −1. The counting sequence cn = |Cn| deﬁnes the
Catalan numbers; Stanley [Sta15] lists 214 combinatorial classes enumerated
by the Catalan numbers.
The recursive deﬁnition for the elements of C gives a bijection of combina-
torial classes between C and Υ ⊔R × C × C, where Υ is the combinatorial class
containing only the empty tree (to account for the case n = 0) and R is the
class containing only the tree with one node (corresponding to a root vertex).
At the generating function level, this bijection yields the algebraic equation
F(z) = 1 + zF(z)2 ,
(2.3)
which has a formal power series solution corresponding to the generating func-
tion C(z) of C. To solve (2.3) in the ring of formal power series we ﬁrst ﬁnd
solutions in the ring of germs of analytic functions, since we can perform our
usual algebraic operations. The quadratic formula yields two solutions
F±(z) = 1 ±
√
1 −4z
2z
.
The solution F+(z) is not analytic at the origin, as its denominator vanishes
when z = 0 but its numerator does not, so the generating function of C is
C(z) = F−(z) = 1 −
√
1 −4z
2z
= 1 + z + 2z2 + 5z3 + · · · .
From this explicit expression, the generalized binomial theorem yields the
closed form cn =
1
n+1
2n
n

.
◁
Exercise 2.6. Deﬁne the class of d-ary until the end trees by altering the deﬁ-
nition in Example 2.14 so that each vertex has at most d children unless all the
children are leaves, in which case an arbitrary number is permitted. Adapt the
argument from Example 2.14 to compute the generating function enumerating
these trees by their number of vertices.
32
Generating functions
The kernel method
We now give an account of the kernel method, one of the most proliﬁc sources
of algebraic generating functions in combinatorics. The kernel method is a
means of producing a generating function for an array {ar} satisfying a linear
recurrence
ar =
X
s∈E
csar−s
(2.4)
for some constants {cs : s ∈E} deﬁned over a ﬁnite set E ⊂Zd, except
when r lies in a set of boundary conditions to be made precise. We will see
in Lemma 2.16 below that this recursion is well founded whenever the convex
hull of E does not intersect the non-positive orthant Rd
≤0.
If the index set E ⊆Nd then Example 2.6 generalizes to show that F(z) =
P
r∈Nd arzr is rational. The kernel method is of interest to this text because it
often produces generating functions which, even though they are not rational,
satisfy the meromorphicity assumptions that allow us to compute their asymp-
totics. It is shown in [BP00] that the complexity of F increases with the number
of coordinates in which points of E are allowed to take negative values: just as
allowing no negative coordinates in E causes F(z) to be rational, it turns out
that allowing only one negative coordinate in E causes F(z) to be algebraic
whenever the generating function encoding its initial conditions is algebraic.
When E contains points with two diﬀerent negative coordinates it is possible to
have very pathological behavior (including sequences whose generating func-
tions do not satisfy polynomial diﬀerential equations). Our presentation of the
kernel method draws heavily on [BP00].
Example 2.15 (a random walk game). Suppose two players play a game, mov-
ing their respective tokens along a track of squares by ﬂipping a fair coin at
each time step to see who moves forward one square. The second player starts
behind the ﬁrst player and the game ends as follows: if the second player passes
the ﬁrst player, the second player wins; if the ﬁrst player reaches a ﬁxed goal
square, the ﬁrst player wins; if both players are on the square immediately
preceding the goal, then it is a draw.
Let ars be the probability of a draw, when the players start at respective
distances 1 + r and 1 + r + s from the goal. For convenience we set a00 = 1
and extend our sequence to have integer indices by deﬁning ars = 0 if at least
one of r or s is negative. Conditioning on which player moves ﬁrst yields the
recursion
ars = ar,s−1 + ar−1,s+1
2
,
2.3 Algebraic generating functions
33
which is valid for all (r, s) with nonnegative coordinates except for (0, 0). Be-
cause shifting indices corresponds to multiplication of the generating func-
tion by monomials, this recurrence suggests that we multiply the generating
function F(x, y) = P arsxrys for {ars} by 1 −(1/2)y −(1/2)(x/y). Clearing de-
nominators, we let Q(x, y) = 2y −y2 −x and note from the recurrence that
all coeﬃcients of Q(x, y)F(x, y) vanish with two exceptions: the coeﬃcient
[x0y1]Q(x, y)F(x, y) = 2a0,0 −a0,−1 −a−1,1 = 2, because the recursion does not
hold at (0, 0), and the coeﬃcients [x jy0]Q(x, y)F(x, y) = 2a j,−1 −aj,−2 −aj−1,0
with j ≥1 do not vanish because only the third term is non-zero. In other
words,
Q(x, y)F(x, y) = 2y −h(x),
(2.5)
where h(x) = P
j≥1 aj−1,0x j = xF(x, 0) will not be known until we solve for F.
This generating function is in fact a simpler variant of the one derived in
[LL99] for the waiting time until the two players collide, which is needed in the
analysis of a sorting algorithm. Their solution is to observe that there is an ana-
lytic curve in a neighborhood of the origin on which Q vanishes. Solving Q = 0
for y yields two solutions, with the solution y = ξ(x) = 1 −
√
1 −x vanishing
at the origin. Since ξ(x) is analytic at the origin we also have Q(x, ξ(x)) = 0 at
the level of formal power series, and substituting y = ξ(x) in (2.5) gives
0 = Q(x, ξ(x))F(x, ξ(x)) = 2ξ(x) −h(x) .
Thus, h(x) = 2ξ(x) and
F(x, y) = 2y −ξ(x)
Q(x, y) =
2
1 +
√
1 −x −y
.
◁
An explanation of the kernel method
Let p be the valley of E, deﬁned as the coordinatewise minimum of the points
in E ∪{0} and deﬁne
Q(z) = z−p
1 −
X
s∈E
cszs
,
where the normalization by z−p guarantees that Q is a polynomial but not
divisible by any zj. We assume p , 0, since we already understand how when
p = 0 the recursion leads to a rational generating function. A set of boundary
locations is any set B ⊆Nd closed under the coordinatewise partial-order ≤,
34
Generating functions
with a corresponding set of boundary values {br : r ∈B}. We study the initial
value problem with initial conditions
ar = br for all r ∈B,
(2.6)
where the recursion (2.4) holds for all r ∈Nd\B (summands with r−s < Nd are
deﬁned to be zero). Our goal here is to take the set of shifts E, the polynomial
Q, and the sets of boundary locations and boundary values, and determine
the generating function enumerating {ar}. Figure 2.1 shows an example setup
where E = {(2, −1), (−1, 2)} and B is the y-axis. We encode the terms in each
polynomial that appears by their Newton diagrams, the set of vectors deﬁned
by the exponents of their monomials.
3
4
5
2
1
1
2
3
4
5
0
−p
r −p
r
0
(2,-1)
(-1,2)
r −s
Figure 2.1 Left: The set E and its convex hull (dashed). Right: A Newton diagram
of K (marked by ×), U (marked by ■), and B (marked by □). The quantities
K, U, B, r, s, and p are deﬁned in the text.
Let Z = Nd \ B and decompose F(z) = FZ(z) + FB(z) where
FZ(z) =
X
r∈Z
arzr
is the generating function for the indices where the recursion (2.4) holds and
FB(z) =
X
r∈B
brzr
enumerates the boundary conditions. Following the method of Example 2.15,
to apply the kernel method we study the product Q(z)FZ(z). Examining this
product shows that there are two types of terms with non-zero coeﬃcients.
• First, for every pair (r, s) with r ∈Z, s ∈E, and r −s ∈B there is a
2.3 Algebraic generating functions
35
coeﬃcient
[zr−p]Q(z)F(z)
|               {z               }
0
−[zr−p]Q(z)FB(z)
|                {z                }
−csbr−s
= csbr−s ,
where the ﬁrst extraction is zero because r ∈Z implies the recurrence (2.4)
holds, and the second extraction is computed directly. Let
K(z) =
X
r∈Z,s∈E
r−s∈B
csbr−szr−p
enumerate such terms. The K stands for known, because the coeﬃcients of
K are determined by the known boundary conditions, which are speciﬁed in
the problem. The example in Figure 2.1 marks the terms of K in the ﬁrst two
rows and columns of Z.
• Second, for every pair (r, s) with r < Z, s ∈E, and r −s ∈Z, direct
expansion shows that
[zr−p]Q(z)FZ(z) = −csar−s,
reﬂecting the fact that the recursion does not hold at r. Let
U(z) =
X
r<Z,s∈E
r−s∈Z
csar−szr−p
enumerate such terms. The U stands for unknown, because these coeﬃcients
are not explicitly determined from the boundary conditions. In the example
from Figure 2.1, U has one row and one column of terms. The value of r
leading to the xy3-term of U is pictured.
We now give a suﬃcient condition for the recurrence (2.4) to be well founded,
and prove that the series FZ and U are unique.
Lemma 2.16 ([BP00, Theorem 5]). Let E be a ﬁnite subset of Nd whose convex
hull does not intersect the non-positive orthant, let {cs : s ∈E} be constants,
let p be the valley of E, let B ⊆Nd be closed under the coordinatewise partial
order ≤with complement Z = Nd \ B, let {bs : s ∈B} be constants, and let
K(z) =
X
r∈Z,s∈E
r−s∈B
csbr−szr−p.
Then there is a unique set of values {ar : r ∈Z} such that (2.4) holds for all
r ∈Z and ar = br for all r ∈B. Consequently, there is a unique pair of formal
power series FZ and U such that
Q(z)FZ(z) = K(z) −U(z) .
36
Generating functions
Furthermore, if K is analytic in a neighborhood of the origin, then so are FZ
and U.
Proof
The convex hull of E and the closed non-positive orthant are disjoint
convex polyhedra so there is a hyperplane that separates them and meets nei-
ther. The normal vector may be perturbed slightly to obtain a rational vector v
such that v · s > 0 for all s ∈E and v · s < 0 for all s , 0 in the non-positive
orthant. The vector v must have positive coordinates and, clearing denomina-
tors, we may assume v has integer coordinates. Linearly order Nd by the value
of the dot product with v, breaking ties arbitrarily, to produce a well ordering
⪯of Nd.
If m ∈Z is ﬁxed then s ∈E and r ≺m implies r −s ≺m. Consequently,
the validity of (2.4) for all r ≺m depends only on values ar with r ≺m.
In particular, if there is a unique set of values of {ar : r ≺m} such that (2.4)
holds for r ≺m then setting r = m in (2.4) uniquely speciﬁes am. Existence
and uniqueness thus follow by induction, with the base case the minimal vector
v ∈Z under ⪯.
To show analyticity of U and FZ, let γ′ = log P
s∈E |cs|. By analyticity of
K we may choose γ′ ≥γ such that |ar| = |br| ≤exp(γ r · v) for any r ∈B.
Furthermore, for r ∈Z we have by induction that
|ar| ≤

X
s∈E
|cs|
sup
s∈E
|ar−s|
≤eγ
sup
m·v<r·v
|am|
≤eγeγ (r·v −1)
= eγ r·v ,
establishing an exponential bound on |ar| for all r ∈Nd. Analyticity of FZ(z)
follows directly, which then implies analyticity of U(z) = K(z) −Q(z)FZ(z).
□
The previous lemma is based on a formal power series approach. Another
way of thinking about this is that FZ is trying to be the power series K/Q
but, since Q vanishes at the origin, one must subtract some terms from K to
cancel whatever factor of Q vanishes at the origin. The kernel method turns this
intuition into a precise statement, when the boundary locations are speciﬁed
using the coordinatewise partial order ≥on Nd.
Theorem 2.17 ([BP00, Theorem 13]). Let d ≥2 be arbitrary and suppose
the boundary locations B are of the form {r : r ≱s} for some s ∈Nd. If the
2.3 Algebraic generating functions
37
coordinates of the valley p satisfy p1, . . . , pd−1 ≥0 > pd and the boundary
generating function K(z) is algebraic then F is algebraic.
Proof
Suppose r < Z and r −s ∈Z with s ∈E. If s′ is the vector whose ﬁrst
d −1 coordinates match s but s′
d = 0 then r < Z implies r −s′ < Z because
the complement of Z is closed under coordinatewise ≤and the hypothesis on
p implies the ﬁrst d −1 coordinates of any point in E are nonnegative. Thus,
sd −pd < rd ≤sd and it follows that U is a polynomial of degree at most pd −1
in zd.
The polynomial Q is equal to zpd
d −P
s∈E cszpd
d zs. It is convenient to regard
this as a polynomial in zd of degree at least pd, over the ﬁeld of algebraic func-
tions in z1, . . . , zd−1. We denote the roots of this polynomial by ξi(z1, . . . , zd−1)
and note that pd of the roots, counted with multiplicities, vanish at the origin
since (0, . . . , 0, j) < E for any j < 0 implies Q(0, . . . , 0, zd) has multiplicity pd
at zd = 0.
If the pd roots of Q vanishing at the origin are distinct then the equation
QFZ = K −U evaluated at each ξi leads to pd equations U(ξi) = K(ξi). The
Lagrange interpolation formula [PS98, Section V1.9] produces a polynomial
P given its values y1, . . . , yk at any k points x1, . . . , xk,
P(x) =
n
X
j=1
y j
Y
i,j
x −xi
x j −xi
.
(2.7)
Over any ﬁeld of characteristic zero, and in particular over the ﬁeld of algebraic
functions in x1, . . . , xd, this is the unique polynomial of degree at most k −
1 passing through the k points. Applying (2.7) to the pd equations U(ξi) =
K(ξi) thus uniquely determines the polynomial U. In particular, U is a rational
function of algebraic quantities, and is thus also algebraic.
If the ξi are not distinct, one has instead the pd equations
U(ξi) = K(ξi), U′(ξi) = K′(ξi), . . . , U(mi−1)(ξi) = k(mi−1)(ξi),
where mi is the multiplicity of the root ξi. One may replace the Lagrange in-
terpolation formula by the Hermite interpolation formula [IK94, Section 6.1,
Problem 10], which again gives U as a rational function of each K(ξi) and its
derivatives.
□
Restricting to d = 2 and B = {0} gives a more explicit formula for F.
Corollary 2.18. Further specialize the hypotheses of Theorem 2.17 to assume
that d = 2, the point p = (0, −p) for some p > 0, and B = {0} with boundary
value b0 = 1. Then there are exactly p formal power series ξ1(x), . . . , ξp(x)
38
Generating functions
such that ξ j(0) = 0 and Q(x, ξj(x)) = 0. Furthermore,
Q(x, y) = −C(x)
p
Y
j=1
(y −ξ j(x))
r
Y
j=1
(y −ρj(x))
for some algebraic functions C(x), ρ1(x), . . . , ρP(x) not vanishing at the origin,
and
FZ(x, y) = K(x, y) −U(x, y)
Q(x, y)
=
Qp
j=1(y −ξj(x))
Q(x, y)
=
1
−C(x) Qr
j=1(y −ρ j(x)) .
Proof
We work in the ring C{x}[y] of polynomials in y with coeﬃcients in the
ring of power series in x converging in a neighborhood of zero. The asserted
factorization of Q follows from its vanishing to order p at y = 0 and having
some degree p + r as a polynomial in y. By deﬁnition K(x, y) = yp and, recall-
ing that the degree of U(x, y) in y is at most p −1, it follows that the degree of
K(x, y) −U(x, y) in y is exactly p. Since K(x, y) −U(x, y) vanishes in a neigh-
borhood of zero when y = ξ j(x) for any j, it is divisible by Qp
j=1(y −ξj(x)).
The leading coeﬃcient of K −U is the same as the leading coeﬃcient of K,
namely 1, so K(x, y) −U(x, y) = Qp
j=1(y −ξ j(x)) as claimed.
□
Dyck, Motzkin, Schr¨oder, and generalized Dyck paths
Let S = {(r1, s1), . . . , (rk, sk)} be a set of integer vectors with rj > 0 for all j
and min j sj = −p < 0 < max j s j = P. The class A of generalized Dyck paths
starting at (0, 0) and taking steps in S consists of all ﬁnite tuples (σ1, . . . , σℓ)
of any length ℓ∈N with elements in S whose partial sums σ1 + · · · + σj for all
1 ≤j ≤ℓhave nonnegative coordinates. The elements of A can be viewed as
lattice paths starting at the origin which never go below the x-axis. The weight
of an element in (σ1, . . . , σℓ) ∈A is the endpoint (r, s) = σ1 + · · · + σℓof the
path.
Let F(x, y) = P
r,s≥0 arsxrys enumerate this class. Because a generalized
Dyck path is either empty, or is a smaller generalized Dyck path with a single
step added we obtain a recurrence of the form treated by the kernel method.
In fact, we are precisely in the situation covered by Corollary 2.18 where
Q(x, y) = yp(1−Pk
i=1 xriysi) and F(x, y) = FZ(x, y). The special case p = P = 1,
that is, vertical displacement of at most 1 per step, occurs often in classical ex-
amples.
Proposition 2.19. Assume the above setup. If p = P = 1 then the generating
2.3 Algebraic generating functions
39
Figure 2.2 A generalized Dyck path of length nine with E = {(1, 2), (1, −1)}.
function for generalized Dyck paths with steps from E is given by
F(x, y) =
ξ(x)
a(x) −C(x)ξ(x)y,
where a(x) = P
i:si=−1 xri, the algebraic function ξ(x) is the unique root of
Q(x, y) in y that vanishes at the origin, and C(x) = P
i:si=P xri.
Proof
Under these hypotheses, Q is a quadratic polynomial in y with lead-
ing coeﬃcient C(x) stated in the proposition. If ξ(x) and ρ(x) are the roots of
Q(x, y) in y then the product ξρ equals a(x)/C(x) where a(x) is stated in the
proposition. The formula in Corollary 2.18 thus simpliﬁes to
F(x, y) =
ξ(x)/a(x)
1 −[C(x)ξ(x)/a(x)]y.
□
We end this section with three of the most famous examples of lattice path
classes.
40
Generating functions
Dyck paths
r   
@
@
@
R
Motzkin paths
r   
@
@
@
R
-
Schr¨oder paths
r   
-
@
@
@
R
Figure 2.3 Legal steps for three types of paths.
• Classical Dyck paths occur when S = {(1, 1), (1, −1)}. Computing the quan-
tities in Proposition 2.19 implies
F(x, y) =
1
−x(y −ρ(x)) =
ξ(x)/x
1 −yξ(x)
where ξ(x) = (1−
√
1 −4x2)/(2x). Setting y = 0 proves the well-known fact
that the Dyck paths coming back to the x-axis at (2n, 0) are counted by the
Catalan number cn.
• Motzkin paths occur when S = {(1, 1), (1, 0), (1, −1)}, ultimately giving the
generating function
F(x, y) =
2
1 −x +
√
1 −2x −3x2 −2xy
.
• Schr¨oder paths occur when S = {(1, 1), (2, 0), (1, −1)}, ultimately giving the
generating function
F(x, y) =
2
1 +
√
1 −6x2 + x4 −x2 −2xy
.
