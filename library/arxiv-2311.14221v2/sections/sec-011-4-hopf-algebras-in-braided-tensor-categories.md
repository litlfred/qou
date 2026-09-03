---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-011-4-hopf-algebras-in-braided-tensor-categories
section_title: "Hopf algebras in braided tensor categories"
section_number: 4
pages: 17-18
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B → C is an exact"
---
4.1. Hopf algebras in braided tensor categories. Let us brieﬂy recall
the notion of Hopf algebras in braided tensor categories, an d how their
corepresentation categories are again tensor categories. For more details,
the reader is referred to [ 19], [ 20], [ 26] and references therein.
A braided tensor category is a pair (C,σ ) whereC is a tensor category and
σV,W : V⊗W → W⊗V is a braiding, that is, a family of natural isomor-
phisms satisfying
σV,U ⊗W = (id U⊗σV,W )(σV,U⊗id W ),
σV ⊗U,W = (σV,W⊗id U )(id V⊗σU,W ).(4.1)
Remark 4.1. Note that in the above axioms we are assuming that C is a
strict tensor category.
The braiding fulﬁlls the braid relation, whence the name. We illustrate
this identity in terms of string diagrams, which we read bott om to top
U V W
W V U
=
U V W
W V U
Deﬁnition 4.2. A bialgebra inC is a collection (H,m,u, ∆ ,ε ), where (H,m,u )
is an algebra, ( H, ∆ ,ε ) is a coalgebra, and ∆ ,ε are algebra morphisms. I.e.
∆ ◦m = (m⊗m)(id⊗σH,H⊗id )(∆⊗∆) ,(4.2)
∆ ◦u = (u⊗u) (4.3)
ε◦m = (ε⊗ε) (4.4)
ε◦u = id 1(4.5)
We illustrate the ﬁrst identity
H
H
H
H
=
H
H
H
H
18 LENTNER AND MOMBELLI
If H is a bialgebra, then the space Hom C(H,H ) has a a convolution
product with unit given by u◦ε. If the identity id H has an inverse S
under the convolution product, then H is a Hopf algebra, and S is called the
antipode. The next Theorem is well known, see for example [ 19].
Theorem 4.3. If H is a Hopf algebra in a braided tensor category C, then
the category of left H-comodules HC is a tensor category. Moreover, if C
is a ﬁnite tensor category, then HC is also a ﬁnite tensor category, and the
forgetful functor f : HC→C is an exact faithful monoidal functor. □
The tensor product of two left H-comodules is given as follows: If ( V,ρ V ),
(W,ρ W ) are objects in HC, then the tensor product V⊗W inC has a left
H-comodule structure given by
(4.6) ρV ⊗W = (m⊗id V ⊗W )(id H⊗σV,H⊗id W )(ρV⊗ρW ).
H
V W
V W
If (V,ρ V )∈ HC then ∗V∈ HC. The coaction is given by
(4.7) ρ∗V =
(
(S⊗id )σ∗V,H⊗evV
)(
id ∗V⊗ρV⊗id ∗V
)(
coevV⊗id ∗V
)
.
The coaction of the right dual V ∗ is deﬁned similarly.
For any V ∈C we can endow V with a trivial H-comodule structure,
given by
ρt
V :V→H⊗V, ρ t
V =u⊗id V.
4.2. Y etter-Drinfeld modules. Let H be a ﬁnite dimensional Hopf al-
gebra in vect k. Then we shall denote by H
HYD the category of ﬁnite-
