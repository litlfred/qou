---
doc_id: arxiv-1001.2933v4
doc_title: "Analytic Continuation Of Chern-Simons Theory"
section_id: sec-020-5-2-the-trefoil-knot
section_title: "The Trefoil Knot"
section_number: "5.2"
pages: 94-108
source_pdf: 1001.2933v4.pdf.txt
source_sha256: b02636c86d593c02
toc_source: inferred
---
5.2 The Trefoil Knot
For both of our examples, the necessary facts about the representation of the fundamental
group of the knot complement are described in [17]. We begin with the case that our knot
K is the trefoil.
The fundamental group of S
3\K can be described by two generators x, y with one relation
xyx = yxy. x and y are both conjugate to the meridian mb; for further details, see fig. 11
in [17]. The longitude is bl = yx2yx−4.
For every choice of the conjugacy class of mb (apart from certain exceptional values that
will be discussed), there are up to gauge transformation two SL(2, C) flat connections on
S
3\K. The first is an abelian flat connection Aab with x = y = diag(m, m−1
). (As usual m
is the eigenvalue of the meridian mb.) Its Chern-Simons invariant vanishes.
There is also a nonabelian flat connection Anab whose monodromies are given up to
conjugation by29
x =

m 1
0 m−1

, y =

m 0
1 − m2 − m−2 m−1

. (5.7)
The eigenvalue of the longitude is
l = −m
−6
. (5.8)
According to (4.35), in SU(2) Chern-Simons theory, m is of modulus 1, so we will need
to analyze this case carefully. If |m| = 1, the flat connection Anab has a structure group
that reduces to either SU(2) or SL(2, R). This can be anticipated as follows. The complex
conjugate of a representation of the fundamental group in SL(2, C) is still a representation
of the fundamental group in SL(2, C), in general with m → m. However, if |m| = 1, the
operation m → m is equivalent to m → m−1 and does not affect the conjugacy class of the
meridian, which is

m 0
0 m−1

. (5.9)
So for |m| = 1, representations of the fundamental group in SL(2, C) occur in complex
conjugate pairs or else are isomorphic to their own complex conjugates. A representation
with the latter property has a structure group that reduces to a real form of SL(2, C) –
either SU(2) or SL(2, R).
For the trefoil knot, as there is only one nonabelian representation up to conjugacy, it
must be equivalent to its own complex conjugate. Concretely, let us try to conjugate the
29Our m is called m1/2
in [17].
94

representation into SU(2). We set
C =

1 −(m − m−1)
−1
0 1 
, (5.10)
so
CxC
−1 =

m 0
0 m−1

(5.11)
is an element of SU(2). Then
CyC
−1 =

(m − m3)
−1
(m − m−1)
−2
1 − m2 − m−2(m−1 − m−3)
−1

. (5.12)
If x and y can be conjugated into SU(2), this can be done in a way that makes x diagonal.
Having put x in the form (5.11), the only further conjugation that leaves it diagonal is by
a diagonal matrix diag(λ, λ−1). Conjugation by a diagonal matrix can map a unimodular
matrix of the form

a b
c a

, (5.13)
such as CyC
−1
, into SU(2) if and only if bc < 0. For |m| = 1, this is equivalent to
1 > m
2 + m−2
, (5.14)
and that therefore is the condition that the flat connection Anab has structure group SU(2).
If instead
1 < m
2 + m−2
, (5.15)
the structure group of Anab reduces to SL(2, R).
5.2.1 Singularities Of The Moduli Space Of Flat Connections
The remaining case 1 = m2 + m−2requires further study. This case corresponds to a singularity of the moduli space of flat connections, where different branches meet, as we will now
describe.
The condition 1 = m2 + m−2is equivalent to
ln m = ±iπ/6, mod πiZ. (5.16)
In this case, the monodromies of eqn. (5.7) are strictly upper triangular, and the structure
group of a flat connection Anab with those monodromies reduces to the triangular subgroup
of SL(2, C), and not to either SU(2) or SL(2, R). In this exceptional case, there is also
95

another flat connection A′
nab that is inequivalent to Anab; its monodromies are the lower
triangular cousins of eqn. (5.7):
x =

m 0
1 m−1

, y =

m 0
0 m−1

. (5.17)
A′
nab is actually gauge equivalent to the complex conjugate of Anab; indeed, eqn. (5.7),
specialized to m2+m−2 = 1, can be transformed to (5.17) via complex conjugation composed
with conjugation by the matrix Ω = 
0 1
−1 0
.
Both Anab nor A′
nab represent unstable critical points in Chern-Simons theory, as their
structure groups are strictly triangular. In fact, when 1 = m2 + m−2, the only semistable
critical point is the abelian one Aab with x = y = diag(m, m−1). Let us discuss the behavior
of Chern-Simons theory in the vicinity of Aab. We think of Aab as a diagonal flat connection
with C
∗
structure group

∗ 0
0 ∗

(5.18)
embedded in SL(2, C). If m is fixed (by specifying the values of n and k in Chern-Simons
gauge theory), then Aab has no diagonal deformations as a flat connection. However, it does
have off-diagonal deformations. There is a one-dimensional space of deformations of upper
triangular form

0 u
0 0
. (5.19)
A deformation of Aab with u 6= 0 gives, up to gauge transformation, the triangular flat
connection Anab. The value of u does not matter, as long as it is nonzero, because Aab has
a C
∗ group of symmetries consisting of constant gauge transformations diag(λ, λ−1
), and
these act on u by u → λ
2u. Similarly (or by complex conjugation composed with the gauge
transformation Ω), Aab has a one-dimensional space of lower triangular deformations

0 0
−v 0

. (5.20)
v transforms under C
∗ by v → λ−2
v, so if v is nonzero, its value does not matter. A lower
triangular deformation of Aab with nonzero v gives A′
nab.
If we take u and v to be both nonzero, then only their product uv is C
∗
-invariant. It
is not possible to take both u, v 6= 0 without varying m away from m2 + m−2 = 1. This is
evident from (5.7), according to which a two-dimensional representation of the fundamental
group of S
3\K that is not triangular has m2 + m−2 6= 1. Let ǫ = 1 − m2 − m−2
; ǫ is real if
|m| = 1. In the space of possible deformations of Aab to an irreducible flat connection, we
can normalize the coordinates u, v so that the relation between u, v, and ǫ is uv = ǫ. This
statement simply says that for a non-abelian flat connection Anab, the C
∗
-invariant uv has a
96

unique value for all ǫ (since Anab is unique up to gauge transformation), with uv = 0 at ǫ = 0
(as we know from eqn. (5.7)), and finally the zero of uv at ǫ = 0 is simple (the monodromies
(5.7) show that it is possible to have u ∼ 1, v ∼ ǫ, and so uv ∼ ǫ; this should be no surprise
as there is no symmetry that would force uv to have a zero of higher order).
Now let us specialize this to SU(2) Chern-Simons theory. In this case, the gauge field A
should be anti-hermitian, so we want v = u. Also, the symmetry group of the abelian flat
connection reduces to U(1) = SO(2). If we set u = x + iy, v = x − iy, where x, y are real
coordinates on the space of first order deformations of the flat SU(2) connection Aab, then
the relation between x, y and ǫ is
x
2 + y2 = ǫ. (5.21)
This equation has real solutions only for ǫ ≥ 0; this encodes the fact that Anab can be
conjugated to SU(2) only under that condition. Let us consider the exponent I = ikW(A)+
iIR(ρ, A) of the path integral of Chern-Simons theory for small ǫ and near the abelian flat
connection Aab. It has critical orbits with x = y = 0 and with x
2 + y2 = ǫ. Moreover, I
vanishes for the abelian flat connection Aab, corresponding to x = y = 0, and in general
is of order n in the semiclassical region of large n with fixed γ = n/k. Finally it has one
nonzero critical orbit at x
2 + y2 = ǫ. These facts suggest that −iI/n can be modeled near
x = y = ǫ = 0 by the simple SO(2)-invariant function
F(x, y) = c

1
2
(x
2 + y2
)
2 − ǫ(x2 + y2
)

(5.22)
with a real constant c. We will verify this shortly using (5.26), but for the moment let us
discuss the implications.
Generically, in expanding around a flat connection, the Chern-Simons function is a nondegenerate Morse function in the directions transverse to the gauge orbits. When this is so,
after gauge fixing, the expansion around a given critical point can be approximated for large
n and k as an infinite-dimensional (oscillatory) Gaussian integral. Nondegeneracy is visible
in (5.22) for ǫ 6= 0. As long as ǫ does not vanish, x = y = 0 is a nondegenerate critical point
of F(x, y), and near the critical orbit x
2+y2 = ǫ, the function F(x, y) is nondegenerate in the
directions transverse to the SO(2) action. However, this nondegeneracy and the Gaussian
nature of the Chern-Simons path integral break down at ǫ = 0, where the two critical orbits
meet.
The expansion of the Chern-Simons path integral around a critical point can then no
longer be approximated by a Gaussian, but the Gaussian approximation fails only for the
two variables x and y. To improve upon the Gaussian approximation, we need only a suitable
approximation to the dependence of I on x and y near the singularity. Assuming that (5.22)
is an appropriate approximation, we can model the integral over the variables x and y by
Z
dx dy exp (inF(x, y)). (5.23)
97

(For the constant multiplying this integral, see (5.5).) The integral (5.23) was studied in
section 3.4.2 as a basic example of an oscillatory integral with symmetry. There were two
main results in that discussion.
First, in eqns. (3.59) and (3.60), we analyzed the integral by a simple scaling argument.
According to (3.59), the integral is n
−1/2
times a transcendental function (essentially an error
function) of n
1/2
ǫ. In the limit n → ∞, ǫ → 0 with n
1/2
ǫ fixed, the colored Jones polynomial
will equal n
1/2
times this error function (times a constant described in (5.5)). The factor of
n
1/2
is most obvious in the special case ǫ = 0: according to (3.60), compared to the behavior
with ǫ 6= 0, the large n behavior of the integral gains an extra factor of n
1/2 at ǫ = 0. We
can immediately apply this to the invariant Jn(k) at the values of n/k (such as 1/6 or 5/6)
that correspond to ǫ = 0 or m2 + m−2 = 1. We expect Jn(k) to grow with a factor of n
1/2 at
ǫ = 0, relative to its behavior for generic real ǫ:
Jn|
ǫ=0
Jn|
ǫ6=0
∼ n
1/2
, n → ∞. (5.24)
This is a known result (Theorem 1.2 of [16]). We have expressed the result in terms of a
ratio of values of Jn because our normalization of Jn (as a path integral rather than a ratio
of path integrals) is not the most common one in the mathematical literature. With the
usual normalization, the colored Jones polynomial is of order 1 for ǫ < 0 and of order n
1/2
at ǫ = 0.
Second, in section 3.4.2 we made a direct analysis of the Stokes phenomena in passing
through ǫ = 0 (or more generally in crossing Stokes lines that pass through ǫ = 0). These
results only depend on the singularity at ǫ = 0, so they carry over immediately to ChernSimons theory. Thus, we can understand some Stokes phenomena in SU(2) Chern-Simons
theory without having to solve four-dimensional flow equations. Details are discussed in
section 5.2.3.
Finally let us return to (5.22), but now consider it as a model of the behavior of SL(2, C)
gauge fields near the singularity at ǫ = 0. In SL(2, C), x and y are complex and the symmetry
group is C
∗
. Unlike the case of SU(2), where the critical orbit x
2+y2 = ǫ becomes equivalent
to x = y = 0 if we set ǫ = 0, in SL(2, C) the equation x
2+y2 = 0 can be solved with x, y 6= 0.
Modulo the C
∗
symmetry (which acts by x ± iy → λ
±2
(x + iy)), the locus with x
2 + y2 = 0
but (x, y) 6= (0, 0) consists of two points, (x, y) = (1, ±i). These two points correspond to
the triangular flat connections Anab, A′
nab. It is also possible to specialize the analysis to
SL(2, R) gauge fields – the same singularity will also play a role in SL(2, R) Chern-Simons
theory – but we leave this for the reader.
98

5.2.2 The Chern-Simons Function
To understand possible Stokes phenomena and to determine the asymptotic behavior of the
Chern-Simons path integral, we must evaluate the Chern-Simons function W(A) for the
flat connection Anab. For this, we use (4.42), which along with (5.8) gives δW(Anab) =
−(6/π)δm/m · ln m = −(3/π)δ ln2 m. So W(Anab) = −3 ln2 m/π + constant. To determine
the constant, we observe that in general W(A) vanishes mod 2π for a representation with
triangular structure group, which we have in the present problem at the values of ln m given
in (5.16). Thus
W(Anab) = −
3
π
ln2 m −
π
12
− 2πs, s ∈ Z. (5.25)
As we are planning to analytically continue in k, we have made explicit the possibility of
adding to W(A) an integer multiple of 2π. We can now evaluate I = ikW(A) + (n − 1) ln l,
using l = −m−6and ln m = iπ(n − 1)/k to evaluate ln l. In the semiclassical limit of large
n, k, we ignore the difference between n−1 and n. However, we do want to take into account
the multivaluedness of ln l, as explained at the end of section 4.2.5. We get
I(Anab) = ik 
3πn2
k
2
−
π
12
− 2πs− in 6π
n
k
+ 2π(r − 1/2), r, s ∈ Z. (5.26)
Alternatively, in terms of γ = n/k, we can write
I(Anab) = −in3πγ + (π/12 + 2πs)γ
−1 + 2π(r − 1/2)
. (5.27)
We can use these formulas to justify (5.22). The relation between m and γ is ln m = iπγ,
so ǫ = 1 − m2 − m−2 vanishes precisely if
γ = ±(1/6 + p), p ∈ Z. (5.28)
For any number y that is congruent to ±1/6 mod Z, the nonabelian flat connection Anab
with γ = y and
s =
3y
2
2
−
1
24
r =
1
2
− 3y (5.29)
is equivalent to an abelian flat connection Aab with its canonical lift (zero Chern-Simons
invariant and ln l = 0). The values of r and s were chosen to ensure vanishing of both
contributions to I(Anab), namely ikW(Anab) and (n − 1) ln l. With these values of r and s,
we find for any γ
I(Anab) = −3πinγ−1

γ − y
2
. (5.30)
99

So for γ = y +ǫ, I is of order nǫ2
. The fact that the coefficient of ǫ
2
is nonzero is the content
of (5.22). Any SO(2)-invariant function F(x, y, ǫ) that vanishes at x = y = 0, has only one
critical orbit with (x, y) 6= 0 that approaches (x, y) = 0 for ǫ → 0, and is of order ǫ
2
at
this orbit, can be put in the form (5.22) modulo a change of variables (an SO(2)-invariant
redefinition of x and y that is the identity near x = y = 0). Possible higher order terms in
F are irrelevant in the sense of singularity theory and do not affect the estimate (5.24) of
the critical behavior of the Chern-Simons path integral.
5.2.3 The Integration Cycle And The Asymptotic Behavior Of The Path Integral
An obvious consequence of (5.26) is that for real k and n, the nonabelian critical points have
I imaginary. Since Re I is strictly increasing or decreasing along a flow line, and vanishes on
the real integration cycle CR, this implies that for real n and k, there are no flows between
CR and a nonabelian critical point. Hence for γ real and small, the integration cycle CR is
simply the Lefschetz thimble Jab associated to the real critical point Aab.
Extending this reasoning slightly, for real n and k, all critical points, abelian or nonabelian, have Re I = 0. So there are no non-trivial flows between them.
How then can anything nontrivial happen for real values of n, k? Something nontrivial
must happen because for suitable real γ, the nonabelian flat connection Anab is SU(2)-valued
and hence must contribute to the SU(2) Chern-Simons path integral.
The answer to this question is that on the real γ axis, jumping of the Lefschetz thimbles
Jσ, or of the coefficients in the usual expansion C =
P
σ
nσJσ, occurs only at values of γ
where two different flat connections become coincident. At these points, which were identified
in eqn. (5.28), Chern-Simons theory has jumping phenomena that can be understood from
a finite-dimensional model of the appropriate singularity, as described in section 5.2.1.
Here we will analyze the integration cycle of the Chern-Simons path integral, and its
asymptotic behavior, for γ close to the real axis. For a full analysis of what happens throughout the complex γ plane, one must analyze the Stokes curves; we postpone this to section
5.2.4.
We want to express the integration cycle of the Chern-Simons path integral for the trefoil
knot in terms of Lefschetz thimbles associated to critical points. To this aim, we let Jab be
the Lefschetz cycle associated to the abelian critical point Aab with its canonical lift. Jab
is the appropriate integration cycle for sufficiently small γ = n/k. It will become clear that
cycles associated to other ways of lifting the Chern-Simons invariant W(Aab) will not play
100

any role. (This is actually a general property for any knot.)
On the other hand, we do have to consider distinct cycles associated to different ways of
lifting the Chern-Simons invariant W(Anab) of the nonabelian critical point Anab, in other
words different choices of the integer s in (5.25). For each number x that is congruent to
±1/6 mod Z, we write Jx for the Lefschetz thimble associated to Anab, with its Chern-Simons
invariant determined by the choice s = 3x
2/2 − 1/24 as in (5.29). These cycles differ only
by the lifting of the Chern-Simons invariant, so they are equivalent when the Chern-Simons
level k is an integer.
We fix the relative orientations of the cycles Jx by requiring that when k is an integer,
the Chern-Simons path integral over Jx is independent of x. Momentarily, we will fix the
overall orientations of the Jx by making a choice for J1/6.
Near γ = 0, the appropriate integration cycle of Chern-Simons theory is simply Jab. Now
we will explore what happens when γ departs from zero, but only near the real γ axis, so
that we only need to worry about jumping due to singularities. As we increase γ along the
positive real axis, nothing happens until we reach the value γ = 1/6. At this point, we meet
a singularity of a type analyzed in sections 3.4.2 and 5.2.1, associated with the fact that
Aab and Anab become stably equivalent30 at γ = 1/6. The resulting Stokes phenomenon
was analyzed in eqn. (3.61): Jab jumps by ±J1/6, depending on orientation. (Jab and J1/6
correspond to Jp and JO in (3.61).) We pick the orientation so that for γ slightly greater
than 1/6, the integration cycle of Chern-Simons theory is Jab + J1/6.
There is a simple intuitive meaning to this result. In general, for integer values of n, k,
the path integral of Chern-Simons theory is given asymptotically for large n and fixed n/k
by a sum over contributions of all SU(2)-valued flat connections, all with weight 1. For
1/6 < n/k < 5/6, there are two such connections, namely Aab and Anab, and both must
contribute with weight 1 to the integration cycle. As long as k ∈ Z, the different Jx are
equivalent, and it does not matter which of them we include. But to describe the analytic
continuation away from integer k in the region just to the right of the Stokes curve that
passes through γ = 1/6, the right integration cycle is Jab + J1/6.
Increasing γ further, nothing new happens until we reach γ = 5/6. In crossing γ = 5/6,
nothing happens to J1/6, but Jab will jump again, picking up ±J5/6. We claim that (with
the orientation convention chosen above) a minus sign is the right choice here, and hence
that the appropriate integration cycle just beyond γ = 5/6 is Jab + J1/6 − J5/6.
To explain why the sign is negative, consider again the behavior for integer n, k with
30This means the following. Anab is triangular at γ = 1/6 and its diagonal part coincides with Aab, so the
gauge orbit containing Anab has Aab in its closure. Hence, to construct a sensible (Hausdorff) moduli space
of flat connections, one has to consider Anab and Aab to be equivalent.
101

5/6 < n/k < 7/6. In this region, the only SU(2)-valued flat connection is the abelian
one, and hence the large n, fixed n/k behavior of the path integral must be given by the
contribution of Aab alone. The contribution of Anab must vanish for integer k. Since J1/6
and J5/6, which arise from two different liftings of Anab, are equivalent for integer k, the
minus sign in the integration cycle Jab + J1/6 − J5/6 ensures this.
Increasing γ further, nothing happens until we reach γ = 7/6. At this point, Jab jumps by
±J7/6. In this part of the real γ axis, there is again an SU(2)-valued flat connection that must
contribute with weight 1. So the sign is + and the integration cycle is Jab+J1/6−J5/6+J7/6.
The next jump is at γ = 11/6, where we must add −J11/6 to the integration cycle.
In general, if x > 0 is a number of the form ±(1/6 + p), p ∈ Z, then just to the right of
γ = x, the appropriate integration cycle is
Jab + J1/6 − J5/6 ± · · · ± Jx. (5.31)
Similarly, for negative γ, the integration cycle is Jab + J−1/6 − J−7/6 ± · · · ± Jx, for the most
negative relevant value of x.
Having found the right integration cycle, it is straightforward to determine the asymptotic behavior of the Chern-Simons path integral for n → ∞ with fixed γ. In general, a
flat connection Aσ with nσ 6= 0 makes a contribution to the path integral which in the
semiclassical limit is of order exp(Iσ), where Iσ is the value of the exponent of the path
integral at A = Aσ. Unless Iσ = 0, this contribution has an exponential dependence on n
for large n, since Iσ is of order n in the semiclassical limit. In general, exp(Iσ) multiplies an
asymptotic series in (not necessarily integral) powers of n. In the context of an expansion
around a complex critical point, this series has been studied in detail in [18]. The dominant
contribution to the path integral, for a given γ, is the one that maximizes Re Iσ, subject to
the condition nσ 6= 0.
In the case of the trefoil knot, the abelian flat connection Aab has Iab = 0. Its contribution
Zab to the path integral is bounded (in fact, of order 1/
√
n) for n → ∞ with fixed γ. On
the other hand, a non-abelian connection Anab, lifted so that it meets the abelian one at
γ = y, has Iy = −3πinγ−1(γ −y)
2
, according to (5.30). So, assuming the relevant coefficient
– which we will call ny – is not zero, the asymptotic behavior of its contribution to the
Chern-Simons path integral is
Zy ∼ exp(−3πinγ−1(γ − y)
2
). (5.32)
These contributions are all oscillatory as long as γ is on the real axis. (On the real axis, they
actually dominate Zab in absolute value by a factor of √
n for large n.) As soon as γ departs
from the real axis, the Zy grow or decay exponentially for n → ∞, depending on the sign of
102

the real part of the exponent. If γ = a + ib with a, b real, the real part of the exponent is
Re log Zy = 3πnb 1 −
y
2
a
2 + b2

. (5.33)
Near the real axis, and assuming |a| > |y| (as otherwise ny = 0), this is positive if and only if
b > 0. So near the real axis, the condition for exponential growth of Jn(q) is that |a| > 1/6
(so that one of the ny is nonzero) and Im γ > 0. In this region, Re log Zy is maximal for
y = ±1/6, so this contribution dominates Jn(q). In section 5.2.4, we will analyze the Stokes
curves and extend this analysis to the rest of the complex γ plane.
What we have just obtained (except so far restricted to the region near the real γ axis)
is the standard picture of the colored Jones polynomial of the trefoil knot. For example,
see eqn. (2.2) of [7] or Proposition 3.2 of [16], where this invariant, and its cousins for
other torus knots, is written as the sum of contributions that correspond to our Zab and
Zy (with the same values of y). The starting point was an integral representation for the
colored Jones polynomial of a torus knot which originally was deduced using formulas that
come from braid group representations, quantum groups, and conformal field theory [5, 30].
This integral representation has recently been obtained directly from the Chern-Simons path
integral [34].
5.2.4 Stokes Curves
By a Stokes curve, we mean a curve l in the complex γ plane on which distinct critical points
have the same value of the quantity Im I that is conserved in the flow equation. There are
many such curves. But we only really care about Stokes curves across which some jumping
occurs. It turns out that there are far fewer of these.
Our basic strategy will be to show that every Stokes curve intersects the real γ axis. But
we already know from section 5.2.3 what sort of jumping occurs along the real axis. It takes
the form Jab → Jab ± Jy, where Jy is a cycle associated to one of the lifts of Anab. This will
enable us to get a general description of the integration cycle. In fact, it turns out that the
integration cycle always takes the form of (5.31), or its cousin with negative x, with some x
that depends on γ in a way that will emerge.
A preliminary observation is that there are no flows between abelian critical points differing in the values of r, s, since all such critical points have Re I = 0, but Re I is never
constant along a non-trivial flow. So in any flow between two critical points, at least one of
them is nonabelian.
To show that all Stokes curves intersect the real γ axis, we use the explicit formula for
I and the fact that Im I is conserved by the flow equations. Equivalently, the conserved
103

quantity is Im I/πn. For a lift of Anab, this can be conveniently expressed in terms of
γ = n/k:
Im I/πn = −Re 3γ +

1
12
+ 2s

γ
−1 + 2r − 1

. (5.34)
If γ = a + ib with a, b real, then
Im I/πn = −3a −

1
12
+ 2s

a
a
2 + b2
− 2r + 1. (5.35)
Let us first consider Stokes curves at which there might be flows between nonabelian
critical points with different values of r, s. The change in Im I/πn in such a process is
∆(Im I/πn) = −2

a ∆s
a
2 + b2
+ ∆r

, (5.36)
where ∆s, ∆r are the jumps in s and r. Setting this to zero, we get
a
2 + b2 +
a ∆s
∆r
= 0. (5.37)
The case ∆s = 0 is not of interest, for then vanishing of (5.36) implies ∆r = 0, in which
case the initial and final critical points are the same and the flow is trivial. If ∆s and ∆r
are both nonzero, the Stokes curve is a circle that intersects the real γ axis in two points; if
∆r = 0, it becomes the line a = 0, intersecting the real γ axis at one point. Either way, at
an intersection point of one of these Stokes curves with the real axis, two nonabelian critical
points with different values of r, s remain different, and there are no flows between them,
since in general there are no non-trivial flows for real γ.
In general, for two critical points pσ, pτ , along a Stokes curve l characterized by Im Iσ =
Im Iτ , the integer mστ that counts flows between pσ and pτ is constant, except possibly at a
point along l at which a third critical point pν has Im Iν = Im Iσ = Im Iτ . Such a point is
a triple intersection of Stokes curve (equality of any two of Im Iσ,Im Iτ , and Im Iν defines
such a curve). At a triple intersection point there can be jumping mστ → mστ + mσνmντ .
Eqn. (5.37) implies that there are no triple intersection points involving different lifts of
Anab. (Two of the curves defined by eqn. (5.37) can intersect away from the real γ axis only
if they coincide identically, in which case the effects they produce can again be analyzed
from what happens on the real axis.) We need not worry about the case that pν is a lift of
Aab, since in this case mντ = 0, as we learned in section 3.3.4.
Hence the net number of flows between nonabelian critical points differing in the values of
r and s is zero anywhere along one of these Stokes curves. So there are no Stokes phenomena
involving flows between different lifts of Anab.
104

The same type of argument can be used to constrain Stokes phenomena involving a flow
between the abelian critical point and a nonabelian one. If we pick the canonical lift of Aab,
it has I = 0 and the change in Im I/πn is given in (5.35). Setting the right hand side of
that equation to zero, we get the equation for a Stokes curve:
b
2 = −
a(3a
2 + (2r − 1)a + (2s + 1/12))
3a + 2r − 1
. (5.38)
If we pick a different lift of Aab, we get the same formula with shifted values of r, s. However,
a byproduct of the following calculation will be to show that different lifts of Aab do not
enter the integration cycle; indeed, all jumping phenomena take the form of (3.61) and do
not shift the “abelian” part of the integration cycle.
Eqn. (5.38) describes many Stokes curves, labeled by the choice of r and s and a component of the part of the a axis on which the right hand side of (5.38) is nonnegative.
Such a component is either a closed interval whose endpoints are zeroes of the numerator
a(3a
2 + (2r − 1)a + (2s + 1/12)) or a half-open interval whose endpoints are such a zero and
the zero of the denominator. Each component intersects the a axis, either in two points (the
first case) or one point (the second case).
We now make the familiar argument. Since every Stokes curve l intersects the a axis, the
jumping that occurs in crossing l anywhere can be deduced from what happens in crossing l
where it meets that axis. If l intersects the a axis at a value of a not of the form ±(1/6 + p),
with p ∈ Z, then l is irrelevant because no jumping can occur at such a value of a. Even
if l intersects the a axis only at a point of the form ±(1/6 + p), something non-trivial can
happen only if r and s are of the form given in (5.29). The reason for this last statement is
that as there are no non-trivial flows for real γ, all that can happen in crossing l at a point
y = ±(1/6 + p) is that some lift of Anab may coincide with Aab with its canonical lift. For
this to happen, r and s must be related to y by (5.29).
So the relevant Stokes curves are determined by their intersection point y = ±(1/6 + p)
with the real axis; the curve is described by (5.38) with r, s given in (5.29). In this special
case, (5.38) simplifies to
b
2 = −
a(a − y)
2
a − 2y
. (5.39)
We now meet a situation described at the end of section 3.4.2. Eqn. (5.39) gives the
condition that a flow is possible between Aab (with its canonical lifting) and Anab (with its
chosen lifting). The flow will go from Aab to Anab if Re I(Anab) is negative, and in the other
direction if Re I(Anab) is positive. However, we also know from the analysis in section 3.4.2
of a singularity of the type that occurs at a = y (or from a more general argument in section
3.3.4) that no jumping comes from flows from Anab to Aab. So just as in fig. 5, we can throw
105

Figure 13: The Stokes curve (5.39) consists of both the solid and dashed curves, but just as in fig.
5, jumping occurs only across the solid part of the curve. (Only the solid parts, therefore, will be
drawn in fig. 14.)
away the part of the curve (5.38) with Re I(Anab) > 0. As sketched in fig. (13), the part of
the curve that we keep is the part with yb(y − a) > 0.
Keeping only the “good” parts of these curves, they divide the complex γ plane in a
way that is sketched in fig. 14. The important point here is that any point γ = γ0 that
is not on one of the relevant Stokes curves can be connected to the a axis in a unique way
(topologically) without crossing any of those curves. The integration cycle C of Chern-Simons
theory analytically continued to γ = γ0 is given by the same formula as on the part of the
a axis to which γ0 can be connected without crossing a Stokes curve. This result for the
integration cycle is in full accord with other analyses of the colored Jones polynomial of the
trefoil knot. What we call the Stokes curve (5.39) – or more exactly the relevant portion of
it with yb(y − a) > 0 – is the curve across which an extra term appears in eqn. (2.2) of [7].
The analytically continued function Jn(q) grows exponentially in the semiclassical region
whenever Re I > 0 for a critical point that contributes to the path integral. This happens
precisely if Im γ > 0 and |γ| > 1/6. (Those conditions are strong enough to ensure, using
eqn. (5.39), that a critical point with y = 1/6 or −1/6 contributes to the path integral, and,
using eqn. (5.33), that it has Re I > 0.)
We are left with only one more issue, which is the behavior along the positive imaginary
γ axis. As one approaches the positive imaginary γ axis from the right, one crosses all
Stokes curves of positive y. As one approaches it from the left, one crosses all Stokes curves
106

Figure 14: The Stokes curves across which jumping occurs for the trefoil knot divide the complex
γ plane as shown here. Sketched here are the curves corresponding to y = ±5/6, ±7/6, and ±11/6.
(All the other curves for larger or smaller values of |y| are obtained from these by suitable scalings
of the γ-plane.) Drawn are only the parts of each curve that actually produce jumping; these
portions meet only at γ = 0, where they all join.
of negative y. A first consequence is that, precisely on the positive imaginary axis, the
representation of the Chern-Simons integration cycle as a sum over Lefschetz thimbles is an
infinite sum. A second consequence is that, unless we can consider the Lefschetz thimble
Jy to be equivalent to J−y, this representation of the integration cycle jumps in crossing
the positive imaginary γ axis. Indeed, in a complete circuit around the point γ = 0, one
crosses exactly once each of the relevant Lefschetz thimbles of fig. 14. This will produce a
monodromy of infinite order, and hence an essential singularity in the integral, unless Jy is
equivalent to J−y.
Can we consider Jy and J−y to be equivalent? Referring back to (5.29), we see that
y → −y amounts to s → s with an integer change in r. In other words, it amounts to a
change in the choice of branch of ln m. The branch of ln m is irrelevant as long as n ∈ Z and
we choose not to replace the loop space of G/TC by its universal cover. This appears to be
the right sense in which the integration cycle is univalent near γ = 0, but clearly, a study of
more examples is needed. For n 6∈ Z, the monodromy of the integration cycle is unavoidable
and an essential singularity of the integral at γ = 0 should be expected.
107
