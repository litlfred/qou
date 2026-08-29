---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to"
section_id: sec-003-121-the-likelihood-approach
section_title: "The likelihood approach"
section_number: 1.2.1
pages: 3-4
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
doc_brief: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to appear in the Handb"
---
The idea behind likelihood-based inference is the following. Suppose we have
data in the form of a sequence of N observations y∗
1:N at times t1, . . . , tN
and a model for the data f(y1:N; θ) where f is typically a probability mass
or density function parametrized by a vector of parameters denoted by θ.
In our context y∗
1:N might, for example, represent the weekly number of
newly reported cases over a certain period of time and θ might contain the
parameters of a suitable Markovian epidemic transmission model. In order
to calibrate the model to our observations we would like to ﬁnd the elements
of the parameter vector θ for which our observations are most likely under
the chosen probability model. In other words, we would like to maximize
this function f with respect to θ evaluated at the data y∗
1:N. This translates
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
3
to optimizing the function
L(θ; y∗
1:N) = f(y∗
1:N; θ).
The function L is called the likelihood function and in the following we will
suppress its dependence on the data and simply write L(θ) for convenience.
The parameter vector which maximizes this function is called the maximum
likelihood estimate (MLE) and is given as
ˆθ = arg max
θ∈Θ
L(θ),
(1)
where Θ is the parameter space containing all possible sets of parameters.
For many applications it is often more convenient to work with the log-
likelihood function
l(θ) = log L(θ).
This transformation often simpliﬁes optimization, but does not change the
location of the MLE since the natural logarithm is a monotonically increasing
function.
1.2.2
