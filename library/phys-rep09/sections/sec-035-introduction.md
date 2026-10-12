---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-035-introduction
section_title: "Introduction"
section_number: null
pages: 48-52
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
The Magnus expansion, as formulated in Section 2, has found extensive use in mathematical physics, quantum chemistry,
control theory etc, essentially as a perturbative tool in the treatment of the linear equation
Y ′ = A(t)Y,
Y(t0) = Y0.
(223)
When the recurrence (49)–(50) is applied, one is able to explicitly get the successive terms Ωk in the series, defining Ωas
linear combinations of multivariate integrals containing commutators acting iteratively on the coefficient matrix A, as in
S. Blanes et al. / Physics Reports 470 (2009) 151–238
199
(42)–(46). As a result, with this scheme, analytical approximations to the exact solution are constructed explicitly. These
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
The second drawback is the increasingly complex structure of the terms Ωk in the Magnus series: each Ωk is a k-
multivariate integral involving a linear combination of (k −1)-nested commutators of A evaluated at different times ti,
i = 1, . . . , k. Although in some cases these expressions can be computed explicitly (for instance, when the elements of
A and its commutators are polynomial or trigonometric functions), in general a special procedure has to be designed to
approximate multivariate integrals and reduce the number of commutators involved.
When the entries of the coefficient matrix A(t) are complicated functions of time or they are only known for certain
values of t, numerical approximation schemes are unavoidable. In many cases, it is thus desirable to obtain numerical
approximations to the exact solution at many different times. This section is devoted precisely to the Magnus series
expansion as a tool for building numerical integrators for Eq. (223).
Before embarking on exposing the technical details contained in this construction, let us first introduce several concepts
which are commonplace in the context of the numerical integration of differential equations.
Given the general (nonlinear) ordinary differential equation (ODE)
x′ = f(t, x),
x(t0) = x0 ∈Cd,
(224)
standard numerical integrators, such as Runge–Kutta and multistep methods, proceed as follows. First the whole time
interval [t0, tf ], is split into N subintervals, [tn−1, tn], n = 1, . . . , N, with tN = tf , and subsequently the value of x(tn)
is approximated with a time-stepping advance procedure of the form
xn+1 = Φ(hn, xn, . . . , h0, x0)
(225)
starting from x0. Here the map Φ depends on the specific numerical method and hn = tn+1 −tn are the time steps. For
simplicity in the presentation, we consider a constant time step h, so that tn = t0 + n h. In this way, one gets xn+1 as an
approximation to x(tn+1). In other words, the exact evolution of the system (224) is replaced by the discrete or numerical
flow (225). The simplest of all numerical methods for (224) is the explicit Euler scheme
xn+1 = xn + h f(tn, xn).
(226)
It computes approximations xn to the values x(tn) of the solution using one explicit evaluation of f at the already computed
value xn−1. In general, the numerical method (225) is said to be of order p if, assuming xn = x(tn), then xn+1 = x(tn+1) +
O(hp+1). Thus, in particular, Euler method is of order one.
Of course, more elaborate and efficient general purpose algorithms, using several f evaluations per step, have been
proposed along the years for the numerical treatment of Eq. (224). In fact, any standard software package and program
library contains dozens of routines aimed at providing numerical approximations with several degrees of accuracy, including
(explicit and implicit) Runge–Kutta methods, linear multistep methods, extrapolation schemes etc, with fixed or adaptive
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
We first summarize the main features of the well know class of Runge–Kutta methods as representative of integrators
of the form (225). They are introduced for the general nonlinear ODE (224) and are subsequently adapted to the linear
case (223).
200
S. Blanes et al. / Physics Reports 470 (2009) 151–238
5.2. Runge–Kutta methods
The Runge–Kutta (RK) class of methods are possibly the most frequently used algorithms for numerically solving ODEs.
Among them, perhaps the most successful during more than half a century has been the 4th-order method, which, applied
to Eq. (224), provides the following numerical approximation for the integration step tn 7→tn+1 = tn + h:
Y1 = xn
Y2 = xn +
h
2
f(tn, Y1)
Y3 = xn +
h
2
f

tn +
h
2, Y2

(227)
Y4 = xn + hf

tn +
h
2, Y3

xn+1 = xn +
h
6

f(tn, Y1) + 2f

tn +
h
2, Y2

+ 2f

tn +
h
2, Y3

+ f(tn + h, Y4)

.
Notice that the function f can always be computed explicitly because each Yi depends only on the Yj, j < i, previously
evaluated. To measure the computational cost of the method, it is usual to consider that the evaluation of the function f(t, x)
is the most consuming part. In this sense, scheme (227) requires four evaluations, which is precisely the number of stages
(or inner steps) in the algorithm.
The general class of s-stage Runge–Kutta methods are characterized by the real numbers aij, bi (i, j = 1, . . . , s) and
ci = Ps
j=1 aij, as
Yi = xn + h
s
X
j=1
aij f(tn + cjh, Yj),
i = 1, . . . , s
xn+1 = xn + h
s
X
i=1
bi f(tn + cih, Yi),
(228)
where Yi, i = 1, . . . , s are the intermediate stages. For simplicity, the associated coefficients are usually displayed with the
so-called Butcher tableau [125,126] as follows:
c1
a11
. . .
a1s
...
...
...
cs
as1
. . .
ass
b1
. . .
bs
(229)
If aij = 0, j ≥i, then the intermediate stages Yi can be evaluated recursively and the method is explicit. In that case, the
zero aij coefficients (in the upper triangular part of the tableau) are omitted for clarity. With this notation, ‘the’ 4th-order
Runge–Kutta method (227) can be expressed as
0
1
2
1
2
1
2
0
1
2
1
0
0
1
1
6
2
6
2
6
1
6
(230)
Otherwise, the scheme is implicit and requires one to numerically solve a system of s d nonlinear equations of the form
y = Xn + h G(h, y),
(231)
where y = (Y1, . . . , Ys)T, Xn = (xn, . . . , xn)T ∈Rsd, and G is a function which depends on the method. A standard procedure
to get xn+1 from (231) is applying simple iteration:
y[j] = Xn + h G(h, y[j−1]),
j = 1, 2, . . . .
(232)
When h is sufficiently small, the iteration starts with y[0] = Xn and stops once ∥y[j] −y[j−1]∥is smaller than a prefixed
tolerance. Of course, more sophisticated techniques can be used [126].
After these general considerations, let us now turn our attention to the linear equation (223). When dealing with
numerical methods applied to this equation, it is important to keep in mind that the relevant small parameter here is no
longer the norm of the matrix A(t) as in the analytical treatment, but the time step h. For this reason, the concept of order of
S. Blanes et al. / Physics Reports 470 (2009) 151–238
201
accuracy of a method is different in this context. Now f(t, x) = A(t)x and the general class of s-stage Runge–Kutta methods
adopt the more compact form
Yi = xn + h
s
X
j=1
aijAjYj,
i = 1, . . . , s
xn+1 = xn + h
s
X
i=1
biAiYi,
(233)
with Ai = A(tn + cih). In terms of matrices, this is equivalent to



Y1
...
Ys



=



xn
...
xn



+ heA



Y1
...
Ys



,
witheA =


a11A1
· · ·
a1sAs
...
...
as1A1
· · ·
assAs


xn+1 = xn + h
 b1A1
· · ·
bsAs




Y1
...
Ys



,
(234)
so that the application of the method for the integration step tn 7→tn+1 = tn + h can also be written as
xn+1 =

Id + h
 b1A1
· · ·
bsAs
  Isd −heA
−1 Isd×d

xn,
(235)
where Isd×d = (Id, Id, . . . , Id)T and Id is the d × d identity matrix. For instance, taking s = 2 and using Matlab this can be
easily implemented as follows
A = [a11 ∗A1 a12 ∗A2 ; a21 ∗A1 a22 ∗A2];
x = (Id + h ∗[b1 ∗A1 b2 ∗A2] ∗((I2d −h ∗A) \ [Id Id]′)) ∗x;
where b1, b2, a11, . . . , a22 are the coefficients of the method, A1, A2 correspond to A1, A2 and Id, I2d are the identity
matrices of dimension d and 2d, respectively.
There is extensive literature regarding RK methods built for many different purposes [125,126]. It is therefore reasonable
to look for the most appropriate scheme to be used for each problem. In practice, explicit RK methods are preferred, because
its implementation is usually simpler. They typically require more stages than implicit methods and, in general, a higher
number of evaluations of the matrix A(t), although this is not always the case. For instance, the 4-stage fourth order method
(227) only requires two new evaluations of A(t) per step (A(tn + h/2) and A(tn + h)), which is precisely the minimum
number of evaluations needed by any fourth order method. In our numerical examples, we will also use the 7-stage sixth
order method with coefficients [125, p. 203-205]
0
5−
√
5
10
5−
√
5
10
5+
√
5
10
−
√
5
10
5+2
√
5
10
5−
√
5
10
−15+7
√
5
20
−1+
√
5
4
15−7
√
5
10
5+
√
5
10
5−
√
5
60
0
1
6
15+7
√
5
60
5−
√
5
10
5+
√
5
60
0
9−5
√
5
12
1
6
−5+3
√
5
10
1
1
6
0
−55+25
√
5
12
−25−7
√
5
12
5 −2
√
5
5+
√
5
2
1
12
0
0
0
5
12
5
12
1
12
(236)
Observe that this method only requires three new evaluations of the matrix A(t) per step. This is, in fact, the minimum
number for a sixth-order method. Other implicit RK schemes widely used in the literature involving the minimum number
of stages at each order are based on Gauss–Legendre collocation points [126]. For instance, the corresponding methods of
order four and six (with two and three stages, respectively) have the following coefficients:
3−
√
3
6
1
4
3−2
√
3
12
3+
√
3
6
3+2
√
3
12
1
4
1
2
1
2
5−
√
15
10
5
36
2
9 −
√
15
15
5
36 −
√
15
30
1
2
5
36 +
√
15
24
2
9
5
36 +
√
15
24
5+
√
15
10
5
36 +
√
15
30
2
9 +
√
15
15
5
36
5
18
4
9
5
18
(237)
202
S. Blanes et al. / Physics Reports 470 (2009) 151–238
