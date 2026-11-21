---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated ﬁltering methods for Markov process epidemic models"
section_id: sec-009-14-iterated-filtering-methods
section_title: "Iterated filtering methods"
section_number: 1.4
pages: 10-10
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
toc_source: outline
text_source: latex
latex_prose_ratio: 0.701
latex_coverage_ratio: 0.567
doc_brief: "Iterated ﬁltering methods for Markov process epidemic models — Dynamic epidemic models have proven valuable for public health decision makers as they provide useful insights into the understanding"
---
[]{#iterated_filtering label="iterated_filtering"} Iterated filtering is a simulation-based method to find the MLE which takes advantage of the structure of POMP models and particle filters. It was first introduced by [@ionides06] and further improved in [@Ionides2015]. The iterated filtering method uses the property that it is easy to simulate from $f_{\bm{X}_n|\bm{X}_{n-1}}$ while the likelihood is not tractable directly. The basic idea is that a particle filter is applied to a model in which the parameter vector for each particle is following a random walk. As iterations progress, the intensity of the perturbations is successively reduced (\"cooling\"). It can be shown that the algorithm converges towards the MLE [@Ionides2015]. At present this method is the only simulation-based frequentist approach that uses the full information contained in the data. Moreover, iterated filtering methods have been able to solve likelihood-based inference problems for infectious disease related questions which were computationally intractable for available Bayesian methods [@Ionides2015].
