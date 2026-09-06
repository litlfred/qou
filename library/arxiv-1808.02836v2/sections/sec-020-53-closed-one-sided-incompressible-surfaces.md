---
doc_id: arxiv-1808.02836v2
doc_title: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds"
section_id: sec-020-53-closed-one-sided-incompressible-surfaces
section_title: "Closed one-sided incompressible surfaces"
section_number: 5.3
pages: 29-32
source_pdf: 1808.02836v2.pdf
source_sha256: 0224a296253122a2
---
In what follows, the weight of a normal surface S in a triangulation T is deﬁned to be the overall number of
intersection points of S with the edges of T .
Lemma 15 Let M be a once-punctured hyperbolic torus bundle and letT be a monodromy ideal triangulation
of M. Furthermore, let S⊂ T be a normal surface of T which is a taut least weight representative of an
even torsion class of H2(M, Z). Then S meets each tetrahedron of T in a single quadrilateral. Moreover,
χ(S) =−(# horizontal quads).
Proof Let S⊂ T be a normal surface of T which is a taut representative of a ﬁxed even torsion class
c∈ H2(M, Z). We assume that S is of least weight amongst all taut representatives. The monodromy ideal
triangulation T naturally endows M with a circular Morse type function: The layering deﬁnes a cyclic ordering
of pairs of faces forming a once-punctured torus ﬁbre. Let T be such a two-triangle ﬁbre.
29
Consider the intersection S∩ T. This is a family of embedded disjoint normal simple closed curves in the two-
triangle structure on T. A well-known elementary fact is that any such curve is either non separating or vertex
linking. Next, note that S∩ T cannot contain two parallel curves, since otherwise we can perform an annular
compression using an innermost ﬁbre 0 weight annulus A and ﬁnd a new homologous normal surface of less
weight or less genus or both.
To be more speciﬁc, consider N(A), where N(A) is a small regular neighbourhood of A. Then S∩ N(A)
contains two annuli and these are replaced by two annuli in ∂N(A) to form a new surface with the same weight
and Euler characteristic as S and representing the same class c. If this surface is disconnected, it is easy to
see one component is one-sided and the other is two-sided, as c is a torsion class. Hence we can discard the
two-sided component (it must bound in M) and the resulting surface still represents c. As this new surface is
not normal, it can be isotoped to a normal surface of less weight, giving a contradiction.
Hence, from now on, we can assume that each ﬁbre meets S in one or two curves. Note that in the latter case
exactly one curve links the ideal vertex in the ﬁbre and the other curve is non separating. Let γ denote the non
separating curve in S∩ T.
The curve γ⊂ T is determined by how often it intersects the three edges ofT. Since γ is connected, these three
intersection numbers are pairwise coprime. This can be seen by the fact that, given two intersection numbers,
the third one must either be the sum or the non-negative difference of the ﬁrst two.
A key observation is thatS propagates across the tetrahedron ∆∈ T layered on top of T in a very well-behaved
way. In what follows, we denote the edge of ∆ opposite T by e, and the new ﬁbre opposite T (i.e., the two
triangles of ∆ containing e) by T′.
Assume that S∩ T contains a vertex linking curve α. α intersects T in six normal arcs (one of each type).
Four of them necessarily yield two normal triangles in ∆ and two normal arcs in T′. For the remaining two
arcs, three cases need to be considered.
1) They are in the boundary of a quadrilateral normal disc in ∆. In this case, the two normal triangles and
the normal quadrilateral containing α intersect both triangles of T′ in two parallel normal arcs. Moreover, all
other normal arcs of S∩T′ must be of the same type (otherwise S self-intersects inside ∆). In particular, S∩T′
has parallel curves, which contradicts our assumption that S is least weight, using the annular compression
argument from above. See Figure 19 on the left.
2) One of them yields a normal triangle t, and the other one is in the boundary of a normal quadrilateral in ∆
together with a normal arc of γ. In this case, S∩ T′, again consists of one type of normal arc per triangle of T′,
with two exceptional normal arcs coming from t. Let one triangle of T′ contain k and the other one contain 𝓁
copies of parallel normal arcs. Hence, one edge of T′ intersects S once, the second one k +1 = 𝓁 times and the
third k times, hence, 𝓁 + 1 = k, a contradiction. See Figure 19 on the right.
3) All of the six normal arcs of α are in the boundaries of normal triangles in ∆. Since 1) and 2) are not
possible, this must be the case for all tetrahedra ofT and S contains a boundary parallel torus. This contradicts
the assumption that S is a least weight taut representative of c.
Hence, for the rest of the proof we can assume thatS∩T is connected for each ﬁbre T. Consequently, it follows
that S∩ T has only one or two normal arc types in each triangle of T, since otherwise S∩ T contains a vertex
linking component.
We claim that ∆ can only contain vertical normal discs of S, unless ∆∩ S consists of a single horizontal quad
and S intersects two edges of T exactly once, and is disjoint from e.
More precisely, there are two cases we have to consider:
30
Figure 19: Left: The normal arcs of α are in two normal triangles and one normal quadrilateral. Right: The
normal arcs of α are in three normal triangles and one normal quadrilateral.
(1) The intersection of S with T is disjoint from one of the edges of T. In this case the other two edges must
intersect S exactly once. If we layer on the edge disjoint from S then there is a single horizontal quadri-
lateral in the tetrahedron, if we layer on one of the other edges, there is a single vertical quadrilateral.
See Figure 20 on the right.
(2) The surface S intersects T in two normal arc types per triangle. In this case all normal discs of S in ∆
must necessarily be vertical. To see this note that a horizontal normal quadrilateral can only have two
normal arcs of S∩ T in its boundary. Since by the assumption, at least one other normal disc must exist
in ∆, this must be a vertical normal triangle. Arguing as in case 1) and 2) above we can then follow that
all three normal arc types must be present per triangle, a contradiction. See Figure 20 on the left.
It is now easy to verify that the Euler characteristic ofS is the negative of the number of horizontal quadrilateral
discs, using the circular Morse type function induced by the layering. For each horizontal quadrilateral disc
induces a simple saddle type singularity of Morse index one, whereas there are no critical points on vertical
triangles or quadrilaterals.
Figure 20: Left: S∩ T has two normal arc types per triangle of T. Right: S∩ T is disjoint from one edge of
T.
Since S is taut, no component can be a torus or Klein bottle. Hence there must be at least one horizontal
31
quadrilateral. We can cut M open along a corresponding ﬁbre T to form a product of the form T× I where T
is a once punctured torus. This product admits an induced ideal triangulation which is minimal layered.
There are two steps to complete the proof. The ﬁrst is to follow the argument in [30, Theorem 12] which shows
that there is a unique isotopy class of incompressible surfaces in a lens space with even fundamental group. We
want to apply a similar argument to an incompressible surface S∗ in a product of a once punctured torus and an
interval.
Consider a product X = T× I where T is a once punctured torus and there are two essential boundary curves
C,C′ in T×{0},T×{1} respectively and the intersection number of C,C′ is even when projected to a copy of
T. We claim there is a unique incompressible surface S∗ up to isotopy with ∂S∗ = C∪C′.
Pick an annulus A in the product structure of X with boundary curve on T×{1} parallel to C′. We can assume
without loss of generality that A is transverse to S∗ and the intersection A∩ S∗ contains only arcs which are
essential on S∗ and have both ends on T×{ 0}. An innermost such an arc on A cuts off a bigon which can be
used to perform a boundary compression of S∗ across T×{ 0}. Exactly as in [30], this boundary compression
must change the boundary curve C of ∂S∗ to a new curve which has smaller intersection number with C′. It
is now easy to show as in [30] that this process produces a unique family of bands attached to a collar about C
forming S∗ which is therefore unique up to isotopy.
The second step is to observe that the canonical quadrilateral surface in the induced ideal layered triangulation
of the product is incompressible. The proof again follows [30]. The key idea is to use induction and the
recursion formula for the genus of the incompressible surface. By removing the tetrahedra up to the ﬁrst
containing a horizontal quadrilateral, we obtain a new product with an induced minimal layered triangulation.
The recursion formula for the change in boundary slope and the genus matches the formula in [30] and this
shows that the canonical quadrilateral surface must be incompressible as it is a minimal genus cobordism
surface connecting C and C′. This completes the proof.
Corollary 16 Let M be a once-punctured hyperbolic torus bundle and let T be a monodromy ideal triangu-
lation of M. Suppose that H2(M, Z) contains a Klein 4-group H. Then
|T| = ∑
0⁄=c∈H
|| c||,
and in particular T is a minimal triangulation.
Proof For each of the three non-trivial classes in H we have least weight taut normal representatives. We
know from the ﬁrst part of Lemma 15 that each of them meets each tetrahedron of T in exactly one normal
quadrilateral. Moreover, since H is a Klein 4-group, the sum of all three representatives must have edge weight
zero mod two. It follows that every tetrahedron contains all three quadrilateral types exactly once. In particular,
in each tetrahedron exactly one of the three representatives has a single horizontal normal quadrilateral.
Hence, by the second part of Lemma 15 the negative of the sum of Euler characteristics of these three repre-
sentatives must equal the number of tetrahedra of T . It now follows from Theorem 1 that T is minimal.
Combining Corollary 16 with the covering argument provided in§5.2 proves Theorem 2.
