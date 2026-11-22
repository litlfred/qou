---
doc_id: agt-v7-n2-p13-s
doc_title: "Quantum hyperbolic geometry"
section_id: sec-007-31-efficient-triangulations
section_title: "Efficient triangulations"
section_number: 3.1
pages: 25-27
source_pdf: agt-v7-n2-p13-s.pdf
source_sha256: affd571adbaac3fc
toc_source: outline
doc_brief: "Quantum hyperbolic geometry — 25 sections: Front matter; Introduction; Universal QHG"
---
Fix a surface F with r boundary components, obtained by removing from S the
interior of small 2–disks Di such that vi 2 @Di . The boundary of F is oriented via
the convention: last is the ingoing normal.
A triangulation T 0 of S with the set of vertices equal to V is called a topological
ideal triangulation of S n V . Given such a T 0, we need a marking of corners of
the 2–simplices. The best suited for 3–dimensional extension are induced by global
branchings b0 of T 0, and it is known that pairs .T 0; b0/ always exist. Then, as in
Section 2, we have a sign function  D .T 0;b0/. A corner map v 7! cv associates to
each vertex v of T 0 the corner at v of a triangle, say tv, in its star. We say that v 7! cv
is t –injective if v 7! tv is injective.
Lemma 3.1 For every .g; r/ ¤ .0; 3/, every triangulation T 0 of S with r vertices
admits t –injective corner maps.
Proof For .g; r/ D .0; 4/ or g > 0 and r D 1, it is immediate to construct such a
triangulation. Subdividing a triangle by taking the cone from an interior point preserves
the existence of t –injective corner maps. By induction on r we deduce that for every
.g; r/ ¤ .0; 3/ there exist triangulations of S as in the statement.
In Figure 6 the corner selection is speciﬁed by a , and the rows show all the possible
ﬂip moves on triangulations of S , up to obvious symmetries, that preserve the injectivity
Algebraic & Geometric Topology, Volume 7 (2007)
870
Stephane Baseilhac and Riccardo Benedetti
of corner maps. Consider triangulations T 0, T 00 of S with r vertices, such that T 00
supports a t –injective corner map. It is well known that T 00 is connected to T 0 via a
ﬁnite sequence of ﬂips. The t –injective corner map for T 00 yields a t –injective corner
map for T 0 by decorating these ﬂips as in Figure 6.
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
Figure 6:
The ﬂips with marked corners
There are no obstructions to use arbitrary corner maps in what follows. Specializing
to injective ones just simpliﬁes the exposition. For .g; r/ D .0; 3/, triangulations
have two 2–simplices, one with two selected corners. From now on, we assume that
.g; r/ ¤ .0; 3/, the extension to the .0; 3/ case being straightforward.
Given a pair .g; r/ ¤ .0; 3/ and .T 0; b0/ as in Lemma 3.1, ﬁx a t –injective corner
map v 7! cv. In the interior of each triangle tv consider a bigon Dv with one vertex
at v, and call v0 the other vertex. Remove from tv the interior of Dv, and triangulate
the resulting cell sv D tv n Int.Dv/ by taking the cone with base v0. Repeating this
procedure for each tv, we get a triangulation T of F with 2r vertices and p C 2r
triangles, where p denotes the number of triangles of T 0. The set of edges of T ,
E.T /, contains E.T 0/ in a natural way, and jE.T /j D jE.T 0/j C 4r . We extend b0
to a branching b on T as in Figure 7, and the sign function .T 0;b0/ to the triangles of
.T; b/ in the natural way. Note that the ﬁgure shows only one of the possible branching
conﬁgurations. In general we extend b0 to b so that we can recover .T 0; b0/ from
.T; b/ by “zipping” and “collapsing”, as suggested at the bottom of Figure 7. In what
follows, for simplicity we will refer to this conﬁguration, as the treatment of the others
is similar.
Deﬁnition 3.2
We call a pair .T; b/ constructed as above from a pair .T 0; b0/ an
efﬁcient triangulation (e–triangulation for short) of F . For each vertex v, the preferred
Algebraic & Geometric Topology, Volume 7 (2007)
Quantum hyperbolic geometry
871
v
v
T
zip
v
T 00
v
T 0
Figure 7:
The branched triangulated cell sv
inner triangle at v is the triangle 
v in sv with an edge on @F whose b–orientation
coincides with the boundary orientation of F .
