---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION"
section_id: sec-004-24-main-probabilistic-theorems
section_title: "Main probabilistic theorems"
section_number: 2.4
pages: 7-11
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION — We study a class of commuting Markov kernels whose simplest element describes the movement ofk particles on a discrete"
---
2.1, we can consider the convolution µ = µ1∗µ2∗...µ m of an arbitrary number of h-probability
measures and its image by the map ξn. As already shown in [18, 50] in the independent and
identically distributed case, we expect that there exists γ >0 depending on some second moments
of (µi)1≤i≤m such that µ is close to the eigenvalue distribution of a unitary Brownian motion at
time γm
n2 as n goes to inﬁnity and under the appropriate scaling. Note that we need some care to
properly deﬁne the unitary Brownian motion, since there is a two-parameters family of bi-invariant
Brownian motions on U(k) because of the semisimple decomposition U(k)≃SU (k)×U(1).
2.4.1. Unitary Dyson Brownian motion. Recall that the n2-dimensional Lie algebra gU(k) ofU(k),
which is the tangent space of the manifold U(k) at the identity, admits the decomposition
gU(k) = gSU (k)⊕ gU(1),
where gSU (k) is the Lie algebra of SU (k) and gU(1) =iR is the Lie algebra of U(1). Each previous
simple Lie algebra respectively admits a natural scalar product called the (negative) Killing form
(see Section 4.4 for an explicit expression). From these scalar products, one can deﬁneBSU (k) (resp.
BU(1)) as the unique Brownian motion on gSU (k) (resp. gU(1)) whose covariance at timet = 1 is the
8 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
identity in an orthonormal basis of SU (k) (resp. U(1)) with respect to its aforementioned scalar
product.
For any α,γ ≥ 0 (with ( α,γ )⁄= 0), there exists then a unique bi-invariant Markov process
(Bα,γ(t))t≥0 onU(k) starting atId which is obtained from the Brownian motionγBSU (k)⊕αBU(1)
on gU(k) by the so-called wrapping procedure (see [39, Section 1.4], a more analytic approach is
given in Section 4.4). By taking the eigenvalues of Bα,γ(t), one gets a stochastic process Bα,γ(t) =
p (Bα,γ(t)) on Tk fort> 0. This stochastic process is actually a continuous Markov process, whose
generator is explicitly given in (22). In the particular case α =γ = 1, the process B1,1 is just the
stochastic process obtained by conditioning k Brownian motions on R/(2πZ) to never intersect by
a Doob h-transform (with the harmonic function being ⃗ u↦→|V (⃗ u)|), see [17, 30]. This process is
also called the unitary Dyson Brownian motion. The kernel K(1,1)
t (⃗ u,⃗ u′) of the Markov process
B1,1(t) has a simple determinantal formula (see [41, Proposition 1.1]) given by
K(1,1)
t (⃗ u,⃗ u′) =|V (⃗ u′)|
|V (⃗ u)| det(Pt(ui,u′
j))1≤i,j≤k,
where Pt(u,v ) =
√
k
2πt
∑
𝓁∈Z(−1)𝓁(k+1)e−k(v−u+𝓁2π)2
2t . There is a natural repulsive behavior of the
Brownian motions conditioned to not intersect, seen for example in the determinantal formula
displayed above in the case (γ,α ) = (1, 1). Hence, as long as γ >0, Bα,γ(t) stays almost surely in
T◦
k for t> 0, where T◦
k ={⃗ u∈Tk,u 1>u 2>··· >u k}.
When α = 0, the process B0,γ stays on the subdomain{⃗ u∈Tk,∑k
i=1ui = 0 [2π]}, which can be
identiﬁed with an alcove of typeAk−1. The distribution of this stochastic process can be translated
onTk by any scalarc∈ R through the action c↦→Rc, yielding a Markov process on all of Tk which
we also call B0,γ: it just corresponds to the projection p◦ B0,γ when B0,γ is started at some scalar
multiple of the identity. Then, the Markov kernel Pγ(x,·) of the extended process does admit a
density with respect to the Lebesgue measure on the subset {⃗ y∈Tk,∑k
i=1yi =∑k
i=1xi [2π]}. We
denote by KSU (k)
t (x,y ) this density.
2.4.2. Moments of a h-probability measure. Let us introduce here several quantities which will be
helpful in stating our main results. In the classical Berry-Esseen theorem, the speed of convergence
towards the Gaussian distribution of a normalized sum of independent random variables is bounded
by their third moment. We thus need to introduce similar quantities in our setting which is a bit
diﬀerent from the one on the real line.
First, since the limiting distribution will be the marginal of the aforementioned radial unitary
Brownian motion, which depends on two parameters, it is natural to expect two kinds of second
and third moments. The second particularity of this model is the cyclic nature of the position. On
R, the barycenter of k particles is straightforwardly given by the mean of their distance to zero.
On a circle however, there are several possible barycenters depending on the choice of the origin of
the circle. We chose one which is well suited for the enumerative application of the present paper
and other choices can be easily adapted for other applications with a more probabilistic ﬂavor.
Given a h-probability measure µ∈M 1(Bk,n), we denote by Iµ a random element of Bk,n whose
distribution is P(Iµ = I) = µ(I)µh(I), and by Eµ the expectation with respect to µ, namely for
f :Bk,n→ R,
Eµ(f(Iµ)) =
∑
I∈Bk,n
µh(I)µ(I)f(I).
ForI∈Bk,n, deﬁne
˜I =I−⟨I⟩
k 1k.
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 9
Remark that ˜I belongs to the (k− 1)-dimensional subspace
{
⃗ u∈ Rk,∑k
i=1ui = 0
}
. For example,
for I =I0 we have ~I0 =
(k−1
2 , k−3
2 ,..., −k−1
2
)
. Then, for µ∈M 1(Bk,n) and p≥ 1, we write
⟨µ⟩ = Eµ(⟨Iµ⟩), Var p(µ) = Eµ [(⟨Iµ⟩−⟨ µ⟩)p], ‖˜µ‖p = E
[‖‖‖~Iµ
‖‖‖
p]
.
Given a sequence m = (µi)1≤i≤m of h-probability measures on Bk,n and X one of the previously
deﬁned parameters on h-probability measures, we write
X(m) =
(
1
m
m∑
i=1
X(µi)
)
−X(I0).
Hence, for example,⟨m⟩ = 1
m
∑m
i=1⟨µi⟩−⟨ I0⟩. Finally, we set
(4) ∗ m =µ1∗µ2∗···∗ µm.
2.4.3. Berry-Esseen theorem. We can now state our ﬁrst main result, which is a precise estimate of
the convergence of a large convolution of h-probability measures (µi)1≤i≤m towards the marginal of
Bα,γ at timet for some parametersα,γ,t depending on the sequence. This Berry-Esseen like result
is given in terms of the 1-Wasserstein distance, which is both tractable and natural to compare
discrete measures to continuous ones. Recall that the 1-Wasserstein distance WE
1 on the set of
probability measures on a metric space ( E,d ) is deﬁned as
WE
1 (µ,ν ) = sup
{⏐⏐⏐⏐
∫
E
fdµ−
∫
E
fdν
⏐⏐⏐⏐, f :E→ R 1-Lipschitz
}
.
In our case, we considerTk viewed as a symmetrized torus with the natural induced metric, namely
with the distance
dTk(z,z′) = inf
σ∈Sk
d(Z/2πZ)k(z,σ·z′), z,z ′∈Tk,
where d(Z/2πZ)k is the usual metric on the torus ( Z/2πZ)k, Sk denotes the symmetric group on
1,...,k and (σ.z′)i = z′
σ(i) for 1≤ i≤ k. Remark also that the action of R on Tk extends to an
action of R onM1(Tk) given by
Rt[µ](A) =µ(Rt(A))
for t∈ R, µ∈M 1(Tk) and A measurable set of Tk, with Rt(A) ={Rt(x),x∈A}.
The quantitative convergence theorem can then be written in the following simple form (the
reader should refer to Theorem 6.1 for a more precise and more general result), where we recall
that ξn is the embedding of Bk,n in Tk deﬁned in Section 2.1 and we identify a random variable
with its distribution.
Theorem 2.4 (Berry-Esseen Theorem, simpliﬁed version) . Suppose that m = (µr)1≤r≤m is a
sequence of h-probability measures on Bk,n and set M = ‖ ˜m‖3
k3‖ ˜m‖3/2
2
. Then, with t0 = (2π)2m
n2 ,
WTk
1
(
Rm⟨m⟩
kn
[ξn (∗m)],Bα,γ (t0)
)
≤CM log(n)
n ,
where
α = Var 2(m)
2k2 , γ= k‖ ˜m‖2
2(k2− 1)
and C depends on k, t0 and α,γ , see (60).
10 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
Remark that C depends decreasingly on t0 and thus this theorem is useful only when m is of
order n2 or larger. By taking appropriate Lipschitz functions, one can deduce from the previous
results convergence estimates for probability of open sets of Tk: namely for an open set O of Tk
⏐⏐⏐P (I∗m∈O)− P
(
Bα,γ
(m
n2
)
∈O
)⏐⏐⏐≤CO
√
logn
n ,
with CO depending on O. The theorem of the next section, which provides a quantitative local
limit theorem, would improve this speed to O
( 1
n
)
in the special case where α = 0.
In comparison, the usual central limit theorem would only state that for eachO open set ofTk, we
have
⏐⏐P
(
I∗(mn)∈O
)
− P (Bα,γ (t)∈O)
⏐⏐ =o(1) as n goes to inﬁnity for some sequence of constant
tn2-uples of h-probability measures mn = (µn,...,µ n) (where µn is a ﬁxed h-probability measure
inBk,n for eachn≥ 0) with‖ ˜mn‖2, Var2(mn) converging to some constant and‖ ˜mn‖3, Var3(mn)
uniformly bounded. The fact that we only require a bound on moments of order 3 to get a central
limit theorem is not at all obvious for constrained random walks. In general, the minimal order of
moment which is required to be ﬁnite to get a central limit theorem should depend on the geometry
of the domain, and may be much higher than 3, see [19]. The fact that our central limit theorem
holds for such minimal moment assumptions (which could actually be lower to require only bound
on moments of order 2 +ϵ for someϵ> 0) is due to the high symmetry of the considered transition
kernels.
Example 2.5. For a concrete application of Theorem 2.4, let us consider the case where for
all 1≤ i≤ m, µi(I) = s
µh(I +)eI + + t
µh(I−)eI− with s +t = 1 and I+ = (k + 1,k − 1,..., 2),
I− = (k,k−1,..., 2, 0). Then, by Proposition 2.1 and the fact that the convolution algebra L2(Bk,n)
is stable by conjugation (see also Remark 2.2),
µi∗y = 1
λ
[
S(sA +tAt)
]h (y)
for all y∈L2(Bk,n), where S is the shift operator introduced in Remark 2.2. Thus, up to the shift
operator, convolution by µi corresponds to the graph of transitions of k particles on n sites, where
at each time a uniformly randomly chosen particle jumps to the right with probability t and to the
left with probability s (with the usual conditioning on non-intersection of the particles), see Figure
3. Beware that the transition probabilities of our model are diﬀerent to the ones of ASEP, since we
are conditioning the particles to not intersect instead of directly deﬁning the transition probabilities
which prevent the intersection. There is a repulsive behavior in the conditioned model which is not
present in the ASEP situation, and the dynamics of both processes are very diﬀerent.
Figure 3. Particles hopping to the left with probability t and to the right with
probabilitys, conditioned to not intersect.
Then, Theorem 2.4 shows a bound of O( logn
n ) on the 1-Wasserstein distance between the law of
the positions of the particles after rescaling and the distribution of k non-intersecting Brownian
motions on a circle conditioned to not intersect each other.
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 11
2.4.4. Local limit theorem. The second main result is a local limit theorem for the decomposition
of the h-probability measure ∗m deﬁned in (4) on the basis B0 ={eI}I∈Bk,n. As usual for local
limit theorems with discrete distributions, there may be some issues regarding the lattice generated
by the distribution of each µi. If the situation may be handled easily when all the distributions
are the same (meaning that µi = µ for all 1 ≤ i≤ k), the problem is trickier when the random
variables are not identically distributed, see [44]. To simplify, we will assume that Var 2(µi) = 0
for all 1≤i≤k. Beware that it does not implies that µi is a Dirac mass, but rather that ⟨Iµi⟩ is
constant.
Theorem 2.6 (Local limit Theorem) . Suppose that m = (µr)1≤r≤m is a sequence of h-probability
measure on Bk,n such that Var 2(m) = 0. Then, for I,I′∈Bk,n,
1
n ((∗m)∗δI) [I′] =δ⟨I′⟩=⟨I⟩+m⟨m⟩
k [n]KSU (k)
γt0
(
ξn(I′),R−m⟨m⟩
kn
[ξn (I)]
)
+O
( 1
n
)
,
whereγ = k‖m‖2
k2−1 , t0 = (2π)2m
n2 and KSU (k) is the Markov kernel deﬁned in Section 2.4.1, and O(·)
depends on k,t 0 and‖m‖i,i = 2, 3.
In the case of a sequence of h-probability measures with Var 2(m) = 0, the latter results implies
the Berry-Essen type result of the previous theorem. However, in the general case the contribution
of the ﬂuctuations of each ⟨Iµi⟩ prevents from easily giving a local limit theorem, as periodicity
patterns may appear. Since this is mainly a one-dimensional issue, one may expect that a more
general local limit theorem should hold and a Berry-Esseen theorem without the log n factor in the
error term.
