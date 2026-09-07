---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-053-67-the-equivalence-to-bimodules-in-this-section
section_title: "The equivalence to bimodules. In this section we assume that h is a Soergel"
section_number: 6.7
pages: 69-69
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
realization over a ﬁeld k. In this section we prove that our diagrammatic category is
equivalent to Soergel bimodules.
By Corollary 6.27 the map H → [D] : H s ↦→[Bs] is a homomorphism. By taking
the graded ranks of Hom spaces in D we obtain a pairing on [D] which induces a
semi-linear pairing (−, −)D on H by pull-back. It is obvious from the diagrammatic
description of D thatBs is self-biadjoint in D, so H s is self-biadjoint in this pairing.
It follows that (−, −)D is determined by the trace εD : H → Z[v±1] : h ↦→(h, 1)D.
Because the degree of any light leaves map is given by the defe ct of the correspond-
ing subexpression, it follows from Proposition 6.12 and Cor ollary 2.11 thatεD agrees
with the standard trace on objects of the form H w for all expressions w. As these
elements generate H we conclude thatε andεD, and hence (−, −)D and the standard
form (−, −), agree.
In section 5.3 we constructed a monoidal functor F : D → BSBim. It induces a
monoidal functor on the idempotent completions F : Kar(D) → SBim.
Theorem 6.28. Under the above assumptions F : Kar(D) → SBim is an equivalence of
monoidal categories.
Proof. Because idempotent completion preserves equivalences, it is enough to show
that F : D → BSBim is an equivalence. Clearly this functor is essentially s urjective,
so it is enough to show that it is fully-faithful. It is a theor em due to Libedinsky
[Lib08] that images under F of the dots, trivalent vertices and 2mst-valent vertices
generate all moprhisms between Bott-Samelson bimodules. I t follows that F is full.
Now by the above discussion and the fact that our realization is a Soergel realiza-
tion, the graded dimensions of the homomorphism spaces in D and BSBim conin-
cide. We conclude that F induces an isomorphism on Hom spaces, being a surjection
between graded vector spaces of the same (ﬁnite) dimension i n each graded compo-
nent. Hence F is fully-faithful. □
Remark 6.29. One can avoid the appeal to Libedinsky’s result as follows. B y ad-
junction, it is enough to prove that the images of dots, triva lent vertices and 2mst-
valent vertices generate Hom(Bw,R ) for any expression w. Now a ﬁxed choice of
light leaves maps LLw,e is obviously mapped to a composition of such maps, and
is mapped to a linearly independent subset of Hom(Bw,R ) by the same localisation
argument as in the proof of Corollary 6.8, this time carrried out in the localized cate-
gory of Soergel bimodules. By comparing the degrees of LLw,e and the graded rank
of Hom(Bw,R ) one concludes that LLw,e spans Hom(Bw,R ) as a graded R-module.
Hence the result. (This is basically an adaption of Libedins ky’s argument.)
