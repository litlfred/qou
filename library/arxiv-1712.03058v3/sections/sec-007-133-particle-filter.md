---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated ﬁltering methods for Markov process epidemic models"
section_id: sec-007-133-particle-filter
section_title: "Particle filter"
section_number: 1.3.3
pages: 7-9
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
toc_source: outline
doc_brief: "Iterated ﬁltering methods for Markov process epidemic models — Dynamic epidemic models have proven valuable for public health decision makers as they provide useful insights into the understanding"
---
1.3.3
Particle ﬁlter
One standard approach to solve a high dimensional integral as in Equation
(2) is to approximate the integral by Monte Carlo methods. However, as it
will turn out, for the model class at hand, this approach is highly ineﬃcient
in practice. Nevertheless, we will demonstrate this approach ﬁrst, in order
to introduce the reader to the problem.
Readers unfamiliar with Monte
Carlo methods might want to consult the relevant literature, e.g. Robert and
Casella (2004); Doucet et al. (2001).
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
7
The basic idea is that the likelihood in Equation (2) which can also be written
as the integral
L(θ) =
Z
N
Y
n=1
fYn|Xn(yn|xn; θ)fX0:N(x0:N; θ)dx0:N
(4)
can be approximated using the Monte Carlo principle as
L(θ) ≈1
J
J
X
j=1
N
Y
n=1
fYn|Xn(y∗
n|xn,j; θ),
where {x0:N,j, j = 1, . . . , J} is a sample drawn from fX0:N(x0:N; θ). This
means that if we generate trajectories by simulating from the Markov pro-
cess, we just have to evaluate the density of the data given the realizations
and then average in order to obtain a Monte Carlo approximation of the
likelihood.
It turns out, however, that with this approach the variability in the approx-
imation of the likelihood is very high, because the way of proposing trajec-
tories is entirely unconditional of the data. This means that in practice this
method is very ineﬃcient, because a lot of simulations are necessary in order
to obtain an estimate of the likelihood that is precise enough to be useful
for parameter estimation or model selection. The longer the time series, the
worse the problem gets (King, 2017). As it turns out, a better idea is to
parametrize the likelihood in (2) as
L(θ) =
N
Y
n=1
Ln|n−1(θ),
(5)
where Ln|n−1(θ) is the conditional likelihood, given as
Ln|n−1(θ) = fYn|Y1:n−1(y∗
n|y∗
1:n−1; θ)
=
Z
fYn|Xn(y∗
n|xn; θ)fXn|Y1:n−1(xn|y∗
1:n−1; θ)dxn,
(6)
with the convention that fX1|Y1:0 = fX1.
In the following we explain how this integral can be eﬃciently approximated
with resampling techniques which are the basis of particle ﬁlter methods.
Since Xn is a Markov chain it follows from the Chapman Kolmogorov equa-
tion that
fXn|Y1:n−1(xn|y∗
1:n−1; θ) =
(7)
Z
fXn|Xn−1(xn|xn−1; θ)fXn−1|Y1:n−1(xn−1|y∗
1:n−1; θ)dxn−1.
