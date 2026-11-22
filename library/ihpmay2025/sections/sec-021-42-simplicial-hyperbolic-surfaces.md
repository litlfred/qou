---
doc_id: ihpmay2025
doc_title: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS"
section_id: sec-021-42-simplicial-hyperbolic-surfaces
section_title: "Simplicial hyperbolic surfaces"
section_number: 4.2
pages: 27-28
source_pdf: IHPMay2025.pdf
source_sha256: 0440a39721552a9e
toc_source: outline
doc_brief: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS — These notes are designed to accompany my mini-course on hyperbolic 3-manifolds at IHP in May 2025."
---
Instead of working with minimal surfaces, we will work with simplicial hyperbolic surfaces.
The intrinsic metric on these manifolds will be hyperbolic except at a finite number of cone
points where the total angle around the cone points is greater than 2π. We interpret these cone
points as points of concentrated (or infinite) negative curvature. In particular, the intrinsic
metric on a simplicial hyperbolic surface is locally CAT(−1), i.e. every geodesic triangle in the
universal cover is at least as thin as a triangle in H2.
We will say that a finite graph T on a surface S is a triangulation if every component of
S −T is bounded by 3 edges (I.e. is the interior of a triangle). One key observation is that
every essential simple closed curve C on S can be extended to a triangulation of S with a single
28
RICHARD D. CANARY
vertex. One simply chooses a vertex v on C and adds disjoint edges which begin and end at v
(no two of which are homotopic rel boundary) until one achieves a triangulation.
A simplicial hyperbolic surface f : S →N is a map so that there exists a triangulation T of
S, so that the image of each face of T is a totally geodesic (filled) triangle in N and the total
angle around each vertex is at least 2π. One obtains a pull-back metric on S, which we call
τf, which is locally isometric to H2 at every point except (possibly) the vertices. If v ∈T (0) is
a vertex, then let a(v) be the total angle of the induced metric about v (i.e. the sums of the
internal angles of triangles with a vertex at v.) Since the area of a triangle is its angle defect
(i.e. the difference between π and the sum of the internal angles), we see that
Area(S, τf) = −2ξ(S) −
X
v∈T (0)
a(v) −2π ≤−2πξ(S)
where ξ(S) is the Euler characteristic of S.
Suppose that g : S →N is a π1-injective map and N has no cusps. If α is a simple closed
curve on S, we complete it to a triangulation T with only one vertex v on α. One may then
homotope g to a map taking v to a point on g(α)∗and pull the remaining edges and faces tight
so that their images are totally geodesic to obtain a map f : S →N. One may check that f is
actually a simplicial hyperbolic surface, by noticing that there is an edge through f(v) which
is a closed geodesic through f(v), so the total angle occuring on either side of this edge is at
least π, so that a(v) ≥2π as required. It may be easiest to understand the picture by looking
at the lifted map ˜f : ˜S →H3 from the universal cover to H3. In this picture, one may consider
the edges arranged around a lift ˜v of v, then there are two edges, both of which are “lifts” of
g(α)∗, which meet at ˜v and are antipodal, so any path of edges joining one edge to another
transverse a total angle at least π Another way to see this is to look at the set of unit tangent
vectors to f(S) at f(v). The set of tangent vectors is a path in T 1
f(v)N and a(v) is the length
of this path. Since the path contains antipodal points, it has length at least 2π. We will say
that f is a simplicial hyperbolic surface which realizes α with one vertex.
If g is not π1-injective, then the above construction works as long as g(α) is homotopically
non-trivial and we can choose T so that every edge of T determines a homotopically non-trivial
loop in N.
