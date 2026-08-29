---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY"
section_id: sec-028-453-recovering-the-hecke-algebra
section_title: "Recovering the Hecke algebra"
section_number: 4.5.3
pages: 27-29
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
doc_brief: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
If we want to produce an algebra isomorphic to H starting with the category
of Soergel bimodules and not just “the positive part”, we just need to add
formally to NB(S3) the element−⟨M⟩ for every Soergel bimodule M . This
element will satisfy the equation−⟨M⟩ +⟨M⟩ = 0. In this manner we obtain a
honest algebra overZ[v,v−1], isomorphic toH. One formal way of doing this
is with the following general deﬁnition.
Deﬁnition 3 LetA be an additive category. The split Grothendieck group
ofA denoted by ⟨A⟩ is the free abelian group over the objects modulo the
27
relationsM =N +P whenever we haveM∼=N⊕P. Given an objectA∈A ,
let⟨A⟩ denote its class in⟨A⟩.
In the case of⟨B(S3)⟩, this group can be endowed with a structure ofZ[v,v−1]-
algebra, as we have seen (addition is direct sum, product is tensor product,
etc).
Soergel’s categoriﬁcation Theorem 4.6 IfW isS3 we have
• The set W×Z is in bijection with the set of indecomposable Soergel
bimodules via the map
(w,m )↦→Bw(m)
• The map
⟨B(S3)⟩→H (S3)
⟨Bw⟩↦→ bw
⟨R(1)⟩↦→ v
is an isomorphism ofZ[v,v−1]-algebras.
Proof The ﬁrst part has already been proved. The second one also, modulo
the remark that before we used the notation ⟨N⟩ =⟨M⟩ if N and M are iso-
morphic, and now we are using it for two elements equal in the Grothendieck
group and this could be confusing notation. In fact, due to the Krull-Schmidt
property explained in the proof of 4.5 these two notations mean the same
thing.
The morphisms between Bott-Samelson bimodules (i.e. bimodules of the form
BsBr··· Bt fors,r,...,t ∈S ) in principle could be quite complicated, or even
atrocious, but we are, oh so very lucky. Two miracles happen. Firstly the Hom
spaces are free asR-modules. This is highly non-trivial.
The second miracle is that there is a combinatorial set (deﬁned by the author
in [Li2]) in the Hom spaces, called “Light leaves” that is a basis of this free
Hom space. In the next section we will introduce Soergel bimodules for any
Coxeter group and we will explain the construction of light leaves before we
can calculate the indecomposable Soergel bimodules for the examples B, C and
D in Section 7.
28
