---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-008-5-invariance-under-the-choice-of-quad
section_title: "Invariance under the choice of quad"
section_number: 5
pages: 19-23
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
doc_brief: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS — We prove that a formal power series associated to an ideally triangu lated cusped hyperbolic 3-manifold (together with some further choices)"
---
The deﬁnition of the series Φ Ξ (ℏ) requires some choices, some of which were described and
dealt with in the previous Section 4. What remains to complete the proof of Theorem 1.1 is
the independence of Φ Ξ (ℏ) under the choice of a nondegenerate quad, and the independenc e
under the 2–3 Pachner moves that connect two ideal triangulation s.
In this section, we will prove that Φ Ξ (ℏ) is independent of the choice of a nondegenerate
quad. Recall that to each pair of opposite edges of an ideal tetrah edron there is an associated
variable called a shape variable. When deﬁning Neumann–Zagier data ( see Section 2.2), we
must choose an edge for each tetrahedron, which associates one of these shapes. There
are three possible choices, which leads to the action on /CI /3 /CI on the each column of the
Neumann–Zagier data. All in all, for a triangulation with N tetrahedra, this leads to 3 N
choices on of Neumann–Zagier data. On the other hand, the deﬁnit ion of the series Φ Ξ (ℏ)
requires a choice of a nondegenerate quad, i.e., one for which det( B) ⁄= 0 (such quads always
exist [ 11, Lem.A.3]). In this section, we will show that any of the 3 N choices of quad with
det(B) ⁄= 0 lead to the same Φ Ξ (ℏ) series.
Theorem 5.1. The series Φ Ξ (ℏ) is independent of the choice of a nondegenerate quad.
Proof. Fix two non–degenerate NZ data Ξ = ( A,B,ν,z,f,f ′′) and ~Ξ = ( ~A,~B,~ν,~z,~f, ~f ′′)
related by a quad change of the same ideal triangulation. The nonde generacy assumption
implies that det(B) ⁄= 0 and det( ~B) ⁄= 0.
After reordering the tetrahedra (which does not change the Φ Ξ (ℏ) series, as follows from
Section 4), we can assume that ~Ξ is obtained by applying a change in quad that ﬁxes the
ﬁrst N0 shapesz(0), replaces the next N1 shapes z(1) byz′(1) and replaces the next N2 shapes
z(2) byz′(2). (Recall that z′ = 1/(1 −z) and z′′ = 1 − 1/z).
This partitions the shapes z = (z(0),z (1),z (2)) into three sets of size N0,N 1,N 2 and the
matrices A and B into three block matrices Ai and Bi of size N ×Ni for i = 0, 1, 2
A = ( A0 |A1 |A2), B = ( B0 |B1 |B2), (71)
and similarly for the ﬂattening f = (f (0),f (1),f (2)) and f ′′ = (f ′′(0),f ′′(1),f ′′(2)). After the
quad moves, the corresponding matrices and vectors are given by
˜A = ( A0 | −B1 | −A2 +B2), ˜B = ( B0 |A1 −B1 | −A2),
˜ν = ν −B11 −A21, ˜z = ( z(0),z ′(1),z ′′(2)),
˜f = ( f (0), 1 −f (1) −f ′′(1),f ′′(2)), ˜f ′′ = ( f ′′(0),f (2), 1 −f (2) −f ′′(2)).
(72)
We also partition the vector of formal Gaussian integration variable sx = (x(0),x (1),x (2)), as
well as the symmetric matrix Q :=B−1A
Q =


Q00 Q01 Q02
Qt
01 Q11 Q12
Qt
02 Qt
12 Q22

 . (73)
With the above notation, we have
Φ Ξ (ℏ) = ⟨I0⟩x,Λ 0 (74)
20 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WH EELER
where
I0 = exp
(ℏ
8ftB−1Af − ℏ
1
2
2 xt(B−1ν − 1)
) N∏
j=1
ψℏ(xj,zj)
and
Λ 0 = diag( z′) −Q.
Applying the ﬁrst quad move as in Theorem 3.4 to the ψℏ with arguments of z(1) and the
second quad move as in its Corollary 3.5 to the ψℏ with arguments z(2), we obtain that
Φ Ξ (ℏ) = ⟨I1⟩(x,y,w),Λ 1 (75)
where
I1 = exp
(ℏ
8ftB−1Af − ℏ
1
2
2 x(0)t
(B−1ν − 1)(0) −N1ℏ
24 − ℏ
1
2
2 x(1)t
(B−1ν − 1)(1)
+
N1∑
j=1
(
yj + x(1)
j z(1)
j
1 −z(1)
j
) ℏ
1
2
2 + N2ℏ
24 − ℏ
1
2
2 x(2)t
(B−1ν − 1)(2) −
N2∑
j=1
x(2)
j
ℏ
1
2
2
)
×
N0∏
j=1
ψℏ(x(0)
j ,z (0)
j )
N1∏
j=1
ψℏ
(
yj + x(1)
j z(1)
j
1 −z(1)
j
, 1
1 −z(1)
j
) N2∏
j=1
ψℏ
(
wj − x(2)
j
1 −z(2)
j
, 1 −z(2)
j
−1)
,
y and w are vectors of size N1 and N2, respectively, and
Λ 1 =


Λ 0 0
0 diag( z′′(1)) 0
0 0 diag( z(2)) −I

 .
Making the change of variables yj ↦→yj −
x(1)
j z(1)
j
1−z(1)
j
andwj ↦→wj +
x(2)
j
1−z(2)
j
and using Lemma 3.1
we obtain that
Φ Ξ (ℏ) = ⟨I2⟩(x,y,w),Λ 2 (76)
where
I2 = exp
(ℏ
8ftB−1Af − ℏ
1
2
2 x(0)t
(B−1ν − 1)(0) − N1ℏ
24 − ℏ
1
2
2 x(1)t
(B−1ν − 1)(1)
+yt1 ℏ
1
2
2 + N2ℏ
24 − ℏ
1
2
2 x(2)t
(B−1ν)(2)
)
×
N0∏
j=1
ψℏ(x(0)
j ,z (0)
j )
N1∏
j=1
ψℏ
(
yj, 1
1 −z(1)
j
) N2∏
j=1
ψℏ
(
wj, 1 −z(2)
j
−1)
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
diag(z′(0)) −Q00 −Q01 −Q02 0 0
−Qt
01 I −Q11 −Q12 I 0
−Qt
02 −Qt
12 −Q22 0 −I
0 I 0 diag( z′′(1)) 0
0 0 −I 0 diag( z(2)) −I








.
PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS 21
Note that x(1) and x(2) do not appear in the arguments of ψℏ. Moreover, since BQ =A, we
see that
B


I Q 01 Q02
0 Q11 −I Q 12
0 Qt
12 Q22




I 0 0
0 I 0
0 0 −I

 = ( B0 |A1 −B1 | −A2) = ~B, (77)
which implies that
det
(
Q11 −I Q 12
Qt
12 Q22
)
⁄= 0, and
(
Q11 −I Q 12
Qt
12 Q22
) −1
=
(
0 I 0
0 0 −I
)
~B−1B


0 0
I 0
0 I

 .
(78)
Therefore, we can apply Fubini’s Theorem (Lemma
3.1) with the integration variables
x(1),x (2), and use Lemma 5.2 and the equality Qf +f ′′ =B−1ν to obtain that
Φ Ξ (ℏ) = ecℏ⟨I3⟩~x,Λ 3. (79)
where~x = (x(0),y,w ),c ∈ 1
24
/CI
I3 = exp
(ℏ
8
~ft~B−1~A~f − ℏ
1
2
2 ~xt(~B−1~ν − 1)
) N∏
j=1
ψℏ(~xj,~zj)
and
Λ 3 = diag( ~z′) − ~B−1~A.
The right hand side of Equation ( 79) is exactly equal to ecℏΦ ~Ξ (ℏ), completing the proof of
Theorem 5.1. □
Lemma 5.2. With the notation as in the proof of Theorem 5.1, we have the following
identities
~B−1~A =


Q00 0 0
0 0 0
0 0 −I

 +


Q01 Q02
−I 0
0 I


(
Q11 −I Q 12
Qt
12 Q22
) −1(
Qt
01 −I 0
Qt
02 0 I
)
, (80)
~B−1~ν − 1 =


I 0 0
0 0 0
0 0 0

 (B−1ν − 1) −


0
1
0


+


−Q01 −Q02
I 0
0 −I


(
Q11 −I Q 12
Qt
12 Q22
) −1((
0 I 0
0 0 I
)
B−1ν −
(
1
0
))
(81)
and for some d ∈
/CI
~f~B−1~ν = ftB−1ν +d
−
(
(B−1ν)t


0 0
I 0
0 I

 −
(1 0 ) ) (
Q11 −I Q 12
Qt
12 Q22
) −1((
0 I 0
0 0 I
)
B−1ν −
(
1
0
))
.
(82)
22 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WH EELER
Proof. We will show that boths sides of Equation ( 80) and Equation ( 81) are equal after
multiplying by the invertible matrix ~B. Denote
(
Q11 −I Q 12
Qt
12 Q22
) −1
=
(
Γ 11 Γ 12
Γt
12 Γ 22
)
, (83)
and note that
~B


−Q01 −Q02
I 0
0 −I


( Q11 −I Q 12
Qt
12 Q22
) −1
= ~B


−Q01Γ 11 −Q02Γ t
12 −Q01Γ 12 −Q02Γ 22
Γ 11 Γ 12
−Γ t
12 −Γ 22


= ( −B0Q01Γ 11 −B0Q02Γ t
12 + (A1 −B1)Γ 11 +A2Γ t
12 | − B0Q01Γ 12 −B0Q02Γ 22 + (A1 −B1)Γ 12 +A2Γ 22)
= (( B1(Q11 −I) +B2Qt
12)Γ 11 + (B1Q12 +B2Q22)Γ t
12 | (B1(Q11 −I) +B2Qt
12)Γ 12 + (B1Q12 +B2Q22)Γ 22)
= ( B1 |B2).
(84)
Therefore, since
~B


Q00 0 0
0 0 0
0 0 −I

 = ( B0Q00 | 0 | −A2), (85)
we see that multiplying the right hand side of Equations (
80) on the left by ~B we have
(B0Q00 +B1Qt
01 +B2Qt
02 | −B1 | −A2 +B2) = ~A, (86)
which completes the proof of Equation (
80). Similarly, since
~B


I 0 0
0 0 0
0 0 0

 (B−1ν − 1) − ~B


0
1
0

 = B0(B−1ν)(0) −B01 −A11 +B11 (87)
we see that multiplying the right hand side of Equations (
81) on the left by ~B we have
B0(B−1ν)(0) −B01 −A11 +B11 +B1(B−1ν)(1) −B11 +B2(B−1ν)(2) = ~ν − ~B1, (88)
which completes the proof of Equation ( 81). For Equation ( 82), we will compute the three
terms that appear there. Firstly, use Equation ( 81) to obtain that
(
0 I 0
0 0 −I
)
(~B−1~ν − 1) = −
(
1
0
)
+
(
Q11 −I Q 12
Qt
12 Q22
) −1((
0 I 0
0 0 I
)
B−1ν −
(
1
0
))
, (89)
to obtain that

(B−1ν)t


0 0
I 0
0 I

 −
(1 0 )


((
0 I 0
0 0 −I
)
(~B−1~ν − 1) +
(
1
0
))
= (( B−1ν)(1)t
− 1)(~B−1~ν)(1) − (B−1ν)(2)t
(~B−1~ν)(2) + (B−1ν)(2)t
1.
(90)
PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS 23
Secondly, expanding out
~ft~B−1~ν = f (0)(~B−1~ν)(0) + (1 −f (1) −f ′′(1))(~B−1~ν)(1) +f ′′(2)(~B−1~ν)(2)
= f (0)(~B−1~ν)(0)
+ (1 −f (1) − (B−1ν)(1)t
+f (0)Q01 +f (1)Q11 +f (2)Qt
12)(~B−1~ν)(1)
+ ((B−1ν)(2)t
−f (0)Q02 −f (1)Q12 −f (2)Q22)(~B−1~ν)(2).
(91)
Finally, using Equation (
77) we obtain that
ftB−1ν −f (1)1 +f ′′(2)1 = ftB−1ν −f (1)1 −ftQ(0, 0, 1)t + (B−1ν)(2)t
1
= ftB−1~ν + (B−1ν)(2)t
1
= f (0)(~B−1~ν)(0)
+ (f (0)Q01 +f (1)(Q11 −I) +f (2)Qt
12)(~B−1~ν)(1)
− (f (0)Q02 +f (1)Q12 +f (2)Q22)(~B−1~ν)(2) + (B−1ν)(2)t
1.
(92)
□
