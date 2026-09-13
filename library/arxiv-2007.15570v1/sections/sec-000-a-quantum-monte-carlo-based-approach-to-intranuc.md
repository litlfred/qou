---
doc_id: arxiv-2007.15570v1
doc_title: "A quantum Monte Carlo based approach to intranuclear cascades"
section_id: sec-000-a-quantum-monte-carlo-based-approach-to-intranuc
section_title: "A quantum Monte Carlo based approach to intranuclear cascades"
section_number: null
pages: 1-14
source_pdf: 2007.15570v1.pdf
source_sha256: 6e46f4346a29fd83
doc_brief: "A quantum Monte Carlo based approach to intranuclear cascades — 2 sections: Front matter; A quantum Monte Carlo based approa"
---
Joshua Isaacson a, William I. Jay a, Alessandro Lovato b,c, Pedro A. N. Machado a, Noemi Rocco a,b,
aTheoretical Physics Department, Fermi National Accelerator Laboratory, P.O. Box 500, Batavia, IL 60510, USA
bPhysics Division, Argonne National Laboratory, Argonne, Illinois 60439, USA
cINFN-TIFPA Trento Institute of Fundamental Physics and Applications, Via Sommarive, 14, 38123 Trento, Italy
(Dated: July 31, 2020)
We propose a novel approach to intranuclear cascades which takes as input quantum Monte
Carlo nuclear conﬁgurations and uses a semi-classical, impact-parameter based algorithm to model
the propagation of protons and neutrons in the nuclear medium. We successfully compare our
simulations to available proton-carbon scattering data and nuclear-transparency measurements. By
analyzing the dependence of the simulated observables upon the ingredients entering our intranuclear
cascade algorithm, we provide a quantitative understanding of their impact. Particular emphasis
is devoted to the role played by nuclear correlations, the Pauli exclusion principle, and interaction
probability distributions.
PACS numbers: 24.10.Cn,25.30.Pt,26.60.-c
I. INTRODUCTION
The propagation of nucleons through the nuclear
medium is an important aspect of nuclear reactions,
heavy-ion collisions, and astrophysical environments. It
is also crucial in the analysis of electron-nucleus scatter-
ing experiments (see e.g. Refs. [1–10]), neutrino oscilla-
tion experiments [11–14], and dark matter searches [15].
For example, scattering of neutrinos on nuclei can pro-
duce a number of outgoing hadrons. The multiplicity
of the recoiling hadrons can indicate statistically if the
incoming particle was more likely to be a neutrino or
anti-neutrino [16]; their momenta are correlated with the
original neutrino energy and direction, which can be used
to gather additional information, for instance, on the lep-
tonicCP phase from the sub-GeV atmospheric neutrino
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
strikes a nucleus [35–38]. In contrast to the standard
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
Li` ege INC [42], NEUT [43], nuance [44], PEANUT (used
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
relation eﬀects. The probability that the propagating
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
IntranuclearCascade. The front-end is written in
Python 3 , while computationally intensive code is writ-
ten in C++, using pybind11 to generate the interface code.
The source code is organized to be portable and modular,
making it easy to use, extend, and improve. All valida-
tions are available in the source code and can be easily
performed by the front-end user.
II. THE PHYSICS OF THE IMPACT
PARAMETER BASED INTRANUCLEAR
CASCADE MODEL
We now discuss in detail the physical content of our
INC and how several ingredients were incorporated in
the model. The INC starts by generating a nuclear con-
ﬁguration, which describes the spatial distribution of pro-
tons and neutrons inside the nucleus. A large number of
these conﬁgurations are computed from quantum Monte
Carlo (QMC) methods [50] that use as input the highly-
realistic Argonnev18 (AV18) [51] plus Illinois 7 (IL7) [52]
Hamiltonian – more details can be found in Sec. II A. All
particles in a nuclear conﬁguration are initially labeled as
background particles. After randomly picking a nuclear
conﬁguration, a random nucleon is selected, struck, and
labeled as a propagating nucleon. Propagating nucleons
are assumed to be point-like, on-shell particles moving at
some velocity given by their four-momentum. The spa-
tial coordinates of background nucleons are kept ﬁxed
until they interact with a propagating particle. In that
case, their momentum is sampled from either a local or
global Fermi gas distribution.
The system is evolved in time steps, which is a pa-
rameter of the cascade model, and should be chosen
small enough to simulate the cascade accurately but large
enough to run in a reasonable amount of time. At each
time step, the following procedure is performed for each
propagating
hit?
FIG. 1: Schematics of a propagating nucleon (black
circle). The distance travelled by the propagating
nucleon is depicted by a black arrow. The crosses
represent background nucleons. An interaction test
would be performed for the nucleon in red.
propagating nucleon. First, it is checked if there are any
background particles within the volume perpendicular to
the line segment deﬁned by the initial to the ﬁnal position
of a propagating particle; this is schematically shown in
Fig. 1. The impact parameter is calculated for all such
nucleons, and this list is sorted from closest to furthest.
Then an accept-reject step is performed on this list, until
either an interaction takes place or the end of the list is
reached. This test determines if an interaction occurred
according to a probability distribution. If an interac-
tion occurred, the phase space is generated using a fully
diﬀerential nucleon-nucleon cross section. The Pauli ex-
clusion principle is approximately taken into account by
comparing the magnitude of the momentum of the ﬁnal
state particles with the Fermi momentum kF (the user
can choose between either the global or the local val-
ues). The interaction takes place only if both momenta
are above kF . Otherwise, the interaction does not hap-
pen, and the propagating particle keeps its original four
momentum.
If the interaction took place, the outgoing particles are
both treated as propagating particles, and a formation
zone is set for each of them [53, 54] (see also Ref. [47]).
Note that, as a distinctive feature of our INC model, the
interaction is ﬁnite ranged and the outgoing nucleons do
not have to be at the same position in space. Finally, a
propagating particle that reaches a suﬃciently large ra-
dius may exit the nucleus if its kinetic energy overcomes
the eﬀective nuclear binding. If there is insuﬃcient en-
ergy to escape, the particle is relabeled as a background
particle. Otherwise, this eﬀective binding energy is sub-
tracted from the particle’s energy, and then the particle
is labeled as a ﬁnal particle and stops propagating. The
INC stops when there are no more propagating particles
in the nucleus.
The structure of the algorithm is summarized in Fig. 2.
In what follows, we provide the details and expressions
that are used in our impact parameter based INC.
3
Start
Generate nuclear
conﬁguration
Kick random nucleon
Evolve propagating
nucleon(s) for time δt
Possible
interaction?
Outside
nucleus?
Remove from prop-
agating particle list
Generate out-
going momenta
Pauli
Blocked?
Restore original
outgoing momenta
Update outgoing
momenta of particles
Add particle to
list and update
formation zone
No
Yes
Yes
No
Yes
No
FIG. 2: The proposed algorithm for the INC model.
A. Nuclear conﬁguration
Nuclei are complicated many-body systems of
fermions, whose structure and dynamics emerge from in-
dividual interactions among the constituent protons and
neutrons. To a remarkably large extent, the latter can
be modeled by the non-relativistic Hamiltonian
H =
∑
i
p2
i
2mN
+
∑
i<j
vij +
∑
i<j<k
Vijk, (1)
where pi denotes the momentum of thei-th nucleon with
mass mN, while vij and Vijk are the nucleon-nucleon
(NN) and three-nucleon (3 N) potentials, respectively.
We employ the highly-realistic Argonne v18 (AV18)NN
interaction [51] that includes spin, isospin, tensor, spin-
orbit and quadratic momentum-dependent terms as well
as isospin-symmetry-breaking corrections and reproduces
the Nijmegen nucleon-nucleon database with aχ2/datum
≃ 1. For the 3 N interaction, we use the Illinois-7 (IL7)
potential [52], which consists of the dominant standard
Fujita-Miyazawa two-pion exchange and smaller multi-
pion-exchange components resulting from the excitation
of intermediate ∆ resonances. The IL7 potential also con-
tains phenomenological isospin-dependent central terms.
The parameters characterizing this three-body potential
have been determined by ﬁtting the low-lying spectra of
nuclei in the mass rangeA=3–10. The overall AV18+IL7
Hamiltonian then leads to predictions of ≈ 100 ground-
and excited-state energies up toA=12, including the 12C
ground- and Hoyle-state energies, in good agreement with
the corresponding empirical values [50].
Over the last decades signiﬁcant progress has been
made in the development of ab initio nuclear methods,
which solve the many-body Schr¨ odinger equation associ-
ated with the Hamiltonian of Eq. (1) with controlled ap-
proximations [55–58]. For light nuclei, quantum Monte
Carlo (QMC) and, in particular, Green’s function Monte
Carlo (GFMC) methods have been exploited to carry
out calculations of nuclear properties, based on realis-
4
tic NN and 3N potentials, and consistent one- and two-
body meson-exchange currents [50]. GFMC begins with
the construction of a trial wave function Ψ T that is a
symmetrized product of two- and three-body correla-
tion operators acting on an antisymmetricA-body single-
particle wave function that has the proper quantum num-
bers for the state of interest. The variational parameters
in ΨT are found by minimizing the energy expectation
value
E0≤ET =⟨ΨT|H|ΨT⟩
⟨ΨT|ΨT⟩ , (2)
where E0 is the true ground-state energy of the system.
The calculation of ET requires the numerical solution of
a multidimensional integral that is carried out employing
standard Metropolis Monte Carlo sampling in conﬁgura-
tion space.
GFMC then projects out the lowest eigenstate Ψ 0 of
the given quantum numbers starting from Ψ T by per-
forming a propagation in imaginary time τ
|Ψ0⟩ = lim
τ→∞
exp[−(H−E0)τ]|ΨT⟩. (3)
The propagation|Ψ(τ)⟩ = exp[−(H−E0)τ]|ΨT⟩ is car-
ried out as a series of many small imaginary-time steps
∆τ. Expectation values of operators are evaluated as
mixed matrix elements O(τ) = ⟨ΨT|O|Ψ(τ)⟩, and the
behavior as a function of τ analyzed to obtain con-
verged results. Because H and exp[−(H−E0)τ] com-
mute, the mixed estimate is the exact expectation of
⟨Ψ(τ/2)|O|Ψ(τ/2)⟩ but linear extrapolations are used to
evaluate other quantities.
In addition to binding energies the GFMC provides
detailed information on the distribution of nucleons in a
nucleus in both coordinate and momentum space, which
are interesting in multiple experimental settings. For ex-
ample, the mixed-estimate of the single-nucleon density
is calculated as
ρN(r) = 1
4πr2
⟨
ΨT
⏐⏐∑
i
δ(r−| ri|)PN
⏐⏐Ψ(τ)
⟩
, (4)
where N = p,n ; PNi =
1±τzi
2 is the neutron or proton
projector operator; and, ρN integrates to the number of
protons or neutrons. The two-body density distribution,
yielding the probability of ﬁnding two nucleons with sep-
aration r, is deﬁned as
ρNN (r) = 1
4πr2
⟨
ΨT
⏐⏐∑
i<j
δ(r−| rij|)PNiPNj
⏐⏐Ψ(τ)
⟩
. (5)
The positions of the constituents protons and neutrons
utilized in the nuclear cascade algorithm are sampled
from 36000 GFMC conﬁgurations. We employ the so-
called constrained-path approximation [59] to make sure
that their Monte Carlo weights remain positive, thereby
facilitating their usage in the cascade algorithm. As a
consequence, the single-proton distribution displayed by
0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0
r (fm)
0.02
0.04
0.06
0.08
0.10
0.12
p(fm 3)
0.0
Quantum Monte Carlo
Mean field
FIG. 3: Nucleon density in carbon from Green’s
function Monte Carlo (red) and mean ﬁeld (blue)
conﬁgurations.
the blue solid circles of Fig. 3 is slightly diﬀerent from the
results reported in Ref. [60], which have been obtained
performing fully unconstrained imaginary-time propaga-
tions. Since we neglect the charge-symmetry breaking
terms in the Hamiltonian, and since 12C is isospin sym-
metric, the single-neutron distribution is identical to that
of the proton.
For benchmark purposes, we also sample 36000 mean-
ﬁeld (MF) conﬁgurations from the single-proton distribu-
tion. The corresponding single-proton densities coincide
by construction with the GFMC one, as shown in Fig. 3.
However, the diﬀerences between GFMC and MF con-
ﬁgurations become apparent when comparing the corre-
sponding two-body density distributions represented in
Fig. 4. The short-range repulsive core of the NN in-
teraction prevents two nucleons from being close to each
other. As a consequence, the pp and np GFMC density
distributions are small at short separation distances. Fur-
thermore, the diﬀerence between the GFMC pp and np
density distributions around r = 1 fm can be attributed
to the strong tensor correlations induced by the one-pion-
exchange part of theNN interaction, which is further en-
hanced by the two-pion-exchange part of the 3 N poten-
tial. Note that the short-range behavior of ρNN , which is
largely nucleus independent, does depend strongly on the
NN interaction model [61]. On the other hand, the MF
ones do not exhibit this rich behavior as the correlations
among nucleons are entirely disregarded.
B. Nucleon momentum distribution
As mentioned above, when a nucleon is struck, its mo-
mentum is obtained assuming either a local or global
Fermi gas distribution. In the case of the local Fermi gas,
5
0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0
r (fm)
0.02
0.04
0.06
0.08
0.10
0.12
0.14
pp(fm 3)
0.0
Quantum Monte Carlo
Mean Field
0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0
r (fm)
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40
np(fm 3)
0.0
Quantum Monte Carlo
Mean Field
FIG. 4: Proton-proton (top panel) and proton-neutron
(bottom panel) correlation functions in carbon from
Green’s function Monte Carlo (red) and mean ﬁeld
(blue) conﬁgurations.
the magnitude of the three-momentum is randomly sam-
pled in the interval [0 ,kN
F (r)] where kN
F (r) is the Fermi
Momentum deﬁned in terms of the single nucleon den-
sity kN
F (r) = (ρN(r)3π3)1/3 and N = p,n . In the case
of the global Fermi gas, the momentum is determined in
the same way, but kN
F is position independent. The lo-
cal Fermi gas model is known to provide a more realistic
nucleon momentum distribution for ﬁnite nuclei than the
global Fermi gas. For this reason, although both mod-
els are implemented in our code, we only present results
based on the local Fermi gas predictions. In the future,
we plan to include more accurate nucleon momentum dis-
tribution, based on state-of-the-art many-body calcula-
tions that properly account for nuclear correlations.
C. Nucleon-nucleon interaction algorithm
To check if an interaction between nucleons occurs,
an accept-reject test is performed on the closest nu-
cleon according to a probability distribution P (b) (see
e.g. Ref. [62] for similar considerations) where b is the
impact parameter. We impose two conditions on this
probability,
P (0) = 1 and
∫ 2π
0
∫ ∞
0
dϕbdbP (b) =σ, (6)
where the cross sectionσ depends on the incoming parti-
cle content and the center-of-mass energy, which is sam-
pled from the nuclear conﬁguration. The second condi-
tion ensures that the mean free path of a nucleon trav-
eling in a medium of uniform density is λmfp = 1/σ¯ρ,
where ¯ρ is the number density.
Two implementations of P (b) have been studied here.
The ﬁrst we dub the cylinder interaction probability,
Pcyl(b) = Θ(σ/π−b2), (7)
where Θ(x) = 1 if x≥ 0, else Θ(x) = 0. This probability
mimics a more classical, billiard ball like system, where
each billiard ball has a radius ≈
√
σ/π. The second
implementation is the Gaussian interaction probability
PGau(b)≡ exp
(
−πb2
σ
)
, (8)
which is inspired by the work of Ref. [62]. Both
Pcyl and PGau satisfy the conditions in Eq. (6). We
use the nucleon-nucleon cross sections from the SAID
database [63] obtained using GEANT4 [64], or from the
NASA parametrization [65].
D. Phase space, Pauli blocking and
after-interaction
If an interaction occurred, the phase space of the
outgoing particles is generated using fully diﬀerential
nucleon-nucleon cross sections. Note that, at the mo-
ment, we only include protons and neutrons in our INC
model. Pauli blocking enforces Fermi-Dirac statistics for
the nucleons and amounts to testing whether their ﬁnal-
state momenta are above the Fermi momentum. Two dif-
ferent models of the Pauli exclusion principle have been
approximately implemented. The global and local Pauli
blocking routines essentially forbid a scattering if the mo-
mentum of any of the ﬁnal state particles is below the av-
erage Fermi momentum (for the global Fermi gas model)
or the local Fermi momentum (for the local Fermi gas
model), respectively. We emphasize again that, although
we have implemented the global Fermi gas model, we do
not report any results using it.
If the interaction took place, the outgoing particles are
both treated as propagating particles, and a formation
6
zone is set for each of them [53, 54] (see also Ref. [47]).
The formation zone is a length or period of time in which
a particle does not interact with any nucleons. This mod-
els the coherence and interference of interactions in quan-
tum mechanics. The formation zone is given by
δt = E′
m2
N−p·p′, (9)
wheremN = 938 MeV is the nucleon mass, E′ is the en-
ergy of the outgoing nucleon, and p and p′ are the four
momenta of the incoming and outgoing nucleon respec-
tively.
E. Exiting the nucleus
When the radial position of a propagating particle is
larger than a certain distance, much larger than the nu-
clear radius, a test is performed to check if the particle
has enough energy to escape the nuclear potential. If its
kinetic energy is larger than the the nuclear potential bar-
rier, then the particle escapes the nucleus and is labeled
as a ﬁnal state particle. The momentum of the particle is
modiﬁed to include the eﬀective nuclear binding. Final
state particles do not propagate and are essentially the
input that should be given to a detector simulation.
III. RESULTS AND MODEL VALIDATION
In this Section, we present the validation tests we
performed and the results we obtained within our INC
model. For comparison purposes, we also implement a
version of the nucleon-nucleon interaction algorithm that
we dub mean free path (MFP). This approach is routinely
used in event generators. Within this algorithm, the sys-
tem is not evolved in time steps but rather in constant
position steps that we indicate as λmax. At each step of
the loop the mean free path of the propagating particle
reads
˜λ = 1/
(
ρp(r)σNp +ρn(r)σNn
)
(10)
where N = n,p refers to the isospin of the propagating
particle andr its distance from the centre of the nucleus.
Note that in the limit of constant density, ρp(n)(r) = ¯ρ,
we would recover ˜λ = λmfp. (see also Sec. III A be-
low). The probability that the struck particle trav-
eled a distance λ without interacting can be written as
P (λ) =e−λ/˜λ. We can then sampleλ =−˜λ·ln(rand[0, 1])
and say that an interaction took place if λ<λ max. Note
thatλmax has to be chosen small enough in order to sat-
isfy the assumption of a constant density.
0.0 2.5 5.0 7.5 10.0 12.5 15.0 17.5 20.0
Distance traveled (fm)
10 7
10 6
10 5
10 4
10 3
10 2
10 1
100
Counts
=1.23 fm
Expected: 1.25 fm
Events
FIG. 5: Distribution of distance traveled (blue
histogram) by 500 MeV test nucleons traveling through
a 0.16 nucleons/fm3 background density of nucleons at
rest, ﬁxed interaction cross-section of 50 mb, and using
the Gaussian interaction probability. The black and
orange lines are the expected distributions for the ﬁtted
(1.23 fm) and expected (1.25 fm) values of the mean
free path, respectively.
A. Mean free path
The simplest validation consists of calculating the
mean free path of a nucleon travelling through a medium
of uniformly distributed nucleons, with ﬁxed interaction
cross sections. Our goal is to obtain
λmfp = 1
σρ, (11)
whereσ is the nucleon-nucleon cross section, andρ is the
number density of nucleons. We simulate a background
of static, randomly and uniformly distributed protons
and neutrons at rest. For an event, we insert into the
medium a test particle with a ﬁxed energy and propa-
gate it through the medium. When the ﬁrst interaction
happens, we record the length the test particle has trav-
eled. Figure 5 shows the distribution of lengths traveled
for a 500 MeV test proton in a 0 .16 nucleons/fm3 back-
ground density of nucleons, assuming a ﬁxed interaction
cross section of 50 mb, and using the Gaussian interac-
tion probability. The expected distributions, according
to Eq. (11), are also shown for the ﬁtted (black line)
and the expected (orange line) values of the mean free
path. The nuclear density and interaction cross section
were chosen arbitrarily. Adjusting these values does not
change the agreement between the expected mean free
path and the calculated mean free path. While not shown
here, using the cylinder interaction probability does not
change the results either. As we can see, our code cor-
rectly reproduces the expected behavior for the mean free
7
path, allowing us to proceed to more complex tests of our
INC.
B. Proton-carbon Scattering Data
Reproducing the proton-nucleus cross section measure-
ments is an important test of the accuracy of the INC
model. Proton-nucleus scattering probes the nucleon-
nucleon cross section which is typically divided into two
pieces, the reaction and the elastic cross sections,
σtot =σR +σel. (12)
In the elastic part, no energy is transferred into nuclear
excitation and the nucleus remains unbroken, that is n +
A→n+A. The reaction cross section includes transition
to nuclear excited states, n +A→ n +A∗, as well as
inelastic reactions n +A→X.
Several experiments have been carried out to deter-
mine the total reaction cross section, see for example
Refs. [66–71]. The latter is typically obtained by measur-
ing the total cross section from the change in intensity of
a calibrated proton beam traversing a carbon target and
then subtracting the calculated elastic cross section.
We compute σR neglecting Coulomb interactions, as
they are expected to contribute mostly to σel. We obtain
the proton-carbon scattering cross section by the follow-
ing simulation (with a diﬀerent setup from the proposed
algorithm of Fig. 2). We deﬁne a beam of protons with
energyE, uniformly distributed over an areaA (orthogo-
nal to the proton momenta). Note that A≫πR2, where
R is the radius of the carbon nucleus. The carbon nucleus
is situated in the center of the beam. We propagate each
proton in time and check for scattering at each step. The
Monte Carlo reaction cross section is then deﬁned as the
area of the beam times the fraction of scattered events,
namely,
σMC =ANscat
Ntot
. (13)
This is not exactly the experimentally measured reaction
cross section. Angular and/or momentum acceptances
for the attenuated beam are ﬁnite, and we do not in-
clude these eﬀects in our calculation. Nevertheless, we
do not expect such eﬀects to change our results signif-
icantly, and thus σMC should be a good approximation
of the reaction cross section. Moreover, imposing Pauli
blocking on both outgoing nucleons will eﬀectively sup-
press the contribution of elastic transitions.
The two panels of Fig. 6 display the proton-carbon
scattering cross sections as a function of the proton ki-
netic energy. In the upper panel our Monte Carlo simu-
lations are compared with experimental data in the en-
tire energy region in which data are available [71], while
the lower panel focuses on proton kinetic energies below
200 MeV. The curves correspond to diﬀerent implemen-
tations of the INC. These implementations are composed
of three ingredients, namely,
0 200 400 600 800 1000
Tp (MeV)
0
100
200
300
400
500
pC
R  (mb)
Data
MF Cyl El
QMC Cyl El
MF Gauss El
QMC Gauss El
MFP El
MF Cyl Tot
QMC Cyl Tot
MF Gauss Tot
QMC Gauss Tot
MFP Tot
0 25 50 75 100 125 150 175 200
Tp (MeV)
0
100
200
300
400
500
pC
R  (mb)
Data
MF Cyl El
QMC Cyl El
MF Gauss El
QMC Gauss El
MFP El
MF Cyl Tot
QMC Cyl Tot
MF Gauss Tot
QMC Gauss Tot
MFP Tot
FIG. 6: Proton-carbon scattering total cross section as
a function of the incoming proton kinetic energy. In the
upper panel the entire energy range for which
experimental data are available is shown. In the lower
panel the low energy region is magniﬁed. The red and
blue curves correspond to the cylinder algorithm where
the mean ﬁeld (MF) and quantum Monte Carlo (QMC)
conﬁgurations have been used, respectively. The green
and orange curves are the same but for the Gaussian
interaction probability. The results displayed in purple
refers to the mean free path (MFP) calculations. The
solid and dashed curves corresponds to the use of the
GEANT4 [64] and NASA [65] parametrization of the cross
section in the interaction probability, respectively. The
data points are from Ref. [71]
1. Nuclear conﬁguration: quantum Monte Carlo
(QMC) or mean ﬁeld (MF);
2. Interaction model: cylinder (cyl), Gaussian
(Gauss), or mean free path (MFP);
3. Nucleon-nucleon cross section: elastic (El) or total
(Tot).
8
Note that the interaction model MFP does not use any
conﬁguration, but rather the local density.
The solid lines have been obtained using the nucleon-
nucleon cross sections from the SAID database [63], ob-
tained using GEANT4 [64], in which only the elastic con-
tribution is retained. The dashed lines used the NASA
parameterization [65], which includes inelasticities. The
inelastic contribution leads to an enhancement of the
cross section which is necessary to reproduce the data
correctly for intermediate to large proton kinetic ener-
gies. The NASA parameterization allows us to approx-
imate the eﬀects of including pions in the cascade. Re-
sults obtained with these two nucleon-nucleon cross sec-
tions are indicated in Fig. 6 by “El” for elastic cross sec-
tion and “Tot” for the total cross section. As expected,
thep-carbon cross section obtained using only the elastic
nucleon-nucleon cross section is consistently lower than
the one obtained using the total nucleon-nucleon cross
section. The eﬀect is large for Tp > 50 MeV, where
pion production becomes relevant. In a future work, we
will explicitly include pion degrees of freedom in our INC
as these are known to play a crucial role in this region.
Additionally, the present results neglect modiﬁcations to
the nucleon-nucleon cross section arising from the nuclear
medium itself. Such modiﬁcations have been considered
in the literature [72]. We also leave these considerations
for a future work.
The dependence of the results on the functional form
of the interaction probability and on the nuclear model
adopted to generate nuclear conﬁgurations has also been
investigated. The blue and red lines are obtained from
the cylinder probability of Eq. (7) and sampling the
initial nucleon conﬁgurations from the quantum Monte
Carlo (QMC) and mean ﬁeld (MF) distributions, respec-
tively. To obtain the orange and green curves, QMC and
MF conﬁgurations were used together with the Gaussian
probability of Eq. (8). We observe that in both cases,
the QMC and MF curves are almost superimposed, in-
dicating that this observable does not depend strongly
on correlation eﬀects among the nucleons. A more de-
tailed discussion of their impact on particle propagation
distances will be discussed in Sec. III D.
The purple lines refer to mean free path (MFP) calcula-
tions which present conceptual diﬀerences with respect to
the cylinder and Gaussian cases and yield large discrep-
ancies in the results. The predictions for the p-carbon
cross section obtained from the MFP approach underes-
timate the experimental data and are signiﬁcantly lower
with respect to the other curves obtained with more re-
ﬁned techniques.
In the lower panel of Fig. 6 we focus on the compari-
son between the diﬀerent MC simulations and the data in
the low energy region, i.e., proton kinetic energies below
200 MeV. The results obtained using the Gaussian and
cylinder algorithm are in fair agreement with the exper-
imental data: the curves display the correct behaviour
although the position of the peak is not exactly repro-
duced. We note that Pauli blocking plays a fundamen-
tal role for these kinematics, signiﬁcantly quenching the
results. More sophisticated techniques aimed at consis-
tently orthogonalizing the nuclear wave function in the
ﬁnal state are discussed in Ref. [73]. Their implementa-
tion in our INC will be the subject of a future work.
The functional forms adopted to determine the prob-
ability distribution (Gaussian vs. cylinder) yield predic-
tions which diﬀer by ∼ 15% in the low energy region
(compare, for instance, the green and red lines in Fig. 6).
For intermediate proton kinetic energies Tp the curves
converge to the same result and reproduce the data. At
lowTp, the predicted cross sections for the MFP method
are∼ 50% smaller than those of the Gaussian and cylin-
der methods. As these diﬀerences are also present in
nuclear transparency, we will discuss their origins in the
next section.
C. Nuclear transparency
The nuclear transparency yields the average probabil-
ity that a struck nucleon (either a proton or a neutron)
leaves the nucleus without interacting with the spectator
particles. Measurements of the nuclear transparency to
high energy protons in quasielastic e +A→ e +p +A′
scattering have been carried out by a number of exper-
iments [4, 6, 7, 74–76]. These measurements are per-
formed with ﬁxed kinematics (i.e., for a ﬁxed incoming
beam energy and scattering angle) and measure the out-
going electron and proton. The proton produced in the
primary vertex can be absorbed or deﬂected while exit-
ing the nuclear medium because of ﬁnal state interactions
with the remnant system, leading to a reduction of the
measurede+A→e+p+A′ cross section. This reduction
deﬁnes the nuclear transparency, which is given by the
ratio of the observed events to events predicted in the
Plane Wave Impulse Approximation (PWIA)
T = Nexp
NPWIA
. (14)
To obtainNPWIA the initial proton is treated as a bound
state with energy and momentum distribution described
by a spectral function; while the ﬁnal proton is a free
particle state propagating as a plane wave.
In our Monte Carlo simulation, the nuclear trans-
parency has been obtained via the following procedure.
We randomly sample a nucleon, its position being gener-
ated according to either the QMC or MF distributions.
We give the nucleon a kick by assigning it a given ki-
netic energy Tp and three-momentum p, and propagate
it through the nuclear medium. The Monte Carlo trans-
parency is then deﬁned as
TMC = 1− Nhits
Ntot
(15)
where Pauli blocking has been implemented in the deter-
mination of Nhits. Note that for a given initial and ﬁnal
9
0 250 500 750 1000 1250 1500 1750 2000
Tp (MeV)
0.4
0.5
0.6
0.7
0.8
0.9
1.0
1.1
Transparency
Data
MF Gauss El
MF Cyl El
QMC Gauss El
QMC Cyl El
MFP El
MF Gauss Tot
MF Cyl Tot
QMC Gauss Tot
QMC Cyl Tot
MFP Tot
FIG. 7: Carbon transparency as a function of the
proton kinetic energy. The diﬀerent curves indicate
diﬀerent approaches used as described in Fig. 6. The
experimental data are taken from Refs. [4, 6, 7, 74–76]
energy and scattering angle of the electron, one can un-
ambiguously deﬁne the momentum q transferred to the
target nucleus. The direction and the momentum of the
nucleon in the ﬁnal state has to be determined apply-
ing energy- and momentum-conservation relations and
accounting for the Fermi motion of the struck nucleon in
the initial state. It follows that deﬁning the kinematics of
the hadronic ﬁnal state after the hard scattering depends
on the nuclear model of choice. However, in the analysis
of diﬀerent experiments, the data are given as a function
of the average nucleon momentum (and kinetic energy)
given by p = q (Tp =
√
|q|2 +m2
N−mN).
In Fig. 7 we compare the nuclear transparency data
from Refs. [4, 74] to our predictions. The diﬀerent lines
are the same as for Fig. 6. We ﬁnd an overall satis-
factory agreement between the Gaussian and cylinder
curves with the experimental data once inelastic eﬀects
are taken into consideration; this corresponds to the re-
sults using the NASA parametrization for the nucleon-
nucleon cross sections. For moderate to large values of
the proton kinetic energy, pions play an important role
in quenching the transparency. Moreover, the Gaussian
and cylinder curves exhibit correct behavior consistent
with the data also for smallTp where the simpliﬁed MFP
model described above fails. As in Fig. 6, we observe
very small diﬀerences between the QMC and MF calcu-
lations. For low and intermediate kinetic energies, the
transparency obtained from the MFP approach is much
smaller than the corresponding results for the cylinder
and Gaussian curves.
Finally, we discuss the origin of the discrepancies be-
tween the MFP and the cylinder algorithm with MF
conﬁgurations for the p-carbon cross section and carbon
transparency. Both approaches rely on the single-nucleon
density distribution to sample the initial nucleon posi-
p
 /⇡
d`
r1
p
 /⇡
d`
x
r1
FIG. 8: Left panel: a schematic picture of an external
proton scattering oﬀ the nucleus. The distance from the
proton to the center of the nucleus is r1, and the
propagation step is d𝓁. The radius of the cylinder is
given by
√
σ/π where σ is the interaction cross section
between the proton and a background particle; d𝓁 is
also the height of the cylinder. Right panel: same as for
the left one, but for a nucleon kicked inside the nucleus.
This follows what is done in the nuclear transparency
event simulations.
tions (nuclear correlations are neglected) but use diﬀer-
ent deﬁnitions of the interaction probability. The left
panel of Fig. 8 schematically shows one contribution to
thep-carbon cross section in which the proton is at a dis-
tance r1 larger than the nuclear radius. In the cylinder
algorithm, the interaction probability is equal to one if a
particle is present in the volume deﬁned by: V =d𝓁·σ.
Both σpp and σnp have a maximum for low proton mo-
mentum values. Hence, for low momenta, the probability
of interaction could be non-vanishing even when the pro-
jectile proton is far from the center of the nucleus.
On the other hand, within the MFP approach, if the
probe is outside the nucleus then the approximation of a
constant density ρ(r1) = 0 within the volume V =d𝓁·σ
yields a vanishing interaction probability. This diﬀerent
behaviour leads to a lower p-carbon cross section using
the MFP approach, as observed in Fig. 6. When com-
puting the nuclear transparency we kick a nucleon which
is located inside the nucleus as displayed in the right
panel of Fig. 8. In this case, assuming a constant density
is more likely to overestimate the interaction probabil-
ity, especially for low momenta where the cross section is
larger. This observation is consistent with Fig. 7 where
the MFP curves predict a larger number of interactions,
and therefore a lower nuclear transparency, for small Tp.
D. Correlation eﬀects
The role played by nuclear correlations in ﬁnal state in-
teractions of the recoiling nucleon has been investigated
10
0 1 2 3 4
Distance Traveled (fm)
0
5
10
15
20
Nevents
=0.5 mb
Total Events: 10000
QMC Hits: 85
MF Hits: 103
QMC MF
0 1 2 3 4 5 6
Distance Traveled (fm)
0
100
200
300
400
Nevents
=10 mb
Total Events: 10000
QMC Hits: 1634
MF Hits: 1755
QMC MF
0 1 2 3 4 5 6 7
Distance Traveled (fm)
0
500
1000
1500
2000
Nevents
=50 mb
Total Events: 10000
QMC Hits: 5600
MF Hits: 5391
QMC MF
0 1 2 3 4 5 6
Distance Traveled (fm)
0
500
1000
1500
2000
2500
3000
3500
Nevents
=100 mb
Total Events: 10000
QMC Hits: 7237
MF Hits: 7012
QMC MF
FIG. 9: The four panels corresponds to histograms of the distance traveled by a struck particle before the ﬁrst
interaction takes place for diﬀerent values of the interaction cross section. The results in blue and red correspond to
MF and QMC initial nucleon conﬁgurations, respectively. For each of the panels we also report the ﬁxed
cross-section used, the total number of events generated, and the number of hits for each conﬁguration.
in Refs. [72, 77–80]. As discussed in Ref. [81] the hit nu-
cleon is surrounded by a short-distance correlation hole
produced by both the Pauli principle and the repulsive
nature of realistic nuclear interactions. Because of this
correlation hole, the stuck nucleon is expected to freely
propagate for∼ 1 fm before interacting with any of the
background particles. To test the validity of these ob-
servations in our INC model, in Fig. 9 we report the
histograms of the distance traveled by a struck nucleon
before its ﬁrst interaction occurs—we stop the simulation
afterwards—with each panel corresponding to a diﬀerent
value of the interaction cross section. In order to gauge
the eﬀect of nuclear correlations, the initial positions of
the nucleons are sampled from either MF (blue) or QMC
(red) conﬁgurations. A random nucleon inside the nu-
cleus is recoiled and assigned a momentum of 200 MeV.
Pauli Blocking has been neglected here to isolate the de-
pendence of the results on the spatial distribution of the
nucleons. We employ the cylinder algorithm and use a
ﬁxed cross section—which determines the cylinder base
area—varying between 0.5 and 100 mb.
For σ = 0.5 and 10 mb, the volume spanned by the
propagating particle is very small. The ﬁrst and second
panels of Fig. 9 clearly show the MF distribution peak-
ing toward smaller distances than the QMC distribution.
This diﬀerence primarily originates from the short-range
repulsion of the AV18 potential that reduces the prob-
ability of ﬁnding two nucleons close to each other and
allows the struck particle to propagate longer before in-
teracting. This eﬀect is more pronounced for cross sec-
tions below about 10 mb = 1 fm2 since correlations aﬀect
nucleon conﬁguration for inter-particle distances within
1∼ 2 fm, as can be seen in Fig. 4. On the other hand,
larger cross sections yield larger cylinders. In this case,
the propagating particle becomes less sensitive to the lo-
cal distribution of nucleons and more sensitive to the in-
tegrated density in a larger volume, reducing the eﬀect
of correlations. For these larger cross sections, the MF
and QMC event distributions follow the same trend, as
can be seen in the lower panels of Fig. 9, corresponding
to σ = 50 and 100 mb.
In each panel we also report the number of hits and the
11
total number of events simulated. Obviously, the num-
ber of interactions increases for the larger cross sections.
It is more interesting to notice that the total number of
hits does not present a strong dependence on conﬁgura-
tions with (QMC) and without (MF) correlations. This
explains why sampling from these two diﬀerent set of con-
ﬁgurations give comparable results for thep-carbon cross
section and carbon transparency, displayed in Figs. 6 and
7. These observables are indeed more sensitive to the oc-
currence of any interaction rather than to its location in-
side the nucleus. This is especially true for the p-carbon
cross section, since the attenuation of a proton beam is
sensitive to the total nuclear density rather than its dif-
ferential proﬁle (compare, e.g., the solid blue and red
lines in Fig. 6).
An alternative way to include correlation eﬀects in
INC models, based on two-body density distributions,
has been recently proposed by the NuWro collaboration
and leads to a larger enhancement of the nuclear trans-
parency than we ﬁnd [49]. This diﬀerence can partly
be ascribed to correlation terms between two spectator
nucleons [79] that are automatically incorporated in our
QMC conﬁgurations, but cannot be modeled by the two-
body correlation functions alone. In addition, as dis-
cussed in Sec. III D, when the nucleon-nucleon cross sec-
tion is larger than about 20 mb, the base of the propagat-
ing cylinder in our model covers the correlation hole and
reduces the importance of correlations. This eﬀect is ab-
sent when only local properties of two-body distribution
functions are considered.
Although nuclear correlations in ﬁnal state interactions
do not play a prominent role in the observables that we
have considered, correlations may be important in other
experimentally relevant quantities or in high-precision
studies. These observables include proton multiplicity
and the distribution of outgoing protons’ direction and
energy. We plan to continue exploring these questions in
future work.
IV. CONCLUSIONS
We have presented a novel INC model that takes as
input realistic QMC nuclear conﬁgurations to sample
the distributions of protons and neutrons inside the nu-
cleus. Either a cylinder or a Gaussian distribution is
used to deﬁne the interaction probability of the propa-
gating nucleon as a function of the impact parameter and
the nucleon-nucleon cross sections. We have considered
the elastic and the total cross sections, corresponding to
the SAID database [63] and to the NASA parametriza-
tion [65], respectively.
To validate the INC we have compared our simulations
with experimental data for p-carbon scattering and car-
bon transparency. For both observables, we ﬁnd minimal
diﬀerence between the cylinder and Gaussian distribu-
tions, and both correctly reproduce the trend of the data.
We gauge the role of nuclear correlations in the propa-
gation of the recoiling nucleons by utilizing nuclear con-
ﬁgurations computed within quantum Monte Carlo and
comparing with mean ﬁeld distributions. The distance
traveled by a struck particle before the ﬁrst interaction
occurs, for suﬃciently small value of the nucleon-nucleon
cross section, is signiﬁcantly longer when nuclear corre-
lations are accounted for. This is due to the short-range
repulsion characterizing the AV18 potential that gives
rise to a correlation hole surrounding the propagating
nucleon, thereby reducing the probability of ﬁnding two
nucleons close to each other. However, the total num-
ber of hits is only mildly aﬀected by the presence of nu-
clear correlations. As a consequence, they mildly aﬀect
our calculations ofp-carbon scattering and carbon trans-
parency. The results presented for the latter quantity by
the NuWro collaboration indicate a larger importance of
nuclear correlations, whose implementation is based on
the two-body density distributions [49].
Nucleon-nucleon cross sections are an important ingre-
dient in INC models. Since the scattering between the
two nucleons takes place in the nuclear medium, the free
nucleon-nucleon cross sections have to be corrected. In
our simulation, we do so by approximately implementing
the Pauli exclusion principle: in the aftermath of each
collision, the magnitude of ﬁnal nucleons’ momenta have
to be larger than the Fermi momentum. This constraint
reduces the eﬀective cross section and considerably im-
proves the agreement between our simulations and exper-
imental data. As a next step, along the line of Ref. [72],
we plan to replace the bare nucleon mass with an eﬀec-
tive one that depends on the momentum and the nuclear
density, leading to a more complete and consistent treat-
ment of in-medium eﬀects.
At energies larger than the pion-production thresh-
old, inelastic contributions to the nucleon-nucleon cross
section become relevant. Using the NASA parametriza-
tion, which includes these inelasticities, noticeably im-
proves the agreement with p-carbon scattering and car-
bon transparency experimental data in the higher-energy
region. Our INC model has yet to include pion propa-
gation in the nuclear medium. Existing event generators
have to rely on a number of semi-phenomenological ap-
proaches constrained by experimental data [33, 82–85],
the validity of which strongly depends upon the energy
of the propagating pion. A consistent implementation
of pion propagation and absorption is an extremely chal-
lenging problem and we leave this aspect for future works.
The transparency measurements used here depend
upon theoretical calculations based on the plane wave im-
pulse approximation. To compare directly to the experi-
mental data, we plan on implementing the primary inter-
action vertex using the spectral function formalism [86–
88]. Additionally to further validate our model, we will
carry out extensive comparison against available semi-
exclusive electron scattering data [89, 90].
12
V. ACKNOWLEDGMENTS
We thank John Arrington, Omar Benhar, Donald
F. Geesaman, Stefan H¨ oche, T.S. Harry Lee, Kajetan
Niewczas, Stefan Prestel, Jan Sobczyk, and Mike Wag-
man for useful discussions . PM and AL thank the Ar-
gonne Physics Division and the Fermilab theory group,
respectively, for providing consistent oﬃce space neces-
sary for the completion of this work. Fermilab is operated
by the Fermi Research Alliance, LLC under contract No.
DE-AC02-07CH11359 with the United States Depart-
ment of Energy. The present research is supported by the
U.S. Department of Energy, Oﬃce of Science, Oﬃce of
Nuclear Physics, under contracts DE-AC02-06CH11357
(A.L. and N.R.) and by the NUCLEI SciDAC program.
[1] P. Barreau et al. , Nucl. Phys. A 402, 515 (1983).
[2] N. Makins et al. , Phys. Rev. Lett. 72, 1986 (1994).
[3] M. Anghinolﬁ et al. , J. Phys. G 21, L9 (1995).
[4] D. Abbott et al. , Phys. Rev. Lett. 80, 5072 (1998).
[5] D. Dutta et al. , Phys. Rev. C 61, 061602 (2000).
[6] D. Dutta et al. (JLab E91013), Phys. Rev. C 68, 064603
(2003), arXiv:nucl-ex/0303011.
[7] D. Rohe et al. (E97-006), Phys. Rev. C72, 054602 (2005),
arXiv:nucl-ex/0506007.
[8] H. Dai et al. (Jeﬀerson Lab Hall A), Phys. Rev. C 98,
014617 (2018), arXiv:1803.01910 [nucl-ex].
[9] H. Dai et al. , Phys. Rev. C 99, 054608 (2019),
arXiv:1810.10575 [nucl-ex].
[10] M. Murphy et al. , Phys. Rev. C 100, 054606 (2019),
arXiv:1908.01802 [hep-ex].
[11] K. Abe et al. (T2K), Phys. Rev. D93, 112012 (2016),
arXiv:1602.03652 [hep-ex].
[12] D. S. Ayres et al. (NOvA), (2007), 10.2172/935497.
[13] K. Abe et al. (Hyper-Kamiokande), (2018),
arXiv:1805.04163 [physics.ins-det].
[14] B. Abi et al. (DUNE), (2020), arXiv:2002.02967
[physics.ins-det].
[15] T. kesson et al. (LDMX), (2018), arXiv:1808.05219 [hep-
ex].
[16] O. Palamara (ArgoNeuT), Proceedings, 10th Interna-
tional Workshop on Neutrino-Nucleus Interactions in the
Few Region (NuInt15): Osaka, Japan, November 16-21,
2015, JPS Conf. Proc. 12, 010017 (2016).
[17] K. J. Kelly, P. A. Machado, I. Martinez Soler, S. J. Parke,
and Y. F. Perez Gonzalez, Phys. Rev. Lett. 123, 081801
(2019), arXiv:1904.02751 [hep-ph].
[18] C. Rott, S. In, J. Kumar, and D. Yaylali, JCAP 01, 016
(2017), arXiv:1609.04876 [hep-ph].
[19] C. Rott, D. Jeong, J. Kumar, and D. Yaylali, JCAP 07,
006 (2019), arXiv:1903.04175 [astro-ph.HE].
[20] R. Serber, Phys. Rev. 72, 1114 (1947).
[21] N. Metropolis, R. Bivins, M. Storm, J. Miller, G. Fried-
lander, and A. Turkevich, Phys. Rev. 110, 204 (1958).
[22] H. W. Bertini, Phys. Rev. 131, 1801 (1963).
[23] J. Cugnon, Phys. Rev. C 22, 1885 (1980).
[24] G. Bertsch, H. Kruse, and S. Gupta, Phys. Rev. C 29,
673 (1984), [Erratum: Phys.Rev.C 33, 1107–1108 (1986)].
[25] H. Stoecker and W. Greiner, Phys. Rept.137, 277 (1986).
[26] W. Bauer, G. Bertsch, W. Cassing, and U. Mosel, Phys.
Rev. C 34, 2127 (1986).
[27] G. Bertsch and S. Das Gupta, Phys. Rept. 160, 189
(1988).
[28] P. Danielewicz and G. Bertsch, Nucl. Phys. A 533, 712
(1991).
[29] L. Kadanoﬀ and G. Baym, Quantum Statistical Mechan-
ics (Benjamin, New York, 1962).
[30] W. Botermans and R. Malﬂiet, Phys. Rept. 198, 115
(1990).
[31] W. Cassing, V. Metag, U. Mosel, and K. Niita, Phys.
Rept. 188, 363 (1990).
[32] S. Teis, W. Cassing, M. Eﬀenberger, A. Hombach,
U. Mosel, and G. Wolf, Z. Phys. A 356, 421 (1997),
arXiv:nucl-th/9609009.
[33] O. Buss, T. Gaitanos, K. Gallmeister, H. van Hees,
M. Kaskulov, O. Lalakulich, A. B. Larionov, T. Leit-
ner, J. Weil, and U. Mosel, Phys. Rept. 512, 1 (2012),
arXiv:1106.1344 [hep-ph].
[34] U. Mosel, J. Phys. G46, 113001 (2019), arXiv:1904.11506
[hep-ex].
[35] J. Cugnon, C. Volant, and S. Vuillier, Nucl. Phys. A
620, 475 (1997).
[36] H. Duarte, Phys. Rev. C 75, 024611 (2007).
[37] H. Iwamoto, M. Imamura, Y. Koba, Y. Fukui, G. Wak-
abayashi, Y. Uozumi, T. Kin, Y. Iwamoto, S. Hohara,
and M. Nakano, Phys. Rev. C 82, 034604 (2010).
[38] Y. Sawada, Y. Uozumi, S. Nogamine, T. Yamada,
Y. Iwamoto, T. Sato, and K. Niita, Nucl. Instrum. Meth.
B 291, 38 (2012).
[39] R. Glauber et al. , (1959).
[40] Y. Golubeva, L. Kondratyuk, A. Bianconi, S. Boﬃ, and
M. Radici, Phys. Rev. C 57, 2618 (1998), arXiv:nucl-
th/9712040.
[41] Y. Uozumi, T. Yamada, S. Nogamine, and M. Nakano,
Phys. Rev. C 86, 034610 (2012).
[42] A. Boudard, J. Cugnon, S. Leray, and C. Volant, Phys.
Rev. C66, 044615 (2002).
[43] Y. Hayato, Nucl. Phys. B Proc. Suppl. 112, 171 (2002).
[44] D. Casper, Nucl. Phys. B Proc. Suppl. 112, 161 (2002),
arXiv:hep-ph/0208030.
[45] G. Battistoni, F. Cerutti, A. Ferrari, J. Ranft, S. Roesler,
and P. Sala, J. Phys. Conf. Ser. 408, 012051 (2013).
[46] G. Battistoni et al. , Annals Nucl. Energy 82, 10 (2015).
[47] T. Golan, C. Juszczak, and J. T. Sobczyk, Phys. Rev.
C86, 015505 (2012), arXiv:1202.4197 [nucl-th].
[48] C. Andreopoulos et al. , Nucl. Instrum. Meth. A 614, 87
(2010), arXiv:0905.2517 [hep-ph].
[49] K. Niewczas and J. T. Sobczyk, Phys. Rev. C 100,
015505 (2019), arXiv:1902.05618 [hep-ex].
[50] J. Carlson, S. Gandolﬁ, F. Pederiva, S. C. Pieper, R. Schi-
avilla, K. Schmidt, and R. Wiringa, Rev. Mod. Phys. 87,
1067 (2015), arXiv:1412.3081 [nucl-th].
[51] R. B. Wiringa, V. G. J. Stoks, and R. Schiavilla, Phys.
Rev. C51, 38 (1995), arXiv:nucl-th/9408016 [nucl-th].
[52] S. C. Pieper, AIP Conference
Proceedings 1011, 143 (2008),
http://aip.scitation.org/doi/pdf/10.1063/1.2932280.
13
[53] L. D. Landau and I. Pomeranchuk, Dokl. Akad. Nauk
Ser. Fiz. 92, 735 (1953).
[54] L. Stodolsky, in Proceedings: International Colloquium
on Multiparticle Reactions, 6th, Oxford, Eng., Jul 14-19,
1975 (1975) p. 577.
[55] S. Bogner, R. Furnstahl, and A. Schwenk, Prog. Part.
Nucl. Phys. 65, 94 (2010), arXiv:0912.3688 [nucl-th].
[56] B. R. Barrett, P. Navratil, and J. P. Vary, Prog. Part.
Nucl. Phys. 69, 131 (2013).
[57] G. Hagen, T. Papenbrock, M. Hjorth-Jensen, and
D. Dean, Rept. Prog. Phys. 77, 096302 (2014),
arXiv:1312.7872 [nucl-th].
[58] C. Barbieri and A. Carbone, “Self-consistent
Green’s function approaches,” (2017) pp. 571–644,
arXiv:1611.03923 [nucl-th].
[59] R. B. Wiringa, S. C. Pieper, J. Carlson, and V. Pand-
haripande, Phys. Rev. C 62, 014001 (2000), arXiv:nucl-
th/0002022.
[60] A. Lovato, S. Gandolﬁ, R. Butler, J. Carlson, E. Lusk,
S. C. Pieper, and R. Schiavilla, Phys. Rev. Lett. 111,
092501 (2013), arXiv:1305.6959 [nucl-th].
[61] R. Cruz-Torres, D. Lonardoni, R. Weiss, N. Barnea,
D. Higinbotham, E. Piasetzky, A. Schmidt, L. Weinstein,
R. Wiringa, and O. Hen, (2019), arXiv:1907.03658 [nucl-
th].
[62] T. Sjostrand and M. van Zijl, Phys. Rev. D36, 2019
(1987).
[63] SAID database, http://gwdac.phys.gwu.edu/.
[64] S. Agostinelli et al. (GEANT4), Nucl. Instrum. Meth. A
506, 250 (2003).
[65] J. Norbury, NASA Technical Paper 215116 (2008).
[66] J. F. Dicello and G. Igo, Phys. Rev. C2, 488 (1970).
[67] B. M. Bobchenko et al. , Sov. J. Nucl. Phys. 30, 805
(1979), [Yad. Fiz.30,1553(1979)].
[68] W. Bauhoﬀ, Atom. Data Nucl. Data Tabl.35, 429 (1986).
[69] S. Kox et al. , Phys. Rev. C35, 1678 (1987).
[70] L. Sihver, C. H. Tsao, R. Silberberg, T. Kanai, and A. F.
Barghouty, Phys. Rev. C47, 1225 (1993).
[71] R. F. Carlson, Atom. Data Nucl. Data Tabl. 63, 93
(1996).
[72] V. Pandharipande and S. C. Pieper, Phys. Rev. C 45,
791 (1992).
[73] R. Gonzlez-Jimnez, A. Nikolakopoulos, N. Jachow-
icz, and J. Udas, Phys. Rev. C 100, 045501 (2019),
arXiv:1904.10696 [nucl-th].
[74] T. G. O’Neill et al. , Phys. Lett. B351, 87 (1995),
arXiv:hep-ph/9408260 [hep-ph].
[75] K. Garrow et al. , Phys. Rev. C 66, 044613 (2002),
arXiv:hep-ex/0109027.
[76] G. Garino et al. , Phys. Rev. C 45, 780 (1992).
[77] M. Radici, S. Boﬃ, S. C. Pieper, and V. Pandharipande,
Phys. Rev. C 50, 3010 (1994), arXiv:nucl-th/9408015.
[78] O. Benhar, V. Pandharipande, and S. C. Pieper, Rev.
Mod. Phys. 65, 817 (1993).
[79] N. N. Nikolaev, A. Szczurek, J. Speth, J. Wambach,
B. Zakharov, and V. Zoller, Phys. Lett. B 317, 281
(1993), arXiv:nucl-th/9306007.
[80] O. Benhar, Phys. Rev. C 87, 024606 (2013),
arXiv:1301.3357 [nucl-th].
[81] O. Benhar, A. Fabrocini, S. Fantoni, S. Pieper, V. Pand-
haripande, and I. Sick, Phys. Lett. B 359, 8 (1995).
[82] L. Salcedo, E. Oset, M. Vicente-Vacas, and C. Garcia-
Recio, Nucl. Phys. A 484, 557 (1988).
[83] D. Ashery, I. Navon, G. Azuelos, H. Walter, H. Pfeiﬀer,
and F. Schleputz, Phys. Rev. C 23, 2173 (1981).
[84] D. Ashery et al. , Phys. Rev. C 30, 946 (1984).
[85] M. Jones et al. , Phys. Rev. C 48, 2800 (1993).
[86] O. Benhar, A. Fabrocini, S. Fantoni, and I. Sick, Nucl.
Phys. A 579, 493 (1994).
[87] N. Rocco, A. Lovato, and O. Benhar, Phys. Rev. Lett.
116, 192501 (2016), arXiv:1512.07426 [nucl-th].
[88] O. Benhar, D. day, and I. Sick, Rev. Mod. Phys. 80, 189
(2008), arXiv:nucl-ex/0603029.
[89] R. Cruz-Torres et al. (Jeﬀerson Lab Hall A Tritium),
Phys. Rev. Lett. 124, 212501 (2020), arXiv:2001.07230
[nucl-ex].
[90] M. Duer et al. (CLAS), Phys. Rev. Lett. 122, 172502
(2019), arXiv:1810.05343 [nucl-ex].
Appendix A: Nucleon-nucleon interaction Models
The nucleon-nucleon cross sections used in our INC
are obtained externally. The elastic cross section is taken
from the SAID database [63], obtained using GEANT4 [64].
The total cross section, including inelastic contributions
(e.g. pion production) is taken from Ref. [65]. For refer-
ence, we reproduce those in Figs. 10. As it can be seen,
the cross sections from these databases are similar in the
region where the elastic contribution dominates, that is,
below 300 MeV for pp interactions and 500 MeV for np
interactions. The diﬀerences at high energy can be at-
tributed to inelastic contributions.
14
0 1000 2000 3000 4000
Tp (MeV)
102
103
ij (mb)
Geant pp
Geant np
NASA pp
NASA np
0 100 200 300 400 500
Tp (MeV)
102
103
ij (mb)
Geant pp
Geant np
NASA pp
NASA np
FIG. 10: Comparison between the two interaction
models used within the intranuclear cascade model.
The GEANT model is based on the SAID database [63]
and obtained using GEANT4 [64] and the NASA model
is given from [65].
