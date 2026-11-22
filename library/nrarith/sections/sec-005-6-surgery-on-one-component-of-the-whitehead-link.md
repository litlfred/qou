---
doc_id: nrarith
doc_title: "Arithmetic of Hyperbolic Manifolds"
section_id: sec-005-6-surgery-on-one-component-of-the-whitehead-link
section_title: "Surgery on one component of the Whitehead link complement"
section_number: 6
pages: 19-29
source_pdf: nrarith.pdf
source_sha256: 085ec9541ddc6cd4
toc_source: inferred
doc_brief: "Arithmetic of hyperbolic manifolds (Neumann–Reid) — survey of arithmetic Kleinian groups: an arithmetic M = H³/Γ is determined up to commensurability by its invariant trace field and quaternion…"
---
6.1.
In [T] Thurston describes how to obtain the complement W of the Whitehead link
(Fig. 5) by identifying faces of an ideal octahedron in pairs. The identiﬁcation matches
face A with A′, B with B′, etc., in Fig. 10, so as to respect the labeling of the edges.
If the octahedron is taken to be a regular ideal octahedron in hyperbolic space, then
one obtains the complete ﬁnite volume hyperbolic structure on W .
As described in
[T] (see also [NZ]), by deforming the octahedron to differently shaped ideal hyperbolic
octahedra one obtains incomplete hyperbolic structures on W , whose metric completions
are hyperbolic Dehn surgeries and generalized Dehn surgeries on the Whitehead link.
We refer the reader to [T] and [NZ] for details on generalized hyperbolic Dehn
surgery. The essential point is that a generalized Dehn surgery on W is parameterized by
B´
A´
C´
C
B
D´
D
A
Figure 10
a “Dehn surgery parameter” (pi, qi) ∈R2∪{∞} for each cusp of W . The result, denoted
W(p1, q1; p2, q2), of this generalized hyperbolic Dehn surgeryis deﬁned if the (pi, qi) are
sufﬁciently close to ∞. Moreover, if (pi, qi) = ∞for i = 1 or 2 then the corresponding
cusp of W is complete—still a cusp—in W(p1, q1; p2, q2), and if (pi, qi) ∈Z2 then
the cusp has been ﬁlled in by a geodesic along which W(p1, q1; p2, q2) has the structure
of a hyperbolic orbifold, or manifold if gcd(pi, qi) = 1, and the underlying topology
is that of topological Dehn surgery, described in the previous section.
(Precisely, if
(pi, qi) = (rp′
i, rq′
i) with (p′
i, q′
i) a coprime integer pair and r > 0, then the cusp is
ﬁlled in by a geodesic with a transverse cone angle of 2π/r, while if pi/qi /∈Q then the
cusp is ﬁlled by a single point at which W(p1, q1; p2, q2) is not topologically a manifold.)
As in the above references, it is convenient to use an ideal triangulation of W to
discuss the deformations, since the shape of an ideal hyperbolic tetrahedron is determined
by a single complex parameter in the upper half plane. By subdividing the octahedron of
Fig. 10 as in Fig. 11, we obtain an ideal triangulation of W with four simplices.
Figure 11
By cutting off the ends of W one obtains a compact manifold-with-boundary W
which can be obtained by identifying truncated tetrahedra as in Fig. 12. The two boundary
tori of W are triangulated as in Fig. 13, where the vertices are labeled according to the
Arithmetic of Hyperbolic Manifolds 293

g d

v
h
N/
()6
<\
a
f c
Figure 12
3 3 3 3
b y
Cc a Qa 6
2 4
d
1 1 1 1
h p
g e u €
2 4
f to)
3 3 3 3
Figure 13

edges of the triangulation of W. Careful inspection shows that the standard topological
meridian and longitude of each component of the Whitehead link are as indicated in
Fig. 14, where we have also included labels for the complex parameters of the four
tetrahedra.

A note on orientations. In the discussion of Dehn surgery on the figure eight knot
complement in [T], and also throughout [NZ], a non-standard orientation convention
was used for the longitude/meridian pair at a cusp, due to the cusp torus being viewed
from inside the manifold rather than outside (this pair is drawn with standard orientation
294 — Walter D. Neumann and Alan W. Reid

Figure 14

in Fig. 18 of [NZ], but this was inconsistent with the text). Thus (p,q) Dehn surgery
in those discussions would be (p,—q) Dehn surgery in the convention which we follow
here, affecting some signs in some formulae.

We can read off from Fig. 14 the consistency relations (see [NZ] or [T]) at the four
edges:

log w” + log z’ + log” + logw’ + log2” + logy’ + logw” + log x’ = 27i
log w + log x + logy + log z = 27

log z” + log w’ + logy” + log z’ + logy” + log a’ + log z” + logy! = 27i
log w + logx + log z+ logy = 277.

Here log denotes the standard branch of natural log on the complex plane split along

(—00, 0]. Since x’ = — and x” = — and similarly for w, y, z, these simplify to
the two relations:

log w + log a + logy + log z = 277i (6.1a)

log(1 — w) + log(1 — x) — log(1 — y) — log(1 — z) =0 (6.16)

Similarly, we can read off the parameters ui, v1, U2, v2, which describe the
holonomy of the meridians and longitudes m1, l1, m2, l2, at the two cusps. They are
u1 = log y′′ + log z′ + log z′′ + log w′ −πi
v1 = log y′′ + log y + log x + log x′ + log w′′ + log z′ + log x′′
+ log x + log y + log y′ + log z′′ + log w′ −4πi
u2 = log z′′ + log y′ + log y′′ + log w′ −πi
v2 = log z′′ + log z + log x + log x′ + log w′′ + log y′ + log x′′
+ log x + log z + log z ′ + log y′′ + log w′ −4πi
which, written in terms of x, y, z, w and simpliﬁed by (6.1), becomes
u1 = log(w −1) + log x + log y −log(y −1) −πi
(6.2a)
v1 = 2 log x + 2 log y −2πi
(6.2b)
u2 = log(w −1) + log x + log z −log(z −1) −πi
(6.2c)
v2 = 2 log x + 2 log z −2πi.
(6.2d)
(u1, u2) can be taken as the “analytic Dehn surgery parameter,” as discussed in [T]
and [NZ], in which case w, x, y, z, constrained by equations (6.1), become complex
analytic functions of this parameter.
The real Dehn surgery parameters (p1, q1) and (p2, q2) are determined by the equa-
tions
p1u1 + q1v1 = 2πi
p2u2 + q2v2 = 2πi.
(6.3)
For the complete structure on W we have u1 = v1 = u2 = v2 = 0, which, with
(6.1) and (6.2), easily implies x = y = z = w = i (this is also clear from the regularity
of the octahedron for the complete structure). We shall thus deform from these values of
x, y, z, w, maintaining the consistency relations (6.1).
6.2.
We are only interested in generalized Dehn surgeries on one cusp of W , so we
always have (p1, q1) = ∞.
The requirement that the ﬁrst cusp is complete means
u1 = v1 = 0. From v1 = 0 and equation (6.2b) we deduce x = −y −1. Equation (6.1a)
then gives z = −w−1 and (6.1b) then gives y = w, so
(x, y, z, w) = (x, −x−1, x, −x−1).
Conversely, (x, y, z, w) = (x, −x−1, x, −x−1) satisﬁes the consistency relations (6.1)
and the cusp relations u1 = v1 = 0 and thus gives a structure on W which is complete
at the ﬁrst cusp. We thus just have the one complex parameter x, in the upper half plane,
describing our deformations.
We abbreviate (u2, v2) = (u, v) and (p2, q2) = (p, q), and we shall write W(p, q)
for W(∞; p, q). The formulae (6.2) simplify to
u = log x + log(x + 1) −log(x −1)
v = 4 log x −2πi
(6.4)
and the real Dehn surgery parameter (p, q) is determined by the equation
pu + qv = 2πi.
(6.5)
Thurston’s complex analytic parameter for hyperbolic Dehn surgery on one component
of the Whitehead link is u. We shall use the parameter x instead. Since x describes
the shape of an ideal simplex, which degenerates for x real, the natural domain for the
parameter x is the complex upper half plane U. The maps x 7→u and x 7→v take U
biholomorphically to the domains U and V, where U is the complex plane split along
the rays (−∞, 2 log(
√
2 −1)] and [2 log(
√
2 + 1), ∞) and V = {v ∈C : −2πi <
Im v < 2πi}. Thus x ∈U, u ∈U, and v ∈V are all equally good complex analytic
parameters for generalized hyperbolic Dehn surgery on one component of the Whitehead
link.
x
x −x−1
−x−1
m
l
−x−1 −x−1
x
x
Figure 15
The triangulation of the cusp torus of W(p, q) is shown in Fig. 15 with the meridian
m and longitude l drawn in. Its isomorphism type as a complex torus C2/Λ is described
by the complex parameter τ = λ2/λ1 with positive imaginary part, after choosing an
oriented base λ1, λ2 for the lattice Λ. We can consider m and l to represent generating
translations in the universal cover of the cusp torus, and we deﬁne:
Deﬁnition. The cusp parameter of W(p, q) is the parameter τ of the cusp torus with
respect to the oriented basis m, −l.
We denote the cusp parameter for W(p, q) by
τ(W(p, q)). (We make this choice of basis for consistency with [T] and [NZ], as well
as because of Theorem 6.3 below, which says this τ is often an algebraic integer; the
seemingly “more natural” choice l, m replaces τ by −τ −1.)
Our next theorem says that τ(W(p, q)) determines W(p, q). To state it we need some
notation. Let N denote the closed parallelogram in R2 with vertices ±(−4, 1), ±(0, 1)
(Fig. 16).
(0,1)
(−4,1)
(0,−1)
(4,−1)
p
q
Figure 16
It is known (and we shall show) that this is the “non-hyperbolic” domain in the space
of real Dehn surgery parameters. Since (p, q) Dehn surgery and (−p, −q) Dehn surgery
give the same result, the space of real surgery parameters for hyperbolic Dehn surgeries
is
H = (R2 ∪{∞} −N)/ ± 1.
Theorem 6.1. The map (p, q) 7→τ(W(p, q)) is a homeomorphism H →U, where U
is the complex upper half plane.
Proof. By elementary calculation from Fig. 15 one obtains τ in terms of x as
τ =
4x
1 −x2 −2.
(6.6)
By solving equation (6.6) for x in terms of τ one veriﬁes that this map x 7→τ is a
2-fold branched cover U →U, branched at x = i, and that x and −x−1 both map to
the same τ. Note that replacing x by −x−1 replaces u by −u, v by −v, and hence
(p, q) by (−p, −q). To prove the theorem we must thus show that the map x 7→(p, q)
is a homeomorphism of U to R2 ∪{∞} −N. We shall denote the map x 7→(p, q) by
φ: U →R2 ∪{∞}.
Thurston’s hyperbolic Dehn surgery theorem (cf., [T] or [NZ]) asserts that φ is
a homeomorphism from a neighborhood of the parameter value x = i corresponding
to the complete structure on W to a neighborhood of ∞.
Elementary computation
shows that φ takes the boundary R ∪{∞} of U homeomorphically to the boundary
of N (speciﬁcally, the intervals [−∞, −1], [−1, 0], [0, 1], [1, ∞] go to the segments
[(4, −1), (0, 1)], [(0, 1), (−4, 1)], [(−4, 1), (0, −1)], [(0, −1), (4, −1)] respectively). It
therefore sufﬁces to show that φ has non-vanishing Jacobian at all x ∈U −{i}.
Denote
a(x) = log x,
b(x) = log x −1
x + 1.
Since a is a biholomorphic map a: U →A = {z ∈C : 0 < Im z < π}, we may show
instead that φ ◦a−1: a 7→(p, q) has non-vanishing Jacobian away from a(i) = πi/2. In
other words, we must show that ∂a/∂p and ∂a/∂q are linearly independent over R for
a̸ = πi/2. The deﬁning equation for p and q is
p(a −b) + q(4a −2πi) = 2πi.
Implicit differentiation of this equation with respect to p and q gives
∂a
∂p(p −p ∂b
∂a + 4q) = b −a
∂a
∂q (p −p ∂b
∂a + 4q) = 2πi −4a,
so we must show that b −a and 2πi −4a are linearly independent over R. However
the map b ◦a−1: a(x) 7→b(x) is conjugate by log to the order 4 M¨obius transformation
x 7→(x−1)/(x+1) and it is thus easy to see that if one divides A into four “quadrants”
by the vertical and horizontal lines through πi/2, then a 7→b rotates each quadrant
clockwise into the next. It follows that the line from b to a never points in the same
direction as the line from the center πi/2 of rotation to a (unless a = πi/2). That is,
b −a and πi/2 −a are independent over R, as was to be shown.
We now restrict to the case that (p, q) /∈N and p ∈Z and q ∈1
2Z. Recall that W
covers the orbifolds W ′ and W ′′ of Figs. 6 and 7 with covering groups C2 and C2×C2.
W(p, q) thus branched covers W ′(p, 2q) and W ′′(p, 2q) in the notation of Sect. 5, and
these are hyperbolic orbifolds under our assumptions on p and q.
Note that (p, q) 7→(p+2q, 2q) transforms the domain N into the square with vertices
(±2, ±2), so part (ii) of Theorem 5.1 is proven. We next compute some arithmetic
invariants of our orbifolds.
Theorem 6.2. Denote z = x −x−1 (so τ = −4/z −2 and Q(z) = Q(τ)). The
invariant trace ﬁelds and trace ﬁelds for W(p, q), W ′(p, 2q), and W ′′(p, 2q) are as
follows:
k(π1W(p, q)) = Q(z)
Q(tr(π1W(p, q))) = Q(√z)
)
q ∈Z,
k(π1W ′(p, 2q)) = k(π1W ′′(p, 2q)) = Q(z)
Q(tr(π1W ′(p, 2q))) = Q(tr(π1W ′′(p, 2q))) = Q(√z, i)
)
q ∈1
2Z.
In particular, the cusp ﬁeld equals the invariant trace ﬁeld for all these examples.
Remark. By Corollary 2.3 it follows that Q(z) = Q(√z) if q ∈Z and p is odd. In
the examples we have checked, Q(z)̸ = Q(√z) otherwise.
a5
a0
a3
a4
a2
a1
Figure 17
Proof. Denote the vertices of our original octahedron O by a0, . . . , a5 as in Fig. 17.
If we position O in H3 with these vertices at 0, 1, ∞, −1, x, x−1, respectively,
then it is easy to compute that the four constituent tetrahedra (Fig. 12) have parameters
x, −x−1, x, −x−1, so O has the correct shape for the value x of our deformation
parameter.
Denote by a the element of PGL2C = Isom(H3) which translates O across its face
A, taking face A′ to A. Thus a takes 0, −1, x−1 to 1, 0, x respectively. Solving
for an element of PGL2C shows that a can be represented by the matrix
a =

1
1
1 −z
1

∈PGL2C.
Similarly, if b, c, d are the translations across faces B, C, D respectively, one
computes that
b =

1
1
1
1 + z

,
c =

1
1 −z
1
1

,
d =

1 + z
1
1
1

.
If q ∈Z then π1W(p, q) is generated by a, b, c, and d. π1W ′(p, 2q) is generated by
the above elements and the additional element
β =

0
1
1
0

which rotates the octahedron about the axis through a1 and a3.
The vertices a0, . . . , a3 lie at the cusp of W ′(p, 2q) and are all in Q(z) ∪{∞} and
the generators a, b, c, d, β, of π1W ′(p, 2q) have entries in Q(z). As in the proof of
Lemma 2.5, it follows that all lifts of the cusp are in Q(z), so k(π1W ′(p, 2q)) ⊂Q(z).
But k(π1W ′(p, 2q)) must contain τ, which generates Q(z), so it equals this ﬁeld.
Suppose q ∈Z. To compute Q(tr π1W(p, q)) we must put the generators a, b,
c, d in SL2C by dividing each by the square root of its determinant, namely √z.
Their traces then evidently generate Q(√z), so Q(tr π1W(p, q)) contains Q(√z). On
the other hand our representation of π1W(p, q) then has image in PSL2Q(√z), so
Q(tr π1W(p, q)) is at most Q(√z).
The additional generator β of π1W ′(p, 2q) is represented by the matrix ( 0 i
i 0) ∈
PSL2Q(√z, i), so Q(tr π1W ′(p, 2q)) ⊆Q(√z, i). But a and βb have traces 1/√z
and i√z, so the trace ﬁeld contains √z and i.
The same argument applies to
π1W ′′(p, 2q), since the additional involution needed to generate π1W ′′(p, 2q) is the
180◦rotation about the axis a0a2, which is
γ =

i
0
0
−i

∈PSL2Q(√z, i).
(Remark: γ does not respect the octahedron after Dehn surgery.)
Theorem 6.3. Suppose (p, q) ∈Z× 1
2Z is not in N. τ = τ(W(p, q)) is not an algebraic
integer if and only if p = 0 and |q| is an odd prime power. π1W ′(p, 2q) fails to have
integral traces if and only if p = 0 or −4q and |q| is an odd prime power.
Proof. Since τ = −4/z−2, the integrality of τ is equivalent to that of 4/z. Moreover,
to check if tr π1W ′(p, 2q) consists of algebraic integers, it sufﬁces to check a set of
generators and their pairwise products (cf. [Mag, p. 148]). Using the generators in the
above proof one obtains traces 2/√z, √z + 2/√z, multiples of these by i, and rational
integral linear combinations of 1, z, and 4/z. So tr π1W(p, q) consists of algebraic
integers if and only if z and 4/z (and hence also their square roots) are algebraic integers.
By (6.4) and (6.5), x satisﬁes the equation
x(x + 1)
x −1
p
x4q = 1,
(6.7)
which multiplies out to a monic polynomial with rational integer coefﬁcients and constant
term ±1 unless p + 4q = 0. Thus x is a unit, whence z = x −x−1 is an algebraic
integer, if p + 4q̸ = 0. On the other hand, if x satisﬁes equations (6.4) and (6.5) for
(p, q) then one checks that (1 −x)/(1 + x) satisﬁes (6.4) and (6.5) for (p + 4q, −q).
But replacing x by (1 −x)/(1 + x) replaces z = x −x−1 by 4/z. Thus 4/z —and
hence also 4/z —is an algebraic integer if p̸ = 0.
To complete the proof it sufﬁces to show that when p = 0, z is an algebraic
integer divisor of 4 if and only if |q| is not an odd prime power. (Recall, that since
q ∈1
2Z, 2q is an arbitrary integer.) Assume p = 0. Then (6.4) and (6.5) imply that
x/i = exp(2πi/4q), so z/i = exp(2πi/4q) + exp(−2πi/4q). Now z will be a divisor
of 4 if and only if ζ := (z/i) exp(2πi/4q) is.
But ζ divides 4 if and only if its
norm divides 4. The norm of ζ = exp(2πi/2q) + 1 is Φ(1), where Φ is the minimal
polynomial for −exp(2πi/2q). Now, −exp(2πi/2q) is a primitive r-th root of unity
with r = |4q|, |q|, or |2q|, according as 2q is an odd integer, twice an odd integer, or
divisible by 4. Thus Φ is the r-th cyclotomic polynomial, and it is known that Φ(1) = 1
unless r is the power of a prime, in which case Φ(1) equals this prime (cf. e.g., [W]).
Thus Φ(1) fails to divide 4 if and only if r is an odd prime power, in which case q = ±r.
An interesting example is W(0, 3) (or W(12, −3), which is commensurable with
it). The invariant trace ﬁeld k(π1W(0, 3)) is Q(√−3), but π1W(0, 3) has non-integral
traces, so it cannot be commensurable with PSL2O3. However its volume turns out to be
20 times the volume of H3/PSL2O3 —this is 10/3 times the volume of a regular ideal
tetrahedron.
