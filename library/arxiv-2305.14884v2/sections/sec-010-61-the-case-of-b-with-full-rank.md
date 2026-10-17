---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-010-61-the-case-of-b-with-full-rank
section_title: "The case of B with full rank"
section_number: 6.1
pages: 25-27
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
toc_source: outline
---
assumption that the matrix B has full rank. In this case, Equation (98) simpliﬁes to the
following one
ΦΞ(ℏ)
ΦeΞ(ℏ)
Pentagon
(100)
since we do not need to apply Fourier transform, nor Fubini’s theorem.
Proposition 6.2. If B has full rank, then ΦΞ(ℏ) is invariant under the 2–3 Pachner move
given in Equation (96).
Proof. To begin with, noting that in this case A = A and B = B, we have:
ΦΞ(ℏ) = ⟨I0⟩x,Λ
(101)
where
I0 = exp
ℏ
8f tB−1Af −ℏ
1
2
2 xt(B−1ν −1)
 N+2
Y
j=1
ψℏ(xj, zj)
and
Λ0 = diag(z′) −Q
26
STAVROS GAROUFALIDIS, MATTHIAS STORZER, AND CAMPBELL WHEELER
and x = (x1, x2, x∗) are the integration variables. Applying the pentagon identity of Theo-
rem 3.6, to the ψℏwith arguments x1, x2 and introducing a new integration variable x0, we
obtain that
ΦΞ(ℏ) = ⟨I1⟩(x0,x),Λ1
(102)
where
I1 = exp

−ℏ
24 + ℏ
8f tB−1Af −ℏ
1
2
2 xt(B−1ν −1)

ψℏ

−x0 −x2 + x1z2 + x2z1
z0
, z1z−1
0

× ψℏ

x0 + x1 + x2 −x1z2 + x2z1
z0
, z0

ψℏ

−x0 −x1 + x1z2 + x2z1
z0
, z2z−1
0
 N
Y
j=1
ψℏ(x∗
j, z∗
j )
and
Λ1 =
 
(z1+z2−z1z2)2
(z1−1)z1(z2−1)z2
0
0
Λ
!
.
Making a change of variables x0 7→x0 + x1(−1 + z2z−1
0 ) + x2(−1 + z1z−1
0 ) using Lemma 3.1,
we obtain that
ΦΞ(ℏ) = ⟨I2⟩(x0,x),Λ2,
(103)
where
I2 = exp

−ℏ
24 + ℏ
8f tB−1Af −ℏ
1
2
2 xt(B−1ν −1)

ψℏ(−x0 + x1, z1z−1
0 )
× ψℏ(x0, z0) ψℏ(−x0 + x2, z2z−1
0 )
N
Y
j=1
ψℏ(x∗
j, z∗
j )
and
Λ2 =








(z1+z2−z1z2)2
(z1−1)z1(z2−1)z2
z1+z2−z1z2
z2(z1−1)
z1+z2−z1z2
z1(z2−1)
0
z1+z2−z1z2
z2(z1−1)
−Q11−z1+z2−z1z2
z2(z1−1)
1 −Q12
−Q∗
1
z1+z2−z1z2
z1(z2−1)
1 −Q12
−Q22−z1+z2−z1z2
z1(z2−1)
−Q∗
2
0
−Q∗
1
t
−Q∗
2
t
diag(z∗′) −Q∗








.
Making a change of variables x1 7→x1 +x0 and x2 7→x2 +x0 using Lemma 3.1, and denoting
ex = (x0, x), ez = (z0, z1z−1
0 , z2z−1
0 , z∗) we obtain that
ΦΞ(ℏ) = ecℏ⟨I3⟩ex,Λ3,
(104)
where
I3 = exp
ℏ
8
ef t eB−1 eA ef −ℏ
1
2
2 ext( eB−1eν −1)
 N+3
Y
j=1
ψℏ(exj, ezj)
and
Λ3 = diag(˜z′) −˜B−1 ˜A .
□
The next lemma identiﬁes vectors and matrices of the two triangulations T and eT .
PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS
27
Lemma 6.3. With the notation used in the proof of the previous Proposition 6.2,
eB−1 eA =






Q11 + 2Q12 + Q22 −1
Q11 + Q12 −1
Q12 + Q22 −1
Q∗
1 + Q∗
2
Q11 + Q12 −1
Q11
Q12 −1
Q∗
1
Q12 + Q22 −1
Q12 −1
Q22
Q∗
2
Q∗
1
t + Q∗
2
t
Q∗
1
t
Q∗
2
t
Q∗






(105)
eB−1eν =

(B−1ν)1 + (B−1ν)2 −1
B−1ν

(106)
ef t eB−1eν = f tB−1ν −ef0
(107)
Proof. We will show that both sides of Equations (105) and Equations (106) are equal after
multiplying by the invertible matrix eB. For Equation (105), we have

−1
1
1
0
0
b1
b2
b∗







Q11 + 2Q12 + Q22 −1
Q11 + Q12 −1
Q12 + Q22 −1
Q∗
1 + Q∗
2
Q11 + Q12 −1
Q11
Q12 −1
Q∗
1
Q12 + Q22 −1
Q12 −1
Q22
Q∗
2
Q∗
1
t + Q∗
2
t
Q∗
1
t
Q∗
2
t
Q∗






=
 
−1
0
0
0
b1(−1+Q11+Q12)+b∗Q∗
1
t
+b2(−1+Q12+Q22)+b∗Q∗
2
t
b1Q11+b∗Q∗
1
t
+b2(−1+Q12)
b2Q22+b∗Q∗
2
t
+b1(−1+Q12)
b1Q∗
1 + b2Q∗
2 + b∗Q∗
!
= eA.
(108)
For Equation (106), we have

−1
1
1
0
0
b1
b2
b∗
 
(B−1ν)1 + (B−1ν)2 −1
B−1ν

=

1
ν

.
(109)
Finally, for Equation (107),
ef t eB−1ν = ef t

(B−1ν)1 + (B−1ν)2 −1
B−1ν

= ( ef0 + ef1)(B−1ν)1 + ( ef0 + ef2)(B−1ν)2 + f ∗(B−1ν)1 −ef0 ,
(110)
and we recall we choose fi = ef0 + efi for i = 1, 2.
□
