---
doc_id: arxiv-1001.2933v4
doc_title: "Analytic Continuation Of Chern-Simons Theory"
section_id: sec-011-3-2-generalization-to-dimension-n
section_title: "Generalization To Dimension n"
section_number: "3.2"
pages: 34-41
source_pdf: 1001.2933v4.pdf.txt
source_sha256: b02636c86d593c02
toc_source: inferred
doc_brief: "Analytic Continuation Of Chern-Simons Theory — The title of this article refers to analytic continuation of three-dimensional ChernSimons gauge theory away from integer values of the usual coupling"
---
3.2 Generalization To Dimension n
In our analysis of the Airy function, we introduced much more machinery than was really
needed. The advantage of having done so is that the generalization to an oscillatory integral
of higher dimension is now straightforward.
We consider a real-valued polynomial function f(x
1
, . . . , xn) of n real variables, and we
assume that f is sufficiently generic that (even after analytic continuation to complex values
of the x
i
) it has only finitely many critical points, which are all nondegenerate. We want to
study the analytic continuation of the oscillatory integral11
Qλ = (−iλ)
n/2
Z
CR
d
nx exp 
iλf(x
1
, . . . , xn)

. (3.31)
The integration is over the cycle CR defined by taking x
1
, . . . , xnto be real. We wish to
analytically continue the integral to (nonzero) complex λ, and to determine the asymptotic
behavior of the analytically continued integral. Depending on f, it may be difficult to see
how to vary the integration cycle C as λ is varied so that the integral remains convergent.
11Including the elementary prefactor (−iλ)n/2 avoids sign changes in the orientations of the Lefschetz
thimbles, as explained at the end of section 3.1.1. This lets us concentrate on the more interesting Stokes
phenomena.
34

So it is difficult in general to imitate the direct approach to the Airy function by rotating C
as λ varies. But the approach via Morse theory can be straightforwardly generalized.
As in the one-variable case, we regard the function I = iλf(x
1
, . . . , xn) as a function of
complex variables, and for fixed complex λ, we let Σ be the set of its critical points. If pσ,
σ ∈ Σ, is a critical point, we write Iσ for I(pσ). Now take h = Re I as a Morse function,
and write hσ for h(pσ). The critical points are all of the same index n, as explained in
section 3.1.1. So h is a perfect Morse function, and can be used to describe the appropriate
relative homology group in which the possible integration cycles take values. This group is
Hn(X, X−T ; Z), where X = C
n
, and X−T is defined by the condition h ≤ −T, for large T.
Introducing on C
n
the Kahler metric ds
2 =
P
i
|dx
i
|
2
, the downward flow equation (3.8)
can be written as in (3.10):
dx
i
dt
= −
∂I
∂x
i
. (3.32)
For generic λ, there are no flows between critical points. This follows from the fact that Im I
is conserved along a critical point, as shown in eqn. (3.11). (That computation generalizes
immediately to n dimensions, as long as the metric on X is hermitian. Just as in the onedimensional case, if X is Kahler, and we use the Kahler form of X as a symplectic form, then
the gradient flow with respect to the Morse function Re I is the same as the Hamiltonian
flow with Hamiltonian Im I; naturally, Im I is conserved in this flow.) If pσ and pτ are
critical points with distinct values of I, then for generic λ they have distinct values of Im I
and there is no flow between them. But if Iσ = Iτ , there is never a flow between pσ and
pτ , since h = Re I is always strictly decreasing along a non-trivial flow, as explained in eqn.
(3.9).
We define a Stokes ray to be a ray along which Im Iσ = Im Iτ for some σ, τ ∈ Σ. There
are only finitely many Stokes rays (we have assumed that Σ is a finite set, but even without
this assumption, for any polynomial f, Σ has only finitely many components, and I, which
is constant along each component, has only finitely many critical values).
Just as in the one-variable case, we attach to each critical point pσ a cycle Jσ, known as a
Lefschetz thimble, by taking the union of all downward flows that start at pσ, or equivalently
the values at t = 0 of downward flows u
i
(t) that start at pσ at t = −∞. As long as λ is not
on a Stokes ray, Jσ is closed and has its ends at h = −∞. Hence, Jσ defines an element of
the relative homology Hn(X, X−T ; Z). Moreover, according to Morse theory, the Jσ give a
basis of this relative homology.
In crossing a Stokes ray along which Im Iσ = Im Iτ , the cycles Jσ and Jτ may jump.
Such jumping involves nontrivial flows between pσ and pτ . A downward flow from pσ to
pτ is only possible if hσ > hτ . The general form of the jumping across a Stokes ray with
35

Im Iσ = Im Iτ , hσ > hτ is
Jσ → Jσ + mστJτ
Jτ → Jτ . (3.33)
Here mστ receives a contribution of ±1 from each downward flow line from pσ to pτ . (The
sign of the contribution is the sign of a certain determinant, described at the end of section
4.1.2.)
Whenever the Lefschetz thimble Jσ is defined, the integral
Qσ,λ = (−iλ)
n/2
Z
Jσ
d
nx exp(I) (3.34)
is always convergent. Moreover, the phase of the function exp(I) is constant along the
integration cycle, and its modulus has a unique maximum at the critical point pσ. Hence,
for large λ, this integral has an asymptotic expansion
Qσ,λ ∼ exp(Iσ)
X∞
t=0
atλ
−t
. (3.35)
To find the asymptotic behavior of the analytically continued integral, we will use the
expansion
C =
X
σ
nσJσ. (3.36)
For real λ, C is simply the original real integration cycle CR. Unlike the case of the Airy
function, we do not necessarily have a convenient way to directly determine the dependence
of C on λ. However, once the coefficients nσ are known for real λ, we can determine their
dependence on λ by using the “wall-crossing” formulas (3.33).
To determine the coefficients for real λ, we proceed as in the one-variable case. For each
critical point pσ, we define a cycle Kσ that consists of upward-going flow lines that start at
pσ. Away from Stokes rays, Kσ is an element of Hn(X, XT) for very large T, where XT ⊂ X
is defined by the condition h ≥ T. Just as for n = 1, the groups Hn(X, X−T ) and Hn(X, XT)
are naturally dual, and moreover the pairings of the Jσ and Kτ are
hJσ, Kτ i = δστ . (3.37)
As a result, the coefficients in (3.36) are
nσ = hC, Kσi. (3.38)
Thus, nσ can be computed by counting (with signs) upward flows from pσ to C.
36

Let us analyze this formula for real λ and the original integration cycle CR. We divide the
set Σ of critical points into three subsets: ΣR consists of critical points with all x
i
real, Σ−
consists of critical points with x
i not all real and h < 0, and Σ≥0 consists of critical points
with x
i not real and h ≥ 0. Note that h = 0 along CR, and in particular hσ = 0 for σ ∈ ΣR.
If σ ∈ ΣR, then the unique upward flow from pσ to CR is the trivial one, as h would increase
along a nonconstant flow. So in this case nσ = 1. If σ ∈ Σ≥0, there are no upward flow lines
from pσ to CR, as this would contradict the fact that h increases along such lines. Finally, if
σ ∈ Σ−, there may or may not be ascending flow lines from pσ to CR.
The general structure of the expression for CR, with real λ, is therefore
CR =
X
σ∈ΣR
Jσ +
X
σ∈Σ−
nσJσ, (3.39)
with unknown integer coefficients nσ. Correspondingly, for real λ, our original integral Qλ is
Qλ =
X
σ∈ΣR
Qσ,λ +
X
σ∈Σ−
nσQσ,λ. (3.40)
Since each term on the right hand side has the asymptotic expansion (3.35), this formula
makes manifest the behavior for large real λ. For complex λ, there is a similar formula, but
of course one must use the appropriate coefficients.
The significance of the formula (3.40) is as follows. In studying the function Qλ for
large real λ, the obvious critical points that one would expect to contribute are the ones
that lie on the real cycle CR. They indeed all contribute with a coefficient of 1, as one
would expect. Critical points in Σ≥0 would make contributions to the large λ behavior that
typically would grow exponentially and dominate the real critical points (if hσ > 0) and that
in the exceptional case hσ = 0 would compete for large real λ with the real critical points
(which also have h = 0). However, such critical points do not contribute to the integral.
Finally, there may be contributions from complex critical points with h strictly negative.
Their contributions are exponentially small for large real λ. But there is no easy recipe to
determine which such critical points do contribute exponentially small corrections to Qλ,
and with what weights. Rather, for σ ∈ Σ−, one simply has to determine the coefficient nσ
by counting (with signs) the upward flow lines from pσ to CR.
3.2.1 Essential Singularities
Now we wish to address the following question: Under what conditions does the analytically
continued integral Qλ have an essential singularity at λ = ∞?
There is one special case in which there is no such singularity. Suppose that, near infinity
in the complex λ plane, the critical points pσ for which the coefficients nσ are nonzero all
37

0
Re I
Iτ
Iσ
Figure 3: The complex I plane is sketched here with h = Re I running vertically. The exponents
Iτ and Iσ of two critical points pτ and pσ have arguments between π and 3π/2. If Arg Iτ > Arg Iσ,
then at a Stokes ray with Im Iτ = Im Iσ, one has hτ > hσ. This ensures that the coefficient nτ is
unaffected in crossing the Stokes line, though nσ may jump. The analytically continued integral
will grow exponentially when λ is varied so that Arg Iτ exceeds 3π/2.
have Iσ = 0. Then Qλ is bounded for λ → ∞, in any direction. In particular, it has no
essential singularity at infinity.
The hypothesis that the Iσ = 0 whenever nσ 6= 0 is very strong, and there are not many
obvious examples, other than an oscillatory Gaussian integral with f(x) = x
2
. However,
something similar is possible in Chern-Simons theory.
Now we want to explain a converse. For simplicity, assume that the values of Iσ at
critical points are distinct. (The purpose of this is to avoid possible cancellations.) Let pσ be
a critical point with Iσ 6= 0, and suppose that in some wedge-shaped region of the complex
λ plane, nσ 6= 0. We claim that in this case, the integral Qλ has an essential singularity
at λ = ∞. This result is immediate if hσ > 0, for then the critical point pσ makes an
exponentially large contribution to Qλ in the wedge-shaped region of the λ plane in which
we have started.
Suppose, though, that in the initially considered region of the λ plane, all critical points
with nσ 6= 0 have hσ ≤ 0. This means that for such critical points, Iσ = rσ exp(iφσ), with
rσ positive and π/2 ≤ φσ ≤ 3π/2. Either the largest of the φσ is at least π or the smallest is
no greater than π; suppose for definiteness we are in the former situation. (Otherwise, one
makes the same argument, rotating λ in a counterclockwise rather than clockwise direction.)
Let τ be such that, in the initially chosen wedge in the complex λ plane, φτ is maximal among
38

critical points with nonzero nτ . (If there is more than one critical point with maximal φ, pick
the one of smallest |I|.) Increasing the argument of λ increases all φσ’s by the same amount.
Increase the argument of λ until φτ exceeds 3π/2, so that hτ becomes positive. In the process,
one may cross Stokes rays, but the fact that φτ is maximal and is at least π ensures that nτ
does not jump in crossing such rays. (See fig. 3; if φτ ≥ φσ and Im Iτ = Im Iσ, then hτ ≥ hσ
so nτ does not jump.) Once hτ becomes positive, Qλ grows exponentially with λ, ensuring
that it has an essential singularity at λ = ∞.
3.2.2 A Special Situation
Now we will consider a special situation that was described in section 2.1. We assume that
n = 2w, and that the polynomial f(x) is actually the imaginary part of a polynomial g in w
complex variables z
1
, . . . , zw; we suppose that g is generic enough to have only finitely many
critical points, which are all nondegenerate. Then we consider the integral
Qλ =
Z
d
w
z d
w
z exp(λ(g(z) − g(z)), (3.41)
initially for real λ.
Actually, we can generalize the problem slightly without any difficulty; the generalization
is relevant to Chern-Simons theory. As λ is initially real, we can absorb it in the definition
of g. Then instead of simply analytically continuing with respect to λ, we can analytically
continue with respect to all of the coefficients in g. In other words, the following integral
Qg,eg =
Z
CR
d
w
z d
w
ze exp(g(z) − eg(ze)), (3.42)
is a convergent oscillatory integral if the polynomial eg is the complex conjugate of the
polynomial g (meaning that ge is obtained from g by complex conjugating all coefficients)
and the integration cycle CR is defined by ze
i = z
i
. We would like to analytically continue
with respect to the coefficients in g and eg to get a holomorphic function of those coefficients.
(A similar generalization could be made in section 3.2; we could absorb the real number λ
in the definition of the polynomial f, and then analytically continue with respect to all of
the coefficients in f, not just λ.)
In our previous analysis, we had to avoid λ = 0, and similarly in the present context, we
must impose a condition on how g and eg are allowed to vary. The condition we want is that
as g and eg vary, the critical points of the polynomials g and eg should remain nondegenerate
and their number should remain fixed. For example, we do not allow leading coefficients in
g or eg to vanish in a way that would cause the number of critical points to become infinite
or would cause some critical points to go to infinity. This restriction is assumed in what
follows.
39

The basic idea behind the analytic continuation with respect to g and eg is the same as we
have already described. For eg 6= g, we will have to relax the condition ze = z and integrate
over a more general cycle C:
QJ ;g,eg =
Z
C
d
w
z d
w
ze exp(g(z) − eg(ze)). (3.43)
Of course, the integration cycle C must be chosen so that the integral converges. By now we
know how to describe cycles of the appropriate form. We set I = g(z) − eg(ze) and h = Re I.
We treat h as a Morse function. To each critical point pσ of h, we attach a Lefschetz thimble
Jσ. These cycles form a basis for the appropriate relative homology group. In the original
case eg = g, we express the original real integration cycle CR as a linear combination of the
Jσ’s, by the usual formula CR =
P
σ
nσJσ. The integrals QJσ;g,eg are convergent for all σ, g
and eg, and the desired analytic continuation Qg,eg of our original integral is given by
Qg,eg =
X
σ
nσQJσ;g,eg. (3.44)
The only subtlety is the usual one. As one varies g and eg away from the locus eg = g,
one may cross surfaces on which the cycles Jσ and therefore the coefficients nσ jump. This
happens when there are flows between different critical points, as a result of which the
downward flow from the critical point with greater h fails to define a relative homology
cycle. Since Im I is a conserved quantity in the flow equation, the jumping can only occur
when two distinct critical points have the same value of Im I. The jumping takes the form
Jσ → Jσ + mστJτ , where hσ > hτ and Im Iσ = Im Iτ . We will refer to surfaces on which
distinct critical points have the same value of Im I as Stokes surfaces. We also use the term
Stokes curve for a Stokes surface of real dimension 1 (thus, a Stokes ray is a special case of
a Stokes curve).
What is rather special about this problem is that I = g(z)−ge(ze) is the sum of a function
on one space (which we will call C
w, parametrized by the zi
) and a function on another
space (which we will call Cew, a second copy of C
w parametrized by the zei
). I is defined on
the product space X = C
2w = Cw × Cew. The fact that I is the sum of functions on the two
factors has obvious implications for the critical points.
Let qσ, σ ∈ Σg be the critical points of g, as a function on C
w, and let rτ , τ ∈ Σeg, be
the critical points of eg, as a function on Cew. Then the critical points of I are the points
pσ,τ = qσ × rτ ∈ C
w × Cew = X. Similarly, the Lefschetz thimble Jσ,τ associated to a critical
point pσ,τ in X is the product of cycles J
g
σ ∈ C
w and Jeg
τ ∈ Cew. Here J
g
σ
is the Lefschetz
thimble in C
w associated to the critical point qσ of the Morse function Re g, and similarly
J
eg
τ
is the Lefschetz thimble in Cew associated to the critical point rτ of the Morse function
Re (−eg).
40

We can therefore rewrite (3.44) as follows:
Qg,eg =
X
σ∈Σg
X
τ∈Σge
nσ,τ Z
J
g
σ
d
w
z exp(g(z)) Z
J
ge
τ
d
w
ze exp(−eg(ze)). (3.45)
Thus Qg,eg is everywhere a finite sum of functions of g times functions of ge, obtained from
integrals over the z’s and the ze’s, respectively. The coefficients in the sum, however, can
jump as one crosses Stokes surfaces.
As was explained in section 2, the problem that we have just described is a prototype for
analytic continuation of Chern-Simons gauge theory with complex gauge group.
