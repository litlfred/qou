---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-032-appendix-a-symplectic-properties-of-a-and-b
section_title: "Appendix A. Symplectic properties of A and B"
section_number: null
pages: 37-39
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
The N×N Neumann-Zagier matrices A and B form the top half of a symplectic ma-
trix ( A B
C D )∈ Sp(2N, Q) [ NZ85]. In this section we discuss some elementary properties of
symplectic matrices.
38 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
Lemma A.1. The N× 2N matrix ( A B ) is the upper half of a symplectic matrix if and
only if ABT is symmetric and ( A B) has maximal rank N.
Proof. It is easy to see that the rows of ( A B) have zero symplectic product (with respect to
the standard symplectic form on Q2N if and only if ABT is symmetric. In addition they span
a vector space of rank N if and only if ( A B) has maximal rank N. The result follows. □
Lemma A.2. If ( A B ) is the upper half of a symplectic matrix and B is non-degenerate,
then B−1A is symmetric.
Proof. Lemma
A.1 implies that ABT is symmetric, and so is ( B)−1ABT ((B)−1)T . □
It is not true in general that B is invertible. However, after a possible change of quad
type, we can assume that B is invertible. This is the content of the next lemma.
Lemma A.3. (a) Suppose ( A B ) is the upper half of a symplectic 2 N× 2N matrix. If A
has rank r, then any r linearly independent columns of A and their complementary N−r
columns in B form a basis for the column space of ( A B).
(b) There always exists a choice of quad type for which B is non-degenerate (for any ﬁxed
choice of redundant edge and meridian path).
Proof. For (a) let rank( A) = r≤ N. Without loss of generality, we may suppose that the
ﬁrst r columns of A are linearly independent. We want to show that, together with the la st
N−r columns of B, they form a matrix of rank N.
If we simultaneously multiply both A and B on the left by any nonsingular matrix U∈
GL(N, R), both the symplectic condition and the columns are preserved. Th is follows from
the fact that
(U 0
0 U −1,T
)
∈ Sp(2N, R). By allowing such a transformation, we may assume
that A takes the block form
(A.1) A =
(
Ir×r A2
0 0
)
for some A2. Similarly, we split B into blocks of size r and N−r,
(A.2) B =
(
B1 B2
B3 B4
)
.
Since (A B) has full (row) rank, we see that the bottom N−r rows of B must be linearly
independent, i.e. rank(B3 B4) = N−r. From the symplectic condition of Lemma
A.1, we
also ﬁnd that B3 +B4AT
2 = 0, so that rank( B3 B4)≤ rank(B4). This then implies that B4
itself must have maximal rank N−r. Therefore, the last N−r columns of B are linearly
independent, and also independent of the ﬁrst N columns of A; i.e. the matrix
(Ir×r B2
0 B4
)
has
maximal rank as desired. This concludes the proof of part (a).
For part (b) let us denote the columns of A and B as ai and bi. A change of quad type
corresponding to a cyclic permutation Zi↦→Z ′
i↦→Z ′′
i ↦→Zi on the ith tetrahedron permutes
the ith columns of A and B as (ai,b i)↦→(bi−ai,−ai). Therefore, given N complementary
columns of ( A B) that have full rank, we can use such permutations to move all the columns
(up to a sign) into B. □
THE QUANTUM CONTENT OF THE GLUING EQUATIONS 39
