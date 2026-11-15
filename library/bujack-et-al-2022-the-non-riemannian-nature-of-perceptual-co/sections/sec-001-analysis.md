---
doc_id: bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-co
doc_title: "The non-Riemannian nature of perceptual color space"
section_id: sec-001-analysis
section_title: "Analysis"
section_number: null
pages: 4-5
source_pdf: bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-color-space.pdf
source_sha256: 2bc66a26d3901a29
toc_source: inferred
doc_brief: "The non-Riemannian nature of perceptual color space — 7 sections: Front matter; Experiment; Analysis"
---
of this type of experiment requires more assumptions to derive
a continuous scale from binary responses, compared with Likert-
scale or open-ended tasks. As a consequence, in all existing models,
additivity of small differences is inherent. Our analysis uses the
underlying theory without requiring this additivity.
Analysis
Regression to Investigate Diminishing Returns. We denote the
differences in a triad (t1, ref , t2) by di := |L∗
ref −L∗
ti|, i = 1, 2.
The existence of diminishing returns implies that as the average
difference of the triad ¯d := 1/2(d1 + d2) increases, the propor-
tion of selecting one test over the other should approach chance.
To illustrate this, consider the two triads in Fig. 4, which were
selected to have the same difference in differences Δd := ||d1| −
|d2||. If the differences were additive, as Thurstone (56) suggests,
participants should select t2 with the same frequency for both
triads.
To test for the existence of diminishing returns, we consider the
degree of consensus C,
C = |pt2 −0.5|,
[9]
where pt2 is the proportion that participants selected the lighter
test. As participants respond more at chance level, C approaches
Fig. 4.
Two triads with the same diﬀerence in diﬀerences Δd = 12.5 in
L∗units. (Upper) L∗= 45, 50, 67.5, respectively. (Bottom) L∗= 20, 50, 92.5,
respectively.
¶A detailed description of the experimental design can be found in Materials and Methods.
zero. If diminishing returns exist, the degree of consensus should
decrease with increased average difference in the triad. We can test
this using least-squares regression,
C = β0 + βΔd=5 × δΔd=5 + βΔd=10 × δΔd=10 + β¯d × ¯d.
[10]
Here, Δd is the difference in differences, and ¯d is the average
difference. We use the differences in L∗for this first analysis, so
Δd takes on three discrete values. We encode this variable as two
dummy variables using the Kronecker Δ,
δΔd=5 =
1,
Δd = 5,
0,
Δd̸ = 5.
[11]
Diminishing returns can be formalized as a negative coefficient for
the average difference, β¯d, indicating responses approaching pure
chance as the average difference in the triad increases.
Maximum
Likelihood
Estimation
to
Model
Diminishing
Returns. To transform binary responses from a 2AFC task into a
perceptual scale, certain assumptions about the underlying process
must be made. The most common analyses rely on Thurstone’s
theory of a Gaussian perceptual process (56). Here, the perception
of any stimulus, xi, is a normally distributed variable
Percept(xi) ∼N(ψi, σ2)
[12]
about its perceived strength (mean), ψi ∈R, with some discrim-
inal dispersion (SD) σ ∈R+. The perception of the difference
between stimuli xi and xj takes the form
Percept(xi −xj) ∼N(ψi −ψj, 2σ2).
[13]
This model revolutionized psychophysics because it explains how
different observers can judge stimuli differently and even how
one observer can judge them differently on different trials of an
experiment (56).
It follows that the perception of the difference of differences
in the triad is also a stochastic variable following a normal
distribution. The frequency of selecting one test should adhere to
the cumulative normal distribution where μ = 0,# as illustrated
in Fig. 3(58). The 2AFC experiment provides the proportion
of responses in which observers selected t1 as more different,
compared with the reference, than t2 [i.e., the probability
P(t1|ψref , ψt1, ψt2, σ)]. This is shown as the shaded region in
the Gaussian in Fig. 3, Lower. From that, the perceived strengths,
ψref , ψt1, and ψt2, can be estimated using the inverse of the
cumulative normal distribution, Φ, or essentially by transforming
the proportions of selecting t1 over t2 into z scores to represent
interpoint distances
P(t1|ψref , ψt1, ψt2, 4σ2)
= Φ4σ2(|ψref −ψt1| −|ψref −ψt2|).
[14]
There exist two suitable methods for this estimation. Torg-
erson (27) detailed how to solve MDS using these z scores.
This approach has been widely implemented using a variety of
algorithms to perform the matrix algebra (27, 41, 42, 55, 59).
More recently, maximum likelihood estimation (MLE) has been
used to construct a unidimensional perceptual scale from 2AFC
data using Thurstone’s theory (53, 57, 60). MLE estimates the set
of parameters, in our case ψi and σ, of a stochastic process, Eq. 14,
that is most likely to produce a given set of observations (here, the
#A more detailed derivation is in Maloney and Yang (57).
Downloaded from https://www.pnas.org by 136.47.145.179 on May 11, 2026 from IP address 136.47.145.179.
responses from the 2AFC experiment). If the likelihood function
can be differentiated with respect to the parameters, MLE can be
performed analytically. Here, however, the parameters are discrete,
so MLE must be performed numerically. Both of these approaches
(MDS and MLE) directly rely on the additivity of normally
distributed variables, which implies that smaller differences can
be added to get larger differences (i.e., the absence of diminishing
returns).
If larger differences are overestimated when summing small
differences, the sum of small differences needs to be scaled. This
can be achieved using a more flexible MLE approach that directly
models the differences Δ(i, j) = f (|ψi −ψj|) between stimuli
through a monotonic scaling function f : R →R rather than
individual stimulus strengths. To do this, we replace Eq. 14,
describing the probability that t1 is selected as closer to the
reference, by
P(t1|ψref , ψt1, ψt2, 2σ2, f )
= Φ2σ (f (|ψref −ψt1|) −f (|ψref −ψt2|))
=
1
2σ
√
2π
 f (|ψref −ψt1|)−f (|ψref −ψt2|)
−∞
e−x2
4σ2 dx.
[15]
This probability can be used as the likelihood of f given a single
response:
L(f |t1, ψref , ψt1, ψt2, 2σ2) = P(t1|ψref , ψt1, ψt2, 2σ2, f ).
[16]
The likelihood of the dataset is the joint probability of all responses
given the parameter space. In practice, the logarithm is taken for
the individual likelihoods to be summed rather than multiplied.
This log likelihood is maximized through MLE to find the optimal
parameters, here the shape of f.
The model, adapted from existing methods validated through
simulations (57, 60), does not assume the existence of additivity or
diminishing returns. Rather, the shape of f will reveal one or the
other. A concave f [i.e., f (Δψi) + f (Δψj ) > f (Δψi + Δψj )]
would indicate that diminishing returns exist. Alternatively, a
linear f [i.e., f (Δψi) + f (Δψj) = f (Δψi + Δψj )] would in-
dicate that differences are additive and that diminishing returns
do not exist.
Our implementation uses a monotonic cubic spline function
as the structure for f, which makes no assumptions about the
concavity. For comparison, we have included MLE models of a
baseline case, which linearly scales the L∗values, and a case where
the perceptual scale, g(L∗) = ψ, is estimated using a monotonic
cubic spline. When modeling the difference scaling function f,
we use the ψ-values determined by g. In addition to the spline
function for f, we can also use MLE to estimate a difference scaling
function using three previously proposed functions: logarithmic,
polynomial, and sinusoidal.
Using MLE to model a potential scaling function is an analysis
developed for responses to a 2AFC task that does not make the
assumption of additivity. As such, it is now possible to test the
existence of diminishing returns in color difference perception.
