---
doc_id: s00526-018-1443-6
doc_title: "Calc. Var. (2019) 58:16 Calculus of Variations On the analyticity of critical points of the Möbius energy Simon Blatt 1 · Nicole Vorderobermeier 1 © The Author(s) 2018"
section_id: sec-005-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 3-5
source_pdf: s00526-018-1443-6.pdf
source_sha256: 34f3cd94e3b2d9d7
doc_brief: "Calc. Var. (2019) 58:16 Calculus of Variations On the analyticity of critical points of the Möbius energy Simon Blatt 1 · Nicole Vorderobermeier 1 © The Author(s) 2018 — We prove that smooth critical"
---
mula. In Sect. 3 we decompose the ﬁrst variation of the Möbius energy into the orthogonal
projection of a main part Q and two remaining parts R1 and R2 of lower order. The main part
123
16 Page 4 of 28 S. Blatt, N. Vorderobermeier
Q and its derivatives get estimated in Sect. 4. Since the orthogonal projection of Q appears
in the ﬁrst variation of the Möbius energy, we estimate the tangential part of Q using new
estimates for a type of bilinear Hilbert transform in Sect. 5. In Sects. 5 and 6 we will cut
off the singularities of the singular integrals involved and derive uniform estimates. More
precisely, in Sect. 6 we rewrite the orthogonal projection of the truncated remaining terms
so that they may be expressed by integrals over analytic functions. In Sect. 7 we will realize
that since the estimates do not depend on the cutoff parameter, the same estimates hold for
the orthogonal projections of Q, R1 and R2 and its derivatives. In the end we will use the
estimates to prove Theorem 1.2 using the method of majorants.
2 Preliminaries
2.1 Fractional Sobolev spaces
Let us recall certain properties of fractional Sobolev spaces that are useful throughout the
whole article. We assume some familiarity with the theory of weak derivatives and Fourier
analysis. For a detailed introduction to Sobolev spaces we may refer to [ 1,9,40].
Let n ∈ N. We denote by |·| the real Euclidean norm |x|: = √⟨x, x⟩Rn on Rn and by
|·| Cn the Euclidean norm |z|Cn := √⟨z, z⟩Cn on Cn .
In the sequel we work with closed curves on the periodic domain R/Z, i.e. we consider
curves f : R → Rn which are periodic with period 1, that means
f (x + 1) = f (x) ∀x ∈ R.
For f ∈ L2(R/Z, Cn) and k ∈ Z the k-th F ourier coefﬁcient of f is deﬁned as
ˆf (k) =
∫1
0
f (x)e−2πikx dx
and the F ourier series of f in x ∈ R/Z is given by ∑
k∈Z ˆf (k)e2πikx .
The fractional Sobolev space of order s ≥ 0 (to be more precise: the Bessel potential
space of order s ≥ 0) is deﬁned by
H s(R/Z, Cn) := { f ∈ L2(R/Z, Cn) |‖ f ‖H s := ‖f ‖H s(R/Z,Cn) :=
√
( f , f )H s < ∞},
equipped with the scalar product
( f , g)H s := ( f , g)H s(R/Z,Cn) :=
∑
k∈Z
(1 + k2)s⟨ˆf (k),ˆg(k)⟩Cn .
We will use the embeddings H s(R/Z, Cn) ⊆ H t(R/Z, Cn) for any s > t, s, t ≥ 0[ 8,
Proposition 2.1, Corollary 2.3] as well as H s(R/Z, Cn) ⊆ C(R/Z, Cn) for any s > 1
2 [8,
Theorem 8.2], which implies that the Fourier series of f converges absolutely and uniformly
to f for any f ∈ H s(R/Z, C), s > 1
2 .
It is well-known that for m ∈ N0 the space H m agrees with the classical Sobolev space
and the norm ‖f ‖W m :=
(∑ m
ν=0 ‖∂ν f ‖2
L2
) 1
2
is equivalent to ‖·‖ H m (cf. [37, Lemma 1.2]
or [ 1, 7.62]). Moreover, we note that for m ∈ N there exists a positive constant Cm < ∞
such that
‖fg ‖H m ≤ Cm‖f ‖H m ‖g‖H m (2.1)
123
On the analyticity of critical points of the Möbius energy Page 5 of 28 16
for all f , g ∈ H m(R/Z, R) by [1, Theorem 4.39].
We will furthermore use the following simple consequence of the chain rule for Sobolev
functions.
Lemma 2.1 There exists a positive constant C c < ∞ only depending on d and e such that
‖g ◦ f ‖H 1 ≤ Cc‖g‖C1 (1 +‖ f ‖H 1 )
for all f ∈ H 1(R/Z, Rd),g ∈ C1(Rd, Re) and e, d ∈ N.
Proof This follows from
‖g ◦ f ‖W 1 ≤‖ g ◦ f ‖L2 +‖(g ◦ f )·‖L2
≤‖ g‖∞ +‖˙g‖∞‖ ˙f ‖L2
≤‖ g‖C1 (1 +‖ f ‖W 1 )
and by the equivalence of W 1-a n d H 1-norm as stated above. ⊓⊔
