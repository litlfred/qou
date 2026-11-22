---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-043-introduction
section_title: "Introduction"
section_number: null
pages: 48-50
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
The Magnus expansion, as formulated in Section 2, has found extensive use in mathematical physics, quantum chemistry,
control theory etc, essentially as a perturbative tool in the treatment of the linear equation
Y’=A(t)Y, — Y(to) = Yo. (223)

When the recurrence (49)-(50) is applied, one is able to explicitly get the successive terms 2; in the series, defining @ as
linear combinations of multivariate integrals containing commutators acting iteratively on the coefficient matrix A, as in
S. Blanes et al. / Physics Reports 470 (2009) 151-238 199

(42)-(46). As a result, with this scheme, analytical approximations to the exact solution are constructed explicitly. These
approximate solutions are fairly accurate inside the convergence domain, especially when high order terms in the Magnus
series are taken into account, as illustrated by the examples considered in Section 4.

There are several drawbacks, however, involved in the procedure developed so far, especially when one tries to find
accurate approximations to the solution for very long times. The first one is implicitly contained in the analysis done in
Section 2: the size of the convergence domain of the Magnus series may be relatively small. The logarithm of the exact
solution Y(t) may have complex singularities and this implies that no series expansion can converge beyond the first
singularity. This disadvantage may be, up to some point, avoided by using different pictures (e.g. the transformations shown
in Section 2.9) in order to increase the convergence domain of the Magnus expansion, a fact also illustrated by several
examples in Section 4. Unfortunately, these preliminary transformations sometimes either do not guarantee convergence,
or the rate of convergence of the series is very slow. In that case, accurate results can only be obtained provided a large
number of terms in the series are taken into account.

The second drawback is the increasingly complex structure of the terms 2, in the Magnus series: each (2, is a k-
multivariate integral involving a linear combination of (k — 1)-nested commutators of A evaluated at different times tj,
i = 1,...,k. Although in some cases these expressions can be computed explicitly (for instance, when the elements of
A and its commutators are polynomial or trigonometric functions), in general a special procedure has to be designed to
approximate multivariate integrals and reduce the number of commutators involved.

When the entries of the coefficient matrix A(t) are complicated functions of time or they are only known for certain
values of t, numerical approximation schemes are unavoidable. In many cases, it is thus desirable to obtain numerical
approximations to the exact solution at many different times. This section is devoted precisely to the Magnus series
expansion as a tool for building numerical integrators for Eq. (223).

Before embarking on exposing the technical details contained in this construction, let us first introduce several concepts
which are commonplace in the context of the numerical integration of differential equations.

Given the general (nonlinear) ordinary differential equation (ODE)

x =f(t,x), — X(to) =x) € C4, (224)

standard numerical integrators, such as Runge-Kutta and multistep methods, proceed as follows. First the whole time
interval [to, ty], is split into N subintervals, [t,_1,t)], n = 1,...,N, with ty = ts, and subsequently the value of x(t)
is approximated with a time-stepping advance procedure of the form

Xn41 = (In, Xn, --- 5 No, Xo) (225)

starting from Xo. Here the map ® depends on the specific numerical method and h, = ty41 — tn are the time steps. For
simplicity in the presentation, we consider a constant time step h, so that t, = to + nh. In this way, one gets x,1 as an
approximation to x(tn+1). In other words, the exact evolution of the system (224) is replaced by the discrete or numerical
flow (225). The simplest of all numerical methods for (224) is the explicit Euler scheme

Xng1 = Xn + hf(tn, Xn)- (226)

It computes approximations x, to the values x(t;,) of the solution using one explicit evaluation of f at the already computed
value X,_1. In general, the numerical method (225) is said to be of order p if, assuming X, = X(tn), then Xp41 = X(tn41) +
©(h?*"), Thus, in particular, Euler method is of order one.

Of course, more elaborate and efficient general purpose algorithms, using several f evaluations per step, have been
proposed along the years for the numerical treatment of Eq. (224). In fact, any standard software package and program
library contains dozens of routines aimed at providing numerical approximations with several degrees of accuracy, including
(explicit and implicit) Runge-Kutta methods, linear multistep methods, extrapolation schemes etc, with fixed or adaptive
step size. They are designed in such a way that the user has to provide only the initial condition and the function f to obtain
approximations at any given time.

This being the case, one could ask the following question: if general purpose integrators are widely available for the
integration of the linear equation (223) (which is a particular case of (224)), what is the point of designing new and somehow
sophisticated algorithms for this specific problem?

It turns out that, in the same way as for classical time-dependent perturbation theory, the qualitative properties of the
exact solution are not preserved by the numerical approximations obtained by standard integrators. This motivates the study
of the Magnus expansion, with the ultimate goal of constructing numerical integration methods. We will show that highly
accurate schemes can, indeed, be designed, which in addition preserve qualitative properties of the system. The procedure
can also incorporate the tools developed for the analytical treatment, such as preliminary linear transformations, to end up
with improved numerical algorithms.

We first summarize the main features of the well know class of Runge-Kutta methods as representative of integrators
of the form (225). They are introduced for the general nonlinear ODE (224) and are subsequently adapted to the linear
case (223).
200 S. Blanes et al. / Physics Reports 470 (2009) 151-238
