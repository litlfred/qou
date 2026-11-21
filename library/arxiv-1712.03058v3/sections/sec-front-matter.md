---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated ﬁltering methods for Markov process epidemic models"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-2
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
toc_source: outline
doc_brief: "Iterated ﬁltering methods for Markov process epidemic models — Dynamic epidemic models have proven valuable for public health decision makers as they provide useful insights into the understanding"
---
Iterated ﬁltering methods for Markov process
epidemic models
Theresa Stocks1
1Department of Mathematics, Stockholm University, Sweden
This manuscript is a preprint of a Chapter to appear in the Handbook
of Infectious Disease Data Analysis, Held, L., Hens, N., O’Neill, P.D.
and Wallinga, J. (Eds.). Chapman & Hall/CRC, 2018. Please use
the book for possible citations.
Chapter Abstract
Dynamic epidemic models have proven valuable for public health decision makers
as they provide useful insights into the understanding and prevention of infectious
diseases.
However, inference for these types of models can be diﬃcult because
the disease spread is typically only partially observed e.g.
in form of reported
incidences in given time periods. This chapter discusses how to perform likelihood-
based inference for partially observed Markov epidemic models when it is relatively
easy to generate samples from the Markov transmission model while the likelihood
function is intractable. The ﬁrst part of the chapter reviews the theoretical back-
ground of inference for partially observed Markov processes (POMP) via iterated
ﬁltering. In the second part of the chapter the performance of the method and as-
sociated practical diﬃculties are illustrated on two examples. In the ﬁrst example
a simulated outbreak data set consisting of the number of newly reported cases
aggregated by week is ﬁtted to a POMP where the underlying disease transmis-
sion model is assumed to be a simple Markovian SIR model. The second example
illustrates possible model extensions such as seasonal forcing and over-dispersion
in both, the transmission and observation model, which can be used, e.g., when
analysing routinely collected rotavirus surveillance data. Both examples are imple-
mented using the R-package pomp (King et al., 2016) and the code is made available
online.
arXiv:1712.03058v3  [stat.ME]  28 Oct 2018
Chapter 1
Iterated ﬁltering methods for
Markov process epidemic models
