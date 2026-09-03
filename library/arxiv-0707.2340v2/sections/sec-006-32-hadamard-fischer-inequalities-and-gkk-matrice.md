---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-006-32-hadamard-fischer-inequalities-and-gkk-matrice
section_title: "Hadamard-Fischer Inequalities and GKK-Matrices"
section_number: 3.2
pages: 15-17
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
---
matrix A over C and S ⊆ [n] denote by A[S] the principal submatrix of A with rows
and columns indexed by S and let A⟨S⟩ = det( A[S′]) be the principal minor of A
with rows and columns indexed by S′ = [n] \ S, where A⟨[n]⟩ = det(A[∅]) := 1. The
matrix A is called a P -matrix if all its principal minors are positive. A much studied
class of P -matrices that uniﬁes several important types of matrices is the c lass of
GKK-matrices, see [28, 40] and references therein. A P -matrix A is a GKK- matrix
(after Gantmacher-Krein and Kotelyansky) if it satisﬁes the Hadamard-Fischer-
Kotelyansky inequalities, that is,
A⟨S⟩A⟨T ⟩ ≥ A⟨S ∪ T ⟩A⟨S ∩ T ⟩, S, T ⊆ [n]. (7)
In other words, an n × n P -matrix A is GKK if and only if the probability measure
µA on 2 [n] deﬁned by
µA(S) = A⟨S⟩det(A + I)−1 (8)
16 J. BORCEA, P. BR ¨AND ´EN, AND T. M. LIGGETT
satisﬁes the negative lattice condition (NLC). It is not hard to see t hat the gener-
ating polynomial of such a measure is
gµA (z) = det( A + I)−1 ∑
S⊆[n]
A⟨S⟩zS = det(A + I)−1 det(A + Z), z S :=
∏
i∈S
zi,
where Z = diag(z1, . . . , zn). Examples of GKK-matrices are:
(I) Positive deﬁnite matrices;
(II) Totally positive matrices, i.e., matrices for which all minors are positive;
(III) Non-singular M -matrices; recall that an M -matrix (named after Minkowski)
is a matrix with all non-negative principal minors and all non-positive o ﬀ-
diagonal entries.
An ambitious project would be to classify GKK-matrices according to the various
negative dependence properties (introduced in §2) that these matrices satisfy. This
would take us beyond the scope of this paper. In what follows we will o nly brieﬂy
discuss some of these aspects.
Deﬁnition 3.1. We say that a P -matrix A is a Rayleigh matrix if the associated
probability measure µA deﬁned in (8) is Rayleigh (in the sense of Deﬁnition 2.5).
By [72, Theorem 4.4], Rayleigh matrices are GKK. In fact, the following holds.
Theorem 3.3. Let A be an n × n matrix over C. The following are equivalent:
(1) A is a Rayleigh matrix;
(2) A + X is a GKK-matrix for all X = diag(x1, . . . , xn), where xi ≥ 0 for all
1 ≤ i ≤ n.
Proof. (1) ⇒ (2): As we already noted, by [72, Theorem 4.4] Rayleigh matrices ar e
GKK and by deﬁnition the set of all Rayleigh matrices is obviously closed under
adding positive diagonal matrices.
(2) ⇒ (1): Let f = det(A + Z). Then
∂f
∂zi
(x) ∂f
∂zj
(x) − ∂2f
∂zi∂zj
(x)f (x) =
(A + X)⟨i⟩ · (A + X)⟨j⟩ − (A + X)⟨i, j⟩ · (A + X)⟨∅⟩.
Using the Hadamard-Fischer-Kotelyansky inequalities (7) for A + X with S = {i}
and T = {j} one gets the desired conclusion. □
It follows immediately from Theorem 3.3 that non-singular M -matrices and pos-
itive deﬁnite matrices are Rayleigh. Now for any s, t ∈ (0, 1) one can easily check
that the matrix
B =


1 1 /2 s/4
1/2 1 1 /2
t/4 1 /2 1

 (9)
is totally positive. Given an n × n matrix A and two subsets S, T ⊆ [n] of the same
size we let A(S, T ) denote the minor of A lying in rows indexed by S and columns
indexed by T . It was proved by Gantmacher-Krein [31] and Carlson [17] that a
necessary and suﬃcient condition for a P -matrix to be GKK is that
A(S, T )A(T, S ) ≥ 0 for any S, T ⊆ [n] with |S| = |T | = |S ∪ T | − 1.
Since
(B + I)(12, 23) = (1 − 2s)/4 and ( B + I)(23, 12) = (1 − 2t)/4
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS 17
we may choose s, t ∈ (0, 1) so that ( B + I)(12, 23)(B + I)(23, 12) < 0. We conclude
that for such values of s, t the matrix B + I fails to be GKK.
It is easy to see that the measures associated with positive deﬁnite and totally
positive matrices have ULC rank sequences. This follows from Newto n’s inequalities
and the fact that Hermitian matrices and totally positive matrices ha ve real-rooted
characteristic polynomials (in the case of totally positive matrices th is goes back to
Gantmacher and Krein [31]). For M -matrices it is not as obvious but nonetheless
true. In [40] Holtz and Schneider conjectured that M -matrices satisfy the conclusion
of Conjecture 2.4. This was subsequently conﬁrmed by Holtz in [39] using a certain
monotonicity property for so-called symmetrized Fischer product s of M -matrices
due to James-Johnson-Pierce [44] (see [8] for further results o n Fischer products).
We end this section with some open questions.
Question 3.1. Is µA an ULC measure whenever A is a Rayleigh matrix?
Question 3.2. For which GKK-matrices A is µA negatively associated?
Again, negative association fails for measures associated with tota lly positive
matrices. Indeed, let B be the totally positive 3 × 3 matrix deﬁned in (9) and ﬁx
s, t ∈ (0, 1) such that A := B + I is not GKK (see the above discussion). It is
known [17, 31] that an n × n P -matrix C is GKK if and only if
C⟨S ∪ {i}⟩ · C⟨S ∪ {j}⟩ ≥ C⟨S ∪ {i, j}⟩ · C⟨S⟩ (10)
for all S ⊆ [n] and i, j ∈ [n] \ S with i ⁄= j. Hence, since A fails to be GKK it
follows that (10) fails for A and some S, i, j. Unraveling the deﬁnitions this means
that for some principal submatrix B′ of B the corresponding measure µB′ will fail
to have pairwise negatively correlated variables (cf. Deﬁnition 2.3). In particular,
since NA ⇒ p-NC, the measure µB′ cannot be negatively associated.
Question 3.3. Describe all n × n Rayleigh matrices.
Question 3.4. Characterize the class of all real stable n× n matrices, that is, n× n
matrices A such that det(A + Z) is real stable.
