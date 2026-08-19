---
doc_id: arxiv-hep-th-9811173v1
doc_title: "b vol(M) = (−D)3/ 2 (2π)2n− 4 ζK(2) 2ζ(2) for a manifold M whose invariant trace ﬁeldK has a single complex place, discriminant D, degree n, and Dedekind zeta value ζK(2). The larg"
section_id: sec-012-42-dirichlet-character
section_title: "Dirichlet character"
section_number: 4.2
pages: 9-10
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
doc_brief: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links — We identify 998 closed hyperbolic 3-manifolds whose volumes are ratio nally related to"
---
The simplest example of a number ﬁeld with a single complex place is an imag inary-
quadratic ﬁeld Q(
√
−d), where d is a square-free positive integer. When d ≡ 3 (mod 4),
the discriminant is D = −d; otherwise it is D = −4d.
It is proven in [24] that
ζK(2)
ζ(2) =
∑
n>0
χ K(n)
n2 (20)
where χ K is the real Dirichlet character of the group of units of the ﬁeld Z/ |D| and D is
the discriminant of the imaginary-quadratic ﬁeld K. The Dirichlet character is related to
the Jacobi (or Kronecker) symbol by
χ K(n) =
( D
n
)
(21)
which vanishes if gcd(D,n )> 1. When D is odd, one may use the alternative form
(
n
|D|
)
.
Using (20) in (1), at n = 2, one happily disposes of powers of π. We dispose of
√
−D,
by using the imaginary-quadratic result [24]
∑
n>0
χ K(n)
n2 = 1√
−D
∑
− D>k>0
χ K(k)Cl2
(
2πk
|D|
)
(22)
which yields a ﬁnite sum over the elements of the group of units. Finally , we dispose of a
factor 2, via the reﬂection relations χ K(k) = −χ K(|D| −k) and Cl 2(θ) = −Cl2(2π −θ),
to obtain the readily computable result
ZK =Z|D| :=D
∑
− D>2k>0
( D
k
)
Cl2
(
2πk
D
)
(23)
with the magnitude of the discriminant identifying the imaginary-quad ratic ﬁeld.
8http://www.research.att.com/~njas/sequences
8
Thanks to David Bailey [22], it is now a routine matter to evaluate (23) t o high
precision9, using [25]
Cl2(θ)
θ = 1 − 1
2 log(θ2) +
∞∑
n=1
ζ(2n)
2n2 +n
(
θ
2π
) 2n
(24)
which converges faster than 1 / 9n, for θ ∈ [0, 2π/ 3]. An angle in [2 π/ 3,π ] may be trans-
formed to a pair in [0 , 2π/ 3], by rearrangement of the duplication formula
1
