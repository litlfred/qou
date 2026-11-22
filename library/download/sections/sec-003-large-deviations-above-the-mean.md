---
doc_id: download
doc_title: "Concentration of empirical distribution functions with applications to non-i.i.d. models"
section_id: sec-003-large-deviations-above-the-mean
section_title: "Large deviations above the mean"
section_number: null
pages: 10-14
source_pdf: Download.pdf
source_sha256: ca9639465b08d34c
toc_source: outline
doc_brief: "Concentration of empirical distribution functions with applications to non-i.i.d. models — 12 sections: Front matter; Introduction; Empirical Poincaré inequalities"
---
In addition to the upper bound on the mean of the Kantorovich–Rubinstein distance W1(Fn,F),
one may wonder how to bound large deviations of W1(Fn,F) above the mean. To this end, the
following general observation may be helpful.
Lemma 4.1. For all points x = (x1,...,xn), x′ = (x′
1,...,x′
n) in Rn, we have
W1(Fn,F ′
n) ≤1
√n∥x −x′∥,
where Fn =
δx1+···+δxn
n
, F ′
n =
δx′
1+···+δx′n
n
.
In other words, the canonical map T from Rn to the space of all probability measures on the
line, which assigns to each point an associated empirical measure, has a Lipschitz seminorm
≤1
√n with respect to the Kantorovich–Rubinstein distance. As usual, the Euclidean space Rn is
equipped with the Euclidean metric
∥x −x′∥=

|x1 −x′
1|2 + ··· + |xn −x′n|2.
Denote by Z1 the collection of all (Borel) probability measures on the real line with ﬁnite ﬁrst
moment. The Kantorovich–Rubinstein distance in Z1 may equivalently be deﬁned (cf. [16,43])
by
W1(G,G′) = inf
π

|u −u′|dπ(u,u′),
where the inﬁmum is taken over all (Borel) probability measures π on R × R with marginal
distributions G and G′. In case of empirical measures G = Fn, G′ = F ′
n, associated to the points
x,x′ ∈Rn, let π0 be the discrete measure on the pairs (xi,x′
i), 1 ≤i ≤n, with point masses 1
n.
Therefore, by Cauchy’s inequality,
W1(T x,T x′) ≤

|u −u′|dπ0(u,u′) = 1
n

i=1
|xi −x′
i| ≤1
√n

i=1
|xi −x′
i|2
1/2
.
This proves Lemma 4.1.
Thus, the map T :Rn →Z1 has the Lipschitz seminorm ∥T ∥Lip ≤
1
√n. As a consequence,
given a probability measure μ on Rn, this map transports many potential properties of μ, such
as concentration, to the space Z1, equipped with the Borel probability measure 
 = μT −1. Note
that it is supported on the set of all probability measures with at most n atoms. In particular, if μ
satisﬁes a concentration inequality of the form
1 −μ(Ah) ≤α(h),
h > 0,
(4.1)
in the class of all Borel sets A in Rn with measure μ(A) ≥1
2 (where Ah denotes an open Euclid-
ean h-neighborhood of A), then 
 satisﬁes a similar (and in fact stronger) property
1 −
(Bh) ≤α

h√n

,
h > 0,
in the class of all Borel sets B in Z1 with measure 
(B) ≥1
2 (with respect to the Kantorovich–
Rubinstein distance). In other words, an optimal so-called concentration function α = αμ in (4.1)
for the measure μ is related to the concentration function of 
 by
α
(h) ≤αμ

h√n

,
h > 0.
(4.2)
Now, in general, the concentration function has a simple functional description as
αμ(h) = supμ{g −m(g) ≥h},
where the sup is taken over all Lipschitz functions g on Rn with ∥g∥Lip ≤1 and where m(g)
stands for a median of g under μ. (Actually, this holds for abstract metric spaces.) The concen-
tration function may therefore be controlled by Poincaré-type inequalities in terms of σ 2 (the
Gromov–Milman theorem). Indeed, since the quantity g −m(g) is translation invariant, one may
assume that g has mean zero. By Lemma 2.2 with t = 1, we get μ{g ≤−σh} ≤3e−h < 1
2, pro-
vided that h > log6, which means that any median of g satisﬁes m(g) ≥−σ log6. Therefore,
again by Lemma 2.2, for any h > log6,
μ{g −m(g) ≥σh} ≤μ{g ≥σ(h −log6)} ≤3 · 6 · e−h
so that
αμ(σh) ≤18e−h.
(4.3)
The latter also automatically holds in the interval 0 ≤h ≤log6. In fact, by a more careful appli-
cation of the Poincaré-type inequality, the concentration bound (4.3) may be further improved to
αμ(σh) ≤Ce−2h (see [3]), but this is not crucial for our purposes.
Thus, combining (4.2) with (4.3), we may conclude that under PI(σ 2),
α
(h) ≤18e−h√n/σ,
h > 0.
Now, in the setting of Theorem 1.1, consider on Z1 the distance function g(H) = W1(H,F).
It is Lipschitz (with Lipschitz seminorm 1) and has the mean E
g = EμW1(Fn,F) ≤a, where
a = Cσ( A+logn
n
)1/3. Hence, m(g) ≤2a under the measure 
 and for any h > 0,

{g ≥2a + h} ≤
{g −m(g) ≥h} ≤α
(h) ≤18e−h√n/σ.
We can summarize as follows.
Proposition 4.2. If a random vector (X1,...,Xn) in Rn, n ≥2, has distribution satisfying a
Poincaré-type inequality with constant σ 2, then, for all h > 0,
P

W1(Fn,F) ≥Cσ
A + logn
n
1/3
+ h
	
≤Ce−h√n/σ,
(4.4)
where A = 1
σ maxi,j |EXi −EXj| and where C is an absolute constant.
Bounds such as (4.4) may be used to prove that the convergence holds almost surely at a certain
rate. Here is a simple example, corresponding to non-varying values of the Poincaré constants.
(One should properly modify the conclusion when applying this to the matrix scheme; see Sec-
tion 7.) Let (Xn)n≥1 be a random sequence such that for each n, (X1,...,Xn) has distribution
on Rn satisfying PI(σ 2) with some common σ.
Corollary 4.3. If maxi,j≤n |EXi −EXj| = O(logn), then W1(Fn,F) = O( logn
n )1/3 with proba-
bility 1.
Note, however, that in the scheme of sequences such as in Corollary 4.3, the mean distribution
function F = EFn might also depend on n.
By a similar contraction argument, the upper bound (4.4) may be sharpened, when the distribu-
tion of (X1,...,Xn) satisﬁes a logarithmic Sobolev inequality. We turn to this type of (stronger)
hypothesis in the next section.
Remarks. Let 
 be a metric space and let d = d(u,u′) be a non-negative continuous function
on the product space 
 × 
. Given Borel probability measures G and G′ on 
, the generalized
Kantorovich–Rubinstein or Wasserstein ‘distance’ with cost function d is deﬁned by
W(G,G′) = inf
π

d(u,u′)dπ(u,u′),
where the inﬁmum is taken over all probability measures π on 
 × 
 with marginal distribu-
tions G and G′. In the case of the real line 
 = R with cost function of the form d(u,u′) =
ϕ(u −u′), where ϕ is convex, this quantity has a simple description,
W(G,G′) =
 1
0
ϕ

G−1(t) −G′−1(t)

dt,
(4.5)
in terms of the inverse distribution functions G−1(t) = min{x ∈R:G(x) ≥t}; see, for example,
[13] and [37], Theorem 2.
If ϕ(u,u′) = |u −u′|, then we also have the L1-representation for W1(G,G′), which we use
from the very beginning as our deﬁnition. Moreover, for arbitrary discrete measures G = Fn =
(δx1 + ··· + δxn)/n and G′ = F ′
n = (δx′
1 + ··· + δx′n)/n, as in Lemma 4.1, the expression (4.5) is
reduced to
W1(Fn,F ′
n) = 1
n
n

i=1
|xi −x′
i|,
(4.6)
where we assume that x1 ≤··· ≤xn and x′
1 ≤··· ≤x′
n.
Now, for an arbitrary random vector X = (X1,...,Xn) in Rn, consider the ordered statistics
X∗
1 ≤··· ≤X∗
n. Equation (4.6) then yields
EW1(Fn,F ′
n) = 1
n
n

i=1
E|X∗
i −(X′
i)∗|,
(4.7)
where (X′
1)∗≤··· ≤(X′
n)∗are ordered statistics generated by an independent copy of X and
where F ′
n are independent copies of the (random) empirical measures Fn associated with X. By
the triangle inequality for the metric W1, we have
EW1(Fn,F ′
n) ≤EW1(Fn,F) + EW1(F,F ′
n) = 2EW1(Fn,F).
It is applied with the mean distribution function F = EFn. On the other hand, any function of the
form H →W1(G,H) is convex on the convex set Z1, so, by Jensen’s inequality, EW1(Fn,F ′
n) ≥
EW1(Fn,EF ′
n) = EW1(Fn,F). The two bounds give
EW1(Fn,F) ≤EW1(Fn,F ′
n) ≤2EW1(Fn,F).
(4.8)
By a similar argument,
E|X∗
i −EX∗
i | ≤E|X∗
i −(X′
i)∗| ≤2E|X∗
i −EX∗
i |.
(4.9)
Combining (4.8) and (4.9) and recalling (4.7), we arrive at the two-sided estimate
1
2n

i=1
E|X∗
i −EX∗
i | ≤EW1(Fn,F) ≤2
n

i=1
E|X∗
i −EX∗
i |,
which is exactly the inequality (1.4) mentioned in the Introduction. Similar two-sided estimates
also hold for other cost functions in the Wasserstein distance.
