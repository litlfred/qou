---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems Jinho Baik∗"
section_id: sec-010-6-ring-domain
section_title: "Ring domain"
section_number: 6
pages: 8-9
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
doc_brief: "KPZ limit theorems Jinho Baik∗ — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
Consider the TASEP on the integer ring ZL = Z/LZ = {0, 1, · · · , L −1} where we identify sites L and 0.
An equivalent model is the TASEP on Z that is spatially periodic, which we may call the periodic TASEP.
We call L the size of the ring or the period of the periodic TASEP.
The number N of particles in the TASEP on the ring is preserved. We assume the step initial condition
shown in Figure 8. For the convenience of presentation, we assume that L is an even integer and N = L/2 so
that the particle density ρ = N/L = 1/2. The initial height function of the periodic TASEP is the bottom
curve in Figure 9. The other curves are the hydrodynamic limits, as time t and period L tend to inﬁnity
proportionally when t/L = 0.5n for n = 1, 2, · · · , 6.
Consider two cases, one that t →∞with L ﬁxed and the other that L →∞with t ﬁxed. If t →∞with L
ﬁxed, the periodic corner growth model becomes essentially a one-dimensional growth model, and we expect
that the height scales as t1/2 and converges to the Gaussian distribution. On the other hand, if L →∞with
t ﬁxed, then the periodic TASEP becomes the usual TASEP on Z. Thus, the height scales as t1/3 if we let
t →∞after taking L →∞. An interesting intermediate regime is when L, t →∞simultaneously such that
t = O(L3/2).
(6.1)
Since the spatial scale for KPZ limit theorems on inﬁnite spaces is t2/3, we expect that the height functions
at all positions on the ring of size L are correlated non-trivially. If (6.1) holds, we say that we are in the
relaxation time regime.
There were some results on transition probabilities and the spectral gap of the generator in the relaxation
time regime, such as [48]. However, KPZ limit theorems were obtained only recently. The paper [71], which
is a non-completely rigorous physics paper, and [9] obtained a one-point KPZ limit theorem almost at the
same time independently. This result was further extended to 2d multi-point distributions in [10,11].
Theorem 6.1 ( [10]). Consider the TASEP on a ring of size L with the step initial condition and extend it
to the periodic TASEP. Assume that L is even and ρ = N/L = 1/2 for the convenience of presentation. Set
T = L3/2.
8
For i = 1, · · · , m, let (γi, τi, hi) ∈R × R+ × R and assume that τ1 < · · · < τm. Then,
lim
T →∞P
 m
\
i=1
h(γiT 2/3, 2τiT) −τiT
−T 1/3
≤hi
	
= F pKPZ
m
(h; γ, τ)
for an m-point distribution function F pKPZ
m
described in the next section.
Like the inﬁnite space case, we expect that the height ﬁeld of the periodic models in the relaxation time
regime converges to a universal ﬁeld, which we may call the periodic KPZ ﬁxed point. The function F pKPZ
m
should be the m-point distribution of this conjectured periodic KPZ ﬁxed point with the (periodic) narrow
wedge initial condition. It is naturally periodic with respect to γi 7→γi + 1. However, unlike the KPZ ﬁxed
point, F pKPZ
m
is not invariant under the rescaling (3.1). Indeed, we conjecture that F pKPZ
m
interpolates the
KPZ ﬁxed point and one-dimensional Brownian motion. Concretely, we expect that
lim
ϵ→0 F pKPZ
m
(hϵ; γϵ, τ ϵ) = Fm(h; γ, τ)
where (hϵ
i, γϵ
i , τ ϵ
i ) = ((τiϵ)1/3hi, (τiϵ)2/3γi, τiϵ)
and Fm is the m-point distribution of the KPZ ﬁxed point, and that
lim
s→∞F pKPZ
m
(hs; γ, τ s) = Gm(h; τ)
where (hs
i, τ s) = (−sτi + s1/2π1/4
√
2
hi, sτi)
and Gm is the m-point distribution of a Brownian motion at times τ1, · · · , τm. These conjectures were proved
for m = 1 in [12], assuming γ1 = 0 for the ϵ →0 case.
Theorem 6.1 is also proved for the discrete-time TASEP on a ring [61]. However, extending the result to
other integrable models is at the moment a challenge.
7
