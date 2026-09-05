---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-021-44-convolution-of-the-g-slice
section_title: "Convolution of the G-slice"
section_number: 4.4
pages: 22-23
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
B2 (X2,W )G signiﬁesB2-equivariant matrix
factorizations from MF B2 (X2,W ) that G-invariant. This description becomes simpler when we introduce a
smaller space X ◦
2 := g×G× b2 and the map p◦ : X2→ X ◦
2 deﬁned by
p◦(X,g 1,Y 1,g 2,Y 2) = (Ad −1
g1 (X),g 12,Y 1, Adg12 (Y2)++).
This map is G-equivariant with the trivial G-action on the target. The space X ◦
2 is a slice to G-action on
X2.
22
If we deﬁne the function W on X ◦
2 by
W (X,g,Y 1,Y 2) = Tr(X(Y1− Adg(Y2)))
Then the pull back ( p◦)∗ : MF sc
B2 (X ◦
2,W )→ MFB2(X2,W )G provides an equivalence of categories.
Indeed, we have an G×B2-equivariant isomorphism Ψ G : X2→G× X ◦
2 :
Ψ G(X,g 1,Y 1,g 2,Y 2) = (g1,p ◦(X,g 1,Y 1,g 2,Y 2)).
The group G-acts on the ﬁrst factor of G× X ◦
2 by left multiplication and acts trivially on the second factor
hence the pull-back functor pr∗
2 : MF sc
B2(G× X ◦
2,W )G → MFsc
B2 (X ◦
2,W ) is an isomorphism. Thus the
equivalence follows because p◦ = Ψ G◦pr2. Thus we can work with the category MF sc
B2 (X ◦
2,W ) instead of
MFsc
B2(X2,W )G.
Deﬁne X ◦
3 := g×G2× n3. The convolution for the objects of MF sc
B2(X ◦
2 ,W ) is deﬁned with modiﬁed
maps π◦
ij : X ◦
3 → X ◦
2 :
π◦
12(X,g 12,g 23,Y 1,Y 2,Y 3) = (X,g 12,Y 1,Y 2),
π◦
23(X,g 12,g 23,Y 1,Y 2,Y 3) = (Ad −1
g12 (X),g 23,Y 2,Y 3),
π◦
13(X,g 12,g 23,Y 1,Y 2,Y 3) = (Ad −1
g13 (X),g 13,Y 1,Y 3),
where g13 =g12g23. The convolution is then deﬁned by
G⋆F =π◦
13∗(CEn(2) (π◦,∗
12 (F )⊗Bπ◦,∗
23 (G)))T (2)
.
Obviously, the pull-back map p∗
◦ is an isomorphism of the convolution algebras.
