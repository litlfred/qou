---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples"
section_id: sec-013-parameter-inference-and-uncertainty-quantificati
section_title: "Parameter Inference and Uncertainty Quantification"
section_number: null
pages: 10-14
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.976
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples — 19 sections: ADoNIS: A Differentiable generatOr; Introduction; Differentiable programming in part"
---
[]{#sec:fitting label="sec:fitting"}

::: figure*
![image](Asimov_xsec_samples){width="\\linewidth"}
:::

This section illustrates how a differentiable event generator constructed as described above can be used directly for parameter inference and uncertainty quantification. In [ADoNIS]{.smallcaps}, the derivative of any observable built from the events is available by construction (Sec. [\[sec:adonis_events\]](#sec:adonis_events){reference-type="ref" reference="sec:adonis_events"}), so any differentiable loss can be optimised directly without external response functions or finite-difference derivatives. We demonstrate this in cross-section space, where experiments routinely report their measurements, and show that the same framework supports the standard inference machinery used in HEP, from fitting and Gaussian uncertainties to profiling and marginalisation. Our focus here is on demonstrating this machinery, thereby enabling applications including tests of the self-consistency of published measurements, global model tuning, and the extraction and Gaussianity testing of correlated cross-section model constraints; pursuing these applications is left to dedicated future studies.

We demonstrate these capabilities using the same $21$ observables and $17$ parameters identified in Sec. [\[sec:jacobian\]](#sec:jacobian){reference-type="ref" reference="sec:jacobian"}. For the closure test, the parameters are randomly displaced within their physical ranges to define an injected truth, and the nominal event bank is reweighted to the corresponding prediction. Each bin is assigned the same $5\%$ uncertainty used in Sec. [\[sec:jacobian\]](#sec:jacobian){reference-type="ref" reference="sec:jacobian"}. No informative parameter priors are imposed, although all parameters remain restricted to their physical ranges. For simplicity, we use a Gaussian $\chi^2$ throughout; the same differentiable prediction can enter any differentiable likelihood.

Parameter optimisation is performed with a Gauss--Newton method [@Nocedal:2006] using the exact Jacobian supplied by [ADoNIS]{.smallcaps}. Sec. [\[sec:fit_performance\]](#sec:fit_performance){reference-type="ref" reference="sec:fit_performance"} describes the method in more detail and compares its performance with MIGRAD [@James:1975dr; @iminuit].

Figure [\[fig:fit_rates\]](#fig:fit_rates){reference-type="ref" reference="fig:fit_rates"} shows the result in observable space. The injected truth is sufficiently displaced from nominal that the pre-fit prediction visibly differs from the data wherever the shifted parameters have an effect, while the post-fit prediction recovers it. Because the closure dataset is generated exactly at the injected truth, the residual at the minimum vanishes by construction.

![(a) Recovery of the $17$ fitted parameters, in units of the reference width $\delta\theta_k$ defined in Sec. [\[sec:jacobian\]](#sec:jacobian){reference-type="ref" reference="sec:jacobian"}. Every parameter returns to its injected truth. The four overlaid bars show the Gaussian, profile, Laplace-marginal and directly sampled marginal intervals, all at $68\%$ and all obtained from the same dataset. The direct marginal is obtained with the No-U-Turn Sampler (NUTS). (b) Distribution over the toy ensemble of $\Delta\chi^2$ between the true and fitted parameters, compared with the $\chi^2$ distribution for $17$ degrees of freedom predicted by Wilks' theorem. The observed coverage is quoted at three confidence levels.](closure_demo){#fig:closure width="\\linewidth"}

The same differentiable prediction can also be used directly for uncertainty quantification, without restricting the analysis to the local Gaussian approximation around the fitted minimum. Panel (a) of Fig. [1](#fig:closure){reference-type="ref" reference="fig:closure"} compares four $68\%$ intervals obtained from the same dataset. The Gaussian interval uses the local covariance at the minimum; the profile evaluates the likelihood away from it along the parameter of interest; the Laplace marginal also accounts for the volume of the nuisance directions; and direct sampling explores the full parameter space. These provide increasingly non-local uses of the same underlying prediction and allow their assumptions to be tested against one another.

::: figure*
![image](corner_plots){width="0.7\\linewidth"}
:::

To demonstrate that the differentiable treatment extends beyond the local curvature, we construct a profile likelihood for each parameter by fixing $\theta_k$ and re-minimising over the remaining $16$ parameters, $$\label{eq:profile}
\chi^2_{\rm prof}(\theta_k)
=
\min_{\bm{\theta}_{\rm nuis}}
\chi^2(\theta_k,\bm{\theta}_{\rm nuis}).$$ Each profile is evaluated at $13$ nodes, with its range extended independently on either side until $\Delta\chi^2_{\rm prof}>25$ or a physical boundary is reached. This adaptive range matters for shallow directions, where several Gaussian widths need not exhaust the likelihood. To compare with the marginal intervals on a common $68\%$ mass basis, we normalise $$\mathcal{L}_{\rm prof}(\theta_k)
\propto
e^{-\Delta\chi^2_{\rm prof}(\theta_k)/2}$$ over the scanned range and quote its shortest $68\%$ region.

The same framework also supports marginalisation, where nuisance parameters are integrated rather than optimised. The marginal likelihood is $$\label{eq:marginal}
\mathcal{L}_{\rm marg}(\theta_k)
=
\int
\mathcal{L}(\theta_k,\bm{\theta}_{\rm nuis})
\,d\bm{\theta}_{\rm nuis}.$$ A second-order expansion about the conditional best fit gives the Laplace approximation $$\label{eq:laplace}
\mathcal{L}_{\rm marg}(\theta_k)
\propto
\mathcal{L}_{\rm prof}(\theta_k)
\sqrt{\det V_{\rm nuis}(\theta_k)},$$ where $V_{\rm nuis}$ is the local nuisance-parameter covariance. The profile measures the height of the likelihood ridge, while the determinant measures its transverse volume; the two differ whenever that volume changes along the ridge.

The second derivatives available from the same model allow this marginalisation to use the exact local curvature rather than reusing the Gauss--Newton, or Fisher, approximation of Eq. [\[eq:adonis_fisher\]](#eq:adonis_fisher){reference-type="ref" reference="eq:adonis_fisher"}. At each profile point we evaluate $V_{\rm nuis}$ from the exact Hessian by nested automatic differentiation. This matters away from the global minimum, where the residual is generally non-zero and the residual-dependent contribution to the Hessian need not vanish. Second-order information can therefore be used where the statistical construction requires it, without building a separate numerical response model.

The analysis is not restricted to marginalisation through a local expansion. We also sample the same $17$-dimensional likelihood directly with the No-U-Turn Sampler (NUTS), an MCMC algorithm based on Hamiltonian Monte Carlo [@Hoffman:2011ukg], assuming a uniform density over the physical parameter ranges of Sec. [\[sec:adonis_reweighting\]](#sec:adonis_reweighting){reference-type="ref" reference="sec:adonis_reweighting"} and no additional prior. The four constructions can then be compared directly: Gaussian versus profile tests the local quadratic description along the parameter of interest; profile versus Laplace tests the importance of nuisance volume; and Laplace versus NUTS tests the quadratic approximation used to describe that volume. All four are obtained from the same differentiable prediction. Gradient information therefore does not confine the analysis to Gaussian or locally approximated uncertainties, but remains available throughout profiling and full marginalisation.

The same fitting machinery remains well behaved when applied repeatedly to statistically fluctuated datasets. Panel (b) of Fig. [1](#fig:closure){reference-type="ref" reference="fig:closure"} repeats the fit for $2000$ toys, obtained by fluctuating the same injected prediction with the per-bin uncertainties, and forms $$\Delta\chi^2
=
\chi^2(\bm{\theta}_{\rm true})
-
\chi^2(\hat{\bm{\theta}}).$$ The ensemble follows the $\chi^2$ distribution with $17$ degrees of freedom expected from Wilks' theorem [@Wilks:1938dza]. The measured coverages are $67.8\pm1.0\%$, $89.4\pm0.7\%$, and $94.9\pm0.5\%$, compared with nominal $68.3\%$, $90\%$, and $95\%$, respectively, and the median $\chi^2$ per degree of freedom is $0.992$. The differentiable treatment therefore reproduces not only the injected minimum, but the expected statistical behaviour of an ensemble of fits without outliers. Carrying exact derivatives through the generator introduces no observable penalty in fit convergence or frequentist coverage.

Physical boundaries are common in HEP fits and provide an important test of the inference machinery. The injected value of $\Delta E_b$ lies close to the physical wall where the spectral-function reweight becomes flat, producing a truncated and strongly asymmetric likelihood. Such a boundary is precisely a regime in which Gaussian approximations cease to apply; when the true value lies on it, the asymptotic likelihood-ratio distribution is described by the corresponding Chernoff mixture rather than the usual Wilks result [@Chernoff:1954]. No modification of the differentiable model is required: the physical range is part of the minimisation domain, the profile terminates at the boundary, and NUTS remains within it. The same gradient information can therefore be used unchanged in fits involving physical limits and strongly non-Gaussian uncertainties.

The derivative information is also usable across correlated multi-parameter regions, not only in the immediate neighbourhood of the best fit. Figure [\[fig:corner\]](#fig:corner){reference-type="ref" reference="fig:corner"} shows this for the three parameters sharing the resonant axial block and for $\Delta E_b$ with its physical boundary. Above the diagonal, agreement of the four uncertainty constructions identifies directions where the local Gaussian description is sufficient; their separation localises the non-Gaussianity to particular parameter combinations and, through the comparisons above, identifies its origin.

Below the diagonal, the same derivatives are evaluated over the full physically allowed parameter space. The arrows show the local Gauss--Newton step from each point: near the minimum they determine the covariance of the inferred region, while farther away they determine the direction in which the fit moves. Their smooth behaviour across the full range shows that the gradient supplied by [ADoNIS]{.smallcaps} is available throughout the parameter space, rather than being a response constructed only around the nominal point or the best fit. The same differentiated model therefore describes both the optimisation landscape and the uncertainty around its solution.

Taken together, these tests show that the gradient information supplied by [ADoNIS]{.smallcaps} can be carried through the full inference workflow without narrowing the statistical tools available to the analysis. At the analysis level, this realises the same advantage that motivates built-in differentiability throughout the generator: additional information and computational leverage are gained without imposing a corresponding restriction on how the physics inference is performed.
