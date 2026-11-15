---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-056-additional-numerical-examples
section_title: "Additional numerical examples"
section_number: null
pages: 64-66
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
The purpose of Section 5.5 was to illustrate the main features of the numerical schemes based on the Magnus expansion
in comparison with other standard integrators (such as Runge-Kutta schemes) and other Lie-group methods (e.g., Fer and
Cayley) on a solvable system. For larger systems the efficiency analysis is more challenging since the (exact or approximate)
computation of exponential matrices play an important role on the performance of the methods. It makes sense, then, to
analyze from this point of view, more realistic problems, where one necessarily has to approximate the exponential in a
consistent way.
S. Blanes et al. / Physics Reports 470 (2009) 151-238 215

A, = sin (t(2-42)) Aj = log (t(i-)/(i+i))

log(Error)
log(Error)

2.8 3 3.2 3.4 3.6 3.8 2 2.5 3 3.5
log(Evaluations) log(Evaluations)

Fig. 18. Efficiency diagram corresponding to the optimized 4-th (circles) and 6-th (squares) order Lie-group solvers based on Magnus (solid lines) and
Cayley (broken lines), and the standard Runge-Kutta methods (dashed lines).

As an illustration of this situation, we next consider two skew-symmetric matrices, A(t) and Y(0) = I, so that the solution
Y(t) of Y’ = A(t)Y is orthogonal for all t. In particular, the upper triangular elements of the matrices A(t) are as follows:

(a) Aj=sin(t(?-?)) 1<i<j<N (283)
(b) Aj = log (: + i) (284)

with N = 10. In both cases Y(t) oscillates with time, mainly due to the time-dependence of A(t) (in (283)) or the norm of
the eigenvalues (in (284)).

The integration is carried out in the interval t € [0, 10] and the approximate solutions are compared with the exact
one at the final time t; = 10 (obtained with very high accuracy by using a sufficiently small time step). The corresponding
error at t¢ is computed for different values of the time step h. The Lie-group solvers are implemented with Gauss-Legendre
quadratures and constant step size.

First, we plot the accuracy of the different 4-th and 6-th order methods as a function of the number of A(t) evaluations.
In contrast to the previous examples, now there is no closed formula for the matrix exponentials appearing in the Magnus
based integrators, so that some alternative procedure must be applied. In particular, the computation of e© to machine
accuracy is done by scaling-(diagonal Padé)-squaring, so that the result is correct up to round-off. Fig. 18 shows the results
obtained for the problems (283) and (284) with fourth- and sixth-order numerical schemes based on Magnus and Cayley,
and also explicit Runge-Kutta methods. In the first problem, Magnus and Cayley show a very similar performance, which
happens to be only slightly better than that of RK methods.

The situation changes drastically, however, for the second problem. Here the behavior of Cayley and RK methods is
essentially similar, whereas schemes based on Magnus are clearly more efficient. The reason seems to be that Cayley and RK
methods give poor approximations to the exponential, which, on the other hand, has to be accurately approximated, since
the eigenvalues of A(t) may take large values.

With respect to symmetric Fer methods, their efficiency is quite similar to that of Magnus if the matrix exponentials are
evaluated accurately up to machine precision. This is so for the matrix (283) even if Padé approximants of relatively low
order are used to replace the exponentials.

On the other hand, the efficiency of “Magnus-Padé” methods (we denote by MPnm a Magnus method of order n where
the exponential is approximated by a diagonal Padé of order m, and MPn if n = m) is highly deteriorated for the problem
(284), although it is always better than that corresponding to Cayley schemes.

To better illustrate all these comments, in Fig. 19 we display the error in the solution corresponding to (283) and (284)
as a function of time in the interval t € [0, 100] for h = 1/20, as is obtained by the previous methods. We should stress that
all schemes require the same number of A evaluations.

In the right picture, the exponentials appearing in the Magnus method are computed using a Padé approximant of order
six (MP6), of order eight (MP68) and to machine accuracy (M6). Observe the great importance of evaluating the exponential
as accurately as possible for the matrix (284): by slightly increasing the computational cost per step in the computation of
the matrix exponential, it is possible to dramatically improve the accuracy of the methods. On the contrary, for problem
(283) the meaningful fact seems to be that the integration scheme provides a solution in the corresponding Lie group.
216 S. Blanes et al. / Physics Reports 470 (2009) 151-238

Aj = sin (t(-4?)) b Aj = log (t(ii)/(i+i))

RK6

log(Error)
i
o
a
log(Error)

0 05 1 15 2
log(Time) log(Time)

Fig. 19. Error as a function of time (in logarithmic scale) obtained with different 6-th order integrators for h = 1/20: (a) problem (283); (b) problem (284).
