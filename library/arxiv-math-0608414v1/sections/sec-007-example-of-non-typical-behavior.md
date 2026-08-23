---
doc_id: arxiv-math-0608414v1
doc_title: "Exponential Asymptotics, Transseries, and Generalized Borel Summation for Analytic, Nonlinear, Rank-One Systems of Ordinary Differential Equations"
section_id: sec-007-example-of-non-typical-behavior
section_title: "Example of non-typical behavior"
section_number: null
pages: 44-46
source_pdf: 0608414v1.pdf
source_sha256: bd9a8d48a6d66945
doc_brief: "Exponential Asymptotics, Transseries, and Generalized Borel Summation for Analytic, Nonlinear, Rank-One Systems of Ordinary Differential Equations — For analytic nonlinear systems of ordinary"
---
Consider the equation
f ′ =−f− 1
2x f + 1
x− 1
2x2 (A.1)
The general solution of this equation is given by
44
f = 1
x + Cx −1/2e−x =
∫ ∞
0
(
p + C√p− 1H(1− p)
)
dp (A.2)
We see that the asymptotic series of f for x→∞ ,ℜ(x) > 0, ˜y0 = 1/x. The
inverse Laplace transform of f is
L−1f = p + C√p− 1H(1− p) (A.3)
i) The Stokes constant is zero and Y0 =B(˜y0) = p is entire.
ii) All combinations λY+
0 + (1− λ)Y−
0 coincide. Therefore (1.30) does
not hold.
Equation (A.1) is exceptional, in the sense that the properties i), ii) above
do not withstand a small perturbation. Indeed, for the equation
f ′ =−f− 1
2xf + 1 + ǫ
x − 1
2x2 (A.4)
we haveB(˜y0) = 2 ǫ + p + ǫ(1− p)−1/2 and the inverse Laplace transform of
the general solution is
L−1(f ) =
{
2ǫ + p + ǫ(1− p)−1/2 for p < 1
2ǫ + p + C(p− 1)−1/2 for p > 1
A.2 AC(f∗ g) versus AC(f )∗ AC(g)
Typically, the analytic continuation along curve in W1 which is not homo-
topic to a straight line will not commute with convolution. For example, in
equation (A.4), B(˜y0)−+∗B (˜y0)−+⁄= [B(˜y0)∗B (˜y0)]−+, as it can be seen
from Remark 42 below (or by direct calculation). This situation is gene ric:
Remark 42 Let y be a function satisfying the conditions stated in Proposi-
tion 41 and assume that p = 1 is a branch point of y. Then,
(y∗ y)−+⁄= y−+∗ y−+ (A.5)
Proof
Indeed, by (2.108) and (2.104)
(y∗ y)−+ = y+∗ y+ + 2[(y+∗ y+
1 )H]◦ τ1⁄= y−+∗ y−+ =
45
[y+ + (Hy+
1 )◦ τ1]∗2 = y+∗ y+ + 2[(y+∗ y+
1 )H]◦ τ1 + [H(y+
1∗ y+
1 )]◦ τ2
(A.6)
since in view of (2.104), in our assumptions, y1⁄≡0 and thus y1∗ y1⁄≡0.
There is also the following intuitive reasoning leading to the same con-
clusion. For a generic system of the form (1.1)–(1.3), p = 1 is a branch point
of Y0 and so Y−
0 ⁄= Y−+
0 . On the other hand, if AC−+ commuted with
convolution, thenL(Y−+
0 ) would provide a solution of (1.1). By Lemma 36,
L(Y−
0 ) is a diﬀerent solution (since Y−
0 ⁄= Y−+
0 ). As Y−
0 and Y−+
0 coin-
cide up to p = 2 we have L(Y−+
0 )−L (Y−
0 ) = O(e−2xxpower) for x→ +∞.
By Theorem 2 however, no two solutions of (1.1)–(1.3) can diﬀer by le ss
than e−xxpower without actually being equal (also, heuristically, this can be
checked using formal perturbation theory), contradiction.
