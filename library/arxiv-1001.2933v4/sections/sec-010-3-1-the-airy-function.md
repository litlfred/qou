---
doc_id: arxiv-1001.2933v4
doc_title: "Analytic Continuation Of Chern-Simons Theory"
section_id: sec-010-3-1-the-airy-function
section_title: "The Airy Function"
section_number: "3.1"
pages: 23-34
source_pdf: 1001.2933v4.pdf.txt
source_sha256: b02636c86d593c02
toc_source: inferred
doc_brief: "Analytic Continuation Of Chern-Simons Theory — The title of this article refers to analytic continuation of three-dimensional ChernSimons gauge theory away from integer values of the usual coupling"
---
3.1 The Airy Function
We begin by examining the Airy integral, initially defined for real λ:
Zλ =
Z ∞
−∞
dx exp iλ(x
3
/3 − x)

. (3.1)
We want to analytically continue the integral to complex λ. This will require deforming the
integration contour away from the real x axis, so we will regard the Airy exponent
I = iλ(x
3
/3 − x) (3.2)
as a function of complex variables x and λ. For real λ, the integration is over the real axis.
As λ varies, we will deform the integration cycle C so as to vary smoothly with λ and in such
a way that the integral always converges.
23

In the case of the Airy function, it is not hard to see by hand how to do this. We divide
the x-plane into “good” regions in which the imaginary part of λx3is positive and “bad”
regions in which it is negative. For positive λ, this is shown in fig. 1. The Airy integrand is
exponentially small in the good regions. The original oscillatory integral over the real x axis
is an integral over the boundary of two good regions. We can deform the contour slightly by
giving x a positive imaginary part so that it will connect two good regions. Now as we vary
λ (keeping away from λ = 0), the good regions rotate continuously to the left or the right,
and we simply rotate the integration contour C as λ varies so that C always connects two
good regions. This gives an analytic continuation of Zλ as a function of λ, but it also makes
it clear that there is a monodromy around λ = ∞ (or 0). In fact, as λ changes in phase by
2π, the three good regions are cyclically permuted. So Zλ has a monodromy of order 3.
Because the contour C does undergo a non-trivial monodromy as λ varies, it is useful to
consider all possible contours in this problem. Denote the three good regions as Vi, i = 1, 2, 3,
as in the figure. For each i, let Ci be a contour connecting region Vi to region Vi+1. The
integrals Zi,λ =
R
Ci
dx exp(iλ(x
3
/3−x)) converge for all i and λ, and any reasonable contour
along which one might integrate the Airy function exp(iλ(x
3
/3 − x)) (or the product of this
function and one with slower growth at infinity) is equivalent to a linear combination of the
Ci. However, the integrals Zi,λ are not independent. They obey
Z1,λ + Z2,λ + Z3,λ = 0. (3.3)
This reflects the fact that the sum of contours C1 + C2 + C3 can be deformed to zero.
3.1.1 Morse Theory
The Airy function is simple enough that we do not really need a more sophisticated theory. Nevertheless, we will use this simple example as a practice case for describing a more
sophisticated approach that is useful in generalizations. To formalize the sense in which
C1 + C2 + C3 = 0, it is useful to regard the Ci as relative homology cycles. Let X denote the
complex x-plane, and for real U, let XU be the part of X with Re(iλ(x
3/3 − x)) ≤ U. Any
reasonable integration cycle C for the Airy integral should represent an element of the relative
homology H1(X, X−T ; Z) for very large T. In other words, C is a closed cycle, and though it
may not be compact, its infinite ends should lie in X−T . Differently put, Re(iλ(x
3/3 − x))
must tend to −∞ at infinity in C.
The Ci have this property, and represent elements of the relative homology. Indeed, they
generate this relative homology, subject to the relation
C1 + C2 + C3 = 0. (3.4)
24

The fact that the Ci generates the relative homology is fairly obvious geometrically in this
simple example. X is contractible, but X−T is the union of three disjoint pieces. A one-cycle
that is non-trivial in H1(X, X−T ; Z) must connect distinct pieces of X−T . The relation (3.4)
is also clear geometrically.
The integration cycle that we started with for real λ – the real x-axis, which we will
call CR – is not quite an element of the relative homology, because at large |x| it lies on
the boundary of, rather than in the interior of, the good regions of fig. (1). However,
CR becomes an element of the relative homology once we displace it slightly by giving x
a small imaginary part ǫ with the same sign as λ. This multiplies the Airy integral by a
convergence factor exp(−λǫx2). The displaced cycle therefore represents an element of the
relative homology. And indeed since the displaced cycle connects two of the good regions at
infinity, it is equivalent to one of the Ci.
For generalizations, we need a more powerful way to analyze the relative homology. We
consider the real part of the Airy exponent
h = Re(I) (3.5)
as a Morse function. A Morse function is simply a real-valued function whose critical points
are nondegenerate. The critical points are the points at which all first derivatives of h vanish,
and nondegeneracy of a critical point means that the matrix of second derivatives is invertible
at that point. The number of negative eigenvalues of this matrix is called the Morse index
of the critical point.
In general, because of the Cauchy-Riemann equations, the critical points of the real part
of a holomorphic function I are the same as the critical points of I. So in this case, there
are two critical points which we call p±, located at x = ±1. The values of I and h at p± are
I± = ∓
2iλ
3
(3.6)
and
h± = ±
2 Imλ
3
. (3.7)
The critical points are nondegenerate, since ∂
2I/∂x2 6= 0 at x = ±1. In general, in a
complex manifold of complex dimension n, if h is a Morse function that is the real part of
a holomorphic function I, its isolated and nondegenerate critical points are all of index n.
(The general form of I near an isolated nondegenerate critical point is I = c+
Pn
i=1 z
2
i
, with
a constant c and local complex coordinates zi; if zi = ui + ivi then h = Re c +
Pn
i=1(u
2
i − v
2
i
)
and the matrix of its second derivatives is diagonal with n negative eigenvalues.) So in our
case, the critical points have index 1.
In general, any Morse function h on a manifold X can be used to compute upper bounds
on the ranks of the real homology (or cohomology) groups of X: the rank of the q-dimensional
25

homology of X is at most the number of critical points of h of Morse index q. If the differences
between the indices of distinct critical points of h are never equal7to ±1, then h is a perfect
Morse function and the ranks of the homology groups are equal to the upper bounds just
stated. In fact, in this case even the integral homology can be described via the critical
points. Our Morse function is perfect, since both critical points have index 1.
If X is a compact manifold, h is automatically bounded above and below, and the critical
points of a perfect Morse function determine the ordinary homology of X. In our case, X
is not compact, and we are dealing with a Morse function h that is unbounded above and
below. In such a case, the critical points of h determine relative homology groups, namely
the homology groups Hk(X, X−T ), where T is a large constant. In our example, h is a
Morse function with two critical points both of index 1, so H1(X, X−T ) is of rank 2, and the
other relative homology groups vanish. (Without using Morse theory, we would observe that
H0(X, X−T ) = 0 since any zero-cycle is a sum of points, which can be deformed into X−T .
And H2(X, X−T ) = 0 since X has non-compact ends even after collapsing X−T to a point.)
For a generic perfect Morse function h, Morse theory also gives a recipe for constructing
a relative one-cycle Jσ attached to each critical point, and representing an element of the
appropriate relative homology group. Moreover, these cycles generate the relative homology
with integer coefficients.
In general, on any manifold X with real coordinates u
i
, pick a Riemannian metric gij
and consider the downward flow or gradient flow equations
du
i
dt
= −g
ij ∂h
∂uj
. (3.8)
These are called downward flow equations, because except for a trivial solution that sits at
a critical point for all t, h is always strictly decreasing along a flow:
dh
dt
=
X
i
∂h
∂ui
du
i
dt
= −
X
i

∂h
∂ui
2
. (3.9)
An important property of the flow equation is that if u
i
(t) equals a critical point at some
t, then the flow equation implies that u
i
(t) is constant for all t. So a nonconstant flow can
only reach a critical point at t = ±∞.
Let p be a nondegenerate critical point of h, and consider the downward flow equations
on the half-line (−∞, 0] with the boundary condition that u
i
(t) approaches p for t → −∞.
If p has index k, the moduli space Jp of such solutions is a k-dimensional manifold, since
there are k independent directions of downward flow from the critical point p. We think
7This condition ensures that in computing the homology of X, there are no cancellations between critical
points of adjacent index.
26

of Jp as a submanifold of X, by mapping a downward flow line u
i
(t) to the corresponding
point u
i
(0) ∈ X. (This gives an embedding of Jp in X since, as the downward flow equation
is first order in time, a flow is uniquely determined by its value at t = 0.) An equivalent
definition of Jp is that it is the submanifold of X consisting of points that can be reached
at any t by a flow that starts at p at t = −∞. Given a flow line u
i
(t) that reaches a point
x ∈ X at t = t
∗
, the flow line u
i
(t − t
∗
) arrives at x at t = 0. A flow line defined on the full
line (−∞, ∞) will be called a complete flow line.
Once we pick an orientation of Jp, Jp will define a cycle8in the relative homology
H1(X, X−T ) if it is closed, meaning that any sequence of points in Jp has a subsequence that
either converges or tends to h = −∞. This fails precisely if there is a complete flow line l
that starts at p at t = −∞ and ends at another critical point q at t = +∞. In that case,
Jp is not closed, since l is contained in Jp, but a sequence of points in l can converge to q,
which is not contained in Jp.
We will determine shortly a necessary condition for a flow line to connect two distinct
critical points p and q. When this condition is not satisfied, Jp defines an element of the
relative homology Hk(X, X−T ). Jp is known as a Lefschetz thimble.
In our problem, the Morse function is the real part of a holomorphic function I. In such
a case, if we pick a Kahler metric ds
2 = |dx|2
, the flow equation can be written
dx
dt
= −
∂I
∂x
,
dx
dt
= −
∂I
∂x . (3.10)
Using the chain rule and (3.10), we find
d Im I
dt
=
1
2i
d(I − I)
dt
=
1
2i

∂I
∂x
dx
dt
−
∂I
∂x
dx
dt

= 0. (3.11)
So Im I is conserved along a flow.
A more conceptual explanation of the existence of this conserved quantity is as follows.
Associated to the Kahler metric |dx|
2
is the Kahler form ω = −idx ∧ dx. Viewing ω as a
symplectic form on the x-plane, the gradient flow with respect to the Morse function Re I
is the same as the Hamiltonian flow with Hamiltonian Im I. Naturally, Im I is conserved in
this flow.
From (3.6), we see that in the Airy case, the values of Im I at the critical points are
Im I± = ∓(2/3)Re λ. These are equal if and only if λ is purely imaginary. Hence a flow
8Our definition of Jp is slightly different from the definition usually used in Morse theory on a compact
manifold M. In such a case, unless p is a local minimum of h, there are always complete flow lines starting at
p and ending at some “lower” critical point, and one takes the closure of Jp to define a Morse theory cycle.
In the situation we consider, as is explained shortly, there generically are no complete flow lines between
critical points, and it is most convenient to define Jp as we have done.
27

(a) (c)
pσ
pτ
(b)
pσ
pτ
pσ
pτ
Figure 2: This figure illustrates the behavior of flow lines when one crosses a Stokes ray. Sketched
are the downward flows from two critical points pσ and pτ . The lines are sketched as flowing
downward, in the direction of smaller h (though it is not literally true that h corresponds to the
height in the figure, as this function has no critical points). The behavior at a Stokes ray is depicted
in (b); there is a downward flow from pσ to pτ . The flows “before” and “after” crossing the Stokes
ray are depicted in (a) and (c). The downward flowing cycle Jτ from the lower critical point is
unaffected by the Stokes ray. As for the cycle Jσ defined by flow from the upper critical point, it
is ill-defined in (b) and jumps by Jσ → Jσ + Jτ between (a) and (c).
can connect the two critical points at x = ±1 only if λ is imaginary. Conversely, if λ is
imaginary, there is indeed a flow that connects the two critical points (the flow line is simply
the part of the real axis with −1 < x < 1). Since we always assume that λ 6= 0, the locus
of imaginary λ is not connected but consists of two open rays, differing by the sign of Im λ.
We refer to these as Stokes rays.
3.1.2 Crossing A Stokes Ray
Away from the Stokes rays, a downward flow that starts at one critical point cannot end at
the other; instead it always flows to h = −∞. So away from the Stokes rays, the downward
flow procedure attaches to each critical point p+ or p− a relative homology one-cycle J±.
Let us see what happens to the Lefschetz thimbles J± in crossing a Stokes ray.
From (3.6), I+ and I− are always unequal (since we always assume that λ 6= 0). On a
Stokes ray Im I+ = Im I−, so necessarily Re I+ 6= Re I−, that is h+ 6= h−. In fact, h+ > h− if
Im λ > 0, and otherwise h− > h+. As we approach a Stokes ray, let us write q and q
′
for the
critical points with the larger and smaller values of h, and J and J
′
for the corresponding
one-cycles. Even when we reach and cross the Stokes ray, nothing happens to J
′
, because
downward trajectories that start at q
′
can only flow to h = −∞. But a trajectory that starts
at q may flow down to q
′
. (As we noted above, in the case of the Airy function, there is such
28

a trajectory, namely the segment of the real axis connecting q and q
′
.) When there is such a
flow line, the definition of the cycle J attached to q fails. Since J is potentially ill-defined
when λ is on a Stokes ray, it might jump in crossing a Stokes ray, and that is actually what
happens. How this happens is sketched in Fig. 2. The jump is J → J ± J ′, where the sign
depends on the orientations of the two cycles and the direction in which λ crosses the Stokes
ray. The change in the pair J , J
′
can thus be written

J
J
′

→

1 ±1
0 1  JJ
′

. (3.12)
In section 3.1.4, we explain in another way why only J and not J
′
changes in crossing the
Stokes ray.
Let us compute the monodromy of the cycles J+ and J− around λ = ∞ (or 0). In
crossing the Stokes ray with Im λ > 0, the monodromy is strictly upper triangular:
U+ =

1 1
0 1
. (3.13)
On the Stokes ray with Im λ < 0, the monodromy is strictly lower triangular:
U− =

1 0
−1 1
. (3.14)
(If the cycles J± are oriented so that the upper right matrix element in (3.13) is +1, then
the lower left matrix element in (3.14) is −1.) The monodromy around λ = ∞ is not simply
the product U−U+, as there is also a minus sign involving the orientation of the cycles J±.
Indeed, the function I can be approximated near x = ±1 by ∓2iλ/3 + iλ(x ∓ 1)2, and an
approximation to the downward flowing cycles J± is given by x = ±1+t(−iλ)
−1/2
, with real
t. To orient the cycles, we need to pick a sign of (−iλ)
−1/2
, and under monodromy around
λ = ∞, this sign is reversed. So the monodromy of the pair 
J+
J−

around λ = ∞ is
M = −U−U+ =

−1 −1
1 0 
. (3.15)
In particular, the monodromy obeys M3 = 1. The fact that the monodromy is of order
3 is clear without Morse theory: under monodromy around λ = ∞, the three good regions
in Fig. 1 undergo a cyclic permutation of order 3. What we have gained from Morse theory
is a powerful framework for generalizations.
In this analysis, the dependence of the orientation of the J± on a sign of √
−iλ is inelegant,
and the resulting jumping in the sign of the nσ is unthematic. This can be avoided by
multiplying the original definition of the Airy integral by √
−iλ. The product of this function
times the orientation of J± has no jumping in sign. With this factor included, the jumping
of nσ occurs only in crossing Stokes lines, and M has the opposite sign to what is given in
(3.15) and obeys M3 = −1.
29

3.1.3 Asymptotic Behavior Of Integrals Over Lefschetz Thimbles
The cycles J± are defined in such a way that, for any λ, the integrals
Z±,λ =
Z
J±
dx exp(I) (3.16)
always converge. Indeed, we have arranged so that Re I → −∞ at infinity along J±.
Not only are the integrals Z±,λ always convergent, but it is straightforward to determine
their asymptotic behavior as λ → ∞ in a fixed direction in the complex plane. The maximum
of h = Re I on the cycle J± is precisely at the critical point x = ±1. Moreover, the phase
Im I is stationary at x = ±1, since those are critical points of I (and in fact the phase Im I
is entirely constant along the cycles J±). So the asymptotic behavior of Z±,λ is dominated
by a contribution from the critical point, giving
Z±,λ ∼ exp(I±)(−iλ)
−1/2X∞
t=0
btλ
−t
, (3.17)
where I± = ∓2iλ/3 and the coefficients btin the asymptotic series can be computed by
expanding around the critical point. If we include a factor of (−iλ)
1/2
in the definition of the
Airy integral, as suggested at the end of section 3.1.1, the factor of (−iλ)
−1/2
, which comes
from a Gaussian integral, would be canceled.
3.1.4 Sum Of Asymptotic Series
An integral ZC,λ over a general cycle C = n+J+ + n−J− can be expressed asymptotically as
a sum of two asymptotic expansions:
ZC,λ ∼ n+ exp(I+)(−iλ)
−1/2X∞
t=0
btλ
−t + n− exp(I−)(−iλ)−1/2X∞
t=0
ctλ
−t
. (3.18)
However, generically one of these series suffices, since in a generic direction in the complex
λ plane, h+ and h− are unequal and one of the two series is exponentially larger than the
other. If h+ = h− (which happens for real λ), the two series compete and must both be
included, and if λ varies so that h+ − h− changes sign, the two series exchange dominance.
On a Stokes ray, h+ and h− are definitely unequal, so one series in (3.18) is exponentially
larger than the other. Consider for definiteness a Stokes ray with h+ > h−. The integral in
(3.18) must vary holomorphically with λ, so the coefficient n+ of the dominant exponential
series must be continuous. But, since the two series are only asymptotic series that leave
30

exponentially small corrections undetermined, the expansion (3.18) in a region with h+ > h−
is not powerful enough to ensure that n− is continuous.
Let us compare this expectation to (3.12), which in the present notation says that the
jumping of J+ and J− is

J+
J−

→

1 ±1
0 1  J+J−

. (3.19)
In order for n+J+ + n−J− to be continuous, the n± transform by

n+ n−

→

n+ n−


1 ∓1
0 1 
. (3.20)
In particular, as expected, n+ is constant and only n− jumps.
An equivalent way to say some of the same things is to observe that since the integral
over J− is exponentially smaller than that over J+, J− cannot jump by a multiple of J+ in
crossing the Stokes ray, but J+ can jump by a multiple of J−.
3.1.5 Expressing The Real Cycle In Terms Of Lefschetz Thimbles
The function Zλ whose analytic continuation we actually want to understand is defined for
real λ by integration over the real cycle CR. So to use the above results, we have to express
CR as a linear combination of the J±. The coefficients will be integers, since the J± are a
basis of the relative homology with integer coefficients. For the Airy integral, we can find
the right coefficients by inspection, but we want to describe a more general method.
On a compact Riemann surface X, given a basis J± of H1(X), to express another class
C ∈ H1(X) in the form C = n+J+ + n−J−, we would find the coefficients n+ and n− via
intersection pairings. In the present case, we cannot do precisely this, because there is no
intersection pairing on the relative homology H1(X, X−T ). (The intersection of two onecycles on the two-manifold X should be a zero-cycle or sum of points; but a point vanishes
in the relative homology H0(X, X−T ), since it can be deformed into X−T .)
There is a good substitute, however. Indeed, Morse theory tells us what are the duals
of the downward flowing cycles from the critical points: they are the upward flowing cycles.
The upward flowing cycle attached to a critical point p is defined by reversing the sign in
the flow equation (3.8). That is, one considers solutions of the upward flowing equation
du
i
dt
= +g
ij ∂h
∂uj
(3.21)
on the half-line (−∞, 0], again requiring that u
i
(t) approaches p for t → −∞. The space of
possible values of u
i
(t) at t = 0 now defines the upward flowing cycle Kp attached to p. It is
31

an n − k-dimensional cycle if p has index k (so that the Morse function −h has index n − k
at p).
The upward flowing cycles take values in a different relative homology. For a real number
T, define XT as the part of the complex x-plane with h ≥ T. The upward flowing cycle
from a critical point p of the type we are considering has its infinite ends contained in XT
for large positive T (as long as we keep away from Stokes rays). So it defines an element of
the relative homology Hk(X, XT).
For r and s of complementary dimensions, there is a natural intersection pairing between
Hr(X, X−T ) and Hs(X, XT). This pairing is easily evaluated for the case of interest to us
– a perfect Morse function with no flows between distinct critical points. The absence of
such flows means that if pσ and pτ are distinct critical points, the corresponding cycles Jσ
and Kτ do not intersect – such an intersection would be a downward flow from pσ to pτ . On
the other hand, for any one critical point pσ, the downward cycle Jσ and the upward cycle
Kσ have precisely one point of intersection – the trivial constant flow, starting and ending
at pσ. With suitable relative orientations of downwards and upward cycles, the trivial flow
contributes +1 to the diagonal intersection pairing hJσ, Kσi. So the intersection pairings are
hJσ, Kτ i = δστ . (3.22)
Given any element C of the downward flowing relative homology, we now can give a
formula to determine the coefficients in the expansion C =
P
σ
nσ Jσ. By intersecting with
Kτ , we find simply
nτ = hC, Kτ i (3.23)
for all τ .
3.1.6 The Asymptotic Behavior Of The Airy Function
We will now give some examples of this procedure. Return to the original Airy function
Zλ =
Z
CR
dx exp iλ(x
3
/3 − x)

(3.24)
with CR being the real axis. The critical points p± at x = ±1 both lie on CR. A nontrivial
upward flow starting at a critical point will end at a point with a strictly positive value of
h = Re I; such a point will not lie on CR, since h vanishes identically on CR. Hence the
intersection of CR with either upward flowing cycle K± consists precisely of the critical point
p±. Modulo a judicious choice of orientations, this tells us the coefficients when we express
the real cycle CR in terms of Lefschetz thimbles associated to critical points:
CR = J+ + J−. (3.25)
32

This formula expresses the integration cycle in terms of Lefschetz thimbles when λ is
real. But when λ is not real, we must integrate over a more general cycle C. As λ varies in
the complex plane, we vary the cycle C smoothly so that it always connects one good region
at infinity to another. On the other hand, the cycles J+ and J− have jumps described in
eqns. (3.13), (3.14) and a jump in sign involving the orientations. Allowing for these jumps,
we get, after analytic continuation from real λ to a wedge-shaped region of the complex λ
plane that does not contain Stokes rays, a formula
C = n+J+ + n−J−. (3.26)
(Instead of keeping track of Stokes rays and orientations, one can in this particular problem
let C evolve continuously so that the Airy integral remains convergent, and then directly use
(3.23) to determine the coefficients in any wedge-shaped region.) Hence in each wedge-shaped
region, the Airy integral can be expressed as
Zλ = n+Z+,λ + n−Z−,λ. (3.27)
Together with (3.17), this determines the asymptotic behavior of Zλ in each wedge-shaped
region. In particular, Zλ grows exponentially at infinity if and only if the expansion (3.26)
has a nonzero coefficient for a critical point at which h > 0.
Let us consider a special case in which there is not exponential growth at infinity. This
is the Airy function with a reversed sign for the linear term in the exponent,
Zeλ =
Z
CR
dx exp iλ(x
3
/3 + x)

, (3.28)
with λ real and with CR again equal to the real axis. This integral is actually a special case of
what one gets by analytic continuation of the original Airy integral, since9(3.24) is mapped
to (3.28) by λ → iλ, x → ix. However, we will simply treat this slightly modified example
directly according to the general recipe.
The critical points are now located at x = ±i. We denote these points as pe±. The value
of Ie = iλ(x
3/3 + x) at pe± is now ∓2λ/3, so for either sign of λ, the function eh = Re Ie is
positive at one critical point and negative at the other critical point. An upward flow from
a critical point with eh > 0 will never meet the real axis CR, since eh = 0 on CR. However,
from the critical point with eh < 0, there is an upward flow to the real axis.10 Write q
+ and
9To be more exact, to map the original Airy function to (3.28) by analytic continuation, one must increase
the argument of λ by 2π(n + 1/4), where the integer n is chosen so that the real cycle of the original Airy
function maps back to the real cycle in (3.28).
10 For example, if λ is real, the part of the imaginary axis between x = i and x = −i is a flow line that
intersects the real axis. In one direction or the other, this is an upward flow from the critical point with
negative eh. If we give λ a small imaginary part to get away from the Stokes ray, the upward flow from
that same critical point still intersects the real axis (it then continues to eh = +∞ rather than to the second
critical point).
33

q
− for the critical points at which eh is positive or negative, and Je± for the corresponding
Lefschetz thimbles. Then the expression for CR in terms of Lefschetz thimbles is simply
CR = Je−. (3.29)
The asymptotic behavior of Zeλ for large real λ is hence
Zeλ ∼
exp Ie(q
−)

λ
1/2
X∞
t=0
atλ
−t
. (3.30)
In particular, Zeλ vanishes exponentially for large real λ, reflecting the fact that there are no
critical points on the real x-axis.
Actually, in this example, the Stokes rays are the positive and negative real λ axis. For
real λ, there is a flow line between the two critical points, as noted in footnote 10. Hence
the cycles Je± jump in crossing the real λ axis. However, the jumping only affects the cycle
Je+ attached to the critical point with eh > 0. This cycle changes by Je+ → Je+ ± Je−. The
cycle Je− is unchanged in crossing the Stokes ray, and hence there is no problem with the
formula (3.29).
