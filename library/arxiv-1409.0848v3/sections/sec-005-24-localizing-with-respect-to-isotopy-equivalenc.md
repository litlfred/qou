---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-005-24-localizing-with-respect-to-isotopy-equivalenc
section_title: "Localizing with respect to isotopy equivalences"
section_number: 2.4
pages: 23-26
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homol ogy, or topological chiral homology, at the generality of stratiﬁed spaces with tangen tial"
---
Here we explain that the∞-category Disk(B)/X , which appears in the Deﬁnition 2.14 of factorization
homology, can be witnessed as a localization of its un-topologized ver sion Disk(B)/X on the collection
of those inclusions of ﬁnite disjoint unions of disks U⊂V inX for which this inclusion is isotopic to
an isomorphism. This comparison plays a fundamental role in recogniz ing certain colimit expressions
in this theory, for instance that support the pushforward formu la of§2.5.
Given a topological space X and a ﬁnite set J, we let ConfJ (X) denote the topological space
of injections from J to X. There is an evident action of the symmetric group Σ J on this space,
and we denote the coinvariants as Conf J (X)Σ J . Finally, given a basic U∼= Rn×C(Z), we denote
by Aut0(U ) the Kan complex of isomorphisms U → U that preserve the origin (0 ,∗)∈ U . (See
Section 4.3 of [AFT].) In the following lemma, B is the classifying space functor.
Lemma 2.21. For B a category of basics, the maximal ∞-groupoid of Disk(B) is canonically
identiﬁed as (
Disk(B)
) ∼
≃
∐
[U= ⨆
i∈I
U ⊔Ji
i ]
∏
i∈I
B
(
Σ Ji≀ EndB(Ui)
)
where the coproduct is indexed by isomorphism classes of ﬁni te disjoint unions of objects of B, whose
connected components are grouped here according to isomorphism type. In particular, the symmetric
monoidal functor [−] : Disk(B)→ Fin is conservative.
For X a B-manifold, the underlying ∞-groupoid of Disk(B)/X is canonically identiﬁed as the
space (
Disk(B)/X
) ∼
≃
∐
[U= ⨆
i∈I
U
⊔Ji
i ]
∏
i∈I
Conf Ji(X[Ui])Σ Ji
given in terms of unordered conﬁguration spaces of various s trata of X.
Proof. The statement concerning Disk(B) follows immediately from the characterization of Bsc
in [AFT].
Upon the canonical equivalence of ∞-categories Disk(B)/X≃ Disk(Bsc)/X , we can assume B =
Bsc, so that Mﬂd(B)≃ Snglr is an ∞-category associated to a Kan-enriched category. In §4.3
23
of [AFT] it is shown that the inclusion of Kan-groups Aut0(U )→ EndBsc(U ) is an equivalence of
underlying Kan complexes. Upon these considerations, to show the ﬁrst statement it is suﬃcient to
show that, for each ﬁnite set J, and each basic U , the Σ J -equivariant map which is evaluation at
each center of U
ev(0)j∈J : MapSnglr
(
U ⊔J,X
)
Aut0(U)J
≃
−−→ConfJ (X[U])
is an equivalence of Σ J -spaces. We do this by induction on the cardinality |J|, with the base case
|J| = 1 oﬀered by results in [AFT]. Now suppose |J| > 1, and choose a non-empty proper subset
J ′⊂J. Restriction along this inclusion of subsets gives the commutative dia gram
MapSnglr
(
U ⊔J,X
)
Aut0(U)J
/d47/d47
ev0
/d15/d15
MapSnglr
(
U ⊔J ′
,X
)
Aut0(U)J′
ev0
/d15/d15
Conf J (X[U]) /d47/d47 Conf J ′ (X[U])
which is evidently appropriately equivariant. In a standard manner, the map of ﬁbers of the hori-
zontal maps is canonically identiﬁed as the map of Σ J/integerdivideJ ′ -spaces
MapSnglr
(
U ⊔J/integerdivideJ ′
,X /integerdivideJ ′)
Aut0(U)J/integerdivideJ′
ev0
−−−→Conf J/integerdivideJ ′ (X[U] /integerdivideJ ′) ,
which is an equivalence by induction. The result follows.
□
Let B be a category of basics; let X be a B-manifold. Consider the ∞-subcategory
(2.4.1) IX⊂ Disk(B)/X
consisting of the same objects but only those morphisms (֒→X)֒→( ֒→X) whose image in
Disk(B)/X is an equivalence. Note that in 2.4.1, we think of X as an object of Mﬂd(B), while when
we refer to Disk(B)/X , we think of X as an object of Mﬂd(B).
Proposition 2.22. The standard functor
(2.4.2) Disk(B)/X−→ Disk(B)/X
witness an equivalence between ∞-operads from the localization (among ∞-operads):
(
Disk(B)/X
)
[I−1
X ] ≃ Disk(B)/X .
In particular, for each symmetric monoidal ∞-category V, restriction deﬁnes a fully faithful functor
AlgDisk(B)/X (V)֒→AlgDisk(B)/X (V)
whose image consists of those Disk(B)/X algebras that carry each isotopy equivalence to an equiva-
lence in V.
Proof. First note that the ∞-subcategory IX⊂ Disk(B)/X lies over equivalences in Fin∗. As so, the
localization
(
Disk(B)/X
)
[I−1
X ] (among ∞-categories) canonically lies over Fin∗. Therefore, should
the canonical functor
(
Disk(B)/X
)
[I−1
X ]
≃
− →Disk(B)/X from the localization (among ∞-categories)
be an equivalence between ∞-categories, then this localization among ∞-categories is in fact an
∞-operad itself; furthermore, this localization among ∞-categories also presents the ∞-operadic
localization. We are thusly reduced to showing that the functor (2.4 .2) is a localization between
∞-categories.
Note that the functor (2.4.2) is essentially surjective, manifestly. We will argue that the resulting
functor from the localization is an equivalence by showing it is an equiva lence on underlying ∞-
groupoids, then that it is an equivalence on spaces of morphisms. We recall that, as in Observation
2.7, since Mﬂd(B)→ Snglr is a right ﬁbration there are canonical equivalences of ∞-categories
Disk(B)/X ≃ Disk(Bsc)/X =: DX and Disk(B)/X ≃ Disk(Bsc)/X =: DX
and we adopt the indicated notation for this proof. Therefore, we can assume B = Bsc.
24
The underlying∞-groupoid of DX is the classifying space BIX . In light of the above coproduct
in Lemma 2.21, ﬁx an isomorphism type [ U = ⨆
i∈I
U ⊔Ji
i ] of a ﬁnite disjoint union of a basic stratiﬁed
space. Consider the full subcategory I[U]
X ⊂ IX consisting of those (֒→X) for which V ∼=U . We
thus seek to show that the resulting functor I[U]
X → ∏
i∈I
Conf Ji(X[Ui])Σ Ji witnesses an equivalence
from the classifying space. We will do this by ﬁrst showing that the fu nctor ∏
i∈I
ConfJi(X[Ui])∩
− : I[U]
X → ∏
i∈I
I
[(U
⊔Ji
i )[Ui ]
X[Ui]
induces an equivalence on classifying spaces, then observing a cano nical
equivalence of spaces BI
[(U ⊔Ji
i )[Ui]]
X[Ui ]
≃ Conf Ji(X[Ui])Σ Ji .
Consider the slice category ( I[U]
X )(Ri֒→X[Ui])i∈I /. An object is an object ( U ′֒→X) of I[U]
X for
which, for each i∈ I, there is an inclusion Ri⊂ U ′
[Ui] which is a bijection on components, and a
morphism is an inclusion of such. Because such ( U ′
[Ui]֒→X[Ui]) form a base for the topology about
Ri֒→X[Ui], then this category is ﬁltered. In particular, the classifying space B(I[U]
X )(Ri֒→X[Ui ])i∈I /≃
∗ is contractible. It follows that the functor ∏
i∈I
Conf Ji(X[Ui])∩− : I[U]
X → ∏
i∈I
I
[(U ⊔Ji
i )[Ui]]
X[Ui ]
induces an
equivalence on classifying spaces, as desired.
Now, let M be a smooth manifold, so that I =∗ is a singleton. The category I[U]
M forms a basis
for the standard Grothendieck topology on ConfJi (M )Σ Ji . It follows from Corollary 1.6 of [DI] that
the canonical map of topological spaces
colim
( ⊔
j∈Ji
Rj֒→M)∈I[U ]
M
∏
j∈Ji
Rj
≃
−−→ Conf Ji(M )Σ Ji
is a homotopy equivalence. Because each term Rj in this colimit is contractible, then this colimit is
identiﬁed as the classifying space
BI[U]
M ≃ colim
( ⊔
j∈Ji
Rj֒→M)∈I[U ]
M
∏
j∈Ji
Rj .
Applying this to the case M =X[Ui], we conclude that BI
[(U ⊔Ji
i )[Ui]
X[Ui ]
≃ ConfJi(M )Σ Ji . In summary,
we have veriﬁed that the map of underlying ∞-groupoids
(
DX [I−1
X ]
) ∼ ≃
−−→
(
DX
) ∼
is an equivalence.
We now show that the functor induces an equivalence on spaces of m orphisms. Consider the
diagram of spaces
(
DU [I−1
U ]
) ∼ /d47/d47
(֒→X)
/d15/d15
D∼
U
(֒→X)
/d15/d15(
DX [I−1
X ]
) (1) /d47/d47
ev1
/d15/d15
D(1)
X
ev1
/d15/d15(
DX [I−1
X ]
) ∼ /d47/d47 D∼
X
where a superscript (1) indicates a space of morphisms, and the upper vertical arrows are given as
(֒→U )↦→
(
(֒→X)֒→( ֒→X)
)
. Our goal is to show that the middle horizontal arrow is an
equivalence. We will accomplish this by showing that the diagram is a map of ﬁber sequences, for
we have already shown that the top and bottom horizontal maps ar e equivalences.
25
The right vertical sequence is a ﬁber sequence because such evalu ation maps are coCartesian
ﬁbrations, in general. Then, by inspection, the ﬁber over (֒→X) is the underlying ∞-groupoid
of the slice ( DX )/(֒→X). This slice is canonically identiﬁed as DU .
Let us show that the left vertical sequence is a ﬁber sequence. Th e space of morphisms of(
DX [I−1
X ]
) (1)
is the classifying space of the subcategory of the functor catego ry FunIX
(
[1], DX
)
⊂
Fun
(
[1], DX
)
consisting of the same objects but only those natural transform ations by I. We claim
the ﬁber over (֒→X) of the evaluation map is canonically identiﬁed as in the sequence
(
DU [I−1
U ]
) ∼ (֒→X)
−−−−−−→
(
DX [I−1
X ]
) (1) ev1
−−−→
(
DX [I−1
X ]
) ∼
.
This claim is justiﬁed through Quillen’s Theorem B, for the named ﬁber is the classifying space of
the slice category ( IX )/(֒→X) which is canonically isomorphic to IU . To apply Quillen’s Theorem
B, we must show that each morphism (֒→X)֒→( ֒→X) in I induces an equivalence of spaces
B
(
(IX )/(֒→X)
)
≃ B
(
(IX )/(֒→X)
)
. This map of spaces is canonically identiﬁed as BIU → BIV .
Through the previous analysis of this proof, this map is further iden tiﬁed as the map of spaces∐
[B]
U[B]→ ∐
[B]
V[B] induced from the inclusion֒→V . Because U and V are abstractly isomorphic,
then results of [AFT] give that each such inclusion is isotopic through stratiﬁed open embeddings to
an isomorphism. We conclude that Quillen’s Theorem B applies. See also T heorem 5.3 of [Ba]. □
Lemma 2.23. Letr : ~X→X be a reﬁnement between stratiﬁed spaces. Then there is a func tor
Disk(Bsc)/ ~X−→ Disk(Bsc)/X
which is a localization.
Proof. There is an obvious functor Snglr(Bsc)/ ~X→ Snglr(Bsc)/X given by assigning to ( ~i : ~֒→~X)
the object (i :֒→X) where Z = ~i( ~Z)⊂X is the image with the inherited stratiﬁcation. Observe
that this functor sends ﬁnite disjoint unions of basics conically smoo thly openly embedding into ~X,
to ﬁnite disjoint unions conically smoothly openly embedding into X. Also observe that this functor
sends stratiﬁed isotopy equivalences to stratiﬁed isotopy equivale nces. After these observations, the
desired functor happens through Proposition 2.22.
Notice that the map of underlying ∞-groupoids
(
Disk(Bsc)/ ~X
) ∼
→
(
Disk(Bsc)/X
) ∼
respects the
presentation of these spaces in Lemma 2.21 as a coproduct of a pro duct. Through the same logic
as in the proof of Proposition 2.22, it is enough to show that the func tor
Bsc/ Confi( ~M )−→ Bsc/ Confi(M)
is a localization for each ﬁnite cardinality i and each reﬁnement ~M
r
− →M of a smooth manifold.
Because ~M→M is a reﬁnement, then so is the map of stratiﬁed spaces Conf i( ~M )→ Confi(M ), by
inspection. The result is an instance of Proposition 1.2.14 of [AFT].
□
