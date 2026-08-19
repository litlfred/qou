---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-016-6-transitive-edge-sets-and-degeneracy-types
section_title: "Transitive edge sets and degeneracy types"
section_number: 6
pages: 14-15
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety forSL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
Note that a decorationD determines a distinguished subset of the edge set ofT , namely those
whose Ptolemy coordinates are zero. We refer to this subset as thezero-set of D.
TRIANGULATION INDEPENDENT PTOLEMY V ARIETIES 15
d (h k )
d (t k )
d (b k )
c 23 ,k− 1
c 13 ,k− 1
c 01 ,k− 1
c 12 ,k
c 03 ,k
c 02 ,k
c 03 ,k− 1 c 12 ,k = c 13 ,k− 1 t k h k
c 02 ,k = c 03 ,k− 1 b k h k
c 01 ,k = c 01 ,k− 1 t k b k
x(d1)
⇐⇒
N−1∑
k=0
dk
k∏
j=1
t2j= 0
dk = c23,k
c12,kc23,k
x(dN−1)
N−1∏
k=0
x(dk)d(tk+1) =I
x(d0)d(t1)
d(t2)
d(tN+1)
Figure 9. Fattened ver-
sion of Figure 7.
Figure 10. Fattened Bruhat
cocycle (top view).
Deﬁnition 6.1.A transitive edge set is a subsetE of the edges ofT such that if two edges
on a face are inE, so is the third. The set of transitive edge sets is denoted byT(T ). Given
E∈ T(T ), we refer to the edges inE as zero-edges. To stress the dependence onT we sometimes
denote a transitive edge set as(T,E ) instead ofE.
Lemma 6.2. The zero-set of a decoration is transitive.
Proof. If g0P, g1P and g2P are the cosets assigned to the vertices of a face, the Ptolemy coor-
dinates are given bycij = det(vi,vj), wherevi =gi ( 1
0 ). Hence, a Ptolemy coordinatecij is zero
if and only ifvi and vj are linearly dependent. The result now follows from the fact that linear
dependence of vectors is transitive. □
Deﬁnition 6.3.LetE∈ T(T ) be a transitive edge set. A face ofT is degenerate if all its three
edges are zero-edges. A simplex ofT is degenerate if all of its six edges are zero-edges.
Deﬁnition 6.4.We divide the transitive edge sets into the following types:
Non-degenerate: No zero-edges (there is a unique such).
Edge-degenerate: Some zero-edges, but no degenerate faces.
Face-degenerate:Some degenerate faces, but no degenerate simplices.
Simplex-degenerate: Some, but not all, simplices are degenerate.
Totally degenerate:All simplices are degenerate (there is a unique such).
Clearly, anyE∈ T(T ) falls into exactly one of these types.
