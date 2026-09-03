---
doc_id: arxiv-0707.3910v1
doc_title: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS"
section_id: sec-005-6-the-sixth-degree-case
section_title: "The sixth degree case"
section_number: 6
pages: 10-11
source_pdf: 0707.3910v1.pdf
source_sha256: ad31f3cba16c4ea4
doc_brief: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS — We present a rational version of the classical Landen transfor- mation for elliptic integrals."
---
We discuss the map T2p : E2p →E2p for the case p = 3. The eﬀect of T6 on
the coeﬃcients P6 = {b0, b1, b2, a1, a2} is denoted by Φ6 : O+
6 →O+
6 and is given
explicitly by
a1
→
9 + 5a1 + 5a2 + a1a2
(a1 + a2 + 2)4/3
(6.1)
a2
→
a1 + a2 + 6
(a1 + a2 + 2)2/3
b0
→
b0 + b1 + b2
(a1 + a2 + 2)2/3
b1
→
b0(a2 + 2) + 2b1 + b2(a1 + 3)
a1 + a2 + 2
b2
→
b0 + b2
(a1 + a2 + 2)1/3
using Theorem 5.1. The map Φ6 preserves the integral
U6(a1, a2, b0; b1, b2)
:=
Z ∞
0
b0z4 + b1z2 + b2
z6 + a1z4 + a2x2 + 1 dz
(6.2)
and the convergence of its iterations has been proved in [3], the main result of which
is the following theorem.
Theorem 6.1. Let x0 := (a0
1, a0
2; b0
0, b0
1, b0
2) ∈R+
5. Deﬁne xn+1 := Φ6(xn). Then
U6 is invariant under Φ6. Moreover, the sequence {(an
1, an
2)} converges to (3, 3) and
LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS 11
{(bn
0, bn
1, bn
2)} converges to (L, 2L, L), where the limit L is a function of the initial
data x0. Therefore
Z ∞
0
b0z4 + b1z2 + b2
z6 + a1z4 + a2z2 + 1 dz
=
L(x0) × π
2 .
This iteration is similar to Landen’s transformation for elliptic integrals that has
been employed in [4] in the eﬃcient calculation of π. Numerical data indicate that
the convergence of xn is quadratic. The proof of convergence is based on the fact
that Φ6 cuts the distance from (a1, a2) to (3, 3) by at least half.
A sequence of algebraic curves. The complete characterization of parameters
(a1, a2) in the ﬁrst quadrant that yield computable rational functions
R(z)
:=
b0z4 + b1z2 + b2
z6 + a1z4 + a2z2 + 1.
of degree 6 remains open.
The polynomial z6 + a1z4 + a2z2 + 1 factors when
a1 = a2 so the diagonal ∆:= {(a1, a2) ∈R+ × R+ : a1 = a2} produces computable
functions. In view of the invariance of the class of computable functions under
iterations by Φ6, the curves Xn := Φ(−n)
6
(∆), with n ∈Z, are also computable.
The curve X1 has equation
(9 + 5a1 + 5a2 + a1a2)3
=
(a1 + a2 + 2)2(a1 + a2 + 6)3
and consists of two branches meeting at the cusp (3, 3). In terms of the coordinates
x = a1 −3 and y = a2 −3 the leading order term is T1(x, y) = 1728(x −y)2. This
curve is rational and can be parametrized by
a1(t)
=
t−2(t5 −t4 + 2t3 −t2 + t + 1)
(6.3)
a2(t)
=
t−3(t5 + t4 −t3 + 2t2 −t + 1).
The rationality of Xn for n̸ = 1 and its signiﬁcance for the integration algorithm
remains open. The complexity of these curves increases with n. For example, the
curve X2 := Φ(−2)
3
(∆) is of total degree 90 in x = a1 −3 and y = a2 −3 with leading
term
T2(x, y)
:=
2121335(x −y)18 
−163(x4 + y4) + 668xy(x2 + y2) −1074x2y2
.
The diagonal ∆can be replaced by a 2-parameter family of computable curves
X(c, d) that are produced from the factorization of the sextic with a1 = c + d and
a2 = cd+ 1/d. All the images Φ(−n)
6
X(c, d) with n ∈Z are computable curves. The
question of whether these are all the computable parameters remains open.
