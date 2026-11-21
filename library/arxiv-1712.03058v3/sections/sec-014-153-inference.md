---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated ﬁltering methods for Markov process epidemic models"
section_id: sec-014-153-inference
section_title: "Inference"
section_number: 1.5.3
pages: 14-17
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.984
doc_brief: "Iterated ﬁltering methods for Markov process epidemic models — Dynamic epidemic models have proven valuable for public health decision makers as they provide useful insights into the understanding"
---
In the following we perform inference for the two epidemiological parameters $\beta$ and $\gamma$ on a set of simulated data from the model where we apply the iterated filtering algorithm presented in Section [\[iterated_filtering\]](#iterated_filtering){reference-type="ref" reference="iterated_filtering"}.\
**Data** We consider a closed population with $\mathcal{N}=10\ 000$ individuals of whom one is initially infectious and the rest are susceptible. A realization from the model presented above with $\beta=1$ and $\gamma=0.5$ for $N=50$ weeks where $t_n=n$ for $n=1,\dots,N$ was simulated. Figure [1](#sim_data){reference-type="ref" reference="sim_data"} shows the number of weekly reported cases where it is assumed that all cases are reported.

<figure id="sim_data">
<div class="center">
<embed src="data.pdf" style="width:10cm" />
</div>
<figcaption>Weekly number of newly reported cases over time, for a simulated set from the POMP model with an underlying Markovian SIR transmission model as defined in Equations (<a href="#states" data-reference-type="ref" data-reference="states">[states]</a>) and (<a href="#poisson" data-reference-type="ref" data-reference="poisson">[poisson]</a>).</figcaption>
</figure>

**Implementation details** We use the iterated filtering algorithm as implemented in the function `mif2` in the R package `pomp` to infer the epidemic parameters $\beta$ and $\gamma$ assuming the initial values and total population size were known. We run the algorithm for $M=100$ iterations and $J=500$ particles. As starting values for the fitting algorithm we use 10 parameter constellations drawn uniformly from a hypercube which contains biologically meaningful parameter values for $\beta$ and $\gamma$. With this procedure we address the potential problem of local maxima in the optimization. In general, if all searches converge to the same MLE for starting values drawn at random from a hypercube this increases the chances that a global maximum has been found [@King2017]. For the perturbation of the parameters we choose a random walk with an initial standard derivation of $0.02$ for both parameters. As cooling scheme we use geometric cooling which means that on the n-th `mif2` iteration, the relative perturbation intensity is $k^{n/50}$ where we chose $k=0.05$. That is, after 50 iterations the perturbation is only half of the intensity compared to the first iteration. In each iteration the variance of the random walk is successively reduced so the log-likelihood of the perturbed model gradually approaches the log-likelihood of the model we are interested in. However, after a finite number of iteration steps, the log-likelihoods of the two models, the one with and the one without perturbed parameters, are not identical. To get around this issue a particle filter evaluation of the `mif2` model output using Equation ([\[eval_pfilter\]](#eval_pfilter){reference-type="ref" reference="eval_pfilter"}) is necessary. Hence, for each of the 10 `mif2` outputs we obtain we run 10 particle filters, each with 1000 particles. From the multiple particle filter evaluation we can then calculate the average log-likelihood and the standard error of the Monte Carlo approximation for every parameter set. Consequently, we choose the parameter constellation of the 10 possible with the highest average log-likelihood as the maximum likelihood estimate. In order to quantify the associated uncertainties of the parameter estimates based on our observations we calculate the 95 % confidence intervals for each parameter. For this we construct the profile likelihood of each parameter and apply the Monte Carlo adjusted profile (MCAP) algorithm [@Ionides2017]. This recently developed methodology accounts for the presence of Monte Carlo error in the likelihood evaluation and adjusts the width of the confidence interval accordingly. This procedure might seem overly complicated at first sight because, intuitively, the parameter swarm we obtain as an output from the iterated filtering algorithm should contain some measure of uncertainty. However, due to particle depletion, which is the situation when only very few different particles have significant weight [@Doucet2011], the information about the local shape of the likelihood surface contained in the particles is not very reliable. The profile likelihood is much more robust in this case since it relies on multiple independent `mif2` searches [@King2017].\
**Results** The inference results are visualized in Figures [2](#mif){reference-type="ref" reference="mif"} and [3](#profile){reference-type="ref" reference="profile"}. As shown in Figure [2](#mif){reference-type="ref" reference="mif"} the randomly drawn starting values for both parameters are converging towards the true values at the same time as the likelihood increases and the number of filtering failures disappears. Both 95% confidence intervals constructed from the profile log-likelihoods cover the true parameters as shown in Figure [3](#profile){reference-type="ref" reference="profile"}.

<figure id="mif">
<div class="center">
<embed src="mif.pdf" style="width:12cm" />
</div>
<figcaption>Diagnostic plot of the iterated filtering algorithm for 100 iterations for simulated incidence data. Shown is the evolution of the log-likelihood (loglik), the number of filtering failures in each <code>mif2</code> iteration (nfail) and parameter estimates for parameters <span class="math inline"><em>β</em></span> and <span class="math inline"><em>γ</em></span> per iteration for 10 trajectories with random starting values drawn from a hypercube.</figcaption>
</figure>

<figure id="profile">

<figcaption>The smoothed profile likelihoods (solid curves) for both parameters of interest where the solid vertical lines show the true values and the dashed vertical lines contain the corresponding MCAP 95% confidence interval. The quadratic approximation in a neighborhood of the maximum is shown as the dashed curves. </figcaption>
</figure>
