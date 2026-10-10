---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to"
section_id: sec-015-18-concluding-comments
section_title: "Concluding comments"
section_number: 1.8
pages: 24-25
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
text_source: latex
latex_prose_ratio: 0.81
latex_coverage_ratio: 1.0
doc_brief: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to appear in the Handb"
---
[]{#comments label="comments"}

## Pros and cons of iterated filtering methods for outbreak data

The method we have described has many positive aspects. First of all, as illustrated in this chapter, the method is highly flexible and can be easily adapted to many different situations of interest. The great strength of the method is that one only needs to simulate from the transmission model if the complete likelihood is not directly tractable. Facilitated by the `R` package `pomp` the method is very straightforward to implement and can be easily adapted for a wide range of settings. The package is optimized for computational efficiency, in particular the simulation functions (such as `euler.sim` or `gillespie.sim`) facilitate implementation considerably and give rise to substantial gains in speed by accessing C code. Secondly, the method facilitates dealing with unobserved variables and has no problem with the fact that transmission is continuous in time, while observations are made at discrete points in time. Furthermore, it is easy to combine transmission noise and observation noise as long as the Markov property is retained. The method also allows the inclusion of covariates in mechanistically reasonable ways. As mentioned earlier, to date this is the only simulation-based frequentist approach for POMP models that does not rely on summary statistics and can perform efficient inference for POMP models in situations where available Bayesian methods cannot [@Ionides2015].\
However, there is one main difficulty with the method. Since it is purely simulation-based it comes at the cost of being computationally very expensive in particular when the time series becomes long and the state space increases. In Section [\[tips\]](#tips){reference-type="ref" reference="tips"} we gave some practical hints of how to mitigate the problem. Moreover, the method requires the transmission model to be Markovian which can be problematic because in practice the stages of diseases are rarely well-described by exponential distributions. An easy way to mitigate the problem is by subdividing the respective compartments so that the waiting times individuals stay in each compartment change from being exponentially distributed to gamma distributed, i.e. having a more pronounced mode. Sometimes it is also possible to formulate non-Markovian processes as alternate Markov processes with additional state variables (e.g., if $X_n$ depends on both $X_{n-1}$ and $X_{n-2}$, i.e., is not Markov, one could define a new, bivariate Markov process $Z_n = (X_{n},X_{n-1}))$. However, these strategies increase the dimension of the unobserved state space of the transmission model which can result in an increase of Monte Carlo noise in the particle filter. Hence, those strategies are only effective up to the point where it becomes computationally too expensive to handle this increase of noise.

## Further reading

For the reader interested in more details about the theoretical background of iterated filtering methods we recommend [@ionides06] and [@Ionides2015] for further reading. For the reader interested in learning how to work with the `R` package `pomp` we recommend the study of [@kingNgu] and to follow some of the very comprehensive online tutorials available through [@King2017]. The package has already been applied to answer many different epidemiological questions for different infectious diseases, e.g. for cholera [@King2008], measles [@He2010], malaria [@bhadra], polio [@martinezpolio], ebola [@King2015], and rotavirus [@martinez; @Stocks2017]. Finally, iterated filtering has facilitated the development and analysis of a divers array of mechanistic models, a recent and comprehensive review of which can be found in [@Breto2017].
