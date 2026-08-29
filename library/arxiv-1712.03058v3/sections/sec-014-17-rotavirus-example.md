---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to"
section_id: sec-014-17-rotavirus-example
section_title: "Rotavirus example"
section_number: 1.7
pages: 21-24
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
doc_brief: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to appear in the Handb"
---
After presenting a simple toy example as a proof of concept, we now give a
short illustration of a real-world problem which accommodates some of the
complications presented in the previous section and was analyzed with iter-
ated ﬁltering. A detailed description of the model and inference results can
be found in Stocks et al. (2018).
The data which were analyzed in that paper are the weekly reported num-
ber of new laboratory-conﬁrmed rotavirus cases among children, adults and
elderly from 2001 until 2008 in Germany, scaled up by an underreporting
rate (cf. Section 1.6) as inferred and described in more detail in Weidemann
et al. (2013). Surveillance of rotavirus infection is relevant to public health
authorities because it is the primary cause for severe gastroenteritis in infants
and young children and causes signiﬁcant morbidity, mortality and ﬁnancial
burdens worldwide (Atkins et al., 2012). Individuals can get the disease more
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
21
than once but the highest reported incidence is observed in children under the
age of 5 and rises again later in life. Parameter estimation from surveillance
data is crucial if one wants to e.g. assess the eﬀect of vaccination campaigns
or other public health control measures.
In Stocks et al. (2018) the disease transmission was modeled as an age-
stratiﬁed SIRS Markov process with overdispersion in the observation (cf.
Equation (17)) as well as in the transmission model (cf. Equation (18)). As
rotavirus in Germany varies seasonally peaking around March, a forcing func-
tion (cf. Equation (1.7)) was used.
Here, we will present a simpliﬁed version of the model which ignores age-
structure and perform inference for one realization of this model; the simu-
lated case report data (black line) is shown in Figure 1.5. The initial values
were ﬁxed at the stationary distribution of the system and the waning of
immunity rate, ω > 0, was also assumed to be ﬁxed and known. With the
notation as in Section 1.5, this translates mathematically into
P[∆NS(t) = 1|X(t)] = µNτ + o(τ)
P[∆NSI(t) = 1|X(t)] = β(t)I(t)S(t)N −1τ + o(τ)
P[∆NIR(t) = 1|X(t)] = γI(t)τ + o(τ)
(19)
P[∆NRS(t) = 1|X(t)] = ωR(t)τ + o(τ)
P[∆NA(t) = 1|X(t)] = µA(t)τ + o(τ)
with A ∈{S, I, R}
where µ > 0 denotes the birth and death rate which was assumed to be con-
stant and known. Moreover, NA(t) counts the number of births and NA(t)
counts the number of deaths with A ∈X in the respective compartment up
until time t. The seasonal-forced transmission rate was deﬁned as
β(t) = β

1 + ρ cos
2π
w t + φ

ξ(t),
where ξ(t) is deﬁned as in Equation (18). The transition probabilities from
(19) are related to the state variables in the following way:
∆S(t) = ∆NS(t) −∆NSI(t) + ∆NRS(t) −∆NS(t)
∆I(t) = ∆NSI(t) −∆NIR(t) −∆NI(t)
∆R(t) = ∆NIR(t) −∆NRS(t) −∆NR(t).
With this notation the true number of newly infected individuals accumu-
lated in each observation time period (tn−1, tn], n ∈{1, 2, . . . , N} is given
as
H(tn) = NSI(tn) −NSI(tn−1).
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
22
The number of recorded cases Yn within this time period was modeled as
Yn ∼NegBin

H(tn), 1
ψ

,
compare Equation (17). In this example we inferred the susceptibility pa-
rameter β, the seasonal forcing parameters ρ and φ and the overdispersion
parameters σ and ψ, hence θ = (β, ρ, φ, σ, ψ)′. A diagnostic plot similar
to the one in Figure 1.3 (available online) shows that the iterated ﬁltering
algorithm performs well as the parameter estimates converge towards the
parameters used for simulation. Figure 1.5 shows the model evaluated at the
MLE obtained from the iterated ﬁltering. Further implementational details
for this example are available at Stocks (2017).
The aim of the analysis in Stocks et al. (2018) was to compare the impact of
diﬀerent kinds of variabilities in the transmission as well as the observation
model. The paper concluded that a model which accounts for overdispersion
in both model components (dark and light shading in Figure 1.5) is best
suited to explain the analyzed data. The strength of using iterated ﬁltering
in this context was that the method allowed for eﬃcient maximum likeli-
hood estimation for a POMP where the underlying transmission model was
stochastic. Hence, it facilitated model comparison with respect to diﬀerent
choices of variability in both model components.
0
25000
50000
75000
2001
2002
2003
2004
2005
2006
2007
2008
2009
Time (weeks)
Weekly new cases
Figure 1.5: The 95% prediction interval (light shading) for 1000 realizations
of the model for rotavirus evaluated at the maximum likelihood estimate for
the simulated case report data (solid back line) and the median (solid white
line). Furthermore, the 95 % prediction interval of these 1000 realizations
for only the transmission model is shown (darker shading).
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
23
1.8
