---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated ﬁltering methods for Markov process epidemic models"
section_id: sec-007-132-evaluation-of-the-likelihood
section_title: "Evaluation of the likelihood"
section_number: 1.3.2
pages: 7-7
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 1.0
doc_brief: "Iterated ﬁltering methods for Markov process epidemic models — Dynamic epidemic models have proven valuable for public health decision makers as they provide useful insights into the understanding"
---
[]{#evaluation label="evaluation"} Before addressing the question of how to maximize the likelihood in ([\[lik\]](#lik){reference-type="ref" reference="lik"}) in an efficient way, we have to first think about how we actually evaluate $\mathcal{L}$ for a given parameter vector $\bm{\theta}$. In the special case that the underlying transmission model is deterministic and the initial values are given, $\bm{X}_n=\bm{x}_n(\bm{\theta})$ is a non-random function of $\bm{\theta}$ for each $n$, hence $f_{\bm{X}_n|\bm{X}_{n-1}}$and $f_{\bm{X}_0}$ are point masses. The likelihood equation ([\[lik\]](#lik){reference-type="ref" reference="lik"}) then reduces to $$\ell(\bm{\theta})=\log \mathcal{L}(\bm{\theta})= \sum_{n=1}^N \log f_{\bm{Y}_n|\bm{X}_{n}}(\bm{y}^*_n;\bm{x}_{n}(\bm{\theta}),\bm{\theta}).$$ So given that we know the distribution of our observation model, evaluation of the log-likelihood corresponds to summing over the logarithm of the observation density given the states of the deterministic "Markov process" at each point in time. Maximum likelihood estimation then reduces to a classical numerical optimization problem for a non-linear function of the parameter vector and for optimization we can use a derivative-free optimizer e.g. the Nelder-Mead method [@nelder]. However, in general evaluating (and optimizing) the function $\mathcal{L}$ is unfortunately not as straightforward because the transmission model is not deterministic. Rather, it is a non-trivial problem because of the high dimension of the integral. In the following we describe how to evaluate Equation ([\[lik\]](#lik){reference-type="ref" reference="lik"}) in a general way with particle filters.
