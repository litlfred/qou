---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland"
section_id: sec-011-gradient-information
section_title: "Gradient information"
section_number: null
pages: 8-14
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland — 17 sections: ADoNIS: A Differe"
---
Neutrino–nucleus scattering is being probed by an
increasingly broad set of measurements. The Fermi-
lab short-baseline programme [148] now has all three of
its liquid-argon detectors operating—MicroBooNE [149],
ICARUS [150] and SBND [151]—providing a grow-
ing body of measurements of neutrino–argon scatter-
ing [141, 152–157]. NOvA [158] and T2K [159] con-
tinue to take data and report cross sections on carbon,
and in the case of T2K on oxygen as well [160–165].
MINERvA, although no longer running, has released its
data publicly [166] and continues to produce measure-
ments [167–171]. The upgraded T2K near detector [172]
is complemented on the same beamline by WAGASCI–
BabyMIND [173] and NINJA [174]. Future facilities will
further broaden this programme, including the interme-
diate water Cherenkov detector and further near-detector
upgrades proposed for Hyper-Kamiokande [175, 176], and
the DUNE near-detector complex, including SAND and
the movable PRISM configuration [177, 178]. Com-
plementary measurements constrain the same nuclear
physics with better-controlled probes, including electron
scattering at Jefferson Lab and MAMI [143, 179], the con-
9
CC0π δpT
CC0π δαT
CC0π pμ
CC0π cos θμ
CC1π pN
CC1π δpTT
CC1π δαT
CC0π δαT
CC0π pn
CC0π δpT
incl. pμ
T
incl. pμ
∥
CC1π +  Tπ
CC1π +  Q2
(e, e′) ω
π +  σreac
π +  σabs
p σreac
p σπprod
n σreac
n σπprod
MQE
A
MRES
A
SQE
A
CA
5
SΔ
sπ
abs
sel
πN
sconv
sel
NN, pp
sel
NN, pn
sel
NN, nn
sinel
NN, pp
sinel
NN, nn
fcex
NN
kF
ΔEb
NSRC
T2K MINERvA e beam hadron beam
amplitudepion
FSI
nucleon
FSInuclear
−1
0
1
FIG. 5. Signed per-bin parameter responseδθ kJik/σi, with each row normalised to its own peak, for the 17 parameters retained
for inference and highlighted in Fig. 6, across the samples and fitted bins shown in Fig. 7.
tinuing e4νprogramme [144, 180], and hadron–nucleus
scattering, whose existing data are used in cascade tun-
ing [181] and are being extended by liquid-argon test-
beam programmes [182].
Taken together, these data provide overlapping con-
straints on the same underlying interaction and nuclear-
model parameters, but their complementarity is not
always apparent from the predictions themselves. In
conventional workflows, questions such as which mea-
surement constrains which parameter, where different
datasets provide redundant or complementary informa-
tion, and which parameter combinations remain degener-
ate can only be answered through dedicated fits and sen-
sitivity studies. Differentiability makes this information
directly accessible through the response of the prediction
to its parameters.
To demonstrate this, we assemble the Jacobian of
Sec. II G across every bin of a concrete set of measure-
ments and ask what each one constrains. The samples are
chosen to span the kinds of information available rather
than to be exhaustive. Each mirrors the signal definition
and, where one is published, the binning of a specific mea-
surement. From T2K we take the CC0πdistributions
inδp T ,δα T ,p µ and cosθ µ [139] and the CC1π + dis-
tributions inp N,δp TT andδα T [140]; from MINERvA
the CC0πdistributions inδα T ,p n andδp T [138], the
inclusive muonp T andp ∥ [183], and the CC1π + dis-
tributions inT π andQ 2 [170]. Electron scattering en-
ters as the inclusive (e,e ′) energy-transfer spectrum at
2.222 GeV andθ e′≈15.5◦ [15, 131, 143]. Finally, tagged
π+,pandnbeams contribute their reaction and, re-
spectively, absorption and pion-production cross sections
as functions of beam momentum. Between them these
span three probes, two neutrino-beam energies a factor
of five apart, exclusive and inclusive observables, and a
purely hadronic probe that involves no interaction ver-
tex at all. The targets are carbon, except for the three
CC1π+ samples, which are on hydrocarbon and so carry
a free-hydrogen contribution, in the gradient as well as
in the prediction.
Figure 5 shows where in each observable the 17 param-
eters used in Sec. V have an effect. We take a reference
variationδθk of 20% of the nominal value for each param-
eter, except for ∆Eb, whose nominal value is close to zero
and for which we use 4 MeV. For each biniwe compute
the signed responseδθkJik/σi, whereσi is an assumed 5%
10
uncertainty in bini, and normalise each parameter row to
its largest absolute value. The figure therefore shows the
shape of each parameter’s response across phase space,
rather than its overall strength.
Similar response shapes indicate degeneracies: if two
parameters change the bins in the same way, the data
cannot tell which one caused the change. Bins where
their responses differ are therefore the ones that can sep-
arate them. The figure also shows which parts of a distri-
bution constrain each parameter. Sensitivity across the
bulk of a distribution makes inference more robust, while
constraints driven mainly by bins in the distribution tails
are more prone to bias from small mismodellings.
Figure 6 uses the same Jacobian to construct the Fisher
information of Eq. 17. We assign each parameter a
Gaussian prior with widthδθ k, using the same reference
variations defined above, and compute the marginalised
posterior-to-prior widthσ post/σprior for each probe. A
value of one means that the probe adds essentially no in-
formation beyond the prior, while smaller values indicate
a stronger constraint. For the inference studies of Sec. V,
we retain the 17 parameters for which at least one probe
givesσ post/σprior <0.5. These are highlighted in orange
and are the same parameters shown in Fig. 5.
The pattern has a direct physical interpretation. The
hadron-beam column leaves every vertex and ground-
state parameter exactly at its prior and constrains only
the cascade, as expected since no interaction vertex is
involved. It is nonetheless the most informative probe of
nucleon and pion final-state interactions. The neutrino
and electron samples together constrain the nuclear pa-
rameters, while the neutrino samples alone are the most
informative about the form factors entering the ampli-
tude. Parameter correlations are equally visible.C A
5 ,
for instance, is directly constrained only by the neutrino
samples. Adding the electron and hadron beams, neither
of which is directly sensitive to it, nevertheless tightens
its constraint by constraining the parameters with which
it is correlated.
Three uses follow directly. The first is fit design: the
gradients show which parameters the data can constrain
and which samples add new information beyond those
already included. The second is measurement design.
Multi-dimensional differential cross sections are already
being published [162, 171, 184], and the statistics of the
next generation will support increasingly fine and high-
dimensional measurements. Because observables and
binnings can be defined after the event-level gradients are
available, alternative measurements can be compared di-
rectly by the parameter information they provide, allow-
ing the observables and binnings that best constrain the
parameters of interest to be identified. The third is ex-
periment design, where different beam energies, targets,
probe types and final-state capabilities can be compared
by the additional information they provide.
ν
T2K + MINERvA
e beam
(e, e′)
hadron beam
π + , p, n
ALL
MQE
A
MRES
A
SQE
A
SQE
V
μp
μn
Gp
E
Gn
E
CA
5
Fpp
SΔ
sπ
abs
sel
πN
scex
πN
sconv
sel
NN, pp
sel
NN, pn
sel
NN, nn
sinel
NN, pp
sinel
NN, pn
sinel
NN, nn
fcex
NN
kF
ΔEb
NSF
NSRC
NQE
NRES
amplitudepion
FSI
nucleon
FSInuclear
0.10 1.00 1.00 0.08
0.25 1.00 1.00 0.18
0.52 1.00 1.00 0.48
0.65 0.66 1.00 0.62
0.83 0.96 1.00 0.82
0.89 0.99 1.00 0.84
0.57 0.93 1.00 0.54
0.99 1.00 1.00 0.95
0.60 1.00 1.00 0.44
0.79 1.00 1.00 0.77
0.46 1.00 1.00 0.34
0.32 1.00 0.14 0.11
0.44 0.95 0.19 0.14
0.85 0.96 0.78 0.57
1.00 1.00 0.41 0.39
0.56 0.98 0.53 0.36
0.39 0.63 0.28 0.20
0.92 0.98 0.51 0.48
0.69 1.00 0.44 0.41
0.96 1.00 0.82 0.76
0.99 1.00 0.43 0.40
0.34 0.74 0.28 0.19
0.04 0.08 1.00 0.03
0.22 0.24 1.00 0.12
0.75 0.72 1.00 0.66
0.51 0.95 1.00 0.39
0.87 0.93 1.00 0.86
0.81 0.71 1.00 0.66
0.0 0.5 1.0
posterior / prior width   σpost/σprior
FIG. 6. Marginalised parameter constraintsσ post/σprior for
samples aggregated by probe type and for all samples com-
bined. Cells withσ post/σprior <0.5 are highlighted in orange.
V. PARAMETER INFERENCE AND
UNCERTAINTY QUANTIFICATION
This section illustrates how a differentiable event gen-
erator constructed as described above can be used di-
rectly for parameter inference and uncertainty quan-
tification. InADoNIS, the derivative of any observ-
able built from the events is available by construction
(Sec. II F), so any differentiable loss can be optimised
directly without external response functions or finite-
difference derivatives. We demonstrate this in cross-
section space, where experiments routinely report their
measurements, and show that the same framework sup-
ports the standard inference machinery used in HEP,
from fitting and Gaussian uncertainties to profiling and
marginalisation. Our focus here is on demonstrating this
machinery, thereby enabling applications including tests
11
0 200 400 600 800 1000
δpT [MeV/c]
0
1
T2K CC0π δpT
χ2 947.4 →  2e-12  (8 bins)
0.0 0.5 1.0 1.5 2.0 2.5 3.0
δαT [rad]
0
1
T2K CC0π δαT
χ2 849.2 →  1e-12  (8 bins)
0 500 1000 1500
pμ [MeV/c]
0
1
15/19 bins
T2K CC0π pμ
χ2 1546.4 →  2e-12  (15 bins)
−0.50 −0.25 0.00 0.25 0.50 0.75 1.00
cos θμ
0
1
T2K CC0π cos θμ
χ2 2356.0 →  3e-12  (20 bins)
0 250 500 750 1000 1250 1500
pN [MeV/c]
0
1
T2K CC1π pN
χ2 125.1 →  3e-13  (4 bins)
−600 −400 −200 0 200 400 600
δpTT [MeV/c]
0
1
T2K CC1π δpTT
χ2 104.3 →  3e-13  (5 bins)
0.0 0.5 1.0 1.5 2.0 2.5 3.0
δαT [rad]
0
1
T2K CC1π δαT
χ2 91.0 →  2e-13  (3 bins)
0.0 0.5 1.0 1.5 2.0 2.5 3.0
δαT [rad]
0
1
MINERvA CC0π δαT
χ2 799.7 →  1e-12  (12 bins)
0 500 1000 1500 2000
pN [MeV/c]
0
1
23/24 bins
MINERvA CC0π pN
χ2 1585.3 →  3e-12  (23 bins)
0 500 1000 1500 2000
δpT [MeV/c]
0
1
23/24 bins
MINERvA CC0π δpT
χ2 1457.9 →  4e-12  (23 bins)
0.0 0.5 1.0 1.5 2.0 2.5
pμ
T [GeV/c]
0
1
19/20 bins
MINERvA incl. pμ
Tχ2 4076.5 →  5e-12  (19 bins)
2 4 6 8 10 12 14
pμ
∥  [GeV/c]
0
1
13/20 bins
MINERvA incl. pμ
∥χ2 1459.3 →  2e-12  (13 bins)
200 400 600 800
ω [MeV]
0
1
43/44 bins
(e, e′)C ω
χ2 2374.3 →  4e-12  (43 bins)
0 50 100 150 200 250 300 350
Tπ [MeV]
0
1
MINERvA CC1π +  Tπ
χ2 246.4 →  1e-11  (10 bins)
0.0 0.5 1.0 1.5 2.0 2.5 3.0
Q2 [GeV2]
0
1
MINERvA CC1π +  Q2
χ2 248.8 →  4e-11  (12 bins)
200 400 600 800 1000
pπ +  [MeV/c]
0
1
π + C σreac
χ2 37.3 →  1e-12  (15 bins)
200 400 600 800 1000
pπ +  [MeV/c]
0
1
π + C σabs
χ2 134.5 →  3e-13  (15 bins)
400 600 800 1000 1200 1400
pp [MeV/c]
0
1
pC σreac
χ2 9.1 →  3e-13  (15 bins)
400 600 800 1000 1200 1400
pp [MeV/c]
0
1
7/15 bins
pC σπprod
χ2 1.6 →  2e-13  (7 bins)
400 600 800 1000 1200 1400
pn [MeV/c]
0
1
nC σreac
χ2 9.5 →  9e-14  (15 bins)
400 600 800 1000 1200 1400
pn [MeV/c]
0
1
7/15 bins
nC σπprod
χ2 106.9 →  5e-13  (7 bins)
differential cross-section  (a.u., peak normalised)
Pre-fit (nominal) Post-fit Asimov data
FIG. 7. Every observable entering the fit, before and after it. Points are the Asimov data with the per-bin uncertainty used
in the fit; hollow points are the bins removed by the Monte Carlo error mask. The pre-fit curve is the prediction at nominal
and the post-fit curve the prediction at the recovered parameters. Each panel is normalised to its own peak and quotes itsχ 2
before and after the fit over the retained bins. For the two observables whose upper edge is not a kinematic limit, the overflow
bin is omitted both from the drawing and from theχ 2.
12
of the self-consistency of published measurements, global
model tuning, and the extraction and Gaussianity test-
ing of correlated cross-section model constraints; pursu-
ing these applications is left to dedicated future studies.
We demonstrate these capabilities using the same 21
observables and 17 parameters identified in Sec. IV. For
the closure test, the parameters are randomly displaced
within their physical ranges to define an injected truth,
and the nominal event bank is reweighted to the corre-
sponding prediction. Each bin is assigned the same 5%
uncertainty used in Sec. IV. No informative parameter
priors are imposed, although all parameters remain re-
stricted to their physical ranges. For simplicity, we use a
Gaussianχ 2 throughout; the same differentiable predic-
tion can enter any differentiable likelihood.
Parameter optimisation is performed with a Gauss–
Newton method [185] using the exact Jacobian sup-
plied byADoNIS. Sec. V A describes the method in
more detail and compares its performance with MI-
GRAD [186, 187].
Figure 7 shows the result in observable space. The in-
jected truth is sufficiently displaced from nominal that
the pre-fit prediction visibly differs from the data wher-
ever the shifted parameters have an effect, while the post-
fit prediction recovers it. Because the closure dataset is
generated exactly at the injected truth, the residual at
the minimum vanishes by construction.
The same differentiable prediction can also be used di-
rectly for uncertainty quantification, without restricting
the analysis to the local Gaussian approximation around
the fitted minimum. Panel (a) of Fig. 8 compares four
68% intervals obtained from the same dataset. The Gaus-
sian interval uses the local covariance at the minimum;
the profile evaluates the likelihood away from it along
the parameter of interest; the Laplace marginal also ac-
counts for the volume of the nuisance directions; and
direct sampling explores the full parameter space. These
provide increasingly non-local uses of the same underly-
ing prediction and allow their assumptions to be tested
against one another.
To demonstrate that the differentiable treatment ex-
tends beyond the local curvature, we construct a pro-
file likelihood for each parameter by fixingθ k and re-
minimising over the remaining 16 parameters,
χ2
prof(θk) = min
θnuis
χ2(θk,θ nuis).(18)
Each profile is evaluated at 13 nodes, with its range ex-
tended independently on either side until ∆χ 2
prof >25
or a physical boundary is reached. This adaptive range
matters for shallow directions, where several Gaussian
widths need not exhaust the likelihood. To compare with
the marginal intervals on a common 68% mass basis, we
normalise
Lprof(θk)∝e −∆χ2
prof(θk)/2 (19)
over the scanned range and quote its shortest 68% region.
−1.5 −1.0 −0.5 0.0 0.5 1.0 1.5
(θ − θnom) / σref
MQE
A
MRES
A
SQE
A
CA
5
SΔ
sπ
abs
sel
πN
sconv
sel
NN, pp
sel
NN, pn
sel
NN, nn
sinel
NN, pp
sinel
NN, nn
fcex
NN
kF
ΔEb
NSRC
Injected truth
BFP
Gaussian
Profile
Marginal (Laplace)
Marginal (NUTS)
amplitude
pion FSI
nucleon FSI
nuclear
a)
0 10 20 30 40
Δχ2 = χ2(θtrue) − χ2( ̂θ)
0.00
0.02
0.04
0.06
density
coverage
68.3%: 67.8±1.0%
90.0%: 89.4±0.7%
95.0%: 94.8±0.5%
χ2(17)b)
FIG. 8. (a) Recovery of the 17 fitted parameters, in units of
the reference widthδθ k defined in Sec. IV. Every parameter
returns to its injected truth. The four overlaid bars show
the Gaussian, profile, Laplace-marginal and directly sampled
marginal intervals, all at 68% and all obtained from the same
dataset. The direct marginal is obtained with the No-U-Turn
Sampler (NUTS). (b) Distribution over the toy ensemble of
∆χ2 between the true and fitted parameters, compared with
theχ 2 distribution for 17 degrees of freedom predicted by
Wilks’ theorem. The observed coverage is quoted at three
confidence levels.
The same framework also supports marginalisation,
where nuisance parameters are integrated rather than op-
timised. The marginal likelihood is
Lmarg(θk) =
Z
L(θk,θ nuis)dθ nuis.(20)
A second-order expansion about the conditional best fit
gives the Laplace approximation
Lmarg(θk)∝L prof(θk)
p
detV nuis(θk),(21)
13
MRES
A
0.8 1.2
SΔ
0.6 0.9 1.2
CA
5
0 0.5 1
ΔEb
0.4
0.8
1.2
MRES
A
0.8
1.6
SΔ
SΔ
0.8
1.2
SΔ
0.8
1.6
CA
5
CA
5
0.6
0.9
1.2
CA
5
0.8 1.6
MRES
A
2
4
ΔEb
0.8 1.6
SΔ
0.8 1.6
CA
5
ΔEb
Laplace Profile NUTS Gaussian BFP
FIG. 9. Four parameters of the fit in two dimensions. Below the diagonal, the parameter pairs are shown over a wide range
of physical values, with arrows giving the local Gauss–Newton step direction over log 10 ∆χ2 in greyscale. The rectangles mark
the regions shown above the diagonal, where the 68% and 90% regions of four uncertainty constructions are compared. The
diagonal panels show the corresponding one-dimensional distributions. The green star marks the best-fit point (BFP), and the
grey band in ∆Eb denotes values outside the physical range.
whereV nuis is the local nuisance-parameter covariance.
The profile measures the height of the likelihood ridge,
while the determinant measures its transverse volume;
the two differ whenever that volume changes along the
ridge.
The second derivatives available from the same model
allow this marginalisation to use the exact local curvature
rather than reusing the Gauss–Newton, or Fisher, ap-
proximation of Eq. 17. At each profile point we evaluate
Vnuis from the exact Hessian by nested automatic differ-
entiation. This matters away from the global minimum,
where the residual is generally non-zero and the residual-
dependent contribution to the Hessian need not vanish.
Second-order information can therefore be used where
the statistical construction requires it, without building
a separate numerical response model.
The analysis is not restricted to marginalisation
through a local expansion. We also sample the same 17-
dimensional likelihood directly with the No-U-Turn Sam-
pler (NUTS), an MCMC algorithm based on Hamiltonian
Monte Carlo [188], assuming a uniform density over the
physical parameter ranges of Sec. II A and no additional
prior. The four constructions can then be compared di-
rectly: Gaussian versus profile tests the local quadratic
description along the parameter of interest; profile ver-
sus Laplace tests the importance of nuisance volume; and
Laplace versus NUTS tests the quadratic approximation
used to describe that volume. All four are obtained from
the same differentiable prediction. Gradient information
therefore does not confine the analysis to Gaussian or lo-
cally approximated uncertainties, but remains available
throughout profiling and full marginalisation.
The same fitting machinery remains well behaved when
applied repeatedly to statistically fluctuated datasets.
Panel (b) of Fig. 8 repeats the fit for 2000 toys, obtained
by fluctuating the same injected prediction with the per-
bin uncertainties, and forms
∆χ2 =χ 2(θtrue)−χ 2( ˆθ).(22)
14
The ensemble follows theχ 2 distribution with 17 de-
grees of freedom expected from Wilks’ theorem [189].
The measured coverages are 67.8±1.0%, 89.4±0.7%,
and 94.9±0.5%, compared with nominal 68.3%, 90%,
and 95%, respectively, and the medianχ 2 per degree of
freedom is 0.992. The differentiable treatment therefore
reproduces not only the injected minimum, but the ex-
pected statistical behaviour of an ensemble of fits without
outliers. Carrying exact derivatives through the gener-
ator introduces no observable penalty in fit convergence
or frequentist coverage.
Physical boundaries are common in HEP fits and pro-
vide an important test of the inference machinery. The
injected value of ∆Eb lies close to the physical wall where
the spectral-function reweight becomes flat, producing a
truncated and strongly asymmetric likelihood. Such a
boundary is precisely a regime in which Gaussian approx-
imations cease to apply; when the true value lies on it,
the asymptotic likelihood-ratio distribution is described
by the corresponding Chernoff mixture rather than the
usual Wilks result [190]. No modification of the differ-
entiable model is required: the physical range is part of
the minimisation domain, the profile terminates at the
boundary, and NUTS remains within it. The same gra-
dient information can therefore be used unchanged in fits
involving physical limits and strongly non-Gaussian un-
certainties.
The derivative information is also usable across corre-
lated multi-parameter regions, not only in the immediate
neighbourhood of the best fit. Figure 9 shows this for the
three parameters sharing the resonant axial block and
for ∆Eb with its physical boundary. Above the diagonal,
agreement of the four uncertainty constructions identi-
fies directions where the local Gaussian description is
sufficient; their separation localises the non-Gaussianity
to particular parameter combinations and, through the
comparisons above, identifies its origin.
Below the diagonal, the same derivatives are evaluated
over the full physically allowed parameter space. The ar-
rows show the local Gauss–Newton step from each point:
near the minimum they determine the covariance of the
inferred region, while farther away they determine the di-
rection in which the fit moves. Their smooth behaviour
across the full range shows that the gradient supplied by
ADoNISis available throughout the parameter space,
rather than being a response constructed only around
the nominal point or the best fit. The same differen-
tiated model therefore describes both the optimisation
landscape and the uncertainty around its solution.
Taken together, these tests show that the gradient in-
formation supplied byADoNIScan be carried through
the full inference workflow without narrowing the statis-
tical tools available to the analysis. At the analysis level,
this realises the same advantage that motivates built-in
differentiability throughout the generator: additional in-
formation and computational leverage are gained without
imposing a corresponding restriction on how the physics
inference is performed.
