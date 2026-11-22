---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-062-the-general-nonlinear-problem
section_title: "The general nonlinear problem"
section_number: null
pages: 70-71
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
In principle, it is possible to adapt all methods built for linear problems to the general nonlinear non-autonomous
equation (159)

x’ = f(t, x),
or equivalently, the operator differential equation (160),

fore ot, =
a? 7 fy) Y= Xo.

As we pointed out in Section 3.4, there are two problematic aspects when designing practical numerical schemes based on
Magnus expansion in the nonlinear case. The first one is how to compute or approximate the truncated Magnus expansion
(or its action on the initial conditions). The second one is how to evaluate the required Lie transforms. For example, to
compute the Lie transform exp(tLy)) acting on y is equivalent to solving the autonomous differential equation x’ = f(x) at
t = hwith x(0) = y, or x(t) = exp(tLtx,))Xo where Xp = y can be considered as a set of coordinates.

Very often, the presence of Lie brackets in the exponent leads to fundamental difficulties, since the resulting vector
fields usually have very complicated structures. Sometimes, however, this problem can be circumvented by using the same
techniques, leading to commutator-free Magnus integrators in the linear case. In any case, one should bear in mind that the
action of the exponentials in the methods designed for the linear case has to be replaced by their corresponding maps.
Alternatively, if the method is formulated in terms of Lie transforms, the order of the exponentials has to be reversed,
according to Eq. (155).

Next we illustrate how to numerically solve the problem

x’ = f, (t,x) + f(t, x) (305)

using the scheme (299) with (303) and the coefficients aj, bj taken from MN¢-4 in Table 1.
Let us consider the Duffing equation

q’ +eq +q°—q=dcos(wt) (306)
S. Blanes et al. / Physics Reports 470 (2009) 151-238 221

Table 2
Algorithms for the numerical integration of (307) or (308): (Algorithm 1) with scheme (298), and (Algorithm 2) with scheme (302).
Algorithm 1: Standard split Algorithm 1: Magnus split
Go = (tn); Po = P(tn):
qo = (tn); Po = P(tn); do i=1,k ,
Shot TP) =T'( +h); Vi@ =V' Gy +ah, 4)
1,m enddo
Pi-1 — haiV' (ta, gi-1) ch t= than
ta + ha; Vi(q) = oi V,(@) +--- + oY (Q)
Gi-1 + AbiT' (ty, pi) Tip) = paT{(P) +--+ + pint (P)
ty = ty + hb; i—1 — AVi(Gi-1)
pet Gi = 1 + AT»)
enddo
which can be obtained from the time-dependent Hamiltonian
—et 1 2 et 1 4 1 2
AGP O=TRH+VG) =e" sp +e" | aa — 54 — dcos(wt)q (307)

or equivalently from

d fq T'(t, p) ep 0
dt {3| = [ne af~) 0 [> e'(q—q?+Scos(wt)) f° (308)
Notice that this system already has the form (305), each part being exactly solvable. In consequence, the splitting method

shown in (298) can be used here. The procedure is described as Algorithm 1 in Table 2.
Observe that the leap-frog composition (281) corresponds to m = 2 and

aq=a=-, b; = 1, b, = 0. (309)

Since by = O one stage can be saved (with a trivial modification of the algorithm) and the scheme is considered as a one
stage method. An efficient symmetric 5-stage fourth order integrator is given by the coefficients (m = 6)
gate yay, (310)
2
i=0,1,...,6 with yo = ye = Oand yy = yy = ya = ys = 1/(4— 4), yy = 1-44.

Alternatively, we can use the Magnus integrator (302). Since the kinetic energy is quadratic in momenta, we can apply
the fourth-order method MNg-4. If we take the fourth-order Gauss-Legendre quadrature rule for the evaluation of the time-
dependent function then we can consider (303), where the coefficients aj, bj are given in Table 1. Here, A(t) plays the role of
T'(t, p) and B(t) plays the role of V’(t, q) (they are not interchangeable, otherwise the performance seriously deteriorates).
The computation of one time step is shown as Algorithm 2 in Table 2.

We take € = 1/20,5 = 1/4, = 1 and initial conditions q(0) = 1.75, p(0) = 0. We integrate up tot = 107 and
measure the average error in phase space, in terms of the number of force evaluations for different time steps (in logarithmic
scale). The results are shown in Fig. 20. The scheme MN¢-4 has 6 stages per step, but only two time-evaluations. For this
reason, in the figure, we have considered, as the number of evaluations per step, both two and six (left and right curves
connected by an arrow). The superiority of the new splitting Magnus integrators for this problem is evident. If the time-
dependent functions dominate the cost of the algorithm, the superiority is even higher. Surprisingly, the method shows
better stability than the leap-frog method, which attains the highest stability possible among the splitting methods for
autonomous problems.
