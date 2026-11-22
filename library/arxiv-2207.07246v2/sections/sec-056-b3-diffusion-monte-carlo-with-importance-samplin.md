---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-056-b3-diffusion-monte-carlo-with-importance-samplin
section_title: "B.3 Diffusion Monte Carlo with Importance Sampling"
section_number: null
pages: 137-137
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
Diﬀusion Monte Carlo with Importance Sampling
DMC with constant short-time step without importance sampling is seldom used.
Because the walkers may explore regions in which the short-time approximation is
poor. When this happens, the branch term e−[
V (x)+V (y)
2
−ET]τ can become abnormally
large, and more and more walkers (conﬁgurations) will sink into such regions, the
walkers will not evolve into the desired distribution, and the variance of estimators
can be too big. Therefore we have to use importance sampling to guide the movement
of walkers and thus reduce the variance.
