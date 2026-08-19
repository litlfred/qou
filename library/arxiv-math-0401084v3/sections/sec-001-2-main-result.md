---
doc_id: arxiv-math-0401084v3
doc_title: "THE COLORED JONES POL YNOMIALS OF THE"
section_id: sec-001-2-main-result
section_title: "Main result"
section_number: 2
pages: 2-4
source_pdf: 0401084v3.pdf
source_sha256: f56bbd4cee4f3418
doc_brief: "THE COLORED JONES POLYNOMIALS OF THE — W e calculate limits of the colored Jones polynomials of the ﬁ gure- eight knot and conclude that in most cases they determine the volumes and the Chern–Simons"
---
To state our main result we recall some of the results in [16, 24].
Let K be a hyperbolic knot in the three-sphere S3, that is, the complement
S3 \ K has a complete hyperbolic structure. The complete hyperbolic stru cture
can be deformed by a complex parameter u that is the logarithm of the ratio of
the eigenvalues of the image of the meridian K by the holonomy representation
π1(S3 \ K) → SL2(C). We also denote by v the logarithm of the eigenvalue of the
image of the longitude. If the structure is complete, then u = 0. Let Φ( u) be the
potential function introduced in [16, Theorem 3] that satisﬁes





d Φ( u)
du = 2v,
Φ(0) = 0 .
We also put
f (u) := Φ( u)
4 − uv
4 .
(see [16, Equation (50)]).
Let ℓ be a loop on the boundary of the tubular neighborhood N (K) of K in
S3. Suppose that the hyperbolic structure parameterized by u on S3 \ K can
be completed to an orbifold Ku by attaching a solid torus such that its meridian
coincides with ℓ. It is called generalized Dehn surgery and if pu + qv = 2π√−1 for
coprime integers p and q, then it is usual ( p, q)-Dehn surgery and Ku becomes a
closed three-manifold [18, Chapter 4] and ℓ is homotopic to p·meridian+ q·longitude
in π1(∂N (K)). Let γ be the core of the solid torus. It is a geodesic in Ku, and
its length and torsion are denoted by length( γ) and torsion( γ) respectively. (If one
travels around γ then the plane perpendicular to it is rotated by torsion( γ). See [24,
Deﬁnition 1.1] for the precise deﬁnition.) Then the volume and the Che rn–Simons
invariant of Ku can be obtained as follows ([24, Theorem 2], which was conjectured
in [16, Conjecture]).
THE COLORED JONES POLYNOMIALS OF THE FIGURE-EIGHT KNOT 3
Theorem 2.1 (T. Yoshida) . Put λ(γ) := length( γ) + √−1 torsion(γ). Then we
have
Vol(Ku) +
√
−1 CS(Ku) ≡ f (u)√−1 − π
2 λ(γ) + Vol
(
S3 \ K
)
+
√
−1 CS
(
S3 \ K
)
mod π2√
−1Z.
Now we study the case where the knot is the ﬁgure-eight knot E.
Let u be a complex parameter near 0. Put
m := − exp(u/2),
z := −m4 + m2 + 1 +
√
(m2 + m + 1)(m2 + m − 1)(m2 − m + 1)(m2 − m − 1)
2m2 ,
and
w := m4 + m2 − 1 +
√
(m2 + m + 1)(m2 + m − 1)(m2 − m + 1)(m2 − m − 1)
2m2 .
We take the branch of the square root so that z = w = exp(π/3) when u = 0. We
also put
v := 2 log
(
z(1 − z)
)
,
where the branch is chosen so that v = 0 when u = 0. Note that z and w satisfy
the following equations.
{
log w + log
(
1 − z
)
= u,
log z + log
(
1 − z
)
+ log w + log
(
1 − w
)
= 0.
Put
f (u) := 1
2π
{
R(z) + R(w) − π2
6
}
−
√−1
2π Vol
(
S3 \ E
)
and
Φ( u) := 4 f (u) + uv,
where
R(ξ) := 1
2 log ξ log(1 − ξ) −
∫ ξ
0
log(1 − η)
η dη
is Roger’s dilogarithm function. Then





d Φ( u)
du = 2v,
Φ(0) = 0 ,
and
Vol(Eu) +
√
−1 CS(Eu) ≡ f (u)√−1 − π
2 λ(γ) + Vol
(
S3 \ E
)
mod π2√
−1Z,
since CS
(
S3 \ E
)
= 0.
Now we state our main result.
Let JN (K; t) be the colored Jones polynomial of a knot K corresponding to the
N -dimensional representation of sl2(C). We normalize it so that JN (unknot; t) = 1.
Then we have the following theorem.
4 HITOSHI MURAKAMI AND YOSHIYUKI YOKOTA
Theorem 2.2. Let E be the ﬁgure-eight knot. There exists a neighborhood U of 0
in C such that for any u ∈ (U \ π√
−1Q) ∪ {0}, the following limit exists:
(u + 2π
√
−1) lim
N →∞
log
(
JN
(
E; exp
(
(u + 2π√−1)/N
)))
N .
Moreover if we denote the limit by H(u), then it can be extended to a complex
analytic function and it satisﬁes the following equalities .





d H(u)
du = v
2 + π√−1,
H(0) = √−1 Vol(S3 \ E).
Remark 2.3. The precise meaning of the limit is as follows. If the ratio
JN
(
E; exp
(
(u + 2π√−1)/N
))
exp
(
N h(u)
)
grows polynomially with respect to N , then we denote the limit
log
(
JN
(
E; exp
(
(u + 2π√−1)/N
)))
N
by h(u). So it is deﬁned modulo 2 π√−1.
As a corollary we can express the volume and the Chern–Simons invar iant of a
three-manifold obtained from the ﬁgure-eight knot by generalized Dehn surgery.
Corollary 2.4. Let Eu be the three-manifold obtained from the ﬁgure-eight knot by
generalized Dehn surgery corresponding to u near 0 such that πu /∈ Q. Then
Vol(Eu) +
√
−1 CS(Eu) ≡ H(u)√−1 − πu − uv
4√−1 − π
2 λ(γ) mod π2√
−1Z.
