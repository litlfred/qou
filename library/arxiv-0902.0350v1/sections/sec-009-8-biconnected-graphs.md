---
doc_id: arxiv-0902.0350v1
doc_title: "A REVISION OF THE PROOFOF THE KEPLER CONJECTURE"
section_id: sec-009-8-biconnected-graphs
section_title: "Biconnected graphs"
section_number: 8
pages: 22-35
source_pdf: 0902.0350v1.pdf
source_sha256: 4591687132c93973
doc_brief: "A REVISION OF THE PROOFOF THE KEPLER CONJECTURE — The Kepler conjecture asserts that no packing of congruent balls in three-dimensional Euclidean space has density greater than that of the"
---
This section gives further detail to the argument of [14,§12.7 p.131]. There
it is claimed that the proof of the main estimate [14, Theorem 12.1] can be
reduced to the case of polygonal standard regions. This claim is correct.
However, the justification of this claim is not complete in the original proof.
This section gives complete justification of the claim. The main result is
Theorem 3, stated below.
This section patches the original proof. As such, it should be imagined
this section to be inserted as an addendum, directly following Section 12.13
in the original proof, as a new Section 12.14. (In fact, Section 12.13 is
itself an addendum to the 1998 preprint, making this section the second
addendum to Section 12.) If the actual insertion were to be carried out, the
corresponding changes to the numbering of the results in this section would
be made: Theorem 3 below would be inserted as a new Theorem 12.21, and
so forth.
In the original proof, the boundaries of standard regions may fail to be sim-
ple polygons. In fact, the failure of the boundaries to be polygons may be
quite severe: the boundaries may contain multiple components and articu-
lation vertices. Anarticulation vertex in a graph is a vertex whose removal
increases the number of connected components of the graph. A connected
graph isbiconnectedif it contains no articulation vertex.
In the original proof, each standard region is first prepared by a process of
erasure (described in [14,§11.1]), then deformed in a way to transform its
boundaryintoasimplepolygon. Thedeformationismadeinsuchawaythat
the values of two key functions vor0,R and τ0,R are left unchanged. These
are the functions that enter into the main estimate [14, Theorem 12.1].
Whattheoriginalprooffailstoconsiderisaparticularhypotheticalsituation
where the deformation might fail. This situation is illustrated in Fig. 3,
where the rigid movement of set of vertices (such as the illustrated triangle
with vertexw) is blocked by a nearby vertexv that is not visible fromw,
when the distance betweenv and w drops to the minimum value2. This
section presents a proof that this hypothetical situation does not occur.
The strategy of the proof in this section is to use a deformation argument.
A general decomposition star is deformed until the graph attached to it
becomes biconnected. In a biconnected planar graph with at least three
vertices, each face is a simple polygon. Thus, by producing a biconnected
A REVISION OF THE PROOF OF THE KEPLER CONJECTURE 23
v u
w
Figure 3. In this figure (not to scale), segments represent
geodesic arcs on the unit sphere. The shaded region is a sub-
region whose boundary is not a simple polygon. We wish to
rigidly slide the triangle containing the vertexw until a new
visible distinguished edge forms (say fromw to u). We will
show that this rigid motion does not decrease the distance
between two vertices (sayw andv) to the minimum distance
2.
graph, we achieve our objective. In the original proof of the Kepler conjec-
ture, biconnected graphs are not mentioned by name. Nevertheless, most of
the graphs that occur in the late stages of the original proof are biconnected.
In more detail, the proof in this section will produce a sequence of admissible
deformations of a decomposition starD in such a way that the individual
standard regionsR are preserved in number and identity (but not in shape)
by the deformations. The deformations will preserve the values of vor0,R(D)
and τ0,R(D), for each standard regionR. The deformations will change the
combinatorial structure of the graph formed by all the subregions of the
decompositionstar. Attheconclusionofthedeformation, thedecomposition
starD will have a graph (formed by all the subregions of the decomposition
star) that is biconnected. As in the original proof, the decomposition star
is first simplified by a process of erasure, before the deformations begin.
In the remainder of this section, we adopt notation, definitions, and conven-
tions without further comment from [14].
8.1. Context. We work in the following restrictive context for Theorem 3
and its proof. We fix a packing centered at a vertex at the origin. As
described in Section 12.6 of the original proof, we assume that all upright
quarters are erased, except loops (that is, those surrounded by anchored
simplices). LetU be the set of (non null) vertices of of height at most2.51.
24 HALES, HARRISON, MCLAUGHLIN, NIPKOW, OBUA, AND ZUMKELLER
As usual, we say two edges{u1,u 2} and{u′
1,u′
2} cross if the interiors of the
triangles formed by{0,u 1,u 2} and{0,u′
1,u′
2} intersect.
We form the set of edgesE′ between vertices inU, consisting of
• all standard edges; that is,{v,w}⊆ U such that0<||v−w||≤ 2.51.
• all edges{v,w}⊆ U of an anchored simplex, whenever the upright
diagonal of the anchored simplex is an unerased loop.
• all edges{v,w}⊆ U such that0<||v−w||≤
√
8, where{v,w} does
not cross any other edge in previous two items. (If two of these edges
cross, pick only one of them. This can only happen with conflicting
diagonals of a quad cluster.)
These edges do not cross. Aspecial simplex{0,u,v,w } has one edge{v,w}
of length at least
√
8, called thespecial edge. A special edge has length at
most 3.2. The other vertexuis called aspecial vertex(orspecial corner). Let
E =E′\S, whereS is the set of special edges (that is, the edges of special
simplices shared with an anchored simplex). The projection of the line
segments formed byE to the unit sphere is a planar graph. The complement
of this graph in the unit sphere is a disjoint union of connected components.
The closures of these connected components are calledsubregions.
We call aloop subregionone that contains an unerased loop{0,v}. If R is
a loop subregion, then there are no enclosed vertices of height≤ 2.51 over
the subregion. The corners of R are the anchors of the upright diagonal
together with the special corners of the subregion. The subregionR is star
convex with center point at the projection ofv to the unit sphere. It follows
that the boundary ofR is a simple polygon.
The graphΓ with verticesU and edgesE is not necessarily connected. The
aim is to deformU (andD) to create a biconnected graph (without changing
the values of vor0,R(D) and τ0,R(D) for standard regionsR; the values for
individual subregions will change). Once the graph Γ is biconnected, the
subregions are simple polygons as desired.
The deformation ofU is admissible if it satisfies the following three condi-
tions.
• If the graphΓ is not connected, the deformation acts by a rotation
about the origin on the vertices of a single chosen connected com-
ponent of Γ, leaving all other vertices ofU fixed. (For example,
in Figure 3, the entire triangle with vertexw may be rotated.) In
particular,||v||, forv∈U, is constant.
A REVISION OF THE PROOF OF THE KEPLER CONJECTURE 25
Figure 4. Theorem 3 breaks into various cases: (a) two
edges with distinct endpoints, (b) three or more edges, (c)
two edges, or (d) a single edge passing through the triangle
{0,v,w}.
• If the graph Γ is connected, but not biconnected, with a chosen
articulation vertexa, then the deformation acts by a rotation about
the axis{0,a}on thevertices ofa single component ofΓ\{a}, leaving
all other vertices ofU fixed.
• The distance betweenv,w remains at least2, for allv,w ∈U.
The deformation stops when either of the followinghalting conditions are
met:
(H1) ||v−w||≤
√
8, where the edge{v,w}⁄∈ E′, with{v,w}⊆ U, does
not cross any edge inE′, or
(H2) ||v−w||decreases to2 for somev,w ∈U, and{v,w} crosses an edge
in E′.
We warn that the deformation is allowed to assume configurations in which
the distance between someu∈ U and the upper endpoint of an unerased
upright diagonald is less than2. This is not a problem because the vertex
u does not end up as a corner of the loop subregion to which the upright
diagonaldbelongs. (In particular, the halting condition (H1) prevents a new
special vertex from being added to a loop subregion.) Thus, when a single
subregion is considered in isolation, all distances between pairs of vertices
in that subregion are at least2.
In the restrictive context that has been described in this section, we have
the following result.
Theorem 3. If the graph Γ = (U,E ) is not biconnected, then a nontriv-
ial admissible deformation ofU exists. The halting condition (H2) never
holds. The admissible deformation can always be continued until the halting
condition (H1) holds.
We break the proof of Theorem 3 into cases (a), (b), (c), (d) according to the
number and combinatorial structure of the edges{u1,u 2} that pass through
26 HALES, HARRISON, MCLAUGHLIN, NIPKOW, OBUA, AND ZUMKELLER
the triangle{0,v,w}. See Figure 4. Lemma 4 below gives Case (a): we
cannot have two such edges{u1,u 2} and{u′
1,u′
2} with distinct endpoints. It
follows that there is an endpointu2 shared by every edge that passes through
the triangle{0,v,w}. Lemma 9 below gives Case (b): there cannot be three
or more edges. Finally, Cases (c) and (d) of one or two edges{u1,u 2} are
treated in further subsections. Each subsection is organized around one of
the main cases (with introductory Section 8.2): Cases (a), (b), (c), and (d)
are treated in the four Sections 8.3, 8.4, 8.5, 8.6, respectively.
When U is deformed until the halting condition (H1) holds, a new edge
{v,w} can be added toE. The theorem is repeated to add further edges,
until a biconnected graph is obtained. The remainder of this section explains
why the halting condition (H2) never holds. For this, we assume on the
contrary, that||v−w|| = 2, where{v,w} belong to different connected
components ofΓ (if Γ is not connected) and different connected components
of Γ\{a} (if a is an articulation vertex of a connected graphΓ). When
this situation occurs, we say thatv,w belong to different bicomponents.
Without loss of generality, we may also assume that{v,w} crosses some
edge ofE′.
8.2. Preliminary lemmas. Lemma 1 below shows that a vertex does not
cross over an edge during a deformation; the halting conditions for the vertex
are met before it reaches the edge. Recall that the termgeometric consid-
erations refers to a specific collection of methods introduced in [22,§4.2]
to prove the existence and non-existence of various simple configurations of
points in R3.
Lemma 1. LetS ={0,v,,u 1,u 2} be a set of four distinct points inR3 whose
pairwise distances are at least2. Suppose that||u||≤ 2.51, for allu∈S. If
the segment{0,v} meets the segment{u1,u 2}, then||v−u1||,||v−u2||≤
2.51.
Proof. This follows by geometric considerations. □
The next two lemmas give conditions under which the halting condition (H2)
cannot hold.
Lemma 2. Let S ={v,w,u 1,u 2,v 0} be a set of five distinct points inR3
whose pairwise distances are at least2. Suppose that the segment{v,w}
passes through{v0,u 1,u 2}. Assume
||u1−u2||≤ 3.2,
||v0−u||≤ 2.51, for u∈S.
Then||v−w||> 2.
A REVISION OF THE PROOF OF THE KEPLER CONJECTURE 27
Proof. This follows by geometric considerations. □
Lemma 3. Let S ={v,w,u 1,u 2,v 0} be a set of five distinct points inR3
whose pairwise distances are at least2. Suppose that the segment{u1,u 2}
passes through{v0,v,w}. Assume
||u1−u2||≤ 2.91,
||v0−u||≤ 2.51, for u∈S.
Then||v−w||> 2.
Proof. This follows by geometric considerations. □
By Lemmas 2 and 3, we may assume that for each edge{u1,u 2} that{v,w}
crosses, we have that{u1,u 2} passes through{0,v,w} and that||u1−u2||>
2.91. This means that the edge{u1,u 2} is an edge of an anchored simplex,
so that the edge is special or bounds a loop subregion. This loop subregion
will provide the key to the proof, because we will show that it prevents the
distance betweenv and w from becoming 2, as assumed (Fig. 5).
Remark 1. As an aside, we mention that this issue of biconnected graphs
is a major issue only in the proof of the Kepler conjecture and not in the
proof of the dodecahedral conjecture[23]. In the proof of the dodecahedral
conjecture there are no loops of anchored simplices, and without loops there
are no difficulties: edges of length at most
√
8 can be be used instead of the
set E′. Lemmas 2 and 3 suffice.
8.3. Case (a): Edge crossings with distinct endpoints.
Lemma 4. There does not exist a setS ={0,v,w,u 1,u 2,u′
1,u′
2} of seven
distinct points inR3 whose pairwise distances are at least2 and that satisfies
the following conditions.
• The edges{u1,u 2} and{u′
1,u′
2} do not cross.
• The edges{u1,u 2} and{u′
1,u′
2} both pass through{0,v,w}.
• ||u||≤ 2.51 for allu∈S.
• ||v−w|| = 2.
• ||u1−u2||,||u′
1−u′
2||≤ 3.2.
• u1 and u′
1 lie in the same half-space bounded by the plane{0,v,w}.
• The directed segment fromv tow crosses the segment{u′
1,u′
2} before
the segment{u1,u 2}.
Note that the last two conditions can always be achieved by suitable labels
on the points{u1,u 2,u′
1,u′
2}.
28 HALES, HARRISON, MCLAUGHLIN, NIPKOW, OBUA, AND ZUMKELLER
v
u
w
L
Figure 5. In this figure (not to scale), segments represent
geodesic arcs on the unit sphere. The two shaded regions
represent subregions. There are possibly other subregions
partitioning the unshaded portions of the figure. These other
subregions are not represented in this figure. The shaded re-
gion markedLrepresents a loop subregion. The other shaded
region represents a subregion with two boundary components
that is undergoing a deformation, by the motion of the tri-
angle with vertexv. The situation of Fig. 3 does not exist
(as will be shown). The intervening loop subregionL forces
v and w to be more than the minimum distance apart.
Proof. This will follow as a direct consequence of Lemmas 6 and 8 below.□
Lemma 5. LetS ={u,v,w} be a triangle such that each side has length at
least 2, and such that||u−v||≤ 2.51,||u−w||≤ 2.51,||v−w|| = 2. Let
X be the set of points in the convex hull ofS that have distance at least1.2
from each vertex ofS. Then the diameter ofX is less than1.044.
Proof. Let x = ||u−v|| and y = ||u−w||. Assume x≥ y. As u moves
away fromv, along a fixed line throughv and an initial positionu0, the
region X expands. Thus, we may assume that x = 2.51. The boundary
of X is a polygonal curve consisting of line segments and concave arcs of
circles. The diameter is realized by the distance between two verticespi(y)
of the polygonal curve. We consider two cases according toy≤ 2.4 and
y≥ 2.4 because the structure of the polygonal curve changes aty = 2.4. We
calculate||pi(y)−pj(y)|| directly, checking for each(i,j ) that the distances
are less than1.044. □
Lemma 6. LetS ={0,,v,w,u 1,u 2,u′
1,u′
2}⊆ R3 be a configuration of seven
points that satisfies the conditions of Lemma 4. Then there exist a pointp
A REVISION OF THE PROOF OF THE KEPLER CONJECTURE 29
on the segment{u1,u 2} and a pointp′ on the segment{u′
1,u′
2} such that
||p−p′||< 1.044.
Proof. Let u∈{ 0,v,w}. By the metric constraints, the distance fromu to
the segment{u1,u 2} (resp.{u′
1,u′
2}) is at least
√
22− (3.2/2)2 = 1.2.
Let p (resp. p′) be the point of intersection of the segment{u1,u 2} (resp.
{u′
1,u′
2}) with the convex hull of{0,v,w}. By Lemma 5, we have||p−p′||<
1.044. □
Lemma 7. Let S ={u1,u′
1,u 2,u′
2}⊆ R3 be a set of four distinct points
such that the distance between each pair of points is at least2. Assume that
||u1−u2||≤ 3.2, ||u′
1−u′
2||≤ 3.2.
If any of the following conditions hold:
(A) ||u1−u′
2||,||u′
1−u2||≥ 2.91;
(B) ||u1−u′
1||,||u2−u′
2||≥ 2.85, ||u1−u′
2||≥ 2.91; or
(C) ||u1−u′
1||≥ 3.64, ||u1−u′
2||≥ 2.91;
then every point on the segment{u1,u 2} has distance greater than 1.044
from every point on the segment{u′
1,u′
2}.
Proof. Assume for a contradiction that the assumptions hold and that the
conclusion is false for some configuration. The metric constraints can be
used to show that the segments{u1,u 2} and{u′
1,u′
2} can be stretched along
their axes without decreasing any edge length. Thus we may assume without
loss of generality that||u1−u2|| =||u′
1−u′
2|| = 3.2. Decreasing one dihedral
angle of the simplexS at a time, we may move the segments closer together,
until all four edges{ui,u′
j} attain their minimum length. Then we have
three rigidly determined simplices (A), (B), (C) (with equality constraints).
An explicit coordinate calculation of the distance between the two segments
shows that the distance is greater than1.044 in each case. □
Lemma 8. LetS ={0,,v,w,u 1,u 2,u′
1,u′
2}⊆ R3 be a configuration of seven
points that satisfies the conditions of Lemma 4. Then there do not exist a
pointp on the segment{u1,u 2} and a pointp′ on the segment{u′
1,u′
2} such
that||p−p′||< 1.044.
Proof. Assume for a contradiction that suchp,p′ exist. In Lemma 7, we may
assume that none of the conditions A, B, C hold. By obvious symmetry,
without loss of generality, we may assume by case A that||u2−u′
1||< 2.91.
By Lemma 3, this implies that{u′
1,u 2} does not pass through{0,v,w}. By
30 HALES, HARRISON, MCLAUGHLIN, NIPKOW, OBUA, AND ZUMKELLER
the conditions of the lemma, the segment{u1,u′
1} does not meet the plane
{0,v,w}, so that{u1,u′
1} does not pass through{0,v,w}. This means that
the triangle{u1,u′
1,u 2} is linked around{0,v,w}; and some edge of{0,v,w}
passes through{u1,u′
1,u 2}. Up to symmetry there are two cases: (1){0,v}
passes through{u1,u′
1,u 2}, or (2){v,w} passes through{u1,u′
1,u 2}.
In the first case, recall that{u′
1,u′
2}does not cross{u1,u 2}. Sou′
2 is enclosed
over (0,{u1,u′
1,u 2}). Then{u′
2,u 1} and{u′
2,u′
1} pass through{0,v,w}. By
Lemma 3, we have||u′
2−u1||,||u′
2−u′
1||≥ 2.91. As we are assuming that
C does not hold, we have||u1−u′
1||≤ 3.64. We claim that{0,u′
2} passes
through{u1,u′
1,u 2}. Otherwise, u′
2 lies in the convex hull of{0,u 1,u′
1,u 2}
and a coordinate calculation shows that the upper bounds on the edges
of the simplex{0,u 1,u′
1,u 2} are inconsistent with the lower bounds on the
distances fromu′
2 to the vertices of the simplex. Since{0,u′
2} passes through
{u1,u′
1,u 2} we may use geometric considerations to show that||u′
2||> 2.51.
This is contrary to the hypotheses of Lemma 4.
Inthesecondcase, {v,w}passesthrough{u1,u′
1,u 2}andthrough{u′
1,u′
2,u 2}.
Geometric considerations give||u1−u′
1||> 2.85 and||u2−u′
2||> 2.85. As-
suming that B does not hold gives||u1−u′
2||< 2.91. The first paragraph
of the proof now gives that{u2,u′
2,u 1} links around the triangle{0,v,w}.
The edge{v,w} does not pass through{u2,u′
2,u 1}. (This can be seen by
drawing the relative positions ofp(u), foru∈S, in the projectionp of the
points to a plane orthogonal to{v,w}.) Thus, we are in the first case, which
has already been treated. □
8.4. Case (b): T riple edge crossings. By Lemma 4, there is a common
endpointu2 such that every edge ofE′ that passes through{0,v,w} hasu2
as an endpoint. Next we show that there cannot be three such edges.
Lemma 9. There does not exist a set of seven distinct points
S ={0,v,w,u 1,u′
1,u′′
1,u 2}
in R3 that satisfies the following conditions.
• The distance between each pair of distinct points inS is at least2.
• The edges{u1,u 2},{u′
1,u 2}, and{u′′
1,u 2} pass through{0,v,w}.
• ||u||≤ 2.51, for allu∈S.
• ||v−w|| = 2.
• ||u−u2||≤ 3.2, foru =u1,u′
1,u′′
1.
Proof. Assume for a contradiction thatS exists. We may pivotw around the
axis{0,v} until||w−u2||≤ 2.51. (The metric constraints on edge lengths
show that the condition∆ > 0 is preserved for the simplices{u,u 2,v,w}
A REVISION OF THE PROOF OF THE KEPLER CONJECTURE 31
and{u,u 2,w, 0}, foru =u1,u′
1,u′′
1, throughout this pivot.) A similar pivot
ofv gives||v−u2||≤ 2.51. We may order the vertices in cyclic order around
{0,u 2} as
(w1,w 2,w 3,w 4,w 5) = (w,u 1,u′
1,u′′
1,v ),
so that settingd(wi,wj) = dih(0,u 2,wi,wj), we have
d(w1,w 5) =
4∑
i=1
d(wi,wi+1)≥d(w2,w 3) +d(w3,w 4).
Interval calculations2 give d(w2,w 3),d (w3,w 4)≥ 0.7 and d(w1,w 5) < 1.4.
We obtain an immediate contradiction:
1.4>d (w1,w 5)≥ 0.7 + 0.7.
□
8.5. Case (c): Double edge crossings. This subsection treats the case
of two edges crossings in the proof of Theorem 3. We continue to assume
the general context of Theorem 3. As usual, the edge{u1,u 2}∈ E′ crosses
{v,w}.
Lemma 10. Let{u1,u 2,w,v} be a set of four distinct points inR3 (in the
given context). Assume that ||v−ui|| ≤2.51, for i = 1, 2. Assume that
no edge ofE′ crosses{v,w} in the open half-spaceA containingv bounded
by the plane{0,u 1,u 2}. (That is,{u1,u 2} is the first edge to cross{v,w},
moving fromv towardw.) Assume there is a loop subregionL along{u1,u 2}
on theA-side of{u1,u 2}. Then{u1,u 2} is a special edge ofE′ with cornerv.
In particular,{u1,u 2}⁄∈ E, so that it is not a bounding edge of a subregion.
Proof. Assume for a contradiction that{u1,u 2} is not special. Note that
loop subregions have simple polygonal boundaries and remain rigid under
all the deformations. In particular, the upright diagonal, special corners,
and so forth remain rigidly positioned with respect to the corners of the
subregion.
Since there are no further edges crossing{v,w}, the subregionL extends to
v. Hencev is a corner of the subregionL. It is either an anchor or a special
corner (with respect toL). However, it cannot be a special corner, by the
assumption that{u1,u 2} is not a special edge. Hence it is an anchor. Also,
u1 and u2 are anchors.
To reach a contradiction, we consider possible locations of the upright diag-
onal{0,u}, and show that it has nowhere to go (Figure 6). Since{u1,u 2}
is an edge, the pointsu1,u 2 are consecutive anchors. This preventsu from
2calc-2799256461, calc-5470795818
32 HALES, HARRISON, MCLAUGHLIN, NIPKOW, OBUA, AND ZUMKELLER
A
BC
D
B
C
Dv
u1 u2
Figure 6. The upright diagonal u cannot be placed over
any of the regionsA,B,C,D . The lines (not to scale) repre-
sent geodesic arcs on the sphere passing through the pairs of
points in{p(u1),p (u2),p (v)}, wherep denotes projection to
the unit sphere.
lying over the regionB. Also, the upright diagonal of any unerased loop
has at least four anchors (sayv,u 1,u 2,w). Moreover, some anchored sim-
plex around the upright diagonal is not an upright quarter (because of the
edge{u1,u 2}). Geometric considerations based on these constraints (say
||w−u1||≥ 2.51) show that the fourth anchorw is not inA. This prevents
u from being located over the regionA. A vertexuj cannot be enclosed over
an upright quarter{0,u,v,u i}. This excludes region C. Finally, an edge
{v,ui} of length at most 2.51 cannot pass through a triangle{0,u,u j} of
sides at most2.51, 2.51,
√
8 (excluding D). □
Lemma 11. Let{u1,u 2,w,v} be a set of four distinct points inR3 (in the
given context). Assume that ||v−ui|| ≤2.51, for i = 1, 2. Assume that
no edge ofE crosses{v,w} in the open half-spaceA containing v bounded
by the plane{0,u 1,u 2}. (That is,{u1,u 2} is the first edge to cross{v,w},
moving fromv towardw.) Then both edges{u1,v} and{u2,v} belong toE.
In particular, there is a circuit of the graphΓ throughv,u 1,u 2.
Proof. If there is a loop subregionL along{u1,u 2} on theA-side of{u1,u 2},
Lemma 10 implies that{u1,u 2} is a special edge ofE′ with corner v. In
particular,{u1,v} and{u2,v} are edges ofE. The conclusion follows in this
case.
Now assume that there is no loop subregion along{u1,u 2} on theA side of
{u1,u 2}.
LetS be the finite set of points ofU enclosed over the simplex{0,u 1,u 2,v}.
We show by contradiction thatS is empty. The plane{0,v,w} separates
S into a disjoint unionS = S1∪S2, according to those in the same half-
space as ui, i = 1, 2. We form the convex hull of the projectionp to the
A REVISION OF THE PROOF OF THE KEPLER CONJECTURE 33
unit sphere of the pointsSi∪{ui,v}. As in [14,§12.13], form a sequence of
geodesic arcs on the unit sphere fromp(ui) to p(v). Let p(wi), forwi∈Si,
be the other endpoint of the arc starting atp(ui) (or setwi = v if Si =∅.
For somew′∈{ w1,w 2}\{ v}, the edges{w′,ui} do not cross any edges of
E. Furthermore, geometric considerations show that||w′−ui||≤ 2.51, for
i = 1, 2. By the criteria for forming edges ofE, we must have{w′,ui}∈ E
fori = 1, 2. This contradicts the assumption that{v,w} does not cross any
edges ofE overA. HenceS =∅.
Since S =∅, the edges{v,ui} do not cross any edges ofE. By the criteria
for forming edges ofE, they belong toE. This completes the proof. □
We are ready to prove the next major case of Theorem 3. We continue
to work in the general context of that theorem, withv and w in different
bicomponents of the graphΓ.
Lemma 12. In this context, there does not exist a set of six points{0,v,w,u 1,u′
1,u 2}
where{u1,u 2} and{u′
1,u 2} pass through{0,v,w} and such that
||u1−u2||≤ 3.2, ||u′
1−u2||≤ 3.2.
Proof. We argue by contradiction. We may assume that{u1,u′
1} are ordered
so that the cyclic order around{0,u 2} is (w1,w 2,w 3,w 4) = (v,u′
1,u 1,w ). By
the previous results, there are at most two edges that pass through{0,v,w}
in this manner. In particular, the part of the line segment{v,w} between
the crossings of{u1,u 2} and{u′
1,u 2} lies in a single subregionL.
We claim that we do not have||v−u′
1||,||v−u2||,||w−u1||,||w−u2||≤
2.51. Otherwise, we break into two cases and derive a contradiction as
follows. Either (1)L is a loop subregion, or (2)L is not a loop subregion,
but both regions adjacent to L (along edges{u1,u 2}, {u′
1,u 2}) are loop
subregions. In case (1), {u1,u 2,u′
1} are corners of the loop subregionL.
Hence, they lie on a circuit inΓformed by the corners of that loop subregion.
If||v−u2||,||v−u′
1||≤ 2.51, then by Lemma 11, the points{v,u′
1,u 2} lie on
a circuit inΓ. A similar conclusion holds if corresponding inequalities hold
||w−u2||,||w−u1||≤ 2.51. If all four inequalities hold, then these circuits
put v,w in the same bicomponent ofΓ, which is contrary to hypothesis. In
case (2), then by Lemma 11,{v,u 2},{v,u′
1}∈ E, so{u′
1,u 2} is a special
edge andL is a loop subregion. This is contrary to the assumption of case
(2). Hence we may assume by symmetry and without loss of generality that
||v−u′
1||≥ 2.51 or||v−u2||≥ 2.51.
We may stretch along the edges{u2,u 1},{u2,u′
1}, movingu1,u′
1, until||u2−
u1|| =||u2−u′
1|| = 3.2. We may add inequality
||u2||≤ 2.23,
34 HALES, HARRISON, MCLAUGHLIN, NIPKOW, OBUA, AND ZUMKELLER
forotherwisebygeometricconsiderations ||u2−u′
1||> 3.2. Similarly,||u′
1||≤
2.23. If||u2−v||≥ 2.51, we may pivotv towardu2 around the axis{0,w}
until||u2−v||≤ 2.51. Similarly, we may assume that||u2−w||≤ 2.51. Set
d(i,j ) = dih(0,u 2,wi,wj). Then interval arithmetic calculations3 give the
contradiction:
1.3>d (1, 4) =d(1, 2) +d(2, 3) +d(3, 4)> 0.5 + 0.8 + 0 = 1.3.
□
8.6. Case (d): Single edge crossings. This subsection treats the proof
of Theorem 3 in the case of a single edge crossing{u1,u 2}. This is the final
case of the proof. We continue to assume the notation and general context
of that theorem. In particular,v and w lie in different bicomponents of the
graph Γ.
Lemma 13. Let{0,u 1,u 2,v,w} be a set of five distinct points such that
{u1,u 2} is the only edge ofE′ that crosses{v,w}. Then||v−w||> 2.
Proof. We assume for a contradiction that||v−w|| = 2. We consider four
cases depending on lengths.
Case 1:||u−ui||≤ 2.51, fori = 1, 2 andu =v,w. By Lemma 11, there are
circuits running through{u,u 1,u 2}, foru = v,w. This is contrary to the
assumption thatv,w lie in different bicomponents of the graphΓ. (In the
remaining cases, there is no loss in generality to assume||w−u2||≥ 2.51.)
Case 2:||w−u2||≥ 2.51,||v−u1||≥ 2.51. Geometric considerations give
the contradiction||u1−u2||> 3.2.
Case 3:||w−u2||≥ 2.51,||v−u2||≥ 2.51. Geometric considerations gives
the contradiction||u1−u2||> 3.2.
Case 4:||w−u2||≥ 2.51,||v−ui||≤ 2.51, fori = 1, 2. The edge{u1,u 2}
cannot be a special edge ofE′. Otherwise,v,w are corners of the same loop
subregion. This contradicts the running assumption that these two vertices
belong to separate bicomponents of the graphΓ. By Lemma 10, there is no
loop subregion along{u1,u 2}on thev-side. Since{u1,u 2}has length greater
than
√
8, there is a loop subregionL bounded by the edge, and it must then
lie on thew-side. Thus,w is a corner ofL and the circuit ofΓ described by
the boundary ofL passes throughw,u 1,u 2. By Lemma 11, there is a circuit
of Γ through v,u 1,u 2. Hence, v,w lie in the same biconnected component,
which is contrary to the running assumption. □
3calc-7431506800, calc-5568465464, calc-4741571261, calc-6915275259
A REVISION OF THE PROOF OF THE KEPLER CONJECTURE 35
