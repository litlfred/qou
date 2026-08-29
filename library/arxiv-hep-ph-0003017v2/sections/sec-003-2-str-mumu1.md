---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "Random Matrix Theory and Chiral Symmetry in QCD J.J.M. Verbaarschot"
section_id: sec-003-2-str-mumu1
section_title: "Str (MU+M†U−1)"
section_number: 2
pages: 27-47
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
doc_brief: "Random Matrix Theory and Chiral Symmetry in QCD J.J.M. Verbaarschot — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---

,
(80)
where i
√
2Φ0/F = Str log U. This partition function is also known as the par-
tially quenched eﬀective partition function. It has been used to obtain a better
understanding of quenched lattice QCD results [104, 105]. The hat on Gl denotes
the maximum Riemannian submanifold of Gl(Nf + 1|1), and Str stands for the
supertrace. An example of an explicit parameterization of U will be given in the
next subsection. The parameter m2
0 is proportional to the topological suscepti-
bility and results in a mass for the singlet channel that does not vanish in the
chiral limit.
The perturbative formulation of this partition function was ﬁrst given by
Bernard and Golterman [104], and a perturbative calculation of the dependence
of the condensate on the spectral mass was ﬁrst performed in Ref. [106]. In that
case, it is acceptable to ignore the convergence properties of the eﬀective partition
function and integrate over the unitary supergroup instead.
An alternative generating function would be obtained by replacing the ratio of
the two determinants by detn(D + z) and putting n →0 after having calculated
the resolvent. This procedure, known as the replica trick [107], successfully repro-
duces the asymptotic expansions of the spectral correlation functions [108, 109].
There have been recent claims that it is possible to derive truly nonperturbative
results by means of the replica trick [110, 111, 112].
We do not believe that
this can be done in general [113, 114, 115]. As mentioned, because of the com-
pact/noncompact structure of the ﬁnal answer, the supersymmetric formulation
is the natural approach to this problem.
4.4
Domains of the Partially Quenched Eﬀective Theory
The Goldstone ﬁelds can be written as
U = ei
√
2Π/F .
(81)
28
J.J.M. Verbaarschot and T. Wettig
To second order in the ﬁelds, the eﬀective Lagrangian in momentum space is
given by
L = 1
V
X
a
X
k
(k2 + M2
a)Π2
a(k) ,
(82)
where the sum is over the momenta in a box of length L (including the zero-
momentum state) and the masses of the Goldstone bosons are denoted by Ma.
The sum over a is over the diﬀerent Goldstone modes. In addition to the usual
Goldstone modes with mass
M2
mm = 2mΣ
F 2
,
(83)
there are both fermionic and bosonic Goldstone bosons with mass
M2
mz = (m + z)Σ
F 2
(84)
and fermionic and bosonic Goldstone bosons with mass
M2
zz = 2zΣ
F 2 .
(85)
In the Lagrangian (82), one can distinguish the zero-momentum modes from the
nonzero-momentum modes. The magnitude of the ﬂuctuations of the nonzero-
momentum modes is of order 1/(k2 +M2
a), whereas the magnitude of the ﬂuctua-
tions of the zero-momentum modes is of order 1/M2
a. Since the smallest nonzero
momenta are of order 1/L, the ﬂuctuations of the zero-momentum modes are
dominant if
M2
a ≪1
L2 .
(86)
This means that the Compton wavelength of the “pion” is much larger than the
size of the box. For nonzero quark masses of order O(L0), the inequality (86)
is never satisﬁed.
However, the spectral mass z is a free parameter, and the
inequality can be rewritten as [116, 117]
z ≪Ec ≡F 2
ΣL2 .
(87)
We sometimes refer to the quantity Ec as the Thouless energy for reasons that will
become clear in Sec. 7.3. In the domain of Eq. (87), the dominant contributions to
the resolvent are from the zero-momentum modes. Thus, the partially quenched
eﬀective partition function (80) can be reduced to the partition function in the
zero-momentum sector [51, 52],
Z =
Z
U∈ˆ
Gl(Nf +1|1)
DUe
1
2V Σ Str (MU+M†U−1) .
(88)
The microscopic spectral density and the spectral correlations computed from
Eq. (88) are identical to those obtained in chRMT [116, 117]. Let us show this
by an explicit calculation of the dependence of the chiral condensate on the
spectral mass z. To cover the complete range (87), the integral over U has to
be done nonperturbatively. This is a straightforward superintegral that can be
evaluated using standard methods. The calculation of the integration measure
Random Matrix Theory and Chiral Symmetry in QCD
29
requires an explicit parameterization of the integration manifold. For example,
in the quenched limit, Nf = 0, a possible choice is
U =
 eiφ
α
β
es

(89)
with α and β Grassmann variables, φ ∈[0, 2π], and s ∈(−∞, ∞). A charac-
teristic feature of the integration manifold is that it consists of a compact and
a noncompact component. The valence-quark mass dependence of this partition
function and its generalization to arbitrary topological charge coincide with the
valence quark mass dependence of the chUE partition function. We merely quote
the ﬁnal result for the resolvent for Nf massless ﬂavors in the sector of topological
charge ν [116],
Σ(u)
Σ
= u [Ia(u)Ka(u) + Ia+1(u)Ka−1(u)] + |ν|
u ,
(90)
where a = Nf + |ν| and u = zV Σ. The compact/noncompact symmetries are
reﬂected in the appearance of the Ia/Ka-Bessel functions and are thus a natural
ingredient of the underlying integration manifold. This result was ﬁrst obtained
from chRMT by integrating the microscopic spectral density in Eq. (55) as follows,
Σ(u)
Σ
=
Z ∞
0
dζ
2u
ζ2 + u2 ρs(ζ) .
(91)
Alternatively, the microscopic spectral density can be obtained by taking the
discontinuity of Σ(u) according to Eq. (77). By integrating back, we ﬁnd that
the mass dependence of the zero-momentum partially quenched partition function
coincides with that of the chRMT partition function for β = 2.
Figure 2 presents a schematic picture of the diﬀerent domains in the Dirac
spectrum. There are other non-QCD theories that can be reduced to the same
partially quenched partition function. Probably the best known example is the
instanton liquid model of QCD [5]. Another example, more closely related to
disordered condensed matter systems, is the random-ﬂux model [118], which is
in essence quenched lattice QCD with Kogut-Susskind fermions but without the
phase factors due to the γ-matrices. Related examples are so-called two-sublattice
models with disorder [119], and disordered lattice models with the chiral and
ﬂavor symmetries of QCD [120, 121].
In the range
Ec ≪z ≪Λ ,
(92)
the eﬀective action (80) is still valid but chiral random matrix theory no longer
applies. In this range, the U ﬁelds can be expanded to second order in the pion
ﬁelds, and the spectral mass dependence of the chiral condensate can be obtained
to one loop order. The spectral density follows by taking the discontinuity of
Σ(z) across the imaginary axis. This calculation can be performed both for the
partition function of Eq. (80) and the eﬀective partition functions for β = 1 and
β = 4. The result for the slope of the spectral density at zero, valid for Nf ≥2,
reads [122, 26]
ρ′(0)
ρ(0) = (Nf −2)(Nf + β)
16πβNf
Σ
F 4 .
(93)
The result for β = 2 was ﬁrst derived by Smilga and Stern [122] from the scalar
susceptibility in standard chiral perturbation theory. We emphasize that this is
30
J.J.M. Verbaarschot and T. Wettig
QCD
6=
non-QCD
 
hiral
theories
z


p
qChPT
z

1
L
2
 
hRMT
Figure 2: Diagram illustrating the diﬀerent domains in the QCD Dirac spec-
trum. Here, pqChPT denotes partially quenched chiral perturbation theory, and
chRMT stands for chiral random matrix theory.
an exact result for the QCD Dirac spectrum that is valid in the thermodynamic
limit. The vanishing of the slope for Nf = 2 has been conﬁrmed by instanton
liquid simulations [123].
The two-point correlation function can also be obtained from a supersymmetric
generating function with, in this case, two diﬀerent spectral masses and two
bosonic superpartners [51].
Again the zero-momentum contribution coincides
with the chUE result. Let us consider the perturbative expansion of the two-
point correlation function. Generalizing Eq. (77), we obtain a relation between
the two-point level correlation function and the pion susceptibility [51, 124],
⟨ρ(λ)ρ(λ′)⟩C =
1
4π2
Σ2
F 4 Disc|z=iλ,z′=iλ′
X
q
1
(q2 + M2)2 ,
(94)
where the meson mass is given by M2 = (
√
z2 +
√
z′2)Σ/F 2 and the superscript
C denotes the connected part of the two-point function. By taking the discon-
tinuities of the zero-momentum contribution, we ﬁnd the two-point correlation
function [51]
⟨ρ(λ)ρ(λ′)⟩C ∼−1
2π2

1
(λ −λ′)2 +
1
(λ + λ′)2

,
(95)
Random Matrix Theory and Chiral Symmetry in QCD
31
which is the correct asymptotic result for the chUE.
4.5
QCD in Three Euclidean Dimensions
QCD in three Euclidean dimensions can be analyzed in much the same way as
discussed above. The main diﬀerence is the absence of the UA(1) symmetry and
the absence of instantons. In terms of the Dirac spectrum, the eigenvalues do not
occur in pairs ±iλ, and strictly zero eigenvalues are absent. The Dirac spectrum
of this theory on the microscopic scale can be analyzed along the same lines as
the four-dimensional theory. The microscopic spectral density and the Leutwyler-
Smilga sum rules have been derived [125, 126], the low-energy eﬀective theory
has been identiﬁed [125, 127], the mass-dependent microscopic spectral density
has been found [59, 128], universality has been studied [56, 129], and lattice QCD
studies have conﬁrmed the theoretical analysis [130].
5
UNIVERSAL PROPERTIES OF THE LATTICE QCD DIRAC
SPECTRUM
5.1
Unfolding
In order to compare eigenvalues of any physical system with RMT results, it
is necessary ﬁrst to “unfold” the empirical spectrum (see e.g. Ref. [131]). The
spacing ∆of the eigenvalues is related to the spectral density by
∆(E) = 1/ρ(E) .
(96)
Unfolding is a local rescaling of the energy scale so that the mean level spacing
of the unfolded eigenvalues is equal to unity throughout the spectrum.
This
is achieved by splitting the spectral density in an average density, ¯ρ(E), and a
ﬂuctuating piece,
ρ(E) = ¯ρ(E) + ρﬂ(E) .
(97)
The average spectral density can be obtained in diﬀerent ways. In some cases, it
can be computed analytically using semiclassical arguments. However, in most
cases ¯ρ(E) is obtained by averaging over many level spacings. There are two
essentially diﬀerent procedures to do this, spectral averaging and ensemble aver-
aging. Spectral averaging is appropriate if only one or a few spectra are available.
The average level spacing at E is then obtained by averaging over many level spac-
ings around E. Ensemble averaging is appropriate if there is a large ensemble
of spectra all drawn from the same statistical distribution. In this case, the av-
erage spacing can be obtained by averaging the spacing at E over each member
of the ensemble. In both cases, the separation of the spectral density into an
average and a ﬂuctuating piece requires a separation of scales that is typically
achieved only in the thermodynamic limit or in the semiclassical limit. The un-
folded spectrum, {xn}, is then obtained from the average spectral density (equal
to the inverse average level spacing) by
xn =
Z En
−∞
¯ρ(λ)dλ ,
(98)
where {En} is the original sequence of eigenvalues. The diﬀerence between the
two procedures is that spectral averaging yields ¯ρ(E) separately for each spectrum
32
J.J.M. Verbaarschot and T. Wettig
whereas ensemble averaging yields a single ¯ρ(E) for all spectra. In both cases,
the average spectral density of the unfolded spectrum becomes ¯ρ(x) = 1, so that
the sequence {xn} has an average level spacing equal to unity. The correlations
of the levels are always calculated for the unfolded spectrum.
The two procedures to calculate the average spectral density do not necessarily
give the same spectral correlations at long distances.
The equivalence of the
two is known as spectral ergodicity. This property has been shown analytically
for several random matrix ensembles [132, 133]. In general, ensemble averaging
results in stronger level ﬂuctuations than does spectral averaging [134, 135, 136].
In practice a mixture of both methods is often useful. For example, one may
calculate the average spectral density by ensemble averaging but, in order to get
better statistics, calculate the correlation functions by both ensemble averaging
and spectral averaging. Spectral averaging requires that the statistical properties
of the eigenvalues be stationary over the spectrum, which is not the case for many
systems and has to be checked each time.
5.2
Lattice Tests of Chiral Random Matrix Theory
We have presented a wealth of analytical evidence supporting the statement that
the local spectral correlations of the Dirac operator are described by universal
functions. Although the Dirac spectrum is not directly observable in experiments,
we can compare the predictions of chiral RMT to numerical data obtained by
lattice gauge simulations. This is the subject of this section.
This review does not discuss the global spectral density of the QCD Dirac op-
erator. Most lattice results have large ﬁnite-size artifacts. Instanton simulations
suggest, contrary to random matrix results, that the fermion determinant has a
signiﬁcant eﬀect on the global Dirac spectrum [50, 123, 137, 138].
5.2.1
BRIEF INTRODUCTION TO LATTICE QCD
QCD is a renormalizable quantum ﬁeld theory that must be regularized. This
can be done by formulating the theory on a discrete lattice with lattice spacing a
[139]. The largest momentum is then π/a. The quark ﬁelds live on the sites and
the gauge ﬁelds on the links of the lattice. If the lattice is ﬁnite, one can simulate
the theory on a computer. This can be done eﬃciently only in Euclidean space,
where the gluonic weight function is exp(−SYM) with SYM real. The discretized
form of the Yang-Mills action SYM is the Wilson action SW. The full weight
function of QCD also contains the fermion determinants, which can be expressed
in terms of the gauge ﬁelds. Observables are computed by generating gauge ﬁeld
conﬁgurations in a Monte Carlo update procedure and averaging an observable
over many conﬁgurations. Since the inclusion of the fermion determinants is very
time consuming, it is common to use only the gluonic part of the weight function
in the Monte Carlo updates. This is called the quenched approximation, which
corresponds to the limit Nf = 0 or, equivalently, to the limit of inﬁnitely heavy
sea quarks. To make contact with continuum physics, the results of lattice sim-
ulations must be extrapolated to inﬁnite lattice size (the thermodynamic limit)
and to zero lattice spacing (the continuum limit).
Lattice simulations are the main source of nonperturbative information about
QCD. Unfortunately, the naive discretization of fermions on a lattice leads to the
so-called doubling problem: The quark propagator has poles at each corner of
Random Matrix Theory and Chiral Symmetry in QCD
33
the Brillouin zone, which gives rise to a total of 2d species in d dimensions. The
unwanted 2d −1 species can be eliminated by adding to the Dirac operator an
additional term, the Wilson term, which removes the doublers in the continuum
limit. However, this term breaks chiral symmetry explicitly. Another possibility
is the use of staggered (or Kogut-Susskind) fermions where one has only one
spinor component per lattice site.
This maintains a residual chiral symmetry
but only partially reduces the number of species to 2d/2 in the a →0 limit.
A no-go theorem by Nielsen and Ninomiya [140] states that it is not possible
simultaneously to solve the doubling problem and have exact chiral symmetry on
the lattice with a local action.
Fortunately, there is a way around this theorem: the remnant chiral symmetry
condition of Ginsparg and Wilson [141],
Dγ5 + γ5D = 2aDγ5RD ,
(99)
where R is a spatially local operator that is trivial in Dirac space. In contrast to
{D, γ5} = 0, chiral symmetry is not exact but is recovered only in the continuum
limit a →0. Thus, with Dirac operators satisfying Eq. (99), it is possible to get
rid of the doublers even at ﬁnite lattice spacing without violating the Nielsen-
Ninomiya theorem. Recently, several solutions of Eq. (99) have been found in the
overlap formalism [142], in the domain-wall formulation in ﬁve dimensions [143],
and in the perfect action approach [144].
As mentioned in Sec. 2.2.3, there may be cases in which the anti-unitary sym-
metries of the various lattice discretizations of the Dirac operator diﬀer from those
of the continuum operator. In particular, this is true for staggered fermions. In
SU(2) color, staggered fermions are in the symmetry class of the chSE, whereas
continuum fermions are in the chOE symmetry class. Staggered fermions in the
adjoint representation of the gauge group (for any Nc) have the symmetries of the
chOE, whereas in the continuum limit the symmetries are those of the chSE. The
Wilson Dirac operator DW does not anticommute with γ5 and is therefore not de-
scribed by any of the chiral ensembles. However, the Hermitian operator γ5DW
has the same anti-unitary symmetries as the continuum Dirac operator and is
described by the corresponding nonchiral ensembles (see also Ref. [145]). Finally,
Dirac operators obeying the Ginsparg-Wilson condition, Eq. (99), have the same
anti-unitary symmetries as the continuum Dirac operator, but the eigenvalues
are located on the complex unit circle [62].
5.2.2
BULK CORRELATIONS
To measure the bulk spectral correlations, one needs all eigenvalues of the Dirac
operator, which is represented on the lattice by a ﬁnite sparse matrix whose
dimension is proportional to the lattice volume and to Nc. The eigenvalues of
such a matrix can be obtained using special algorithms, e.g. by the Cullum-
Willoughby version of the Lanczos algorithm [146]. On the lattice, this was ﬁrst
done by Kalkreuter [147]. The numerical eﬀort of this method scales with the
square of the matrix dimension.
For example, in SU(3) on a 104 lattice, the
Dirac matrix has 15,000 distinct positive eigenvalues, which can be computed
on a typical workstation in about 40 minutes. There are exact sum rules for
the sum of the squares of all Dirac eigenvalues, which can be used to check the
numerical accuracy. Because the number of eigenvalues per conﬁguration is very
large and because the ensemble average can be replaced by a spectral average
34
J.J.M. Verbaarschot and T. Wettig
Figure 3: Number variance Σ2(n), spectral rigidity ∆3(n), and nearest-neighbor
spacing distribution P(s) of the lattice Dirac operator with gauge group SU(2).
Top: Wilson fermions, V = 83 × 12, Nf = 2.
Bottom: staggered fermions,
V = 124, Nf = 4, ma = 0.05. (From Ref. [149]. Note that in Ref. [149], the
ﬁgure of P(s) for Wilson fermions shows data points for staggered fermions. This
has been corrected in the present ﬁgure.)
under the assumption of spectral ergodicity and stationarity, one needs only a
few conﬁgurations to construct the bulk spectral correlations with great accuracy.
The bulk correlations have been measured in a number of lattice studies for
all three symmetry classes [148, 149, 150, 135, 151, 152] and in instanton liquid
simulations [137] for β = 2. As mentioned above, they are insensitive to the
number of ﬂavors and the topological charge. In all cases, excellent agreement
with the predictions of the appropriate random matrix ensemble was obtained
(see e.g. Fig. 3). The agreement is perfect not only in the strong-coupling regime
but also at weak coupling. In fact, the bulk spectral correlations are given by
RMT even in the deconﬁnement phase [150, 151], indicating that the gauge ﬁelds
retain a suﬃcient degree of randomness in this region of the phase diagram.
Spectral ergodicity was investigated in Ref. [135], and the equivalent of a Thou-
less energy was found for ensemble averaging, whereas spectral averaging resulted
in complete agreement with RMT correlations over distances as long as several
hundred average level spacings.
5.2.3
MICROSCOPIC CORRELATIONS
Because only the lowest eigenvalues contribute to the microscopic spectral cor-
relations, a large number of statistically independent spectra are necessary. In
contrast to the bulk correlations, the microscopic correlations are sensitive to the
number of ﬂavors and the topological charge.
The RMT predictions do not contain an energy scale. In order to make com-
parisons with lattice data, one needs to determine the energy scale 1/V Σ to be
used in the RMT expressions, see e.g. Eq. (25). This can be done by extracting
Random Matrix Theory and Chiral Symmetry in QCD
35
Figure 4: Valence quark mass dependence of the chiral condensate Σ(mv) plotted
as Σ(mv)/Σ versus mvV Σ. The dots and squares represent lattice results by the
Columbia group [153] for the values of β indicated in the ﬁgure. The solid lines
are chRMT results. (From Ref. [116].)
ρ(0) from the data and applying the Banks-Casher relation, Eq. (20). Because
this procedure makes no reference to RMT, the comparisons of lattice data with
RMT are parameter-free.
The ﬁrst numerical results for the microscopic spectral density ρs were obtained
using instanton liquid conﬁgurations for Nc = 2, 3 and Nf = 0, 1, 2 [50], and
the expected agreement with the corresponding random matrix predictions was
found. The microscopic spectral density was ﬁrst observed on the lattice via the
dependence of the chiral condensate on a valence quark mass mv, as studied by
the Columbia group [153]. Figure 4 shows Σ(mv)/Σ as a function of mvV Σ for
diﬀerent values of the coupling constant [116]. The data for diﬀerent coupling
strengths in the broken phase fall on a single curve and agree with the chRMT
result for Σ(mv) for Nf = |ν| = 0, see Eq. (90).
This ﬁgure also shows a
deviation from the chRMT predictions at a scale that is of the order of the
Thouless energy given in Eq. (87). The spectral mass dependence of the chiral
condensate has recently been studied for diﬀerent symmetry classes and diﬀerent
types of fermions, and a similar quality of agreement has been found [154, 30].
The microscopic spectral correlations have also been investigated in great detail
on the lattice [155, 156, 130, 157, 158, 159, 154], and the random matrix predic-
tions were conﬁrmed with very high accuracy for all three symmetry classes. A
typical example is shown in Fig. 5.
Although most of these simulations have been performed in the quenched ap-
proximation, it is also possible to include dynamical fermions. Deviations from
the Nf = 0 results are observed only if the sea quarks are very light, with masses
on the scale 1/V Σ. Otherwise, the mass term in Eq. (1) dominates the small
eigenvalues in the factors of (iλn + mf). Analytical results for the microscopic
spectral correlations in the presence of sea quarks with mass ∼1/V Σ were ob-
tained in Refs. [160, 161, 162, 163, 85]. Lattice results in this regime agree very
36
J.J.M. Verbaarschot and T. Wettig
Figure 5: Distribution of the smallest eigenvalue (left) and microscopic spectral
density (right) of the staggered Dirac operator in quenched SU(2). The dashed
lines are the predictions of the chSE for Nf = 0 and ν = 0. (From Ref. [155].)
well with the corresponding RMT predictions [164]. In the Schwinger model, it
is numerically feasible to consider massless sea quarks, and the lattice data are
again well described by RMT [165].
Recall that the energy scale for the small eigenvalues is 1/V Σ.
Given the
agreement of the microscopic spectral quantities with RMT, this means that
RMT can be used to determine the inﬁnite-volume chiral condensate Σ [166].
This is most easily done by ﬁtting the numerically determined distribution of the
smallest eigenvalue to the RMT result. Since the lattice volume is known, this
immediately yields Σ.
5.2.4
TOPOLOGY
The random matrix predictions for the microscopic spectral correlations depend
on the number of zero modes of the Dirac operator and, thus, on the topological
charge ν of the gauge ﬁeld conﬁgurations.
Thus, one should sort the conﬁg-
urations according to their values of ν and make the comparison with RMT
separately in sectors of ﬁxed topological charge.
The results presented in the previous section were obtained for the staggered
Dirac operator. If one is interested in topological properties, this operator has
problems. The zero modes that one would obtain in the continuum limit are
shifted at ﬁnite lattice spacing a by an amount proportional to a2 [167]. For
reasonable simulation parameters, this amount is larger than the level spacing
near zero so that the would-be zero modes are completely mixed with the nonzero
modes. Thus, one should expect all spectra of the staggered Dirac operator, even
if computed from gauge ﬁeld conﬁgurations with nonzero topological charge, to
be described by the RMT results for ν = 0. This was indeed observed in the early
data [116, 155] and more recently conﬁrmed in a detailed study (though only in
strong coupling) [168]. As the continuum limit is approached, the would-be zero
modes should move toward λ = 0 and eventually separate completely from the
nonzero modes. This eﬀect has recently been observed in the Schwinger model
in two dimensions [169].
Random Matrix Theory and Chiral Symmetry in QCD
37
Figure 6: Distribution of the smallest Dirac eigenvalue in the ν = 1 sector for
all three symmetry classes.
The data were obtained using the overlap Dirac
operator on a 44 lattice. Solid lines represent the corresponding RMT results.
(From Ref. [152].)
Fortunately, Dirac operators satisfying the Ginsparg-Wilson condition (99) do
not have this problem. The overlap operator [142] has exact zero modes even at
ﬁnite lattice spacing, and the microscopic spectral correlations in sectors of ﬁxed
ν are in perfect agreement with the corresponding random matrix predictions
[165, 152, 154, 30, 170]. Figure 6 shows an example.
5.2.5
CHIRAL PHASE TRANSITION
As mentioned in Sec. 3.5, the microscopic correlations are given by chiral RMT
only if ρ(0)/V > 0, i.e. if chiral symmetry is spontaneously broken. Chiral sym-
metry is restored above a critical temperature Tc.
The way in which ρ(0)/V
approaches zero determines the order of the chiral phase transition and, if it is
second-order, the associated critical exponents. Lattice investigations of these
questions are very diﬃcult because at ﬁnite volume there are no sharp phase
transitions. Simulations are plagued by ﬁnite-size eﬀects, critical slowing down,
and other problems. It is therefore of great interest to investigate the fate of
the small Dirac eigenvalues at T = Tc analytically in random matrix models, as
was discussed at the end of Sec. 3.5. There are two recent lattice studies of this
question [171, 172]. Some of the theoretical expectations were conﬁrmed qualita-
tively, e.g. the gap in the eigenvalue distribution above Tc and the agreement of
the eigenvalue distribution in this region with the soft-edge predictions of RMT.
However, further studies are needed to clarify the situation at T = Tc. We are
looking forward to upcoming work in this area.
5.3
The Thouless Energy and Beyond
As discussed above, the Dirac spectrum is described by chRMT — or, equiv-
alently, by the zero-mode approximation of the low-energy eﬀective theory, —
only below the so-called Thouless energy Ec. The theoretical prediction for this
quantity [116, 117],
Ec ∼
F 2
Σ
√
V ,
(100)
38
J.J.M. Verbaarschot and T. Wettig
Figure 7: The data points represent the disconnected susceptibility computed on
the lattice in quenched SU(3) with staggered fermions (V = 104, β = 5.4). The
solid line is the prediction of chPT, the dashed line the prediction of chRMT.
(The dashed line is hidden by the data points for u < 10.) (From Ref. [175].)
has been conﬁrmed quantitatively in the instanton liquid model [137, 173] and on
the lattice [174, 158, 135]. To compute the Dirac spectrum beyond the Thouless
energy, the calculation must include the kinetic terms in the low-energy eﬀective
theory, as discussed in Sec. 4.
The results of such an analysis can again be
tested by lattice simulations. This has been done for staggered fermions [175].
Note that in this case, the eﬀective low-energy theory must be modiﬁed to take
into account the symmetries of staggered fermions at ﬁnite lattice spacing. A
convenient quantity to test the theory is the disconnected scalar susceptibility,
deﬁned by
χdisc(m) = 1
N
*
N
X
k,l=1
1
(iλk + m)(iλl + m)
+
−1
N
* N
X
k=1
1
iλk + m
+2
.
(101)
This quantity can also be computed in chRMT and in chiral perturbation theory
(chPT). The result of chRMT is expected to describe the data up to Ec. The
result of chPT should describe the data beyond Ec but is expected to break down
on the scale of the smallest eigenvalue, i.e. for m ∼1/V Σ. These expectations
are conﬁrmed by the lattice analysis (see Fig. 7 for an example).
6
SCHEMATIC MODELS
We wish to emphasize again that there are two diﬀerent types of applications of
RMT to physical problems. RMT may be applied as an exact theory for correla-
tions of eigenvalues, as discussed in the ﬁrst part of this review, or it may serve as
a schematic model for chaos and disorder in physical systems. Below, we intro-
duce a random matrix model for the chiral phase transition at nonzero chemical
potential and temperature. Random matrix theories as schematic models are
mostly used for a description of nonuniversal phenomena. This does not exclude
that they describe universal ﬂuctuations of the eigenvalues as well. Typically,
Random Matrix Theory and Chiral Symmetry in QCD
39
a random matrix model describes both universal and nonuniversal properties.
Well-known examples are the Anderson model for localization phenomena [176]
and the use of random matrix theory in quantum gravity [177, 178].
We argued in Sec. 1.1 that chiral symmetry breaking can be understood in
terms of the stiﬀness of the Dirac spectrum resulting from interactions of the
strong color force. Because spectral stiﬀness is a characteristic feature of RMT,
it is natural to describe the chiral phase transition in terms of a random matrix
model. Several diﬀerent types of schematic random matrix models have been
introduced. Here we discuss models for the chiral phase transition at nonzero
temperature T, for the chiral phase transition at nonzero chemical potential µ,
and for the phase diagram of QCD. We also discuss random matrix models for
diﬀerent types of fermions at µ > 0.
6.1
Chiral Random Matrix Models for the Chiral Phase Transition at
Nonzero Temperature
The original motivation for introducing chiral random matrix models was to ob-
tain a better understanding of the QCD Dirac spectrum for temperatures around
the critical temperature for the chiral phase transition [179, 180]. The idea is
to split the Dirac operator into the time derivative and a remainder that will be
replaced by a chRMT,
D = γ0∂0 + R .
(102)
In a chiral basis with time dependence given by exp[i(2n + 1)πTτ], where τ
is the Euclidean time, the ﬁrst term in D is diagonal and is given by a direct
sum of Matsubara frequencies ωn = (2n + 1)πT. The simplest model for D is
obtained by replacing the diagonal matrix with positive Matsubara frequencies by
the identity matrix times an eﬀective Matsubara frequency t, and replacing the
diagonal matrix with negative Matsubara frequencies by the opposite eﬀective
Matsubara frequency. After a suitable basis change, this model can be written
(in the sector of zero topological charge) as [179, 180]
ZNf (m) =
Z
DWdetNf (D + m)e−1
2NΣ2Tr (W †W ) ,
(103)
where
D =

0
iW + it
iW † + it
0

.
(104)
We restrict ourselves to the unitary case (β = 2) with a complex matrix W
of dimension N/2.
The integral is over the real and imaginary parts of the
matrix elements of W. For simplicity, we consider only a Gaussian probability
distribution. The normalization is such that the parameter Σ is equal to the
magnitude of the chiral condensate at zero temperature,
Σ = lim
m→0 lim
N→∞
1
NNf
∂m log ZNf (m)

t=0 .
(105)
It can be shown that the eﬀect of the fermion determinant on the macroscopic
spectral density is subleading in Nf/N, so that ρ(λ) can be calculated in the
quenched limit. By expanding the resolvent of the Dirac operator, deﬁned by
G(z) = 1
N Tr

1
z −D

,
(106)
40
J.J.M. Verbaarschot and T. Wettig
1
0.5
0
-4
-3
-2
-1
0
1
2
3
1.5
1
0.5
0
(z
)
z

t
Figure 8: The spectral density of the QCD Dirac operator as a function of an
eﬀective Matsubara frequency t that models the eﬀect of temperature. (From
Ref. [181].)
in a geometric series of the random matrix, it can be shown that g = G/Σ2
satisﬁes a cubic equation [179, 75, 181],
g3 −2zg2 + g(z2 −t2 + 1/Σ2) −z/Σ2 = 0 .
(107)
A variant of the method by which this equation was derived in Refs. [179, 75] is
sometimes referred to as the Blue’s function method [182]. The spectral density,
obtained from the discontinuity of the resolvent, is shown in Fig. 8. We observe
that chiral symmetry is broken up to t = 1/Σ with a chiral condensate given by
G(T, z →0) = Σ
q
1 −(Σt)2 .
(108)
Above this temperature, the spectrum splits into two disconnected regions. Since
this model has no spacetime dependence, it should not be a surprise that all
critical exponents are given by their mean ﬁeld values. From Eq. (108), we see
that β = 1/2. For t →1/Σ, we ﬁnd
G ∝z1/3 ,
(109)
resulting in another critical exponent δ = 3. The spectral density at the critical
point follows by taking the discontinuity of G across the imaginary axis, see
Eq. (77), and is thus given by
ρ(λ) = N
π λ1/3 .
(110)
The unfolded eigenvalues in this case are given by
xk = 3N
4π λ4/3
k
,
(111)
and a nontrivial scaling limit at t = 1/Σ is obtained by introducing the micro-
scopic variable [88, 89]
z = λN 3/4 .
(112)
Random Matrix Theory and Chiral Symmetry in QCD
41
Starting from the exact analytical result derived in Ref. [75], it is possible to take
the limit N →∞with the scaling relation (112) and to obtain an analytical result
for the microscopic spectral density at the critical point [88, 89]. We emphasize
that this result is based on mean ﬁeld critical exponents and is thus not applicable
to QCD with nontrivial critical exponents (see also the discussions in Secs. 3.5
and 5.2.5).
As a last application of the partition function (103), we mention the explanation
of the observation [153] that the temperature at which chiral symmetry is restored
is higher for gauge ﬁeld conﬁgurations with a nonzero Z3-phase than for gauge
ﬁeld conﬁgurations with zero Z3-phase. The explanation in terms of the random
matrix model (103) is that the lowest Matsubara frequency for the nonzero Z3-
phases is shifted to a lower value by the phase of the Polyakov loop, and thus the
critical temperature is higher [181].
6.2
Chiral Random Matrix Models at Nonzero Chemical Potential
6.2.1
QCD PARTITION FUNCTION AT NONZERO CHEMICAL POTEN-
TIAL
The QCD partition function at nonzero temperature T and chemical potential µ
is given by [183]
Z(m, µ, T) = Tr e−
HQCD−µN
T
=
X
α
e−Eα−µNα
T
,
(113)
where HQCD is the Hamiltonian of QCD with eigenvalues Eα and N is the quark
number operator. At zero temperature, only the states with Eα/Nα < µ con-
tribute to the partition function.
We thus expect that the partition function
is independent of µ below a critical chemical potential µc given by the lightest
baryon mass per unit quark number. Therefore, for µ < µc ≈mN/3 (where mN
is the nucleon mass), the baryon density remains zero and the chiral condensate
is constant.
The quark chemical potential appears in the Lagrangian in the form µψ†ψ =
¯ψ(µγ0)ψ and is therefore introduced in the Dirac operator by the substitution
∂0 →∂0 + µ .
(114)
This substitution destroys the Hermiticity properties of the QCD Dirac operator,
and the resulting complex phase of the fermion determinant makes Monte Carlo
simulations impossible. Because of the success of the quenched approximation in
lattice QCD simulations at µ = 0, it is tempting to ignore the fermion determinant
in this case. However, it was shown [184, 185] that the critical chemical potential
for quenched simulations is determined by the pion mass rather than the nucleon
mass. Obviously, the basic physics of the problem is not visible in the quenched
approximation. An analytical understanding of this problem was ﬁrst obtained
by means of a random matrix model for the Dirac operator of QCD at ﬁnite
density [186].
6.2.2
A RANDOM MATRIX MODEL FOR QCD AT FINITE DENSITY
A random matrix model for QCD at nonzero chemical potential model is obtained
by writing the Dirac operator as [186]
D(µ) = µγ0 + R
(115)
42
J.J.M. Verbaarschot and T. Wettig
and replacing R by a chiral random matrix ensemble. The partition function is
thus given by
ZNf (m) =
Z
DWdetNf (D + m)e−1
2NΣ2Tr (W †W )
(116)
with a Dirac operator given by
D =

0
iW + µ
iW † + µ
0

.
(117)
For QCD with three or more colors (chUE) this Dirac operator has no Hermiticity
properties. Therefore, the fermion determinant in Eq. (116) has a complex phase,
and the partition function cannot be simulated by Monte Carlo methods.
The partition function with Dirac operator (117) can be rewritten in terms of
a σ-model. For Nf = 1, the partition function is particularly simple,
Z(µ) =
Z
dσdσ∗[(σ + m)(σ∗+ m) −µ2]ne−n|σ|2 ,
(118)
where we have set Σ = 1 for ease of notation. For n = N/2 →∞the integrals
can be evaluated by a saddle-point approximation. In the chiral limit, we ﬁnd
that [186]
¯σ =
(
0
for
µ > µc
⇒
Z = µ2n
p
1 + µ2
for
µ < µc
⇒
Z = e−n(µ2+1)
(119)
with µc given by the point where the two partition functions are equal, i.e. µ2
c =
exp(−1 −µ2
c), which is solved by µc ≈0.53.
The vacuum properties of this
partition function depend on µ for µ ≤µc. The reason for this unphysical result
is discussed below in Sec. 6.2.4. As was demonstrated in Ref. [187] for β = 2, this
model does not show diquark condensation. However, a random matrix model
that does show diquark condensation was formulated in Ref. [188].
The QCD partition function (116) is a polynomial in m and µ with coeﬃcients
that can be obtained analytically [189]. Its properties can be analyzed by means
of its zeros in the complex chemical potential plane and the complex mass plane.
Figure 9 shows a ﬁrst-order phase transition at µ ≈0.53. In the chirally restored
phase, the cut on the imaginary m axis is no longer present. The ﬁgure also
shows the points (stars) where two solutions of the saddle-point equations of the
σ-model coincide. Indeed, the cuts end on these branch points.
In lattice QCD at ﬁnite density, the zeros of the QCD function in the complex
µ plane can be studied by means of the Glasgow method [190]. This method has
been analyzed in terms of the above random matrix model [191] with the conclu-
sion that it requires an exponentially large number of gauge ﬁeld conﬁgurations
to obtain statistically signiﬁcant results.
6.2.3
ZERO TEMPERATURE LIMIT
The random matrix model discussed in the previous section has attracted a great
deal of interest, and more sophisticated versions of this model have been proposed
[192, 189, 193, 194, 191].
One problem of the model (116) is that the chiral
condensate is µ-dependent below the critical value of the chemical potential. The
correct zero temperature limit, with a chiral condensate that remains constant
up to the critical value of the chemical potential, is obtained if all Matsubara
Random Matrix Theory and Chiral Symmetry in QCD
43
Figure 9: Zeros of the partition function in the complex µ and m plane. (From
Ref. [189].)
frequencies are taken into account.
We illustrate this with a one-dimensional
lattice QCD model.
Writing the Dirac operator as
D(µ) = γ0(∂0 + µ) + R ,
(120)
the µ-dependence of the fermion determinant can be gauged away by means of a
time-dependent gauge transformation, i.e.
γ0(∂0 + µ) + R = e−µτ [γ0∂0 + R] eµτ .
(121)
The µ-dependence is now in the boundary conditions, but for T →0 we expect
that they are not important and that the partition function becomes independent
of µ. The lesson is that in order to obtain a condensate that is µ-independent, one
must treat the time derivative exactly, or, in other words, all Matsubara frequen-
cies have to be taken into account. This was ﬁrst worked out in detail for lattice
QCD models at nonzero chemical potential [195]. Let us discuss the strong cou-
pling limit of a one-dimensional SU(Nc) lattice QCD model with Kogut-Susskind
fermions [196]. In that case, the matrix elements of the discretized Dirac operator
are given by
Dkl = δk,l−1Ukleµ −δk,l+1U†
kle−µ ,
(122)
where the indices are modulo N, the number of lattice sites. Antiperiodic bound-
ary conditions result in an extra minus sign for the matrix elements D1N and DN1.
The matrices Ukl are independent SU(Nc) matrices. By using gauge invariance,
one can reduce this partition function to a single SU(Nc) integral, which can be
44
J.J.M. Verbaarschot and T. Wettig
performed analytically, resulting in the partition function
ZN = 2 cosh(NcNµ) + sinh[(Nc + 1)N sinh−1 m]
sinh[N sinh−1 m]
.
(123)
The number of lattice sites N can be interpreted as the total number of Matsubara
frequencies. A sharp transition is obtained in the limit N →∞. For example,
the chiral condensate is given by [196]
lim
N→∞
1
N ∂m log ZN =
(
Nc/
√
1 + m2
for sinh µ < m ,
0
for sinh µ > m .
(124)
Similar results have been derived for a large-d strong coupling expansion of lattice
QCD at ﬁnite density [197] (with d the Euclidean dimensionality). The failure
of the quenched approximation has been reproduced in such lattice models. The
eﬀect of including all Matsubara frequencies has also been investigated in a ran-
dom matrix model obtained by replacing the remainder R in Eq. (120) by a
chiral random matrix. After ensemble averaging, one obtains a similar partition
function with similar conclusions [198].
6.2.4
QUENCHING AT NONZERO CHEMICAL POTENTIAL
The failure of the quenched approximation at nonzero chemical potential was ﬁrst
understood analytically in terms of chRMT by Stephanov [186]. He showed that
the quenched limit is the limit Nf →0 of a partition function with the absolute
value of the fermion determinant,
| det(D(µ) + m)|Nf ,
(125)
rather than
[det(D(µ) + m)]Nf .
(126)
The absolute value of the fermion determinant can be written as
det(D + m) det(D† + m∗) = det
 iW + µ
m
m
iW † + µ

det
 iW † −µ
m∗
m∗
iW −µ

.
(127)
Writing the fermion determinant as a Grassmann integral, we observe that the
quenched partition function can be interpreted as a partition function of quarks
and conjugate antiquarks. Therefore, in addition to the usual Goldstone modes,
we have Goldstone modes consisting of a quark and a conjugate antiquark [199,
186]. Such modes, with the same mass as the usual Goldstone bosons, have a
nonzero baryon number. The critical chemical potential given by the mass of
the lightest particle with nonzero baryon number is thus mπ/2. The failure of
the quenched approximation thus has an important beneﬁt: It allows us to write
down the exact low-energy eﬀective partition function, which is discussed in the
next section. The product of the two determinants in Eq. (127) can be written
as the determinant of a single Hermitian matrix. This procedure is known as
Hermitization [200, 201, 102].
6.2.5
QUENCHED DIRAC SPECTRA
A chRMT for quenched QCD at nonzero chemical potential is obtained by re-
placing the determinant in Eq. (116) by its absolute value. This model can be
Random Matrix Theory and Chiral Symmetry in QCD
45
solved analytically in the large-N limit [186]. However, we will follow a diﬀerent
approach by analyzing the corresponding eﬀective theory [202]. The advantage
of this approach is that the eﬀective theory is as valid for quenched QCD as it is
for the quenched chiral random matrix model.
For non-Hermitian matrices, the eigenvalues are scattered in the complex plane.
Using the fact that
∂z∗1
z = πδ2(z) ,
(128)
where the complex delta function is deﬁned as δ2(z) = δ(Re z)δ(Im z), we ﬁnd
that the two-dimensional spectral density is (up to a normalization constant)
given by
ρ(λ) = 1
π∂z∗G(z)

z=λ
.
(129)
The resolvent is deﬁned as
G(z) =
1
NfV ∂z log Z ,
(130)
and the quenched result is obtained in the limit Nf = 0 of the partition function
Z =
D
detNf (D(µ) + z)detNf (D†(µ) + z∗)
E
.
(131)
The product in Eq. (131) can be written as
detNf (D(µ) + z)detNf (D†(µ) + z∗) = det
 
iW12Nf + BR
ζ
ζ
iW †12Nf + BL
!
(132)
with
B ≡BR = BL =
 
µ1Nf
0
0
−µ1Nf
!
and
ζ =
 
z1Nf
0
0
z∗1Nf
!
,
(133)
where we have displayed the degeneracy in ﬂavor space by means of the identity
matrices 12Nf and 1Nf . For z = µ = 0, the quenched partition function is thus
invariant under SUR(2Nf) × SUL(2Nf). This symmetry is broken spontaneously
to the diagonal subgroup, SUV (2Nf).
At low energies, the eﬀective partition
function is therefore given by a partition function of Goldstone modes parame-
terized by matrices U ∈SU(2Nf). The static eﬀective Lagrangian is obtained
from the requirement that it should have the same symmetries as the underlying
microscopic partition function. The mass term was discussed in Sec. 4.1. The
chemical potential term remains invariant under SU(2Nf) × SU(2Nf) transfor-
mations if at the same time BR and BL, now considered as independent matrices,
are transformed as
BR →URBRU−1
R ,
BL →ULBLU−1
L
.
(134)
The matrices U in the Goldstone manifold transform as U →URUU−1
L . To lowest
nontrivial order in µ, we can write two invariant combinations,
Tr UBLU−1BR
and
Tr BB .
(135)
The coeﬃcients follow from the conditions that the critical chemical potential is
equal to one third of the mass of the lightest baryon and that the baryon density
46
J.J.M. Verbaarschot and T. Wettig
should vanish below µc. For the static limit of the eﬀective partition function,
we ﬁnd
Z =
Z
U∈SU(2Nf )
DUe−F 2V
4
Tr [U,B][U−1,B]+ 1
2ΣV Tr (MU+M†U−1) ,
(136)
with the mass matrix given by
M =
 
z1Nf
0
0
z∗1Nf
!
.
(137)
This partition function can be derived more elegantly by means of a local gauge
invariance principle [203, 204]. For real masses z the Dirac operator satisﬁes the
relation det(D†(µ)+z∗) = det(D(−µ)+z), so that the partition function deﬁned
in Eq. (131) and the corresponding low-energy eﬀective partition function given
in Eq. (136) can be interpreted as the partition function of QCD at ﬁnite isospin
density [205].
Below the critical chemical potential, µ < mπ/2, only the vacuum state con-
tributes to the partition function, so that
Z = eΣV Nf (z+z∗) .
(138)
In terms of the eﬀective theory, the saddle point is at U = 1. The resolvent (130)
is given by
G(z) =
1
NfV ∂z log Z = Σ .
(139)
Since G(z) does not depend on z∗, it follows from Eq. (129) that the spectral
density is zero in the region where (139) holds. Because m2
π = (z + z∗)Σ/F 2, see
Eqs. (83) through (85), the condition µ < mπ/2 means that the spectral density
vanishes everywhere except in a strip
|Re z| < 2µ2F 2
Σ
.
(140)
For z inside this strip, the Goldstone modes contribute to the partition func-
tion. In terms of the eﬀective partition function, the saddle point rotates away
from U = 1, leading to a nonvanishing diquark condensate.
The rotation of
the saddle point is a generic feature of low-energy eﬀective partition functions of
non-Hermitian ﬁeld theories [206, 207, 203, 204, 208].
These results are in qualitative agreement with spectra of the quenched lattice
QCD Dirac operator at µ̸ = 0 [184]. The correlations of the complex eigenvalues
are not so well understood, but the ﬁrst lattice QCD calculations [209] seem to
conﬁrm the theoretical expectations [210, 211, 212, 213].
6.3
Phase Diagram for the QCD Partition Function
The random matrix models at nonzero temperature and nonzero chemical po-
tential introduced in the previous sections can be merged into a single schematic
chRMT model for the chiral phase transition [183],
Z =
Z
DWdetNf

m
iW + iC
iW † + iC
im

e−1
2NΣ2Tr W W † ,
(141)
Random Matrix Theory and Chiral Symmetry in QCD
47
0
0.2
0.4
0.6
0.8
1
0.1
0.2
0.3
0.1
0.2
0.3
0.4
0.5
0.6
0.7
t

m
Figure 10: Phase diagram of QCD with two light ﬂavors of mass m as calculated
from the random matrix model. The almost parallel curves on the wing surface
are cross sections of this surface with m =constant planes. (From Ref. [183].)
where C is a diagonal matrix with Ckk = t −iµ for one half of the diagonal
elements and Ckk = −t −iµ for the other half. In the following, we set Σ = 1 for
simplicity.
This random matrix partition function can be rewritten as a σ-model. For the
case Nf = 1 it is given by
Z(t, µ) =
Z
dσe−N
