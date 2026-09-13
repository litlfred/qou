---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland"
section_id: sec-003-differentiability-by-reweighting
section_title: "Differentiability by reweighting"
section_number: null
pages: 3-4
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland — 17 sections: ADoNIS: A Differe"
---
A neutrino event generator is an intrinsically stochas-
tic program: it samples a neutrino energy from a flux, an
interaction channel, a struck nucleon from the nuclear
ground state, a hard-scattering kinematic configuration
from a squared amplitude, where applicable the hadro-
nisation of the produced partonic state, and final-state
interactions as the outgoing particles propagate through
the nuclear medium. Differentiating such a program di-
rectly is obstructed at every one of these steps, both by
the discrete choices and by the expensive, tabulated am-
plitude evaluations that are not themselves written to be
differentiated.
ADoNIScircumvents this by separating the physics
that has to be differentiated from the physics that does
not: the expensive, well-understood calculation is evalu-
atedonce, when the events are generated, and captured
in a compact per-event record; differentiability is then
arranged only over the physics parameters of interest,
through a closed-formreweightingof that record. Con-
cretely,ADoNISgenerates a fixed sample of events, a
bank, and stores with each event the auxiliary quantities
from which its weight can be recomputed as a function
ofθ. The generation is a conventional, stochastic for-
ward pass; the object that is made differentiable is the
per-event weight
wi(θ) =w 0
i rvertex
i (θ)| {z }
amplitude
rFSI
i (θ)| {z }
cascade
rSF
i (θ)| {z }
nucleus
,(1)
wherew 0
i is the fixed proposal weight assigned at gen-
eration and each factorr i is a differentiable ratio, equal
to one at the nominal tune, that transports the event
from the parameters it was generated with to the pa-
rametersθ. The three factors correspond to the three
physics blocks above and are described in the subsections
that follow. Because everyr i is a pure JAX function of
θ, so is the product, and the entire mapθ7→w i(θ) is
available to automatic differentiation. Generation and
reweighting are performed in double precision (64-bit),
since small variations of the reweighting factors around
unity can fall below single-precision resolution.
Each of the three factors is controlled by its own group
of parameters, and each reweight below is constructed to
be identically unity when its parameters sit at nominal,
so that the nominal prediction is untouched. The 28
parameters divide into eleven acting at the electroweak
vertex, eleven in the cascade, four on the spectral func-
tion, and two overall channel normalisations; each is in-
troduced below in the subsection where it acts.
Each parameter also carries a physically allowed range,
which is enforced wherever it is varied. Most multi-
plicative rate and normalisation parameters have nom-
inal value unity and are restricted to positive values;
4
for the cascade rates of Sec. II D, positivity is addition-
ally required because the total-rate scalegappears in
the denominator of exp(−a/g).f cex
NN is a probability
and is restricted to [0,1]. The axial masses enter only
throughM 2
A, so the prediction is exactly invariant under
MA→−M A and the two signs describe the same phys-
ical model. The one boundary that directly affects the
gradient, the wall in ∆Eb, is discussed in Sec. II B.
