---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-006-34-matrix-representations
section_title: "Matrix representations"
section_number: 3.4
pages: 12-13
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
Proposition 3.1 already tells us that any rational matrix of the form A = (Im|A′) is 1 / ˙κA-
integral, and according to Lemma 3.3, the inverse of every non-singular square submatrix of A
is also 1/ ˙κA-integral. It is natural to ask whether every linear subspac e W can be represented
as W = ker(A) for an integer matrix A with the same property on the inverse matrices.
We show that this is true if the dual space is anchored but false in general. Recall that this
means that every elementary vector gC , C∈C W ⊥ has a ±1 entry. In particular, ˙κW = pα for
some prime number p∈ P implies that both W andW ⊥ are anchored; in this case we also have
κW = ˙κW .
In [ Lee89, Section 7], it is shown that if B is a basis minimizing | det(AB)| for a full rank
A∈ Rm×n, then every nonzero entry in A−1
B A is at least 1 in absolute value. Moreover, a simple
greedy algorithm is proposed (called 1-OPT) that ﬁnds such a basis within m pivots for k-adic
spaces. Our next statement can be seen as the variant of this f or anchored-spaces, using the
lcm-circuit imbalance ˙κA. We note that ﬁnding a basis minimizing | det(AB)| is computationally
hard in general [ Kha95].
Proposition 3.18. LetW⊆ Rn, dim(W ) = n−m be a rational subspace such that W ⊥ is an
anchored space. Then there exists an integer matrix A∈ Zm×n such that ker(A) = W , and
(i) All entries of A divide ˙κW .
(ii) For all non-singular submatrices M of A, M −1 is 1
˙κW
-integral.
(iii) ˙∆ A is an integer divisor of ( ˙κW )m.
Proof. Let ¯A∈ Qm×n be an arbitrary matrix with ker( ¯A) = W . By performing row operations
we can convert ˜A into A = (D|A′)∈ Zm×n where D ∈ Dm is positive diagonal and A′ ∈
Zm×(n−m) (after possibly permuting the columns). If D = Im, then we are already done.
Property (i) follows by Proposition 3.1; property (ii) follows by Lemma 3.3, and property (iii)
holds since det(M )· det(M −1) = 1, det(M )∈ Z, and det(M −1) is 1
( ˙κW )m -integral.
If D is not the identity matrix, then we show that A can be brought to the form ( Im|A′′)
with an integer A′′ by performing further basis exchanges. Let us assume that gc d(Ai) = 1 for
all rows Ai,i∈ [m]. By Lemma 3.13,Ai∈F (W ⊥). Assume Dii =Aii> 1 for some i∈ [m]. As
Ai is a circuit and W ⊥ is anchored, there exists an index k∈ [n] such that |Aik| = 1.
Let us perform a basis exchange between columns i andk. That is, subtract integer multiples
of rowi from the other rows to turn column k intoei. We then swap columns i andk and obtain
12
the matrix again in the form ( D′|A′′). Notice that the matrix remains integral, D′
ii = 1, and
D′
jj =Djj for j∈ [m], j⁄=i. Hence, repeating this procedure at most n times, we can convert
the matrix to the integer form ( Im|A′), completing the proof.
Note that the proof gives an algorithm to ﬁnd such a basis repr esentation using a Gaussian
elimination and at most m additional pivot operations. If W ⊥ is not anchored, we show the
following weaker statement.
Proposition 3.19. LetW⊆ Rn, dim(W ) = n−m be a rational subspace. Then there exists an
integer matrix A∈ Zm×n with ker(A) = W such that
(i) All entries of A divide ˙κW ;
(ii) For all non-singular submatrices M of A, M −1 is 1
( ˙κW )2 -integral.
(iii) ˙∆ A is an integer divisor of ( ˙κW )m.
Proof. The proof is an easy consequence of Proposition 3.1 and Lemma 3.3. Consider any basis
form A = (Im|A′) with ker( A) = W (after possibly permuting the columns). According to
Proposition 3.1, all entries of A are 1/ ˙κW integral. By Lemma 3.13, the rows Ai∈F (W ⊥) for
i∈ [m]. We can write Ai =gi/di for some gi∈F (W ⊥)∩ Zm and di∈ Q such that gcd(gi) = 1
for each i∈ [m]. By the deﬁnition of ˙κA, the entries of each gi are divisors of ˙κA. Since Aii = 1
it follows that di∈ Z and di| ˙κA. Let D∈ Dm be the diagonal matrix with entries Dii = di.
Then, ¯A =DA is an integer matrix where all entries divide ˙ κA, proving (i). Part (ii) follows by
Lemma 3.3 and noting that the subdeterminants get multiplied by a subm atrix D−1.
For part (iii), let us start use a basis B such that | det(AB)| is maximal; w.l.o.g. assume
B = [m]. Then, in the basis form ( Im|A′) for B, all subdeterminants are ≤ 1. This holds as
for any submatrix M∈ Qk×k of A′ with det(M )⁄= 0 we have that augmenting the columns of
M by the columns i∈B such that i is not a row of M results in a basis BM with| det(M )| =
| det
(
(Im|A′)BM
)
| ≤det(Im) = 1 by assumption on B. After multiplying by D as above,
¯A =DA, all subdeterminants will be ≤ det(D)≤ ( ˙κA)m.
Note that parts (i) and (ii) are true for any choice of the basis form, whereas (iii) requires
one to select AB with maximum determinant. The maximum subdeterminant is NP -hard even
to approximate better than cm for some c> 1 [ DSEFM14]. However, it is easy to see that even
if we start with an arbitrary basis, then ˙∆ A| ( ˙κW )2m, since every subdeterminant of A−1
B A is
at most ( ˙κW )m follows by Lemma 3.3.
We now give an example to illustrate why Proposition 3.18(ii) cannot hold for arbitrary
values of ˙κW . The proof is given in the Appendix.
Proposition 3.20. Consider the matrix
A =
[1 3 4 3
0 13 9 10
]
.
For this matrix ˙κA = 5850 = 2 × 32× 52× 13 holds, and there exists no ˜A∈ Z2×4 such that
ker( ˜A) = ker(A) and the inverse of every nonsingular 2× 2 submatrix of ˜A is 1/5850-integral.
