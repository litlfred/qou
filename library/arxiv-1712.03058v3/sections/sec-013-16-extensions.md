---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to"
section_id: sec-013-16-extensions
section_title: "Extensions"
section_number: 1.6
pages: 18-21
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
doc_brief: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to appear in the Handb"
---
In the previous section we used a simple model to explain the concept of it-
erated ﬁltering in order to facilitate understanding. However, reality is often
way more complicated than this toy example. In the following we discuss
some important complications of infectious disease data and how they can
be included in POMP models.
Underreporting Underreporting is a common problem appearing in surveil-
lance data and is usually the more pronounced the less severe the disease is.
It arises for diﬀerent reasons e.g. it can result from asymptomatic cases, cases
where individuals do not consult the doctor, cases that are not identiﬁed as
such (misdiagnosis) or cases which just get lost in the reporting system (Gib-
bons et al., 2014). One way to include underreporting in a POMP model is
to change the observation model to
Yn ∼Pois (κ · H(tn)) .
where κ ∈(0, 1] is the reporting rate which then also can be estimated.
Seasonality For many diseases such as childhood diseases or vector borne
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
18
diseases the transmission rate β is not constant but varies through time. This
might be due to social aggregations of the host such as in daycare institutions
and schools which are closed during summer, changes in environment that
inﬂuence the biology of vector populations or changes in weather such as
temperature or precipitation. One way to introduce this complexity into our
models is through seasonal forcing of the transmission rate so that the num-
ber of infectious contacts changes through time as β(t). Following Keeling
and Rohani (2008), one possible choice is
β(t) = β

1 + ρ cos
2π
w t + φ

,
(16)
where ρ ∈[0, 1] is the amplitude of the forcing, 2π/w ∈R+ is the period of
the forcing and φ ∈[0, 2π] is the phase shift parameter. With this choice of
forcing function the parameter β can be interpreted as the average transmis-
sion rate of an individual which varies between (1 −ρ)β and (1 + ρ)β during
the forcing period.
A more ﬂexible way to choose the forcing function is through splines. If si(t),
i = 1, . . . , k is a periodic B-spline basis, then we can for example deﬁne
β(t) =
k
X
i=1
bisi(t).
Variation of the coeﬃcients bi then gives a wide variety of shapes for β(t).
For the reader new to the theory of splines we recommend Stoer and Bulirsch
(2002). A comprehensive overview of the problems of seasonal forcing can
be found in Keeling and Rohani (2008).
Overdispersion A common phenomenon in calibration of models from data
is the presence of greater variability in the set of observations than would be
expected under the assumed model, cf. e.g. McCullagh and Nelder (1989);
Bretó et al. (2009).
Reasons for this include heterogeneities in the pop-
ulation, model misspeciﬁcations or unmodelled processes which we either
cannot quantify or are very hard to measure in any way. This phenomenon
is called overdispersion and we can account for it in two diﬀerent ways. On
the one hand, we can introduce overdispersion into the observation model
by changing the observation distribution from the Poisson distribution to a
distribution where the variance can be adjusted separately from the mean. In
the case of count data, a natural distribution would be the negative binomial
distribution, so
Yn ∼NegBin

H(tn), 1
ψ

,
(17)
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
19
with H(tn) being the true number of accumulated incidences per time unit
(tn−1, tn] and NegBin(µ, 1/ψ) with ψ > 0 denotes the negative binomial dis-
tribution with mean µ and variance µ + ψµ2. Another choice could be the
truncated normal distribution where the results are rounded to integers.
However, in outbreak data, we often see ﬂuctuations which are clearly not
only due to variation in data collection, but due to phenomena not captured
by the model.
In the toy example in Section 1.5, we have accounted for
stochasticity in the underlying system by assuming that individuals move
between classes at random times. However, for large population sizes the
stochastic system approaches the deterministic system and, hence, the role
of randomness decreases as the population size increases; for details cf. e.g.
Fuchs (2013). One way to account for overdispersion in the transmission
model is to stochastically perturb the transmission rate by multiplying a
continuous-time white noise process ξ(t) which ﬂuctuates around the value
one with the transmission rate. In Bretó et al. (2009) it is shown that by
choosing the corresponding integrated noise process Γ(t) in a way such that
its increments are independent, stationary, non-negative and unbiased the
Markov property is retained. One suitable example for such a process is a
Lévy process with
ξ(t) = d
dtΓ(t),
where marginally
Γ(t + τ) −Γ(t) ∼Gamma
 τ
σ2, σ2
,
and where τ/σ2 denotes the shape and σ2 the age-independent scale pa-
rameter with corresponding mean τ and variance τσ2. The parameter σ2 is
called the inﬁnitesimal variance parameter (Karlin and Taylor, 1981). We
can include this into the model by letting the transmission rate be
β(t) = β · ξ(t).
(18)
More details about this kind of overdispersion can be found in Bretó et al.
(2009); Bretó and Ionides (2011).
Structured populations To make mathematical models for disease spread
more realistic diﬀerent kinds of host heterogeneities can be introduced (Keel-
ing and Rohani, 2008). For example age structure, spatial heterogeneity or
varying risk structures of the individuals might play an important role in
disease transmission and can be easily accommodated in a POMP.
Covariates It can be interesting to investigate what impact a vector-valued
covariate process {Z(t) : t ≥0} has on the disease dynamics. That might
e.g. be environmental covariates such as temperature, precipitation, or demo-
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
20
graphic information such as numbers of births and deaths over time. Inclu-
sion of such a covariate vector is unproblematic in a POMP setting because
the densities fX0, fXn|Xn−1 and fYn|Xn can depend on the observed process
{Z(t) : t ≥0} (King et al., 2016). If one is e.g. interested in investigating
the inﬂuence of a speciﬁc covariate on the transmission rate one could check
the model’s capability to ﬁt the data with and without this covariate and
compare the results.
Initial values In our toy example of Section 1.5 we assumed that the dis-
tribution of the initial values of the Markov process, fX0, is known. Besides
some special cases that could arise e.g. in some experimental situations, this
distribution is, however, not known or observable. If the disease we observe
is endemic in the population and does not vary signiﬁcant over time, it might
make sense to assume that the initial values originate from the stationary
distribution of the system. If this is not the case we can treat the value of
X0 as a parameter to be estimated. In this case, fX0 is a point mass, the
concentration of which depends on θ (King et al., 2016).
Missing data Missing values in outbreak data are a common complication.
When using the R package pomp, the pomp object can handle missing values
if the observation model probability density function is implemented so as
to deal with them appropriately. One way is to construct the observation
density so it returns e.g. a log-likelihood of 0 for the missing data entries, for
implementational details c.f. the FAQ in King (2017).
1.7
