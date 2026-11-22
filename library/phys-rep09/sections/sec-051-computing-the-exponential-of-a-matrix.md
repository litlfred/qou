---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-051-computing-the-exponential-of-a-matrix
section_title: "Computing the exponential of a matrix"
section_number: null
pages: 60-61
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
We have seen that the numerical schemes based on the Magnus expansion provide excellent results when applied to Eq.
(223) with coefficient matrix (272). In fact, they are even more efficient than several Runge-Kutta algorithms. Of course,
for this particular example, the number of A(t) evaluations is a good indication of the computational cost required by the
numerical schemes, since the evaluation of exp({2) can be done analytically by means of formula (18). In general, however,
the matrix exponential also has to be approximated numerically, and thus the performance of the numerical integration
algorithms based on the Magnus expansion strongly depends on this fact. It may be that the evaluation of exp(C), where C
is a (real or complex) N x N matrix, represents the major factor in the overall computational cost required by this class of
algorithms and is probably one of the most problematic aspects.

As a matter of fact, the approximation of the matrix exponential is among the oldest and most extensively researched
topics in numerical mathematics. Although many efficient algorithms have been developed, the problem is still far from
being solved in general. It seems, then, reasonable to briefly summarize here, some of the most widely used procedures in
this context.

Let us begin with two obvious but important remarks. (i) First, one has to distinguish whether it is necessary to
evaluate the full matrix exp(C) or only the product exp(C)v for some given vector v. In the latter case, special algorithms
can be designed, requiring a much reduced computational effort. This is especially true when C is large and sparse
S. Blanes et al. / Physics Reports 470 (2009) 151-238 211

(E=0.3,7=10) (€=0.3,y=100)

AKE

Cayley6

Fer
Magnus-6 |

e e
i] wu
DB BD
° °
Ss 4
3 3.2 3.4 3.6 3.8 4
Log(Evaluations) Log(Evaluations)

Fig. 17. Rosen-Zener model: Same as Fig. 16 where we compare the performance of the 6th-order Magnus, symmetric-Fer, Cayley and RK6.

(as often happens with matrices arising from the spatial discretization of partial differential equations). (ii) Second, for
the numerical integration methods based on ME, one has to compute exp(C(h)), where C(h) = O(h?), h is a (not too large)
step size and p > 1. In other words, the matrices to be exponentiated typically have a small norm (usually restricted by the
convergence bounds of the expansion).

In any case, prior to the computation of exp(C), it is important to have as much information about the exponent C as
possible. Thus, for instance, if the matrix C resides in a Lie algebra, then exp(C) belongs to the corresponding Lie group
and one has to decide whether this qualitative property has to be exactly preserved, or if constructing a sufficiently accurate
approximation (e.g., at a higher order than the order of the integrator itself) is enough. Also, when C can be split into different
parts, one may consider a factorization of the form exp(C) * exp(C;) exp(C2) - -- exp(Cm) if each individual exponential is
easy to evaluate exactly.

An important reference in this context is [138] and its updated version [139], where up to nineteen (or twenty
in [139]) different numerical algorithms for computing the exponential of a matrix are carefully reviewed. An extensive
software package for computing the matrix exponential is Expokit, developed by R. Sidje, with Fortran and Matlab versions
available [140,141]. In addition to computing the matrix-valued function exp(C) for small, dense matrices C, Expokit has
functions for computing the vector-valued function exp(C)v for both small, dense matrices and large, sparse matrices.
