---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-028-72-the-matrix-coefficients-and-the-fundamental-c
section_title: "The matrix coefficients and the fundamental corepresentation"
section_number: 7.2
pages: 58-61
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
The matrix coeﬃcients and the fundamental corepresen-
tation
Recall that for SL+(2, R) ⊂SL(2, R) the positive semigroup, the class of principal
series representation can be expressed by considering the actions on homogeneous
monomials (see e.g. [43]):
xl−iµyl+iµ
7→
(ax + cy)l−iµ(bx + dy)l+iµ
:=
Z
R
tl
µν(g)xl−iνyl+iνdν,
(7.22)
where µ ∈R, l ∈−1
2 + iR, so that the representation is unitary.
In terms of
coordinates, the representation acts on L2(R) by
g · f(µ) 7→
Z
R
tl
µν(g)f(ν)dν.
(7.23)
In [8], it is noted that for commuting variables x, y,
[xz11 + yz21, xz12 + yz22] = 0
(7.24)
by the commutation relations. Hence the following fundamental corepresentation
for D(A) = GL+
q (2, R) is well-deﬁned:
Deﬁnition 7.10. The fundamental corepresentation of GL+
q (2, R) on L2(R) is de-
ﬁned by
T λ : f(s) 7→
Z
R
T λ
s,α(z)f(α)dα,
(7.25)
58
where T λ
s,α(z) is formally deﬁned by
(xz11 + yz21)b−1(l−is)(xz12 + yz22)b−1(l+is)N
Q
2b =:
Z
R
T λ
s,α(z)xb−1(l−iα)yb−1(l+iα)dα

(7.26)
with l := −Q
2 + iλ, α, λ ∈R and N = z11z22 −z12z21 = A ˆA.
More generally, we can introduce arbitrary character of the determinant, and
will consider the corepresentation T λ,t deﬁned by
T λ,t
s,α(z) := N ib−1(t−λ)/2T λ
s,α(z)N ib−1(t−λ)/2.
(7.27)
Remark 7.11. The term N
Q
2b is to make the corepresentation unitary. As seen
from below, it is coming from the modular element δ−1
2 in the fundamental corepre-
sentation (6.45) of the quantum plane. The factor chosen for N in T λ,t is for later
convenience when we obtain the fundamental representation.
Remark 7.12. Using the Mellin transform, we can also write T λ
s,α(z) as
T λ
s,α(z) =
1
2πb
Z ∞
0
(xz11 + z21)b−1(l−iα)(xz12 + z22)b−1(l+iα)xb−1(−l+is) dx
x

N
Q
2b .
(7.28)
This can be seen as the generalization of the matrix coeﬃcients in the compact case,
see e.g. [11].
Proposition 7.13. The matrix coeﬃcient is given explicitly by
T λ,t
s,α(z)
=
Z
R+i0

l + iα
iτ + iα

b

l + iτ
is + iτ

b
eπi(t−λ)(s+α+2τ)eπQ(s+τ) ·
Aib−1(t−s)Bib−1(s+τ) ˆBib−1(α+τ) ˆAib−1(t−τ)dτ
(7.29)
=
Z
R+i0
Gb(−iτ −iα)Gb( Q
2 + iτ −iλ)
Gb( Q
2 −iα −iλ)
Gb(−iτ −is)Gb( Q
2 + is −iλ)
Gb( Q
2 −iτ −iλ)
·
eπi(t−λ)(s+α+2τ)eπQ(s+τ)Aib−1(t−s)Bib−1(s+τ) ˆBib−1(α+τ) ˆAib−1(t−τ)dτ,
(7.30)
where l = −Q
2 + iλ and

α
β

b
= Gb(−β)Gb(β−α)
Gb(−α)
is the q-binomial coeﬃcient (cf.
Lemma 3.8).
Hence under some changes of variables, the corepresentation
f(s) 7→
Z
R
T λ,t
s,α(z)f(α)dα
59
is given by
f(s)
7→
Z
R+i0
Z
R+i0
f(s + α −τ) Gb(−iα)
Gb(Q + iτ)
Gb( Q
2 −is + iλ + iτ)Gb( Q
2 −is −iλ + iτ)
Gb( Q
2 −is + iλ)Gb( Q
2 −is −iλ −iα + iτ)
eπiλ(τ−α)e−2πiτseπit(τ+α)Aib−1(t−s)Bib−1τ ˆBib−1α ˆAib−1(t+s−τ)dαdτ.
(7.31)
Proof. We can make use of the Gauss decomposition (Proposition 7.3) and obtain
T λ
s,α(z) =
Z
tλ
s,τ(A)ˆtλ
τ,α( ˆ
A)dτ,
(7.32)
where the matrix coeﬃcients correspond to the fundamental representation of the
quantum plane (6.45):
tλ
s,α
:
Z
f(s)xb−1(l−is)yb−1(l+is)ds
7→
Z
f(s)(xA + yB)b−1(l−is)yb−1(l+is)ds

A
Q
2b
=
Z
f(s)
 l −is
iα

b
A−Q
2b +ib−1(λ−s−α)Bib−1αA
Q
2b xb−1(l−is−iα)yb−1(l+is+iα)dαds
=
Z
f(s)

l −is
iα −is

b
eπQ(α−s)Aib−1(λ−α)Bib−1(α−s)xb−1(l−iα)yb−1(l+iα)dαds.
Hence renaming s ←→α, we see that the matrix coeﬃcient is given by
tλ
s,α(A) =
 l −iα
is −iα

b
eπQ(s−α)Aib−1(λ−s)Bib−1(s−α).
(7.33)
A similar analysis using
ˆtλ
s,α :
Z
f(s)xb−1(l−is)yb−1(l+is)ds 7→
Z
f(s)xb−1(l−is)(x ˆB + y ˆA)b−1(l+is)ds

ˆA
Q
2b
shows that ˆtλ
s,α( ˆ
A) is given by
ˆtλ
s,α( ˆ
A) =
 −l + iα
−is + iα

b
ˆBib−1(α−s) ˆAib−1(s+λ).
(7.34)
Hence using (7.32) with the contour of τ separating the poles of Gb(· ± iτ), we
obtain
T λ
s,α(z)
=
Z
R−i0

l + iα
−iτ + iα

b
 l −iτ
is −iτ

b
eπQ(s−τ)Aib−1(λ−s)Bib−1(s−τ) ˆBib−1(α−τ) ˆAib−1(λ+τ)dτ
=
Z
R+i0

l + iα
iτ + iα

b

l + iτ
is + iτ

b
eπQ(s+τ)Aib−1(λ−s)Bib−1(s+τ) ˆBib−1(α+τ) ˆAib−1(λ−τ)dτ.
60
Finally, for T λ,t
s,α(z), by commuting A and ˆA of N ib−1(t−λ)/2 = (A ˆA)ib−1(t−λ)/2 to the
corresponding sides, we pick up the factor eπi(t−λ)(s+α+2τ), and obtain the desired
formula.
Corollary 7.14. The matrix coeﬃcient T λ
s,α(z) can also be expressed in closed form
as
T λ
s,α(z)
=
Ab−1(l−is)Bb−1(l+is) ˆBb−1(l+iα)

2l
l + is

b
Fb(−l −is, −l −iα, −2l; −ζ−1)N
Q
2b ,
(7.35)
where l = −Q
2 + iλ, ζ = qB ˆB ˆA−1 is the hyperbolic element deﬁned in (7.21),
Fb(α, β, γ; z) :=
Gb(γ)
Gb(α)Gb(β)
Z
C
(−z)ib−1τeπiτ 2 Gb(α + iτ)Gb(β + iτ)Gb(−iτ)
Gb(γ + iτ)
dτ
(7.36)
is the b-hypergeometric function (slightly modiﬁed from [32]), which is the quantum
analogue of the classical 2F1(a, b, c; z). Hence (7.35) is exactly the quantum analogue
of the classical formula for SL+(2, R) given in [43, VII. 4.1(4)], where the hyperbolic
element is ζ = sinh2 θ:
T l
mn =
1
2πiAl−mBl+m ˆBl+n Γ(−l −m)Γ(−l + m)
Γ(−2l)
2F1(−l −m, −l −n, −2l; −
1
sinh2 θ),
(7.37)
where A, B, ˆB are the corresponding variables in the Gauss decomposition for SL+
2 (R).
