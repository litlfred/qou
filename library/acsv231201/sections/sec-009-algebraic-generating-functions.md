---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-009-algebraic-generating-functions
section_title: "Algebraic generating functions"
section_number: null
pages: 48-69
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
doc_brief: "Analytic Combinatorics in Several Variables — 85 sections: Preface to the second edition; List of Symbols; Introduction"
---
A formal power series F(z) is called an algebraic power series if there ex-
ists a polynomial P(z, y)∈ C[z, y] such that P(z, F(z)) = 0. Algebraic series
2.3 Algebraic generating functions 31
are often considered to be the second simplest class of generating functions,
after rational series, to arise frequently in combinatorics. The main reason al-
gebraic series arise often is that a decomposition of the elements in a combi-
natorial class into products or disjoint unions involving smaller elements from
the same class yields an algebraic equation satisﬁed by the generating function
of the class. Perhaps the most famous example of a (non-rational) algebraic
generating function is the following.
Example 2.14 (binary trees and Catalan numbers). LetC be the class of planar
rooted binary trees, deﬁned recursively by saying that the empty tree lies inC
and every element ofC with n≥ 1 vertices is formed by a root vertex together
with a left subtree L∈C and a right subtree R∈C such that the number of
vertices in L and R sum to n− 1. The counting sequence cn =|Cn| deﬁnes the
Catalan numbers; Stanley [Sta15] lists 214 combinatorial classes enumerated
by the Catalan numbers.
The recursive deﬁnition for the elements ofC gives a bijection of combina-
torial classes betweenC and Υ⊔R×C×C , where Υ is the combinatorial class
containing only the empty tree (to account for the case n = 0) andR is the
class containing only the tree with one node (corresponding to a root vertex).
At the generating function level, this bijection yields the algebraic equation
F(z) = 1 + zF(z)2, (2.3)
which has a formal power series solution corresponding to the generating func-
tion C(z) ofC. To solve (2.3) in the ring of formal power series we ﬁrst ﬁnd
solutions in the ring of germs of analytic functions, since we can perform our
usual algebraic operations. The quadratic formula yields two solutions
F±(z) = 1±
√
1− 4z
2z .
The solution F+(z) is not analytic at the origin, as its denominator vanishes
when z = 0 but its numerator does not, so the generating function ofC is
C(z) = F−(z) = 1−
√
1− 4z
2z = 1 + z + 2z2 + 5z3 +··· .
From this explicit expression, the generalized binomial theorem yields the
closed form cn = 1
n+1
(2n
n
)
. ◁
Exercise 2.6. Deﬁne the class of d-ary until the end trees by altering the deﬁ-
nition in Example 2.14 so that each vertex has at mostd children unless all the
children are leaves, in which case an arbitrary number is permitted. Adapt the
argument from Example 2.14 to compute the generating function enumerating
these trees by their number of vertices.
32 Generating functions
The kernel method
We now give an account of thekernel method, one of the most proliﬁc sources
of algebraic generating functions in combinatorics. The kernel method is a
means of producing a generating function for an array {ar} satisfying a linear
recurrence
ar =
∑
s∈E
csar−s (2.4)
for some constants {cs : s ∈ E} deﬁned over a ﬁnite set E ⊂ Zd, except
whenr lies in a set of boundary conditions to be made precise. We will see
in Lemma 2.16 below that this recursion is well founded whenever the convex
hull of E does not intersect the non-positive orthantRd
≤0.
If the index set E⊆ Nd then Example 2.6 generalizes to show that F(z) =∑
r∈Nd arzr is rational. The kernel method is of interest to this text because it
often produces generating functions which, even though they are not rational,
satisfy the meromorphicity assumptions that allow us to compute their asymp-
totics. It is shown in [BP00] that the complexity ofF increases with the number
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
2 ,
2.3 Algebraic generating functions 33
which is valid for all (r, s) with nonnegative coordinates except for (0, 0). Be-
cause shifting indices corresponds to multiplication of the generating func-
tion by monomials, this recurrence suggests that we multiply the generating
function F(x, y) = ∑ ars xrys for{ars} by 1− (1/2)y− (1/2)(x/y). Clearing de-
nominators, we let Q(x, y) = 2y− y2− x and note from the recurrence that
all coe ﬃcients of Q(x, y)F(x, y) vanish with two exceptions: the coe ﬃcient
[x0y1]Q(x, y)F(x, y) = 2a0,0− a0,−1− a−1,1 = 2, because the recursion does not
hold at (0, 0), and the coeﬃcients [x jy0]Q(x, y)F(x, y) = 2a j,−1− a j,−2− a j−1,0
with j ≥ 1 do not vanish because only the third term is non-zero. In other
words,
Q(x, y)F(x, y) = 2y− h(x), (2.5)
where h(x) = ∑
j≥1 a j−1,0x j = xF(x, 0) will not be known until we solve for F.
This generating function is in fact a simpler variant of the one derived in
[LL99] for the waiting time until the two players collide, which is needed in the
analysis of a sorting algorithm. Their solution is to observe that there is an ana-
lytic curve in a neighborhood of the origin on whichQ vanishes. Solving Q = 0
for y yields two solutions, with the solution y = ξ(x) = 1−
√
1− x vanishing
at the origin. Sinceξ(x) is analytic at the origin we also have Q(x,ξ (x)) = 0 at
the level of formal power series, and substituting y =ξ(x) in (2.5) gives
0 = Q(x,ξ (x))F(x,ξ (x)) = 2ξ(x)− h(x).
Thus, h(x) = 2ξ(x) and
F(x, y) = 2y−ξ(x)
Q(x, y) = 2
1 +
√
1− x− y
.
◁
An explanation of the kernel method
Letp be the valley of E, deﬁned as the coordinatewise minimum of the points
in E∪{ 0} and deﬁne
Q(z) =z−p
1−
∑
s∈E
cszs
 ,
where the normalization by z−p guarantees that Q is a polynomial but not
divisible by any z j. We assumep, 0, since we already understand how when
p = 0 the recursion leads to a rational generating function. A set of boundary
locations is any set B⊆ Nd closed under the coordinatewise partial-order ≤,
34 Generating functions
with a corresponding set of boundary values{br :r∈ B}. We study the initial
value problem with initial conditions
ar = br for allr∈ B, (2.6)
where the recursion (2.4) holds for allr∈Nd\B (summands withr−s<Nd are
deﬁned to be zero). Our goal here is to take the set of shifts E, the polynomial
Q, and the sets of boundary locations and boundary values, and determine
the generating function enumerating{ar}. Figure 2.1 shows an example setup
where E ={(2,−1), (−1, 2)} and B is the y-axis. We encode the terms in each
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
r − p
r
0
(2,-1)
(-1,2)
r − s
Figure 2.1 Left: The set E and its convex hull (dashed).Right: A Newton diagram
of K (marked by ×), U (marked by ■), and B (marked by □). The quantities
K, U, B,r,s, andp are deﬁned in the text.
Let Z =Nd\ B and decompose F(z) = FZ(z) + FB(z) where
FZ(z) =
∑
r∈Z
arzr
is the generating function for the indices where the recursion (2.4) holds and
FB(z) =
∑
r∈B
brzr
enumerates the boundary conditions. Following the method of Example 2.15,
to apply the kernel method we study the product Q(z)FZ(z). Examining this
product shows that there are two types of terms with non-zero coeﬃcients.
• First, for every pair ( r,s) with r ∈ Z,s ∈ E, and r−s ∈ B there is a
2.3 Algebraic generating functions 35
coeﬃcient
[zr−p]Q(z)F(z)|               {z               }
0
− [zr−p]Q(z)FB(z)|                {z                }
−csbr−s
= csbr−s,
where the ﬁrst extraction is zero becauser∈ Z implies the recurrence (2.4)
holds, and the second extraction is computed directly. Let
K(z) =
∑
r∈Z,s∈E
r−s∈B
csbr−szr−p
enumerate such terms. The K stands for known, because the coeﬃcients of
K are determined by the known boundary conditions, which are speciﬁed in
the problem. The example in Figure 2.1 marks the terms ofK in the ﬁrst two
rows and columns of Z.
• Second, for every pair ( r,s) with r < Z,s ∈ E, and r−s ∈ Z, direct
expansion shows that
[zr−p]Q(z)FZ(z) =−csar−s,
reﬂecting the fact that the recursion does not hold atr. Let
U(z) =
∑
r<Z,s∈E
r−s∈Z
csar−szr−p
enumerate such terms. TheU stands for unknown, because these coeﬃcients
are not explicitly determined from the boundary conditions. In the example
from Figure 2.1, U has one row and one column of terms. The value of r
leading to the xy3-term of U is pictured.
We now give a suﬃcient condition for the recurrence (2.4) to be well founded,
and prove that the series FZ and U are unique.
Lemma 2.16 ([BP00, Theorem 5]). Let E be a ﬁnite subset ofNd whose convex
hull does not intersect the non-positive orthant, let {cs :s∈ E} be constants,
letp be the valley of E, let B⊆Nd be closed under the coordinatewise partial
order≤ with complement Z =Nd\ B, let{bs :s∈ B} be constants, and let
K(z) =
∑
r∈Z,s∈E
r−s∈B
csbr−szr−p.
Then there is a unique set of values {ar :r∈ Z} such that (2.4) holds for all
r∈ Z and ar = br for allr∈ B. Consequently, there is a unique pair of formal
power series FZ and U such that
Q(z)FZ(z) = K(z)− U(z).
36 Generating functions
Furthermore, if K is analytic in a neighborhood of the origin, then so are F Z
and U.
Proof The convex hull of E and the closed non-positive orthant are disjoint
convex polyhedra so there is a hyperplane that separates them and meets nei-
ther. The normal vector may be perturbed slightly to obtain a rational vectorv
such thatv·s> 0 for alls∈ E andv·s< 0 for alls, 0 in the non-positive
orthant. The vectorv must have positive coordinates and, clearing denomina-
tors, we may assumev has integer coordinates. Linearly orderNd by the value
of the dot product withv, breaking ties arbitrarily, to produce a well ordering
≼ ofNd.
Ifm∈ Z is ﬁxed thens∈ E andr≺m impliesr−s≺m. Consequently,
the validity of (2.4) for all r≺ m depends only on values ar withr≺ m.
In particular, if there is a unique set of values of{ar :r≺m} such that (2.4)
holds forr≺m then settingr =m in (2.4) uniquely speciﬁes am. Existence
and uniqueness thus follow by induction, with the base case the minimal vector
v∈ Z under≼.
To show analyticity of U and FZ, let γ′ = log∑
s∈E|cs|. By analyticity of
K we may choose γ′≥ γ such that|ar| =|br|≤ exp(γr·v) for any r∈ B.
Furthermore, forr∈ Z we have by induction that
|ar|≤

∑
s∈E
|cs|
 sup
s∈E
|ar−s|
≤ eγ sup
m·v<r·v
|am|
≤ eγeγ (r·v− 1)
= eγr·v,
establishing an exponential bound on|ar| for allr∈Nd. Analyticity of FZ(z)
follows directly, which then implies analyticity of U(z) = K(z)− Q(z)FZ(z).
□
The previous lemma is based on a formal power series approach. Another
way of thinking about this is that FZ is trying to be the power series K/Q
but, since Q vanishes at the origin, one must subtract some terms from K to
cancel whatever factor ofQ vanishes at the origin. The kernel method turns this
intuition into a precise statement, when the boundary locations are speciﬁed
using the coordinatewise partial order≥ onNd.
Theorem 2.17 ([BP00, Theorem 13]) . Let d ≥ 2 be arbitrary and suppose
the boundary locations B are of the form {r :r ≱s} for somes∈ Nd. If the
2.3 Algebraic generating functions 37
coordinates of the valley p satisfy p 1,..., pd−1 ≥ 0 > pd and the boundary
generating function K(z) is algebraic then F is algebraic.
Proof Supposer< Z andr−s∈ Z withs∈ E. Ifs′ is the vector whose ﬁrst
d− 1 coordinates matchs buts′
d = 0 thenr < Z impliesr−s′ < Z because
the complement of Z is closed under coordinatewise≤ and the hypothesis on
p implies the ﬁrst d− 1 coordinates of any point in E are nonnegative. Thus,
sd− pd < rd≤ sd and it follows that U is a polynomial of degree at most pd− 1
in zd.
The polynomial Q is equal to zpd
d − ∑
s∈E cszpd
d zs. It is convenient to regard
this as a polynomial in zd of degree at least pd, over the ﬁeld of algebraic func-
tions in z1,..., zd−1. We denote the roots of this polynomial byξi(z1,..., zd−1)
and note that pd of the roots, counted with multiplicities, vanish at the origin
since (0,..., 0, j)< E for any j< 0 implies Q(0,..., 0, zd) has multiplicity pd
at zd = 0.
If the pd roots of Q vanishing at the origin are distinct then the equation
QFZ = K− U evaluated at each ξi leads to pd equations U(ξi) = K(ξi). The
Lagrange interpolation formula [PS98, Section V1.9] produces a polynomial
P given its values y1,..., yk at any k points x1,..., xk,
P(x) =
n∑
j=1
y j
∏
i, j
x− xi
x j− xi
. (2.7)
Over any ﬁeld of characteristic zero, and in particular over the ﬁeld of algebraic
functions in x1,..., xd, this is the unique polynomial of degree at most k−
1 passing through the k points. Applying (2.7) to the pd equations U(ξi) =
K(ξi) thus uniquely determines the polynomial U. In particular, U is a rational
function of algebraic quantities, and is thus also algebraic.
If theξi are not distinct, one has instead the pd equations
U(ξi) = K(ξi), U′(ξi) = K′(ξi), ... , U(mi−1)(ξi) = k(mi−1)(ξi),
where mi is the multiplicity of the root ξi. One may replace the Lagrange in-
terpolation formula by the Hermite interpolation formula [IK94, Section 6.1,
Problem 10], which again gives U as a rational function of each K(ξi) and its
derivatives. □
Restricting to d = 2 and B ={0} gives a more explicit formula for F.
Corollary 2.18. Further specialize the hypotheses of Theorem 2.17 to assume
that d = 2, the pointp = (0,−p) for some p > 0, and B ={0} with boundary
value b 0 = 1. Then there are exactly p formal power series ξ1(x),...,ξ p(x)
38 Generating functions
such thatξ j(0) = 0 and Q(x,ξ j(x)) = 0. Furthermore,
Q(x, y) =−C(x)
p∏
j=1
(y−ξ j(x))
r∏
j=1
(y−ρ j(x))
for some algebraic functions C(x),ρ 1(x),...,ρ P(x) not vanishing at the origin,
and
FZ(x, y) = K(x, y)− U(x, y)
Q(x, y) =
∏p
j=1(y−ξ j(x))
Q(x, y) = 1
−C(x)∏r
j=1(y−ρ j(x)).
Proof We work in the ringC{x}[y] of polynomials iny with coeﬃcients in the
ring of power series in x converging in a neighborhood of zero. The asserted
factorization of Q follows from its vanishing to order p at y = 0 and having
some degree p + r as a polynomial in y. By deﬁnition K(x, y) = yp and, recall-
ing that the degree of U(x, y) in y is at most p− 1, it follows that the degree of
K(x, y)− U(x, y) in y is exactly p. Since K(x, y)− U(x, y) vanishes in a neigh-
borhood of zero when y = ξ j(x) for any j, it is divisible by ∏p
j=1(y−ξ j(x)).
The leading coeﬃcient of K− U is the same as the leading coe ﬃcient of K,
namely 1, so K(x, y)− U(x, y) = ∏p
j=1(y−ξ j(x)) as claimed. □
Dyck, Motzkin, Schr¨oder, and generalized Dyck paths
Let S ={(r1, s1),..., (rk, sk)} be a set of integer vectors with r j > 0 for all j
and min j s j =−p< 0< max j s j = P. The classA of generalized Dyck paths
starting at (0, 0) and taking steps in S consists of all ﬁnite tuples (σ1,..., σ𝓁)
of any length𝓁∈N with elements in S whose partial sumsσ1 +··· +σ j for all
1≤ j≤ 𝓁 have nonnegative coordinates. The elements ofA can be viewed as
lattice paths starting at the origin which never go below thex-axis. The weight
of an element in (σ1,..., σ𝓁)∈A is the endpoint (r, s) =σ1 +··· +σ𝓁 of the
path.
Let F(x, y) = ∑
r,s≥0 ars xrys enumerate this class. Because a generalized
Dyck path is either empty, or is a smaller generalized Dyck path with a single
step added we obtain a recurrence of the form treated by the kernel method.
In fact, we are precisely in the situation covered by Corollary 2.18 where
Q(x, y) = yp(1−∑k
i=1 xriysi) and F(x, y) = FZ(x, y). The special case p = P = 1,
that is, vertical displacement of at most 1 per step, occurs often in classical ex-
amples.
Proposition 2.19. Assume the above setup. If p = P = 1 then the generating
2.3 Algebraic generating functions 39
Figure 2.2 A generalized Dyck path of length nine with E ={(1, 2), (1,−1)}.
function for generalized Dyck paths with steps from E is given by
F(x, y) = ξ(x)
a(x)− C(x)ξ(x)y,
where a(x) = ∑
i:si=−1 xri, the algebraic function ξ(x) is the unique root of
Q(x, y) in y that vanishes at the origin, and C(x) = ∑
i:si=P xri.
Proof Under these hypotheses, Q is a quadratic polynomial in y with lead-
ing coeﬃcient C(x) stated in the proposition. If ξ(x) and ρ(x) are the roots of
Q(x, y) in y then the product ξρ equals a(x)/C(x) where a(x) is stated in the
proposition. The formula in Corollary 2.18 thus simpliﬁes to
F(x, y) = ξ(x)/a(x)
1− [C(x)ξ(x)/a(x)]y.
□
We end this section with three of the most famous examples of lattice path
classes.
40 Generating functions
Dyck paths
r 
 
  
@
@
@ R
Motzkin paths
r 
 
  
@
@
@ R
-
Schr¨oder paths
r 
 
  
-
@
@
@ R
Figure 2.3 Legal steps for three types of paths.
• Classical Dyck paths occur when S ={(1, 1), (1,−1)}. Computing the quan-
tities in Proposition 2.19 implies
F(x, y) = 1
−x(y−ρ(x)) = ξ(x)/x
1− yξ(x)
whereξ(x) = (1−
√
1− 4x2)/(2x). Setting y = 0 proves the well-known fact
that the Dyck paths coming back to the x-axis at (2n, 0) are counted by the
Catalan number cn.
• Motzkin paths occur when S ={(1, 1), (1, 0), (1,−1)}, ultimately giving the
generating function
F(x, y) = 2
1− x +
√
1− 2x− 3x2− 2xy
.
• Schr¨oder paths occur when S ={(1, 1), (2, 0), (1,−1)}, ultimately giving the
generating function
F(x, y) = 2
1 +
√
1− 6x2 + x4− x2− 2xy
.
2.4 D-ﬁnite generating functions and diagonals
The more explicitly a generating function is described, the better the prospects
are for extracting information from it. This includes not only exact formu-
lae and asymptotic estimation, but also additional properties like bijections to
other classes and random sampling algorithms for objects in the class. Ratio-
nal generating functions (with coeﬃcients in the integers or rational numbers)
2.4 D-ﬁnite generating functions and diagonals 41
are easy to work with because they are speciﬁed by the ﬁnite data of their
numerator and denominator polynomials.
We have seen that some common and very natural combinatorial operations
take us from the class of rational functions to the larger class of algebraic gen-
erating functions. Algebraic functions also have canonical representations: if
f is algebraic then there is a minimal polynomial P for which P( f (z),z) = 0
and the series f may be speciﬁed by writing down the coeﬃcients of P, which
are themselves polynomials and therefore ﬁnitely speciﬁed, and enough initial
terms to uniquely determine f among all roots of P. In Chapter 8 we discuss
techniques in computational algebra that allow one to manipulate algebraic
quantities implicitly using symbolic methods, making the class of algebraic
generating functions reasonably nice to work with. There are, however, com-
mon combinatorial operations that take us out of the class of algebraic func-
tions, and this drives us to consider a more general class of generating functions
involving diﬀerential equations. A more complete discussion of the hierarchy
for univariate generating functions may be found in [Mel21, Chapter 2] and
[Sta99, Chapter 6].
Rational 
Algebraic
D−finite
Figure 2.4 Common classes of generating functions.
42 Generating functions
Univariate D-ﬁnite functions
Because any formal power series with a non-zero constant is invertible, the
ﬁeld of fractions ofC[[z]] is the ﬁeld of formal Laurent series
C((z)) =

∑
n≥κ
anzn :κ∈Z and an∈C for all n

containing series with a ﬁnite number of terms with negative exponents, where
addition is still deﬁned termwise and multiplication is still deﬁned by convo-
lution. Section 6.1 gives further information on Laurent series.
Deﬁnition 2.20. A formal power series f (z)∈ C[[z]] is a D-ﬁnite series if
and only if there is an integer m and polynomials P0(z),..., Pm(z)∈C[z] with
Pm(z), 0 such that
P0(z) f (z) + P1(z) f′(z) +··· + Pm(z) f (m)(z) = 0. (2.8)
Equivalently, f is D-ﬁnite if and only if f and its derivatives span a ﬁnite
dimensional vector space inC((z)) over the ﬁeldC(z) of rational functions.
Remark. The more natural deﬁnition of a D-ﬁnite series is one whose deriva-
tives span a ﬁnite dimensional space over the polynomial ring C[z]. Vector
spaces over ﬁelds are simpler than modules over rings, so we phrase this in
terms of vector space dimension over the rational functions instead. This re-
quires that the rational functions act on C[[z]], which requires us to extend
C[[z]] toC((z)).
Remark. If f (z) is a formal power series that satisﬁes a non-homogeneous
linear equation
P0(z) f (z) + P1(z) f′(z) +··· + Pm(z) f (m)(z) = P(z)
with P(z), P0(z),..., Pm(z)∈C[z] then repeated diﬀerentiation proves that f (z)
is D-ﬁnite.
Variants of this deﬁnition are discussed in [Sta99, Proposition 6.4.1]. The
Venn diagram in Figure 2.4 depicting the hierarchy of generating function class
is justiﬁed by the following classical proposition.
Proposition 2.21. If f (z)∈C[[z]] is algebraic then f (z) is D-ﬁnite.
Proof Since f (z) is algebraic there exists P(z, y) = ∑m
j=0 P j(z)y j ∈ C[z, y]
such that P(z, f (z)) = 0. Assume P is selected among all such polynomials
to have minimal degree in y, so that the partial derivative Py(z, y), which has
2.4 D-ﬁnite generating functions and diagonals 43
smaller degree in y than P(z, y), is non-zero wheny = f (z). Implicit diﬀerentia-
tion of the equation P(z, f (z)) = 0 shows that Pz(z, f (z)) + f′(z)Py(z, f (z)) = 0,
so Py(z, f (z)), 0 implies
f′(z) =− Pz(z, f (z))
Py(z, f (z)). (2.9)
We have now shown thatf′(z) lies in the ﬁeld of fractions of the ringC[z][ f ].
The quotient rule thus implies that the derivative of any element of the ﬁeld
extensionC(z, f ) is again in C(z, f ), so induction implies all derivatives of f
are inC(z, f ). Because f is algebraic,C(z, f ) is a ﬁnite extension ofC(z). Thus,
f and its derivatives span a ﬁnite vector space overC(z), and f is D-ﬁnite. □
Recall that a series f = ∑∞
n=0 anzn is rational if and only if the sequence
{an : n≥ 0} satisﬁes a linear recurrence with constant coeﬃcients. There is no
equivalent linear characterization for the coe ﬃcients of algebraic generating
functions, but there is for D-ﬁnite functions.
Deﬁnition 2.22 (P-recursiveness). A univariate sequence{an : n≥ 0} is said
to be a P-recursive sequence (or polynomially recursive) if there exist polyno-
mials P0(n),..., Pr(n)∈C[n] with Pm(n), 0 such that
Pr(n)an+r + Pr−1(n)an+r−1 +··· + P0(n)an = 0 (2.10)
for all n≥ 0.
Example 2.23. If an = 1/n! then{an} is P-recursive as (n + 1)an+1− an = 0 for
all n≥ 0. Furthermore, if f (z) enumerates{an} then ∑
n≥0(n + 1)an+1zn = f′(z),
so f′(z)− f (z) = 0 and f is D-ﬁnite. We can compute f by solving this linear
diﬀerential equation with the initial condition a0 = 1, obtaining the expected
solution f (z) = ez = ∑
n≥0 zn/n!. ◁
The correspondence between P-recursive sequences and D-ﬁnite series is a
classical result, known at least as far back as Frobenius’s work on computing
series solutions to ordinary diﬀerential equations.
Theorem 2.24 (P-recursive corresponds to D-ﬁnite). A sequence{an : n≥ 0}
is P-recursive if and only if its generating function f(z) = ∑∞
n=0 anzn is D-ﬁnite.
Proof First, suppose f is D-ﬁnite and satisﬁes (2.8). Diﬀerentiating the power
series for f shows that for any n∈ N and k∈ [n] the coeﬃcient [zn−k] f ( j)(z)
equals (n− k + j) jan−k+ j, where ( u) j := u(u− 1)··· (u− j + 1) denotes the
falling factorial. Let bk, j = [zk]P j(z) and let D denote the maximum degree of
the coeﬃcient polynomials P0(z),..., Pm(z). Then for anyn≥ 0, extracting the
44 Generating functions
coeﬃcient of zn in (2.8) gives the linear equation
m∑
j=0
D∑
k=0
bk, j (n− k + j) j an−k+ j = 0
having polynomial coeﬃcients in n of degrees at most m. This is a non-trivial
linear recurrence for{an}, because for any k such that bk,m = [zk]Pm(z), 0 the
coeﬃcient of an−k+m is bm,knm + O(nm−1), 0.
Conversely, suppose that{an} is P-recursive and satisﬁes (2.10). The set of
falling-factorial polynomials{(n + j) j : j≥ 0} forms a basis for C[n] which
is triangular with respect to the basis{n j : j≥ 0}, hence each Pk(n) is a ﬁnite
linear combination Pk(n) = ∑
j ck, j(n + j) j and substitution into (2.10) yields
m∑
k=0
deg Pk∑
j=0
ck, j (n + j) jan+k = 0.
The rules for di ﬀerentiating formal power series extend to the di ﬀerentiation
of Laurent series, and imply that the coeﬃcient of zn in the repeated derivative
(z j−k f (z))( j) is (n + j) j an+k. Multiplying our last equality by zn and summing
over all values of n thus gives the relation
m∑
k=0
deg Pk∑
j=0
ck, j
(
z j−k f (z)
)( j)
= 0.
Using the product rule, this becomes a non-trivial linear ODE in f (z) with
coeﬃcients in C[z, z−1], and multiplying through by a su ﬃciently high power
of z proves that f (z) is D-ﬁnite. □
Multivariate D-ﬁnite functions
Generalizing the univariate deﬁnition, a multivariate formal power seriesf (z)∈
C[[z]] is called a D-ﬁnite sequence when f and all its iterated partial deriva-
tives generate a ﬁnite dimensional vector space over C(z). The correct ana-
logue of P-recursiveness in the multivariate case is not as obvious: the fol-
lowing deﬁnition, recursive in the dimension d, comes from [Lip89, Deﬁni-
tion 3.2].
Deﬁnition 2.25 (P-recursiveness in arbitrary dimension). Suppose d > 1 and
P-recursiveness has been deﬁned for arrays of dimension d− 1. Then the mul-
tivariate sequence{ar :r∈Nd} is said to be a P-recursive sequence if there is
some positive integer k such that the following two conditions hold.
2.4 D-ﬁnite generating functions and diagonals 45
(i) For each j∈ [d] there are polynomials
{
P j
τ (n) :τ∈{ 0,..., k}d
}
, not all
zero, such that
∑
τ∈{0,...,k}d
P j
τ (r j)ar−τ = 0 for all r1,..., rd≥ k.
(ii) All the ( d− 1)-variate arrays obtained from{ar} by holding one of the d
indices ﬁxed at a value less than k are P-recursive.
The following result, proved in [Lip89, Theorem 31], shows that this deﬁni-
tion of P-recursiveness is the correct one.
Theorem 2.26. The array{ar :r∈Nd} is P-recursive if and only if its gener-
ating function f (z) = ∑
r arzr is D-ﬁnite. □
2.4.1 Diagonals
D-ﬁnite generating functions are ﬁnitely speciﬁable, the arrays they enumerate
satisfy nice recursions, and they appear often in combinatorics. In addition,
D-ﬁnite functions form an interesting family to study because they satisfy nice
closure properties. First, we note that D-ﬁnite functions are closed under addi-
tion and multiplication, just like rational and algebraic functions.
Theorem 2.27. If f (z) and g (z) are D-ﬁnite then so are f (z) + g(z) and
f (z)g(z).
Proof Let V be theC(z)-subspace ofC((z)) spanned by f (z)+g(z) and all its
derivatives. ThenV is contained in the sum of subspacesV f +Vg spanned by the
derivatives of f and g. Hence, V is a ﬁnite-dimensional space with dimension
at most dim(V f ) + dim(Vg) and f (z) + g(z) is D-ﬁnite.
Similarly, the products f (r)(z)g(s)(z) of the partial derivatives of f and g
span a ﬁnite dimensional space W of dimension at most dim( V f )· dim(Vg).
By the product rule, every derivative of f (z)g(z) lies in W, so f (z)g(z) is
D-ﬁnite. □
A more interesting closure property has to do withdiagonals of multivariate
series.
Deﬁnition 2.28 (diagonal of a formal power series) . Let F(z) = ∑
r∈Nd arzr
be a formal power series ands∈Rd be a ﬁxed vector. Thes-diagonal of F is
the univariate series
(∆sF)(z1) :=
∑
n≥0
anszn
1
consisting of the series coe ﬃcients of F whose indices are multiples of s,
46 Generating functions
where ans = 0 if ns < Nd (so the s-diagonal is only non-trivial when s has
nonnegative rational coordinates). When s = 1 thes-diagonal of F is called
the main diagonal and denoted diag F or ∆F. For 1≤ i < j≤ d the (zi, z j)-
elementary diagonal of F is the formal power series
(∆zi=z j F)(z1,..., z j−1, z j+1,..., zd)
obtained by taking the terms ofF where the exponent ofzi equals the exponent
of z j and setting z j = 1. Note that the main diagonal of F can be computed by
taking d− 1 elementary diagonals.
Exercise 2.7. Show that if f (x) is the diagonal of F(x, y) then it is also the
diagonal of F(−x,−y).
Example 2.29. Consider the generating function
F(x, y, z) = 1
1− x− y− z =
∑
r,s,t≥0
(r + s + t)!
r!s!t! xryszt
enumerating the trinomial coeﬃcients. Then the (x, y)-elementary diagonal of
F is the series
(∆x=yF)(x, z) =
∑
r,t≥0
(2r + t)!
(r!)2 t! xrzt,
while the main diagonal is
(∆F)(x) =
∑
n≥0
(3n)!
(n!)3 xn = 1 + 6x + 90x2 +··· .
◁
Exercise 2.8. Let F(x, y) = ∑
r,s≥0 ars xrys be a bivariate formal power series.
What is the diﬀerence between diag F and F(x, x)?
It is interesting to note that even though the generating function in Exam-
ple 2.29 is rational, the main diagonal∆F is transcendental (i.e., not algebraic).
Perhaps the easiest way to see this is to compute asymptotics of the diagonal
coeﬃcients using the methods of Chapter 9 and verify that they do not have
asymptotic growth compatible with being an algebraic series [Mel21, Corol-
lary 2.1].
Although the classes of rational and algebraic series are not closed under
taking diagonals, the class of D-ﬁnite series is.
Theorem 2.30(Lipshitz [Lip88]). Any elementary diagonal of a D-ﬁnite series
in d variables is a D-ﬁnite series in d − 1 variables. In particular, the main
diagonal of a D-ﬁnite series is a univariate D-ﬁnite function. □
2.4 D-ﬁnite generating functions and diagonals 47
Because many other operations on power series can be phrased as diagonals,
Theorem 2.30 ﬁnds a wide variety of applications.
Example 2.31. The Hadamard product of two formal power series F(z) =∑
r∈Nd arzr and G(z) = ∑
r∈Nd brzr is the series (F⊙ G)(z) = ∑
r∈Nd arbrzr.
The repeated diagonal expression
(F⊙ G)(z) = ∆z1=y1··· ∆zd=yd F(z)G(y)
implies that F⊙ G is D-ﬁnite whenever F and G are D-ﬁnite. See [CS98]
for an algorithm to compute an annihilating D-ﬁnite equation for F⊙ G from
annihilating D-ﬁnite equations for F and G. ◁
Exercise 2.9. Thez-constant term of an analytic series F(z, t) ∈ C[[z, t]]
is the series F(0, t)∈ C[[t]]. Prove that the z-constant term of F is the main
diagonal of F(z, z1··· zdt).
Finally, we note that the class of D-ﬁnite series is not closed under compo-
sition or division.
Exercise 2.10. Let f (x) = sin x and g(x) = 1/x. Prove that f and g are D-ﬁnite
but g( f (x)) is not.
Algebraic series and diagonals
The family of series obtained as main diagonals of rational functions appears
in many combinatorial applications, and sits naturally between the classes of
algebraic and D-ﬁnite series. Indeed, it turns out that the diagonals of bivariate
rational series form precisely the set of algebraic series. This means that com-
putation of asymptotics for the main diagonal of a bivariate rational series can
be reduced to computing asymptotics of a univariate algebraic series (see the
discussion in Section 13.1) or vice versa (see Section 9.3.1).
The proof that the diagonal of a bivariate rational series is algebraic was
sketched by Furstenberg [Fur67] and given in more detail by Hautus and Klarner
[HK71]. Because we work with series over the complex numbers, we give a
straightforward analytic proof that helps compute an annihilating polynomial
for the diagonal. Stanley [Sta99, Theorem 6.3.3] gives an algebraic proof hold-
ing over arbitrary ﬁelds.
Theorem 2.32 (bivariate diagonal extraction). If F (x, y) is a rational power
series in two variables then ∆F is algebraic.
Proof Write F(x, y) = P(x, y)/Q(x, y) for coprime polynomials P and Q with
Q(0, 0) , 0, and let h(y) = (∆F)(y). Since F converges in a neighborhood of
48 Generating functions
the origin, when|y| is suﬃciently small the functionF(z, y/z) is absolutely con-
vergent for z in some annulus A(y). Treating y as a constant, we view F(z, y/z)
as a convergent Laurent series in z inside the annulus A(y) with constant term
h(y). The Cauchy Integral Formula then gives the integral expression
h(y) = 1
2πi
∫
C
P(z, y/z)
zQ(z, y/z) dz,
where C is any positively oriented circle in the annulus of convergence A(y).
By the Residue Theorem,
h(y) =
∑
α
Res
z=α(y)
( P(z, y/z)
zQ(z, y/z)
)
, (2.11)
where the sum is over all poles α(y) inside the circle C. These residues are
all rational expressions of the poles, which are roots of Q(z, y/z), so we have
represented the diagonal as a sum of algebraic functions, which is also alge-
braic. □
Remark. Taking|y| suﬃciently small in the proof of Theorem 2.32 allows one
to pick a circle C such that the poles of the Cauchy integrand inside the circle
are precisely the roots z = α(y) of Q(z, y/z) that approach zero as y→ 0. An
annihilating polynomial for the diagonal can be computed from (2.11) using
algebraic tools like the resultant, although in low-degree cases it can usually
be computed directly.
Example 2.33 (Delannoy numbers, continued) . Recall from above that the
generating function of the Delannoy numbers is F(x, y) = 1/(1− x− y− xy),
so
x−1F(x, y/x) = 1
x− x2− y− xy
has poles at
x±(y) = 1− y±
√
1− 6y + y2
2
with only x−(y)→ 0 as y→ 0. Since x−1F(x, y/x) =−1/[(x−x−(y))(x−x+(y))],
the sequence of Delannoy numbers where both indices are equal has generating
function
(∆F)(y) = Res
x=x−(y)
x−1F(x, y/x) = −1
x−(y)− x+(y) = 1√
1− 6y + y2
.
◁
The converse of Theorem 2.32 also holds. First, we give an explicit formula
of Furstenberg [Fur67] that holds in a special case.
2.4 D-ﬁnite generating functions and diagonals 49
Proposition 2.34. Let f (x) be an algebraic univariate power series satisfying
P(x, f (x)) = 0 for some P (x, y)∈ C[x, y]. Suppose further that f (0) = 0 and
Py(0, 0), 0. Then
f (x) = ∆
(y2Py(xy, y)
P(xy, y)
)
.
The proof of Proposition 2.34 follows directly from factoring P(x, y) = (y−
f (x))u(x, y) for some u∈C[[x]][y] with u(0, 0), 0 and then examining which
terms lie on the diagonal of y2Py(xy, y)/P(xy, y).
Example 2.35. The generating function for binary trees counted by external
nodes is the shifted Catalan generating function f (x) = (1−
√
1− 4x)/2 with
minimal polynomial P(x, y) = y2− y + x. Proposition 2.34 yields the rational
function F(y, z) = y(1− 2y)/(1− x− y) whose diagonal is f (x). ◁
The hypothesis that Py(0, 0) , 0 in Proposition 2.34 restricts it to the case
where P(x, y) has a single root that passes through the origin. One natural
generalization to the multivariate setting is the following, which can be found
in [Saf00, Lemma 2].
Proposition 2.36. Let f (z) be an algebraic power series with P(z, f (z)) = 0
for some P(z, y)∈C[z, y]. Suppose further that f is divisible by z d and that in
some neighborhood of0 there is a positive integer k and factorization P(z, y) =
(y− f (z))ku(z, y) such that u(0, 0) , 0. Then f (z) is the elementary diagonal
∆zd=yF(z, y) of the rational function
F(z, y) = y2Py(z1,..., zd−1, yzd, y)
kP(z1,..., zd−1, yzd, y) .
Example 2.37. The Narayana numbers [FS09, Example III.13], deﬁned by
the explicit formula
ars = 1
r
(r
s
)( r
s− 1
)
,
are a reﬁnement of the Catalan numbers which enumerate, for example, rooted
ordered trees by edges and leaves. The Narayana generating function
f (x, y) = 1 + x(y− 1)−
√
1− 2x(y + 1) + x2(y− 1)2
2
is a root of the polynomial
P(x, y, w) = w2− w[1 + x(y− 1)] + xy = [w− f (x, y)][
w− f (x, y)
]
,
50 Generating functions
where f denotes the algebraic conjugate of f , obtained by changing the sign
in front of the square root in f . Proposition 2.36 gives the diagonal expression
f (x, y) = ∆x=w
( w(1− 2w− wx(1− y))
1− w− xy− wx(1− y)
)
.
Note that we cannot use Proposition 2.36 with respect to the variable y. ◁
The following example from [Saf00] shows that the hypotheses of Proposi-
tion 2.36 are necessary for its conclusion.
Example 2.38. Let f (x, y) = y
√
1− x− y. If f (x, y) could be expressed as the
(y, w)-elementary diagonal of a trivariate rational series F(x, y, w) then
Fyw(x, 0, 0) = [yw]F(x, y, w) = [y] f (x, y) = fy(x, 0) =
√
1− x,
contradicting the fact that
√
1− x is irrational while Fyw(x, 0, 0) is rational. ◁
To extend Proposition 2.36 to larger classes of algebraic series we can ei-
ther increase the dimension of the rational function in question, or relax our
deﬁnition of a diagonal. In the ﬁrst direction, Denef and Lipshitz proved that
every algebraic function has a rational diagonal expression in at most double
the number of variables.
Proposition 2.39 (Denef and Lipshitz [DL87, Theorem 6.2]) . If f (z) is an
algebraic power series in d variables then there exists a rational series R(z,y)
in 2d variables such that f (z) = ∆z1=y1··· ∆zd=ydR(z,y). □
In the second direction, Safonov gave an algorithm to express any algebraic
function in d variables as a generalized diagonal of a rational function in d + 1
variables.
Deﬁnition 2.40. A unimodular matrix is a matrix having integer entries and
determinant±1. Let F(z, y) = ∑
(r,s)∈Nd+1 ar,szrys be a formal power series
in d + 1 variables and let M be a unimodular d× d matrix with nonnegative
entries. The M-diagonal or generalized diagonal (with respect to M) of F is
the formal power series in d variables given by ∑
r∈Nd brzr with br = as,sd,
wheres = Mr.
Exercise 2.11. Let M =
(
1 0
1 1
)
and suppose that F(x, y) is the M-diagonal of
H(x, y, z). Express ∆F in terms of the coeﬃcients ar,s,t of H.
Theorem 2.41 (Safonov [Saf00]). Let f (z) be an algebraic function in d vari-
ables. Then there is a unimodular matrix M ∈ Nd×d and a rational function
F(z, y) in d + 1 variables such that f is the M-diagonal of F.
