---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-011-62-the-case-of-b-with-nullity-one
section_title: "The case of B with nullity one"
section_number: 6.2
pages: 27-33
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
doc_brief: "PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS — We prove that a formal power series associated to an ideally triangu lated cusped hyperbolic 3-manifold (together with some further"
---
assumption that the matrix B has nullity 1. In this case, starting from the series Φ Ξ (ℏ), there
are three intermediate formulas (shown as bullets) in Equation ( 98) that eventually iden-
tify the result with Φ ~Ξ (ℏ). The intermediate formulas involve a Fourier transform (adding
one integration variable), a pentagon (adding a second variable), a n inverse Fourier trans-
form (adding a third), and an application of Fubini’s theorem that rem oves two integration
variables. The detailed computation is given in the next proposition.
Proposition 6.4. IfB has rank N + 1 then Φ Ξ (ℏ) is invariant under the 2–3 Pachner move
given in Equation (
98).
28 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WH EELER
Proof. Following the discussion above we can assume that rank( b1 |b2 |b∗) = rank(b2 |b∗) =
N + 1. Then by [ 11, Lem.A.3], the matrix ( a1 |b2 |b∗) has full rank and we can apply a quad
move to the ﬁrst columns of ( A |B) to obtain
A = ( −b1 |a2 |a∗), B = ( a1 −b1 |b2 |b∗), ν = ν −b1, (111)
where B has full rank. The proof will use the following sequence of intermedia te matrices
(A | B | ν ) =
(
−b1 a2 a∗ a1 −b1 b2 b∗ ν −b1
)
q−1
1 × 1
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
1 ×q1 × 1
(~A |~B |~ν ) =
(
−1 −1 0 0 −1 −1 1 0 0
a1 +a2 −b1 −b2 −b1 a2 −b1 a∗ 0 a1 −b1 −b2 b2 b∗ ν −b1
)
(112)
where B and ~B are invertible. With x = (x1,x 2,x ∗) and z = (z1,z 2,z ∗) vectors of size N + 2,
Φ Ξ (ℏ) is deﬁned by
Φ Ξ (ℏ) = ⟨I0⟩(x1,x2,x∗),Λ 0 (113)
where with f = (f ′
1,f 2,f ∗)
I0 = exp
(ℏ
8 ftB−1Af − ℏ
1
2
2 x(B−1ν − 1)
)
ψℏ
(
x1, 1
1 −z1
)
ψℏ(x2,z 2)
N∏
j=1
ψℏ(x∗
j,z ∗
j )
and
Λ 0 = diag( z′′
1,z ′
2,z ∗′) − Q.
We apply Corollary
3.5 to the ψℏ with argument x1 and introduce a new variable w1 to
obtain
Φ Ξ (ℏ) = ⟨I1⟩(w1,x1,x2,x∗),Λ 1 (114)
where
I1 = exp
( ℏ
24 + ℏ
8 ftB−1Af − ℏ
1
2
2 x(B−1ν − 1) −x1
ℏ
1
2
2
)
×ψℏ
(
w1 −x1(1 −z−1
1 ),z 1
)
ψℏ(x2,z 2)
N∏
j=1
ψℏ(x∗
j,z ∗
j )
PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS 29
and
Λ 1 =
( z1
1−z1
0
0 Λ
)
.
We substitute w1 ↦→w1 +x1(1 −z−1
1 ) and obtain, from Lemma 3.1, that
Φ Ξ (ℏ) = ⟨I2⟩(w1,x1,x2,x∗),Λ 2 (115)
where
I2 = exp
( ℏ
24 + ℏ
8 ftB−1Af − ℏ
1
2
2 x(B−1ν − 1) −x1
ℏ
1
2
2
)
ψℏ(w1,z 1)ψℏ(x2,z 2)
N∏
j=1
ψℏ(x∗
j,z ∗
j )
and with Q11 = 0 from Lemma
6.5
Λ 2 =





z1
1−z1
−1 0 0
−1 0 −Q12 −Q∗
1
0 −Q12
1
1−z2
− Q22 −Q∗
2
0 −Q∗
1
t −Q∗
2
t z∗′ − Q∗




.
We apply the pentagon identity of Theorem
3.6 to the ψh with arguments w1 and x1 and
obtain, with the new integration variable x0, that
Φ Ξ (ℏ) = ⟨I3⟩(x0,w1,x1,x2,x∗),Λ 3 (116)
where
I3 = exp
(ℏ
8 ftB−1Af − ℏ
1
2
2 x(B−1ν − 1) −x1
ℏ
1
2
2
)
ψℏ
(
−x0 −x2 + w1z2 +x2z1
z0
,z 1z−1
0
)
ψℏ
(
x0 +w1 +x2 −w1z2 +x2z1
z0
,z 0
)
ψℏ
(
−x0 −w1 + w1z2 +x2z1
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

(z1+z2−z1z2)2
(z1−1)z1(z2−1)z2
0 0 0 0
0 z1
1−z1
−1 0 0
0 −1 0 −Q12 −Q∗
1
0 0 −Q12
1
1−z2
− Q22 −Q∗
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


.
We use Lemma
3.1 to change the variables x0 ↦→x0 −w1 −x2 + w1z2+x2z1
z0
and obtain that
Φ Ξ (ℏ) = ⟨I4⟩(x0,w1,x1,x2,x∗),Λ 4 (117)
where
I4 = exp
(ℏ
8 ftB−1Af − ℏ
1
2
2 x(B−1ν − 1) −x1
ℏ
1
2
2
)
×ψℏ(−x0 +w1,z 1z−1
0 )ψℏ(x0,z 0)ψℏ(−x0 +x2,z 2z−1
0 )
N∏
j=1
ψℏ(x∗
j,z ∗
j )
30 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WH EELER
and
Λ 4 =
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
(z1−1)z2
0 z1+z2−z1z2
z1(z2−1) 0
z1+z2−z1z2
(z1−1)z2
z1
z2(1−z1) −1 1 0
0 −1 0 −Q12 −Q∗
1
z1+z2−z1z2
z1(z2−1) 1 −Q12 −Q22 − z1+z2−z1z2
z1(z2−1) −Q∗
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



.
We substitute w1 ↦→w1 +x0 and x2 ↦→x2 +x0 to obtain, with Lemma
3.1, that
Φ Ξ (ℏ) = ⟨I5⟩(x0,w1,x1,x2,x∗),Λ 5 (118)
where
I5 = exp
(ℏ
8 ftB−1Af − ℏ
1
2
2 x(B−1ν − 1) − ℏ
1
2
2 x0(B−1ν 2 − 1) −x1
ℏ
1
2
2
)
×ψℏ(w1,z 1z−1
0 )ψℏ(x0,z 0)ψℏ(x2,z 2z−1
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
−Q22 + 1
(z1−1)(z2−1) 0 −1 − Q12 1 − Q22 −Q∗
2
0 z1
z2(1−z1) −1 1 0
−1 − Q12 −1 0 −Q12 −Q∗
1
1 − Q22 1 −Q12 −Q22 + z1+z2−z1z2
z1(z2−1) −Q∗
2
−Q∗
2
t 0 −Q∗
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
3.4 to ψℏ(w1,z 1z−1
0 ) we obtain, with a new
integration variable y1, that
Φ Ξ (ℏ) = e− ℏ
24 ⟨I6⟩(y1,x0,w1,x1,x2,x∗),Λ 6 (119)
where
I6 = exp
(
− ℏ
24 + ℏ
8 ftB−1Af − ℏ
1
2
2 x(B−1ν − 1)
− ℏ
1
2
2 x0((B−1ν )2 − 1) −x1
ℏ
1
2
2 +
(
y1 + w1z1z−1
0
1 −z1z−1
0
) ℏ
1
2
2
)
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
ψℏ(x0,z 0)ψℏ(x2,z 2z−1
0 )
N∏
j=1
ψℏ(x∗
j,z ∗
j )
PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS 31
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

(z1−1)z2
z1
0 0 0 0 0
0 −Q22 + 1
(z1−1)(z2−1) 0 −1 − Q12 1 − Q22 −Q∗
2
0 0 z1
z2(1−z1) −1 1 0
0 −1 − Q12 −1 0 −Q12 −Q∗
1
0 1 − Q22 1 −Q12 −Q22 + z1+z2−z1z2
z1(z2−1) −Q∗
2
0 −Q∗
2
t 0 −Q∗
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

.
We change variables y1 ↦→y1 −w1
z1z−1
0
1−z1z−1
0
using Lemma 3.1 and obtain that
Φ Ξ (ℏ) = ⟨I7⟩(y1,x0,w1,x1,x2,x∗),Λ 7 (120)
where
I7 = exp
(
− ℏ
24 + ℏ
8 ftB−1Af − ℏ
1
2
2 x(B−1ν − 1) − ℏ
1
2
2 x0((B−1ν )2 − 1) −x1
ℏ
1
2
2 +y1
ℏ
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
ψℏ(x0,z 0)ψℏ(x2,z 2z−1
0 )
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

(z1−1)z2
z1
0 1 0 0 0
0 −Q22 + 1
(z1−1)(z2−1) 0 −1 − Q12 1 − Q22 −Q∗
2
1 0 0 −1 1 0
0 −1 − Q12 −1 0 −Q12 −Q∗
1
0 1 − Q22 1 −Q12 −Q22 + z1+z2−z1z2
z1(z2−1) −Q∗
2
0 −Q∗
2
t 0 −Q∗
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

.
Therefore, we can apply Fubini’s Theorem (Lemma
3.1) with the integration variables w1,x 1,
to obtain that
Φ Ξ (ℏ) = ⟨I8⟩(y1,x0,x2,x∗),Λ 8 (121)
where
I8 = exp
(
− ℏ
24 + ℏ
8 ftB−1Af − ℏ
1
2
2 (x0((B−1ν )2 − 1) +y1((B−1ν )1 − 1)
+x2((B−1ν )2 + (B−1ν )1 − 1) +x∗((B−1ν )∗ − 1))
)
×ψℏ
(
y1, 1
1 −z1z−1
0
)
ψℏ(x0,z 0)ψℏ(x2,z 2z−1
0 )
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
−Q12 − 1 −Q12 −Q∗
1
−Q12 − 1 1
(z1−1)(z2−1) − Q22 −Q12 − Q22 −Q∗
2
−Q12 −Q12 − Q22 −2Q12 − Q22 + z1+z2−z1z2
z1(1−z2) −Q∗
1 − Q∗
2
−Q∗
1
t −Q∗
2
t −Q∗
1
t − Q∗
2
t z∗′ − Q∗




 .
32 STA VROS GAROUF ALIDIS, MATTHIAS STORZER, AND CAMPBELL WH EELER
Using Lemma 6.5 we obtain, with respect to the integration variables ˜x = (x0,y 1,x 2,x ∗) and
some c ∈ 1
24
/CI , that
Φ Ξ (ℏ) = ecℏ⟨I9⟩˜x,Λ 9 (122)
where
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
j )
and with ~A, ~B as in (
112)
Λ 9 = diag( ~z′
0,~z′′
1,~z′
2,~z∗′) −~B−1~A.
□
Lemma 6.5. With the notation used in the previous proof of Proposition 6.4 we have
Q11 = 0 and the following equalities:
~B−1~A =




Q22 Q12 + 1 Q12 + Q22 Q∗
2
Q12 + 1 0 Q12 Q∗
1
Q12 + Q22 Q12 2Q12 + Q22 Q∗
1 + Q∗
2
Q∗
2
t Q∗
1
t Q∗
1
t + Q∗
2
t Q∗



, (123)
~B−1~ν =




(B−1ν )2
(B−1ν )1
(B−1ν )1 + (B−1ν )2
(B−1ν )∗



, (124)
~ft~B−1~ν = ftB−1ν. (125)
Proof. Similarly to the proof of Lemma
6.3 we will proof Equations ( 123) and ( 124) by
showing that both sides are equal after multiplying by the invertible m atrix ~B. Using
Q = B−1A and the fact that ( a1 |b2 |b∗) are linearly independent we conclude Q11 = 0. For
(123) we compute
(
−1 −1 1 0
0 a1 −b1 −b2 b2 b∗
)




Q22 Q12 + 1 Q12 + Q22 Q∗
2
Q12 + 1 0 Q12 Q∗
1
Q12 + Q22 Q12 2Q12 + Q22 Q∗
1 + Q∗
2
Q∗
2
t Q∗
1
t Q∗
1
t + Q∗
2
t Q∗




=
(
−1 −1 0 0
(a1−b1)Q12
+b2Q22+b∗Q∗
2
t b2Q12+b∗Q∗
1
t b2Q12+b∗Q∗
1
t+
(a1−b1)Q12+b2Q22+b∗Q∗
1
t
(a1−b1−b2)Q∗
1
+b2(Q∗
1+Q∗
2)+b∗Q∗
)
= ~A
(126)
PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS 33
For (124) we have
(
−1 −1 1 0
0 a1 −b1 −b2 b2 b∗
)




(B−1ν )2
(B−1ν )1
(B−1ν )1 + (B−1ν )2
(B−1ν )∗




=
(
0
ν
)
(127)
For Equation (
125), we have
~ft




(B−1ν )2
(B−1ν )1
(B−1ν )1 + (B−1ν )2
(B−1ν )∗




= ( ~f ′
1 + ~f2)(B−1ν )1 + (~f0 − ~f2)(B−1ν )2 + ~f ∗(B−1ν )∗.
(128)
Then, using the analogous relations between the ﬂattening as given in Equation (
94) for the
shapes, we have ~f ′
1 + ~f2 =f ′
1 = f1 and ~f0 − ~f2 =f2 = f2. □
