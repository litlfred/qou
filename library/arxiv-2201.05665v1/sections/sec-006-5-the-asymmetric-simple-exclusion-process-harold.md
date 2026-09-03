---
doc_id: arxiv-2201.05665v1
doc_title: "HAROLD WIDOM’S WORK IN RANDOM MATRIX THEORY"
section_id: sec-006-5-the-asymmetric-simple-exclusion-process-harold
section_title: "The asymmetric simple exclusion process. Harold Widom's papers 133,134,135"
section_number: 5
pages: 10-14
source_pdf: 2201.05665v1.pdf
source_sha256: bad7bde03d199a73
doc_brief: "HAROLD WIDOM’S WORK IN RANDOM MATRIX THEORY — This is a survey of Harold Widom’s work in random matrices."
---
The asymmetric simple exclusion process (ASEP) was introduced (in the probability lit-
erature) in Spitzer’s 1970 work [Spi]. It is a continuous time Markov process of interacting
particles on the integer lattice Z. A particle at a location x waits an exponential time with
parameter one (independently of all other particles). When that time has elapsed, the parti-
cle ﬂips a coin and with probability p attempts to jump one position to the right, and with
probability q = 1 −p attempts to jump one position to the left. These jumps are achieved
only if the destination site is unoccupied at that time. Due to the memoryless property of
the exponential distribution, this deﬁnes a Markov process. See Figure 4 for an illustration
of ASEP. Since its appearance, the ASEP model has attracted immense attention in both
the mathematical and physics communities, due to the fact that this is one of the simplest
nontrivial processes modeling nonequilibrium phenomena.
When p = 0, the model is known as TASEP, with the T standing for “totally” since
now particles only march to the left. In the paper [Joh2], building on [BDJ], an important
relation of the particle probabilities of the totally asymmetric process (TASEP, p = 0) to
the distribution function of the largest eigenvalue in the Laguerre unitary random matrix
HAROLD WIDOM’S WORK IN RANDOM MATRIX THEORY
11
Figure 3. In the ASEP, particles jump left and right according to exponential
clocks with rates q and p. All jumps are independent, and those that would lead to
collisions are excluded (the grey ×).
ensemble was discovered. Relying on tools from random matrix theory (namely, orthogonal
polynomials and Fredholm determinants) [Joh2] shows that the limiting particle distribution
in TASEP is given by the Tracy-Widom β = 2 distribution (see also [PrSp]). The decade
after [BDJ] saw incredible developments in the analysis of models like TASEP and the longest
increasing subsequence whose analysis reduces to studying asymptotics of determinants (these
models are called “determinantal”, see [Bor1]).
The extension of this result to ASEP when q̸ = p > 0 posed an enormous challenge
since ASEP, as opposed to TASEP, is not determinantal and a direct relationship to random
matrices is no longer available. The extraordinary series of papers [15, 16, 17], nevertheless
provides this extension by building on the relationship between ASEP and the Heisenberg
XXZ spin chain and exploiting the ideas of the coordinate Bethe Ansatz8. These works broke
new ground as the ﬁrst instance of a non-determinantal model for which the Tracy-Widom
distributions was demonstrated.
The starting point for Tracy and Widom’s work on ASEP is an exact formula for the
transition probability of the N-particle ASEP. For N ∈N, consider a system of N particles
on Z. For two vectors of ordered integers,⃗x = {x1 < · · · < xN}, and⃗y = {y1 < · · · < yN},
let P⃗y(⃗x; t) denote the probability that ASEP starts in state⃗y at time zero, and is in state⃗
x at time t. This function solves the “Master equation” (or Kolmogorov forward equation).
When N = 1, this equation reads
d
dtPy(x; t) = ∆p,qPy(x; t),
Py(x; 0) = 1x=y
where ∆p,q acts in the x variable as ∆p,qf(x) = pf(x −1) + qf(x + 1) −f(x). This equation
can be solved explicitly using the Fourier transform, yielding
Py(x; t) =
1
2πi
Z
ξx−y−1eϵ(ξ)tdξ,
ϵ(ξ) = pξ−1 + qξ −1
where ξ is integrated along the complex unit circle centered at 0.
When N ≥2, the Master equation becomes more complicated. When the xi are well-
spaced (at least distance two apart), the right-hand side becomes the sum of N terms, each
involving ∆p,q acting on each of the xi variables. However, when the xi neighbor each other,
certain terms need to be excluded (corresponding to the excluded jumps in ASEP). Thus,
the system becomes non-constant coeﬃcient and non-separable and so there is no a priori
reason to expect such a simple contour integral formula as above.
There is hope, however. The generator of ASEP (the operator on the right-hand side of the
Master equation) is related by a similarity transform to the Hamiltonian of the XXZ quantum
spin chain, itself a special limit of the six-vertex model. These models have a long history in
the realm of exactly solvable models in statistical mechanics, e.g. [Bax], and it was known
since [Lieb] that the coordinate Bethe ansatz can be used to diagonalize the six-vertex model
transfer matrix. For the six-vertex model and XXZ spin chain, one has to assume boundary
8This method dates back to 1931 work of Hans Bethe [Bet] in studying the Heisenberg XXX spin chain
[Hei].
12
IVAN Z. CORWIN, PERCY A. DEIFT, AND ALEXANDER R. ITS
conditions (e.g. work on a torus). However, since the generator of ASEP is stochastic, one
can work directly on the full space Z. This actually leads to a signiﬁcant simpliﬁcation to the
Bethe ansatz—there are no longer complicated Bethe equations! Instead, one has to develop
an analog of the classical Plancherel theory, now for the Bethe ansatz eigenfunctions. This
is essentially accomplished by [15] as well as [BCPS].
Figure 4. Harold Widom with his long-time collaborator, Craig Tracy at Ober-
wolfach in May 2009. Seen on the blackboard is calculations related to their work
on ASEP. Photo courtesy of the Archives of the Mathematisches Forschungsinstitut
Oberwolfach.
The following formula was proved in [15]. The N = 2 case had previously appeared in
work of R´akos and Sch¨utz [RaSc]. Provided p̸ = 0,
P⃗y(⃗x; t) =
X
σ∈SN
1
(2πi)N
Z
· · ·
Z
Aσ
N
Y
j=1
ξ
xj−yσ(j)−1
σ(j)
eϵ(ξj)tdξj.
(5.1)
Here, the sum σ ∈SN is taken over all permutations σ on N elements; the ξj variables are
complex and integrated over contours which are assumed to be circles around the origin with
radii small enough so as not to contain any poles of the Aσ term; this Aσ term is given by
the formula
Aσ =
Y
{Sαβ : {α, β} is an inversion of σ} ,
Sαβ = −p + qξαξβ −ξα
p + qξαξβ −ξβ
.
where the product is of terms Sαβ over all pairs 1 ≤α < β ≤N such that σ(α) > σ(β).
This sum over the symmetric group may seem reminiscent of the expansion formula for
determinants. In the special case when p = 1 (which is the same at taking p = 0, up to some
symmetry), there is factorization and Aσ = (−1)σ QN
j=1(1 −ξσ(j))σ(j)−j. This implies that
for p = 1,
P⃗y(⃗x; t) = det
 1
2πi
Z
(1 −ξ)j−iξxi−yj−1eϵ(ξ)tdξ
N
i,j=1
which recovers one aspect of the determinantal structure for TASEP, see [Sch].
HAROLD WIDOM’S WORK IN RANDOM MATRIX THEORY
13
Returning to (5.1), just like in random matrix eigenvalue measures, the challenge now
becomes how to extract large N asymptotics for marginals of this measure on point con-
ﬁgurations.
Random matrix methods, though informative to this aim, were not directly
applicable. The paper [15] extracted summation formulas for the marginal distribution of xm
for general N and initial data⃗y. Taking yi = i and then taking N to inﬁnity led Tracy and
Widom to study “step” initial condition for ASEP in which initially every positive integer
site is occupied. The paper [15] closed with an inﬁnite summation formula for the marginal
distribution of the location of the mth left-most particle at time t, for any m. This formula
was further manipulated in [16] into an integral transform of a Fredholm determinant. They
had discovered a hidden determinantal structure in this model—one which would then allow
them to extract asymptotics in [17]. It should be remarked that the analysis of the Fred-
holm determinant in [17] was itself quite novel, requiring a number of ingenious operator
manipulations.
Let us now record the main result of the asymptotics performed in [17]. In fact, in [18],
a more general class of initial data was considered in which sites in N are inititally occupied
according to independent Bernoulli coin ﬂips with probability ρ ∈(0, 1] of having a particle.
The case ρ = 1 recovers the step initial data.
Assume that 0 ≤p < q and put γ := q −p. Denote also σ = m/t ≤1 and deﬁne the
constants,
c1 := −1 + 2√σ,
c2 := σ−1/6
1 −√σ
2/3
.
Then [17, 18] shows that (cf. (4.3) and (4.11)),
lim
t→∞Prob


xm

t/γ

−c1t
c2t1/3
≤s

= F2(s),
when
0 < σ < ρ2,
(5.2)
and
lim
t→∞Prob


xm

t/γ

−c1t
c2t1/3
≤s

= F1(s)2,
when
σ = ρ2,
ρ < 1.
(5.3)
We emphasize again that ASEP is not a determinantal process and hence none of the usual
“integrable techniques”, such as the orthogonal polynomial approach, the Riemann-Hilbert
method, the Borodin-Okounkov formula, or the theory of integrable Fredholm operators are
readily applicable. In spite of the absence of such tools, the Tracy-Widom distributions still
arise!
Besides demonstrating that the Tracy-Widom distribution is universal for ASEP regardless
of the choice of parameters (provided p̸ = q), the work in [15, 16, 17] demonstrated that non-
determinantal models could still be solved, albeit with diﬀerent techniques.
Over the decade or so since Tracy and Widom’s initial work on ASEP, there have been a
number of developments in the ﬁeld of integrable probability in this direction. This is too vast
a subject to try to survey here, so we simply refer to a few existing surveys [ABW, Bor2, BoGo,
BoPe1, BoPe2, BoWh, Cor1, Cor2, Cor3, Cor4, OCon, QuSp, Zyg] and mention some general
topics: Kardar-Parisi-Zhang universality class, replica method, Markov duality, quantum
Toda Hamiltonian, Macdonald processes (and limits to Whittaker, Jack, Hall-Littlewood or
Schur processes), stochastic vertex models, spin q-Whittaker and Hall-Littlewood functions.
The list goes on, as does the inﬂuence of Tracy and Widom’s work on ASEP and random
matrices.
14
IVAN Z. CORWIN, PERCY A. DEIFT, AND ALEXANDER R. ITS
