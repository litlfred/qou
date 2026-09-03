---
doc_id: arxiv-math-9910147v1
doc_title: "Tensor Products of Principal Unitary Representations of Quantum Lorentz Group and Askey-Wilson Polynomials E. Buffenoir ∗"
section_id: sec-046-52-r-matrix-in-the-tensor-product-of-inﬁnite-dim
section_title: "R-matrix in the Tensor Product of Inﬁnite dimensional Re presen-"
section_number: 5.2
pages: 24-26
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
doc_brief: "Tensor Products of Principal Unitary Representations of Quantum Lorentz Group and Askey-Wilson Polynomials E. Buffenoir ∗ — We study the tensor product of principal unitary representa tions of the"
---
tations
In this section we will compute the R-matrix in the tensor product of two irreducible inﬁnite
dimensional representations (
(X0 X1 )
Π ⊗
(Y0 Y1 )
Π ). We will in particular show that the expression of
(
(X0 X1 )
Π ⊗
(Y0 Y1)
Π )( R) is an operator which domain contains all the vectors of the form
A
em(X0X1)⊗
B
e n(Y0Y1), and more precisely we have the following proposition:
Proposition 13 The expression of the R matrix of Uq(sl(2, C)R) represented on
(X0 X1)
V ⊗
(Y0 Y1)
V
is given by the following action:
(
(X0 X1)
Π ⊗
(Y0 Y1)
Π )( R)(
B
e m ⊗
C
e n) =
∑
DF
B
e j ⊗
F
e p
( p j
F B
D
x
)( x
D
B C
m n
)
Λ BD
F C (X0,X 1). (84)
In particular this expression is a ﬁnite sum although the uni versal formula for R is an inﬁnite
sum.
Proof:
The element
A
L are multipliers of ˜Uq(sl(2, C)R) and we have the trivial relation
A
L(±)i
j =
∑ ⊕
B
AB
R ik
jl
B
X l
k. The R matrix of Uq(sl(2, C)R) is written as: R = ∑
A
A
X i
j ⊗ 1 ⊗ 1 ⊗
A
g j
i. From
the expression of a representation ˜Π of ˜Uq(sl(2, C)R), associated to ( X0,X 1) a straightforward
computation of the representation of the R-matrix gives the form ula of the statement. □
Remark. This situation is in sharp contrast with the case of SUq(1, 1) for q real. The
structure of Hopf algebra on Uq(su(1, 1)) is the same as Uq(su(2)), the only diﬀerence is in
the deﬁnition of the star structure: J ⋆
z = Jz,J ⋆
+ = −J−,J ⋆
− = −J+. It is easy to classify the
irreducible unitary representations, the principal unitary repres entation of U(su(1, 1)) being now
easily quantized as follows:
Jz.em =mem J+.em = [m −τ +ǫ]em+1 J−.em = −[m +τ +ǫ]em+1
where as usual ǫ ∈ {0, 1
2 },τ =iν − 1
2,ν ∈ R, andem is an orthonormal basis of the representation.
The universal R matrix is still formally deﬁned by R =q2Jz⊗Jze(q−q−1) ( qJz J+⊗J−q−Jz )
q−1 . It is easy
to see that (π⊗π′)(R)(em⊗e′
n) has no meaning in the l2 sense except in the trivial case where q =
1. Indeed a straightforward computation shows that a formal expa nsion of (π ⊗π′)(R)(em ⊗e′
n)
gives (π⊗π′)(R)(em⊗e′
n) =∑ +∞
p=0ap(em+p⊗e′
n−p) withap ∼ (q−q−1)γq −2p2+αp+β for 0<q < 1
with γ ⁄= 0.
24
5.3 Connection with Askey-Wilson Polynomials.
In the sequel, we will show that we can reexpress N
(X0X1 ) ( Y0 Y1)
(Z0 Z1 )
[ X0X1 Y0Y1
A B
C
Z0Z1
]
in terms
of q-Racah polynomials and Askey-Wilson polynomials, and that the re lation (81) is an orthog-
onality property mixing q-Racah polynomials and Askey-Wilson polynom ials in a non trivial
way.
Lemma 3 The following three identities are satisﬁed:
1)
[ X0X1 Y0Y1
A B
C
Z0Z1
]
=ψ2
[ X1X0 Y1Y0
A B
C
Z1Z0
]
2)
[ X1X0 Y1Y0
A B
C
Z1Z0
]
=ψ3
[ X1X0 Y1Y0
A B
C
Z1Z0
]
3)
[
X1X0 Y1Y0
A B
C
Z1Z0
]
=e−iπB√
[dB]
∑
X2
{
T Z 1
Y0 X0
Z0
X2
}
(3)
{
C B
X1 X0
A
X2
}
(1)
×
×
{
B Y 1
Z1 X2
Y0
X1
}
(3)
v1/4
A v1/2
X2
v1/4
B v1/4
C v1/4
X0v1/4
X1
(85)
whereψ2 =eiπ(B+C+mX +A), and ψ3 is such that
ψ1ψ2ψ3 =eiπ(mX +mY −mZ )ϕ(2X1+1,−1)ϕ(2Y1+1,−1)ϕ(2Z1+1,−1)
Proof:
The identity 1) follows from a very simple computation. The identity 2) follows from the
use of propositions (2) and (9). Identity 3) is a direct consequenc e of a Racah and a pentagonal
equation on 6j(3) symbols. □
Using these identities theorem (3) can be reformulated as follows
Proposition 14
∫
d(Z0Z1)Γ
(X0 X1)(Y0 Y1 )
(Z0 Z1)
{ A Z 1
Y0 X0
Z0
X2
}
(3)
{ A Z 1
Y0 X0
Z0
X3
}
(3)
{ B Y 1
Z1 X2
Y0
X1
}
(3)
{ C Y 1
Z1 X3
Y0
X1
}
(3)
=
=δX2,X3δB,CY (1)
(A,X0−X2)Y (1)
(B,X1−X3)Y (1)
(B,Y0−Y1). (86)
with
Γ
(X0 X1 )(Y0 Y1 )
(Z0 Z1 ) = q2Z0−2Z1+2Y0−2Y1 (1)2
∞(1 −q2)[dB]
(2X1 +1)1(2Y0 +1)1(2Z0+1)1
×
× ξ(2X1 +1, 2Y1+1, 2Z1+1)
ξ(Y1 +X1−Z1+1,X 1+Z1−Y1+1,Y 1+Z1−X1+1,X 1+Y1+Z1+2) (87)
Proof:
Straightforward using a Racah-Wigner symmetry on 6 j(3) and an orthogonality relation on
6j(1) symbols. □
Theorem 5 Using the notations (102) we have
√
P(Z0Z1)
√
Γ
(X0 X1)(Y0 Y1)
(Z0 Z1)
{
B Y 1
Z1 X2
Y0
X1
}
(3)
=
√
ℏ
√
w(AW )(z;a,b,c,d )
h(AW )
n (a,b,c,d )
p(AW )
n (τ (z);a,b,c,d )(88)
with n =B +Y0 −Y1,a =q2X1+2Y1+3,b =q2Y1−2X1+1,c =q2X2−2Y0+1,d =q−2Y0−2X2−1, 2z =
2Z1 + 1.
25
Proof:
Using two Sears transformations we can turn the parameters of t he hypergeometric functions
of the left handside into those of the right handside. Checking now t he identity (88) is therefore
reduced to straightforward but tedious manipulations on ν∞ functions. □
Note that the relation (86) when A = 0 reduces to the identity:
∫
dρZ P(0,ρ Z) Γ (X0X1) ( Y0Y1)
(Z0Z0)
{ B Y 1
Z0 X0
Y0
X1
}
(3)
{ C Y 1
Z0 X0
Y0
X1
}
(3)
=δB,C (89)
which is exactly, using (88), the orthogonality condition on Askey-W ilson polynomials for the
family of parameters n = B +Y0 −Y1,a = q2X1+2Y1+3,b = q2Y1−2X1+1,c = q2X0−2Y0+1,d =
q−2Y0−2X0−1, 2z = 2Z0 + 1.
Although one would suspect that the relation (86) can be proved fo r any A by disentangling
the sum over mZ and the integration over ρZ, we have not been able to prove it in this way.
