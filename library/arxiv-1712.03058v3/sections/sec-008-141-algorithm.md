---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to"
section_id: sec-008-141-algorithm
section_title: "Algorithm"
section_number: 1.4.1
pages: 10-12
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
doc_brief: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to appear in the Handb"
---
At present this method is the only simulation-based frequentist approach that
uses the full information contained in the data. Moreover, iterated ﬁltering
methods have been able to solve likelihood-based inference problems for in-
fectious disease related questions which were computationally intractable for
available Bayesian methods (Ionides et al., 2015).
1.4.1
Algorithm
In the following we present the pseudocode for iterated ﬁltering as imple-
mented in the mif2 function in the R package pomp and explain how to draw
samples from fXn|Xn−1.
Pseudocode iterated ﬁltering (mif2) cf. Ionides et al. (2015)
Input: Simulators for fX0(x0; θ) and fXn|Xn−1(xn|xn−1; θ); evaluator for fYn|Xn(yn|xn; θ);
data y∗
1:N
Algorithmic parameters: # of iterations M; # of particles J; initial parameter swarm
{θ0
j, j = 1, . . . , J}; perturbation density hn(θ|ϕ; σ); perturbation scale σ1:M
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
10
Procedure:
1.
For m in 1:M
2.
θF,m
0,j
∼h0( · |θm−1
j
; σm) for j in 1:J
3.
XF,m
0,j
∼fX0( · ; θF,m
0,j ) for j in 1:J
4.
For n in 1:N
5.
θP,m
n,j ∼hn( · |θF,m
n−1,j, σm) for j in 1:J
6.
XP,m
n,j
∼fXn|Xn−1( · |XF,m
n−1,j; θP,m
n,j ) for j in 1:J
7.
wm
n,j = fYn|Xn(y∗
n|XP,m
n,j ; θP,m
n,j ) for j in 1:J
8.
Draw k1:J with P(kj = i) = wm
n,i
. PJ
u=1 wm
n,u
9.
θF,m
n,j = θP,m
n,kj and XF,m
n,j
= XP,m
n,kj for j in 1:J
10.
End For
11.
Set θm
j = θF,m
N,j for j in 1:J
12.
End For
Output: Final parameter swarm, {θM
j , j = 1, . . . , J}
In the algorithm the initial parameter values are perturbed (line 2) by a per-
turbation density where its standard deviation σm is a decreasing function
of m. The Markov process is initialized (line 3) as a draw from the initial
density dependent on the proposed parameter vector. What follows in lines
4 - 10 is a particle ﬁlter as described in the section above with the only dif-
ference being that the parameter vector is stochastically perturbed in every
iteration through the data. The M loop repeats the particle ﬁlter with de-
creasing perturbations and throughout the algorithm the superscripts F and
P denote ﬁltering and prediction distribution, respectively. The algorithm
returns the best guess of the parameter swarm after M iterations. In the R
package pomp the point estimate that the function mif2 returns is the mean
of the parameter swarm.
To generate realizations from fXn|Xn−1 we can use the Gillespie algorithm
(Gillespie, 1977). Given the current state of the system, the algorithm simu-
lates the waiting time of the next event and updates the number of individuals
in each compartment and the overall time is incremented accordingly. The
whole procedure is repeated until a pre-deﬁned stopping time is reached. In
the case of constant per capita transition rates, the simulation of every indi-
vidual event gives us a complete and detailed history of the process, however,
it is usually a very time-consuming task for systems with large population and
state space, because of the enormous number of events that can take place.
As a way to speed up such simulations an approximate simulation method
can be used, the so called τ-leap algorithm which is based on the Gillespie
algorithm (Gillespie, 2001). The τ-leap algorithm holds all rates constant in
a small time interval τ and simulates the numbers of events that will occur in
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
11
this interval, then updates all state variables, computes the transition rates
again and the procedure is repeated until the stopping time is reached (Er-
hard et al., 2010; King et al., 2015b). Given the total number of jumps, the
number of individuals leaving any of the states by any available route during
a time interval τ is then multinomially distributed. Note that the simulation
time step is not identical with the time scale the observation process evolves
on. Both simulation algorithms are conveniently implemented in the pomp
package as the functions gillespie.sim and euler.sim.
1.5
Iterated ﬁltering for SIR model given inci-
dence data
1.5.1
