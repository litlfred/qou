---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-002-a-reminder-on-2-categories
section_title: "A reminder on 2-categories."
section_number: null
pages: 7-10
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasiz ing the importance of a pairing which generalizes Mukai’s pairi ng on the cohomology of K3"
---
We will review the notion of a 2-category at the same time as in troducing
the notation we will be using. Recall that a 2-category consi sts of three
levels of structure: objects; 1-morphisms between objects ; and 2-morphisms
between 1-morphisms. It is worth mentioning a few examples t o bear in
mind during the following exposition.
1. The ﬁrst example is the 2-category C at of categories, functors and
natural transformations.
2. The second example is rather a family of examples. There is a corre-
spondence between 2-categories with one object ⋆ and monoidal cat-
egories. For any monoidal category the objects and morphism s give
respectively the 1-morphisms and 2-morphisms of the corres ponding
2-category.
3. The third example is the 2-category A lg with algebras over some ﬁxed
commutative ring as its objects, with the set of A-B-bimodules as its
1-morphisms from A to B, where composition is given by tensoring
over the intermediate algebra, and with bimodule morphisms as its
2-morphisms.
There are various ways of notating 2-categories: the most co mmon way
is to use arrow diagrams , however the most convenient way for the ideas
in this paper is via string diagrams which are Poincar´ e dual to the arrow
diagrams. In this subsection we will draw arrow diagrams on t he left and
string diagrams on the right to aid the reader in the use of str ing diagrams.
Recall the idea of a 2-category. For any pair of objects X and Y there is
a collection of morphisms 1-Hom(X, Y); if Φ ∈ 1-Hom(X, Y) is a 1-morphism
then it is drawn as below.
Φ 
Y X X
Φ 
Y
These 1-dimensional pictures will only appear as the source and target
of 2-morphism, i.e., the top and bottom of the 2-dimensional pictures we
will be using. In general 1-morphisms will be denoted by thei r identity
2-morphisms, see below.
If Φ, Φ′ ∈ 1-Hom(X, Y) are parallel 1-morphisms — meaning simply that
they have the same source and target — then there is a set of 2-m orphisms
2-Hom(Φ, Φ′) from Φ to Φ ′. If α ∈ 2-Hom(Φ, Φ′) is a 2-morphism then it
is drawn as below.
α 
Y X
Φ 
Φ ′
α 
Φ 
Φ ′
Y X
7
At this point make the very important observation that diagr ams are read
from right to left and from bottom to top.
There is a vertical composition of 2-morphisms so that if α : Φ⇒ Φ ′ and
α ′ : Φ ′⇒ Φ ′′ are 2-morphisms then the vertical composite α ′ ◦v α : Φ⇒ Φ ′′
is deﬁned and is denoted as below.
Φ ′′
Y X
Φ 
α 
α ′
≡ α ′ ◦v α Y X
Φ 
Φ ′′
α 
Y X
Φ ′′
Φ 
Φ ′
α ′
≡ α ′ ◦v α Y
Φ ′′
Φ 
X
This vertical composition is strictly associative so that (α ′′ ◦v α ′) ◦v α =
α ′′ ◦v (α ′ ◦v α) whenever the three 2-morphisms are composable. Moreover,
there is an identity 2-morphism IdΦ : Φ⇒ Φ for every 1-morphism Φ so
that α ◦v IdΦ = α = IdΦ ′ ◦v α for every 2-morphism α : Φ⇒ Φ ′. This means
that for every pair of objects X and Y, the 1-morphisms between them are
the objects of a category Hom(X, Y), with the 2-morphisms forming the
morphisms. In the string notation the identity 2-morphisms are usually just
drawn as straight lines.
Φ 
Y X
Φ 
IdΦ
Φ 
Y X
There is also a composition for 1-morphisms, so if Φ : X→ Y and Ψ : Y→
Z are 1-morphisms then the composite Ψ◦Φ : X→ Z is deﬁned and is denoted
as below.
Ψ Φ 
Y XZ
≡
Z X
Ψ ◦ Φ Φ 
Y XZ
Ψ ≡
XZ
Ψ ◦ Φ 
Again, these pictures will only appear at the top and bottom o f 2-morphisms.
This composition of 1-morphisms is not required to be strict ly associative,
but it is required to be associative up to a coherent 2-isomorphism. This
means that for every composable triple Θ, Ψ and Φ of 1-morphisms there
is a speciﬁed 2-isomorphism (Θ ◦ Ψ) ◦ Φ ∼=⇒ Θ ◦ (Ψ ◦ Φ) and these 2-
isomorphisms have to satisfy the so-called pentagon cohere ncy condition
which ensures that although Θ ◦ Ψ ◦ Φ is ambiguous, it can be taken to mean
either (Θ ◦ Ψ) ◦ Φ or Θ ◦ (Ψ ◦ Φ) without confusion. The up-shot of this is
that parentheses are unnecessary in the notation.
Each object X also comes with an identity 1-morphism IdX, but again,
in general, one does not have equality of IdY ◦ Φ, Φ and Φ ◦ IdX, but rather
the identity 1-morphisms come with coherent 2-isomorphism s IdY ◦ Φ ∼⇒ Φ,
and Φ ◦ IdX
∼⇒ Φ. Again this means that in practice the identities can
be neglected in the notation: so although we could denote the identity 1-
morphism with, say, a dotted line, we choose not to. This is il lustrated
8
below.
X
IdX
X ≡ X
A strict 2-category is one in which the coherency 2-isomorphisms for
associativity and identities are themselves all identitie s. So the 2-category
C at of categories, functors and natural transformations is a st rict 2-category.
The last piece of structure that a 2-category has is the horizontal compo-
sition of 2-morphisms. If Φ, Φ′ : X→ Y and Ψ, Ψ′ : Y→ Z are 1-morphisms,
and α : Φ⇒ Φ ′ and β : Ψ⇒ Ψ ′ are 2-morphisms, then β◦hα : Ψ◦Φ⇒ Ψ ′◦Φ ′
is deﬁned, and is notated as below.
Ψ ′ Φ ′
β α 
Ψ Φ 
XZ Y ≡ Z X
Ψ ◦ Φ 
β ◦h α 
Ψ ′ ◦ Φ ′
Ψ 
Z Xα β
Φ 
Φ ′
Y
Ψ ′
≡
Ψ ′
Z X
Φ 
Φ ′Y
Y
β ◦h α 
Ψ 
The horizontal and vertical composition are required to obe y the interchange
law.
(β ′ ◦v β) ◦h (α ′ ◦v α) = ( β ′ ◦h α ′) ◦v (β ◦h α).
This means that the following diagrams are unambiguous.
Y
Φ 
Xα 
α ′
Φ ′′
Ψ 
Z β
β′
Ψ ′′
Ψ ′′
Φ ′
Φ ′′
Φ 
Z
β′
β
α ′
α 
XY
Ψ 
Ψ ′
It also means that 2-morphisms can be ‘slid past’ each other i n the following
sense.
YZ
α 
X
Φ 
Ψ ′
β
Ψ 
Φ ′
=
Ψ ′
Z X
Ψ 
β
α 
Φ ′
Y
Φ 
From now on, string diagrams will be drawn without the grey bo rders,
and labels will be omitted if they are clear from the context.
1.2 The 2-category V ar.
The 2-category V ar, of spaces and integral kernels, is deﬁned as follows.
The objects are spaces, as deﬁned in the introduction, and th e hom-category
HomV ar(X, Y) from a space X to a space Y is the derived category D(X × Y),
which is to be thought of as the category of integral kernels f rom X to
Y. Explicitly, this means that the 1-morphisms in V ar from X to Y are
objects of D(X × Y) and the 2-morphisms from Φ to Φ ′ are morphisms
9
in HomD(X×Y)(Φ, Φ′), with vertical composition of 2-morphisms just being
usual composition in the derived category.
Composition of 1-morphisms in V ar is deﬁned using the convolution of
integral kernels: if Φ ∈ D(X × Y) and Ψ ∈ D(Y × Z) are 1-morphisms then
deﬁne the convolution Ψ ◦ Φ ∈ D(X × Z) by
Φ ◦ Ψ := πXZ,∗(π∗
YZΨ ⊗ π∗
XYΦ),
where πXZ, πXY and πYZ are the projections from X×Y×Z to the appropriate
factors. The horizontal composition of 2-morphisms is simi larly deﬁned.
Finally, the identity 1-morphism IdX: X→ X is given by O∆ ∈ D(X × X),
the structure sheaf of the diagonal in X × X.
The above 2-category is really what is at the heart of the stud y of integral
transforms, and it is entirely analogous to A lg, the 2-category of algebras
described above. For example, the Hochschild cohomology gr oups of a space
X arise as the second homotopy groups of the 2-category V ar, at X:
HH•(X) := Ext•
X×X(O∆ , O∆ ) ∼= Hom•
D (X×X)(O∆ , O∆ )
=: 2-HomV ar(IdX, IdX).
There is a 2-functor from V ar to C at which encodes integral transforms:
this 2-functor sends each space X to its derived category D(X), sends each
kernel Φ : X→ Y to the corresponding integral transform Φ : D(X)→ D(Y),
and sends each map of kernels to the appropriate natural tran sformation.
Many of the statements about integral transforms have bette r formulations
in the language of the 2-category V ar.
