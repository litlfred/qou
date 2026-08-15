---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-020-61-proof-for-edge-equations
section_title: "Proof for edge equations"
section_number: 6.1
pages: 18-19
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
k simplices ∆ 0,..., ∆k−1 along the common edge 01, pairing all faces via the permutation
(23), see Figure 12.
0
1
2 3
3
2 3 2 3
3
3
0
21
Figure 12. Local model near an
edge point.
Figure 13. Local model near a face
point.
Lemma 6.5. If{c∆i} is a Ptolemy assignment on K, the assignments{µ(c∆i)} satisfy the
edge equations for all integral points on the edge 01. The same holds for the complex K′
obtained by reordering the vertices of the simplices of K.
Proof. An integral point p on 01 has representatives (t, ∆i) with t = (t0,t 1, 0, 0) being ﬁxed.
The left hand side of the edge equation for p is given by
(6.5) z1100
s,0 z1100
s,1 ··· z1100
s,k−1 with s = (t0− 1,t 1− 1, 0, 0),
which expands to
cs+1001,0cs+0110,0
cs+1010,0cs+0101,0
cs+1001,1cs+0110,1
cs+1010,1cs+0101,1
··· cs+1001,k−1cs+0110,k−1
cs+1010,k−1cs+0101,k−1
.
Since the Ptolemy coordinates c1001,i = c1010,i+1 and c0101,i = c0110,i+1 on two adjacent sim-
plices are identiﬁed, all terms cancel. Hence, (6.5) equals 1 as desired. The corresponding
result for K′ follows from compatibility under reordering (Lemmas 6.2, 4.12 and 5.10). □
Corollary 6.6. Theorem 6.3 holds for the edge equations.
Proof. The complex K models a neighborhood around an edge e ofT in the sense that
there is a simplical map π : K→ ˆM mapping 01 to e, which is unique up to changing the
orientation of K and cyclically relabeling the simplices. By compatibility under reordering,
we may assume that π is order preserving. A Ptolemy assignment on T pulls back to a
Ptolemy assignment on K, such that edge equations on 01 descend to the corresponding
edge equations on e. The result now follows from Lemma 6.5. □
GLUING EQUATIONS FOR PGL( n, C)-REPRESENTATIONS OF 3-MANIFOLDS 19
