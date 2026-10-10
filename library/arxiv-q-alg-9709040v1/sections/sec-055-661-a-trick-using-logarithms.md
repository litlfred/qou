---
doc_id: arxiv-q-alg-9709040v1
doc_title: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I"
section_id: sec-055-661-a-trick-using-logarithms
section_title: "A trick using logarithms"
section_number: 6.6.1
pages: 29-30
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
doc_brief: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I — 83 sections: Front matter; Introduction; Deformation quantization"
---
Theorem. LetX be a complex algebraic variety of dimension N≥ 1, and Z1,...,Z 2N be rational functions
onX, not equal identically to zero. Let U be any Zariski open subset of X such that functions Zα are deﬁned
and non-vanishing on U , and U consists of smooth points. Then the integral
∫
U(C)
∧2N
α =1d(ArgZ α )
is absolutely convergent, and equal to zero.
This result seems to be new, although the main trick used in th e proof is well-known. A. Goncharov
told me that he also came to the same result in his study of mixe d Tate motives.
Proof: First of all, we claim that the diﬀerential form ∧2N
α =1dArg(Zα ) on U (C) coincides with the form
∧2N
α =1dLog|Zα| (this is the trick).
We can replace dArg(Zα ) by the diﬀerence of a holomorphic an anti-holomorphic form
1
2i
(
d(LogZ α )−d(LogZ α )
)
.
Thus, the form which we integrate over U (C) is a sum of products of holomorphic and of anti-holomorphic
forms. The summand corresponding to a product of a non-equal number of holomorphic and of anti-
holomorphic forms, vanishes identically because U (C) is a complex manifold. The conclusion is that the
number of anti-holomorphic factors in non-vanishing summa nds is the same for all of them, it coincides
with the complex dimension N of U (C). The same products of holomorphic and of anti-holomorphic forms
survive in the product
2N⋀
α =1
dLog|Zα| =
2N⋀
α =1
1
2
(
d(LogZ α ) +d(LogZ α )
)
.
Let us choose a compactiﬁcation U of U such that U\U is a divisor with normal crossings. If φ is a
smooth diﬀerential form on U (C) such that coeﬃcients of φ are locally integrable on U (C), then we denote
byI(φ) corresponding diﬀerential form on U (C) with coeﬃcients in the space of generalized functions.
29
Lemma. Let ω be a form on U (C) which is a linear combination of products of functions Log|Zα| and of
1-forms dLog|Zα| where Zα ∈O×(U ) are regular invertible functions on U . Then coeﬃcients of ω and of
dω are locally L1 functions on U(C). Moreover, I(dω) = d(I(ω)). Also, the integral
∫
U(C)
ω is absolutely
convergent and equal to the integral
∫
U(C)
I(ω).
The lemma is an elementary exercise in generalized function s, after passing to local coordinates on
U (C). We leave details of the proof to the reader. Also, the state ment of the lemma remains true without
the condition that U\U is a divisor with normal crossings. Q.E.D.
The vanishing of the integral in the theorem is clear now by th e Stokes formula:
∫
U(C)
2N⋀
α =1
dArg (Zα ) =
∫
U(C)
2N⋀
α =1
dLog|Zα| =
∫
U(C)
I
(
d
(
Log|Z1|
2N⋀
α =2
dLog|Zα|
))
=
=
∫
U(C)
d
(
I
(
Log|Z1|
2N⋀
α =2
dLog|Zα|
))
= 0 . Q.E.D.
