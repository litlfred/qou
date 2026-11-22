---
doc_id: arxiv-math-0611504v1
doc_title: "QUANTUM HYPERBOLIC GEOMETRY"
section_id: sec-007-31-efficient-triangulations
section_title: "Efficient triangulations"
section_number: 3.1
pages: 13-14
source_pdf: 0611504v1.pdf
source_sha256: a33d2771c873a97e
toc_source: outline
doc_brief: "Quantum hyperbolic geometry — 25 sections: Front matter; Introduction; Universal QHG"
duplicate_of: "agt-v7-n2-p13-s"
---
from S the interior of small 2-disks Di such that vi ∈∂Di.
A triangulation T ′ of S with the set of vertices equal to V is called a topological ideal triangulation
of S \ V . Given such a T ′, we need a marking of corners of the 2-simplices. The best suited to
3-dimensional extension are induced by global branchings b′ of T ′, and it is known that pairs (T ′, b′)
always exist. Then, as in section 2, we have a sign function σ = σ(T ′,b′). A corner map v 7→cv
associates to each vertex v of T ′ the corner at v of a triangle, say tv, in its star. We say that v 7→cv
is t-injective if v 7→tv is injective.
Lemma 3.1. For every (g, r)̸ = (0, 3), every triangulation T ′ of S with r vertices admits t-injective
corner maps.
Proof. For (g, r) = (0, 4) or g > 0 and r = 1, it is immediate to construct such a triangulation.
Subdividing a triangle by taking the cone from an interior point preserves the existence of t-injective
corner maps. By induction on r we deduce that for every (g, r)̸ = (0, 3) there exist triangulations of
S as in the statement.
In Figure 6 the corner selection is speciﬁed by a ∗, and the rows show all the possible ﬂip moves on
triangulations of S, up to obvious symmetries, that preserve the injectivity of corner maps. Consider
triangulations T ′, T ′′ of S with r vertices, such that T ′′ supports a t-injective corner map. It is well
known that T ′′ is connected to T ′ via a ﬁnite sequence of ﬂips. The t-injective corner map for T ′′
yields a t-injective corner map for T ′ by decorating these ﬂips as in Figure 6.
✷
*
*
*
*
*
*
*
*
*
*
Figure 6.
The ﬂips with marked corners.
14
ST´EPHANE BASEILHAC1 AND RICCARDO BENEDETTI2
There are no obstructions to use arbitrary corners maps in what follows. Specializing to injective ones
just simpliﬁes the exposition. For (g, r) = (0, 3), triangulations have two 2-simplices, one with two
selected corners. From now on, we assume that (g, r)̸ = (0, 3), the extension to the (0, 3) case being
straightforward.
Given a pair (g, r)̸ = (0, 3) and (T ′, b′) as in Lemma 3.1, ﬁx a t-injective corner map v 7→cv. In the
interior of each triangle tv consider a bigon Dv with one vertex at v, and call v′ the other vertex.
Remove from tv the interior of Dv, and triangulate the resulting cell sv = tv \ Int(Dv) by taking the
cone with base v′. Repeating this procedure for each tv, we get a triangulation T of F with 2r vertices
and p + 2r triangles, where p denotes the number of triangles of T ′. The set of edges of T , E(T ),
contains E(T ′) in a natural way, and |E(T )| = |E(T ′)| + 4r. We extend b′ to a branching b on T as in
in Figure 7, and the sign function σ(T ′,b′) to the triangles of (T, b) in the natural way. Note that the
ﬁgure shows only one of the possible branching conﬁguration. In general we extend b′ to b so that we
can recover (T ′, b′) from (T, b) by “zipping” and “collapsing”, as suggested at the bottom of Figure
7. In what follows, for simplicity we will refer to this conﬁguration, as the treatment of the others is
similar.
v
v
v
v
T
T"
T’
zip
Figure 7.
The branched triangulated cell sv.
Deﬁnition 3.2. We call the pair (T, b) an eﬃcient triangulation (for short: e-triangulation) of F.
For each vertex v, the preferred innner triangle at v is the triangle τv in sv with an edge on ∂F whose
b-orientation coincides with the boundary orientation of F.
