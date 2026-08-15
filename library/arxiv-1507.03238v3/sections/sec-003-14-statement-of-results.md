---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-003-14-statement-of-results
section_title: "Statement of results"
section_number: 1.4
pages: 3-5
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety forSL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
pendent Ptolemy varieties. A summary of their deﬁnition is given in Section 1.5, and explicit
computationsaregiveninSection11. Let M beacompact, orientable 3-manifoldwithnon-empty
boundary, and letT be a topological ideal triangulation ofM.
Any P-decorated boundary-unipotent representationρ: π1(M)→ SL(2, C) assigns Ptolemy
coordinates to the edges ofT (see Section 2). If all Ptolemy coordinates are zero, we say that
the decorated representation istotally degenerate. This notion turns out to be independent of
the (ideal) triangulation and implies that the representation is reducible (see Section 6.2).
Recall that although the set of representations ofπ1(M) is a variety, the set of representations
up to conjugation is not a variety in general. The same holds for decorated representations.
However, if we discard the totally degenerate decorations, we get a variety:
Theorem 1.2.The conjugation action on the set of non totally degenerate decorated boundary-
unipotent representations has a geometric quotient. For each triangulationT ofM, the invariant
Ptolemy varietyP (T ) provides explicit coordinates, i.e. we have an isomorphism of varieties
(1.1) P (T )∼=
{
Not totally degenerate,P-decorated,
boundary-unipotentπ1(M)→ SL(2, C)
}/
Conj.
In particular,P (T ) is independent of the triangulation. Morever,P (T ) embeds inP (T ) as a
Zariski open subset. □
Deﬁnition 1.3.A representation is boundary-nondegenerate if its restriction to π1(∂iM) is
non-trivial for each boundary component∂iM of M.
Theorems 1.4, 1.5 and 1.6 below are elementary corollaries of Theorem 1.2 and its analogues
for the modiﬁed variants. They were previously known for representations admitting ageneric
decoration (see [8, 9, 13]).
Theorem 1.4. The map
(1.2) P (T )red→
{
Boundary-unipotent
π1(M)→ SL(2, C)
}/
Conj
induced from(1.1) by ignoring the decoration has image containing all irreducible representations
and is one-to-one over the set of irreducible boundary-nondegenerate representations. □
Theorem 1.5. Letk =
⏐⏐H 1(M,∂M ; Z/2Z)
⏐⏐. The map
(1.3) P
σ
(T )red→



Boundary-unipotent
π1(M)→ PSL(2, C)
with obstruction classσ



/
Conj
has image containing all irreducible representations and isk : 1 over the set of irreducible,
boundary-nondegenerate representations. □
4 MATTHIAS GOERNER AND CHRISTIAN K. ZICKERT
Theorem 1.6. SupposeM has c boundary components, all of which are tori. There is a map
(1.4) EP (T )red→
{
Boundary-Borel
π1(M)→ SL(2, C)
}/
Conj
with image containing all irreducible representations. It is generically2c : 1 over the irreducible,
boundary-nondegenerate representations. Moreover, the projection to the(ms,ls) coordinates is
the variety of eigenvalues ofµs and λs. □
This can be used to compute theA-polynomial; see Section 11.3 for an example.
Remark 1.7. The image of (1.2), (1.3), and (1.4) may contain reducible representations as
well (see e.g. the example in Section 11.4.1), but such are necessarily boundary-degenerate (see
Proposition 6.7). The preimage over a representation which is not boundary-nondegenerate is
typically (although not always; see Remark 2.15) higher dimensional.
Remark 1.8. One could detect all representations (including all reducible ones) by performing
a single barycentric subdivision [9]. The resulting variety, however, is not a topological invariant
since each non-ideal vertex (generically) increases the dimension by one. The growth in the
number of simplices and the expected dimension also makes computations infeasible. More
importantly, invariants such as the loop invariant [4], important in quantum topology, are only
deﬁned when all vertices are ideal.
Remark 1.9. Our varieties are really schemes overZ. They are typically not irreducible, and
the coordinate rings may have nilpotents.
1.5. Deﬁnition and computation of the reﬁned Ptolemy varieties - an overview.We
consider onlyP (T ) here. The modiﬁed variants are deﬁned and computed in a similar way. As
mentioned earlier, a decorated representation deﬁnes Ptolemy coordinates, and thus gives rise
to a distinguished set of edges, namely those having Ptolemy coordinate zero. The idea is to
consider all possible such sets. It turns out that they have to satisfy a transitivity property.
Deﬁnition 1.10.A transitive edge setis a setE of edges ofT satisfying that if any two edges
of a face are inE, so is the third. The edges in a transitive edge set are calledzero-edges. We
sometimes denoteE by (T,E ) to stress the signiﬁcance of the triangulation.
There are always at least two transitive edge sets: thenon-degenerate edge set with no zero-
edges, and thetotally degenerateedge set where all edges are zero-edges. In Section 7 we deﬁne
for all transitive edge setsE (except the totally degenerate one) a Ptolemy varietyP (T,E ),
parametrizing decorated representations whose Ptolemy coordinates are zero exactly at the edges
in E. The triangulation independent Ptolemy varietyP (T ) is then deﬁned as the union of all
the P (T,E ) (see Deﬁnition 8.1). For the non-degenerate edge setP (T,E ) is simplyP (T ). If
each face has at most one zero-edge (theedge-degenerate case; see Deﬁnition 6.4),P (T,E ) is
deﬁned by the usual Ptolemy relations together with anedge relation(5.1) for each zero-edge.
If one or more faces consists entirely of zero-edges, one can reduce to the edge-degenerate case
by considering an auxilary triangulationT′ obtained fromT by performing an explicit sequence
of 2-3 moves.
1.5.1. Algorithm. We describe an algorithm that is guaranteed to ﬁnd all boundary-unipotent
irreducible representations of a manifold, no matter what triangulationT0 is used as input. The
steps involve triangulations obtained fromT0 by performing 2-3 moves, but these are purely
auxiliary.
A simplex isdegenerate if all six edges are zero. A face isdegenerate if all 3 edges are zero.
TRIANGULATION INDEPENDENT PTOLEMY V ARIETIES 5
Step 0: Compute all transitive edge sets(T0,E 0) ignoring the totally degenerate one.
Step 1: If (T,E ) has a degenerate simplex, replace it by a descendant (Deﬁnition 7.12)
(T′,E′) after performing a 2-3 move at a face adjacent to a non-degenerate and a
degenerate simplex. This procedure reduces the number of degenerate simplices
by one. Repeat until all simplices are non-degenerate.
Step 2: If (T,E ) has a degenerate face, replace it by the set of descendants (T′,E′)
whereT′ is the triangulation obtained fromT by performing a 2-3 move on each
degenerate face. No descendants have degenerate faces.
Step 3: For each(T,E ) from step 2 compute the primary decomposition of the reduced
Ptolemy varietyP (T,E )red.
Step 4: For each zero dimensional component ofP (T,E )red, compute the correspond-
ing boundary-unipotent SL(2, C)-representations via the Bruhat cocycle (Sec-
tion 4.2). The output is a matrix of exact algebraic expressions for each generator
of π1(M) in the face pairing presentation.
Remark 1.11. If a Ptolemy variety contains a higher dimensional componentC, one can com-
pute the tautological representationπ1(M)→ SL(2,F (C)), whereF (C) is the function ﬁeld of
C. See Section 11.4.3 for an example.
Remark 1.12. Among the 61911 manifolds in the SnapPy censusOrientableCuspedCensus
there is no manifold with more than 53 transitive edge sets (average 16). Most of these edge sets
are only edge-degenerate (72%), so steps 1 and 2 above are rarely needed.
Remark 1.13. In case there are only two transitive edge sets it follows immediately from the
deﬁnition thatP (T ) = P (T ), so in this case the standard Ptolemy variety is guaranteed to
detect all boundary-unipotent representations. Unfortunately, the only manifolds in the SnapPy
census OrientableCuspedCensus with only two transitive edge sets are:m003, m004, m015, m016,
m017, m019, m118, m119, m180, m185.
