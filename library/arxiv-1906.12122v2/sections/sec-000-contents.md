---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear effective field theory: status and perspectives"
section_id: sec-000-contents
section_title: "Contents"
section_number: null
pages: 1-9
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
doc_brief: "Nuclear effective field theory: status and perspectives — 34 sections: Contents; Two-body scattering amplitude; Power counting"
---
I. Introduction 2
∗ Hans-Werner.Hammer@physik.tu-darmstadt.de
† sekoenig@theorie.ikp.physik.tu-darmstadt.de
‡ vankolck@ipno.in2p3.fr
A. Nuclei from the perspective of QCD 3
B. The way of EFT 4
C. Nuclear EFTs 6
II. Pionless EFT 8
A. Motivation 8
B. Weakly bound S-wave systems 9
1. Two-body scattering amplitude 9
2. Power counting 9
3. Regularization and renormalization 11
arXiv:1906.12122v2  [nucl-th]  6 Apr 2020
2
4. Renormalization group 12
5. Dibaryon ﬁelds 13
6. Spin-isospin projection and parametrizations 13
7. Coulomb eﬀects and other isospin breaking 14
8. External currents 15
C. Light nuclei: bound and scattered 17
1. Extension to three particles 17
2. The triton as a near-Eﬁmov state 17
3. More neutron-deuteron scattering 19
4. Proton-deuteron scattering and helion 21
5. Infrared regulators 22
6. Four nucleons 22
7. Beyond four nucleons 23
8. External currents and reactions 24
D. Outstanding issues and current trends 24
III. Halo/Cluster EFT 25
A. Motivation 25
B. S-wave neutron halos 26
C. Excited Eﬁmov states in halo nuclei 27
D. Ab initio methods and Eﬁmov states in heavier nuclei 29
E. Higher partial waves and resonances 30
F. Electromagnetic properties and reactions 31
1. Form Factors 32
2. E1 transition and photodisintegration 33
3. Correlations 35
4. Neutron capture 36
G. Proton halos 36
H. Cluster systems 37
I. Outlook 38
IV. Chiral EFT 38
A. Motivation 38
B. Basic elements 39
1. Degrees of freedom and symmetries 39
2. Chiral Lagrangian 40
C. Chiral Perturbation Theory and the nuclear potential 41
1. Power counting 41
2. Nuclear potential 43
D. Nuclear amplitudes and observables 46
1. Weinberg’s prescription 46
2. Renormalization of singular potentials 48
3. Connection with Pionless EFT 49
4. Perturbative pions 50
5. Partly perturbative pions 50
6. Other approaches 52
E. Pion and electroweak reactions 53
F. Outstanding issues and current trends 54
V. Broader applications 56
A. Connection with QCD 56
1. Nuclear physics at large quark masses 56
2. Fine-tuning in Chiral EFT and infrared limit cycle 57
B. Antinucleon systems 57
C. Hypernuclei 58
D. Hadronic molecules 58
E. Fundamental symmetries 59
1. Parity violation 59
2. Time-reversal violation 60
3. Other symmetries 60
F. Dark-matter detection 61
G. Bosons with large scattering length 61
VI. Conclusion 61
Acknowledgments 62
References 62
I. INTRODUCTION
The problem of obtaining the properties of atomic nu-
clei from the interactions among the constituent nucleons
has been central to nuclear physics since its inception.
Attempts to derive nuclear forces and currents from the
exchange of mesons—in particular the lightest meson, the
pion—were derailed in the 1950s by a lack of renormaliz-
ability, that is, by an uncontrolled sensitivity to physics
at short distances. 1 The rise in the 1970s of a renormal-
izable theory of the strong interactions, Quantum Chro-
modynamics (QCD), did not immediately oﬀer a path
forward: because QCD—formulated in terms of quarks
and gluons—is nonperturbative for processes character-
ized by external momenta Q <∼ MQCD ∼ 1 GeV, it is
very diﬃcult to calculate the properties of hadrons and
nuclei, a problem that becomes more severe as the num-
ber A of nucleons increases. Yet, a precise and accurate
description of nuclei is crucial for the transition from the
perturbative regime of the Standard Model to the atomic
domain and beyond, governed by Quantum Electrody-
namics (QED) and its small ﬁne-structure constant. Ex-
amples relying on input from nuclear physics include tests
of fundamental symmetries (such as neutrinoless double-
beta decay to probe lepton number violation) and reac-
tions in astrophysical environments.
About a quarter of a century ago eﬀective ﬁeld theories
(EFTs) entered nuclear physics (Weinberg, 1990; Rho,
1991; Weinberg, 1991; Ord´ o˜ nez and van Kolck, 1992;
Weinberg, 1992; van Kolck, 1993). EFTs had been de-
veloped in particle and condensed-matter physics to deal
with systems containing multiple momentum scales. An
EFT captures the most general dynamics among low-
energy degrees of freedom that is consistent with some
assumed symmetries. In nuclear physics, where the sym-
metries of QCD are known, an EFT provides a realization
of QCD in terms of hadrons instead of quarks and gluons.
All the details of the QCD dynamics at short distances
are encoded in the EFT interaction strengths (“Wilson
coeﬃcients” or “low-energy constants”). Scattering am-
plitudes (and their poles representing bound states and
resonances) are calculated as expansions in Q/Mhi and
Mlo/Mhi, with Mhi the momentum scale where the EFT
1 Not long after the successful renormalization of QED, it was
understood that the only relativistic pion-nucleon coupling that
is renormalizable in the same sense is pseudoscalar (Matthews
and Salam, 1951). However, pseudoscalar coupling diﬀers from
pseudovector coupling by a large nucleon-pair term, which was
found to be in conﬂict with pion phenomenology (Marshak,
1952). The favored pseudovector coupling required the intro-
duction of short-distance cutoﬀs, on which description of two-
nucleon data depended sensitively (see, for example, (Garten-
haus, 1955)). Subsequent work increasingly emphasized the phe-
nomenology of short-range interactions. A brief history of nu-
clear potential models is given by Machleidt and Entem (2011)
and Machleidt (2017).
3
breaks down and Mlo standing for low-energy scales of
physics we want to capture. An EFT is renormalizable
in the sense that at each order in the expansion the sen-
sitivity to unaccounted short-distance physics is small,
that is, of relative O(Q/Mhi,M lo/Mhi). EFTs opened
the door to a description of nuclear phenomena with sys-
tematic error estimates.
EFTs have, in fact, revolutionized nuclear physics.
Most of the “ ab initio ” studies of nuclear structure—
based on the explicit solution of the Schr¨ odinger equation
or its equivalents—are now carried out with potentials in-
spired by EFT. A host of nuclear properties has been pre-
dicted or postdicted from two- and three-nucleon forces,
and one- and two-nucleon currents with low-energy con-
stants were determined from A≤ 3 experimental data.
In parallel, starting with Beane et al. (2006), fully dy-
namical simulations of QCD on a discretized and boxed
spacetime have been able to access some A≤ 4 prop-
erties. Matching an EFT to results from lattice QCD
(LQCD), and not just to experiment, allows for a deter-
mination of the low-energy constants. EFTs thus build
a bridge between QCD and nuclear structure and reac-
tions.
Historically the ﬁrst nuclear EFT was Chiral (or
Pionful) EFT (Weinberg, 1990; Rho, 1991; Weinberg,
1991; Ord´ o˜ nez and van Kolck, 1992; Weinberg, 1992; van
Kolck, 1993), which is designed for momenta of the or-
der of the pion mass. In addition to nucleons, it in-
cludes explicit pions, whose interactions are constrained
by an approximate global symmetry of QCD, the chi-
ral symmetry of independent ﬂavor rotations of left- and
right-handed quarks. Chiral EFT generalizes a popu-
lar hadronic EFT, Chiral Perturbation Theory (Wein-
berg, 1979; Gasser and Leutwyler, 1984, 1985), to A≥ 2.
Despite its phenomenological successes, Chiral EFT has
proven to be extremely challenging to renormalize due
to the singularity of the dominant interactions, which
have to be treated nonperturbatively in order to produce
bound states and resonances, i.e., nuclei. Originally con-
ceived as a renormalization playground, a simpler EFT—
Pionless (or Contact) EFT —focuses on momenta be-
low the pion mass (Bedaque and van Kolck, 1998; van
Kolck, 1997; Kaplan et al., 1998a; Bedaque et al., 1998;
Kaplan et al., 1998b; van Kolck, 1999b; Birseet al., 1999).
This EFT, whose renormalization is relatively well un-
derstood, is constrained only by QCD spacetime sym-
metries. It exhibits a high degree of universality, and
except for the degrees of freedom it is formally identical
to other EFTs where all interactions are of short range.
Light nuclei are well described within the same frame-
work that has been successful for atomic systems with
large scattering lengths (for example, near a Feshbach
resonance) (Braaten and Hammer, 2006). A variant of
this EFT, Halo/Cluster EFT, has been applied (Bertu-
lani et al., 2002; Bedaque et al., 2003a) to bound states
and reactions involving halo and cluster nuclei, charac-
terized by such low energies that one or more tight clus-
ters of nucleons can be treated as elementary degrees of
freedom.
No doubt there are “more eﬀective” EFTs to be discov-
ered for larger nuclei. In fact, a description of rotational
and vibrational bands in heavy nuclei has been initiated
by Papenbrock (2011), with successful applications to
diﬀerent nuclei and processes (Papenbrock and Weiden-
mueller, 2014; Coello P´ erez and Papenbrock, 2015, 2016;
Coello P´ erezet al. , 2018a,b; Chen et al. , 2018, 2019).
These recent developments extend the EFT paradigm
to generalized degrees of freedom that capture the low-
energy physics of deformed nuclei.
Here we present a summary of the main ideas, achieve-
ments, and prospects for the nuclear EFTs formulated in
terms of nucleons and clusters thereof. These theories can
be thought of as a tower of EFTs at successively lower
Mhi, starting at MQCD. Our emphasis is not on phe-
nomenology, but on the conceptual similarities and dif-
ferences among Chiral, Pionless, and Halo/Cluster EFTs.
Our hope is that a focused approach will stimulate a re-
formulation of our understanding of heavy nuclei, just
as these EFTs have shed new light on the structure and
reactions of light nuclei.
In the remainder of this section some common aspects
of nuclear EFTs are presented. Each of the three fol-
lowing sections deal with one nuclear EFT. In Sec. V we
address the connection between these EFTs and QCD,
as well as broader applications. We conclude in Sec. VI.
We use throughout units such that ℏ = 1 and c = 1.
A. Nuclei from the perspective of QCD
As an SU (3)c gauge theory of colored quarks and glu-
ons, QCD is characterized by a coupling constantgs that
becomes strong at low momenta. The fact that most
hadron masses are about 1 GeV or higher—for example,
the nucleon mass mN≃ 940 MeV—reveals that nonper-
turbative QCD phenomena are associated with a mass
scale MQCD∼ 1 GeV. The EFT at the scale of a few
GeV includes not only strong interactions, but also elec-
troweak and even weaker interactions. In contrast to
most textbooks, for convenience we refer to this EFT,
which is our starting point, simply as QCD. Focusing on
the two lightest (up and down) quarks most relevant to
nuclear physics, the QCD Lagrangian is written in terms
of quark q = (ud )T , gluon Gµ and photon Aµ ﬁelds as
LQCD = ¯q [iγµ (∂µ + igsGµ + ieQAµ) + ¯m (1−ετ3)]q
− 1
2TrGµνGµν− 1
4FµνFµν +··· , (1)
where γµ and τi are the Dirac and Pauli matrices, and
Gµν and Fµν are the gauge and photon ﬁeld strengths.
Neglecting the “··· ”, which include for example weak in-
teractions, the only parameters in QCD are the quark
4
masses and electromagnetic charges. We can express
quark masses in terms of the common mass ¯m = (mu +
md)/2 ∼ 5 MeV and of the relative mass splitting
ε = (md−mu)/(mu +md)∼ 1/3. The quark charges
are fractions Q = diag(2/3,−1/3) of the proton charge
e =
√
4πα∼ 1/3.
Below MQCD, QCD is best represented as a theory
of colorless hadrons, where SU (3)c is realized trivially.
An important role is played by pions, which arise as
pseudo-Goldstone bosons from the spontaneous break-
ing of approximate SU (2)L×SU (2)R chiral symmetry
down to its vector subgroup SU (2)V of isospin. In the
chiral limit ¯m = 0, ε = 0 and e = 0, chiral symmetry is
exact, and pions are massless and interact purely deriva-
tively. Away from the chiral limit, the common quark
mass breaks chiral symmetry explicitly and leads to a
nonzero common pion mass mπ ≃ 140 MeV and non-
derivative pion interactions. The QCD interactions asso-
ciated with ε and e further break isospin, and appear in
relatively small quantities such as the pion mass splitting
δm2
π =m2
π±−m2
π0≃ (36 MeV)2 and the neutron-proton
mass diﬀerence δmN =mn−mp≃ 1.3 MeV.
A more complete understanding of the low-energy con-
sequences of QCD can be achieved if we consider alterna-
tive realities where ¯m,ε, ande are varied from their real-
world values. So far, LQCD simulations of nuclear quan-
tities have been carried out in the isospin-symmetry limit,
whereε = 0 ande = 0. The only remaining QCD param-
eter, ¯m, can be traded for the pion massmπ. Because the
signal-to-noise ratio for A-nucleon correlation functions
at large time t scales as exp [−A(mN− 3mπ/2)t] (Lep-
age, 1989a; Beane et al. , 2011), current simulations are
limited to unphysically large mπ and to small A. Al-
though one can expect future simulations at smaller pion
masses and more nucleons, it is more eﬃcient to switch to
an EFT description suited to the large distances involved
in nuclear physics.
Years of experience suggest that nuclei can be seen
as bound states or resonances made out of nucleons, or
perhaps clusters of nucleons. The choice of degrees of
freedom determines the range of validity Mhi of the re-
spective EFT. Because isospin violation is a relatively
small eﬀect for most nuclear dynamics (more so for light
nuclei), we can classify nuclear EFTs by their regions of
applicability according to typical momentum and pion
mass, see Fig. 1. A possible estimate of the typical bind-
ing momentum, where each nucleon contributes equally
to the binding energy BA, is QA∼
√
2mNBA/A. Nu-
clear saturation for large A leads, at physical pion mass,
to a constant BA/A∼ 10 MeV and nuclear radii RA∼
R0A1/3, where R0∼ 1.2 fm. Numerically, QA∼ R−1
0
is not very diﬀerent from mπ, and it has been assumed
that Chiral EFT is best suited for typical nuclei. (In fact,
we will see in Sec. IV how BA/A∼ 10 MeV arises nat-
urally within Chiral EFT.) At suﬃciently small Q and
mπ (i.e., below a scale MNN∼ 270 MeV at the physical
Figure 1 Landscape of nuclear EFTs in the plane of typical
momentumQ and pion mass mπ.
pion mass, see Eq. (76) for a precise deﬁnition), one ex-
pects pions to be perturbative. As Q increases at ﬁxed
mπ, chiral-symmetric pion interactions become nonper-
turbative (for A≥ 2), and as Q increases further the
EFT eventually ceases to converge. As mπ increases at
ﬁxedQ, chiral-symmetry breaking becomes more impor-
tant and again the Chiral EFT expansion eventually fails.
We expect that Mhi∼MQCD, but the exact breakdown
values ofQ andmπ are not well known. It seems that for
A = 0, for example, Chiral EFT (in the form of ChPT)
has Mhi≤ 500 MeV (D¨ urr, 2015).
Light nuclei are weakly bound and radii scale diﬀer-
ently than in the saturation regime. Pions can be treated
as short-range interactions and in Pionless EFT we ex-
pect Mhi∼ mπ at all mπ, including values beyond the
breakdown of Chiral EFT such as in LQCD simulations
to date. For Q smaller than the inverse radius of a nu-
cleus, the nucleus itself can be treated as an elementary
particle in more complex systems where it appears as a
sub-unit. In the Halo/Cluster EFT relevant for cluster-
ized nuclei, Mhi∼ R−1
c , the inverse cluster radius. Pi-
onless and Halo/Cluster EFTs carry the information of
QCD to the large distances of nuclear dynamics near the
driplines.
B. The way of EFT
How does one ensure that a nuclear EFT reproduces
QCD in the appropriate energy domain? Once degrees
of freedom have been selected according to the energies
of interest, one constructs the most general Lagrangian
L involving the corresponding set of ﬁelds {ψ}, which is
constrained only by the QCD symmetries,
L =
∑
i
ci(Mlo,M hi, Λ)Oi({ψ}), (2)
where the Oi({ψ}) are operators that involve ﬁelds at
the same spacetime point but contain an arbitrary num-
5
ber of derivatives, andci(Mlo,M hi, Λ) are the low-energy
constants (LECs). Here Λ denotes an arbitrary regu-
lator parameter with dimension of mass. With L, or
the corresponding Hamiltonian, the propagation and in-
teraction of the low-energy degrees of freedom can be
calculated. The procedure might be entirely perturba-
tive, as represented by Feynman diagrams with a ﬁnite
number of loops, or partially nonperturbative, as ob-
tained by an inﬁnite sum of Feynman diagrams or the
solution of an equivalent integral or diﬀerential equa-
tion such as, respectively, the Lippmann-Schwinger or
the Schr¨ odinger equation. In either case, the interactions
are singular, which requires regularization. When the
calculation can be reduced to a ﬁnite number of loops,
dimensional regularization can be employed, which in-
troduces a renormalization scale µ. However, in nuclear
physics we are most often faced with summing an inﬁnite
number of loops with overlapping momenta which, with
present techniques, can only be made ﬁnite by the intro-
duction, at either interaction vertices or propagators, of a
momentum-regulator functionf(p/Λ) such thatf(0) = 1
and f(x→∞ ) = 0. Here p refers to the momentum of
a nucleon, in which case the regulator is separable, or
the transferred momentum, when the regulator is non-
separable. We can alternatively look at position space,
where the nonseparable regulator is local ( i.e., a func-
tion of position only) whereas the separable regulator is
nonlocal.
The goal is to construct the T matrix for a low-energy
process as an expansion in Q/Mhi < 1, schematically,
T (Q) =N
∞∑
ν=0
( Q
Mhi
)ν
×F (ν)
( Q
Mlo
,Q
Λ ;γ(ν)
(Mlo
Mhi
, Λ
Mhi
))
, (3)
whereN is a normalization factor, theF (ν) are functions
generated by the dynamics of the {ψ}, the γ(ν) =O(1)
are dimensionless combinations of theci, andν is a count-
ing index. “Power counting” is the relation between ν
and the interaction label i in Eq. (2). While the form
of the Oi in the Lagrangian (2) depends on the choice
of ﬁelds, the expansion (3) must not (Chisholm, 1961;
Kamefuchi et al. , 1961). Likewise, observables obtained
from Eq. (3) must not depend on the arbitrary regulariza-
tion procedure—renormalization-group (RG) invariance.
Once the expansion (3) has been achieved, one can
truncate the sum at a given ν =V with a small error,
T (Q∼Mlo) =T (V)(Q, Λ)
[
1 +O
(
QV+1
MV+1
hi
)]
. (4)
Before renormalization, non-negative powers of Λ can ap-
pear, which originate in the short-distance part of loops.
The uncertainty principle ensures that such contributions
cannot be separated from that of LECs. Renormalization
is the procedure that ﬁxes the cutoﬀ dependence of the
LECs so that the truncated amplitude T (V)(Q, Λ) satis-
ﬁes approximate RG invariance,
Λ
T (V)(Q, Λ)
dT (V)(Q, Λ)
dΛ =O
(QV+1
MV
hiΛ
)
. (5)
This condition ensures the error introduced by the ar-
bitrary regularization procedure is no larger than the
Q/Mhi error stemming from the neglect of higher-order
terms in Eq. (4), as long as Λ >∼ Mhi. In this “modern
view” of renormalization, there is no need to take the
Λ→∞ limit (Lepage, 1989b). However, while in ana-
lytical calculations Eq. (5) can be veriﬁed explicitly, in
numerical calculations varying the regulator parameter
widely above the breakdown scale is usually the only tool
available to check RG invariance. In contrast, Λ < Mhi
generates relatively large errors from the regularization
procedure. Failure to satisfy Eq. (5) altogether means
uncontrolled sensitivity to short-distance physics: results
depend on the value of Λ and on the choice of the regula-
tor functionf(x), which acquires the status of a physical,
model-dependent “form factor.”
After renormalization, when the contribution from mo-
menta of the order of the large cutoﬀ have been removed,
the dominant terms in loop integrals come from momenta
ofO(Q). Counting powers of Q in individual contribu-
tions to Eq. (3) is similar to determining the superﬁ-
cial degree of divergence of diagrams. There is, in gen-
eral, also residual Λ dependence (Eq. (5)) which can be
absorbed in the LECs of higher-derivative interactions.
Since shuﬄing short-range physics between loops and
LECs does not change observables, the ﬁnite part of an
LEC is expected to be set by the replacement Λ →Mhi
(see, for example, (Veltman, 1981)) 2, which then places
an upper bound on the order these interactions appear at.
The exception is when a symmetry suppresses the cor-
responding interaction (’t Hooft, 1980). “Naturalness”
assumes that all terms in the eﬀective Lagrangian (re-
specting the relevant symmetries) have dimensionless co-
eﬃcients ofO(1) when the appropriate powers ofMlo and
Mhi are factored out. Renormalization is thus a powerful
tool to estimate sizes of the LECs.
This framework is a generalization of the ancient re-
quirement of renormalizability by a ﬁnite set of parame-
ters. If all interactions needed for Eq. (5) are present at
each order, the resulting S matrix incorporates the rela-
tions among QCD S-matrix elements demanded by sym-
metries, with no other assumption than an expansion in
Q/Mhi < 1. Every low-energy observable depends on a ﬁ-
nite number of LECs at leading order (LO), whereV = 0,
2 Burgess (2015) oﬀers a clear discussion in the speciﬁc context of
the cosmological constant.
6
a few more at next-to-leading order (NLO), whereV = 1,
etc. Once the LECs are determined from a ﬁnite number
of data, all other observables can be pre- or postdicted
with a controlled error. Traditionally the input data have
been experimental, but LQCD results can now be used
instead (Barnea et al., 2015; Beane et al., 2015; Kirscher
et al., 2015).
One of the virtues of the model independence encoded
in Eq. (5) is that it provides an a priori estimate of the-
oretical errors. At the simplest level errors can be esti-
mated from the higher-order terms in Eq. (4) with a guess
for Mhi. A lower bound on the theoretical error is pro-
vided by cutoﬀ variation fromMhi to much higher values.
The breakdown scaleMhi itself can be inferred comparing
the energy dependence at various orders with data (Lep-
age, 1997). Reliance on data can be minimized by using
instead EFT results at diﬀerent cutoﬀs (Grießhammer,
2016). Up to now both data ﬁtting and propagation of
errors have employed standard statistical analyses previ-
ously used for models. However, these methods can lead
to biases because they are not particularly well suited to
the a priori EFT error estimates, which typically increase
withQ, while experimental data are sometimes more pre-
cise at higher Q. A comprehensive theory of EFT error
analysis based on Bayesian methods is currently being
developed (Schindler and Phillips, 2009; Furnstahl et al.,
2015c,b; Wesolowski et al., 2016) with the promise of be-
coming the standard in the ﬁeld.
C. Nuclear EFTs
The implementation of these ideas in nuclear physics
has posed some unexpected challenges. They can be
traced to the fact that at LO some interactions need to
be fully iterated—or, equivalently, a dynamical equation
should be solved exactly—in order to produce the bound
states and resonances that we refer to as nuclei.
Nuclear EFTs typically include ﬁelds for the nucleon
or clusters of nucleons. These particles have masses of
O(MQCD), and the expansion (3) includes a Q/mN ex-
pansion around the nonrelativistic limit. Creation of vir-
tual heavy particle-antiparticle pairs takes place at small
distances r <∼ 1/(2mN) and its eﬀects can be absorbed
in the LECs. As a consequence, a process involving A
heavy particles is not aﬀected by interactions in Eq. (2)
involving more than 2A ﬁelds associated with these heavy
particles. The simplest way to incorporate the fact that
the (large) particle rest energy does not play any role
is to employ a “heavy ﬁeld” from which the trivial evo-
lution factor due to the rest energy is removed (Jenk-
ins and Manohar, 1991a). Lorentz invariance for these
ﬁelds is encoded in “reparametrization invariance” (Luke
and Manohar, 1992). Kinetic terms reduce to the stan-
dard nonrelativistic form that respects Galilean invari-
ance, with relativistic corrections suppressed by inverse
powers of mN appearing at higher orders.
There is a crucial diﬀerence between A = 1 and A≥ 2
processes. The former processes involve also light par-
ticles (e.g., photons) in initial and ﬁnal states with mo-
mentaQ∼Mlo. They deposit on the nucleon an energy
ofO(Q) which is larger than the recoil ofO(Q2/(2mN)),
so that the nucleon is essentially static—deviation from
the static limit can be treated as a perturbation. Inter-
mediate states diﬀer in energy from the initial state by
an amount ofO(Q). In contrast, there are Feynman di-
agrams for the T matrix of an A≥ 2 process—whether
it involves external probes or not—that include interme-
diate states which diﬀer in energy from the initial state
only by a small diﬀerence in nucleon kinetic energies of
O(Q2/(2mN)). In these “reducible” diagrams nucleons
are not static, and there is an infrared (IR) enhancement
relative to intermediate states forA = 1 processes (Wein-
berg, 1991). Nucleon recoil cannot be treated perturba-
tively, although relativistic corrections remain small.
The “full” nuclear potential V is deﬁned as the sum of
irreducible diagrams for a process involvingA nucleons in
initial and ﬁnal states. The full T matrix (3) is obtained
by sewing potential subdiagrams with nucleon lines rep-
resenting the freeA-body Green’s function G. This gives
rise to the Lippmann-Schwinger equation, schematically
T =V +
∫
VGT =V +
∫
VGV +··· , (6)
or alternatively to the Schr¨ odinger equation and its
many-body relatives. The full potential so deﬁned in-
volves all A bodies but it includes components with
1≤ C≤ A− 1 separately connected pieces. Frequently
the potential is thought of as one of these connected
pieces. One thus deﬁnes the “A-nucleon (AN) potential”
as the sum of diagrams with C = 1 in the A-nucleon sys-
tem. For A = 2 all diagrams in the nuclear potential are
connected (C = 1), but starting at A = 3 multiply con-
nected diagrams appear, i.e., the full potential is made
up of a sum of fewer-body potentials. Diagrams with
C =A− 1 are made out of the 2 N potential and A− 2
disconnected nucleon lines. Diagrams in the full poten-
tial that have 1 < C < A− 1 are made of combinations
of lower-A potentials and disconnected nucleon lines.
In contrast to phenomenological models, all mesons
with masses >∼ MQCD and nucleon excitations heav-
ier than the nucleon by the same amount can be in-
tegrated out because their eﬀects can be captured by
the LECs. As we are going to see in Sec. II, in Pio-
nless EFT the potential consists purely of contact in-
teractions, while in Chiral EFT pion exchanges are
present as well (Sec. IV). In either case, the potential
involves small transfers of energy O(Q2/(2mN)), and
the total exchanged four-momentum is close to the total
transferred three-momentum. Dependence on the latter
translates into a function of the position in coordinate
space—the potential is local. Meanwhile, dependence on
7
other nucleon momenta leads to derivatives with respect
to position, i.e., the momentum operator in quantum
mechanics—the potential becomes nonlocal. We expect
to be able to expand the potential in momentum space
analogously to Eq. (3),
V (Q, Λ) =
∞∑
µ=0
V (µ)(Q, Λ) = ˜N
∞∑
µ=0
( Q
Mhi
)µ
× ˜F (µ)
( Q
Mlo
;Q
Λ ; ˜γ(µ)
(Mlo
Mhi
, Λ
Mhi
))
, (7)
where ˜N is a normalization factor, 3 the ˜F (µ) are func-
tions obtained from irreducible diagrams, the ˜ γ(µ) =
O(1) are dimensionless combinations of the ci, and µ is
a counting index for the potential.
When the nucleus is disturbed by low-momentum ex-
ternal probes (photons, leptons, perhaps pions), similar
considerations apply. One can deﬁne nuclear currents
(or reaction kernels) as the sum of irreducible diagrams
to which the probes are attached. Again, currents in-
volve all A nucleons but include disconnected diagrams.
A subtlety is that a probe can deposit an energy O(Q)
on a nucleon line, and thus there can be purely nucleonic
intermediate states in irreducible diagrams. Observables
come from the sandwich of currents between wavefunc-
tions of the initial and ﬁnal states. Currents have an
expansion similar to Eq. (7).
The nuclear potential and associated currents can al-
ways be deﬁned as such intermediate quantities between
L and T . We have reduced the EFT to a quantum-
mechanical problem, but one in which the form of the
potential and currents is determined. This is a distinct
improvement over a purely phenomenological approach,
particularly in what concerns the bewildering variety of
many-body potentials and currents one can construct.
This feature is one of the major reasons for the dominant
role nuclear EFTs play nowadays in the nuclear theory
community.
However, one should keep in mind that the potential
and currents are not directly observable. There are im-
portant diﬀerences between Eqs. (7) and (3):
• The potential does not need to obey an equation
such as (5). EFT potentials involve terms that are
singular and often attractive, in the sense of diverg-
ing faster than−1/(4mNr2) as the relative position
r→ 0. The potential would generate strong regu-
lator dependence in Eq. (6) integrals if it did not
itself depend strongly on Λ, see, e.g., a pedagogical
discussion by Lepage (1997).
3 Note that, in the units we use, the momentum-space potential,
like theT matrix, has mass dimension−2. Its Fourier transform,
which involves three powers of momentum, has mass dimension
+1, as it should.
• Since after renormalization Λ disappears from T
(apart from arbitrarily small terms),
∫
VGV ∼ Q3
4π
mN
Q2 V 2∼ mNQV
4π V (8)
and the expansion (6) is in the dimensionless ratio
mNQV/(4π) (Bedaque and van Kolck, 2002). For
Q >∼ 4π/(mNV (0)), F (0) in Eq. (3) stems from an
inﬁnite iteration of the LO potential V (0). This is
good, because nuclear bound states and resonances,
as poles of T matrices, can only be obtained from
a nonperturbative LO.
• Equations (7) and (6) do not imply that all terms
in V should be treated on the same footing. One
cannot immediately identify µ with ν because a
term in V contributes to various orders in the T
matrix. Higher-order F (ν>0) can be obtained from
V (µ>0) in a distorted-wave Born expansion: F (1)
from a single insertion of V (1), F (2) from a single
insertion of V (2) or two insertions of V (1), and so
on. Treating the potential truncated at a sublead-
ing order exactly—i.e., treating it as a phenomeno-
logical potential—is in general not correct from a
renormalization point of view. In an expansion in
Q, the potential gets more and more singular with
increasing order. Resumming a partial subset of
higher-order terms will in general not include all
the LECs needed for proper renormalization. 4
The age-long challenge in nuclear physics has been to
achieve RG invariance when some interactions are non-
perturbative and yet some others can be treated as small.
In an EFT, that translates into the nontrivial task of
developing a power counting that guarantees Eqs. (4)
and (5). In a purely perturbative context the cutoﬀ de-
pendence of loops can be obtained analytically. Assum-
ing naturalness and looking at individual loop diagrams,
a simple rule has been devised for the size of the LECs
needed for perturbative renormalization (Manohar and
Georgi, 1984; Georgi and Randall, 1986). This “na¨ ıve di-
mensional analysis” (NDA) states that, for an operator
4 An example of resummation of higher-order interactions is
found in lattice implementations of Nonrelativistic QCD
(NRQCD) (Thacker and Lepage, 1991). In Heavy Quark Eﬀec-
tive Theory (HQET) all Q/mQ corrections in the heavy quark
massmQ are treated perturbatively, and lattice simulations have
a continuum limit (Sommer, 2010). For NRQCD, lattice practice
is to treat exactly not only heavy quark recoil but also the asso-
ciated, subleading gluon interactions. Thus, only for relatively
large values of the lattice spacing a do observables look like they
might converge, before 1/a-type eﬀects take over. There are also
situations where one can resum higher-order interactions with-
out introducing essential regulator dependence. An example is
given by Lepage (1997).
8
Oi in Eq. (2) with canonical dimension Di involvingNi
ﬁelds ψ,
ci =O
(
(4π)Ni−2
MDi−4
QCD
cired
)
, (9)
where the dimensionless “reduced” LECcired is of the or-
der of the combination of reduced QCD parameters that
give rise to it. Examples for Chiral Perturbation Theory
are given in Sec. IV. It is, however, not immediately ob-
vious that NDA applies to LECs of operators involving
four or more nucleon ﬁelds subject to nonperturbative
renormalization, i.e., which are renormalized once LO
interactions are resummed. In fact, as we are going to
see below, cutoﬀ variations in the Lippmann-Schwinger
equation (6) require signiﬁcant departures from NDA for
contact interactions among nucleons. These departures
were ﬁrst understood within Pionless EFT. Its simplicity
makes Pionless EFT the poster-child for nuclear EFT,
and we therefore make it the start of this review.
II. PIONLESS EFT
A. Motivation
At very low energies— i.e., for momenta Q≪ mπ—
few-nucleon systems are not sensitive to the details as-
sociated with pion (or other meson) exchange. This fact
makes it possible to describe such systems with short-
range interactions alone ( i.e. interactions of ﬁnite range
or falling oﬀ at least as an exponential in the interparticle
distance), an approach dating back to Bethe and his ef-
fective range expansion (ERE) for nucleon-nucleon (NN)
scattering (Bethe, 1949)—see also related work by Bethe
and Peierls (1935a,b); Fermi (1936); Schwinger (1947);
Jackson and Blatt (1950). Casting this basic idea into a
modern systematic framework leads directly to what has
become known as Pionless EFT.
Historically, Pionless EFT emerged out of the eﬀort
to understand the renormalization of EFTs where a cer-
tain class of interactions need to be treated nonpertur-
batively. It had been shown by Kaplan et al. (1996),
Phillips et al. (1998), and Beane et al. (1998b) that the
original prescription (Weinberg, 1990, 1991) to extend
Chiral Perturbation Theory to few-nucleon systems (dis-
cussed in Sec. IV) could not be implemented satisfying
RG invariance. It turned out that there is a surprisingly
rich structure of phenomena in the low-energy regime
where explicit pion exchange cannot be resolved.
Formally, the pion can be regarded as “integrated out”
if all other dynamical scales are much smaller than the
pion mass. Consider, for example, the Yukawa potential
corresponding to one-pion exchange:
⟨k′|V2N,π|k⟩∝ 1
q2 +m2π
, q = k′− k, (10)
q2 ≪ m2
π − →
+ · · ·
Figure 2 Reduction of pion exchange (dashed line) to a series
of contact interactions between nucleons (solid lines) forq2≪
m2
π.
where k and k′ are incoming and outgoing momenta of
two scattered nucleons (in their center-of-mass frame). If
these are both small compared tomπ, Eq. (10) can be ex-
panded in q2, with the leading term being just a constant
and the following terms coming with ever higher powers
of q2. This shrinking of the original interaction to a point
is illustrated in Fig. 2. Fourier-transforming into con-
ﬁguration space one obtains a series of delta functions
with a growing number of derivatives. In Chiral EFT,
which includes pions, analogous contact interactions rep-
resent the exchange of heavier mesons. Integrating out
pions to arrive at Pionless EFT means merging unre-
solved pion exchange with these operators. It should be
noted, however, that Chiral EFT is based on an expan-
sion around a vanishing pion mass, whereas Pionless EFT
treats mπ as a large scale. As such, these two EFTs are
very diﬀerent—in particular, the respective LECs cannot
in general be related by perturbative matching—but they
are both well-deﬁned low-energy limits of QCD.
In practice, one does not have to derive Pionless EFT
from a more fundamental EFT by integrating out explicit
pions. Instead, one can just follow the EFT paradigm
and write down an eﬀective Lagrangian, Eq. (2), with
all contact interactions between nucleons that are al-
lowed by symmetry. This restriction means that one re-
quires invariance under “small” Lorentz boosts (Galilean
boosts plus systematic relativistic corrections), rotations,
isospin, and discrete symmetries like parity and time re-
versal, the systematic breaking of which can also be ac-
counted for. The same EFT with other particles substi-
tuted for nucleons can describe diﬀerent systems where
the important dynamics takes place at distances beyond
the range of the force. Some of these systems are dis-
cussed in Secs. III and V. In particular, Pionless EFT
captures the universal aspects of Eﬁmov physics (Braaten
and Hammer, 2006).
In this section we discuss the basic features and for-
malism of Pionless EFT, ﬁrst in the context of two-body
systems (Sec. II.B) and later for a larger number of parti-
cles (Sec. II.C). Some of the outstanding issues are raised
in Sec. II.D.
9
B. Weakly bound S-wave systems
Two very-low-energy particles, represented by a ﬁeld
ψ, can be described by an eﬀective Lagrangian
L =ψ†
(
i∂0 + ∇2
2mN
)
ψ− C0
2 (ψ†ψ)2
+ C2
16
[
(ψψ)† (ψ
↔
∇
2
ψ) + H.c.
]
+··· , (11)
where
↔
∇ =
←
∇−
→
∇ is the Galilei-invariant derivative and
H.c. denotes the Hermitian conjugate. The “ ··· ” repre-
sent local operators with other combinations of deriva-
tives, including relativistic corrections. Here we have
adopted the notation of Hammer and Furnstahl (2000),
but various forms for the Lagrangian—diﬀering by pref-
actors absorbed in the low-energy constants (C0,C2, etc.)
or choice of equivalent operators—exist in the literature.
One can treat the two NN S-wave channels (3S1 or 1S0,
in the spectroscopic notation 2s+1lj wherel,s, and j de-
note respectively orbital angular momentum, spin, and
total angular momentum) simultaneously using a nucleon
ﬁeld N that is a doublet in spin and isospin space. We
will come back to this after discussing the general fea-
tures of the two-body sector on the basis of Eq. (11).
