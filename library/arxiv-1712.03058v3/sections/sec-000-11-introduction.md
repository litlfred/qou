---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated ﬁltering methods for Markov process epidemic models"
section_id: sec-000-11-introduction
section_title: "Introduction"
section_number: 1.1
pages: 2-3
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
toc_source: outline
doc_brief: "Iterated ﬁltering methods for Markov process epidemic models — Dynamic epidemic models have proven valuable for public health decision makers as they provide useful insights into the understanding"
---
Introduction
In this chapter we describe how iterated ﬁltering methods (Ionides et al.,
2006, 2015) can be used to analyze available infectious disease outbreak data
in the form of time series. The centerpiece of these methods is the assump-
tion that the outbreak data can be modeled as a noisy and only partially
observed realization of a disease transmission process that is assumed to be a
Markov process (King et al., 2016). The general inference approach is to (i)
formulate a suitable Markovian transmission process; (ii) connect the data to
the transmission process via some suitable observation process; (iii) use iter-
ated ﬁltering to perform inference for the model parameters. The inference
method presented here is likelihood-based. It is designed for models where it
is relatively easy to draw samples from the Markov process compared to eval-
uating its transition probabilities. The iterated ﬁltering algorithm is, among
others, implemented in the R package pomp (King et al., 2016) which spans a
wide collection of simulation, inference and model selection methods for par-
tially observed Markov processes (POMP). Other simulation-based inference
methods for this model class are simulated moments (Kendall et al., 1999),
synthetic likelihood (Wood, 2010), non-linear forecasting (Sugihara and May,
1990) or Bayesian approaches such as approximate Bayesian computations
(Toni et al., 2009; Liu and West, 2001) and particle MCMC (Andrieu et al.,
2010). However, at present iterated ﬁltering methods are the only currently
available, frequentist, full-information, simulation-based methods for POMP
models (Ionides et al., 2015).
In this chapter we focus on the “simplest” Markovian SIR trasmission model
1
