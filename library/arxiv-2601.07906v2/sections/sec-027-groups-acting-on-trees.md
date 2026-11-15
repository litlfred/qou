---
doc_id: arxiv-2601.07906v2
doc_title: "A universal sum over topologies in 3d gravity"
section_id: sec-027-groups-acting-on-trees
section_title: "Groups acting on trees"
section_number: null
pages: 89-91
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
toc_source: outline
doc_brief: "A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
Groups acting on trees
The motivation for studying Bass-Serre theory is that the fundamental groups gen-
erated by the gravitational machine are described using amalgamated products and
HNN extensions. In this setting, the machine provides a graph of groups, and our
goal is to reconstruct the associated group from this graph. We also want to build
a tree on which this group acts. The passage from a graph of groups to a tree with
a group action is the content of the Fundamental Theorem of Bass-Serre theory.
This theorem is explained in the next section; here, we provide the formal definitions
needed in the construction.
Trees.
An oriented tree T = (˜V, ˜E)43 is a connected graph with a collection of
vertices ˜v ∈˜V and oriented edges ˜e ∈˜E such that there are no loops. That is, every
43We use the tilde notation to refer to the vertices and edges of the tree. The notation without
a tilde refers to the vertices and edges of the graph of groups.
– 89 –
pair of vertices ˜v, ˜w ∈˜V is connected by exactly one path. In particular, a tree has
no multi edges. For each edge ˜e we denote its target (the vertex the edge points to)
by ˜e+ and its source by ˜e−. The trees considered below are typically infinite, and
vertices may have infinitely many adjacent edges.
In a tree, there is a unique path (without backtracking) that connects any two
vertices. This path is called the geodesic between the vertices, and its length is the
distance between them. The distance from ˜v to ˜w is denoted by d(˜v, ˜w). We have
d(˜v, ˜v) = 0, and d(˜v, ˜w) = 1 if ˜v and ˜w are adjacent.
Let G be a group acting on T. We assume that the action of G on T preserves
edge orientations, so edge inversions are not allowed. Let Fix(g) = {˜x ∈T | g˜x = ˜x},
then every g ∈G comes in two forms:
• Elliptic: Fix(g) is not the empty set, i.e. a number of vertices is stabilized.
• Hyperbolic: g stabilizes a unique geodesic set-wise; i.e. g translates along an
infinite line through the tree.
There are no other options. For example, translations by an integer on the real line
correspond to hyperbolic elements. In the case of D∞, the two Z2 components as
well as their conjugates are elliptic elements. For the Farey tree, S and ST and their
conjugates are elliptic, while the hyperbolic elements are those matrices in PSL(2, Z)
whose trace has absolute value larger or equal to two.
Graph of groups.
For a group G acting on a tree T, we can form the quotient
T/G, where we identify all edges in a group orbit and all vertices in a group orbit.
The resulting space is still a graph, but not necessarily a tree. For the four examples
of Z, D∞, PSL(2, Z) and SL(2, Z), the quotient graphs look like
,
,
,
.
(B.13)
The first example shows that the quotient need not be a tree. The other three quo-
tient graphs look identical. Clearly, taking the quotient forgets a lot of structure.
The main idea of Bass-Serre theory is to upgrade this quotient of trees to a graph
of groups. For a graph of groups, we retain the additional information regarding the
stabilizers of the relevant vertices and edges. Let us give the formal definition.
A graph of groups Γ = (V, E, GV, GE) consists of the following objects:
• An underlying connected oriented graph with a set of edge E and a set of
vertices V. Multi-edges and loops are allowed. For every edge e ∈E, we denote
the corresponding target vertex again by e+ and the source vertex by e−.
• A group Ge to every edge e ∈E and a group Gv to every vertex v ∈V. Every
edge group injects naturally in both the source and the target vertex group,
Ge ,−→Ge±.
– 90 –
• Boundary maps, that is group homomorphisms describing the inclusions ∂+
e :
Ge →Ge+ and ∂−
e : Ge →Ge−.
The quotient T/G described above naturally carries the structure of a graph of
groups. Indeed, we can associate to every vertex v ∈T/G and edge e ∈T/G the
stabilizer groups Stab(˜v) = {g ∈G | g˜v = ˜v} and Stab(˜e), respectively. Here, ˜v and
˜e are elements of the tree T which have been lifted from the quotient T/G. For a
stabilized edge ˜e, also the source and target vertices ˜e−and ˜e+ are stabilized, which
gives natural inclusions Stab(e) ,→Stab(e±) yielding the monomorphisms ∂±
e . These
constructions depend in principle on the chosen lifts, but this only conjugates the
monomorphisms. In particular the resulting graph of groups for different choices are
isomorphic.
