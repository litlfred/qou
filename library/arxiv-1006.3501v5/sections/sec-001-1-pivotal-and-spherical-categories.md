---
doc_id: arxiv-1006.3501v5
doc_title: "On two approaches to 3-dimensional TQFTs"
section_id: sec-001-1-pivotal-and-spherical-categories
section_title: "Pivotal and spherical categories"
section_number: 1
pages: 3-5
source_pdf: 1006.3501v5.pdf
source_sha256: e939aec50387ce2d
toc_source: outline
doc_brief: "On two approaches to 3-dimensional TQFTs — W e prove that|M |C = τZ(C)(M ) for any closed oriented 3-manifold M and for any spherical fusion category C of non-zero dimension."
---
We review several classes of monoidal categories needed in the seq uel.
1.1. Pivotal categories ( [Mal]). By a pivotal (or sovereign) category, we mean a
strict monoidal category C with unit object 1 such that to each object X∈ Ob(C)
there are associated a dual object X ∗∈ Ob(C) and four morphisms
evX :X ∗⊗X→ 1, coevX : 1→X⊗X ∗,
~evX :X⊗X ∗→ 1, ~coevX : 1→X ∗⊗X,
satisfying the following conditions:
(a) For every X∈ Ob(C), the pair (ev X, coevX ) is a left duality for X, i.e.,
(idX⊗ evX )(coevX⊗ idX ) = id X and (ev X⊗ idX ∗)(idX ∗⊗ coevX ) = id X ∗ ;
(b) For every X∈ Ob(C), the pair ( ~evX, ~coevX ) is a right duality for X, i.e.,
(~evX⊗ idX )(idX⊗ ~coevX ) = id X and (id X ∗⊗ ~evX )(~coevX⊗ idX ∗ ) = id X ∗ ;
(c) For every morphism f : X→Y inC, the left dual
f ∗ = (ev Y⊗ idX ∗)(idY ∗⊗f⊗ idX ∗ )(idY ∗⊗ coevX ) :Y ∗→X ∗
is equal to the right dual
f ∗ = (id X ∗⊗ ~evY )(idX ∗⊗f⊗ idY ∗)(~coevX⊗ idY ∗ ) :Y ∗→X ∗;
(d) For all X,Y ∈ Ob(C), the morphisms X ∗⊗Y ∗→ (Y⊗X)∗ deﬁned as
(evX⊗ id(Y ⊗X)∗)(idX ∗⊗ evY⊗ idX⊗(Y ⊗X)∗ )(idX ∗⊗Y ∗⊗ coevY ⊗X )
and as
(id(Y ⊗X)∗⊗ ~evY )(id(Y ⊗X)∗⊗Y⊗ ~evX⊗ idY ∗)(~coevY ⊗X⊗ idX ∗⊗Y ∗ )
4 V. TURAEV AND A. VIRELIZIER
are equal (these morphisms are called monoidal constraints);
(e) ev 1 = ~ev1 : 1∗→ 1 (or, equivalently, coev 1 = ~coev1 : 1→ 1∗).
Note that the morphisms ev 1 and coev 1 (respectively, ~ev1 and ~coev1) are mutu-
ally inverse isomorphisms. The monoidal constraints in (d) also are iso morphisms.
By abuse of notation, we will suppress these isomorphisms in the for mulas. For
example, we will write ( f⊗g)∗ =g∗⊗f ∗ for morphisms f,g inC.
1.2. T races and dimensions. For an endomorphismf of an object X of a pivotal
categoryC, one deﬁnes the left and right traces trl(f ), trr(f )∈ EndC(1) by
trl(f ) = ev X (idX ∗⊗f )~coevX and tr r(f ) = ~evX (f⊗ idX ∗ )coevX.
Both traces are symmetric: tr l(gh) = tr l(hg) and tr r(gh) = tr r(hg) for any mor-
phisms g : X→ Y and h : Y → X inC. Also tr l(f ) = tr r(f ∗) = tr l(f ∗∗) for any
endomorphism f of an object (and similarly with l,r exchanged). If
(2) α⊗ idX = id X⊗α for all α∈ EndC(1) and X∈ Ob(C),
then tr l, trr are ⊗-multiplicative: tr l(f⊗ g) = tr l(f ) trl(g) and tr r(f⊗ g) =
trr(f ) trr(g) for all endomorphisms f,g of objects of C.
The left and right dimensions of X∈ Ob(C) are deﬁned by dim l(X) = tr l(idX )
and dim r(X) = tr r(idX ). Clearly, dim l(X) = dim r(X ∗) = dim l(X ∗∗) (and sim-
ilarly with l,r exchanged). Note that isomorphic objects have the same dimen-
sions and dim l(1) = dim r(1) = id 1. If C satisﬁes (2), then left and right dimen-
sions are ⊗-multiplicative: dim l(X⊗Y ) = dim l(X) diml(Y ) and dim r(X⊗Y ) =
dimr(X) dimr(Y ) for any X,Y ∈ Ob(C).
1.3. Penrose graphical calculus. We represent morphisms in a category C by
plane diagrams to be read from the bottom to the top. The diagrams are made of
oriented arcs colored by objects of C and of boxes colored by morphisms of C. The
arcs connect the boxes and have no mutual intersections or self- intersections. The
identity id X of X∈ Ob(C), a morphism f : X→ Y , and the composition of two
morphisms f :X→Y and g :Y →Z are represented as follows:
idX =
PSfrag replacements
X
Y
f
g
Z
, f =
PSfrag replacements
X
Y
fg
Z
, and gf =
PSfrag replacements
X
Y
f
g
Z
.
IfC is monoidal, then the monoidal product of two morphisms f : X → Y and
g :U→V is represented by juxtaposition:
f⊗g =
PSfrag replacements
X
f
Y
PSfrag replacements
X
f
Y
U
g
V
.
In a pivotal category, if an arc colored by X is oriented upwards, then the corre-
sponding object in the source/target of morphisms is X ∗. For example, id X ∗ and
a morphism f : X ∗⊗Y→U⊗V ∗⊗W may be depicted as:
idX ∗ =PSfrag replacements
X
=
PSfrag replacements
X
X ∗
and f =
PSfrag replacements
X
X ∗
X
f
Y
U V W
.
The duality morphisms are depicted as follows:
evX =PSfrag replacements
X , coev X =PSfrag replacements
X , ~evX =PSfrag replacements
X , ~coevX =
PSfrag replacements
X
X
.
The dual of a morphism f : X→Y and the traces of a morphism g : X→X can
be depicted as follows:
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 5
f ∗ =
PSfrag replacements
X
f
Yg
=
PSfrag replacements
X
f
Yg
and tr l(g) =
PSfrag replacements
X
f
Y g , tr r(g) =
PSfrag replacements
X
f
Y g .
IfC is pivotal, then the morphisms represented by the diagrams are inva riant under
isotopies of the diagrams in the plane keeping ﬁxed the bottom and to p endpoints.
1.4. Linear and spherical categories. A monoidal k-category is a monoidal cat-
egoryC such that its hom-sets are (left) k-modules, the composition and monoidal
product of morphisms are k-bilinear, and End C(1) is a free k-module of rank one.
Then the map k→ EndC(1),k ↦→k id1 is a k-algebra isomorphism. It is used to
identify End C(1) = k.
A pivotal k-category satisﬁes (2). Therefore the traces tr l, trr and the dimensions
diml, dimr in such a category are ⊗-multiplicative. Clearly, tr l, trr are k-linear.
A spherical category is a pivotal category whose left and right traces are equal,
i.e., tr l(g) = tr r(g) for every endomorphism g of an object. Then tr l(g) and tr r(g)
are denoted tr(g) and called the trace of g. Similarly, the left and right dimensions
of an object X are denoted dim(X) and called the dimension of X.
For spherical categories, the corresponding Penrose graphical calculus has the
following property: the morphisms represented by diagrams are inv ariant under
isotopies of diagrams in the 2-sphere S2 = R2∪{∞} , i.e., are preserved under
isotopies pushing arcs of the diagrams across ∞. For example, the diagrams above
representing trl(g) and tr r(g) are related by such an isotopy. The condition tr l(g) =
trr(g) for all g is therefore necessary (and in fact suﬃcient) to ensure this prop erty.
1.5. Remark. Our deﬁnition of a pivotal category is equivalent to the standard
deﬁnition given in terms of pivotal structures, see [Mal]. A pivotal structure on a
monoidal categoryC with left duality{(X ∗, ev, coev)}X∈Ob(C) is a monoidal natural
isomorphism ψ ={ψX : X→ X ∗∗}X∈Ob(C), i.e., ψX⊗Y = ψX⊗ψY and ψ1 = id 1
(up to the monoidal constraints). A pivotal category C obtains a pivotal structure by
ψX = (~evX⊗ idX ∗∗)(idX⊗ coevX ∗ ) for X∈ Ob(C). Conversely, a pivotal structure
makesC pivotal by ~evX = ev X ∗ (ψX⊗ idX ∗ ) and ~coevX = (id X ∗⊗ψ−1
X )coevX ∗.
