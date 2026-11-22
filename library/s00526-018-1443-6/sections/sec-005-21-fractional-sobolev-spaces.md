---
doc_id: s00526-018-1443-6
doc_title: "On the analyticity of critical points of the Möbius energy"
section_id: sec-005-21-fractional-sobolev-spaces
section_title: "Fractional Sobolev spaces"
section_number: 2.1
pages: 4-5
source_pdf: s00526-018-1443-6.pdf
source_sha256: 34f3cd94e3b2d9d7
toc_source: outline
doc_brief: "On the analyticity of critical points of the Möbius energy — We prove that smooth critical points of the Möbius energy E parametrized by arc-length are analytic."
---
Let us recall certain properties of fractional Sobolev spaces that are useful throughout the
whole article. We assume some familiarity with the theory of weak derivatives and Fourier
analysis. For a detailed introduction to Sobolev spaces we may refer to [1,9,40].
Let n ∈N. We denote by | · | the real Euclidean norm |x| := √⟨x, x⟩Rn on Rn and by
| · |Cn the Euclidean norm |z|Cn := √⟨z, z⟩Cn on Cn.
In the sequel we work with closed curves on the periodic domain R/Z, i.e. we consider
curves f : R →Rn which are periodic with period 1, that means
f (x + 1) = f (x) ∀x ∈R.
For f ∈L2(R/Z, Cn) and k ∈Z the k-th Fourier coefﬁcient of f is deﬁned as
f (k) =
 1
0
f (x)e−2πikxdx
and the Fourier series of f in x ∈R/Z is given by 
k∈Z f (k)e2πikx.
The fractional Sobolev space of order s ≥0 (to be more precise: the Bessel potential
space of order s ≥0) is deﬁned by
Hs(R/Z, Cn) := { f ∈L2(R/Z, Cn) | ∥f ∥Hs := ∥f ∥Hs(R/Z,Cn) :=

( f , f )Hs < ∞},
equipped with the scalar product
( f , g)Hs := ( f , g)Hs(R/Z,Cn) :=
	
k∈Z
(1 + k2)s⟨f (k),g(k)⟩Cn.
We will use the embeddings Hs(R/Z, Cn) ⊆Ht(R/Z, Cn) for any s > t, s, t ≥0 [8,
Proposition 2.1, Corollary 2.3] as well as Hs(R/Z, Cn) ⊆C(R/Z, Cn) for any s > 1
2 [8,
Theorem 8.2], which implies that the Fourier series of f converges absolutely and uniformly
to f for any f ∈Hs(R/Z, C), s > 1
2.
It is well-known that for m ∈N0 the space Hm agrees with the classical Sobolev space
and the norm ∥f ∥W m :=

m
ν=0 ∥∂ν f ∥2
L2

 1
2 is equivalent to ∥· ∥Hm (cf. [37, Lemma 1.2]
or [1, 7.62]). Moreover, we note that for m ∈N there exists a positive constant Cm < ∞
such that
∥f g∥Hm ≤Cm∥f ∥Hm∥g∥Hm
(2.1)
On the analyticity of critical points of the Möbius energy
Page 5 of 28
16
for all f , g ∈Hm(R/Z, R) by [1, Theorem 4.39].
We will furthermore use the following simple consequence of the chain rule for Sobolev
functions.
Lemma 2.1 There exists a positive constant Cc < ∞only depending on d and e such that
∥g ◦f ∥H1 ≤Cc∥g∥C1(1 + ∥f ∥H1)
for all f ∈H1(R/Z, Rd), g ∈C1(Rd, Re) and e, d ∈N.
Proof This follows from
∥g ◦f ∥W 1 ≤∥g ◦f ∥L2 + ∥(g ◦f )·∥L2
≤∥g∥∞+ ∥˙g∥∞∥˙f ∥L2
≤∥g∥C1(1 + ∥f ∥W 1)
and by the equivalence of W 1- and H1-norm as stated above.
⊓⊔
