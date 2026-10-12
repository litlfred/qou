---
doc_id: arxiv-1001.2933v4
doc_title: "Analytic Continuation Of Chern-Simons Theory"
section_id: sec-014-3-5-analytic-continuation-in-k-a-prototype
section_title: "Analytic Continuation In k: A Prototype"
section_number: "3.5"
pages: 55-62
source_pdf: 1001.2933v4.pdf.txt
source_sha256: b02636c86d593c02
toc_source: inferred
doc_brief: "Analytic Continuation Of Chern-Simons Theory — The title of this article refers to analytic continuation of three-dimensional ChernSimons gauge theory away from integer values of the usual coupling"
---
3.5 Analytic Continuation In k: A Prototype
We have discussed at great length the analytic continuation of the integral of an exponential
exp(iλf) from real to complex values of λ. For a more precise analog of Chern-Simons theory,
we should consider analytic continuation of an integer parameter (such as the Chern-Simons
level k) to complex values.
For an example, we consider the integral representation of the Bessel function:
I(κ, λ) = 1
2πi I
dz
z
z
κ
exp(λ(z − z
−1
)), (3.66)
with an integer κ that in our analysis of section 5 will correspond roughly13 to the ChernSimons level k.
We take the integration cycle to be the circle |z| = 1. Alternatively, we can write
I(κ, λ) = 1
2πi I
dz
z
exp(I), (3.67)
with
I = λ(z − z
−1
) + κ ln z. (3.68)
For real λ and integral κ, this integral is an oscillatory integral of the general type that
we have been considering, except that the integration cycle is compact, so that analytic
continuation in λ poses no problem. However, we would like to analytically continue the
integral to complex values of κ. This is a rough analog of analytically continuing ChernSimons gauge theory with respect to the level k.
13In that analysis, λ corresponds roughly to the index n of the colored Jones polynomial Jn(q), so the
analogy would be closer if also λ were constrained to be an integer.
55

0
Im w
C Re w
2πi
Figure 7: The contour C in the complex t-plane that is used in analytic continuation of the Bessel
function.
Let us recall the steps that were described somewhat abstractly in section 2.5.1. The
holomorphic form that we are trying to integrate is naturally defined in the punctured zplane, with the point z = 0 omitted. To analytically continue in κ, we want to lift the
integral from the punctured z-plane to its universal cover, which is the complex w-plane
where z = e
w. The integration cycle |z| = 1 can be lifted to the line segment in the w-plane
from αi to (2π + α)i, for an arbitrary α. Picking α = 0, the integral becomes
I(κ, λ) = 1
2πi Z 2πi
0
dw exp(2λ sinhw + κw). (3.69)
The integration is now over an open contour whose ends are the two points w = 0 and
w = 2πi. If we stop here, Bessel’s equation (whose proof requires integration by parts), will
fail when κ /∈ Z. An analogous procedure in quantum field theory would lead to a failure of
the Ward identities. Instead, following a classical procedure, and assuming that Re λ > 0,
we add to the contour two more half lines given (fig.7) by the negative real axis and its
translate by 2πi, suitably oriented to give a closed although noncompact integration contour
C, which represents a cycle in the appropriate relative homology. The integral over this cycle
I(κ, λ) = 1
2πi Z
C
dw exp(2λ sinhw + κw) (3.70)
converges (if Re λ > 0), and in this integral, κ can now be treated as a complex variable.
This gives an analytic continuation of the Bessel function to complex values of κ, since if κ
is an integer, the two half lines that have been added to the integration contour cancel each
other and the extended integral reduces to the original one. To analytically continue beyond
the region Re λ > 0, one must shift C vertically in the w-plane as the argument of λ varies.
But we will mainly study the dependence on κ with Re λ > 0.
56

If λ and κ are real and obey suitable inequalities (λ and 2λ + κ should be positive), the
two half-lines that we added to complete the integration contour are precisely as described
in section 2.5.1: they are the downward flow lines from the endpoints w = 0 and w = 2πi of
the naive integration contour in the complex w plane. If we vary λ and κ slightly, the flow
lines move but without changing the relative homology class of the integration cycle C.
We have described a simple procedure for analytic continuation away from integer values
of κ, but there is no avoiding a basic fact discussed in section 2.5.2: analytic continuation
away from integer values is not unique. For an illustrative special case of this, note that we
could have begun by lifting the circle |z| = 1 to a line segment in the w-plane connecting
the points w = ±πi. This would be analogous to a different choice of α in section 2.5.1.
Provided λ and κ are real and obey suitable inequalities (λ and 2λ + κ should be negative),
the downward flow lines from w = ±i are again half-lines parallel to the real axis, but
they extend in the opposite direction to Rew >> 0. The two analytic continuations are
qualitatively different. The original Bessel integral (3.66) obeys I(−κ, λ) = (−1)κI(κ, λ), as
follows from the change of variables z ↔ −1/z. This symmetry is broken by the choice of
whether to extend the contour to Rew << 0, as in fig. 7, or to Rew >> 0. With either
choice, it turns out that when κ is not an integer, the large κ behavior depends very much
on the sign of Re κ.
In the rest of our analysis, we will stick with the analytic continuation corresponding to
the contour C of fig. 7. We want to study the behavior of the integral (3.70) as κ and λ
become large with a fixed value of ρ = κ/2λ. First we will learn what we can by inspection,
taking κ real and λ positive, and then we will reconsider the matter using Morse theory.
The critical point equation is z
2 + 2ρz + 1 = 0 or coshw + ρ = 0 and the critical points
are at
z = −ρ ± i
p
1 − ρ
2
. (3.71)
or
w = ±arccosh(−ρ) + 2πin = ln(−ρ ±
p
ρ
2 − 1) + 2πin, n ∈ Z. (3.72)
First let us suppose that κ is an integer, so that Iκ,λ can be defined by the original
integral on the contour |z| = 1, and we can use (3.71) to identify the critical points. If
|ρ| ≤ 1, the critical points are at |z| = 1, on the integration contour. They make oscillatory
contributions to the integral, and this gives the behavior of the integral for large κ and fixed
ρ in this region.
Now, still with integer κ, suppose that |ρ| > 1. The critical points move off the integration
contour |z| = 1, and the integral therefore vanishes exponentially.
Next, suppose that κ is not an integer. We must consider the effects of the two halflines that have been added to the integration contour. If |ρ| ≤ 1, the addition of these
57

half-lines does not lead to a qualitative change; the integral is still dominated by oscillatory
contributions from critical points at |z| = 1. We must be more careful if |ρ| > 1, and
the two cases ρ > 1 and ρ < −1 turn out to be completely different.14 If ρ > 1, there
is no critical point on the integration contour and I(κ, λ) vanishes exponentially whether
κ is an integer or not. (The most precise analysis is by a saddle point analysis that we
describe shortly.) For ρ < −1 (which means negative κ, since we have taken λ > 0), the
behavior is more delicate. There are two critical points on our chosen integration cycle
C, namely at w = ln(−ρ −
p
ρ
2 − 1) and w = ln(−ρ −
p
ρ
2 − 1) + 2πi. The two critical
points have the same positive value of h = Re I, and they both make contributions that are
exponentially large for κ → −∞. (Indeed, h ∼ −κf(ρ) for −κ large, where the function
f(ρ) = (ρ
2 − 1)1/2
/ρ + ln(−ρ + (ρ
2 − 1)1/2
) is positive for ρ < −1.) On the other hand, Im I
vanishes for one critical point and is κ Im w = 2πκ at the other. Allowing for the opposite
orientations of the two half-lines that are part of the contour C, the two real critical points
contribute
exp(−κf(ρ)) (1 − exp(2πiκ)) (3.73)
times the usual sort of asymptotic series. For integer κ, these contributions cancel, but for
generic κ << 0, their sum grows exponentially with |κ|.
3.5.1 Description By Lefschetz Thimbles
Finally, we will seek a more precise description by expressing the cycle C as a sum of Lefschetz thimbles Jσ associated to critical points pσ. Let us formulate the most parsimonious
hypothesis that is consistent with the observations above:
(1) For ρ > 1, it is reasonable to guess that C is equivalent to the Lefschetz thimble
associated to the critical point at w = ln(−ρ +
p
ρ
2 − 1) (w has negative real part and we
pick the branch of the logarithm such that Im w = π). This is the unique critical point
enclosed by C if ρ > 1, and as h is negative at this critical point, the associated Lefschetz
thimble makes an exponentially small contribution to the integral, as expected.
(2) For 1 > ρ > −1, the two critical points at |z| = 1 must certainly be included. There
is no obvious need for more.
(3) For ρ < −1, the situation is more tricky. The two real critical points that account
for the exponentially growing asymptotics in (3.73) must certainly contribute when C is
expressed in terms of Lefschetz thimbles. But as they cancel when κ is an integer, while
I(κ, λ) is not zero in that case, the expression for C in terms of Lefschetz thimbles must
14This difference results entirely from the choice of how to analytically continue the function I(κ, λ) to
nonintegral values of κ, since for κ ∈ Z, the Bessel function has a symmetry I(−κ, λ) = (−1)κI(κ, λ), as
already noted.
58

receive a contribution from at least one more critical point. This critical point must have
h < 0, since I(κ, λ) is exponentially small for integer κ and ρ < −1.
In summary, in regions (1), (2), or (3), C must be a sum of at least 1, 2, or 3 critical
point contours, respectively. This most parsimonious interpretation is actually correct, as
one can see from fig.8, where the relevant Lefschetz thimbles are sketched.
3.5.2 Singularities At ρ = ±1
The most interesting values of ρ are at ρ = ±1, where critical points meet. Let us first
examine the behavior at these points on the z-plane, and then on the w-plane. The analysis
on the z-plane is simpler, but it only tells us what happens when κ is an integer. To analyze
the behavior for non-integral κ, we need to work on the w-plane.
There are precisely two critical points on the z-plane, located at z = −ρ ± i
p
1 − ρ
2
.
Precisely for ρ = ±1, the two critical points meet. This is reminiscent of the most basic
example of critical behavior, the cubic polynomial f(x) = x
3/3 − ǫx related to the Airy
function, whose two critical points meet at ǫ = 0. The critical points of f are real for ǫ > 0
and form a complex conjugate pair for ǫ < 0. The consequences of the singularity at ǫ = 0
were explored in section 3.4.1.
Our problem on the z-plane is exactly analogous. We endow the punctured z-plane with
the antiholomorphic involution z → 1/z, so that the real points (the fixed points of the
involution) are the circle |z| = 1. The two critical points at z = −ρ±i
p
1 − ρ
2 are real for ρ
real and |ρ| < 1 but form a complex conjugate pair for ρ real and |ρ| > 1. The singularities
at ρ = ±1 are just analogous to the Airy function singularity at ǫ = 0.
As long as κ is an integer and we work on the z-plane, the behavior of the Bessel integral
that we found in section 3.5.1 precisely mirrors the behavior of the Airy integral
I(ǫ) = Z ∞
−∞
dx exp i(x
3
/3 − ǫx)

. (3.74)
Region (2) of the Bessel integral corresponds to the case ǫ > 0 for the Airy integral: the
integration cycle is equivalent to the sum of two Lefschetz thimbles associated to two real
critical points. Regions (1) and (3) of the Bessel integral correspond to the case ǫ < 0 for
the Airy integral: the integral is equivalent to an integral over a single Lefschetz thimble
that makes an exponentially small contribution. In section 3.5.1, we found that three critical
points are needed in region (3) to describe the integral on the w-plane, but two of them (the
ones that make exponentially growing contributions) cancel upon projection to the z-plane.
The analysis on the w-plane is more complicated because each critical point on the z59

0
c)
2πi
I
II
III
2πi
b)
0
2πi
a)
0
Figure 8: Qualitative behavior of Lefschetz thimbles in analytic continuation of the Bessel function,
for (a) ρ > 1 , (b) 1 > ρ > −1, and (c) −1 > ρ. In each case, the critical points are marked by black
dots. In (a), the integration cycle of fig. 7 is equivalent to a single Lefschetz thimble associated
to a complex critical point that makes an exponentially decaying contribution to the integral. In
(b), it is equivalent to the sum of two Lefschetz thimbles that make oscillatory contributions. And
in (c), it is equivalent to the sum of a Lefschetz thimble associated to a critical point (labeled as
I) that makes an exponentially decaying contribution and two critical points (labeled II and III)
whose contributions are exponentially growing, but cancel if κ is an integer. In (c), ρ has been
given a small imaginary part to avoid a Stokes line.
60

plane lifts to infinitely many critical points on the w-plane (differing by w → w + 2πin,
n ∈ Z). Nevertheless, it is very illuminating to repeat the analysis of the Bessel function
emphasizing its interpretation in terms of Airy function singularities:
(1′) We start for ρ > 1 with a single critical point at we− = ln −ρ +
p
ρ
2 − 1

, picking
the branch of the logarithm so that we− = πi at ρ = 1. (Choosing a different branch would
multiply the analytically continued Bessel integral by an integer power of exp(2πiκ).) The
name we− is motivated by the fact that in section 3.4.1, a complex critical point that makes
an exponentially small contribution to the Airy function for ǫ < 0 was called pe−. As in
section 3.4.1, we write Je− for the Lefschetz thimble corresponding to this critical point. For
ρ > 1, as we have learned in section 3.5.1, the integration cycle C that we have used to
analytically continue the Bessel function is equivalent to Je−.
(2′) The ρ > 1 critical point at we− = ln(−ρ +
p
ρ
2 − 1), when continued to ρ = 1, meets
two real critical points that for ρ < 1 are located at w± = ln(−ρ±i
p
1 − ρ
2
). Here branches
of the logarithm are chosen so that at ρ = 1, we have w+ = w− = we− = πi. As in the Airy
case, we denote as J+ and J− the Lefschetz thimbles that correspond to the real critical
points w±. We can use the Airy relation (3.58) to express the region (1) integration cycle Je−
in terms of Lefschetz thimbles J± appropriate to region (2). The relation is Je− = J+ + J−.
So the right integration cycle in region (2) is J+ + J−.
(3′) So far working on the w-plane instead of the z-plane has not given anything essentially
new. Now we study how the critical points w± evolve as we vary ρ from 1 to −1. We have
chosen branches of the logarithm so that w± = ln(−ρ ± i
p
1 − ρ
2
) are both equal to πi at
ρ = 1. However, when continued (along the real ρ axis) to ρ = −1, they are not equal.
Rather,
w+(ρ = −1) = 0, w−(ρ = −1) = 2πi. (3.75)
Hence, we cannot analyze what is happening at ρ = −1 in terms of a single Airy singularity. We must consider two different Airy singularities, located at w = 0 and at w = 2πi.
This will make the analysis a little longer, though the basic idea is just to use what we know
about the Airy integral.
Near w = 0, let us write J
′
± for the Lefschetz thimbles associated to real critical points at
ρ > −1, and Je′
± for the Lefschetz thimbles associated to complex critical points at ρ < −1.
We write J
′′
± and Je′′± for Lefschetz thimbles associated to the analogous real and complex
critical points near w = 2πi. (The reason for the notation J
′ and J′′ is to distinguish these
cycles from the ones we have already defined near ρ = 1.)
We have already found that for ρ just less than 1, the integration cycle is J+ + J−.
Continuing along the real axis to ρ just greater than −1 with the aid of eqn. (3.75), we
61

Figure 9: Qualitative behavior of the conserved quantity Im I/κ for critical points in the region
−1 ≤ ρ ≤ 1. ρ is plotted horizontally and Im I/κ vertically. A black dot represents a pair of real
critical points that become coincident at ρ = 1 or ρ = −1. At ρ = 1 (right), there are a pair of
real critical points for every value of Im I/κ of the form (2w + 1)π, w ∈ Z. Reducing ρ, Im I/κ
increases for one of these critical points and reduces for the other. At ρ = −1, the critical points
recombine in pairs, but now with Im I/κ of the form 2πw, w ∈ Z. In all cases, these critical points
are found by solving the equation cosh w = −ρ.
see that J+ + J− evolves to J
′
+ + J
′′
−. To continue past ρ = −1, we use the Airy relations
(3.57), which give J
′
+ = −Je′+ + Je′−, and J
′′
− = Je′′+. So J
′
+ + J
′′
− = −Je′+ + Je′′+ + Je′−, and this
is the integration cycle for ρ < −1. For integer κ, −Je′
+ and Je′′+ cancel and the integration
cycle is equivalent to Je′
−. For general κ, the contribution from −Je′+ + Je′′+ dominates and is
described qualitatively in eqn. (3.73).
With a view to our application in section 5.3, the key point to remember is that the two
real critical points on the z-plane, if lifted to the w-plane so that they coincide at ρ = 1, do
not coincide at ρ = −1. The flow of critical points is sketched in fig. 9.
