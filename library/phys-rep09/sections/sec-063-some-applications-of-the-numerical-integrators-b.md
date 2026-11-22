---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-063-some-applications-of-the-numerical-integrators-b
section_title: "Some applications of the numerical integrators based on ME"
section_number: null
pages: 71-72
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
In this section we collect several examples where the numerical integration methods based on the Magnus expansion
have been applied in the recent literature. Special attention is dedicated to the numerical integration of the Schrédinger
equation, since the Magnus series expansion has been extensively used in this setting almost since its very formulation.
The time-independent Schrédinger equation can be considered as a particular example of a Sturm-Liouville problem, so we
also review the applicability of Magnus based techniques in this context. Then we consider a particular nonlinear system
(the differential Riccati equation) which can be, in some sense, linearized, so that at the end one may work with finite-
dimensional matrices. Finally, we summarize a recent but noteworthy application: the design of new classes of numerical
schemes for the integration of stochastic differential equations.
222 S. Blanes et al. / Physics Reports 470 (2009) 151-238

OF SU,4

-1

MN,-4 s2

LOG(ERROR)

5

1.5 2 25 3 3.5
LOG(N. EVAL.)

Fig. 20. Average error versus number of force evaluations in the numerical integration of (308) using second and fourth order symplectic integrators
for general separable systems (S2 corresponds to the second order leapfrog method with coefficients (309) and SUs4 to the fourth order method with
coefficients (310)) and the fourth order symplectic Runge-Kutta-Nystr6m method MN¢-4 with initial conditions q(0) = 1.75, p(0) = Oande = 1/20,
$= 1/4,0=1.
