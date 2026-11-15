---
doc_id: arxiv-2501.03424v1
doc_title: "Soergel bimodules and Kazhdan-Lusztig polynomials"
section_id: sec-040-definition
section_title: "Definition"
section_number: null
pages: 17-17
source_pdf: 2501.03424v1.pdf
source_sha256: 53e00a30fd850a5b
toc_source: outline
doc_brief: "Soergel bimodules and Kazhdan-Lusztig polynomials — This paper presents an exposition of Soergel bimodules, the categoriﬁcation of Hecke alge- bras, and their applications to various topics in"
---
Deﬁnition
Let w = (s1, . . . , sm) be a reduced expression for w. The Bott-Samelson module BS(w) is the
graded right R-module
BS(w) = k ⊗R BS(w) = k ⊗R Bs1 ⊗R · · · ⊗R Bsm
≃k ⊗R R ⊗Rs1 R ⊗Rs2 · · · ⊗Rsm R(m).
Now we can see more clearly how we get our Soergel modules.
Explicitly, they’re any graded
right R-modules isomorphic to a ﬁnite direct sum of shifts of direct summands of Bott-Samelson
modules. Our subcategory SBim(h, W) from earlier is in fact a full subcategory of gmod-R. We
can now consider the functor
k ⊗R (−) : R-gmod-R →gmod-R,
which is an additive functor sending BS(w) 7→BS(w). Thus it restricts to
k ⊗R (−) : SBim(h, W) −→SBim(h, W).
This gives us the idea that Soergel modules can equivalently be thought of as graded R-modules
that come from direct summands of k ⊗R B, where B is a Soergel bimodule. To make use of this
functor, we give the following
