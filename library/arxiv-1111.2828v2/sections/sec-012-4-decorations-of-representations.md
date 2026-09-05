---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-012-4-decorations-of-representations
section_title: "Decorations of representations"
section_number: 4
pages: 13-14
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
---
In this section we review the notion of decorated representa tions introduced in Zickert [ 30].
Throughout the section, G denotes an arbitrary group, not necessarily a Lie group. Let H be
subgroup of G. An ordered simplex is a simplex with a ﬁxed vertex ordering.
Deﬁnition 4.1. A closed 3-cycle is a cell complex K obtained from a ﬁnite collection of ordered
3-simplices ∆ i by gluing together pairs of faces using order preserving sim plicial attaching maps.
We assume that all faces have been glued, and that the space M (K), obtained by truncating the
∆ i’s before gluing, is an oriented 3-manifold with boundary. Let ǫi be a sign indicating whether or
not the orientation of ∆ i given by the vertex ordering agrees with the orientation of M (K).
Note that up to removing disjoint balls (which does not eﬀect the fundamental group), the
manifold M (K) only depends on the underlying topological space of K, and not on the choice of
3-cycle structure. Also note that for any compact, oriented 3-manifold M with (possibly empty)
boundary, the space ˆM obtained from M by collapsing each boundary component to a point has a
structure of a closed 3-cycle K such that M = M (K).
14 STA VROS GAROUF ALIDIS, DYLAN P. THURSTON, AND CHRISTIAN K . ZICKERT
Let K be a closed 3-cycle, and let M = M (K). Let L denote the space obtained from the
universal cover ~M of M by collapsing each boundary component to a point. The 3-cycle structure
of K induces a triangulation of L, and also a triangulation of M by truncated simplices. The
covering map extends to a map L → K, and the action of π1(M ) on ~M by deck transformations
extends to an action on L, which is determined by ﬁxing, once and for all, a base point i n M
together with one of its lifts. Note that the stabilizer of ea ch zero cell is a peripheral subgroup of
π1(M ), i.e. a subgroup induced by inclusion of a boundary componen t.
Deﬁnition 4.2. Let H be a subgroup of G. A representation ρ : π1(M ) → G is a (G, H)-
representation if the image of each peripheral subgroup is a conjugate of H.
Deﬁnition 4.3. Let ρ be a (G, H)-representation. A decoration (on K) of ρ is a ρ-equivariant
assignment of a left H-coset to each vertex of L, i.e. if α ∈ π1(M ) and the coset geH is assigned to
e, the coset assigned to αe must be ρ(α)geH.
Note that g−1
e ρ(Stab(e))ge ⊂ H, where Stab(e) is the stabilizer of e.
Deﬁnition 4.4. Two decorations {geH} and {g′
eH} of ρ are equivalent if the corresponding sub-
groups g−1
e ρ(Stab(e))ge and g′−1
e ρ(Stab(e))g′
e of H are conjugate (in H).
Note that if {geH} is a decoration of ρ, then {ggeH} is a decoration of gρg−1. Since we are only
interested in representations up to conjugation, we consid er such two decorations to be equal.
Remark 4.5. Letting NG(H) denote the normalizer of H in G, and h the number of boundary
components of M , right multiplication induces an action of (NG(H)/H)h on the set of equivalence
classes of decorations. If G = SL( n, C) and H = N , NG(H)/H, is the group of diagonal matrices,
and since two subgroups of N are conjugate if and only if they are conjugate by an element i n the
Borel subgroup B of upper diagonal matrices, this action is transitive.
Proposition 4.6. Let E be a ﬂat G-bundle over M whose holonomy representation is a (G, H)-
representation ρ. There is a 1-1 correspondence between decorations of ρ up to equivalence, and
reductions of E∂M to an H-bundle over ∂M .
Proof. For each boundary component Si of M , choose a base point in Si and a path to the base point
of M . This determines a lift ei in L of the vertex of K corresponding to Si, and an identiﬁcation
of π1(Si) with Stab(ei) ⊂ π1(M ). If F is a reduction of E∂M , the holonomy representations
ρi : π1(Si) → H of FSi are conjugate to ρ, so there exist gi ∈ G such that g−1
i ρgi = ρi. Assigning
the coset giH to ei yields a decoration, which up to equivalence is independent of the choice of gi’s.
On the other hand, a decoration assigns cosets giH to ei such that g−1
i ρ(Stab(ei))gi ⊂ H. Hence,
gi deﬁnes an isomorphism of ESi with an H-bundle, which up to isomorphism only depends on the
equivalence class of the decoration. □
