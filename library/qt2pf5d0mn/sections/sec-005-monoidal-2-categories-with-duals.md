---
doc_id: qt2pf5d0mn
doc_title: "UC Santa Barbara"
section_id: sec-005-monoidal-2-categories-with-duals
section_title: "Monoidal 2-categories with Duals"
section_number: null
pages: 36-42
source_pdf: qt2pf5d0mn.pdf
source_sha256: 4c8581c3b46398e3
toc_source: outline
doc_brief: "UC Santa Barbara — 19 sections: Front matter; Abstract; Introduction"
---
A
Figure 2.12: The twist θA
2. θA∗= (θA)∗;
3. θ1 = I;
4.
(θA)
h
= θ A
h .
2.3
Monoidal 2-categories with Duals
In this section we show that a monoidal 2-category with certain extra structures can
be constructed from a G-crossed braided spherical fusion category (G-BSFC) introduced
in the previous section. The readers can skip this section if they are only interested in
the (3 + 1)-TQFT out of a G-BSFC. Here we do not intend to list the full deﬁnition of
monoidal 2-categories as it would be of too much distraction. Rather we only give the
core structures and refer the readers to [30][31][32] for detailed discussions.
A (strict) 2-category has 0-morphisms (objects), 1-morphisms, and 2-morphisms. For
any two objects A, B, there is a set of 1-morphisms Hom1(A, B) and for any two 1-
morphisms f, g with same the domain and codomain, there is a set of 2-morphisms
Hom2(f, g).
Usually, 0-morphisms will be denoted by capital letters A, B, C, etc., 1-
morphisms by lowercase letters f, g, h, etc., and 2-morphisms by Greek letters α, β, γ,
etc. We use regular arrows for 1-morphisms and double arrows for 2-morphisms, namely,
f : A −→B, α : f =⇒g. Both 1- and 2-morphisms can be composed. Only in this
27
Section 2.3
Monoidal 2-categories with Duals
section, we will use the convention that composition of morphisms are to be read from
left to right. Explicitly,
• Composition of 1-morphisms:
◦: Hom1(A, B) × Hom1(B, C) −→Hom1(A, C)
(f, g)
7−→
f ◦g
• ‘Vertical’ composition of 2-morphisms: for f, g, h ∈Hom1(A, B),
∗: Hom2(f, g) × Hom2(g, h) −→Hom2(f, h)
(α, β)
7−→
α ∗β
• ‘Horizontal’ composition of 2-morphisms: for f, g ∈Hom1(A, B), f ′, g′ ∈Hom1(B, C),
◦: Hom2(f, g) × Hom2(f, g′) −→Hom2(f ◦f ′, g ◦g′)
(α, α′)
7−→
α ◦α′
These compositions satisfy various associativity axioms. (In the non-strict case, the
associativity axioms need to be replaced by certain Pentagon Identity similar to that
in the deﬁnition of monoidal categories.) In fact, monoidal categories are in one-to-one
correspondence with 2-categories with only one object. Explicitly, if C is a monoidal
category, deﬁne a 2-category ˜C with a single object as follows:
Denote the object by ∗(or anything else). Then 1-morphisms between ∗and ∗are
objects of C and 2-morphisms of ˜C are 1-morphisms of C. Composition of 1-morphisms
and horizontal composition of 2-morphisms in ˜C are given by tensor product of objects
28
Section 2.3
Monoidal 2-categories with Duals
and tensor product of morphisms in C, respectively. Vertical composition is just the
regular composition of morphisms in C.
Conversely, given ˜C, a 2-category with one object ∗, by reversing the rules in the
above paragraph one can deﬁne a monoidal category.
Thus, a 2-category is in some sense a generalization of monoidal categories. And
similar to the case of monoidal categories, the coherence theorem for 2-categories shows
that every 2-category is equivalent to a strict 2-category in an appropriate sense.
A (semi-strict) monoidal 2-category with duals is a (strict) 2-category C with the
following structures:
• For A, B ∈C0, there is an object A ⊗B ∈C0;
• For f ∈Hom1(A, B), C ∈C0, there are 1-morphisms f ⊗C ∈Hom1(A ⊗C, B ⊗C)
and C ⊗f ∈Hom1(C ⊗A, C ⊗B);
• For α ∈Hom2(f, g), C ∈C0, there are 2-morphisms α ⊗C ∈Hom2(f ⊗C, g ⊗C)
and C ⊗α ∈Hom2(C ⊗f, C ⊗g);
• For f ∈Hom1(A, B), g ∈Hom1(C, D), there is a 2-morphism, called the tensorator,
⊗f,g : (A ⊗g) ◦(f ⊗D) =⇒(f ⊗C) ◦(B ⊗g);
• There is a unit object 1 ∈C0;
• For f ∈Hom1(A, B), there is a 1-morphism f ∗∈Hom1(B, A), a 2-morphism
if : IA =⇒f ◦f ∗, and a 2-morphism ef : f ∗◦f =⇒IB called the dual, the unit,
and the counit of f, respectively;
• For A ∈C0, there is an object A∗∈C0, a 1-morphism iA : 1 −→A ⊗A∗and
a 1-morphism eA : A∗⊗A −→1 called the dual, the unit and the counit of A,
29
Section 2.3
Monoidal 2-categories with Duals
respectively, and a 2-morphism TA : (iA⊗A)◦(A⊗eA) =⇒IA called the triangulator
of A.
Again these structures need satisfy certain compatible axioms. See [31].
Now we show that from a G-BSFC we can construct a monoidal 2-category with duals
and certain extra structures as well. Let C×
G be a G-BSFC and we denote the morphism
space Hom(A, B) by HomC×
G(A, B) to avoid confusion. Deﬁne a 2-category ˜C as follows.
• 0-morphisms ˜C0 := G.
• 1-morphisms Hom1(g1, g2) := C0
¯g1g2 for g1, g2 ∈G; namely, the 1-morphisms from g1
to g2 are objects in C¯g1g2, where ¯g1 is the inverse of g1.
• 2-morphisms Hom2(A, B) := HomC×
G(A, B) for A, B ∈Hom1(g1, g2) = C0
¯g1g2; name-
ly, the 2-morphisms from A to B are the regular morphisms from A to B in C×
G.
Note that here and only in this example, the notations for each level of morphisms
are diﬀerent from those speciﬁed at the beginning of the section. Namely, in ˜C,
we will use g1, g′
1, · · · , for objects, capital letters A, B, · · · , for 1-morphisms, and
Greek letters α, β, · · · , for 2-morphisms.
• For A ∈Hom1(g1, g2), B ∈Hom1(g2, g3), the composition A ◦B := A ⊗B ∈
Hom1(g1, g3).
• For α ∈Hom2(A, B), β ∈Hom2(B, C), the vertical composition α ∗β := α ◦β ∈
Hom2(A, C); namely, vertical composition in ˜C corresponds to regular composition
in C×
G.
• For α ∈Hom2(A, B), α′ ∈Hom2(A′, B′), where A, B ∈Hom1(g1, g2), A′, B′ ∈
Hom1(g2, g3), the horizontal composition α ◦α′ := α ⊗α′ ∈Hom2(A ⊗A′, B ⊗B′).
30
Section 2.3
Monoidal 2-categories with Duals
One can check this deﬁnes a 2-category. Now we introduce the monoidal structure and
duals on ˜C. To avoid confusion, the tensor product in ˜C will be denoted by the symbol ⊠
instead of ⊗, while in C×
G still by ⊗. We list below explicit constructions corresponding
to the items in the deﬁnition of monoidal 2-categories with duals.
• g1 ⊠g2 := g1g2.
• For A ∈Hom1(g1, g2), g ∈G, A ⊠g := A
¯g
∈Hom1(g1g, g2g) and g ⊠A := A ∈
Hom1(gg1, gg2). Note that as a set, Hom1(g1, g2) = Hom1(gg1, gg2).
• For α ∈Hom2(A, B), g ∈G, α ⊠g := α
¯g
∈Hom2(A ⊠g, B ⊠g) = Hom2( A
¯g , B
¯g
)
and g ⊠α := α ∈Hom2(g ⊠A, g ⊠B) = Hom2(A, B).
• For A ∈Hom1(g1, g2), A′ ∈Hom1(g′
1, g′
2), note that (g1 ⊠A′) ◦(A ⊠g′
2) = A′ ⊗
A
g′
2
and (A ⊠g′
1) ◦(g2 ⊠A′) =
A
g′
1
⊗A′. Deﬁne the tensorator ⊠A,A′ := c
A′,
A
g′
2 .
• The unit 1 := e is the unit of G.
• For A ∈Hom1(g1, g2), A∗is the same as the dual of A when viewed as an object of
C×
G; The iA and eA are deﬁned as bA and dA, respectively.
• For g ∈G, g∗:= ¯g, and ig, eg are deﬁned as the unit 1 of C×
G, and Tg is the identity
map I1.
It is direct, though a little tedious, to check ˜C is indeed a monoidal 2-category with
duals.
Below we show that actually there are more structures in ˜C. However, these structures
do not make it into a ‘spherical 2-category ’ deﬁned in [32].
Given A ∈Hom1(g1, g2), deﬁne
A
#
:=
A
g2
, A# :=
A
g1
∈Hom(¯g2, ¯g1) as follows [32].
¯g2
¯g1 ⊠g1 ⊠¯g2
¯g1 ⊠g2 ⊠¯g2
¯g1
=
¯g1⊠A⊠¯g2
=
31
Section 2.3
Monoidal 2-categories with Duals
¯g2
¯g2 ⊠g1 ⊠¯g1
¯g2 ⊠g2 ⊠¯g1
¯g1
=
¯g2⊠A⊠¯g1
=
Therefore,
A
#
:=
A
g2
, A# :=
A
g1
. Similarly, for α ∈Hom2(A, B), A, B ∈Hom1(g1, g2),
deﬁne
α
#
:=
α
g2
∈Hom2( A
# , B
#
), α# :=
α
g1
∈Hom1(A#, B#). Note that there is the
isomorphism:
θ−1
A# :
A
#
−→A#
According to Deﬁnition 2.4 in [32], the isomorphisms θ−1
A# make ˜C a pivotal 2-category.
According to Deﬁnition 2.5 in [32], for any g ∈G, A ∈Hom1(g, g) = Ce, the left trace
TrL(A) := g ⊠A = A and the right trace TrR(A) := A ⊠g =
A
¯g .
According to
Deﬁnition 2.8 in [32], for the category to be spherical, there should be a 2-isomorphism
σA : TrL(A) =⇒TrR(A) which satisﬁes certain conditions as speciﬁed there. However, in
a G-BSFC, this implies that for any A ∈Ce, g ∈G, there is an isomorphism σA : A −→
A
¯g , which in general does not exist.
As a summary, out of a G-BSFC we have constructed a pivotal 2-category, which in
general violates Deﬁnition 2.8 in [32], and thus is not necessarily a spherical 2-category.
32
Chapter 3
