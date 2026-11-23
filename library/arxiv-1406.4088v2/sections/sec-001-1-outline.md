---
doc_id: arxiv-1406.4088v2
doc_title: "Ab initio calculation of the neutron-proton mass difference"
section_id: sec-001-1-outline
section_title: "Outline"
section_number: 1
pages: 13-13
source_pdf: 1406.4088v2.pdf
source_sha256: d8f2ff1efb5bea30
toc_source: outline
doc_brief: "Ab initio calculation of the neutron-proton mass difference — 27 sections: Front matter; 1; Outline"
---
Outline
In the following sections we provide details of the work presented in the main paper. In Sec. 2 we deﬁne the
theory that we use, namely QCD and QED with four quark ﬂavors on a four dimensional lattice. After ﬁxing
our notations we discuss the action for the photon ﬁeld in Sec. 2.1. There are many subtleties here, such as
gauge ﬁxing and zero-mode subtraction. In Sec. 2.2 we deﬁne our Dirac operator, which contains both photon
and gluon ﬁelds. We apply one step of APE smearing to the electromagnetic ﬁeld and 3 steps of HEX smearing
to the SU(3) ﬁeld. In Sec. 2.3 we discuss in detail what the advantages of these choices are and how we
optimized the smearing parameters.
The determination of the mass splittings for the isospin multiplets needs a careful treatment of QED on the
lattice. In Sec. 3 we discuss in detail the differences between two possible formulations of lattice QED (28)
and illustrate numerically the disadvantages of the one used in all previous numerical studies in Sec. 4. We also
compare our numerical implementation of lattice QED with lattice perturbation theory up to O(e2) order (31)
and recover the tiny O(e4) corrections.
The photon ﬁelds are long-ranged and the mass corrections are proportional to 1/L, 1/L2, ... types, where
L is the spatial size of the system. These are much larger corrections than those in QCD, which are exponen-
tially suppressed for stable particles. Actually they are of the same order as the mass-splittings themselves. In
Sec. 3 we determine the ﬁnite-volume corrections analytically for point particles. In Sec. 5 the study is gener-
alized to the case of composite particles. Using the Ward-Takahashi identities we show that the coefﬁcients of
the 1/L and 1/L2 terms are universal 1 and we compare these analytical ﬁndings to our numerical QCD+QED
simulation results.
Starting with Sec. 6 we present the details of the many simulations that are performed and summarized here.
The use of Rational Hybrid Monte-Carlo method is discussed with a special emphasis on the lowest eigenvalues
of the Dirac operator. Autocorrelations are under control for our choice of parameters in the QCD part of our
work. However, due to the zero mass of the photon and the correspondingly large correlation lengths, a standard
Hybrid Monte-Carlo integration of the photon ﬁelds results in large autocorrelation times. We show how we
solved this problem by developing a Fourier accelerated algorithm. For the propagator calculations we used a
2-level multi-grid approach to have several hundred source positions and signiﬁcantly improve our statistics.
We present the ensembles generated for this project in Sec. 7. We use four different lattice spacings in the
range of 0.06 to 0.10 fm, and pion masses down to 195 MeV. We have runs with zero electromagnetic coupling
and with non-zero ones. Altogether we have accumulated 41 ensembles, whose parameters are detailed in that
section. In Sec. 8 we present our renormalization prescription for the electric charge.
In the ﬁnal sections, Secs. 10, 11 and 12, we detail the procedure that is used to extract mass splittings. We
explain how we separate the QED and quark-mass-difference contributions to these differences. In obtaining
our ﬁnal results, we conduct a thorough investigation of systematic uncertainties. To determine these, we use
the histogram method (16). We extend it by using the Akaike’s information criterion (AIC).
