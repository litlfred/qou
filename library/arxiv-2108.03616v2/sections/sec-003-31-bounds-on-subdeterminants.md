---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-003-31-bounds-on-subdeterminants
section_title: "Bounds on subdeterminants"
section_number: 3.1
pages: 7-9
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
For an integer matrix A∈ Zm×n, we deﬁne
∆ A := max{| det(B)| :B is a nonsingular submatrix of A}, and
˙∆ A := lcm{| det(B)| :B is a nonsingular submatrix of A}.
(2)
The matrix is totally unimodular (TU) , if ∆ A = 1: thus, all subdeterminants are 0 or ±1.
This class of matrices plays a foundational role in combinat orial optimization, see e.g., [ Sch98,
Chapters 19-20]. A signiﬁcant example is the node-arc incid ence matrix of a directed graph. A
key property is that they deﬁne integer polyhedra, see Theor em 3.5 below. A polynomial-time
algorithm is known to decide whether a matrix is TU, based on t he deep decomposition theorem
by Seymour from 1980 [ Sey80].
The next statement is implicit in [ Lee89, Proposition 5.3].
Proposition 3.2. For every integer matrix A∈ Zm×n, ¯κA≤ ∆ A and ˙κA≤ ˙∆ A.
7
Proof. LetC∈C A be a circuit, and select a submatrix ˆA∈ Z(|C|−1)×|C| ofA where the columns
are indexed by C, and the rows are linearly independent. Let ˆA−i be the square submatrix
resulting from deleting the column corresponding to i from ˆA. From Cramer’s rule, we see
that|gC
i| =| det( ˆA−i)|/α for some α∈ Q, α≥ 1. This implies both claims ¯ κA≤ ∆ A and
˙κA≤ ˙∆ A.
In Propositions 3.18 and 3.19, we show that for any matrix A∈ Qm×n there exists a matrix
˜A∈ Zm×n such that ker(A) = ker( ˜A) and ˙∆ ˜A≤ ( ˙κA)m.
To see an example where ∆ A can be much larger than κA, let A∈ Zn×(n
2) be the node-edge
incidence matrix of a complete undirected graph on n nodes; assume n is divisible by 3. The
determinant corresponding to any submatrix corresponding to an odd cycle is ±2. Let H be an
edge set of n
3 node-disjoint triangles. Then AH is a square submatrix with determinant ±2n/3.
In fact, ∆ A = 2n/3 in this case, since ∆ A for a node-edge incidence matrix equals the maximum
number of node disjoint odd cycles, see [ GKS95]. On the other hand, κA = ¯κA = ˙κA∈{ 1, 2}
for the incidence matrix A of any undirected graph; see Section 3.2.
For TU-matrices, the converse of Proposition 3.2 is also true. In 1956, Heller and Tompkins
[Hel57,HT56] introduced the Dantzig property. A matrix A∈ Rm×n has the Dantzig property if
A−1
B A is a 0,±1-matrix for every nonsingular m×m submatrixAB. According to Proposition 3.1,
this is equivalent to κA = 1. Theorem 3.4 below can be attributed to Cederbaum [ Ced57,
Proposition (v)]; see also Camion’s PhD thesis [ Cam64, Theorem 2.4.5(f)]. The key is the
following lemma that we formulate for general 1 / ˙κA for later use.
Lemma 3.3. LetA = (Im|A′)∈ Rm×n. Then, for any nonsingular square submatrix M of A,
the inverse M −1 is 1/ ˙κA-integral, with non-zero entries between 1/κA and κA in absolute value.
Proof. Let M be any k×k nonsingular submatrix of A; w.l.o.g., let us assume that it uses the
ﬁrst k rows of A. Let B be the set of columns of M , along with the m−k additional columns
i∈ [k + 1,m ], i.e., the last m−k unit vectors from Im. Thus, AB∈ Rm×m is also nonsingular.
After permuting the columns, this can be written in the form
AB =
( M 0
L Im−k
)
for some L∈ Z(m−k)×k. We now use Proposition 3.1 for ˜A = A−1
B A. Note that the ﬁrst m
columns of ˜A correspond to A−1
B . Moreover, we see that
A−1
B =
( M −1 0
−LM −1 Im−k
)
Thus,M −1 is 1/ ˙κA-integral, with non-zero entries between 1 /κA and κA completing the proof.
Appa and Kotnyek deﬁne k-regular matrices as follows: a rational matrix A′∈ Rm×n is k-
regular if and only if the inverse of all nonsingular submatr ices is 1/k-integral. From the above
statement, it follows that A′ is k-regular in this sense for k =κ(Im|A′). See also Corollary 3.9.
Theorem 3.4 (Cederbaum, 1957) . Let W⊂ Rn be a linear subspace. Then, the following are
equivalent.
(i) κW = ¯κW = ˙κW = 1.
(ii) There exists a TU matrix A, such that W = ker(A).
(iii) For any matrix A in basis form such that W = ker(A), A is a TU-matrix.
8
Proof. (iii)⇒ (ii) is straightforward, and (ii)⇒ (i) follows by Proposition 3.2. It remains to
show (i)⇒ (iii). Let rk( W ) = n−m, and consider any A∈ Rm×n in basis form such that
W = ker(A). For simplicity of notation, assume the basis is formed by t he ﬁrst m columns, that
is, A = (Im|A′) for some A′∈ Rm×(n−m).
Proposition 3.1 implies that all entries of A are 0 and ±1. Consider any nonsingular square
submatrix M of A. By Lemma 3.3, M −1 is also a 0, ±1 matrix. Consequently, both det( M )
and det(M −1) are nonzero integers, which implies that | det(M )| = 1, as required.
