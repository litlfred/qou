---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-007-42-certifying-error-bounds-on-integrals
section_title: "Certifying error bounds on integrals"
section_number: 4.2
pages: 8-8
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
bounds is that we have inequalities involving integrals that need to be checked. For exam-
ple, one of our bounds requires that
(4.1) bf(i/2)≥2(g−1)
Z ∞
0
bf(x)xtanh(πx)dx.
To obtain functions that satisfy this inequality, we first compute numerical approximations
In of the integrals Z ∞
0
L(−1/2)
n (x2)e−x2/2xtanh(πx)dx.
In our linear system of equations, we then impose that bf(i/2) =q(−1/4)e 1/8 is equal to
ρtimes the numerical approximation of 2(g−1)
R∞
0
bf(x)xtanh(πx)dx(given by a linear
combination of the approximationsI n), whereρ>1 is some rational number. Technically,
we also replacee 1/8 by a rational approximation in this equation.
Once we have found a good candidate functionf, we verify a posteriori that inequality
(4.1) is satisfied. This is done by evaluating the left-hand side using interval arithmetic
(which provides true lower and upper bounds on bf(i/2)) and finding certified bounds on
the integral.
For a functionhthat is analytic in a neighborhood of a compact interval [a,b], the
Arbpackage [Joh17] inSageMath[The21] is able to compute the integral
Rb
a h(x)dxwith
certified error bounds. However, improper integrals (and in particular infinite intervals)
cannot be handled. We thus use theArbpackage to estimate
Rb
0
bf(x)xtanh(πx)dxfor
some largeband then estimate the remainder
R∞
b
bf(x)xtanh(πx)dxseparately. For this,
we use the inequalities
tanh(πb)≤tanh(πx)≤1
forx≥b. In all cases, our hypotheses will require that bfis eventually of constant sign, so
it remains to estimate Z ∞
b
bf(x)xdx=
Z ∞
b
xq(x2)e−x2/2dx.
However, sincexq(x 2) is an odd polynomial, the functionxq(x 2)e−x2/2 admits an explicit
primitive and the integral can be computed exactly.
We will sometimes have to deal with more complicated integrals, in which case we
estimate the remainder terms using ad hoc inequalities.
