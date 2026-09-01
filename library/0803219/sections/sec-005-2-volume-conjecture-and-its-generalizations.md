---
doc_id: 0803219
doc_title: "ACTA MATHEMATICA VIETNAMICA 219 AN INTRODUCTION TO THE VOLUME CONJECTURE AND ITS GENERALIZATIONS"
section_id: sec-005-2-volume-conjecture-and-its-generalizations
section_title: "Volume conjecture and its generalizations"
section_number: 2
pages: 9-10
source_pdf: 0803219.pdf
source_sha256: 8e37e11b8c8953c8
---
In this paper we use another normalization CS( M ) := − 2π 2 cs(M ) so that
Vol(M ) + √ − 1 CS(M ) can be regarded as a complexiﬁcation of the volume
Vol(M ). Note that if M has a cusp (that is, if M is homeomorphic to the
interior of a manifold with torus boundary), cs is deﬁned mod ulo 1 / 2 and so CS
is deﬁned modulo π 2. It is known that the imaginary part of the SL(2; C) Chern–
Simons function of the holonomy representation is the volum e with respect to the
hyperbolic metric and the real part is the SO(3) Chern–Simons invariant up to
multiplications of some constants [59, Lemma 3.1] (see also [33, p. 554]).
When M has a cusp and possesses a complete hyperbolic structure of ﬁ nite
volume, we can deform the structure to incomplete ones by usi ng a complex pa-
rameter u around 0, where u = 0 corresponds to the complete structure. Then
T. Yoshida [59, Theorem 2] (see also [51, Conjecture]) prove d that there exists a
complex analytic function f (u) around 0 such that if the corresponding (incom-
plete) hyperbolic manifold can be completed to a closed mani fold Mu by adding
a geodesic loop γ , then
(1.2) Vol( Mu) +
√
− 1 CS(Mu) −
{
Vol(M ) +
√
− 1 CS(M )
}
≡ f (u)√ − 1 − π
2
{
length(γ ) +
√
− 1 torsion(γ )
}
(mod π 2√
− 1Z),
where length( γ ) and torsion( γ ) are the length and the torsion of γ respectively.
(The torsion measures how much a normal vector is twisted whe n it travels around
γ .)
We can interpret (1.2) in terms of Kirk and Klassen’s Chern–S imons function
csM .
For simplicity we assume that M := S3 \ K is the complement of a hyperbolic
knot K, that is, we assume that M has a complete hyperbolic structure with ﬁnite
volume. Then u deﬁnes an (incomplete) hyperbolic structure, and so gives t he
holonomy representation ρ of π 1(M ) at P SL(2; C). (Recall that the orientation
preserving isometry group of the hyperbolic space H3 is P SL(2; C). Since the
universal cover of M is H3, the lift of an element in π 1(M ) deﬁnes an isometric
translation in H3, giving an element in P SL(2; C).) We choose a lift of ρ to
SL(2; C) [7] and denote it also by ρ .
We can regard exp( u) as the ratio of the eigenvalues of the image of the merid-
ian µ ∈ π 1(M ) by the representation ρ , that is, the eigenvalues of ρ (µ ) ∈ SL(2; C)
are exp(u/ 2) and exp( − u/ 2). We can also deﬁne v(u) so that exp
(
v(u)
)
is the ra-
tio of the eigenvalues of the image of the longitude λ . Then from [33, pp. 553–556]
csK := cs M can be expressed in terms of f (u) as follows.
(1.3) cs K
(
[ρ ]
)
=
[ u
4π √ − 1 , v(u)
4π √ − 1 ; exp
(√ − 1
2π f (u)
)]
.
Note that here we use ( µ, λ ) for the basis of π 1(∂M ).
228 HITOSHI MURAKAMI
Remark 1.5. Note that here we are using the SL(2; C) theory; not P SL(2; C).
So we have to divide the term appearing in exp of (1.3) by − 4 [33, pp. 553–556].
See [33, p. 543].
Note also that we are using the normalization of W. Neumann an d D. Za-
gier [51] for f (u). So Yoshida’s (and Kirk and Klassen’s) f (u) is our f (u)× 2
π √ − 1 .
Remark 1.6. From (1.3), one can deﬁne f (u) modulo 4 π 2Z, but in this paper we
deﬁne it only modulo π 2Z. So we may have to say that we are using P SL(2; C)
theory, and SL(2; C) theory for normalization.
If the incomplete metric is completed by adding a geodesic lo op γ , then the
resulting manifold Ku is obtained from S3 by ( p, q )-Dehn surgery along K for
some coprime integers p and q satisfying p u + q v(u) = 2 π √ − 1. Then from [51,
Lemma 4.2] we have
length(γ ) +
√
− 1 torsion(γ ) = − r u − s v(u) (mod 2 π
√
− 1Z).
where r and s are integers satisfying ps − qr = 1.
Therefore we can express the right hand side of (1.2) in terms of u and v(u).
(1.4) Vol( Ku) +
√
− 1 CS(Ku) −
{
Vol(K) +
√
− 1 CS(K)
}
≡ f (u)√ − 1 + π
2
(
r u + s v(u)
)
(mod π 2√
− 1Z),
where Vol(K) := Vol(S3 \ K) and CS( K) := CS( S3 \ K). Note that this formula
can also be obtained from (1.3) [33].
We also have from [51, (34), p. 323]
length(u) = − 1
2π Im(uv(u)).
Therefore from (1.2) and (1.4) we have
Vol(Ku) − Vol(K) = Im f (u) + 1
