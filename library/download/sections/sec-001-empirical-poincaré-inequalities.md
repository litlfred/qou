---
doc_id: download
doc_title: "Concentration of empirical distribution functions with applications to non-i.i.d. models"
section_id: sec-001-empirical-poincaré-inequalities
section_title: "Empirical Poincaré inequalities"
section_number: null
pages: 5-7
source_pdf: Download.pdf
source_sha256: ca9639465b08d34c
toc_source: outline
doc_brief: "Concentration of empirical distribution functions with applications to non-i.i.d. models — 12 sections: Front matter; Introduction; Empirical Poincaré inequalities"
---
We assume that the random variables X1,...,Xn have a joint distribution μ on Rn, satisfying
the Poincaré-type inequality (1.1). For a bounded smooth function f on the real line, we apply it
to
g(x1,...,xn) = f (x1) + ··· + f (xn)
n
=

f dFn,
(2.1)
where Fn is the empirical measure, deﬁned for the ‘observations’ X1 = x1,...,Xn = xn. Since
|∇g(x1,...,xn)|2 = f ′(x1)2 + ··· + f ′(xn)2
n2
= 1
n

f ′2 dFn,
(2.2)
we obtain an integro-differential inequality, which may viewed as an empirical Poincaré-type
inequality for the measure μ.
Proposition 2.1. Under PI(σ 2), for any smooth F -integrable function f on R such that f ′
belongs to L2(R,dF), we have
E


f dFn −

f dF

2
≤σ 2
n

f ′2 dF.
(2.3)
Recall that F = EFn denotes the mean of the empirical measures. The inequality continues to
hold for all locally Lipschitz functions with the modulus of the derivative, understood in the gen-
eralized sense, that is, |f ′(x)| = limsupy→x
|f (x)−f (y)|
|x−y|
. As long as

f ′2 dF is ﬁnite,

f 2 dF is
also ﬁnite and (2.3) holds.
The latter may be extended to all Lp-spaces by applying the following general lemma.
Lemma 2.2. Under PI(σ 2), any Lipschitz function g on Rn has a ﬁnite exponential moment: if

g dμ = 0 and ∥g∥Lip ≤1, then

etg/σ dμ ≤2 + t
2 −t ,
0 < t < 2.
(2.4)
Moreover, for any locally Lipschitz g on Rn with μ-mean zero,
∥g∥p ≤σp∥∇g∥p,
p ≥2.
(2.5)
More precisely, if |∇g| is in Lp(μ), then so is g and (2.5) holds true with the standard notation
∥g∥p = (

|g|p dμ)1/p and ∥∇g∥p = (

|∇g|p dμ)1/p for Lp(μ)-norms. The property of being
locally Lipschitz means that the function g has a ﬁnite Lipschitz seminorm on every compact
subset of Rn.
In the concentration context, a variant of the ﬁrst part of the lemma was ﬁrst established by
Gromov and Milman in [23] and independently in dimension 1 by Borovkov and Utev [12].
Here, we follow [10], Proposition 4.1, to state (2.4). The second inequality, (2.5), may be derived
by similar arguments; see also [11], Theorem 4.1, for an extension to the case of Poincaré-type
inequalities with weight.
Now, for functions g =

f dFn as in (2.1), in view of (2.2), we may write
|∇g|p =
1
np/2

f ′2 dFn
p/2
≤
1
np/2

|f ′|p dFn
so that Eμ|∇g|p ≤
1
np/2

|f ′|p dF . Applying (2.5) and (2.4) with t = 1, we obtain the following
proposition.
Proposition 2.3. Under PI(σ 2), for any smooth function f on R such that f ′ belongs to
Lp(R,dF), p ≥2,
E


f dFn −

f dF

p
≤(σp)p
np/2

|f ′|p dF.
In addition, if |f ′| ≤1, for all h > 0,
μ


f dFn −

f dF
 ≥h
	
≤6e−nh/σ.
The empirical Poincaré-type inequality (2.3) can be rewritten equivalently if we integrate by
parts the ﬁrst integral as

f dFn −

f dF = −

f ′(x)(Fn(x)−F(x))dx. At this step, it is safe
to assume that f is continuously differentiable and is constant near −∞and +∞. Replacing f ′
with f , we arrive at
E


f (x)

Fn(x) −F(x)

dx

2
≤σ 2
n

f 2 dF
(2.6)
for any continuous, compactly supported function f on the line. In other words, the integral
operator Kf (x) =
 +∞
−∞K(x,y)f (y)dy with a (positive deﬁnite) kernel
K(x,y) = E

Fn(x) −F(x)

Fn(y) −F(y)

= cov(Fn(x),Fn(y))
is continuous and deﬁned on a dense subset of L2(R,dF(x)), taking values in L2(R,dx). It
has the operator norm ∥K∥≤
σ
√n, so it may be continuously extended to the space L2(R,dF)
without a change of the norm. In the following, we will use a particular case of (2.6).
Corollary 2.4. Under PI(σ 2), whenever a < b, we have
E

 b
a

Fn(x) −F(x)

dx
 ≤σ
√n

F(b) −F(a).
