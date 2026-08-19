---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-007-2-borel-resummation-and-stokes-automorphisms
section_title: "Borel resummation and Stokes automorphisms"
section_number: 2
pages: 9-24
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
2.1. Borel resummation. In this section we brieﬂy review the process of Borel resumma-
tion of a factorially divergent series, its Laplace integral along rays and the corresponding
Stokes automorphism across a Stokes ray. The material in this section is classical and well-
known and is explained in detail in the books [Cos09, Mil06, MS16], and in the references
therein. We will be following the physics convention of Borel resummation as found for ex-
ample in [Mn15, Sec. 3.2] and [ZJ93, Sec.42.5], which diﬀers by a factor ofτ from the Borel
resummation found in the math literature.
Borel resummation is a 2-step process to pass from a factorially divergent seriesF (τ) to
the analytic functions(F )(τ) deﬁned in the right half-planeRe(τ) > 0 summarized in the
following diagram
F (τ)↝ ˆF (ζ)↝s(F )(τ). (23)
10 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
Here one starts with a Gevrey-1 a formal power seriesF (τ)
F (τ) =
∞∑
n=0
fnτn, f n =O(Cnn!) (24)
and deﬁnes its Borel stransformˆF (ζ) by
ˆF (ζ) =
∞∑
n=0
fn
n!ζn. (25)
It follows thatˆF is the germ of an analytic function atζ = 0. If it analytically continues
to anL1-analytic function along the rayρθ := eiθR+ where θ = argτ, we deﬁne its Laplace
transform by
sθ(F )(τ) =
∫ ∞
0
ˆF (τζ )e−ζdζ = 1
τ
∫
ρθ
ˆF (ζ)e−ζ/τ dζ (26)
The functions(F )(τ) is often called the Borel resummation of the formal power seriesF, and
we often suppress the subscriptθ = 0 when τ is real and positive. If we varyθ = argτ and
we do not encounter singularities ofˆF, the functionsθ(F )(τ) is locally analytic. Thus, the
problem is to understand the analytic continuation ofˆF and to analyze what happens to the
Borel resummationsθ(F )(τ) when θ = arg(τ) crosses a Stokes ray, i.e., a ray in Borel plane
that contains one or more singularities ofˆF. This is described by a Stokes automorphism.
2.2. Stokes automorphism. We will specialize our discussion to the series of interest,
namely to the Borel transform ˆΦ(x;ζ) of the vector of series Φ(x;τ). The singularities
of Φ(x;τ) are conjectured to be in the set (13) that generates a set of Stokes rays whose
complement is a countable union of open cones in Borel plane. Whenθ is in a ﬁxed such cone
C, the Laplace transformsθ(Φ)(x;τ) depends onC but not onθ. To compare two adjacent
such cones, letι(𝓁,k)
σ,σ′ denote one of the singularities ofΦσ(x;τ), θ denote its argument and
ρ = eiθR + denote the corresponding Stokes ray. Whenx is generic, a Stokes ray contains a
single singularity and the Laplace integrals to the right and the left ofρ are related by
sθ+(Φσ)(x;τ) =sθ−(Φσ)(x;τ) +S(𝓁,k)
σ,σ′ ˜x𝓁˜qksθ−(Φσ′)(x;τ), (27)
whereS(𝓁,k)
σ,σ′ is the Stokes constant. In matrix form, the above formula reads
sθ+(Φ)(x;τ) = Sθ(˜x; ˜q)sθ−(Φ)(x;τ) (28)
where
Sθ(˜x; ˜q) =I +S(𝓁,k)
σ,σ′ ˜x𝓁 ˜qkEσ,σ′ (29)
where Eσ,σ′ is the elementary matrix with(σ,σ′)-entry 1 and all other entries zero.
More generally, consider two non-Stokes raysρθ+ and ρθ− whose arguments satisfy 0≤
θ+−θ−≤π. Then, the Laplace integrals are related by
sθ+(Φ)(x;τ) = Sθ−→θ+(˜x; ˜q)sθ−(Φ)(x;τ) (30)
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 11
where the Stokes matrices satisfy the factorization property
Sθ−→θ+(˜x, ˜q) =
←−∏
θ−<θ<θ+
Sθ(˜x, ˜q). (31)
where the ordered product is taken over the Stokes rays in the cone genarated byρθ− and
ρθ+. This factorization is well-known in the classical litetature on WKB (see for instance
Voros [Vor83, p.228] who called it the “radar method” for obvious visual reasons). In our
case, there are four special non-Stokes rays denoted by
I = eiϵR +, II = ei(π−ϵ)R +, III = ei(π+ϵ)R +, IV = ei(2π−ϵ)R + (32)
(for ϵ > 0 and suﬃcently small) that belong to the four distinguished cones (labeled
I,II,III,IV ) adjacent to the real axis and free of Stokes lines. The corresponding Stokes
matrices
S+(˜x; ˜q) = SI→II (˜x; ˜q) SIV→I(˜x; ˜q), S−(˜x; ˜q) = SIII→IV (˜x; ˜q) SII→III (˜x; ˜q) (33)
that swap two complementary and nearly horizontal half-planes separated by a lineL are
the ones that appear in Conjecture 3. They are related to the matricesMρ in the second
part of that conjecture by
SI→II (˜x; ˜q) = (MII (˜x; ˜q))−1·MI(˜x; ˜q), |˜q|< 1
SIII→IV (˜x; ˜q) = (MIV (˜x; ˜q−1))−1·MIII (˜x; ˜q−1), |˜q|< 1
SIV→I(˜x; ˜q) = (MI(˜x; ˜q))−1·MIV (˜x; ˜q),
SII→III (˜x; ˜q) = (MIII (˜x; ˜q))−1·MII (˜x; ˜q). (34)
We now come to an important feature of our resurgent series, a unique factorization prop-
erty for the Stokes matrices reminiscent of the “stability data” description of DT-invariants in
Kontsevich-Soibelman [KS11, KS, KS14]), and of the properties of BPS spectrum generators
in Gaiotto-Moore-Neitzke [GMN10, GMN13, GMN12].
Lemma 8. S uniquely determines Sθ for allθ.
Proof. Without loss of generality, we will show that S+ uniquely determines the Stokes
matrices Sθ for allθ such that−ε<θ <π −ε for ε> 0 and suﬃciently small. We have
S+(˜x; ˜q) =
←−∏
σ,σ′,k,𝓁
(I +S(𝓁,k)
σ,σ′ ˜x𝓁 ˜qkEσ,σ′) (35)
where the product is over all the singularities above the lineL. The entries of the above
matrices are in the ringZ [˜x±][[˜q]]. For each ﬁxed natural numberN, there are only ﬁnitely
many horizontal lines of singularities in Borel plane, of height at mostN and within those,
there are ﬁnitely many˜x-dots. It follows by induction onk that the ﬁnite collection{S(𝓁,k)
σ,σ′}𝓁
is uniquely determined fromS+(˜x; ˜q). □
It follows that we can repackage the information of the Stokes constants in two matrices
S+ andS− deﬁned by
12 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
S±(˜x; ˜q) =
∑
𝓁,k
S(𝓁,k)
σ,σ′ ˜x𝓁 ˜qkEσ,σ′ (36)
where the sum inS+ (resp.S−) is over the singularities above (resp., below)L. The matrices
S±(˜x; ˜q) appear to have some positivity properties; see Sections 5.4 and 6.4 below for the41
and the 52 knots.
3. A summary of the story when u = 0
In this section we recall brieﬂy the results from [GGMn] for our two sample hyperbolic
knots, the 41 and the 52 knot.
3.1. The 41 knot whenu = 0. The state integral of the41 at u = 0 is given by
Z41(0;τ) =
∫
R +i0
Φb(v)2 e−πiv2
dv. (37)
The critical points of the integrand are the logarithms of the solutions ξ1 = e 2πi/6 and
ξ2 = e−2πi/6 of the polynomial equation
(1−y)(1−y−1) = 1. (38)
The labeling setP ={σ1,σ 2}, whereσ1 corresponds to the geometric representation of the
41 andσ2 to the complex conjugate of the geometric representation. Observe thatξ1 (resp.,
ξ2) lie in the trace ﬁeldQ (√−3)(resp., its complex conjugate) of the41 knot, whereQ (√−3)
is a subﬁeld of the complex numbers with√−3 taken to have positive imaginary part.
The ﬁrst ingredient is a vector of formal power series
Φ(τ) =
(
Φσ1(τ)
Φσ2(τ)
)
(39)
deﬁned by the asymptotic expansion of the state-integral (37) at each of the two critical
points, and which has the form
Φσ(τ) = exp
(V (σ)
2πiτ
)
ϕσ(τ), (40)
satisﬁes the symmetryΦσ2(τ) = iΦσ1(−τ), where
V (σ1) = iVol(41) = i 2Im Li2(eiπ/3) = i 2.029883... . (41)
with Vol(41) being the hyperbolic volume of41 and the ﬁrst few terms ofϕσ1(τ/(2πi))∈
3−1/4Q (√−3)[[τ]] are given by
ϕσ1
( τ
2πi
)
= 1
4√
3
(
1 + 11τ
72√−3 + 697τ 2
2 (72√−3)2 + 724351τ 3
30 (72√−3)3 +···
)
. (42)
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 13
The second ingredient is a vectorG(q) =
(
G0(q)
G1(q)
)
of q-series deﬁned for|q|< 1 by
G0(q) =
∞∑
n=0
(−1)nqn(n+1)/2
(q;q)2
n
(43a)
G1(q) =
∞∑
n=0
(−1)nqn(n+1)/2
(q;q)2
n
(
E1(q) + 2
n∑
j=1
1 +qj
1−qj
)
, (43b)
where E1(q) = 1− 4∑∞
n=1qn/(1−qn) is the Eisenstein series, and extended to|q| > 1 by
G0(q−1) =G0(q) and G1(q−1) =−G1(q). These series are motivated by, and appear in, the
factorization of the state-integral of the41 knot given in [GK17, Cor.1.7]
Z41(0;τ) =− i
2
(q
˜q
) 1
24
(√τG 0(˜q)G1(q)− 1√τG0(q)G1(˜q)
)
, (τ∈ C \ R ) (44)
where
q = e2πiτ, ˜q = e−2πi/τ. (45)
The above factorization follows by applying the residue theorem to the integrand of (37),
a meromorphic function ofv with prescribed zeros and poles. In particular, the integrand
of (37) determines the q-hypergeometric formula for the vectorG(q) of q-series. Below,
given aq-series H(q) deﬁned on|q|⁄ = 1, we denote byh(τ) = H(e2πiτ) the corresponding
holomorphic function inC \ R .
The vectorG(q) of q-series and the vector of asymptotic seriesΦ(τ) come together when
we consider the asymptotics ofdiag( 1√τ,√τ)g(τ) in theτ-plane (as was studied in [GZa]) and
compare them with the Borel summed vectorΦ. Recall that when the Borel transform of an
asymptotic series has singular pointsιi in the Borel plane, the rays (Stokes rays) emanating
from the origin with angleθ = argιi divide the complex plane into diﬀerent sectors. When
one crosses into neighboring sectors, the Borel sum of the asymptotic series undergoes Stokes
automorphism. In the case of the vector of asymptotic seriesΦ(τ), the singularities of the
Borel transforms of its two component asymptotic series are located at
ιi,j = V (σi)−V (σj)
2πi , i,j = 1, 2, i⁄=j, (46)
as well as
2πik, ιi,j + 2πik, k ∈ Z⁄=0, (47)
forming vertical towers as illustrated in Figure 2. In particular, the two singularitiesι1,2,ι 2,1
are on the positive and the negative real axis. We pick out four sectors which separate the
two singularities on the real axis and all the others, and label them byI,II,III,IV , as
illustrated in Figure 3. The relation between the vectorG(q) and the Borel summed vector
Φ(τ) depend on the sectorR. In [GGMn], we found out that we do not get an agreement,
but rather both sides agree up to powers of the exponentially small quantity˜q, and what
is more, several coeﬃcients of those powers were numerically recognized to be integers. In
other words, we found that
diag( 1√τ,√τ)g(τ) =MR(˜q)sR(Φ)(τ). (48)
14 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
where diag(v) denotes the diagonal matrix with diagonal given byv and MR(q) is a matrix
of q-series with integer coeﬃcients.
ι1,2 = Vol(41)/π
ϕσ1(τ )
ι2,1 = −Vol(41)/π
ϕσ2(τ )
Figure 2. The singularities in the Borel plane for the seriesϕσj(0;τ) for
j = 1, 2 of knot 41.
III
IVIII
L
Figure 3. Four diﬀerent sectors in theτ-plane for Φ(0;τ) of knot 41.
To identify the matricesMR, we used the third ingredient, namely the linearq-diﬀerence
equation
ym+1(q)− (2−qm)ym(q) +ym−1(q) = 0 ( m∈ Z ). (49)
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 15
It has a fundamental solution set given by the columns of the following matrix
Wm(q) =
(
G0
m(q) G1
m(q)
G0
m+1(q) G1
m+1(q)
)
, (|q|⁄ = 1) (50)
where Gm(q) =
(
G0
m(q)
G1
m(q)
)
, andG0
m(q) and G1
m(q) are deﬁned by
G0
m(q) =
∞∑
n=0
(−1)nqn(n+1)/2+mn
(q;q)2
n
(51a)
G1
m(q) =
∞∑
n=0
(−1)nqn(n+1)/2+mn
(q;q)2
n
(
2m +E1(q) + 2
n∑
j=1
1 +qj
1−qj
)
, (51b)
for|q|< 1 and extended to|q|> 1 byGj
m(q−1) = (−1)jGj
m(q). Observe thatG0(q) =G(q),
the vector that appears in the factorization (44) of the state-integralZ41(0;τ). The matrix
Wm(q) of holomorphic functions in|q|⁄ = 1 satisﬁes several properties summarized in the
following theorem.
Theorem 9.Wm(q) is a fundamental solution of the linearq-diﬀerence equation(49) that
has constant determinant
det(Wm(q)) = 2, (52)
satisﬁes the symmetry
Wm(q−1) =W−m(q)
(
1 0
0 −1
)
, (53)
the orthogonality property
1
2Wm(q)
(
0 1
−1 0
)
Wm(q)T =
(
0 1
−1 0
)
(54)
as well as
1
2Wm(q)
(
0 1
−1 0
)
W𝓁(q)T∈ SL(2, Z [q±]) (55)
for all integersm,𝓁 and for|q|⁄ = 1.
Conjecture 10.Equation (48) holds where the matricesMR(q) are given in terms ofW−1(q)
as follows
MI(q) =W−1(q)T
(
0 −1
1 −1
)
, |q|< 1, (56a)
MII (q) =
(
1 0
0 −1
)
W−1(q)T
(
1 0
1 −1
)
, |q|< 1, (56b)
MIII (q) =W−1(q−1)T
(
1 0
1 1
)
, |q|> 1, (56c)
MIV (q) =
(
1 0
0 −1
)
W−1(q−1)T
(
0 1
1 1
)
, |q|> 1. (56d)
16 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
Assuming the above conjecture, we can now describe completely the resurgent structure
of Φ(τ). The Stokes matrices are given by
S+(q) = SI→II (q)SIV→I, S−(q) = SIII→IV (q)SII→III , (57)
where
SI→II (q) =MII (q)−1MI(q) SIII→IV (q) =MIV (q−1)−1MIII (q−1) (58a)
SIV→I =MI(q)−1MIV (q) SII→III =MIII (q)−1MII (q). (58b)
(Compare with Equations (33) and (34) after we set˜x = 1 and replace ˜q by q). Note that
since MI(q),MII (q) and MIII (q),MIV (q) are given respectively asq-series andq−1-series in
(56a),(56b) and (56c),(56d), analytic continuation as discussed below (51b) is needed when
one computes SIV→I, SII→II in (58b). Using (52)–(55) we can express the answer in terms
of W−1(q). Explicitly, the Stokes matrices are given by
S+(q) = 1
2
(
0 −1
1 1
)
W−1(q)
(
0 1
1 0
)
W−1(q)T
(
0 −1
1 2
)
, |q|< 1, (59a)
S−(q) = 1
2
(
−1 −1
0 1
)
W−1(q)
(
0 1
1 0
)
W−1(q)T
(
1 0
−2 1
)
, |q|< 1. (59b)
In theq→ 0 limit,
S+(0) =
(
1 3
0 1
)
, S−(0) =
(
1 0
−3 1
)
(60)
whose oﬀ-diagonal entries−3, +3 are Stokes constants associated to the singularitiesι2,1
and ι1,2 on the negative and positive real axis respectively, and they agree with the matrix
of integers obtained numerically in [GH18, GZb]. In addition, we can assemble the Stokes
constants into the matrixS of Equation (36) (after we set˜x = 1 and replace ˜q by q). The
resulting matrixS+(q) has entries inqZ [[q]], and we ﬁnd
S+
σ1,σ1(q) =S+(q)1,1− 1
=− 8q− 9q2 + 18q3 + 46q4 + 90q5 + 62q6 +O(q7), (61)
S+
σ1,σ2(q) =S+(q)1,2/S+(q)1,1−S (0)
σ1,σ2
=9q + 75q2 + 642q3 + 5580q4 + 48558q5 + 422865q6 +O(q7), (62)
S+
σ2,σ1(q) =S+(q)2,1/S+(q)1,1
=− 9q− 75q2− 642q3− 5580q4− 48558q5− 422865q6 +O(q7), (63)
S+
σ2,σ2(q) =S+(q)2,2− 1− S+(q)1,2S+(q)2,1/S+(q)1,1
=8q + 73q2 + 638q3 + 5571q4 + 48538q5 + 422819q6 +O(q7). (64)
We notice the symmetry
S(k)
1,2 =−S(k)
2,1, for k∈ Z>0, (65)
which is due to the reﬂection propertyϕσ1(−τ∗) = ϕσ2(τ)∗ of the asymptotic series. Also
experimentally it appears that the entries of the matrixS+(q) = (S+
σi,σj(q)) (except the
upper-left one) are (up to a sign) inN[[q]]. Similarly we can extract the Stokes constants
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 17
S(−k)
σi,σj associated to the singularities in the lower half planes and collect them inq−1-series
S−
σi,σj(q−1) accordingly, and we ﬁnd
S(−k)
σi,σj =−S(+k)
σj,σi, i⁄=j, and S(−k)
σ1,σ1 =S(+k)
σ2,σ2, S(−k)
σ2,σ2 =S(+k)
σ1,σ1, for k∈ Z>0. (66)
A nontrivial consistency check in the above calculation is that the matricesSIV→I(q) and
SII→III (q) should come out to be independent ofq, and coincide with S−(0) and S+(0).
That is exactly what we ﬁnd.
The fourth and last ingredient, which makes a full circle of ideas, is the descendant state-
integral of the41 knot
Z41,m,µ(0;τ) =
∫
D
Φb(v)2 e−πiv2+2π(mb−µb−1)v dv (m,µ∈ Z ). (67)
The integration contourD asymptotes at inﬁnity to the horizontal line Imv = v0 with
v0 >|Re(mb−µb−1)| but is deformed near the origin so that all the poles of the quantum
dilogarithm located at
cb + ibr + ib−1s, r,s ∈ Z≥0, (68)
are above the contour. The integralZ41,m,µ(0;τ) is a holomorphic function ofτ∈ C ′ that
coincides with Z41(0;τ) when m = µ = 0 and can be expressed bilinearly inGm(q) and
Gµ(˜q) as follows
Z41,m,µ(0;τ) = (−1)m−µ+1iq
m
2 ˜q
µ
2
(q
˜q
) 1
24 1
2
(√τG 0
µ(˜q)G1
m(q)− 1√τG1
µ(˜q)G0
m(q)
)
. (69)
It follows that the matrix-valued function
Wm,µ(τ) = (Wµ(˜q)T )−1
(
1/√τ 0
0 √τ
)
Wm(q)T (70)
deﬁnedforτ = C \R , hasentriesgivenbythedescendantstate-integrals(uptomultiplication
by a prefactor of (69)) and hence extends to a holomorphic function ofτ∈ C ′ for all integers
mandµ. Using this form =−1andµ = 0 and the orthogonality relation (54), it follows that
we can express the Borel sums ofΦ(τ) in a regionR in terms of descendant state-integrals
and hence, as holomorphic functions ofτ∈ C ′ as follows. For instance, in the regionI we
have
sI(Φ)(τ) =MI(˜q)−1
( 1√τg0
0(τ)√τg 1
0(τ)
)
= i
(q
˜q
)− 1
24
(
Z41,0,0(0;τ)− ˜q1/2Z41,0,−1(0;τ)
Z41,0,0(0;τ)
)
(71)
This completes the discussion ofu = 0 for the 41 knot.
3.2. The 52 knot whenu = 0. The state integral of the52 at u = 0 is given by
Z52(0;τ) =
∫
R +i0
Φb(v)3 e−2πiv2
dv. (72)
Thecriticalpointsoftheintegrandarethelogarithmsofthesolutions ξ1≈ 0.78492+1.30714i,
ξ2≈ 0.78492− 1.30714i and ξ3≈ 0.43016 of the polynomial equation
(1−y)3 =y2. (73)
18 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
The trace ﬁeld of the52 knot is Q (ξ1), the cubic ﬁeld of discriminant−23, which has three
complex embeddings labeled byσj for j = 1, 2, 3 corresponding to thexj, and the labeling
set isP ={σ1,σ 2,σ 3}, whereσ1 corresponds to the geometric representation of the52 knot,
σ2 to the complex conjugate of the geometric representation andσ3 for the corresponding
real representation.
The ﬁrst ingredient is a vector of formal power series
Φ(τ) =


Φσ1(τ)
Φσ2(τ)
Φσ3(τ)

 (74)
where
ImV (σ1) =−ImV (σ2) = Vol(52) = 2.82812... (75)
isthehyperbolicvolumeoftheknot 52 andtheﬁrstfewtermsof ϕσj(τ/(2πi))∈δ−1/2
j Q (ξj)[[τ]]
are given by
ϕσj
( τ
2πi
)
=
(
−3ξ2
j + 3ξj− 2
23
)1/4(
1 +−242ξ2 + 209ξ− 454
22· 232 τ + 12643ξ2− 22668ξ + 25400
25· 233 τ 2
(76)
+−35443870ξ2 + 85642761ξ− 164659509
27· 3· 5· 235 τ 3 +...
)
.
The second ingredient is two vectorsH+(q) = ( H+
0 (q),H +
1 (q),H +
2 (q))T and H−(q) =
(H−
0 (q),H−
1 (q),H−
2 (q))T of q-series deﬁned for|q|< 1 by
H+
0 (q) =
∞∑
n=0
qn(n+1)
(q;q)3
n
, (77a)
H+
1 (q) =
∞∑
n=0
qn(n+1)
(q;q)3
n
(
1 + 2n− 3E(n)
1 (q)
)
, (77b)
H+
2 (q) =
∞∑
n=0
qn(n+1)
(q;q)3
n
(
(1 + 2n− 3E(n)
1 (q))2− 3E(n)
2 (q)− 1
6E2(q)
)
. (77c)
and
H−
0 (q) =
∞∑
n=0
(−1)nq
1
2n(n+1)
(q;q)3
n
, (78a)
H−
1 (q) =
∞∑
n=0
(−1)nq
1
2n(n+1)
(q;q)3
n
(1
2 +n− 3E(n)
1 (q)
)
, (78b)
H−
2 (q) =
∞∑
n=0
(−1)nq
1
2n(n+1)
(q;q)3
n
((1
2 +n− 3E(n)
1 (q)
)2
− 3E(n)
2 (q)− 1
12E2(q)
)
, (78c)
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 19
where
E(n)
l (q) =
∞∑
s=1
sl−1qs(n+1)
1−qs . (79)
The two sets ofq-series can be extended to|q| > 1 and are in fact related byH+
k (q−1) =
(−1)kH−
k (q), and deﬁne aq-series Hk(q) for|q|⁄ = 1 by
Hk(q) =
{
H+
k (q) |q|< 1
(−1)kH−
k (q−1) |q|> 1. (80)
Likewise, we deﬁne holomorphic functionshk(τ) in C \ R by
hk(τ) =
{
H+
k (e2πiτ), Im(τ)> 0
(−1)kH−
k (e−2πiτ), Im(τ)< 0, k = 0, 1, 2. (81)
These series appear in the factorization of the state-integral of the52 knot given in [GK17,
Cor.1.8]
Z52(0;τ) =−e
πi
4
2
(q
˜q
) 1
8(
τH−
0 (˜q)H+
2 (q)− 2H−
1 (˜q)H+
1 (q) +τ−1H−
2 (˜q)H+
0 (q)
)
, (τ∈ C \R ).
(82)
The above factorization follows by applying the residue theorem to the integrand of (72),
a meromorphic function ofv with prescribed zeros and poles. In particular, the integrand
of (72) determines theq-hypergeometric formula for the vectorsH+(q), H−(q) of q-series.
As in the case of the41 knot, multiplying the vectorh(τ)T = (h0(τ),h 1(τ),h 2(τ))T by the
automorphy factors diag(τ−1, 1,τ ) (dictated by (82)), and looking at the asymptotics asτ
approaches zero in sectors, we found that
e
3πi
4 diag(τ−1, 1,τ )h(τ) =MR(˜q)sR(Φ)(τ), (83)
where the right hand side depends on the sectors of Borel resummation. The Borel plane
singularities of the component series of the vectorΦ(τ) are similarly located at
ιi,j = V (σi)−V (σj)
2πi , i,j = 1, 2, 3,i⁄=j, (84)
as well as
2πik, ιi,j + 2πik, k ∈ Z⁄=0, (85)
which form vertical towers as illustrated in Figure 4. In particular, the two singularities
ι1,2,ι 2,1 are on the positive and negative real axis. We pick out the four sectors which separate
the two singularities on the real axis and all the others, and label them byI,II,III,IV , as
illustrated in Figure 5.
To identify the matrices MR, we consider the third ingredient, the linear q-diﬀerence
equation
ym(q)− 3ym+1(q) + (3−q2+m)ym+2(q)−ym+3(q) = 0 ( m∈ Z ), (86)
20 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
ϕσ1(τ )
ι1,2
ι1,3
ϕσ2(τ )
ι2,1
ι2,3
ϕσ3(τ )
ι3,1 ι3,2
Figure 4. The singularities in the Borel plane for the seriesϕσj(0;τ) for
j = 1, 2, 3 of knot 52.
III
IVIII
L
Figure 5. Four diﬀerent sectors in theτ-plane forΦ(0;τ) of knot 52 and the
line L that divides theτ-plane.
They have fundamental solution sets given by the columns of the following matrix
Wm(q) =



W +
m(q), |q|< 1

0 0 1
0 1 0
1 0 0

W−
−m−2(q−1)


1 0 0
0 −1 0
0 0 1

, |q|> 1. (87)
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 21
where the matricesWε
m(q) with ε =± are respectively
Wε
m(q) =


Hε
0,m(q) Hε
1,m(q) Hε
2,m(q)
Hε
0,m+1(q) Hε
1,m+1(q) Hε
2,m+1(q)
Hε
0,m+2(q) Hε
1,m+2(q) Hε
2,m+2(q)

, (|q|⁄ = 1) (88)
with entries theq-series
H+
0,m(q) =
∞∑
n=0
qn(n+1)+nm
(q;q)3
n
, (89a)
H+
1,m(q) =
∞∑
n=0
qn(n+1)+nm
(q;q)3
n
(
1 + 2n +m− 3E(n)
1 (q)
)
, (89b)
H+
2,m(q) =
∞∑
n=0
qn(n+1)+nm
(q;q)3
n
(
(1 + 2n +m− 3E(n)
1 (q))2− 3E(n)
2 (q)− 1
6E2(q)
)
, (89c)
and
H−
0,m(q) =
∞∑
n=0
(−1)nq
1
2n(n+1)+nm
(q;q)3
n
, (90a)
H−
1,m(q) =
∞∑
n=0
(−1)nq
1
2n(n+1)+nm
(q;q)3
n
(1
2 +n +m− 3E(n)
1 (q)
)
, (90b)
H−
2,m(q) =
∞∑
n=0
(−1)nq
1
2n(n+1)+nm
(q;q)3
n
((1
2 +n +m− 3E(n)
1 (q)
)2
− 3E(n)
2 (q)− 1
12E2(q)
)
,
(90c)
for|q| < 1 and extended to|q| > 1 by the relationH+
k,m(q−1) = (−1)kH−
k,−m(q). Observe
thatHε
k,0(q) =Hε
k(q). The matrixWm(q) of holomorphic functions in|q|⁄ = 1 satisﬁes several
properties summarized in the following theorem.
Theorem 11.Wm(q) is a fundamental solution of the linearq-diﬀerence equation(86) that
has constant determinant
det(Wm(q)) = 2, (91)
satisﬁes the orthogonality property
1
2Wm−1(q)


0 0 1
0 2 0
1 0 0

W−m−1(q−1)T =


1 0 0
0 0 1
0 1 3 −qm

 . (92)
as well as
1
2Wm(q)


0 0 1
0 2 0
1 0 0

W𝓁(q−1)T∈ SL(3, Z [q±]) (93)
for all integersm,𝓁 and for|q|⁄ = 1.
22 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
Conjecture 12.Equation (83) holds where the matricesMR(q) are given in terms ofW−1(q)
as follows
MI(q) =W−1(q)T


0 0 1
−1 3 0
0 −1 0

, |q|< 1, (94a)
MII (q) =


1 0 0
0 −1 0
0 0 1

 W−1(q)T


0 0 1
3 −1 0
−1 0 0

, |q|< 1, (94b)
MIII (q) =W−1(q)T


0 0 1
−1 −1 0
−1 0 0

, |q|> 1, (94c)
MIV (q) =


1 0 0
0 −1 0
0 0 1

 W−1(q)T


0 0 1
−1 −1 0
0 −1 0

, |q|> 1. (94d)
Assuming the above conjecture, we can now describe completely the resurgent structure
of Φ(τ), following the same computation as in the case of the41 knot. The Stokes matrices
are given by (57)–(58b). Note that sinceMI(q),MII (q) and MIII (q),MIV (q) are given re-
spectively asq-series andq−1-series in (94a),(94b) and (94c),(94d), analytic continuation as
discussed below (79) is needed when one computesSIV→I, SII→II in (58b). Using (91)–(93)
we can express the answer in terms ofW−1(q). Once again, we ﬁnd that the the Stokes matri-
ces SIV→I(q) and SII→III (q) are independent ofq, consistent with semiclassical asymptotics.
The Stokes matrices are given by
S+(q) = 1
2


0 1 0
0 1 1
−1 0 0

W−1(q−1)


0 0 1
0 −2 0
1 0 0

W−1(q)T


0 0 −1
1 1 0
0 1 0

, |q|< 1 (95a)
S−(q) = 1
2


0 3 −1
0 −1 0
1 0 0

W−1(q)


0 0 1
0 −2 0
1 0 0

W−1(q−1)T


0 0 1
3 −1 0
−1 0 0

 , |q|< 1.
(95b)
These Stokes matrices completely describe the resurgent structure ofΦ(τ). They also satisfy
other statements in Conjectures 3 and 4 whenx = 1. Theq→ 0 limit of the Stokes matrices
factorizes
S+(0) =Sσ3,σ1Sσ3,σ2Sσ1,σ2 =


1 0 0
0 1 0
−3 0 1




1 0 0
0 1 0
0 3 1




1 4 0
0 1 0
0 0 1

, (96)
S−(0) =Sσ1,σ3Sσ2,σ3Sσ2,σ1 =


1 0 3
0 1 0
0 0 1




1 0 0
0 1 −3
0 0 1




1 0 0
−4 1 0
0 0 1

, (97)
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 23
where the non-vanishing oﬀ-diagonal entry ofSσi,σj is the Stokes constant associated to the
Borel singularityιi,j. Assembling these oﬀ-diagonal entries in a matrix, we obtain the matrix


0 4 3
−4 0 −3
−3 3 0

 (98)
that was found numerically in [GZb, Sec.3.3]. In addition, we can assemble the Stokes
constants into the matrixS of Equation (36) (after we set˜x = 1 and replace ˜q by q). The
resulting matrixS+(q) has entries inqZ [[q]], and we ﬁnd
S+
σ1,σ1 =S+(q)1,1− 1
=− 12q + 3q2 + 74q3 + 90q4 + 33q5 +O(q6), (99a)
S+
σ1,σ2 =12q + 141q2 + 1520q3 + 17397q4 + 191970q5 +O(q6), (99b)
S+
σ1,σ3 =q + 3q2 + 9q3 + 30q4 + 99q5 +O(q6), (99c)
S+
σ2,σ1 =− 12q− 141q2− 1520q3− 17397q4− 191970q5 +O(q6), (99d)
S+
σ2,σ2 =12q + 141q2 + 1582q3 + 17583q4 + 194703q5 +O(q6), (99e)
S+
σ2,σ3 =− 21q− 235q2− 2586q3− 28593q4− 316104q5 +O(q6), (99f)
S+
σ3,σ1 =−q− 3q2− 9q3− 30q4− 99q5 +O(q6), (99g)
S+
σ3,σ2 =21q + 235q2 + 2586q3 + 28593q4 + 316104q5 +O(q6), (99h)
S+
σ3,σ3 =0. (99i)
The Stokes constants enjoy the symmetry
S(k)
σi,σj =−S(k)
σϕ(i),σϕ(j), i⁄=j, for k∈ Z>0, (100)
with ϕ(1) = 2 ,ϕ (2) = 1 ,ϕ (3) = 3 . We notice that the entries of the matrix S+(q) =
(S+
σi,σj(q)) (except the upper-left one) are (up to a sign) inN[[q]]. Similarly we can extract
the Stokes constantsS(−k)
σi,σj associated to the singularities in the lower half plane, and we ﬁnd
S(−k)
σi,σj =−S(+k)
σj,σi, i⁄=j, and S(−k)
σi,σi =S(+k)
σϕ(i),σϕ(j), for k∈ Z>0. (101)
The fourth and last ingredient, which makes a full circle of ideas, is the descendant state-
integral of the52 knot
Z52,m,µ(0;τ) =
∫
D
Φb(v)3 e−2πiv2+2π(mb−µb−1)v dv (m,µ∈ Z ). (102)
Here the same contourD as in (67) is used. It is a holomorphic function ofτ ∈ C ′ that
coincides withZ52(0;τ) when m = µ = 0 and can be expressed bilinearly inH+
k,m(q) and
H−
k,µ(˜q) as follows
Z52,m,µ(0;τ) =(−1)m−µ+1 e
πi
4
2 q
m
2 ˜q
µ
2
(q
˜q
) 1
8
(103)
(
τH −
0,µ(˜q)H+
2,m(q)− 2H−
1,µ(˜q)H+
1,m(q) +τ−1H−
2,µ(˜q)H+
0,m(q)
)
.
24 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
It follows that the matrix-valued function
Wm,µ(τ) = (Wµ(˜q)T )−1


τ−1 0 0
0 1 0
0 0 τ

Wm(q)T (104)
deﬁnedforτ = C \R , hasentriesgivenbythedescendantstate-integrals(uptomultiplication
by a prefactor of (103)) and hence extends to a holomorphic function ofτ∈ C ′ for all integers
mandµ. Using this form =−1andµ = 0 and the orthogonality relation (92), it follows that
we can express the Borel sums ofΦ(τ) in a regionR in terms of descendant state-integrals
and hence, as holomorphic functions ofτ∈ C ′ as follows. For instance, in the regionI we
have
sI(Φ)(τ) = e
3πi
4 MI(˜q)−1


τ−1h0(τ)
h1(τ)
τh 2(τ)

 = i
(q
˜q
)− 1
8


Z52,0,0(0;τ)− ˜q1/2Z52,0,−1(0;τ)
Z52,0,0(0;τ)
˜q−1/2Z52,0,1(0;τ)

 (105)
This completes the discussion ofu = 0 for the 52 knot.
