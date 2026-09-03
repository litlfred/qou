---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to"
section_id: sec-011-153-inference
section_title: "Inference"
section_number: 1.5.3
pages: 14-17
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
doc_brief: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to appear in the Handb"
---
In the following we perform inference for the two epidemiological parameters
β and γ on a set of simulated data from the model where we apply the iter-
ated ﬁltering algorithm presented in Section 1.4.
Data We consider a closed population with N = 10 000 individuals of whom
one is initially infectious and the rest are susceptible. A realization from the
model presented above with β = 1 and γ = 0.5 for N = 50 weeks where
tn = n for n = 1, . . . , N was simulated. Figure 1.2 shows the number of
weekly reported cases where it is assumed that all cases are reported.
0
250
500
750
1000
0
10
20
30
40
50
Time (weeks)
Weekly new reported cases
Figure 1.2: Weekly number of newly reported cases over time, for a simulated
set from the POMP model with an underlying Markovian SIR transmission
model as deﬁned in Equations (13) and (15).
Implementation details We use the iterated ﬁltering algorithm as imple-
mented in the function mif2 in the R package pomp to infer the epidemic
parameters β and γ assuming the initial values and total population size
were known. We run the algorithm for M = 100 iterations and J = 500
particles. As starting values for the ﬁtting algorithm we use 10 parameter
constellations drawn uniformly from a hypercube which contains biologically
meaningful parameter values for β and γ. With this procedure we address
the potential problem of local maxima in the optimization. In general, if
all searches converge to the same MLE for starting values drawn at random
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
14
from a hypercube this increases the chances that a global maximum has been
found (King, 2017). For the perturbation of the parameters we choose a ran-
dom walk with an initial standard derivation of 0.02 for both parameters. As
cooling scheme we use geometric cooling which means that on the n-th mif2
iteration, the relative perturbation intensity is kn/50 where we chose k = 0.05.
That is, after 50 iterations the perturbation is only half of the intensity com-
pared to the ﬁrst iteration. In each iteration the variance of the random walk
is successively reduced so the log-likelihood of the perturbed model gradually
approaches the log-likelihood of the model we are interested in. However, af-
ter a ﬁnite number of iteration steps, the log-likelihoods of the two models,
the one with and the one without perturbed parameters, are not identical.
To get around this issue a particle ﬁlter evaluation of the mif2 model output
using Equation (11) is necessary. Hence, for each of the 10 mif2 outputs we
obtain we run 10 particle ﬁlters, each with 1000 particles. From the multiple
particle ﬁlter evaluation we can then calculate the average log-likelihood and
the standard error of the Monte Carlo approximation for every parameter
set. Consequently, we choose the parameter constellation of the 10 possible
with the highest average log-likelihood as the maximum likelihood estimate.
In order to quantify the associated uncertainties of the parameter estimates
based on our observations we calculate the 95 % conﬁdence intervals for each
parameter. For this we construct the proﬁle likelihood of each parameter and
apply the Monte Carlo adjusted proﬁle (MCAP) algorithm (Ionides et al.,
2017). This recently developed methodology accounts for the presence of
Monte Carlo error in the likelihood evaluation and adjusts the width of the
conﬁdence interval accordingly. This procedure might seem overly compli-
cated at ﬁrst sight because, intuitively, the parameter swarm we obtain as
an output from the iterated ﬁltering algorithm should contain some measure
of uncertainty. However, due to particle depletion, which is the situation
when only very few diﬀerent particles have signiﬁcant weight (Doucet and
Johansen, 2011), the information about the local shape of the likelihood sur-
face contained in the particles is not very reliable. The proﬁle likelihood is
much more robust in this case since it relies on multiple independent mif2
searches (King, 2017).
Results The inference results are visualized in Figures 1.3 and 1.4.
As
shown in Figure 1.3 the randomly drawn starting values for both parameters
are converging towards the true values at the same time as the likelihood
increases and the number of ﬁltering failures disappears.
Both 95% con-
ﬁdence intervals constructed from the proﬁle log-likelihoods cover the true
parameters as shown in Figure 1.4.
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
15
β
γ
loglik
nfail
0
25
50
75
100
0
25
50
75
100
0
5
10
15
0.3
0.4
0.5
0.6
0.7
-1000
-750
-500
-250
0.4
0.8
1.2
1.6
MIF2 Iteration
Figure 1.3: Diagnostic plot of the iterated ﬁltering algorithm for 100 it-
erations for simulated incidence data.
Shown is the evolution of the log-
likelihood (loglik), the number of ﬁltering failures in each mif2 iteration
(nfail) and parameter estimates for parameters β and γ per iteration for 10
trajectories with random starting values drawn from a hypercube.
-160
-158
-156
-154
0.90
0.95
1.00
1.05
1.10
1.15
β
Loglikelihood
(a) Proﬁle log-likelihood for β
-160
-158
-156
-154
0.40
0.45
0.50
0.55
0.60
γ
Loglikelihood
(b) Proﬁle log-likelihood for γ
Figure 1.4: The smoothed proﬁle likelihoods (solid curves) for both param-
eters of interest where the solid vertical lines show the true values and the
dashed vertical lines contain the corresponding MCAP 95% conﬁdence in-
terval. The quadratic approximation in a neighborhood of the maximum is
shown as the dashed curves.
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
16
1.5.4
