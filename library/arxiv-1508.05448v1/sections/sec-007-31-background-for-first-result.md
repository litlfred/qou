---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-007-31-background-for-first-result
section_title: "Background for First Result"
section_number: 3.1
pages: 36-41
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
doc_brief: "Concentration of Measure Techniques and Applications — 23 sections: Biographical Sketch; Acknowledgments; Abstract"
---
In a recent work of Chatterjee and Ledoux on concentration of measure for random
submatrices [Chatterjee and Ledoux, 2009], it is proved that for an arbitrary Hermi-
tian matrix of order n and k≤n suﬃciently large, the distribution of eigenvalues is
almost the same for any principal submatrix of order k. Their proof uses the random
transposition walk on the symmetric group Sn and concentration of measure tech-
niques. To further generalize their results, we observe that it is important to use a
Markov chain which does not change too many matrix entries all at once and whose
spectral gap is known. Instead of looking at a Markov chain on Sn, we ﬁrst consider
a Markov chain on the special orthogonal group SO(n). SO(n) is the group of n×n
orthogonal matrices with determinant 1. As a linear transformation, every element of
SO(n) is a rotation and preserves distances. We introduce Kac’s walk on SO(n) and
demonstrate that it is suﬃciently similar to the transposition Markov chain to allow
for Chatterjee and Ledoux’s results to carry over to the more general case of operator
compressions. It should be noted that a similar result has been proved by Meckes and
Meckes [Meckes and Meckes, 2011] using diﬀerent techniques. In a more recent work
[Meckes and Meckes, 2013], Meckes and Meckes have extended their techniques to
28
include several other classes of random matrices and prove almost sure convergence
of the empirical spectral measure. The purpose of this paper is to highlight the fact
that the methods of Chatterjee and Ledoux can be extended to include more general
cases, provided the Markov chain used satisﬁes appropriate conditions. To emphasize
this point, we also apply the method to get a concentration of measure result for a
compression by a matrix of Gaussians using Kac’s walk coupled to a thermostat. We
also show an application of this method applied to the length of the longest increasing
subsequence of a random walk evolving under the asymmetric exclusion process. The
results of this section can be found in [Ng and Walters, 2014].
Following the notation of Chatterjee and Ledoux, for a given Hermitian matrix A
of order n, with eigenvalues given byλ1,...,λ n, we let FA denote the empirical spec-
tral distribution function of A. This is deﬁned as
FA(x) := #{i :λi≤x}
n
3.2 Kac’s Walk on SO(n)
The following model, introduced by Kac [Kac, 1954], describes a system of particles
evolving under a random collision mechanism such that the total energy of the system
is conserved. Given a system of n particles in one dimension, the state of the system
is speciﬁed by⃗ v= (v1,...v n), the velocities of the particles. At a time step t,i andj
are chosen uniformly at random from{1,...,n } andθ is chosen uniformly at random
on (−π,π ]. The i andj correspond to a collision between particles i andj such that
the energy,
E =
n∑
k=1
v2
k
is conserved. Under this constraint, after a collision, the new velocities will be of the
form vnew
i =vi cos(θ) +vj sin(θ) and vnew
j =vj cos(θ)−vi sin(θ). For i<j , let Rij(θ)
29
be the rotation matrix given by:
Rij(θ) =


I
cos(θ) sin( θ)
I
− sin(θ) cos( θ)
I


where the cos(θ) and sin(θ) terms are in the rows and columns labeledi andj, and the
I denote identity matrices of diﬀerent sizes (possibly 0). We will use the convention
that Riiθ =I. After one step of the process, ⃗ vnew =Rij(θ)⃗ v.
In our case, we will be considering this process acting on SO(n), so instead of
vectors in Rn, our states will be given by matrices G∈ SO(n). Then we can deﬁne
the one-step Markov transition operator for Kac’s walk, Q, on continuous functions
of SO(n):
Qf(G) = 1(n
2
)
∑
i<j
∫ 2π
0
f(Rij(θ)G) 1
2πdθ (3.1)
for anyG∈SO(n), and where f is a continuous function on SO(n). Notice that this
is a slightly diﬀerent setup than we introduced in Chapter 2. Instead of a ﬁnite state
space Markov chain, we now have an inﬁnite state space. We will pause to discuss the
diﬀerences between our previous case and this case. Since our state space is inﬁnite,
we cannot deﬁne our transition probabilities using ﬁnite dimensional matrices. We
instead deﬁne a Markov transition operator on continuous functions of our space. In
the context of our earlier discussion from before,
Qf(G) = E(f(X1)|X0 =G)
In other words, Qf(G) gives us the expected value after one step of the chain, condi-
tioned on the fact that we start at G∈ SO(n). It turns out that this fully speciﬁes
30
our Markov chain. In order to generalize the methods of Chatterjee and Ledoux to
this case, we need to know the invariant distribution and the spectral gap of Kac’s
walk. This is given in the following result.
Theorem 3.2.1 ([Carlen et al., 2000; Maslen, 2003]). Kac’s walk on SO(n) is ergodic
and its invariant distribution is the uniform distribution on SO(n). Furthermore, the
spectral gap of Kac’s walk on SO(n) is n+2
2(n−1)n.
Using our Markov transition operator, we can deﬁne the Dirichlet form, Q (·,·).
As discussed in chapter 2, it is well known that for a Markov chain with spectral gap,
λ1, the Poincare inequality holds:
λ1Var(f)≤Q (f,f ).
For the Kac’s walk, we have
Q (f,f ) = 1
2
(n
2
)
∑
1≤i<j≤n
∫ 2π
0
1
2π
∫
SO(n)
(f(G)−f(Rij(θ)G))2dµn(G)dθ,
where µn is the Haar measure on SO(n) normalized so that the total measure is 1.
Let us deﬁne the triple norm:
|||f|||2
∞ = 1
2
(n
2
) sup
G∈SO(n)
∑
1≤i<j≤n
∫ 2π
0
1
2π|f(G)−f(Rij(θ)G)|2dθ. (3.2)
The following result is analogous to Theorem 3.3 from Ledoux’s Concentration of
Measure Phenomenon book [Ledoux, 2005] (discussed and proved in chapter 2) . We
reproduce the proof of the theorem here to verify that even though our situation does
not satisfy the conditions of the theorem, the exact same argument carries through
for Kac’s walk on SO(n). We omit some details here as they are the same as the
argument in chapter 2.
31
Theorem 3.2.2. Consider Kac’s walk on SO(n), and let F : SO(n)→ R be given
such that|||F|||∞≤ 1. Then, F is integrable with respect to µn, and for every r≥ 0,
µn
(
F≥
∫
Fdµn +r
)
≤ 3e−r√λ1/2
whereλ1 = n+2
2(n−1)n is the spectral gap of Kac’s walk on SO(n).
Proof. We ﬁrst demonstrate thatQ
(
eλF/2,eλF/2)
)≤ λ2|||F|||2
∞
4
∫
SO(n)eλF (G)dµn(G) by
using symmetry (see chapter 2 for details).
Q
(
eλF/2,eλF/2)
= 1
2
(n
2
)
∑
1≤i<j≤n
∫ 2π
0
1
2π
∫
SO(n)
(
eλF (G)−eλF (Rij(θ)G))2
dµn(G)dθ
= 1(n
2
)
∑
1≤i<j≤n
∫ 2π
0
1
2π
∫
F (G)>F (Rij(θ)G)
(
eλF (G)−eλF (Rij(θ)G))2
dµn(G)dθ
≤ λ2
4
1
2
(n
2
)
∑
1≤i<j≤n
∫ 2π
0
1
2π
∫
SO(n)
(F (G)−F (Rij(θ)G))2eλF (G)dµn(G)dθ
= λ2
4|||F|||2
∞
∫
SO(n)
eλF (G)dµn(G)
Setting Λ(λ) =
∫
SO(n)eλF (G)dµn(G), we combine this with the Poincare inequality to
obtain
λ1Var(eλF/2) =λ1
(
Λ(λ)− Λ2
(λ
2
))
≤Q
(
eλF/2,eλF/2)
≤ λ2
4|||F|||2
∞Λ(λ).
Incorporating the assumption|||F|||∞≤ 1 yields
Λ(λ)≤ 1
1− λ2
4λ1
Λ2(λ/2).
Iterating the inequality n times gives
Λ(λ)≤
n−1∏
k=0
(
1
1− λ2
4k+1λ1
)2k
Λ2n
(λ/2n).
32
Since Λ(λ) = 1 +o(λ), we see that Λ 2n
(λ/2n)→ 1 as n→∞ . This gives the upper
bound
Λ(λ)≤
∞∏
k=0
(
1
1− λ2
4k+1λ1
)2k
.
By plugging in λ =√λ1, using the crude estimate ∏∞
k=0
(
1
1− 1
4k+1
)2k
< 3, and apply-
ing Chebyshev’s inequality (similarly to as in chapter 2), we obtain the result.
