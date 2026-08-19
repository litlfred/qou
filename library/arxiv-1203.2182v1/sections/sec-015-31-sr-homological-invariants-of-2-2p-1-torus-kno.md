---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-015-31-sr-homological-invariants-of-2-2p-1-torus-kno
section_title: "Sr homological invariants of (2, 2p + 1) torus knots"
section_number: 3.1
pages: 12-15
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
Our goal in this section is to compute the colored superpolyn omials P R(a,q,t ) for (2, 2p + 1)
torus knots and symmetric and anti-symmetric representati ons, R = Sr and R = Λ r. In
performing this calculation, we ﬁrst review the analogous computation of the polynomial knot
invariants (on the left side of Figure 2) in Chern-Simons gau ge theory and then “reﬁne” it.
We should stress right away, however, that the reﬁned calculation is not done in a topological
3d gauge theory or, at least, such a 3d gauge theory interpret ation of the formal steps that
we are going to take is not known at present.
In Chern-Simons gauge theory, one can eﬃciently compute (3. 1) using the topological
invariance of the theory. Dividing a 3-manifold M into two piecesM1 andM2 along a surface
Σ, one can express the partition function Z CS
SU (N )(M,K R;q) as a pairing between the two
elements |ψM1;KR⟩ and |ψM2;KR⟩ in the physical Hilbert space HΣ :
Z CS
SU (N )(M,K R;q) = Σ ⟨ψM2;KR|ψM1;KR⟩Σ . (3.12)
The physical Hilbert space HΣ is obtained by the canonical quantization of the Chern-Simons
gauge theory on Σ × R, and the following correspondence is found in [25, 29]:
HΣ ≃
{
conformal blocks for G/G WZW model on Σ
}
,
whereG =SU (N). If the knotKR meets the surface Σ atm points, the physical Hilbert space
HΣ; R1···Rm consists of conformal blocks for m-point functions which carry representations
Ra =R or
R (a = 1, · · ·,m ) depending on the orientation at the intersection.
Here we will focus on the torus knots T 2,2p+1 in a 3-sphere and follow the steps of [30].
Among various choices of the surface Σ, we will consider a sli cing of S3 into a pair of 3-
dimensional balls B3 connected by a cylinder, as in Figure 3. The physical Hilbert space
HS2;R R R R for this slice consists of conformal blocks for the four poin t function:
φQ(R,R, R,R), Q ∈R ⊗R, (3.13)
– 11 –
R1 R2¯R1 ¯R2
B
B
B
|ψ0(R1,R 2)⟩
⟨ψ0(R1,R 2)|
Σ
Figure 3: Slicing and braiding.
whose the intermediate state carries an irreducible repres entation Q ∈ R ⊗R. In general,
HS2;R1R2R3R4 is spanned by orthonormal states:
⟨φQ′(R1,R 2,R 3,R 4)|φQ(R1,R 2,R 3,R 4)⟩ =δQQ′, Q,Q ′ ∈R1 ⊗R2. (3.14)
R1
R2 ¯R3
¯R4
Q
φQ(R1,R 2, ¯R3, ¯R4)
Figure 4: Conformal block φQ′(R1,R 2,R3,R4) for the four point function.
For a state |ψ0(R1,R 2)⟩ ∈ H S2;R1R2R2R1 associated with the lower half of the 3-ball in
Figure 3, the following expansion can be considered:
|ψ0(R1,R 2)⟩ =
∑
Q∈R1⊗R2
µQ
R1R2|φQ(R1,R 2,
R2,R1)⟩. (3.15)
– 12 –
The coeﬃcient µQ
R1R2 is determined by taking a pairing of this state with itself:
⟨ψ0(R1,R 2)|ψ0(R1,R 2)⟩ =
∑
Q∈R1⊗R2
(
µQ
R1R2
) 2
= Z CS
SU (N )(S3,
R1 R2;q). (3.16)
Since the two unknots here are not linked, we can separate them by an application of another
slicing along a surface Σ 2 ≃ S2, as in Figure 5:
Z CS
SU (N )(S3, R1 R2;q)Z CS
SU (N )(S3;q) = Z CS
SU (N )(S3, R1;q)Z CS
SU (N )(S3, R2;q). (3.17)
∪ ∪
ZCS
SU (N )(S3, © R1, © R2;q) ZCS
SU (N )(S3;q) ZCS
SU (N )(S3, © R1;q) ZCS
SU (N )(S3, © R2;q)
R1 R2R1 R2Σ
Σ 2 Σ 2 Σ 2 Σ 2
Figure 5: Slicing along Σ 2 ≃ S2.
The partition function of the unknot R in S3 is given by the quantum dimension:
Z CS
SU (N )(S3, R;q)
Z CS
SU (N )(S3;q) = dim qR. (3.18)
Here, the quantum dimension dim qR is a specialization of the Schur polynomial sR(x):
dimqR = sR(q̺), ̺ = (̺1, · · ·,̺ N), ̺ i = N + 1
2 −i, (3.19)
which enjoys the following identity:
sR1(x)sR2(x) =
∑
Q∈R1⊗R2
sQ(x). (3.20)
Using these relations, the coeﬃcient µQ can be determined as:
(
µQ
R1R2
) 2
= sQ(q̺) ·Z CS
SU (N )(S3;q). (3.21)
The state |ψ2p+1(R1,R 2)⟩ associated with the top part of the picture 3 is constructed b y
acting 2p + 1 times with the braid operator BR1R2 on the 3-ball state |ψ0(R1,R 2)⟩:
|ψ2p+1(R1,R 2)⟩ = B2p+1
R1R2|ψ0(R1,R 2)⟩. (3.22)
– 13 –
The action of the braid operator BR1R2 on the conformal block φQ(R1,R 2,R 3,R 4) obeys a
monodromy transformation. The eigenvalue of the monodromy for the conformal block is
determined by the conformal weights hRa of primary states in the G/G WZW model [31]:
λ′
Q(R1,R 2) = ǫQ
R1R2eπi(hR1 +hR2 −hQ) = ǫQ
R1R2q
1
