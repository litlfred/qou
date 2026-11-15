---
doc_id: arxiv-q-alg-9709040v1
doc_title: "Deformation quantization of Poisson manifolds"
section_id: sec-011-3-deformation-theory-via-diﬀerential-graded-lie
section_title: "Deformation theory via diﬀerential graded Lie algebras"
section_number: 3
pages: 7-7
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
toc_source: inferred
doc_brief: "Deformation quantization of Poisson manifolds — 75 sections: Front matter; Plans; Star-products"
---
3.1. Tensor categories Super and Graded
Here we make a comment about the terminology. This comment looks a bit pedantic, but it could help
in the struggle with signs in formulas.
The main idea of algebraic geometry is to replace spaces by commutative associative rings (at least
locally).
One can further generalize this considering commutative associative algebras in general tensor
categories (see [De]). In this way one can imitate many constructions from algebra and diﬀerential geometry.
The fundamental example is supermathematics, i.e. mathematics in the tensor category Superk of super
vector spaces over a ﬁeld k of characteristic zero (see Chapter 3 in [M]). The category Superk is the category
of Z/2Z-graded vector spaces over k (representations of the group Z/2Z) endowed with the standard tensor
product, with the standard associativity functor, and with a modiﬁed commutativity functor (the Koszul
rule of signs). We denote by Π the usual functor Superk−→Superk changing the parity. It is given on
objects by the formula ΠV = V ⊗k0|1. In the sequel we will consider the standard tensor category V ectk of
vector spaces over k as the subcategory of Superk consisting of pure even spaces.
The basic tensor category which appears everywhere in topology and homological algebra is a full
subcategory of the tensor category of Z-graded super vector spaces. Objects of this category are inﬁnite
sums E = ⊕n∈ZE(n) such that E(n) is pure even for even n, and pure odd for odd n. We will slightly abuse the
language calling this category also the category of graded vector spaces, and denote it simply by Gradedk.
We denote by En the usual k-vector space underlying the graded component E(n). The super vector space
obtained if we forget about Z-grading on E ∈Objects(Gradedk) is L
n∈Z Πn(En).
Analogously, we will speak about graded manifolds. They are deﬁned as supermanifolds endowed with
Z-grading on the sheaf of functions obeying the same conditions on the parity as above.
The shift functor [1] : Gradedk−→Gradedk (acting from the right) is deﬁned as the tensor product with
graded space k[1] where k[1]−1 ≃k, k[1]̸=−1 = 0. Its powers are denoted by [n], n ∈Z. Thus, for graded
space E we have
E =
M
n∈Z
En[−n] .
Almost all results in the present paper formulated for graded manifolds, graded Lie algebras etc., hold
also for supermanifolds, super Lie algebras etc.
