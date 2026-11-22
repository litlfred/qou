---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples"
section_id: sec-016-conclusions
section_title: "Conclusions"
section_number: null
pages: 17-17
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.995
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples — 19 sections: ADoNIS: A Differentiable generatOr; Introduction; Differentiable programming in part"
---
We have presented [ADoNIS]{.smallcaps}, a fully differentiable neutrino interaction event generator. By separating stochastic event generation from the differentiable reweighting of the resulting event bank, [ADoNIS]{.smallcaps} propagates exact derivatives through the nuclear ground state, hard-scattering amplitudes and intranuclear cascade without modifying the underlying interaction physics. Its agreement with ACHILLES across neutrino, electron and hadron probes demonstrates that differentiability can be introduced without loss of physical fidelity.

Event reweighting and its gradients are available directly from the generator, removing the need for external response functions to encode the dependence of the prediction on the interaction-model parameters. We showed how the exact Jacobian exposes which measurements constrain which parameters, where those constraints originate in phase space, and how different probes break degeneracies. The same differentiated prediction supports standard frequentist and Bayesian parameter inference and uncertainty quantification, while providing substantial computational gains for optimisation, curvature evaluation and gradient-based MCMC. We further carried the same framework through detector response in a $196$-parameter unfolding example, showing that the gradient information remains directly usable in reconstructed-space analyses.

[ADoNIS]{.smallcaps} is released as an open-source implementation of this approach[^1], intended both as a practical tool and as a reference for how differentiable neutrino event generators can be constructed. The differentiable intranuclear cascade developed here is itself modular and can be applied directly to the pre-FSI output of other event generators, independently of the model used for the primary interaction. Natural next steps for [ADoNIS]{.smallcaps} are the inclusion of two-body currents and deep-inelastic scattering, using approaches analogous to those demonstrated in this paper. Extending differentiability to hadronisation models such as PYTHIA [@Sjostrand:2006za; @Sjostrand:2014zea] is also a valuable undertaking in its own right, given their central role not only in DIS modelling for neutrino generators but throughout high-energy physics. Importantly, these extensions are not prerequisites for using the framework: until native differentiable implementations of two-body currents and DIS are available, events from these channels can be taken from existing generators, combined with the [ADoNIS]{.smallcaps} QE and RES samples, and propagated through the [ADoNIS]{.smallcaps} cascade. The resulting prediction therefore retains the full differentiable dependence of the [ADoNIS]{.smallcaps} QE and RES channels on their model parameters, while preserving differentiability with respect to the FSI parameters across all channels. Imported channels can additionally be given differentiable parameter dependence through multiplicative event weights, mirroring the flux and template parameters of Sec. [\[sec:unfolding\]](#sec:unfolding){reference-type="ref" reference="sec:unfolding"}.

[^1]: <https://github.com/cesarjesusvalls/ADoNIS>
