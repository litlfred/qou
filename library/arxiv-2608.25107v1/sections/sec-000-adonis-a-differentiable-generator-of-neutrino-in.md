---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples"
section_id: sec-000-adonis-a-differentiable-generator-of-neutrino-in
section_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples"
section_number: null
pages: 1-1
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
toc_source: outline
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples — 19 sections: ADoNIS: A Differentiable generatOr; Introduction; Differentiable programming in part"
---
C´esar Jes´us-Valls1, ∗
1European Organization for Nuclear Research (CERN), 1211 Geneva 23, Switzerland
Neutrino interaction generators are central to precision oscillation analyses, but conventional imple-
mentations do not directly provide derivatives of their predictions with respect to physics parame-
ters, leaving analyses to obtain this dependence through reweighting, finite differences or external
response models. We present ADoNIS, a fully differentiable neutrino interaction event generator
that makes event reweighting and its gradients directly available, propagating exact derivatives
through the nuclear ground state, hard-scattering amplitudes and stochastic intranuclear cascade.
Following the physics choices of ACHILLES, we demonstrate agreement with its predictions across
neutrino, electron and hadron probes, showing that differentiability is achieved without loss of phys-
ical fidelity. We then show how the resulting Jacobian exposes which measurements and regions
of phase space constrain each parameter and how different probes break degeneracies, providing
a quantitative tool for fit design, model tuning, measurement design and experiment design. The
same differentiable predictions can be used directly in frequentist and Bayesian inference and carried
through detector response to reconstructed observables for unfolding, while also yielding computa-
tional gains. In sum, ADoNIS provides a practical recipe for constructing differentiable neutrino
event generators, applicable beyond the particular physics models implemented here, and this paper
demonstrates their use across a wide range of tasks relevant to both theory and experiment.
