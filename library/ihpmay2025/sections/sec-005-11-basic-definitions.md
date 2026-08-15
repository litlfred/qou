---
doc_id: ihpmay2025
doc_title: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS RICHARD D. CANARY"
section_id: sec-005-11-basic-definitions
section_title: "Basic definitions"
section_number: 1.1
pages: 7-10
source_pdf: IHPMay2025.pdf
source_sha256: 0440a39721552a9e
doc_brief: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS RICHARD D. CANARY — These notes are designed to accompany my mini-course on hyperbolic 3-manifolds at IHP in May 2025."
---
For simplicity, we will assume throughout these lectures that all groups are finitely gener-
ated, non-abelian and torsion-free. Selberg’s Lemma guarantees that every finitely generated
subgroup of any linear group contains a finite-index torsion-free subgroup, so the assumption
that groups are torsion-free is not very restrictive.
A Kleinian group Γ is a discrete subgroup of PSL(2, C)∼= Isom+(H3). Since we have assumed
that Γ is torsion-free,
NΓ = H3/Γ
is a hyperbolic 3-manifold.
The limit set Λ(Γ) of a Kleinian group Γ is the set of accumulation points of an orbit in the
boundary of H3, i.e. if x0∈ H3, then
Λ(Γ) = Γ(x0)− Γ(x0)⊂∂H3.
One may easily check that Λ(ρ) does not depend on the choice of basepoint x0 (If x0,y 0∈ H3,
{γn}⊂ Γ and γn(x0)→z∈∂H3, then γn(y0)→z∈∂H3).
For example, if Γ ⊂ PSL(2, R) ⊂ PSL(2, C) and H2/Γ is a closed surface, then Λ(Γ) =
R∪{ 0}⊂ ∂H3.
A better example is provided by looking at Schottky groups. If {C1,C 2,...,C 2n−1,C 2n} is a
family of disjoint round circles inC =∂H3 bounding disjoint (closed) disks{D1,D 2,...,D 2n−1,D 2n}
(whose closures are disjoint in C), then we may construct a free Kleinian groups by letting γi
be a M¨obius transformation taking Di to C− int(D2i) for all i. The classical ping-pong lemma
implies that Γ = ⟨γ1,...,γ n⟩ is a free group and that if F = C−Sn
i=1Di and if γ̸= id∈ Γ,
then Γ(F ) is disjoint from F (and that γi(F ) abuts F along ∂D2i). If you think about this
picture a bit you can convince yourself that C− Γ(F ) is a Cantor set which is, by construction,
Γ-invariant (whereF is the closure of F ). In fact, Λ(Γ) = C− Γ(F ).
Lemma 1.1. If Γ is a Kleinian group, which is not virtually abelian, then Γ acts on H3 = H3∪∂H3
as a (discrete) convergence group. Specifically, if {γn} is a sequence of distinct elements of Γ,
then there exists w,z ∈ Λ(Γ) (not necessarily distinct) and a subsequence, still called {γn} so
that γn(x)→z uniformly on compact subsets of H3−{w}.
Proof. Let{γn} is a sequence of distinct elements of Γ and let x0 = (0, 0, 1)∈ H3. We may
pass to a subsequence so that γn(x0)→z andγ−1
n (x0)→w. If x∈ H3, thend(γn(x0),γn(x)) =
d(x,x 0), so since γn(x0)→z, we see that γn(x)→z.
Now suppose thatx∈∂H3−{w}. Let Rn be the geodesic ray joining γ−1
n (x0) tox. Then Rn
converges to the geodesic L joining w to x. It follows that d(x0,Rn) is uniformly bounded, so
8 RICHARD D. CANARY
there exists xn∈ Rn so that d(xn,x 0) is bounded. Now consider any convergent subsequence
of γn(Rn), it will be a geodesic ray emanating from x0. Moreover, since d(γn(x0),γn(xn) is
bounded and γn(x0)→z, the ray R must emanate from z. Therefore, γn(x)→z.
In order to check that this convergence is uniform on compacta, we just need to check that if
{xn} is a sequence in H3−{w} converging tox∈ H3−{w}, then γn(xn)→z. If x∈ H3, then
d(xn,x ), and hence d(xn,x 0) is bounded for all large enough n, so γn(xn)→z. If x∈∂H3, let
Rn be the geodesic ray (or segment) joining γ−1
n (x0)→xn (for all large enough n) and proceed
exactly as before. □
Exercise: Prove that Λ(Γ) is the closure of the set of fixed points of elements of Γ. Observe that
if Λ(Γ) is not virtually abelian, then Λ(Γ) is the smallest non-empty closed subset of ∂H3 which
is invariant under Γ. Moreover, in this case Λ(Γ) is perfect, hence uncountable.
The complement Ω(Γ) = ∂H3\ Λ(Γ) of the limit set is called the domain of discontinuity.
Lemma 1.2. If Γ is a Kleinian group, then Γ acts properly discontinuously on Ω(Γ).
Proof. Let K be a compact subset of Ω(Γ). Suppose there exists a sequence γn of distinct
elements of Γ so thatγn(K)∩K is non-empty. Then, by Lemma 1.1, there exists a subsequence
{γn} andw,z ∈ Λ(Γ) so that γn(x)→z uniformly on compact subsets of ∂H3−{w}. Since K
is a compact subset of ∂H3−{w}, this is a contradiction. □
We can then consider the conformal boundary
∂cNΓ = Ω(Γ)/ρ(Γ)
which has the structure of a Riemann surface. Notice that the conformal boundary can be
empty, for example if NΓ is cocompact. We can combine the hyperbolic manifold and its
conformal boundary to obtain the conformal bordification
bNΓ = (H3∪ Ω(Γ))/Γ =NΓ∪∂cNΓ
If Γ is a Fuchsian group uniformizing a closed surface S, then ∂cNΓ is two copies of the
surface S (one the quotient of the upper half-plane and the other is the quotient of the lower
half plane) and their is an anti-conformal involution of ∂cNΓ which switches the two surfaces
(which is the just the quotient of the map z→ ¯z). Moreover, bNΓ∼=S× [0, 1].
If Γ is the Schottky group constructed above, then F is a fundamental domain for the action
of Γ on Ω(Γ), so one may easily check that ∂cNΓ is a closed surface of genus n. One can further
check that bN is a handlebody of genus n.
The convex hull of the limit set CH (Λ(Γ)) is defined to be the smallest closed convex subset
of H3 containing all bi-infinite geodesics with end points in Λ(Λ(Γ)). Concretely, CH (Λ(Γ))
is the union of all ideal tetrahedra with endpoints in the limit set. (The convex hull clearly
contains all such ideal tetrahedra and is clearly closed, it only remains that any geodesic joining
points in ideal tetrahedra T1 andT2 lies in the union of all ideal tetrahedra whose endpoints lie
in the union of the endpoints of T1 and T2.) The convex core is then given by
C(NΓ) =CH (Λ(Γ))/Γ⊂NΓ
Notice that sinceCH (Λ(Γ)) is convex, there exists a well-defined retraction, called thenearest
point retraction,
˜r : H3→CH (Λ(Γ))
IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS 9
so that ˜r(x) is the unique point on CH (Λ(Γ)) closest to x. (Notice that if x̸=y and d(z,x ) =
d(z,y ) then there exists a point u∈ xy so that d(z,u ) < d(z,x ).) Since CH (Λ(Γ)) is ρ(Γ)-
invariant, ˜r isρ-equivariant, so descends to a retraction, still called the nearest point retraction,
r :NΓ→C(NΓ).
It is often useful to consider the closed neighborhoodC1(Nρ) of radius one of the convex core.
C1(Nρ) is the quotient of the closed neighborhood of radius one of the convex hull of the limit
set. One key feature here is that C1(N) is strictly convex (since if d(x,w ) = 1 and d(y,z ) = 1
and u lies in the interior of xy, then d(u,wz)< 1).
Lemma 1.3. If Γ is a Kleinian group which is not virtually abelian, then ∂C1(Nρ) is a C1-
submanifold.
Proof. Consider the map f : H3−CH (Λ(ρ))→ (0,∞), given by f(x) = d(x,r (x)). By the
regular value theorem, It suffices to show that f is a C1-submersion. If y∈ H3−CH (Λ(Γ)),
then let Py be the totally geodesic plane through x which is perpendicular to yr(y), which is a
support plane for CH (λ(ρ) if g(x) = d(y,x ) and h(y) = d(x,Py), then h(x)≤f(x)≤g(x) for
all x in the same component of H3−Px as x. Moreover, f(y) = g(y) = h(y) and f and h are
differentiable aty and the have the same derivative at y (which is simply the dot product with
the unit tangent vector to yr(y) pointing towards y), so f is differentiable at y. Notice that f
is a submersion at y, since the restriction of f to−−−→r(y)y is a submersion. □
Remark: With a little more care, one can show that ∂C1(NΓ) is actually C1,1.
Suppose that x,y∈NΓ−C1(NΓ) and−−−→r(x)x and r(y)y intersect∂C1(NΓ) at the same point
z, thenr(z) =r(y) =r(x), so−−−→r(x)x =−−−→r(y)y =−−−→r(z)z. It follows that there is a homeomorphism
F :NΓ−C(NΓ)→∂C1(NΓ)× (0,∞) given by F (x) =
−−−→r(x)x∩∂C1(NΓ),d (x,r (x))

.
(Notice that if r(x) = r(y) it need not be the case that −−−→r(x)x =−−−→r(y)y, which is another main
reason we work mostly with C1(NΓ).)
One may continuously extend ˜r to a map ∂˜r : Ω(Γ)→CH (Λ(Γ)) by letting ˜r(z) be the first
point of contact of an expanding family of horospheres based at z with CH (Λ(Γ)). Again, ˜r
descends to a map
∂r :∂cNΓ→C(NΓ).
We can then define a homeomorphism
∂F :∂cNΓ→∂C1(NΓ) given by ∂F (z) =−−−→r(z)z∩∂C1(NΓ).
One may use F and ∂F to construct a homeomorphism
G : bNρ→C1(NΓ)
where if x∈C(NΓ) then G(x) =x, if x∈NΓ−C(NΓ), then
G(x) =F−1
−−−→r(x)x∩∂C1(N), 1− 1
1 +d(r,r (x))

and if z∈∂cNΓ, then G(z) =∂F (z). So we see:
10 RICHARD D. CANARY
Proposition 1.4. If Γ is a Kleinian group, then bNΓ is homeomorphic to C1(NΓ).
We say that Γ is convex cocompact if C1(NΓ) is compact. Notice that this is equivalent to
requiring that either bNΓ or C(NΓ) is compact.
If ρ is convex cocompact, then we identified Nρ−C1(Nρ) with C1(Nρ)× (1,∞). We may
then show that in these coordinates Nρ−C1(Nρ) is bilipschitz to the metric
cosh2tds2
∂C1(Nρ) +dt2
where ds2
∂C1(Nρ) is the intrinsic metric on ∂C1(Nρ) and t is the real coordinate. (This fact is
implicit in the work of Epstein-Marden [35]. See Section 4.2 of Biringer-Souto [11] for a more
precise discussion.)
We observe that convex cocompact Kleinian groups contain no parabolic elements.
Corollary 1.5. If NΓ = H3/Γ is a convex cocompact hyperbolic 3-manifold, then Γ contains no
elliptic or parabolic elements, so every non-trivial element of Γ is hyperbolic.
Proof. Let Γ be a convex cocompact Kleinian group and let π : H3 → NΓ be the obvious
covering map. Γ contains no elliptic elements, since Γ acts freely on H3. If Γ contains a
parabolic element α, then there exists a sequence {yn}⊂ CH (Λ(Γ)) so that d(yn,α (yn))→ 0.
(One obtains such a sequence by approaching the parabolic fixed point of α along a geodesic
in CH (Λ(Γ)). This implies that the injectivity radius inj NΓ(π(yn)) of π(yn) in NΓ converges
to 0. This is a contradiction since C(N) is compact, π(yn)∈C(N) and every point in N has
positive injectivity radius. □
