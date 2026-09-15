---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-009-34-the-trace-and-categories-of-complexes
section_title: "The trace and categories of complexes"
section_number: 3.4
pages: 16-17
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a high er categorical level."
---
interesting variant of Euler characteristic. Let Kom( C) be the category of bounded complexes over C.
Recall that the objects of Kom( C) are complexes
A• : ... − →Ai
di
− →Ai−1
di−1
− →...
d2
− →A1
d1
− →A0 − →0,
where Ai ∈ Ob(C) and di ∈ C (Ai,A i−1), and the morphisms are chain maps.
The “traced” Euler characteristic of a complex A• is deﬁned by
χtr(A•) =
∑
i
(−1)i[1Ai] ∈ Tr(C),
where [1 x] is the class of 1 x in Tr(C) for any x ∈ Ob(C). More generally, to any chain endomorphism
F :A• →A• we can associate its “traced” Lefschetz number
τ (F ) =
∑
i
(−1)i[Fi].
Then χtr(A•) = τ (1A• ).
Lemma 3.3. For any A• ∈ Kom(C) and homotopic chain endomorphisms F,G : A• → A• we have
τ (F ) = τ (G). Furthermore, χtr is homotopy invariant.
Exercise 12. Prove this lemma using the deﬁnition of the chain homotopy, i .e. F −G =dh +hd.
An interesting application of the traced Euler characteristic was giv en by Bar-Natan [4]. There he
deﬁned a quotient Cob / of the /CI [1/2]-linear category of 2-dimensional cobordisms, and associated a
complex in Kom(Cob ⊕
/ ) to any tangle, which he called a Khovanov bracket. He showed that isotopies
of the tangle do not change the homotopy type of this complex. The following theorem of Bar-Natan
shows that the traced Euler characteristic can be used as decate goriﬁcation map in a categoriﬁcation
of the Jones polynomial.
Theorem 3.4 (Theorem 6 [4]) . The traced Euler characteristic of the Khovanov bracket of a tan gle
in Bar-Natan’s category is equal to the Jones polynomial.
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR 17
