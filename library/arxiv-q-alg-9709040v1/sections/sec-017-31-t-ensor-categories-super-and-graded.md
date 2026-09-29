---
doc_id: arxiv-q-alg-9709040v1
doc_title: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I"
section_id: sec-017-31-t-ensor-categories-super-and-graded
section_title: "T ensor categories Super and Graded"
section_number: 3.1
pages: 7-7
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
doc_brief: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I — 83 sections: Front matter; Introduction; Deformation quantization"
---
Here we make a comment about the terminology. This comment lo oks a bit pedantic, but it could help
in the struggle with signs in formulas.
The main idea of algebraic geometry is to replace spaces by co mmutative associative rings (at least
locally). One can further generalize this considering comm utative associative algebras in general tensor
categories (see [De]). In this way one can imitate many const ructions from algebra and diﬀerential geometry.
The fundamental example is supermathematics, i.e. mathema tics in the tensor category Super k of super
vector spaces over a ﬁeld k of characteristic zero (see Chapter 3 in [M]). The category Super k is the category
of Z/2Z-graded vector spaces over k (representations of the group Z/2Z) endowed with the standard tensor
product, with the standard associativity functor, and with a modiﬁed commutativity functor (the Koszul
rule of signs). We denote by Π the usual functor Super k−→Super k changing the parity. It is given on
objects by the formula Π V =V⊗ k0|1. In the sequel we will consider the standard tensor category Vect k of
vector spaces over k as the subcategory of Super k consisting of pure even spaces.
The basic tensor category which appears everywhere in topol ogy and homological algebra is a full
subcategory of the tensor category of Z-graded super vector spaces. Objects of this category are in ﬁnite
sumsE =⊕n∈ZE (n) such thatE (n) is pure even for even n, and pure odd for odd n. We will slightly abuse the
language calling this category also the category of graded v ector spaces, and denote it simply by Gradedk.
We denote by E n the usual k-vector space underlying the graded component E (n). The super vector space
obtained if we forget about Z-grading onE∈ Objects(Gradedk) is ⨁
n∈Z Π n(E n).
Analogously, we will speak about graded manifolds. They are deﬁned as supermanifolds endowed with
Z-grading on the sheaf of functions obeying the same conditio ns on the parity as above.
The shift functor [1] : Gradedk−→Gradedk (acting from the right) is deﬁned as the tensor product with
graded space k[1] where k[1]−1≃ k, k[1]⁄=−1 = 0. Its powers are denoted by [ n], n∈ Z. Thus, for graded
spaceE we have
E =
⨁
n∈Z
E n[−n] .
Almost all results in the present paper formulated for grade d manifolds, graded Lie algebras etc., hold
also for supermanifolds, super Lie algebras etc.
