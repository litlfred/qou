---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to"
section_id: sec-015-18-concluding-comments
section_title: "Concluding comments"
section_number: 1.8
pages: 24-25
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
doc_brief: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to appear in the Handb"
---
1.8.1
Pros and cons of iterated ﬁltering methods for
outbreak data
The method we have described has many positive aspects. First of all, as
illustrated in this chapter, the method is highly ﬂexible and can be easily
adapted to many diﬀerent situations of interest. The great strength of the
method is that one only needs to simulate from the transmission model if
the complete likelihood is not directly tractable. Facilitated by the R pack-
age pomp the method is very straightforward to implement and can be easily
adapted for a wide range of settings. The package is optimized for computa-
tional eﬃciency, in particular the simulation functions (such as euler.sim or
gillespie.sim) facilitate implementation considerably and give rise to sub-
stantial gains in speed by accessing C code. Secondly, the method facilitates
dealing with unobserved variables and has no problem with the fact that
transmission is continuous in time, while observations are made at discrete
points in time. Furthermore, it is easy to combine transmission noise and
observation noise as long as the Markov property is retained. The method
also allows the inclusion of covariates in mechanistically reasonable ways. As
mentioned earlier, to date this is the only simulation-based frequentist ap-
proach for POMP models that does not rely on summary statistics and can
perform eﬃcient inference for POMP models in situations where available
Bayesian methods cannot (Ionides et al., 2015).
However, there is one main diﬃculty with the method. Since it is purely
simulation-based it comes at the cost of being computationally very expen-
sive in particular when the time series becomes long and the state space
increases. In Section 1.5.4 we gave some practical hints of how to mitigate
the problem. Moreover, the method requires the transmission model to be
Markovian which can be problematic because in practice the stages of dis-
eases are rarely well-described by exponential distributions. An easy way
to mitigate the problem is by subdividing the respective compartments so
that the waiting times individuals stay in each compartment change from
being exponentially distributed to gamma distributed, i.e. having a more
pronounced mode. Sometimes it is also possible to formulate non-Markovian
processes as alternate Markov processes with additional state variables (e.g.,
if Xn depends on both Xn−1 and Xn−2, i.e., is not Markov, one could deﬁne
a new, bivariate Markov process Zn = (Xn, Xn−1)). However, these strate-
gies increase the dimension of the unobserved state space of the transmission
model which can result in an increase of Monte Carlo noise in the particle
ﬁlter.
Hence, those strategies are only eﬀective up to the point where it
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
24
becomes computationally too expensive to handle this increase of noise.
1.8.2
