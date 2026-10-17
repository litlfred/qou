---
doc_id: arxiv-2007.15570v1
doc_title: "A quantum Monte Carlo based approach to intranuclear cascades"
section_id: sec-000-a-quantum-monte-carlo-based-approach-to-intranuc
section_title: "A quantum Monte Carlo based approach to intranuclear cascades"
section_number: null
pages: 1-2
source_pdf: 2007.15570v1.pdf
source_sha256: 6e46f4346a29fd83
toc_source: outline
---
Joshua Isaacson a, William I. Jay a, Alessandro Lovato b,c, Pedro A. N. Machado a, Noemi Rocco a,b,
aTheoretical Physics Department, Fermi National Accelerator Laboratory, P.O. Box 500, Batavia, IL 60510, USA
bPhysics Division, Argonne National Laboratory, Argonne, Illinois 60439, USA
cINFN-TIFPA Trento Institute of Fundamental Physics and Applications, Via Sommarive, 14, 38123 Trento, Italy
(Dated: July 31, 2020)
We propose a novel approach to intranuclear cascades which takes as input quantum Monte
Carlo nuclear conﬁgurations and uses a semi-classical, impact-parameter based algorithm to model
the propagation of protons and neutrons in the nuclear medium.
We successfully compare our
simulations to available proton-carbon scattering data and nuclear-transparency measurements. By
analyzing the dependence of the simulated observables upon the ingredients entering our intranuclear
cascade algorithm, we provide a quantitative understanding of their impact. Particular emphasis
is devoted to the role played by nuclear correlations, the Pauli exclusion principle, and interaction
probability distributions.
PACS numbers: 24.10.Cn,25.30.Pt,26.60.-c
I.
INTRODUCTION
The propagation of nucleons through the nuclear
medium is an important aspect of nuclear reactions,
heavy-ion collisions, and astrophysical environments. It
is also crucial in the analysis of electron-nucleus scatter-
ing experiments (see e.g. Refs. [1–10]), neutrino oscilla-
tion experiments [11–14], and dark matter searches [15].
For example, scattering of neutrinos on nuclei can pro-
duce a number of outgoing hadrons.
The multiplicity
of the recoiling hadrons can indicate statistically if the
incoming particle was more likely to be a neutrino or
anti-neutrino [16]; their momenta are correlated with the
original neutrino energy and direction, which can be used
to gather additional information, for instance, on the lep-
tonic CP phase from the sub-GeV atmospheric neutrino
samples [17] or from searches for dark matter annihila-
tion from the Sun [18, 19].
The quantitative understanding of nucleons propaga-
tion in the nuclear medium would in principle require
a fully quantum-mechanical description of the hadronic
ﬁnal state. Due to its tremendous diﬃculty, this prob-
lem has been tackled by introducing diﬀerent approxima-
tions. The seminal papers by Serber and Metropolis et.
al. [20–23] laid the foundations for the use of Monte Carlo
techniques in semi-classical intranuclear cascades (INC)
that assume classical propagation between consecutive
scatterings. The latter are modeled using free-space el-
ementary cross sections whose ﬁnal state is modiﬁed to
account for the Pauli principle. The results obtained by
these ﬁrst implementations of INC agree at least qualita-
tively with experimental data on nuclear transparencies
and the frequency and angular distribution of emitted
fast protons [21].
Experiments in heavy-ion reactions have spurred the-
oretical eﬀorts to describe the dynamical evolution of
nucleus-nucleus collisions using transport methods [24–
28] based on the Kadanoﬀ-Baym equations [29, 30].
The impossibility of solving these equations exactly on
real-world computers requires the introduction of ap-
proximations, such as the gradient expansion leading
to the Boltzmann-Uehling-Uhlenback equations (BUU).
For instance, the Giessen Boltzmann-Uehling-Uhlenback
(GiBUU) model is based on this truncated set of semi-
classical kinetic equations, which describe the dynamics
of the hadronic system explicitly in phase space and in
time [31, 32]. It can be diﬃcult to estimate systematic
eﬀects coming from the truncation of the transport equa-
tions. Although initially developed to simulate heavy-ion
collisions, GiBUU has been extended to the description
of lepton and photon scattering on nuclei [33, 34].
Over the years, several studies have been devoted to
improving the accuracy and extending the predictive
power of INC models, with a focus on the analysis of nu-
clear spallation processes, where a hadronic probe with
energy from a few tens of MeV to a few hundred MeV
strikes a nucleus [35–38].
In contrast to the standard
Glauber approach [39], where the so-called frozen approx-
imation is utilized, INC simulations explicitly account for
the motion of the background particles or scattering cen-
ters [40]. The validity of the semi-classical propagation
assumed in the INC has yet to be fully assessed. However,
genuine quantum-mechanical eﬀects can either be safely
neglected because they are expected to play a minor
role—as for coherent scattering in nuclear transparency
calculations—or they can be eﬀectively parametrized by
means of trajectory deﬂections and nuclear collective ex-
citations, as in the analysis of nuclear spallation pro-
cesses [41].
Important examples of state-of-the-art INC codes used
in hadron- and lepton-nucleus scattering analyses are the
Li`ege INC [42], NEUT [43], nuance [44], PEANUT (used
within FLUKA) [45, 46], NuWro [47], and GENIE [48]
programs. Despite some diﬀerences in technical aspects
and degree of sophistication, all the above INC models
use as input elementary cross sections and mean-ﬁeld
properties of nuclei, such as single-nucleon densities. A
notable exception is NuWro, which has recently been ex-
arXiv:2007.15570v1  [hep-ph]  30 Jul 2020
2
tended to incorporate eﬀective nucleon-nucleon correla-
tions [49].
In this work, we propose a novel cascade model that
employs nuclear conﬁgurations obtained from quantum
Monte Carlo (QMC) calculations, which retains all cor-
relation eﬀects.
The probability that the propagating
nucleon scatters with a background particle is modeled
using two diﬀerent weight functions that depend on the
impact parameter of the two nucleons and their cross sec-
tion. The nucleon-nucleon cross sections used in the sim-
ulation are taken to be the same as in vacuum; in-medium
eﬀects are partially accounted for by imposing the Pauli
exclusion principle and an eﬀective nuclear binding.
Our semi-classical approach allows for the calculation
of exclusive quantities in nuclear scattering, such as the
fully diﬀerential phase space and the number of outgoing
nucleons. To test the validity of our model, we compare
our simulations with available data on proton-nucleus
scattering cross sections and nuclear transparencies.
On the technical side, the INC code developed here
is publicly available at https://github.com/jxi24/
IntranuclearCascade.
The front-end is written in
Python 3, while computationally intensive code is writ-
ten in C++, using pybind11 to generate the interface code.
The source code is organized to be portable and modular,
making it easy to use, extend, and improve. All valida-
tions are available in the source code and can be easily
performed by the front-end user.
II.
THE PHYSICS OF THE IMPACT
PARAMETER BASED INTRANUCLEAR
CASCADE MODEL
We now discuss in detail the physical content of our
INC and how several ingredients were incorporated in
the model. The INC starts by generating a nuclear con-
ﬁguration, which describes the spatial distribution of pro-
tons and neutrons inside the nucleus. A large number of
these conﬁgurations are computed from quantum Monte
Carlo (QMC) methods [50] that use as input the highly-
realistic Argonne v18 (AV18) [51] plus Illinois 7 (IL7) [52]
Hamiltonian – more details can be found in Sec. II A. All
