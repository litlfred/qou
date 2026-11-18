---
doc_id: arxiv-1406.4088v2
doc_title: "Ab initio calculation of the neutron-proton mass difference"
section_id: sec-009-4-finite-volume-and-lattice-spacing-corrections
section_title: "Finite-volume and lattice-spacing corrections in QED: numerical investigations"
section_number: 4
pages: 23-24
source_pdf: 1406.4088v2.pdf
source_sha256: d8f2ff1efb5bea30
toc_source: outline
doc_brief: "Ab initio calculation of the neutron-proton mass difference — 27 sections: Front matter; 1; Outline"
---
Finite-volume and lattice-spacing corrections in QED: numerical in-
vestigations
The results of this section serve to verify the implementation of the QED part of our simulation, which is
one of the novel features of this work. The inﬁnite volume and continuum extrapolations will be shown to
be under control. Both extrapolations from the numerical data yield results that are consistent with analytical
calculations.
Our QED setup is obtained from the full case by setting the gluon ﬁelds to U = 1. Since we focus on the
order e2 behavior, we will use the quenched QED approximation in this illustrative section, which is correct up
to e4 effects. We take e =
p
4π/137 and a fermion charge of q = 1 unless stated otherwise. In some cases we
switch off the clover improvement and/or the photon ﬁeld smearing.
The ﬁeld conﬁguration generation in the absence of fermion loops can be done by a heatbath algorithm.
Using a normal Gaussian distributed random vector ηµ, a Feyman-gauge ﬁeld conﬁguration with the right
distribution is given by Aµ,k = |ˆk|−1ηµ,k. This is then ﬁxed to Coulomb-gauge by the operator in Eq. (S4).
Let us ﬁrst take a look at the effective mass of a fermion in the two different realizations of ﬁnite volume
QED: QEDTL and QEDL (see Fig. S2). The difference is in the zero-mode removal prescription. The following
parameters were used: spatial box size L = 4, bare Wilson mass m = 0.4, no clover improvement, no smearing.
In QEDTL no clear plateaus can be seen, moreover increasing the time extent also increases the mass values.
This is in complete agreement with the analytical ﬁnding of Sec. 3: the mass diverges in the inﬁnite time extent
limit, if the spatial box size is kept ﬁxed. This of course makes the conventional mass extraction procedure,
which examines the asymptotic behavior of the propagator, ambiguous in this scheme. If instead we work with
the zero-mode prescription of QEDL, we get masses that are insensitive to the time extent of the lattice, as
predicted.
Now let us consider the ﬁnite size dependence of the fermion mass (see Fig. S3). For the plot we used a
bare Wilson mass of m = 0.2, clover improvement and smearing. The points with ﬁlled symbols are obtained
in the QEDL formulation. We also extract masses using data in the QEDTL setup, though identiﬁcation of the
plateaus is sometimes unclear, as discussed above. These are the open symbols on the plot and correspond to
three different aspect ratios. The masses change with T at a ﬁxed spatial volume. We ﬁt the results of QEDL
and QEDTL together to the analytical formulae of Eqs. (S22) and (S24) with a single ﬁt parameter, which is the
inﬁnite volume fermion mass. A good quality ﬁt can be achieved, if we restrict the boxes to a/L < 0.04. The
results are the solid lines on the plot. The small disagreements for smaller boxes can probably be explained
by exponentially small ﬁnite size corrections, which are neglected in the formulae. The data has sufﬁcient
precision to determine the coefﬁcient of the 1/L3 term. It strongly favors the one that we ﬁnd by analytic
calculation in Eq. (S24) over the one obtained by reducing the composite-particle result of (32) to the point-
particle case. 2 Fitting the numerical results to the formula of (32) leads to a χ2/dof = 1.4. A ﬁt of the
2We perform this reduction by setting the charge radius and all other coefﬁcients which reﬂect the composite nature of the
particle to zero.
reduced, NNLO expression of (32) to the QEDL points gives a χ2/dof= 15. These ﬁts are shown in Fig. S3
with solid/dotted lines. Including also the small volumes in the analysis (dashed lines) the χ2/dof is increased
by a factor of 2.5 for Eq. (S24), whereas the formula of (32) provides a χ2/dof well over 100.
Now let us turn our attention to the lattice artefacts of our QED lattice action. In order to carry out a lattice
spacing scaling study, we need two observables: one which sets the lattice spacing and another which has a
non-trivial continuum limit3. For the ﬁrst the obvious choice is the fermion mass, in a given ﬁnite box. We
denote it mL. For the second we take the ﬁnite volume correction: the difference of mL to the mass measured
on a lattice with twice the spatial extent, denoted by m2L. We set the box size as LmL = 2 and work in the
QEDL formulation. The result is shown in Fig. S4. The ﬁlled/open points are obtained with/without clover
improvement and smearing. In the unimproved case we use two functions to extrapolate into the continuum:
one is linear and the other is linear-plus-quadratic in the lattice spacing. For the improved case a quadratic
function is plotted, but the data is even consistent with a constant after ignoring the result from the coarsest
lattice. A continuum value can also be obtained analytically using the results of the previous section. At a
mass of LmL = 2 the exponential corrections cannot be neglected. Thus we compute the L(m2L −mL) using
Eq. (S7) and evaluating the relevant integrals and sums in Eq. (S15) numerically instead of using the asymptotic
formulae. This is the crossed circle on the plot. Both the unimproved and the improved results agree with the
analytical formula, though the unimproved has a much larger systematic error coming from the continuum
extrapolation.
Finally in order to further support our QED setup, we compare the inﬁnite volume extrapolated fermion
masses at ﬁnite lattice spacing to analytical results from the literature. In (31) Mertens, Kronfeld and El-
Khadra calculated the pole position of the fermion propagator for arbitrary Wilson mass, clover coefﬁcient and
to leading order in e2. For the comparison we used the QEDL formulation, clover improvement and unsmeared
photons. The bare Wilson mass was set to am = 0.2. We carried out the inﬁnite volume extrapolation using
the analytical ﬁnite volume formula, Eq. (S22). There is a small discrepancy at the standard coupling value,
e =
p
4π/137. To demonstrate, that it is an O(e4) effect, we carried out simulations at two other coupling
values. The inﬁnite volume extrapolated results are recorded in Tab. S1. The difference to the analytical result
is consistent with being an e4 correction.
