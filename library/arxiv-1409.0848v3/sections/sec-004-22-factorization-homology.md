---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-004-22-factorization-homology
section_title: "Factorization homology"
section_number: 2.2
pages: 17-23
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homol ogy, or topological chiral homology, at the generality of stratiﬁed spaces with tangen tial"
---
be an ∞-category of basics. The (absolute) factorization homology functor is a left adjoint to the
restriction
∫
− : AlgDisk(B)(V)
/d37/d37❡ ❞ ❝ ❜ ❵ ❫ ❭ ❲ ❖
Fun⊗(
Mﬂd(B), V
)
./d111/d111
ForX a B-manifold, the (relative) factorization homology functor is a left adjoint to the restriction
∫
− : AlgX (V)
/d32/d32❡ ❞ ❝ ❜ ❵ ❫ ❬ ❱ ▼
AlgMﬂd(B)/X (V) ./d111/d111
The left adjoint in the previous deﬁnition need not exist. The essent ial result provided in the
following is that for a large class of targets V, factorization homology both exists and has a relatively
simple expression, agreeing with the left adjoint at the level of unde rlying∞-categories; i.e., without
remembering the monoidal structures.
17
Theorem 2.15. Let V be a symmetric monoidal ∞-category which is ⊗-sifted cocomplete, and let
B be an ∞-category of basics. Then each of the absolute and the relati ve factorization homology
functors exists and each is fully faithful, and each evaluat es as
(2.2.1)
∫
X
A ≃ colim
(
Disk(B)/X→ Disk(B)
A
− →V
)
≃ Disk(B)/X
⨂
Disk(B)
A
– here, all terms are as the underlying ∞-categories of the respective ∞-operads.
We give a proof of this result predicated on several results to come . In Lemma 2.16, we identify
the general formal features for symmetric monoidal and operad ic left Kan extension to exist and
agree with the underlying left Kan extension. In the following section s, we show that these formal
features hold in our example of interest.
Proof of Theorem 2.15. This is an application of Lemmas 2.16 and 2.17.
To apply this result, we need these three facts:
• Let X be a B-manifold. Then the slice ∞-category Disk(B)/X is sifted. This is Corol-
lary 2.28 to come.
• The functor Disk(B)/ /BD
Disk(B) → Mﬂd(B)/ /BD
Mﬂd(B) is ﬁnal. In our case, this functor is an
equivalence, manifestly.
• LetX andX ′ be B-manifolds. Then the functor Disk(B)/X× Disk(B)/X ′→ Disk(B)/X⊔X ′
is ﬁnal. In our case, this functor is actually an equivalence, by inspec tion.
□
Lemma 2.16. Let V be a symmetric monoidal ∞-category; let ι : B→ M be a symmetric monoidal
functor with small domain and locally small codomain. Consi der the commutative diagram of solid
arrows
Fun⊗(B, V)
ι⊗
♮
/d35/d35❢ ❡ ❞ ❜ ❵ ❫ ❬ ❑
/d15/d15
Fun⊗(M, V)
ι∗
/d111/d111
/d15/d15
Fun(B, V)
ι♮
/d31/d31❢ ❡ ❞ ❜ ❵ ❫ ❬ ❑
Fun(M, V)ι∗
/d111/d111
where ι∗ is restriction along ι, and the vertical arrows forget that a given functor was symm etric
monoidal. Suppose both:
(1) the underlying ∞-category of V admits sifted colimits;
(2) for each M∈ M, the slice ∞-category B/M is sifted.
Then ι∗ has a left adjoint ι♮ as indicated, which can be calculated as
(2.2.2) ι♮F :M↦→colim
(
B/M→ B
F
− →V
)
≃ ι∗M⊗
B
F .
The last expression is a coend, and we have identiﬁed M ∈ M with its image under the Yoneda
functor. In addition, suppose
(3) the symmetric monoidal structure for V distributes over sifted colimits;
(4) the functor between slice ∞-categories over units
B/ /BD
B→ B/ /BD
M
is ﬁnal; and
18
(5) for each pair of objects M,M ′∈ M, the tensor product functor
⨂
: B/M× B/M′−→ B/M⊗M ′
is ﬁnal.
Then there is a left adjoint ι⊗
♮ as indicated, and the downward right square commutes. If ι is fully
faithful then so are each of ι♮ and ι⊗
♮ .
Proof. Conditions (1) and (2) grant that each value of the expression (2.2 .2) exists. Lemma 4.3.2.13
of [Lu1] states that these expressions depict a functor as indicat ed. Proposition 4.3.3.7 of [Lu1]
states that this functor satisﬁes the universal property of bein g a left adjoint to ι∗.
We now argue that conditions (3) and (4) grant that, for each sym metric monoidal functor
B
F
− →V, and for each based map among ﬁnite sets I+
f
− →J+, the diagram of ∞-categories
MI
f∗
/d15/d15
(ι♮F )I
/d47/d47 VI
f∗
/d15/d15
MJ (ι♮F )J
/d47/d47 VJ
commutes. Each based map f : I+→ J+ is canonically a composition of a surjective active map
f surj followed by an injective active map f inj followed by an inert map f inrt, and so it is enough to
verify commutativity for each such class of maps. The case of inert maps is obvious, because then
f∗ is projection and ( ι♮F )I is deﬁned as the I-fold product of functors. The case of injective active
maps amounts to verifying that ι♮F sends a symmetric monoidal unit to a symmetric monoidal unit.
This follows from Condition (4) because F does so.
The case of surjective active maps follows from the case that f : I+→∗ + is given by i↦→∗,
so that f∗ = ⨂ I is the I-fold tensor product. Well, because F is symmetric monoidal, there is
a canonical arrow ι♮F◦ ⨂ I −→ ⨂ I◦(ι♮F )I between functors MI → V that we will argue is an
equivalence. This arrow evaluates on ( Mi)i∈I as the horizontal one in the following natural diagram
inside V:
colim( B/ ⨂
i∈I
Mi → B F− → V) /d47/d47 ⨂
i∈ I
colim( B/M i → B F− → V)
colim( ∏
i∈ I
B/M i → BI F I
− − → VI
⨂ I
− − → V)
(5)
/d106/d106❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚ (3)
/d52/d52❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥
.
The arrow labeled by (3) is an equivalence precisely because of condit ion (3). Condition (5) implies
that the functor ∏
i∈I B/Mi→ B/ ⨂
i∈I
Mi is ﬁnal, for it is a composition of ﬁnal functors. It follows
that the arrow labeled by (5) is an equivalence, after observing the following diagram among ∞-
categories:
∏
i∈I
B/Mi
⨂ I
/d47/d47
/d15/d15
B/ ⨂
i∈I
Mi
/d15/d15
BI
⨂ I
/d47/d47
F I
/d15/d15
B
F
/d15/d15
VI
⨂ I
/d47/d47 V.
□
Recall Notation 1.21. We now state a likewise result as Lemma 2.16 for t he case of the∞-operads
of Notation 1.21. The proof of this lemma is the same as that for Lemm a 2.16.
19
Lemma 2.17. Let V be a symmetric monoidal ∞-category. Let ι : D→ M be a symmetric monoidal
functor between symmetric monoidal ∞-categories with D small and M locally small. Suppose both
the symmetric monoidal unit for each of D and M is initial. Let X ∈ M be an object of the
underlying∞-category, and consider the ∞-operads D/X and M/X over D and M, respectively.
Consider the solid commutative sub-diagram of restriction and forgetful functors
AlgD/X (V)
ι⊗
♮
/d31/d31❢ ❡ ❝ ❜ ❵ ❫ ❬ ▲
/d15/d15
AlgM/X (V)
ι∗
/d111/d111
/d15/d15
Fun(D/X, V)
ι♮
/d31/d31❢ ❡ ❝ ❜ ❵ ❫ ❬ ▲
Fun(M/X, V)ι∗
/d111/d111
where the superscript ∗ denotes the evident restriction and the vertical arrows res trict to active
∞-subcategories. Suppose both:
(1) the underlying ∞-category of V admits sifted colimits;
(2) for each Z = (Z→X)∈ M/X , the slice ∞-category (D/X )/Z≃ D/Z is sifted.
Then ι∗ has a left adjoint ι♮ as indicated, which can be calculated as
(2.2.3) ι♮A : (Z→X)↦→colim
(
D/Z→ D/X
A
− →V
)
≃ ι∗(Z→X) ⊗
D/X
A
– here in the expression of the coend we identify (Z→ X)∈ M with its image under the Yoneda
functor. In addition, suppose
(3) the symmetric monoidal structure for V distributes over sifted colimits;
(4) the functor between slice ∞-categories over units
D/ /BD
D→ M/ /BD
M
is ﬁnal;
(5) for each pair of objects (Z→X), (Z ′→X)∈ M/X , the tensor product functor
⨂
: D/Z× D/Z′−→ D/Z⊗Z′
is ﬁnal.
Then there is a left adjoint ι⊗
♮ as indicated, and the downward right square commutes. If ι is fully
faithful then so are each of ι♮ and ι⊗
♮ .
2.3. Disks and ﬁnite subsets
We pause our development of factorization homology to relate the ∞-category Disk(Bsc)/X , which
appears in the Deﬁnition 2.14 of factorization homology, with the ent er-path∞-category of another
stratiﬁed space associated to X: the Ran space of X.
Let i be a ﬁnite cardinality. For X a topological space, the bounded Ran space Ran≤i(X) is
the topological space consisting of subsets S⊂ X with bounded cardinality |S|≤ i for which the
inclusion֒→X is surjective on connected components; the topology on Ran≤i(X) is the coarsest
for which, for each set I with cardinality |I| = i equal to i, the map Image : X I → Ran≤i(X) is
continuous. For f :֒→Y an open embedding that is surjective on connected components, t he
evident map Ran≤i(f ) : Ran≤i(X)→ Ran≤i(Y ) is an open embedding.
In§3 of [AFT] we prove the following result, which in particular states tha t Ran≤i(X) inherits
the structure of a stratiﬁed space from one on X. We use the notation
(2.3.1) Snglrsurj ⊂ Snglr
20
for the∞-subcategory with the same objects and with those morphisms tha t induce surjections on
connected components.
Proposition 2.18 (Proposition 3.7.5 of [AFT]) . Let i be a ﬁnite cardinality. There is a functor
between∞-categories
(2.3.2) Ran≤i : Snglrsurj−→ Snglr
for which the underlying topological space of each value Ran≤i(X) is the bounded Ran space of the
underlying space of X, and whose value on a morphism X
f
− →Y is Ran≤i(f ).
The next result gives a description of the topology of Ran≤i(X) in terms of that of X.
Lemma 2.19. Let i be a ﬁnite cardinality. Let X be a stratiﬁed space. Consider the collection of
open embeddings
{
Ran≤i(U )
Ran(f )
−−−−−→Ran≤i(X)
}
{U
f
− →X}
indexed by conically smooth open embeddings from ﬁnite disj oint unions of basics which are surjective
on connected components. This collection of open embeddins forms a basis for the topology of
Ran≤i(X).
Proof. LetS∈ Ran≤i(X) be an element, and let S∈O⊂ Ran≤i(X) be an open neighborhood. We
must show that there is a disjoint union of basics֒→X openly embedding into X as a surjection
on components so that S belongs to the image of the map Ran≤i(U )→ Ran≤i(X) and this image
lies in O.
Fix a set I of cardinality i. Choose a map I
f0
−→X for which the image Image(f0) = S equals S.
From the deﬁnition of the topology of Ran≤i(X), the subset O⊂ Ran≤i(X) being open implies the
subset
~O :=
{
I
f
− →X| Image(f )∈O
}
⊂ X I
is open. From the deﬁnition of the product topology on X I, for each s ∈ S there is an open
subset s ∈ Vs ⊂ X so that the product ∏
i∈I
Vf0(i) ⊂ ~O lies inside ~O. From the deﬁnition of a
stratiﬁed space in the sense of §3 of [AFT], the collection of conically smooth open embeddings
from basics into X forms a basis for the topology of X. Therefore, we can choose each Vs above
to be a basic s∈ Us֒→X. Because X is in particular Hausdorﬀ, we can make these choices
so that the intersection Us∩Us′ is empty whenever s⁄= s′∈ S. We obtain an open embedding
U := ⨆
s∈S
Us֒→X from a ﬁnite disjoint union of basics which is surjective on component s. By
construction, this embedding has the desired properties stated a t the beginning of this proof.
□
Through Proposition 2.18, and with the notation of (2.3.1), there is t he functor between over
∞-categories
(2.3.3) Ran≤i : Snglrsurj
/X→ Snglrsurj
/ Ran≤i(X)
for each stratiﬁed space X. For the next result, we will denote the full ∞-subcategory
Disk(Bsc)surj,≤i
/X ⊂ Snglrsurj
/X
consisting of those open embeddings֒→X that are surjective on components and for which U
has at most i connected components, each of which is isomorphic to a basic strat iﬁed space.
Lemma 2.20. Leti be a ﬁnite cardinality. Let X be a stratiﬁed space. The functor (2.3.3) restricts
as an equivalence of ∞-categories
Ran≤i : Disk(Bsc)surj,≤i
/X
≃
−−→Bsc/ Ran≤i(X) .
21
Proof. The factorization happens because Ran≤i(U ) is a basic whenever U is an (at most) i-fold
disjoint union of basics – this statement is proved in §3 of [AFT]. We will argue that this functor
is an equivalence by showing it is an equivalence on maximal ∞-subgroupoids, then that it is an
equivalence on spaces of morphisms.
Keeping with the notation of [AFT], for each stratiﬁed space Z we will denote the over∞-category
Entr(Z) := Bsc/Z
of basic stratiﬁed spaces over Z. In §4 of [AFT] we show that, for Z a stratiﬁed space, the maximal
∞-subgroupoid of Entr(Z) is ∐
[B]
Entr[B](Z) where the coproduct is indexed by isomorphism classes
of basics, and Entr[B](Z) = B End(B)/Z is the ∞-subcategory of those basics over Z which are
isomorphic toB. Also in§4 of [AFT] we show that Entr[B](Z)≃ Emb
(
B,Z
)
Aut0(B) is the coinvariants
by the origin preserving automorphisms of B, and thereafter that this latter space evaluates at the
center of B as an equivalence with the underlying space of the [ B]-stratum Z[B]⊂Z. In summary,
the maximal∞-subgroupoid of Entr(Z) is canonically identiﬁed as
∐
[B]
Entr[B](Z) ≃
∐
[B]
Z[B] .
Similarly, the maximal ∞-subgroupoid of Disk(Bsc)surj,≤i
/Z is canonically identiﬁed as
∐
[U]
∏
α∈A
Disk(Bsc[Uα])surj,=iα
/X ≃
∐
[U]
∏
α∈A
Conf Iα(W[Uα])Σ Iα
which we now explain. The coproducts are indexed by isomorphism clas ses of ﬁnite disjoint unions
of basics U = ⨆
α∈A
(Uα)⊔Iα, grouped here according to isomorphism type, for which ∑
α∈A
|Iα|≤ i.
Bsc[Uα] is the full ∞-subcategory of Bsc consisting of those basics which are isomorphic to Uα; and
iα :=|Iα| is the cardinality. So the left [ U ]-cofactor is the largest ∞-subgroupoid of Disk(Bsc)surj
/X
consisting of those open embeddings֒→X for whichV is isomorphic to an iα-fold disjoint union of
the basic Uα. For M a smooth manifold, Conf J (M ) is the underlying space of the open submanifold
M J consisting of the injections֒→M . The subscript denotes the coinvariants by the evident
Σ J -action.
Thus, the map of maximal∞-subgroupoids induced by the functor Disk(Bsc)surj,≤i
/X
Ran≤i
− −−− →Bsc/ Ran≤i(X)
is canonically identiﬁed as the map of spaces
∐
[U]
∏
α∈A
Conf Iα(X[Uα])Σ Iα ≃
∐
[U]
∏
α∈A
Disk(Bsc[Uα])surj,=iα
/X −→
∐
[B]
Entr[B]
(
Ran≤i(X)
)
≃
∐
[B]
(
Ran≤i(X)
)
[B]
in where the indexing set of the left coproduct consists of those su ch isomorphism classes [ U ] for
which U has at most i components. Lemma 2.19 grants that this map is a bijection on the se ts
indexing the coproducts. That this map of spaces is an equivalence t hen follows because, by detailed
inspection, there is a canonical isomorphism of stratiﬁed spaces
∏
α∈A
ConfIα (X[Uα])Σ Iα
∼=
(
Ran≤i(X)
)
[Ran≤i(U)]
whose map of underlying spaces is a summand of the above composite map.
22
We now consider the map of spaces of morphisms induced by the func tor Disk(Bsc)surj,≤i
/X
Ran≤i
−−−− →
Entr
(
Ran≤i(X)
)
. This map ﬁts as the top horizontal arrow in the diagram of spaces
Map
(
[1], Disk(Bsc)surj,≤i
/X
) /d47/d47
ev1
/d15/d15
Map
(
[1], Entr
(
Ran≤i(X)
) )
ev1
/d15/d15(
Disk(Bsc)surj,≤i
/X
) ∼ /d47/d47
(
Entr
(
Ran≤i(X)
) ) ∼
.
We have already shown that the bottom horizontal map is an equivale nce of spaces. To show that
the top horizontal map is an equivalence of spaces, it is enough to sh ow that, for each point (֒→X)
of the bottom left space, the map of associated ﬁbers is an equivale nce.
Let (֒→X) ∈ Disk(Bsc)surj,≤i
/X . Both Disk(Bsc)surj,≤i
/X and Entr
(
Ran≤i(X)) being slice- ∞-
categories, we canonically identify the map of ﬁbers over (֒→X) as the map of maximal ∞-
subgroupoids (
Disk(Bsc)surj,≤i
/U
) ∼
−→
(
Entr
(
Ran≤i(U )
) ) ∼
induced by Ran≤i. We have already shown that this map is an equivalence, and so conclu des this
proof.
□
