---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-006-25-pushforward
section_title: "Pushforward"
section_number: 2.5
pages: 26-30
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homol ogy, or topological chiral homology, at the generality of stratiﬁed spaces with tangen tial"
---
For this subsection, we ﬁx a symmetric monoidal ∞-category V that is⊗-sifted cocomplete.
Lemma 2.24. LetX be a B-manifold and Y a B′-manifold, and let f : X→Y be a constructible
bundle of the underlying stratiﬁed spaces. Taking inverse i mages deﬁnes a functor of ∞-operads
f −1 : Disk(B′)/Y −→ Mﬂd(B)/X
which on objects sends֒→Y to f −1֒→X. As a consequence, there is a natural pushforward
functor
f∗ : AlgX (V)−→ AlgY (V)
26
that sends an algebra A on X to the algebra on Y taking values
f∗A(֒→Y ) ≃
∫
f −1U
A .
Proof. Note that taking point-wise inverse images deﬁnes a functor of disc rete categories Disk(Bsc)/Y →
Snglr/X which, additionally, preserves the multi-category structure of Co nstruction 2.4. We ﬁrst
show that this functor can be naturally extended to the topologica l case, i.e., that there is a preferred
ﬁller in the diagram of ∞-operads
Disk(Bsc)/Y
f −1
/d47/d47
/d15/d15
Snglr/X
/d15/d15
Disk(Bsc)/Y
f −1
/d47/d47❴ ❴ ❴ ❴ ❴ ❴Snglr/X .
Because f is a constructible bundle, the collections I and J of isotopy equivalences in Disk(Bsc)/Y
and Snglr/X , respectively, are mapped to one another by f −1. Further, they map to equivalences
in Disk(Bsc)/Y and Snglr/X , respectively. By the universal property of localization, we can th us
factor the previous diagram as
Disk(Bsc)/Y
f −1
/d47/d47
/d15/d15
Snglr/X
/d15/d15
Disk(Bsc)/Y [I−1]
f −1
/d47/d47
∼
/d15/d15
Snglr/X [J−1]
/d15/d15
Disk(Bsc)/Y
f −1
/d47/d47❴ ❴ ❴ ❴ ❴ ❴ ❴ ❴Snglr/X .
Proposition 2.22 states that the bottom left downward arrow is an e quivalence, as indicated, thereby
determining the ﬁller.
Recall from Observation 2.7 that B-manifold structure on X deﬁnes an equivalence Snglr/X≃
Mﬂd(B)/X , directly from the deﬁnition of structures by right ﬁbrations; the same is true for the
B′-manifold structures on basics in Y . Under the hypotheses of the Lemma, we consequently have a
map of∞-operads Disk(B′)/Y → Mﬂd(B)/X deﬁned by f −1. The desired functor is the composition
f∗ : AlgX (V)
∫
− /d47/d47 AlgMﬂd(B)/X (V)
(f −1)∗
/d47/d47 AlgY (V) .
□
We have the following result about this pushed-forward algebra f∗A.
Theorem 2.25 (Pushforward). Let V be a symmetric monoidal ∞-category which is ⊗-sifted co-
complete; let X be a B-manifold with f : X→ Y a weakly constructible bundle over a stratiﬁed
spaceY . There is a commutative diagram:
AlgX (V)
∫
X /d47/d47
f∗ /d37/d37▲▲▲▲▲▲▲▲▲▲ V
AlgY (V)
∫
Y
/d60/d60①①①①①①①①①
In particular, for any Disk(B)-algebraA, there is a canonical equivalence in V:
∫
Y
f∗A ≃
∫
X
A .
27
The proof of this theorem will involve an auxiliary ∞-category Xf built from the constructible
bundle f .
Deﬁnition 2.26. LetX be a B-manifold, and letY be a B′-manifold. For f :X→Y a constructible
bundle, the∞-category Xf is the limit of the following diagram
Disk(B)/X/d116/d20
/d38/d38◆◆◆◆◆◆◆◆◆◆◆ Fun
(
[1], Mﬂd(B)/X
)
ev1
/d40/d40◗◗◗◗◗◗◗◗◗◗◗◗◗
ev0
/d118/d118♠♠♠♠♠♠♠♠♠♠♠♠♠
Disk(B′)/Y
f −1
/d120/d120♣♣♣♣♣♣♣♣♣♣♣
Mﬂd(B)/X Mﬂd(B)/X
where Fun
(
[1], Mﬂd(B)/X
)
is the∞-category of 1-morphisms in Mﬂd(B)/X .
Informally, Xf consists of compatible triples (֒→f −1V ), where V is a ﬁnite disjoint union
of basics in Y ; U is a ﬁnite disjoint union of basics in X; the embedding֒→f −1V is compatible
with the embeddings f −1֒→X and֒→X. We are able to utilize this ∞-category Xf because
of the following key ﬁnality property.
Lemma 2.27. For any constructible bundle X
f
− →Y between stratiﬁed spaces, the functor ev0 :
Xf→ Disk(B)/X is ﬁnal.
Proof. The functor ev0 is a Cartesian ﬁbration of ∞-categories. Thus, to check ﬁnality, by Lemma
4.1.3.2 of [Lu1], it suﬃces to show that, for each U∈ Disk(B)/X , the ﬁber ev−1
0 V has contractible
classifying space. So let V ∈ Disk(B)X . Unwinding the deﬁnition of Xf , we must show contractibility
of the classifying space of the iterated slice ∞-category
(
Disk(B)/Y
) U/
.
The projection from this slice
(
Disk(B)/Y
) U/
→ Disk(B)/Y is a left ﬁbration, and so it is classiﬁed
by a functor, justiﬁably written as
MapMﬂd(B)/X (U,f −1−) : Disk(B)/Y → Spaces ,
whose colimit is identiﬁed as the relevant classifying space
B
(
Disk(B)/Y
) U/
≃ colim
(֒→Y )∈Disk(B)/Y
MapMﬂd(B)/X (U,f −1V ) .
So we seek to show the righthand colimit is contractible.
Formal is that the sequence of maps
MapMﬂd(B)/X (U,f −1V ) −→ MapMﬂd(B)(U,f −1V ) −→ MapMﬂd(B)(U,X )
is a ﬁber sequence (here the ﬁber is taken over any implicit morphism֒→X, thereby giving
meaning to the lefthand space). So we seek to show the map from th e colimit
colim
(֒→Y )∈Disk(B)/Y
MapMﬂd(B)(U,f −1V ) −→ MapMﬂd(B)(U,X )
is an equivalence of spaces. We recognize this map of spaces as the m ap of ﬁbers over U∈ Disk(B)
of the map of right ﬁbrations over Disk(B):
colim
(֒→Y )∈Disk(B)/Y
Disk(B)/f −1V −→ Disk(B)/X .
Being right ﬁbrations, it is enough to show that this functor is an equ ivalence on underlying ∞-
groupoids.
Through Lemma 2.21 this is the problem of showing, for each ﬁnite set J and each basic U , that
the map of spaces
colim
(֒→Y )∈Disk(B)/Y
Conf J
(
(f −1V )[U]
)
Σ J
−→ Conf J (X[U])Σ J
is an equivalence. So we can assume that the underlying stratiﬁed sp ace of X =M is an ordinary
smooth manifold.
28
Lemma 2.22 grants that the forgetful map
colim
(֒→Y )∈Disk(Bsc)/Y
Conf J
(
f −1V
)
Σ J
≃
−−→ colim
(֒→Y )∈Disk(B)/Y
ConfJ
(
f −1V
)
Σ J
is an equivalence of spaces. Now notice that, for each (֒→Y )∈ Disk(Bsc)/Y , the map Conf J (f −1V )→
Conf J (M ) an open embedding. Also, for each point c :֒→M the image f
(
c(J)
)
⊂Y has cardi-
nality at most J. So there is an object (֒→Y ) of Disk(Bsc)/Y whose image contains the subset
f
(
c(J)
)
. We see then that the collection of open embeddings
{
ConfJ (f −1V )Σ J֒→ConfJ (M )Σ I| (֒→Y )∈ Disk(Bsc)/Y
}
form an open cover.
Proved in [AFT] is that open embeddings of basics into Y form a basis for the topology of Y .
It follows that the collection of (at most) |J|-tuples of disjoint basics in Y form an open cover of
Y in such a way that any ﬁnite intersection of such is again covered by s uch. It follows that the
collection of open embeddings above is an open cover for which any ﬁn ite intersection of its terms
is again covered by terms of the collection. In particular, this collect ion of open embeddings forms
a hypercover of Conf J (M )Σ J . Corollary 1.6 of [DI] gives that the map
colim
(֒→Y )∈Disk(Bsc)/Y
ConfJ
(
f −1V
)
Σ J
≃
−−→ConfJ (M )Σ J
is an equivalence of spaces. This completes the proof.
□
This has the following important corollary, which completes the proof of Theorem 2.15.
Corollary 2.28. ForX a B-manifold, the ∞-category Disk(B)/X is sifted.
Proof. The∞-category Disk(B)/X is evidently nonempty, as it contains the object ( ∅֒→X). We
must then prove that the diagonal functor Disk(B)/X → Disk(B)/X× Disk(B)/X is ﬁnal. This
diagonal functor ﬁts into a diagram among ∞-categories
Disk∇
ev0 /d47/d47
ev1
/d15/d15
Disk(B)/X⊔X
Disk(B)/X
diag /d47/d47 Disk(B)/X× Disk(B)/X
≃ ⊔
/d79/d79
that we now explain. The upper left ∞-category is that of Deﬁnition 2.26 applied to the fold map
∇ : M⊔M→ M ; as so, it is equipped with the indicated projection functors. The rig ht vertical
arrow is induced by the symmetric monoidal structure on Mﬂd(B), which is disjoint union. This
right vertical arrow is an equivalence; an inverse is given by declaring its projection to each factor to
be given by intersecting with the corresponding cofactor of the dis joint union. Therefore, to prove
that the diagonal functor is ﬁnal it is suﬃcient to prove that both o f the projection functors ev1
and ev0 are ﬁnal. The ﬁnality of ev0 is Lemma 2.27.
We explain that ev1 is ﬁnal. Note that the functor ∇−1 : Disk(B)/X → Mﬂd(B)/X⊔X factors
through the full ∞-subcategory Disk(B)/X⊔X . As so, there is a canonical identiﬁcation between
∞-categories
Disk∇ ≃ Disk(B)/X ×
Disk(B)/X⊔X
Ar(Disk(B)/X⊔X )
over Disk(B)/X . Through this identiﬁcation, the composite functor
Disk(B)/X
∇
−−→Disk(B)/X⊔X
const
−−−−→Ar(Disk(B)/X⊔X )
determines a right adjoint to the functor ev1. Finality of ev1 follows.
□
Using Lemma 2.27, we can now prove our push-forward formula for f actorization homology.
29
Proof of Theorem 2.25. After Lemma 2.23, we can assume that the weakly constructible bundle f
is actually constructible.
The functor
f∗A : Disk(Bsc)/Y
f −1
/d47/d47 Disk(B)/X
∫
A /d47/d47 V
is the left Kan extension of A : Xf→ V along the functor ev1 : Xf→ Disk(Bsc)/Y . Therefore there
is a natural equivalence
colim
Xf
A≃ colim
U∈Disk(Bsc)/Y
∫
f −1U
A≃
∫
N
f∗A .
By Lemma 2.27, the functor ev0 : Xf→ Disk(B)/X is ﬁnal, which implies the equivalence colimXfA≃∫
MA, and the result follows. □
In the case of the projection map X×Y → Y oﬀ of a product, this result has the following
consequence.
Corollary 2.29 (Fubini). Let B− and B+ and B be∞-categories of basics with a functor B−×
B+→ B over the product functor Bsc× Bsc
×
− →Bsc. Let A be a Disk(B)-algebra in V. Let X be a
B−-manifold, and Y be a B+-manifold; so X×Y is canonically equipped as a B-manifold. There
is a canonical equivalence in V: ∫
X×Y
A ≃
∫
Y
∫
X
A .
