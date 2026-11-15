---
doc_id: arxiv-1001.2933v4
doc_title: "Analytic Continuation Of Chern-Simons Theory"
section_id: sec-021-5-3-the-figure-eight-knot
section_title: "The Figure-Eight Knot"
section_number: "5.3"
pages: 108-121
source_pdf: 1001.2933v4.pdf.txt
source_sha256: b02636c86d593c02
toc_source: inferred
doc_brief: "Analytic Continuation Of Chern-Simons Theory — The title of this article refers to analytic continuation of three-dimensional ChernSimons gauge theory away from integer values of the usual coupling"
---
5.3 The Figure-Eight Knot
Here we will consider in a similar way the figure-eight knot (also known as the 41 knot),
which we denote K. The fundamental group of S
3\K again has two generators x, y, either
of them conjugate to the meridian mb, with one relation. The relation is ωx = yω, with
ω = xy−1x
−1y.
For a generic eigenvalue m of the meridian, there are up to gauge transformation three
SL(2, C) flat connections on S
3\K. As usual, one is an abelian flat connection Aab, whose
monodromies are up to conjugacy x = y = diag(m, m−1). In addition, there are two nonabelian flat connections with monodromies
x =

m 1
0 m−1

, y =

m 0
−d m−1

, (5.40)
with
d =
1
2

m
2 + m−2 − 3 ±
p
(m2 + m−2 + 1)(m2 + m−2 − 3). (5.41)
The longitude is bl = xy−1xyx−2yxy−1x
−1
, leading to
l =
1
2

m
4 − m2 − 2 − m−2 + m−4

±
m2 − m−2
2
p
(m2 + m−2 + 1)(m2 + m−2 − 3). (5.42)
We denote as A± a flat connection with the monodromies just indicated. These are the
SL(2, C) flat connections that, if m = ±1, are related to the complete hyperbolic metric on
S
3\K.
The longitude l is a zero of the A polynomial, which is
A(l, m) = l −

m
4 − m2 − 2 − m−2 + m−4

+ l
−1
. (5.43)
Apart from the standard symmetries m → −m and m → m−1, this has an additional symmetry l → l
−1
, which exchanges the two branches of the square root in (5.42). This symmetry
reflects the existence of a diffeomorphism τ of S
3
that maps K to itself, reversing the orientation of K but preserving the orientation of its normal bundle. (τ acts on the above
presentation of the fundamental group by x ↔ y.) Such a symmetry maps m → m, l → l
−1
.
It reverses the orientation of S
3
, so it changes the sign of the Chern-Simons function W(A)
and is not a symmetry of Chern-Simons gauge theory. Nevertheless, it will help us in understanding the behavior of the theory. A knot for which such a symmetry exists is called
amphichiral. Actually, the figure-eight knot is amphichiral in the strong sense that S
3
admits
another diffeomorphism τe that maps K to itself (pointwise) while reversing the orientation
of its normal bundle. (It acts on the presentation of the fundamental group by x → y
−1
,
y → x
−1
.) Again, τe reverses the orientation of S
3 and reverses the sign of the Chern-Simons
invariant. It acts by m → m−1, l → l. (We leave it to the reader to verify that the unknot is
108

a simpler example of a knot in S
3
that admits diffeomorphisms of both of these types.) The
product τ τe preserves the Chern-Simons invariant and acts by m → m−1, l → l
−1
.
Unlike the trefoil, where all of the interesting action occurs for |m| = 1, for the figure-eight
knot both the real m axis and the circle |m| = 1 are worthy of careful study. The eigenvalues
of an element of SL(2, R) are either real or of modulus 1, so in general flat connections with
SL(2, R) structure group may have |m| = 1 (as for the trefoil) or real m (as happens for
the figure-eight knot). The eigenvalues of an element of SU(2) are of modulus 1, so flat
connections with SU(2) structure group will arise only for |m| = 1.
5.3.1 Real m
Suppose first that m is real and that
m
2 + m−2 > 3. (5.44)
Then by inspection, for both flat bundles A±, the matrices x and y are real, so the entire
representation of the fundamental group has its image in SL(2, R). The diffeomorphism τ
exchanges A+ with A− (since it maps l → l
−1
). It leaves Aab invariant.
The region with m real and
m
2 + m−2 < 3 (5.45)
is also easy to understand qualitatively. The flat connections A+ and A− are still exchanged
by τ . Now, however, they are no longer real (since the square roots in the monodromy
formulas are imaginary) and are exchanged by complex conjugation. In fact, the region
m2+m−2 < 3 includes the points m = ±1 where A+ and A− are the SL(2, C) flat connections
that are related to a hyperbolic metric on S
3\K.
As one might expect, among the most interesting points on the real m axis are the points
with
m
2 + m−2 = 3. (5.46)
For such m, since d vanishes, the matrices x and y are both upper triangular. The flat
bundles A+ and A− become equivalent to each other. They are unstable upper triangular deformations of the abelian flat bundle Aab. Aab, just as in (5.18), is a diagonal flat
connection

∗ 0
0 ∗

. (5.47)
It has automorphism group C
∗
; this symmetry group reduces to R
∗ ∼= SO(1, 1) if we consider
Aab (for real m) as a flat bundle with structure group SL(2, R). The symmetry extends to
O(1, 1) if we include the outer automorphism of SL(2, R) corresponding to conjugation by
109

diag(1, −1) or diag(i, −i), and we will do so.31 Aab has no deformations as a flat bundle
with specified m, but as in (5.19), it has a one-dimensional space of deformations of upper
triangular form

0 u
0 0
. (5.48)
Here u is a real parameter if we consider deformations in SL(2, R). The value of u, assuming
it is not zero, does not matter modulo the action of O(1, 1), and the upper triangular
deformation gives us the triangular flat bundle A+ or A−. Just as in (5.20), Aab has a
similar lower triangular deformation, schematically

0 0
−v 0

. (5.49)
If we take v 6= 0 but u = 0, we get a lower triangular flat bundle, and again the value of v
is inessential assuming that it is nonzero.
As in our discussion of the trefoil, there is no deformation with u, v nonzero and m2 +
m−2 = 3, since a flat SL(2, C) bundle at such a value of m is triangular (or abelian). If
we do turn on both u and v, the O(1, 1)-invariant parameter is the product uv. One might
expect as in the discussion of the trefoil that we would have uv ∼ ǫ where ǫ = m2 + m−2 − 3.
However, in (5.40) the upper triangular parameter is 1 and the lower triangular parameter
is −d, so this case corresponds to uv ∼ −d. Moreover, from (5.41), we have d ∼ ±√
ǫ near
ǫ = 0. Critical points therefore are at uv = 0 or ±
√
ǫ. Apart from a multiplicative constant,
the function with this critical behavior is
f(u, v) = (uv)
3
/3 − ǫuv. (5.50)
The oscillatory integral associated to this function was studied in section 3.4.3.
Why have we arrived at this peculiar structure, with no (uv)
2
term in f(u, v)? The
answer has to do with amphichirality. As τ leaves fixed Aab and exchanges A±, at a point
at which one of these becomes triangular and meets Aab, the other must do so as well. This
structure is lost if we add a (uv)
2
term to f. More fundamentally, τ reverses the sign of the
Chern-Simons function and hence of f, which describes its critical behavior. The fact that
τ exchanges A± implies that if we lift the action of τ to the flat bundle with connection Aab
in such a way that τ (u) = u, then τ (v) = −v. (By composing with the outer automorphism
of SL(2, R), one can also choose a lifting so that τ (u) = −u, τ (v) = v.) Thus, τ reverses the
sign of uv. Since τ reverses the sign of both uv and f, f is an odd function of uv, and this
accounts for the structure that we have found.
31In SL(2, R) gauge theory, one would consider two critical points that differ by this outer automorphism
to be inequivalent. But in SL(2, C) gauge theory, or analytic continuation of SU(2) gauge theory, which are
our focus in this paper, they are equivalent, since diag(i, −i) is an element of SU(2).
110

As in our analysis of the trefoil, some of the Stokes phenomena of Chern-Simons theory
of the figure-eight knot can be described in terms of critical behavior of the function f.
However, for brevity, the only issue that we will discuss here will be the large n behavior
of the colored Jones polynomial near ǫ = 0, that is, near m2 + m−2 = 3. First we simply
set ǫ = 0. The parameter λ in eqn. (3.65) corresponds in Chern-Simons theory to n (or
equivalently k, since the ratio n/k is fixed when we specify ǫ). So according to (3.65),
Jn(k)|
ǫ=0
Jn(k)|
ǫ<0
∼ n
2/3
, n → ∞. (5.51)
Accordingly, if we normalize the colored Jones polynomial of the figure-eight knot so that
it is of order 1 for ǫ < 0, then it is of order n
2/3
for ǫ = 0. This is a known result ( [16],
Theorem 1.1). Instead of simply setting ǫ = 0, we can consider the limit n → ∞, ǫ → 0 with
n
2/3
ǫ fixed. The singular contribution to the colored Jones polynomial is this limit follows
from (3.64) and is an Airy function (times n
2/3
in the usual mathematical normalization),
as one can see by introducing polar coordinates in the xy plane.
5.3.2 m Of Modulus 1
Now let us analyze what happens for |m| = 1. When are the flat connections A± unitary?
For this to be the case, l must be of modulus 1. From (5.42), the condition for this (assuming
that |m| = 1) is
m
2 + m−2 + 1 ≤ 0. (5.52)
Conversely, if this condition is obeyed and |m| = 1, one can explicitly conjugate the flat
bundle with monodromies (5.40) into SU(2) by the same steps that we used in discussing
the trefoil knot.
For |m| = 1 and m2 + m−2 + 1 > 0, the bundles A± have structure group SL(2, C).
A reduction to SL(2, R) cannot occur because mb has eigenvalues of unit modulus while bl
has real eigenvalues; commuting (and noncentral) elements of SL(2, R) do not have this
property. Also, the region |m| = 1, m2 + m−2 > 1 again contains the points m = ±1 where
the connections A± are SL(2, C) connections related to the hyperbolic metric on S
3\K.
As usual, we have to look more closely at what happens for m2 + m−2 + 1 = 0. It is
convenient to set ǫ = −m2 − m−2 − 1, so that ǫ is real for |m| = 1 and the flat connections
A± have SU(2) structure group precisely when ǫ ≥ 0. Unlike our previous examples, the
nonabelian flat connections A± remain irreducible at those points and as a result the abelian
flat connection Aab will play no role in critical behavior near ǫ = 0. All that happens when
ǫ = 0 is that the two critical points Aab become coincident. Moreover, near ǫ = 0, the
difference between the two critical points is of order ǫ
1/2
; this is evident from the formulas
111

(5.40) for the monodromies. Finally, the critical points are real (in the natural real structure
of SU(2) gauge theory) if ǫ > 0. These are the properties of the familiar function
f(x) = x
3
/3 − ǫx (5.53)
associated to the Airy integral. This function describes the critical behavior of the ChernSimons function W(A) near the points ǫ = 0, and hence in studying Stokes phenomena, we
will be able to borrow results from section 3.4.1.
For now, we simply describe qualitatively the behavior of the colored Jones polynomial
Jn(q) for real ǫ near ǫ = 0. First we consider the limit n → ∞ with ǫ fixed:
(1) For ǫ < 0, the only real critical point is the abelian one. Its contribution to the path
integral, for any knot, is of order 1/
√
n, so we have
Jn(q) ∼
C
n1/2
, ǫ < 0 (5.54)
with a constant C. (Actually, in a more precise description, C is the first term in an
asymptotic expansion C + C
′/n + . . . in integer powers of 1/n.)
(2) For ǫ > 0, the flat bundles A± appear as real critical points in the path integral. They
give oscillatory contributions, but without the factor 1/
√
n that appears in the contribution
of Aab. Including also the abelian contribution, the integral behaves as
Jn(ǫ) ∼
C
n1/2
+ C+ exp(inf+) + C− exp(inf−), ǫ > 0 (5.55)
with constants C± (which again are the leading terms of asymptotic series). Here we have
written the action I(A±) as inf±(ǫ), where f±(ǫ) is independent of n. We have f±(0) = 0,
since A± coincide with Aab at ǫ = 0. Also, as explained in section 5.3.3, f+(ǫ) = −f−(ǫ) for
real ǫ.
(3) What happens at ǫ = 0? Typically the n-dependence of the integral over any one
mode of the path integral is that of a Gaussian integral R
dx exp(inx2) ∼ 1/n1/2. For the
path integral around an irreducible flat connection with vanishing cohomology (such as A±
at ǫ 6= 0), these factors, after taking into account the regularization and the volume of the
gauge group, ultimately cancel in a complete evaluation of the path integral. This is why
the oscillatory terms in (5.55) do not have a power of n as a prefactor. But at ǫ = 0, the
integral over x, rather than being Gaussian, becomes Rdx exp(inx3) ∼ 1/n1/3 = n
1/6
/n1/2.
The denominator participates in the usual cancellation, but the numerator does not, so we
expect
Jn(0) ∼ n
1/6
. (5.56)
(In the usual mathematical normalization, one divides by the path integral (5.3) of the
unknot, and then the colored Jones polynomial grows as n
2/3
.)
112

So far we have described what happens for n → ∞ with fixed ǫ. If instead we consider
the limit n → ∞ with n
2/3
ǫ fixed, then in view of (3.55), the singular behavior of the colored
Jones polynomial is an Airy function (times n
2/3
in the usual mathematical normalization).
5.3.3 The Real Part Of The Chern-Simons Function
For the figure-eight knot, we will study only the simplest properties of the Chern-Simons
function.
First we focus on the region |m| = 1. We denote as C the operation of complex conjugation of a flat SL(2, C) bundle. C maps (m, l) to (m, l). Let us compose this operation with
the symmetry τe, which maps (m, l) to (m−1, l). The composite acts by (m, l) → (m −1
, l). If
|m| = 1, then m −1 = m and the action is (m, l) → (m, l).
There are two somewhat different cases:
(1) If m2 + m−2 + 1 < 0, the two flat bundles are SU(2) bundles with complex conjugate
values of l. The composite Cτe exchanges the two values of l, so it exchanges the two flat
bundles.
(2) If m2 + m−2 + 1 > 0, the two flat bundles are SL(2, C) bundles with real and unequal
values of l. The composite Cτe leaves fixed the two values of l, so it also leaves fixed the
isomorphism class of each of these two flat bundles.
Now let us analyze the Chern-Simons invariant W(A) in the two cases. C transforms W
to its complex conjugate, while τe (because it reverses the orientation of S
3
) maps it to −W.
So the composite maps W to −W.
In case (1), W is real, since in general the Chern-Simons invariant of an SU(2) connection
is real. So W transforms simply to −W under the exchange of the two flat bundles. Thus
they have equal and opposite real values of W.
In case (2), W is complex. The fact that the two flat bundles are invariant under Cτe tells
us that their Chern-Simons functions are invariant under W → −W. This tells us nothing
about Im W, but it implies that Re W = −Re W. Before concluding that Re W = 0, we
should recall that Re W is only well-defined modulo 2π. So the correct conclusion is only
that Re W vanishes mod π.
In case (2), we are left with two possible cases: Re W may vanish mod 2π or may equal
π mod 2π. The region m2 + m−2 + 1 > 0, |m| = 1, has two connected components, as m may
113

be near either 1 or −1. It turns out that Re W = 0 mod 2π if m is near 1, and Re W = π
mod 2π if m is near −1.
To show this, we observe first that if m2 +m−2 + 3 = 0, then the flat bundle is triangular,
which guarantees that W = 0 mod 2π. Let m0 be a positive root of the equation m2 +m−2 +
3 = 0. Then −m0 is a negative root. We can calculate W(A) for m = 1 by integrating eqn.
(4.42) along the real m axis from m0 to 1. We get
W(A; m = 1) = W(A; m = m0) + (1/π)
Z 1
m0
ln m d ln l. (5.57)
Along the integration path, ln m is real. On the other hand, according to eqn. (5.42), l is
of modulus 1 for m real,32 so ln l is imaginary. Hence, the integral is imaginary. Since the
integration constant W(A; m = m0) vanishes, we learn that
Re W(A; m = 1) = 0 mod 2π. (5.58)
Similarly we have W(A; m = −1) = W(A; m = −m0) + (1/π)
R −1
−m0
ln m d ln l, and again the
integration constant vanishes. But now we get a different result because the imaginary part
of ln m along the negative m axis is equal to π. From (5.42), we see that as m varies from
−m0 to −1, l makes a half-circuit around the unit circle from 1 to −1. So ln l changes by iπ
and finally we get
Re W(A; m = −1) = π mod 2π. (5.59)
Now let us discuss the behavior for m = exp(iπγ) as a function of real γ with |γ| ≤ 1.
The condition m2 + m−2 + 1 < 0 amounts to 1/3 < |γ| < 2/3. So case (2) in the above
analysis corresponds to |γ| < 1/3 or |γ| > 2/3. In either of those regions, Re W can only
take the values 0 or π, so it is constant by continuity.33 Hence Re W = 0 if |γ| ≤ 1/3, and
Re W = π if |γ| ≥ 2/3.
For 1/3 ≤ |γ| ≤ 2/3, there are up to isomorphism two flat SU(2) connections, which we
denote as A±. At |γ| = 1/3, A+ and A− both coincide with the flat SL(2, C) connection
considered in the last paragraph. So in that case, Re W = 0 mod 2π. It is convenient to lift
the Chern-Simons invariants so that A± have Re W = 0 at |γ| = 1/3.
Now let us follow the two SU(2) flat connections A+ and A− continuously from |γ| = 1/3
to |γ| = 2/3. At |γ| = 2/3, we can use (5.59), along with the constancy of Re W for
|γ| ≥ 2/3, to deduce that W(A+) and W(A−) are each congruent to π mod 2π. Since we
also showed above that W(A+) = −W(A−), it follows that for some integer w, we have
W(A±) = ±(2w + 1)π at |γ| = 2/3.
32Fundamentally, this reflects the fact that for m real, the two flat bundles are invariant under the composite
Cτ, which leaves real m fixed while mapping l to l
−1
.
33This constancy is also a direct consequence of eqn. (4.42). In the region in question, ln m is imaginary
and ln l is real, so the real part of ln m d ln l vanishes.
114

Figure 15: Qualitative behavior of the conserved quantity Im I/k for real critical points in the
region 1/3 ≤ |γ| ≤ 2/3. The structure is in perfect parallel with fig. 9 of section 3.5.2, except now
γ is plotted on the horizontal axis. At |γ| = 1/3 (left), there are a pair of real critical points for
every value of Im I/k of the form 2πw, w ∈ Z. Increasing |γ|, Im I/k increases for one of these
critical points and reduces for the other. At |γ| = 2/3 (right), the critical points recombine in pairs,
but now with Im I/k of the form (2w + 1)π, w ∈ Z.
It can be shown by integrating (4.42) that w = 1. (This is greatly facilitated by symmetrizing the integrand between γ and 1 − γ before attempting to integrate.) Now let us
discuss what happens when we include all possible lifts of W(A±).
For |γ| < 1/3, critical points come in complex conjugate pairs. In passing through |γ| =
1/3, a pair of complex conjugate critical points meet and recombine into two inequivalent
real critical points A±. Actually, this occurs infinitely many times, once corresponding to
each complex lift of W.
Increasing γ past |γ| = 2/3, the reverse process occurs: a pair of inequivalent real critical
points recombine into a complex conjugate pair of critical points. Again this actually occurs
infinitely many times.
The flow in W between |γ| = 1/3 and |γ| = 2/3 leads to a crucial detail. Actually,
this detail also arose in analytic continuation of the Bessel function in section 3.5, and was
illustrated in fig. 9. That figure is repeated for convenience in fig. 15, with a caption adapted
to the present problem. The point is that a pair of real critical points that are “born” at
|γ| = 1/3 with the same value of W no longer have the same value of W by the time they
“arrive” at |γ| = 2/3. Rather they have values of W that differ by 2π. The pairs of critical
points that separate at |γ| = 1/3 are not the same as the pairs that rejoin at |γ| = 2/3.
115

Precisely the same phenomenon led in section 3.4.2 to exponential growth of the analytically continued Bessel function for negative and non-integer values of κ. It should therefore
come as no surprise that this mechanism will lead to exponential growth of the function Jn(q)
associated to the figure-eight knot in the region |γ| > 2/3, as long as the Chern-Simons level
k is not an integer.
5.3.4 The Imaginary Part Of W
We will now discuss much more briefly the simplest properties of Im W along the unit circle
|m| = 1.
For m2 + m−2 + 1 ≤ 0, the nonabelian flat connections are SU(2)-valued flat connections
A±. As we have already noted, like any SU(2)-valued connections, these have Im W = 0.
For m2 + m−2 + 1 > 1, there are a pair of SL(2, C) flat connections A±, exchanged by
complex conjugation. Since Im W is odd under complex conjugation, we have Im W(A+) =
−Im W(A−).
The most important property of the invariant Im W is its relation to the hyperbolic
volume of the knot complement S
3\K. S3\K admits a complete hyperbolic metric, unique
up to diffeomorphism. Though this metric is complete, it has the property that the volume
is convergent.34 We denote this volume as V .
Like a hyperbolic metric on any three-manifold, the complete hyperbolic metric on S
3\K
determines a flat P SL(2, C) bundle on this manifold. Upon picking a spin structure on
S
3\K, the flat P SL(2, C) bundle can be lifted to a flat SL(2, C) bundle. The conjugacy
class of the meridian for this flat bundle is
mb = ±

1 1
0 1
, (5.60)
where the sign depends on the choice of spin structure (in other words, the two flat bundles
with different signs of m differ by twisting by a flat line bundle of order 2 – the operation
considered in section 4.2.7). The flow equations in the presence of such unipotent monodromy
were discussed in section 4.2.2; for our present purposes, all we need to know is that the
34Near K, the metric can be modeled by ds2 = z2
(dx
2 + dy2
) + dz
2/z2
, where x and y parametrize a
two-torus and K is at z = 0. Thus the region near K is the “infrared” region in the context of the AdS/CFT
correspondence. This description can be used to compute the conjugacy class of mb given in eqn. (5.60)
below. Both mb and bl arise in this description from shifts in x and y; such shifts correspond to unipotent
elements of P SL(2, C).
116

eigenvalue of mb is m = ±1. On the other hand, from eqn. (5.42), it follows that35 l = −1,
for either sign of m.
The relation between the hyperbolic volume and the Chern-Simons invariant is simply
that, if we label A± correctly,
Re (iW(A±; m = ±1)) = ±
V
2π
. (5.61)
This means that Im W(A±; m = ±1) = ∓V/2π. The sign may look unnatural, but it
ensures that A± make exponentially growing and decaying contributions to the path integral,
respectively; this seems like the most useful mnemonic.
If we depart from m = ±1, there is no longer a complete hyperbolic metric on S
3\K with
m as the eigenvalue of the meridian. But there is an incomplete hyperbolic metric with this
property (it has a conical singularity along K), and a statement along the lines of (5.61)
remains valid for this incomplete metric. We will not describe details here.
We have explained the qualitative properties of Re W and Im W that will be of most
concern for the limited application that we consider next. We should note, however, that (as
summarized in [17], for example) by integrating the usual formula (4.42) and using (5.42),
one can express W(A) for flat connections on the complement of the figure-eight knot in
terms of a dilogarithm function.
5.3.5 The Volume Conjecture For The Figure-Eight Knot
The volume conjecture for knots emerged from the following observation [2, 3] about the
analytically continued invariant Jn(q) of the figure-eight knot. For γ approaching 1 from a
direction away from the real axis, the large n behavior of Jn(q) is, roughly speaking,
Jn(q) ∼ exp(nV/2π), (5.62)
where V is the hyperbolic volume of the knot complement, discussed in section 5.3.4. A
more precise statement will emerge below.
A partial explanation of this was given in [6]. It was noted that nV/2π is the value
of the exponent I = ikW(A) of the analytically-continued Chern-Simons path integral
at the complex critical point A+. So an expansion around this critical point would give a
35From this we can actually give a new demonstration of one result of section 5.3.3, which was that Re W
shifts by π under m → −m. In section 4.2.2, we showed that the shift is ∆W = −i ln l, which here equals π
mod 2π as l = −1.
117

contribution growing as exp(V/2π). (In this paper, and subsequent literature, generalizations
of the statement to other values of γ were also made. For example, see [3, 5, 9].)
There has always been a puzzle about this partial explanation. For physical values of k
and n – positive integers – the Chern-Simons path integral is dominated in the semiclassical
limit by real critical points. Contributions, if any, of complex critical points are exponentially
small. Therefore, at least for positive rational values of γ = n/k, there are no exponentially
growing contributions to the path integral. How then can exponential growth be observed
just because γ is infinitesimally displaced from 1?
The reader who has paid close attention to sections 3.4.2 and 5.3.4 will hopefully anticipate the answer. Once we analytically continue away from integer values of k, we need to
work not on the space UC of complex-valued connections modulo gauge transformations, but
on a cover UbC on which the Chern-Simons function W(A) is C-valued (rather than valued in
C/2πZ). A given flat connection A corresponds to infinitely many critical points that differ
only by the choice of a complex lift of W(A). When the integration cycle of the analytically
continued theory is expressed in terms of Lefschetz thimbles associated to critical points,
it is possible for contributions from critical points that differ only in this lift to cancel for
integer k, but give exponential growth as soon as k is not an integer.
Let us first express in terms of Lefschetz thimbles the integration cycle C of Chern-Simons
theory for what proves to be the simplest case: positive integer k and n with 1/3 < γ < 2/3,
where as usual γ = k/n. This is easy to do because in this range there are no complex critical
points, only real ones. Up to gauge transformation, there is an abelian flat connection Aab,
and two nonabelian but SU(2)-valued flat connections A±. As they are all SU(2)-valued,
they all contribute to the integration cycle with a coefficient 1. This cycle is then in an
obvious notation
C = Jab + J+ + J−. (5.63)
As long as k and n are integers, there is also no problem in extending this answer outside
the range 1/3 < γ < 2/3. At either γ = 1/3 or γ = 2/3, there is an Airy-type singularity.
The two real flat connections A± recombine to a complex conjugate pair of SL(2, C)-valued
flat connections, which we will call A′
± for γ < 1/3 or A′′± for γ > 2/3. We choose the
subscript so that, as in (5.61) (where m = ±1 are treated together), Re (iW(A′
+)) > 0 for
γ < 1/3 and Re (iW(A′′
+)) > 0 for γ > 2/3. This ensures that the integrals over the Lefschetz
thimbles J
′
− and J
′′
− associated to A′− and A′′− are exponentially decaying, while the integrals
over the other Lefschetz thimbles J
′
+, J
′′
+ associated to A′+, A′′+ are exponentially growing.
When we cross the Airy-like singularities at γ = 1/3 or 2/3, according to eqn. (3.58), the
sum J+ + J− recombines to a Lefschetz thimble J
′
− or J
′′
−, whose contribution to the path
118

integral is exponentially decaying. The integration cycle thus becomes
C =
(
Jab + J
′
− for γ < 1/3
Jab + J
′′
− for γ > 2/3.
(5.64)
Now let us continue away from integer values of k and n. Starting in the region 1/3 <
γ < 2/3, to make an analytic continuation, we must pick lifts of the Chern-Simons invariants
W(A±). When we do this, we write, for example, J+,w for the Lefschetz thimble associated to
A+ with a Chern-Simons invariant 2πw; we extend this notation to the other flat connections
in an obvious way. Here for J±, the value of w mod Z depends smoothly on γ (varying from
0 mod Z at γ = 1/3 to 1/2 mod Z at γ = 2/3); for J
′
±, w takes values in Z; and for J
′′
±, w
takes values in 1/2 + Z.
If we do not want exponential growth for n → ∞ and γ < 1/3, we must pick the lifts
of W(A+) and W(A−) to be equal at γ = 1/3; otherwise, according to (3.58), in continuing
past the Airy singularity, J
′
+ as well as J
′
− will appear in the integration cycle, giving
exponential growth. Similarly, if we do not want exponential growth for γ > 2/3, we need
W(A+) = W(A−) at γ = 2/3. But it is impossible to obey both of these conditions, since
as was illustrated in fig. 15, if W(A+) and W(A−) are equal at γ = 1/3, then they differ by
2π at γ = 2/3, and vice-versa.
Exponential growth is therefore unavoidable, once k is not an integer, either for γ < 1/3
or for γ > 2/3. As explained in section 5.1, we wish to pick an analytic continuation that
leads to no exponential growth for γ < 1/3. A further clue is that, to preserve τ and
τe symmetry, Jn(q) should be real for real k. (Complex conjugation of the path integral
reverses the sign of k, but as the figure-eight knot is amphichiral, one can compensate for
this with the symmetry τ or τe.) This suggests that we should take the lift of A′
− such that
Re W(A′
−) = 0. Then the integration cycle for γ just less than 1/3 is
C = Jab + J
′
−,0
. (5.65)
Continuing past γ = 1/3, cycles J+,w and J−,w appear, initially with w = 0. But by
the time we reach γ = 2/3, the values are w = ±1/2, as we learned in section 5.3.4. So the
integration cycle as γ approaches 2/3 from below is
C = Jab + J+,1/2 + J−,−1/2. (5.66)
To continue past γ = 2/3, we use eqn. (3.57) to express J+,1/2 and J−,−1/2 in terms of
corresponding cycles J
′′
±,w. Since w does not change in this process, the result is J+,1/2 →
−J ′′
+,1/2 + J
′′
−,1/2
, and J−,−1/2 → J ′′
+,−1/2
. The integration cycle for γ just greater than 1/3
is therefore
C = Jab − J ′′
+,1/2 + J
′′
−,1/2 + J
′′
+,−1/2
. (5.67)
119

Near or on the real γ axis, with Re γ > 2/3, exponential growth comes from the terms
J
′′
+,−1/2 − J ′′+,1/2
in (5.67). Just as in the analytic continuation of the Bessel function, the
relative minus sign is the reason that exponential growth is avoided when k is an integer.
For γ near 1, using (5.61), the value of the path integral is
Jn(q) ∼ exp(nV/2π) (exp(−iπk) − exp(iπk)). (5.68)
Here the exponential factors exp(±iπk) reflect the values w = ±1/2 for the relevant Lefschetz
thimbles. Also, near γ = 1, we have written the exponentially growing factor as exp(nV/2π)
(with n rather than k in the exponent) to put the formula in a more recognizable form for
some readers.
The expression log Jn(q)/n does not have a simple large n limit if γ is on the real axis,
because of the oscillatory factor (exp(−iπk) − exp(iπk)). As soon as γ is off the real axis,
there is a simple limit, but it is discontinuous on the real γ axis. The reason for that is that
the large n limit of log (exp(−iπk) − exp(iπk)) /n is ∓iπk/n = ∓iπ/γ, depending on the
sign of Im k.
In the region 2/3 < γ < 4/3, the flat connection A+, with its various possible lifts, has
the maximum value of Re I, among all flat connections. This ensures that, once the cycles
J
′′
+,±1/2
appear in C at γ = 2/3, they cannot disappear at least until γ = 4/3. At γ = 4/3,
and more generally at every value of γ of the form ±1/3 mod Z, one meets another family
of Airy-type singularities. To analyze the consequences, it may be necessary to take into
account Stokes phenomena beyond what follows from the singularities. (For example, there
appears to be a Stokes line crossing the real γ axis between the values 2/3 and 1; if there is
a flow from Aab to A− along this line, this might cause J
′′
−,1/2
to disappear from C.)
The normalization of Jn(q) that is most often used in the mathematical literature differs
from ours by dividing by a factor (namely the right hand side of eqn. (5.3)) that has no
exponential growth in the semiclassical limit but does have a simple zero at γ = 1. This
makes the proper statement about the semiclassical limit simpler at γ = 1, though not at
other real values near γ = 1. The function Jn(q), normalized as we do, vanishes (assuming
that n is an integer) for q
n = 1 or n = k + 2. One may ask what that vanishing means in
the context of integration over Lefschetz thimbles. The answer is that it may be hard to see
the vanishing exactly, but we can certainly see it approximately. The exponentially growing
contributions cancel if n = k + 2, since after all this implies that k = n−2 is an integer. The
remaining contribution is then dominated by Jab, but this contribution vanishes at n = k+2
since at this value, the dimension of the automorphism group of the abelian flat connection
Aab increases.
120
