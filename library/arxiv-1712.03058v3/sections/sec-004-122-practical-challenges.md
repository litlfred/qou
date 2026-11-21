---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated ﬁltering methods for Markov process epidemic models"
section_id: sec-004-122-practical-challenges
section_title: "Practical challenges"
section_number: 1.2.2
pages: 4-5
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.959
doc_brief: "Iterated ﬁltering methods for Markov process epidemic models — Dynamic epidemic models have proven valuable for public health decision makers as they provide useful insights into the understanding"
---
In principle, the optimization problem in ([\[mle\]](#mle){reference-type="ref" reference="mle"}) looks rather straightforward, however, there are a number of challenges in practice. Firstly, the evaluation of $\mathcal{L}$ can be difficult because the function might not be available in closed form. Secondly, even if evaluation is possible, it might be very hard to derive the first and higher order derivatives of $\mathcal{L}$ analytically or even numerically which are needed for numerical optimization methods, cf. [@Nocedal1999]. In this case we need derivative-free optimizers. Those optimizers might impose other problems, for example when the likelihood can only be approximated stochastically, e.g. by Monte Carlo methods [@Robert2004]. In that case standard deterministic derivative-free optimizers fail. All the problems mentioned above occur for the model class at hand because the likelihood is a complex integral. In the following sections we will give more rigorous details about the problem and introduce a method which gets around these challenges. The problems mentioned arise in the specific setting of our model formulation. In addition, there are some other general challenges with likelihood-based inference in a statistical context. Usually, the point estimate we obtain from maximum likelihood estimation is not very meaningful by itself unless we also quantify the uncertainty of the estimate. One way to solve this problem in a likelihood setting is to construct confidence intervals for the parameters by e.g. calculating the profile log-likelihood for each parameter of interest and invert Wilks' likelihood ratio test to get the desired intervals [@Wilks1938]. Another very common challenge is that often there exist multiple local maxima and the optimization algorithm can get stuck in one of these and not return the global maximum. It is therefore important to use a wide range of starting values for the numerical algorithm in order to improve chances that the global maximum is reached. Moreover, it might very well happen that the maximum is not unique because the surface of the likelihood function has ridges. In that case confidence intervals are a good way to quantify the parameter range. In the following, we introduce and formulate the likelihood of partially observed Markov processes and explain how to tackle all of the issues mentioned above.
