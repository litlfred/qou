---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-028-higher-order-terms-in-the-expansions
section_title: "Higher order terms in the expansions"
section_number: null
pages: 147-152
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
129
then gives an asymptotic expansion for the integral over each simplex. Invari-
ance of det J(Υ)/
√
H under coordinate transformations equates the summand
in (5.7) with the result (5.4) in Theorem 5.2, provided the correct sign in (5.7)
is chosen to match (5.4). Summing these expansions then ﬁnishes the proof of
Theorem 5.3.
□
Exercise 5.11. The simplest case of Theorem 5.3 occurs when p = 0, d =
1, and k = 0. Take φ(z) = −z2, so e−λφ(z) = eλz2, and let M be the 1-chain
consisting of the imaginary axis. Which sign in the equality
Z
M
eλz2dz = ±i
r
2π
λ
is correct when parametrizing M by z = it for t ∈R, and which sign is correct
when parametrizing M by z = −it?
5.5 Higher order terms in the expansions
All of our explicit asymptotic computations ultimately reduce to computing
terms in the asymptotic expansions of Fourier–Laplace integrals. It is therefore
useful to have a closed formula for the higher-order terms that can appear. The
following result is derived in [H¨or83, Thm. 7.7.5] using smooth methods, and
we refer the reader to that source for a proof.
Lemma 5.16. Let X ⊆Rd be an open neighborhood of the origin and let φ and
A be smooth functions on X such that Re{φ} ≥0 on X. Further suppose that φ
has a unique critical point on the support of A at the origin, that φ(0) = 0, and
that the Hessian H of φ at 0 is nonsingular. Then for any positive integer M
and λ > 0 there exist constants Lk(A, φ) such that

Z
X
A(x)e−λφ(x)dx −λ−d/2 (2π)d/2
√
det H
X
0≤k<M
λ−kLk(A, φ)

≤C(φ)λ−d/2−M X
|β|≤2M
sup |DβA|,
where the constant C(φ) has a uniform bound when φ stays in a bounded set of
(3N + 1)-diﬀerentiable functions on X for which ∥x∥/∥∇φ(x)∥has a uniform
bound. Setting
φ(x) = φ(x) −(1/2)x · H ·xT,
130
Multivariate Fourier–Laplace integrals
which vanishes to order three at 0, we have
Lk(A, φ) = (−1)k X
0≤ℓ≤2k
Dℓ+k 
A(x) · φ(x)ℓ
2ℓ+kℓ!(ℓ+ k)!

x=0
,
(5.14)
where D is the diﬀerential operator
D = −
X
1≤i,j≤d

H−1
i j ∂i∂j.
The total number of derivatives of A in the term Lk(A, φ) is at most 2k and the
total number of derivatives of φ is at most 2k + 2.
□
Interpreting this in our context, we obtain the following.
Corollary 5.17 (full expansion of Fourier–Laplace integral). Assume the hy-
potheses of Theorem 5.2 and suppose further that φ has a single critical point
on N which lies at the origin. Then the constants in (5.3) satisfy
ck = (2π)d/2
√
det H
Lk(A, φ)
for each k ≥0, where Lk is as deﬁned by (5.14).
The fact that Lemma 5.16 requires only smoothness also makes it easy to
localize.
Lemma 5.18. If φ has a ﬁnite number of critical points on N where the hy-
potheses of Corollary 5.17 hold, then an asymptotic expansion for I(λ) is
obtained by summing the expansions corresponding to each of these critical
points.
Proof
The proof of Theorem 5.2 shows that the contribution from the bound-
ary of the domain of integration may be ignored – we may localize to a neigh-
borhood N′ of the critical point that is diﬀeomorphic to an open ball in Rd.
Replacing A by the product Aα of A with a compactly supported smooth func-
tion α that is equal to one on N′, the result follows from Lemma 5.16.
□
Exercise 5.12. Verify that when A(0) , 0 the leading constant of (5.3) matches
the expression in Corollary 5.17.
Notes
A number of the results in this section originally appeared in [PW10]. In the
case of purely real or imaginary phase, the results of this chapter are fairly
5.5 Higher order terms in the expansions
131
standard; see [BH86; Won01] for real phase or [Ste93] for imaginary phase.
We have not seen the complex phase result Theorem 5.2 stated before, though
such a result was certainly understood to be true. The remaining statements
and proofs via complex deformation methods are new, though not surprising.
Theorem 5.4.8 from the ﬁrst edition has been replaced by Theorem 5.3. The
proof has been split into two parts. The ﬁrst part, involving stratiﬁed Morse
deformations, is a standard stratiﬁed construction and is summarized in Ap-
pendix D. The second part, deforming a chain by complexifying and manipu-
lating the chain through complex space, is new as far as we know and spelled
out in Section 5.4.
According to B. Lamel (personal communication), intrinsic complexiﬁca-
tions of strata of any stratiﬁed space (see Remark 5.12) should ﬁt together to
form a complex stratiﬁed space, provided the (real) tangent spaces E at every
point satisfy E∩iE = {0}. This would imply that Lemma 5.11 and hence Theo-
rem 5.3 holds for any stratiﬁed space of dimension m analytically embedded in
Cm. However, this appears to require some condition about extending the (real)
chart maps of each stratum beyond its boundary, which can be done with ∆p
and Md−1 but not for arbitrary stratiﬁed spaces (where the boundary might be
a singularity of the stratum). We could not ﬁnd such an argument in the exist-
ing literature, which is why Theorem 5.3 is restricted to products of stratiﬁed
spaces for which we have explicit complexiﬁcations.
The general approach, namely to stay in the analytic category and use de-
formations suggested by stratiﬁed Morse theory for complex spaces, is an ex-
tension of our treatment of univariate Fourier–Laplace integrals in Chapter 4.
The main motivation for doing things the way we have is that the analysis of
multiple points in Chapter 10 requires us to integrate over the product of a
chain in V with an abstract simplex; when integrating terms with imaginary
phase over manifolds with boundary, one needs a way to eliminate boundary
terms. A result similar to Theorem 5.3 was proved in [PV19, Theorem 4.2], via
an approach which avoids Morse theoretic contour deformation arguments, re-
placing these by iterated integrals and single parameter steepest descent curves.
The ﬁrst edition of the book assumed a strong torality hypothesis when de-
riving asymptotics (see, e.g., Corollaries 9.2.4 and 9.2.9 there), which allowed
use of known techniques in the case where the phase is purely imaginary and
the contour of integration has no boundary. In the present edition this overly
strong hypothesis has been replaced by a weaker notion for which Theorem 5.3
has been speciﬁcally designed (see Theorem 9.12).
132
Multivariate Fourier–Laplace integrals
Additional exercises
Exercise 5.13. Consider an integrand of the form A(x, y, z)e−λS (x,y,z) dz, where
A(x, y, z) = (x2 +y2 +z2)α is not smooth at the origin when α < Z>0. What kind
of asymptotic estimate or expansion can be obtained in this case?
Exercise 5.14. Prove that for critical points on the boundary of the chain of
integration, where the chain is locally diﬀeomorphic to a halfspace and φ has
vanishing one-sided normal derivative, the conclusion of Theorem 5.2 holds
with the leading coeﬃcient multiplied by 1/2. (See Example 10.66 in Chap-
ter 10 for an application of this result.)
Exercise 5.15. (non-isolated critical points) Consider the integral
Z ε
−ε
Z 1
0
e−λφ(θ,t)dtdθ,
where φ(θ, t) = (1−t)g1(θ)+tg1(θ) and each gi is analytic and vanishes to order
2 at θ = 0, with positive second derivative. Calculate the ﬁrst-order asymptotic
as λ →∞in terms of derivatives of g1 and g2 at 0. (This foreshadows the
computations in Section 10.5, in particular Proposition 10.62.)
Exercise 5.16. Use the vanishing to order 3 of φ at the origin to write a simpler
expression for L1(A, φ). Further simplify it in the cases where A vanishes to
orders one, two, and three, respectively, at the origin.
Exercise 5.17. (alternative method to compute higher order terms) This exer-
cise outlines an alternative way of computing higher order terms in the asymp-
totic expansion of a Fourier–Laplace integral. Assume for simplicity that the
phase φ has a single critical point, occurring at 0, and that the amplitude A
vanishes outside the closure of a neighborhood of 0. Let S be the standard
quadratic S (z) = Pd
i=1 z2
i .
(i) Prove that when φ = S , the diﬀerential operator
X
|r|=k
∂2r1
1 · · · ∂2rd
d
4kr1! · · · rd!,
when applied to A and evaluated at 0, gives the coeﬃcient ck from Theo-
rem 5.3.
(ii) The Complex Morse Lemma gives an analytic change of variables z =
ψ(y) such that S (y) = (φ ◦ψ)(y). Apply the result of (i) and solve a
triangular system to compute the derivatives of ψ at 0. Note that this
changes the amplitude function A to (A ◦ψ) det ψ′.
5.5 Higher order terms in the expansions
133
(iii) Use Corollary 5.7 and steps (i) and (ii) to derive an explicit formula for
asymptotics in the case d = k = 1. Check your result against the formula
given in Corollary 5.17.
