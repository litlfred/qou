---
doc_id: arxiv-math-9910147v1
doc_title: "Tensor Products of Principal Unitary Representations of Quantum Lorentz Group and Askey-Wilson Polynomials E. Buffenoir ∗"
section_id: sec-035-4-alternative-construction-of-intertwiners-in-te
section_title: "Alternative Construction of Intertwiners in terms of the"
section_number: 4
pages: 17-19
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
---
Quantum Haar Measure
Let us deﬁne the linear map ˆΦ[X0X1,Y 0Y1] : V (X0X1)⊗V (Y0Y1) →
∫ ⊕
d(Z0Z1)H(Z0Z1) where
∀w ∈V (X0X1) ⊗V (Y0Y1), ˆΦ[X0X1,Y 0Y1](w) is the family of functions deﬁned by
ˆΦ[X0X1,Y 0Y1](w)(Z0Z1) = N
(X0 X1) ( Y0 Y1)
(Z0 Z1 ) Φ
(X0 X1 ) (Y0 Y1)
(Z0 Z1) (w), and N
(X0 X1) ( Y0 Y1 )
(Z0 Z1 ) are complex num-
bers depending on X0,X 1,Y 0,Y 1,Z 0,Z 1.
We want to ﬁnd N such that ˆΦ[X0X1,Y 0Y1] is an isometry. As explained in the introduction,
this is a delicate problem which requires another description of the sp ace of intertwiners, where
this isometry property is a direct consequence of Plancherel theo rem.
Theorem 2 Let l ∈ V (X0X1),l ′ ∈ V (Y0Y1),v ′′ ∈ V (Z0Z1), the following operator is well
deﬁned, and is an intertwiner of Uq(sl(2, C)R) module:
Υ
(X0X1 )(Y0 Y1)
(Z0 Z1) [l,l ′;v′′] : V (X0X1) ⊗V (Y0Y1) →V (Z0Z1),
Υ
(X0X1 )(Y0 Y1)
(Z0 Z1) [l,l ′;v′′] =
∑
IJK
(Z0 Z1)
Π ( uK) † |v′′><l ⊗l′|
(X0 X1)
Π ( uI ) ⊗
(Y0 Y1 )
Π ( uJ )h(uIuJuK). (64)
Its matrix elements satisfy the relation:
∑
IJK
(X0 X1)
Π A′,i′
A,i (uI )
(Y0 Y1 )
Π B′,j′
B,j (uJ )
(Z0 Z1 )
Π †C,k
C ′,k′ (uK) h(uIuJuK) =
=
∑
v
( k
C
A B
i j
)
C
µv
k′
( i′ j′
A′ B′
C′
v
) 

A’ B’
X0X1 Y0Y1
A B
C’
Z0Z1
C


with


A’ B’
X0X1 Y0Y1
A B
C’
Z0Z1
C

=
∑
KLM N
[dN ][dK]
[dC ][dC ′ ] Λ KL
A′A(X0X1)Λ KM
B′B(Y0Y1)Λ KN
C ′C (Z1Z0) ×
×
{ K A
B N
L
C
}
(0)
{ A′ B′
K N
C′
M
}
(0)
{ B K
A′ N
M
L
}
(0)
.(65)
This inﬁnite series converges absolutely and uniformly in ρX,ρ Y,ρ Z. Its square is a continuous
function of ρX,ρ Y,ρ Z.
17
Proof:
We will use the convention of summation of repeated up and low small in dices.
∑
IJK
(X0 X1)
Π A′,i′
A,i (uI)
(X0 X1 )
Π B′,j′
B,j (uJ )
(X0 X1 )
Π †C,k
C ′,k′ (uK)h(uIuJuK) =
=
∑
KLK ′M K′′N
Λ KL
A′A(X0X1)
( r s
A′ K
L
t
)( t
L
K A
u i
)
Λ K ′M
B′B (Y0Y1)
( a b
B′ K ′
M
c
)( c
M
K ′ B
d j
)
×
×Λ K ′′N
C ′C (Z1Z0)
(
n
N
C′ K ′′
m p
)(
l k
K ′′ C
N
n
)
C ′
w qk′ (
C ′
w −1)moh(
A′
k i′
r ⊗
K
Eu
s
B′
k j′
a ⊗
K ′
E d
b
C ′
k q
o ⊗
K ′′
E p
l )
=
∑
KLM N
e2iπK [dK]
[dC ′ ] Λ KL
A′A(X0X1)Λ KM
B′B(Y0Y1)Λ KN
C ′C (Z1Z0)
( r s
A′ K
L
t
)( t
L
K A
u i
)( a p
B′ K
M
c
)
×
( c
M
K B
s j
)( n
N
C′ K
m p
)( l k
K C
N
n
)( m
C′
A′ B′
r a
)
(
K
µ−1)u
l
( i′ j′
A′ B′
C′
v
)
C ′
µ v
k′
after the use of formulae (57) and (8)
=
∑
KLM N
e2iπK [dK ]
[dC ′ ] Λ KL
A′A(X0X1)Λ KM
B′B (Y0Y1)Λ KN
C ′C (Z1Z0)
{
A′ B′
K N
C′
M
}
(0)
(
r s
A′ K
L
t
)
×
( t
L
K A
u i
)( n
N
A′ M
r c
)( c
M
K B
s j
)( l k
K C
N
n
)
(
K
µ−1)u
l
( i′ j′
A′ B′
C′
v
)
C ′
µ v
k′
=
∑
KLM N
e2iπK [dK ]
[dC ′ ] Λ KL
A′A(X0X1)Λ KM
B′B (Y0Y1)Λ KN
C ′C (Z1Z0)
{
A′ B′
K N
C′
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
×
(
t
L
K A
u i
)(
n
N
L B
t j
)(
l k
K C
N
n
)
(
K
µ−1)u
l
(
i′ j′
A′ B′
C′
v
)
C ′
µ v
k′
after having used twice the formula (11)
=
∑
KLM N
e2iπK [dK ]
[dC ′ ] Λ KL
A′A(X0X1)Λ KM
B′B (Y0Y1)Λ KN
C ′C (Z1Z0)
{ A′ B′
K N
C′
M
}
(0)
{ B K
A′ N
M
L
}
(0)
×e2iπ(N −C)[dN ]
[dC ]
(
l t
K L
A
i
)(
n
N
L B
t j
)(
k
C
K N
l n
)
(
K
µ−1)u
l
(
i′ j′
A′ B′
C′
v
)
C ′
µ v
k′
= righthandside of (65),
where we have used formulae (7) and (11) to conclude.
This proof holds true as soon as we have shown that these series ar e absolutely convergent.
Proof of the convergence of the last series can be obtained using a symptotic properties of coeﬃ-
cients Λ BC
AD, as well as asymptotic properties of 6 j(0). Indeed, using the selection rules of 6 j(0),
we know that in the four sums
∑
Klmn
[dK+n][dK ]
[dC ][dC ′ ] Λ K K +l
A′A (X0X1)Λ K K +m
B′B (Y0Y1)Λ K K +n
C ′C (Z1Z0) ×
×
{
K A
B K +n
K +l
C
}
(0)
{
A′ B′
K K +n
C′
K +m
}
(0)
{
B K
A′ K +n
K +m
K +l
}
(0)
, (66)
18
for a ﬁxed K, the range of the sum over l,m,n is ﬁnite and ﬁxed by |l| ≤ min(A,A ′), |m| ≤
min(B,B ′), |n| ≤ min(C,C ′), |l −n| ≤ B, |n −m| ≤ A′. Thus, in order to show the abso-
lute convergence of this series, it is suﬃcient to bound the general term in K by a geometric
series. This can be proved using the behaviour of the coeﬃcients Λ KK +l
AD when K is large,
derived in the appendix. Precisely, using (111) and (16)(17), we ha ve the following property:
∀l,m,n,A,B,C,A ′,B ′,C ′ ∈ 1
