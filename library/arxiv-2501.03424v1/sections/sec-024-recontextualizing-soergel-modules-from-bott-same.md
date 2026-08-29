---
doc_id: arxiv-2501.03424v1
doc_title: "Soergel bimodules and Kazhdan-Lusztig polynomials ethan eugene wynner"
section_id: sec-024-recontextualizing-soergel-modules-from-bott-same
section_title: "Recontextualizing Soergel modules from Bott-Samelson modules"
section_number: null
pages: 16-17
source_pdf: 2501.03424v1.pdf
source_sha256: 53e00a30fd850a5b
doc_brief: "Soergel bimodules and Kazhdan-Lusztig polynomials ethan eugene wynner — This paper presents an exposition of Soergel bimodules, the categ oriﬁcation of Hecke alge- bras, and their applications to"
---
We now take an arbitrary Coxeter system ( W, S) and a W -representation h over some ﬁeld k.
Let R = Sym( h∗) with deg( h∗) = 2 . Consider the subcategories SBim(h, W ) of Soergel bimodules
and BSBim(h, W ) of Bott-Samelson bimodules. Recall that Soergel modules are obt ained via these
respective bimodules. We have to be a little tricky here and view k as a graded R-module with all
positive degree polynomials acting by zero.
16
4.4.1 Deﬁnition
Let w = ( s1, . . . , sm) be a reduced expression for w. The Bott-Samelson module BS (w) is the
graded right R-module
BS (w) = k⊗R BS (w) = k⊗R Bs1⊗R···⊗ R Bsm
≃ k⊗R R⊗Rs1 R⊗Rs2···⊗ Rsm R(m).
Now we can see more clearly how we get our Soergel modules. Explicitly , they’re any graded
right R-modules isomorphic to a ﬁnite direct sum of shifts of direct summand s of Bott-Samelson
modules. Our subcategory SBim(h, W ) from earlier is in fact a full subcategory of gmod- R. We
can now consider the functor
k⊗R (−) : R-gmod-R→ gmod-R,
which is an additive functor sending BS (w)↦→BS(w). Thus it restricts to
k⊗R (−) : SBim(h, W )−→ SBim(h, W ).
This gives us the idea that Soergel modules can equivalently be thoug ht of as graded R-modules
that come from direct summands of k⊗R B, where B is a Soergel bimodule. To make use of this
functor, we give the following
