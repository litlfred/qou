---
doc_id: arxiv-1403.4021v2
doc_title: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS"
section_id: sec-013-62-a-genuine-extension-of-bmwn
section_title: "A genuine extension of BMWn"
section_number: 6.2
pages: 26-27
source_pdf: 1403.4021v2.pdf
source_sha256: 046d02411e0dc086
toc_source: outline
doc_brief: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS — We classify the Markov traces factoring through the Birman-Wenzl-Murakami (BMW) algebras."
---
n . Using the abelianization morphism Bn ↠Z we can
deﬁne a 3-dimensional Hn ⊗R S††-module by
si 7→


a
1
0
0
b
1
0
0
b−1


It is easily checked that R1 acts by 0 in this module, hence we get a 3-dimensional BMW ††
n -
module. We get that ei = a((si + s−1
i )/x −1) is mapped to


(ab−1)(−b+a)
b2+1
ab−1
b2+1
b
b2+1
0
0
0
0
0
0


while eisi+1ei −ei and eis−1
i+1ei −ei are both mapped to
2ab −b2 −1
(b2 + 1)2


(ab −1)(a −b)
ab −1
b
0
0
0
0
0
0


This proves that this module induces a Fn ⊗A S††-module, and therefore a Fn ⊗A S††
± -
module, which do not factorize through BMW ±
n . It follows that BMW ††
n and Fn are genuine
extensions of the Birman-Wenzl-Murakami algebra. We need to prove a similar result for
the specializations appearing in the previous section. However, for one of them the above
argument does not work, because it corresponds to a root of ab −b2 −1. Nevertheless, we
know by proposition 4.2 (iii) that BMW ††
n
is ﬁnitely generated as a S††-module. Because
of this, the dimension of every specialization is at least the dimension of BMW ††
n over the
ﬁeld of fractions of S†† (this classical fact follows for instance from Nakayama’s lemma, by
replacing S†† by its localization at the deﬁning ideal of the specialization). This proves the
following.
Proposition 6.4. For every morphism λ : S†† →C, BMW ††
n ⊗λ C and (Fn ⊗A S††) ⊗λ C
have dimension at least 1 + dim BMW +
n .
Corollary 6.5. For every morphism λ : S†† ,→C, the image of C inside (Fn ⊗A S††) ⊗λ C
is nonzero.
Corollary 6.6. The A-module Fn is free of rank 1 + dim BMW ±
n
Proof. Let us denote A± = Q[a, x, x−1]/(a ∓1) ≃Q[x, x−1].
By the natural A-module
decomposition A ≃A+ ⊕A−it is enough to prove that F ±
n = Fn ⊗A A± is a free A±-module
of rank 1+N with N = dim BMW ±
n . Now notice that BMW ±
n ⊗S± S††
± is actually deﬁned by
a presentation with coeﬃcients in A±, and that the corresponding A±-form is free of rank N
by [19]. Therefore, as in proposition 6.1 (ii), we get a surjective A±-morphisme F ±
n ↠AN
± by
mapping C to 0. Letting s± denote a section of this morphism, we get a surjective morphism
u± : A1+N
±
≃(A±C) ⊕AN
± →F ±
n by (λC, m) 7→λC + s±(m).
Letting K± denote the
quotient ﬁeld of A±, it follows that u± ⊗A± K± is surjective. But proposition 6.4 implies
that F ±
n ⊗A± K± has dimension 1 + N. Therefore the source and target of u± ⊗A± K± have
MARKOV TRACES ON THE BMW-ALGEBRAS
27
the same dimension hence u± ⊗K± is injective. Since the source of u± is a free module this
implies that u± is injective and this proves the claim.
□
Corollary 6.7. The natural algebra morphism Fn →Fn+1 is injective.
Proof. As before, using the notations of the previous proof, it is equivalent to show that
the natural maps F ±
n →F ±
n+1 are injective. This is true because the following diagram of
horizontal short exact sequences is commutative, and because its two extremal vertical arrows
are known to be injective.
0
/ A±C
/

F ±
n
/

BMW ±
n
/

0
0
/ A±C
/ F ±
n+1
/ BMW ±
n+1
/ 0
□
