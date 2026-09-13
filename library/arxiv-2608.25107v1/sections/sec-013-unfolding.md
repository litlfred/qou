---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland"
section_id: sec-013-unfolding
section_title: "Unfolding"
section_number: null
pages: 15-17
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland — 17 sections: ADoNIS: A Differe"
---
The previous section used the differentiable prediction
directly in truth space to constrain interaction-model
parameters. The same machinery can also be carried
through the detector response, allowing the signal in
true kinematics to be extracted from reconstructed data
while fitting flux, detector and interaction-model nui-
sance parameters simultaneously. This is the setting of
a cross-section measurement: experiments observe event
distributions in reconstructed kinematics, from which the
corresponding signal rates in true kinematics must be
inferred after accounting for detector effects and back-
grounds, before normalisation by the integrated flux and
number of targets. Exploiting the differentiability of
ADoNIS, we illustrate this extraction with a template-
fit unfolding, the standard approach used in T2K cross-
section measurements3.
We demonstrate this by mirroring the T2Kν µ CC0π
double-differential measurement of Ref. [200], in muon
momentum and angle,d 2σ/dpµdcosθ µ. We adopt the
same signal definition: aν µ charged-current interaction
with exactly oneµ −, no pions or other mesons after
FSI, any number of nucleons, and no restriction on the
muon kinematics. We also retain the same 58 truth bins,
while splitting each momentum interval in two at recon-
struction level to obtain 116 reconstructed bins. A sim-
ple stochastic detector model applies a 10% momentum
smearing and a 5◦ angular smearing event by event. To
introduce a background component, charged pions below
400 MeV/care reconstructed with 50% efficiency, imple-
mented as an event-by-event random selection, so missed
pions allow CC1πevents to enter the CC0πselection,
giving a signal purity of 0.915. The prediction is nor-
malised to an exposure corresponding to approximately
170 000 selected events, while the underlying event bank
provides about 24 times larger Monte Carlo statistics.
The prediction in reconstructed biniis
µi(c,f,θ,d) =d i

X
j,b
Aijbcjfb +
X
b
Bib(θ)fb

,(23)
whereAijb is the nominal signal template contributing to
reconstructed binifrom truth binjand neutrino-energy
3 A direct comparison with iterative Bayesian unfolding [198], the
other widely used approach in the field, is given in Ref. [199].
16
0.0 0.2 0.4 0.6
pμ [GeV/c]
0
1
2
3
4
5
6
7
d2σ/dpμ dcos θμ
[10−39cm2/nucleon/(GeV/c)]
0.20 < cos θμ < 0.60
0 1 2 3
pμ [GeV/c]
0
2
4
6
8
10
12
0.94 < cos θμ < 0.98
closure signal ×1.20 truth (input) unfolded (result)
FIG. 10. Unfolded T2K CC0πdouble-differential cross sec-
tion in two of the nine cosθ µ slices, for a closure test and for
a dataset in which the true signal is increased by 20%.
0.00 0.05 0.10 0.15 0.20 0.25 0.30
σ(cj) with block enabled
0
57 linearised truth bin index
statistical
cross section
flux
detector
FIG. 11. Uncertainty on the 58 unfolded templates as statis-
tical and systematic contributions are successively included.
binb, whileB ib(θ) is the corresponding background pre-
diction. The 58 template parameterscindependently
scale the signal truth bins and are left unconstrained, so
that the signal cross section is determined directly by the
fit rather than by the interaction model. The unfolded
cross section in each truth bin is therefore obtained by
applying the fittedc j to the corresponding nominal cross
section.
The flux is described by 10 parametersf, each scal-
ing all signal and background events within an interval of
true neutrino energy. The intervals are 0–600 MeV, four
100 MeV bins between 600 and 1000 MeV, two 200 MeV
bins between 1000 and 1400 MeV, two 300 MeV bins
between 1400 and 2000 MeV, and an open bin above
2000 MeV. For illustration, they are assigned a correlated
Gaussian prior with 10% marginal uncertainties and co-
⃗c ⃗f ⃗x ⃗d
⃗c  templates
⃗f  flux
⃗x  cross section
⃗d  detector
−1
−0.1
−0.01
0
0.01
0.1
1
correlation (symlog)
FIG. 12. Post-fit correlation matrix of the 196 fitted param-
eters: 58 signal templatesc, 10 flux parametersf, 12 cross-
section parametersθand 116 detector parametersd. The
scale is symmetric-logarithmic, becoming linear for correla-
tions below 0.01 in magnitude.
variance
Σbb′ =σ bσb′ exp

−| ¯Eν,b− ¯Eν,b′|
400 MeV

,(24)
whereσ b = 0.10 and ¯Eν,b is the centre of flux binb. For
the open final bin, we set ¯Eν,b = 2150 MeV by extrapo-
lating the width of the preceding finite bin, providing a
finite representative energy for the correlation kernel.
Of the 28 cross-section parameters introduced in
Sec. II A, we retain the 12 whose variation on the refer-
ence scales defined in Sec. IV produces a non-negligible
change in the predicted background:k F ,S ∆,C A
5 ,N SF,
NRES,M RES
A ,f cex
NN ,s el
NN,pn , ∆Eb,s π
abs,N SRC ands el
πN .
Concretely, we require∥(∂B/∂θ k)σ ref
k /√µ∥2 ≥1 over
the reconstructed bins, whereµis the nominal signal-
plus-background prediction andσ ref
k the corresponding
reference variation. These parameters are also left un-
constrained.
Finally, the 116 detector parametersd, one per recon-
structed bin, carry independent Gaussian 5% normalisa-
tion uncertainties. The fit therefore contains 196 param-
eters in total and deliberately spans three different nui-
sance treatments: unconstrained cross-section parame-
ters, independently constrained detector parameters, and
correlated flux parameters.
An important feature of Eq. 23 is that mapping the
prediction from true to reconstructed kinematics intro-
duces no additional obstacle to differentiability. For a
given analysis definition, the outcomes of detector smear-
ing, event selection, and assignment to true and recon-
structed bins are fixed; they determine which events con-
tribute to each bin, but not how their weights respond to
the fitted parameters. Importantly, these analysis choices
are themselves downstream of event generation. Different
signal definitions, selections and binnings can therefore
17
be explored efficiently by reapplying these downstream
operations to the same event-level predictions and deriva-
tives.
Once this mapping is defined, the parameterisation
used here is multilinear in the template, flux, and detec-
tor parameters,c,fandd, so their derivatives follow
directly from the precomputed signal and background
tensors.
Figure 10 shows the unfolded result for a closure
dataset and for a second dataset in which the true sig-
nal is increased uniformly by 20%. In both cases the fit
recovers the injected spectrum, demonstrating that the
unfolding pipeline behaves as expected.
The relative contributions to the uncertainty across
the 58 truth bins are shown in Fig. 11. Statistical,
flux and detector uncertainties all contribute appreciably,
while the cross-section component remains small because
the high-purity sample limits the role of the interaction
model to the background prediction.
The corresponding post-fit correlations are shown in
Fig. 12. The signal templates are anticorrelated with the
flux because both control the overall signal rate, while
neighbouring templates can be anticorrelated through de-
tector migration between adjacent truth bins. The detec-
tor block remains approximately diagonal, reflecting the
independent reconstructed-bin normalisations. Correla-
tions involving the cross-section parameters are more het-
erogeneous: different interaction parameters induce dis-
tinct, generally non-linear distortions of the background
and can therefore correlate positively or negatively with
different signal templates.
Taken together, these results show that the same dif-
ferentiable framework can be used directly for unfolding.
