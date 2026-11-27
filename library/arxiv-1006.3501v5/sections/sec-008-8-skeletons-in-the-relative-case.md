---
doc_id: arxiv-1006.3501v5
doc_title: "On two approaches to 3-dimensional TQFTs"
section_id: sec-008-8-skeletons-in-the-relative-case
section_title: "Skeletons in the relative case"
section_number: 8
pages: 22-26
source_pdf: 1006.3501v5.pdf
source_sha256: e939aec50387ce2d
toc_source: outline
doc_brief: "On two approaches to 3-dimensional TQFTs — W e prove that|M |C = τZ(C)(M ) for any closed oriented 3-manifold M and for any spherical fusion category C of non-zero dimension."
---
We study skeletons of 3-manifolds with boundary and their transfo rmations.
8.1. Skeletons of pairs. LetM be a compact 3-manifold (with boundary). Let G
be an oriented graph in ∂M such that all vertices of G have valence≥ 2. (A graph
is oriented, if all its edges are oriented.) A skeleton of the pair (M,G ) is an oriented
stratiﬁed 2-polyhedron P⊂M such that
(i) P∩∂M =∂P =G;
(ii) every vertex v of G is an endpoint of a unique edge dv of P not contained
in ∂M ; moreover, dv∩∂M ={v} and dv is not a loop;
(iii) every edge a of G is an edge of P of valence 1; the only region Da of P
adjacent to a is a closed 2-disk, Da∩∂M =a, and the orientation of Da is
compatible with that of a (see Section 5.2 for compatibility of orientations);
(iv) M\P is a disjoint union of a ﬁnite collection of open 3-balls and a 3-
manifold homeomorphic to ( ∂M\G)× [0, 1) through a homeomorphism
extending the identity map
(12) ∂(M\P ) = ∂M\G = (∂M\G)×{ 0}.
Conditions (i)–(iii) imply that in a neighborhood of ∂M , a skeleton of (M,G ) is a
copy of G× [0, 1]. The primary moves T ±1
1 −T ±1
4 on skeletons of closed 3-manifolds
extend to skeletons P of (M,G ) in the obvious way. These moves (and all other
moves on skeletons considered below) keep ∂P =G and preserve the skeletons in a
neighborhood of their boundary G. In particular, the move T1 adds an edge with
both endpoints in Int( M ), the move T2 collapses an edge contained in Int( M ), etc.
Ambient isotopies of skeletons in M keeping the boundary pointwise are also viewed
as primary moves.
Lemma 8.1. Every pair (a compact orientable 3-manifold M , an oriented graph G
in ∂M such that all vertices of G have valence ≥ 2) has a skeleton. Any two
skeletons of (M,G ) can be related by primary moves in M .
We prove this lemma in Section 8.3 using the results of Section 8.2 and th e theory
of special skeletons which we brieﬂy outline. Suppose that the grap h G⊂ ∂M is
trivalent, i.e., all its vertices have valency 3 (possibly, G =∅). A skeleton P of
(M,G ) is special or an s-skeleton if all regions of P are 2-disks, all edges of P are
trivalent, all vertices of P are incident to 4 half-edges, and every point of P\G has
a neighborhood in P homeomorphic to an open subset of the set (10). As in the
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 23
proof of Lemma 7.2, we can transform any skeleton P of (M,G ) into a s-skeleton
by primary moves applied away from ∂P =G. By [TV], Corollary 6.4.C, any two
s-skeletons of ( M,G ) can be related by MP-moves and lune moves applied away
from G. The MP-moves on s-skeletons of ( M,G ) are deﬁned as in Section 7.4
and the lune moves L±1 are shown in Figure 7. These moves on s-skeletons are
allowed here only when they produce s-skeletons (this is always the c ase for the
MP-moves and L) and preserve the orientation of the regions. In particular, the
moveL−1 is allowed only when the orientations of two regions united by this move
are compatible and the union of these regions is a 2-disk. The orienta tion of the
small disk regions destroyed or created by the MP-moves and L±1 may be arbitrary.
Note that Corollary 6.4.C of [TV] does not handle orientations of the s keletons
but remains true in the oriented setting: the indeterminacy in the ch oice of the
orientation of the regions can be resolved as in Section 7.4.
Figure 7. The lune moves L±1
8.2. Skeletons and frames. Fix a compact 3-manifold M . We assume that M is
oriented and endow ∂M with the induced orientation.
A skeleton of M is a skeleton of the pair ( M,∅) in the sense of Section 8.1.
(For closed M , this notion is the same as in Section 6.2.) A skeleton Q of M is
a frame if there is an embedding i : ∂M× [0, 1]→M extending the identiﬁcation
∂M×{ 0} =∂M such that
Q∩i(∂M× [0, 1]) = i(∂M×{ 1}),
and the orientation of the regions of Q contained in i(∂M×{ 1}) is induced by
that of ∂M via i. Such an embedding i is called a Q-collar. By the deﬁnition of a
skeleton, all components of M\ (Q∪i(∂M× [0, 1])) are open 3-balls.
Not all skeletons of M are frames. We illustrate this claim with an example.
Consider an unknotted torus T = S1×S1 in a closed 3-ball B and add to T two
disks in B lying on diﬀerent sides of T and bounded by the loops S1×{s} and
{s}× S1, where s∈ S1. For any orientation of the regions, the resulting oriented
2-polyhedron is a skeleton of B but not a frame.
For a skeleton Q⊂ Int(M ) of M , denote by ˆQ the union of Q with all open ball
components of M\Q. The skeleton Q is a frame if and only if ˆQ is a 3-manifold
with boundary and the orientation of all regions of Q contained in ∂ˆQ is induced by
the orientation of M restricted to ˆQ. The surface Q+ =∂ˆQ⊂Q is homeomorphic
to ∂M and equal to i(∂M×{ 1}) for any Q-collar i. A local analysis shows that
any edge of Q meeting Q+ either lies in Q+ or meets Q+ in one or two endpoints.
Every vertex of Q lying in Q+ is incident to at least one edge of Q lying in Q+.
Therefore the set Q+∩Q(1) is a graph whose edges and vertices are the edges and
vertices of Q lying in Q+. (Recall that Q(1) is the union of edges of Q.)
By primary moves on a frame Q ofM , we mean the primary moves on skeletons
T ±1
1 −T ±1
4 applied inside M at vertices of Q not lying in Q+ or at edges of Q
24 V. TURAEV AND A. VIRELIZIER
disjoint from Q+. Such vertices and edges are surrounded by the ball components
of M\Q. Therefore these moves do not modify ˆQ and produce frames of M .
By generalized MP-moves on frames, brieﬂy GMP-moves, we mean the moves
{T m,n}m,n, (T ′′
4 )±1 introduced in Section 7.2 and the lune moves L±1 shown in
Figure 7. These moves are allowed in this context only when they prod uce frames
and preserve the orientation of the regions. In particular, the mo veL−1 is allowed
only when the orientations of two regions united by this move are com patible. The
orientation of the small disk regions destroyed or created by the m oves may be
arbitrary.
As we know, all GMP-moves on frames except possibly the lune moves expand
as compositions of primary moves on skeletons though the intermed iate skeletons
may not be frames. The lune moves also expand as compositions of pr imary moves
on skeletons; we leave it to the reader as an exercise.
Lemma 8.2. The manifold M has a frame. Any two frames of M can be related
by a ﬁnite sequence of primary moves and GMP-moves in the clas s of frames.
Proof. Fix a triangulation t of M and denote ∂t the induced triangulation of ∂M .
The triangulation t gives rise to a dual cellular decomposition t∗ ofM . It is formed
by the cells of the cellular decomposition ( ∂t)∗ of∂M dual to ∂t and the cells dual
to the simplices of t inM . The 2-skeleton Qt = (t∗)(2)⊂M oft∗ is a 2-polyhedron
containing ∂M , and M\Qt is the disjoint union of the open 3-cells of t∗. The
edges of t∗ form a stratiﬁcation of Qt. We endow all regions of Qt lying in ∂M with
the orientation induced by that of ∂M . All other regions of Qt are oriented in an
arbitrary way. Pushing Qt inside M we obtain a frame of M .
The construction of Qt can be generalized as follows. Let F be the (trivalent)
graph in ∂M formed by the vertices and edges of ( ∂t)∗. Any skeleton P of the pair
(M,F ) determines a 2-polyhedron Q =Q(P ) = P∪∂M . The edges of P⊂Q form
a stratiﬁcation of Q. We endow all regions of Q lying in ∂M with the orientation
induced by that of ∂M . The other regions of Q inherit their orientation from P .
Pushing Q inside M we obtain a frame of M . The frames of M obtained in this
way from skeletons of ( M,F ) are called t-frames.
The discussion at the end of Section 8.1 shows that any two skeleton s of (M,F )
can be related by primary moves in the class of skeletons of ( M,F ). Extending
these moves to the associated t-frames in the obvious way, we obtain that any two
t-frames of M can be related by primary moves in the class of t-frames.
We show now that any frame Q of M can be transformed into a t-frame by
GMP-moves. Pick a Q-collar i : ∂M× [0, 1]֒→M . Let V and E be the sets of
vertices and edges of the graph F respectively. Deforming i, we can ensure that the
graphFi =i(F×{ 1})⊂Q+ is generic in the sense that its vertices {i(v×{ 1})}v∈V
lie in Q+\Q(1) and its edges {i(a×{ 1})}a∈E are transversal to the edges of the
graph Q+∩Q(1). Set
R =Q∪i(F× [ 1
2, 1])∪i(∂M×{ 1
2}).
We stratify the 2-polyhedron R⊂ Int(M ) as follows. The points of Fi∩Q(1) split
the edges of the graphs Fi andQ+∩Q(1) into smaller subedges. For edges of R we
take all these subedges together with the edges of Q not lying in Q+ and the arcs
{i(v× [ 1
2, 1])}v∈V and{i(a×{ 1
2})}a∈E. Then the vertices of R are the vertices of Q
and the points of the sets Fi∩Q(1) and{i(v×{ 1
2, 1})}v∈V . Clearly,
R(1) =Q(1)∪i(V× [ 1
2, 1])∪i(F×{ 1
2, 1}).
We orientR as follows: the regions contained in Q inherit their orientation from Q,
the orientation of the regions contained in i(∂M×{ 1
2}) is induced by that of ∂M ,
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 25
the regions {i(a× [ 1
2, 1])}a∈E are oriented in an arbitrary way. It is clear that R
is a t-frame of M . Each region r of R contained in R+ =i(∂M×{ 1
2}) is a 2-disk
whose boundary can be pushed towards Q+ and further contracted into a small
circle by GMP-moves in the class of frames. At the end, this “moving” disk can be
eliminated via the inverse bubble move. Note that the orientation of t he regions ofR
yield no obstructions to these moves because all regions of R contained in Q+ are
oriented coherently. In this way, eliminating consecutively all region s ofR contained
inR+, we can transform R intoQ by GMP-moves. The inverse sequence of moves
transformsQ into the t-frameR. Now, the properties of t-frames established above
imply the claim of the lemma. □
8.3. Proof of Lemma 8.1. It is enough to consider the case where M is connected.
The case ∂M =∅ having been treated above, we assume that ∂M ⁄=∅. Fix an
orientation ofM . Denote by V andE the sets of vertices and edges of G respectively.
In analogy with the construction of the polyhedron R at the end of the proof
of Lemma 8.2, we construct a skeleton of ( M,G ) from any frame Q⊂ M . Pick a
Q-collari : ∂M× [0, 1]֒→M such that the graph Gi =i(G×{ 1})⊂Q+ is generic,
i.e., its vertices {i(v×{ 1})}v∈V lie in Q+\Q(1) and its edges {i(a×{ 1})}a∈E are
transversal to the edges of the graph Q+∩Q(1). Set
P =P (Q,i ) = Q∪i(G× [0, 1]).
We stratify the 2-polyhedron P as follows. The points of Gi∩Q(1) split the edges
of Gi and the edges of Q+∩Q(1) into smaller subedges. In the role of edges of P
we take all these subedges together with the edges of Q not lying in Q+ and the
arcs{i(v× [0, 1])}v∈V and{i(a×{ 0})}a∈E. The vertices of P are the vertices of Q
and the points of the sets Gi∩Q(1) and{i(v×{ 0, 1})}v∈V . Clearly,
P (1) =Q(1)∪i(V× [0, 1])∪G∪Gi.
We orientP as follows: the regions contained in Q inherit their orientation from Q;
the orientation of the regions {i(a× [0, 1])}a∈E is induced by that of G. Since all
vertices of G have valency≥ 2, we have ∂P =G. Clearly, P is a skeleton of (M,G ).
A diﬀerent choice of the Q-collari may lead to a diﬀerent skeleton. However, any
two Q-collars are isotopic in the class of Q-collars. Making an isotopy {is}s∈[0,1]
between them transversal to Q+∩Q(1), we can ensure that for all but a ﬁnite set
of values of s, the graph Gis =is(G×{ 1})⊂Q+ is generic, and when s increases
through each of the exceptional values, the skeleton P (Q,i s) is modiﬁed via T m,n
orL±1. The orientation of the regions do not create obstructions to the se moves
because all regions of P (Q,i s) contained inQ+ are oriented coherently. We conclude
that up to GMP-moves, the skeleton P (Q,i ) does not depend on the choice of i.
Consider two frames Q and Q′ of M . If Q′ is obtained from Q by a primary
move, thenˆQ′ = ˆQ and anyQ-collari is also a Q′-collar. Then the skeleton P (Q′,i )
is obtained from P (Q,i ) by the same primary move. Suppose that Q′ is obtained
fromQ by a GMP-moveT . This move proceeds inside a small neighborhood U⊂Q
of an embedded arc in Q. Deforming a Q-collar i in the class of Q-collars, we can
ensure that Gi∩U =∅. Then an appropriate deformation of i yields a Q′-collar i′
such that Gi = Gi′ . Clearly, the skeleton P (Q′,i ′) is obtained from P (Q,i ) by
the same move T . Since T expands as a product of primary moves, the skeletons
P (Q,i ) and P (Q′,i ′) are related by primary moves. By Lemma 8.2, the skeletons
of (M,G ) associated with any two frames of M are related by primary moves.
To complete the proof, it is enough to show that any skeleton P of (M,G ) can
be transformed by primary moves in a skeleton of ( M,G ) associated with a frame.
Recall the edges {dv}v∈V and the regions {Da}a∈E of P from the deﬁnition of a
skeleton. The transformation of P proceeds in three steps. At Step 1 we blow
26 V. TURAEV AND A. VIRELIZIER
up all vertices of P lying in Int(M ) (including the standard vertices) as at Step 5
of the proof of Lemma 7.2. It is explained there that this blowing up ca n be
achieved by primary moves. We need to tune up a little this procedure : the regions
of the resulting skeleton, P1, lying on the small 2-spheres created by blowing up
are endowed with orientation induced by that of M restricted to the small 3-balls
bounded by these spheres (the orientation of all other regions of P1 is induced by
that of P ). The skeleton P1 has edges of two types: the “short” edges lying on
the small spheres (in the proof of Lemma 7.2, these are the edges o f Γ x lying in
∂Bx) and the “long” edges obtained by shortening the original edges of P at their
endpoints. In particular, the edges {dv}v∈V of P give rise to long edges {d′
v}v∈V
of P1. The long edges of P1 are pairwise disjoint. A long edge e distinct from
{d′
v}v∈V has an open ball neighborhood Ue inM that can be identiﬁed with R3 so
that
P1∩Ue = (R2×{ 0, 1})∪ (Yn× [0, 1]),
wheren≥ 2 is the valence of e,Yn⊂ R2 is a union of n rays with common origin O,
and e =O× [0, 1]. Let D⊂ R2 be a 2-disk centered at O and meeting Yn along n
radii. We modify P1 by adding the cylinder ∂D× [0, 1]⊂ Ue surrounding e. The
orientation of the regions lying on this cylinder is induced by that of M restricted
to D× [0, 1]⊂ Ue while the orientation of all other regions is induced from that
of P1. This modiﬁcation can be achieved by MP-moves and hence by primary
moves. We apply these modiﬁcations in disjoint neighborhoods of all lo ng edges
of P1 distinct from {d′
v}v∈V . The resulting skeleton, P2, has regions of two types:
the “small” or “narrow” regions created by the previous transfor mations at the
vertices and edges and the “wide” regions obtained by cutting the o riginal regions
of P2 near their boundary. In particular, the regions {Da}a∈E of P give rise to
slightly smaller regions {D′
a}a∈E of P2. The wide regions of P2 (as well as their
closures) are pairwise disjoint. All regions of P2 except{D′
a}a∈E lie in Int(M ). For
a wide region r of P2 lying in Int(M ), we can use MP-moves to add to P2 a new
region r′ parallel to r, cf. the end of the proof of Lemma 7.4. This can be done so
that the orientations of r and r′ are induced by that of M restricted to the solid
cylinder r× [0, 1] between r and r′. These modiﬁcations are applied to all wide
regions of P2 except{D′
a}a∈E inside their disjoint neighborhoods in M . This gives
a skeleton, P3, of ( M,G ). We claim that P3 is associated with a frame of M . To
see this, consider the 2-polyhedron Q⊂P3∩ Int(M ) obtained from P3 by removing
the graph G = ∂P =∂P3, the interiors of the edges {d′
v}v∈V , and the interiors of
the regions{D′
a}a∈E. The 2-polyhedron Q can be stratiﬁed so that the graphs Q(1)
andQ∩∪ aD′a have only double transversal crossings and the union of these gra phs
is equal to Q∩P (1)
3 . All regions of Q are regions (or unions of regions) of P3 and
inherit orientation from P3. This turns Q into an oriented stratiﬁed 2-polyhedron.
Since P3 is a skeleton of ( M,G ), the polyhedron Q is a skeleton of M . We claim
that Q is a frame. Indeed, the set ˆQ⊂M is the union of a regular neighborhood
of P in M with all 3-ball components of M\P . This union is a 3-manifold with
boundary, and the orientation of all regions of Q contained in ∂ˆQ is induced by the
orientation of M restricted to ˆQ. Now, it is easy to see from the deﬁnitions that
there is a Q-collar i : ∂M× [0, 1]֒→M such that i({v}× [0, 1]) = d′
v for all v∈V
and i(a× [0, 1]) = D′
a for all a∈ E. Then P = P (Q,i ) is the skeleton associated
with Q.
