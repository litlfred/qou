---
doc_id: maximal-hoermander-q-var-revised-v03
doc_title: "q-variational Hörmander functional calculus and Schrödinger and wave maximal estimates"
section_id: sec-008-pointwise-continuity-of-time-paths-for-abstract
section_title: "Pointwise continuity of time paths for abstract Schrödinger and wave equations"
section_number: null
pages: 28-35
source_pdf: Maximal-Hoermander-q-Var-revised-v03.pdf
source_sha256: 135332c04a1b3bb8
toc_source: outline
doc_brief: "q-variational Hörmander functional calculus and Schrödinger and wave maximal estimates — 12 sections: Front matter; Introduction; R-boundedness"
---
Pointwise continuity of time paths for abstract Schrödinger
and wave equations
The goal of this section is to provide an application of Corollary 5.3 to the continuity in time
t ∈R 7→u(t, x, ω) = exp(itA)f(x, ω) of the solution of the abstract Schrödinger equation
(
−i ∂
∂tu(t, x, ω)
= Axu(t, x, ω)
u(0, x, ω)
= f(x, ω).
This requires naturally the inital data f to be suﬃciently smooth, i.e. belonging to a fractional
domain space D(Aδ) of A. Note that when A = −∆on L2(Rd) (classical Schrödinger equation),
then Carleson [Car, Theorem p.24] asked for the optimal parameter δ such that f ∈Hδ(Rd) =
D(Aδ/2) implies that u(t, x) →f(x) pointwise a.e. x ∈Rd as t →0+ (which then yields by
isometry of exp(itA) on Hδ(Rd) that u(t, x) →u(t0, x) pointwise a.e. x ∈Rd as t →t0).
Carleson himself found that in the one-dimensional case, δ >
1
4 is suﬃcient and no δ <
1
8
is suﬃcient.
Du-Guth-Li [DGL] recently found that in the two-dimensional case δ >
1
3 is
suﬃcient, and Du-Zhang [DuZh] that in the d-dimensional case, δ >
d
2(d+1) is suﬃcient. That
no δ <
d
2(d+1) is admissible is in turn a recent result by Bourgain [Bou16]. In this section we
provide an abstract version how to deduce from Hörmander calculus of a 0-sectorial operator
such pointwise continuity of Schrödinger (or wave) equation paths. Lebesgue exponent is as
before in the range 1 < p < ∞. The price for our generality is that we need a higher value of δ
than for the classical free Schrödinger equation. However, our approach allows general measure
spaces Ωin place of Rd, more general operators A and works also for Lp(Y ) valued initial values,
lying in a domain of a fractional power of A. The analogous question of pointwise continuity
of the solution for the free wave equation, u(t, x) = exp(it
√
−∆)f(x) seems to be more diﬃcult
and less results appear in the literature than for the Schrödinger equation. See e.g. [RV2]. Our
approach works also for the wave equation, see e.g. Corollary 6.8 with a = 1.
In the ﬁrst main result, Theorem 6.1, we obtain continuity on (0, ∞), i.e. outside of 0. Then
we will enhance the result to continuity on R in Corollary 6.5. At the end we compare our
result to others before in the literature and thus return to the case of A being selfadjoint on
some L2 space, where the parameter δ simpliﬁes and our space D(Aδ) often becomes again a
Sobolev Hs(Rd) space.
Theorem 6.1 Let Y be a UMD lattice, 1 < p < ∞and (Ω, µ) a σ-ﬁnite measure space. Let
A = A0 ⊗IdY have a Hα
2 calculus on Lp(Y ) for some α > 1
2, and A0 generate a lattice positive
and contractive semigroup on Lp(Ω). Pick
δ > α + max
1
2,
1
type Lp(Y ) −
1
cotype Lp(Y )

+ 3
2.
Then for any f ∈D(Aδ), for a.e. (x, ω) ∈Ω× Ω′, the function
(
(0, ∞)
7−→C
t
7−→exp(itA)f(x, ω)
is continuous. Similarly, for a.e. x ∈Ω, the function
(
(0, ∞)
7−→Y
t
7−→exp(itA)f(x, ·)
is continuous.
27
The proof is divised in several steps which we address in the following lemmas. Recall the
calculus kernel DA = {φ(A)f : f ∈Lp(Y ), φ ∈C∞
c (R+)} from Lemma 2.16. We ﬁx in the
following a function ψ0 ∈C∞
c (0, ∞).
Lemma 6.2 Assume that the assumptions of Theorem 6.1 hold. The calculus kernel DA is
contained in D(Aδ) and is dense in it with respect to the norm

(1 + A)δf

Lp(Y ).
Proof : Let f ∈DA and φ ∈C∞
c (R+) such that f = φ(A)f. Then m(λ) = φ(λ)(1+λ)δ belongs
to C∞
c (R+), and thus, m(A)f belongs to Lp(Y ). But m(A)f = (1 + A)δφ(A)f = (1 + A)δf, so
f ∈D(Aδ). Moreover, according to the Convergence Lemma 2.15, if g ∈D(Aδ) and (ϕn)n∈Z is
a dyadic partition of unity of R+, fn = Pn
k=−n ϕk(A)g ∈DA and

(1 + A)δ(fn −g)

Lp(Y ) =

 
n
X
k=−n
ϕk(A) −Id
!
(1 + A)δg

Lp(Y )
→0
(n →∞).
Lemma 6.3 Assume that the assumptions of Theorem 6.1 hold. Let f ∈DA belong to the
calculus kernel. Then for a.e. (x, ω) ∈Ω× Ω′, the mapping R+ →C, t 7→exp(itA)f(x, ω)
extends to an entire holomorphic function on C. In particular, it is a continuous function.
Similarly, for a.e.
x ∈Ωthe mapping R+ →Y, t 7→exp(itA)f(x, ·) extends to an entire
function, thus continuous on R+. Finally, C × Ω× Ω′ →C, (z, x, ω) 7→exp(izA)f(x, ω) is a
measurable function.
Proof : Let φ ∈C∞
c (0, ∞) such that f = φ(A)f. The function z 7→exp(izλ)φ(λ) is holomorphic
C →Hα
2 , so the function z 7→exp(izA)φ(A) is holomorphic C →B(Lp(Y )). Thus there exists
a sequence (fn)n in Lp(Y ) such that
F(z) = exp(izA)φ(A)f =
∞
X
n=0
fnzn
(z ∈C).
By the Cauchy integral formula, for any R > 0 there exists CR < ∞such that ∥fn∥⩽CRR−n
for any n ∈N0. For N ∈N and R > 0, we consider the truncation
FN,R(z) =
∞
X
n=0
fn1|fn|⩽NR−nzn.
Then FN,R is holomorphic C →Lp(Y ), but also
z 7→FN,R(z, x, ω) =
∞
X
n=0
fn(x, ω)1|fn(x,ω)|⩽NR−nzn
is holomorphic B(0, R) →C for ﬁxed (x, ω) ∈Ω×Ω′. For n ∈N0 ﬁxed, Rn 

fn1|fn|>NR−n

Lp(Y ) =

Rnfn1|Rnfn|>N

Lp(Y ) →0 as N →∞thanks to the σ-order continuity of Lp(Y ). Moreover

Rnfn1|Rnfn|>N

Lp(Y ) ⩽Rn ∥fn∥Lp(Y ) ⩽CR is bounded for n, N ∈N0. Then we deduce

sup
z∈B(0,R−ε)
|FN,R(z) −F(z)|

Lp(Y )
⩽
∞
X
n=0

Rnfn1|fn|>NR−n

Lp(Y )
(R −ε)n
Rn
−→0
(N →∞).
28
According to a standard proof of completeness of Lp, convergence in Lp(Y ) implies pointwise
a.e. convergence of a subsequence. Thus, for a.e. (x, ω) ∈Ω× Ω′, F(z) is the uniform limit
of FNk,R. Since analyticity is preserved under uniform limits, we infer that z 7→F(z, x, ω) is
indeed analytic B(0, R −ε) →C for a.e. (x, ω). Letting R →∞then shows the claim on
analyticity. Since FN,R is clearly measurable as a function in (z, x, ω) as pointwise limit of easy
functions, also the uniform (hence pointwise) limit F is measurable as a function in (z, x, ω).
Proof of Theorem 6.1 :
Let f ∈D(Aδ) and choose g ∈DA an approximation of f as in Lemma
6.2. Assume that ψ0 ∈C∞
c (0, ∞) satisﬁes ψ0(t) = 1 for t in a neighborhood of [a, b], where
[a, b] ⊆(0, ∞) is any ﬁxed interval on which we want to prove continuity of paths. We have

lim sup
ε→0
sup
|t−t0|<ε, t0∈[a,b]
| exp(itA)f −exp(it0A)f|

Lp(Y )
⩽

lim sup
ε→0
sup
|t−t0|<ε, t0∈[a,b]
| exp(itA)(f −g)|

Lp(Y )
+

lim sup
ε→0
sup
|t−t0|<ε, t0∈[a,b]
| exp(itA)g −exp(it0A)g|

Lp(Y )
+

 sup
t0∈[a,b]
| exp(it0A)(f −g)|

Lp(Y )
.
(6.1)
For the ﬁrst expression in (6.1), we note that
lim sup
ε→0
sup
|t−t0|<ε, t0∈[a,b]
| exp(itA)(f −g)(x, ω)| ⩽
sup
t∈[a−ε,b+ε]
| exp(itA)(f −g)(x, ω)|
⩽
sup
t∈(0,∞)
|ψ0(t) exp(itA)(f −g)(x, ω)|.
Therefore,

lim sup
ε→0
sup
|t−t0|<ε, t0∈[a,b]
| exp(itA)(f −g)|

Lp(Y )
⩽

 sup
t∈(0,∞)
|ψ0(t) exp(itA)(f −g)|

Lp(Y )
Corollary5.3
≲

(1 + A)δ(f −g)

Lp(Y )
The same estimate applies for the third expression in (6.1) and shows that

 sup
t0∈[a,b]
| exp(it0A)(f −g)|

Lp(Y )
≲

(1 + A)δ(f −g)

Lp(Y ) .
Then for the second expression, Lemma 6.3 shows that, in fact
lim sup
ε→0
sup
|t−t0|<ε, t0∈[a,b]
| exp(itA)g(x, ω) −exp(it0A)g(x, ω)| = 0
29
for a.e. (x, ω) ∈Ω× Ω′. Thus the second expression vanishes. We obtain that

lim sup
ε→0
sup
|t−t0|<ε, t0∈[a,b]
| exp(itA)f −exp(it0A)f|

Lp(Y )
≲

(1 + A)δ(f −g)

Lp(Y ) .
By Lemma 6.2,

(1 + A)δ(f −g)

Lp(Y ) is ﬁnite for any g ∈DA and by density becomes arbi-
trarily small. We conclude that for a.e. (x, ω) ∈Ω× Ω′,
lim sup
ε→0
sup
|t−t0|<ε, t0∈[a,b]
| exp(itA)f(x, ω) −exp(it0A)f(x, ω)| = 0.
In other words, for a.e. (x, ω) ∈Ω× Ω′, [a, b] →C, t 7→exp(itA)f(x, ω) is continuous. Now let
a →0+ and b →∞to see that R+ →C, t 7→exp(itA)f(x, ω) is continuous.
For the second mapping, it suﬃces to redo the same proof starting with

lim sup
ε→0
sup
|t−t0|<ε, t0∈[a,b]
∥exp(itA)f(x) −exp(it0A)f(x)|∥Y

Lp(Ω)
on the l.h.s. of the estimate, and already in the ﬁrst step to use that this is majorised by

lim supε→0 sup|t−t0|<ε, t0∈[a,b] | exp(itA)f(x) −exp(it0A)f(x)|

Lp(Y ).
Remark 6.4 In the situation of Theorem 6.1, one might wonder whether for general f ∈
D(Aδ), Ω× Ω′ →C[a, b], (x, ω) 7→(t 7→exp(itA)f(x, ω)) is a priori mesurable, in particular
whether the scalar function (x, ω) 7→supt∈[a,b] | exp(itA)f(x, ω)| is measurable.
To this end, note ﬁrst that if f belongs to DA, then according to Lemma 6.3, (t, x, ω) 7→
exp(itA)f(x, ω) is measurable and also
t 7→sup
t∈[a,b]
| exp(itA)f(x, ω)| =
sup
t∈[a,b], t∈Q
| exp(itA)f(x, ω)|
is measurable, where equality follows from continuity in t. So, exp(itA)f then belongs indeed to
Lp(Y (C[a, b])). Then for general f ∈D(Aδ), we let fn ∈DA approximate f in H according to
Lemma 6.2. Then according to the proof of Theorem 6.1 as it stands,
∥t 7→exp(itA)(fn −fm)∥Lp(Y (C[a,b])) ≲∥fn −fm∥H ,
so that (exp(itA)fn)n is a Cauchy sequence in Lp(Y (C[a, b])), and possesses a limit X ∈
Lp(Y (C[a, b])). Moreover, for ﬁxed t ∈[a, b],
exp(itA)fn =

(1 + A)−δ exp(itA)

(1 + A)δfn →exp(itA)f,
since (1+A)−δ exp(itA) is a bounded operator thanks to Hörmander calculus and (1+A)δfn →
(1 + A)δf in Lp(Y ), as f ∈D(Aδ). By unicity of limit, this implies that for all t > 0 and
a.e. (x, ω) ∈Ω× Ω′: exp(itA)f(x, ω) = X(t, x, ω). Then we choose for each ﬁxed t > 0 the
representative of exp(itA)f such that it coincides with X(t, ·, ·). Thus we conclude that we can
choose for any t > 0 a representative Ω× Ω′ →C of exp(itA)f in Lp(Y ) such that for a.e.
(x, ω) ∈Ω× Ω′, the function (0, ∞) →C, t 7→exp(itA)f(x, ω) is continuous.
With the price that the initial value f lies in a fractional domain space of A of a higher
order, we can obtain a.e. continuous paths t 7→exp(itA)f(x, ω) on the whole real line and in
particular continuity in 0 as in the classical Carleson problem.
30
Corollary 6.5 Let Y be a UMD lattice, 1 < p < ∞and (Ω, µ) a σ-ﬁnite measure space. Let
A = A0 ⊗IdY have a Hα
2 calculus on Lp(Y ) for some α > 1
2, and A0 generate a lattice positive
and contractive semigroup on Lp(Ω). Pick
δ > 2α + max
1
2,
1
type Lp(Y ) −
1
cotype Lp(Y )

+ 3
2.
Then for any f ∈D(Aδ), for a.e. (x, ω) ∈Ω× Ω′, the function
(
R
7−→C
t
7−→exp(itA)f(x, ω)
is continuous. Similarly, for a.e. x ∈Ω, the function
(
R
7−→Y
t
7−→exp(itA)f(x, ·)
is continuous.
Proof : Fix some t0 > 0 and ε > 0 such that δ > ε+2α+max

1
2,
1
type Lp(Y ) −
1
cotype Lp(Y )

+ 3
2.
Put δ′ = δ −α −ε which then satisﬁes the assumption on δ in Theorem 6.1. Let
g := exp(−it0A)f = (1 + A)−(α+ε) exp(−it0A)(1 + A)α+εf.
As λ 7→(1 + λ)−(α+ε) exp(−it0λ) belongs to Hα
2 [KrW3, Lemma 3.9 (2)] and (1 + A)α+εf
belongs to D(Aδ′), g belongs to D(Aδ′) too.
Then we infer by Theorem 6.1 that for a.e.
(x, ω), t 7→exp(itA)g(x, ω) is continous (0, ∞) →C (resp. for a.e. x, t 7→exp(itA)g(x, ·) is
continuous (0, ∞) →Y ). However, by functional calculus, exp(itA)g = exp(i(t −t0)A)f, so
that t 7→exp(itA)f(x, ω) is continuous (−t0, ∞) →C (resp. t 7→exp(itA)f(x, ·) is continuous
(−t0, ∞) →Y ) a.e. We conclude by letting t0 →∞.
In case that Lp(Ω, Y ) = L2(Ω, C) and A self-adjoint positive, Corollary 6.5 comes with
(smaller) better exponent δ = 2 + ε. At this point, we remark that e.g. for the case of the free
Schrödinger propagator and f ∈H
d
2 +ϵ(Rd), the pointwise convergence exp(it∆)f(x) →f(x)
as t →0+ follows from a simple application of Fourier-Plancherel and the Hölder inequality.
Since in Proposition 6.6 below, δ = 2 + ε does not depend on the dimension, this result does
not seem to be reducible to such easy argument.
Proposition 6.6 Let (Ω, µ) be a σ-ﬁnite measure space. Let A be a self-adjoint positive oper-
ator on L2(Ω) such that e−tA is positivity preserving for all t ⩾0 (more generally, such that
|e−tAf| ⩽St|f| where St : L2(Ω) →L2(Ω) is a positive contraction semigroup). Let δ > 2.
Then for any f ∈D(Aδ), for a.e. x ∈Ω, the function
(
R
7−→C
t
7−→exp(itA)f(x)
is continuous.
Proof : The proof goes along the same lines as that of Theorem 5.1, Corollary 5.3, Theorem
6.1 and Corollary 6.5. This time, we pick α > 1
2, since the selfadjoint calculus of A implies
Hα
2 calculus for such α (note that Hα
2 embeds into the space of bounded Borel functions on
31
[0, ∞)). Then the additional summand max

1
2,
1
type Lp(Y ) −
1
cotype Lp(Y )

in the choice of δ is
not necessary, since L2(Ω) is a Hilbert space, and thus, bounded Hα
2 calculus is equivalent to R-
bounded Hα
2 calculus (see Proposition 2.14 and the proof of Theorem 5.1). Also the additional
summand α in Corollary 6.5 is not necessary, since exp(itA) is bounded on L2(Ω) (without a
smoothing power of resolvent of A). We conclude that we can choose δ > α+0+ 3
2 = 1
2 + 3
2 = 2.
In the following let us compare Proposition 6.6 with other results in the literature on conti-
nuity of t 7→exp(itA)f(x). First note that in case A = −∆, the optimal parameter s in order
that this continuity in t = 0 holds for all f ∈Hs(Rd) is Carleson’s problem [Car, p. 24], with
solution s >
d
2(d+1). A generalization to fractional powers (−∆)a/2 of −∆was obtained in [Zh,
Theorem 1.2]. See also [ChoKo, MYZ] for related results in dimension two, and [Sj2, SjS] for
higher dimensions but sequential convergence exp(itk(−∆)a/2)f(x) →f(x) for sequences (tk)k
converging rapidly to 0+.
Proposition 6.7 [Zh, Theorem 1.2] Let a > 0, d ∈N and s > d min(1, a)/4. Let A = (−∆)a/2.
Then exp(itA)f(x) →f(x) as t →0 for a.e. x ∈Rd if f ∈Hs(Rd).
An application of Proposition 6.6 yields the following improvement in case of high dimension
(e.g. d > 8 if a ∈(0, 1)).
Corollary 6.8 Let 0 < a < 2, d ∈N and s > 2a. Let A = (−∆)a/2. Then exp(itA)f(x) →
f(x) as t →0 for a.e. x ∈Rd if f ∈Hs(Rd).
Proof
: Note that we can apply Proposition 6.6. Indeed, A generates a positive contraction
semigroup on L2(Rd) (as it is subordinated to the heat semigroup) and is self-adjoint. Our
proposition applies for f ∈D(Aδ) = D((−∆)aδ/2) = Haδ(Rd) with δ > 2 so with aδ > 2a.
In another direction, in [LW, Theorem 1.4], a.e. convergence of exp(itA)f(x) is proved with
A = P(D), where P : Rd →R is a real valued function, and P(D) is the selfadjoint Fourier
multiplier with symbol P(ξ).
Proposition 6.9 [LW, Theorem 1.4] Let m, s0 > 0 and d ∈N. Let P : Rd →R be continuous
such that |P(ξ)| ≲|ξ|m as |ξ| →∞.
Assume that for each s > s0 the following maximal
inequality holds.

 sup
0<t<1

eitP (D)f

Lp(B(0,1))
≲∥f∥Hs(Rd) ,
p ⩾1.
Then for all f ∈Hs+δ(Rd), 0 ⩽δ < m,
eitP (D)f(x) −f(x) = o(t
δ
m )
a.e. x ∈Rd as t →0+.
With somewhat diﬀerent assumptions, we obtain pointwise convergence (without o infor-
mation) for such Fourier multipliers A = P(D) in the following way. Note that the lattice
positivity assumption holds e.g. if d = 1 and P is an even function such that its restriction to
[0, ∞) is concave. For then, the Fourier transform of e−tP (ξ), which is the convolution kernel of
e−tP (D), takes positive values. The lattice positivity assumption also will hold if P is negative
deﬁnite, for then by Schoenberg’s Theorem [Schoe], e−tP (ξ) is positive deﬁnite, so by Bochner’s
theorem [Loo], its Fourier transform is a positive measure. Since ξ 7→|ξ|a is negative deﬁnite for
0 < a ⩽2, the corollary below applies e.g. if P(ξ) = Pm
k=1 αk|ξ|ak with αk ⩾0 and ak ∈(0, 2].
32
Corollary 6.10 Let P : Rd →R+ be a measurable function taking positive values and P(D) the
associated positive self-adjoint Fourier multiplier. Assume that e−tP (D) is lattice positive (more
generally, |e−tP (D)f| ⩽St|f| for some positive contraction semigroup St : L2(Rd) →L2(Rd)).
Let f ∈D(P(D)δ) with δ > 2 (e.g. if |P(ξ)| ∼= |ξ|a, then f ∈Hs(Rd) with s > 2a suﬃces).
Then
eitP (D)f(x) →f(x)
a.e. x ∈Rd as t →0+.
Proof : Apply Proposition 6.6 directly.
In a third direction, the Schrödinger equation and the Carleson problem can also be studied
on domains Ω⊆Rd. The following result has been obtained in [Zhe, (1.4)].
Proposition 6.11 [Zhe, Corollary 1.2] Let Ωbe the right half plane {(x, y) ∈R2 : x > 0}.
Let ∆D = ∂2
x + (1 + x)∂2
y together with Dirichlet boundary conditions on ∂Ω.
Let s >
1
2
and f ∈Hs
D(Ω), where the latter space is the completion of C∞
c (Ω) with respect to the norm
∥f∥2
Hs
D(Ω) = ∥f∥2
L2(Ω) +

(−∆D)
s
2 f

2
L2(Ω). Then exp(it∆D)f(x, y) →f(x, y) as t →0+ for a.e.
(x, y) ∈Ω.
We obtain the following variant of this result. Note that we are able to take quite general
open (not necessarily convex) domains Ωand second order diﬀerential operators with Dirich-
let boundary conditions, but have to take the larger exponent δ > 2, which however is still
dimension free (and thus beyond any Sobolev embedding argument for high dimensions).
Corollary 6.12 Let Ω⊆Rd be open non-empty equipped with Lebesgue measure. Let A be the
unbounded selfadjoint operator on L2(Ω) associated to the form a : H1
0(Ω) × H1
0(Ω) →C
a(u, v) =
Z
Ω
d
X
j,k=1
akj∂ku∂jvdx,
where akj = ajk : Ω→R are bounded measurable such that the principal part is elliptic. That
is, there exists a constant η > 0 such that
d
X
j,k=1
akj(x)ξjξk ⩾η|ξ|2
(ξ ∈Cn, a.e. x ∈Ω).
Let δ > 2. Then for any f ∈D(Aδ),
exp(itA)f(x) →f(x)
as t →0+ for a.e. x ∈Ω.
Proof : According to [Ouh, Corollary 4.3 p. 104], e−tA is lattice positive. Moreover, according
to [Ouh, Corollary 4.12 p. 115], e−tA is L∞contractive, so by self-adjointness L1 contractive
and by complex interpolation L2 contractive. Thus, A is positive self-adjoint, so that it suﬃces
to apply Proposition 6.6.
Note that in the same source [Ouh], one can ﬁnd more general second order operators
e.g. with lower order terms, or with other boundary conditions such as Neumann, or mixed
boundary conditions, that still satisfy the assumptions and thus the conclusion of Proposition
6.6. In other words, for such operators, Corollary 6.12 also holds.
33
