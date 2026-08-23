---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-021-74-simplex-degenerate-edge-sets
section_title: "Simplex-degenerate edge sets"
section_number: 7.4
pages: 19-20
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety forSL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
d(E) denote the number of degenerate simplices.
Lemma 7.16.LetE∈ T(T ) be simplex-degenerate and letT′ be a triangulation obtained from
T be performing a 2-3 move at a face between a degenerate and a non-degenerate simplex. Then
E has a unique descendantE′∈ T(T ). Furthermored(E′) =d(E)− 1.
Proof. Transitivity holds if and only if the new edge is non-zero. Hence, none of the new simplices
are degenerate (see Figure 14). This proves the result. □
Corollary 7.17.LetE∈ T(T ) be simplex-degenerate. There exists a triangulationT′ obtained
fromT by performing 2-3 moves such thatE has a unique descendantE′∈ T(T′), which is face-
degenerate.
Proof. Repeatedly perform 2-3 moves at a face between a degenerate and a non-degenerate
simplex until there are no more degenerate simplices. □
Deﬁnition 7.18.LetE∈ T(T ) be simplex-degenerate and letE′ andT′ be as in Corollary 7.17.
Deﬁne
(7.8) P (T,E ) =P (T′,E′)
and deﬁnePσ(T,E ) andEP (T,E ) similarly.
Note that as a subset ofA(V (M)) the deﬁnition is independent of the choice ofT′.
Theorem 7.19. The one-to-one correspondences(7.2), (7.3), and (7.4) hold for all transitive
edges setsE that are not totally degenerate.
Proof. This follows from Theorem 7.15 and Corollary 7.17. □
20 MATTHIAS GOERNER AND CHRISTIAN K. ZICKERT
8. The inv ariant Ptolemy v arieties
For the non-degenerate edge setE, deﬁneP (T,E ) to be the standard Ptolemy variety (Def-
inition 2.3). The Ptolemy variety for the other types were deﬁned in Deﬁnitions 7.3, 7.14, and
7.18. We denote the totally degenerate edge set where all edges are zero-edges by0∈ T(T ).
Deﬁnition 8.1.The invariant Ptolemy varietyP (T ) is deﬁned by
(8.1) P (T ) =
⋃
E∈T(T )\{0}
P (T,E ),
where the (disjoint) union is taken insideA(V (M)). We similarly deﬁneP
σ
(T ) andEP (T ).
