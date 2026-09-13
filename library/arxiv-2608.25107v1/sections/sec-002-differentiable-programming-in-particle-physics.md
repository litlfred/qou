---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland"
section_id: sec-002-differentiable-programming-in-particle-physics
section_title: "Differentiable programming in particle physics"
section_number: null
pages: 2-3
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland — 17 sections: ADoNIS: A Differe"
---
Differentiable programming makes a simulation differ-
entiable in its own inputs, so that derivatives of the pre-
diction are produced by the program rather than recon-
structed outside it. Automatic differentiation [109] de-
composes a program into elementary operations and ap-
plies the chain rule through each of them, giving the exact
derivative of the output with respect to any input; in re-
verse mode a full gradient costs a small constant multiple
of one forward evaluation, independent of the number of
inputs, and higher derivatives follow by nesting the same
construction.
Physics is adopting this formalism broadly [110–117].
Within high-energy physics, applications are emerging
rapidly. The stochastic sampling long presumed to ob-
struct them has proved tractable [118], and gradient
information has been put to use across the full range
of common experimental tasks: detector design [119],
physics modelling [120–123], and data analysis [124].
In neutrino physics, differentiable frameworks now ex-
ist for the two most widely used detector technologies,
liquid argon time projection chambers [125] and opti-
cal Cherenkov and scintillation detectors [126, 127], with
demonstrated applications to detector calibration and
event reconstruction.ADoNISextends this emerging
paradigm to the modelling of neutrino interactions.
II. A DIFFERENTIABLE NEUTRINO EVENT
GENERATOR
We developedADoNIS,A Differentiable generatOr
ofNeutrinoInteractionSamples, a JAX-based open-
source neutrino event generator 1.ADoNISfollows the
interaction physics choices of the ACHILLES genera-
tor [86, 90, 99], implemented in a fully differentiable man-
ner, and so provides differentiable event weights for fully
exclusive neutrino–nucleus final states.
ACHILLES is a modern, open-source 2, self-consistent
generator built around fully exclusive final states. Its
vertex implements two channels. Quasi-elastic scattering
is computed from the one-body electroweak current in
the extended factorisation scheme [86], with Kelly vec-
tor andz-expansion axial nucleon form factors [50, 128].
1 https://github.com/cesarjesusvalls/ADoNIS/
2 https://github.com/AchillesGen/Achilles
3
Resonant single-pion production is taken from the ANL–
Osaka dynamical coupled-channels model [28], whose
meson–baryon amplitudes also enter the corresponding
scattering cross sections used in the intranuclear cascade.
The nuclear ground state is carried by hole spectral func-
tionsS(p,E)—the probability of removing a nucleon of
momentumpand leaving the residual system with exci-
tation energyE, normalised separately for protons and
neutrons—obtained for 12C from correlated-basis func-
tion theory [129, 130] and for 40Ar from (e,e ′p) mea-
surements [15, 87, 131]. Hadrons produced at the vertex
are transported through a sampled nucleon configuration,
taken from Green’s function Monte Carlo for carbon [132]
and, since argon is not amenable to continuum quantum
Monte Carlo, from single-nucleon densities there [99];
pion absorption follows the Oset model [133]. Charged-
current, neutral-current and electromagnetic probes are
all supported, so the same code is confronted with (e,e ′)
data as well as with neutrino measurements, and a tagged
hadron beam allows the cascade to be exercised on its
own.ADoNISmirrors these choices. The full deriva-
tions are given in the ACHILLES papers [86, 90, 99];
what follows recalls each ingredient only as far as is
needed to show how it is made differentiable, and then
describes how gradient information is carried from the
physics parameters through to the final observables.
Meson-exchange currents and deep-inelastic scattering
are absent from ACHILLES and are planned additions
to it [90]; the same is true ofADoNIS, and both lie out-
side the scope of this paper. More generally, the physics
choices described above are inherited from ACHILLES
rather than selected as preferred models: their purpose
here is to provide a realistic generator chain on which to
demonstrate differentiability. In particular, reproducing
the fully stochastic ACHILLES intranuclear cascade in
ADoNISdemonstrates that differentiability can be re-
tained even through discrete transport histories.
JAX [134] supplies the automatic differentiation, just-
in-time compilation and vectorisation, and allows the
same implementation to run on CPU or GPU. Their
relative performance depends strongly on the stage of
event generation. For neutrino interactions on carbon
with energies sampled from the T2K flux, pre-FSI gen-
eration showed no GPU acceleration, running at about
1.8×103 events/s on both a single AMD EPYC CPU core
and an NVIDIA A100 GPU. The computational bottle-
neck is instead the intranuclear cascade, whose through-
put increases from about 55 events/s on a single CPU
core to 560 events/s on an RTX 2080 Ti GPU and 720
events/s on an A100 GPU. A GPU is therefore not re-
quired for event generation, but can substantially accel-
erate the cascade calculation. The computational per-
formance of the differentiable inference is discussed sep-
arately in Sec. V A.
We denote byθthe vector of differentiable physics pa-
rameters. For illustration, in this paper we consider 28
parameters, chosen to exercise every part of the gener-
ator and to demonstrate operation in high-dimensional
spaces.
