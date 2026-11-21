---
doc_id: arxiv-math-0608414v1
doc_title: "Exponential Asymptotics, Transseries, and Generalized Borel Summation for Analytic, Nonlinear, Rank-One Systems of Ordinary Differential Equations"
section_id: sec-010-example-of-non-typical-behavior
section_title: "Example of non-typical behavior"
section_number: null
pages: 44-45
source_pdf: 0608414v1.pdf
source_sha256: bd9a8d48a6d66945
toc_source: outline
doc_brief: "Exponential Asymptotics, Transseries, and Generalized Borel Summation for Analytic, Nonlinear, Rank-One Systems of Ordinary Differential Equations — For analytic nonlinear systems of ordinary"
---
Example of non-typical behavior
Consider the equation
f ′ = −f −1
2xf + 1
x −1
2x2
(A.1)
The general solution of this equation is given by
44
f = 1
x + Cx−1/2e−x =
Z ∞
0

p +
C
√p −1H(1 −p)

dp
(A.2)
We see that the asymptotic series of f for x →∞, ℜ(x) > 0, ˜y0 = 1/x. The
inverse Laplace transform of f is
L−1f = p +
C
√p −1H(1 −p)
(A.3)
i) The Stokes constant is zero and Y0 = B(˜y0) = p is entire.
ii) All combinations λY+
0 + (1 −λ)Y−
0 coincide. Therefore (1.30) does
not hold.
Equation (A.1) is exceptional, in the sense that the properties i), ii) above
do not withstand a small perturbation. Indeed, for the equation
f ′ = −f −1
2xf + 1 + ǫ
x
−1
2x2
(A.4)
we have B(˜y0) = 2ǫ + p + ǫ(1 −p)−1/2 and the inverse Laplace transform of
the general solution is
L−1(f) =

2ǫ + p + ǫ(1 −p)−1/2
for p < 1
2ǫ + p + C(p −1)−1/2
for p > 1
A.2
