---
doc_id: download
doc_title: "Concentration of empirical distribution functions with applications to non-i.i.d. models"
section_id: sec-005-local-behavior-of-empirical-distributions
section_title: "Local behavior of empirical distributions"
section_number: null
pages: 16-20
source_pdf: Download.pdf
source_sha256: ca9639465b08d34c
toc_source: outline
doc_brief: "Concentration of empirical distribution functions with applications to non-i.i.d. models — 12 sections: Front matter; Introduction; Empirical Poincaré inequalities"
---
In this section, we develop a few direct applications of Proposition 5.4 to the behavior of em-
pirical distribution functions Fn(x) at a ﬁxed point. Such functionals are linear, that is, of the
form

f dFn, corresponding to the indicator function of the half-axis f = (−∞,x]. When f
is smooth, Proposition 5.2 tells us that the deviations of Lnf =

f dFn −

f dF are of order
σ/√n. In the general non-smooth case, the inﬁmum- and supremum-convolution operators Ptf
and Qtf behave differently for small values of t and this results in a different rate of ﬂuctuation
for Lnf .
To see this, let f = (−∞,x]. In this case, the functions Ptf and Qtf may easily be computed
explicitly, but we do not lose much by using the obvious bounds
1(−∞,x−
√
2t] ≤Qtf ≤Ptf ≤1(−∞,x+
√
2t].
Therefore, (5.5) and (5.6) yield the following proposition.
Proposition 6.1. Under LSI(σ 2), for any x ∈R and t > 0, with h =

2σ 2t
n ,
logEet(Fn(x)−F(x)) ≤t

F(x + h) −F(x)

,
(6.1)
logEet(F(x)−Fn(x)) ≤t

F(x) −F(x −h)

.
(6.2)
These estimates may be used to sharpen Corollary 3.2 and therefore to recover Theorem 1.1
(under the stronger hypothesis on the joint distribution μ, however). Indeed, for any t > 0,
Eet|Fn(x)−F(x)| ≤Eet(Fn(x)−F(x)) + Ee−t(F(x)−Fn(x)) ≤2et(F(x+h)−F(x−h)).
Taking the logarithm and applying Jensen’s inequality, we arrive at
E|Fn(x) −F(x)| ≤

F(x + h) −F(x −h)

+ log2
t
.
Now, just integrate this inequality over an arbitrary interval (a,b), a < b, and use the general
relation
 +∞
−∞(F(x + h) −F(x −h))dx ≤2h to obtain that
E
 b
a
|Fn(x) −F(x)|dx ≤2h + log2
t
(b −a) = 2

2σ 2t
n
+ log2
t
(b −a).
Optimization over t leads to an improved version of Corollary 3.2.
Corollary 6.2. Under LSI(σ 2), for all a < b,
E
 b
a
|Fn(x) −F(x)|dx ≤4
σ 2(b −a)
n
1/3
.
Note that in both cases of Proposition 6.1, for any t ∈R,
logEet(Fn(x)−F(x)) ≤|t|

F(x + h) −F(x −h)

,
h =

2σ 2|t|/n.
Hence, the local behavior of the distribution function F near a given point x turns out to be
responsible for the large deviation behavior at this point of the empirical distribution function Fn
around its mean.
For a quantitative statement, assume that F has a ﬁnite Lipschitz constant M = ∥F∥Lip, so
it is absolutely continuous with respect to Lebesgue measure on the real line and has a density,
bounded by M. It follows from (6.1), with t = (αn1/3)λ and α3 =
2
9M2σ 2 , that
Eeλξ ≤e(2/3)|λ|3/2,
λ ∈R,
where ξ = αn1/3(Fn(x) −F(x)). By Chebyshev’s inequality, for any r > 0,
μ{ξ ≥r} ≤e(2/3)λ3/2−λr = e−r3/3,
where λ = r2.
Similarly, μ{ξ ≤−r} ≤e−r3/3. Therefore, μ{αn1/3|Fn(x) −F(x)| ≥r} ≤2e−r3/3. Changing
the variable, we are ﬁnished.
Recall that we use the quantity
β = (Mσ)2/3
n1/3
.
Proposition 6.3. Assume that F has a density, bounded by a number M. Under LSI(σ 2), for
any x ∈R and r > 0,
P{|Fn(x) −F(x)| ≥βr} ≤2e−2r3/27.
(6.3)
In particular, with some absolute constant C, we have
E|Fn(x) −F(x)| ≤Cβ.
(6.4)
Note that (6.4) is consistent with the estimate of Theorem 1.1. To derive similar bounds on the
uniform (Kolmogorov) distance ∥Fn −F∥= supx |Fn(x) −F(x)| (which we discuss in the next
section), it is better to split the bound (6.3) into the two parts,
P{Fn(x) −F(x) ≥βr} ≤e−2r3/27,
(6.5)
P{F(x) −Fn(x) ≥βr} ≤e−2r3/27,
(6.6)
which were obtained in the last step of the proof of (6.3).
However, since one might not know whether F is Lipschitz or how it behaves locally, and
since one might want to approximate this measure itself by some canonical distribution G, it is
reasonable to provide a more general statement. By Proposition 6.1, for any t ≥0,
logEet(Fn(x)−G(x)) ≤t

F(x + h) −G(x)

≤t

G(x + h) −G(x)

+ t∥F −G∥
and, similarly,
logEet(G(x)−Fn(x)) ≤t

G(x) −G(x −h)

+ t∥F −G∥.
Repeating the preceding argument with the random variable
ξ = αn1/3
Fn(x) −G(x) −∥F −G∥

and then interchanging Fn and G, we get a more general version of Proposition 6.3.
Proposition 6.4. Under LSI(σ 2), for any distribution function G with ﬁnite Lipschitz seminorm
M = ∥G∥Lip, for any x ∈R and r > 0,
P{|Fn(x) −G(x)| ≥βr + ∥F −G∥} ≤2e−2r3/27,
where β = (Mσ)2/3n−1/3. In particular, up to some absolute constant C,
E|Fn(x) −G(x)| ≤Cβ + ∥F −G∥.
(6.7)
Let us stress that in all of these applications of Proposition 5.4, only the indicator functions
f = 1(−∞,x] were used. One may therefore try to get more information about deviations of the
empirical distributions Fn from the mean F by applying the basic bounds (5.5) and (5.6) with
different (non-smooth) functions f .
For example, of considerable interest is the so-called local regime, where one tries to estimate
the number
NI = card{i ≤n:Xi ∈I}
of observations inside a small interval I = [x,x + ε] and to take into account the size of the
increment ε = |I|. In case of i.i.d. observations, this may done using various tools; already, the
formula
Var(Fn(I)) = 1
nF(I)

1 −F(I)

≤F(x + ε) −F(x)
n
suggests that when F is Lipschitz, Fn(I) has small oscillations for small ε (where Fn and F are
treated as measures).
However, the inﬁmum- and supremum-convolution operators Ptf and Qtf do not provide
such information. Indeed, for the indicator function f = 1I , by (5.5), we only have, similarly to
Proposition 6.1, that
logEet(Fn(I)−F(I)) ≤t

F(x + ε + h) −F(x)

−

F(x) −F(x −h)


,
where t > 0 and h =

2σ 2t
n . Here, when h is ﬁxed and ε →0, the right-hand side is not van-
ishing, in contrast with the i.i.d. case. This also shows that standard chaining arguments, such
as Dudley’s entropy bound or more delicate majorizing measure techniques (described, e.g., in
[40]), do not properly work through the inﬁmum-convolution approach.
Nevertheless, the above estimate is still effective for ε of order h, so we can control devi-
ations of Fn(I) −F(I) relative to |I| when the intervals are not too small. This can be done
with the arguments used in the proof of Proposition 6.3 or, alternatively (although with worse
absolute constants), one can use the inequality (6.3), by applying it to the points x and x + ε.
This immediately gives that
P{|Fn(I) −F(I)| ≥2βr} ≤4e−2r3/27.
Changing variables, one may rewrite the above in terms of NI as
P{|NI −nF(I)| ≥nδ|I|} ≤4exp

−c
δ|I|
β
3	
with c = 1/112. Note that the right-hand side is small only when |I| ≫β/δ, which is of order
n−1/3 with respect to the number of observations.
This can further be generalized if we apply Proposition 6.4.
Corollary 6.5. Let G be a distribution function with density g(x) bounded by a number M.
Under LSI(σ 2), for any δ > 0 and any interval I of length |I| ≥4∥F −G∥/δ,
P
NI −n

I
g(x)dx
 ≥nδ|I|
	
≤4exp

−c
δ|I|
β
3	
,
where β = (Mσ)2/3n−1/3 and c > 0 is an absolute constant.
Hence, if
|I| ≥C
δ max{β,∥F −G∥}
and C > 0 is large, then, with high probability, we have that | NI
n −

I g(x)dx| ≤δ|I|.
