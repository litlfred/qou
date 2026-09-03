---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-061-limit-laws-from-probability-theory
section_title: "Limit laws from probability theory"
section_number: null
pages: 430-442
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
---
We now show how to use the techniques of ACSV to derive limit laws. Al-
though probabilistic interpretations and limit laws can hold for series with neg-
ative coeﬃcients, to simplify our presentation we restrict to the most common
case of a series F with nonnegative coe ﬃcients. Suppose the array {ar} en-
codes some combinatorial structure, and that the size of an object is given by
a mapγ(r) into the integers – most commonlyγ(r) = rd orγ(r) =|r|.
To discuss typical behavior, we deﬁne agrand measureµ onZd as a sum of
point mass measures
µ =
∑
r∈Zd
arδr,
whereδr(s) = 1 ifs =r and 0 otherwise, and normalize its slices
µk =
∑
γ(r)=k arδr
∑
γ(r)=k ar
12.8 Limit laws from probability theory 413
on the objects of size k to be probability measures. One can ask for limit laws
with varying degrees of subtlety. Aweak law tells us thatµk is concentrated on
a region of diameter o(k). More precisely, a weak law with limit m holds for
the sequence{µk} if, for anyε> 0,
µk
{
r :
⏐⏐⏐⏐⏐
r
k−m
⏐⏐⏐⏐⏐>ε
}
→ 0 (12.20)
as k→∞ . More delicate is a central limit theorem, which states that the distri-
bution ofµk in a region of diameterO(k1/2) around km has Gaussian behavior:
µk
{
r : r− km
k1/2 ∈ A
}
→ Φ(A) (12.21)
as k→∞ , where A is any “nice” region and Φ is a multivariate normal distri-
bution.
Exercise 12.1. When a central limit theorem holds, what (if anything) can you
conclude from (12.21) about the probabilities µk{⌊km⌋}, where the greatest
integer function is applied coordinatewise? What about the probabilities
µk
{
r :|r− km|
k > c
}
for ﬁxed c> 0 as k→∞ ?
Even better is a local central limit theorem (LCLT) which estimates µk at
individual points. A LCLT tells us thatµk(r)∼ n(r), where n is the density of
a multivariate normal distribution. In the case where the size parameter is rd,
for example, the normal density looks like
n(r) = (2π rd)(1−d)/2√
det N exp
[−1
2 (r◦− rdv)T N (r◦− rdv)
]
, (12.22)
wherer◦ denotes (r1,..., rd−1), the vectorv is the mean of the limit Gaussian
distribution, and the matrix N is the inverse covariance matrix. As we will see,
so-called Ornstein–Zernike behavior ar∼ C( ˆr)|r|(1−d)/2z−r leads to Gaussian
estimates for individual probabilities if the coordinates of z are nonnegative
real numbers. Ornstein–Zernike asymptotics are precisely the conclusion of
our asymptotic estimates in the case where there is a single smooth point and
the Hessian matrix is nondegenerate. Thus, all we require for a weak law and
LCLT is that asymptotics are governed by a single smooth point with nonde-
generate Hessian matrix. The remainder of this section is devoted to the state-
ment and proof of a weak law and local central limit theorem, holding under
smoothness and nondegeneracy assumptions.
Exercise 12.2. Suppose ar = 0 unless ∑d
j=1 r j is even.
414 Combinatorial applications
(a) How would you expect (12.22) to be altered?
(b) How would you expect this to be reﬂected in the generating function?
Weak laws
Unless otherwise speciﬁed, our results in this section apply to the power series
expansion of a generating function F(z) = P(z)/Q(z) with nonnegative coef-
ﬁcients, where Q is a polynomial containing all variables z1,..., zd. Conﬁning
our statements to power series rather than Laurent series simpliﬁes matters by
ensuring ﬁnite support of the cross-sectional measuresµk.
Theorem 12.31 (weak law for diagonal slices). Let q(z) = Q(z,..., z) and let
p > 0 be the smallest value such that q (p) = 0. If z = p is a strictly minimal
simple zero of q(z) and P(p,..., p) , 0 then the sequence{µk} of probability
measures deﬁned above satisﬁes a weak law (12.20) with limitm, where
m =−∇ log Q(p,..., p).
Proof The domain of convergence of the power series deﬁned by F cor-
responds to the component B of the complement of amoeba(Q)c that con-
tains all points of the form −(N,..., N) for all su ﬃciently large N > 0. In
fact, because B is convex the set of points ( x,..., x) for x ∈ R must inter-
sect ∂B (or else B would be all of Rd). Proposition 6.38 then implies that
q(ex) = Q(ex,..., ex) = 0 has a real solution, so the polynomial q has posi-
tive roots and p> 0 is well deﬁned.
Due to nonnegativity of the coe ﬃcients, every point of ∂B is a zero of Q◦
exp. Writep = (p,..., p) and deﬁne logp coordinate-wise. If∇ Q(p) = 0 then
q(z) would have a zero of order at least two atz = p, so our assumptions imply
∇ Q(p), 0, hence∇(Q◦ exp)(logp), 0 and the zero set of Q◦ exp in a real
neighborhood of logp is a smooth hypersurface normal tom.
Letting Z denote the real points of V, we claim that the logarithm maps
a neighborhood of p in Z into ∂B. Denoting the homeomorphism type of a
(d− 1)-ball with a distinguished interior point ( N, x), the intersection I of B
with a closed ball around logp is compact and, via projection from the center
of a sphere in the interior, has homeomorphism type ( N, x). By the implicit
function theorem, a neighborhood ofp in Z also has type (N, x). Any homeo-
morphism from one pair of type (N, x) to another covers a neighborhood of the
distinguished point. Therefore, the logarithm maps some neighborhood ofp in
Z into a neighborhood of logp in∂B, and we see that Z coincides locally with
∂B.
Thus, for anyr not parallel to m the maximum value of r·x overx∈ B
12.8 Limit laws from probability theory 415
is strictly greater than r· logp, so ar = O((p +ε)−|r|) for some ε >0 whose
choice is uniform as ˆr varies over any neighborhood not containing ˆm. The
generating function ∑
k≥0 Ckzk of the sequence Ck = ∑
γ(r)=k ar is F(z,..., z),
which has a strictly minimal simple pole at z = p. Proposition 3.1 then implies
that Ck ∼ cp−k for some constant c. In particular, ∑
r∈R ar = o(Ck) as k→
∞ whereR consists of all indices whose directions are in a compact set not
containing ˆm, so a weak law holds with limitm. □
Example 12.32 (multinomial distribution). Let c1,..., cd > 0 sum to 1 and let
F(z) = 1/(1− c·z) be the generating function for the multinomial distribution
ar =
( |r|
r1,..., rd
)
cr1
1··· crd
d
with parameters c. The denominator of F is Q(z) = 1− c·z. It follows that
Q(z,..., z) = 1−z regardless of c and the hypotheses of Theorem 12.31 are sat-
isﬁed with p = 1. Thus, there is a weak law with limitm =−∇ log Q(p,..., p) =
c, recovering the well-known weak law for repeated rolls of a die with weightsc.
◁
Often combinatorial classes are enumerated by a size parameter that is not
the sum|r| of the indices but is just one of the indices, say rd. A similar weak
law holds in this case, except that the probability measures{µk} no longer have
ﬁnite support and an added hypothesis is required. Adding this hypothesis al-
lows us to work with Laurent series, instead of only power series.
Theorem 12.33 (weak law for coordinate slices) . Let F (z) = P(z)/Q(z) =∑
r arzr be a Laurent series with nonnegative coe ﬃcients converging on a
component B of amoeba(Q)c. Suppose there is some p> 0 such that Q(1, p) =
0 and (0, log x)∈ B if and only if 0 < x < p. Then Ck = ∑
rd=k ar is ﬁnite for
all k and if z = p is also a strictly minimal simple zero of q (z) = Q(1, z) and
P(1, p), 0 then the sequence{µk} of probability measures deﬁned by
µk = 1
Ck
∑
rd=k
arδr
satisﬁes a weak law with limit
m =−∇ log Q(1, p).
Proof Arguing as in the proof of Theorem 12.31, we see again that exp(u)∈
V for everyu∈∂B and that∇(Q◦ exp) is nonvanishing at (0, log p). Because
(1, log x)∈ B for 0< x< p, we have convergence of the sum
F(1, zd) =
∑
rd=k
arzrd
d =
∑
k≥0
Ckzk
d
416 Combinatorial applications
whenever 0< zd < p, so Ck takes on ﬁnite values and its univariate generating
function has radius of convergence p. Just as in the proof of Theorem 12.31,
our hypothesis that q(z) has a simple strictly minimal zero at z = p implies
Ck ∼ cp−k for some constant c, and the total weight of µk is o(p−k) on sets
for which ˆr is bounded away from ˆm, since any hyperplane through (0, log p)
other than the hyperplane normal to the dth coordinate plane intersects the
interior of B. □
Example 12.34 (IID sums). Letµ be a probability measure on a ﬁnite subset
E⊆Zd−1. The spacetime generating function F for convolutions ofµ is given
by
F(z) =
∑
k≥0
∑
r∈Zd−1
µ(k)(r)z(r,k) = 1
1− zdφµ(z1,..., zd−1),
whereφµ is the (d− 1)-variable generating function for µ. Then 1 is a simple
pole of Q and is strictly minimal as long asφ is aperiodic. Directly,∇log Q(1) =
(m, 1), where m is the mean vector of µ. Theorem 12.33 then recovers the
weak law of large numbers for sums of IID samples fromµ. ◁
Remark. More generally, we may allow µ to be any measure on Zd−1 whose
moment generating function is ﬁnite everywhere. This takes us out of the the-
ory of amoebas of polynomials. However, all the facts that are required con-
cerning logarithmic domains of convergence still hold. Because we have not
developed the theory of analytic amoebas, we do not include a statement or
proof of this result. The greatest generality for weak laws via this type of ar-
gument is achieved by weakening the hypothesis to ﬁniteness of the moment
generating function in a neighborhood of the origin.
Exercise 12.3. Find a weak law for the binomial coe ﬃcients ars =
(r+s
s
)
with
generating function 1/(1− x− y) under the size γ(r, s) = r + 2s. Rather than
using Stirling’s formula, maximize m−1 log ars over r + 2s = m using that the
exponential growth of ars is x−ry−s where (x, y) = (r/(r + s), s/(r + s)) is the
critical point in the directionr = (r, s) computed in Example 9.10.
Central limits
We now derive a local central limit theorem for the proﬁle {ar : rd = k} as
k→∞ . Similar limit theorems for proﬁles such as{ar :|r| = k} also hold, but
the arguments are similar and we ﬁnd it simplest to stick to the case where the
size parameter is the last coordinate, mirroring classical limit theorems for the
spacetime generating function of a stochastic process onZd−1. We do, however,
12.8 Limit laws from probability theory 417
weaken our hypotheses to allowF to be a (non-rational) meromorphic function
in a suitable domain.
Before giving a limit theorem we need a lemma describing Ornstein–Zernike
behavior in this setting. We use the notation e j for the jth elementary unit
vector and recall the notation Te(x) for the set of complex vectors z with
(log|z1|,..., log|zd|) =x.
Lemma 12.35. Let F(z) = ∑
r∈Zd−1×N arzr be a d-variate series with logarith-
mic domain of convergence of convergence B⊆Rd. Suppose that B intersects
the negative ed-axis in the ray (−∞, t] for some real number t, that F is mero-
morphic on a neighborhood of the torus Te(0, t) with F (z) = P(z)/Q(z) for
analytic functions P and Q in a neighborhood of w = (1, et), and thatw is a
strictly minimal pole of F where Q zd(w) , 0. Then the logarithmic pole vari-
ety logV of F is a smooth complex analytic hypersurface in a neighborhood
of logw = (0, t).
Letm denote the vector (∇log Q)(1, et) scaled so that m d = 1, and let g
be the function parametrizing (x◦, xd)∈ logV by x d = g(x◦) near logw. If
the Hessian matrixH for g is nonsingular at the origin then as r varies over
a neighborhood of m in S = Rd−1×{ 1} the point w(r)∈ Vnearw with
(∇log Q)(w(r)) =r varies smoothly. In this case there is an Ornstein–Zernike
estimate
ar∼ (2π|rd|)(1−d)/2
√
sgn(rd) detH
·− sgn(rd)P(w(r))
zdQzd(w(r)) · exp(−r·w(r)). (12.23)
Proof The ﬁrst conclusion, that logV is a smooth complex analytic hypersur-
face near logw, follows from the implicit function theorem, since∇(Q◦ exp)
is nonvanishing at logw under our assumptions. Proposition 9.44 implies that
nonsingularity of the Jacobian of the Gauss map is equivalent to nondegener-
acy of the critical point w, and to nonvanishing of the Gaussian curvature of
V. Thus, the inverse of the mapz↦→ (∇log Q)(z) is smooth nearw andw(r)
varies smoothly with r. Theorem 9.4 and Remark 9.19 from Chapter 9 then
yield (12.23). □
Theorem 12.36 (LCLT). Let F be a d-variate generating function satisfying
the hypotheses of Lemma 12.35 and let M =H(0) denote the Hessian matrix
of g at the origin. If M is nonsingular then there is a constant c such that
etk ar◦,k∼ c nk(r◦)
as k→∞ with|r◦− km| = o(k2/3), where
nk(r◦) = (2πk)(1−d)/2
√
det M
exp
[
− 1
2k (r◦− km)T M−1(r◦− km)
]
(12.24)
418 Combinatorial applications
denotes the (d− 1)-variate normal density with mean km and covariance M.
It follows that
sup
r:rd=k
k(d−1)/2 ⏐⏐⏐etk ar− c n(r◦)
⏐⏐⏐→ 0
as k→∞ .
Remark. We can compute the constant c by comparing (12.23) and (12.24),
although a LCLT traditionally does not require knowledge of the normalizing
constant.
Proof Letx(r) = logw(r). Comparing (12.24) to (12.23) in Lemma 12.35,
it is suﬃcient to prove that the rate functionβ(r) =−r·x(r) satisﬁes
β(km +y) =− 1
2kyT M−1y + Ck + o(1)
as k→∞ with|y| = o(k2/3). The rate function is homogeneous of degree one,
so this is the same as
β(m +y) =−1
2yT M−1y + C′
k + o(k−1), (12.25)
where we have scaledy by 1/k so it is now restricted to be o(k−1/3).
The hyperplane with normal r going throughx(r) is a support hyperplane
to B, sox(r) is a minimizing point for−r·x on B. Whenr∈ S we may write
r = (r◦, 1), and we write x = (x◦, g(x◦)) for points x in a neighborhood of
x(m) in logV∩∂B. The functiong is concave, because locally the logarithmic
domain of convergence B is described by{(x, u) : u≤ g(x)} and logarithmic
domains of convergence are convex. Thus,
β(r◦, 1) = inf
x◦∈Rd−1
{−g(x◦)−r◦·x◦}
which is the negative of the convex dual of the convex function −g. As dis-
cussed in Chapter 6, the convex dual of the quadratic form x↦→ xT Ax rep-
resented by a positive deﬁnite matrix A is represented in the dual basis by the
inverse matrix r ↦→ rT A−1r. The quadratic Taylor expansion of the convex
dual at a pointr is determined by the quadratic Taylor expansion of the func-
tion (assuming this is nondegenerate) at the point where the minimum occurs.
The minimizing point for r =m is at the origin and the quadratic term in
the expansion of−g at the origin is the matrix−M representing the Hessian of
−g at the origin. Therefore the Taylor expansion ofβ aboutm on S is given by
β(m +y) =β(m)− 1
2yT M−1y + O(|y|3).
The condition|y| = o(k−1/3) is exactly what is needed for O(|y|3) to be o(k−1)
12.8 Limit laws from probability theory 419
and taking C′
k to beβ(m) (not depending on k after all) establishes (12.25) and
the ﬁrst conclusion.
Pickν with 1/2<ν< 2/3. When|r− km|≤ kν, the ﬁrst conclusion implies
that
|etk ar− c n(r)| = o(n(r)) = o(k(1−d)/2).
It remains to establish the second conclusion when |r− km|≥ kν, which we
do by showing that both terms being compared are small separately. The term
n(r) is in fact bounded above by exp(−ckν−1/2) for some c > 0. On the other
hand, when r∈ S the quantity r·x(r) diﬀers from its value at r = m by
at least a constant multiple of |r−m|2. In general, when rd = k the value of
r·x(r) diﬀers from its value at r = km by at least a constant multiple of
k−1|r− km|2. When|r− km|≥ kν this is of order at least k2ν−1, which is a
positive power of k. Plugging this into (12.23) shows that ar is also at most
exp(−ck2ν−1), completing the proof. □
Classical LCLT
We end by deriving the classical LCLT for sums of independent lattice ran-
dom variables whose moment generating functions are everywhere ﬁnite using
Theorem 12.36. Let µ be an aperiodic probability distribution on Zd, let µ(k)
denote the k-fold convolution ofµ, and let
F(z, zd+1) =
∑
(r,k)∈Zd×N
µ(k)(r)zrzk
d+1
denote the spacetime generating function for the random walk with increments
distributed asµ. The d-dimensional probability generating function φ forµ is
deﬁned by
φ(z) =
∑
r∈Zd
µ(r)zr
and ﬁniteness of the moment generating function implies φ is an entire func-
tion. The spacetime generating function F is related to the moment generating
functionφ for the distributionµ via
F(z) = 1
1− zd+1φ(z).
The singular variety of F is globally deﬁned by zd+1 = 1/φ(z) so the logarith-
mic singular variety is the graph of the function
g(x) =− logφ(exp(x)).
420 Combinatorial applications
Nonnegativity of series coeﬃcients implies that (x, t) is in the interior of the
domain of convergence when t < g(x), while no point ( x, g(x)) lies in the
logarithmic domain because it is on logV. Whenz is on the torus Te(x, g(x)),
aperiodicity implies that φ(z) , 0 unless z is real. Therefore, each point of
VR =V∩ Rd is the only point ofV on its torus, and such a minimal point is
strictly minimal.
As µ is a probability measure, g(0) = log(1) = 0. The chain rule further
implies
∂
∂x j
g(0) =− ∂
∂x j
(log◦φ◦ exp)(0) =−
e0φz j(exp(0))
φ(exp(0))
=−φz j(1),
and this partial derivative evaluates to∑
r∈Zd r jµ(r), so
m =−∇ (φ◦ exp)(0) =
∑
r∈Zd
rµ(r)
is the mean of the distributionµ. Diﬀerentiating again, if i, j we ﬁnd that
∂
∂xix j
g(0) =−
[exiex jφziz j◦ exp
φ◦ exp −
exiex j(φzi◦ exp)(φz j◦ exp)
(φ◦ exp)2
]
(0)
=φziz j(1)− mim j
so that the (i, j) entry of the Hessian of g at the origin is indeed the covariance
of the i and j coordinates underµ. A similar computation works for i = j and
establishes that the Hessian matrix of g at the origin is the covariance matrix
forµ. Applying Theorem 12.36, we see that µ(k)(r) is asymptotically equal to
c nk(r). There is no need to compute c because we know ∑
r◦µ(k)(r◦) = 1.
Thus c = 1 and we recover the classical LCLT.
Theorem 12.37. If µ is an irreducible aperiodic probability measure on Zn
with moment generating functionφ everywhere ﬁnite, then
µ(k)(r)∼ nk(r)
as k→∞ with|r−km| = o(k2/3), where nk is deﬁned by(12.24) with d = n+1,
the vectorm equal to the mean ofµ, and M equal to the covariance matrix of
µ. It follows that
sup
r∈Zd
kd/2|ar− n(r)|→ 0
as k→∞ . □
12.8 Limit laws from probability theory 421
Example 12.38. Recalling nonnegative Riordan arrays from Section 12.2, ob-
serve that setting x = 1 gives
µ(v; 1) = v′(1)
v(1)
and
σ2(v; 1) = v(1)v′′(1)− v′(1)2 + v(1)v′(1)
v(1)2 .
Thus, when the hypotheses of Theorem 12.33 are satisﬁed, a WLLN holds with
meanm =µ(v; 1). Hereµ(v; 1) is simply the mean of the renormalized distri-
bution on the nonnegative integers with probability generating function v, and
σ2(v; 1) is the variance of the renormalized distribution. The quadratic form in
the exponent of (12.24) in Theorem 12.36 is given by (s−µ(v; 1)r)2/(2kσ2(v; 1)),
meaning a local central limit theorem holds with varianceσ2(v; 1). ◁
Exercise 12.4. Large deviation theory is used to provide bounds on µ(k){|r−
km| > Ck}, which are exponentially small in k. What bounds on this kind of
event follow from Theorem 12.37?
Notes
The material in Sections 12.2 and 12.3 is largely taken from [PW08, Sec-
tion 4.3], as is the message passing example in Section 12.4. The idea for
Exercise 12.6 comes from [Nob10], and Exercise 12.8 comes from [PW02, Ex-
ample 3.4]. Exercise 12.9 is suggested by a line of work on rook walks, see for
example [KZ11]. The results of Exercise 12.10 are generalized in [Wil15] to
diagonal asymptotics of products of combinatorial classes. Elementary deriva-
tions of some of the limit theorems presented here are given in Melczer [Mel21,
Section 5.3.3].
Riordan arrays have been widely studied. In addition to enumerating a great
number of combinatorial classes, Riordan arrays also behave in an interest-
ing way under matrix multiplication (note that the condition v(0) = 0 implies
ank = 0 for k< n, and, by triangularity of the inﬁnite array, that multiplication
in the Riordan group is well deﬁned). Surveys of the Riordan group and its
combinatorial applications may be found in [Spr94; Sha+91].
There are many multivariate generalizations of the Lagrange Inversion For-
mula, but we know of none that are useful for our purposes. Proposition 12.8
was given in [Wil05]. The asymptotic behavior of univariate QRWs is derived
in several papers, of which [CIR03] is perhaps the most complete. Some of
422 Combinatorial applications
our presentation comes from [BP07], and our second QRW example comes
from [Bar+10, Section 4.1].
It is an interesting question to pick how many terms to compute in an asymp-
totic expansion when the goal is to numerically approximate a ﬁxed coeﬃcient.
The books [PK01; Par11] give a good introduction, and applications to inte-
grals arising from coeﬃcient extraction are treated in [DH02].
Additional exercises
Exercise 12.5. (general Lagrange inversion) Use the change of variables de-
scribed in the proof of Proposition 12.7 and the exact diﬀerential d
[ψ(y)
n
( v(y)
y
)n]
to prove the more general Lagrange inversion formula (12.13).
Exercise 12.6. Compute dominant asymptotics for µ(n, n), where µ(m, n) =∑n
k=0(−1)k
(n
k
)(2m
k
)
. Hint: Replace−1 by z, multiply by xmyn and sum overk, m, n
to obtain a trivariate generating function.
Exercise 12.7. Using the results in Section 12.2, compute asymptotics for the
generalized Dyck paths described in Section 2.3.
Exercise 12.8. Let F(x, y) = 1/(3− 3x + x2− y) be the generating function
of a generalized Riordan array{ars}. Compute asymptotics for directions (r, s)
when r/s> 1, then do the same thing when 0 < r/s< 1. What happens when
r = s?
Exercise 12.9. Let ar count the number of ways in which a chess rook can
move from the origin to r by moves that increase one coordinate and do not
decrease any other. The methods of Chapter 2 yield the generating function
F(z) =
∑
r∈Nd
arzr = 1
1− ∑d
i=1
zi
1−zi
=
∏d
i=1(1− zi)
∑d
j=0(−1) j( j + 1)e j(z)
,
where e j is the jth elementary symmetric polynomial.
a) Use Theorem 2.32 in Chapter 2 to ﬁnd the generating function of the main
diagonal of F when d = 2. What happens when you try this for d = 3?
b) Compute the ﬁrst-order asymptotic approximation to ar for d = 3.
c) Use a computer algebra system, or write your own program, to compute ar
exactly, for values of d up to 10. Compare with the ﬁrst-order asymptotic
whenr = (100,..., 100).
12.8 Limit laws from probability theory 423
d) Compute the next term in the expansion and determine how much better
is the accuracy of the 2-term asymptotic approximation when d = 3 and
r = (100, 100, 100).
Exercise 12.10. Derive the bivariate generating function∑
r,s≥0 ars xrys for the
number of ordered pairs of ordered sequences of integers with parts in a ﬁxed
set A⊂ N, the ﬁrst summing to r and the second to s, each having the same
number of parts. Compute the asymptotics of the coe ﬃcients on the main di-
agonal. Compare your results and methods with those in [BH12].
Exercise 12.11. Prove that embedding an algebraic generating functionA into
a rational one R using the method of Lemma 2.36 always makes the numerator
of R vanish at the contributing points of R.
13
