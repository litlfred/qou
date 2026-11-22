---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-031-451-some-definitions
section_title: "Some definitions"
section_number: 4.5.1
pages: 31-32
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
toc_source: outline
doc_brief: "Standard model physics from an algebra? — 77 sections: Front matter; Abstract; Acknowledgements"
---
Some deﬁnitions
Let V be the vector space over a ﬁeld F. A quadratic form, Q, is a map Q : V →F such
that ∀v, w ∈V and λ ∈F,
Q(λv) = λ2Q(v)
(4.4)
and such that the map B : V × V →F,
B : (v, w) 7→Q(v + w) −Q(v) −Q(w)
(4.5)
is linear in both v and w. This V, together with its quadratic form, is called a quadratic
vector space.
23
We will be especially interested in the quadratic vector space given by V and Q, where
V is the n-dimensional vector space spanned by the generating elements ej of deﬁnition
(4.1). Here, the quadratic form will be given by Q(v) = {v, v}, and the corresponding
bilinear form is then B(v, w) = 2{v, w}. Note that V here is only the generating subspace
of our Cliﬀord algebra, it does not represent the entire Cliﬀord algebra.
A subspace U of V is said to be totally isotropic if B(αi, αj) = 0 ∀αi, αj ∈U. In
the following construction, we will be interested in maximal totally isotropic subspaces of
V , which are deﬁned to be totally isotropic subspaces of V with maximal dimension. As
explained in [1], for Cliﬀord algebras over C with n even, the dimension of any maximal
totally isotropic subspace will be n/2. In fact, we ﬁnd that the generating space splits into
exactly two maximal totally isotropic subspaces, each with the dimension n/2.
It is interesting to note that our maximal totally isotropic subspace, U of V, generates
a Grassmann algebra, seeing as how B(αi, αj) = 2{αi, αj} = 0 ∀αi, αj ∈U. This fact
merits notice, especially in consideration of recent work by L´aszl´o, [49].
