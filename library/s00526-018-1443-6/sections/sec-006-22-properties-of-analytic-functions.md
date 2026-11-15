---
doc_id: s00526-018-1443-6
doc_title: "On the analyticity of critical points of the Möbius energy"
section_id: sec-006-22-properties-of-analytic-functions
section_title: "Properties of analytic functions"
section_number: 2.2
pages: 5-6
source_pdf: s00526-018-1443-6.pdf
source_sha256: 34f3cd94e3b2d9d7
toc_source: outline
doc_brief: "On the analyticity of critical points of the Möbius energy — We prove that smooth critical points of the Möbius energy E parametrized by arc-length are analytic."
---
Let us recall some elementary facts about analytic functions. More on the topic can be found
for example in [9, Chapter 6.4] and [11, Chapter 1, D]. Let n, m ∈N and 	 ⊆Rm be an
open set throughout this section.
We will use the following well-known characterization of analytic functions, which can
be deduced from [24, Proposition 2.2.10] by a standard covering argument.
Theorem 2.2 Let f ∈C∞(	, Rn). Then f is analytic on 	 if and only if for every compact
set K ⊂	 there are constants rK > 0, CK < ∞such that
∥∂α f ∥L∞(K) ≤CK
|α|!
r|α|
K
holds for every multiindex α ∈Nm
0 .
Combining this with the embedding of the classical Sobolev space W k = W k,2 into C0
for k ∈N with k > m
2 we get the following.
Corollary 2.3 Let f ∈C∞(	, Rn). Then f is analytic on R/Z if and only if for every compact
set K ⊂	 there are constants rK > 0, CK < ∞such that
∥∂α f ∥W 1(K) ≤CK
|α|!
r|α|
K
holds for every multiindex α ∈Nm
0 .
From the equivalence of the W 1- and the H1-norm on R/Z we hence get
Corollary 2.4 Let f ∈C∞(R/Z, Rn). Then f is analytic on 	 if and only if there are
constants r > 0, C < ∞such that
∥∂k f ∥H1 ≤C k!
rk
holds for all k ∈N0.
16
Page 6 of 28
S. Blatt, N. Vorderobermeier
Let us mention a special case of the theorem of Cauchy–Kovalevskaya, which is originally
an existence and uniqueness theorem for analytic nonlinear partial differential equations
associated with Cauchy initial value problems. Proofs based on the method of majorants
which we will also use to prove the main result of this article can be found in [11, Chapter
1, D] and [9, Chapter 4.6.3, Theorem 2].
Theorem 2.5 (Cauchy–Kovalevskaya—ODE case) Let ε > 0. Suppose g : Rn →Rn is real
analytic around 0, and f ∈C∞(] −ε, ε[, Rn), f (x) = ( f1(x), . . . , fn(x)), be a solution of
the initial value problem

˙f (x) = g( f (x)) for x ∈] −ε, ε[
f (0) = 0.
Then f is real analytic around 0.
