---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "Random Matrix Theory and Chiral Symmetry in QCD J.J.M. Verbaarschot"
section_id: sec-004-2-tr-ωσ
section_title: "Tr Ω(σ) ,"
section_number: 2
pages: 47-54
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
doc_brief: "Random Matrix Theory and Chiral Symmetry in QCD J.J.M. Verbaarschot — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
(142)
where
Ω(σ) = σσ∗−1
2 log[(σ + m)(σ∗+ m) −(µ + it)2]
−1
2 log[(σ + m)(σ∗+ m) −(µ −it)2] .
(143)
For t = 0 this is exactly the σ-model discussed in Sec. 6.2.2. At the saddle point,
the chiral condensate is given by the expectation value of σ. For m = 0 the
saddle-point equation is of ﬁfth order in σ,
σ[σ4 −2(µ2 −t2 + 1
2)σ2 + (µ2 + t2)2 + µ2 −t2] = 0 .
(144)
The critical points occur where one of the solutions of the quartic equation merges
with the solution σ = 0, i.e. along the curve (µ2 + t2)2 + µ2 −t2 = 0. At the
tricritical point, three solutions merge. This happens if in addition µ2−t2+ 1
2 = 0.
Figure 10 shows the phase diagram in the µtm-space. In the m = 0 plane,
we observe a line of second-order phase transitions and a line of ﬁrst-order phase
transitions.
They join at the tricritical point.
Also joining at the tricritical
point is a line of second-order phase transitions in the m-direction, which is the
boundary of the plane of ﬁrst-order transitions in µtm-space. This line is the
collection of end points of lines of ﬁrst-order phase transitions. We expect that
the critical exponents for such a liquid-gas transition are given by the three-
dimensional Ising model. The tricritical point was also found in a Nambu–Jona-
Lasinio model [214, 215].
48
J.J.M. Verbaarschot and T. Wettig
Because the saddle-point equation (144) is of ﬁfth order in σ, the critical prop-
erties of the random matrix model (141) are very similar to those of a φ6-theory.
The critical dimension at the tricritical point of such theories is three, so that
mean ﬁeld theory, and therefore RMT, describes the correct critical behavior at
this point. This random matrix model can be considered as the matrix equiv-
alent of a Landau-Ginzburg functional. The advantage over using the standard
Landau-Ginzburg theory is that in this case the spectrum of the Dirac operator is
also accessible. This allows us to study the critical properties of the Dirac eigen-
values. For example, for µ = 0 we have found that the distribution of the smallest
nonzero eigenvalue of the Dirac operator may serve as an order parameter for the
chiral transition [179].
6.4
Random Matrix Triality at µ̸ = 0
In previous sections, we have shown that the pattern of chiral symmetry break-
ing and the correlations of the Dirac eigenvalues are related to the anti-unitary
symmetries of the Dirac operator. Since the chemical potential occurs only in
the combination ∂0 + µ, the anti-unitary symmetries at µ̸ = 0 are the same as
for zero chemical potential. Thus for QCD with two colors and fermions in the
fundamental representation the Dirac operator is real (β = 1), whereas for QCD
with adjoint fermions the Dirac operator is quaternion real (β = 4). In the ﬁrst
case, the Dirac operator has the structure [193]
D =

0
W + µ
−W T + µ
0

with W real.
(145)
In the second case, D is given by
D =

0
W + µ
−W † + µ
0

with W quaternion real.
(146)
In this case, the quaternion real matrix elements of W satisfy the reality relation
W ∗
kl = σ2Wklσ2. In both cases, it is easy to show that the fermion determinant
is real. Furthermore, because of
detNf W detNf W T = det2Nf W
for β = 1,
(147)
detNf W detNf W † = det2Nf W
for β = 4,
(148)
the ﬂavor symmetry group is enhanced to U(2Nf) in both cases (for ν = 0).3
The full ﬂavor symmetry is broken spontaneously to Sp(2Nf) and O(2Nf), re-
spectively, and is broken in the same way by the mass term.
The chemical
potential breaks the symmetry according to U(2Nf) →U(Nf) × U(Nf) in both
cases. For both β = 1 and β = 4 the pseudoreality of the Dirac operator leads
to Goldstone modes with a nonzero baryon number in the same way we have
seen for the phase quenched partition function. An exact low-energy eﬀective
partition function valid to lowest order in m and µ2 can be written down [204].
3For β = 4 and µ = 0, the Dirac operator satisﬁes the relation (CD)T = −CD whereas
(Cµγ0)T = Cµγ0 (with C the charge conjugation matrix). Therefore, for β = 4 and µ̸ = 0,
the Pfaﬃan of the Dirac operator is not deﬁned and the fermion determinant detNf /2(D + µγ0)
cannot be expressed as an integral over Nf Majorana fermions with ﬂavor symmetry U(Nf), as
discussed in Sec. 2.2.3. Instead, we write detNf (D + µγ0) as an integral over Nf Dirac fermions
with ﬂavor symmetry U(2Nf).
Random Matrix Theory and Chiral Symmetry in QCD
49
Figure 11: Scatter plot of the real (x) and imaginary (y) parts of the eigenvalues
of the random matrix Dirac operator at nonzero chemical potential. The val-
ues of β and µ are given in the ﬁgures. Full curves show the analytical result
for the boundary. The line along the imaginary axis for β = 1 represents the
accumulation of eigenvalues on this axis. (From Ref. [193].)
For an elaborate discussion of the symmetries, their breaking pattern, and the
low-energy eﬀective theory in both cases, see Ref. [204].
For an even number of ﬂavors, dynamical Monte Carlo simulations are possible
for β = 1 and β = 4, though not for β = 2. However, quenched simulations
have been performed for all three classes. A cut along the imaginary axis below
a cloud of eigenvalues was found in instanton liquid simulations [216] for Nc = 2
at µ̸ = 0, which corresponds to β = 1. In lattice QCD simulations with staggered
fermions for Nc = 2 [217], a depletion of eigenvalues along the imaginary axis
was observed, whereas for Nc = 3 the eigenvalue distribution did not show any
pronounced features [184].
A chiral random matrix model for the Dirac operator at µ̸ = 0 in each sym-
metry class is obtained by drawing the matrix elements of W from a Gaussian
probability distribution. In the quenched approximation, the spectral proper-
ties of the random matrix Dirac operator of Eq. (117) can easily be studied
numerically by diagonalizing a set of matrices with the probability distribution
of Eq. (116). Figure 11 shows results [193] for the eigenvalues of a few 100 × 100
matrices for µ = 0.15 (dots). The solid curves represent the analytical result
for the boundary of the domain of eigenvalues derived in Ref. [186] for β = 2.
However, the analysis can be extended [193] to β = 1 and β = 4, and with the
proper scale factors, the solution is identical.
For β = 1 and β = 4 we observe exactly the same structure as in the previously
mentioned (quenched) QCD simulations. There is an accumulation of eigenvalues
on the imaginary axis for β = 1 and a depletion of eigenvalues along this axis for
β = 4. The depletion can be understood as follows. For µ = 0 all eigenvalues
are doubly degenerate. This degeneracy is broken at µ̸ = 0, which produces the
observed repulsion between the eigenvalues.
The number of purely imaginary eigenvalues for β = 1 scales as
√
N and is
thus not visible in a leading-order saddle-point analysis. Such a
√
N scaling is
typical for the regime of weak non-Hermiticity ﬁrst identiﬁed by Fyodorov et
al.
[211].
Using the supersymmetric method of RMT, Efetov [207] obtained
50
J.J.M. Verbaarschot and T. Wettig
the
√
N dependence analytically. The case β = 4 was also analyzed analytically
[218], with results that are in complete agreement with the numerical simulations.
Obviously, more work is needed in order to arrive at a complete characterization
of universal features [212] of the spectrum of non-Hermitian operators.
7
RELATED MODELS AND RELATIONS TO OTHER FIELDS
Random matrix theory has been used extensively in many diﬀerent ﬁelds includ-
ing nuclear physics, atomic and molecular physics, condensed matter physics,
quantum chaos, quantum gravity, and mathematical physics. Before reviewing a
few applications that might have some relation to QCD, we brieﬂy discuss another
class of matrix models for the QCD partition function. For a more comprehensive
review of the material in this section, see Refs. [18, 219, 220, 221, 222].
7.1
One-Plaquette Models of Lattice QCD
One class of matrix models for QCD are lattice QCD partition functions on a 2d
lattice. The simplest model in this class is the one-plaquette partition function
for pure gauge theory in d = 2. This model is known as the Br´ezin-Gross-Witten
model [223] and is deﬁned by
Z(J, J†) =
Z
U∈U(N)
DUeTr (JU†+J†U) ,
(149)
where the integral is over the Haar measure of U(N) and J is an arbitrary complex
source term. We have shown that this partition function can be expressed as a
determinant of modiﬁed Bessel functions [90, 23, 93]. For J a multiple of the
identity (with the interpretation of J ∼1/g2, where g is the Yang-Mills coupling
constant), this model was solved analytically in the large-N limit by Gross and
Witten. They found a third-order phase transition at a critical value of J. A
large-N chiral phase transition is obtained by extending this model with a fermion
determinant [224]. Despite considerable eﬀort, the generalization of this model
to more than two dimensions, which is known as the Eguchi-Kawai model [225],
could not be solved analytically [226].
The Br´ezin-Gross-Witten model [223] can be rewritten as a generalized Kont-
sevich model, which has received a great deal of attention in the theory of exactly
integrable systems [227, 222]. There are many other relations between RMT and
the theory of exactly solvable systems. Among others, the asymptotic properties
of correlation functions can be derived by means of conformal ﬁeld theory [228].
An interesting overview in the context of string theory is given in Ref. [227].
Another class of related models is the Kazakov-Migdal model [229], which is
also known as induced QCD. In its simplest form it is deﬁned by
Z =
Z
DHDUe
P
x Tr H2(x)+P
x,µ Tr [U(x)H(x)U†(x)H(x+µ)] ,
(150)
where the H(x) are Hermitian matrices and the U(x) are unitary matrices. The
sum is over a lattice in d dimensions. A zero-dimensional form of this model was
proposed as a model for the transition between Poisson statistics and Wigner-
Dyson statistics [230, 173].
Random Matrix Theory and Chiral Symmetry in QCD
51
7.2
Universal Conductance Fluctuations in Disordered Mesoscopic
Systems
In condensed matter physics, a mesoscopic system is a system whose linear size is
larger than the elastic mean free path of the electrons but smaller than the phase
coherence length, which is essentially the inelastic mean free path.
A typical
size is about 1 µm. The conductance g of mesoscopic samples is closely related
to their spectral properties. Using a scaling block picture, Thouless found that
in the diﬀusive regime, the conductance is given by g = EC/∆, where EC/¯h is
the inverse diﬀusion time of an electron through the sample and ∆is the mean
level spacing [231]. This can be rewritten as g = ⟨N(EC)⟩, where ⟨N(E)⟩is the
mean level number in an energy interval E.
Thus the variance, ⟨δg2⟩, of the
conductance is related to the number variance, Σ2, of the energy levels [232].
Low-temperature experiments have been performed in which the conductance
of mesoscopic wires was measured as a function of an external magnetic ﬁeld. The
observed ﬂuctuations in g are of the order of e2/h, independent of the details of
the system (shape, material, etc). These are the so-called universal conductance
ﬂuctuations [233]. One can understand this phenomenon qualitatively by esti-
mating the number ﬂuctuations of the electron levels using RMT results. Both
the magnitude of the ﬂuctuations and their universality can be obtained through
the transfer matrix method. An interesting numerical result is that the density
of eigenvalues of the transmission matrix in the Hofstadter model for universal
conductance ﬂuctuations can be described in terms of the microscopic spectral
density of the chUE [234, 235].
7.3
Anderson Localization
In more than two dimensions, a good conductor becomes an insulator when the
disorder becomes suﬃciently strong. This phenomenon is called Anderson local-
ization. In the localized phase, the wave function of the electron is not described
by Bloch waves, but by a localized form that decays exponentially,
ψ(r) ∼e−r/Lc .
(151)
The length scale Lc is known as the localization length. This phenomenon was
ﬁrst described by the Anderson model [176], which is a hopping model with a
random potential on each lattice point. The dimensionality of the lattice plays an
important role. It has been shown that in one dimension all states are localized.
The critical dimension is two, whereas in three dimensions there is a delocalization
transition at an energy EL. The states below EL are localized whereas the states
above EL are extended, i.e. with a wave function that scales with the size of
the system. The eigenvalues of the localized states are not correlated, and their
correlations are described by the Poisson distribution.
An interesting question is whether Dirac eigenfunctions can be exponentially
localized. Parisi argued that localized states can only occur in quenched systems
[236]. In QCD this argument goes as follows. If the eigenfunctions were spatially
localized, the eigenvalues would be uncorrelated, and there would be no repulsion
between the eigenvalues. Because of the fermion determinant and the measure
in Eq. (34), the eigenvalues would be repelled from the origin. Since there would
be no mechanism to compensate for this repulsion, ρ(0)/V and the chiral con-
densate would be zero. Therefore, if chiral symmetry is spontaneously broken,
52
J.J.M. Verbaarschot and T. Wettig
the eigenfunctions of the Dirac operator must be spatially extended. Indeed, this
has been found for the wave functions of the Dirac operator for a gauge ﬁeld
ensemble given by a liquid of instantons [137] as well as in lattice QCD [237].
In the extended domain, the situation is more complicated.
An important
energy scale is the Thouless energy [231], which is related to the diﬀusion time
of an electron through the sample (see Sec. 7.2). With that diﬀusion time given
by L2/D (the diﬀusion constant is denoted by D), the Thouless energy is [238]
Ec = ¯hD
L2 .
(152)
On time scales larger than ¯h/Ec, an initially localized wave packet diﬀuses all over
phase space. If this wave function ψ(t) at t > ¯h/Ec is expressed as a superposition
of eigenfunctions φi(t = 0), many of the overlaps ⟨ψ(t)|φi⟩are nonzero. Therefore
we expect that for energy diﬀerences below Ec the eigenvalues are correlated
according to RMT.
The diﬀusive behavior of electrons is described by Goldstone modes, called
diﬀusons.
Classically, they satisfy a diﬀusion equation [238, 239, 102].
The
diﬀusion modes can be described in terms of a σ-model, which has the same
structure as the low-energy eﬀective theory for the QCD partition function. The
Thouless energy corresponds to the energy scale below which the ﬂuctuations of
the zero-momentum modes dominate the ﬂuctuations of the nonzero-momentum
modes, i.e. the scale discussed in Sec. 4.4, below which the QCD Dirac spectra
are given by chRMT. The analysis of classically chaotic quantum systems has
made it clear that spectra are described by RMT if and only if the corresponding
classical motion is chaotic [240, 241]. If we interpret the Dirac operator as a
Hamiltonian in four Euclidean dimensions plus one artiﬁcial time dimension,
we thus conclude that the classical motion of the quarks is chaotic4 [99] and
therefore diﬀusive in four Euclidean dimensions and one artiﬁcial time dimension,
in agreement with the interpretation of Goldstone modes as diﬀusion modes [239,
243]. The equivalent of the diﬀusion constant can be read oﬀimmediately by
comparing the two σ-models, or equivalently by comparing the scale of Eq. (87)
with the Thouless energy, and is given by D ∼F 2/Σ [137, 244].
Quantum
mechanically, the Thouless energy can be interpreted as the spreading width of
the exact eigenstates over the states of the noninteracting Hamiltonian [245, 246].
7.4
Non-Hermitian Models with Disorder
In the past few years, several non-Hermitian models with disorder have been
introduced in the literature. We mention only the simplest model, which was
motivated by the study of ﬂux-line pinning in superconductors [247, 248]. Its
Hamiltonian is given by
H =
1
2m(p + ih)2 + V (r) ,
(153)
where V (r) is a random disorder potential, p is the momentum operator, and ih
is a constant imaginary vector potential. The new feature of such models is that
a localization-delocalization transition can occur even in one and two dimensions.
Although the wave functions corresponding to real eigenvalues remain localized,
4There is an elaborate literature on the classical dynamics of gauge ﬁelds. For a discussion
of this topic, see Ref. [242].
Random Matrix Theory and Chiral Symmetry in QCD
53
the wave functions of complex eigenvalues can be extended. For a detailed dis-
cussion of such models, see Refs. [201, 249].
The dependence on h in the Hamiltonian H occurs only in the combination
p + ih, i.e. in exactly the same way as the chemical potential in the QCD Dirac
operator. There are two important diﬀerences from QCD: (a) the operator H
does not have a chiral structure, and (b) the disorder is uncorrelated Gaussian and
quenched. The connection between delocalization in the Hatano-Nelson model
(153) and diquark condensation in quenched QCD at nonzero chemical potential
is not yet understood and deserves further attention.
After the initial work of Ginibre [210], non-Hermitian RMT has received a
great deal of attention in the mathematics literature as well. Probably the best
overview of results in this area is in the book by Girko [200].
7.5
Andreev Scattering
The term Andreev scattering (or Andreev reﬂection) refers to a process in which
an electron hits the interface between a normal metal and a superconductor and
is reﬂected as a hole with the opposite momentum (or vice versa) [250]. Stated
diﬀerently, two electrons can tunnel through the interface so that a Cooper pair
is added to the superconducting condensate (or removed from it). This process
can be described in a microscopic mean ﬁeld model by the Bogoliubov-deGennes
Hamiltonian, which can be written in matrix form as
H =
 A
B
B†
−AT

,
(154)
where A (−AT ) represents the Hamiltonian for particles (holes) and B represents
the pairing ﬁeld. The requirement that H be Hermitian means that A must be
Hermitian. If the system under consideration is invariant under time reversal
or spin rotation or both, there may be additional symmetries. If the system is
invariant under spin rotation, B is symmetric (in this case we consider the Hamil-
tonian in the space of spin-up states only). If, in addition, the system is invariant
under time reversal, the elements of H are real. Otherwise, they are complex. On
the other hand, if the system is not invariant under spin rotation, B is antisym-
metric. In this case, if the system is invariant under time reversal, the elements
of H are quaternion real. Otherwise, they are complex. This classiﬁcation es-
tablishes four new random matrix ensembles [251, 33]. The microscopic spectral
correlations of these ensembles are identical to those of the chiral ensembles if
the parameters (the Dyson index β and the number of massless ﬂavors Nf) are
chosen appropriately.
7.6
Mathematical Physics and Quantum Gravity
RMT has received a great deal of attention as a problem in mathematical physics.
We mention the relation between universal behavior in RMT and the asymptotic
behavior of orthogonal polynomials [42, 43, 65, 252, 253], the relation between
the classiﬁcation of random matrix ensembles and the Cartan classiﬁcation of
symmetric spaces [34], and the theory of Riemannian superspaces [34].
Vari-
ous methods for the solution of random matrix problems have been proposed.
We mention the mapping to a gas of noninteracting fermions, the Coulomb gas
method [27], the Brownian motion method [27], the replica method [107], the
54
J.J.M. Verbaarschot and T. Wettig
orthogonal polynomial method [17], the supersymmetric method [102], and the
operator method [177].
Generally, the problem for β = 2 is much simpler than for β = 1 and β = 4.
Nevertheless, a great deal of progress has been made for β = 1 and β = 4.
We mention relations between the kernels of the correlation functions [47, 48,
82, 83] and the relation between massless and massive correlators [85]. Novel
mathematical methods have been developed for β = 1 and β = 4. We mention
only the skew-orthogonal polynomial method [254, 255, 43, 47] and the extension
of an operator method for β = 2 [81, 256, 82].
There exists an elaborate literature on the random matrix formulation of 2-
d quantum gravity (see e.g. the recent reviews by Abdalla et al. [178] and Di
Franceso et al. [177]). The idea is that the partition function, which is a sum
over all metrics, can be rewritten as a sum over random surfaces. The sum over
the dual graphs of a discretization of these random surfaces can be rewritten in
terms of a random matrix partition function that can be analyzed with standard
random matrix methods.
8
