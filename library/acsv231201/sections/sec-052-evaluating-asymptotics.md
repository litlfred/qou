---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-052-evaluating-asymptotics
section_title: "Evaluating asymptotics"
section_number: null
pages: 379-386
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
doc_brief: "Analytic Combinatorics in Several Variables — 85 sections: Preface to the second edition; List of Symbols; Introduction"
---
quote the argument from [BP11, Theorem 5.8]. The range of the homotopy
Φε,u,η
t is a projective set in a neighborhood ofw, meaning locally it coincides
with a conical set of the form {λb : b∈ K,λ > 0} for some closed subset
K of the unit sphere. The varietyV˜q deﬁned by ˜q is also a closed conical set
intersecting the unit sphere in some set L. On the unit sphere these closed sets
do not intersect and hence are separated by a positive distance ρw. The set of
normalized secants (z−w)/|z−w| forz∈V q and|z−w|< s converges as
s↓ 0 to L, hence, once the parameterρ is chosen smaller than half eachρw the
homotopy Φt(y) must avoidVq for ally in this case.
The ﬁnal case occurs when y∈N (w)∩N (w′) for some w∈ local( ˆr∗)
andw′ < local( ˆr∗). Reasoning as in Conclusion (i), we observe that K˜q,B(y)
is a subset of the cone Z(y) once ρ is suﬃciently small as a consequence of
part (iii) of Lemma 11.27, and the reasoning of the ﬁrst conclusion applies
again. □
Let c = Φ 1(Tﬂat) be the ﬁnal cycle in the homotopy described in Theo-
rem 11.33. In order to produce a homotopy and a ﬁnal cycle that completely
avoidsVq, we stop the homotopy early nearlocalarg. Deﬁneρ(y) byρ(y) =
minw∈localarg|y−w|, the distance fromy to the closest point of localarg.
Deﬁnition 11.34 (chains and stopped homotopy). Consider the following def-
initions.
(i) Fix δ> 0 and deﬁne the stopped homotopy Φδ
t (y) := Φε,u,η,δ
t (y) by
Φδ
t (y) = iy +x +ε[(1− t[1− (δ−ρ(y))+])u + t[1− (δ−ρ(y))+]η(y)],
(11.11)
where the notation x+ for a real number x denotes x+ = max{0, x}.
(ii) Let cδ = Φδ
1(Tﬂat) denote the cycle resulting from the stopped homotopy;
see Figure 11.3 for depictions of c and cδ.
(iii) For w∈ localarg and 0 < δ < ρ, whereρ is less than half the distance
fromw to the nearest other point in localarg, deﬁne cδ
ρ(w) to be the
chain obtained by restricting Φ1 to the ball of radiusρ centered atw.
11.3 Evaluating asymptotics
Let F(z) = P(z)/Q(z) = ∑
r arzr be a rational Laurent series whose open
logarithmic domain of convergence is the component B of the complement of
amoeba(Q). Let ˆr∗ be a direction such that the height function h(x) =− ˆr∗·x
achieves a unique minimum m on B at some point x∗ ∈ ∂B, and suppose
362 Cone point asymptotics
u xmin
c
minT(x      )
r*
^
cδ
u xmin
log
Figure 11.3 Deforming the chain: ˆ r∗ points to the right; the dotted plane is
x−u + iRd. The ﬁgure on the left shows that this can be deformed to the pro-
jective contour c. The ﬁgure on the right shows that stopping early produces a
contour diﬀering in an arbitrary small neighborhood of any point of localarg
and completely avoidingVq.
that the set of local points local( ˆr∗) with respect to x∗ is nonempty. Theo-
rem 11.33 and Deﬁnition 11.34 show how to deform T =x∗−u + i(R/2π)d in
L withx∗−u∈ B into a cycle cδ, which is the sum overw∈ localarg( ˆr∗) of
locally projective chainscδ
ρ(w) nearx∗+iw together with a chain inM≤m−s for
some s > 0. Applying Cauchy’s integral formula to F, changing coordinates
via the exponential map, and breaking into pieces near each local point gives
the following corollary.
Corollary 11.35. Assume the hypotheses in the previous paragraph and let
f = F◦ exp. There is a constant c< m, a neighborhoodR of ˆr∗, and constants
0<δ<ρ such that
ar =
∑
w∈localarg(r)
1
(2πi)d
∫
cδ
ρ(w)
e−r·z f (z) dz + O(ec|r|)
=
∑
w∈localarg(r)
z−r
(2π)d
∫
B(w,ρ)
e−ir·y f (iy + Φδ
1(y))J(y) dy + O(ec|r|)
uniformly as ˆr =r/|r| ranges overR, where Φδ
1 is speciﬁed in Deﬁnition 11.34
and J is the Jacobian determinant of the mapy↦→ Φδ
1(y). □
We are left with the task of asymptotically evaluating the integrals in Corol-
lary 11.35. While the use of the locally projective deformation in the last corol-
lary is only to save a few lines in the estimate (Theorem 11.5 would have done
instead), Lemmas 11.37 and 11.39 and Theorem 11.40 do require it.
When asymptotically evaluating integrals, the ﬁrst step is typically to ap-
proximate the amplitude via a series, with each summand having a canonical
11.3 Evaluating asymptotics 363
form that is particularly easy to integrate; for instance, in Chapters 4 and 5
saddle point integrals with general amplitudes are reduced to those whose am-
plitudes are monomials. The key result for doing this is aBig-O Lemma, which
tells us that functions diﬀering by a small quantity will have integrals diﬀering
by a correspondingly small quantity. First, we show how to approximate the
reciprocal of a function by its leading homogeneous part.
Lemma 11.36 (Straightening Lemma) . Suppose that q (x) = ˜q(x) + R(x),
where ˜q is a homogeneous polynomial of degreeα and R is analytic in a neigh-
borhood of the origin with R (x) = O(|x|α+1). Let K be any closed cone on
which ˜q does not vanish. Then on the intersection of K with some neighbor-
hood of the origin the function q does not vanish and there is a convergent
expansion
q(x)−s =
∞∑
n=0
˜q(x)−s−n

∑
|m|≥n(α+1)
c(m, n)xm
 . (11.12)
Furthermore,
q(x)−s−
∑
|m|−αn<N
c(m, n)xm ˜q(x)−s−n = O
(
|x|−αs+N)
. (11.13)
Proof Let R(x) = ∑
|m|≥α+1 b(m)xm be a power series expansion for R, ab-
solutely convergent in some ball Bε centered at the origin, and let
M =
sup
|x|∈Bε
∑
|m|≥α+1
|b(m)||x|m
inf
|x|∈∂Bε∩K
˜q(x) .
By homogeneity
∑
|m|≥α+1
|b(m)xm|
|˜q(x)| ≤ 1/2
on the ball Bε/(2M) of radius ε/(2M) centered at the origin, and the binomial
expansion (1 + u)−s = ∑
n≥0
(−s
n
)
un converges for|u| < 1/2. Thus, the series
expansion
(
1 + R(x)
˜q(x)
)−s
=
∑
n≥0
(−s
n
)
∑
|m|≥α+1
b(m)xm
˜q(x)

n
converges on Bε/(2M)∩ K, and multiplying through by ˜q−s yields (11.12). Con-
vergence on any neighborhood of the origin implies the estimate (11.13). □
Exercise 11.7. Let q(x, y) = y− x− x2. Find ˜q and R, the expansion (11.12) to
second order, and the exponent in the remainder term in (11.13).
364 Cone point asymptotics
Recall from Deﬁnition 6.46 that deg( Q,w) denotes the order of vanishing
of an analytic function Q at a pointw, equal to zero if Q(z), 0. We deﬁne the
order of vanishing of a real power Q(z)s to be s· deg(Q,z), and remark that if
Q is a Laurent polynomial then a branch of Qs may be deﬁned on the domain
of convergence of any Laurent series for F. Finally, we also deﬁne the degree
of a product Q(z) = ∏k
j=1 Q j(z)s j of Laurent polynomials by
deg(Q,w) =
k∑
j=1
s j deg(Q j,w)
and abuse notation slightly by writing
amoeba(Q) = amoeba

k∏
j=1
Q j
 =
k⋂
j=1
amoeba(Q j).
Lemma 11.37 (Big-O Lemma). Let Q(z) = ∏k
j=1 Q
s j
j (z) for Laurent polyno-
mials Q1,..., Qk and real numbers s1,..., sk that are not negative integers, let
F = P(z)/Q(z) for a Laurent polynomial P coprime to Q, and let f = F◦ exp.
Fix a component B of amoeba(Q)c corresponding to the convergent expansion
F(z) = ∑
r arzr on B, and ﬁx a direction ˆr∗ such that− ˆr∗·x is minimized on B
at a unique pointx∗∈∂B. Letz = exp(x∗ + iw) for somew∈ localarg( ˆr∗).
Assume the last conclusion of Lemma 11.27 and let Cδ(z) = exp[cδ(w)] be
a chain satisfying the conclusion of Lemma 11.32. If ˆr∗ is a non-obstructed
vector in the interior to the dual cone N(z) then the following estimates hold
uniformly asr→∞ while ˆr =r/|r| varies over a neighborhood of ˆr∗.
(i) If φ(z) is any function that is O(|z|β) at the origin withβ + d> 0 then
|zr|
∫
c(w)
exp(−r·z′)φ(z′) dz′ = O(|r|)−d−β. (11.14)
(ii) The same estimate holds for the chain cδ(w) in place of c(w).
(iii) Let D = deg(F,z) = deg(P,z)−∑k
j=1 s j deg(Q j,z). Then for any bounded
functionψ,
|zr|
∫
cδ(w)
ψ(z′)q(z′) exp(−r·z′) dz′ = O
(
|r|−d−D)
.
(iv) The estimate|z|r ar = O(|r|−d−D∗) holds where D∗ = minw∈local deg(F,w).
Proof The cone c(w) is a subset of an inﬁnite cone ⋃
λ≥0λS , and we may
decompose dz = td−1 dt∧dS where dS is a ﬁnite measure onS . It follows from
11.3 Evaluating asymptotics 365
conclusion (iv) of Lemma 11.32 that there is aθ> 0 for which Re{r·y}≥ θ|r|
on S . Thus,
|zr|
⏐⏐⏐⏐⏐⏐
∫
cδ(w)
exp(−r·z′)φ(z′) dz′
⏐⏐⏐⏐⏐⏐≤
∫ ∞
0
(∫
S
C e−θt|r|tβ dS
)
td−1 dt
≤
∫ ∞
0
C′e−θt|r|tβ+d−1 dt
= O(|r|)−d−β,
proving (i).
The chains cδ(w) are all homotopic inM. Thus, for any ﬁxedr the integral
in (ii) is independent ofδ. We have seen thatβ+d> 0 implies absolute integra-
bility on c(w). The same estimates imply that the integral over the intersection
of cδ(w) with an ε-neighborhood of w goes to zero as ε→ 0 uniformly in
δ. This implies convergence of the integrals in ( ii) to the integral in ( i), and
because the integrals in ( ii) are all the same, they are all equal to the integral
in (i), proving the second conclusion. The third conclusion follows from the
ﬁrst with φ = ψq and from the estimate q(z′) = O(|z′|)D on cδ(w), which is a
consequence of Lemma 11.36 with q = f . The fourth conclusion follows from
the second and Corollary 11.35. □
11.3.1 Fourier transforms
Our results up to this point hold for an arbitrary product Q(z) = ∏k
j=1 Q j(z)s j
of powers of Laurent polynomials. We now specialize to k = 1 and let Q be
a polynomial whose leading term is a Lorentzian quadratic. The summands in
Corollary 11.35 are evidently Fourier transforms which, as we will shortly see,
are classically known. Recall that the standard Lorentzian quadratic S (y) =
y2
1− ∑d
j=2 y2
j (discussed in Example 11.22 above) is in fact equivalent to any
other Lorentzian quadratic q in the sense that there is a real linear map M
such that q = S◦ M−1. The Fourier transform of a Lorentzian quadratic is
known [Rie49; ABG70; BP11], as is the transform of any power S−s as long
as s is not 0 ord/2−1. In the formula that follows,S∗ denotes the dual quadratic
which has an identical formula r2
1−∑d
j=2 r2
j, and q∗(r) = S∗(M∗r) where M∗ is
the adjoint of the linear map M. Note that what we call the Fourier transform,
while standard, is called the inverse Fourier transformin [ABG70; BP11].
Proposition 11.38 (Fourier transform of a Lorentzian quadratic). Let s be any
real number for which neither s nor s + 1− d/2 is a non-positive integer. The
366 Cone point asymptotics
generalized Fourier transform of S−s is given by
ˆS−s(r) = eiπs S∗(r)s−d/2
22s−1π(d−2)/2Γ(s)Γ(s + 1− d/2).
More generally, for any monomial xm and any Lorentzian quadratic q, the
Fourier transform ofxm q−s is given by
ˆxmq−s(r) = eiπs i|m| |M|(∂/∂r)mq∗(r)s−d/2
22s−1π(d−2)/2Γ(s)Γ(s + 1− d/2). (11.15)
□
There is a catch to the statements in Proposition 11.38: the functionxmq−s
will fail to be integrable at inﬁnity if the homogeneous degree|m|− 2s is−d or
more, and the integral deﬁning the Fourier transform blows up at the origin if
|m|− 2s≤− d. Proposition 11.38 is thus properly stated in terms ofgeneralized
functions. These generalized functions are deﬁned as limits of actual functions
onu + iRd asu→ 0 in a cone of hyperbolicity of the quadratic, their integrals
over noncompact sets are deﬁned by weak limits of compact integrals, and
their Fourier transforms are deﬁned not by direct integration against eir·x but
by their integrals against (classical) Fourier transforms of smooth, compactly
supported functions. When s or s + 1− d/2 is a non-positive integer, a Fourier
transform can be constructed that is itself a generalized function (in particular,
a sort of delta function supported on the hypersurface S = 0). For further
details of generalized functions, we refer to [GS16] or the summary in [BP11].
We do not worry about these subtleties here, and use only the following
result from [BP11, Lemma 6.3]. The proof is not trivial, involving the right
choice of insertions of compactly supported functions and truncation estimates.
The statement in [BP11] assumes that Q is the product of quadratic and linear
factors, but in fact relies only on the conclusion of Theorem 11.33, and thus
holds whenever conclusion (iii) of Lemma 11.27 holds.
Lemma 11.39. Fixx∗∈∂B, letw be one of ﬁnitely many points oflocalarg,
and let N denote the negative dual of tanx∗(B). Assume the last conclusion of
Lemma 11.27. Asr→∞ through a compact set of non-obstructed directions
in N, the generalized Fourier transformˆS−s(r) correctly computes the integral
of exp(−r·x)S−s(x) over the chain cδ
ρ(w). More generally, the same is true of
xmq−s and of F◦ exp when F is a Laurent polynomial. □
11.3.2 Main result on coe ﬃcient asymptotics
Let Q(z) = ∏k
j=1 Q j(z)s j be a product of powers of Laurent polynomials
satisfying the conclusions of Theorem 11.33, and let B be a component of
11.3 Evaluating asymptotics 367
amoeba(Q)c corresponding to a convergent Laurent expansion of the form
F(z) = P(z)/Q(z) = ∑
r arzr. Pickx∗∈∂B and suppose that there is a non-
obstructed direction ˆr∗ in the interior ofNx∗(B), such that the setlocal( ˆr∗) is a
singleton{z} ={exp(x∗+iy)}. Writing q j = Q j◦exp and ˜q j = hom(q j,x∗+iy),
Lemma 11.36 allows us to develop each q
−s j
j as a sum of terms of the form
c(m, n, j)xm ˜q−s−n
j . Multiplying these series and then multiplying by P gives
an expansion of the form
f (x) = F(exp(x)) =
∑
m
c(n,m)xm ˜q(x)−s−n, (11.16)
where ˜q(x)−s−n = ∏k
j=1 ˜q j(x)−s j−n j, the vectorn has nonnegative integer co-
ordinates, the sum contains only terms whose degrees are the degree of ˜ q or
greater, and the sum contains only ﬁnitely many terms of any ﬁxed degree.
Theorem 11.40. Under the setup above, letb = (b1,..., bk) be the sequence of
degrees of homogeneous polynomials q1,..., qk and let χn,m be the general-
ized Fourier transform ofxmQ−s−n. Then there is an asymptotic development
ar≈z−r(2π)−d
∑
n,m
c(n,m)χn,m(r) (11.17)
valid whenr→∞ with ˆr restricted to some neighborhood of ˆr∗. For any N,
there are only ﬁnitely many terms with|m| + d− (s +n)·b< N. When N > 0,
truncating the sum to the ﬁnitely many terms satisfying this inequality yields a
remainder of O
(
|r|−N)
.
If local( ˆr∗) has cardinality greater than 1 and ˆr∗ is interior to N(z) and
non-obstructed for everyz∈ local( ˆr∗) then the series on the right-hand side
of (11.17) can be summed overz∈ local( ˆr∗) to give an asymptotic series for
ar.
Proof We have seen in Corollary 11.35 that, up to a term of lower expo-
nential order, ar is computed by a sum of integrals over chains cδ
ρ(w) of
Fourier integrands f (z)e−r·z dz. We assume without loss of generality that
local( ˆr∗) ={z} ={exp(x∗ + iy)}; the case of cardinality greater than one
follows by a similar argument. Expand f via the series (11.16), ordered by in-
creasing homogeneous degree. Equation (11.13) of Lemma 11.36 shows that
the series is a true asymptotic development, in the sense that the remainders be-
ginning with a term of a given homogeneous degree β are O(|x|β) nearx + iy
on any closed cone avoiding logV.
Lemma 11.37 tells us we can integrate f (z)e−r·z dz term by term overcδ
ρ(y)
for all terms of homogeneous degree less thanβ, and as long asβ> −d the re-
mainder of the integral will be O(|r|−β−d). By Lemma 11.39 each integral over
368 Cone point asymptotics
c is given by its generalized Fourier transform χn,m, proving the theorem in
the case thatβ> −d. Finally, ifβ≤− d we observe that the generalized Fourier
transform of a homogeneous function of degree α is always homogeneous of
degree−α− d. Therefore, lettingα run over all degrees of terms that are in the
interval [β,−d], the remainder is expressed as the sum of ﬁnitely many terms of
type O(|r|−α−d) together with a remainder that is at mostO(1). This establishes
that the remainder is O(|r|−β−d) and ﬁnishes the proof. □
