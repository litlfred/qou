---
doc_id: arxiv-2103.00651v1
doc_title: "On Concentration Inequalities for Vector-Valued Lipschit z Functions Dimitrios Katselis katselis@illinois.edu"
section_id: sec-003-4-example
section_title: "Example"
section_number: 4
pages: 5-9
source_pdf: 2103.00651v1.pdf
source_sha256: c5505d3e4891168e
doc_brief: "On Concentration Inequalities for Vector-Valued Lipschit z Functions Dimitrios Katselis katselis@illinois.edu — We derive two upper bounds for the probability of deviation of a vect or-valued"
---
Consider a sample X0:n−1 = {X0, X1, . . . , Xn−1} of size n drawn from an ergodic, discrete-
time, ﬁnite-state Markov chain ( Xk)k≥0 with state space E = [K] = {1, 2, . . . , K}, transition
matrix P = [P ij] and X0 ∼ ̺, where ̺ denotes the initial measure of the chain. We denote
such a Markov chain by (P , ̺) and the corresponding stationary chain by (P , π), where π is
5
the underlying invariant measure. Let the chain be r-contractive with Dobrushin coeﬃcient
r < 1. Consider the natural plug-in estimators for the stationa ry probabilities:
ˆπi(X0:n−1) = 1
n
n−1∑
k=0
/BD (Xk = i).
By the Ergodic Theorem for Markov chains Br´ emaud (2013), ˆ πi → πi, ∀i ∈ E with proba-
bility 1 as n → ∞ for any initial measure ̺.
The distance of (P , ̺) from stationarity can be quantiﬁed by the (nonstationarit y) index
Paulin (2015)
‖‖‖ ̺
π
‖‖‖
2
2,π
= Eπ
[ (d̺
dπ
)2]
=
∑
i∈E
[
̺(i)√
π(i)
] 2
, (14)
where the ﬁrst equality corresponds to the general deﬁnitio n of the index for ̺ ≪ π and
the second equality is the specialization of this deﬁnition to our setting. Furthermore,
1 ≤ ‖ ̺/π‖2,π ≤ ∞ and ‖ · ‖ 2,π is the norm induced by the inner product ⟨f, g⟩π =∑
i∈E f (i)g(i)π(i) in ℓ2(π) Levin and Peres (2017). Due to ergodicity, min i∈E π(i) > 0 and
also ‖̺/π‖2,π ≤ 1/
√
mini∈E π(i). Additionally, ‖̺/π‖2,π = 1 for ̺ = π and ‖̺/π‖2,π = ∞
if ̺ is not absolutely continuous with respect to π.
The index in (14) is useful in our context due to the following theorem Paulin (2015):
Theorem 2 Let X0:n−1 be a sample drawn from a time-homogeneous Markov chain (P, ̺)
with state space E and stationary measure π. Then for any measurable function g : En → R
and ∀ǫ > 0,
P̺ (g(X0:n−1) ≥ ǫ) ≤
‖‖‖ ̺
π
‖‖‖
2,π
√
Pπ(g(X0:n−1) ≥ ǫ),
where P̺ is the law of (P, ̺) and Pπ is the law of (P, π).
Our goal is to bound P̺(‖ˆπ − π‖p ≥ ǫ) = P̺(‖ˆπ − Eπ[ˆπ]‖p ≥ ǫ) for p ≥ 1. To tackle the
problem within the transportation method framework, we wil l use the following theorem
due to Marton Marton (1996) adapted to our setting:
Theorem 3 Consider a Markov chain (Xk)k≥0 with a ﬁnite state space X , transition ma-
trix P = [Pij] and Dobrushin coeﬃcient r < 1. For x0:n−1, ˜x0:n−1 ∈ X n let ˜d1,X n(x0:n−1, ˜x0:n−1) =∑ n−1
k=0
/BD (xk ⁄= ˜xk). Then,
W1 (µ, ν) ≤
[ n
2(1 − r)2 D(µ‖ν)
] 1/2
,
where ν = P̺ is the measure on (X = X n, dX = ˜d1,X n) due to the Markov chain starting at
some arbitrary initial measure ̺ and µ is any measure on (X, dX).
We now compare diﬀerent approaches for bounding P̺(‖ˆπ − π‖p ≥ ǫ) and show that the
bound obtained in Theorem 1 gives better results than other, more direct applications of
the theorem of Bobkov and G¨ otze.
Approach 1: Direct application of the theorem of Bobkov and G¨ otze . Let f (x) =
f (x0:n−1) = ‖ˆπ(x0:n−1) − π‖p. Assume that x = x0:n−1 and ˜x = ˜x0:n−1 are two realizations
6
of the random sequence X0:n−1, which diﬀer at a single element. By employing the reverse
triangle inequality for the ℓp-norm we obtain
|f (x) − f (˜x)| ≤ ‖ ˆπ(x0:n−1) − ˆπ(˜x0:n−1)‖p
≤
p√
2
n =
p√
2
n
˜d1,En(x0:n−1, ˜x0:n−1) =
p√
2
n
n−1∑
k=0
/BD (xk ⁄= ˜xk). (15)
Clearly, (15) implies that ‖f ‖Lip =
p√
2/n for any x0:n−1, ˜x0:n−1 (not necessarily diﬀerent at a
single element). This can be easily seen by expressing ˆ π(x0:n−1) = (1 /n)∑ n−1
k=0
∑ K
i=1
/BD (xk =
i)ei, where {e1, . . . , eK } is the canonical basis in RK.
Consider the stationary chain (P , π). An application of the theorem of Bobkov and
G¨ otze (one-sided version) combined with Theorem 3 gives
Pπ(‖ˆπ(X0:n−1) − π‖p ≥ Eπ[‖ˆπ(X0:n−1) − π‖p] + ǫ) ≤ e−21−2/pnǫ2(1−r)2
, ∀ǫ > 0
or equivalently, ∀ǫ > E π[‖ˆπ(X0:n−1) − π‖p],
Pπ(‖ˆπ(X0:n−1) − π‖p ≥ ǫ) ≤ e−21−2/pn(ǫ−Eπ[‖ˆπ(X0:n−1)−π‖p])2(1−r)2
.
Theorem 2 now implies that ∀ǫ > E π[‖ˆπ(X0:n−1) − π‖p],
P̺(‖ˆπ(X0:n−1) − π‖p ≥ ǫ) ≤
‖‖‖ ̺
π
‖‖‖
2,π
e−2−2/pn(ǫ−Eπ[‖ˆπ(X0:n−1)−π‖p])2(1−r)2
. (16)
Finally, for any δ ∈ (0, 1) and any ǫ > E π[‖ˆπ(X0:n−1) − π‖p], P̺(‖ˆπ(X0:n−1) − π‖p ≥ ǫ) ≤ δ
for any n such that
n ≥
2
2
p log
(‖ ̺
π ‖2,π
δ
)
(ǫ − Eπ[‖ˆπ(X0:n−1) − π‖p])2 (1 − r)2 . (17)
Approach 2: A union bound approach
We may try to eliminate the problem of ǫ being bounded away from zero by using the
observation that any ℓp-norm is separable in the corresponding coordinates. We hav e
Pπ(‖ˆπ − π‖p ≥ ǫ) = Pπ
( K∑
i=1
|ˆπi − πi|p ≥ ǫp
)
≤
K∑
i=1
Pπ
(
|ˆπi − Eπ[ˆπi]| ≥ ǫ
p√
K
)
,
where the union bound and the fact that ˆ πi are unbiased estimators ∀i have been used. In
this case f (x) = f (x0:n−1) = ˆπi(x0:n−1), therefore
|f (x) − f (˜x)| ≤ 1
n
˜d1,En(x0:n−1, ˜x0:n−1), ∀x0:n−1, ˜x0:n−1 ∈ En.
By combining the theorem of Bobkov and G¨ otze with Theorems 2 and 3 we obtain:
P̺(‖ˆπ(X0:n−1) − π‖p ≥ ǫ) ≤
√
2K
‖‖‖ ̺
π
‖‖‖
2,π
e−K −2/pnǫ2(1−r)2
. (18)
7
Finally, for any δ ∈ (0, 1) and any ǫ > 0, P̺(‖ˆπ(X0:n−1) − π‖p ≥ ǫ) ≤ δ for any n such
that
n ≥
K
2
p log
(√
2K‖ ̺
π ‖2,π
δ
)
ǫ2(1 − r)2 . (19)
Approach 3: Application of Theorem 1
For simplicity, we will work with the ﬁrst bound in (2). Note t hat by working with both
bounds in (2) we can only obtain an improvement of the derived sample complexity.
We observe that by the usual norm equivalence constants, the deﬁnition of τp in (3) and
the hierarchy of ℓp-norms in Rk we have that τ1 ≤
√
k, τ2 = 1, τp ≤ 1 for any p > 2 and
τp1 ≤ τp2 for p1 ≥ p2. By Theorems 1, 2 and 3 we obtain that ∀ǫ > 0 and ∀ε ∈ (0, 1],
P̺(‖ˆπ(X0:n−1) − π‖p ≥ ǫ) ≤
‖‖‖ ̺
π
‖‖‖
2,π
(
1 + 2
ε
)K
2
e
− nǫ2(1−ε)2(1−r)2
2τ 2p . (20)
Therefore, for any δ ∈ (0, 1), any ǫ > 0 and any ε ∈ (0, 1], P̺(‖ˆπ(X0:n−1) − π‖p ≥ ǫ) ≤ δ
for any n such that
n ≥ 2τ 2
p
ǫ2(1 − ε)2(1 − r)2
[ K
2 log
(
1 + 2
ε
)
+ log
(‖‖‖ ̺
π
‖‖‖
2,π
)
+ log
(1
δ
)]
. (21)
Sample Complexity Comparisons
We ﬁrst note that ‖̺/π‖2,π ≤ 1/
√
mini∈E π(i) and often min i∈E π(i) ≍ 1/Km for some
m ≥ 1. For a rough complexity comparison between (17) and (21) co nsider for simplicity
the special case of i.i.d. random variables and p = 1. In this setting, we correspondingly
work with Pπ(·) only (only Pπ(·) is meaningful). It turns out that Eπ[‖ˆπ − π‖1] ≲ K/√n.
Then, (17) and (21) are orderwise the same, but without the pr oblem of ǫ being bounded
away from zero in (21). Further, (21) is better by a logarithmic in K factor over (19)
for p ∈ {1, 2}. For chains such that min i∈E π(i) ≍ 1/eK , (21) is better by a K factor over
(19) for p ∈ {1, 2}. We also note that depending on the geometry of f (X), f and ν, τp may
or may not have a favorable value for a particular p. More speciﬁcally, it is possible that
the last approach is orderwise better than the union bound ap proach for some choices of p,
primarily for p ∈ {1, 2}, while it is worse for other values of p, depending on the particular
problem at hand.
Acknowledgment
This work was supported by the ONR Grant Navy N00014-19-1-25 66.
References
Sergej G Bobkov and Friedrich G¨ otze. Exponential integrab ility and transportation cost
related to logarithmic sobolev inequalities. Journal of Functional Analysis , 163(1):1–28,
1999.
St´ ephane Boucheron, G´ abor Lugosi, and Pascal Massart. Concentration inequalities: A
nonasymptotic theory of independence . Oxford university press, 2013.
8
Pierre Br´ emaud. Markov chains: Gibbs ﬁelds, Monte Carlo simulation, and queu es, vol-
ume 31. Springer Science & Business Media, 2013.
Amir Dembo and Ofer Zeitouni. Large Deviations Techniques and Applications . Springer-
Verlag, New York, 1998.
Mikhail Gromov. Metric structures for Riemannian and non-Riemannian space s. Springer
Science & Business Media, 2007.
Daniel Hsu, Sham Kakade, and Tong Zhang. A tail inequality fo r quadratic forms of
subgaussian random vectors. Electronic Communications in Probability, 17(52):1–6, 2012.
Tor Lattimore and Csaba Szepesv´ ari.Bandit algorithms. Cambridge University Press, 2020.
David A Levin and Yuval Peres. Markov chains and mixing times , volume 107. American
Mathematical Soc., 2017.
Katalin Marton. A simple proof of the blowing-up lemma (corr esp.). IEEE Transactions
on Information Theory , 32(3):445–446, 1986.
Katalin Marton. Bounding ¯d-distance by informational divergence: A method to prove
measure concentration. The Annals of Probability , 24(2):857–866, 1996.
Colin McDiarmid. Centering sequences with bounded diﬀerenc es. Combinatorics Probability
and Computing , 6(1):79–86, 1997.
Daniel Paulin. Concentration inequalities for Markov chai ns by Marton couplings and
spectral methods. Electronic Journal of Probability , 20(79):1–32, 2015.
Maxim Raginsky and Igal Sason. Concentration of measure ine qualities in information
theory, communications, and coding. arXiv:1212.4663, pages 1–180, 2014.
Fraydoun Rezakhanlou. Lectures on the large deviation principle . Lecture Notes, Math UC
Berkeley, 2015.
Ramon Van Handel. Probability in High Dimension . APC 550 Lecture Notes, Princeton
University, 2016.
Roman Vershynin. High-dimensional probability: An introduction with appli cations in data
science, volume 47. Cambridge University Press, 2018.
C´ edric Villani.Optimal transport: old and new , volume 338. Springer Science & Business
Media, 2008.
Martin J Wainwright. High-dimensional statistics: A non-asymptotic viewpoint , volume 48.
Cambridge University Press, 2019.
9
