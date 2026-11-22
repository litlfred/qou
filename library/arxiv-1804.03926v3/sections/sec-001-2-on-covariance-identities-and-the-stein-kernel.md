---
doc_id: arxiv-1804.03926v3
doc_title: "Weighted Poincaré inequalities, concentration inequalities and tail bounds related to Stein kernels in dimension one"
section_id: sec-001-2-on-covariance-identities-and-the-stein-kernel
section_title: "On covariance identities and the Stein kernel"
section_number: 2
pages: 3-8
source_pdf: 1804.03926v3.pdf
source_sha256: 8ad8e2d5a8881a5b
toc_source: outline
doc_brief: "Weighted Poincaré inequalities, concentration inequalities and tail bounds related to Stein kernels in dimension one — We investigate links between the so-called Stein’s density approach in dimension"
---
On covariance identities and the Stein kernel
Take a real random variable X of distribution ν with density p with respect to the Lebesgue measure
on R and cumulative distribution function F. Assume that the mean of the distribution ν exists and
denote it by µ = E [X]. Denote also Supp (ν) = {x ∈R : p (x) > 0} ⊂¯R( := R∪{−∞, +∞}) the
support of the measure ν, deﬁned as the closure of the set where the density is positive and assume
that this support is connected. We denote by a ∈R∪{−∞}, b ∈R ∪{+∞}, a < b, the edges of
Supp(ν). For convenience, we also denote by I (ν) = Int (Supp(ν)) the interior of the support of ν.
The distribution ν is said to have a Stein kernel τ ν, if the following identity holds true,
E [(X −µ) ϕ (X)] = E

τ ν (X) ϕ′ (X)

,
(5)
with ϕ being any diﬀerentiable test function such that the functions x 7→(x −µ) ϕ (x) and x 7→
τ ν (x) ϕ′ (x) are ν-integrable and [τ νpϕ]b
a = 0.
It is well-known ([LNP15, CFP17, LRS17]), that
3
under our assumptions the Stein kernel τ ν exists, is unique up to sets of ν-measure zero and a
version of the latter is given by the following formula,
τ v (x) =
1
p (x)
Z ∞
x
(y −µ) p (y) dy ,
(6)
for any x ∈I (ν). Formula (6) comes from a simple integration by parts. Notice that τ ν is almost
surely positive on the interior of the support of ν.
Although we will focus only on dimension one, it is worth noting that the deﬁnition of a Stein
kernel extends to higher dimension, where it is matrix-valued. The question of existence of the Stein
kernel for a particular multi-dimensional measure ν is nontrivial and only a few general results
are known related to this problem (see for instance [LNP15] [CFP17] and [Fat18]). In particular,
[CFP17] proves that the existence of a Stein kernel is ensured whenever a (converse weighted) Poincar´e
inequality is satisﬁed for the probability measure ν. Recently, Stein kernels that are positive deﬁnite
matrices have been constructed in [Fat18] using transportation techniques.
In this section, that essentially aims at stating some background results that will be instrumental
for the rest of the paper, we will among other things recover Identity (6) and introduce a new
formula for the Stein kernel by means of a covariance identity recently obtained in [MO13] and
further developed in [SW18a]. It actually appears that Menz and Otto’s covariance identity is a
consequence of an old result by Hoeﬀding (see the discussion in [SW18b]).
We deﬁne a non-negative and symmetric kernel kν on R2 by
kν (x, y) = F (x ∧y) −F (x) F (y) ,
for all (x, y) ∈R2.
(7)
For any p ∈[1, +∞], we denote by Lp (ν) the space of measurable functions f such that ∥f∥p
p =
R
|f|p dν < +∞for p ∈[1, +∞) and ∥f∥∞= ess supx∈R |f (x)| < +∞for p = +∞. If f ∈Lp (ν),
g ∈Lq (ν), p−1 + q−1 = 1, we also write
Cov (f, g) =
Z 
f −
Z
fdν

gdν
the covariance of f and g with respect to ν. For f ∈L2 (ν), we write Var (f) = Cov (f, f) the
variance of f with respect to ν.
For a random variable X of distribution ν, we will also write
E [h (X)] = E [h] =
R
hdν.
Proposition 1 (Corollary 2.2, [SW18a]) If g and h are absolutely continuous and g ∈Lp(ν),
h ∈Lq(ν) for some p ∈[1, ∞] and p−1 + q−1 = 1, then
Cov(g, h) =
ZZ
R2 g′(x)kν(x, y)h′(y)dxdy.
(8)
It is worth mentioning that the covariance identity (8) heavily relies on dimension one, since it
uses the properties of the cumulative distribution function F through the kernel kν. In dimension
greater than or equal to 2, a covariance identity of the form of (8) - with derivatives replaced by
gradients -, would actually imply that the measure ν is Gaussian (for more details, see [BGH01] and
also Remark 2 below).
Remark 2 In the context of goodness-of-ﬁt tests, Liu et al. [LLJ16] introduce the notion of kernelized
Stein discrepancy as follows. If K (x, y) is a kernel on R2, p and q are two densities and (X, Y ) is a
4
pair of independent random variables distributed according to p, then the kernelized Stein discrepancy
SK (p, q) between p and q related to K is
SK (p, q) = E [δq,p (X) K (X, Y ) δq,p (Y )] ,
where δq,p (x) = (log q (x))′ −(log p (x))′ is the diﬀerence between scores of p and q. This notion is in
fact presented in [LLJ16] in higher dimension and is used as an eﬃcient tool to assess the proximity
of the laws p and q. From formula (8), we see that if we take Kν (x, y) = kν(x, y)pν (x)−1 pν (y)−1,
then we get the following formula, valid in dimension one,
SKν (p, q) = Varν

log
p
q

.
In higher dimension, Bobkov et al. [BGH01] proved that the Gaussian measures satisfy a covariance
identity of the same form as in (8) above, with derivatives replaced by gradients. More precisely,
let (X, Y ) be a pair of independent normalized Gaussian vectors in Rd, let µα be the measure of the
pair

X, αX +
√
1 −α2Y

and let pN (x, y) be the density associated the measure
R 1
0 µαdα. Then we
have
Cov (g (X) , h (X)) =
ZZ
R2 ∇g(x)T pN(x, y)∇h(y)dxdy .
This gives that for a kernel KN (x, y) = pN (x, y) ϕ−1 (x) ϕ−1 (y), where ϕ is the standard normal
density on Rd, we also have
SKN (p, q) = Var

log
p
q

(X)

.
The following formulas will also be useful. They can be seen as special instances of the previous
covariance representation formula.
Corollary 3 (Corollary 2.1, [SW18a]) For an absolutely continuous function h ∈L1(F),
F(z)
Z
R
hdν −
Z z
−∞
hdν =
Z
R
kν (z, y) h′(y)dy
(9)
and
−(1 −F(z))
Z
R
hdν +
Z
(z,∞)
hdν =
Z
R
kν (z, y) h′(y)dy.
(10)
By combining Theorem 1 and Corollary 3, we get the following covariance identity.
Proposition 4 Let ν be a probability measure on R and p, q ≥1 such that p−1 + q−1 = 1. Denote
Lh (x) =
R ∞
x hdν −(1 −F (x))
R
R hdν = F (x)
R
R hdν −
R x
−∞hdν for every x∈R. If g ∈Lp (ν) and
h ∈Lq (ν) are absolutely continuous and if g′Lh is integrable with respect to the Lebesgue measure,
then
Cov (g, h) =
Z
R
g′ (x) Lh (x) dx ,
(11)
Furthermore, if ν has a density p with respect to the Lebesgue measure that has a connected support,
then
Cov (g, h) =
Z
R
g′ (x) ¯Lh (x) p (x) dx = E

g′ (X) ¯Lh (X)

,
(12)
5
where, for every x ∈I (ν),
¯Lh (x)
=
p (x)−1 Lh (x)
=
1
p (x)
Z ∞
x
hdν −1 −F (x)
p (x)
E [h] .
(13)
If x /∈I (v), we take ¯Lh (x) = 0.
Proof. Identity (11) consists in applying Fubini theorem in the formula of Theorem 1 and then
using Corollary 3. If ν has a density p with respect to the Lebesgue measure that has a connected
support then for every x /∈I (ν) we have Lh (x) = 0. Consequently, from Identity (11) we get, for
g ∈L∞(ν), h ∈L1 (ν) absolutely continuous,
Cov (g, h)
=
Z
I(ν)
g′ (x) Lh (x) dx
=
Z
I(ν)
g′ (x) ¯Lh (x) p (x) dx
and so Identity (12) is proved.
From Proposition 4, we can directly recover formula (6) for the Stein kernel, when it is assumed
that the measure has a connected support and ﬁnite ﬁrst moment. Indeed, by taking h (x) = x −µ,
we have h ν-integrable and diﬀerentiable and so, for any absolutely continuous function g ∈L∞(ν)
such that g′ ¯Lh is ν-integrable, applying Identity (12) - since g′Lh = g′ ¯Lhp a.s. is Lebesgue integrable
- yields
Cov (g, h) =
Z
R
(x −µ) g (x) p (x) dx =
Z
R
g′ ¯Lhdν .
(14)
As by a standard approximation argument - i.e. truncations and an application of the dominated con-
vergence theorem -, identity (14) can be extended to any g such that the functions x 7→(x −µ) g (x)
and x 7→τ ν (x) g′ (x) are ν-integrable and [τ νpg]b
a = 0, we deduce that a version of the Stein kernel
τ v is given by ¯Lh, which is nothing but the right-hand side of Identity (6).
Following the nice recent survey [LRS17] related to the Stein method in dimension one, identity
(12) is exactly the so-called ”generalized Stein covariance identity”, written in terms of the inverse
of the Stein operator rather than the Stein operator itself. Indeed, it is easy to see that the inverse
Tν of the operator ¯L acting on integrable functions with mean zero is given by the following formula
Tνf = (fp)′
p
1I(ν) ,
which is exactly the Stein operator (see Deﬁnition 2.1 of [LRS17]).
It is also well known, see again [LRS17], that the inverse of the Stein operator, that is ¯L, is
highly involved in deriving bounds for distances between distributions. From Corollary 3, we have
the following seemingly new formula for this important quantity,
T −1
ν
h (x) = ¯Lh (x) =
1
p (x)
Z
R
kν (x, y) h′(y)dy .
(15)
Particularizing the latter identity with h (x) = x −µ, we obtain the following identity for the Stein
kernel,
τ ν (x) =
1
p (x)
Z
R
kν (x, y) dy .
(16)
6
A consequence of (16) that will be important in Section 3 when deriving weighted functional in-
equalities is that for any x ∈I (ν) the function y 7→kν (x, y) (p (x) τ ν (x))−1 can be seen as the
density - with respect to the Lebesgue measure - of a probability measure, since it is nonnegative
and integrates to one.
We also deduce from (15) the following upper bound,

T −1
ν
h (x)

 ≤∥h′∥∞
p (x)
Z
R
kν (x, y) dy = ∥h′∥∞
p (x)

F (x)
Z
R
xdν (x) −
Z x
−∞
xdν (x)

,
which is exactly the formula given in Proposition 3.13(a) of [D¨ob15].
Let us note ϕ (x) = −log p (x) when p (x) > 0 and +∞otherwise, the so-called potential of
the density p. If on I (ν), ϕ has derivative ϕ′ ∈L1 (ν) absolutely continuous, then Corollary 2.3 in
[SW18a] gives
Z
R
kν (x, y) ϕ′′(y)dy = p (x) .
Using the latter identity together with (15), we deduce the following upper-bound: if p is strictly
log-concave (that is ϕ′′ > 0 on I (ν)), then
sup
x∈I(ν)

T −1
ν
h (x)

 ≤sup
x∈I(ν)
|h′ (x)|
ϕ′′ (x) .
(17)
In particular, if p is c-strongly log-concave, meaning that ϕ′′ ≥c > 0 on R, then the Stein kernel
is uniformly bounded and ∥τ ν∥∞≤c−1. For more about the Stein method related to (strongly)
log-concave measures, see for instance [MG16].
Furthermore, by diﬀerentiating (15), we obtain for any x ∈I (ν),
 T −1
ν
h
′ (x)
=
ϕ′ (x) T −1
ν
h (x) −h (x) −
Z
R
F (y) h′ (y) dy
=
ϕ′ (x) T −1
ν
h (x) −h (x) + E [h (X)] ,
that is
 T −1
ν
h
′ (x) −ϕ′ (x) T −1
ν
h (x) = −h (x) + E [h (X)] .
This is nothing but the so-called Stein equation associated to the Stein operator.
We conclude this section with the following formulas, that are available when considering a density
with connected support and that will be useful in the rest of the paper (see in particular Sections
3.2 and 5).
Proposition 5 Assume that X is a random variable with distribution ν having a density p with
connected support with respect to the Lebesgue measure on R. Take h ∈L1 (ν) with E [h (X)] = 0
and assume that the function ¯Lh deﬁned in (13) is ν-almost surely strictly positive. We have, for
any x0, x ∈I (ν),
p (x) = E

h (X) 1{X≥x0}

¯Lh (x)
exp

−
Z x
x0
h (y)
¯Lh (y)dy

.
(18)
Consequently, if X has a ﬁnite ﬁrst moment, for any x ∈I (ν),
p (x) = E [|X −µ|]
2τ ν (x)
exp

−
Z x
µ
y −µ
τ ν (y)dy

.
(19)
7
By setting Th (x) = exp

−
R x
x0
h(y)
¯Lh(y)dy

and I (ν) = (a, b), if the function h is ν-almost positive,
diﬀerentiable on (x, b) and if the ratio Th (y) /h (y) tends to zero when y tends to b−, then we have,
for any x0, x ∈I (ν),
P (X ≥x) = E

h (X) 1{X≥x0}
 Th (x)
h (x) −
Z b
x
h′ (y)
h2 (y)Th (y) dy

.
(20)
Formula (18) can also be found in [D¨ob15], Equation (3.11), under the assumption that h is
decreasing and for a special choice of x0. Since E [h (X)] = 0, it is easily seen through its deﬁnition
(13), that if h̸ = 0 ν −a.s. then ¯Lh > 0 ν −a.s. When h = Id −µ, formulas (19) and (20) were
ﬁrst proved respectively in [NV09] and [Vie09], although with assumption that the random variable
X belongs to the space D1,2 of square integrable random variables with the natural Hilbert norm of
their Malliavin derivative also square integrable.
In order to take advantage of formulas (18) and (20), one has to use some information about ¯Lh.
The most common choice is h = Id −µ, which corresponds to the Stein kernel ¯L (Id −µ) = τ ν.
Proof. Begin with Identity (18). As x0 ∈I (ν) and the function Lh deﬁned in (4) is ν-almost surely
positive, we have for any x ∈I (v),
Lh (x) = Lh (x0) exp
Z x
x0
(ln (Lh))′ (y) dy

.
To conclude, note that Lh (x0) = E

h (X) 1{X≥x0}

and (ln (Lh))′ = −h/ ¯Lh. To prove (19), simply
remark that is follows from (18) by taking h = Id −µ and x0 = µ.
It remains to prove (20). We have from (18), p = E

h (X) 1{X≥x0}

Th/ ¯Lh and by deﬁnition of
Th, T ′
h = −hTh/ ¯Lh. Hence, integrating between x and b gives
P (X ≥x)
=
E

h (X) 1{X≥x0}
 Z b
x
Th (y)
¯Lh (y)dy
=
E

h (X) 1{X≥x0}
 Z b
x
−T ′
h (y)
h (y) dy
=
E

h (X) 1{X≥x0}

 −Th
h
b
x
−
Z b
x
h′ (y) Th (y)
h2 (y)
dy
!
=
E

h (X) 1{X≥x0}
 Th (x)
h (x) −
Z b
x
h′ (y) Th (y)
h2 (y)
dy

.
