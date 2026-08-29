---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems Jinho Baik∗"
section_id: sec-009-4-multi-point-distributions
section_title: "Multi-point distributions"
section_number: 4
pages: 7-8
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
doc_brief: "KPZ limit theorems Jinho Baik∗ — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
Pr¨ahofer and Spohn [70], and Johansson [55] extended the one-point distribution results of Theorem 3.1
and 3.2 to equal-time, multi-position distributions for the Poisson DLPP and the TASEP with step initial
condition, respectively. Their results were further extended to other models and initial conditions by [29–
31, 78] in 2005-2008. These results conﬁrmed, in particular, that the spatial correlations are of order T 2/3
and identiﬁed the equal-time slice of the KPZ ﬁxed point for several initial conditions. See also [40] for more
recent progress on other more diﬃcult models.
On the other hand, multi-time distributions and fully 2d multi-position distributions remained unan-
swered for a while though some short and long time correlations were studied in [42], conﬁrming that the
time scale is T. In a breakthrough paper [66] published in 2021, Mateski, Quastel, and Remenik proved
the convergence of the entire 2d height ﬁeld of the TASEP. The limiting 2d ﬁeld, the KPZ ﬁxed point, is
constructed as a Markov process with explicit transition probabilities. The result applies to general initial
conditions. The authors used the result of [29, 78] on the transition probabilities of the TASEP for gen-
eral initial conditions and proved that they converge. Dauvergne, Ortmann, and Vir´ag gave an alternative
formulation of the KPZ ﬁxed point in terms of a variational formula and proved the ﬁeld convergence for
another model, the Brownian DLPP [36]. See also [91].
In the meantime, Johansson and Rahman [58], and Liu [64] computed the limit of 2d multi-point dis-
tributions of the discrete-time PNG and the continuous-time TASEP, respectively, in 2021 and 2022. Their
results give an explicit formula of multi-point distributions for the KPZ ﬁxed point with the narrow wedge
initial condition. See Section 7 for the formula. Two-time distributions were previously computed in [56,57].
5
Half-inﬁnite space
We discussed so far models on inﬁnite spaces. For example, the TASEP was deﬁned on Z. In this and the
following sections, we consider diﬀerent domains and their eﬀects on the limit.
Consider the TASEP on the half-inﬁnite space Z+ ∪{0}. We introduce a parameter α > 0 representing
the injection rate at site 0: if the origin is empty, a new particle is injected with rate α. Once injected,
particles follow the usual TASEP rule. Suppose that we start with the empty conﬁguration. If we could
inject particles freely without being blocked by existing particles in the domain, then the height function at
the origin would satisfy h(0, T)/T →2α in probability as T →∞. However, due to the particles already in
the domain, the height grows at a slower rate, and the hydrodynamic limit at the origin turns out to be
h(0, T)
T
→max

2α(1 −α), 1
2
	
,
showing that the eﬀective injection rate is max{α(1 −α), 1/4}. The formula changes at α = 1/2.
7
Figure 8: Step initial condition on an integer ring
Figure 9: Hydrodynamic limits of periodic height
function when t = O(t)
The papers [14, 15] obtained a one-point KPZ limit theorem at the origin for the Poisson PNG and
discrete-time TASEP models. The height scales as T 1/3 for α ≥1/2 and as T 1/2 for α < 1/2. The limiting
distribution is a variation of the Tracy-Widom distribution for α > 1/2, another variation for α = 1/2,
and the Gaussian distribution for α < 1/2. The result is extended to general positions and equal-time,
multi-position distributions in [5,79] for the Poisson PNG and the discrete and continuous-time TASEP. The
one-point distribution result was also extended to other models recently. The ASEP was analyzed in [17] for
a particular value of the boundary condition. The paper [52] established one-point distribution results for
log-Gamma directed polymer, q-PushTASEP, and multiplicative stochastic heat equation, for general values
of the boundary condition. However, multi-time limit theorems are still yet to be established
6
