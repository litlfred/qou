---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-040-cayley-transform-methods
section_title: "Cayley-transform methods"
section_number: null
pages: 57-60
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
We have seen in Section 1.2 that, for the J-orthogonal group OJ(n), the Cayley transform (23) provides a useful alternative
to the exponential mapping, relating the Lie algebra to the Lie group. This fact is particularly important for numerical
methods where the evaluation of the exponential matrix is the most computation-intensive part of the algorithm.
If the solution of Eq. (223) is written as
Y(t) =

I −
1
2
C(t)
−1 
I +
1
2
C(t)

Y0
(268)
then C(t) ∈oJ(n) satisfies the equation [135]
C′ = A −
1
2[C, A] −
1
4
CAC,
t ≥t0,
C(t0) = 0.
(269)
Time-symmetric methods of order 4 and 6 have been obtained, based on the Cayley transform (268), by expanding the
solution of (269) in a recursive manner and constructing quadrature formulae for the multivariate integrals that appear
in the procedure [135–137]. It turns out that efficient Cayley based methods can be built directly from Magnus based
integrators [40]. In particular, we get:
Order 4:
C[4] = Ω[4]

I −
1
12(Ω[4])2

= α1 −
1
12[α1, α2] −
1
12α3
1 + O(h5),
(270)
where C[4] = C(h) + O(h5).
208
S. Blanes et al. / Physics Reports 470 (2009) 151–238
Order 6:
C[6] = Ω[6]

I −
1
12(Ω[6])2

I −
1
10(Ω[6])2

= C(h) + O(h7).
(271)
Three matrix–matrix products are required in addition to the three commutators involved in the computation of Ω[6], for a
total of nine matrix–matrix products per step.
5.5. Numerical illustration: The Rosen–Zener model revisited
Next we apply the previous numerical schemes to the integration of the differential equation governing the evolution of
a particular quantum two-level system. Our purpose here is to illustrate the main issues involved, and compare the different
approximations obtained with both the analytical treatment done in Section 4 and the exact result. Specifically, we consider
the Rosen–Zener model in the Interaction Picture already analyzed in Section 4.1.2. In this case, the equation to be solved is
U′
I = ˜HI(t)UI, or equivalently, Eq. (223) with Y(t) = UI(t) and coefficient matrix (¯h = 1)
A(t) = ˜HI(t) = −iV(s) (σ1 cos(ξs) −σ2 sin(ξs)) ≡−i b(s) · σ.
(272)
Here V(s) = V0/ cosh(s), ξ = ωT and s = t/T. Given the initial condition |+⟩≡(1, 0)T at t = −∞, our purpose is to get
an approximate value for the transition probability to the state |−⟩≡(0, 1)T at t = +∞. Its exact expression is collected
in the first line of Eq. (204), which we reproduce here for the reader’s convenience:
Pex = |(UI)12(+∞, −∞)|2 =
sin2 γ
cosh2(πξ/2),
(273)
with γ = πV0T.
To obtain, in practice, a numerical approximation to Pex, we have to integrate the equation in a sufficiently large time
interval. We take the initial condition at s0 = −25 and the numerical integration is carried out until sf = 25. Then, we
determine (UI)12(sf , s0).
As a first numerical test, we take a fixed (and relatively large) time step h such that the whole numerical integration in the
time interval s ∈[s0, sf ] is carried out with 50 evaluations of the vector b(s) for all methods. In this way, their computational
cost is similar.
To illustrate the qualitative behavior of Magnus integrators in comparison with standard Runge–Kutta schemes, the
following methods are considered:
• Explicit first-order Euler (E1): Yn+1 = Yn + hA(tn)Yn with tn+1 = tn + h and h = 1 (solid lines with squares in the
figures).
• Explicit fourth-order Runge–Kutta (RK4), i.e., scheme (227) with h = 2, since only two evaluations of b(s) per step are
required in the linear case (solid lines with triangles).
• Second-order Magnus (M2): we consider the midpoint rule (one evaluation per step) to approximate Ω1 taking h = 1
(dashed lines), i.e.,
Yn+1 = exp (−ih bn · σ) Yn =

cos(hbn)I −i
sin(hbn)
hbn
bn · σ

Yn
(274)
with bn ≡b(tn + h/2) and bn = ∥bn∥. The trapezoidal rule is equally valid by considering bn ≡(b(tn) + b(tn + h))/2.
• Fourth-order Magnus (M4). Using the fourth-order Gauss–Legendre rule to approximate the integrals and taking h = 2,
one has the scheme (254) which, for this problem, reads
b1 = b(tn + c1h),
b2 = b(tn + c2h),
d =
h
2 (b1 + b2) −h2
√
3
6
i(b1 × b2)
(275)
Yn+1 = exp (−ih d · σ) Yn
with c1 = 1
2 −
√
3
6 , c2 = 1
2 +
√
3
6 (dotted lines).
We choose ξ = 0.3 and ξ = 1, and each numerical integration is carried out for different values of γ in the range
γ ∈[0, 2π]. We plot the corresponding approximations to the transition probability in a similar way as in Fig. 7 for the
analytical treatment. Thus we obtain the plots of Fig. 14. As expected, the performance of the methods deteriorates as γ
increases. Notice, also, that the qualitative behavior of the different numerical schemes is quite similar as that exhibited
by the analytical approximations. Euler and Runge–Kutta methods do not preserve unitarity and may lead to transition
probabilities greater than 1 (just like the standard perturbation theory). On the other hand, for sufficiently small values of
γ (inside the convergence domain of the Magnus series) the fourth-order Magnus method improves the result achieved by
the second-order, whereas for large values of γ , a higher order method does not necessarily lead to a better approximation.
S. Blanes et al. / Physics Reports 470 (2009) 151–238
209
Fig. 14. Rosen–Zener model: Transition probabilities as a function of γ , with ξ = 0.3 and ξ = 1. The curves are coded as follows. Solid line represents the
exact result; E1: solid lines with squares; RK4: solid lines with triangles; M2: dashed lines; M4: dashed-broken lines (indistinguishable from exact result
in left panel).
Fig. 15. Rosen–Zener model: Transition probabilities as a function of ξ, with γ = 2 and γ = 5. Lines are coded as in Fig. 14.
In Fig. 15 we repeat the experiment, now taking γ = 1 and γ = 2, and for different values of ξ. In the first case, only the
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
To illustrate this issue, in Fig. 16 we collect the efficiency plots of the previous schemes when ξ = 0.3 with γ = 10
(left) and γ = 100 (right). We have also included the results obtained by several higher order integrators, namely the
sixth-order RK method (RK6) whose coefficients are collected in (229) and the sixth-order Magnus integrator (M6) given
210
S. Blanes et al. / Physics Reports 470 (2009) 151–238
Fig. 16. Rosen–Zener model: Error in the transition probabilities versus the number of evaluations of the Hamiltonian HI(s) for ξ = 0.3 and γ = 10 (left
panel) and γ = 100 (right panel).
by (251) and (257). We clearly observe that the Euler method is, by far, the worst choice if accurate results are desired.
Notice the (double) logarithmic scale of the plots: thus, for instance, when γ = 10 the range goes approximately from
300 to 3000 evaluations of A(t). Magnus integrators, in addition to providing results in SU(2) by construction (as the exact
solution), show a better efficiency than Runge–Kutta schemes for these examples, and this efficiency increases with the value
of γ considered. The implicit Runge–Kutta–Gauss–Legendre methods (237) show slightly better results than the explicit RK
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
both cases the Gauss–Legendre quadrature. The results obtained are collected in Fig. 17. We clearly observe that the relative
performance of the Cayley method deteriorates by increasing the value of γ similarly to the RK6. In spite of preserving the
qualitative properties, this example shows that for some problems, polynomial or rational approximations do not perform
efficiently. Here, in particular, the Magnus scheme is slightly more efficient than the symmetric Fer method, although for
other problems their performance is quite similar.
