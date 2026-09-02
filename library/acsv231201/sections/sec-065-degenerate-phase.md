---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-065-degenerate-phase
section_title: "Degenerate phase"
section_number: null
pages: 444-448
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
---
Most of our results in previous chapters have relied on reduction to a stationary
phase integral for which the phase is quadratically nondegenerate at an isolated
13.3 Degenerate phase 427
critical point, and hence amenable to a Complex Morse Lemma argument, but
more complicated situations can arise.
Example 13.3. Recall from Example 10.69 the generating function
F(x, y) =
∑
r,s
ars xrys = 1
(1− xy)(1− x/2− y/2)
with main diagonal terms arr = ∑r
j=0 4− j
(2 j
j
)
.
The critical point equations for the factorH1 = 1− x/2− y/2 in the direction
(1, 1) have a unique solution (1, 1), while every point on the torus|x| =|y| = 1
satisﬁes the critical point equations for the factor H2 = 1− xy. The point
(1, 1) is therefore a minimal, but not strictly minimal, critical point which is a
double point of the singular variety. In addition to a torus of singularities with
the same coordinate-wise modulus, the varieties V(H1) andV(H2) intersect
tangentially at (1, 1).
A systematic application of the surgery approach reduces the problem of
ﬁnding asymptotics of arr as r→∞ to ﬁnding asymptotics of
1
2π
∫
D
A(θ, t) exp(−λφ(θ, t)) dµ
asλ→∞ , where
A(θ, t) = 2
2− eiθ
φ(θ, t) =− log
(
1− t
(
1− e−iθ
2− eiθ
))
,
the domain of integration D = [−π,π ]× [0, 1]⊂ R2, and µ is the Lebesgue
measure. Note that Re φ is nonnegative on D, with minimum value 0. The
stationary points of φ on D are (0, t) for 0≤ t≤ 1, and (θ, 0) for−π≤ θ≤ π.
Not only is the phase not equivalent via a smooth change of variables tot2 +θ2
(it looks more like tθ2), the stationary phase set consists of more than a single
point, being a 1-dimensional T-shaped subset of the rectangle. ◁
Example 10.69 derived asymptotics for Example 13.3 using an ad hoc ap-
proach.
Example 13.4. Develop a systematic theory for such degenerate integrals. ◁
Example 13.5. If S denotes the set ofn×n Hermitian matrices with Frobenius
norm 1, and E denotes the subset ofS containing matrices with repeated eigen-
values, then E has positive codimension in S but has a volume with respect to
the Riemannian metric inherited from S . It turns out 1 that this volume is, up
1 K. Kozhasov (personal communication)
428 Challenges and extensions
to an easily computed constant, the coeﬃcient of (z1z2z3z4)n in the generating
function
M(z1, z2, z3, z4) =
∏
1≤i< j≤4
(zi− z j)
1− e1(z)2 + 4e2(z)
,
where e j is the jth elementary symmetric function in the variables z1, z2, z3, z4.
While symmetry initially makes the problem tractable, the stationary phase
set is a union of curves rather than points and, to make things worse, the nu-
merator vanishes to diﬀerent orders on these curves and their intersections. By
computing a D-ﬁnite equation satisﬁed by the main diagonal of M, and using
the numeric methods discussed in Section 8.4.2 and Section 13.1 above, it can
be shown that the coeﬃcient of interest has asymptotic behavior Cn−5/264n as
n→∞ for a constant C≈ 0.4527. It would be interesting to derive this result
using multivariate techniques. ◁
In the case of real phase, it is possible to compute a degenerate integral as
a Laplace integral by determining volumes of level sets. Suppose we wish to
compute an integral of the form
∫
D
exp(−λφ(x))A(x) dx,
where D = [0, 1]d⊂ Rd in some dimension d≥ 1, the parameter λ is large,
andφ and A are analytic functions on D. Fubini’s Theorem tells us that for a
nonnegative measurable function f deﬁned on a measure space (X,µ ) we have
∫
X
f (x) dµ(x) =
∫ ∞
0
µ ({x : f (x)≥ z}) dz,
and the change of variable z = exp(−u) converts this integral to
∫ ∞
−∞
e−uµ({x :− log f (x)≤ u}) du.
Let Vu denote the measure of the sub-level setµ({x :− log f (x)≤ u}). Letting
f (x) = e−λφ(x), we obtain
Vu =
∫
D
1φ(x)≤u/λdµ(x)
and, for simple enough φ, it may be possible to compute Vu explicitly. Propo-
sition 4.7 can then be applied to determine asymptotics.
Exercise 13.1. Compute asymptotics asλ→∞ for
∫ 1
0
∫ 1
0
e−λxy2
xy dx dy.
13.4 Critical points at inﬁnity 429
Degeneracies of phase can also, in principle, be handled by resolving singu-
larities to obtain a normal crossing, using a change of coordinates mapping the
phase function into a monomial, expanding the resulting amplitude function
into a power series, and then applying known exact asymptotics to each term.
Resolution of singularities, together with the methods of [Var77], implies that
the possible asymptotic behaviors for any rational asymptotics fall in a limited
set of leading terms.
13.4 Critical points at inﬁnity
Let T = T(x), where x is in some component B of the complement of the
amoeba of the denominator Q of some rational function. As seen in Chapter 7,
non-existence of CPAI in the direction ˆr is a suﬃcient condition for [T] to be
representable as the sum of cycles corresponding to attachments at aﬃne criti-
cal points in direction ˆr. However, this non-existence is by no means necessary.
For instance,
• The trajectories ﬂowing to a CPAI may not be trajectories of any stratiﬁed
gradient-like ﬂow.
• A trajectory ﬂowing to a CPAI may be a gradient-like ﬂow, but the particular
torus [T] may ﬂow down to an aﬃne critical point and not be pulled down a
path leading to this CPAI.
• [T] may not ﬂow down without being pulled to inﬁnity, but there may be a
cobordism between T and a cycle lower than any CV AI.
• Even if [T] is pulled to inﬁnity by some gradient-like vector ﬁeld, the CPAI
there may not alter the topology and it might be possible to deform [ T] to
“come back from inﬁnity.”
Problem 13.3. a) Can there be unreachable CPAI, meaning that there is a
downward gradient-like ﬁeld that has no ﬂows reaching a CPAI?
b) If so, how can we compute which CPAI are like this?
c) Do all CPAI alter the topology of V∗? Is there an attachment theory for
CPAI, giving a way to compute the topological eﬀect of each CPAI?
d) If there is a local attachment, can we ﬁnd a cycle α representing it and
determine
∫
αz−r−1F(z) dz?
Another useful tool would be the capability to rule out the existence of CPAI
in some direction without an overly long computer algebra computation. An
early conjecture, which turned out not to be true, was that all CPAI must be
parallel to some face of the Newton polytope ofQ. Some ongoing work proves
430 Challenges and extensions
that this conjecture is true when the polytope is sch¨ on, a property deﬁned in
terms of compactiﬁcations via toric varieties [Huh13, Deﬁnition 3.6]. The set
of directions parallel to a face of the Newton polytope is a small set (it has
positive codimension) so it is useful to know when CPAI are restricted to these
directions. Generally, we would like to ﬁnd computable restrictions on the pos-
sible directions of CPAI.
