---
doc_id: ihpmay2025
doc_title: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS"
section_id: sec-003-03-teichmüller-space
section_title: "Teichmüller space"
section_number: 0.3
pages: 4-6
source_pdf: IHPMay2025.pdf
source_sha256: 0440a39721552a9e
toc_source: outline
doc_brief: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS — These notes are designed to accompany my mini-course on hyperbolic 3-manifolds at IHP in May 2025."
---
A complete orientable Riemannian surface X is said to be hyperbolic if it is locally isometric
to H2. In this case, the universal cover ˜X is a simply connected complete Riemannian manifold
locally isometric to H2 and hence can be identified with H2. Therefore, X = H2/Γ where Γ
is a discrete subgroup of Isom+(H2) ∼= PSL(2, R). Notice that Γ is only well-defined up to
conjugacy, since the identification of ˜X with H2 is not canonical.
A marked hyperbolic structure on a closed oriented surface S is a pair (X, f) where f : S →X
is an orientation-preserving homeomorphism and X is a hyperbolic surface.
If X = H2/Γ,
then f∗: π1(S) →π1(X) ∼= Γ is an isomorphism and hence we obtain a discrete, faithful
representation ρ : π1(S) →PSL(2, R). However, ρ is only well-defined up to conjugation in
PSL(2, R).
One may build a hyperbolic surface of genus two, by starting with a regular hyperbolic
octagon, all of whose internal angles are π
4 and then gluing by the standard gluing pattern.
Similarly, one may build a hyperbolic surface of genus g by starting with a regular (4g −4)-gon
with internal angles
π
2g.
We will choose to formalize Teichm¨uller space by using representations. Recall that a marked
hyperbolic structure on a closed surface S, gives rise to a (conjugacy class of a) discrete,
faithful representation ρ : π1(S) →PSL(2, R).
In turn, a discrete, faithful representation
ρ : π1(S) →PSL(2, R) gives rise to a hyperbolic surface Xρ = H2/ρ(π1(S)). Since Xρ is homo-
topy equivalent to S, it is homeomorphic to S. Moreover, there is homeomorphism hρ : S →Xρ
so that (hρ)∗is conjugate to ρ. (Here, we are using a special property of the topology of closed
surfaces. The Nielsen-Baer Theorem, see Farb-Margalit [36, Chapter 8], gives that every ho-
motopy equivalence of a closed orientable surface is homotopic to a homeomorphism.) We then
let
eT (S) = {ρ : π1(S) →PSL(2, R) | ρ discrete, faithful, and hρis orientation-preserving}
and the Teichm¨uller space of S is the quotient
T (S) = eT (S)/PSL(2, R)
IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS
5
where eT (S) inherits a topology as a subset of Hom(π1(S), PSL(2, R)), PSL(2, R) acts by conju-
gation and T (S) inherits the quotient topology.
Alternatively, one may define T (S) to be the space of marked hyperbolic structure on S up
to the equivalence (X1, f1) ∼(X2, f2) if and only if f2 ◦f−1
1
is homotopic to an isometry. One
may think of X as hyperbolic clothing for the naked topological surface S and f as instructions
for how to wear the clothing. The equivalence relation allows one to adjust the clothing, but
not to wear it backwards or to stick your head through the hole designated for the arm.
It is a classical theorem, going back to the 19th century, that T (S) is homeomorphic to R6g−6
if g ≥2 is the genus of S. (Notice that π1(S) has a presentation with 2g relations and one
relation, one would expect that DF(π1(S), PSL(2, R)) has dimension (2g)3 −3 = 6g −3, so one
would predict that Teichm¨uller space has dimension 6g −6.) The mapping class group Mod(S)
is the group of (isotopy classes of) self-homeomorphisms of S. Fricke showed that the mapping
class group acts properly discontinuously, but not freely, on T (S) and its quotient is the moduli
space of unmarked hyperbolic structures on S.
We now give a quick sketch of the Fenchel-Nielsen coordinates on Teichm¨uller space. Suppose
that X is a closed orientable hyperbolic surface of genus g ≥2. Recall that, since X is negatively
curved, every homotopically non-trivial closed curve is homotopic to a unique closed geodesic.
Morever, if two homotopically non-trivial simple closed curves are disjoint and non-parallel,
then their geodesic representatives are also disjoint. Let α = {α1, . . . , α3g−3} be a maximal
collection of disjoint simple closed curves and let α∗be their geodesic representatives on X.
The components of X −α∗are a collection of 2g −2 hyperbolic pairs of pants with geodesic
boundary.
(A topological pair of pants is a disk with two holes.)
Therefore, every closed
hyperbolic surface may be built from hyperbolic pairs of pants.
If P is a hyperbolic pair of pants with geodesic boundary and s1, s2 and s3 are the shortest
paths joining boundary components (called seams), then P −{s1, s2, s3} is a pair of all-right
hyperbolic hexagons (i.e. hexagons all of whose interior angles are π
2 ). An all-right hexagon
is determined by the lengths of any 3 non-consecutive sides. Moreover, any 3 lengths can be
achieved. It follows that P is the double of the unique all-right hexagon with alternate sides
having lengths agreeing with the lengths of the seams of P. Moreover, we can build a geodesic
pair of pants with any collection of boundary lengths and this geodesic pair of pants is entirely
determined by its boundary lengths.
So the hyperbolic structure on X is determined, up to isometry, by the lengths of the com-
ponents of α∗and instructions for gluing the pants together. Since the pants are glued along
closed geodesic curves, there is a one-dimensional space of ways to glue them. This suggests
more forcefully that the space of hyperbolic structures on X has dimension 6g −6.
More formally, we get a map L : T (S) →R3g−3
+
where
L(X, f) =

ℓX(f(αi)∗)
3g−3
i=1 .
At each element of α we can define a twist coordinate in R which records how the geodesic
pairs of pants are glued along f(αi)∗, so we obtain Θ : T (S) →R3g−3. It is natural to think
at first that the twist should lie in S1. One way to see that this is not the case is to observe
that because we have marked the surface, we can detect the homotopy class of the shortest
curve crossing α. When you make a full positive twist, the shortest such curve changes by a
6
RICHARD D. CANARY
full negative twist (at least if it is unique). One can then see that
(L, Θ) : T (S) →R3g−3
+
× R3g−3 ∼= R6g−6
is a homeomorphism. For a careful discussion of twist coordinates see, for example, Thurston
[76, Section 4.6], Farb-Margalit [36, Section 10.6] or Martelli [51, Chapter 7].
References: Farb and Margalit [36] give a nice treatment of Teichm¨uller space from a modern
geometrical/topological viewpoint. Bers’ survey paper [7] is a beautiful treatment of the classical
complex analytic approach. Thurston [76, Section 4.6] gives a concise treatment of the Fenchel-
Nielson coordinates. Abikoff [1] gives a treatment of the classical theory with an eye towards
the modern viewpoint.
