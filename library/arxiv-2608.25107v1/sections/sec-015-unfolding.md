---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples"
section_id: sec-015-unfolding
section_title: "Unfolding"
section_number: null
pages: 15-17
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.971
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples — 19 sections: ADoNIS: A Differentiable generatOr; Introduction; Differentiable programming in part"
---
[]{#sec:unfolding label="sec:unfolding"}

The previous section used the differentiable prediction directly in truth space to constrain interaction-model parameters. The same machinery can also be carried through the detector response, allowing the signal in true kinematics to be extracted from reconstructed data while fitting flux, detector and interaction-model nuisance parameters simultaneously. This is the setting of a cross-section measurement: experiments observe event distributions in reconstructed kinematics, from which the corresponding signal rates in true kinematics must be inferred after accounting for detector effects and backgrounds, before normalisation by the integrated flux and number of targets. Exploiting the differentiability of [ADoNIS]{.smallcaps}, we illustrate this extraction with a template-fit unfolding, the standard approach used in T2K cross-section measurements[^1].

We demonstrate this by mirroring the T2K $\nu_\mu$ CC0$\pi$ double-differential measurement of Ref. [@T2K:2020sbd], in muon momentum and angle, $d^2\sigma/dp_\mu\,d\cos\theta_\mu$. We adopt the same signal definition: a $\nu_\mu$ charged-current interaction with exactly one $\mu^-$, no pions or other mesons after FSI, any number of nucleons, and no restriction on the muon kinematics. We also retain the same $58$ truth bins, while splitting each momentum interval in two at reconstruction level to obtain $116$ reconstructed bins. A simple stochastic detector model applies a $10\%$ momentum smearing and a $5^\circ$ angular smearing event by event. To introduce a background component, charged pions below $400$ MeV/$c$ are reconstructed with $50\%$ efficiency, implemented as an event-by-event random selection, so missed pions allow CC1$\pi$ events to enter the CC0$\pi$ selection, giving a signal purity of $0.915$. The prediction is normalised to an exposure corresponding to approximately $170\,000$ selected events, while the underlying event bank provides about $24$ times larger Monte Carlo statistics.

![Unfolded T2K CC0$\pi$ double-differential cross section in two of the nine $\cos\theta_\mu$ slices, for a closure test and for a dataset in which the true signal is increased by $20\%$.](unfolding_example){#fig:unfold_result width="0.99\\linewidth"}

![Uncertainty on the $58$ unfolded templates as statistical and systematic contributions are successively included.](unfolding_uncertainty_budget){#fig:unfold_budget width="0.8\\linewidth"}

![Post-fit correlation matrix of the $196$ fitted parameters: $58$ signal templates $\bm{c}$, $10$ flux parameters $\bm{f}$, $12$ cross-section parameters $\bm{\theta}$ and $116$ detector parameters $\bm{d}$. The scale is symmetric-logarithmic, becoming linear for correlations below $0.01$ in magnitude.](unfolding_param_correlations){#fig:unfold_corr width="0.99\\linewidth"}

The prediction in reconstructed bin $i$ is $$\label{eq:unfold_model}
\mu_i(\bm{c},\bm{f},\bm{\theta},\bm{d})
=
d_i\left[
\sum_{j,b} A_{ijb}\,c_j f_b
+
\sum_b B_{ib}(\bm{\theta})\,f_b
\right],$$ where $A_{ijb}$ is the nominal signal template contributing to reconstructed bin $i$ from truth bin $j$ and neutrino-energy bin $b$, while $B_{ib}(\bm{\theta})$ is the corresponding background prediction. The $58$ template parameters $\bm{c}$ independently scale the signal truth bins and are left unconstrained, so that the signal cross section is determined directly by the fit rather than by the interaction model. The unfolded cross section in each truth bin is therefore obtained by applying the fitted $c_j$ to the corresponding nominal cross section.

The flux is described by $10$ parameters $\bm{f}$, each scaling all signal and background events within an interval of true neutrino energy. The intervals are $0$--$600$ MeV, four $100$ MeV bins between $600$ and $1000$ MeV, two $200$ MeV bins between $1000$ and $1400$ MeV, two $300$ MeV bins between $1400$ and $2000$ MeV, and an open bin above $2000$ MeV. For illustration, they are assigned a correlated Gaussian prior with $10\%$ marginal uncertainties and covariance $$\Sigma_{bb'}=\sigma_b\sigma_{b'}
\exp\!\left(
-\frac{|\bar E_{\nu,b}-\bar E_{\nu,b'}|}{400~\mathrm{MeV}}
\right),$$ where $\sigma_b=0.10$ and $\bar E_{\nu,b}$ is the centre of flux bin $b$. For the open final bin, we set $\bar E_{\nu,b}=2150$ MeV by extrapolating the width of the preceding finite bin, providing a finite representative energy for the correlation kernel.

Of the $28$ cross-section parameters introduced in Sec. [\[sec:adonis_reweighting\]](#sec:adonis_reweighting){reference-type="ref" reference="sec:adonis_reweighting"}, we retain the $12$ whose variation on the reference scales defined in Sec. [\[sec:jacobian\]](#sec:jacobian){reference-type="ref" reference="sec:jacobian"} produces a non-negligible change in the predicted background: $k_F$, $S_\Delta$, $C_5^A$, $N_{\rm SF}$, $N_{\rm RES}$, $M_A^{\rm RES}$, $f^{\rm cex}_{NN}$, $s^{\rm el}_{NN,pn}$, $\Delta E_b$, $s_{\rm abs}^{\pi}$, $N_{\rm SRC}$ and $s^{\rm el}_{\pi N}$. Concretely, we require $\|(\partial B/\partial\theta_k)\,\sigma_k^{\rm ref}/\sqrt{\mu}\|_2\ge 1$ over the reconstructed bins, where $\mu$ is the nominal signal-plus-background prediction and $\sigma_k^{\rm ref}$ the corresponding reference variation. These parameters are also left unconstrained.

Finally, the $116$ detector parameters $\bm{d}$, one per reconstructed bin, carry independent Gaussian $5\%$ normalisation uncertainties. The fit therefore contains $196$ parameters in total and deliberately spans three different nuisance treatments: unconstrained cross-section parameters, independently constrained detector parameters, and correlated flux parameters.

An important feature of Eq. [\[eq:unfold_model\]](#eq:unfold_model){reference-type="ref" reference="eq:unfold_model"} is that mapping the prediction from true to reconstructed kinematics introduces no additional obstacle to differentiability. For a given analysis definition, the outcomes of detector smearing, event selection, and assignment to true and reconstructed bins are fixed; they determine which events contribute to each bin, but not how their weights respond to the fitted parameters. Importantly, these analysis choices are themselves downstream of event generation. Different signal definitions, selections and binnings can therefore be explored efficiently by reapplying these downstream operations to the same event-level predictions and derivatives.

Once this mapping is defined, the parameterisation used here is multilinear in the template, flux, and detector parameters, $\bm{c}$, $\bm{f}$ and $\bm{d}$, so their derivatives follow directly from the precomputed signal and background tensors.

Figure [1](#fig:unfold_result){reference-type="ref" reference="fig:unfold_result"} shows the unfolded result for a closure dataset and for a second dataset in which the true signal is increased uniformly by $20\%$. In both cases the fit recovers the injected spectrum, demonstrating that the unfolding pipeline behaves as expected.

The relative contributions to the uncertainty across the $58$ truth bins are shown in Fig. [2](#fig:unfold_budget){reference-type="ref" reference="fig:unfold_budget"}. Statistical, flux and detector uncertainties all contribute appreciably, while the cross-section component remains small because the high-purity sample limits the role of the interaction model to the background prediction.

The corresponding post-fit correlations are shown in Fig. [3](#fig:unfold_corr){reference-type="ref" reference="fig:unfold_corr"}. The signal templates are anticorrelated with the flux because both control the overall signal rate, while neighbouring templates can be anticorrelated through detector migration between adjacent truth bins. The detector block remains approximately diagonal, reflecting the independent reconstructed-bin normalisations. Correlations involving the cross-section parameters are more heterogeneous: different interaction parameters induce distinct, generally non-linear distortions of the background and can therefore correlate positively or negatively with different signal templates.

Taken together, these results show that the same differentiable framework can be used directly for unfolding.

[^1]: A direct comparison with iterative Bayesian unfolding [@DAgostini:1994fjx], the other widely used approach in the field, is given in Ref. [@T2K:2016jor].
