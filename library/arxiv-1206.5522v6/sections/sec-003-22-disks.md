---
doc_id: arxiv-1206.5522v6
doc_title: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS"
section_id: sec-003-22-disks
section_title: "Disks"
section_number: 2.2
pages: 9-11
source_pdf: 1206.5522v6.pdf
source_sha256: 6e992242435b5e9f
doc_brief: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS — Factorization homology theories of topological manifolds , after Beilinson, Drinfeld and Lurie, are homology-type theories for topological"
---
maximal∞-subgroupoid of DiskB
n/M, B-framed n-disks embedding into a B-framed n-manifold.
Deﬁnition 2.9. The symmetric monoidal ∞-category DiskB
n is the full ∞-subcategory of MﬂdB
n
whose objects are disjoint unions of B-framed n-dimensional Euclidean spaces.
Remark 2.10. Consider∗→ BTop(n), the basepoint of BTop(n). A ∗-structure on an n-manifold
M is then equivalent to a topological framing of the tangent microbund le τM of M ,4 and we denote
the associated∞-category of framed n-disks as Diskfr
n. This symmetric monoidal ∞-category Diskfr
n
is homotopy equivalent to the PROP associated to the En operad of Boardman-Vogt [BV]. This
follows because the inclusion of rectilinear embeddings as framed emb eddings determines a homotopy
equivalence En(I)
∼
− →Embfr(⨆
I Rn, Rn) from the I-ary space of the En operad.
Example 2.11. For B = BO(n), with the usual map BO(n)→ BTop(n), the ∞-category of topo-
logical n-disks with BO(n)-framings is equivalent to the ∞-category of smooth n-disks and smooth
embeddings, Disksm
n ≃ DiskBO(n)
n . These are both equivalent to the PROP associated to the unori-
ented version of the ribbon, or “framed,” En operad; see [SW] for a treatment of this operad. 5 To see
these equivalences it is enough to explain why each of the natural ma ps O(n)→ Embsm(Rn, Rn)→
EmbBO(n)(Rn, Rn) is an equivalence. Smoothing theory ([KS]) gives the equivalence of t he second
map. Via Gram–Schmidt, the inclusion O(n)
≃
− →GL(Rn) is a deformation retraction. Conju-
gation by scaling and translation, ( f, t)↦→
(
x↦→ f (tx)−f (0)
t + f (0)
)
, demonstrates the inclusion
GL(Rn)
≃
− →Embsm(Rn, Rn) as a deformation retraction.
Given a topological space X and a ﬁnite cardinality i, we let Conf i(X)⊂ X i denote the subspace
of those maps {1, . . . , i}→ X which are injective. This conﬁguration space has an evident free
action of the symmetric group Σ i.
In the next result, for M a B-framed n-manifold, we consider the over ∞-category
DiskB
n/M := DiskB
n ×
MﬂdB
n
MﬂdB
n/M .
Informally, an object is an embedding ⊔
i
Rn֒→M for some i.
Lemma 2.12. The maximal ∞-subgroupoid of DiskB
n is canonically identiﬁed as the space
∐
i≥0
Bi
Σ i ≃
(
DiskB
n
) ∼
where the coproduct is indexed by ﬁnite cardinalities and ea ch cofactor is the Σ i-homotopy coin-
variants of the i-fold product of the space B. In particular, the symmetric monoidal functor
[−] : DiskB
n→ Fin, given by taking sets of connected components of underlying manifolds, is conser-
vative.
For M a B-framed n-manifold, the maximal ∞-subgroupoid of DiskB
n/M is canonically identiﬁed
as the space ∐
i≥0
Conf i(M )Σ i ≃
(
DiskB
n/M
) ∼
where the coproduct is indexed by ﬁnite cardinalities, and e ach cofactor is an unordered conﬁguration
space.
4By smoothing theory, framed topological manifolds are esse ntially equivalent to framed smooth manifolds except
in dimension 4.
5The historical use of “framed” here is potentially misleadi ng, since in the “framed” En operad the embeddings
do not preserve the framing, while in the usual En operad the embeddings do preserve the framing (up to scale). It
might lead to less confusion to replace the term “framed En operad” with “unoriented En operad.”
9
Proof. Lemma 2.5 gives an equivalence DiskB
n/M≃ Diskn/M. So it suﬃces to assume the case of an
equality B = BTop(n).
The maximal ∞-subgroupoid of Diskn necessarily lies over the maximal ∞-subgroupoid of Fin,
which is ∐
i≥0
BΣ i. The ﬁrst assertion will be implied upon verifying, for each i≥ 0, that the map
Σ i≀ Top(n)−→ Emb(⊔
i
Rn,⊔
i
Rn)
is weakly homotopy equivalent to an inclusion of connected componen ts. This is an immediate
consequence of the Kister–Mazur Theorem 2.3. Via translation, th e inclusion of the subgroup
of origin preserving homeomorphisms Top0(n)
≃
− →Top(n) is a homotopy equivalence, and so we
recognize further the identiﬁcation
∐
i≥0
B(Σ i≀ Top0(n))
≃
−−→(Diskn)∼ .
Because the projection Diskn/M → Diskn is a right ﬁbration, we recognize the maximal ∞-
subgroupoid of Diskn/M as
∐
i≥0
Emb
(
⊔
i
Rn, M
)
Σ i≀Top0(n)
≃
−−→(Diskn/M)∼ .
Therefore, the second assertion follows upon showing that the Σ i-equivariant continuous map
ev0 : Emb
(
⊔
i
Rn, M
)
Top0(n)i−→ Confi(M )
is a weak homotopy equivalence. This is implied upon showing the homoto py ﬁber of the continuous
map
ev0 : Emb(⊔
i
Rn, M)−→ Conf i(M )
is weakly homotopy equivalent to Top0(n)i. In a standard manner, this map is a Serre ﬁbration,
and the ﬁber over c :{1, . . . , i}֒→M is the space Emb0(⊔
i
Rn, M) of embeddings under c. Fix such
a based embedding e0 : ⊔
i
Rn֒→M . So we must show that the composite inclusion
Top0(n)i֒→Emb((0∈ Rn), (0∈ Rn))i∼= Emb0(⊔
i
Rn,⊔
i
Rn)
−◦e0
−−−→Emb0(⊔
i
Rn, M)
is a weak homotopy equivalence.
The Kister–Mazur Theorem gives that the ﬁrst of these maps is a ho motopy equivalence. The
problem is thus reduced to showing that the second of these maps is a weak homotopy equivalence.
This is the problem of showing that each solid diagram among topologica l spaces
Sk−1 f0 /d47/d47
/d15/d15
Emb0(⊔
i
Rn,⊔
i
Rn)
/d15/d15
Dk
f
/d47/d47
~f
/d54/d54♠♠♠♠♠♠♠♠ Emb0(⊔
i
Rn, M)
admits a ﬁller with respect to which the diagram commutes up to homot opy. Choose a continuous
map φ : (0 , 1]× Rn→ Rn such that φt is an origin preserving open embedding for each t, φ1 = idRn ,
the closure φs(Rn)⊂ φt(Rn) whenever s < t , and the collection of images {φt(Rn)| 0 < t≤ 1} is a
basis for the topology about 0 ∈ Rn. Choose a continuous map Dk ǫ
− →(0, 1] for which the restriction
ǫ|Sk−1≡ 1 is identically one, and the composition
Dk f
−−→Emb0(⊔
i
Rn, M)
(⊔
i
φǫ)∗
−−−−−→Emb0(⊔
i
Rn, M)
10
factors through Emb0(⊔
i
Rn,⊔
i
Rn). Deﬁne ~f to be this factorization. By construction, the restric-
tion ~f|Sk−1 = f0. The map [0 , 1]× Dk → Emb0(⊔
i
Rn, M) given by ( t, p)↦→f◦ (⊔
i
φtǫ+(1−t))∗(p)
demonstrates a homotopy making the lower triangle commute.
□
We conclude this section by justifying the term tangent classiﬁer for the functor Mﬂdn
τ
− →
Spaces/ BTop(n) of (1).
Corollary 2.13. The value of the tangent classiﬁer (1) on a topological n-manifold M is the map
of spaces M
τM
−−→BTop(n) classifying the tangent microbundle.
Proof. Recognize Eucn⊂ Diskn as the full ∞-subcategory consisting of the connected n-manifolds.
Specialize the second statement of Lemma 2.12 to i = 1 to obtain an identiﬁcation
M ≃ Eucn/M ≃ Emb(Rn, M)Top(n)−→ BTop(n)
involving the homotopy Top(n)-coinvariants. Manifestly, this map of spaces agrees with the tan gent
classiﬁer in the case M = Rn. By construction, this map is functorial in the argument M∈ Mﬂdn.
The general case follows. □
