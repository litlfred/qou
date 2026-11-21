---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-056-surgery-non-generic-directions-and-non-arrangeme
section_title: "Surgery, non-generic directions, and non-arrangement points"
section_number: null
pages: 345-357
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Algorithms to compute global monodromy – typically using numerical al-
gebraic geometry to approximate continuations along paths with rigorous er-
ror bounds – are known [HRS18, Section 3]. Unfortunately, modiﬁed methods
working to compute local monodromy are currently only conjectured, the dif-
ﬁculty being a way to certify that one has sampled enough curves to have a set
of generators for the local monodromy group (so that if all generators are the
identity then p is a multiple point).
Example 10.55. Let Q1(x, y) = xy −z3 and Q2(x, y) = xy. Both varieties
contain the origin, where they have leading homogeneous term xy. However,
the origin is a multiple point of VQ2 but not a multiple point of VQ1. This
can be established, for instance, by varying a line parallel to the z-axis through
x = y = α as α traces out a small circle around the origin. The three roots are
the three values of α2/3, and permute cyclically when α makes one loop around
the origin. Hence the local monodromy group is not the trivial group. This
example illustrates the value of the monodromy characterization, as showing
local monodromy to be non-trivial may be easier than showing irreducibility
in the local ring.
◁
10.5 Surgery, non-generic directions, and non-arrangement
points
Instead of the iterated residue approach described above, multiple points were
originally studied using a surgery method involving only univariate residues.
While iterated residues provide a more direct path to coeﬃcient asymptotics
for multiple points, and work under weaker assumptions, the surgery method
does have some advantages. For instance, in addition to more elementary com-
putations, the explicitness of intermediate steps allows one to analyze certain
non-generic and degenerate cases.
In this ﬁnal section we follow the surgery approach, computing an explicit
univariate residue and employing an analytic trick to asymptotically evaluate
the resulting integrals. To simplify our discussion, we consider only power
series expansions and assume that each smooth divisor meeting at a multiple
point is locally parametrized by the same coordinates z1, . . . , zd−1. Recall from
previous chapters that for any d-vector v we write v◦= (v1, . . . , vd−1).
Consider a multivariate generating function F(z) = P
r∈Nd arzr with do-
main of convergence D. For the remainder of this section, we make the fol-
lowing assumptions.
(1) F is meromorphic on some open set D′ containing D.
328
Multiple point asymptotics
(2) p ∈Cd
∗is a strictly minimal contributing point of F in a direction ˆr∗.
(3) In a neighborhood of p, we can write
F(z) =
P(z)
Q1(z) · · · Qn(z)
with each Q j having nonvanishing gradient at p.
The implicit function theorem implies the Weierstrass factorization
F(z) =
ψ(z)
Qn
j=1(1 −zdv j(z◦))
(10.25)
at p, where ψ(p) , 0 and the vj are analytic at p◦with v j(p◦) = 1/pd. We call
the v j the inverse roots of the Q j at p, and their reciprocals u j(z◦) = 1/vj(z◦)
the roots of the Q j at p.
Remark 10.56. More generally, we could have
F(z) =
P(z)
Q1(z)m1 · · · Qn(z)mn
for any positive integers mj. We stick to the simple pole case where m = 1
for two reasons. First, the general case is already covered above. Second, it
is always possible to reduce to the simple pole case using cohomological re-
ductions (see [AY83, Theorem 17.6] or the deﬁnition of iterated residues for
non-smooth higher order poles in Appendix C). Laurent series can also be
treated in an analogous manner.
Exercise 10.13. Show that Q(x, y) = 2 −x −2y + y2 has a multiple point at
(1, 1), and ﬁnd a Weierstrass factorization of 1/Q there.
A residue sum
Let w ∈D be suﬃciently close to w and let C = T(wd), so that breaking apart
the Cauchy integral for ar gives
ar =
1
(2πi)d
Z
T(w◦)

Z
C
F(z) dzd
zrd+1
d

dz◦
(z◦)r◦−1 .
Analogously to the smooth case described in Chapter 9, for a suﬃciently small
neighborhood N of p◦in T(p◦) we can ﬁnd a point w′ suﬃciently close to
p such that h ˆr(p) > h ˆr(w′) and N × C′ is disjoint from V for C′ = T(w′
d).
Deﬁning
χ =
1
(2πi)d
Z
N

Z
C−C′ F(z) dzd
zrd+1
d

dz◦
(z◦)r◦−1
(10.26)
10.5 Surgery, non-generic directions, and non-arrangement points 329
Figure 10.15 Two tori around a multiple point.
then gives the following result, mirroring the smooth case.
Lemma 10.57. Under the assumptions above, |pr (ar −χ)| →0 exponentially
fast in |r| as r →∞with ˆr →ˆr∗.
Proof
If
R1 =
1
(2πi)d
Z
T(p◦)\N

Z
C
F(z) dzd
zrd+1
d

dz◦
(z◦)r◦−1
and
R2 =
1
(2πi)d
Z
N

Z
C′ F(z) dzd
zrd+1
d

dz◦
(z◦)r◦−1
then
ar =
1
(2πi)d
Z
T(p◦)

Z
C
F(z) dzd
zrd+1
d

dz◦
(z◦)r◦−1
= R1 +
1
(2πi)d
Z
N

Z
C
F(z) dzd
zrd+1
d

dz◦
(z◦)r◦−1
= R1 + R2 + χ.
The quantity |prR1| is exponentially small because F(z◦, t) is analytic for t in
an annulus extending beyond |pd| by an amount bounded away from zero when
z◦< N. The quantity |prR2| is exponentially small because the integrand of
R2 is exponentially smaller than p−r on its domain of integration.
□
Let Λ denote the set of values z◦∈N for which the roots u1(z), . . . , un(z)
330
Multiple point asymptotics
are not all distinct, and for z◦< Λ deﬁne
R(z◦) = −
n
X
j=1
Res
t=uj(z◦)
 F(z◦, t)
trd+1
!
.
(10.27)
Because (10.26) is absolutely integrable, it follows from the univariate residue
theorem that
χ =
1
(2πi)d−1
Z
N
R(z◦)
dz◦
(z◦)r◦+1
(10.28)
when Λ has measure zero.
If R had the form A(z◦)e−λφ(z◦), which it does in the smooth case, then we
could asymptotically approximate (10.28) as a Fourier–Laplace integral using
the results of Chapter 5. Unfortunately, the n summands deﬁning R have this
form, but each on its own is not integrable when there is more than one sheet
meeting at p. To work around this diﬃculty, we introduce a new integral ex-
pression representing R as a symmetric rational sum.
Let ∆n−1 denote the standard (n −1)-simplex
∆n−1 =
t ∈Rn
≥0 :
n
X
j=1
t j = 1
,
which is parametrized by its projection
π∆n−1 =
t ∈Rn−1
≥0 :
n−1
X
j=1
t j ≤1

onto its ﬁrst n −1 coordinates. We write ι for the map ι(t) = (t1, . . . , tn−1, 1 −
Pn−1
j=1 tj) that inverts the projection, so that ι(t) · v is a convex combination:
ι(t) · v = t1v1 + · · · + tn−1vn−1 +
1 −
n−1
X
j=1
t j
vn .
Lemma 10.58. Let f be an analytic function of one complex variable and let
v1, . . . , vn ∈C be distinct. Then
n
X
j=1
f(vj)
Q
r,j(vj −vr) =
Z
π∆n−1
f (n−1) (ι(t) · v) dt .
(10.29)
Applying this with f(v) = vrd+n−1ψ(z◦, 1/v) to the inverse roots v j(z◦) yields
R(z◦) = −
Z
π∆n−1
f (n−1) (ι(t) · v(z◦)) dt .
(10.30)
10.5 Surgery, non-generic directions, and non-arrangement points 331
Proof
The identity (10.29) is proved in [DL93, p. 121]. The second conclu-
sion follows from (10.27), since each zd = uj(z◦) is a simple pole and
Res
t=uj(z◦)
 F(z◦, t)
trd+1
!
= vj(z◦)rd+n−1ψ(z◦, 1/vj(z◦))
Q
r, j[vr(z◦) −v j(z◦)]
=
f(vj(z◦))
Q
r,j[vr(z◦) −vj(z◦)].
□
Exercise 10.14. Use the Fundamental Theorem of Calculus to verify (10.29)
in the case n = 2.
Theorem 10.59. Under the assumptions above
ar ∼
 1
2πi
!d−1 Z
N
 Z
π∆n−1
h ι(t) · v(z◦) dt
!
dz◦
(z◦)r◦+1 ,
(10.31)
where
h(y) = dn−1
dyn−1
 
yrd+n−1ψ
 
z◦, 1
y
!!
.
This estimate holds uniformly as r →∞with r = λ ˆr∗+ O(1).
Proof
If r = λ ˆr∗then the result follows from Lemmas 10.57 and 10.58. If
r = λ ˆr+α then there is an extra factor of z−α in the integrand. If α is bounded
then this extra factor and all its derivatives are uniformly bounded, meaning the
remainder in an asymptotic expansion changes in a uniform manner.
□
Asymptotic formulae
Having derived (10.31), we are now ready to compute asymptotics. First, we
make a change of variables z◦= p◦eiθ = (p1eiθ1, . . . , pd−1eiθd−1) to convert the
neighborhood N of p◦in T(p◦) to a neighborhood N′ of the origin in Rd−1.
Let ∆= π∆n−1, let dt denote the push-forward of Lebesgue measure by π, and
let E = N′ ×∆, which we equip with the measure dθ ×dt. Deﬁne the functions
φ(θ, t) = ir◦· θ
rd
−log

pdι(t) · v(p◦eiθ)

βj(s) =
(n −1)!Γ(s + n)
j!(n −1 −j)!Γ(s + j + 1)
A j(θ) =
 d
dy
! j
ψ(p◦eiθ, 1/y)

y=v j(p◦eiθ)
332
Multiple point asymptotics
for 0 ≤j ≤n −1, and observe that βj(s) is a constant multiple of a falling
factorial with n −j −1 terms, and therefore has degree n −j −1 in s.
Lemma 10.60. The right side of (10.31) in Theorem 10.59 can be rewritten
as
χ =
 1
2π
!d−1
p−r
n−1
X
j=0
βj(rd)
Z
E
e−rdφ(θ,t)A j(θ) d(θ) × dt,
(10.32)
and the phase φ satisﬁes Re φ ≥0 on E.
Proof
Applying the Leibniz rule for diﬀerentiating a product to f in (10.30)
yields
f (n−1)(y) =
n−1
X
j=0
 n −1
j
! d
dy
!n−1−j
yrd+n−1
 d
dy
! j
ψ(p◦eiθ, 1/y)
=
n−1
X
j=0
(n −1)!(rd + n −1)!
j!(n −1 −j)!(rd + j)!yrd+j
 d
dy
! j
ψ(p◦eiθ, 1/y)
= yrd
n−1
X
j=0
βj(rd)yj
 d
dy
! j
ψ(p◦eiθ, 1/y) .
Plugging this into (10.30) and using the deﬁnitions of Aj, φ, and pj yields the
stated formula. By strict minimality of p, for each j the modulus of vj(z◦)
achieves its maximum only when z = p◦. Thus each convex combination of
v j(z◦) with z , p has modulus less than |vj(p◦)|, meaning that Re φ ≥0 on E
with equality only on {0} × ∆.
□
Analysis of the integral in (10.32) requires the advanced Theorem 5.3 from
Chapter 5, as the simpler Theorem 5.2 assumes that the real part of the negative
phase function has a strict minimum in the interior of the domain of integration.
Our present assumptions imply that Re φ will be strictly positive away from
the origin in the θ-coordinates, but allow the real part of φ to vanish up to the
boundary in the t-coordinates.
To apply Theorem 5.3 we need to determine the set G′ of stratiﬁed critical
points for which Re φ is maximized, i.e., the critical points in {0} × ∆. Let C
be the n × d matrix with entries
Cij =

pjpd
∂vi
∂zj (p)
if j < d
1
if j = d.
Exercise 10.15. What is the exact relation between C used in this section and
ΓΨ used in the residue approach?
10.5 Surgery, non-generic directions, and non-arrangement points 333
Proposition 10.61. Fix a vector r ∈N(p). The set G′ of critical points of φ in
the direction ˆr on E is the set of points (0, t) with t ∈S(r), where
S(r) =
(
t ∈π∆n−1 | ι(t)C(p) = r
rd
)
.
Proof
Since Re φ(θ) > 0 when θ , 0, all critical points in G′ are of the
form (0, t) for t ∈∆n−1. In fact, φ is somewhat degenerate: φ(0, t) = 0 for
all t ∈∆n−1, so not only does the real part of φ vanish when θ = 0, but also
the t-gradient of φ vanishes there. This is something of a blessing: checking
for non-zero derivatives in directions for which the point (0, t) is interior to E
reduces to checking whether or not the θ-gradient vanishes at (0, t). For j , d,
∂φ
∂θ j
= i
 rj
rd
−
zj
ι(t) · v(p◦)ι(t) ·
 ∂
∂z j
!
v(z◦)
!

z=p
and the result follows because vj(p◦) = 1/pd for all j.
□
Specialization to known cases
Proposition 10.61 may look ugly, but it simpliﬁes in several situations. For
instance, if p is a transverse multiple point then the rows of C are linearly
independent and there is at most one point in S. The normal cone N(p) is the
set of convex combinations of the lognormal vectors, so there is at least one
point in S and S is a singleton {t}. If r is interior to N(p) then t is in the interior
of ∆.
Conversely, if two sheets of singularities V1 = V(Q1) and V2 = V(Q2) are
tangent then the ﬁrst two rows of C are equal, so any solution t leads to a line
of solutions (t1 −s, t2 + s, t3, . . . , tn). For example, if d = n = 2, then N(p) is a
singleton and S is the whole unit interval.
Proposition 10.62 (Hessian of φ in the singleton case). Suppose that S con-
sists of the single point (0, t∗). Then the Hessian matrix of rdφ(θ, t) at (0, t∗)
has the block form
H(0, t∗) =

H(0, t∗)
−iC
T
−iC
0
,
(10.33)
where
• the (d −1) × (d −1) block H(0, t∗) is the Hessian of the restriction of rdφ to
the θ-variables,
• the zero block has dimensions (n −1) × (n −1), and
• the (n −1) × (d −1) matrix C is formed by subtracting the last row of C
from each other column, and stripping the last row and column.
334
Multiple point asymptotics
Remark 10.63. The last column of H in (10.33), corresponding to the dth
coordinate, is stripped oﬀbecause this is a function of the others in the θ
parametrization; the last row is stripped oﬀbecause we parametrize the simplex
by its ﬁrst n −1 coordinates.
Proof
Let v denote the vector function (v1, . . . , vn). Constancy of φ in the t-
directions at θ = 0 shows that the second partial derivatives in those directions
vanish, giving the block of zeros. Computing (∂/∂θj)φ gives, up to a constant,
−
i
ι(t)v(z◦) ι(t)zj
∂
∂zj
v(z◦)

z=p
.
Because ι(t)v(θ, t) is constant in t when θ = 0, diﬀerentiating in the t direc-
tions recovers the blocks −iC and −i(C)T. The second partial derivatives in
the θ directions are unchanged.
□
Specializing further yields a proof of Theorem 10.38 via surgery.
Surgery proof of Theorem 10.38
Under our assumptions S is a singleton, so
we may apply Theorem 5.3 to the integral over E in each summand of (10.32)
giving an asymptotic series in decreasing powers of rd. The polynomials βj
decrease in degree from n −1 to zero and integration may be carried out term
by term because the remainders are uniformly one power of rd lower as long
as ˆr is restricted to a compact subset of N(p). The leading term comes from a
careful examination of the terms appearing in the saddle point integral.
□
Remark 10.64. Theorem 5.3 allows us to localize as long as we don’t put a
boundary somewhere that the height is maximized while simultaneously cre-
ating a critical point somewhere in a stratum of this boundary. This allows us
to go beyond the standing hypothesis of strict minimality in Theorem 10.59
and Lemma 10.60, however the analysis of maximal height critical points in
Proposition 10.61 is more complicated.
The surgery method handles complicated geometries of the stationary set
better, in principle, than the method of iterated residues. One example of this
advantage appears when ˆr is on a facet of N(p) (a face of the cone whose
dimension is one less than the dimension of the whole cone).
Theorem 10.65. Fix a direction ˆr = ˆr∗and assume that the hypotheses of
Theorem 10.38 hold with m = 1, except that ˆr∗lies on a facet of N(p) instead of
being in the interior. If r →∞such that r−|r| ˆr∗stays bounded, an asymptotic
expansion of the form (10.17) still holds. The leading term in this expansion is
half the value Theorem 10.38 would predict if ˆr∗were in the interior of N(p).
10.5 Surgery, non-generic directions, and non-arrangement points 335
Proof
The condition that ˆr∗is on a facet of N(p) is equivalent to the condition
that ι(t(r∗)) is on a facet of ∆n−1. The main contribution to the inner integral
in (10.32) comes from an ε-ball about t(r) for any suﬃciently small ε > 0, and
when t is on a facet this integral is over a halfspace neighborhood rather than a
ball neighborhood. The leading term in such an integral is precisely half of the
leading term for a ball neighborhood. After introducing a factor of 1/2 in the
inner integral of (10.32), the new hypotheses leave everything else unchanged.
This proves the result when r is a precise multiple of ˆr∗. When r −|r| ˆr∗is
bounded, the uniformity statement in Theorem 10.59 shows that (10.31) and
hence (10.32) remain valid, introducing the factor of 1/2 and completing the
proof.
□
Example 10.66 (two lines, boundary directions). Suppose F = 1/Q(x, y),
where
Q(x, y) =
 
1 −1
3 x −2
3y
! 
1 −2
3 x −1
3y
!
.
As we have seen in Example 10.27, ars ∼3 when r, s →∞with r/s in a
compact subset of (1/2, 2). By Theorem 10.65, the coeﬃcients along the (1, 1)-
diagonal are asymptotically half of the coeﬃcients on the interior of the cone
1/2 < r/s < 2, thus
a2s,s ∼3/2
as s →∞. In fact, this approximation holds for any ars with r−2s = O(1). Note
that as we approach the boundary of the cone from the interior, the convergence
to the limiting value becomes slower and slower; on the boundary the relative
error term is no longer exponentially small, but of order 1/s.
◁
Remark 10.67. The requirement that r −|r| ˆr∗remain bounded is not best
possible. In [BMP23, Section 6.2] it is shown that, for linear divisors, uniform
estimates hold when |r
−|r| ˆr∗| = o(|r|1/2), yielding a Gaussian transition
regime whose width scales as |r|1/2.
Non-arrangement points
As a ﬁnal application of the surgery method, we consider the case where
n = d = 2 and the two divisors V1 and V2 meet tangentially. In this case,
the meeting point p is not an arrangement point because the intersection lat-
tice of the divisors has order 2, whereas the intersection lattice of the tangent
planes has order 1 (both tangent lines coincide). Furthermore, the normal cone
at p degenerates to a single ray, so that this direction is a boundary direction
336
Multiple point asymptotics
and hence is not generic. For these reasons we turn to surgery. The Fourier–
Laplace integral in Theorem 10.59 is more degenerate than can be handled by
Theorem 5.3 of Chapter 5. However, we can still complete the analysis for this
speciﬁc situation.
Proposition 10.68 (two curves intersecting tangentially in two dimensions).
Suppose that F(x, y) = P(x, y)/ (Q1(x, y)Q2(x, y)), where Q1 and Q2 deﬁne
smooth divisors V j intersecting at a strictly minimal multiple point (1, 1). Sup-
pose further that V1 and V2 intersect tangentially at (1, 1), where ∇log Q1 and
∇log Q2 are both multiples of some direction (λ, 1). Let u1 and u2 denote ana-
lytic functions such that V j = {(x, u j(x)) : x ∈C} in a neighborhood of (1, 1),
let v j(x) = 1/uj(x) denote the inverse roots, and let gj(θ) = log v j(eiθ) be the
parametrization of the logarithmic inverse roots in polar coordinates. If
gj(θ) = ir∗θ −κj
2 θ2 + O(θ)3
for each j with κ1 + κ2 > 0, the κ j nonnegative, and P(1, 1) , 0 then
ars ∼P(1, 1)
√
2π
2
√κ1 + √κ2
s1/2
as (r, s) →∞with r = λs + O(1).
Proof
Lemma 10.60 implies that
ars ∼
s
(2πi)2
Z
E
e−sφ(θ,t)A0(θ) dθ dt
for (r, s) = λ(ˆr, ˆs) + O(1), where E = N × π∆1 with N a neighborhood (−δ, δ)
of zero in R, the amplitude A0(x, y) = P(x, y)/(xy), and π∆1 = [0, 1]. The phase
function φ is the convex combination
−φ(θ, t) = tg1(θ) + (1 −t)g2(θ),
which has nonnegative real part on (−δ, δ) × [0, 1], which vanishes on the line
segment S = {0} × [0, 1]. As opposed to previous cases we have considered,
the entire line segment is now critical for φ. Integrating e−sφ(θ,t) dθ over (−δ, δ)
for ﬁxed t gives
(2πsκt)−1/2 + O

s−3/2
,
where κt = tκ1 + (1 −t)κ2 is the quadratic term of φ(θ, t). The O(s−3/2) error
term is uniformly o(s−1/2), therefore the expression for the leading term may
10.5 Surgery, non-generic directions, and non-arrangement points 337
be integrated over [0, 1]. Using the change of variables y = κt leads to
ars ∼P(1, 1) √s
√
2π
Z 1
0
κ−1/2
t
dt
= P(1, 1) √s
√
2π
Z κ1
κ2
y−1/2
dy
κ1 −κ2
= P(1, 1) √s
√
2π
2
√κ1 + √κ2
.
The substitution y = κt, dy = (κ1 −κ2) dt is valid only when κ1 , κ2 but the
resulting expression for
R 1
0 κ−1/2
t
is valid for all κ1, κ2 ≥0 with κ1 + κ2 > 0.
□
Example 10.69 (partial sums of normalized binomials, continued). Recall
the generating function F =
2
(2−x−y)(1−xy) from Example 10.11, whose (s, s)-
coeﬃcient is the normalized binomial sum Ps
i=0 4−i2i
i

computing the expected
number of returns of a simple random walk to zero by time 2s. Expanding
functions g1(θ) = −log(2 −eiθ) and g2(θ) = iθ around θ = 0 gives quadratic
coeﬃcients κ1 = 2 and κ2 = 0, so the identity P(1, 1) = 2 implies
as,s ∼2
r s
π .
This result can be veriﬁed by univariate methods, as the main diagonal has the
algebraic generating function f(z) = (1 −z)−3/2. Note that even though (1, 1)
is a complete intersection, there is no longer an exponentially decreasing error
term. Instead the relative error is O(1/s).
◁
Notes
Computations for multiple points based on the theory of iterated residues ﬁrst
appeared in the work of [BM93] on queueing models. More information on
iterated residues can be found in [AY83; Pha11]. As noted above, the coeﬃ-
cient asymptotics in this chapter were ﬁrst computed via the surgery method
in [PW02; PW04]. The surgery method is only valid in its original form for
ﬁnitely minimal points, which is why more advanced methods using hyper-
bolic polynomials and Morse theoretic arguments were introduced. The spe-
cial case where all divisors are linear, and the pole variety is a hyperplane
arrangement, is worked out at length in [BMP23].
The computation of the residue from an explicit factorization via Algo-
rithm 4 is eﬀective, assuming the factors Q j are in a nice class of functions
338
Multiple point asymptotics
such as polynomials or algebraic functions. The eﬃciency of such algorithms
is a topic of ongoing study. Some speciﬁc problems that can be studied with the
results of this chapter can likely be improved with a more focused study. For
instance, De Loera and Sturmfels [DS03] discuss alternate approaches to the
enumeration of lattice points in a polytope, one involving computation of the
Todd class of an associated toric variety and another pioneered by Barvinok et
al. [Bar94].
The decomposition of the positive orthant into regions (chambers) in which
the counts vary polynomially are objects of classical study, as are the counts
themselves; one example is the enumeration of lattice points in the dilated
Birkhoﬀpolytope, where even the leading term asymptotic was found only in
2009 [CM09].
The fact that the iterated residue of a rational function is a polynomial for
complete intersections, and its consequences for generating function asymp-
totics, are discussed in [Pem00].
The proof of Lemma 10.45 suggested by Exercise 10.16 was supplied to us
by Frank Sottile.
Additional exercises
Exercise 10.16. Assume the hypotheses of Lemma 10.45. Prove the following
statements, then prove Lemma 10.45.
(a) The gradients ∇Qi(p) are non-zero for all i ≤n.
(b) For any U ⊆T, let VU = T
i∈U Vi. If the set of gradients {∇Qi(p) : i ∈U}
are linearly independent then VU is smooth near p and equal to VT.
(c) For such sets U, the ideal ⟨fi : i ∈U⟩is reduced in Op.
(d) For such sets U, the ideal ⟨fi : i ∈U⟩is prime in Op.
Exercise 10.17. Suppose that d = 2 and let p be a homogeneous point of V
of degree k. Prove that p is a multiple point or is a cusp whose tangents are all
equal.
Exercise 10.18. Let F(x, y, z) =
z/2
(1−yz)(1−(x+x−1+y+y−1)z/2+z2) be the Aztec dia-
mond placement generating function, to be studied in Example 11.45 and The-
orem 11.49. For what directions ˆr are there critical points on the stratum which
is the intersection of the two divisors in the denominator of F? Determine, up
to a constant factor, the asymptotic contribution at such a point. (These points
never contribute to the leading asymptotics of arst, their contribution being too
small to contribute in the cases when there is no exponential decay as in The-
orem 11.49 and too large to contribute when there is, as in Example 11.45.)
