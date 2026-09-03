---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to"
section_id: sec-005-131-likelihood-of-a-pomp
section_title: "Likelihood of a POMP"
section_number: 1.3.1
pages: 5-7
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
doc_brief: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to appear in the Handb"
---
dard methods to ﬁnd the MLE do not apply here and ﬁnally describe how
iterated ﬁltering methods overcome these problems. In the following, the
exposition and notation is adopted from King et al. (2016) and the materials
and tutorials in King (2017).
1.3.1
Likelihood of a POMP
A POMP consists of two model components, (i) an unobserved Markov pro-
cess {X(t; θ) : t ≥0}, which can be discrete or continuous in time, and (ii) an
observation model which describes how the data collected at discrete points
in time t1, . . . , tN, is connected to the transmission model. For notational
convenience, we write Xn = X(tn; θ) and X0:N = (X0, . . . , XN). In our ap-
plication, the process X0:N describes the dynamics of the disease spread, e.g.
in the case of the simple Markovian SIR model Xn = (S(tn), I(tn), R(tn))′
counts the number of susceptible, infectious and removed individuals at time
tn. Let Yn denote the random variable counting the observations at time tn
which depend on the state of the transmission process Xn at that time, cf.
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
5
Figure 1.1: A partially observed Markov process where Yn, n = 1, . . . , N,
denotes the observations at time tn, which depend on the state of the trans-
mission process Xn := X(tn; θ) at that time.
Figure 1.1. Our data, y∗
1:N = (y∗
1, . . . , y∗
N), are then modeled as a realization
of this observation process. Depending on how many aspects of the disease
dynamics we observe, y∗
1:N can be either a univariate or multivariate time
series. Assuming that the observable random variable Yn is independent of
all other variables given the state of the transmission process Xn, the joint
density of the states and the observations is deﬁned as the product of the
one-step transmission density, fXn|Xn−1(xn|xn−1; θ), the observation density,
fYn|Xn(yn|xn; θ), and the initial density fX0(x0; θ) as
fX0:N,Y1:N(x0:N, y1:N; θ) =fX0(x0; θ)
×
N
Y
n=1
fXn|Xn−1(xn|xn−1; θ)fYn|Xn(yn|xn; θ).
Hence, the likelihood of the parameter vector can be written as the marginal
density for a sequence of observations Y1:N evaluated at the data y∗
1:N as
L(θ) = fY1:N(y∗
1:N; θ) =
Z
fX0:N,Y1:N(x0:N, y∗
1:N; θ)dx0:N.
(2)
The dimension of the integral in (2) depends on the number of compartments
of the Markov process and the number of observations, so this integral is
usually high-dimensional and, except for the simplest situations, cannot be
solved analytically. The method we will present in the following sections uses
the property that it is fairly easy to draw samples from the density fXn|Xn−1
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
6
rather than evaluating the function.
Because the distribution fX0 of the
initial state of the Markov process is usually not known, one practical way
to deal with this is to ﬁx the initial values of the system at some reasonable
values or, treat them as parameters we would like to estimate, see Section
1.6 for further discussion.
1.3.2
