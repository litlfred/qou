---
doc_id: arxiv-hep-ph-9502366v1
doc_title: "Chiral Perturbation Theory"
section_id: sec-003-42-chiral-loops
section_title: "Chiral loops"
section_number: 4.2
pages: 11-13
source_pdf: 9502366v1.pdf
source_sha256: 56df064956ca03f8
toc_source: inferred
doc_brief: "Chiral Perturbation Theory — An introduction to the basic ideas and methods of Chiral Perturbation Theory is presented."
---
ChPT is a quantum ﬁeld theory, perfectly deﬁned through equation (3.19). As
such, we must take into account quantum loops with Goldstone-boson propagators
in the internal lines. The chiral loops generate non-polynomial contributions, with
logarithms and threshold factors, as required by unitarity.
The loop integrals are homogeneous functions of the external momenta and the
pseudoscalar masses occurring in the propagators.
A simple dimensional counting
shows that, for a general connected diagram with Nd vertices of O(pd) (d = 2, 4, . . .)
and L loops, the overall chiral dimension is given by (Weinberg 1979)
D = 2L + 2 +
X
d
Nd (d −2) .
(4.2)
§ Since we will only need L4 at tree level, the general expression of this Lagrangian has been simpliﬁed,
using the O(p2) equations of motion obeyed by U. Moreover, a 3 × 3 matrix relation has been used
to reduce the number of independent terms.
For the two-ﬂavour case, not all of these terms are
independent (Gasser and Leutwyler 1984, 1985).
Each loop adds two powers of momenta; this power suppression of loop diagrams is at
the basis of low-energy expansions, such as ChPT. The leading D = 2 contributions
are obtained with L = 0 and d = 2, i.e. only tree-level graphs with L2 insertions. At
O(p4), we have tree-level contributions from L4 (L = 0, d = 4, N4 = 1) and one-loop
graphs with the lowest-order Lagrangian L2 (L = 1, d = 2).
The Goldstone loops are divergent and need to be renormalized.
Although
eﬀective ﬁeld theories are non-renormalizable (i.e.
an inﬁnite number of counter-
terms is required), order by order in the momentum expansion they deﬁne a perfectly
renormalizable theory.
If we use a regularization which preserves the symmetries
of the Lagrangian♯, such as dimensional regularization, the counter-terms needed to
renormalize the theory will be necessarily symmetric. Since by construction the full
eﬀective Lagrangian contains all terms permitted by the symmetry, the divergences
can then be absorbed in a renormalization of the coupling constants occurring in the
Lagrangian. At one loop (in L2), the ChPT divergences are O(p4) and are therefore
renormalized by the low-energy couplings in equation (4.1):
Li = Lr
i(µ) + Γiλ ,
Hi = Hr
i (µ) + eΓiλ ,
(4.3)
where
λ = µd−4
16π2

1
d −4 −1
2 [log (4π) + Γ′(1) + 1]

.
(4.4)
The explicit calculation of the one-loop generating functional Z4 (Gasser and
Leutwyler 1985) gives:
Γ1 = 3
32 ,
Γ2 = 3
16 ,
Γ3 = 0 ,
Γ4 = 1
8 ,
Γ5 = 3
8 ,
Γ6 = 11
144 ,
Γ7 = 0 ,
Γ8 = 5
48 ,
Γ9 = 1
4 ,
Γ10 = −1
4 ,
eΓ1 = −1
8 ,
eΓ2 = 5
24 .
(4.5)
The renormalized couplings Lr
i(µ) depend on the arbitrary scale of dimensional
regularization µ. This scale dependence is of course cancelled by that of the loop
amplitude, in any measurable quantity.
A typical O(p4) amplitude will then consist of a non-polynomial part, coming from
the loop computation, plus a polynomial in momenta and pseudoscalar masses, which
depends on the unknown constants Li. The non-polynomial part (the so-called chiral
logarithms) is completely predicted as a function of the lowest-order coupling f and
the Goldstone masses.
This chiral structure can be easily understood in terms of dispersion relations.
Given the lowest-order Lagrangian L2, the non-trivial analytic behaviour associated
with some physical intermediate state is calculable without the introduction of
new arbitrary chiral coeﬃcients.
Analyticity then allows us to reconstruct the
♯
A rather comprehensive analysis of diﬀerent regularization schemes in ChPT has been given by
Espriu and Matias (1994).
full amplitude, through a dispersive integral, up to a subtraction polynomial.
ChPT generates (perturbatively) the correct dispersion integrals and organizes the
subtraction polynomials in a derivative expansion.
ChPT is an expansion in powers of momenta over some typical hadronic scale,
usually called the scale of chiral symmetry breaking Λχ. The variation of the loop
contribution under a rescaling of µ, by say e, provides a natural order-of-magnitude
estimate∗of Λχ (Weinberg 1979, Manohar and Georgi 1984): Λχ ∼4πfπ ∼1.2 GeV.
