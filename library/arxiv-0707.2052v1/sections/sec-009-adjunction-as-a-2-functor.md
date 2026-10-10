---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-009-adjunction-as-a-2-functor
section_title: "Adjunction as a 2-functor."
section_number: null
pages: 17-17
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasiz ing the importance of a pairing which generalizes Mukai’s pairi ng on the cohomology of K3"
---
As shown in Section 3.2, in the 2-category V ar every 1-morphism, that is
every kernel, Φ : X→ Y has a right adjoint ΣX ◦ Φ∨ . This can be extended
to a ‘right adjunction 2-functor’ τR: V arcoop→ V ar, where V arcoop means
the contra-opposite 2-category of V ar, which is the 2-category with the
same collections of objects, morphisms and 2-morphisms, bu t in which the
direction of the morphisms and the 2-morphisms are reversed .
Before deﬁning τR, however, it is perhaps useful to think of the more
familiar situation of a one-object 2-category with right ad joints, i.e., a
monoidal category with (right) duals. So if C is a monoidal category in
which each object a has a dual a∨ with evaluation map ǫa: a∨ ⊗ a→ 1 and
coevaluation map ηa: 1→ a ⊗ a∨ , then for any morphism f : a→ b deﬁne
f∨ : b∨ → a∨ to be the composite:
b∨ Id⊗η
− − −→ b∨ ⊗ a ⊗ a∨ Id⊗f⊗Id− − − − −→ b∨ ⊗ b ⊗ a∨ ǫ ⊗Id− − −→ a∨ .
This gives rise to a functor (−) ∨ : C op→ C .
Now return to the case of interest and deﬁne τR: V arcoop → V ar as
follows. On spaces deﬁne τR(X) := X. On a kernel Φ : X→ Y deﬁne τR(Φ) :=
ΣX ◦ Φ∨ . Finally, on morphisms of kernels deﬁne it as illustrated:
τR


Φ 
α 
Φ ′

 :=
Φ ′
α 
Φ 
.
It is a nice exercise for the reader to check that this is a 2-fu nctor.
Clearly a left adjoint 2-functor τL: V arcoop→ V ar can be similarly cre-
ated by deﬁning it on a kernel Φ : X→ Y by τL(Φ) := Φ∨ ◦ ΣY and by
deﬁning it on morphisms of kernels by
τL


Φ 
α 
Φ ′

 :=
Φ 
α 
Φ ′
.
