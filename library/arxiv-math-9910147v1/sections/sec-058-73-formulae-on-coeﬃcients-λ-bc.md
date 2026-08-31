---
doc_id: arxiv-math-9910147v1
doc_title: "Tensor Products of Principal Unitary Representations of Quantum Lorentz Group and Askey-Wilson Polynomials E. Buffenoir ∗"
section_id: sec-058-73-formulae-on-coeﬃcients-λ-bc
section_title: "Formulae on coeﬃcients Λ BC"
section_number: 7.3
pages: 29-31
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
---
AD(X0X1)
Let us recall some properties of the coeﬃcients Λ BC
AD(X0X1) which were proved in [1]. We will
say that the coeﬃcients Λ BC
AD are oﬀ-diagonal if A ⁄=D and diagonal if A =D (in the latter case
29
we will use the notation Λ BC
A = Λ BC
AA). The coeﬃcients Λ BC
A are said to be on the boundary
if B +C = A, A +B = C, or A +C = B. The coeﬃcients Λ BC
AD(X0X1) are proportional to
Y (0)
(A,B,C )Y (0)
(D,B,C )Y (1)
(A,X0−X1)Y (1)
(D,X0−X1), so they vanish according to these selection rules. The
following relation holds true (it is in fact equivalent to the property th at
(X0 X1 )
Π is a representation
of Uq(an(2))):
Λ AC
F GΛ BD
GH =
∑
KU
eiπ(G+U)([dU ][dG])
1
2 Λ KU
F H
eiπ(C+D)([dC ][dD])
1
2
{
B C
A D
U
G
}
(0)
{
F A
B U
C
K
}
(0)
{
A B
H U
K
D
}
(0)
. (105)
As a result, by taking F = H in this expression, the oﬀ-diagonal coeﬃcients are obtained,
up to a sign, from the diagonal coeﬃcients.
These diagonal coeﬃcients can be computed in various ways. They s atisfy the following
system of linear equations:
∀(A,B,C ) ∈ 1
2 Z+ × 1
2 Z+ × 1
2 Z+∗/B +A−C, B+C −A, A+C −B ∈ N∗
[A+B+C+1]
[2A+1] Λ B C
A + [A+C− B+1]
[2A+1] Λ B−1 C
A − [C+B− A− 1]
[2A+1] Λ B−1 C−1
A + [B+A− C+1]
[2A+1] Λ B C−1
A =
= [A+B− C− 1]
[2A− 1] Λ B−1 C
A−1 + [A+C− B− 1]
[2A − 1] Λ B C −1
A−1 + [A+B+C− 1]
[2A − 1] Λ B−1 C−1
A−1 − [C+B− A+1]
[2A− 1] Λ B C
A−1, (106)
as well as ∀A,B,C ∈ 1
2 Z+/Y (0)
(A,B,C ) = 1,
[B+C−A+ 1][A+B+C+ 2]q±(C−B)Λ
B+ 1
2 C+ 1
2
A − [A+C−B][A+B−C+ 1]q∓(C+B+1)Λ
B+ 1
2 C− 1
2
A +
+[A+C+B+ 1][B+C−A]q∓(C−B)Λ
B− 1
2 C− 1
2
A − [A+B−C][A+C−B+ 1]q±(C+B+1)Λ
B− 1
2 C+ 1
2
A
=ω±[2C+ 1][2B+ 1]ΛB C
A , (107)
where we have denoted ω+ =q2X0+1 +q−2X0−1, ω− =q2X1+1 +q−2X1−1.
These two linear systems have a unique normalized solution. The value of the diagonal
coeﬃcients on the boundary have the following simple expression:
Λ B C
B+C (X0X1) =
B∑
k=−B
q−2k(X0+X1+1)( B+C+X0−X1
B+k
)
q
( B+C−X0+X1
B−k
)
q
(−1)2B( 2B+2C
2B
)
q
, (108)
Λ B A +B
A (X0X1) =
B∑
k=−B
q−2k(X0+X1+1)( A+X0−X1+B−k
B−k
)
q
( A−X0+X1+B+k
B+k
)
q( 2A+2B+1
2B
)
q
= vX0
vX1
Λ A+B B
A (X1X0). (109)
Diﬀerent explicit formulae for the coeﬃcients Λ BC
AD can be obtained, the fundamental one
is expressed in terms of 6j(1) (53). This last expression can be simp liﬁed, using the universal
shifted cocycle associated to 6 j(1), and we get:
Λ BC
AD(X0,X 1) =
∑
σ1σ2
v1/4
A
v1/4
D
N (D)(q2X1+1,m X )
N (A)(q2X1+1,m X )
( mX
A
C B
σ2 σ1
)
q−2iσ1ρX
( σ1 σ2
B C
D
mX
)
(110)
where N (A)(q2X+1,σ ) are normalization factors, given in [1], which values will not be useful in
our paper. This last expression is simpler than (53) in many aspects: it is a sum of a product
30
of basic hypergeometric of 3-2 type rather than 4-3 type, and mo reover it explicitely shows that
Λ BC
A are Laurent polynomials in qiρX.
Remark: From the system of constraints satisﬁed by the coeﬃcien ts Λ BC
AD, it is easy to show
that (Λ BC
AD)2 is a Laurent polynomials in both variables q2X0+1,q 2X1+1.
The constraint systems described before, as well as explicit expre ssions, allow us to derive
most of the asymptotic properties of these coeﬃcients when some of the variables are large.
Proposition 15 The coeﬃcients Λ BC
AD satisfy the following inequality:
∀A,D ∈ 1
