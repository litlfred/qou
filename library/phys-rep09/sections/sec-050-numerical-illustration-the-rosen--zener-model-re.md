---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-050-numerical-illustration-the-rosen--zener-model-re
section_title: "Numerical illustration: The Rosen--Zener model revisited"
section_number: null
pages: 58-60
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
Next we apply the previous numerical schemes to the integration of the differential equation governing the evolution of
a particular quantum two-level system. Our purpose here is to illustrate the main issues involved, and compare the different
approximations obtained with both the analytical treatment done in Section 4 and the exact result. Specifically, we consider
the Rosen-Zener model in the Interaction Picture already analyzed in Section 4.1.2. In this case, the equation to be solved is
U; = H,(t)U;, or equivalently, Eq. (223) with Y(t) = U;(t) and coefficient matrix (fh = 1)

A(t) = A(t) = —iV(s) (0; cos(Es) — 02 sin(Es)) = —ib(s)-o. (272)

Here V(s) = Vo/ cosh(s), € = wT ands = t/T. Given the initial condition |+) = (1, 0)" at t = —oo, our purpose is to get
an approximate value for the transition probability to the state |—) = (0, 1)" at t = +00. Its exact expression is collected
in the first line of Eq. (204), which we reproduce here for the reader’s convenience:

ind
sin’ y
Pex = |(U;)12(+00, —00)|? = —>——_,, (273)
cosh* (7 & /2)
with y = 2VoT.
To obtain, in practice, a numerical approximation to P.,, we have to integrate the equation in a sufficiently large time
interval. We take the initial condition at sy) = —25 and the numerical integration is carried out until ss = 25. Then, we

determine (U;)12(S, So).

As a first numerical test, we take a fixed (and relatively large) time step h such that the whole numerical integration in the
time interval s € [5o, s;] is carried out with 50 evaluations of the vector b(s) for all methods. In this way, their computational
cost is similar.

To illustrate the qualitative behavior of Magnus integrators in comparison with standard Runge-Kutta schemes, the
following methods are considered:

e Explicit first-order Euler (E1): Yni1 = Yn + MA(ty)Yn with th, = t + hand h = 1 (solid lines with squares in the
figures).

e Explicit fourth-order Runge-Kutta (RK4), i.e., scheme (227) with h = 2, since only two evaluations of b(s) per step are
required in the linear case (solid lines with triangles).

e Second-order Magnus (M2): we consider the midpoint rule (one evaluation per step) to approximate (2; taking h = 1
(dashed lines), i.e.,

. _sin(hb,)

Yn41 = exp (—ihb, - 0) Y, = {| cos(hb,)I — i hb b,-o ) Yn (274)

in
with b, = b(t, + h/2) and by, = ||b,||. The trapezoidal rule is equally valid by considering b, = (b(t,) + b(t, + h))/2.

e Fourth-order Magnus (M4). Using the fourth-order Gauss-Legendre rule to approximate the integrals and taking h = 2,
one has the scheme (254) which, for this problem, reads

b, = b(t, + ch), bz = b(t, + coh),

h 3
d= "oy +b) — 9 ie x br) (275)
Yn41 = exp (—ihd- 0) Y,

; 8, Q=Ft Re (dotted lines).

We choose € = 0.3 and € = 1, and each numerical integration is carried out for different values of y in the range
y € [0, 277]. We plot the corresponding approximations to the transition probability in a similar way as in Fig. 7 for the
analytical treatment. Thus we obtain the plots of Fig. 14. As expected, the performance of the methods deteriorates as y
increases. Notice, also, that the qualitative behavior of the different numerical schemes is quite similar as that exhibited
by the analytical approximations. Euler and Runge-Kutta methods do not preserve unitarity and may lead to transition
probabilities greater than 1 (just like the standard perturbation theory). On the other hand, for sufficiently small values of
y (inside the convergence domain of the Magnus series) the fourth-order Magnus method improves the result achieved by
the second-order, whereas for large values of y, a higher order method does not necessarily lead to a better approximation.

with c; =
S. Blanes et al. / Physics Reports 470 (2009) 151-238 209

1

— Exact
Ke Eul
og} | = Bier
— — Magnus-2

0.8 + Magnus-4 4

0.7
2
3 0.6 | 4
Q
[4
a
© 0.5 |
aI
g 0.4}
©
fc

0.3 |

o2b

0.1}

Fig. 14. Rosen-Zener model: Transition probabilities as a function of y, with € = 0.3 and € = 1. The curves are coded as follows. Solid line represents the
exact result; E1: solid lines with squares; RK4: solid lines with triangles; M2: dashed lines; M4: dashed-broken lines (indistinguishable from exact result
in left panel).

Transition Probability

1
§

Fig. 15. Rosen-Zener model: Transition probabilities as a function of €, with y = 2 and y = 5. Lines are coded as in Fig. 14.

In Fig. 15 we repeat the experiment, now taking y = 1 and y = 2, and for different values of &. In the first case, only the
Euler method differs considerably from the exact solution, and in the second case this happens for both RK methods.

To increase the accuracy, one can always take smaller time steps, but then the number of evaluations of A(t) increases,
and this may be computationally very expensive for some problems due to the complexity of the time dependence and/or
the size of the matrix. In those cases, it is important to have reliable numerical methods, providing the desired accuracy as
fast as possible or, alternatively, leading to the best possible accuracy at a given computational cost.

A good perspective of the overall performance of a given numerical integrator is provided by the so-called efficiency
diagram. This efficiency plot is obtained by carrying out the numerical integration with different time steps, corresponding
to different numbers of evaluations of A(t). For each run, one compares the corresponding approximation with the exact
solution, and plots the error as a function of the total number of matrix evaluations. The results are better illustrated in a
double logarithmic scale. In that case, the slope of the curves should correspond, in the limit of very small time steps, to
(minus) the order of accuracy of the method.

To illustrate this issue, in Fig. 16 we collect the efficiency plots of the previous schemes when € = 0.3 with y = 10
(left) and y = 100 (right). We have also included the results obtained by several higher order integrators, namely the
sixth-order RK method (RK6) whose coefficients are collected in (229) and the sixth-order Magnus integrator (M6) given
210 S. Blanes et al. / Physics Reports 470 (2009) 151-238

(€=0.3,y=10) (§=0.3,7=100)

—@ Evier
mm AKA
te PKG
Magnus-2
Magnus-4
— Magnus-6

Log(Error)
Log(Error)

3 3.2 3.4 3.6 3.8 4
Log(Evaluations) Log(Evaluations)

Fig. 16. Rosen-Zener model: Error in the transition probabilities versus the number of evaluations of the Hamiltonian H,(s) for € = 0.3 and y = 10 (left
panel) and y = 100 (right panel).

by (251) and (257). We clearly observe that the Euler method is, by far, the worst choice if accurate results are desired.
Notice the (double) logarithmic scale of the plots: thus, for instance, when y = 10 the range goes approximately from
300 to 3000 evaluations of A(t). Magnus integrators, in addition to providing results in SU(2) by construction (as the exact
solution), show a better efficiency than Runge-Kutta schemes for these examples, and this efficiency increases with the value
of y considered. The implicit Runge-Kutta-Gauss—Legendre methods (237) show slightly better results than the explicit RK
methods, but still considerably worse than Magnus integrators.

If we compare Magnus integrators of different orders of accuracy, we observe that the most efficient scheme is the second
order method M2 when relatively low accuracies are desired. For higher accuracy, however, it is necessary to carry out a
thorough analysis of the computational cost of the methods for a given problem before asserting the convenience of M4
or M6 with respect to higher order schemes. For a fixed time step h, the computational cost of a certain family of methods
(such as those based on Magnus) usually increases with the order. However, if one fixes the number of A(t) evaluations, this
is not necessarily the case (sometimes higher order methods require more commutators but less exponentials).

Let us now compare the performance of the Magnus methods with respect to other Lie-group solvers, namely Fer and
Cayley methods. We repeat the same experiments as in Fig. 16 but, for clarity, only the results for the 6th-order methods are
shown. We consider the symmetric-Fer method given by (265) and (267) and the Cayley method (268) with (271), using in
both cases the Gauss—Legendre quadrature. The results obtained are collected in Fig. 17. We clearly observe that the relative
performance of the Cayley method deteriorates by increasing the value of y similarly to the RK6. In spite of preserving the
qualitative properties, this example shows that for some problems, polynomial or rational approximations do not perform
efficiently. Here, in particular, the Magnus scheme is slightly more efficient than the symmetric Fer method, although for
other problems their performance is quite similar.
