---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-005-21-basic-examples-of-mod-convergence
section_title: "Basic examples of mod-convergence"
section_number: 2.1
pages: 9-12
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
vergence, which will guide our intuition throughout the paper. In these examples, it
will be useful sometimes to precise the speed of convergence in Deﬁnition 1.1.
Deﬁnition 2.1. We say that the sequence of random variables (Xn)n∈N converges mod-φ at
speed O((tn)−v) if the difference of the two sides of Equation (1) can be bounded by CK (tn)−v
for any z in a given compact subset K of S(c,d). We use the analogue deﬁnition with the o (·)
notation.
Example 2.2. Let (Yn)n∈N be a sequence of centered, independent and identically dis-
tributed real-valued random variables, with E[ezY] = E[ezY1] analytic and non-vani-
shing on a stripS(c,d), possibly with c =−∞ and/or d = + ∞. Set Sn = Y1 +··· + Yn.
If the distribution of Y is inﬁnitely divisible, then Sn converges mod-Y towards the
limiting function ψ≡ 1 with parameter tn = n.
But there is another mod-convergence hidden in this framework (we now drop the
assumption of inﬁnite divisibility of the law of Y). The cumulant generating series of
Sn is
log E[ezSn] = n log E[ezY] = n
∞
∑
r=2
κ(r)(Y)
r! zr,
which is also analytic onS(c,d) — the coefﬁcients κ(r)(Y) are the cumulants of the vari-
able Y. Let v≥ 3 be an integer such that κ(r)(Y) = 0 for each integer r strictly between
3 and v− 1, and set Xn = Sn
n1/v . It is always possible to take v = 3, but sometimes we
can also consider higher value of v, for instance v = 4 as soon as Y is a symmetric ran-
dom random variable, and has therefore its odd moments and cumulants that vanish.
One has
log ϕn(z) = n
v−2
v
κ(2)(Y)
2 z2 + κ(v)(Y)
v! zv +
∞
∑
r=v+1
κ(r)(Y)
r! nr/v−1 zr,
and locally uniformly on C the right-most term is bounded by C
n1/v . Consequently,
ψn(z) = exp
(
−n
v−2
v
σ2z2
2
)
ϕn(z)→ exp
(
κ(v)(Y)
v! zv
)
+ O(n−1/v),
that is, (Xn)n∈N converges in the mod-Gaussian sense with parameters tn = σ2 n
v−2
v ,
speed O(n−1/v) and limiting function ψ(z) = exp(κ(v)(Y) zv/v!). Note that this ﬁrst
example was used in [KNN13] to characterize the set of limiting functions in the setting
of mod-φ convergence.
10 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
Through this article, we shall commonly rescale random variables in order to get
estimates of ﬂuctuations at different regimes. In order to avoid any confusion, we
provide the reader with the following scheme, which details each possible scaling,
and for each scaling, the regimes of ﬂuctuations that can be deduced from the mod-
φ convergence, as well as their scope. We also underline or frame the scalings and
regimes that will be studied in this paper, and give references for the other kinds of
ﬂuctuations.
scaling
Sn
Sn
n1/v
mod-convergence
tn φ
n Y
σ2n1− 2
v NR(0, 1)
Sn
n
Sn
n1−1/(v+1)
Sn
n1−1/v
Sn
n1/2
large deviations
(cf. [BR60, DZ98])
moderate deviations
regime of ﬂuctuations
normality zone
local limit theorem
(cf. [DKN11, KN12, FMN15a])
FIGURE 1. Panorama of the ﬂuctuations of a sum of n i.i.d. random variables.
The content of this scheme will be fully explained in Section 4 (see in particular Section
4.4).
Example 2.3. Denote Xn the number of disjoint cycles (including ﬁxed points) of a ran-
dom permutation chosen uniformly in the symmetric group S(n). Feller’s coupling
(cf. [ABT03, Chapter 1]) shows thatXn =(law) ∑n
i=1B(1/i), whereBp denotes a Bernoulli
variable equal to 1 with probability p and to 0 with probability 1− p, and the Bernoulli
variables are independent in the previous expansion. So,
E[ezXn] =
n
∏
i=1
(
1 + ez− 1
i
)
= eHn(ez−1)
n
∏
i=1
1 + ez−1
i
e
ez−1
i
where Hn = ∑n
i=1
1
i = log n + γ + O(n−1). The Weierstrass inﬁnite product in the right-
hand side converges locally uniformly to an entire function, therefore (see [WW27]),
E[ezXn] e−(ez−1) log n→ eγ (ez−1)
∞
∏
i=1
1 + ez−1
i
e
ez−1
i
= 1
Γ(ez)
locally uniformly, i.e., one has mod-Poisson convergence with parameters tn = log n
and limiting function 1/Γ(ez). Moreover, the speed of convergence is aO(n−1), hence,
a o((tn)−v) for any integer v. We shall study generalizations of this example in Section
7.3.
MOD-φ CONVERGENCE, I 11
scaling
Xn
Xn−Hn
(Hn)1/3
mod-convergence
tn φ
Hn P (1)
(Hn)1/3 NR(0, 1)
Xn
Hn− 1
Xn−Hn
(Hn)3/4
Xn−Hn
(Hn)2/3
Xn−Hn
(Hn)1/2
large deviations
(cf. [Rad09])
moderate deviations
regime of ﬂuctuations
normality zone
local limit theorem
FIGURE 2. Panorama of the ﬂuctuations of the number of cycles Xn of a
random permutation of size n.
Once again, there is another mod-convergence hidden in this example. Indeed, con-
sider Yn = Xn−Hn
(Hn)1/3 . Its generating function has asymptotics
E[ezYn] = e
Hn
(
e
z
(Hn)1/3−1
)
−z(Hn)2/3
(1 + o(1)) = e(Hn)1/3 z2
2 exp
( z3
6
)
(1 + o(1)).
Therefore, one has mod-Gaussian convergence of Yn with parameters tn = ( Hn)1/3
and limiting function exp(z3/6).
This is in fact a particular case of a more general phenomenon: every sequence that
converges mod-φ converges with a different rescaling in the mod-Gaussian sense.
Proposition 2.4. Assume X n converges mod- φ with parameters t n and limiting function ψ,
where φ is not the Gaussian distribution. Let
m = min
i≥3
{i| η(i)(0)⁄= 0}.
Then, the sequence of random variables Y n = ( Xn− tnη′(0))/(tn)1/m converges in the
mod-Gaussian sense with parameters (tn)1−2/mη′′(0) towards the limiting function Ψ(z) =
exp
(
η(m)(0)zm/m!).
Proof. This follows from a simple computation
E
[
exp
(z(Xn− tnη′(0))
(tn)1/m
)]
= exp
(−tnη′(0))
(tn)1/m
)
exp
(
tn η
( z
(tn)1/m
))
ψ
( z
(tn)1/m
)
(1 + o(1)).
The factor ψ( z
(tn)1/m ) tends to 1 and we do a Taylor expansion of η( z
(tn)1/m ). We get
E
[
exp
( z(Xn− tnη′(0))
(tn)1/m
)]
= exp
(
(tn)1−2/mη′′(0)z2
2 + η(m)(0)zm
m! + o(1)
)
(1 + o(1)).
□
12 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
Naturally, the mod- φ convergence gives more information than the implied mod-
Gaussian convergence: our deviation results — Theorems 3.4 and 4.3 — for the former
involve deviation probabilities of Xn at scale O(tn), while with the mod-Gaussian con-
vergence, we get deviation probabilities of Yn at scale O((tn)1−2/m), that is deviations
of Xn at scale O((tn)1−1/m).
