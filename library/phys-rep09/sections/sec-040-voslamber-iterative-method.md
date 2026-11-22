---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-040-voslamber-iterative-method
section_title: "Voslamber iterative method"
section_number: null
pages: 46-47
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
Just to keep the same structure as in preceding subsections, we mention that the Voslamber iterative method of
Section 3.1 also yields the exact solution for the linearly driven harmonic oscillator after computing the second iteration.

Next, for the two-level system with a rectangular step, described by the Hamiltonian (194), we compute the second iterate
2 and compare with second order ME approximation for U;. As a test, we shall again obtain the transition probability P(t)
given by (196). The expression (193) will be calculated here, assuming: U; ~ exp 2‘ = exp 2;, U; © exp(Qy + 22) and
U, ~ exp 2”.

The second order Magnus approximation to the transition probability is given by (201), whereas the second iterate is
obtained from (124),

2%) =-i% ie {[sin?(A) + cos?(A) cos €] 0; + cos?(A) sin € og — sin(2A) sin(€/2) o3}dé, (217)
@ Jo

where A = ral sin(&/2)|, y = Vot/h, € = at. Since it does not seem possible to derive an analytical expression for 2,

the corresponding matrix elements have been computed by approximating the integral in (217) with a sufficiently accurate
quadrature.
S. Blanes et al. / Physics Reports 470 (2009) 151-238 197

Exact

— — - Fer/Wilcox-1
- Fer-2
—-—- Fer-3

0.6 4

0.44

Transition Probability (E=1)

0.24

0.0

Fig. 11. Rectangular step: Transition probability as a function of y, with € = 1. Lines are coded as in Fig. 9. Computations up to third order, in the Interaction
Picture.

10 ——
Exact
ax, S81) —-—-- Iterative 2
Q
VY — — — Magnus 2
=
2Po065s \\e tee 1st order
a
o
8
2
o
c 044
i]
a
2
£
* 024
0.0
0

Fig. 12. Rectangular step: Transition probability in the two level system as a function of €, for y = 1.3: Exact result (204) (solid line), second iterate of
Voslamber method (dashed line), second order ME (dotted line) and first Voslamber iterate (or order in ME) (dash-dotted line). Computations are done in
the Interaction Picture.

In Fig. 12, the various approximated transition probabilities, as well as the exact result (196), have been plotted as a
function of € for a fixed value y = 1.5. We observe that the approximation from the second iterate keeps the trend of the
exact solution in a better way than the second order Magnus approximation does.

In Fig. 13 we have plotted the corresponding transition probabilities versus y for fixed value € = 1. Although locally, the
second order Magnus approximation may be more accurate, it seems that the trend of the exact solution is mimicked for a
longer interval of y.

As it has already been pointed out above, the Magnus expansion works better the more sudden the perturbation. Thus,
the re-summation involved in the iterative method slightly improves that issue. Further results on the present example may
be found in [93].
