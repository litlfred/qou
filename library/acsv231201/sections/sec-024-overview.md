---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-024-overview
section_title: "Overview"
section_number: null
pages: 132-136
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
In this chapter we generalize the univariate saddle point techniques of Chap-
ter 4 to multivariate Fourier–Laplace integrals of the form
I(λ) =
Z
C
A(z) exp(−λφ(z)) dz ,
(5.1)
where the amplitude A and phase φ are now analytic functions of a vector
argument z in d variables and C is a d-chain in Cd (see Section A.3 of Ap-
pendix A for deﬁnitions involving integration of chains on manifolds). In one
variable, the comprehensive Theorem 4.1 covers all degrees of vanishing of
the phase and amplitude functions. The range of possibilities for the phase
function φ in higher dimensions is much greater, however, and we restrict our-
selves here to the case of nondegenerate phase where the d×d Hessian matrix
H =
 ∂2φ
∂zj ∂zk
!
of φ is nonsingular at the points in the domain of integration de-
termining asymptotics. The Taylor series for φ at a point p ∈Cd is
φ(z) = φ(p) + (z −p)T(∇φ)(p) + 1
2(z −p)T H(p)(z −p) + O

|z −p|3
,
hence the Hessian matrix H(p) represents (twice) the quadratic term in the
phase, and nondegeneracy is a generalization of nonvanishing of the quadratic
term for a univariate phase function.
Exercise 5.1. Determine whether the phase function φ(x, y, z) = z2+(x+y)z+xy
is degenerate at the origin.
We begin, analogously to the univariate case, by considering integrals whose
phase is restricted to the standard quadratic S (z) := z2
1 + · · · + z2
d. Asymptotic
behavior when A is monomial and φ is the standard quadratic (Corollary 5.7
114
5.1 Overview
115
below) is coupled with a big-O bound (Lemma 5.8 below), allowing us to
integrate term by term and obtain the following result. Recall that if r ∈Nd we
write |r| = r1 + · · · + rd.
Theorem 5.1 (standard phase). Let A(x) = P
r∈Nd arxr be a real analytic
function deﬁned on a neighborhood N of the origin in Rd. If
I(λ) =
Z
N
A(x)e−λS (x) dx
(5.2)
then there is an asymptotic series expansion
I(λ) ≈
X
n≥0
X
|r|=n
arβrλ−(|r|+d)/2 ,
where
βr =

0
if any r j is odd
πd/2
d
Y
j=1
(2m j)!
mj!4m j
if r = 2m
.
After establishing Theorem 5.1 in Section 5.2, we use a change of variables
and contour deformation to study the case of nondegenerate phase whose real
part has a strict minimum at the origin. Our next result is proven in Section 5.3;
note that we change our variables from x to z to reﬂect the fact that our proof
works over the complex numbers.
Theorem 5.2 (Re{φ} has a strict minimum). Let A and φ be complex-valued
analytic functions on a compact neighborhood N of the origin in Rd. Suppose
that the real part of φ is nonnegative on N and vanishes only at the origin,
and that the Hessian matrix H of φ at the origin is nonsingular. Then I(λ) =
R
N A(z)e−λφ(z) has an asymptotic expansion
I(λ) ≈
X
ℓ≥0
cℓλ−d/2−ℓ
(5.3)
with leading coeﬃcient
c0 = A(0) (2π)d/2
√
det H
,
(5.4)
where
√
det H is the product of the principal square roots of the eigenvalues
of H.
Exercise 5.2. Show that the expansion in (5.3) can be written as
I(λ) ≈
A(0)
√
det 2πλ H
X
ℓ≥0
c′
ℓλ−ℓ,
(5.5)
116
Multivariate Fourier–Laplace integrals
where c′
0 = 1.
Exercise 5.3. Let c > 0, where c is independent of λ. What happens to the
right side of (5.5) if we change φ to φ/c and λ to cλ?
When Re{φ} is strictly positive except at a ﬁnite number of points in the do-
main of integration of I(λ) then, up to an asymptotically negligible error, we
can express I(λ) as a sum of integrals localized to neighborhoods of these van-
ishing points. A chain of integration in a manifold which can be localized to
arbitrarily small neighborhoods can be pulled back to correspondingly local-
ized integrals over Rd, which is why the above results are stated for integrals
over neighborhoods of the origin in Rd. In dimension greater than one, how-
ever, it is possible for an analytic function to have a real part that vanishes
along a set of positive dimension without vanishing everywhere, meaning it
may not be possible to localize.
Exercise 5.4. Over which of the following chains in C2 does φ(x, y) = x2 + y2
have a nonnegative real part and, among those where this holds, which have
the real part of φ vanishing only at the origin?
(a) a small neighborhood of 0 in the real × real subspace of C2
(b) a small neighborhood of 0 in the imaginary × imaginary subspace of C2
(c) a small neighborhood of 0 in the diagonal subspace {(x, y) ∈C2 : x = y} of
C2
(d) a small neighborhood of 0 in the linear subspace of C2 spanned over R by
(1 + i, 0) and (0, 1 + i)
Such diﬃculties lead us to state our most general results in the language of
stratiﬁed spaces and vector ﬂows. A vector ﬂow on a space X is the solution Ψ :
X ×[0, T] →X to a diﬀerential equation (d/dt)Ψ(x, t) = v(Ψ(x, t)), where v is
a vector ﬁeld on X (see, e.g., Lemma 5.14); an upward gradient ﬂow is deﬁned
by the vector ﬁeld v = ∇φ, while a downward gradient ﬂow is deﬁned by
v = −∇φ. These constructions and results, summarized in Appendix D, have
been around for over 50 years, though they are not very well known outside of
diﬀerential topology and singularity theory. To ease exposition we now state
our main result using some terminology to be deﬁned in Section 5.4, where the
result is proved. If X is an oriented stratiﬁed space then q ∈X is a critical point
(in the stratiﬁed sense) of an analytic map φ : X →C if q lies in a stratum
S and the diﬀerential dφ|S at q is zero. Appendix D contains a more complete
explanation of the vector ﬂows we use.
5.1 Overview
117
Theorem 5.3 (minimum of Re{φ} is not strict but there are ﬁnitely many criti-
cal points). Let V be a smooth complex (d −k)-dimensional algebraic variety
and suppose that
(i) X = ∆p × Md−k is a stratiﬁed space of dimension p + d −k in Cp+d−k,
where ∆p ⊆Rp is the standard p-simplex and Md−k ⊆V ⊆Cd is a
smooth (d −k)-dimensional analytic submanifold of V,
(ii) the closure of X is represented by an analytic (p + d −k)-chain C,
(iii) φ : X →C is an analytic map with minx∈X Re φ(x) = 0, and
(iv) η = A(z) dz is a holomorphic (p + d −k)-form on X.
Assume that the set G of critical points of φ on C is ﬁnite and that the subset
G′ ⊆G where Re φ vanishes are all in strata of dimension p + d −k. Suppose
also that
(v) det H(q) , 0 for all q ∈G′, where H is the Hessian matrix for φ in some
local coordinates near q,
(vi) the imaginary part (and thus all) of φ(q) is zero for all q ∈G′,
(vii) the boundary ∂C is supported on strata of dimension at most p+d−k−1,
with its simplices σ j analytic orientation preserving maps having disjoint
interiors, and
(viii) the elements of G′ lie in the interiors of distinct simplices σj.
Then the integral
I(λ) =
Z
C
e−λφ(z) η
has an asymptotic expansion
I(λ) ≈
∞
X
ℓ=0
cℓλ−(d−k)/2−ℓ
(5.6)
as λ →∞, with leading term
c0 = (2π)d/2 X
q∈G′
A(q)
p
det H(q)
.
(5.7)
The sign for the square root of the determinant is computed by choosing a
parametrization Υ for X near q by a neighborhood of the origin in Rp+d−k
and then multiplying the principal square roots of the eigenvalues of φ in these
coordinates with the Jacobian determinant det dΥ(q).
Without the assumption that the imaginary part of φ(q) vanishes for q ∈G′
the formula (5.7) holds when each summand is multiplied by the term e−λφ(q)
with modulus 1, making c0 = c0(λ) dependent on λ but having bounded modu-
lus.
118
Multivariate Fourier–Laplace integrals
Remark 5.4. We apply Theorem 5.3 at two points in this book: ﬁrst with p = 0
and k = 1 to derive Theorem 9.12, and second in its more general form to prove
asymptotics for multiple points in Chapter 10. In the statement of the theorem,
the ﬁrst four conditions are geometric conditions ensuring the existence of the
necessary deformations and analytic extensions, while the last four ensure we
know how to do computations.
Example 5.5. Let X = I × S 1, where I is the interval [−1, 1] and S 1 is the unit
circle parametrized by θ ∈[−π, π] with the endpoints identiﬁed, so that X can
be nicely embedded in C2. We apply Theorem 5.3 in the case p = k = 1 and
d = 2, with A(x, y) = 1 and φ : X →C deﬁned by
φ(t, θ) = Kθ2 + iLθt
(5.8)
for real numbers K > 0 and L. The phase φ is analytic on X, and the 2-chain C
representing X can be any cell complex with a subcomplex I×N for a compact
neighborhood N of θ = 0 in S 1. There is a single critical point p = (0, 0), at
which Re φ vanishes, so G′ = G = {p}.
Note that the strip I × {0} on which the phase function vanishes extends out
to the bounding circles of the cylinder X, so we are not in a case where the
magnitude of the integrand is small away from p, and Theorem 5.2 does not
apply. The Hessian matrix of φ at p is

2K iL
iL 0

, so Theorem 5.3 implies
I(λ) =
Z
N×I
e−λφ(x) dx ∼2π
λ |L|.
The choice of sign on the term
√
L2 = |L| is arbitrary and depends on properly
orienting N × I for the application at hand.
◁
Exercise 5.5. Let X be the real sphere {(x, y, z) ∈R3 : x2 + y2 + z2 = 1} ⊂C3
and let φ(x, y, z) = z2 + ix2.
(a) Identify the sets G and G′.
(b) Determine H(q) for q ∈G′.
(c) Determine c0(λ) when A(x, y, z) = 1 + x + y.
