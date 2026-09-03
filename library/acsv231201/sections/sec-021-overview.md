---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-021-overview
section_title: "Overview"
section_number: null
pages: 132-136
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
doc_brief: "Analytic Combinatorics in Several Variables — 85 sections: Preface to the second edition; List of Symbols; Introduction"
---
In this chapter we generalize the univariate saddle point techniques of Chap-
ter 4 to multivariate Fourier–Laplace integrals of the form
I(λ) =
∫
C
A(z) exp(−λφ(z)) dz, (5.1)
where the amplitude A and phase φ are now analytic functions of a vector
argumentz in d variables andC is a d-chain in Cd (see Section A.3 of Ap-
pendix A for deﬁnitions involving integration of chains on manifolds). In one
variable, the comprehensive Theorem 4.1 covers all degrees of vanishing of
the phase and amplitude functions. The range of possibilities for the phase
functionφ in higher dimensions is much greater, however, and we restrict our-
selves here to the case ofnondegenerate phase where the d×d Hessian matrix
H =
( ∂2φ
∂z j∂zk
)
ofφ is nonsingular at the points in the domain of integration de-
termining asymptotics. The Taylor series forφ at a pointp∈Cd is
φ(z) =φ(p) + (z−p)T (∇φ)(p) + 1
2(z−p)TH(p)(z−p) + O
(
|z−p|3)
,
hence the Hessian matrix H(p) represents (twice) the quadratic term in the
phase, and nondegeneracy is a generalization of nonvanishing of the quadratic
term for a univariate phase function.
Exercise 5.1. Determine whether the phase functionφ(x, y, z) = z2+(x+y)z+xy
is degenerate at the origin.
We begin, analogously to the univariate case, by considering integrals whose
phase is restricted to the standard quadratic S (z) := z2
1 +··· + z2
d. Asymptotic
behavior when A is monomial and φ is the standard quadratic (Corollary 5.7
114
5.1 Overview 115
below) is coupled with a big-O bound (Lemma 5.8 below), allowing us to
integrate term by term and obtain the following result. Recall that ifr∈Nd we
write|r| = r1 +··· + rd.
Theorem 5.1 (standard phase). Let A (x) = ∑
r∈Nd arxr be a real analytic
function deﬁned on a neighborhoodN of the origin inRd. If
I(λ) =
∫
N
A(x)e−λS (x) dx (5.2)
then there is an asymptotic series expansion
I(λ)≈
∑
n≥0
∑
|r|=n
arβrλ−(|r|+d)/2,
where
βr =

0 if any r j is odd
πd/2
d∏
j=1
(2m j)!
m j!4m j
ifr = 2m .
After establishing Theorem 5.1 in Section 5.2, we use a change of variables
and contour deformation to study the case of nondegenerate phase whose real
part has a strict minimum at the origin. Our next result is proven in Section 5.3;
note that we change our variables fromx toz to reﬂect the fact that our proof
works over the complex numbers.
Theorem 5.2 (Re{φ} has a strict minimum) . Let A and φ be complex-valued
analytic functions on a compact neighborhoodN of the origin inRd. Suppose
that the real part of φ is nonnegative onN and vanishes only at the origin,
and that the Hessian matrixH ofφ at the origin is nonsingular. ThenI(λ) =∫
N A(z)e−λφ(z) has an asymptotic expansion
I(λ)≈
∑
𝓁≥0
c𝓁λ−d/2−𝓁 (5.3)
with leading coeﬃcient
c0 = A(0) (2π)d/2
√
detH
, (5.4)
where
√
detH is the product of the principal square roots of the eigenvalues
ofH.
Exercise 5.2. Show that the expansion in (5.3) can be written as
I(λ)≈ A(0)√
det 2πλH
∑
𝓁≥0
c′
𝓁λ−𝓁, (5.5)
116 Multivariate Fourier–Laplace integrals
where c′
0 = 1.
Exercise 5.3. Let c > 0, where c is independent of λ. What happens to the
right side of (5.5) if we changeφ toφ/c andλ to cλ?
When Re{φ} is strictly positive except at a ﬁnite number of points in the do-
main of integration ofI(λ) then, up to an asymptotically negligible error, we
can expressI(λ) as a sum of integrals localized to neighborhoods of these van-
ishing points. A chain of integration in a manifold which can be localized to
arbitrarily small neighborhoods can be pulled back to correspondingly local-
ized integrals over Rd, which is why the above results are stated for integrals
over neighborhoods of the origin in Rd. In dimension greater than one, how-
ever, it is possible for an analytic function to have a real part that vanishes
along a set of positive dimension without vanishing everywhere, meaning it
may not be possible to localize.
Exercise 5.4. Over which of the following chains inC2 doesφ(x, y) = x2 + y2
have a nonnegative real part and, among those where this holds, which have
the real part ofφ vanishing only at the origin?
(a) a small neighborhood of 0 in the real× real subspace ofC2
(b) a small neighborhood of 0 in the imaginary× imaginary subspace ofC2
(c) a small neighborhood of 0 in the diagonal subspace{(x, y)∈C2 : x = y} of
C2
(d) a small neighborhood of 0 in the linear subspace ofC2 spanned overR by
(1 + i, 0) and (0, 1 + i)
Such diﬃculties lead us to state our most general results in the language of
stratiﬁed spaces and vector ﬂows. Avector ﬂow on a space X is the solutionΨ :
X× [0, T]→ X to a diﬀerential equation (d/dt)Ψ(x, t) =v(Ψ(x, t)), wherev is
a vector ﬁeld on X (see, e.g., Lemma 5.14); anupward gradient ﬂow is deﬁned
by the vector ﬁeld v =∇φ, while a downward gradient ﬂow is deﬁned by
v =−∇ φ. These constructions and results, summarized in Appendix D, have
been around for over 50 years, though they are not very well known outside of
diﬀerential topology and singularity theory. To ease exposition we now state
our main result using some terminology to be deﬁned in Section 5.4, where the
result is proved. IfX is an oriented stratiﬁed space thenq∈ X is a critical point
(in the stratiﬁed sense) of an analytic map φ : X→ C ifq lies in a stratum
S and the diﬀerential dφ|S atq is zero. Appendix D contains a more complete
explanation of the vector ﬂows we use.
5.1 Overview 117
Theorem 5.3 (minimum of Re{φ} is not strict but there are ﬁnitely many criti-
cal points). LetV be a smooth complex (d− k)-dimensional algebraic variety
and suppose that
(i) X = ∆ p× Md−k is a stratiﬁed space of dimension p + d− k in Cp+d−k,
where ∆p ⊆ Rp is the standard p-simplex and M d−k ⊆ V ⊆Cd is a
smooth (d− k)-dimensional analytic submanifold ofV,
(ii) the closure of X is represented by an analytic (p + d− k)-chainC,
(iii) φ : X→C is an analytic map with minx∈X Reφ(x) = 0, and
(iv) η = A(z) dz is a holomorphic (p + d− k)-form on X.
Assume that the set G of critical points of φ onC is ﬁnite and that the subset
G′⊆ G where Reφ vanishes are all in strata of dimension p + d− k. Suppose
also that
(v) detH(q), 0 for allq∈ G′, whereH is the Hessian matrix forφ in some
local coordinates nearq,
(vi) the imaginary part (and thus all) of φ(q) is zero for allq∈ G′,
(vii) the boundary ∂C is supported on strata of dimension at most p+d−k−1,
with its simplicesσ j analytic orientation preserving maps having disjoint
interiors, and
(viii) the elements of G′ lie in the interiors of distinct simplicesσ j.
Then the integral
I(λ) =
∫
C
e−λφ(z)η
has an asymptotic expansion
I(λ)≈
∞∑
𝓁=0
c𝓁λ−(d−k)/2−𝓁 (5.6)
asλ→∞, with leading term
c0 = (2π)d/2
∑
q∈G′
A(q)√
detH(q)
. (5.7)
The sign for the square root of the determinant is computed by choosing a
parametrization Υ for X near q by a neighborhood of the origin in Rp+d−k
and then multiplying the principal square roots of the eigenvalues ofφ in these
coordinates with the Jacobian determinant det dΥ(q).
Without the assumption that the imaginary part ofφ(q) vanishes forq∈ G′
the formula (5.7) holds when each summand is multiplied by the term e −λφ(q)
with modulus 1, making c0 = c0(λ) dependent onλ but having bounded modu-
lus.
118 Multivariate Fourier–Laplace integrals
Remark 5.4. We apply Theorem 5.3 at two points in this book: ﬁrst withp = 0
and k = 1 to derive Theorem 9.12, and second in its more general form to prove
asymptotics for multiple points in Chapter 10. In the statement of the theorem,
the ﬁrst four conditions are geometric conditions ensuring the existence of the
necessary deformations and analytic extensions, while the last four ensure we
know how to do computations.
Example 5.5. Let X = I× S 1, where I is the interval [−1, 1] and S 1 is the unit
circle parametrized by θ∈ [−π,π ] with the endpoints identiﬁed, so that X can
be nicely embedded in C2. We apply Theorem 5.3 in the case p = k = 1 and
d = 2, with A(x, y) = 1 andφ : X→C deﬁned by
φ(t,θ ) = Kθ2 + iLθt (5.8)
for real numbers K > 0 and L. The phaseφ is analytic on X, and the 2-chainC
representing X can be any cell complex with a subcomplexI×N for a compact
neighborhoodN ofθ = 0 in S 1. There is a single critical point p = (0, 0), at
which Reφ vanishes, so G′ = G ={p}.
Note that the strip I×{ 0} on which the phase function vanishes extends out
to the bounding circles of the cylinder X, so we are not in a case where the
magnitude of the integrand is small away from p, and Theorem 5.2 does not
apply. The Hessian matrix ofφ atp is
(
2K iL
iL 0
)
, so Theorem 5.3 implies
I(λ) =
∫
N×I
e−λφ(x) dx∼ 2π
λ|L|.
The choice of sign on the term
√
L2 =|L| is arbitrary and depends on properly
orientingN× I for the application at hand. ◁
Exercise 5.5. Let X be the real sphere{(x, y, z)∈R3 : x2 + y2 + z2 = 1}⊂ C3
and letφ(x, y, z) = z2 + ix2.
(a) Identify the sets G and G′.
(b) Determine H(q) forq∈ G′.
(c) Determine c0(λ) when A(x, y, z) = 1 + x + y.
