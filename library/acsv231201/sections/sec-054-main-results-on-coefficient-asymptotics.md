---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-054-main-results-on-coefficient-asymptotics
section_title: "Main results on coefficient asymptotics"
section_number: null
pages: 320-340
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Having approximated the asymptotics of integrals near critical multiple points,
to determine asymptotics of ar it remains only to determine the coeﬃcients
10.3 Main results on coeﬃcient asymptotics
303
κw in (10.1). We ﬁrst give results when V is a hyperplane arrangement: Sec-
tion 10.3.1 assumes transverse intersections and gives a method to compute all
coeﬃcients, while Section 10.3.2 reduces a general hyperplane arrangement
to transverse arrangements using algebraic reductions. Next, we show how
to compute dominant asymptotics for non-linear divisors. As in the smooth
case, we need to characterize which minimal critical points contribute to dom-
inant asymptotic behavior. Section 10.3.3 deals with transverse intersections
and Section 10.3.4 deals with non-transverse intersections that are arrange-
ment points.
Notation and terminology
For each point σ on the boundary of the amoeba of a smooth algebraic hyper-
surface VQ, some complex scalar multiple of (∇log Q)(σ) will be real and point
into amoeba(Q). We use this to deﬁne contributing points on the boundary of
the amoeba.
Deﬁnition 10.17 (lognormal cones and contributing multiple points). Suppose
that σ is a transverse multiple point in a stratum of codimension k, such that
F(z) = P(z)/Q1(z)m1 · · · Qk(z)mk near σ with the gradients of the Q j linearly
independent at z = σ. If Relog(σ) ∈∂amoeba(Q) then the lognormal cone
N(σ) to V at σ is the positive real span of the lognormals to the Q j at σ,
scaled so that the lognormal of Q j is a real vector pointing into amoeba(Q j)
at Relog(σ). The set W( ˆr) of contributing multiple points in the direction
ˆr consists of the critical points τ for which Relog(τ) ∈∂amoeba(Q) and
ˆr ∈N(τ).
Remark 10.18. The height function h ˆr(z) = −ˆr · Relog(z) is minimized on
the closure B of a component of amoeba(Q)c at σ ∈∂B if and only if σ
is a contributing multiple point. Deﬁnition 10.17 fails when amoeba(Q) has
codimension one near σ, for instance in the case of the line amoeba(1 −xy).
However, when the component B of amoeba(Q)c is ﬁxed then contributing
multiple points can still be deﬁned in this pathological case for any σ ∈∂B by
scaling the lognormals deﬁning N(σ) so that they point away from B.
Exercise 10.7. Let P = 1 and Q = (1−2x/3−y/3)(1−x/3−2y/3). First, deter-
mine the directions ˆr for which the point (1, 1) is a contributing multiple point.
Second, ﬁnd all contributing multiple points in the main diagonal direction.
10.3.1 Linear divisors: transverse arrangements
Suppose that F(z) = P(z)/Q(z) such that for polynomials P and Q such
that Q(z) = ℓ1(z)m1 · · · ℓn(z)mn for positive integers mk and real linear fac-
304
Multiple point asymptotics
tors ℓ1, . . . , ℓn vanishing on distinct hyperplanes V1, . . . , Vn in Cd, with the
factors scaled so that ℓj(z) = 1 −z · b(j) for a real vector of coeﬃcients b(j).
Let M = Cd
∗\ V denote the set where F is analytic, and deﬁne MR = M ∩Rd.
A stratum S in V can be represented by its closure, which is an intersection
S = Vk1 ∩· · · ∩Vks of some of the hyperplanes deﬁning V with the hyper-
planes not in S removed. By the convexity of the height function, each stratum
contains at most one critical point in each orthant of Rd, and if ξ ∈{±1}d then
we let σS = σS,ξ( ˆr) denote the unique critical point of S in the same orthant as
ξ. We further deﬁne MR(S) to be Rd
∗with the hyperplanes deﬁning S removed,
and let BS = BS,ξ denote the unique component of MR(S) in the same orthant
as ξ whose closure contains the origin.
The homology and cohomology of (complements of) hyperplane arrange-
ments has been well studied. Recall the relative homology group Hd(M, −∞)
that describes the homology of M relative to any sublevel set M<c = {z ∈M :
h ˆr(z) < c}, where c is smaller than the heights of all critical points.
Deﬁnition 10.19 (imaginary ﬁbers). For each component B of MR, the imag-
inary ﬁber with respect to B is any chain CB = x + iRd with x ∈B, oriented
so that each copy of R goes from −∞to +∞.
The imaginary ﬁber CB is well deﬁned in Hd(M), as if x, y ∈B then f(t) =
(1−t)x+ty+iRd deﬁnes a homotopy between f(0) = x+iRd and f(1) = y+iRd
which stays in M.
Proposition 10.20. If ˆr is a generic direction then the set of ﬁbers CB as B
varies over components of MR on which h ˆr is bounded from below is a basis
for Hd(M, −∞).
Proof
See Varchenko and Gelfand [VG87, page 268].
□
Proposition 10.20 implies that for linear divisors the domains of integration
Cw in (10.1) can be expressed in terms of imaginary ﬁbers. We now specialize
to the case of a transverse arrangement, where all nonempty intersections of k
hyperplanes have codimension k. In this case we can explicitly compute cycle
representatives for another homology basis using the following construction.
Deﬁnition 10.21 (linking tori). For any w ∈VR let Adj(w) be the set of
components B in MR with w ∈B. If w is contained in the stratum S with
closure S = Vk1 ∩· · · ∩Vks then the linking torus τw is the relative cycle
τw =
X
B∈Adj(w)
sgnw(B) CB
(10.8)
10.3 Main results on coeﬃcient asymptotics
305
Figure 10.9 Left: The ﬁber basis for H2(M, −∞) for three lines not intersecting
at a common point. Right: Linking tori are shown for the three critical points on
these lines, and one of the codimension-2 critical points.
in Hd(M, −∞), where sgnw(B) denotes the sign of x1 · · · xdℓk1(x) · · · ℓks(x) for
any x ∈B.
Example 10.22. Figure 10.9 shows the zero set VR deﬁned by the three linear
functions ℓ1(x, y) = 3−2x−y, ℓ2(x, y) = 33/16−x−y, and ℓ3(x, y) = 3−x−3y.
The real plane is split into six bounded components by VR and the coordinate
axes, together with ten unbounded components. In any direction ˆr with positive
coordinates the height function h ˆr is unbounded from below on the unbounded
regions, so a basis for H2(M, −∞) is given by imaginary ﬁbers through points
in each of the six bounded regions (illustrated on the left side of the ﬁgure).
The right side of Figure 10.9 shows the six critical points of V in the di-
rection ˆr = (1/5, 4/5), three of which are smooth points (on codimension one
strata) and three of which form their own strata of codimension two. Two link-
ing tori are shown, one on a stratum of codimension two that consists of four
ﬁbers and another at a smooth point that consists of two ﬁbers.
◁
Asymptotics of interest will be given by a sum of integrals over linking tori,
but we still need to determine which linking tori appear in the sum, correspond-
ing to the coeﬃcients κw in (10.1) that are non-zero. In general this is a very
diﬃcult question, but in the linear divisor case we can answer it exactly. Note
that in this linear case the lognormal cone N(σ) at a point σ in the stratum S
deﬁned by the intersection S = Vk1 ∩· · · ∩Vks is the positive span of the
vectors ˜b(k1), . . . , ˜b(ks) with coordinates ˜b
(kj)
i
= b
(k j)
i
σi.
Theorem 10.23 (change of basis to linking tori). Fix a generic direction ˆr and
306
Multiple point asymptotics
Figure 10.10 Because the integrand of the Cauchy integral decays suﬃciently
quickly away from the origin, the ends of the imaginary ﬁbers deﬁning a link-
ing torus can be joined and the resulting curve deformed to give an actual torus.
Similarly, a torus can be broken apart into a linking torus.
suppose that the ℓj deﬁne a transverse arrangement. Then
T(ε, . . . , ε) =
X
w∈W( ˆr)
τw
(10.9)
in Hd(M, −∞) for all suﬃciently small ε > 0. In particular, the power series
coeﬃcients ar of F satisfy
ar =
1
(2πi)d
X
σ∈W( ˆr)
Z
τσ
F(z)z−r−1dz .
The decomposition (10.9) varies with ˆr but is unique for each generic ˆr
because the linking tori form a basis. For simplicity we restrict Theorem 10.23
to power series expansions, however decompositions analogous to (10.9) can
be computed for any torus T(w) with Relog(w) < amoeba(Q).
Proof Sketch
Because any torus in M can be expressed as a sum of imagi-
nary ﬁbers, it is suﬃcient to prove that any imaginary ﬁber can be expressed
as a sum of linking tori. For each bounded component B of MR there exists
a critical point σB that minimizes the height function h ˆr on B, and this crit-
ical point is a contributing point. If x lies in B then we can replace the ﬁber
Cx by the τσB plus a sum of ﬁbers Cx′,where h ˆr(x′) < h ˆr(σB). Repeatedly
applying this rewriting process results in a sum of linking tori plus imaginary
ﬁbers over points in components of MR on which h ˆr is unbounded from be-
low. These ﬁnal imaginary ﬁbers are null homologous in (M, −∞), and thus
may be discarded. The result then follows by writing T(ε, . . . , ε) as a “linking
10.3 Main results on coeﬃcient asymptotics
307
Figure 10.11 When a saddle crosses p the linking torus changes by τp.
torus” around the origin (see Figure 10.10), then proving inductively that the
coeﬃcient of every contributing point is 1. See [BMP23] for a full proof.
□
Example 10.24. Figure 10.11 shows three critical points a, b, and p on two
crossing lines. As the direction ˆr varies from a slope of 3 on the left of the
ﬁgure to a slope of 2/5 on the right of the ﬁgure, the critical point b crosses
ρ. As illustrated in the ﬁgure, on the left-hand side T(ε, ε) = τa + τb while on
the right side T(ε, ε) = τa + τb + τp. Varying ˆr farther to a slope of 1/5, the
critical point a crosses p, whereupon the coeﬃcient of τp becomes zero again
and T(ε, ε) = τa + τb, this time with a and b both to the right of p.
◁
Combining Theorems 10.15 and 10.23 gives coeﬃcient asymptotics for func-
tions whose denominators consist of transversely intersecting linear divisors.
Theorem 10.25 (transverse hyperplane arrangement asymptotics). Let Q(z) =
Qn
j=1 ℓj(z)mj for positive integers m j and real linear functions ℓj deﬁning a
transverse hyperplane arrangement, normalized so that Q(0) = 1 (as is the
case when each ℓj(z) = 1−b(j) ·z). Let P
r arzr be a convergent power series
expansion for F(z) = P(z)/Q(z) and ˆr be a generic direction. Then
ar ≈
X
σ∈W( ˆr)
Φσ(r) ,
(10.10)
where Φσ is an inﬁnite asymptotic expansion when σ lies in a stratum of di-
mension at least one, and a ﬁnite expansion (an exponential times a polynomial
in r) when σ lies in a complete intersection. These expansions are computed
(up to sign) in Theorems 10.12 and 10.15, and have the following leading
terms.
308
Multiple point asymptotics
(i) For complete intersection points σ,
Φσ(r) ∼p−r (−1)|m−1|
(m −1)!
P(p)
|det ΓΨ(p)| (rΓ−1
Ψ )m−1 .
(10.11)
(ii) For critical points σ in strata of positive dimension,
Φσ(r) ∼p−r (−1)|m−1|
(m −1)!
P(p) Q
j∈π |pj|
|det ΓΨ(p)|
( ˆrΓ−1
Ψ )m−1
(2π)(d−k)/2 p
det H(p)
|r|−(d−k)/2+|m−1| .
(10.12)
In both (i) and (ii), asymptotics are uniform as ˆr varies over compact sets
of generic directions where the leading terms of the summands do not cancel.
Proof
At this point, most of our work consists of getting the correct signs
in (10.11) and (10.12). The linking torus τσ and the torus T (σ) are generators
for the rank-d local homology of M at a complete intersection point σ. For
such a point, deﬁne sgn(τσ, T (σ)) = ±1 according to whether these generators
are equally or oppositely oriented. More generally, if γ is a generator of the
relative homology group at σ within the stratum, then both τσ and T (σ) × γ
generate the rank-d local homology of M and we again let sgn(τσ, T (σ), γ) =
±1 according to whether these generators are equally or oppositely oriented.
Casting the conclusion of Theorem 10.23 in terms of the tori T gives
ar ≈
1
(2πi)d
X
σ∈W( ˆr)
sgn(τσ, T (σ), γ)
Z
T (σ)×γ
F(z)z−r−1dz ,
and plugging in the results of Theorems 10.12 and 10.15, respectively, pro-
duces (10.11) and (10.12), up to sign. We proceed to check the signs. Recall
that the deﬁnition of T required us to normalize the factors Qi so that the en-
tries of ΓΨ are real.
Case 1 (complete intersection): For (10.11) we need to check that
sgn(τσ, T )
det ΓΨ
=
1
| det ΓΨ| .
(10.13)
Let D be the cell in the complement of Rd
∗\ A(σ) whose closure contains
both the origin and σ, where A(σ) denotes the sub-arrangement of all hy-
perplanes passing through σ. The tangent planes to both τσ and T can be
made to pass through any point p′ = e−εp for ε suﬃciently close to zero.
At such a point, the two tangent planes, call them K and L respectively, are
both subspaces of the purely imaginary space p′ + iRd, with K oriented by
the standard orientation of Rd and L oriented by y 7→Q−1(p′ + iy), with
10.3 Main results on coeﬃcient asymptotics
309
Q : (z1, . . . , zd) 7→(Q1(z), . . . , Qd(z)). The Jacobian of this change of coor-
dinates is dQ/dz, hence sgn(τσ, T ) = sgn(det ΓΨ) and establishing (10.13)
and (10.11).
Case 2 (positive dimension): To establish (10.12), we need to check that
sgn(τσ, T , γ)
Q
j∈π pj
det ΓΨ
=
Q
j∈π |pj|
| det ΓΨ| .
(10.14)
The linking torus τσ is homologically a product of a k-dimensional torus τ′ in
the normal slice with the (d −k)-dimensional imaginary contour γ′ through σ
within the stratum. The tangent plane to τ′ coincides up to orientation with the
tangent plane to T . As we have seen above, the orientation sgn(τ′, T ) is the
sign of det ΓΨ. Therefore it remains to show that the orientations to γ′ and γ
of the imaginary space in the stratum are related by Q
j∈π sgn(pj). The plane
γ′ is oriented by the imaginary coordinates yπ(1), . . . , yπ(d−k) listed in that order
and all increasing. The plane γ is parametrized by these same coordinates in
the same order, inheriting the orientation from dzπ(1) ∧· · · ∧dzπ(d−k). Thus, the
imaginary part is increasing when the real part is positive, and decreasing when
the real part is negative. This establishes (10.14), hence (10.12), ﬁnishing the
proof of the theorem.
□
Remark 10.26. Theorem 10.25 holds when the numerator P(z) is any analytic
function, provided that an error term that decreases faster than any exponential
function is added to the right-hand side of (10.10).
Example 10.27. Suppose that a and b are positive integers and let F(x, y) =
1/Q(x, y) where Q(x, y) =

1 −2
3 x −1
3y
a 
1 −1
3 x −2
3y
b. For a general direc-
tion ( ˆr, ˆs) = (r, s)/(r + s) there are contributing points
p1 =
 3r
r + s,
3s
2(r + s)
!
and p2 =
 
3r
2(r + s), 3s
r + s
!
on each of the individual smooth divisors. Letting λ = r/s, the exponential
rates contributed by these smooth critical points are
R1 = 2λ(1 + λ)1+λ
3(3λ)λ)
= 1
3
 2(1 + 1/λ)
3
!λ
(1 + λ)
R2 = 2(1 + λ)1+λ)
3(3λ)λ)
= 2
3
 1 + 1/λ
3
!λ
(1 + λ).
The detailed asymptotic contributions of p1 and p2 can be worked out either
from the results of Chapter 9 or from (10.7). The point p = (1, 1) is a minimal
critical multiple point for every direction ˆr, but is only contributing when λ ∈
310
Multiple point asymptotics
[1/2, 2], since the lognormal cone at p is spanned by the vectors (2, 1) and
(1, 2) with slopes 1/2 and 2.
When (r, s) lies in the open cone deﬁned by λ ∈(1/2, 2), the exponen-
tial contributions R1 and R2 can be bounded below 1 as they are increasing
functions of λ. Thus, Theorem 10.25 with det ΓΨ = 1/3 implies that when
1/2 < λ < 2,
ars ∼3 (r −2s)b−1 (s −2r)a−1
(a −1)!(b −1)!
.
Note that the boundary directions λ ∈{1/2, 2} are not generic and so The-
orem 10.25 does not apply. In these cases p1 and p2 are distinct, but one of
them coincides with p and the other corresponds to an exponentially decay-
ing contribution. We deal with this boundary case in Example 10.66 via the
surgery method. It is also possible for λ to approach the boundary of the inter-
val rather than being constant, and in this case the analysis of asymptotics is
more delicate – see Section 13.2 for a brief discussion.
◁
Example 10.28 (queueing partition function). Let a, b, c, and d be positive real
constants, and consider the partition generating function
F(x, y) =
exp(x + y)
(1 −ax −by)(1 −cx −dy)
for a closed multi-class queueing network with one inﬁnite server [BM93;
Kog02]. The most interesting case in applications occurs, without loss of gen-
erality, when a > c and b < d, whence D = ad−bc > 0. The two linear divisors
intersect in the positive real quadrant at the point p = (x0, y0) =
 d−b
D , a−c
D

,
which is a critical transverse multiple point. In the main diagonal direction,
there are also critical points at (1/2a, 1/2b) and (1/2c, 1/2d), contributing ex-
ponential growth rates of 4ab and 4cd; the ﬁrst of these coincides with the
double point p if and only if ad + bc −2ab = 0, and the second if and only if
ad + bc −2cd = 0. Thus, if we consider the case where the two points listed
above are distinct and each diﬀerent from the double point, the calculation
(ad −bc)2 −4ab(a −c)(d −b) = [a(d −b) + b(a −c)]2 −4ab(a −c)(d −b)
= [a(d −b) −b(a −c)]2
= [ad + bc −2ab]2 > 0 ,
and an analogous one with 4cd in place of 4ab, shows that the double point
has larger exponential growth rate than either of the smooth points. Leading
asymptotics are determined by (10.5) throughout the cone of directions (r, s)
10.3 Main results on coeﬃcient asymptotics
311
for which
b(a −c)
a(d −b) < s
r < d(a −c)
c(d −b).
In particular,
ann ∼
D2n−1 exp
 a+d−(b+c)
D

(a −c)n+1(d −b)n+1 .
◁
Example 10.29. Consider again the rational function 1/(Q1Q2) from Exam-
ple 10.3. The intersection of the zero sets of Q1 and Q2 contains the single
critical point
(x0, y0, z0) =
 
4(r + s)
3(r + s + t),
4(r + s)
3(r + s + t),
4t
r + s + t
!
in the direction (r, s, t). The lognormal cone at this point is two-dimensional,
so the same point will be critical for many directions: for instance, the point
(x0, y0, z0) = (1, 1, 1) is critical in directions where r + s = 3t. When (r, s, t)
lies in the lognormal cone at (x0, y0, z0) then this point determines dominant
asymptotics, and we recover expansions such as a3t,3t,2t ∼(48πt)−1/2 as t →
∞.
◁
Exercise 10.8. Let Q = (3−x−2y)(3−2x−y)(5−3x−3y). Sketch the real part of
V, show the positions of all the critical points in the main diagonal direction,
state which one(s) contribute to the leading term of an,n, and determine whether
the leading term is computed by Theorem 10.12 or by Theorem 10.15.
Exercise 10.9. Theorem 10.15 handles smooth point asymptotics in the special
case where k = 1. Reconcile the formulae given here with the diﬀerent-looking
formulae from Chapter 9. Start with a concrete example such as Delannoy
numbers F(x, y) = (1 −x −y −xy)−1.
10.3.2 Linear divisors: non-transverse arrangements
A rational function whose singular variety forms a non-transverse hyperplane
arrangement can be analyzed using a form of partial fraction decomposition.
For a hyperplane arrangement A deﬁned by real linear functions ℓ1, . . . , ℓn,
the matroid they deﬁne is the set of all subsets T ⊂[n] of indices correspond-
ing to linearly independent collections {ℓj : j ∈T}. Subsets of [n] not in the ma-
troid are dependent sets, and minimal dependent sets are called circuits. Cir-
cuits need not all have the same cardinality. Following Brylawski [Bry77], we
deﬁne a broken circuit to be a circuit with its greatest element deleted, and call
312
Multiple point asymptotics
a set containing no broken circuit χ-independent (note that χ-independence
implies independence, but not vice versa). The support of a rational function
is the set of divisors – without multiplicities – appearing in its denominator
when in lowest terms.
Example 10.30. Let ℓ1, ℓ2, and ℓ3 vanish on concurrent lines, as in Figure 10.12.
Each pair of lines is linearly independent, but the set of all three is linearly de-
pendent, so there is a unique circuit [3] = {1, 2, 3} and a unique broken circuit
{1, 2}. A subset of [3] is independent if its cardinality is at most 2, and is χ-
independent if it does not contain both 1 and 2.
◁
Figure 10.12 Three concurrent lines.
Let S A denote the set of meromorphic functions whose pole variety is con-
tained in the union of hyperplanes of A. Broken circuits allow us to character-
ize S A as a module over holomorphic functions.
Proposition 10.31. Let A = {ℓ1, . . . , ℓn} be a hyperplane arrangement in Cd.
(i) The set of rational functions  ℓi1(z) · · · ℓis(z)−1 ∈S A with χ-independent
support is linearly independent over C.
(ii) The span over C of the rational functions  ℓi1(z)m1 · · · ℓis(z)ms−1 ∈S A
with χ-independent support and total degree −Ps
j=1 mj contains the in-
verses of all products of the ℓj over multisets of cardinality Ps
j=1 mj.
Proof
The claimed results follow from properties of hyperplane arrange-
ments derived in [OT92] (see [BMP23, Proposition 5.2]).
□
10.3 Main results on coeﬃcient asymptotics
313
If w is a circuit and P
j∈w ajℓj(z) = 0 then dividing by Q
j∈w ℓj(z)mj yields a
linear relation among elements of S A of total degree 1 −Ps
j=1 mj,
a j
Q
i∈w ℓi(z)mi−δij = −
X
j′∈w
j′,j
aj′
Q
i∈w ℓi(z)mi−δij′ .
(10.15)
Such relations allow for a reduction to the transverse case above.
Algorithm 4: Decomposition into transverse hyperplane arrangements.
Input: Rational or meromorphic function F(z) = P(z)/Q(z) whose
singular variety is the hyperplane arrangement deﬁned by the
vanishing of Q(z) = Qn
j=1 ℓj(z)m j.
Output: Rational or meromorphic functions F1, . . . , Fs such that
F(z) = F1(z) + · · · + Fs(z) and the singular variety of each F j
is a transverse hyperplane arrangement contained in the
singular variety of F.
Set S = F(z).
While there is a summand s(z) of S with a broken circuit {ℓj1, . . . , ℓjk−1}:
Apply (10.15) to s(z) with jk > jk−1 such that {ℓj1, . . . , ℓjk} is
dependent, and replace
s(z) in S by the result
Return S
Example 10.32. Let Q = ℓ1(x, y)ℓ2(x, y)ℓ3(x, y) = (3−2x−y)(3−x−2y)(2−x−
y). The variety V consists of three concurrent lines, as shown in Example 10.30
and Figure 10.12. By examination we ﬁnd that 2ℓ1(x, y)+2ℓ2(x, y)−6ℓ3(x, y) =
0. Dividing through by 6Q gives
1
ℓ1(x, y)ℓ2(x, y) =
1/3
ℓ1(x, y)ℓ3(x, y) +
1/3
ℓ2(x, y)ℓ3(x, y) .
Starting with any fraction F(x, y) = g(x, y)/ℓ1(x, y)aℓ2(x, y)bℓ3(x, y)c, this rela-
tion may be used in Algorithm 4 to reduce factors ℓ1ℓ2ℓ3 in the denominator
until there are none remaining, resulting in a sum
F(x, y) =
X
a+b≥j≥0
e j(x, y)
ℓ1(x, y) jℓ3(x, y)a+b+c−j +
X
a+b≥j≥0
fj(x, y)
ℓ2(x, y)jℓ3(x, y)a+b+c−j .
Whereas F(x, y) had a non-transverse multiple point at (1, 1), each summand
now has a transverse multiple point at (1, 1).
◁
Theorem 10.33. Let Q(z) = Qn
j=1 ℓj(z)m
j be a product of real linear functions
314
Multiple point asymptotics
deﬁning a hyperplane arrangement. Given a meromorphic function F(z) =
P(z)/Q(z) with poles on the zero set of Q, Algorithm 4 terminates and pro-
duces the claimed representation of F.
Proof
Let w be a circuit and consider the weight function
w

n
Y
j=1
ℓj(z)aj
=
n
X
j=1
ja j.
The reduction described in (10.15) replaces one term by a sum of terms whose
denominators have greater weight but the same total degree (the sum of the ex-
ponents that appear on the linear factors). Repeatedly applying the decompo-
sition gives terms with the same total degree but successively higher weights.
Because the weight function is bounded among terms whose total degree is
ﬁxed, the loop in the algorithm must terminate, and when it terminates every
summand has a denominator whose linear factors form a χ-independent set.
Thus, the pole set of each summand returned forms a transverse hyperplane
arrangement contained in V(Q).
□
Corollary 10.34. If F(z) = P
r arzr is a convergent power series expansion
of a meromorphic function having poles on a hyperplane arrangement then
asymptotics of ar can be computed by decomposing F into a sum of functions
having poles on transverse hyperplane arrangements using Theorem 10.33 and
applying Theorem 10.25 to each summand.
We note that the sum may have a large number of terms, the computations
can be diﬃcult to carry out by hand, and a computer algebra system is often
useful.
Example 10.35. Let F = P(x, y)/Q(x, y), where P(x, y) = 1 and Q(x, y) =
(3 −2x −y)(3 −x −2y)(2 −x −y)2, a simple variation of Example 10.32. The
decomposition algorithm yields
F =
1/3
(3 −x −2y)(2 −x −y)3 +
1/3
(3 −2x −y)(2 −x −y)3
so that ar ∼(r −2s)2/2 for directions ˆr = (r, s) with s/r ∈(1/2, 1), while
ar ∼(s −2r)2/2 when s/r ∈(1, 2), and ar is exponentially small when s/r is
bounded strictly away from these two intervals.
◁
Up to this point, our roadmap for general hyperplane arrangements has been
to use matroid theory and algebra to reduce to the transverse case. We ﬁnish our
treatment of linear divisors by describing the general topological story. We will
not be using these results, but include some discussion because it can help un-
derstand the non-linear case. The topology local to a critical point is the same
10.3 Main results on coeﬃcient asymptotics
315
for an arrangement point as it is for the hyperplane arrangement deﬁned by the
tangent planes of the surfaces intersecting near the point. However, when Q
factors locally but not globally near several diﬀerent multiple points, it is not
clear how multiple local partial fraction decompositions of the type produced
in Theorem 10.33 can be used together to give the correct integral represen-
tations for coeﬃcients. Therefore, though we don’t have an application that
makes essential use of the homological decomposition in the non-transverse
case, we will go ahead and describe it.
Without a transversality assumption, there is no longer a single generator
per critical point in the Morse theoretic decomposition of Hd(M). Instead of a
single linking torus τσ whose coeﬃcient will be zero or non-zero depending
on whether r is in the normal cone, there will be more than one homology gen-
erator. Diﬀerent regions of ˆr may yield diﬀerent non-zero homology elements
local to σ which combine with linking tori elsewhere to produce the Cauchy
domain of integration. We sum this up as follows.
Let A denote the hyperplane arrangement deﬁned by the linear divisors
ℓj and suppose that σ is a critical point in the direction ˆr on some ﬂat E
of codimension k in a generic direction ˆr. Let N(σ) denote a suﬃciently
small ball around σ in M and consider the rank-d homology group G(σ) =
Hd(N(σ), N(σ)≤h(σ)−ε), where ε > 0 is small enough that this pair is the at-
tachment pair at σ.
Proposition 10.36. Let A(E) ⊆A be the subarrangement of A consisting
of all hyperplanes containing E and let A′ ⊆A(E) be any collection of k
hyperplanes of A(E) whose (necessarily transverse) common intersection is E.
Let ι denote the inclusion Cd
∗\A(E) ,→Cd
∗\A′ and let τσ,A′ denote the linking
torus at σ in Cd
∗\A′. There is a unique homology element β(σ, ˆr) ∈G(σ) such
that for every such collection A′ we have ι∗β = τσ,A′ if ˆr ∈NA′(σ) and ι∗β = 0
otherwise. These homology elements satisfy
[T(ε, . . . , ε)] =
X
σ∈critical( ˆr)
β(σ, ˆr)
(10.16)
for any ε > 0 suﬃciently small.
□
Example 10.37 (Example 10.32, continued). If ˆr has slope 3/2, as shown in
Figure 10.13, then β(σ, ˆr) is the sum of imaginary ﬁbers with signs shown
in the ﬁgure. To see this, observe that if the ﬂattest line, called ℓ2 in Exam-
ple 10.32, is removed then the + and −ﬁbers cancel in pairs, corresponding
to ι∗β vanishing because ˆr is not in the normal cone spanned by the other
two normals (1, 1) and (2, 1). Conversely, if either of the other two lines is re-
moved then ι∗β equals τσ, corresponding to the fact that ˆr is in the normal
316
Multiple point asymptotics
Figure 10.13 The linking torus at σ for a non-transverse intersection, with ˆr hav-
ing slope 3/2. The codimension 2 critical point σ is at the base of the arrow, while
the codimension 1 critical points are depicted by smaller dots.
cone spanned by (1, 2) and either (1, 1) or (2, 1). If we change ˆr to have slope a
little less than 1, then the critical point on the middle line moves to the right of
σ and the negative ﬁbers move from the regions between the two lines of least
slope to the regions between the two lines of greatest slope. When ˆr does not
have slope between 1/2 and 2 then ˆr < N(σ) and β(σ, ˆr) = 0, again consistent
with the fact that ˆr < NA(E′)(σ) for any E′.
◁
10.3.3 Non-linear divisors: transverse multiple points
In the case of non-linear divisors, we determine the critical point(s) contribut-
ing to the asymptotics only when there are minimal critical points. As above,
let p be a transverse multiple point on a stratum S of codimension k, so that
we can write
F(z) =
P(z)
Q1(z)m1 · · · Qk(z)mk
for positive integers mj and analytic functions P, Q1, . . . , Qk at z = p with the
gradients of the Q j linearly independent at z = p.
Near p the singular variety V is locally homeomorphic to the hyperplane
arrangement P deﬁned by the ﬁrst-order expansions of the Q j at p. In fact,
these sets are locally isotopic in the sense that for some neighborhood N of
p there is a homotopy of the pair (N, N ∩V) ﬁxing ∂N such that inside a
smaller neighborhood N′ the homotopy takes V ∩N′ to P ∩N′. It follows
from this isotopy that the local homology at p has rank 1, and is generated by
10.3 Main results on coeﬃcient asymptotics
317
the linking torus [τp]. A representative of this homology class is T × γ where
T is an actual torus in the normal link and γ is homeomorphic to a (d −k)-disk,
lies in the stratum containing p, and has a boundary lying below height h ˆr(p).
In the case of non-linear divisors, we use the term “linking torus” to refer to
T × γ; when k = d this is an absolute cycle, namely a d-torus, while for k < d
it is a relative cycle. Combining this observation with the expansion computed
in Theorem 10.15 gives the following.
Theorem 10.38 (strictly minimal transverse multiple point asymptotics). Let
p be a transverse multiple point of F with local decomposition
F(z) =
P(z)
Q1(z)m1 · · · Qk(z)mk
as described above. Suppose that p = p( ˆr) is a minimal point for the Laurent
expansion F(z) = P
r arzr with domain of convergence D = Relog−1(B), is a
critical point in the generic direction ˆr, and is the unique critical point with its
height. Let N(p) be the lognormal cone described in Deﬁnition 10.17 above.
(i) If ˆr ∈N(p) and det H(p) , 0 then
ar ≈Φp(r),
(10.17)
where Φp(r) is the asymptotic expansion deﬁned in Theorem 10.25 by
(10.11) (for a complete intersection) or (10.12) (otherwise). This asymp-
totic expansion holds uniformly as |r| →∞with ˆr varying such that it
and p( ˆr) satisfy the assumptions above.
(ii) If ˆr < N(p) then ar grows exponentially smaller than p−r.
Proof
We have already seen that the local homology group of M at p has a
single generator C, and that
1
(2πi)d
Z
C
z−r−1F(z) dz ∼Φz(r). To prove con-
clusion (i) it remains to show that the domain of integration T in the Cauchy
integral for ar satisﬁes [T] = ±τp in Hd(M, M≤c−ε), where c = h ˆr(p), and that
the modulus / absolute value signs in the middle term on the right of (10.12)
capture the orientation.
In Section 10.5 we will see that this is indeed true by following the original
derivation in [PW04]. That derivation involves the residue sum identity (10.29),
but the topological fact may also be seen directly by applying the Thom iso-
morphism one divisor at a time. For the orientation, note that
Q
j∈π |pj|
| det ΓΨ| =

Q
j∈π pj
det ΓΨ

 =

1
det Γ′
Ψ

 ,
where the rows of Γ′
Ψ are augmented by elementary basis vectors eπ(j) in-
stead of z jeπ( j). This matrix is real, so again the absolute value multiplies by
318
Multiple point asymptotics
sgn(det Γ′). This is equal to sgn(τp, T , γ) because the picture is the same, ex-
cept rotated in the j-coordinate by the argument of pj.
Conclusion (ii) is a consequence of the Paley–Wiener theorem for ACSV,
described in Theorem 11.42. Brieﬂy, the lognormal cone N(p) is the dual of
the geometric tangent cone to B at p and, for any minimal point, the class [T]
is represented as a ﬁber exp(x + iy) over some point x ∈B. Because ˆr is not
in the dual to the geometric tangent cone to B at p, there is some point p′ ∈B
with −ˆr · p′ < −ˆr · p, implying (ii).
□
Example 10.39 (lemniscate, continued). Let F(x, y) = 1/Q(x, y) be the gen-
erating function from Example 10.4. To apply Theorem 10.38 we ﬁrst prove
that the critical point (1, 1) is strictly minimal. The parametrization (10.18) be-
low shows that V does not enter the unit polydisk near the point (1, 1). If this
curve enters the unit polydisk anywhere else, then there is a point (x0, y0) with
one coordinate having modulus 1 and the other having modulus less than 1.
By symmetry, it suﬃces to check the points on V with |x| = 1 to see if
|y| ≤1 can hold. Using a rational parametrization of the unit circle, such as
x(t) = (1 −t2)/(1 + t2) + i(2t)/(1 + t2), we can solve for the square norm of
y(t) as an algebraic function of t. Studying the zeroes of the derivative |y(t)|2
allows one to prove that |y(t)|2 ≥1 with equality only at t = 0, meaning (1, 1)
is strictly minimal.
Applying Theorem 10.38 is now straightforward. The cone N(1, 1) consists
of the directions (r, s) between the logarithmic normals to the two branches of
V; the lognormal directions were computed in Example 10.43 to be the rays
with slopes 2 and 1/2. The point (1, 1) is a square-free complete intersection so
we may apply Corollary 10.14, with the values of x0, y0 and P(x0, y0) all equal
to 1. We obtain
ars = 1
6 + Rrs,
where Rrs is a remainder converging to zero exponentially as (r, s) →∞with
r/s remaining in a compact subset of (1/2, 2). The exponential decay of the er-
ror term is detectable numerically: for instance, the asymptotic approximation
of a30,30 ≈0.1652 has a relative error rate around 0.8%, while the relative error
approximating a60,60 is around 0.04%.
◁
Example 10.40. The number of nearest-neighbor walks of length n on the
integer lattice that start at the origin, take steps in {NE, NW, S }, and remain
conﬁned to the nonnegative quadrant is shown in [MW19] to be the main di-
agonal of
(1 + x)(1 −2xy2z)
(1 −y)(1 −z(1 + x2 + xy2))(1 −zxy2).
10.3 Main results on coeﬃcient asymptotics
319
A short analysis shows that dominant asymptotics are determined by the con-
tributing point (1, 1, 1/3) where the ﬁrst two of the divisors above vanish (but
the third does not) and Theorem 10.38 implies
annn ∼3n √
3
2 √πn.
◁
Because the homology group Hd(M, M≤c−ε) is the direct sum of local ho-
mology groups near critical points, similar results hold when the minimal
critical multiple point determining asymptotics has a ﬁnite number of critical
points with the same coordinate-wise modulus (this mirrors the ﬁnite criticality
hypothesis discussed in Chapter 9).
Corollary 10.41 (minimal transverse multiple point asymptotics). Suppose
that w is a minimal point such that the torus T(w) contains a ﬁnite number of
critical points p1, . . . , pm, and suppose that each pj satisﬁes the conditions of
Theorem 10.38 (aside from strict minimality).
(i) If ˆr ∈N(pj) for some j then
ar ≈
X
p∈W( ˆr)
Φp(r) ,
where Φp(r) is the expansion described in (10.17).
(ii) If ˆr < N(pj) for all 1 ≤j ≤m then ar grows exponentially smaller than
w−r.
□
Exercise 10.10. Let m(1), . . . , m(d) be positive integer vectors forming a lat-
tice basis of Zd and let F(z) = 1/Q(z) for Q(z) = Qd
j=1(1 −zm( j)). Com-
pare the behavior of ar as r →∞when r is in the open positive hull of
{m( j) : 1 ≤j ≤d} and when it is not, using Corollary 10.41. Why does this
make sense combinatorially?
10.3.4 Non-linear divisors: arrangement points
Similar to the linear case, near a general arrangement point p we can decom-
pose F(z) into a ﬁnite sum of functions whose singular varieties have trans-
verse multiple points at p. Unlike the linear case, however, we need to carefully
consider the ring in which we perform this decomposition.
Deﬁnition 10.42. The local ring of analytic germs Op at p consists of all
equivalence classes of analytic functions on neighborhoods of p under the re-
lation of agreement on some neighborhood of p. Because analytic functions
320
Multiple point asymptotics
are determined by their values in a neighborhood, all functions in such an
equivalence class are analytic continuations of each other, making the situa-
tion somewhat simpler than for germs of smooth functions: Op is isomorphic
to the ring Cp{z} of power series centered at p that converge in some neighbor-
hood of p. The ring Op is a local ring whose unique maximal ideal is the germs
of functions vanishing at p, and we consider the local ring as lying between
the polynomial ring and the formal power series ring: C[z] ⊂Op ⊂Cp[[z]].
Example 10.43 (lemniscate, continued). Let Q be the polynomial from Exam-
ple 10.4, whose zero set in R2 has the shape of a ﬁgure eight. The polynomial
Q is irreducible in C[x, y] but according to its geometry it must factor in O(1,1).
A computer algebra system computes parametrizations (x, y1(x)) and (x, y2(x))
for V near (1, 1) with
y1(x) −1 = x2 −(x −1)
√
−4 x2 + 8 x + 5 −7 x + 10
x2 −2 x + 5
(10.18)
= −2(x −1) + 2
3(x −1)3 + · · · ;
(10.19)
y2(x) −1 = x2 + (x −1)
√
−4 x2 + 8 x + 5 −7 x + 10
x2 −2 x + 5
(10.20)
= −1
2(x −1) −1
24(x −1)3 + · · · .
(10.21)
The two branches have slopes −2 and −1/2 at the point (1, 1).
◁
The decomposition of a function near an arrangement point is facilitated by
the following result.
Lemma 10.44. Let p be an arrangement point of F(z) where V is locally the
union of smooth sets V1, . . . , Vn deﬁned by the vanishing of analytic functions
Q1, . . . , Qn. If w is a circuit in the matroid deﬁned by the tangent hyperplanes
of the varieties V1, . . . , Vn at z = p then there is a collection {gi(z) : i ∈w}
of invertible elements of Op such that P
i∈w gi(z)Qi(z) = 0 in Op.
Our proof of Lemma 10.44 relies on the following result, whose proof is
outlined in Exercise 10.16. Recall from (10.2) that for a set T indexing some
divisors Qi the symbol T denotes the set of all j such that Vj contains T
i∈T Vi.
Lemma 10.45. Suppose p is a multiple point with local irreducible factors
Q1, . . . , Qn and for an index set T ⊂[n] let JT denote the ideal in Op generated
by {Qi : i ∈T}. If p is an arrangement point then for all T ⊂[n] the ideal JT
is radical. It follows that JT = JT for all T, and that the codimension of this
ideal is equal to the codimension of LT.
10.3 Main results on coefficient asymptotics 321

Proof of Lemma 10.44 Fix any i € wand let S = V; N---NV,,. Because
p is an arrangement point, near p we have the containment () jew\) Vj C Vi;
which is equivalent to Q; being in the radical of the ideal of O, generated by
{Q;: j # i}. By Lemma 10.45, this ideal is already radical, hence

O42) =D) 820A) (10.22)

jew\ti}

for some functions gj € Op. Taking gradients at p we have

(VOM) = DY) 8i(PKV Op).

jew\ti}

Because w \ {i} is a circuit, the gradients on the right-hand side are linearly
independent, hence this equation uniquely determines the values {gj(p) : j €
w \ {i}}. Also, the fact that w is a circuit implies that none of these values g j(p)
is zero, for that would imply a linear dependence among w \ { j}. By continuity,
there is a neighborhood of p where none of the functions g; vanishes, hence
these functions are all units, and the representation (10.22) along with g; = —1
proves the lemma. ia)

Corollary 10.46. Let F(z) = >), a,z" be a convergent Laurent expansion. If
p is a strictly minimal arrangement point then modifying Algorithm 4 to work
over the local ring using Lemma 10.44 decomposes F(z) near p as a finite sum
of meromorphic functions with transverse multiple points at p. Asymptotics
of ay can be computed using Theorem 10.38 when the summands satisfy the
hypotheses of that theorem at p. If p is not strictly minimal but the torus Tp)
through p has only a finite number of critical points then asymptotics of ay can
be determined by performing this decomposition and analysis at all critical
points in T(p), provided the hypotheses of Theorem 10.38 are always satisfied.

We conclude this section with an example involving a binomial variety; for
a similar application concerning lattice point enumeration, see Example 12.28.

Example 10.47. Continuing the analysis of the GF in Example 10.8, we con-
sider the power series expansion of F(x, y) = 1/Q(x, y), where

Ox, y) = Qi(x, y)Q2(x, y)O3(x, y) = (1 — x) - y)C1 — xy).

Localizing at the common intersection point (1, 1), we know that each factor
should be in the ideal generated by the others in Oc,1), and in fact

Q3(x, y) = Qi(x, y) + Qo(x,y) — Qi(%, y)Q2(x, y). (10.23)
322
Multiple point asymptotics
We have a broken circuit {1, 2}, so we eliminate the factor of Q3 in the denom-
inator of F(x, y) by dividing (10.23) by Q to obtain
1
Q1(x, y)Q2(x, y) =
1
Q2(x, y)Q3(x, y) +
1
Q1(x, y)Q3(x, y) −
1
Q3(x, y) .
We may write the last term as −
Q2(x,y)
Q2(x,y)Q3(x,y) so that
1
(1 −x)(1 −y) =
y
(1 −y)(1 −xy) +
1
(1 −x)(1 −xy)
and thus
F(x, y) = F1(x, y) + F2(x, y) =
y
(1 −y)(1 −xy)2 +
1
(1 −x)(1 −xy)2 .
The generating functions F1 and F2 have a transverse multiple point at (1, 1),
which is the only critical point when ˆr < {(0, 1), (1, 0), (1, 1)}. Asymptotics can
be obtained by applying Theorem 10.38 to these two rational functions at the
point p = (1, 1). The lognormal directions for the divisors 1 −x, 1 −y, and
1 −xy are, respectively, horizontal, vertical, and on the main diagonal; ˆr thus
lies in the dual normal cone to F1 at p but not the dual normal cone to F2 when
ˆr has positive slope greater than 1, and vice versa when ˆr has positive slope
less than 1. We deduce that
ars =

r + O(1)
if ε−1 > s
r > 1 + ε
s + O(1)
if 1 −ε > s
r > ε
,
uniformly for any ε > 0. A glance at the generating function shows that in fact
ars = 1 + min{r, s}.
◁
