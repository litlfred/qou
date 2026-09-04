---
doc_id: arxiv-math-9910147v1
doc_title: "Tensor Products of Principal Unitary Representations of Quantum Lorentz Group and Askey-Wilson Polynomials E. Buffenoir ∗"
section_id: sec-015-2-z-and-deﬁned-by
section_title: "Z and deﬁned by"
section_number: 2
pages: 8-10
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
doc_brief: "Tensor Products of Principal Unitary Representations of Quantum Lorentz Group and Askey-Wilson Polynomials E. Buffenoir ∗ — We study the tensor product of principal unitary representa tions of the"
---
{
A X 1
Z1 Y1
X2
Y2
}
(3)
=
{{
A X 1
Z1 Y1
X2
Y2
}}
Y (1)
(A,X1−X2)Y (1)
(A,Y1−Y2). (34)
These 6j(3) satisfy properties, which will be used in the rest of the paper an d which are
continuation of the identities satisﬁed by 6 j(0) and 6 j(1). We prefered to give combinatorial
proofs of these properties rather than continuation arguments , in order to prepare to the 6 j(6)
case. Here again, the sums are ﬁnite which is a consequence of the s election rules in the deﬁnition
of 6j(3). Note that these 6 j(3) satisfy other relations, which will be explained in the section 5,
as consequences of the study of the tensor product of principal representations of the quantum
Lorentz group.
Proposition 3 The following symmetry properties are satisﬁed:
{ A X 1
Z1 Y1
X2
Y2
}
(3)
=
{ A Y 1
Z1 X1
Y2
X2
}
(3)
= (eiπq)(X1−X2+Y1−Y2)ν1(dX2 )ν1(dY2 )
ν1(dX1 )ν1(dY1 )
{ A X 2
Z1 Y2
X1
Y1
}
(3)
.(35)
Proof:
Simple use of Sears identity (99). □
Proposition 4 We also have a discrete orthogonality property
∑
X2
{
A X 1
Z1 Y1
X2
Y2
}
(3)
{
A X 1
Z1 Y1
X2
Y3
}
(3)
=δY2,Y3Y (1)
(A,Y1−Y2). (36)
8
Proof:
This is equivalent to the orthogonality of q-Racah polynomials (see ou r appendix for notations
(101) and [19][20] for proofs):
N∑
x=0
w(R)(x;a,b,c,d )p(R)
n (µ(x);a,b,c,d )p(R)
m (µ(x);a,b,c,d ) = δn,mh(R)
n (a,b,c,d ), (37)
because N
(
T X 1
Z1 Y1
X2
Y2
) 2
= w(R)(x;a,b,c,d )
h(R)
n (a,b,c,d )
, and
4Φ 3
[
X1 − X2− T X1 +X2− T +1 Y2 − Y1− T − Y2 − Y1− T− 1
− 2T − Y1 − Z1− T +X1 X1 + Z1 − Y1− T +1
]
=p(R)
n (µ(x);a,b,c,d ),
with n =T +X2−X1, x=T +Y1−Y2, N = 2T,
a =q−4T −2, b=q4X1+2, c=q2(Z1+X1−Y1−T ), d=q−2(Z1+Y1+X1+T +2). (38)
□
These 6j(3) symbols satisfy the pentagonal relations:
Proposition 5
∑
C
{ A B
Y3 Y2
C
Y1
}
(1)
{ B A
X1 X2
C
X3
}
(1)
{ C X 1
Z1 Y3
X2
Y2
}
(3)
=
{ A X 1
Z1 Y1
X3
Y2
}
(3)
{ B X 3
Z1 Y3
X2
Y1
}
(3)
,(39)
∑
X3
{ B X 2
Z1 Y3
X3
Y1
}
(3)
{ A X1
B X3
X2
X4
}
(1)
{ A X 4
Y3 Z1
X3
Z2
}
(3)
=
{ A X 1
Y1 Z1
X2
Z2
}
(3)
{ B X 1
Z2 Y3
X4
Y1
}
(3)
.(40)
Proof:
These identities are simply proved by induction on A. Indeed, for A = 0 these identities
are trivial and for A = 1
2 they are easily checked on the exact expression of the 6 j(3) using
the ﬁnite diﬀerence equations veriﬁed by basic hypergeometric fun ctions. The induction easily
follows from the use of orthogonality and pentagonal equations on 6j(1).
□
Finally, we have a Racah relation:
Proposition 6
∑
Y2
{ A Y 1
Z2 X1
Y2
X2
}
(3)
{ A Z 2
X1 Y1
Z1
Y2
}
(3)
( v1/2
Y2 v1/2
Z1 v1/2
X2
v1/2
Z2 v1/2
Y1 v1/2
X1v1/2
A
)±1 =
{ A X 1
Y1 Z2
X2
Z1
}
(3)
(41)
Proof:
It can be proved by continuation arguments from the 6 j(1) case. □
We can prove other identities, which will be useful in the following chap ters, and which are
direct consequences of the previous ones.
Proposition 7 The following pentagonal equations are satisﬁed:
∑
X2
{ C X 1
Y1 Z3
X2
Z2
}
(3)
{ A C
X1 X3
B
X2
}
(1)
{ A X 2
Y1 Z1
X3
Z3
}
(3)
=
{ B X 1
Y1 Z1
X3
Z2
}
(3)
{ C A
Z1 Z2
B
Z3
}
(1)
, (42)
∑
Z2
{
A X 4
Y1 Z1
X2
Z2
}
(3)
{
B X 1
Z2 Y1
X4
Y2
}
(3)
{
A X 1
Y2 Z1
X3
Z2
}
(3)
=
{
A X1
B X2
X3
X4
}
(1)
{
B X 3
Z1 Y1
X2
Y2
}
(3)
. (43)
9
Proof:
It is obtained from the pentagonal relations (39)(40) and the disc rete orthogonality relation
(36). □
We also have the hexagonal equation:
Proposition 8
∑
C
v1/2
C v1/2
Y2
v1/2
B v1/2
Y1
{
C Y 3
Z1 X1
Y1
X2
}
(3)
{
A B
Y3 Y1
C
Y2
}
(1)
{
A B
X1 X2
C
X3
}
(1)
=
=
∑
Z2
v1/2
X2v1/2
Z2
v1/2
X3v1/2
Z1
{ A X 3
Y3 Z1
X2
Z2
}
(3)
{ A Y 2
X1 Z1
Y1
Z2
}
(3)
{ B X 1
Z2 Y3
X3
Y2
}
(3)
. (44)
Proof:
It is obtained by applying successively (41)(39)(43)(41). □
Finally the action of the automorphism of the complex line is given as follo ws:
Proposition 9
{ A X 1
Z1 Y1
X2
Y2
}
(3)
=
{ A X 1
Z1 Y1
X2
Y2
}
(3)
g(A,X 1,X 2,Z 1,Y 1,Y 2)(−1)Y1−Y2+X1−X2 (45)
whereg is a fourth root of unit which expression is:
g = ϕ(−Y2+X1+Z1,X1−X2+Y1−Y2)ϕ(X1+Y2+Z1+1,X1−X2+Y2−Y1)ϕ(X1+Y2−Z1,X1−X2+Y2−Y1)
ϕ(2Y2+1,1)ϕ(2X2+1,1)ϕ(Y2+Y1−A,−2A−1)ϕ(X1+X2−A,−2A−1)ϕ(Y2+Z1−X1,Y2−Y1+X2−X1)
. (46)
Proof:
It is proved using the inversion relation and the Sears identity. Using the explicit expression
for ϕ(α,n ) with n integer, we obtain that g is a fourth root of unit, but there is no simpler
formula for g. □
