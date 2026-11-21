---
doc_id: download
doc_title: "Concentration of empirical distribution functions with applications to non-i.i.d. models"
section_id: sec-004-empirical-log-sobolev-inequalities
section_title: "Empirical log-Sobolev inequalities"
section_number: null
pages: 14-16
source_pdf: Download.pdf
source_sha256: ca9639465b08d34c
toc_source: outline
doc_brief: "Concentration of empirical distribution functions with applications to non-i.i.d. models — 12 sections: Front matter; Introduction; Empirical Poincaré inequalities"
---
As before, let (X1,...,Xn) be a random vector in Rn with joint distribution μ. Similarly to
Proposition 2.1, now using a log-Sobolev inequality for μ, we arrive at the following ‘empirical’
log-Sobolev inequality.
Proposition 5.1. Under LSI(σ 2), for any bounded, smooth function f on R,
Entμ

f dFn
2
≤2σ 2
n

f ′2 dF.
In analogy with Poincaré-type inequalities, one may also develop reﬁned applications to the
rate of growth of moments and to large deviations of various functionals of empirical measures.
In particular, we have the following proposition.
Proposition 5.2. Under LSI(σ 2), for any smooth function f on R such that f ′ belongs to
Lp(R,dF), p ≥2,
E


f dFn −

f dF

p
≤(σ√p)p
np/2

|f ′|p dF.
(5.1)
In addition, if |f ′| ≤1, then, for all h > 0,
μ


f dFn −

f dF
 ≥h
	
≤2e−nh2/2σ 2.
(5.2)
The proof of the second bound, (5.2), which was already noticed in [24] in the context of
random matrices, follows the standard Herbst’s argument; see [29] and [6]. The ﬁrst family of
moment inequalities, (5.1), can be sharpened by one inequality on the Laplace transform, such
as
Eexp

f dFn −

f dF
	
≤Eexp
σ 2
n

|f ′|2 dFn
	
.
The proof is immediate, by [6], Theorem 1.2.
However, a major weak point in both Poincaré and log-Sobolev inequalities, including their
direct consequences, as in Proposition 5.2, is that they may not be applied to indicator and other
non-smooth functions. In particular, we cannot estimate directly at ﬁxed points the variance
Var(Fn(x)) or other similar quantities like the higher moments of |Fn(x) −F(x)|. Therefore,
we need another family of analytic inequalities. Fortunately, the so-called inﬁmum-convolution
operator and associated relations concerning arbitrary measurable functions perfectly ﬁt our pur-
poses. Moreover, some of the important relations hold true and may be controlled in terms of the
constant involved in the logarithmic Sobolev inequalities.
Let us now turn to the important concept of inﬁmum- and supremum-convolution inequalities.
They were proposed in 1991 by Maurey [33] as a functional approach to some of Talagrand’s
Concentration of empirical distribution functions 1399

concentration results concerning product measures. Given a parameter t > 0 and a real-valued
function g on R” (possibly taking the values +00), put

. 1
Qrg(x) = inf [eo + xe - iP],

1
P.g(x) = sup [eo ~ le- viP.
yeR" t

Q;g and P;g then represent, respectively, the infimum- and supremum-convolution of g with
cost function being the normalized square of the Euclidean norm in R”. By definition, one puts
Qog = Pog =8.

For basic definitions and basic properties of the infimum- and supremum-convolution opera-
tors, we refer the reader to [19] and [5], mentioning just some of them here. These operators are
dually related by the property that for any functions f and g on R", g> Pf => f < Org.
Clearly, P;(—g) = —Q;g. Thus, in many statements, it is sufficient to consider only one of these
operators. The basic semigroup property of both operators is that for any g on R” and t, s > 0,

O1458 = Q:Os8, Pr4s8 = PrPsg.

For any function g and ¢ > 0, the function P;g is always lower semicontinuous, while Q;g is
upper semicontinuous. If g is bounded, then P;g and Q;g are bounded and have finite Lipschitz
seminorms. In particular, both are differentiable almost everywhere.

Given a bounded function g and ¢ > 0, for almost all x € R”, the functions t > P;g(x) and
t > Q;g(x) are differentiable at ¢ and

aPig(x) 1
arti

9O,g8(x) _

1
IVPg@Il’, aT —5IIV Org? ae.

In other words, the operator Tg = 31VgP appears as the generator for the semigroup P,,
while —I° appears as the generator for Q;. As a result, u(x,t) = Q;g(x) represents the solu-
tion to the Hamilton-Jacobi equation au =— 5 || Vu]? with initial condition u(x, 0) = g(x).

Below, we separately formulate a principal result of [5] which relates logarithmic Sobolev
inequalities to supremum- and infimum-convolution operators.

Lemma 5.3. Let jz be a probability measure on R" satisfying LS\(o7). For any 1-integrable
Borel-measurable function g on R", we have

| Poogdu> tog [ edu (5.3)
and, equivalently,

[sue tog f e228 ay. (5.4)
Alternatively, for further applications to empirical measures, one could start from the inﬁmum-
convolution inequalities (5.3) and (5.4), taking them as the main hypothesis on the measure μ.
They take an intermediate position between Poincaré and logarithmic Sobolev inequalities. How-
ever, logarithmic Sobolev inequalities have been much better studied, with a variety of sufﬁcient
conditions having been derived.
Now, as in Section 2, we apply the relations (5.3) and (5.4) to functions g(x1,...,xn) =

f dFn, where Fn is the empirical measure deﬁned for ‘observations’ x1,...,xn. By the very
deﬁnition, for any t > 0,
Ptg(x1,...,xn) =
sup
y1,...,yn∈R

g(y1,...,yn) −1
2t
n

i=1
|xi −yi|2

= 1
n
sup
y1,...,yn∈R
n

i=1

f (yi) −
1
2t/n|xi −yi|2

=

Pt/nf dFn.
Similarly, Qtg =

Qt/nf dFn. Therefore, after integration with respect to μ and using the iden-
tity Pa(tf ) = tPtaf , we arrive at corresponding empirical supremum- and inﬁmum-convolution
inequalities, as follows.
Proposition 5.4. Under LSI(σ 2), for any F -integrable Borel-measurable function f on R and
for any t > 0,
logEet(

f dFn−

f dF) ≤t

[Ptσ 2/nf −f ]dF,
(5.5)
logEet(

f dF−

f dFn) ≤t

[f −Qtσ 2/nf ]dF.
(5.6)
Note that the second inequality may be derived from the ﬁrst by changing f to −f .
