---
doc_id: 104171-owr-2018-52
doc_title: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018)"
section_id: sec-005-1-galleries
section_title: "Galleries"
section_number: 1
pages: 27-28
source_pdf: 10.4171-owr-2018-52.pdf
source_sha256: b33ed36eaa470877
doc_brief: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018) — The workshop brought together experts investigating algeb raic Lie theory from the geometric and categorical"
---
Jacinta Torres
Let g be a complex, simple Lie algebra, and L(λ) a simple module over the complex
numbers of highest weight λ∈X +. Consider the set
Γ ={γ : [0, 1]−→XR :γ(1)∈X, γ(0) = 0}
of piecewise linear paths starting at the origin and ending at an integr al weight. In
[2], Littelmann deﬁned a ﬁnite set of paths P(γλ)⊂ Γ depending on a single path
γλ∈ Γ with endpoint γλ(1) = λ and contained in the dominant Weyl chamber,
for which the character of L(λ) is a generating function in the following sense:
ch(L(λ)) =
∑
γ∈P (γλ)
xγ(1).(1)
The setP(γλ) is constructed by applying certain root operators fα, one for every
simple root α, to γλ. Together with their partial inverses eα, they endow the set
P(γλ) with the structure of a crystal isomorphic to B(λ).
Question. Given a path γ∈ Γ, how can one decide if it belongs to P (γλ) for
some γλ contained in the dominant Weyl chamber?
In this note, we give necessary conditions for galleries of alcoves , that is, certain
sequences of alcoves in the corresponding aﬃne Coxeter complex ( which has the
same underlying space XR), with the ﬁrst alcove containing the origin and a choice
of integral weight contained in the last one. Our ongoing work gener alizes work of
Gaussent-Littelmann in [1], where they introduce so-called Lakshmib ai-Seshadri
galleries, for which the formula (1) makes sense and still holds after replacingη(1)
for a path η by the endpoint e(γ) of a gallery γ.
1. Galleries
A gallery of alcoves , or just a gallery, is a sequence
γ := (v0,a 0,p 1,··· ,pr,ar,vr)(2)
of alcoves and panels (i.e. codimension one faces of alcoves) ai−1⊃ pi⊂ ai for
i∈ [1,r ]. In addition we require a choice of a ﬁnal vertex vr∈X, an integral weight
contained in the last alcove, and ask that the ﬁrst alcove a0 contains the origin
v0 = 0. The integral weight vr is the endpoint e(γ) of the gallery γ. By labelling
the codimension one faces of the fundamental alcove with colours I ={i0,...,i n},
where n is the rank of the Lie algebra g, we obtain a labelling of every panel.
The label of a panel p will be denoted by t(p) and referred to as the type of the
panel. The type of a vertex v is the set t(v) ={t(p) : v∈p} of types of the panels
containingv. The type of γ is the sequence of types
t(γ) := (t(p1),...,t (pr))
3108 Oberwolfach Report 52/2018
of its panels and endpoint. Given a dominant integral weight λ∈ X +, we will
denote by
γλ := (v′
0,a ′
0,p ′
1,··· ,p ′
r,a ′
r,v ′
r)(3)
a gallery with v′
r =λ and such that each one of its alcoves and panels is contained
in the dominant Weyl chamber. We will call such a gallery dominant.
