---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland"
section_id: sec-014-conclusions
section_title: "Conclusions"
section_number: null
pages: 17-17
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples César Jesús-Valls1,∗ 1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland — 17 sections: ADoNIS: A Differe"
---
We have presentedADoNIS, a fully differentiable neu-
trino interaction event generator. By separating stochas-
tic event generation from the differentiable reweighting
of the resulting event bank,ADoNISpropagates ex-
act derivatives through the nuclear ground state, hard-
scattering amplitudes and intranuclear cascade without
modifying the underlying interaction physics. Its agree-
ment with ACHILLES across neutrino, electron and
hadron probes demonstrates that differentiability can be
introduced without loss of physical fidelity.
Event reweighting and its gradients are available di-
rectly from the generator, removing the need for external
response functions to encode the dependence of the pre-
diction on the interaction-model parameters. We showed
how the exact Jacobian exposes which measurements
constrain which parameters, where those constraints
originate in phase space, and how different probes break
degeneracies. The same differentiated prediction sup-
ports standard frequentist and Bayesian parameter in-
ference and uncertainty quantification, while providing
substantial computational gains for optimisation, cur-
vature evaluation and gradient-based MCMC. We fur-
ther carried the same framework through detector re-
sponse in a 196-parameter unfolding example, showing
that the gradient information remains directly usable in
reconstructed-space analyses.
ADoNISis released as an open-source implementation
of this approach 4, intended both as a practical tool and
as a reference for how differentiable neutrino event gener-
ators can be constructed. The differentiable intranuclear
cascade developed here is itself modular and can be ap-
plied directly to the pre-FSI output of other event genera-
tors, independently of the model used for the primary in-
teraction. Natural next steps forADoNISare the inclu-
sion of two-body currents and deep-inelastic scattering,
using approaches analogous to those demonstrated in this
paper. Extending differentiability to hadronisation mod-
els such as PYTHIA [201, 202] is also a valuable under-
taking in its own right, given their central role not only
in DIS modelling for neutrino generators but through-
out high-energy physics. Importantly, these extensions
are not prerequisites for using the framework: until na-
tive differentiable implementations of two-body currents
and DIS are available, events from these channels can be
taken from existing generators, combined with theADo-
NISQE and RES samples, and propagated through the
ADoNIScascade. The resulting prediction therefore re-
tains the full differentiable dependence of theADoNIS
QE and RES channels on their model parameters, while
preserving differentiability with respect to the FSI pa-
rameters across all channels. Imported channels can ad-
ditionally be given differentiable parameter dependence
through multiplicative event weights, mirroring the flux
and template parameters of Sec. VI.
