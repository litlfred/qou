---
doc_id: arxiv-1006.3501v5
doc_title: "On two approaches to 3-dimensional TQFTs"
section_id: sec-006-6-state-sums-on-skeletons-of-3-manifolds
section_title: "State sums on skeletons of 3-manifolds"
section_number: 6
pages: 14-16
source_pdf: 1006.3501v5.pdf
source_sha256: e939aec50387ce2d
toc_source: outline
doc_brief: "On two approaches to 3-dimensional TQFTs — W e prove that|M |C = τZ(C)(M ) for any closed oriented 3-manifold M and for any spherical fusion category C of non-zero dimension."
---
We compute |M|C as a state sum on any skeleton of M . This generalizes the
state sums of Section 5 and of [TV, BW1]. We begin with topological pre liminaries.
6.1. Stratiﬁed 2-polyhedra. By a 2-polyhedron, we mean a compact topological
space that can be triangulated using only simplices of dimension ≤ 2. For a 2-
polyhedron P , denote by Int(P ) the subspace of P consisting of all points having a
neighborhood homeomorphic to R2. Clearly, Int(P ) is an (open) 2-manifold without
boundary. By an arc in P , we mean the image of a path α : [0, 1]→ P which is
an embedding except that possibly α(0) = α(1). (Thus, arcs may be loops.) The
points α(0), α(1) are the endpoints and the set α((0, 1)) is the interior of the arc.
To work with polyhedra, we will use the language of stratiﬁcations as follows.
Consider a 2-polyhedron P endowed with a ﬁnite set of arcs E such that
(a) diﬀerent arcs in E may meet only at their endpoints;
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 15
(b) P\∪ e∈Ee⊂ Int(P ) and P\∪ e∈Ee is dense in P .
The arcs of E are called edges of P and their endpoints are called vertices of P .
The vertices and edges of P form a graph P (1) =∪e∈Ee. Since all vertices of P
are endpoints of the edges, P (1) has no isolated vertices. Cutting P along P (1),
we obtain a compact surface ~P with interior P\P (1). The polyhedron P can be
recovered by gluing ~P toP (1) along a map p : ∂~P→P (1). Condition (b) ensures the
surjectivity of p. We call the pair ( P,E ) (or, shorter, P ) a stratiﬁed 2-polyhedron if
the setp−1(the set of vertices of P ) is ﬁnite and each component of the complement
of this set in ∂~P is mapped homeomorphically onto the interior of an edge of P .
A 2-polyhedron P can be stratiﬁed if and only if Int( P ) is dense in P . For such
aP , the edges of any triangulation form a stratiﬁcation. Another exa mple: a closed
surface with an empty set of edges is a stratiﬁed 2-polyhedron.
For a stratiﬁed 2-polyhedron P , the connected components of ~P are called regions
of P . Clearly, the set Reg( P ) of the regions of P is ﬁnite. For a vertex x of P ,
a branch of P at x is a germ at x of a region of P adjacent to x. (Formally, the
branches of P at x can be deﬁned as paths γ : [0, 1]→ P such that γ(0) = x and
γ((0, 1])⊂P\P (1), considered up to homotopy in the class of such paths.) The set
of branches of P at x is ﬁnite and non-empty. The branches of P at x bijectively
correspond to the elements of the set p−1(x), where p : ∂~P→P (1) is the map above.
Similarly, for an edge e of P , a branch of P at e is a germ at e of a region of P
adjacent to e. (A formal deﬁnition proceeds in terms of paths γ : [0, 1]→ P such
thatγ(0) lies in the interior of e andγ((0, 1])⊂P\P (1).) The set of branches of P
at e is denoted Pe. This set is ﬁnite and non-empty. There is a natural bijection
betweenPe and the set of connected components of p−1(interior ofe). The number
of elements of Pe is the valence ofe. The edges of P of valence 1 and their vertices
form a graph called the boundary ofP and denoted ∂P . We say that P is orientable
(resp. oriented) if all regions of P are orientable (resp. oriented).
6.2. Skeletons of closed 3-manifolds. A skeleton of a closed 3-manifold M is an
oriented stratiﬁed 2-polyhedron P⊂M such that ∂P =∅ and M\P is a disjoint
union of open 3-balls. An example of a skeleton of M is provided by the (oriented)
2-skeletont(2) of a triangulation t of M , where the edges of t(2) are the edges of t.
Any vertex x of a skeleton P⊂M has a closed ball neighborhood Bx⊂M such
that Γ x =P∩∂Bx is a ﬁnite non-empty graph and P∩Bx is the cone over Γ x. The
vertices of Γ x are the intersections of ∂Bx with the half-edges of P incident tox; the
edges of Γ x are the intersections of ∂Bx with the branches of P atx. The condition
∂P =∅ implies that every vertex of Γ x is incident to at least two half-edges of Γ x.
The pair ( ∂Bx, Γ x) is determined by the triple ( M,P,x ) up to homeomorphism.
This pair is the link of x in (M,P ). If M is oriented, then we endow ∂Bx with
orientation induced by that of M restricted toM\Int(Bx). Then the link ( ∂Bx, Γ x)
of x is determined by ( M,P,x ) up to orientation preserving homeomorphism.
6.3. Computation of|M|C. LetC andI be as in Section 5.2 and let M be a closed
oriented 3-manifold. We compute |M|C∈ k as a state sum on any skeleton P ofM .
For a map c : Reg(P )→ I and an oriented edge e of P , we deﬁne a k-module
Hc(e) = H(Pe), where Pe is the set of branches of P ate turned into a cyclic C- set
as te in Section 5.2. Here by the c-color of a branch b∈ Pe, we mean the c-color
of the region of P containing b. If eop is the same edge with opposite orientation,
then Peop = (Pe)op. This induces a duality between the modules Hc(e), Hc(eop)
and a contraction ∗e : Hc(e)⋆⊗Hc(eop)⋆→ k.
As in Section 5.2, the link of a vertex x∈P determines aC-colored graph Γ x in
∂Bx≃S2. An example of Γ x is given in Figure 2; note that since the orientation
of∂Bx is induced by that of M restricted to M\ Int(Bx), the identiﬁcation of ∂Bx
16 V. TURAEV AND A. VIRELIZIER
PSfrag replacements
i
i
jj kk
ll
m
m
n
n
q
q
p
p
s
s
t
t
x
1
23
Γ x =
Figure 2. The graph Γ x⊂S2 associated with a vertex x
with the standard 2-sphere S2 = R2∪{∞} (oriented counterclockwise) requires in
this example a mirror reﬂection.
Section 3.3 yields a tensor FC(Γ x)∈Hc(Γ x)∗. By deﬁnition, Hc(Γ x) =⊗eHc(e),
wheree runs over all edges ofP incident tox and oriented away fromx (an edge with
both endpoints in x appears in this tensor product twice with opposite orientations).
The tensor product⊗x FC(Γ x) over all verticesx ofP is a vector in⊗eHc(e)⋆, where
e runs over all oriented edges of P . Set ∗P =⊗e∗e :⊗e Hc(e)⋆→ k. The following
theorem will be proved in Section 7.
Theorem 6.1. For any skeleton P of M ,
(9) |M|C = (dim(C))−|P |∑
c

 ∏
r∈Reg(P )
(dimc(r))χ(r)

∗P (⊗x FC(Γ x))∈ k,
where|P| is the number of components of M\P ,c runs over all maps Reg(P )→I,
and χ(r) is the Euler characteristic of r.
Formula (8) is a special case of (9) for the oriented 2-skeleton P = t(2) of a
triangulationt of M . When P is the oriented 2-skeleton of the cellular subdivision
of M dual to t and the orientation of P is induced by that of M and a total
order on the set of vertices of t, Formula (9) is equivalent to the Turaev-Viro-
Barrett-Westbury state sum on t. Theorem 6.1 implies that our deﬁnition of |M|C
is equivalent to the one in [BW1].
We illustrate Theorem 6.1 with two examples. An oriented 2-sphere em bed-
ded in S3 is a skeleton of S3 with void set of edges and vertices and one region.
Formula (9) gives |S3|C = (dim(C))−2∑
i∈I (dim(i))2 = (dim(C))−1. Pick a point
x∈S1 and a circle ℓ⊂S2. The set P = ({x}×S2)∪(S1×ℓ) is a skeleton of S1×S2
with one edge {x}× ℓ viewed as a loop; the orientation of the three regions of P is
arbitrary. Formula (9) and the second formula of Lemma 4.3 give |S1×S2|C = 1.
