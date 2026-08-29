---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to"
section_id: sec-010-152-formulation-of-a-pomp-model
section_title: "Formulation of a POMP model"
section_number: 1.5.2
pages: 12-14
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
doc_brief: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to appear in the Handb"
---
We will ﬁrst formulate a Markov transmission model and in a second step
relate the data to the transmission model via some observation model which
then gives us fYn|Xn.
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
12
Transmission model As transmission model we choose a stochastic
SIR model among a closed population of N individuals where X(t) =
(S(t), I(t), R(t)) denotes the number of susceptible, infectious and recov-
ered individuals at time t. Individuals are mixing homogeneously and β is
the average number of infectious contacts an infectious individual has per
time unit. Furthermore, we assume that the time an individual is infectious
is exponentially distributed with mean γ−1. We will now fromulate this in
a way which makes understanding of the code in Stocks (2017) easier. So
let {NAB(t) : t ≥0} denote a stochastic process which counts the number
of individuals which have transitioned from compartment A to compart-
ment B during the time interval [0, t) with A, B ∈X, where X = {S, I, R}
contains all model compartments. The inﬁnitesimal increment probabilities
of a jump between compartments fully specify the continuous-time Markov
process describing the transmission dynamics.
With the notation above,
∆NAB(t) = NAB(t + τ) −NAB(t) counts the number of individuals changing
compartment in an inﬁnitesimal time interval τ > 0. Thus,
P[∆NSI(t) = 1|X(t)] = βI(t)S(t)N −1τ + o(τ)
P[∆NIR(t) = 1|X(t)] = γI(t)τ + o(τ).
(12)
Moreover, the state variables and the transition probabilities (12) are related
in the following way:
∆S(t) = −∆NSI(t)
∆I(t) = ∆NSI(t) −∆NIR(t)
(13)
∆R(t) = ∆NIR(t).
Observation model We now relate the transmission model to our obser-
vations of the weekly number of newly reported cases. With the notation
above the true number of newly infected individuals accumulated in each
observation time period (tn−1, tn], n ∈{1, 2, . . . , N} is given as
H(tn) = NSI(tn) −NSI(tn−1).
(14)
To incorporate the count nature of the observations a natural assumption
is to model the actual reported cases as realizations of a Poisson-distributed
random variable with a given time-dependent mean. The number of recorded
cases Yn within a given reporting interval (tn−1, tn], is then
Yn ∼Pois (H(tn)) .
(15)
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
13
This distribution then corresponds to fYn|Xn which is easy to evaluate. One
interpretation of this choice of observation noise is to account for uncertainty
in classiﬁcation of cases, including false positives.
1.5.3
