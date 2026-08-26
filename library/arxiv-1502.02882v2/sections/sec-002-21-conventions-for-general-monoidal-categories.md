---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams Bruce Bartlett"
section_id: sec-002-21-conventions-for-general-monoidal-categories
section_title: "Conventions for general monoidal categories"
section_number: 2.1
pages: 4-5
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
doc_brief: "Fusion categories via string diagrams Bruce Bartlett — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
The string diagram calculus for a monoidal category C is well-known (see [26]
or [3, Chap. 4] for an overview). Each diagram refers to a certain morphism in
C. Our diagrams go from top to bottom, so that a morphism f :A→B⊗C is
drawn as
.
In these pictures there is no explicit parenthesis scheme on the input and output
tensor products. Thus it is often supposed that one needs a a strict monoidal
category in order to make this calculus well-deﬁned. In fact, this is not so
— the calculus makes perfect sense when reasoning about equations between
morphisms, which is all we will ever need. For instance, supposef :A→A′⊗E,
g :B⊗C→D⊗C′,h :E⊗D→B′,k :A⊗(B⊗C)→F⊗C′,l :F→A′⊗B′,
and consider the following equation:
=
How are we to interpret this? This equation should be regarded as an inﬁnite
number of equations, one for each ﬁxed parenthesis scheme (this may include
insertions of the unit object 1 of the monoidal category) of the source and
target objects, which are taken to be the same on both sides of the equation. For
instance, ((1⊗A)⊗(B⊗1))⊗C is a possible choice of parenthesis scheme for the
source object in the above equation. For each such choice of parenthesis schemes,
one should insert an appropriate sequence of associators and unit isomorphisms
in order to make each side well-typed. Coherence for monoidal categories [17]
guarantees that the evaluation of the resultant morphism is independent of this
choice. Each equation implies all the others (see [3, Chap. 4]).
A monoidal category C is called right rigid if for each object V there exists
an object V∗ which can be equipped with unit and counit maps η : 1→V∗⊗V ,
ϵ :V⊗V∗→ 1 such that the rigidity equations hold:
=
 ,
 =
 (2)
4
Note that we have added orientations to the strands in (2), this is simply a visual
aid. The monoidal category C is called left rigid if for each objectV there exists
an object∗V which can be equipped with unit and counit mapsn : 1→V⊗∗V ,
e :∗V⊗V → 1 satisfying the horizontally-reversed versions of (2). We say that
C is rigid if it is both right rigid and left rigid. Our approach is to avoid making
ﬁxed initial choices of duals for each object, to keep constructions as canonical
as possible (thus we do not refer to a right dual functor ∗ : C→ Cop).
Formally, the invariance of the evaluation of string diagrams under diﬀeo-
morphisms of the plane can be expressed as follows. We imagine each diagram
as living in an outer disk D, with strands labelled by objects of the category,
and couponsCi (drawn as discs or square regions) labelled by morphisms, which
go from the tensor product of the objects labelling the strands in the northern
hemisphere of the coupon to the tensor product of the objects labelling the
strands in the southern hemisphere of the coupon. We deﬁne a rigid isotopy of
such a diagram to be a smooth path of diﬀeomorphisms φt :D→D, t∈ [0, 1]
such thatφ0 is the identity,φt is the identity on the boundary of D for allt and
such that φt restricted to each coupon Ci is a translation for all t.
The following theorem is well-known and combines coherence for monoidal
categories, rigidity, and the interchange law.
Theorem 2.1 (see eg. [26]) . The evaluation of a string diagram taking labels
in a rigid monoidal category is invariant under diﬀeomorphisms which are rigid
isotopic to the identity.
Remark 2.2. In a companion paper, motivated by [15], we will express the
diﬀeomorphism invariance for string diagrams taking labels in a fusion category
in the language of spin structures.
