---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-066-time-independent-schrödinger-equation
section_title: "Time-independent Schrödinger equation"
section_number: null
pages: 75-75
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
Restricting ourselves to the time-independent Schrédinger equation (312), we next illustrate how Magnus integrators
can, in fact, be used to compute the discrete eigenvalues defined by the problem. Although only the Schrodinger equation
in a finite domain is considered,

Co

dx?
the procedure can be easily adapted to other types of eigenvalue problems, in which one has to find both A = E and ¢. Here
it is assumed that the potential is smooth, V € C™(a, b) and, for simplicity, g(a) = gy(b) = 0.

Under these assumptions, it is well known that the eigenvalues are real, distinct and bounded from below. The problem
(328) can be formulated in the special linear group SL(2),

+V(x)p =, xe (a,b) (328)

dy 0 1 1
ax = (vas at 0) y, xe€(a,b), wherey = (g, dg/dx) , (329)
so that the Magnus expansion can be applied in a natural way. As usual, rather than approximating the fundamental solution
of (329) in the entire interval (a, b) by exp({2), the idea is to partition the interval into N small subintervals, and then apply
a conveniently discretized version of the Magnus expansion. In this way, the convergence problem no longer restricts the
size (b — a) [70].

For the sake of simplicity, let us consider the fourth-order method (254). Writing

racv(ae(t—Z)p). wav (ue(te 2s)

where h = (b — a)/N and x, = a+ hn, we form

V3
a hP(Va,1 — Vn.2) h
on(A) = V3 ,
5h(Vn.1 + Vn2) — RA Sh? (Vi.1 — Vn.a)
2 12
forn = 0,1,...,N — 1. Then, the fourth-order approximation to the solution of (329) at x = b is
y(b) = eN-1A) ., @o1) 0 ya) (330)

and the values of A are obtained from (330) by repeatedly using the expression of the exponential of a traceless matrix,
Eq. (24), and requiring that y(a) = g(b) = O. The resulting nonlinear equation in 4 can be solved, for instance, by
Newton-Raphson iteration, which provides quadratic convergence for starting values sufficiently near the solution [70].

Although, by construction this procedure leads to a global order of approximation @(h?) if a pth-order Magnus method
is applied, it turns out that the error also depends on the magnitude of the eigenvalue. Specifically, the error in a pth-order
method grows as @(h?+',?/2-') [70], and thus one expects poor approximations for large eigenvalues. This difficulty can
be overcome, up to a point, by analyzing the dependence on A of each term in the Magnus series and considering partial
sums of the terms carrying the most significant dependence on X. For instance, it is possible to design a sixth-order Magnus
integrator for this problem with error @(h’4), which therefore behaves like a fourth-order method when h?A ~ 1, whereas
the standard sixth-order Magnus scheme, carrying an error of @(h’ A”), reduces to an order-two method [70]. In any case,
getting accurate approximations when |A| — oo is more problematic [185].
