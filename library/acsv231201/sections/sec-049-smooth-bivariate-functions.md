---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-049-smooth-bivariate-functions
section_title: "Smooth bivariate functions"
section_number: null
pages: 280-297
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
This section further explores bivariate rational functions, for which we can be
more explicit and give stronger results.
9.3.1 Smooth bivariate power series
We ﬁrst present a complete algorithm for bivariate power series that ﬁnds all
smooth contributing critical points, without any assumption of minimality, fol-
lowing the techniques of [DeV11; DvdHP11].
Assumption 9.1. In this section we always assume that V is smooth and Q is
square-free, so that for every (x, y) ∈V, at least one of Qx(x, y) and Qy(x, y) is
non-zero, and that the set of critical points is ﬁnite. If Q is not square-free then
our arguments characterizing the singularities that determine asymptotics still
hold when Q is replaced by its square-free part.
In any number of variables, a potential program to determine asymptotics is
the following.
1. Explicitly compute a cycle representing the intersection class.
2. Try to push the cycle below each critical point, starting at the highest.
3. When it is not possible to push past a point, describe the local cycle that is
‘snagged’ on the critical point.
4. Check whether this is a quasi-local cycle of the form we have already de-
scribed and, if so, read oﬀthe estimate from saddle point asymptotics.
This program is not generally eﬀective because the step of ‘pushing the cycle
down’ is not algorithmic, which is why we use the framework of stratiﬁed
Morse theory. However, an exception occurs when d = 2, since the cycle C has
codimension 1 in V and thus, up to a time change, there is only one way for it
to ﬂow downward.
9.3 Smooth bivariate functions
263
Fix a direction ˆr = (ˆr, ˆs) with ˆr and ˆs positive (otherwise all series coef-
ﬁcients in this direction are zero, or given by a univariate rational function,
since we consider the power series expansion of F). Because Q does not van-
ish at the origin, there exists some ε > 0 such that V = VQ does not in-
tersect the set {(x, y): |x| ≤ε, |y| ≤ε}. Now, for any c ∈R if the height
h(x, y) = −ˆr log |x| −ˆs log |y| of a point (x, y) is at least c then either |x| ≤e−c
or |y| ≤e−c. Taking c ≥log(1/ε) thus shows that no connected component of
V≥c contains both points with |x| ≤ε and points with |y| ≤ε.
On the other hand, for suﬃciently large c every connected component of
V≥c contains points with arbitrarily large height, and hence points with either
|x| ≤ε or |y| ≤ε. Thus, we may decompose V≥c for suﬃciently large c into
a disjoint union X≥c ∪Y≥c, where X≥c is the union of connected components
containing points with arbitrarily small x-coordinates and Y≥c is the union of
connected components containing points with arbitrarily small y-coordinates.
Puiseux’s Theorem states that in a suﬃciently small neighborhood of the origin
in x, with a ray from the origin removed to account for branch cuts, every
branch y(x) of Q(x, y) = 0 has a representation
y(x) =
X
j≥j0
cjx j/k
for a ﬁxed branch of the kth root, where j0 ∈Z and k is a positive integer (and
analogous representations for the branches of x in terms of y also hold). By
Rouch´e’s Theorem, projection of such a connected component to its x-value
is diﬀeomorphic as a covering to the projection of the graph of yk = Cx j for
some constant C, such a covering space being diﬀeomorphic to a punctured
disk. Thus, for any suﬃciently large c, the connected components of X≥c and
Y≥c are diﬀeomorphic to disjoint open disks with their origins removed. The
values of c such that this decomposition holds form an interval [cxy, ∞) for
some cxy ∈R.
Critical points at inﬁnity
Puiseux’s Theorem also helps characterize critical points at inﬁnity. In partic-
ular, any branch y(x) of Q(x, y) = 0 near the origin x = 0 satisﬁes
y(x) = Cxα(1 + o(1))
for some C ∈C and α ∈Q, and any branch x(y) near the origin y = 0 satisﬁes
x(y) = C′yβ(1 + o(1))
for some C′ ∈C and β ∈Q. If F(x, y) has a CPAI in the direction ˆr then either
α = −ˆr
ˆs for some branch y(x) or β = −ˆs
ˆr for some branch x(y). We thus make
the following assumption to rule out the existence of CPAI.
264
Smooth point asymptotics
Assumption 9.2 (No CPAI). For any branch y(x) = Cxα(1+o(1)) of Q(x, y) =
0 as x →0 we have α , −ˆr
ˆs and for any branch x(y) = C′yβ(1 + o(1)) of
Q(x, y) = 0 as y →0 we have β , −ˆs
ˆr.
When Assumption 9.2 holds we can be very explicit about the behavior of
the height function near the coordinate axes.
Lemma 9.27. Assume there are no CPAI. For any suﬃciently small ε > 0,
ﬁxed θ ∈[−π, π], and branch y(x) of Q(x, y) = 0 near x = 0, the parametrized
height function
hθ(t) = h

teiθ, y

teiθ
is monotonic for t ∈[0, ε]. Furthermore, if y(x) ∼Cxα as x →0 then
lim
t→0+ hθ(t) =

∞
if α > −ˆr/ˆs
−∞
if α < −ˆr/ˆs
.
Proof
Puiseux’s theorem implies we can always ﬁnd α ∈Q,C ∈C, and a
function φ with φ(x) and xφ′(x) in o(1) such that y(x) = Cxα(1 + φ(x)) as
x →0. The height function is the real part of H(x, y) = −ˆr log x −ˆs log y, so
d
dthθ(t) = cos(θ)Re Hx(x, y(x)) −sin(θ)Im Hx(x, y(x)) ,
where
Hx(x, y(x)) = −ˆr −ˆsα
x
−
φ′(x)
1 + φ(x) ∼−ˆr −ˆsα
x
.
Thus
d
dthθ(t) ∼−ˆr −ˆsα
|x|
,
which is strictly positive or strictly negative under Assumption 9.2. Finally, we
note
hθ(t) ∼log

Ct−ˆr−ˆsα
for t suﬃciently small, giving the stated asymptotic behavior.
□
Corollary 9.28. Under Assumption 9.2 the connected components of X≥c are
diﬀeomorphic to disjoint open disks with their origins removed, corresponding
to the branches y(x) ∼Cxα of Q(x, y) = 0 as x →0 with −ˆr/ˆs < α ≤0.
9.3 Smooth bivariate functions 265

Intersection cycles and flows
Fixing |x| small and expanding |y| gives a homotopy that (up to minor pertur-
bation) intersects V transversely. In particular, the intersection cycle C created
from this operation contains a positively oriented circle around the removed
origin from each of the punctured disks in X*° for c sufficiently large. As usual,
we get a residue integral expression

ays = J [[R05(5% » xt ty ld a as}
2ni Jc Ox, y)

when P and Q are polynomials. More generally, when P is an analytic function
over appropriate regions of C“ we get

1 POY) pts res
= — | Res| —— “dx Ad on
ans = f a Oany? > hry +0")

as r,s — oo, for any 6 > 0.

As we have already seen multiple times, in the absence of CPAI the topology
of V*¢ cannot change with c except at critical values. Because we work in two
dimensions, we can be very explicit about the change in topology as c passes
through a critical value.

Definition 9.29. Suppose o = (xo, yo) is a critical point where O,(o) # 0, so
that we can parametrize y = y(x) in a neighborhood of o in V. The degree of
degeneracy of Q at a is the integer k such that there is a series expansion

» C(x - w|

pak

A(x, y(x)) = h(o) + Re

in a neighborhood of x9 with c, # 0. Because o is a critical point of the
height function h, the degree of degeneracy is always at least 2, and o is a
nondegenerate critical point precisely when the degree of degeneracy is equal
to 2. Because # has no zero coordinate and o is a critical point, Q,(a) # 0 and
the degree of degeneracy is the same parametrizing by y instead of x.

If o = (X, Yo) is a critical point with degree of degeneracy k then we can
substitute y = y(x) and expand H(x, y) = —? log x — Slog y near xo to obtain

A(x, y(x)) = C + (x x0) g(x)

for some C € C and analytic function g with g(x) # 0. In particular, if w =
(x—x0)g(x)'/* then (dw/dx)(xo) # 0 and we can parametrize the height function
hin the local coordinate w near o as

h(x(w), yew) = Re [A(xGv), xxw)))] = A(o) + Re [w*].
266
Smooth point asymptotics
Thus, near σ the set V contains k disjoint ascent regions, where h increases
while moving towards σ, which alternate with k disjoint descent regions, where
h decreases while moving towards σ; this is illustrated in Figure 9.5 below.
Deﬁnition 9.30. Let cxy ∈[−∞, ∞) be the inﬁmum of all values c such that
X>c ∩Y>c = ∅(which is also the smallest value c such that X>c and Y>c are
well-deﬁned). If cxy = −∞then let W = ∅, otherwise let W be the nonempty
set of critical points σ such that h(σ) = cxy and, for any suﬃciently small
neighborhood U of σ in V, the sets U ∩X>cxy and U ∩Y>cxy are nonempty.
Our choice of the notation W comes from the following result.
Theorem 9.31. Suppose Assumptions 9.1 and 9.2 hold. If W is empty then the
intersection cycle C is in the same homology class as a cycle with maximum
height −m for all suﬃciently large m ∈R (it can be pushed down forever). If
W is nonempty then C is in the same homology class as a cycle κ such that
(i) The points of κ with maximum height are precisely the points of W.
(ii) For σ ∈W and a suﬃciently small neighborhood U of σ in V, if
A0, . . . , Ak−1 and D0, . . . , Dk−1 denote the ascent and descent regions of
κ ∩U enumerated counterclockwise such that Dj lies between Aj and
Aj+1 mod k then
κ ∩U =
k−1
X
j=0
h
X( j + 1) −X( j)
i
γ j,
where each γ j is a curve traveling downward in Dj starting at σ and
X( j) =

1
if Aj mod k ⊂X>cxy
0
if Aj mod k ⊂Y>cxy .
In particular, κ ∩U projects to a non-trivial cycle in the relative homology
group H1(U, U ∩V≤cxy−ε) for any ε > 0 suﬃciently small (so the intersection
cycle gets stuck at height cxy).
Proof
Let M ∈R be larger than all critical values of h. Then C is homologous
to closed curves in each component of X≥M, and in fact it is homologous to the
boundary ∂X≥M. First, we show that we can push down the intersection cycle
until arriving at cxy. The topology of V≥c only changes at critical values c, so
let σ be a critical value in (cxy, M] and suppose that σ is the only critical point
with h(σ) = σ.
Figure 9.3 shows V≥c (shaded) for three values of c when the degree of de-
generacy of σ is k = 2 and a circle enclosing a region where the parametriza-
tion h = σ + Re[wk] holds (higher degrees of degeneracy are similar, just with
9.3 Smooth bivariate functions
267
Figure 9.3 V≥c and its boundary for three values of c.
more components). In the top diagram c > σ, in the middle diagram c = σ,
and in the bottom c < σ, with the arrows showing the orientation of ∂V≥c
inherited from the complex structure of V.
Consider the ﬁrst picture where c > σ. Because c > cxy each of the k shaded
regions is in X≥c or Y≥c, but not both. In fact, since σ > cxy this persists in
the limit as c ↓σ, so either all k regions are in Y≥c or all k regions are in
X≥c. In the ﬁrst case ∂X≥c does not contain any critical points of h on V with
height in an interval (σ−2ε, σ+2ε), so the ﬁrst Morse Lemma implies ∂X≥σ+ε
is homotopic to ∂X≥σ−ε as desired. In the latter case, the diﬀerence between
∂V≥σ+ε and ∂V≥σ−ε is a boundary ∂B (see Figure 9.4, or Figure 9.5 below) so
these sets are still homologous. In fact, one can show they are still homotopic.
Thus, we can push the intersection cycle below any critical value above cxy
that has a single corresponding critical point, and the same argument holds
generally by working locally around each critical point of ﬁxed height larger
than cxy. In particular, if W is empty then we can push the intersection cycle
down to arbitrarily low height.
It remains only to show that the intersection cycle can be represented by
the stated cycle κ. Just as in Figure 9.3, the connected components of ∂X≥cxy+ε
will contain curves moving through a descent region of V near σ, crossing
over an ascent region, then going back out through an adjacent descent region.
However, unlike for critical points at higher height where all ascent regions are
268
Smooth point asymptotics
Figure 9.4 ∂V≥σ+ε and ∂V≥σ−ε diﬀer locally by a boundary.
covered or none were, in this case the curves will only cross the ascent regions
containing points of X>cxy; see Figure 9.5.
Figure 9.5 Left: Plot of V near a critical point with degree of degeneracy k = 3,
where V>cxy contains two ascent regions with points in X>cxy and one region with
points in Y>cxy. The set V>cxy+ε is colored gray and the part of ∂X≥cxy+ε in view is
drawn. Right: Straightening out the connected components of ∂X≥cxy+ε near this
critical point gives the stated curves γ j.
The connected components of ∂X≥cxy+ε can be straightened into rays γ j (in
terms of the local coordinate w) that stay in each descending region adjacent
to an ascending region containing points of X>cxy. If the descending region is
between ascending components containing points of Y>cxy and X>cxy, working
counterclockwise, then γ j will start at the critical point and move down the
descending region. Conversely, if the descending region is between ascend-
9.3 Smooth bivariate functions
269
ing components containing points of X>cxy and Y>cxy, working counterclock-
wise, then γj will move up the descending region to peak at the critical point.
Descending regions between two ascending regions both containing points of
X>cxy have γ j twice with opposite orientations, which can be joined and pushed
to lower height. Descending regions between two ascending regions both con-
taining points of Y>cxy are not touched by the intersection cycle. Taking these
sign considerations into account gives the stated formula for κ.
□
Theorem 9.31 immediately gives an algorithm for the bivariate case.
Algorithm 3: Determination of W in the smooth, bivariate case.
Input: Bivariate rational function F(x, y) and direction (r, s).
Output: Set of critical points W determining coeﬃcient asymptotics of
F in the (r, s) direction.
1 Verify that Assumptions 9.1 and 9.2 hold using Gr¨obner bases and Puiseux
expansions
2 List the critical value in order of decreasing height
3 Set the provisional value of cxy to the highest critical value
4 For each critical point at height cxy do
(a) Compute the order k of the critical point
(b) Follow each of the k ascent paths until it is clear whether the
x-coordinate or the y-coordinate goes to zero
(c) Add the point to the set W if and only if at least one of the k paths has
x-coordinate going to zero and at least one of the k paths has
y-coordinate going to zero
5 If W is nonempty then terminate and output cxy and W
6 Else, if cxy is not the least critical value then replace cxy by the next lower
critical value and go to step 4
7 Else, if no critical values remain then cxy = −∞, W is empty, and the
asymptotics decay super-exponentially
The doctoral dissertation [DeV11] discusses how to turn this breakdown
into eﬀective steps, and [MS22] give an implementation in Sage using interval
arithmetic. The trickiest part is Step 4b. Ascent paths could conceivably get
caught in a trap, approaching a critical point rather than continuing to height
+∞. However, this is a higher critical point, hence already known to be in
an x- or y-component. Therefore, one only needs to know a radius ε for each
higher critical point p such |w −p| < ε implies w is in the same component as
p, which can be done with interval arithmetic. We conclude this section with
270
Smooth point asymptotics
an example of the evaluation of the intersection class for a particular smooth
bivariate generating function whose analysis ﬁrst appeared in [DeV10].
Example 9.32 (bi-colored supertrees). A bi-colored supertree [FS09, Exam-
ple VI.10] is a planar binary tree with each node replaced by a bi-colored
rooted planar binary tree. The class of bi-colored supertrees is counted by the
main diagonal of the bivariate function
F(x, y) = P(x, y)
Q(x, y) = 2x2y(2x5y2 −3x3y + x + 2x2y −1)
x5y2 + 2x2y −2x3y + 4y + x −2 ,
and we give asymptotics following the algorithm above.
First, we note that there is one branch y(x) ∼(−4)x−5 of y as x →0 and
four branches x(y) of x as y →0, two of which satisfy x(y) ∼y−1/2 and two of
which have x(y) ∼−y−1/2. In particular, there are no critical points at inﬁnity in
the main diagonal direction (r, s) = (1, 1). A quick Gr¨obner basis computation
further veriﬁes that the system
Q(x, y) = Qx(x, y) = Qy(x, y) = 0
has no solution, and the smooth critical point system
Q(x, y) = xQx(x, y) −yQy(x, y) = 0
has three solutions
1 −
√
5, 3 +
√
5
16
,
 
2, 1
8
!
,
1 +
√
5, 3 −
√
5
16
,
listed here in order of decreasing height under h1/2,1/2.
The highest critical point is nondegenerate, meaning V locally has two as-
cent paths. Following both ascent paths using, for instance, the Sage package
of [MS22] shows that both contains points arbitrarily close to the x-axis, so
the intersection cycle can be pushed lower. In this case we could also simply
observe that the highest critical point cannot contribute to the asymptotics be-
cause the coordinates are real and of opposite sign. The factor x−ny−n in the
asymptotic formula for an,n would then force the signs to alternate on the diag-
onal, whereas we know the diagonal terms to be positive.
Continuing to the next-highest point we consider the point (2, 1/8). This
point has degree of degeneracy four, of which three climb to the x-axis and
one climbs to the y-axis. In particular, the point (2, 1/8) determines dominant
diagonal asymptotics and, using the notation of Theorem 9.31, the intersection
cycle is homologous to γ = γ j −γ j−1 where j is the index of the region whose
ascent region goes to the y-axis. Among the four descent regions, this path
9.3 Smooth bivariate functions
271
inhabits two consecutive ones, making a right-angle turn as it passes through
the saddle.
Finally, we evaluate the univariate integral over this cycle. To compute the
residue form in this example it is easiest to parametrize a neighborhood of
(2, 1/8) in V by the x-coordinate and use Proposition C.8 from Appendix C
with j = 2 to see that
ω = Res

F(x, y)x−n−1y−n−1dx ∧dy

=
−P(x, y)
xy(x)Qy(x, y(x)) x−ny(x)−n dx.
Moving the origin to x = 2, equals
1
2πi
Z
γ
ω = 4n
Z
γ
A(x)e−nφ(x) dx
where the series expansions for A and φ are given by
A(x) = −x3
8 −x4
16 + O(x5)
φ(x) = −x4
16 + O(x6) .
Applying Theorem 4.1 to evaluate the integral on the segment −γ j+1 using the
parametrization x = (i −1)t for 0 ≤t ≤ε gives a series for
1
2πi
R
ω that begins
4n

−i
4πn−1 + (1 + i)
√
2Γ(5/4)
8π
n−5/4 + O(n−3/2)
.
Similarly, on γj we parametrize by x = (−i −1)t and obtain the complex con-
jugate of the previous expansion,
4n

i
4πn−1 + (1 −i)
√
2Γ(5/4)
8π
n−5/4 + O(n−3/2)
.
When the two contributions are summed the ﬁrst terms cancel and we are left
with
an,n ∼4n √
2Γ(5/4)
4π
n−5/4 .
◁
9.3.2 Laurent series
In this section we discuss what can be done when the hypotheses of Algo-
rithm 3 are satisﬁed, except that the series in question is a Laurent series rather
than an ordinary power series. We ﬁrst revisit Algorithm 3 from a diﬀerent
point of view, involving intersection numbers of middle-dimensional cycles.
272 Smooth point asymptotics

Definition 9.33. Let X be a smooth, oriented real 2k-manifold, and let y, and
Y2 be two smooth, oriented k-cycles on X, intersecting transversely at finitely
many points %;,...,Z,,. The signed intersection number of y, and y2 is the
integer

m

#1, 2) = » sgn(axj),

jl
where sgn(aj) = 1 if the oriented bases B; and B» for the tangent spaces T,(y;)
and T,,(y2) form (in this order) a positively oriented basis for the tangent space
T,(X), and sgn(a;) = —1 otherwise.

The following construction can be found in [GP74] or [BJ82, pages 151-
152].

Proposition 9.34. Let X be an oriented real manifold of dimension 2k and let a
and B be smooth oriented compact cycles of dimension k. Then generic pertur-
bations of a and f will intersect transversely in a finite number of points [GP74,
Section 2.3], and the resulting signed intersection number does not depend on
the generic perturbation. In fact, the signed intersection number is an invari-
ant [GP74, Section 3.3] of the homology classes [a] and [B] in H;(X). oO

Let h be a (not necessarily proper) smooth Morse function on a complex
k-manifold X with finitely many critical points #1,..., 2, listed in order of
decreasing height h(a) > --- > h(a»), such that all critical points have middle
index k. For each j < m, let y; be a smooth cycle agreeing with the stable
manifold of the (upward) gradient flow of h in a neighborhood of a; having
x; as its highest point. Similarly, let y/ be a smooth cycle agreeing with the
unstable manifold of the gradient flow of / in a neighborhood of x; with x;
as its lowest point. The y; are absolute cycles representing attachments in the
Morse filtration at « ; (described in Appendix C). Similarly, the y/ are absolute
cycles representing attachments in the reverse Morse filtration at #;, obtained
by replacing h by —/h.

Proposition 9.35. Let L be the subspace of H,(X) generated over the complex
numbers by {{yj] : j < m} and let L* denote the dual space to L. Then {ly] :
J < mj is a basis for L* and the signed intersection number #(y;,y!) is a
nonsingular pairing whose representing matrix M is upper triangular.

Proof When i = j the cycles y; and y/ represent the stable and unstable
manifolds of the gradient flow for a Morse function at the critical point aj.
Morse functions are quadratically nondegenerate, therefore locally these inter-
sect transversely at a single point, and they cannot intersect anywhere else due
9.3 Smooth bivariate functions
273
to the height restrictions. Hence the intersection number is ±1. When i > j the
height restrictions prevent γi and γ j from intersecting at all, whence Mi j = 0,
so M is an upper triangular matrix with ±1 diagonal entries, and thus nonsin-
gular.
□
Remark 9.36. If h(x j) = h(x j+r) for r ≥1 then again the height restrictions
prevent γi from intersecting γℓwhen i and ℓare distinct elements of {j, . . . , j +
r}, hence the only non-zero entries in the submatrix M[ j,j+r],[ j, j+r] are those on
the diagonal.
Algorithm 3 may be understood in terms of this pairing, as we now sketch.
Sketched alternative proof of correctness for Algorithm 3
Suppose that some
component B′ of the complement of the amoeba of Q(x, y) contains a ray with
small x coordinate that points up in the y direction, let T be the torus of in-
tegration for the bivariate Cauchy integral, with both x- and y-radii arbitrarily
small, and let γ be the intersection cycle INT(T, T ′), where the basepoint of
T ′ still has small x-coordinate but has suﬃciently large y-coordinate to be in
B′. Then γ consists of small cycles around the points (0, s), as s ranges over
the roots of Q(0, y). Assuming these to be simple roots, the circles wind once
about the origin.
The key is to interpret Steps 4(b-c) in Algorithm 3 using intersection num-
bers. Suppose pj is a nondegenerate critical point reached by the algorithm,
with corresponding ascent path γ j. Steps 4(b-c) compute the intersection num-
ber of γ with γ j. If, among the two branches of γ, one goes to the x-axis and
one goes to the y-axis, then γ will intersect precisely one of the circles around
a point (0, s) and the intersection number will be ±1. If both branches go to
the x-axis then the intersection number is zero because they cannot intersect
any of the small circles around the points (0, s). Furthermore, the intersection
number depends only on the homology class of the intersection cycle γ and, as
shown in Corollary C.5 of Appendix C, the homology class of the intersection
cycle obtained by keeping |x| small and taking |y| to inﬁnity is the same as the
intersection cycle obtained by keeping |y| small and expanding |x| to inﬁnity.
Interpreting the intersection cycle using this second construction shows that if
both branches go to the y-axis then the intersection number is also zero.
The upshot is that in Step 4(c), the point pj is added to W if and only if
#(γ, γ j) = ±1 is non-zero. If any point at a given height is added, then all
points at that height are added for which the intersection number of the ascent
path with γ is ±1 and no lower points are added. Inverting the dual basis shows
that γ −P
i:pi∈W ±γi is zero in H1(V∗, V<cxy).
□
We now return to the case of more general Laurent series. The diﬀerence
274
Smooth point asymptotics
between these and ordinary power series is that we can no longer count on
the intersection cycle γ to be the union of small circles around points of inter-
section of V with one of the coordinate axes. The solution is to consider the
components B where the series is deﬁned and B′ where height goes to −∞and
trace an explicit intersection path γ between two points in these components.
One can then try to infer the intersection numbers #(γ, γ j) between γ and every
ascent path γ j from every critical point pj. If successful, this identiﬁes W as
the set of pj such that h(pj) is maximized among pj such that #(γ, γ j) = ±1.
Example 9.37. The generating function 1/Q(x, y), where
Q(x, y) = 3 + x + x−1 + y + y−1 + 1
2(x + x−1)(y + y−1) + 1
5(x −x−1 + y −y−1),
appears in the analysis of certain matrix inversions arising from Green’s func-
tion computations [Wan22]. Figure 9.6 shows a plot of the amoeba of Q. Its
Newton polygon is the convex hull of the 3×3 grid of lattice points with |x| ≤1
and |y| ≤1.
Figure 9.6 The amoeba of Q (reproduced with permission of Hong-Yi Wang).
The complement of the amoeba of Q has seven components, illustrated in
9.3 Smooth bivariate functions
275
Figure 9.6. Six of the components are unbounded and correspond to vertices on
the perimeter of the Newton polygon, and the seventh component is a bounded
component corresponding to the origin, which is an interior lattice point of the
Newton polygon.
Exercise 9.9. Laurent polynomials whose Newton polygons are as in Example
9.37 can have as many as nine components in the amoeba complement. How-
ever the speciﬁc Laurent polynomial Q(x, y) under consideration only admits
seven.
(a) Let Qx+(x, y) denote the sum of the three monomials in Q that have x-
degree 1. How many distinct values do the magnitudes of the roots of
Qx+(y) take?
(b) Let Qx−(x, y) denote the sum of the three monomials of Q that have x-
degree −1. How many distinct values do the magnitudes of the roots of
Qx−(y) take?
(c) Explain why there is only one amoeba ‘tentacle’ in the negative x direction
whereas there are two in the positive x direction.
Continuing our current example, the component unbounded in the (−1, −1)
direction corresponds to a power series expansion. However, the series of com-
binatorial interest in this case is the one corresponding to the bounded com-
ponent, which we call B. Speciﬁcally, asymptotics of this series in the (1, 1)
direction are desired. For the component B′ we may choose any where h(1,1)
is unbounded from below, and for speciﬁcity we choose the component in the
upper right.
A quick computation shows the variety VQ to be smooth and identiﬁes eight
critical points in the direction ˆr parallel to (1, 1). Their projections under the
Relog map are shown on the amoeba in Figure 9.6 and denoted by p1, . . . , p8.
All but two of the points, p3 and p4, are on the boundary of the amoeba, and
the four points p2 = p1 and p8 = p7 come in conjugate pairs.
As described immediately prior to the example, we choose an explicit in-
tersection cycle γ by moving the product of circles represented by the point
x ∈B to one represented by a point in B′. The size of a ﬁber amoeba−1(x)
for x ∈B only changes when crossing a point of the amoeba contour drawn in
Figure 9.6, so by sampling points and performing algebraic computations it is
possible to determine that the interior of the amoeba has four regions on which
the log-modulus map from V to amoeba(Q) is two-to-one, while the map is
four-to-one on the remainder of the amoeba (the four-to-one regions are more
heavily shaded in Figure 9.6).
To construct the intersection cycle γ, we ﬁrst choose x to be the origin and
276
Smooth point asymptotics
move it in the (1, 0) direction halfway to p5, then up and around the boundary
of the component containing p5 moving rightward to the edge of the picture
and then upward into B′. Until the very end, this traces a single path in each of
the two preimages of the log-modulus map. Therefore γ will be a single arc,
centered on the preimage of the point x′ where the amoeba was ﬁrst entered
(this boundary point having a single preimage) and extending downward until
another piece of arc appears when passing through where the preimage size is
four. This second arc can be made to occur below every critical point, therefore
as a cycle relative to −∞the cycle γ is a simple arc in the preimage size 2 region
with p5 on its boundary.
We conclude immediately that p1, p2, p3, p4, p5, and p6 do not contribute.
The ﬁrst four are in fact higher than the origin, so the upward trajectories can-
not possibly intersect the intersection cycle. For p5, it suﬃces to check that
the two upward trajectories can be drawn to be disjoint from our choice of
γ. Indeed, the two ascent arcs, projected to the amoeba, move initially in the
(−1, −1) direction, and can do so until they are higher than the highest point
on the intersection cycle. Where they go after that is unclear, because upon
entering the preimage size 4 region it is no longer clear which is the increasing
time direction, so the image of the arcs may no longer be able to move in the
(−1, −1) direction. However, they are already high enough that they cannot in-
tersect γ. By symmetry, an identical argument (choosing a diﬀerent γ) shows
that p6 cannot contribute.
By symmetry, p7 contributes if and only if p8 contributes. By process of
elimination, because we know the asymptotics are non-zero, these both con-
tribute. To argue this geometrically, one needs to understand where the two
ascent arcs from p7 go. The description in terms of the four preimages is a lit-
tle complicated, but one ﬁnds in the end that the projections of the two ascent
arcs to the amoeba pass around the hole (the region B) in opposite ways, one
to the north and one to the south. This forces the intersection number with γ to
be ±1; see [Wan22] for details.
We conclude that the intersection cycle γ is homologous to the sum of a
homology generator going downward from p7 and a homology generator going
downward from p8, with properly chosen signs. The coordinates of the critical
points are algebraic numbers satisfying
55 x8 +664 x7 +2840 x6 +5780 x5 +5610 x4 +2520 x3 +440 x2 −44 x−45 = 0 .
The points p7 and p8 are on the diagonal, conjugate to each other, with co-
ordinates −2.19 . . . ± i1.10 . . .. The two contributions have opposite phases,
9.3 Smooth bivariate functions
277
ultimately giving that
an,n ∼Cn−1/2α−n cos(nθ),
where α = 6.03 . . . is the absolute value of the product of the coordinates in p7
(or equivalently the coordinates of p8) and C and θ are non-zero constants.
◁
Exercise 9.10. Find the constants C and θ for this example.
9.3.3 Smooth Bivariate Generating Functions with Degeneracies
Using the results of Chapter 4 we can give asymptotics for bivariate smooth
point asymptotics in directions where the phase function φ vanishes to arbitrary
order. For simplicity, we consider a power series expansion and assume that
the dominant singularities are ﬁnitely minimal points where the numerator P
is nonvanishing. It is also possible to derive (more complicated) results when
these conditions fail: for instance, they fail in Example 9.32 above.
Let (x∗, y∗) be a smooth minimal critical point in the direction ˆr and assume
that Qy(x∗, y∗) , 0 so that we can parameterize y = g(x) on V near (x∗, y∗).
Theorem 9.17 and (9.16) deﬁne functions A and φ such that
xr
∗ys
∗(ars −χ) = O  e−εs ,
where
χ(r, s) = x−r
∗y−s
∗
1
2π
Z ε
−ε
e−sφ(θ)A(θ) dθ .
(9.19)
Let c = cκ denote the leading non-zero series coeﬃcient in the expansion
φ(x) ∼cκxκ as x →0 and deﬁne the quantity
Φx∗,y∗(r) = −Γ(1/κ)
2κπ (1 −ζ) P(x∗, y∗)
y∗Qy(x∗, y∗)c−1/κs−1/kx−r
∗y−s
∗,
(9.20)
where, as in Theorem 4.1(iii), ζ = −1 if κ is even and ζ = exp(σiπ/κ) if κ is
odd.
Theorem 9.38. If (x∗, y∗) is a strictly minimal critical point in the direction ˆr
and satisﬁes the conditions above then as (r, s) →∞with the distance from
(r, s) to the ray {t ˆr : t ≥0} remaining bounded, there is an asymptotic series
of the form
ars ≈x−r
∗y−s
∗
∞
X
j=0
ν js(−1−j)/k
with leading term Φx∗,y∗(r). If (x∗, y∗) is a ﬁnitely minimal point and all critical
points with the same coordinate-wise modulus satisfy the same conditions as
278
Smooth point asymptotics
(x∗, y∗) then an asymptotic series for ars is obtained by adding the contributions
of each of the critical points.
Proof
The asymptotic development follows from (9.19) and Theorem 4.1. It
remains to check that the leading term is given by (9.20). Starting from (9.19)
use Theorem 4.1 with ℓ= 0 to get, in the notation of Theorem 4.1, the leading
term
χ ∼x−r
∗y−s
∗
2π
Z ε
−ε
A(x)e−sφ(x) dx
= x−r
∗y−s
∗
2π
I(s)
= x−r
∗y−s
∗
2π
(1 −ζ)C(κ, 0)A(0)(cs)−1/κ.
Parametrizing by y means choosing coordinate k = 2 giving sign (−1)k−1 = −1
in A(0) = −P(x∗, y∗)
y∗Qy(x∗, y∗), and the fact that C(κ, 0) = Γ(1/κ)
κ
gives (9.20).
□
Example 9.39 (Cube root asymptotics). Let F(x, y) = 1/(3 −3x −y + x2) so
that the set V is parametrized by y = g(x) = x2 −3x + 3. If ˆr = (a, 1 −a) then
asymptotic behavior depends on whether a is less than, equal to, or greater than
1/2. When a < 1/2 there are two real critical points on the curve y = g(x) –
as a increases from 0 to 1/2 one approaches (1, 1) from the left, and the other
approaches (1, 1) from the right (see Figure 9.7). Only the critical point on
the right of (1, 1) is minimal, and it determines asymptotics. When a = 1/2,
the two critical points meet and h becomes quadratically degenerate. Once
a > 1/2, the critical points have complex conjugate coordinates and are both
minimal.
Because (1, 1) is a minimal point, the main diagonal has exponential rate
zero, while all other directions have exponential decay at a rate that is uni-
form over compact subsets of directions not containing the diagonal. Implicit
diﬀerentiation implies
g′′(x) = −3 x(x2 −4x + 3)
(x2 −3x + 3)2 ,
which vanishes when x = 1 as the critical point (1, 1) in the main diagonal
direction is degenerate. Computing further, we ﬁnd that g(x) −g(1) vanishes
to order κ = 3 here, with c = c3 = g′′′(1)/3! = i. Checking the signs gives
ζ = −eiπ/3 and therefore
i−1/3(1 −ζ) = eiπ/6 + e−iπ/6 = 2 cos(π/6) =
√
3.
