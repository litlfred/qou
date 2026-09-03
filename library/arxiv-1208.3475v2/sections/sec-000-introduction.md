---
doc_id: arxiv-1208.3475v2
doc_title: "Poisson - Random Matrix transition in the QCD Dirac spectrum Tamás G. Kovács Institute for Nuclear Research of the Hungarian Academy of Sciences"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-6
source_pdf: 1208.3475v2.pdf
source_sha256: d53fc4eefa070ba3
doc_brief: "Poisson - Random Matrix transition in the QCD Dirac spectrum Tamás G. Kovács Institute for Nuclear Research of the Hungarian Academy of Sciences — 9 sections: Introduction; What is the distance scale"
---
The spectrum of the QCD quark Dirac operator is a
quantity not directly accessible by experiments but it
contains essential physical information concerning the be-
havior of strongly interacting systems. The most well-
known example of that is the Banks-Casher relation im-
plying that a non-vanishing Dirac spectral density at zero
indicates the spontaneous breaking of chiral symmetry
[1]. Another prominent example is that in the interme-
diate volume so called “epsilon-regime” the lowest part
of the Dirac spectrum is described by Random Matrix
Theory (RMT) which makes it possible to extract the
low-energy constants of chiral perturbation theory from
the eigenvalues of the Dirac operator (see e.g. [2] and ref-
erences therein). More recently the Dirac spectrum has
also been used to determine the mass anomalous dimen-
sion of QCD-like theories with many fermions [3]-[6].
Since at low-temperature the low-lying Dirac spectrum
has been so extensively studied it is surprising how lit-
tle is known about it in the high-temperature regime.
The only solid piece of information above the ﬁnite tem-
perature cross-over is that since chiral symmetry is re-
stored there the spectral density of the Dirac operator
should vanish at zero. In principle Random Matrix The-
ory also has predictions for the spectral statistics at such
a “soft edge”. However, unlike at zero temperature, at
high temperature a priori there is no reason to believe
that the QCD Dirac spectrum is described by this edge
RMT statistics. Indeed, attempts to verify this numeri-
cally did not produce fully convincing results [7, 8].
It turns out that random matrix statistics is only one
of two possible extremes concerning the eigenvalue statis-
tics. It corresponds to the case of completely delocalized
eigenvectors occurring only if typical (gauge ﬁeld) ﬂuctu-
ations can easily mix eigenmodes nearby in the spectrum.
The other extreme possibility is localized eigenmodes
that cannot be mixed by typical ﬂuctuations. In that case
the spectrum consists of independent eigenvalues obey-
ing Poisson statistics. Many examples of both types of
behavior in large linear systems are known both in the
mathematics and in the physics literature. In fact the
Bohigas-Giannoni-Schmit conjecture asserts that quan-
tum systems whose classical counterparts are chaotic ex-
hibit random matrix type spectra whereas integrable sys-
tems after quantization have Poisson-type spectra [9]. An
example where the same physical system, depending on
the circumstances, can exhibit both types behavior is An-
derson localization [10].
In that case the transition of
single electron states from delocalized ones described by
RMT statistics to localized states with Poisson statistics
is driven by impurities in the crystal lattice.
Already a long time ago the idea was put forward that
such a transition might also occur in QCD at ﬁnite tem-
perature [11]. Later on numerical studies concluded that
it is not the case and the Dirac spectrum is described
by RMT even above the ﬁnite temperature deconﬁning
and chiral transition [12]. This conclusion, however, was
based on the study of full Dirac spectra. It is known that
in the case of the Anderson transition for weak disorder
only the states along the band edge become localized and
states deep inside the band can still remain delocalized.
Therefore a statistical analysis of full spectra might not
reveal a localization transition occurring only along the
band edge.
With this additional insight the idea of a localization-
delocalization transition in QCD at Tc was revived some-
time later [13]. Both instanton liquid calculations [14]
and lattice QCD simulations were [15] done to provide ev-
idence that such a transition occurs at Tc. However, these
calculations were performed around the critical tempera-
ture and therefore it was not possible to see clear Poisson
statistics in the spectrum. For that lattice simulations
were needed well above Tc where localized modes are
fully developed. Indeed, further support for localization
in QCD was obtained by a detailed demonstration that
the lowest two eigenvalues of the overlap Dirac operator
in quenched SU(2) gauge theory obey Poisson statistics
[16]. Finally in the same system a clear transition was
2
observed in the spectrum of the staggered Dirac operator
from localized Poisson modes to delocalized RMT modes
[17].
The picture emerging from these studies is that
above the ﬁnite temperature transition the lowest part
of the Dirac spectrum consists of localized modes obey-
ing Poisson statistics. Higher up in the spectrum there
is a cross-over to delocalized modes described by random
matrix statistics. In the meantime, independently, other
groups also observed the tendency of low modes to be-
come localized above Tc [18], although the connection to
an Anderson-type transition was not made by them. A
useful account of the spatial structure of low Dirac modes
and their localization properties can also be found in [19].
So far all the direct evidence for the transition came
from quenched SU(2) simulations. In the present paper
we study the question whether full QCD with physical
light dynamical quarks also exhibits delocalized Dirac
modes above Tc.
The question is non-trivial since
light dynamical quarks suppress the lowest quark modes
through the quark determinant in the action.
Never-
theless we ﬁnd that localization also occurs in full QCD
with quarks of physical masses. We demonstrate this by
presenting the results of lattice QCD simulations with
Nf = 2 + 1 ﬂavors of dynamical staggered quarks. We
also study how the location of the transition within the
spectrum depends on the physical temperature.
The paper is organized as follows. At ﬁrst in Section
II we summarize the technical details of our QCD lat-
tice simulations. In Section III we describe the analogy
between the QCD delocalization-localization transition
and the Anderson transition. Here we analyze in detail
the unfolded level spacing distribution that can be used
to distinguish between localized and delocalized modes.
We show that in larger spatial volumes the transition
becomes sharper and most likely in the thermodynamic
limit it becomes a genuine phase transition. Also in this
Section we show how to compute the mobility edge sep-
arating localized and delocalized states in the spectrum
and analyze localization in terms of the participation ra-
tio of eigenmodes. In Section IV we study how the transi-
tion scales in the continuum limit. In particular, we show
that the localization length of localized states is always
smaller than the inverse temperature. We also demon-
strate that the properly renormalized mobility edge scales
in the continuum limit and investigate its temperature
dependence in the temperature range 1.7Tc < T < 5Tc.
Finally, in Section V we summarize our results and indi-
cate further questions.
II.
SIMULATION DETAILS
At ﬁrst we summarize the details of our lattice simula-
tions. We use the Symanzik improved gauge and and the
two level stout smeared staggered fermion action of Ref.
[20] with Nf = 2 + 1 ﬂavors. We take the simulation pa-
rameters from the work of the Budapest-Wuppertal col-
laboration who determined the lattice spacing from the
β
mud
ms
a(fm)
3.75
0.001786
0.05030
0.125
3.938
0.001172
0.03300
0.082
4.08477
0.000836
0.02354
0.062
TABLE I. The bare parameters we used in the lattice simu-
lations; the inverse gauge coupling (β), the light quark mass
(mud), the strange quark mass (ms) and the corresponding
lattice spacing (a).
kaon decay constant fK and set the bare quark masses
by requiring the pion and kaon masses to be equal to
their physical value [21]. The bare parameters we used
and the corresponding lattice spacings are summarized
in Table I.
To explore the dependence of the localized-delocalized
mode transition on the temperature and the lattice spac-
ing we performed the simulations at three diﬀerent lattice
spacings a = 0.06, 0.082 and 0.125 fm and three diﬀerent
temporal lattice extensions Nt = 4, 6, 8.
The physical
temperature of the system is set by its temporal exten-
sion as
T =
1
Nta.
(1)
In this way the lattice parameters we used correspond to
the physical temperature range of 1.7Tc < T < 5Tc.
To understand the nature of the transition it is crucial
to consider the spatial volume dependence of spectral and
wave function statistics. For this reason we also repeated
some simulations on diﬀerent spatial volumes. The spa-
tial linear size of the boxes we used were all in the range
2 fm ≤L ≤6 fm. The details of the parameters of our
ensembles are summarized in Table II.
Since low Dirac modes can potentially be slow modes
of the system we also checked for autocorrelations. In a
long run performed on the ﬁnest lattice we found that
the autocorrelation time for the smallest Dirac modes is
deﬁnitely smaller than ten trajectories. To be on the safe
side on the ﬁnest lattice the conﬁgurations that we used
for spectrum calculations were always separated by thirty
trajectories. Even on the coarsest lattice conﬁgurations
were separated by ten trajectories.
III.
ANDERSON TRANSITION IN THE DIRAC
SPECTRUM
Previously it was seen that in the high temperature
deconﬁning phase of SU(2) Yang-Mills theory there is a
transition in the staggered Dirac spectrum from localized
low modes to delocalized modes higher up in the spec-
trum [17]. The question we ask here is whether such a
transition also occurs in real QCD with light dynamical
quarks. This is a non-trivial question since light quarks
3
T (MeV)
a(fm)
Ns
Nt
Nconf
Nevs
A1
263
0.125
24
6
430
512
A2
36
420
256
B
300
0.082
32
8
434
256
C1
394
0.125
16
4
1622
512
C2
24
1600
512
C3
32
900
512
C4
48
604
128
D1
401
0.082
24
6
440
512
D2
36
440
256
E
397
0.062
32
8
593
256
F
530
6
420
512
G
601
0.082
24
4
396
512
H
794
0.062
32
4
417
512
TABLE II. The parameters of the simulations; the tempera-
ture, the lattice spacing, the spatial and temporal box size,
the inverse gauge coupling, the number of conﬁgurations and
the number of Dirac eigenvalues computed on each conﬁgu-
ration.
suppress low Dirac modes through the fermion determi-
nant in the functional integral and in the quenched case
it is exactly the lowest Dirac modes that are localized.
The hallmark of a transition from localized to delo-
calized modes in terms of spectral statistics is a change
from Poisson statistics to random matrix statistics in the
spectrum. Intuitively speaking, localized modes are such
because they cannot mix with other modes; typical gauge
ﬁeld ﬂuctuations do not mix them. Localized modes close
in the spectrum are peaked at spatially distant locations
and they are sensitive only to gauge ﬁeld ﬂuctuations
there. As a result the corresponding eigenvalues are sta-
tistically independent and the level spacings obey Pois-
son statistics. Delocalized modes, in contrast, are mixed
by typical gauge ﬁeld ﬂuctuations. Gauge ﬁeld ﬂuctu-
ations change several delocalized modes together which
introduces delicate correlations in the spectrum and as
a result the eigenvalue statistics is described by Random
Matrix Theory (RMT).
The simplest way to detect a transition in the spec-
trum from Poisson to RMT statistics is to consider the
so called unfolded level spacing distribution. Unfolding
is essentially a local rescaling of the eigenvalues to have
unit spectral density throughout the spectrum. We did
the unfolding by ordering all eigenvalues in the given en-
semble and replacing them with their rank order nor-
malized by the total number of conﬁgurations. On a few
ensembles we also checked unfolding by using local spline
approximations to the spectral density but there was no
discrepancy between the two methods of unfolding.
Since the unfolded level spacing distribution (ULSD)
is known analytically for both the Poisson and the RMT
statistics it can be easily used to distinguish between the
0
1
2
3
4
s
0
0.2
0.4
0.6
0.8
1
P(s)
Random Matrix
Poisson
C3 data
(a)
0
1
2
3
4
s
0
0.2
0.4
0.6
0.8
1
P(s)
Random Matrix
Poisson
C3 data
(b)
0
1
2
3
4
s
0
0.2
0.4
0.6
0.8
1
P(s)
Random Matrix
Poisson
C3 data
(c)
0
1
2
3
4
s
0
0.2
0.4
0.6
0.8
1
P(s)
Random Matrix
Poisson
C3 data
(d)
FIG. 1. The unfolded level spacing distribution in diﬀerent re-
gions of the spectrum of ensemble C3. The ﬁgures correspond
to the spectral regions 0.15 ≤λa ≤0.19 (a), 0.29 ≤λa ≤0.32
(b), 0.34 ≤λa ≤0.35 (c) and 0.375 ≤λa ≤0.385 (d).
The dashed line indicates the exponential distribution cor-
responding to the localized (Poisson) case and the dotted line
indicates the chiral unitary Wigner surmise expected in the
delocalized (RMT) case.
two cases. For Poisson statistics the ULSD is a simple
exponential,
PPoisson(s) = exp(−s).
In the RMT case the unfolded level spacing distribution
depends on the universality class which in the case of
staggered fermions in the fundamental representation of
the SU(3) gauge group is the Chiral Unitary Ensemble
(ChUE) [2]. The corresponding ULSD is very precisely
approximated by the chiral unitary Wigner surmise,
PChUE(s) = 32
π2 s2 · exp

−4
π s2

.
(2)
To demonstrate the transition in the spectrum in Fig. 1
we plot the ULSD in diﬀerent regions of the spectrum of
ensemble C3; 0.15 ≤λa ≤0.19 (a), 0.29 ≤λa ≤0.32
(b), 0.34 ≤λa ≤0.35 (c) and 0.375 ≤λa ≤0.385 (d).
We also indicate in the same Figure the distributions
corresponding to the Poisson (localized) and the RMT
(delocalized) case. The transition from localized modes
at the edge of the spectrum to delocalized modes in the
bulk can be clearly seen. This shows that light dynam-
ical fermions do not change the picture observed in the
quenched case earlier and the transition also occurs in
QCD with quarks of physical masses.
4
A.
Analogy with the Anderson transition
The transition in the spectrum from localized to de-
localized modes is reminiscent of the Anderson metal-
insulator transition occurring in conducting crystalline
solids when impurities are introduced [10]. In that case
in the presence of impurities single electron Bloch states
along the band edge turn into localized states. In three
dimensions if the impurity concentration is not too high
states at the band center can still remain delocalized.
The boundary between localized and delocalized states
is known as the mobility edge.
Increasing the density
of impurities pushes the mobility edge further towards
the center of the band until all the states in the band
become localized.
When the mobility edge passes the
Fermi energy and the Fermi energy gets into the delo-
calized part of the spectrum the system has a vanishing
zero-temperature conductivity. The states that can be
excited are all non-conducting localized states.
It has been conjectured that the ﬁnite temperature
QCD transition might be similar to the Anderson transi-
tion [13]. Further indications to support this picture were
obtained from instanton liquid [14] and lattice QCD sim-
ulations [15].
We now sketch the analogy between the spectrum of
the one electron Hamiltonian in disordered media and
that of the QCD Dirac operator.
Due to the symme-
tries of the QCD Dirac operator its spectrum is symmet-
ric with respect to the real axis. In the continuum and
also in the case of the staggered lattice Dirac operator,
the one we use here, the spectrum is purely imaginary.
That is if the quark mass is zero, otherwise the quark
mass provides a trivial real part to all the eigenvalues.
In the chiral limit (zero quark mass) the spectral density
at zero is proportional to the chiral condensate, the order
parameter of spontaneous chiral symmetry breaking [1].
At high enough temperature chiral symmetry is restored
and the spectral density at zero vanishes. In that case
the spectrum has a so called “soft edge” and there might
even be a gap around zero in the spectrum [7, 8]. This
“edge” of the spectrum at the low end is analogous to
the band edge in condensed matter systems.
In the condensed matter literature numerical studies of
the Anderson transition usually concentrate on the band
center and locate the critical disorder when states at the
center become localized. As we will see, in the case of
QCD the location of the mobility edge is controlled by
the temperature and there is no analog of the band cen-
ter since the spectral density continues to be non-zero
all the way up to the cut-oﬀscale. Therefore, unlike in
most of the condensed matter literature, here we do not
attempt to determine the critical disorder where all delo-
calized states disappear but rather study how the mobil-
ity edge changes with the temperature. This approach is
not completely unknown in the condensed matter litera-
ture either [22].
0.15
0.2
0.25
0.3
0.35
0.4
λa
0.2
0.4
0.6
0.8
1
1.2
σ
2
Ns=16
Ns=24
Ns=32
FIG. 2. Variance of the unfolded level spacing distribution
across the transition in the spectrum for ensembles C1, C2
and C3 that diﬀer only in their spatial volume. The dashed
horizontal lines at 1 and 0.178 indicate the expected limits in
the localized (Poisson) and delocalized (RMT) regime.
B.
Second moment of the unfolded level spacing
distribution
As can be seen in Fig. 1 the unfolded level spacing dis-
tribution changes in the spectrum from the exponential
to the Wigner surmise in a continuous fashion. There
does not appear to be a sharp mobility edge, λc, separat-
ing localized and delocalized states. Even in the case of
Anderson transitions, however, a sharp transition is ex-
pected only in the thermodynamic limit when the spatial
size of the system, Ns, goes to inﬁnity. This is completely
analogous to second order phase transitions where a truly
divergent correlation length and a sharp phase transition
can only be observed in inﬁnite systems. In principle any
physical quantity that changes in a well deﬁned way from
the localized to the delocalized regime can be used to de-
ﬁne a transition point in the spectrum. If there is a sharp
transition in the thermodynamic limit then non-analytic
behavior should appear in all these quantities at a given
point, λc, in the spectrum. In what follows we will look
for a quantity that can be used to deﬁne the transition
point.
Since the ﬁrst moment of the unfolded level spacing
distribution is unity by construction, the simplest quan-
tity to consider is its second moment or variance. In the
localized case the level spacings are exponentially dis-
tributed and the variance is
σ2
s = ⟨s2⟩−⟨s⟩2 = 1,
(3)
while in the delocalized regime the second moment of the
distribution of Eq. (2) can be analytically determined to
be σ2
s = 3π
8 −1. In Fig. 2 we plot how the variance changes
in the spectrum throughout the transition region. The
three data sets correspond to ensembles C1-C3 with three
5
0.3
0.35
0.4
0.45
λa
0.2
0.3
0.4
0.5
0.6
0.7
0.8
σ
2
Ns=16
Ns=24
Ns=32
FIG. 3. The same as Fig. 1 but zooming in on the transitions
region. The dotted, dashed and the continuous curve indicate
the ﬁts of the form Eq. (4) to the Ns = 16, 24 and 32 data
respectively.
diﬀerent spatial volumes but otherwise identical param-
eters.
It is apparent that with increasing volume the
transition becomes sharper.
To deﬁne a ﬁnite volume
pseudocritical point in the spectrum we locate the inﬂec-
tion point of the curve σ2(λ). To this end we use the
three-parameter ﬁtting Ansatz
σ2(λ) = A {1 −tanh(B(λ −C))} + 3π
8 −1.
(4)
This form ensures the correct limit for large λ and yields
good ﬁts starting already from λa = 0.2, 0.25 i.e. already
from below the transition point. Using this Ansatz the in-
ﬂection point can be easily seen to be at λca = C and the
slope of the curve there is AB. These two parameters are
largely independent of the starting point of the ﬁt as long
as it starts at smaller values of λ than where the inﬂection
point occurs. The location of the inﬂection point turns
out to be also independent of the volume yielding pseudo-
critical points C = λca = 0.321(4), 0.322(1), 0.324(2) for
the spatial sizes Ns = 16, 24, 32. The slope at the inﬂec-
tion point is AB = 7.6(5), 10.96(36), 13.8(5) for the three
diﬀerent spatial sizes and it scales roughly proportionally
to the linear spatial size of the box. This indicates that
there might be a genuine sharp transition in the ther-
modynamic limit. The sharpening of the transition with
the volume can be better seen in Fig. 3 where we plot
again the variance of the unfolded level spacing distribu-
tion but zoom in on the transition region and also show
the ﬁtted curves with the above described parameters.
C.
Eigenvector statistics
Besides the spectrum the spatial proﬁle of the corre-
sponding eigenvectors also contains important informa-
tion concerning their localization properties. A quantity
that is widely used in this context is the inverse partici-
pation ratio (IPR) deﬁned as [23]
Pψ =
X
x
|ψ(x)|4,
(5)
where ψ is an eigenvector normalized as
X
x
|ψ(x)|2 = 1.
(6)
The qualitative physical meaning of the IPR can be eas-
ily seen by noting that an eigenmode that spreads uni-
formly in a four-volume v and is zero everywhere else
has IPR = 1/v. The IPR−1 thus measures the volume
occupied by an eigenmode. Alternatively one can use the
participation ratio, PR = IPR−1 ·V , where V is the total
volume of the system. This measures the fraction of the
total volume occupied by the eigenmode.
The behavior of the IPR and the PR in the thermo-
dynamic limit can be used to distinguish between local-
ized and delocalized modes. By deﬁnition a part of the
spectrum consists of localized modes if their average IPR
remains ﬁnite as the volume goes to inﬁnity. This also
implies that their average PR vanishes in the thermody-
namic limit. In contrast delocalized modes have vanish-
ing IPR which usually implies non-vanishing PR.
In Fig. 4 we plot how the average participation ra-
tio of eigenmodes changes throughout the spectrum on
ensembles C1-C4. The four data sets correspond to dif-
ferent spatial sizes but otherwise identical parameters.
It is clearly seen that the average PR for the low eigen-
modes decreases as the volume is increased; the aver-
age PR here tends to zero in the thermodynamic limit.
This suggests that these eigenmodes are localized. They
ﬁll a vanishing fraction of the total box volume in the
thermodynamic limit.
Higher up in the spectrum the
average PR becomes a volume independent constant of
order unity, which means that these eigenmodes are de-
localized. They ﬁll a non-zero fraction of the total box
volume in the thermodynamic limit.
IV.
CONTINUUM LIMIT AND
RENORMALIZATION
We saw that on all the ensembles that we considered
there is a critical point (“mobility edge”), λc, in the Dirac
spectrum that separates localized and delocalized eigen-
modes. If the lowest part of the spectrum becomes lo-
calized that can have a dramatic eﬀect on long distance
correlators of quark operators and the masses associated
with them.
This happens because in the spectral de-
composition of the quark propagator, (D + m)−1, each
eigenmode is weighted by the inverse of the correspond-
ing eigenvalue. Therefore the lowest eigenmodes receive
the largest weight. On the other hand, eigenmodes local-
ized to a distance scale l have negligible contribution to
correlators at distance scales much larger than l.
6
0
0.1
0.2
0.3
0.4
0.5
λa
0.0001
0.001
0.01
0.1
1
PR
Ns=16
Ns=24
Ns=32
Ns=48
FIG. 4. Average PR of the eigenvectors for lattices with the
same temperature and lattice spacing but with four diﬀerent
aspect ratios.Nt = 4
To assess the physical implications of localization in
QCD we are thus lead to study two questions;
