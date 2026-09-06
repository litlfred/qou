---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-003-21-disk-algebras
section_title: "Disk algebras"
section_number: 2.1
pages: 14-17
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homol ogy, or topological chiral homology, at the generality of stratiﬁed spaces with tangen tial"
---
Factorization homology will have a universal property with respect to monoidal and operadic struc-
tures on Mﬂd(B) and Mﬂd(B)/X , which we present below in Constructions 2.1 and 2.4.
Construction 2.1 (The symmetric monoidal structures on Mﬂd(B) and Disk(B)). Using disjoint
union, we endow Snglr, Snglr, Mﬂd(B), and Mﬂd(B) with natural symmetric monoidal structures.
The details are as follows: Disjoint union makes each of the Kan-enriched categories Snglr and
Snglr into a symmetric monoidal Kan-enriched category in the usual sense. We then realize each as
14
a symmetric monoidal ∞-category (by taking the simplicial nerve, for instance – see Propo sition
2.1.1.27 of [Lu2]).
To further endow Mﬂd(B) and Mﬂd(B) with symmetric monoidal structures, recall that they are
deﬁned via limit diagrams as below
Mﬂd(B) /d47/d47
/d15/d15
Mﬂd(B) /d47/d47
/d15/d15
PShv(Bsc)/B
/d15/d15
Snglr /d47/d47 Snglr τ /d47/d47 PShv(Bsc)
where the functor τ is the tangent classiﬁer, i.e., the restriction of the Yoneda embeddin g to basics.
In light of Lemma 1.12, to endow Mﬂd(B) with a symmetric monoidal structure it suﬃces to
lift the diagram among ∞-categories Snglr → PShv(Bsc) ← PShv(Bsc)/B to a diagram among
symmetric monoidal ∞-categories; this is easily accomplished. Both PShv(Bsc) and PShv(Bsc)/B
are cocomplete and hence carry a coCartesian monoidal structur e (i.e., the monoidal structure
given by coproducts); since the forgetful functor PShv(Bsc)/B→ PShv(Bsc) preserves colimits, it in
particular preserves coproducts, and is thus symmetric monoidal with respect to this coCartesian
monoidal structure. Now, because each basic U is connected, there is a canonical isomorphism of
Kan complexes ∐
i∈I
Snglr(U,M i)
∼=−−→Snglr
(
U,
⨆
i∈I
Mi
)
.
So Snglr
τ
− →PShv(Bsc) canonically extends as a symmetric monoidal functor.
Finally, since Snglr→ Snglr preserves disjoint union, through the same logic Mﬂd(B) obtains a
symmetric monoidal structure.
Deﬁnition 2.2. The symmetric monoidal ∞-categories
Disk(B) ⊂ Mﬂd(B) and Disk(B) ⊂ Mﬂd(B)
are smallest full symmetric monoidal subcategories containing B⊂ Mﬂd(B) and B ×
Mﬂd(B)
Mﬂd(B)⊂
Mﬂd(B), respectively.
Remark 2.3. The objects of Disk(B) are disjoint unions of elements of B.
The slice categories Disk(B)/X and Mﬂd(B)/X do not carry symmetric monoidal structures –
for instance, there is no natural way to take a disjoint union of two embeddings if the embeddings
overlap. Regardless, we endow these categories with the structu re of an ∞-operad. As usual (see
Section 2.1 of [Lu2]), one can think of these ∞-operads as colored operads, one color for every
embedding of a ﬁnite disjoint union of basics֒→X.
Construction 2.4 (Disk(B)/X as an ∞-operad). The empty stratiﬁed space ∅ is a symmetric
monoidal unit for Snglr and Snglr, and it is also initial in each of the associated underlying ∞-
categories. It follows that the same is true for the symmetric mono idal structures on Mﬂd(B) and
Mﬂd(B). Let X be a B-manifold. Notation 1.21 produces the ∞-operads Mﬂd(B)/X and Mﬂd(B)/X
as well as Disk(B)/X and Disk(B)/X .
Example 2.5. The ﬁber of the ∞-operad Snglr/X over the ﬁnite set ∗+ is an ∞-category whose
objects are conically smooth open embeddings (֒→X), where Y is a connected stratiﬁed space.
A morphism (֒→X)→ (Y ′֒→X) is speciﬁed by a conically smooth open embedding֒→Y ′
and an isotopy from֒→X to the composite֒→Y ′֒→X. A multi-morphism from
(
(Y1֒→
X), (Y2֒→X)
)
to (֒→X) is a conically smooth open embedding Y1⊔Y2֒→Y from the disjoint
union, together with a pair of isotopies γν :Yν×[0, 1]→X from the givenYν֒→X to the composition
Yν֒→Y1⊔Y2֒→X. Notice that this last composition makes use of ∅ being both initial and the
symmetric monoidal unit.
15
Remark 2.6. We caution the reader about a notational conﬂict: There are equiv alences
(
Disk(B)/X
)
|∗+
≃ Disk(B)/X and
(
Mﬂd(B)/X
)
|∗+
≃ Mﬂd(B)/X .
Here, the lefthand side of each equivalence is the underlying ∞-category of the∞-operad deﬁned in
Construction 2.4, while the righthand side is the ∞-category of disks/ B-manifolds equipped with a
map to X. Furthermore, the maps of ∞-operads
Disk(B)/X→ Disk(B) and Mﬂd(B)/X→ Mﬂd(B)
restrict to the standard functors on underlying ∞-categories.
Observation 2.7. LetX = (X,g ) be a B-manifold. Then the ∞-operad Disk(B)/X is independent
of the B-structure on the underlying stratiﬁed space of X. More precisely, because B→ Bsc is a
right ﬁbration, then the map
Disk(B)/X
≃
−−→Disk(Bsc)/X
is an equivalence of ∞-operads. For the same reason, for (֒→X) a point of Disk(B)/X , there is
a canonical identiﬁcation of ∞-categories
Disk(B)/U ≃
(
Disk(B)/X
)
/(֒→X) .
The analogous assertions hold if replacing Disk(B) by Mﬂd(B).
Notation 2.8. Deﬁned in [AFT] is the category of basics Dn, governing smooth n-manifolds, and
the various elaborations governing smooth n-manifolds with boundary, possibly equipped with a
framing. We use the shorthand notation
Diskn = Disk(Dn) , Diskfr
n = Disk(Dfr
n) , Disk∂
n = Disk(D∂
n) , Diskfr
d⊂n = Disk(Dfr
d⊂n) ,
and likewise for other elaborations on D. For example, the underlying ∞-category of Disk(Dn) is
the∞-category whose objects are diﬀeomorphic to a ﬁnite disjoint union of standard Rn, and whose
morphisms are given by smooth open embeddings between them. The underlying∞-category of
Diskfr
n has objects ﬁnite, disjoint unions of Rn together with a framing. The space of morphisms
between two framed manifolds has the homotopy type of the space of smooth embeddings together
with a choice of homotopy between framings. In all these cases, th e symmetric monoidal structure
is disjoint union.
Notation 2.9. Prompted by the upcoming Proposition 2.12, and by Notation 1.21, we will make
the following notational conventions
AlgDisk(B)(V) := Fun⊗(
Disk(B), V
)
and AlgDisk(B)(V) := Fun⊗(
Disk(B), V
)
and refer to their objects as Disk(B)-algebras and Disk(B)-algebras, respectively.
Remark 2.10. We caution the reader concerning our non-standard notation, wh ich is summarized
as follows.
• As Notation 1.8, we do not distinguish between the notation for a sym metric monoidal
∞-category and its underlying ∞-category.
• As Notation 1.21, we do not distinguish between the notation for cer tain slice∞-categories
and their corresponding ∞-operads.
• As Notation 2.9, we use AlgDisk(B)(V) for symmetric monoidal functors, not just maps of
operads. Likewise for the other variants such as that concerning Mﬂd(B).
• As Notation 1.21 we use AlgX (V) for those maps of ∞-operads Disk(B)/X→ V that send
pre-coCartesian edges to coCartesian edges. Likewise for the other variants such as that
concerning Mﬂd(B).
Example 2.11. A Diskfr
1 -algebra in V is canonically identiﬁed as an A∞-algebra in V.
In what follows, we let En denote the∞-operad of little n-disks.
16
Proposition 2.12. Let V be a symmetric monoidal ∞-category. Let n be a ﬁnite cardinality. There
is a canonical equivalence of ∞-categories
AlgDiskfr
n
(V)
≃
− →AlgEn (V) .
With respect to the given O(n)-action on the righthand side of the above equivalence, ther e is an
equivalence of∞-categories
AlgDiskn (V)
≃
− →AlgEn (V)O(n)
to the O(n)-invariants.
Proof. The evident En-algebra in Diskfr
n induces a symmetric monoidal functor Env(En)→ Diskfr
n
from the symmetric monoidal envelope. The mapping homotopy type s of both sides of this functor
are in terms of the spaces ConfI (Rn) := {֒→Rn}, spaces of injective maps into Rn from ﬁnite
sets. Inspecting this symmetric monoidal functor reveals that it is an equivalence. This gives the
ﬁrst equivalence.
There is the symmetric monoidal right ﬁbration Diskfr
n→ Diskn, which manifestly factors through
the O(n)-invariants. The ﬁber over Rn is canonically identiﬁed as Emb(Rn, Rn)≃ O(n), with the
translation action of O(n). The second equivalence follows.
□
Example 2.13. Consider the category of basics D∂,fr
n . Then a D∂,fr
n manifold is an n-manifold
possibly with boundary, equipped with a framing of the n-manifold and a splitting of the framing
on the boundary as a product framing. Disk∂,fr
n -algebras are equivalent to algebras over the Swiss-
cheese operad of [Vo]; an object can be regarded as a triple ( A,B,α ) of a Diskfr
n-algebra A, a
Diskfr
n−1-algebra B, and a map
α :A−→ HC∗
Dfr
n−1
(B) := Mod
Diskfr
n−1
B (B,B )
which is a map of Diskfr
n-algebras; this reformulation is the higher Deligne conjecture, pro ved in this
generality in [Lu2] and [Th].
2.2. F actorization homology
The following is the main deﬁnition and object of interest in the presen t paper, that of factorization
homology with coeﬃcients in a disk algebra.
Recall Notation 1.21 for the ∞-category of Diskn-algebras.
