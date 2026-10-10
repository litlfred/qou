---
doc_id: arxiv-1001.2933v4
doc_title: "Analytic Continuation Of Chern-Simons Theory"
section_id: sec-006-2-5-analytic-continuation-for-compact-gauge
section_title: "Analytic Continuation For Compact Gauge Groups"
section_number: "2.5"
pages: 12-17
source_pdf: 1001.2933v4.pdf.txt
source_sha256: b02636c86d593c02
toc_source: inferred
doc_brief: "Analytic Continuation Of Chern-Simons Theory — The title of this article refers to analytic continuation of three-dimensional ChernSimons gauge theory away from integer values of the usual coupling"
---
2.5 Analytic Continuation For Compact Gauge Groups
Now we will discuss the analytic continuation of Chern-Simons theory with a compact gauge
group. We consider it first in a naive way and then in relation to the theory with a complex
gauge group.
12

In Chern-Simons gauge theory on a three-manifold M with a compact gauge group H,
the gauge field is a connection A on an H-bundle E → M. In terms of the Chern-Simons
function W(A), which we normalize as usual to be well-defined modulo 2πZ, the action is
I = kW, where k is taken to be an integer so that the integrand exp(iI) = exp(ikW) of
the path integral is well-defined. Then one defines the path integral as the integral over the
space4 U of connections mod gauge transformations:
ZH(k) = Z
U
DA exp(ikW(A)). (2.18)
In the presence of a knot K labeled by a representation R, one includes a holonomy factor
and considers the integral:
ZH(K; k) = Z
U
DA exp(ikW(A)) TrRP exp −
I
K
A

. (2.19)
As written, the integral does not make sense unless k is an integer. Indeed, as W(A)
is defined only modulo 2π, the expression exp(ikW(A)) makes sense as a function on U if
and only if k ∈ Z. Can we evade this limitation? A naive way to try to do so is to replace
U by its universal cover5 Ub. Ub is the quotient of the space of connections by the group of
topologically trivial gauge transformations. The expression exp(ikW(A)) is invariant under
such gauge transformations, so it makes sense as a function on Ub. However, its integral
vanishes for k 6∈ Z, since the integrand transforms with a non-trivial phase under the deck
transformations associated to the cover U → U b .
To cure this problem, we complexify the gauge field, replacing A by a complex-valued
connection A. A is now a connection on an HC-bundle EC → M. We replace U and
Ub by their complexifications UC and UbC, which respectively parametrize complex-valued
connections modulo complex-valued gauge transformations or modulo topologically trivial
complex-valued gauge transformations. Finally, in UbC, we pick an integration cycle C and
define the integral
ZH,C(k) = Z
C
DA exp(ikW(A)). (2.20)
4 A variant in which one takes U to be the quotient of the space of connections by the group of based gauge
transformations is also useful. (A based gauge transformation is one that equals 1 at a prescribed point; the
advantage of dividing only by this group is that it acts freely, so dividing by it produces no singularities.) In
this variant, one must divide the path integral by a constant factor, the volume of the residual group of gauge
transformations. Another important variant arises in working out the contribution to the path integral from
a given gauge orbit of flat connections on M; here one may take U to be a transversal to the given orbit
in the space of all connections on E. When we speak loosely of U as the space of connections mod gauge
transformations, we refer to any of these variants that may be most convenient in a given context.
5To be more precise, we can take Ub to be the smallest cover of U on which the Chern-Simons function
W(A) makes sense as a real-valued function. If H is connected and simply-connected, this is the same as
the universal cover.
13

(When a knot K is present, we denote the corresponding integral as ZH,C(K; k).) The
analytic continuation of the path integral measure DA on Ub is a holomorphic volume form
on UbC that we continue to denote simply as DA. In section 2.7.1, it will be expressed in
terms of the holomorphic volume form DA used in the complex path integral (2.13).
We will pick C so that the integral (2.20) converges even when k becomes a complex
number. It will be constructed from Lefschetz thimbles in the usual way,
C =
X
σ
nσJσ. (2.21)
Here the pσ correspond to flat connections Aσ with structure group HC, each with a chosen
lift to UbC. (The sum in (2.21) will generally be a finite sum, but see the end of section 5.2.4
for an exception.) The analytically continued path integral will therefore be
ZH(k) = X
σ
nσZH,σ(k) (2.22)
with
ZH,σ(k) = Z
Jσ
DA exp(ikW(A)). (2.23)
A finite sum (2.21) is not invariant under the deck transformations of the cover UbC → Ub,
so it is not possible to use those deck transformations to show that ZH,C(K, k) = 0 for k /∈ Z.
(Invariance under deck transformations would require including every lift of a given Aσ.)
As a cycle in the appropriate homology, C will be locally constant in k (Stokes jumping of
cycles Jσ is compensated by jumping of coefficients nσ), ensuring that ZH,C(K, k) will be
holomorphic in k.
2.5.1 Downward Flow Again
To get an analytic continuation of the original Chern-Simons integral (2.18), C should obey
one more condition: it should be chosen so that ZH,C(k) = ZH(k) for integer k.
In a finite dimensional problem of this type, a suitable C can be found as follows. (For a
prototype, see the review in section 3.5 of the analytic continuation of the Bessel function.)
First, lift the real cycle U ⊂ UC to a non-closed chain C0 ⊂ UbC as follows. Pick a real number
α and define a point in C0 to be a real connection A whose Chern-Simons function takes
values in the closed interval [α, α+2π]. (We are using the fact that on UbC, the Chern-Simons
function is an ordinary complex-valued function.) We have to use a closed interval here or C0
would not be closed. Though closed, C0 is not a cycle because it has a non-zero boundary ∂C0
14

– consisting of real connections with Chern-Simons function α or α + 2π. Of course, ∂C0 is a
union of two disjoint pieces, which we will loosely call components (we do not need to know
if they are connected), corresponding to those two values of the Chern-Simons function.
We want to complete C0 to a candidate integration cycle C ⊂ UbC. For this, we add to C0
an additional piece C1 defined as follows. We define C1 by downward Morse flow from the
boundary ∂C0, with respect to the usual Morse function h = Re (ikW(A)). Assume first
that downward flow from ∂C0 leads to no critical points. Then C1 is closed and, if we orient
correctly its two components, then C = C0 ∪ C1 has no boundary and is the integration cycle
we want. (In the prototype of fig. 7 in section 3.5, the two components of C1 correspond to
the two half-lines that start at w = 0 and w = 2πi.)
C1 fails to be closed only if a downward flow from ∂C0 approaches a critical point for
t → +∞. (This critical point is then in the closure of C1, but not in C1 itself.) This possibility
is severely limited because the downward flow equations have a conserved quantity, which
for Chern-Simons theory is Im (ikW(A)), while in addition, Re(ikW(A)) decreases along a
flow. So C1 may fail to be closed only if there is a critical point at which W(A) has positive
imaginary part and real part α or α + 2π. For a generic choice of α, there is no such critical
point and the above definition works and gives a suitable cycle C.
Now consider the integral
Z
C
DA exp(ikW(A)) = Z
C0
DA exp(ikW(A)) + Z
C1
DA exp(ikW(A)). (2.24)
Here C1 consists of two components (downward flow from real connections with W(A) equal
to α or α + 2π) that differ from each other by a deck transformation that shifts W(A) by
2π. For k ∈ Z, the integrand exp(ikW(A)) is invariant under this deck transformation,
but on the other hand, the two components of C1 are oppositely oriented (that is, the deck
transformation maps the orientation of one to minus the orientation of the other). So for
k ∈ Z, we have R
C1
DA exp(ikW(A)) = 0 and R
C DA exp(ikW(A)) = RC0
DA exp(ikW(A)).
But for k ∈ Z, the function exp(ikW(A)) is a pullback from the original space UC of complexvalued connections modulo gauge transformations, and the cycle C0 pushes down in UC to
the original real integration cycle U. In short, R
C DA exp(ikW(A)) is equivalent to the
original Chern-Simons path integral when k is an integer. We have accomplished our goal
of expressing the Chern-Simons path integral ZH(k) with a compact gauge group in a form
that makes sense when k is not an integer.
C is an unfamiliar sort of integration cycle for a path integral, but actually, it is straightforward in concept to use (2.16) to re-express C in terms of Lefschetz thimbles. We just
count the upward flows from a given critical point Aσ to C. If k is real, the flow equations
conserve Im (iW(A)), so, given the condition that we have imposed on α, nσ is nonzero only
for critical points for which Im (iW(A)) takes values in the open interval (α, α + 2π).
15

2.5.2 Indeterminacy of C
The only problem with the analytic continuation that we have obtained for the Chern-Simons
path integral is that it is not unique.
The choice of C and therefore the analytic continuation of the Chern-Simons path integral
ZH(k) will in general jump in crossing the exceptional values of α at which C1 fails to be
closed. This is related to a very basic fact. The contribution of any given critical point pσ
to the path integral can be multiplied by exp(2πimk), for any integer m, without changing
its value for k ∈ Z. This multiplicative factor has a simple interpretation: it results from
shifting the Chern-Simons invariant of the flat connection Aσ by 2πm. So, without more
input, we cannot expect analytic continuation in k to be unique.
In a situation (such as that of section 5) in which the Chern-Simons path integral depends
on another parameter γ in addition to k, it may not be possible to make our almost canonical
choice of C uniformly in γ. The reason is that it may not be possible to choose α so that
it varies continuously with γ and never coincides with the value of Im (iW(A)) for any flat
connection A. If we choose C as above for some range of γ, then upon varying γ and letting
C evolve continuously, we will arrive at a more general C and hence a more general form of
the analytic continuation.
A rather general C would entail multiplying the contribution to the path integral from
each representation of the fundamental group by a finite sum
X
m∈Z
am exp(2πimk), (2.25)
where the integers am are almost all zero and P
m am = 1. In general, the am may be
different for different representations of the fundamental group. A function such as this will
naturally arise in an example in section 5.2.3.
2.5.3 Knots
There is an important case in which there is a completely natural choice of the analytic continuation. This is the case or knots or links in S
3
. As is known from any of their standard
characterizations, the usual Wilson loop invariants for knots or links can be analytically
continued to a Laurent polynomial in q = exp(2πi/(k + h)) and with this analytic continuation, they have no essential singularity at k = ∞. Since the function exp(2πik) does
have an essential singularity at k = ∞, the cycle C used in analytically continuing the knot
invariants is unique if one wants the analytically continued function to be free of an essential
singularity at infinity.
16

Perhaps we should spell out a detail concerning the last paragraph. The Jones polynomial
and its generalizations are usually normalized to equal 1 for the unknot. From the point of
view of quantum field theory, this definition amounts to defining the Jones polynomial of a
given knot K by analytic continuation of a ratio ZH(K; k)/ZH(K0; k), where ZH(K; k) was
defined in (2.19) and K0 is the unknot. The ratio is certainly 1 if K = K0. It is such ratios
that analytically continue to Laurent polynomials in q. The numerator and denominator,
when taken separately, have an analytic continuations in k with no essential singularity at
k = ∞, but they are not Laurent polynomials in q. For example, for H = SU(2), the
denominator is ZH(K0; k) = p
2/(k + 2) sin(π/(k + 2)), which is not a Laurent polynomial
in q, but has no essential singularity at k = ∞. The theory developed in the present paper
applies more naturally to a path integral than to a ratio of path integrals, and therefore we
will simply study the functions ZH(K; k) rather than ratios of such functions.
