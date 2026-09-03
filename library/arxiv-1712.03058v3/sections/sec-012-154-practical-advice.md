---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to"
section_id: sec-012-154-practical-advice
section_title: "Practical advice"
section_number: 1.5.4
pages: 17-18
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
doc_brief: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to appear in the Handb"
---
In the R package pomp a partially observed Markov process together with
observations in the form of a uni- or multivariate time series can be repre-
sented via a so called pomp object. The whole package’s functionality such
as simulation and inference is centered around this object. Depending on
which functions one would like to use, the model can be implemented by
specifying some or all model components. In order to help identify possible
error sources that can occur while applying the algorithm we now describe a
few practical hints.
The ﬁrst step after constructing the pomp object is to simulate realizations
from the model in order to check that the code is working and the model
gives the expected output. A good idea at this stage is to also construct the
corresponding deterministic skeleton of the stochastic Markov transmission
model in order to have a simpliﬁed version of the model and to also generate
trajectories and compare if the mean of the stochastic model corresponds to
the deterministic version. Another beneﬁt of simulating from the model in
general is that it helps to identify a range of likely parameters which generate
realizations that resemble the data. Before the data comes into play and the
actual ﬁtting starts we ﬁnd it very helpful to ﬁrst test the algorithm with
simulated data. For this a realization of the model is generated, then the
known set of parameters which was used to generate the realization is evalu-
ated with the particle ﬁlter. This way we make sure that the core function in
the iterated ﬁltering method is working. Then the algorithm can be applied
to the simulated set and it should give back the values used for simulation.
This procedure also helps understanding how the parameter estimators are
correlated and if they are identiﬁable.
Now, let us move to the data. As a last step before applying the iterated
ﬁltering algorithm to our observations we recommend to ﬁt the data ﬁrst to
the simpler, deterministic model in order to get a feeling for how the param-
eters behave and identify possible problems with the likelihood surface etc.
Then, when the mif2 is ﬁnally used it makes sense to choose likely values
as starting values for the parameters we want to estimate ﬁrst. However,
in a last step a global search should be carried out which means that ran-
dom starting values are chosen and, ideally, then all searches converge to the
same MLE regardless of their starting values. In practice, the likelihood is
often ridged so some searches can get stuck in local maxima. That is why it
is important to use many initial values from many diﬀerent starting values.
Another common problem in practice is that parameter values are suggested
which are very unlikely which in turn leads to ﬁltering failures. In that case
it can be useful to add stochasticity to the model which accounts for model
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
17
misspeciﬁcations or unmodelled disease characteristics.
Working with the mif2 algorithm can be a time consuming task because the
method is simulation-based. This is the price we pay for not needing to be
able to evaluate the density function of the Markov model directly. That is
why we also want to give some hints of how to speed up the procedure to
some extent. The ﬁrst idea is to parallelize the code so that multiple searches
can be carried out at the same time. This, in turn, poses some challenges
in preventing repetition of expensive computations and trying to ensure re-
producibility and – we present one way of doing this in the manual Stocks
(2017), more can be found in the tutorials at King (2017). In order to ensure
that the information about the likelihood surface is continually improved it
is useful to keep a record of all parameter vectors estimated with the mif2
function, together with the computed likelihood for each parameter set, e.g.
by saving the obtained results in a CSV ﬁle (King, 2017). Moreover, it is
sometimes worth accepting approximation errors by choosing the simulation
time step in the τ leaping algorithm to be not too small, which can lead to
signiﬁcant gains in computational speed; for a short discussion on numerical
solutions based on discretizations in the context of POMP models cf. Bretó
et al. (2009).
1.6
