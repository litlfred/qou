---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland"
section_id: sec-001-introduction
section_title: "Introduction"
section_number: null
pages: 1-2
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland — 17 sections: ADoNIS: A Differe"
---
Neutrino oscillation experiments have entered a preci-
sion era. The determination of the leptonic charge-parity
(CP)-violating phase, the resolution of the neutrino mass
ordering, and the increasingly stringent tests of the three-
flavour paradigm all rest on comparing measured event
rates against predictions at the percent level [1–4]. Be-
cause accelerator neutrino beams are broad-band, the
energy of each interacting neutrino is not known a pri-
ori and must be inferred from the observed final state.
That inference is made through a model of the neutrino–
nucleus interaction, so the accuracy of the model prop-
agates directly into the accuracy of the oscillation mea-
surement. Interaction modelling is consequently among
the leading systematic uncertainties of the field, and one
of the most difficult to control, since its sources lie in de-
tails of nuclear physics that are not directly observable,
and can mimic the very shifts in the oscillation parame-
ters that are being measured [5–7].
The difficulty is that atO(GeV) energies, typical
of accelerator neutrino oscillation experiments, several
neutrino–nucleus interaction channels contribute simul-
taneously and involve a broad range of nuclear and par-
ticle physics. Quasielastic scattering, multinucleon pro-
cesses and resonance production depend on the nuclear
environment and nucleon structure, while at higher en-
ergies interactions increasingly probe the internal struc-
ture of the nucleon. A realistic prediction must there-
fore combine the initial nuclear state, the relevant inter-
action mechanisms, the transport of produced hadrons
through the nucleus, and the de-excitation of the rem-
nant, while providing a consistent description across kine-
matic regimes and target nuclei.
∗ cesar.jesus@cern.ch
Every one of these stages is a research front in its
own right, pursued by different groups with different for-
malisms, approximations, and domains of validity. De-
scriptions of the nuclear ground state continue to be re-
fined [8–18]. At the primary interaction, quasielastic
and resonant descriptions [19–35], two-body currents [36–
48], nucleon form factors [49–59], coherent pion pro-
duction [60–65], and shallow- and deep-inelastic scat-
tering [66–79] are all subjects of active theoretical and
phenomenological development. The subsequent trans-
port of hadrons through the nucleus [80–90] and the de-
excitation of the residual system [91, 92] are likewise ac-
tive areas of development.
Making these ingredients consistent across interaction
channels and target nuclei remains an open and ac-
tively contested problem [7, 93–95]. Event generators
are where these ingredients are assembled into complete
final-state predictions for experimental analyses. The
field therefore uses several generators, including GE-
NIE [96, 97], NEUT [98], NuWro [82], GiBUU [80], and
ACHILLES [86, 99], reflecting different scopes, use cases,
and choices of physics implementation.
Once these ingredients are assembled in an event gen-
erator, a separate challenge remains: using its output to
infer physics from data. An event generator maps a set
of physics parameters to simulated final states, which an
analysis then turns into observable predictions that can
be compared with measurements. At truth level, these
predictions can be compared with cross-section measure-
ments to validate interaction models, tune their parame-
ters and derive constraints. In an experimental analysis,
instead, the simulated events are propagated through the
detector and compared with data in reconstructed kine-
matics to infer the underlying physics. In either case, in-
ference requires knowing how the observable predictions
change when the physics parameters are varied. Conven-
tional generators do not provide this information directly
arXiv:2608.25107v1  [hep-ex]  25 Aug 2026
2
as derivatives, so analyses must obtain it through addi-
tional parameter-response machinery [100–104]. Build-
ing and maintaining this machinery, sometimes tied to
particular analysis choices, slows the adoption of new the-
oretical developments in experiments and, in turn, delays
the experimental feedback that helps theorists steer fur-
ther improvements. That delay matters especially now,
when many parts of neutrino-interaction modelling are
being improved at the same time and experiments in-
creasingly need those developments to keep pace with
their precision.
For parameter inference, one way to work around
this limitation is simulation-based inference, which trains
a machine-learning model on repeated simulations to
learn an inverse mapping from the resulting observ-
ables back to the physics parameters [105, 106], an ap-
proach recently applied to neutrino-interaction model
tuning [107, 108]. The way the predictions change when
the physics parameters are varied is, however, already
encoded in the physics calculation itself. A differentiable
generator exposes this response directly, event by event,
through exact derivatives. Rather than learning an ap-
proximate inverse relation from repeated simulations, it
provides the derivatives of the forward calculation itself.
These derivatives can then be propagated to arbitrary ob-
servables to show which parameters affect them, where
different parameters produce similar effects, and which
datasets add new information, while also supporting pa-
rameter inference, uncertainty estimation and measure-
ment design.
Differentiability concerns how a calculation is imple-
mented rather than which physics model it represents,
and therefore need not favour one model over another or
come at the expense of physical fidelity or interpretabil-
ity. The construction presented here is therefore general:
it provides a recipe for making event generators differen-
tiable that is not tied to the particular interaction models
implemented inADoNIS. This motivates treating differ-
entiability as a general capability of future neutrino inter-
action generators. To demonstrate this in a realistic set-
ting, this paper presentsADoNIS, a fully differentiable
neutrino event generator. We use it to show how differ-
entiability can be maintained throughout the neutrino-
interaction calculation, including through the stochastic
intranuclear cascade, and explore what the resulting gra-
dient information makes possible.
The remainder of this paper is organised as fol-
lows. Section II describes the construction ofADo-
NISand how exact derivatives are propagated from the
interaction-model parameters to individual events and
arbitrary observables. Section III validates the differ-
entiable implementation against ACHILLES across neu-
trino, electron and hadron probes. Section IV uses the
resulting Jacobian to show where model parameters af-
fect measured distributions, which combinations are con-
strained or degenerate, and how different measurements
provide complementary information. Section V demon-
strates how the exact gradient information can be used
directly for parameter inference and uncertainty quan-
tification, including the computational advantages it pro-
vides. Finally, Sec. VI demonstrates unfolding within the
same differentiable framework, carrying the prediction
through detector response and extracting a cross section
from reconstructed data.
