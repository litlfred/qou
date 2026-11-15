---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-061-nonlinear-matrix-equations-in-lie-groups
section_title: "Nonlinear matrix equations in Lie groups"
section_number: null
pages: 70-70
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
As we have already mentioned, the strategy adopted by most Lie-group methods for solving the nonlinear matrix
differential equation (139),

Y=A(L,Y)Y, YO =%E¥Y

defined in a Lie group 9, whilst preserving its Lie group structure, is to lift Y(t) from % to the underlying Lie algebra g
(usually with the exponential map), then formulate and numerically solve there an associated differential equation, and
finally map the solution back to 9. In this way, the discretization procedure works in a linear space rather than in the Lie
group. In particular, the idea of the so-called Runge-Kutta-Munthe-Kaas class of schemes is to approximate the solution of
the associated differential equation in the Lie algebra g by means of a classical Runge-Kutta method [59,179,180].

To generalize Magnus integrators when A = A(t, Y), an important difference with respect to the linear case is that, now,
multivariate integrals depend also on the value of the (unknown) variable Y at quadrature points. This leads to implicit
methods and nonlinear algebraic equations in every step of the integration [181], which in general cannot compete in
efficiency with other classes of geometric integrators such as splitting and composition methods.

An obvious alternative is just to replace the integrals appearing in the nonlinear Magnus expansion developed in
Section 3.3 by affordable quadratures, depending on the particular problem. If, for instance, we use Euler’s method to
approximate the first term in (142), 2'"I(h) = hA(O, Yo) + @(h?) and 2/2! is discretized with the midpoint rule, we get
the second order scheme

hs
v2) = hA (5. ely) = 2Pl(hy + 0(n?)

Y; =e”Yp. (304)

The same procedure can be carried out at higher orders, consistently discretizing the integrals appearing in 2!"!(h) for
m > 2 [99].
