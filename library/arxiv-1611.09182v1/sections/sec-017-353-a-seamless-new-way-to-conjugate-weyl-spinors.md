---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-017-353-a-seamless-new-way-to-conjugate-weyl-spinors
section_title: "A seamless new way to conjugate Weyl spinors"
section_number: 3.5.3
pages: 21-22
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
doc_brief: "Standard model physics from an algebra? — 57 sections: Abstract; Acknowledgements; Introduction"
---
In quantum ﬁeld theory textbooks, it is typically explained that a left handed Weyl spinor,
ΨL, can be conjugated so as to give a right-handed Weyl spinor. The procedure necessary
to do so, in the usual matrix-and-column-vector formalism, entails (1) complex conjugating
the left-handed spinor’s two components, and (2) multiplying this column vector by the
matrix ϵ =−iσy = ( 0−1
1 0 ),
[
ψ↑
L, ψ↓
L
]⊤
→ (1)→
[
ψ↑
L
∗
, ψ↓
L
∗]⊤
→ (2)→
[
−ψ↓
L
∗
, ψ↑
L
∗]⊤
. (3.16)
Notice what happens, though, if we write these Weyl spinors instead in terms of the
C⊗ H algebra:
Ψ∗
L =ψ↑
L
∗
ϵ↑↑
∗ +ψ↓
L
∗
ϵ↓↑
∗ =−ψ↓
L
∗
ϵ↑↓ +ψ↑
L
∗
ϵ↓↓. (3.17)
That is, we arrive at the exact same result using nothing more than the complex conjugate:
i↦→−i.
Now, in order to return back to the original left-handed Weyl spinor, in the usual
matrix-and-column-vector formalism, we must again (1) complex conjugate the spinor’s
components, but this time, (2)′ multiply by the new matrix−ϵ,
[
−ψ↓
L
∗
, ψ↑
L
∗]⊤
→ (1)→
[
−ψ↓
L, ψ↑
L
]⊤
→ (2)′→
[
ψ↑
L, ψ↓
L
]⊤
. (3.18)
In comparison, the same result is achieved in C⊗ H more simply by taking the complex
conjugate twice,
ΨL
∗∗ = ΨL. (3.19)
13
Readers should note that∗ : ΨL↦→ ΨR is a basis-independent statement in our formal-
ism. It holds, regardless of whether Ψ L is written in the Weyl, Dirac, or Majorana basis of
the Dirac algebra. To the best of this author’s knowledge, [34] was the ﬁrst instance where
this more streamlined method of conjugating spinors has been proposed.
In considering these two formalisms, one comes to notice that no ϵ-type object was
needed in the C⊗ H case. Somehow, the complex conjugate i↦→−i automatically encoded
the information given by ϵ. It is natural to ask, then, why ϵ is necessary in the matrix-
and-column-vector formalism.
After comparing equations (3.16) and (3.17), one sees that ϵ was what was needed so
as to account for the complex conjugation of basis vectors. In the C⊗ H formalism, we
naturally take the complex conjugate of both the coeﬃcients, and the basis vectors. On
the other hand, there is no notion of complex conjugating basis vectors in the matrix-
and-column-vector formalism. The matrix ϵ needs to be introduced so as to account for
this. The conjugation of Weyl spinors, as explained here, then exposes a naturalness to
the purely algebraic formalism.
