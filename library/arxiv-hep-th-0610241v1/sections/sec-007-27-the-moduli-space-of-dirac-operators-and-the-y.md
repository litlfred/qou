---
doc_id: arxiv-hep-th-0610241v1
doc_title: "Gravity and the standard model with neutrino mixing"
section_id: sec-007-27-the-moduli-space-of-dirac-operators-and-the-y
section_title: "The moduli space of Dirac operators and the Yukawa parameters"
section_number: 2.7
pages: 15-18
source_pdf: hep-th-0610241.pdf
source_sha256: 6a71ab6f6459c070
toc_source: inferred
doc_brief: "Gravity and the standard model with neutrino mixing — We present an eﬀective uniﬁed theory based on noncommutative geometry for the standard model with neutrino mixing, minimally coupled to gravity."
---
Let us start by considering the moduli space C3 of pairs of invertible 3×3 matrices (Y(↓3), Y(↑3))
modulo the equivalence relation
Y ′
(↓3) = W1 Y(↓3) W ∗
3 , Y ′
(↑3) = W2 Y(↑3) W ∗
3 ,
(2.39)
where the Wj are unitary matrices.
16
CHAMSEDDINE, CONNES, AND MARCOLLI
Proposition 2.24. The moduli space C3 is the double coset space
C3 ∼= (U(3) × U(3))\(GL3(C) × GL3(C))/U(3)
(2.40)
of real dimension 10.
Proof. This follows from the explicit form of the equivalence relation (2.39). The group U(3)
acts diagonally on the right.
Remark 2.25. Notice that the 3 in C3 corresponds to the color charge for quarks (like the 1
in C1 below will correspond to leptons), while in the right hand side of (2.40) the 3 of GL3(C)
and U(3) corresponds to the number of generations.
Each equivalence class under (2.39) contains a pair (Y(↓3), Y(↑3)) where Y(↑3) is diagonal (in
the given basis) and with positive entries, while Y(↓3) is positive.
Indeed, the freedom to chose W2 and W3 makes it possible to take Y(↑3) positive and diagonal
and the freedom in W1 then makes it possible to take Y(↓3) positive.
The eigenvalues are the characteristic values (i.e. the eigenvalues of the absolute value in the
polar decomposition) of Y(↑3) and Y(↓3) and are invariants of the pair.
Thus, we can ﬁnd diagonal matrices δ↑and δ↓and a unitary matrix C such that
Y(↑3) = δ↑,
Y(↓3) = C δ↓C∗.
Since multiplying C by a scalar does not aﬀect the result, we can assume that det(C) = 1.
Thus, C ∈SU(3) depends a priori upon 8 real parameters. However, only the double coset
of C modulo the diagonal subgroup N ⊂SU(3) matters, by the following result.
Lemma 2.26. Suppose given diagonal matrices δ↑and δ↓with positive and distinct eigen-
values. Two pairs of the form (δ↑, C δ↓C∗) are equivalent iﬀthere exists diagonal unitary
matrices A, B ∈N such that
A C = C′ B.
Proof. For A C = C′ B one has
A Y(↑3) A∗= Y ′
(↑3) ,
A Y(↓3) A∗= Y ′
(↓3)
and the two pairs are equivalent. Conversely, with Wj as in (2.39) one gets W1 = W3 from
the uniqueness of the polar decomposition
δ↓= (W1W ∗
3 ) (W3δ↓W ∗
3 ).
Similarly, one obtains W2 = W3. Thus, W3 = W is diagonal and we get
W C δ↓C∗W ∗= C′ δ↓C′∗,
so that W C = C′ B for some diagonal matrix B. Since W and B have the same determinant
one can assume that they both belong to N.
The dimension of the moduli space is thus 3 + 3 + 4 = 10 where the 3 + 3 comes from
the eigenvalues and the 4 = 8 −4 from the above double coset space of C’s. One way to
parameterize the representatives of the double cosets of the matrix C is by means of three
angles θi and a phase δ,
C =


c1
−s1c3
−s1s3
s1c2
c1c2c3 −s2s3eδ
c1c2s3 + s2c3eδ
s1s2
c1s2c3 + c2s3eδ
c1s2s3 −c2c3eδ

,
(2.41)
GRAVITY AND THE STANDARD MODEL WITH NEUTRINO MIXING
17
for ci = cos θi, si = sin θi, and eδ = exp(iδ). One has by construction the factorization
C = R23(θ2) d(δ) R12(θ1) R23(−θ3)
(2.42)
where Rij(θ) is the rotation of angle θ in the ij-plane and d(δ) the diagonal matrix
d(δ) =


1
0
0
0
1
0
0
0
−eiδ


Let us now consider the moduli space C1 of triplets (Y(↓1), Y(↑1), YR), with YR symmetric,
modulo the equivalence relation
Y ′
(↓1) = V1 Y(↓1)V ∗
3
Y ′
(↑1) = V2 Y(↑1) V ∗
3
(2.43)
Y ′
R = V2 YR ¯V ∗
2 .
(2.44)
Lemma 2.27. The moduli space C1 is given by the quotient
C1 ∼= (U(3) × U(3))\(GL3(C) × GL3(C) × S)/U(3),
(2.45)
where S is the space of symmetric complex 3 × 3 matrices and
• The action of U(3)×U(3) on the left is given by left multiplication on GL3(C)×GL3(C)
and by (2.44) on S.
• The action of U(3) on the right is trivial on S and by diagonal right multiplication on
GL3(C) × GL3(C).
It is of real dimension 21 and ﬁbers over C3, with generic ﬁber the quotient of symmetric
complex 3 × 3 matrices by U(1).
Proof. By construction one has a natural surjective map
π : C1 →C3
just forgetting about YR. The generic ﬁber of π is the space of symmetric complex 3 × 3
matrices modulo the action of a complex scalar λ of absolute value one by
YR 7→λ2 YR.
The (real) dimension of the ﬁber is 12−1 = 11. The total real dimension of the moduli space
C1 is then 21.
The total 31-dimensional moduli space of Dirac operators is given by the product
C1 × C3.
(2.46)
Remark 2.28. The 31 real parameters of (2.46) correspond to the Yukawa parameters in
the standard model with neutrino mixing and Majorana mass terms. In fact, the parameters
in C3 correspond to the masses of the quarks and the quark mixing angles of the CKM matrix,
while the additional parameters of C1 give the lepton masses, the angles of the PMNS mixing
matrix and the Majorana mass terms.
18
CHAMSEDDINE, CONNES, AND MARCOLLI
