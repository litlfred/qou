---
doc_id: arxiv-math-9201302v1
doc_title: "The Quantum G 2 Link Invariant"
section_id: sec-002-21-topological-preliminaries
section_title: "Topological preliminaries"
section_number: 2.1
pages: 4-5
source_pdf: 9201302v1.pdf
source_sha256: 67987dd432f58488
toc_source: inferred
doc_brief: "The Quantum G_2 Link Invariant — We derive an inductive, combinatorial deﬁnition of a polynomial-valued regular isotopy invariant of links and tangled graphs."
---
Topological preliminaries
By a planar graph we mean a ﬁnite combinatorial graph which is embedded in the sphere S2. We allow
planar graphs to have edges which go in a circle and have no vertices, as well as a multiple edges between
vertices and vertices connected to themselves. A face of a planar graph is a connected component of the
complement of the graph. When interpreting the illustrations of planar graphs in this paper, the reader
should identify the border of the page to a point.
Let D be a disk in S2. We deﬁne a planar graph with boundary to be the intersection of D with a planar
graph which is transverse to the boundary of D. Thus a planar graph with boundary is a graph which is
embedded in a disk such that the edges of the graph meet the boundary of the disk transversely at special
vertices of degree 1, called endpoints. The boundary of a planar graph in D is deﬁned to be the boundary
of D together with the endpoints and an inward-pointing normal. If b is a boundary, the opposite boundary
−b is deﬁned to be the same object with the distinguished normal vector reversed. In this paper we will
consider graphs decorated in various ways and it is understood that the endpoints of a graph with boundary
should be decorated correspondingly. For example, if the edges of a graph are colored, the endpoints should
be assigned the same colors. If the edges are oriented, each endpoint should be assign a distinguished normal
vector. The idea is that if two possibly decorated planar graphs have opposite boundaries, their union should
be a planar graph without boundary decorated in the same way.
We deﬁne a graph projection to be a planar graph with special tetravalent vertices, called crossings, such
that one pair of opposite incoming edges is labeled as passing “over” the other pair, like so:
We deﬁne a graph projection with boundary similarly.
We deﬁne a regular isotopy of a graph projection to be a sequence of operations consisting of ambient
isotopy of the 2-sphere and the following combinatorial moves:
1.  
  ⇒  
2.  
  ⇒  
3.  
  ⇒  
4.  
  ⇒  
There are versions of the last two moves for every possible kind of vertex in the graph, although the moves
are only illustrated for a trivalent vertex. We deﬁne a tangled ribbon graph (introduced in [11]) to be an
equivalence class of graphs projections under regular isotopy. Regular isotopy moves for graph projections
with boundary are the same, except that an ambient isotopy must leave the boundary of the graph ﬁxed.
We can also consider regular isotopy of graphs decorated in various ways; there is a version of each regular
isotopy move for every possible decoration of the arcs involved in the move.
Two important classes of graph projections are those with no vertices, which are called link projections,
and those with only trivalent vertices, which we will call freeway projections.
(A link projection with
boundary is allowed to have univalent vertices at the boundary.) Here is an example of a freeway projection:
A ribbon link (also called a framed link) is an equivalence class of link projections, a freeway is an equivalence
class of freeway projections, a ribbon link with boundary (also called a framed tangle) is an equivalence class
of ribbon links with boundary, and a freeway with boundary is an equivalence class of freeway projections
with boundary. Here is an example of a freeway projection with boundary:
A tangled ribbon graph has a natural 3-dimensional interpretation as (the equivalence class under ambient
isotopy of) a graph embedded in S3 together with a (continuous) distinguished normal vector at each point.
Alternatively we can think of a tangled ribbon graph as a graph embedded in S3 together with a ribbon
(a long, thin rectangle) assigned to each edge and a disk assigned to each vertex with the incident ribbons
attached at the boundary in such a way that an oriented surface results. A graph projection is then the
projection of the graph in the usual sense, where the normal vector everywhere points upward out of the
plane of the projection, or the surface consisting of the ribbons and disks lies ﬂat against the plane of the
projection. A tangled ribbon graph with boundary can be thought of as a graph, with its ribbons or normal
vectors, embedded in a ball in S3 and with its endpoints lying at the boundary of the ball.
We deﬁne a freeway invariant to be a function deﬁned on freeway projections which depends only on the
underlying freeway.
