---
doc_id: arxiv-2212.04436v1
doc_title: "Dilute neutron star matter from neural-network quantum states"
section_id: page-001
section_title: "Page 1"
section_number: null
pages: 1-1
source_pdf: 2212.04436v1.pdf
source_sha256: 0f98a851d030ec05
toc_source: undetermined
doc_brief: "Dilute neutron star matter from neural-network quantum states — 6 sections: Page 1; Page 2; Page 3"
---
Dilute neutron star matter from neural-network quantum states
Bryce Fore,1 Jane M. Kim,2 Giuseppe Carleo,3 Morten Hjorth-Jensen,2, 4 and Alessandro Lovato5, 6, 7
1Physics Division, Argonne National Laboratory, Argonne, IL 60439, USA
2Department of Physics and Astronomy and Facility for Rare Isotope Beams,
Michigan State University, East Lansing, MI 48824, USA
3Institute of Physics, ´Ecole Polytechnique F´ed´erale de Lausanne (EPFL), CH-1015 Lausanne, Switzerland
4Department of Physics and Center for Computing in Science Education, University of Oslo, N-0316 Oslo, Norway
5Physics Division, Argonne National Laboratory, Argonne, IL 60439
6Computational Science Division, Argonne National Laboratory, Argonne, IL 60439
7INFN-TIFPA Trento Institute of Fundamental Physics and Applications, 38123 Trento, Italy
(Dated: December 9, 2022)
Low-density neutron matter is characterized by fascinating emergent quantum phenomena, such
as the formation of Cooper pairs and the onset of superﬂuidity.
We model this density regime
by capitalizing on the expressivity of the hidden-nucleon neural-network quantum states combined
with variational Monte Carlo and stochastic reconﬁguration techniques. Our approach is competitive
with the auxiliary-ﬁeld diﬀusion Monte Carlo method at a fraction of the computational cost. Using
a leading-order pionless eﬀective ﬁeld theory Hamiltonian, we compute the energy per particle of
inﬁnite neutron matter and compare it with those obtained from highly realistic interactions. In
addition, a comparison between the spin-singlet and triplet two-body distribution functions indicates
the emergence pairing in the 1S0 channel.
Introduction.
Multi-messenger astronomy has opened
new windows into the state of matter at densities and
isospin asymmetries that cannot be directly probed
by terrestrial experiments [1–4]. Concurrently, nuclear
many-body theory has made considerable progress in
computing the nucleonic-matter equation of state at den-
sities corresponding to the inner core of neutron stars
starting from realistic Hamiltonians [5–10]. Comparisons
between theoretical predictions and astrophysical obser-
vation pose stringent constraints on models of nuclear
dynamics, particularly three-nucleon forces [11].
In this work, we focus on lower densities, ρ ≲0.04
fm−3, which are relevant to the phenomenology of the
stellar inner crust and outer core. In this region, both
conditions for superﬂuidity — strong Fermi degeneracy
and an attractive interaction between neutron pairs in
the 1S0 channel — are believed to be met [12–14]. In
addition to lowering the system’s energy, the formation of
Cooper pairs plays a critical role in neutrino emission [15,
16], and the phenomenology of glitches [17]. Pairing is
also relevant in modeling neutron-rich nuclei, which are
the subject of intense experimental activities [18].
Quantum Monte Carlo approaches [19], and in partic-
ular the auxiliary-ﬁeld diﬀusion Monte Carlo (AFDMC)
method [20] have been extensively applied to accurately
compute neutron-matter properties [6, 7, 21]. In the low-
density regime, AFDMC calculations have convincingly
shown a depletion of the superﬂuid gap with respect to
the Bardeen–Cooper–Schrieﬀer theory [22, 23]. However,
because of the fermion sign problem, AFDMC predic-
tions depend upon the starting variational wave function.
For instance, the superﬂuid phase must be assumed a pri-
ori by using pfaﬃan wave functions [24].
Neural-network
quantum
states
[25]
(NQS)
have
gained popularity in solving the Schr¨odinger equation
of atomic nuclei both in real space [26–30] and in the
occupation-number formalism [31]. In this work, we in-
troduce a periodic NQS suitable to model both the nor-
mal and superﬂuid phases of neutron matter. The ansatz
is based on the “hidden-nucleon” architecture, which can
model the ground-state wave functions of nuclei up to
16O with high accuracy [29]. Inspired by chemistry ap-
plications [32, 33], we further improve the expressivity
of the hidden-nucleon NQS using generalized backﬂow
correlations, which generalize both the pfaﬃan and the
spin-dependent backﬂow of Ref. [34].
Our model of nuclear dynamics is the leading-order
pionless eﬀective ﬁeld theory (/πEFT) Hamiltonian of
Ref. [35], which qualitatively reproduces the binding en-
ergies of nuclei with up to A = 90 nucleons. Arguments
based on the expansion around the unitary limit [36],
and Brueckner-Hartree-Fock calculations of inﬁnite nu-
clear matter [37], indicate that /πEFT should provide ac-
curate energies of dilute neutron matter. We test this
hypothesis by comparing the /πEFT energy per particle
against the sophisticated Argonne v18 [38] plus Urbana
IX [39] (AV18+UIX) Hamiltonian used in the Akmal-
Pandharipande-Ravenhall (APR) [40] equation of state.
To better quantify the role of dynamical correlations,
we evaluate the two-body spatial distribution functions,
separating the spin-triplet and spin-singlet channels. We
analyze the self-emergence of pairing correlations, not
explicitly included in the NQS ansatz, as a function of
neutron-matter density.
Method.
We model the interactions among neutrons
through the leading-order /πEFT Hamiltonian “o” of
Ref. [35]. The two-body contact potential is designed to
reproduce the np scattering lengths and eﬀective ranges
in the S/T = 0/1 and 1/0 channels. Thus, it yields a
neutron-neutron scattering length of ann = −22.5 fm,
arXiv:2212.04436v1  [nucl-th]  8 Dec 2022
