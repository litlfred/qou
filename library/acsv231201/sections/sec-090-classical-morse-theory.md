---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-090-classical-morse-theory
section_title: "Classical Morse theory"
section_number: null
pages: 517-523
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
499
Functoriality of the residue, combined with (C.2.19), now implies
Res
"
z−r−1 P(z)
Q(z)m dz; SD
#
=
1
(m −1)!
 ∂
∂u
!m−1 z(u)−r−1P(Ψ−1(u))
JΨ(Ψ−1(u))
!

(0,u)=Ψ(z)
dzπ .
(C.2.20)
Applying Corollary C.23 to the right-hand side of (C.2.20) and noting that
ΓΨ =
 
∂ui
∂log zj(u)
!
implies
∂log zi(u)
∂uj
=

Γ−1
Ψ

i j
we obtain an expression
 ∂
∂u
!m−1 
z(u)−rP(Ψ−1(u))
Qd
j=1 zj(u)JΨ(Ψ−1(u)


(0,u)=Ψ(z)
= z−r
P(z)
det ΓΨ(z)
˜P(r, z)
Q
j∈π zj
whose leading term is as stated.
□
Remarks. The leading term (C.2.15) depends on the divisors Q j only through
their gradients. When the stratum S is a single point (k = d), the residue at p
is a 0-form – i.e., a polynomial P(r) in r.
C.3 Classical Morse theory
After using residues to replace our starting Cauchy integral with a residue in-
tegral over an intersection class σ in V, we need to understand how to deform
σ in V. The possible deformations we can make, and which deformations will
allow us to compute asymptotic behavior, depend on the topological properties
of V. Morse theory attempts to describe the topology of a space X by means of
the geometry of X near critical points of a smooth, proper function h : X →R.
Our destination in this appendix is Theorems C.38 and C.39, which state that
we may ﬁnd a basis for each homology group Hk(X) consisting of quasi-local
cycles at the critical points of h: for each critical point p there will be a cycle
with height bounded by h(p)−ε except in an arbitrarily small neighborhood of
p. We establish this result by studying the sublevel sets X≤a := {x ∈X : h(x) ≤
a} as a increases and showing that the homotopy type of X does not change
(the Morse Lemma C.27) except at critical points, where a cell is attached
(Theorem C.28). Along the way, a description of X as a cell complex is given in
Theorem C.32. A description of the attachments in terms of relative homology
is also given in the last section.
Our material here covers classical (smooth) Morse theory, which assumes
500 Residue forms and classical Morse theory

that the space X under consideration is a manifold. More general spaces are
handled in Appendix D.

Homotopy equivalence except at critical points

Let X be a smooth manifold and let h : X — R be a smooth function; we think
of / as giving the points on X a height (see Figure C.4 below). The critical
points of the height function h are the points p € X for which the differential
dh\p is zero on the tangent space T,(X). The values h(p) of h at its critical
points p are called the critical values of the height function h. A critical point
p is a nondegenerate critical point for h if the quadratic form given by the
quadratic terms in the Taylor approximation for / at p has no zero eigenvalues.

In coordinates, this means that the determinant of the Hessian matrix | aa )|
OX}

is non-zero when X is locally coordinatized by x;,...,xy near p. While the
Hessian matrix itself depends on the coordinates, its (non)singularity does not;
see [Mil63, Section 2.1]. While it is traditional to require Morse functions to
be proper and have distinct critical values, we will not require this.

Definition C.26 (Morse function). A smooth function h : X — R is called a
Morse function if the critical points of h are nondegenerate. If h is a proper
map (meaning the inverse image of any closed and bounded interval is com-
pact) then we call h a proper Morse function. If the critical values of h are
distinct, then h is a Morse function with distinct critical values.

Exercise C.2. In which of the following cases is h a proper Morse function on
Xx?

(1) X is the surface of a doughnut lying on a table and h is height.
(2) X is the infinite cylinder {(x, y, z) : e+ y = 1} and / is the z coordinate.
(3) X is the unit sphere and h is the distance to the point (—2, 0,0).

Let X be a smooth manifold with proper Morse function h. If a is a real
number, we let X<, denote the topological subspace {a € X : h(x) < a}. The
fundamental Morse Lemma states that the topology of X<q changes only when
ais a critical value of h.

Lemma C.27 (Morse Lemma). Let a < b be real numbers, suppose that the
interval [a,b] contains no critical values of h, and assume that h-\({a, b]) is
compact. Then the inclusion X<q — Xzp is a homotopy equivalence.

Proof The Morse Lemma is proven in [Mil63, Theorem 3.1] by constructing
a homotopy on X<, that follows the orthogonal trajectories of the level-sets
C.3 Classical Morse theory
501
h = c for constants c ∈[a, b]. This is accomplished using a downward gradient
ﬂow constructed locally using the gradient of h(x) (which never vanishes when
h(x) ∈[a, b] due to the absence of critical points).
□
Exercise C.3. Let X be the torus embedded in R3 and let f be the distance
from points on X to a ﬁxed point not on X. Use the Morse Lemma to prove that
f has a critical point on X that is either degenerate or is neither a maximum
nor a minimum.
Attachment at critical points
Suppose now that there is precisely one critical point p with h(p) ∈[a, b]. The
Hessian of h at p is a real symmetric matrix and therefore has real eigenvalues.
We deﬁne the Morse index of h at p to be the number of negative eigenvalues
of the Hessian. The Morse index can range from 0 at a local minimum to
the dimension d of X at a local maximum. We now describe the topology of
X≤b as an attachment of a space Y to X≤a, where Y and the attaching map
depend on the Morse index of h at p. Following standard terminology in Morse
theory, a k-cell (more properly a topological k-cell) is a ball of dimension k (in
Appendix A we used this term for k-simplices, but topologically a k-ball and
k-simplex are equivalent).
Theorem C.28. Suppose that h−1([a, b]) is compact and contains precisely
one critical point p, with critical value h(p) strictly between a and b. Then
the space X≤b has the homotopy type of X≤a with a λ-cell attached along its
boundary, where λ is the Morse index of the critical point p (a 0-cell is a point
with empty boundary).
Proof
See [Mil63, Theorem 3.2].
□
Example C.29. Suppose X is the unit sphere in R3 and consider the height
function h(x, y, z) = z (when working in R3, we often set h(x, y, z) = z so
that the “height” function measures actual height). There are only two critical
points of h, namely its minimum (0, 0, −1) at height −1 and maximum (0, 0, 1)
at height 1.
Let us follow X≤a as a increases from −∞to +∞. For a < −1, the set X≤a
is empty. As a passes −1, Theorem C.28 states that a 0-cell is added with no
identiﬁcation, making X≤a, homotopically, a point. Geometrically, X≤a with
a ∈(−1, 1) is a small dish, which is contractible to a point. The only other
attachment occurs at the top of the sphere. For a < 1 ≤b, the set X≤b \ X≤a is
a polar cap. Thus, geometrically as well as homotopically, a 2-cell is attached
502
Residue forms and classical Morse theory
Figure C.3 Sublevel sets of a sphere, which form a contractible subset of the
sphere until reaching its maximum, when a cap is attached to complete the sphere.
along its bounding circle. All spaces resulting from attaching a k-cell to a con-
tractible space are homotopy equivalent to attaching a k-cell to a point. In the
present case k = 2 and the resulting space is homotopy equivalent to a 2-sphere,
recovering the homotopy class of X; see Figure C.3. We remark that analyz-
ing the attachments recovers only the homotopy type, not the homeomorphism
class.
◁
Example C.30. Let X be the torus in R3 obtained by rotating the circle (x −
5)2 + (y −5)2 = 1 about the y-axis and let h(x, y, z) = z. The function h has
four critical points, all on the z-axis: a maximum (Morse index 2) at (0, 0, 6),
a minimum (Morse index 0) at (0, 0, −6), and saddle points (Morse index 1) at
(0, 0, 4) and (0, 0, −4); see Figure C.4.
p
c
c
c
c1
2
2
3
4
p1
4
3
p
p
Figure C.4 The critical points on a torus for the standard height function.
For −6 ≤a < −4 we see that, as in Example C.29, X≤a is homotopic to a
point (geometrically, it is a dish). As a passes −4, the theorem tells us to add
a 1-cell along its boundary. The only way of attaching a 1-cell to a point is to
map both endpoints to the point, leaving a circle. Geometrically, if −4 < a < 4
C.3 Classical Morse theory
503
then the set X≤a is a patch in the shape of a 2-cell with two disjoint segments
of its boundary attached to two disjoint segments of the geometric boundary of
X≤a; see Figure C.5.
Figure C.5 Crossing the critical value c2.
The critical point at height 4 adds another 1-cell modulo its boundary, mak-
ing the homotopy type of X≤a for 4 ≤a < 6 the union of two circles touching
at a point. Finally, crossing the top of the sphere a 2-cell B is added modulo
its boundary. There is more than one choice for the homotopy type of the at-
tachment, and keeping track only of the homotopy type throughout the process
of attaching cannot resolve this choice – one must look at the geometry of the
attachment. In this case, because the attachment is to a topological circle (the
6−ε level set) and results in a nonintersecting surface in R3, there are only two
possibilities for the attaching map in homology: ∂B is mapped to the circle in
one of two orientations. Either choice results in a torus.
We remark that knowing the mapping of the last attachment in homology
is not suﬃcient to compute the homotopy type of the space. For example, at-
taching a 2-cell to two circles joined at a point by mapping the boundary of the
2-cell to the common point produces a sphere with two circular handles, which
is not homotopy equivalent to a torus.
◁
Although Theorem C.28 speciﬁes the attachment pair when the topology of
X changes, Example C.30 shows that the computation of the attaching map is
not automatic. It will help to have some results that narrow down this compu-
tation to certain constructions local to the critical point: the homotopy in the
Morse Lemma may be improved so that outside of a neighborhood of p, every
point is pushed down at least to a level c −ε.
Let p be a critical point with height c = h(p) and suppose a < c < b are
such that p is the only critical point with height in [a, b]. Given ε > 0, let
Bε(p) denote the ε-neighborhood of p. We will see a formal version of the
local Morse Lemma, in a more general context, in Appendix D. For now, we
note that the local Morse Lemma implies that the homotopy type of X≤b is the
same as the homotopy type of X≤c−ε ∪Bε(p) for suﬃciently small ε.
Deﬁnition C.31. Let Xc+ := X≤c−ε ∪Bε(p) for any suﬃciently small ε > 0,
and let Xp,loc denote the pair (Xc+, X≤c−ε) depicted in Figure C.6.
504
Residue forms and classical Morse theory
c − 
p
c
p
c
ε
Figure C.6 The space Xc+ with points of height c represented by a dotted line.
The discussion above implies that the attachment pair (X≤b, X≤a) is homo-
topy equivalent to Xp,loc. Suppose now that h is a Morse function whose critical
values need not be distinct. If [a, b] contains the unique critical value c ∈(a, b)
then the homotopy pushes points down to X≤c−ε except in a neighborhood of
the set of critical points whose value is p. Since this set of critical points is
discrete under our assumptions,
(X≤b, X≤a) ≃]
M
p:h(p)=c
Xp,loc
(C.3.1)
for suﬃciently small ε > 0, where the tilde sum denotes the wedge of spaces,
meaning a disjoint union with the second space in each pair identiﬁed. This
equivalence states that (X≤b, X≤a) is homotopy equivalent to the wedge of the
local pairs at all critical points p with value c. The reduced homology of a
wedge is the direct sum of the reduced homologies of the individual spaces.
Exercise C.4. Intuitively, why is (C.3.1) a (reduced) direct sum? That is, ex-
plain why cycles in diﬀerent summands cannot cancel each other.
The last step for this section is to put all this information together to produce
a global topological picture of X. At the level of homotopy type, the result is
that X has the topology of a cell complex, about which certain information is
known.
Theorem C.32. Let X be a manifold and h : X →R be a diﬀerentiable
function with no degenerate critical points. Suppose each sublevel set X≤a is
compact. Then X has the homotopy type of a cell complex with one cell of
dimension λ for each critical point of Morse index λ in X≤a.
Proof
A full proof of Theorem C.32 can be found in [Mil63, Theorem 3.5],
but we give a sketch here. The proof for the case of ﬁnitely many critical points
with distinct critical values involves showing inductively that for any critical
value c the homotopy equivalence between X≤c−ε and a cell complex may be
extended, via the attachment of a cell, to a homotopy equivalence between
X≤c+ε and a cell complex with one more cell. The restriction on distinct critical
