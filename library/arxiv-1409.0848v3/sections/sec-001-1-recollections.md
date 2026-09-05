---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-001-1-recollections
section_title: "Recollections"
section_number: 1
pages: 6-14
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homol ogy, or topological chiral homology, at the generality of stratiﬁed spaces with tangen tial"
---
This entire work is founded on a predecessor, [AFT], which lays our fo undation for structured
stratiﬁed spaces and the∞-categories organizing them. In this ﬁrst subsection, we brieﬂy re call some
of the concepts introduced there, skipping many speciﬁcs. The re sults mentioned in this section will
be precise, but we refer any reader who wishes to truly understan d the precise deﬁnitions to [AFT].
In the second subsection we review some essentials of symmetric mo noidal∞-categories, after §2
of [Lu2].
1.1. Stratiﬁed spaces
Before deﬁning conically smooth stratiﬁed spaces which occupy this work, we ﬁrst review the baselin e
topological notions. We will regard a poset P as a topological space with closed sets P≤p, for each
element p∈ P . A stratiﬁed topological space indexed by a poset P is a paracompact Hausdorﬀ
topological space X with a continuous map X→P . For many purposes, the indexing poset P can
be taken to be the totally ordered set [ n] ={0< 1<...< n }, where n is the maximal dimension
of a neighborhood of a point in X. A stratiﬁed topological space X is a stratiﬁed topological space
indexed by a poset P (typically omitted from the notation). The stratum Xp⊂ X is the inverse
image of the element p∈P . The depth of a stratiﬁed topological space is the depth of its stratifying
poset, by which we mean the maximum among lengths of strictly increa sing sequences, should it
exist. A map between stratiﬁed topological spaces X→Y is a commutative diagram of topological
spaces
X /d47/d47
/d15/d15
Y
/d15/d15
P /d47/d47Q
where P and Q are the indexing posets for X and Y . Such maps are closed under composition, so
this forms a category. We say such a map is an open embedding if X→ Y is an open embedding
between topological spaces.
Example 1.1. We observe an essential operation for generating new stratiﬁed t opological spaces
from old ones: taking cones. First, for P is a poset, then the left-cone P ⊳ onP is the poset deﬁned
by adding a new minimum element to P . Note an identiﬁcation [ n]⊳ = [n + 1]. For X a stratiﬁed
topological space indexed by P , then the open cone on X,
C(X) :={0}
∐
{0}×X
[0,∞)×X−→{ 0} ∐
{0}×P
[1]×P =P ⊳ ,
is a stratiﬁed topological space indexed by P ⊳. Note that the cone C(X) carries a natural action by
multiplication of the nonnegative reals R≥0, by scaling in the cone coordinate. Note also that the
stratifying poset P ⊳ has strictly greater depth than the poset P , provided the latter exists.
The category of C0 stratiﬁed space is the smallest full subcategory of stratiﬁed topological spaces
characterized by the following properties:
(1) The empty set ∅ is a C0 stratiﬁed space indexed by the empty poset.
(2) If X is a C0 stratiﬁed space and both X and its indexing poset P are compact, then the
open cone C(X) is a C0 stratiﬁed space.
(3) If X andY areC0 stratiﬁed spaces, then the product stratiﬁed space X×Y is aC0 stratiﬁed
space.
6
(4) If X is a C0 stratiﬁed space and ( U → P|U )→ (X → P ) is an open embedding, then
(U→P|U ) is a C0 stratiﬁed space.
(5) If X is a stratiﬁed topological space admitting an open cover by C0 stratiﬁed spaces, then
X is a C0 stratiﬁed space.
Observe these examples of C0 stratiﬁed spaces:
• a singleton,∗ = (∗→∗ );
• a half-open interval, [0 ,∞) =
(
[0,∞)→ [1]
)
, with stratiﬁcation such that the 0-stratum is
precisely{0};
• Euclidean spaces, Ri = (Ri→∗ );
• anyC0 manifold.
We now add a conical smoothness condition to our stratiﬁcations. The assumption of conical
smoothness will be present throughout this work. This is, unfortu nately and perhaps ineluctably,
an inductive deﬁnition. The induction is on the depth of the stratifying poset.
A conically smooth stratiﬁed space , or stratiﬁed space for short, is a C0 stratiﬁed space X that is
equipped with a conically smooth atlas
{
Riα× C(Zα)֒→X
}
α
by basics. We now explain these terms. Each Zα is a compact stratiﬁed space of depth strictly less
than that of X; so we assume that we have already deﬁned what it means for Zα to be equipped
with a conically smooth atlas. In general, a basic is the data of a non-negative integer i and a
compact stratiﬁed space Z; together, these data deﬁne the C0 stratiﬁed space Ri× C(Z), which
might also be referred to as a basic when the conically smooth atlas on Z is understood. Note that,
forP the stratifying poset of Z, the stratifying poset of Ri× C(Z) is P ⊳; the cone-locus of this basic
is the stratum Ri = Ri×∗ , which is that indexed by the adjoined minimum. Continuing toward our
deﬁnition of a stratiﬁed space, a conically smooth atlas is a collection of basics openly embedding
as C0 stratiﬁed spaces into X. This collection satisﬁes three conditions:
(1) This collection of open embeddings forms a basis for the topology of X, in particular it
forms an open cover of X.
(2) The transition maps , by which we mean the inclusions of open embeddings Ri× C(W )֒→
Rj× C(Z) over X, are conically smooth, which we explain momentarily.
(3) This collection is maximal with respect to (1) and (2).
To complete our deﬁnition of a stratiﬁed space, it remains to explain t he condition for an open
embedding between basics to be conically smooth . So consider an C0 open embedding f : Ri×
C(Y )֒→Rj× C(Z) between basics. This open embedding f is conically smooth in the sense of §3.3
of [AFT] if the following conditions are satisﬁed.
• Away from the cone-locus: Each element of the atlas ψ : Rk× C(W )֒→Y determines a
composite open embedding Ri× (0,∞)× Rk× C(W )֒→Ri× C(Y )֒→Rj× C(Z). By way of
a smooth identiﬁcation (0 ,∞)∼= R, we recognize the domain of this composition as a basic.
Using that f is an open embedding between stratiﬁed topological spaces, neces sarily this is
the data of an open embedding fψ : Ri+1+k× C(W )֒→Rj× C(Z) /integerdivide Rj to the complement
of the cone-locus. As so, for each such ψ, the condition of conical smoothness requires this
open embedding fψ is a member of the atlas of the target, which carries meaning via the
induction in the deﬁnition of a stratiﬁed space.
• Along the cone-locus: Should the preimage of the cone-locus be empty, then the above
point entirely stipulates the conical smoothness condition on f . So suppose the preimage
of the cone-locus is not empty. Using that f is an open embedding between stratiﬁed
topological spaces, upon representing the values of f =
[
(f‖,f r,f θ)
]
as coordinates, then
fr(p, 0,y ) = 0 for all ( p,y )∈ Ri×Y . For 0 <k <∞, the condition that f is conically Ck
7
(along the cone-locus) requires the assignment
(1.1.1) ( p,v,s,y ) ↦→ lim
t→0+
[ ( f‖(p +tv,ts,y )−f‖ (p, 0,y )
t ,fr(p +tv,ts,y )
t ,f θ(p +tv,ts,y )
) ]
to be deﬁned as a map D‖f : T Ri× C(Y )→ T Rj× C(Z), required to be conically Ck−1
along the cone-locus (which carries meaning via induction on k). The condition of conical
smoothness requires that f is conically Ck for all k≥ 0.
Outlined above is a deﬁnition of a stratiﬁed space, in the sense of [AFT ]. We now, more brieﬂy,
outline the deﬁnition of a conically smooth map between two; the assumption of conical smoothness
on maps between stratiﬁed spaces will be present throughout this work, unless otherwise stated. Like
the deﬁnition of a stratiﬁed space, a conically smooth map between t wo stratiﬁed spaces is oﬀered
by induction on depth. For X and Y stratiﬁed spaces, a map f : X→Y between their underlying
stratiﬁed topological spaces is conically smooth if, for each pair of basic charts φ : Ri×C(Y )֒→X and
ψ : Rj×C(Z)֒→Y for which there is a containment f (φ(Ri))⊂ψ(Rj) of the images of the cone-loci,
the map ψ−1◦f◦φ : Ri× C(Y )→ Rj× C(Z) is conically smooth. This latter use of the term means
conically smooth away from the cone-locus , which can be ensured to carry meaning via induction
on depth, and conically smooth along the cone-locus which means f abides by expression (1.1.1).
Example 1.2. Note that smooth manifolds are precisely those stratiﬁed spaces t hat have no strata
of positive codimension. If g :M→N is a smooth map between compact smooth manifolds, then
the map of cones C(g) : C(M )→ C(N ) is conically smooth. If additionally h : Ri→ Rj is a smooth
map between Euclidean spaces, then the product map h× C(g) : Ri× C(M )→ Rj× C(N ) is again
conically smooth.
Let f : X → Y be a map between stratiﬁed spaces. We single out three important c lasses of
conically smooth maps:
• Sayf is an embedding if it is an isomorphism onto its image, and that it is an open embedding
if it is an embedding and it is an open map.
• Say f is a reﬁnement if it is a homeomorphism of underlying topological spaces, and its
restriction to each stratum of X is an embedding.
• Sayf is a constructible bundle if the following is true:
Let Y → Q be the stratiﬁcation of Y . Then for each q∈ Q, the restriction to the
q-stratum f| : X|f −1Yq→Yq is a ﬁber bundle of stratiﬁed spaces.
Unlike in the preceding deﬁnitions, for this next notion of weak constructibility the map f does not
preserve the stratiﬁcation (i.e., it does not lie over a map of posets) .
• Say a continuous map f : X→ Y between the underlying topological spaces of stratiﬁed
spaces is a weakly constructible bundle if there is a diagram among stratiﬁed spaces X
r
← −
~X
f
− →Y , with r a reﬁnement and f a constructible bundle, for which there is an equality
between maps of underlying topological spaces: f =f◦r.
Conically smooth maps compose, as do those that are open embeddin gs, thereby yielding the pair
of categories
Strat ⊃ Snglr .
The category Strat admits ﬁnite products, and so we regard it as enriched over the Car tesian category
Fun(Stratop, Set) of set-valued presheaves on itself through the expression
MapStrat(X,Y ) :Z↦→Strat/Z(X×Z,Y ×Z)
where the subscript /Z indicates those maps that commute with projecting to Z. Restricting along
the standard cosimplicial object ∆ •
e : ∆ −→ Strat given by [p]↦→{[p]
t
− →R| ∑
i∈[p]ti = 1}, gives
a natural enrichment of Strat, and thereafter of Snglr, over simplicial sets. In [AFT] we show that
these enrichments factors as a Kan-enrichments. In a standard manner, we obtain ∞-categories
Snglr and Strat
8
of stratiﬁed spaces and spaces of open embeddings among them, and respectively of conically smoot h
maps among them. Manifestly, there are natural functors Snglr→ Snglr and Strat→ Strat. There
is a full subcategory and an ∞-subcategory,
ι : Bsc ⊂ Snglr and ι : Bsc ⊂ Snglr
consisting of the basics. A key result is that the functor [−] : Bsc→ [Bsc] to the poset of isomorphism
classes is conservative (i.e., it does not create isomorphisms), which has immense consequen ces that
are speciﬁc to the set-up herein. (See Theorem 4.3.1 of [AFT].)
The tangent classiﬁer is the restricted Yoneda functor
Snglr
j
−−→PShv(Snglr)
ι∗
−−→PShv(Bsc) , X ↦→
(
Entr(X)
τX
−−→Bsc
)
where, here, we have taken the model for presheaves on ∞-categories as right ﬁbrations . Speciﬁcally,
each stratiﬁed space X determines an ∞-category Entr(X) := Bsc/X over Bsc. (A key result
in [AFT] is that Entr(X) is identiﬁed as the enter-path category of the stratiﬁed space X, though we
do not explain this result here for we do not use it.) Imitating the notio n of a tangential structure
in diﬀerential topology, we deﬁne a category of basics as a right ﬁbration
B = ( B→ Bsc)
and declare a B-manifold to be a stratiﬁed space X together with a lift of its tangent classiﬁer:
B
/d15/d15
Entr(X)
τX /d47/d47
g
/d54/d54♠♠♠♠♠♠♠♠♠♠♠♠♠♠
Bsc.
A B-manifold (X,g ) will typically be denoted simply as X. More precisely, we deﬁne the pullback
∞-categories
Mﬂd(B) /d47/d47
/d15/d15
Mﬂd(B) /d47/d47
/d15/d15
PShv(Bsc)/B
/d15/d15
Snglr /d47/d47 Snglr τ /d47/d47 PShv(Bsc)
and refer to the upper middle as that of B-manifolds.
Remark 1.3. Via the straightening/unstraightening construction (see Section 2.2 of [Lu1] – this is
the∞-categorical analogue of the Grothendieck construction), a righ t ﬁbration B→ Bsc is the same
data as a presheaf of spaces: Bscop→ Spaces. Precomposing this presheaf with the tangent classiﬁer
for X determines another presheaf of spaces: Entr(X)op τX
−−→Bscop B
− →Spaces. Via Theorem A.9.3
of [Lu2], such a presheaf is the data of a sheaf of spaces on X that happens to be constructible with
respect to the given stratiﬁcation of X. As so, a B-manifold is a stratiﬁed space X together with a
section g the sheaf named just above.
Deﬁnitionally, there is a fully faithful inclusion
ι : B֒→Mﬂd(B) .
A main result of [AFT] is that Mﬂd(B) is generated by B through the formations of collar-gluings
and sequential unions :
• A collar-gluing is a weakly constructible bundle X
f
− →[−1, 1]. We typically denote such a
collar-gluing as X∼= X−
⋃
R×X0
X+ where X− := f −1[−1, 1) and X0 := f −1(0) and X+ :=
f −1(−1, 1]; we regard X as the collar-gluing of X− and X+ along X0.
• A sequential union is a sequence of open subspaces X0⊂X1⊂···⊂ X of a stratiﬁed space
for which ⋃
i≥0
Xi =X.
9
It is also useful to single out this notion of a ﬁnitely-presented B-manifolds, namely one which
is generated from B only by collar-gluings. We say that an ∞-subcategory M of Mﬂd(B) is closed
under the formation of collar-gluings if X belongs to M whenever X0, X−, and X+ belong to M,
where X→ [−1, 1] is a weakly constructible bundle with those inverse images. The ∞-category
Mﬂd(B)ﬁn of ﬁnitary B-manifolds is the smallest full ∞-subcategory of Mﬂd(B) which contains B
and is closed under collar-gluings.
Example 1.4. Disjoint unions are instances of collar-gluings. That is, if B is a category of basics,
and X := X−⊔X+ is a disjoint union of B-manifolds, then the map f : X→ [−1, 1], given by
f|X±≡± 1, is a collar-gluing.
We conclude this subsection with a remark on our use of weakly const ructible bundles.
Remark 1.5. Wherever we use weakly constructible bundles in this work, we will only work with a
single map at a time. That is, we will not consider any sort of category or∞-category of stratiﬁed
spaces whose morphisms are weakly constructible bundles. This is du e to a technical issue: it is
unclear how to directly topologize the set of weakly constructible bu ndles (and then how to ensure
a well-deﬁned composition on these spaces of maps). This issue is dea lt with in a successor work,
[AFR], by the construction of the ∞-category cBun. This is an ∞-category of compact stratiﬁed
spaces whose morphisms are proper contructible bundles over the asymmetrically stratiﬁed interval
{0}⊂ [0, 1]. A main result of that paper implies that such a proper constructib le bundleX→ [0, 1] is
equivalent to a weakly constructible bundle map X1→X0 from the generic ﬁber to the special ﬁber.
Consequently, one could deﬁne the∞-category of compact stratiﬁed spaces and weakly constructible
bundles among them to be cBunop, but we have chosen not to incorporate this later work into the
present paper.
1.2. Symmetric monoidal ∞-categories
We review some aspects of symmetric monoidal ∞-categories, as well as ∞-operads, that we will
make use of later on. The content of this section is essentially extra cted from§2 of [Lu2].
We use the notation Fin∗ for the category of based ﬁnite sets. We let Fin denote the category
of (possibly empty) ﬁnite sets, and Fininj the subcategory of only injective morphisms. There is a
functor ( Fininj)op inert
−−→Fin∗ given on objects as I↦→I+ (i.e., attaching a disjoint basepoint) and
on morphisms as ( f :֒→J)↦→(f + :J+→ I+) where f + is speciﬁed by requiring both that the
diagram of ﬁnite sets
I+
= /d47/d47
f+
/d15/d15
I+
J+ =
/d47/d47J+
f +
/d79/d79
commutes and that f sends J /integerdividef (I), the complement of the image of f , to the basepoint +. We
denote the essential image of inert as Fininrt
∗ ⊂ Fin∗ and refer to its morphisms as inert maps – these
are the maps for which the inverse image of a point (which is not the ba sepoint) consists of at most
a single element. The category Fininj≃ (Fininrt
∗ )op carries the standard Grothendieck topology in
which the covers are surjective maps.
Deﬁnition 1.6 (After Deﬁnition 2.1.1.10 of [Lu2]) . An∞-operad is a functor O → Fin∗ that
satisﬁes the following points:
• For each inert map I+
f
− →J+, and for each lift O∈ O|I+ , there is a coCartesian morphism
O
~f
− →O′ lifting f . In particular, the restriction O| Fininrt
∗
→ Fininrt
∗ is a coCartesian ﬁbration.
• The coCartesian ﬁbration O| Fininrt
∗
→ Fininrt
∗ ∼= (Fininj)op is a Cat∞-valued sheaf whose value
on + is terminal.
10
• Let (Oi)i∈I∈ O×I
∗+≃ ∏
i∈I
O{i}+
≃
← −O|I+ be an object, and likewise let ( O′
j)j∈J∈ O|J+ be an
object. The canonical map of spaces
MapO
(
(Oi)i∈I, (O′
j)j∈J
) ≃
−−→
∐
I+
f
− →J+
∏
j∈J
MapO
(
(Oi)f (i)=j,O j
)
is an equivalence.
Let O be an∞-operad. We say O is unital if O has an initial object. The active∞-subcategory
Oact := O| Fin
is the restriction of O along the functor Fin
(−)+
−−−→Fin∗ that adjoins a disjoint base point. An active
morphism in O whose target lies over ∗+∈ Fin∗ is called a multi-morphism.
Remark 1.7. Deﬁnition 1.6 of an ∞-operad is an ∞-categorical version of a colored operad, also
known as a multi-category. In that terminology, each object of the ﬁber O|∗+ is a color.
Notation 1.8. Let O→ Fin∗ be an∞-operad. We will typically only carry the notation O for such
an∞-operad. We will refer to its restriction to ∗+ as the underlying∞-category, and again denote
it as O. Context should prevent confusion.
Remark 1.9. Recall that giving a coCartesian ﬁbration O → Fininrt
∗ is equivalent to giving a
functor Fininrt
∗ → Cat∞ by the straightening/unstraightening construction (see Section 2.2 of [Lu1] –
this is the ∞-categorical analogue of the Grothendieck construction). Furt her, the sheaf condition
guarantees that the ﬁber over the based ﬁnite set I+ is an∞-category equivalent to anI-fold product
of the ﬁber over +.
Deﬁnition 1.10 (Deﬁnition 2.1.2.7 of [Lu2]) . For O and P∞-operads, the∞-category of O-algebras
in P is the full ∞-subcategory
AlgO(P) ⊂ FunFin∗ (O, P)
consisting of those functors over based ﬁnite sets that preserv e inert-coCartesian morphisms. There
is an∞-category Operad∞ whose objects are ∞-operads and whose space of morphisms from O to
P is the underlying ∞-groupoid of AlgO(P). (See Deﬁnition 2.1.4.1 of [Lu2].)
Deﬁnition 1.11 (Deﬁnition 2.0.0.7 of [Lu2]; see also Remark 2.1.2.19 of [Lu2].) . A symmetric
monoidal∞-category is a coCartesian ﬁbration V→ Fin∗ whose restriction V| Fininrt
∗
→ Fininrt
∗ is a
Cat∞-valued sheaf whose value on + is terminal. (In particular, a symmetr ic monoidal∞-category
is an ∞-operad.) Let V be a symmetric monoidal ∞-category. A symmetric monoidal unit /BD
V for
V is a target of a morphism in V over +→∗ +. For D another symmetric monoidal ∞-category, the
∞-category of symmetric monoidal functors (from V to D) is the full ∞-subcategory
Fun⊗(V, D) ⊂ FunFin∗ (V, D)
consisting of those functors over based ﬁnite sets that preserv e coCartesian morphisms. There
is an ∞-category Cat⊗
∞ whose objects are symmetric monoidal ∞-categories and whose space of
morphisms from V to D is the underlying∞-groupoid of Fun⊗(O, V). (See Variant 2.1.4.13 of [Lu2].)
Lemma 1.12. The forgetful functor
Operad∞−→ Cat∞/ Fin∗
creates limits. The underlying ∞-category functor
Cat⊗
∞−→ Cat∞
is conservative and creates limits.
11
Proof. The ﬁrst statement can be veriﬁed directly. Consider a small diagra m K → Operad∞,
denoted k↦→Ok, and a limit cone K⊳→ Cat∞/ Fin∗ . Denote the value of the cone-point as O. Let
I+
f
− →J+ be an inert map, and let O∈ (O)|I+ be an object over I+. Consider the composite functor
K→ Operad∞→ Cat∞/ Fin∗
{O} ×
(−)|I+
FuncoCart
(
[1],(−)
)
|f
−−−−−−−−−−−−−−−−−−→Cat∞
given by assigning to an object k the category of coCartesian lifts of Ok
~fk
−→O′
k in Ok from the
image of O. This functor takes values in terminal ∞-categories, and so the limit too is terminal and
it is equipped with a functor to
lim
k∈K
(
{O} ×
(Ok)|I+
Fun
(
[1], Ok
)
|f
) ≃
← −{O} ×
O|I+
Fun
(
[1], O
)
|f .
By design, a morphism O
~f
− →O′ in the essential image of this functor is coCartesian.
Now consider a functor O|I+ → ∏
i∈I
O{i}+ induced by the diagram of inert morphisms ( I+
ai
−→
{i}+)i∈I . That this functor is an equivalence follows because limits commute wit h ﬁnite products.
Likewise, for each pair of objects ( Oi)i∈I∈ O|I+ and (O′
j )j∈J∈ O|J+, consider the map of spaces
MapO
(
(Oi)i∈I, (O′
j )j∈J
)
−→
∏
j∈J
MapO
(
(Oi){f (i)=j},O j
)
.
That this map is an equivalence follows again because limits commute with ﬁnite products.
The second statement is easier to ﬁnd the literature. By Lemma 3.2.2 .6 of [Lu2], a forgetful
map from a category of algebras over an operad is both conservat ive and limit-creating. Symmetric
monoidal∞-categories are commutative algebra objects in the symmetric mon oidal category Cat∞,
hence Lemma 3.2.2.6 of [Lu2] applies. □
Remark 1.13. Let F : O→ V be a symmetric monoidal functor. Since F preserves coCartesian
morphisms, it induces a map between the sheaves on Fininj associated to O and V. Hence for every
f :I+→J+, we obtain a diagram [1] × [1]→ Cat∞ as follows:
OI
f∗
/d15/d15
F I
/d47/d47 VI
f∗
/d15/d15
OJ F J
/d47/d47 VJ.
ForJ =∗, one can interpret the diagram as specifying an equivalence ⨂ I
VF (Oi)≃F (⨂ I
OOi).
Remark 1.14. Let V and D be symmetric monoidal∞-categories. There is an evident full inclusion
Fun⊗(V, D)⊂ AlgV(D) – it is typically not essentially surjective. The latter corresponds t o lax
monoidal functors.
For each ﬁnite set I, there is then a canonical diagram of ∞-categories
⊗ : VI ≃
←−−VI+
V(I+ →∗)
−−−−−→V .
Deﬁnition 1.15. For K a small ∞-category, the symmetric monoidal structure of V distributes
over K-shaped colimits if for each c∈ V, the composite functor
c⊗− : V≃∗× V
c×idV
− −−− →V× V
⊗
− →V
commutes with colimits of K-shaped diagrams. We say V is⊗-sifted cocomplete if its underlying∞-
category admits sifted colimits and its symmetric monoidal structur e distributes over sifted colimits,
where an∞-category K is sifted if it is nonempty and the diagonal K→ K× K is a ﬁnal functor.
12
Lemma 1.16 (Section 2.2.4 of [Lu2]) . The forgetful functor admits a left adjoint
Env : Operad∞ ⇄ Cat⊗
∞ ,
referred to as the symmetric monoidal envelope functor.
Observation 1.17. There is a canonical ﬁller in the diagram among ∞-categories:
Cat⊗
∞
(−)op
/d47/d47❴ ❴ ❴ ❴ ❴ ❴
/d15/d15
Cat⊗
∞
/d15/d15
Cat∞
(−)op
/d47/d47 Cat∞.
In other words, the opposite of the underlying ∞-category of a symmetric monoidal ∞-category is
canonically endowed with a symmetric monoidal structure.
Example 1.18. Here are some examples of symmetric monoidal ∞-categories that are ⊗-sifted
cocomplete.
• (Chk,⊕) and ( Chk,⊗): chain complexes over a ring k with equivalences given by quasi-
isomorphisms, equipped with direct sum, or with tensor product.
• (Spectra,∨) and (Spectra,∧): spectra with equivalences generated by stable homotopy equiv-
alences, equipped with wedge sum, or with smash product.
• (X,×): any cocomplete Cartesian closed ∞-category (for instance Spaces or Cat∞) with
ﬁnite product.
• Let V be any symmetric monoidal ∞-category whose underlying ∞-category admits small
colimits and whose symmetric monoidal structure distributes over s mall colimits. Then,
for O any∞-operad, the ∞-category of algebras AlgO(V) inherits a standard symmetric
monoidal structure which is given pointwise, and this symmetric mono idal∞-category is
⊗-sifted cocomplete.
An example of a symmetric monoidal ∞-category that is not⊗-sifted cocomplete is ( Chop
Q,⊗), for
⊗ does not distribute over totalizations.
We are about to deﬁne an ∞-operad V/c for V a unital symmetric monoidal∞-category andc∈ V
an object in its underlying ∞-category. Recall the construction from §2.4.3 of [Lu2] of an ∞-operad
D∐ from an∞-category D. Quickly, a functor K→ D∐ is the datum of a functor K×
Fin∗
Fin∗,∗′→ D
where the second factor in the ﬁber product is the category of ﬁn ite sets equipped with an inclusion
from the two-element set {∗,∗′} and maps among such that preserve such inclusions. Should D be
an ordinary category, then the D∐ is an ordinary colored operad with one color for each object of
D, while a multi-morphism from ( d1,...,d n) to d is simply a collection of morphisms di→ d for
each 1≤i≤n.
Lemma 1.19. For O = (O→ Fin∗) a unital ∞-operad, there is a preferred map of ∞-operads
O−→ (O|∗+)∐ .
Proof. We will use the notation Fininj⊂ Fin
(−)+
−−−→Fin∗ for the category of ﬁnite sets and injections
among them. Consider the category Funinj
(
[1], Fin∗
)
consisting of those functors from the two-
object totally ordered set [1] = {0< 1} which classify injective maps among based ﬁnite sets, and
natural transformations among them. Evaluation at 0 gives a func tor Funinj
(
[1], Fin∗
) ev0
−−→Fin∗.
Notice the evident functor Fin∗,∗′→ Funinj
(
[1], Fin∗
)
, and notice that it factors as an equivalence
Fin∗,∗′
≃
− →ev−1
0 (∗+).
The∞-operad O being unital grants that the underlying ∞-category O|∗+ has an initial object.
It follows that the restricted projection O| Fininj→ Fininj is a Cartesian ﬁbration. In particular, there
13
is a canonical ﬁller in the diagram of ∞-categories
O ×
Fin∗
Funinj
(
[1], Fin∗
) /d47/d47❴ ❴ ❴ ❴ ❴ ❴ ❴ ❴
ev0
/d39/d39❖❖❖❖❖❖❖❖❖❖
O
/d127/d127         
Fin∗
in which the implicit functor Funinj
(
[1], Fin∗
) ev1
−−→Fin∗ is evaluation at 1. Restricting the second
factor in the above ﬁber product to Fin∗,∗′ gives the functor O→ (O|∗+ )∐. It is direct to verify that
this functor sends inert-coCartesian morphisms to inert-coCart esian morphisms.
□
Corollary 1.20. Let O be a unital ∞-operad. Let E|∗+ → O|∗+ be a right ﬁbration over the
underlying∞-category. We denote the pullback ∞-category
E /d47/d47
/d15/d15
(E|∗+ )∐
/d15/d15
O /d47/d47 (O|∗+ )∐ .
After Lemma 1.12, the composite functor E→ O→ Fin∗ makes E into an∞-operad, and the functor
E→ O is a map of ∞-operads.
Notation 1.21. Let D→ M be a symmetric monoidal functor between symmetric monoidal ∞-
categories, each for which the symmetric monoidal unit is initial. Let X∈ M be an object of the
underlying∞-category. We use the notation
D/X
for the output of Corollary 1.20 applied to the right ﬁbration D/X→ D. By construction, this ∞-
operad is equipped with an ∞-operad map to D for which the functor on underlying ∞-categories
is the standard projection from the slice. Say a morphism of D/X is pre-coCartesian if its image
in D is coCartesian over Fin∗. We adopt the following notational convention: for V a symmetric
monoidal∞-category, the∞-category of D/X -algebras in V is the full ∞-subcategory
AlgD/X (V) ⊂ FunFin∗
(
D/X, V
)
consisting of those functors that send pre-coCartesian morphis ms to coCartesian morphisms.
2. F actorization
