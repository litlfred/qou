---
doc_id: arxiv-1804.03926v3
doc_title: "Weighted Poincaré inequalities, concentration inequalities and tail bounds related to Stein kernels in dimension one"
section_id: sec-001-2-on-covariance-identities-and-the-stein-kernel
section_title: "On covariance identities and the Stein kernel"
section_number: 2
pages: 3-8
source_pdf: 1804.03926v3.pdf
source_sha256: 8ad8e2d5a8881a5b
doc_brief: "Weighted Poincaré inequalities, concentration inequalities and tail bounds related to Stein kernels in dimension one — We investigate links between the so-called Stein’s density approach indimension"
---
Take a real random variableX of distributionν with densityp with respect to the Lebesgue measure
on R and cumulative distribution functionF. Assume that the mean of the distribution ν exists and
denote it by µ = E [X]. Denote also Supp ( ν) = {x ∈ R :p (x)> 0} ⊂ ¯R( := R∪ {−∞, +∞}) the
support of the measure ν, deﬁned as the closure of the set where the density is positiv e and assume
that this support is connected. We denote by a ∈ R∪ {−∞}, b ∈ R ∪ {+∞}, a < b, the edges of
Supp (ν). For convenience, we also denote by I (ν) = Int (Supp (ν)) the interior of the support of ν.
The distribution ν is said to have a Stein kernel τν, if the following identity holds true,
E [(X −µ)ϕ (X)] = E
[
τν (X)ϕ ′ (X)
]
, (5)
with ϕ being any diﬀerentiable test function such that the function s x ↦→(x −µ)ϕ (x) and x ↦→
τν (x)ϕ ′ (x) are ν-integrable and [ τνpϕ ]b
a = 0. It is well-known ([LNP15, CFP17, LRS17]), that
3
under our assumptions the Stein kernel τν exists, is unique up to sets of ν-measure zero and a
version of the latter is given by the following formula,
τv (x) = 1
p (x)
∫ ∞
x
(y −µ)p (y)dy , (6)
for any x ∈ I (ν). Formula (6) comes from a simple integration by parts. Noti ce that τν is almost
surely positive on the interior of the support of ν.
Although we will focus only on dimension one, it is worth noti ng that the deﬁnition of a Stein
kernel extends to higher dimension, where it is matrix-valu ed. The question of existence of the Stein
kernel for a particular multi-dimensional measure ν is nontrivial and only a few general results
are known related to this problem (see for instance [LNP15] [ CFP17] and [Fat18]). In particular,
[CFP17] proves that the existence of a Stein kernel is ensured whenever a (converse weighted) Poincar´ e
inequality is satisﬁed for the probability measure ν. Recently, Stein kernels that are positive deﬁnite
matrices have been constructed in [Fat18] using transporta tion techniques.
In this section, that essentially aims at stating some background results that will be instrumental
for the rest of the paper, we will among other things recover I dentity (6) and introduce a new
formula for the Stein kernel by means of a covariance identit y recently obtained in [MO13] and
further developed in [SW18a]. It actually appears that Menz and Otto’s covariance identity is a
consequence of an old result by Hoeﬀding (see the discussion i n [SW18b]).
We deﬁne a non-negative and symmetric kernel kν on R2 by
kν (x,y ) =F (x ∧y) −F (x)F (y), for all (x,y ) ∈ R2. (7)
For any p ∈ [1, +∞], we denote by Lp (ν) the space of measurable functions f such that ‖f ‖p
p =∫
|f |pdν <+∞ for p ∈ [1, +∞) and ‖f ‖∞ = ess supx∈R |f (x)| < +∞ for p = +∞. If f ∈ Lp (ν),
g ∈Lq (ν), p−1 +q−1 = 1, we also write
Cov (f,g ) =
∫ (
f −
∫
fdν
)
gdν
the covariance of f and g with respect to ν. For f ∈ L2 (ν), we write Var (f) = Cov (f,f ) the
variance of f with respect to ν. For a random variable X of distribution ν, we will also write
E [h (X)] = E [h] =
∫
hdν.
Proposition 1 (Corollary 2.2, [SW18a]) If g and h are absolutely continuous and g ∈ Lp(ν),
h ∈Lq(ν) for some p ∈ [1, ∞] and p−1 +q−1 = 1, then
Cov(g,h ) =
∫∫
R2
g′(x)kν(x,y )h′(y)dxdy. (8)
It is worth mentioning that the covariance identity (8) heav ily relies on dimension one, since it
uses the properties of the cumulative distribution functio n F through the kernel kν. In dimension
greater than or equal to 2, a covariance identity of the form o f (8) - with derivatives replaced by
gradients -, would actually imply that the measure ν is Gaussian (for more details, see [BGH01] and
also Remark 2 below).
Remark 2 In the context of goodness-of-ﬁt tests, Liu et al. [LLJ16] introd uce the notion of kernelized
Stein discrepancy as follows. If K (x,y ) is a kernel on R2, p and q are two densities and (X,Y ) is a
4
pair of independent random variables distributed accordin g to p, then the kernelized Stein discrepancy
SK (p,q ) betweenp and q related to K is
SK (p,q ) = E [δq,p (X)K (X,Y )δq,p (Y )] ,
whereδq,p (x) = (logq (x))′ − (logp (x))′ is the diﬀerence between scores of p and q. This notion is in
fact presented in [LLJ16] in higher dimension and is used as an e ﬃcient tool to assess the proximity
of the laws p and q. From formula (8), we see that if we take Kν (x,y ) = kν(x,y )pν (x)−1pν (y)−1,
then we get the following formula, valid in dimension one,
SKν (p,q ) = Varν
(
log
(p
q
))
.
In higher dimension, Bobkov et al. [BGH01] proved that the Gau ssian measures satisfy a covariance
identity of the same form as in (8) above, with derivatives re placed by gradients. More precisely,
let (X,Y ) be a pair of independent normalized Gaussian vectors in Rd, let µ α be the measure of the
pair
(
X,αX +
√
1 −α 2Y
)
and let pN (x,y ) be the density associated the measure
∫ 1
0 µ αdα . Then we
have
Cov (g (X),h (X)) =
∫∫
R2
∇g(x)TpN(x,y )∇h(y)dxdy .
This gives that for a kernel KN (x,y ) = pN (x,y )ϕ −1 (x)ϕ −1 (y), where ϕ is the standard normal
density on Rd, we also have
SKN (p,q ) = Var
(
log
(p
q
)
(X)
)
.
The following formulas will also be useful. They can be seen a s special instances of the previous
covariance representation formula.
Corollary 3 (Corollary 2.1, [SW18a]) For an absolutely continuous function h ∈L1(F),
F(z)
∫
R
hdν −
∫ z
−∞
hdν =
∫
R
kν (z,y )h′(y)dy (9)
and
− (1 −F(z))
∫
R
hdν +
∫
(z, ∞)
hdν =
∫
R
kν (z,y )h′(y)dy. (10)
By combining Theorem 1 and Corollary 3, we get the following c ovariance identity.
Proposition 4 Let ν be a probability measure on R and p,q ≥ 1 such that p−1 +q−1 = 1. Denote
Lh (x) =
∫ ∞
x hdν − (1 −F (x))
∫
Rhdν = F (x)
∫
Rhdν −
∫ x
−∞hdν for every x∈ R. If g ∈Lp (ν) and
h ∈Lq (ν) are absolutely continuous and if g′Lh is integrable with respect to the Lebesgue measure,
then
Cov (g,h ) =
∫
R
g′ (x) Lh (x)dx , (11)
Furthermore, if ν has a density p with respect to the Lebesgue measure that has a connected sup port,
then
Cov (g,h ) =
∫
R
g′ (x) ¯Lh (x)p (x)dx = E
[
g′ (X) ¯Lh (X)
]
, (12)
5
where, for every x ∈I (ν),
¯Lh (x) = p (x)−1 Lh (x)
= 1
p (x)
∫ ∞
x
hdν − 1 −F (x)
p (x) E [h] . (13)
If x /∈I (v), we take ¯Lh (x) = 0.
Proof. Identity (11) consists in applying Fubini theorem in the for mula of Theorem 1 and then
using Corollary 3. If ν has a density p with respect to the Lebesgue measure that has a connected
support then for every x /∈ I (ν) we have Lh (x) = 0. Consequently, from Identity (11) we get, for
g ∈L∞ (ν), h ∈L1 (ν) absolutely continuous,
Cov (g,h ) =
∫
I(ν)
g′ (x) Lh (x)dx
=
∫
I(ν)
g′ (x) ¯Lh (x)p (x)dx
and so Identity (12) is proved.
From Proposition 4, we can directly recover formula (6) for t he Stein kernel, when it is assumed
that the measure has a connected support and ﬁnite ﬁrst momen t. Indeed, by taking h (x) =x −µ,
we have h ν-integrable and diﬀerentiable and so, for any absolutely con tinuous function g ∈L∞ (ν)
such thatg′ ¯Lh isν-integrable, applying Identity (12) - sinceg′Lh =g′ ¯Lhp a.s. is Lebesgue integrable
- yields
Cov (g,h ) =
∫
R
(x −µ)g (x)p (x)dx =
∫
R
g′ ¯Lhdν . (14)
As by a standard approximation argument - i.e. truncations and an application of the dominated con-
vergence theorem -, identity (14) can be extended to any g such that the functions x ↦→(x −µ)g (x)
and x ↦→τν (x)g′ (x) are ν-integrable and [τνpg]b
a = 0, we deduce that a version of the Stein kernel
τv is given by ¯Lh, which is nothing but the right-hand side of Identity (6).
Following the nice recent survey [LRS17] related to the Stei n method in dimension one, identity
(12) is exactly the so-called ”generalized Stein covarianc e identity”, written in terms of the inverse
of the Stein operator rather than the Stein operator itself. Indeed, it is easy to see that the inverse
Tν of the operator ¯L acting on integrable functions with mean zero is given by the following formula
Tνf = (fp)′
p 1I(ν) ,
which is exactly the Stein operator (see Deﬁnition 2.1 of [LR S17]).
It is also well known, see again [LRS17], that the inverse of t he Stein operator, that is ¯L, is
highly involved in deriving bounds for distances between di stributions. From Corollary 3, we have
the following seemingly new formula for this important quan tity,
T −1
ν h (x) = ¯Lh (x) = 1
p (x)
∫
R
kν (x,y )h′(y)dy . (15)
Particularizing the latter identity with h (x) = x −µ, we obtain the following identity for the Stein
kernel,
τν (x) = 1
p (x)
∫
R
kν (x,y )dy . (16)
6
A consequence of (16) that will be important in Section 3 when deriving weighted functional in-
equalities is that for any x ∈ I (ν) the function y ↦→kν (x,y ) (p (x)τν (x))−1 can be seen as the
density - with respect to the Lebesgue measure - of a probabil ity measure, since it is nonnegative
and integrates to one.
We also deduce from (15) the following upper bound,
⏐⏐T −1
ν h (x)
⏐⏐ ≤ ‖h′‖∞
p (x)
∫
R
kν (x,y )dy = ‖h′‖∞
p (x)
(
F (x)
∫
R
xdν (x) −
∫ x
−∞
xdν (x)
)
,
which is exactly the formula given in Proposition 3.13(a) of [D¨ ob15].
Let us note ϕ (x) = − logp (x) when p (x) > 0 and + ∞ otherwise, the so-called potential of
the density p. If on I (ν), ϕ has derivative ϕ ′ ∈L1 (ν) absolutely continuous, then Corollary 2.3 in
[SW18a] gives ∫
R
kν (x,y )ϕ ′′(y)dy =p (x) .
Using the latter identity together with (15), we deduce the f ollowing upper-bound: if p is strictly
log-concave (that is ϕ ′′ > 0 on I (ν)), then
sup
x∈I(ν)
⏐⏐T −1
ν h (x)
⏐⏐ ≤ sup
x∈I(ν)
|h′ (x)|
ϕ ′′ (x) . (17)
In particular, if p is c-strongly log-concave, meaning that ϕ ′′ ≥ c >0 on R, then the Stein kernel
is uniformly bounded and ‖τν ‖∞ ≤ c−1. For more about the Stein method related to (strongly)
log-concave measures, see for instance [MG16].
Furthermore, by diﬀerentiating (15), we obtain for any x ∈I (ν),
(
T −1
ν h
) ′
(x) = ϕ ′ (x) T −1
ν h (x) −h (x) −
∫
R
F (y)h′ (y)dy
= ϕ ′ (x) T −1
ν h (x) −h (x) + E [h (X)] ,
that is (
T −1
ν h
) ′
(x) −ϕ ′ (x) T −1
ν h (x) = −h (x) + E [h (X)] .
This is nothing but the so-called Stein equation associated to the Stein operator.
We conclude this section with the following formulas, that are available when considering a density
with connected support and that will be useful in the rest of t he paper (see in particular Sections
3.2 and 5).
Proposition 5 Assume that X is a random variable with distribution ν having a density p with
connected support with respect to the Lebesgue measure on R. Take h ∈ L1 (ν) with E [h (X)] = 0
and assume that the function ¯Lh deﬁned in (13) is ν-almost surely strictly positive. We have, for
any x0,x ∈I (ν),
p (x) = E
[
h (X) 1{X≥x0}
]
¯Lh (x) exp
(
−
∫ x
x0
h (y)
¯Lh (y)dy
)
. (18)
Consequently, if X has a ﬁnite ﬁrst moment, for any x ∈I (ν),
p (x) = E [|X −µ |]
2τν (x) exp
(
−
∫ x
µ
y −µ
τν (y)dy
)
. (19)
7
By setting Th (x) = exp
(
−
∫ x
x0
h(y)
¯Lh(y)dy
)
and I (ν) = (a,b ), if the function h is ν-almost positive,
diﬀerentiable on (x,b ) and if the ratio Th (y)/h (y) tends to zero when y tends to b−, then we have,
for any x0,x ∈I (ν),
P (X ≥x) = E
[
h (X) 1{X≥x0}
] (Th (x)
h (x) −
∫ b
x
h′ (y)
h2 (y)Th (y)dy
)
. (20)
Formula (18) can also be found in [D¨ ob15], Equation (3.11), under the assumption that h is
decreasing and for a special choice of x0. Since E [h (X)] = 0, it is easily seen through its deﬁnition
(13), that if h ⁄= 0 ν −a.s. then ¯Lh >0 ν −a.s. When h = Id −µ, formulas (19) and (20) were
ﬁrst proved respectively in [NV09] and [Vie09], although wi th assumption that the random variable
X belongs to the space D1, 2 of square integrable random variables with the natural Hilb ert norm of
their Malliavin derivative also square integrable.
In order to take advantage of formulas (18) and (20), one has t o use some information about ¯Lh.
The most common choice is h =Id −µ, which corresponds to the Stein kernel ¯L (Id −µ) =τν.
Proof. Begin with Identity (18). As x0 ∈I (ν) and the function Lh deﬁned in (4) is ν-almost surely
positive, we have for any x ∈I (v),
Lh (x) = Lh (x0) exp
(∫ x
x0
(ln (Lh))′ (y)dy
)
.
To conclude, note that Lh (x0) = E
[
h (X) 1{X≥x0}
]
and (ln (Lh))′ = −h/ ¯Lh. To prove (19), simply
remark that is follows from (18) by taking h =Id −µ and x0 =µ.
It remains to prove (20). We have from (18), p = E
[
h (X) 1{X≥x0}
]
Th/ ¯Lh and by deﬁnition of
Th, T ′
h = −hTh/ ¯Lh. Hence, integrating between x and b gives
P (X ≥x) = E
[
h (X) 1{X≥x0}
] ∫ b
x
Th (y)
¯Lh (y)dy
= E
[
h (X) 1{X≥x0}
] ∫ b
x
−T ′
h (y)
h (y) dy
= E
[
h (X) 1{X≥x0}
]
([ −Th
h
] b
x
−
∫ b
x
h′ (y)Th (y)
h2 (y) dy
)
= E
[
h (X) 1{X≥x0}
] (Th (x)
h (x) −
∫ b
x
h′ (y)Th (y)
h2 (y) dy
)
.
