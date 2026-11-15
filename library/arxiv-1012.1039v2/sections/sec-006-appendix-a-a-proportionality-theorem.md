---
doc_id: arxiv-1012.1039v2
doc_title: "SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS"
section_id: sec-006-appendix-a-a-proportionality-theorem
section_title: "Appendix A. A proportionality theorem"
section_number: null
pages: 14-18
source_pdf: 1012.1039v2.pdf
source_sha256: acb2575050db419d
toc_source: outline
doc_brief: "SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS — Let M be a hyperbolic n–manifold whose cusps have torus cross- sections."
---
The purpose of this appendix is to establish the following proportionality theo-
rem.
Theorem A.1. Let M be a manifold with boundary, so that the interior V of M
admits a complete hyperbolic metric of volume Vol(V ) < ∞. Then
∥M, ∂M∥= Vol(V )
vn
.
Thurston gives a proof in dimension 3 of a version of theorem A.1 in his lecture
notes [Thu80, 6.5.4], where the norm ∥M, ∂M∥is replaced by one coming from
measure homology. There is a natural map from singular homology to measure
homology, which at least does not increase norm. Zastrow and Hansen indepen-
dently showed this map to be an isomorphism of vector spaces for any CW pair
[Han98, Zas98], leaving open the question of whether it was an isometry.
L¨oh
[L¨oh06] proved that the map from (absolute) singular homology to measure ho-
mology is an isometric isomorphism for all connected CW complexes. Since it is
not entirely clear whether measure homology is isometric to singular homology in
the relative case, we give a proof of Theorem A.1 which avoids measure homology.
Such a proof can also be obtained as a special (and simpler) case of the arguments
in Frigerio–Pagliantini [FP10]. Some related ideas may be found in Francaviglia
[Fra04].
Our proof of Theorem A.1 follows closely Benedetti and Petronio’s proof of
[BP92, C.4], which covers the case of ∂M = ∅. As some parts of our proof are
identical to steps in [BP92], we refer to that text for some details. The proof in
[BP92] uses ordinary real singular chains, rather than symmetrized ones, so we do
not symmetrize our chains here.
We use the following notation for parts of the manifold V : For I ⊆R>0, we
let VI be the subset of V consisting of points x ∈V where the injectivity radius
inj(V, x) is in I.
Deﬁnition A.2. Let M be a Riemannian n–manifold, and let σ: ∆n →M be
a smooth singular simplex. The algebraic volume of σ, written algvol(σ) is the
integral over ∆n of the pullback of the volume form on M. The algebraic volume
is extended to smooth chains by linearity.
Obtaining the correct lower bound for simplicial volume is fairly easy.
SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS
15
Lemma A.3. ∥M, ∂M∥≥Vol(V )
vn
.
Proof. This direction is Thurston’s “straightening” argument [Thu80, 6.5.4]. For
any suﬃciently small ǫ > 0, the subset V(0,ǫ] is an open neighborhood of the cusps
of V . Collapsing the components of V(0,ǫ] to their boundaries gives a homotopy
equivalence of pairs (V, V(0,ǫ]) →(M, ∂M). Since the Gromov norm of a (relative)
homology class is homotopy invariant, we can use chains (V, V(0,ǫ]) to compute
∥M, ∂M∥.
The straightening map (see [BP92] or [Rat94] for a precise deﬁnition) is a chain
map
str: C∗(V ) →C∗(V ),
chain homotopic to the identity, and taking each singular simplex to a totally
geodesic simplex with the same vertices.
The map str preserves the subspace
C∗(V(0,ǫ]) (because horoballs are convex), as does the chain homotopy between str
and the identity, so str induces a (norm-decreasing) chain homotopy equivalence of
C∗(V, V(0,ǫ]) to itself. It follows that we need only consider straight (and therefore
smooth) chains.
If z = Pk
i λiσi is a real smooth chain representing the relative fundamental class
[V, V(0,ǫ]], then
algvol(z) =
k
X
i
λi algvol(σi).
The absolute value |algvol(z)| is at least as big as Vol(V[ǫ,∞)), the volume of the
thick part of V .
Let zǫ = Pk
i λiσi be a straight real singular chain representing [V, V(0,ǫ]] which
ǫ–nearly realizes ∥M, ∂M∥, i.e., so that
∥zǫ∥1 ≤∥M, ∂M∥+ ǫ.
We then have
(8)
Vol(V[ǫ,∞)) ≤|algvol(zǫ)| ≤
k
X
i=1
|λi|vn = ∥zǫ∥1vn ≤(∥M, ∂M∥+ ǫ)vn.
Letting ǫ tend to zero in (8) yields the lemma.
□
It is worth noting that essentially the same proof establishes the bound of Lemma
A.3 for measure cycles.
To obtain the upper bound for simplicial volume, we must construct chains repre-
senting the fundamental class which are “close” to the smeared chains from measure
homology. The argument from [BP92] in the closed case uses rather strongly that
there is a compact (and therefore ﬁnite diameter) fundamental domain. We work
around this by chopping the fundamental domain into pieces of bounded diameter.
Proposition A.4. ∥M, ∂M∥≤V ol(V )
vn
Proof. We suppose that V is an orientable ﬁnite volume hyperbolic n–manifold
with m cusps, homeomorphic to the interior of M.
Let Γ < Isom(Hn) be the
fundamental group of V , so that Hn/Γ = V . Let D be the closure of a convex
fundamental domain for the action of Γ on Hn, and let π: D →V be the quotient.
16
K. FUJIWARA AND J. F. MANNING
There is a number µ > 0 so that V(0,ǫ] has exactly m connected components
for any ǫ ≤µ. Let P0 ⊆V be equal to V(µ,∞), and choose some x0 ∈P0. The
complement of P0 in V is a union of cusp neighborhoods C1, . . . , Cn.
Let D0 = π−1(P0) ⊂D, and choose ˜x0 in the interior of D0. Let x0 = π(˜x0) ∈P0.
For each l ∈N, and each j ∈{1, . . . , m}, we let
Pj,l = {x ∈V | l −1 ≤d(x, P0) ≤l} ∩Cj,
and let Dj,l = π−1(Pj,l) ⊂D. We will refer to any Γ–translate of D0 or Dj,l as a
piece.
There is some d > 0 so that diam(Dα) < d for every piece Dα ⊂Hn.
For
each l ∈N and each j ∈{1, . . ., m}, choose ˜xj,l in the interior of Dj,l and let
xj,l = π(˜xj,l). The union of the Γ–orbits of ˜x0 and the ˜xj,l can be identiﬁed in an
obvious way with
ˆΓ := Γ ∪(Γ × {1, . . . , m} × N) .
(This is essentially the 0–skeleton of the “cusped space” of [GM08] associated to
the pair (Γ, {π1(Cj)}) .) Vertices of ˆΓ have a depth associated to them: The depth
of an element of Γ is 0, and the depth of an element of Γ × {1, . . . , m} × N is given
by the third coordinate. The group Γ acts on ˆΓ by left multiplication in an obvious
way, and this action preserves depth.
We let Ωbe the quotient Γ\ ˆΓn+1. For k > 0 an integer, let ˆΓk ⊂ˆΓ be the
subset of vertices of depth at most k. Let ˜Ωk = ˆΓn+1
k
, and let Ωk ⊂Ωbe the set of
Γ–orbits in ˜Ωk.
For any element ω = [(y0, . . . , yn)] ∈Ω, there is a unique straight simplex
σω : ∆n →V
which is equal to the composition of a simplex ˜σω : ∆n →Hn satisfying ˜σω(vi) = yi
with the projection Hn →V . (Here vi is the ith vertex of the n–simplex ∆n.) As
in [BP92], we deﬁne
S(R) = {(u0, . . . un) ∈(Hn)n+1 | d(ui, uj) = R, ∀i̸ = j} = S+(R) ⊔S−(R),
where S+ and S−are those tuples which determine positively and negatively ori-
ented straight n–simplices in Hn, respectively. There is a measure on S(R) coming
from Haar measure on Isom(Hn), and we denote this measure by m. For
ω = [(y0, . . . , yn)] ∈Ω,
and R > 0, we deﬁne
a+
R(ω) = m ({(u0, . . . , un) ∈S+(R) | ui and yi lie in the same piece}) , and
a−
R(ω) = m ({(u0, . . . , un) ∈S−(R) | ui and yi lie in the same piece}) .
Obviously these deﬁnitions do not depend on the choice of representative of ω.
Moreover, for a given R and k, there are only ﬁnitely many ω ∈Ωk for which a+
R(ω)
or a−
R(ω) is nonzero. (This is because there are only ﬁnitely many elements of ˆΓ
which are distance approximately R from a given element of ˆΓ.) It follows that if
we deﬁne aR(ω) := a+
R(ω) −a−
R(ω), then
zR,k =
X
ω∈Ωk
aR(ω)σω
SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS
17
is a ﬁnite real singular n–chain in V . Moreover, we claim that
(9)
zR,∞=
X
ω∈Ω
aR(ω)σω
is a locally ﬁnite real singular n–chain. Indeed, let p ∈V , and r > 0. We must show
only ﬁnitely many simplices in the support of zR,∞(i.e., occurring in the sum (9)
with nonzero coeﬃcient) intersect the ball of radius r about p. Let ˜p be any point
in π−1(p) ⊂D, and note that any simplex σω in the support of zR,∞must lift to
one which comes within r of ˜p, and whose vertices are therefore within R+2d+r of
˜p. As there are only ﬁnitely many such vertices, there are only ﬁnitely many such
simplices σω in the support of zR,∞.
Claim A.5. The chain zR,∞is a locally ﬁnite cycle.
Proof. We have just argued that zR,∞is locally ﬁnite. The proof that zR,∞is a
cycle is nearly the same as the proof of Claim (ii) on pp. 115–116 of [BP92], except
that sums/unions over Γ are replaced by sums/unions over ˆΓ, and conditions of
the form “ui ∈γi(D)” are replaced by “ui ∈D(i)” for appropriately chosen pieces
D(i).
□
For k ∈N, let ǫ(k) be the smallest injectivity radius at any point in a piece of
depth at most k, i.e.,
ǫ(k) = inf
(
inj(V, x)

 x ∈P0 or x ∈
[
{Pj,l | j ∈{1, . . ., m}, l ≤k}
)
.
It is not hard to see that as k →∞, the quantity ǫ(k) tends to zero. In particular,
there is a constant C so that if k > C, then ǫ(k) < µ.
Claim A.6. Let R > 0, and let C be such that ǫ(k′) < µ for all k′ > C.
If
k > R + C + 2d + 1, then zR,k is a relative cycle in (V, V(0,µ]).
Proof. Suppose an (n −1)–dimensional simplex σ is in the support of ∂zR,k. By
Claim A.5, σ must also be in the support of ∂(zR,∞−zR,k), so any lift ˜σ of σ to
Hn must have a vertex mapped to ˆΓ ∖ˆΓk. The diameter of the image of ˜σ is at
most R + 2d. Thus the vertices lie in ˆΓ ∖ˆΓk′ for k′ = k −⌈R + 2d⌉> C, and no
part of the image of ˜σ lies in a translate of the “fat piece” D0. Since ǫ(k′) < µ, σ
has image in the part of V with injectivity radius less than µ.
□
Claim A.7. If R > 2d then a+
R(ω) · a−
R(ω) = 0 for all ω ∈Ω.
Proof. This statement (and its proof) are identical to Claim (iii) on pp. 116–117
of [BP92].
□
Claim A.8. There is a quantity δ(R) > 0 so that limR→∞δ(R) = 0 and so that
the simplices in the support of zR,∞all have volume at least vn −δ(R).
Proof. This statement is a slight rephrasing of Claim (iv) on p. 117 of [BP92]. The
proof is the same.
□
Claim A.9. If R > 2d and aR(ω)̸ = 0, then aR(ω)algvol(σω) > 0.
Proof. See Claim (v) on p. 117 of [BP92]. Claim A.7 is used here.
□
18
K. FUJIWARA AND J. F. MANNING
Claim A.10. Suppose R > 2d + C and k > 2R + 1, where C is the constant
from Claim A.6. The classes [zR,∞] ∈Hlf
n (V ; R) and [zR,k] ∈Hn(V, V(0,µ]; R) are
nontrivial.
Proof. See Claim (vi) on p.117 of [BP92]. The point here is just that some element
of S(R) is a tuple of interior points of pieces corresponding to some tuple ω, so that
there is an open (and therefore positive measure) neighborhood of tuples of points
all corresponding to the same tuple ω.
□
We now complete the proof of the Proposition. Suppose R > 2d + C and k =
⌈2R⌉+ 2.
It follows from Claim A.10 that there is some λ > 0 so that λ[z∞,R] is the
fundamental class in the locally ﬁnite homology group Hlf
n (V ; R) and some λ′ so
λ′[zk,R] is the fundamental class in Hn(V, V(0,ǫ]; R). In fact we must have λ′ = λ,
since both λ[z∞,R] and λ′[zk,R] restrict to the orientation cycle at x0, and the set
of simplices in the supports of zk,R and z∞,R which intersect a small neighborhood
of x0 is the same.
It follows from Claim A.9 that algvol(zk,R) ≤algvol(z∞,R). Moreover, an easy
argument shows that if c is a locally ﬁnite fundamental cycle for V , then Vol(V ) =
algvol(c). We therefore have:
Vol(V ) ≥algvol(λzk,R)
=
X
ω∈Ωk
λaR(ω)algvol(σω)
=
X
ω∈Ωk
λ|aR(ω)| · |algvol(σω)|
by A.9
≥(vn −δ(R))
X
ω∈Ωk
λ|aR(ω)|
by A.8
= (vn −δ(R))∥λzk,R∥1 ≥(vn −δ(R))∥M, ∂M∥,
since λzk,R gives a representative for the fundamental class of (M, ∂M) via the
homotopy equivalence of pairs (V, V(0,µ]) →(M, ∂M). Letting R tend to inﬁnity,
Claim A.8 says that δ(R) tends to zero, so we have
Vol(V ) ≥vn∥M, ∂M∥,
and the proposition is proved.
□
Lemma A.3 and Proposition A.4 together immediately imply Theorem A.1.
