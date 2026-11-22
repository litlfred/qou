---
doc_id: bsmf-2002-130-3-457-0
doc_title: "Hyperideal polyhedra in hyperbolic 3-space"
section_id: sec-007-6-realizing-large-angles
section_title: "Realizing large angles"
section_number: 6
pages: 32-34
source_pdf: BSMF_2002__130_3_457_0.pdf
source_sha256: 63f79235d0c13ba8
toc_source: inferred
doc_brief: "Hyperideal polyhedra in hyperbolic 3-space — — A hyperideal polyhedron is a non-compact polyhedron in the hyperbolic 3-space 3 which, in the projective model for 3 ⊂ 3, is just the intersection of 3"
---
To realize hyperideal polyhedra with large external dihedral angles, namely
with small internal dihedral angles, we will rely on Andreev’s classiﬁcation of
compact hyperbolic polyhedra with acute internal dihedral angles [2]. We ﬁrst
state this classiﬁcation with our current terminology.
Recall that the complete graph Kn is the graph with n vertices where any
pair of distinct vertices are joined by one edge. Let K−
n be obtained from Kn
by removing one arbitrary edge.
Theorem 25 (see [2]). — Let Γ be a planar 3-connected graph, diﬀerent from
the graphs K4 and K−
5 . Let a weight θe ∈[ 1
2π, π[ be attached to each edge e of Γ.
There exists a compact polyhedron P in H3 with dual graph isomorphic to Γ
and with external dihedral angle θe at the edge corresponding to the edge e of Γ
if and only if the following three conditions are satisﬁed:
1) every component of S2 −Γ contains exactly three edges e1, e2 and e3 of
Γ, and !3
i=1 θei < 2π;
2) for every simple closed curve γ embedded in Γ and passing through ex-
actly three edges e1, e2 and e3, !3
i=1 θei > 2π unless γ is the boundary of a
component of S2 −Γ;
3) for every simple closed curve γ embedded in Γ and passing through exactly
four edges e1, e2, e3 and e4, !4
i=1 θei > 2π unless γ bounds in S2 a diamond
made up of two components of S2 −Γ and of one edge of Γ separating them.
In addition, if P exists, it is unique up to isometry of H3.
Andreev also provides a similar result for the graph K−
5 , for which there is an
additional condition. Note that K−
5 is the dual graph of a prism with triangular
basis. The case of the graph K4, which is the dual graph of a tetrahedron, is
treated in [17]. However, we will not need to consider these two graphs.
Consider a strictly hyperideal polyhedron P0 ∈PΓ, and its associated trun-
cated polyhedron P Trun
0
. The dual graph ΓTrun of P Trun
0
is obtained from Γ as
follows: For each component A of S2 −Γ, add to Γ a vertex vA and join by an
edge this new vertex vA to each vertex of Γ located in the boundary of A. In
particular, ΓTrun can be described purely in terms of Γ. Also, note that each
edge of ΓTrun −Γ corresponds to an edge of P Trun
0
where the external dihedral
angle is equal to 1
2π.
tome 130 – 2002 – no 3
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE
489
Proposition 26. — Let Γ be a planar 3-connected graph with at least 4 ver-
tices, and with a weight θe ∈] 2
3π, π[ attached to each edge e of Γ. Then there
exists a strictly hyperideal polyhedron P in H3 with dual graph isomorphic to Γ
and with external dihedral angle θe at the edge corresponding to the edge e of Γ.
In addition, P is unique up to isometry of H3.
Proof. — Let ΓTrun be the graph associated to Γ as above. Let us associate to
each edge e of ΓTrun the weight θe ∈[ 2
3π, π[ of the data of Proposition 26 if e
is in Γ ⊂ΓTrun, and the weight θe = 1
2π otherwise. We ﬁrst show that ΓTrun
with these edge weights satisfy the conditions of Theorem 25.
By construction, ΓTrun is planar. One easily checks that it is 3-connected.
Also, Γ has at least 4 vertices and S2 −Γ has at least 4 components, by 3-
connectedness. It follows that ΓTrun has at least 8 vertices, and in particular is
neither K4 nor K−
5 .
Every component of S2 −ΓTrun is a triangle bounded by two edges e1 and e2
of ΓTrun −Γ and one edge e3 of Γ. Then θe1 = θe2 = 1
2π and θe3 < π, so that
!3
i=1 θei < 2π. As a consequence, Condition 1 of Theorem 25 is satisﬁed.
Let γ be a simple closed curve embedded in ΓTrun which crosses exactly
three edges e1, e2 and e3. If at least one vertex of γ is in ΓTrun −Γ, it easily
follows from the 3-connectedness of Γ that γ is the boundary of a component
of S2 −ΓTrun. Otherwise, each ei is also an edge of Γ because the edges of
ΓTrun −Γ all join a vertex of Γ to a vertex of ΓTrun −Γ. It follows that each θei
is greater than 2
3π, and therefore that !3
i=1 θei > 2π. Therefore, Condition 2
of Theorem 25 is satisﬁed.
Finally, let γ be a simple closed curve embedded in ΓTrun which crosses
exactly four edges e1, e2, e3 and e4. It can contain at most two vertices of
ΓTrun−Γ, since no two vertices of ΓTrun−Γ are adjacent in ΓTrun. If γ contains
two vertices of ΓTrun −Γ, it again follows from the 3-connectedness of Γ that
γ bounds a diamond made up of the union of two components of S2 −ΓTrun
and of one edge of Γ. If γ contains exactly one vertex of ΓTrun −Γ, say the
vertex separating e1 from e2, then e1 and e2 are both in ΓTrun −Γ and e3 and
e4 are edges of Γ, so that θe1 = θe2 = 1
2π, θe3 > 2
3π and θe4 > 2
3π; it follows
that !4
i=1 θei > 7
3π > 2π. Finally, if no vertex of γ is in ΓTrun −Γ, then each
ei is in Γ, so that θei > 2
3π; consequently !4
i=1 θei > 8
3π > 2π in this case. It
follows that Condition 3 of Theorem 25 is satisﬁed.
By Theorem 25, there consequently exists a compact polyhedron P ′ in H3
whose dual graph is isomorphic to ΓTrun and with external dihedral angle θe
at the edge corresponding to the edge e of ΓTrun.
The faces of P ′ correspond to vertices of ΓTrun, and therefore are of two types:
those which correspond to vertices of Γ, and those which correspond to vertices
of ΓTrun −Γ. Let f1, f2, . . . , fn be the faces of P ′ that correspond to vertices
of Γ, and let Πi ⊂RP3 be the projective plane containing fi. Let P Proj be the
closure of the component of RP3 −,n
i=1 Πi that contains the interior of P ′.
BULLETIN DE LA SOCI´ET´E MATH´EMATIQUE DE FRANCE
490
BAO (X.) & BONAHON (F.)
At this point, we know that the dual graph of the cell decomposition of
∂P Proj contains Γ and has no additional vertex. If f is a face of P ′ which
corresponds to a vertex of ΓTrun −Γ, namely to a component of S2 −Γ, and
if fi1, fi2, . . . , fik are the faces of P ′ adjacent to f, the fact that the fij are
orthogonal to f implies that the projective planes Πij all pass through the point
Π⊥∈RP3 −H3 ∪∂∞H3 dual to the projective plane Π containing f. It follows
that the dual graph of ∂P Proj has no additional edges, and is equal to Γ.
Incidentally, this shows that P Proj is really a convex polyhedron in RP3,
namely satisﬁes the additional condition that it contains no projective line.
Otherwise, it would be projectively equivalent to the closure of an inﬁnite
prism in R3 ⊂RP3 and its dual graph Γ would be homeomorphic to a circle,
which is excluded by 3-connectedness.
This also shows that the hyperbolic polyhedron P = P Proj ∩H3 is strictly
hyperideal. By construction of P ′, the external dihedral angle of P along the
edge corresponding to the edge e of Γ is equal to θe.
Conversely, the uniqueness of P follows from the uniqueness of P ′ provided
by Theorem 25.
