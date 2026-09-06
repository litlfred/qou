---
doc_id: arxiv-1206.5522v6
doc_title: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS"
section_id: sec-005-24-localizing-with-respect-to-isotopy-equivalenc
section_title: "Localizing with respect to isotopy equivalences"
section_number: 2.4
pages: 12-14
source_pdf: 1206.5522v6.pdf
source_sha256: 6e992242435b5e9f
doc_brief: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS — Factorization homology theories of topological manifolds , after Beilinson, Drinfeld and Lurie, are homology-type theories for topological"
---
DiskB
n/M is a localization of its un-topologized version DiskB
n/M on the collection of those inclusions
of ﬁnite disjoint unions of disks U⊂ V in M that are isotopic to an isomorphism. This comparison
plays a fundamental role in recognizing certain colimit expressions in t his theory, for instance those
that support the pushforward formula of §3.4.
Deﬁnition 2.18. The ordinary symmetric monoidal category Mﬂdn is that for which an object is
a topological n-manifold, and a morphism is an open embedding between two such; co mposition is
composition of maps, and the symmetric monoidal structure is given by disjoint union. Likewise,
the ordinary symmetric monoidal category Diskn⊂ Mﬂdn is the full subcategory consisting of those
topological n-manifolds that are homeomorphic to a ﬁnite disjoint union of Euclidea n spaces.
Notice the natural functors
Diskn−→ Diskn and Mﬂdn−→ Mﬂdn
which are symmetric monoidal. We denote the pullback symmetric mono idal∞-categories
DiskB
n
/d15/d15
/d47/d47 DiskB
n
/d15/d15
MﬂdB
n /d47/d47
/d15/d15
MﬂdB
n
/d15/d15
Diskn /d47/d47 Diskn and Mﬂdn /d47/d47 Mﬂdn .
For each topological n-manifold M , we denote the ∞-subcategory
(2) IM ⊂ DiskB
n/M := DiskB
n ×
Mﬂd B
n
MﬂdB
n/M
consisting of the same objects but only those morphisms (֒→M )֒→( ֒→M ) whose image in
DiskB
n/M is an equivalence.
Proposition 2.19. The functor DiskB
n/M−→ DiskB
n/M witness a localization of ∞-categories:
(
DiskB
n/M
)
[I−1
M ] ≃ DiskB
n/M .
Proof. Manifestly, the functor is essentially surjective, and it carries the ∞-subcategory IM to the
maximal∞-subgroupoid
(
DiskB
n/M
) ∼
. There results a functor
(
DiskB
n/M
)
[I−1
M ]→ DiskB
n/M from the
localization. We will argue that this functor is an equivalence by showin g it is an equivalence on
maximal∞-subgroupoids, then that it is an equivalence on spaces of morphism s. After Lemma 2.5,
it is enough to consider the case of B = BTop(n). We will adopt the following notation for this
proof:
DM := Diskn/M and DM := Diskn/M .
The maximal ∞-subgroupoid of DM is the classifying space BIM . In light of the coproduct
expression in Lemma 2.12, ﬁx a cardinality i≥ 0. Consider the full subcategory Ii
M⊂ IM consisting
of those (֒→M ) for which the cardinality of the connected components |[U ]| = i. We thus seek
to show that the resulting functor Ii
M→ Conf i(M )Σ i witnesses an equivalence from the classifying
12
space. We explain the following sequence of weak homotopy equivalen ces
BIi
M ≃ colim
(֒→M)∈Ii
M
(Rn)i
≃
− →p.s.colim
(֒→M)∈Ii
M
(Rn)i
∼=− →Conf i(M )Σ i
where p.s.colim denotes the ordinary point-set colimit of topological spaces. The ﬁ rst equivalence is
formal, because each term in the homotopy colimit is contractible. By inspection, the category Ii
M
forms a basis for the standard Grothendieck topology on Confi(M )Σ i . The third homeomorphism
follows. Because Confi(M )Σ i is paracompact, Corollary 1.6 of [DI] gives that the second map is a
weak homotopy equivalence. In summary, we have veriﬁed that the map of maximal∞-subgroupoids
(
DM [I−1
M ]
) ∼ ≃
−−→
(
DM
) ∼
is an equivalence.
We now show that the functor from the localization induces an equiva lence on spaces of mor-
phisms. Consider the diagram of spaces
(
DU [I−1
U ]
) ∼ /d47/d47
(֒→M)
/d15/d15
D∼
U
(֒→M)
/d15/d15(
DM [I−1
M ]
) (1) /d47/d47
ev1
/d15/d15
D(1)
M
ev1
/d15/d15(
DM [I−1
M ]
) ∼ /d47/d47 D∼
M
where a superscript (1) indicates a space of morphisms, and the upper vertical arrows are given as
(֒→U )↦→
(
(֒→M )֒→( ֒→M )
)
. Our goal is to show that the middle horizontal arrow is
an equivalence. We will accomplish this by showing that the diagram is a m ap of homotopy ﬁber
sequences, for we have already shown that the top and bottom ho rizontal maps are equivalences.
The right vertical sequence is a ﬁber sequence is because such eva luation maps are coCartesian
ﬁbrations, in general. Then, by inspection, the ﬁber over (֒→M ) is the maximal ∞-subgroupoid
of the over ∞-category ( DM )/(֒→M). This over ∞-category is canonically identiﬁed as DU .
We now show that the left vertical sequence is a homotopy ﬁber seq uence. The space of morphisms(
DM [I−1
M ]
) (1)
is the classifying space of the subcategory of the functor catego ry FunIM
(
[1], DM
)
⊂
Fun
(
[1], DM
)
consisting of the same objects but only those natural transform ations by I. We claim
the ﬁber over (֒→M ) of the evaluation map is canonically identiﬁed as in the sequence
(
DU [I−1
U ]
) ∼ (֒→M)
−−−−−−→
(
DM [I−1
M ]
) (1) ev1
−−−→
(
DM [I−1
M ]
) ∼
.
This claim is justiﬁed through Quillen’s Theorem B, for the named ﬁber is the classifying space
of the over ∞-category ( IM )/(֒→M) which is canonically isomorphic to IU . To apply Quillen’s
Theorem B we must show that each morphism (֒→M )֒→( ֒→M ) in I induces an equivalence
of spaces B
(
(IM )/(֒→M)
)
≃ B
(
(IM )/(֒→M)
)
. This map of spaces is canonically identiﬁed as the
map BIU→ BIV induced from the inclusion֒→V , which, by design, is a bijection on connected
components. Through the previous analysis of this proof, this map is further identiﬁed as the map
of spaces֒→V . The Kister–Mazur Theorem 2.3 implies this inclusion֒→V is isotopic to
an isomorphism, from which it follows that the map of spaces BIU
≃
− →BIV is an equivalence. We
conclude that Quillen’s Theorem B applies. (For an ∞-categorical account of Quillen’s Theorem B,
see for instance Theorem 5.3 of [Bar].) □
13
Remark 2.20. Proposition 2.19 implies that, for each symmetric monoidal ∞-category V, the re-
striction functor AlgDiskB
n
(V)→ AlgDiskB
n
(V) is fully faithful and the essential image consists of the
locally constant DiskB
n -algebras. This result also appears in [Lu2] as Theorem 5.4.5.9.
Proposition 2.19 oﬀers the following construction.
Construction 2.21. Let f : M→ N be a continuous map from a B-framed n-manifold to a B′-
framed k-manifold, possibly with boundary. Given a regularity condition on f , we will produce a
composite map of colored operads
f −1 : Disk∂,B ′
k/N−→ MﬂdB
n/M−→ MﬂdB
n/M .
The second functor is the standard one. To describe the ﬁrst fun ctor we make use of Lemma 2.5
so that we can assume the maps B→ BTop(n) and B′→ BTop(k) are equivalences. For this case,
the ﬁrst functor is given by (֒→N )↦→(U×
N
֒→M ), which is evidently functorial as well as
monoidal.
Suppose the two restrictions
f| : f −1(N /i⋉tegerdivide∂N )→ N /i⋉tegerdivide∂N and f| : f −1(∂N )→ ∂N
are manifold bundles. Then, by inspection, this functor f −1 carries isotopy equivalences to equiva-
lences. Through Proposition 2.19, there results a multi-functor
(3) f −1 : DiskB′
k/N−→ MﬂdB
n/M .
