---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-056-time-independent-schrödinger-equation
section_title: "Time-independent Schrödinger equation"
section_number: null
pages: 75-76
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
Restricting ourselves to the time-independent Schrödinger equation (312), we next illustrate how Magnus integrators
can, in fact, be used to compute the discrete eigenvalues defined by the problem. Although only the Schrödinger equation
in a finite domain is considered,
−
d2ϕ
dx2 + V(x)ϕ = λϕ,
x ∈(a, b)
(328)
the procedure can be easily adapted to other types of eigenvalue problems, in which one has to find both λ ≡E and ϕ. Here
it is assumed that the potential is smooth, V ∈Cm(a, b) and, for simplicity, ϕ(a) = ϕ(b) = 0.
Under these assumptions, it is well known that the eigenvalues are real, distinct and bounded from below. The problem
(328) can be formulated in the special linear group SL(2),
dy
dx =

0
1
V(x) −λ
0

y,
x ∈(a, b),
where y = (ϕ, dϕ/dx)T,
(329)
so that the Magnus expansion can be applied in a natural way. As usual, rather than approximating the fundamental solution
of (329) in the entire interval (a, b) by exp(Ω), the idea is to partition the interval into N small subintervals, and then apply
a conveniently discretized version of the Magnus expansion. In this way, the convergence problem no longer restricts the
size (b −a) [70].
For the sake of simplicity, let us consider the fourth-order method (254). Writing
Vn,1 = V
 
xn +
 
1
2 −
√
3
6
!
h
!
,
Vn,2 = V
 
xn +
 
1
2 +
√
3
6
!
h
!
,
where h = (b −a)/N and xn = a + h n, we form
σn(λ) =


−
√
3
12
h2(Vn,1 −Vn,2)
h
1
2
h(Vn,1 + Vn,2) −hλ
√
3
12
h2(Vn,1 −Vn,2)

,
for n = 0, 1, . . . , N −1. Then, the fourth-order approximation to the solution of (329) at x = b is
y(b) = eσN−1(λ) · · · eσ1(λ) eσ0(λ)y(a)
(330)
and the values of λ are obtained from (330) by repeatedly using the expression of the exponential of a traceless matrix,
Eq. (24), and requiring that ϕ(a) = ϕ(b) = 0. The resulting nonlinear equation in λ can be solved, for instance, by
Newton–Raphson iteration, which provides quadratic convergence for starting values sufficiently near the solution [70].
Although, by construction this procedure leads to a global order of approximation O(hp) if a pth-order Magnus method
is applied, it turns out that the error also depends on the magnitude of the eigenvalue. Specifically, the error in a pth-order
method grows as O(hp+1λp/2−1) [70], and thus one expects poor approximations for large eigenvalues. This difficulty can
be overcome, up to a point, by analyzing the dependence on λ of each term in the Magnus series and considering partial
sums of the terms carrying the most significant dependence on λ. For instance, it is possible to design a sixth-order Magnus
integrator for this problem with error O(h7λ), which therefore behaves like a fourth-order method when h2λ ≈1, whereas
the standard sixth-order Magnus scheme, carrying an error of O(h7λ2), reduces to an order-two method [70]. In any case,
getting accurate approximations when |λ| →∞is more problematic [185].
6.2. Sturm–Liouville problems
The system defined by (328) with boundary conditions ϕ(a) = ϕ(b) = 0 is just one particular example of a second order
Sturm–Liouville problem [186,187]. It is thus quite natural to try to apply Magnus integrators to more general problems
within this class.
226
S. Blanes et al. / Physics Reports 470 (2009) 151–238
A second order Sturm–Liouville eigenvalue problem has the form
d
dx

p(x)
dy
dx(x)

+ q(x)y(x) = λ r(x)y(x)
on (a, b)
(331)
with separated boundary conditions which commonly have the form
A1y(a) + A2p(a)y′(a) = 0
B1y(b) + B2p(b)y′(b) = 0
(332)
for given constants Ai, Bi and functions p(x), q(x) and r(x). Solving this problem means, of course, determining the values
λn of λ for which Eq. (331) has a nontrivial (continuously differentiable square integrable) solution yn(x) satisfying Eq.
(332) [187,188].
These and other higher order Sturm–Liouville problems can be recast as a linear matrix system of the form
Y ′ = (λB + C(x))Y
(333)
by transforming to the so-called compound matrix or modified Riccati variables [189,185]. Here B is a constant matrix. When
generalizing the above treatment based on the Magnus expansion to this problem, there is one elementary but important
remark worth stating explicitly: unless the differential equation (333) has the same large λ-asymptotics as some differential
equation with x-independent coefficients, then it will be impossible to develop a Magnus method which accurately approximates
its solutions for large λ [185]. The reason is that a Magnus method approximates the solution by a discrete solution, calculated
using a formula of the form Y(xn+1) = exp(σn(λ))Y(xn); in particular, on the first step (x0, x1), the differential equation is
approximated by one in which the coefficient matrix is replaced by the x-independent matrix σ0(λ)/(x1 −x0).
In consequence, the attention should be restricted to systems for which it is known that a suitable constant-coefficient
system provides the correct asymptotics. This is the case, in particular, for Eq. (328), and more generally for linear equations
of order 2n in which the (2n −1)st derivative is zero, such as
(−1)ny(2n) +
2n−2
X
j=0
qj(x)y(j) = λy.
Here the asymptotics are determined by the equation (−1)ny(2n) = λy [190]. Even then, the methods developed in [70] for
Eq. (328) and implemented for systems with matrices of general size in [185] require a λ-dependent step size restriction of
the form h ≤O(|λ|−1/4) in order to be defined. Nevertheless, the analysis carried out in [185] shows that the fourth order
Magnus integrator based on a two-point Gaussian quadrature appears to offer significant advantages over conventional
methods based on power series and library routines.
Magnus integrators have also been successfully applied in the somewhat related problem of computing the Evans
function for spectral problems arising in the analysis of the linear stability of traveling wave solutions to reaction–diffusion
PDEs [169]. In this setting, Magnus integrators possess some appealing features in comparison, for instance, with
Runge–Kutta schemes: (1) they are unconditionally stable; (2) their performance is superior in highly oscillatory regimes
and (3) their step size can be controlled in advance. Items (2) and (3) are due to the fact that error bounds for Magnus
methods depend only on low order derivatives of the coefficient matrix, not (as for Runge–Kutta schemes) on derivatives of
the solution. Therefore, performance and, correspondingly, the choice of optimal step size remain uniform over any bounded
region of parameter space [169].
