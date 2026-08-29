---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to"
section_id: sec-007-14-iterated-filtering-methods
section_title: "Iterated filtering methods"
section_number: 1.4
pages: 9-10
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
doc_brief: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to appear in the Handb"
---
8
From Bayes’ theorem it also follows that
fXn|Y1:n(xn|y∗
1:n; θ) = fXn|Yn,Y1:n−1(xn|y∗
n, y∗
1:n−1; θ)
=
fYn|Xn(y∗
n|xn; θ)fXn|Y1:n−1(xn|y∗
1:n−1; θ)
R
fYn|Xn(y∗
n|xn; θ)fXn|Y1:n−1(xn|y∗
1:n−1; θ)dxn
,
(8)
where we use the fact that Yn only depends on Xn.
The distribution
fXn|Y1:n−1 is called the prediction distribution and fXn|Y1:n is called the ﬁl-
tering distribution at time tn. The idea now works as follows. Assume we
have a set of J points {xF
n−1,j}J
j=1, in the following referred to as particles,
from the ﬁltering distribution at time tn−1. Equation (7) then implies that
we obtain a sample {xP
n,j} from the prediction distribution at time tn if we
just simulate from the Markov model
xP
n,j ∼fXn|Xn−1( · |xF
n−1,j; θ)
with
j = 1, . . . , J.
(9)
Equation (8) in turn tells us that resampling from {xP
n,j} with weights pro-
portional to
ωn,j = fYn|Xn(y∗
n|xP
n,j; θ)
(10)
gives us a sample from the ﬁltering distribution at time tn. By the Monte
Carlo principle it follows from (6) that
Ln|n−1(θ) ≈1
J
J
X
j=1
fYn|Xn(y∗
n|xP
n,j; θ),
where xP
n,j is approximately drawn from fXn|Y1:n−1(xn|y∗
1:n−1; θ). In order
to obtain the full likelihood we have to iterate through the data, alternating
between simulating (9) and resampling (10) in every time step, until we reach
n = N so that
ℓ(θ) = log L(θ) =
N
X
n=1
log Ln|n−1(θ).
(11)
This method to evaluate the likelihood is called a sequential Monte Carlo al-
gorithm or particle ﬁlter (Kitagawa, 1987; Doucet et al., 2001; Arulampalam
et al., 2002). The method is implemented as the pfilter function in the
pomp package (King et al., 2016) and returns a stochastic estimate of the
likelihood which can be shown to be unbiased (Del Moral, 1996).
It can happen that at some time point a very unlikely particle is suggested.
In practice, if the conditional likelihood of this particle is below a certain
tolerance value, then that particle is considered to be uninformative. If, at
some time point, the conditional likelihood of every particle is below this cho-
sen tolerance a ﬁltering failure occurs. When a failure occurs, re-sampling
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
9
is omitted, the conditional likelihood at that time point is set equal to the
tolerance and the iteration through the data set continues, hence the time
point at which the ﬁltering failure occurred is taken to contain no informa-
tion. In general, ﬁltering failures are an implication that the model and data
might not be consistent (King, 2017).
The variability of the approximation in Equation (11) can be reduced by
increasing the number J of particles, however, the variability will usually not
vanish completely. This might create problems for standard optimizers which
assume that the likelihood is evaluated deterministically. A better choice in
this case is to use stochastic optimizers such as the iterated ﬁltering method
that we present in the section below.
1.4
Iterated ﬁltering methods
Iterated ﬁltering is a simulation-based method to ﬁnd the MLE which takes
advantage of the structure of POMP models and particle ﬁlters. It was ﬁrst
introduced by Ionides et al. (2006) and further improved in Ionides et al.
(2015). The iterated ﬁltering method uses the property that it is easy to
simulate from fXn|Xn−1 while the likelihood is not tractable directly. The ba-
sic idea is that a particle ﬁlter is applied to a model in which the parameter
vector for each particle is following a random walk. As iterations progress, the
intensity of the perturbations is successively reduced ("cooling"). It can be
