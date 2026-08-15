---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-012-63-the-case-of-b-with-nullity-two
section_title: "The case of B with nullity two"
section_number: 6.3
pages: 33-41
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
doc_brief: "PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS — We prove that a formal power series associated to an ideally triangu lated cusped hyperbolic 3-manifold (together with some further"
---
assumption that the matrix B has nullity 2. Similarly to the proof of Proposition 6.4, we use
three intermediate formulas in Equation ( 98). They involve two Fourier transforms (adding
two variables), a pentagon (adding a third variable), two inverse Fo urier transforms (adding
two variables) and an applications of Fubini’s Theorem (removing four integration variables).
The details are given in the following proposition.
Proposition 6.6. If B has rank N then Φ Ξ (ℏ) is invariant under the 2–3 Pachner move
given in Equation (
98).
Proof. Following the discussion above, we can assume that rank( b1 |b2 |b∗) = rank( b∗) = N.
Then by [ 11, Lem.A.3], the matrix ( a1 −b1 |a2 −b2 |b∗) has full rank and we can apply a
quad move to the ﬁrst columns of ( A |B) to obtain
A = ( −b1 | − b2 |a∗), B = ( a1 −b1 |a2 −b2 |b∗) (129)
34 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WH EELER
where B has full rank. The proof will use the following sequence of intermedia te matrices
(A | B | ν ) =
(
−b1 −b2 a∗ a1 −b1 a2 −b2 b∗ ν −b1 −b2
)
q−1
2 × 1
(A |B |ν) =
(
a1 a2 a∗ b1 b2 b∗ ν
)
2 → 3
(~A |~B |~ν) =
(
−1 0 0 0 −1 1 1 0 1
a1 +a2 −b1 −b2 a1 −b2 a2 −b1 a∗ 0 b1 b2 b∗ ν
)
1 ×q2 × 1
(~A |~B |~ν ) =
(
−1 −1 −1 0 −1 −1 −1 0 −1
a1 +a2 −b1 −b2 −b1 −b2 a∗ 0 a1 −b1 −b2 a2 −b1 −b2 b∗ ν −b1 −b2
)
(130)
where B and ~B are invertible. With x = (x1,x 2,x ∗) and z = (z1,z 2,z ∗) vectors of size N + 2,
Φ Ξ (ℏ) is deﬁned by
Φ Ξ (ℏ) = ⟨I0⟩(x1,x2,x∗),Λ 0 (131)
where with f = (f ′
1,f ′
2,f ∗)
I0 = exp
(ℏ
8 ftB−1Af − ℏ
1
2
2 xt(B−1ν − 1)
)
×ψℏ
(
x1, 1
1 −z1
)
ψℏ
(
x2, 1
1 −z2
) N∏
j=1
ψℏ(x∗
j,z ∗
j )
and
Λ 0 = diag(1 −z−1
1 , 1 −z−1
2 ,z ∗′) − Q.
By applying Corollary
3.5 to both ψℏ(x1, 1
1−z1
) and ψℏ(x1, 1
1−z1
) we obtain with new integra-
tion variables w1 and w2 that
Φ Ξ (ℏ) = ⟨I1⟩(w1,w2,x1,x2,x∗),Λ 1 (132)
where
I1 = exp
( ℏ
12 + ℏ
8 ftB−1Af − ℏ
1
2
2 xt(B−1ν − 1) − (x1 +x2) ℏ
1
2
2
)
×ψℏ
(
w1 −x1(1 −z−1
1 ),z 1
)
ψℏ
(
w2 −x2(1 −z−1
2 ),z 1
) N∏
j=1
ψℏ(x∗
j,z ∗
j )
PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS 35
and
Λ 1 =


z2
1−z2
0 0
0 z1
1−z1
0
0 0 Λ


The substitutions w1 ↦→w1 +x1(1 −z−1
1 ) and w2 ↦→w2 +x2(1 −z−1
2 ) imply according to
Lemma
3.1 that
Φ Ξ (ℏ) = ⟨I2⟩(w1,w2,x1,x2,x∗),Λ 2 (133)
where
I2 = exp
( ℏ
12 + ℏ
8 ftB−1Af − ℏ
1
2
2 xt(B−1ν − 1) − (x1 +x2) ℏ
1
2
2
)
×ψℏ(w1,z 1)ψℏ(w2,z 2)
N∏
j=1
ψℏ(x∗
j,z ∗
j )
and with Q11 = Q12 = Q22 = 0 from Lemma
6.7
Λ 2 =






z1
1−z1
0 −1 0 0
0 z2
1−z2
0 −1 0
−1 0 0 0 −Q∗
1
0 −1 0 0 −Q∗
2
0 0 −Q∗
1
t −Q∗
2
t z∗′ − Q∗






.
We apply the pentagon identity of Theorem
3.6 to the ψh with arguments w1 and w1 and
obtain with the new integration variable x0
Φ Ξ (ℏ) = ⟨I3⟩(x0,w1,w2,x1,x2,x∗),Λ 3 (134)
where
I3 = exp
( ℏ
24 + ℏ
8 ftB−1Af − ℏ
1
2
2 xt(B−1ν − 1) − (x1 +x2) ℏ
1
2
2
)
×ψℏ
(
−x0 −w2 + w1z2 +w2z1
z0
,z 1z−1
0
)
ψℏ
(
x0 +w1 +w2 −w1z2 +w2z1
z0
,z 0
)
×ψℏ
(
−x0 −w1 + w1z2 +w2z1
z0
,z 2z−1
0
) N∏
j=1
ψℏ(x∗
j,z ∗
j )
and
Λ 3 =
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
0 0 0 0 0
0 z1
1−z1
0 −1 0 0
0 0 z2
1−z2
0 −1 0
0 −1 0 0 0 −Q∗
1
0 0 −1 0 0 −Q∗
2
0 0 0 −Q∗
1
t −Q∗
2
t z∗′ − Q∗








.
With change of variables x0 ↦→x0 −w1 −w2 + w1z2+w2z1
z0
Lemma 3.1 gives that
Φ Ξ (ℏ) = ⟨I4⟩(x0,w1,w2,x1,x2,x∗),Λ 4 (135)
36 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WH EELER
where
I4 = exp
( ℏ
24 + ℏ
8 ftB−1Af − ℏ
1
2
2 xt(B−1ν − 1) − (x1 +x2) ℏ
1
2
2
)
×ψℏ(−x0 +w1,z 1z−1
0 )ψℏ(x0,z 0)ψℏ(−x0 +w2,z 2z−1
0 )
N∏
j=1
ψℏ(x∗
j,z ∗
j )
and
Λ 4 =


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
(z1−1)z2
z1+z2−z1z2
(z2−1)z1
0 0 0
z1+z2−z1z2
(z1−1)z2
z1
1−z1
1 −1 0 0
z1+z2−z1z2
(z2−1)z1
1 z2
1−z2
0 −1 0
0 −1 0 0 0 −Q∗
1
0 0 −1 0 0 −Q∗
2
0 0 0 −Q∗
1
t −Q∗
2
t z∗′ − Q∗









.
We substitute w1 ↦→w1 +x0 and w2 ↦→w2 +x0 to obtain with Lemma
3.1 that
Φ Ξ (ℏ) = ⟨I5⟩(x0,w1,w2,x1,x2,x∗),Λ 5 (136)
where
I5 = exp
( ℏ
24 + ℏ
8 ftB−1Af − ℏ
1
2
2 xt(B−1ν − 1) − (x1 +x2) ℏ
1
2
2
)
×ψℏ(w1,z 1z−1
0 )ψℏ(x0,z 0)ψℏ(w2,z 2z−1
0 )
N∏
j=1
ψℏ(x∗
j,z ∗
j )
and
Λ 5 =








z1+z2−z1z2
(z1−1)(z2−1) 0 0 −1 −1 0
0 z1
(1−z1)z2
1 −1 0 0
0 1 z2
(1−z2)z1
0 −1 0
−1 −1 0 0 0 −Q∗
1
−1 0 −1 0 0 −Q∗
2
0 0 0 −Q∗
1
t −Q∗
2
t z∗′ − Q∗








.
By applying the ﬁrst quad move from Theorem
3.4 to both ψℏ(w1,z 1z−1
0 ) and ψℏ(w2,z 2z−1
0 )
we obtain with new integration variables y1 and y2 that
Φ Ξ (ℏ) = ⟨I6⟩(y1,y2,x0,w1,w2,x1,x2,x∗),Λ 6 (137)
where
I6 = exp
(
− ℏ
24 + ℏ
8 ftB−1Af − ℏ
1
2
2 xt(B−1ν − 1) − (x1 +x2) ℏ
1
2
2
+
(
y1 + w1z1z−1
0
1 −z1z−1
0
) ℏ
1
2
2 +
(
y2 + w2z2z−1
0
1 −z2z−1
0
) ℏ
1
2
2
) N∏
j=1
ψℏ(x∗
j,z ∗
j )
×ψℏ
(
y1 + w1z1z−1
0
1 −z1z−1
0
, 1
1 −z1z−1
0
)
ψℏ
(
y2 + w2z2z−1
0
1 −z2z−1
0
, 1
1 −z2z−1
0
)
ψℏ(x0,z 0)
PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS 37
and
Λ 6 =













(z1−1)z2
z1
0 0 0 0 0 0 0
0 (z2−1)z1
z2
0 0 0 0 0 0
0 0 z1+z2−z1z2
(z1−1)(z2−1) 0 0 −1 −1 0
0 0 0 z1
(1−z1)z2
1 −1 0 0
0 0 0 1 z2
(1−z2)z1
0 −1 0
0 0 −1 −1 0 0 0 −Q∗
1
0 0 −1 0 −1 0 0 −Q∗
2
0 0 0 0 0 −Q∗
1
t −Q∗
2
t z∗′ − Q∗













.
We change variablesy1 ↦→y1 −w1
z1z−1
0
1−z1z−1
0
andy2 ↦→y2 −w2
z2z−1
0
1−z2z−1
0
using Lemma 3.1 to obtain
that
Φ Ξ (ℏ) = ⟨I7⟩(y1,y2,x0,w1,w2,x1,x2,x∗),Λ 7 (138)
where
I7 = exp
(
− ℏ
24 + ℏ
8 ftB−1Af − ℏ
1
2
2 xt(B−1ν − 1) − (x1 +x2) ℏ
1
2
2 + (y1 +y2) ℏ
1
2
2
)
×ψℏ
(
y1, 1
1 −z1z−1
0
)
ψℏ
(
y2, 1
1 −z2z−1
0
)
ψℏ(x0,z 0)
N∏
j=1
ψℏ(x∗
j,z ∗
j )
and
Λ 7 =













(z1−1)z2
z1
0 0 1 0 0 0 0
0 (z2−1)z1
z2
0 0 1 0 0 0
0 0 z1+z2−z1z2
(z1−1)(z2−1) 0 0 −1 −1 0
1 0 0 0 1 −1 0 0
0 1 0 1 0 0 −1 0
0 0 −1 −1 0 0 0 −Q∗
1
0 0 −1 0 −1 0 0 −Q∗
2
0 0 0 0 0 −Q∗
1
t −Q∗
2
t z∗′ − Q∗













.
Therefore, we can apply Fubini’s Theorem (Lemma
3.1) with the integration variables
w1,w 2,x 1,x 2, to obtain that
Φ Ξ (ℏ) = ⟨I8⟩(y1,y2,x0,x∗),Λ 8 (139)
38 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WH EELER
where
I8 = exp
(
− ℏ
4 (B−1ν )1(B−1ν )2 − ℏ
24 + ℏ
8 ftB−1Af + ℏ
1
2
2
(
x0
(
(B−1ν )1 + (B−1ν )2
))
− ℏ
1
2
2 y1
(
(B−1ν )1 − 1
)
− ℏ
1
2
2 y2
(
(B−1ν )2 − 1
)
− ℏ
1
2
2 x∗t(
(B−1ν )∗ − (B−1ν )2Q∗
1 − (B−1ν )1Q∗
2 − 1
) )
×ψℏ
(
y1, 1
1 −z1z−1
0
)
ψℏ
(
y2, 1
1 −z2z−1
0
)
ψℏ(x0,z 0)
N∏
j=1
ψℏ(x∗
j,z ∗
j )
and
Λ 8 =





(z1−1)z2
z1
0 −1 −Q∗
1
0 (z2−1)z1
z2
−1 −Q∗
2
−1 −1 z1+z2−z2z2
(z1−1)(z2−1) + 2 Q∗
1 + Q∗
2
−Q∗
1
t −Q∗
2
t Q∗
1
t + Q∗
2
t −Q∗ + Q∗
1Q∗
2 + Q∗
2Q∗
1




.
Using Lemma
6.7, we obtain with respect to the integration variables ˜x = (x0,y 1,y 2,x ∗) and
some c ∈ 1
24 Z that
Φ Ξ (ℏ) = ecℏ⟨I9⟩˜x,Λ 9 (140)
where with ~A,~B and~ν as in Equation ( 130) and
I9 = exp
(ℏ
8
~ft~B−1~A~f − ℏ
1
2
2 ˜xt(~B−1~ν − 1)
) N +2∏
j=0
ψℏ(~x∗
j,~z∗
j ) (141)
and
Λ 9 = diag( ~z′
0,~z′′
1,~z′′
2,~z∗′) −~B−1~A. (142)
□
Lemma 6.7. With the notation used in the proof of the previous Proposition
6.6 we have
Q11 = Q12 = Q22 = 0 and the following equalities:
~B−1~A =




−1 1 1 −Q∗
1 − Q∗
2
1 0 0 Q∗
1
1 0 0 Q∗
2
−Q∗
1
t − Q∗
2
t Q∗
1
t Q∗
2
t Q∗ − Q∗
1
tQ∗
2 − Q∗
2
tQ∗
1



, (143)
~B−1~ν =




−(B−1ν )1 − (B−1ν )2 + 1
(B−1ν )1
(B−1ν )2
(B−1ν )∗ − (B−1ν )1Q∗
2 − (B−1ν )2Q∗
1



, (144)
~ft~B−1~ν = ftB−1ν + ~f0 − 2(B−1ν )1(B−1ν )2. (145)
PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS 39
Proof. The relation B−1A = Q and the fact that the columns of ( a1 |a2 |b∗) are linearly
independent imply that Q11 = Q12 = Q22 = 0. We will prove Equation ( 143) by showing
the identity after multiplying by the invertible matrix ~B. For ( 143) we compute
(
−1 −1 −1 0
0 a1 −b1 −b2 a2 −b1 −b2 b∗
)




−1 1 1 −Q∗
1 − Q∗
2
1 0 0 Q∗
1
1 0 0 Q∗
2
−Q∗
1
t − Q∗
2
t Q∗
1
t Q∗
2
t Q∗ − Q∗
1
tQ∗
2 − Q∗
2
tQ∗
1




=
(
−1 −1 −1 0
a1+a2−2b1−2b2
−b∗Q∗
1
t−b∗Q∗
2
t b∗Q∗
1
t b∗Q∗
2
t (a1−b1)Q∗
1
t+(a2−b2)Q∗
2
t
−b2Q∗
1
t−b1Q∗
2
t+b∗Q∗−b∗Q∗
1
tQ∗
2−b∗Q∗
2
tQ∗
1
)
= ~A.
(146)
For Equation ( 144), we compute
(
−1 −1 −1 0
0 a1 −b1 −b2 a2 −b1 −b2 b∗
)




−(B−1ν )1 − (B−1ν )2 + 1
(B−1ν )1
(B−1ν )2
(B−1ν )∗ − (B−1ν )1Q∗
2 − (B−1ν )2Q∗
1




=
(
−1
ν
)
.
(147)
For Equation (
145), we note that for i = 1, 2 we have
~f ∗tQ∗
i = ( ~B−1~ν )i −~f0 −~f ′′
i (148)
and so
~ft~B−1~ν = ~f0 + (~f ′
1 + ~f2)(B−1ν )1 + (~f1 + ~f ′
2)(B−1ν )2 + ~f ∗t(B−1ν )∗ − 2(B−1ν )1(B−1ν )2 (149)
Then, using the analogous relations between the ﬂattening as given in Equation (
94) for the
shapes, we have ~f ′
1 + ~f2 =f ′
1 = f1 and ~f1 + ~f ′
2 =f ′
2 = f2. □
7. The series of the simplest hyperbolic 41 knot
In this section, we discuss an eﬀective computation of the power se ries Φ Ξ (ℏ) for the
simplest hyperbolic knot, namely the 4 1 knot. This example was studied extensively in [ 11].
From [11, Ex. 2.6], we obtain that the NZ datum Ξ 41 is given by
A =
(
2 2
1 1
)
, B =
(
1 1
1 0
)
, ν =
(
2
1
)
, f =
(
0
1
)
, f ′′ =
(
0
0
)
, (150)
and z1 =z2 =ζ6 =e2πi/6. Therefore, we have
Φ Ξ 41 (ℏ) = e
ℏ
8 ⟨ψℏ(x1,ζ 6)ψℏ(x2,ζ 6)⟩(x1,x2),Λ 0, (151)
where
Λ 0 =
(
ζ6 − 1 −1
−1 ζ6 − 1
)
. (152)
40 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WH EELER
This is a two dimensional formal Gaussian integral which can be simpliﬁe d. Using ζ6 =
1/(1 −ζ6) = 1 −ζ −1
6 and applying a change of coordinates x1 ↦→x1 −ζ6x2, we ﬁnd that
Φ Ξ 41 (ℏ) = e
ℏ
8 ⟨ψℏ(x1 −ζ6x2,ζ 6)ψℏ(x2,ζ 6)⟩(x1,x2),Λ 1, (153)
where
Λ 1 =
(
ζ6 − 1 0
0 2 ζ6 − 1
)
. (154)
We can apply Fubini’s theorem [ 4, Prop.2.13] and Corollary 3.5 to perform the integral over
x1. After renaming the variable x2 by x, we express Φ Ξ 41 (ℏ) by a one-dimensional formal
Gaussian integral
Φ Ξ 41 (ℏ) = e
ℏ
6
⟨
exp
(x
2 ℏ
1
2
)
ψℏ(x,ζ 6)2
⟩
x,2ζ6−1
. (155)
Using the deﬁnition of ψℏ from Equation ( 1) and expanding to O(ℏ5/2), we obtain that
exp
(x
2 ℏ
1
2
)
ψ ℏ(x,ζ 6)2
= 1 +
(1
3x3 +
(
ζ6 − 1
2
)
x
)
ℏ1/2 +
( 1
18x6 +
(1
2ζ6 − 1
4
)
x4 − 7
8x2 +
(
− 1
6ζ6 + 1
6
) )
ℏ
+
( 1
162x9 +
(1
9ζ6 − 1
18
)
x7 − 1
2x5 +
(
− 73
72ζ6 + 77
144
)
x3 +
( 1
12ζ6 + 1
4
)
x
)
ℏ3/2
+
( 1
1944x12 +
( 5
324ζ6 − 5
648
)
x10 − 37
288x8 +
(
− 1337
2160ζ6 + 1357
4320
)
x6
+
( 1
24ζ6 + 1027
1152
)
x4 +
(23
48ζ6 − 5
16
)
x2 − 1
72ζ6
)
ℏ2 +O(ℏ5/2).
(156)
Noting that 2 ζ6 − 1 = √−3, we can then evaluate Equation ( 155) with Equation ( 20) to
obtain that
e− ℏ
4 Φ Ξ 41 (ℏ) = 1 + 11
72√−3 ℏ + 697
2(72√−3)2 ℏ2 +O(ℏ4). (157)
This is in agreement with computations in [ 11, 12, 21]. The one-dimensional formal Gaussian
integral ( 155) gives an eﬀective computation of the series Φ Ξ 41 (ℏ). Indeed, using a pari-gp
program one can compute one hundred coeﬃcients in a few seconds and two hundred coef-
ﬁcients in a few minutes, the ﬁrst few of them are given by
e− ℏ
4 Φ Ξ 41 (ℏ)
= 1 − 11
216
√
−3 ℏ − 697
31104 ℏ2 + 724351
100776960
√
−3 ℏ3 + 278392949
29023764480 ℏ4 − 244284791741
43883931893760
√
−3 ℏ5
− 1140363907117019
94789292890521600 ℏ6 + 212114205337147471
20474487264352665600
√
−3 ℏ7 + 367362844229968131557
11793304664267135385600 ℏ8
− 44921192873529779078383921
1260940134703442115428352000
√
−3 ℏ9 − 3174342130562495575602143407
23109593741473993679123251200 ℏ10 +O(ℏ11).
(158)
Similar to the case of the 4 1, one can obtain one-dimensional formal Gaussian integrals for
the next two simplest hyperbolic knots, the 5 2 and the ( −2, 3, 7)-pretzel knot, whose details
we omit.
PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS 41
