---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-010-41-speed-of-convergence
section_title: "Speed of convergence"
section_number: 4.1
pages: 24-30
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
we denote Xn = 1
n1/4 ∑n
i=1 Bi a scaled sum of±1 independent Bernoulli random vari-
ables; Yn the random variable with modiﬁed law
Qn[dy] = e
y2
2n1/2 Pn[dy]
E
[
e
(Xn)2
2n1/2
] ;
Gn an independent Gaussian random variable of variance 1
n1/2 ; and Wn = Yn
n1/2 + Gn. It
follows from the previous results that the law of Wn has density
ψn(x)
In
= 1
In
e− n1/2 x2
2
(
cosh x
n1/4
)n
,
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS25
which converges in L 1 towards the law ψ(x)
I∞ = 1
I∞ e− x4
12 . We hence wish for an upper
bound for the Kolmogorov distance between Yn
n1/2 and W∞. For this we shall need the
following general lemmas.
Lemma 12. Consider the two distributions Wn = ψn(x) dx
In and W∞ = ψ(x) dx
I∞ . The Kolmogorov
distance between them is smaller than
‖ψ− ψn‖L1
I∞
(1 + o(1)).
Proof. Fix a∈ R, and suppose for instance that
∫
R ψ(x) dx≥∫
R ψn(x) dx. We have
FWn(a)− FW∞(a) =
(∫ a
−∞ ψn(x) dx
In
−
∫ a
−∞ ψ(x) dx
In
)
+
(∫ a
−∞ ψ(x) dx
In
−
∫ a
−∞ ψ(x) dx
I∞
)
=
∫ a
−∞(ψn(x)− ψ(x)) dx
In
+
(∫ a
−∞
ψ(x) dx
)∫ ∞
−∞(ψ(x)− ψn(x)) dx
I∞In
≤−
∫ a
−∞(ψ(x)− ψn(x)) dx
In
+
∫ ∞
−∞(ψ(x)− ψn(x)) dx
In
≤
∫ ∞
a (ψ(x)− ψn(x)) dx
In
≤‖ψ− ψn‖L1
In
.
Writing FW∞(a)− FWn(a) = ( 1− FWn(a))− (1− FW∞(a)), one sees that the inequality is
in fact valid with an absolute value on the left-hand side. Since In = I∞(1 + o(1)), this
shows the claim. If
∫
R ψn(x) dx≥∫
R ψ(x) dx, it sufﬁces to exchange the roles played
by ψn and ψ to get the inequality. □
The asymptotics of the L1-norm‖ψ− ψn‖L1 in the Curie-Weiss model are computed
as follows. Noting that one always has ψn(x)≥ ψ(x), it sufﬁces to compute
∫
R
ψn(x) dx =
∫
R
e− n1/2 x2
2
(
cosh(x n−1/4)
)n
dx = n1/4
∫
R
(
e− u2
2 cosh(u)
)n
du.
By the Laplace method (see [Zor04, Formula (19.17), p. 624-625]), the asymptotics of
the integral is
n− 1
4
(
121/4 Γ( 1
4 )
2
)
+ n− 3
4
(
123/4 Γ( 3
4 )
10
)
+ smaller terms.
The ﬁrst term corresponds to I∞ =∫
R ψ(x) dx =∫
R e−x4/12 dx. As a consequence,
‖ψ− ψn‖L1
I∞
= 1
n1/2
√
12 Γ( 3
4 )
5 Γ( 1
4 ) (1 + o(1)).
The main work now consists in computing dKol( Yn
n1/2 , Wn). We start by a Lemma
which is a variation of arguments used for i.i.d. random variables in [Tao12, p. 87].
26 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
In the following, given a function f ∈ L1(R), we write its Fourier transform ˆf (ξ) =∫
R f (x) eiξx dx. Recall that the function
υ(ξ) =
{
e
− 1
1−4ξ2 if|ξ| < 1
2,
0 otherwise.
is even, of classC ∞ and with compact support [− 1
2, 1
2 ]. We set ˆρ⋆ = υ, so that
ρ⋆(x) = 1
2π
∫ 1
2
− 1
2
υ(ξ) e−ixξ dξ
by the Fourier inversion theorem. By construction, the Fourier transform of ρ⋆ has
support equal to [− 1
2, 1
2 ]. Set now
ρ(x) = (ρ⋆(x))2
∫
R(ρ∗(y))2 dy .
By construction, ρ is smooth, even, non-negative and with integral equal to 1. More-
over,ˆρ is up to a constant equal to ν∗ ν(ξ), so it has support included into [−1, 1]. The
convolution of ρ with characteristic functions of intervals will allow us to transform
estimates on test functions into estimates on cumulative distribution functions. More
precisely, for a∈ R and ε > 0, set ρε(x) = 1
ε ρ( x
ε ), and φa,ε(x) = φε(x− a), where φε is
the function 1(−∞,0]∗ ρε. One sees φa,ε as a smooth approximation of the characteristic
function 1(−∞,a].
For all a, ε, φa,ε has Fourier transform compactly supported on
[
− 1
ε , 1
ε
]
. Moreover, it
has negative derivative, and decreases from 1 to 0. Later, we will use the identity
φε(εx) = φ1(x) = φ(x).
On the other hand, we have the following estimates for K > 0 (we used S AGE for
numerical computations):
|ρ∗(K)| = 1
2πK2
⏐⏐⏐⏐⏐
∫ 1
2
− 1
2
υ′′(ξ) e−iKξ dξ
⏐⏐⏐⏐⏐≤ 1
2πK2
∫ 1
2
0
|υ′′(ξ)| dξ = 1.0166−
K2 ;
∫
R
(ρ∗(y))2 dy = 1
2π
∫ 1
2
0
|υ(ξ)|2 dξ = 0.01059+.
Therefore, for any K > 0,
ρ(K) = ρ(−K) = (ρ∗(K))2
∫
R(ρ∗(y))2 dy≤ 99
K4 ;
φ(K) = 1− φ(−K) =
∫ ∞
0
ρ(K + y) dy≤ 33
K3 .
Lemma 13. Let V and W be two random variables with cumulative distribution functions FV
and FW. Assume that for some ε > 0
|E[φa,ε(V)]− E[φa,ε(W)]|≤ Bε,
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS27
where the positive constant B is independent of a. We also suppose that W has a density w.r.t.
Lebesgue measure that is bounded by m. Then,
sup
a∈R
|FV(a)− FW(a)|≤ 2(B + 10m) ε.
Proof. Fix a positive constant K, and denote δ = supa∈R|FV(a)− FW(a)| the Kolmogo-
rov distance between V and W. One has
FV(a) = E[1V≤a]≤ E[φa+Kε,ε(V)] + E[(1− φa+Kε,ε(V)) 1V≤a]
≤ E[φa+Kε,ε(W)] + E[(1− φa+Kε,ε(V)) 1V≤a] + Bε.
The second expectation writes as
E[(1−φa+Kε,ε(V)) 1V≤a] =
∫
R
(1− φa+Kε,ε(x)) 1(−∞,a](x) fV(x) dx
=−
∫
R
((1− φa+Kε,ε(x)) 1(−∞,a](x))′ FV(x) dx
=
∫
R
φ′
a+Kε,ε(x) 1(−∞,a](x) FV(x) dx +
∫
R
(1− φa+Kε,ε(x)) 1a(x) FV(x) dx.
For the ﬁrst integral, since FV(x)≥ FW(x)− δ and the derivative of φa+Kε,ε is negative,
an upper bound on I1 is
∫
R
φ′
a+Kε,ε(x) 1(−∞,a](x) FW(x) dx− δ
∫
R
φ′
a+Kε,ε(x) 1V≤a(x)
=
∫
R
φ′
a+Kε,ε(x) 1(−∞,a](x) FW(x) dx + (1− φa+Kε,ε(a)) δ
=
∫
R
φ′
a+Kε,ε(x) 1(−∞,a](x) FW(x) dx + (1− φ(−K)) δ.
As for the second integral, it is simply (1− φa+Kε,ε(a))FV(a), and by writing FV(a)≤
FW(a) + δ, one gets the upper bound on I2
∫
R
(1− φa+Kε,ε(x)) 1a(x) FW(x) dx + (1− φa+Kε,ε(a)) δ
=
∫
R
(1− φa+Kε,ε(x)) 1a(x) FW(x) dx + (1− φ(−K)) δ.
One concludes that
E[(1− φa+Kε,ε(V)) 1V≤a]≤ E[(1− φa+Kε,ε(W)) 1W≤a] + 2(1− φ(−K))δ.
On the other hand, if m is a bound on the density fW of W, then
E[φa+Kε,ε(W) 1W≥a] =
∫ ∞
a
φa+Kε,ε(y) fW(y) dy
≤ m
∫ ∞
a
φε(y− a− Kε) dy = m
∫ ∞
0
φε(y− Kε) dy
≤ mε
∫ ∞
0
φ(u− K) du≤ mε (K + 4.82) ,
28 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
by using on the last line the bound φ(x)≤ 33
x3 . As a consequence,
E[φa+Kε,ε(W)]≤ E[φa+Kε,ε(W) 1W≤a] + m (K + 4.82) ε
FV(a)≤ FW(a) + (B + m (K + 4.82)) ε + 2 33
K3 δ.
Similarly, FV(a)≥ FW(a)− (B + m(K + 4.82))ε− 2 33
K3 δ, so in the end
δ = sup
a∈R
|FV(a)− FW(a)|≤ (B + m (K + 4.82)) ε + 66
K3 δ.
As this is true for every K, one can for instance take K =
3√
132, which gives
δ≤ 1
1− 1
2
(
B + m
(
3√
132 + 4.82
))
ε≤ 2(B + 10m) ε.
□
We are going to apply Lemma 13 with V = Yn
n1/2 and W = Wn. First, notice that a
bound on the density of Wn is
|ψn(x)|
In
≤ 1
I∞
= 2
121/4 Γ( 1
4 ) = m.
On the other hand, using the Fourier transform of the Heaviside function
ˆ1(−∞,a](ξ) = eiaξ
(
πδ0(ξ) + i
ξ
)
,
we get
E
[
φa,ε
( Yn
n1/2
)]
− E[φa,ε(Wn)] = 1
2πIn
∫ 1
ε
− 1
ε
ˆφa,ε(ξ)ˆψn(ξ)
(
e
ξ2
2n1/2− 1
)
dξ
= 1
2πIn
∫ 1
ε
− 1
ε
ˆρε(ξ) eiaξ
( i
ξ
)
ˆψn(ξ)
(
e
ξ2
2n1/2− 1
)
dξ;
⏐⏐⏐⏐E
[
φa,ε
( Yn
n1/2
)]
− E[φa,ε(Wn)]
⏐⏐⏐⏐≤ 1
2πIn n1/2
∫ 1
ε
− 1
ε
|ˆρ(εξ)||ˆψn(ξ)| e
ξ2
2n1/2 dξ
by controlling e
ξ2
2n1/2− 1 by its ﬁrst derivative (notice that we used the vanishing of
this quantity at ξ = 0 in order to compensate the singularity of the Fourier transform
of the Heavyside distribution). Since ‖ˆρ‖L∞ =‖ρ‖L1 = 1, the previous bound can be
rewritten as
⏐⏐⏐⏐E
[
φa,ε
( Yn
n1/2
)]
− E[φa,ε(Wn)]
⏐⏐⏐⏐≤ 1
2πIn n1/2
∫ 1
ε
− 1
ε
|ˆψn(ξ)| e
ξ2
2n1/2 dξ.
We then need estimates on the Fourier transform ofˆψn, and more precisely estimates
of exponential decay. To this purpose, we use the following Lemma, which is related
to [RS75, Theorem IX.13, p. 18]:
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS29
Lemma 14. Let f be a function which is analytic on a band {z∈ C|| Im(z)| < c}. For any
b∈ (0, c),
|ˆf (ξ)|≤ 2
(
sup
−b≤a≤b
‖ f (· + ia)‖L1
)
e−b|ξ|,
assuming that the supremum is ﬁnite.
Proof. Notice that the Fourier transform of τa f (·) = f (· + ia) is
∫
R
τa f (x) eixξ dx =
∫
R
f (x + ia) eixξ dx =
(∫
R
f (x + ia) ei(x−ia)ξ dx
)
e−aξ.
By analyticity of the function in the integral, using Cauchy’s integral formula, one sees
that the last term is also
(∫
R
f (x) eixξ dx
)
eaξ = ˆf (ξ) e−aξ,
(see the details on page 132 of the book by Reed and Simon). It follows that
|ˆf (ξ)| ea|ξ|≤| ˆf (ξ)| (eaξ + e−aξ)≤| ˆτa f (ξ)| +|ˆτ−a f (ξ)|≤‖ τa f‖L1 +‖τ−a f‖L1.
□
Thus we need to compute for a > 0 the L1-norm of ψn(· + ia). We write
|ψn(x + ia)| = e− n1/2 (x2−a2)
2
⏐⏐⏐⏐cosh
( x + ia
n1/4
)⏐⏐⏐⏐
n
=|ψn(x)| e
n1/2a2
2
⏐⏐⏐cos2
( a
n1/4
)
+ tanh2
( x
n1/4
)
sin2
( a
n1/4
)⏐⏐⏐
n
2
=|ψn(x)| e
n1/2a2
2
⏐⏐⏐1−
(
1− tanh2
( x
n1/4
))
sin2
( a
n1/4
)⏐⏐⏐
n
2
.
For n large enough, sin2( a
n1/4 )≥ a2
n1/2− a4
3n, and on the other hand, 0≤ tanh2
(
x
n1/4
)
≤
x2
n1/2 , so
⏐⏐⏐⏐
ψn(x + ia)
ψn(x)
⏐⏐⏐⏐≤ e
n1/2a2
2 exp
(
− n1/2a2
2
(
1− tanh2
( x
n1/4
))(
1− a2
3n1/2
))
≤ e
a4
3 e
a2x2
2 .
Since ψn(x) behaves as e−x4/12, the previous Lemma can be applied, with an asymp-
totic bound
‖ψn(· + ia)‖L1≲ e
a4
3
∫
R
e− x4
12 + a2x2
2 dx = e
13a4
12
∫
R
e− (x2−3a2)2
12 dx
≲ e
13a4
12
(
2
√
3 a + I∞
)
by cutting the integral in two parts according to the sign ofx2− 3a2. We have therefore
proven:
30 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
Proposition 15. For any b≥ 0,
|ˆψn(ξ)|≲ K(b) e−b|ξ|,
where K(b) = 2e
13b4
12 (2
√
3 b + I∞) and where the symbol≲ means that the inequality is true
up to any multiplicative constant 1 + ε, for ε > 0 and n large enough.
We can now conclude. Fix b > 0, and D < 2b. On the interval [−Dn1/2, Dn1/2], we
have
ξ2
2n1/2− b|ξ| =−|ξ|
(
b− |ξ|
2n1/2
)
≤−| ξ|
(
b− D
2
)
.
Therefore, with ε = 1
Dn1/2 ,
⏐⏐⏐⏐E
[
φa,ε
( Yn
n1/2
)]
− E[φa,ε(Wn)]
⏐⏐⏐⏐≲ K(b)
2πI∞ n1/2
∫
R
e−(b− D
2 )|ξ| dξ = K(b)
πI∞ n1/2 (
b− D
2
)
≲ K(b) D
πI∞
(
b− D
2
) ε.
So, Lemma 13 applies to V = Yn
n1/2 and W = Wn, with
dKol
( Yn
n1/2 , Wn
)
≲ 2
(
K(b) D
πI∞
(
b− D
2
) + 10
I∞
)
ε = 2
I∞ n1/2
(
K(b)
π (b− D
2 ) + 10
D
)
.
Taking b = D = 0.77, we get ﬁnally
dKol
( Yn
n1/2 , Wn
)
≲ 2
I∞ n1/2
(2 K(b)
π b + 10
b
)
≤ 10.27
n1/2 .
Adding the bound on dKol(Wn, W∞) yields then:
Theorem 16. For n large enough,
dKol
( Yn
n1/2 , W∞
)
≤ 11 n−1/2.
Notice that we have only used arguments of Fourier analysis and the language of
mod-Gaussian convergence in order to get this bound.
