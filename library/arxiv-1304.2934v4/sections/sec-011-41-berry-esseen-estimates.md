---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-011-41-berry-esseen-estimates
section_title: "Berry-Esseen estimates"
section_number: 4.1
pages: 26-29
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
Esseen estimates in the setting of mod-φ convergence.
Proposition 4.1 (Berry-Esseen expansion). We place ourselves under the assumptions of
Deﬁnition 1.1, with φ non-lattice inﬁnitely divisible law, and the strip S(c,d) that contains 0.
Denote
g(y) = 1√
2π
e−y2/2
the density of a standard Gaussian variable, and F n(x) = P[Xn≤ tnη′(0) +
√
tnη′′(0) x].
One has
Fn(x) =
∫ x
−∞
(
1 + ψ′(0)√
tnη′′(0)
y + η′′′(0)
6
√
tn(η′′(0))3 (y3− 3y)
)
g(y) dy + o
( 1√tn
)
with the o(·) uniform on R.
Proof. We use the same arguments as in the proof of [Fel71, Theorem XVI.4.1], but
adapted to the assumptions of Deﬁnition 1.1. Given an integrable function f , or more
generally a distribution, its Fourier transform is f∗(ζ) = ∫
R eiζx f (x) dx. Consider a
probability law F(x) = ∫ x
−∞ f (y) dy with vanishing expectation ( f∗)′(0) = 0; and
G(x) =∫ x
−∞ g(y) dy a m-Lipschitz function with g∗ continuously differentiable and
(g∗)′(0) = 0 ; lim
y→−∞
G(y) = 0 ; lim
y→+∞
G(y) = 1.
Then Feller’s Lemma [Fel71, Lemma XVI.3.2] states that, for anyx∈ R and any T > 0,
|F(x)− G(x)|≤ 1
π
∫ T
−T
⏐⏐⏐⏐
f∗(ζ)− g∗(ζ)
ζ
⏐⏐⏐⏐ dζ + 24m
πT .
Notice that this is true even when f is a distribution. Deﬁne the auxiliary variables
Yn = Xn− tnη′(0)√
tnη′′(0)
We shall apply Feller’s Lemma to the functions
Fn(x) = cumulative distribution function of Yn;
Gn(x) =
∫ x
−∞
(
1 + ψ′(0)√
tnη′′(0)
y + η′′′(0)
6
√
tn(η′′(0))3 (y3− 3y)
)
g(y) dy.
Note that each Gn is clearly a Lipschitz function (with a uniform Lipschitz constant,
i.e. that does not depend on n). Besides, by Lemma 2.7, (2), the Fourier transform
corresponding to the distribution function Gn is, setting z = i ζ,
g∗
n(ζ) = e
z2
2
(
1 + ψ′(0) z√
tnη′′(0) + η′′′(0) z3
6
√
tn(η′′(0))3
)
. (13)
MOD-φ CONVERGENCE, I 27
Consider now f∗
n (ζ): if z = i ζ, then
f∗
n (ζ) = E
[
e
z
(
Xn−tnη′(0)√
tnη′′ (0)
)]
= exp
(
−z
√
tn
η′′(0) η′(0)
)
× ϕn
(
z√
tnη′′(0)
)
= exp
(
tn
(
η
(
z√
tnη′′(0)
)
− η′(0) z√
tnη′′(0)
))
× ψn
(
z√
tnη′′(0)
)
But
ψn
(
z√
tnη′′(0)
)
=
(
1 + ψ′
n(0) z√
tnη′′(0) + o
( z√tn
))
=
(
1 + ψ′(0) z√
tnη′′(0) + o
( z√tn
))
where the o is uniform in n because of the local uniform convergence of the analytic
functions ψn to ψ (and hence, of ψ′
n and ψ′′
n to ψ′ and ψ). Thus
f∗
n (ζ) = exp
(
z2
2 + η′′′(0) z3
6
√
tn(η′′(0))3 +|z|2 o
( z√tn
))
×
(
1 + ψ′(0) z√
tnη′′(0) + o
( z√tn
))
= e
z2
2
(
1 + ψ′(0) z√
tnη′′(0) + η′′′(0) z3
6
√
tn(η′′(0))3 + (1 +|z|2) o
( z√tn
))
. (14)
Beware that in the previous expansions, the o(·) is
o
( z√tn
)
= |z|√tn
ε
( z√tn
)
with lim
t→0
ε(t) = 0.
In particular, z might still go to inﬁnity in this situation. To make everything clear
we will continue to use the notation ε(t) in the following. Fix 0 < δ < ∆ and take
T = ∆√tn. Comparing (13) and (14) and using Feller’s lemma, we get:
|Fn(x)− Gn(x)|≤ 1
π
∫ ∆√tn
−∆√tn
⏐⏐⏐⏐
f∗
n (ζ)− g∗
n(ζ)
ζ
⏐⏐⏐⏐ dζ + 24m
∆π√tn
≤ 1
π√tn
∫ δ√tn
−δ√tn
e− ζ2
2 (1 +|ζ|2) ε
( ζ√tn
)
dζ + 24m
∆π√tn
+ 1
πδ√tn
∫
[−∆√tn,∆√tn]\[−δ√tn,δ√tn]
| f∗
n (ζ)− g∗
n(ζ)| dζ. (15)
In the right-hand side, the ﬁrst part is of the form ε′(δ)√tn
when limδ→0 ε′(δ) = 0, while
the second part is smaller than M
∆√tn
for some constant M.
Let us show that the last integral goes to zero faster than any power of tn. Indeed,
for|ζ|∈ [δ√tn, ∆√tn],
| f∗
n (ζ)| =
⏐⏐⏐⏐⏐ϕn
(
iζ√
tnη′′(0)
)⏐⏐⏐⏐⏐≤
⏐⏐⏐⏐⏐ψn
(
iζ√
tnη′′(0)
)⏐⏐⏐⏐⏐×
⏐⏐⏐⏐⏐exp
(
tn η
(
iζ√
tnη′′(0)
))⏐⏐⏐⏐⏐
The ﬁrst part is bounded by a constant K(∆) because of the uniform convergence of ψn
towards ψ on the complex segment [−i∆/
√
η′′(0), i∆/
√
η′′(0)]. The second part can
28 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
be bounded by

 max
δ√
η′′ (0)≤|u|≤ ∆√
η′′ (0)
| exp(η(iu))|


tn
,
but the maximum is a constant qδ,∆ strictly smaller than 1, because η is not lattice
distributed. This implies that in the domain [−∆√tn, ∆√tn]\ [−δ√tn, δ√tn], one has
the bound
| f∗
n (ζ)|≤ K(∆)(qδ,∆)tn.
The explicit expression (13) shows that the same kind of bound holds for |g∗
n(ζ)|. We
shall use the notation ~K(∆) and~qδ,∆ for constants valid for both | f∗
n (ζ)| and|g∗
n(ζ)|.
Thus the third summand in the bound (15) is bounded by
4∆
πδ
~K(∆) (~qδ, 1
δ
)tn.
Fix ε > 0, then δ such that ε(δ) < ε and Mδ < ε. Take ∆ = 1
δ; we get
|Fn(x)− Gn(x)|≤ 2ε√tn
+ 4
πδ2
~K(δ−1) (~qδ,∆)tn≤ 3ε√tn
for tn large enough. This completes the proof of the proposition. □
Remark 4.2. Proposition 4.1 gives an approximation for the Kolmogorov distance be-
tween the law µn and the normal law. Indeed, assume to simplify that the reference
law φ is the Gaussian law. Then, η′′(0) = 1 and η′′′(0) = 0, and one computes
dKol(µn,NR(0, 1)) = 1√tn
sup
x∈R
⏐⏐⏐⏐
∫ x
−∞
ψ′(0) y g(y) dy
⏐⏐⏐⏐ + o
( 1√tn
)
=|ψ′(0)|√2πtn
+ o
( 1√tn
)
.
This makes explicit the bound given by Theorem 1 in [Hwa98]. If ψ′(0)⁄= 0 (e.g., as in
Lemma 4.7), we get an equivalent of the Kolmogorov distance. However, if ψ′(0) = 0,
then the estimate dKol = o(1/√tn) may not be optimal. Indeed, in the case of a scaled
sum of i.i.d. random variables, tn = n1/3 and one obtains the bound
dKol
(
1√n
n
∑
i=1
Yi,NR(0, 1)
)
= o
( 1
n1/6
)
,
which is not as good as the classical Berry-Esseen estimate O( 1
n1/2 ). There is a way to
modify the arguments in order to get such optimal estimates, by controlling the zone
of mod-convergence. We refer to [FMN15a], where such "optimal" computations of
Kolmogorov distances is performed.
MOD-φ CONVERGENCE, I 29
