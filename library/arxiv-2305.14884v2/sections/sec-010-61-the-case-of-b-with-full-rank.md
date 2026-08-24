---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-010-61-the-case-of-b-with-full-rank
section_title: "The case of B with full rank"
section_number: 6.1
pages: 25-27
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
doc_brief: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS — We prove that a formal power series associated to an ideally triangu lated cusped hyperbolic 3-manifold (together with some further choices)"
---
3.6 under the
assumption that the matrix B has full rank. In this case, Equation ( 98) simpliﬁes to the
following one
Φ Ξ (ℏ) Φ ~Ξ (ℏ)
Pentagon
(100)
since we do not need to apply Fourier transform, nor Fubini’s theore m.
Proposition 6.2. If B has full rank, then Φ Ξ (ℏ) is invariant under the 2–3 Pachner move
given in Equation ( 96).
Proof. To begin with, noting that in this case A = A and B = B, we have:
Φ Ξ (ℏ) = ⟨I0⟩x,Λ (101)
where
I0 = exp
(ℏ
8ftB−1Af − ℏ
1
2
2 xt(B−1ν − 1)
) N +2∏
j=1
ψℏ(xj,zj)
and
Λ 0 = diag( z′) − Q
26 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WH EELER
and x = (x1,x 2,x ∗) are the integration variables. Applying the pentagon identity of Th eo-
rem 3.6, to the ψℏ with arguments x1,x 2 and introducing a new integration variable x0, we
obtain that
Φ Ξ (ℏ) = ⟨I1⟩(x0,x),Λ 1 (102)
where
I1 = exp
(
− ℏ
24 + ℏ
8ftB−1Af − ℏ
1
2
2 xt(B−1ν − 1)
)
ψ ℏ
(
−x0 −x2 + x1z2 +x2z1
z0
,z 1z−1
0
)
×ψ ℏ
(
x0 +x1 +x2 − x1z2 +x2z1
z0
,z 0
)
ψ ℏ
(
−x0 −x1 + x1z2 +x2z1
z0
,z 2z−1
0
) N∏
j=1
ψ ℏ(x∗
j,z ∗
j )
and
Λ 1 =
(
(z1+z2−z1z2)2
(z1−1)z1(z2−1)z2
0
0 Λ
)
.
Making a change of variables x0 ↦→x0 +x1(−1 +z2z−1
0 ) +x2(−1 +z1z−1
0 ) using Lemma 3.1,
we obtain that
Φ Ξ (ℏ) = ⟨I2⟩(x0,x),Λ 2, (103)
where
I2 = exp
(
− ℏ
24 + ℏ
8ftB−1Af − ℏ
1
2
2 xt(B−1ν − 1)
)
ψℏ(−x0 +x1,z 1z−1
0 )
×ψℏ(x0,z 0)ψℏ(−x0 +x2,z 2z−1
0 )
N∏
j=1
ψℏ(x∗
j,z ∗
j )
and
Λ 2 =
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
z1(z2−1) 0
z1+z2−z1z2
z2(z1−1) −Q11−z1+z2−z1z2
z2(z1−1) 1 − Q12 −Q∗
1
z1+z2−z1z2
z1(z2−1) 1 − Q12 −Q22−z1+z2−z1z2
z1(z2−1) −Q∗
2
0 −Q∗
1
t −Q∗
2
t diag(z∗′) − Q∗








.
Making a change of variables x1 ↦→x1 +x0 andx2 ↦→x2 +x0 using Lemma
3.1, and denoting
~x = (x0,x ),~z = (z0,z 1z−1
0 ,z 2z−1
0 ,z ∗) we obtain that
Φ Ξ (ℏ) = ecℏ⟨I3⟩~x,Λ 3, (104)
where
I3 = exp
(ℏ
8
~ft~B−1~A~f − ℏ
1
2
2 ~xt(~B−1~ν − 1)
) N +3∏
j=1
ψℏ(~xj,~zj)
and
Λ 3 = diag(˜z′) − ˜B−1 ˜A.
□
The next lemma identiﬁes vectors and matrices of the two triangulat ions T and ~T .
PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS 27
Lemma 6.3. With the notation used in the proof of the previous Proposition 6.2,
~B−1~A =






Q11 + 2Q12 + Q22 − 1 Q11 + Q12 − 1 Q12 + Q22 − 1 Q∗
1 + Q∗
2
Q11 + Q12 − 1 Q11 Q12 − 1 Q∗
1
Q12 + Q22 − 1 Q12 − 1 Q22 Q∗
2
Q∗
1
t + Q∗
2
t Q∗
1
t Q∗
2
t Q∗






(105)
~B−1~ν =
(
(B−1ν)1 + (B−1ν)2 − 1
B−1ν
)
(106)
~ft~B−1~ν = ftB−1ν − ~f0 (107)
Proof. We will show that both sides of Equations (
105) and Equations ( 106) are equal after
multiplying by the invertible matrix ~B. For Equation ( 105), we have
(
−1 1 1 0
0 b1 b2 b∗
)






Q11 + 2Q12 + Q22 − 1 Q11 + Q12 − 1 Q12 + Q22 − 1 Q∗
1 + Q∗
2
Q11 + Q12 − 1 Q11 Q12 − 1 Q∗
1
Q12 + Q22 − 1 Q12 − 1 Q22 Q∗
2
Q∗
1
t + Q∗
2
t Q∗
1
t Q∗
2
t Q∗






=
(
−1 0 0 0
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
+b1(−1+Q12) b1Q∗
1 +b2Q∗
2 +b∗Q∗
)
= ~A.
(108)
For Equation ( 106), we have(
−1 1 1 0
0 b1 b2 b∗
)(
(B−1ν)1 + (B−1ν)2 − 1
B−1ν
)
=
(
1
ν
)
. (109)
Finally, for Equation ( 107),
~ft~B−1ν = ~ft
(
(B−1ν)1 + (B−1ν)2 − 1
B−1ν
)
= ( ~f0 + ~f1)(B−1ν)1 + (~f0 + ~f2)(B−1ν)2 +f ∗(B−1ν)1 − ~f0,
(110)
and we recall we choose fi = ~f0 + ~fi for i = 1, 2. □
