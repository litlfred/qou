---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-060-b4-diffusion-monte-carlo-algorithm
section_title: "B.4 Diffusion Monte Carlo Algorithm"
section_number: null
pages: 141-143
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
Diﬀusion Monte Carlo Algorithm
The algorithm for N-particle system as illustrated by Fig. B.1 mainly consists the
following steps (Hammond et al. (1994); Apaja (2009)).
N particles
drift
N particles
N particles
branch
N particles
drift
N particles
N particles
branch
…
N particles
drift
N particles
N particles
prepare the initial  (!) walkers/configurations  according to a reasonable distribution by VMC
Mth Step
Compaction and form the new  (") walkers(configurations)
branch
Go to the next step/generation
Figure B.1: The illustration of the parallel DMC algorithm. Each walker means a
computer core which can store the conﬁguration of the N-particle system.
Initialization For the N-particle system, ﬁrst we need to choose the short-time step
τ and M conﬁgurations (walkers) as the ﬁrst generation, let us denote the
M as M (1). We then use M(RT)2 algorithm to make this M (1) conﬁgurations
distributed according to the importance sampling wave function Ψ. In other
words, we set the initial wave function φ as the importance sampling function Ψ.
This step is carried out by the VMC procedure in which we also calculate the
Evar ≡⟨ψT |H|ψT ⟩
⟨ψT |ψT ⟩= ⟨EL⟩, and take this Evar as the trial energy ET for the ﬁrst
generation.
Drifting Then, let us begin with the ﬁrst walker in the initial M (1) conﬁgurations. In
this walker, we drift all the N particles in this walker one by one. The diﬀusion
part of the Green’s function tells us that, for the ith particle, we can drift it from
the old position xi to its possible new position yi according to
(yi)α = (xi)α + Dτ(FiQ)α + χ,
(B.49)
where χ is a Gaussian random number with zero mean value and 2Dτ as variance,
the subscript α means the x, y or z component of the ith particle. The acceptance
probability A(y, x, τ) = min[1, q(y, x, τ)] in the M(RT)2 algorithm should have
q(y, x, τ) = [ ˜Gdiﬀ(x, y, τ)|Ψ(y)|2]/[ ˜Gdiﬀ(y, x, τ)|Ψ(x)|2]. Now we use A(y, x, τ)
to judge if this move is accepted. In principle we should move all the particles
131
(not one by one) in a walker at the same time, then judge if the new walker is
accept. If the time step τ is small, the acceptance ratio of a good DMC run
should be close to 100%. In principle we should make sure the drift force is a
constant during the time step (however this condition is actually violated, and
that is why there is a linear term of time-step error in the extrapolation function).
Anything violating the short-time approximation should be well-treated.
Branching Until here, the old walker x with M (1) particles has been ‘drifted’ to the
new walker y. Now we need to do branching. Namely, we need judge how many
of the new walkers do we need, zero (means we destroy the new walker), one,
two, three or more? We judge this by ﬁrst calculating
˜GB(y, x, τ) = e−[ EL(x)+EL(y)
2
−ET ]τeﬀ,
(B.50)
and then
MB = MIN

INT[ ˜GB + RAN], 2

,
(B.51)
here RAN means a uniform random number and INT means the integer part.
Here the 2 is put by hand, we can use other values. This upper limit is to prevent
more and more walkers sinking into abnormal regions where MB is very big
which may cause incorrect distributions. If MB is 0, we destroy this walker. If
MB is 1, we keep the walker. If MB ≥2, we keep MB copies of the new walker.
Usually MB is around 1.
Ergodicity Until here, in the ﬁrst generation of M (1) walkers, we have drifted and
branched the ﬁrst walker. Now we need to drift and branch all the rest of the
walkers in the ﬁrst generation. So we do it in this stage. Once we ﬁnished this,
we go to compaction.
Compaction Now, all the M (1) walkers in the ﬁrst generation has been drifted and
branched. Some were killed, some remain, some were replicated. In this procedure
we just remove those dead walkers and form the new M (2) number of walkers
for the second generation.
Population control Once we obtain the M (2) walkers, we need to keep the number of
walkers in each generations almost the same as the initial M (1). The feedback
mechanism I use is direct shrinking.
Loop Now we have the new generation of M (2) walkers, we then go to the loop,
Drifting→Branching→Ergodicity→Compaction→Population control→Drifting,
and the number of the loops is the number of the total generations. The number
of generations is large enough such that all the excited states are removed, and
the distribution of walkers are stabilized and is Ψφ0.
Calculations After enough generations of diﬀusion for the given time step τ, we sample
⟨EL⟩from the stabilized generations. We take the average of those ⟨EL⟩and
ﬁnd its error. We then do extrapolation to obtain the ground state energy with
error bar.
132
