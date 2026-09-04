---
doc_id: arxiv-math-9910147v1
doc_title: "Tensor Products of Principal Unitary Representations of Quantum Lorentz Group and Askey-Wilson Polynomials E. Buffenoir ∗"
section_id: sec-044-5-decomposition-theorem-of-the-tensor-product-of
section_title: "Decomposition Theorem of the Tensor Product of Prin-"
section_number: 5
pages: 22-23
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
doc_brief: "Tensor Products of Principal Unitary Representations of Quantum Lorentz Group and Askey-Wilson Polynomials E. Buffenoir ∗ — We study the tensor product of principal unitary representa tions of the"
---
cipal Representations and Askey-Wilson Polynomials
5.1 Decomposition Theorem of the Tensor Product of Principa l Rep-
resentations
Let us now prove that, chosing N
(X0X1 ) ( Y0 Y1)
(Z0 Z1 ) = ( M
(X0 X1 )(Y0 Y1)
(Z0 Z1 ) )1/2 > 0, ˆΦ[X0X1,Y 0Y1] is an
isometry.
Theorem 3 ˆΦ[X0X1,Y 0Y1] : V (X0X1) ⊗V (Y0Y1) →
∫ ⊕
d(Z0Z1)H(Z0Z1) is an isometry. This
is a direct consequence of the following identity:
∀C ∈ 1
2 Z+,
∫
dP(Z0Z1)


A’ B’
X0X1 Y0Y1
A B
C
Z0Z1
C

 =δA,A′δB,B ′Y (1)
(A,X0−X1)Y (1)
(B,Y0−Y1). (81)
22
Proof:
V (X0X1) ⊗V (Y0Y1) is a Uq(su(2)) module, let us denote by ( V (X0X1) ⊗V (Y0Y1))[C] its
isotypic component of spin C. From the deﬁnition of ˆΦ[X0X1,Y 0Y1] and the choice N =
(M
(X0 X1 )(Y0 Y1 )
(Z0 Z1) )1/2, it is simple to show that the restriction of ˆΦ[X0X1,Y 0Y1] to ( V (X0X1) ⊗
V (Y0Y1))[C] is an isometry if and only if (81) is satisﬁed for this C. We already proved that

A’ B’
X0X1 Y0Y1
A B
C
Z0Z1
C

 is a piecewise continuous function of ρZ, as a result it is integrable,
and using formula (65) and the uniform convergence properties of this series, we can invert the
integral and the sum:
lefthandside of (81) =
=
∑
KLM N
[dN ][dK ]
[dC ]2 Λ KL
A′A(X0X1)Λ KM
B′B (Y0Y1)
∫
dP(Z0Z1)Λ KN
A′A(Z1Z0) ×
×
{
K A
B N
L
C
}
(0)
{
A′ B′
K N
C
M
}
(0)
{
B K
A′ N
M
L
}
(0)
Using the Plancherel formula (59), we obtain that this series is equa l to:
=δA,A′δB,B ′Λ 0A
AA(X0X1)Λ 0B
BB (Y0Y1)
{ 0 A
B C
A
C
}
(0)
{ A B
0 C
C
B
}
(0)
{ B 0
A C
B
A
}
(0)
=
= righthandside of (81) .
□
ˆΦ[X0X1,Y 0Y1] being an isometry from V (X0X1)⊗V (Y0Y1) to the Hilbert space
∫ ⊕d(Z0Z1)H(Z0Z1),
there exists a unique isometry Φ #[X0X1,Y 0Y1] from the tensor product of Hilbert space H(X0X1)⊗
H(Y0Y1) to
∫ ⊕d(Z0Z1)H(Z0Z1) which restriction toV (X0X1)⊗V (Y0Y1) gives back ˆΦ[X0X1,Y 0Y1].
Theorem 4 Φ #[X0X1,Y 0Y1] : H(X0X1) ⊗H(Y0Y1) →
∫ ⊕d(Z0Z1)H(Z0Z1) is an invertible
isometry of Hilbert space.
Proof:
It is trivial that Φ #[X0X1,Y 0Y1] is an isometry, as a result it is injective. We therefore
have only to show that Φ #[X0X1,Y 0Y1] is surjective. The proof goes along the same lines
as the proof of the surjectivity of the Fourier transform in [1]. It is suﬃcient to show that
E = Φ #[X0X1,Y 0Y1](V (X0X1) ⊗V (Y0Y1)) is dense in
∫ ⊕
d(Z0Z1)H(Z0Z1), which is equivalent
to show that E⊥ = {0}. Let f ∈
∫ ⊕
d(Z0Z1)H(Z0Z1), and assume that <f, Φ[X0X1,Y 0Y1](
A
ei
(X0X1)⊗
B
ej (Y0Y1))>= 0, ∀A,B,i,j. This in particular implies that
<f, Φ[X0X1,Y 0Y1](∆( a)(
A
e i (X0X1)⊗
B
ej (Y0Y1)))>= 0 (82)
for any element a in the center of Uq(sl(2, C))R. As a result, by taking a = Ω p
+Ω r
− and using
the property that Φ
(X0 X1 )(Y0 Y1)
(Z0 Z1) is an intertwiner, we get the identity: ∀p,r ∈ N, ∀A,B,C ∈
1
