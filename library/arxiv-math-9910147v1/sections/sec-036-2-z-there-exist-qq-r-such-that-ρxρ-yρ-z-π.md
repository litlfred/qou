---
doc_id: arxiv-math-9910147v1
doc_title: "Tensor Products of Principal Unitary Representations of Quantum Lorentz Group and Askey-Wilson Polynomials E. Buffenoir ∗"
section_id: sec-036-2-z-there-exist-qq-r-such-that-ρxρ-yρ-z-π
section_title: "Z, there exist Q,Q ′ ∈ R, such that ∀ρX,ρ Y,ρ Z ∈] − π"
section_number: 2
pages: 19-21
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
---
ℏ, π
ℏ ] :
∀K,
⏐⏐⏐⏐
[dK+n][dK]
[dC ][dC ′] Λ K K +l
A′A (X0X1)Λ K K +m
B′B (Y0Y1)Λ K K +n
C ′C (Z1Z0)
⏐⏐⏐⏐ ≤ QK 3q2K
∀K,
⏐⏐⏐⏐⏐
{ K A
B K +n
K +l
C
}
(0)
{ A′ B′
K K +n
C′
K +m
}
(0)
{ B K
A′ K +n
K +m
K +l
}
(0)
⏐⏐⏐⏐⏐ ≤ Q′. (67)
The series is therefore absolutely convergent and uniformly conve rgent in ρX,ρ Y,ρ Z. From this
last result and using the property that N (A)(q2X1+1,m X )N (D)(q2X1+1,m X )−1Λ BC
AD(X0X1) is a
continuous functions of ρX, the square of the matrix coeﬃcients of the operator Υ
(X0 X1) (Y0 Y1 )
(Z0 Z1) are
continuous functions of the three variables ρX,ρ Y,ρ Z. Note that in the case where A =A′,B =
B′,C =C′ the expression (65) is itself a continuous function of ρX,ρ Y,ρ Z.
We still have to show that the linear map Υ
(X0 X1) (Y0 Y1 )
(Z0 Z1) [l,l ′;v′′] is an intertwiner. We have
Υ
(X0 X1 )(Y0 Y1 )
(Z0 Z1) [l,l ′;v′′] =
=
∑
IJK
(Z0 Z1 )
Π ( uK) † |v′′ ><l ⊗l′|
(X0 X1 )
Π ( uI ) ⊗
(Y0 Y1)
Π ( uJ )h(uIuJuK)
=
∑
IJK
(Z0 Z1 )
Π ( S−1(uK))|v′′ ><l ⊗l′|
(X0 X1 )
Π ( uI ) ⊗
(Y0Y1 )
Π ( uJ )h(uIuJuK)
Using the identity veriﬁed by any Haar measure on a co-quasitriangu lar Hopf algebra A [8, 9]
h(ab) =
∑
(a)
h(ba(2))<µ,a (1) ><µ,a (3) >, ∀a,b ∈A, (68)
and simple transformations using properties of the antipode and of the group-like element µ, we
obtain that Υ
(X0 X1) (Y0 Y1 )
(Z0 Z1 ) [l,l ′;v′′] is related to the operator:
Ξ
(X0 X1 ) (Y0 Y1)
(Z0 Z1 ) [l,l ′;v′′] : V (X0X1) ⊗V (Y0Y1) →V (Z0Z1), (69)
Ξ
(X0 X1 ) (Y0 Y1)
(Z0 Z1 ) [l,l ′;v′′] =
∑
IJK
(Z0 Z1)
Π ( S(uK)µ)|v′′ ><l ⊗l′|
(X0 X1 )
Π ( uI ) ⊗
(Y0 Y1)
Π ( uJ )h(uKuIuJ ),
as follows:
Υ
(X0 X1 )(Y0 Y1 )
(Z0 Z1) [l,l ′;v′′] =∑
C,r Ξ
(X0 X1) (Y0 Y1 )
(Z0 Z1 ) [l,l ′;
C
e r]<
C
µ
C
e r,v ′′>.
As a result it is equivalent to show that Ξ
(X0 X1 )(Y0 Y1 )
(Z0 Z1) [l,l ′;v′′] is an intertwiner operator. This
is a simple consequence of the absolute convergence of the series a nd of the right invariance of
the Haar measure. □
The following proposition gives the link between intertwiners constru cted using the Haar
measure and the reduced elements.
Proposition 11 There exists a real number M
(X0 X1 )(Y0 Y1 )
(Z0 Z1) such that


A’ B’
X0X1 Y0Y1
A B
C’
Z0Z1
C

 = M
(X0X1 ) (Y0 Y1)
(Z0 Z1 )
[ X0X1 Y0Y1
A B
C
Z0Z1
] [ X0X1 Y0Y1
A’ B’
C’
Z0Z1
]
. (70)
19
Proof:
The operator Ξ
(X0 X1) (Y0 Y1 )
(Z0 Z1 ) [l,l ′;v′′] being an intertwiner,the theorem 1 ensures the existence
of a complex number λ(l,l ′;v′′) such that: Ξ
(X0 X1) (Y0 Y1 )
(Z0 Z1 ) [l,l ′;v′′] = λ(l,l ′;v′′)Φ
(X0 X1) (Y0 Y1 )
(Z0 Z1 ) . We
will denote Π =
(X0 X1)
Π , Π ′ =
(Y0 Y1 )
Π , Π ′′ =
(Z0 Z1 )
Π and we have the following sequence of equalities:
λ(l,l ′;v′′) <l ′′|Φ Π Π ′
Π ′′ |v ⊗v′> =
=
∑
IJK
<v ′′|Π ′′((S(eI )µ)∗)|l′′><v ⊗v′|Π(eJ ∗) ⊗ Π ′(eK ∗)|l ⊗l′>h(eIeJeK) =
=
∑
IJK
<v ′′|Π ′′(µS−1(eI ∗))|l′′ ><v ⊗v′|Π(eJ ∗) ⊗ Π ′(eK ∗)|l ⊗l′>h (e∗
Ke∗
Je∗
I ) =
=
∑
IJK
<v ′′|Π ′′(µS−1(eI ))|l′′ ><v ⊗v′|Π(eJ ) ⊗ Π ′(eK)|l ⊗l′>h (S−1(eK)S−1(eJ )S−1(eI )) =
=
∑
IJK
<v ′′|Π ′′(S(eI )µ)|l′′ ><v ⊗v′|Π(eJ ) ⊗ Π ′(eK)|l ⊗l′>h (eIeJeK) =
=λ(v,v ′;l′′) <v ′′|Φ Π Π ′
Π ′′ |l ⊗l′>.
As a result
λ(v,v ′;l′′) = MΠ Π ′
Π ′′ <l ′′|Φ Π Π ′
Π ′′ |v ⊗v′>,
from which we get
∑
IJK
<l ′′|Π ′′(S(eI )µ)|v′′ ><l |Π(eJ )|v ><l′|Π ′(eK)|v′ > h(eIeJeK) =
= MΠ Π ′
Π ′′ <l ′′|Φ Π Π ′
Π ′′ |v ⊗v′><v ′′|Φ Π Π ′
Π ′′ |l ⊗l′>. (71)
Using the relation between the operator Ξ
(X0 X1 ) (Y0 Y1)
(Z0 Z1 ) [l,l ′;v′′] and Υ
(X0 X1) (Y0 Y1 )
(Z0 Z1) [l,l ′;v′′] we obtain
the announced result. □
In order to make a precise connection, later on, between matrix ele ments of ˆΦ[X0X1,Y 0Y1]
and Askey-Wilson polynomials we need an explicit formula for M.
Proposition 12 The normalization factor M
(X0 X1) (Y0 Y1 )
(Z0 Z1) is a positive number and is given by
the following expression:
M
(X0 X1 )(Y0 Y1 )
(Z0 Z1) = |q2(X0−X1+Y0−Y1+Z0−Z1)(1 −q2)(1)2
∞
ν1(2X0+1)2ν1(2Y0 +1)2ν1(2Z0+1)2 | ×
× |ξ(2X1+1)ξ(2Y1+1)ξ(2Z1+1)|
|ξ(X1 +Y1−Z1+1)ξ(X1−Y1+Z1+1)ξ(Y1+Z1−X1 +1)ξ(X1+Y1+Z1 +2)| (72)
where we have deﬁned the function ξ, by ξ(z) = (z)∞(1 −z)∞.
Proof:
We will identify certain asymptotics of the lefthandside and the right handside of (70) in
order to compute the normalization M
(X0 X1 )(Y0 Y1 )
(Z0 Z1) . Let us ﬁrst ﬁnd the behaviour of
f (T ) =


P+T P
X0X1 Y0Y1
P+T P
T
Z0Z1
T

 when T → +∞, P =Y0 −Y1 > 0. (73)
20
It can be seen from the properties (16)(17)(113), that the uniq ue leading term in the explicit
expression :
f (T ) =
∑
KlM n
[dT +n][dK]
[dT ]2 Λ K P +T +l
P +T (X0X1)Λ K M
P (Y0Y1)Λ K T +n
T (Z1Z0)×
×
{ K P +T
P T +n
P +T +l
T
}
(0)
{ K P
P +T T +n
M
T
}
(0)
{ P K
P +T T +n
M
P +T +l
}
(0)
,
is the term corresponding to l =n = 0. The behaviour when T → +∞ off (T ) is therefore given
by
f (T ) ∼q2T (1 −q2)
∑
KM
[dK]
( −P
M
K P
0 −P
)( −P 0
P K
M
−P
)
Λ K M
P (Y0Y1).
The series in the right handside can be exactly computed using the fo rmula (114) proved in the
appendix. We ﬁnally obtain, for P =Y0 −Y1 > 0 :


P+T P
X0X1 Y0Y1
P+T P
T
Z0Z1
T

 ∼T →+∞ q2T (1 −q2) ℏ[d|Y0−Y1|]
2πP(Y0Y1). (74)
From the fact that the righthandside of the last expression is posit ive, and that the right handside
of (70) is in this situation a modulus square we obtain that M
(X0 X1 )(Y0 Y1 )
(Z0 Z1) is a positive number.
Let us now compute the behaviour of the righthandside of (70) for T → +∞,P = mY (this
computation has been done for 0 ≤ mY, but for mY < 0 a similar proof can be done). In the
appendix, we have proved the following result:
[
X0X1 Y0Y1
T +Y0− Y1 Y0− Y1
T
Z0Z1
]
∼e−iπ2Tq−T (Y0+Y1) eiπ( X0−X1
2 )q−Z0Z1
√
[dY0−Y1]×
×ν1(2X1 +1)ν1(2Z0+1)ϕ(2X0,P+T+X0−X1)ϕ(Z1+X1−Y1,Z1−Z0+X1−X0+Y0−Y1)
ϕ(Z0+Z1,T )
×
× ν∞(Y0 +X0−Z0+1)ν∞(Y0 +X0+Z0+2)ν∞(Y0 −X0−Z0)ν∞(Y0 +Z0−X0+1)
q
3
