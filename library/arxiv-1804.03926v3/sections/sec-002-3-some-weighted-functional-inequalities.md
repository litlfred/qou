---
doc_id: arxiv-1804.03926v3
doc_title: "Weighted Poincaré inequalities, concentration inequalities and tail bounds related to Stein kernels in dimension one"
section_id: sec-002-3-some-weighted-functional-inequalities
section_title: "Some weighted functional inequalities"
section_number: 3
pages: 8-14
source_pdf: 1804.03926v3.pdf
source_sha256: 8ad8e2d5a8881a5b
---
Weighted functional inequalities appear naturally when generalizing Gaussian functional inequalities
such as Poincar´ e and log-Sobolev inequalities. They were put to emphasis for the generalized Cauchy
distribution and more generalκ-concave distributions by Bobkov and Ledoux [BL09b, BL09a], also in
connection with isoperimetric-type problems, weighted Ch eeger-type inequalities and concentration
of measure. Then several authors proved related weighted fu nctional inequalities ([BCG08, BJ14,
BJM16a, BJM16b, CGGR10, CGW11, CEG17, Goz10]). In the follo wing, we show the strong con-
nection between Stein kernels and the existence of weighted functional inequalities. Note that a
remarkable ﬁrst result in this direction was recently estab lished by Courtade et al. [CFP17] who
8
proved that a reversed weighted Poincar´ e inequality is suﬃcient to ensure the existence of a Stein
kernel in Rd, d ≥ 1.
Our results are derived in dimension one. Indeed, the proofs of weighted Poincar´ e inequalities
(Section 3.1) and asymmetric Brascamp-Lieb type inequalit ies (Section 3.3) rely on covariance iden-
tities stated in Section 2, that are based on properties of cu mulative distribution functions available
in dimension one. Recently, Fathi [Fat18] generalized in hi gher dimension the weighted Poincar´ e
inequalities derived in Section 3.1 using transportation t echniques. We also derive in Section 3.2
some weighted log-Sobolev inequalities, that are derived t hrough the use of some Muckenhoupt-type
criteria that are only valid in dimension one. However, it is natural to conjecture a multi-dimensional
generalization, especially using tools developed in [Fat1 8], but this remains an open question. Fi-
nally, using a formula for the isoperimetric constant in dim ension one due to Bobkov and Houdr´ e
[BH97], we prove that a uniformly bounded Stein kernel is ess entially suﬃcient to ensure a positive
isoperimetric constant. Again, the problem in higher dimen sion seems much more involved and is
left as an interesting open question.
3.1 Weighted Poincar´ e-type inequality
According to [BL09b], a measure ν on R is said to satisfy a weighted Poincar´ e inequality if there
exists a nonnegative measurable weight function ω such that for any smooth function f ∈L2 (ν),
Var (f (X)) ≤ E
[
ω (X)
(
f ′ (X)
) 2]
. (21)
The following theorem shows that a probability measure havi ng a ﬁnite ﬁrst moment and density
with connected support on the real line satisﬁes a weighted P oincar´ e inequality, with the weight
being its Stein kernel.
Theorem 6 Take a real random variable X of distribution ν with density p with respect to the
Lebesgue measure on R. Assume that E [|X|] < +∞, p has a connected support and denote τν the
Stein kernel of ν. Take f ∈L2 (ν), absolutely continuous. Then
Var (f (X)) ≤ E
[
τν (X)
(
f ′ (X)
) 2]
. (22)
The preceding inequality is optimal whenever ν admits a ﬁnite second moment, that is E
[
X 2]
< +∞,
since equality is reached for f =Id, by deﬁnition of the Stein kernel.
Proof. We have
Var (f (X)) = E
[
√
τν (X)f ′ (X)
¯Lf (X)√
τν (X)
]
≤
√
E
[
τν (X) (f ′ (X))2
]
/radicaltp/radicalvertex/radicalvertex√ E
[
τν (X)
( ¯Lf (X)
τν (X)
) 2]
.
By the use of Jensen’s inequality, for any x ∈I (ν),
( ¯Lf (x)
τν (x)
) 2
=
(∫
f ′ (y) kν (x,y )∫
kν (x,z )dzdy
) 2
≤
∫ (
f ′ (y)
) 2 kν (x,y )∫
zkν (x,z )dzdy
=
∫ kν (x,y )
τν (x)p (x)
(
f ′ (y)
) 2dy .
9
Hence,
E
[
τν (X)
( ¯Lf (X)
τν (X)
) 2]
≤
∫
τv (x)p (x)
(∫ kν (x,y )
τν (x)p (x)
(
f ′ (y)
) 2dy
)
dx
=
∫ ∫
kν (x,y )
(
f ′ (y)
) 2dxdy
=
∫
τν (y)
(
f ′ (y)
) 2p (y)dy ,
which concludes the proof.
It is worth mentioning that the famous Brascamp-Lieb inequa lity provides another weighted
Poincar´ e inequality in dimension one: if ν is strictly log-concave, of density p = exp (−ϕ ) with a
smooth potential ϕ , then for any smooth function f ∈L2 (ν),
Var (f (X)) ≤ E
[ (
ϕ ′′ (X)
) −1(
f ′ (X)
) 2]
. (23)
In particular, if ν is strongly log-concave (that is ϕ ′′ ≥ c >0 for some constant c >0), then both
the Brascamp-Lieb inequality (23) and inequality (22) - com bined with the estimate ‖τν ‖∞ ≤ c−1
coming from inequality (17) - imply the Poincar´ e inequality Var (f (X)) ≤c−1E
[
(f ′ (X))2
]
, that also
follows from the Bakry-´Emery criterion. However, in general, the Stein kernel appe aring in (22) may
behave diﬀerently from the inverse of the second derivative o f the potential and there is no general
ordering between the right-hand sides of inequalities (22) and (23).
Indeed, let us discuss the situation for a classical class of examples in functional inequalities,
namely the class of Subbotin densities pα (x) = Z −1
α exp (− |x|α /α ) for x ∈ R, where Zα > 0 is the
normalizing constant. Recall that densities pα are not strongly log-concave and do not satisfy the
Bakry-´Emery criterion - except forα = 2 which corresponds to the normal density - but they satisfya
Poincar´ e inequality if and only ifα ≥ 1 and a log-Sobolev inequality if and only if α ≥ 2 (see [LaO00]
and also [BJ14] for a thorough discussion on optimal constan ts in these inequalities). We restrict
our discussion to the condition α> 1 for which pα is strictly log-concave, so that the Brascamp-Lieb
inequality applies. More precisely, by writingpα = exp (−ϕ α ), we have (ϕ ′′)−1 (x) = (α − 1)−1 |x|2−α .
Using the explicit formula (16) for the Stein kernel and an in tegration by parts, one can easily check
that if α ∈ (1, 2), then τα (x) < |x|2−α where τα is the Stein kernel associated to pα . We thus get,
forα ∈ (1, 2), (ϕ ′′)−1 (x)>τ α (x) for anyx ∈ R and so the Brascamp-Lieb inequality is less accurate
than Theorem 6 in this case. Furthermore, if α> 2 then τα (x)> |x|2−α and so (ϕ ′′)−1 (x)<τ α (x)
for anyx ∈ R, which means that the Brascamp-Lieb inequality is more accu rate than Theorem 6 for
α> 2. However, we can not recover through the use of Theorem 6 - or the Brascamp-Lieb inequality
- the existence of a spectral gap for α ∈ [1, 2). Finally, Theorem 6 gives us the existence of some
weighted Poincar´ e inequalities for anyα > 0, whereas Brascamp-Lieb inequality only applies for
α> 1.
It is also worth mentioning that Theorem 6 has been recently g eneralized to higher dimension by
Fathi [Fat18], for a Stein kernel that is a positive deﬁnite m atrix and that is deﬁned through the use
of a so-called moment map. The proof of this (non-trivial) ex tension of our result is actually based
on the Brascamp-Lieb inequality itself, but applied to a mea sure also deﬁned through the moment
map problem.
Let us now detail some classical examples falling into the se tting of Theorem 6.
The beta distribution Bα,β , α,β > 0 is supported on (0, 1), with density pα,β given by
pα,β (x) = xα −1 (1 −x)β −1
B (α,β ) , 0 <x< 1. (24)
10
The normalizing constantB (α,β ) is the classical beta function of two variables. The beta distribution
has been for instance recently studied in [BL14] in connecti on with the analysis of the rates of
convergence of the empirical measure on R for some Kantorovich transport distances. The Stein
kernelτα,β associated to the Beta distribution is given byτα,β (x) = (α +β)−1x (1 −x) forx ∈ (0, 1)
(see for instance [LRS17]) and thus Theorem 6 allows to exact ly recover Proposition B.5 of [BL14]
(which is optimal for linear functions as noticed in [BL14]) . Our techniques are noticeably diﬀerent
since the weighted Poincar´ e inequality is proved in [BL14]by using orthogonal (Jacobi) polynomials.
Notice also that the beta density pα,β is strictly log-concave on the interior of its support. Inde ed,
by writing pα,β = exp
(
−ϕ α,β
)
, we get, for any x ∈ (0, 1),
(
ϕ ′′) −1 (x) = x2 (1 −x)2
(α − 1) (1 −x)2 + (β − 1)x2 .
Remark that, for instance, (ϕ ′′)−1 (x) ∼x→0+ x2/ (α − 1), whereas τα,β (x) ∼x→0+ x/ (α +β), so the
weights in the Brascamp-Lieb inequality (23) and in inequal ity (22) are not of the same order at
0 (or by symmetry at 1), although it is also easy to show that th ere exists a constant cα,β > 0 -
cα,β = (α +β)/
(
2
√
(α − 1) (β − 1)
)
works - such that (ϕ ′′)−1 (x) ≤cα,β τα,β (x) for any x ∈ (0, 1).
Note that considering Laguerre polynomials, that are eigen functions of the Laguerre operator for
which the Gamma distribution is invariant and reversible, o ne can also show an optimal weighted
Poincar´ e inequality for the Gamma distribution, which include as a special instance the exponential
distribution (see [BL97] and also [BGL14], Section 2.7). Th eorem 6 also gives an optimal weighted
Poincar´ e inequality for the Gamma distribution and more generally for Pearson’s class of distributions
(see below).
Note also that the beta distribution seems to be outside of th e scope of the weighted Poincar´ e
inequalities described in [BJM16a] since it is assumed in th e latter article that the weight of the
considered Poincar´ e-type inequalities is positive onR, which is not the case for the beta distribution.
Furthermore, [BL14] also provides some weighted Cheeger in equality for the Beta distribution, but
such a result seems outside the scope of our approach based on covariance identity (8). When
considering concentration properties of beta distributions in Section 4 below, we will however provide
some improvements compared to the results of [BL14].
Furthermore, it has also been noticed that the generalized Cauchy distribution satisﬁes a weighted
Poincar´ e distribution, which also implies in this case a re verse weighted Poincar´ e inequality (see
[BL09b, BJM16a]). In fact, [BL09b] shows that the generaliz ed Cauchy distribution plays a central
role when considering functional inequalities for κ-concave measures, with κ< 0.
The generalized Cauchy distributionνβ of parameterβ >1/ 2 has densitypβ (x) =Z −1
β
(
1 +x2) −β
for x ∈ R and normalizing constant Zβ > 0. Its Stein kernel τβ exists for β > 1 and writes
τβ (x) =
(
1 +x2)
/ (2 (β − 1)). This allows us to recover in the case where β >3/ 2 - that is νβ has a
ﬁnite second moment - the optimal weighted Poincar´ e inequality also derived in [BJM16a], Theorem
3.1. Note that Theorem 3.1 of [BJM16a] also provides the opti mal constant in the weighted Poincar´ e
inequality with a weight proportional to 1 + x2 in the range β ∈ (1/ 2, 3/ 2].
Let us conclude this short list of examples by mentioning Pea rson’s class of distributions, for
which the density p is solution to the following diﬀerential equation,
p′ (x)
p (x) = α −x
β 2 (x −λ)2 +β 1 (x −λ) +β 0
, (25)
for some constantsλ,α,β j,j = 0, 1, 2. This class of distributions, that contains for instance Gaussian,
Gamma, Beta and Student distributions, has been well studie d in the context of Stein’s method, see
11
[LRS17] and references therein. In particular, if a density satisﬁes (25) with β 2 ⁄= 1/ 2, then the
corresponding distribution ν has a Stein kernel τν (x) = (1 − 2β 2)−1(
β 0 +β 1x +β 2x2)
, for any x ∈
I (ν). Particularizing to the Student distribution tα with densitypα proportional to
(
α +x2) −(1+α )/ 2
on R for α> 1, we get that for any smooth function f ∈L2 (tα ),
Vartα (f) ≤ 1
α − 1
∫ (
x2 +α
)
f ′2 (x)dtα (x) .
We will investigate concentration inequalities in Section 4. In fact, existence of a weighted
Poincar´ e inequality already implies concentration of mea sure. The following corollary is a direct
consequence of Theorem 4.1 and Corollary 4.2 in [BL09b], in l ight of Theorem 6 above.
Corollary 7 Take a real random variable X of distribution ν with density p with respect to the
Lebesgue measure on R. Assume that E [|X|] < +∞, p has a connected support and denote τν the
Stein kernel of ν. Assume that √τν has a ﬁnite rth moment, r ≥ 2. Then any Lipschitz function f
on R has a ﬁnite rth moment. More precisely, if f is 1-Lipschitz and E [f] = 0, then
‖f ‖r ≤ r√
2
‖√τν ‖r . (26)
Furthermore, by setting t1 =
‖‖√τν
‖‖
rer, it holds
ν (|f | ≥ t) ≤
{
2e−t/ (‖√τ ν ‖re),
2
(‖√τ ν ‖rr
t
) r
,
if 0 ≤t ≤t1,
if t ≥t1.
Inequality (26) of Corollary 7 may be compared to Theorem 2.8 in [LNP15]. Indeed, under the
conditions of Corollary 7, Theorem 2.8 in [LNP15] applies an d gives the following bound,
‖f ‖r ≤C
(
Sr (ν |γ ) + √r ‖√τν ‖r
)
, (27)
where Sr (ν |γ ) = ‖τν − 1‖r is the so-called Stein discrepancy of order r of the measure measure ν
with respect to the normal distribution γ andC >0 is a numerical constant, independent of r. Note
that the latter inequality is in fact derived in [LNP15] in higher dimension (for a matrix-valued Stein
kernel) and is thus from this point of view much more general t han Inequality (26) above.
Considering a measure ν with a uniformly bounded Stein kernel, as it is the case for a s mooth
perturbation of the normal distribution that is Lipschitz a nd bounded from zero (see Remark 2.9
in [LNP15]), for a bounded perturbation a measure with bound ed Stein kernel (see Section 3.4
below for details) or for a strongly log-concave measure as p roved in Section 2 above, Inequality
(26) only implies a moment growth ‖f ‖r = O (r) corresponding to exponential concentration of f
- which is legitimate since in this case the weighted Poincar ´ e inequality (62) is roughly equivalent
to a Poincar´ e inequality, the latter classically implying exponential concentration rate - whereas
Inequality (27) allows to deduce a sub-Gaussian moment grow th ‖f ‖r = O (√r). Using a suitable
covariance inequality, we will also recover in Section 4 bel ow a sub-Gaussian concentration rate for
a measure admitting a uniformly bounded Stein kernel.
Notice also that as soon as the moment
‖‖√τν
‖‖
r grows with r, the moment growth of ‖f ‖r given
by (26) is stricly worst than the rate O (r) that is achieved by the exponential concentration rate.
However, considering for instance the exponential distrib ution dνe = exp (−x) 1 {x ∈ [0; +∞[}dx,
its Stein kernel is given by τν e (x) =x on R+ and it is easy to see that Inequality (27) again allows
to recover the right exponential concentration rate, on con trary to (26) that is sub-optimal in this
12
case. The concentration of measures having a sub-linear Ste in kernel is also investigated in Section
4 below.
Weakening again the concentration rate, let us consider a generalized Cauchy measureνβ , of den-
sity proportional to
(
1 +x2) −β ,β >1. Its Stein kernel exists and it holds,τν β (x) =
(
1 +x2)
/ (2 (β − 1)).
In this case, basic computations give that Inequality (26) e nsures that for any r <2β − 1, ‖f ‖r is
ﬁnite for any centered Lipschitz function f, whereas Inequality (27) yields a ﬁnite estimate only for
r < β− 1/ 2. Consequently, (26) allows to consider higher moments tha n (27) for the generalized
Cauchy distributions.
Fathi et al. [CFP17] proved that if a probability measure on Rd,d ≥ 1, satisﬁes a converse
weighted Poincar´ e inequality, then a Stein kernel exists f or this measure and the authors further
provide an estimate of the moment of order two of the Stein ker nel under a moment assumption
involving the inverse of the weight.
Actually, a slight modiﬁcation of the arguments provided in [CFP17] shows that, reciprocally
to Theorem 6, if a probability measure satisﬁes a (direct) we ighted Poincar´ e inequality then there
exists a natural candidate for the Stein kernel, in the sense that it satisﬁes equation (5) on W 1, 2
ν,ω ,
the (weighted) Sobolev space deﬁned as the closure of all smo oth functions in L2 (ν) with respect
to the Sobolev norm
∫(
f 2 +f ′2ω
)
dν. However, to deﬁne a Stein kernel, it is usually required tha t
equation (5) is satisﬁed on W 1, 2
ν , the Sobolev space deﬁned as the closure of all smooth functi ons in
L2 (ν) with respect to the Sobolev norm
∫
f 2 +f ′2dν, see for instance [LNP15] and [CFP17]. As we
can assume without loss of generality that ω ≥ 1, we only have in general W 1, 2
ν,ω ⊂W 1, 2
ν .
Theorem 8 Assume that a probability measure ν on R with mean zero and ﬁnite second moment
satisﬁes a weighted Poincar´ e inequality (21) with weight ω . Denote W 1, 2
ν,ω the Sobolev space deﬁned
as the closure of all smooth functions in L2 (ν) with respect to the Sobolev norm
∫(
f 2 +f ′2ω
)
dν.
Then there exists a function ˜τν , satisfying equation (5) on W 1, 2
ν,ω such that
∫
˜τ2
νω −1dν ≤
∫
x2dν . (28)
If ˜τν ∈ L2 (ν), the weight ω is locally bounded and the measure has a density p that is also locally
bounded, then ˜τν is a Stein kernel in the sense that equation (5) is satisﬁed on W 1, 2
ν .
One can notice that working with the Stein discrepancy - as for instance in [LNP15] and [CFP17]
- requires that the Stein kernel is square integrable. In The orem 8, we state that if ˜τν ∈L2 (ν), the
weightω is locally bounded and the measure has a density p that is also locally bounded, then ˜τν is
indeed a Stein kernel.
Proof. The proof is a simple modiﬁcation of the proof of Theorem 2.4 in [CFP17]. We give it for the
sake of completeness. Set W 1, 2
ν,ω, 0 =W 1, 2
ν,ω ∩
{
f ∈L2 (ν) :
∫
fdν = 0
}
. Then
∫
f ′g′ωdν is a continuous
bilinear form on W 1, 2
ν,ω, 0 ×W 1, 2
ν,ω, 0 and is coercive by the weighted Poincar´ e inequality (21). So by the
Lax-Milgram theorem, there exists a unique g0 ∈W 1, 2
ν,ω, 0 such that
∫
f ′g′
0ωdν =
∫
xfdν
13
for any f ∈W 1, 2
ν,ω, 0. Hence, τν =g′
0ω is a Stein kernel for ν. Furthermore, we have
∫
g′2
0ωdν =
∫
xg0dν
≤
√ ∫
g2
0dν
√ ∫
x2dν
≤
√ ∫
g′2
0ωdν
√ ∫
x2dν
Noticing that ω > 0 a.s. on I (ν), we have
∫
g′2
0ωdν =
∫
τ2
νω −1dν, which gives (28). Now, if ω and
p are locally bounded, then C ∞
c ⊂ W 1, 2
ν,ω where C ∞
c is the set of inﬁnitely diﬀerentiable functions
with compact support. So, by density of C ∞
c in W 1, 2
ν (which since p is locally bounded follows from
the same arguments as the classical density of C ∞
c in the usual Sobolev space with respect to the
Lebesgue measure, see for instance Theorem 6.15 in [LL01]), as ˜τν ∈ L2 (ν) and as ν has a ﬁnite
second measure, equation (5) is valid on W 1, 2
ν .
Note that for ease of presentation, we stated Theorem 8 in dim ension one, but it is seen from the
proof above that it directly extends to Rd,d ≥ 2, by considering the Hilbert-Schmidt scalar product
between matrices - since the Stein kernel is matrix-valued - just as in [CFP17].
