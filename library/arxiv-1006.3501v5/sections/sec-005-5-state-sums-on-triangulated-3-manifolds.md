---
doc_id: arxiv-1006.3501v5
doc_title: "On two approaches to 3-dimensional TQFTs"
section_id: sec-005-5-state-sums-on-triangulated-3-manifolds
section_title: "State sums on triangulated 3-manifolds"
section_number: 5
pages: 13-14
source_pdf: 1006.3501v5.pdf
source_sha256: e939aec50387ce2d
toc_source: outline
doc_brief: "On two approaches to 3-dimensional TQFTs — W e prove that|M |C = τZ(C)(M ) for any closed oriented 3-manifold M and for any spherical fusion category C of non-zero dimension."
---
In this section, we derive a topological invariant of closed oriented 3 -manifolds
from a spherical fusion category.
5.1. Preliminaries on triangulated 3-manifolds. LetM be a 3-manifold (with-
out boundary). Let t be a triangulation of M . The simplices of t of dimension 0,
1, 2, 3 are called respectively vertices, edges, faces, and tetrah edra. For a vertex x
oft, the union of all simplices of t incident to x (i.e., containing x) is a closed 3-ball
B⊂ M . The simplices of t lying in ∂B form a triangulation of ∂B . Let Γ ⊂ ∂B
be the 1-skeleton of this triangulation, i.e., the union of vertices and edges of t
contained in ∂B . The pair ( ∂B, Γ) is called the link of x in (M,t ).
The link of x can be visualized in a small neighborhood of x. Pick a (small)
closed 3-ball Bx⊂M centered at x such that Bx meets every simplex of t incident
to x along a concentric subsimplex with vertex x. The link of x can be identiﬁed
with the pair (∂Bx, Γ x), where Γ x is the intersection of ∂Bx with the 2-skeleton t(2)
of t (formed by the simplices of t of dimension ≤ 2). The vertices (resp. edges)
of Γ x are the intersections of ∂Bx with the edges (resp. faces) of t incident to x.
In the sequel, the set of all faces of t is denoted by Reg( t). By an orientation of
the 2-skeleton t(2) of t, we mean a choice of orientation in all faces of t (we impose
no compatibility conditions on these orientations of faces).
5.2. Invariants of 3-manifolds. LetC be a spherical fusion category over k whose
dimension is invertible in k. Fix a (ﬁnite) representative set I of simple objects ofC.
For each closed oriented 3-manifold M , we deﬁne a topological invariant |M|C∈ k.
Pick a triangulation t of M with oriented 2-skeleton and a map c : Reg(t)→I.
For each oriented edge e of t, we deﬁne a k-module Hc(e) as follows. The orienta-
tions of e and M determine a positive direction on a small loop in M encircling e;
this direction determines a cyclic order on the set te of all faces of t containing e.
To each face r∈ te we assign the object c(r)∈ I and a sign equal to + if the
orientations of r and e are compatible and to − otherwise. (The orientations of r
and e are compatible if each pair (a tangent vector directed outward r at a point
of e, a positive tangent vector of e) is positively oriented in r.) In this way, te
becomes a cyclic C- set. Set Hc(e) = H(te). If eop is the same edge with opposite
orientation, then teop = (te)op. This induces a duality between the modules Hc(e),
Hc(eop) and a contraction ∗e : Hc(eop)⋆⊗Hc(e)⋆→ k, see Section 2.4. Note that
the contractions∗e and∗eop are equal up to permutation of the tensor factors.
Consider the link ( ∂Bx, Γ x) of a vertex x of t. Every edge α of Γ x lies in a
face rα of t incident to x. We color α with c(rα) ∈ I and endow α with the
orientation induced by that of rα\ Int(Bx). In this way, Γ x becomes a C-colored
graph in ∂Bx. We identify ∂Bx with the standard 2-sphere S2 via an orientation
preserving homeomorphism, where the orientation of ∂Bx is induced by that of M
restricted toM\Int(Bx). Then H(Γ x) =⊗e∈txHc(e), wheretx is the set of all edges
of t incident to x and oriented away from x. Section 3.3 gives FC(Γ x)∈ H(Γ x)⋆.
14 V. TURAEV AND A. VIRELIZIER
The tensor product ⊗x FC(Γ x) over all vertices x of t is a vector in ⊗eHc(e)⋆,
where e runs over all oriented edges of t. The contractions ∗e apply to diﬀerent
tensor factors, and their tensor product ∗t =⊗e∗e is a map ⊗eHc(e)⋆→ k. Set
(8) |M|C = (dim(C))−|t|∑
c

 ∏
r∈Reg(t)
dimc(r)

∗t(⊗x FC(Γ x))∈ k,
where|t| is the number of tetrahedra of t and c runs over all maps Reg( t)→ I.
The following theorem will be proved in Section 7.
Theorem 5.1. |M|C is a topological invariant of M (independent of the choice of t
and of the orientation of t(2)). This invariant does not depend on the choice of I.
It is clear from the deﬁnitions that |M∐N|C =|M|C|N|C for any oriented closed
3-manifolds M,N . One can show that |− M|C =|M|Cop, where −M is M with
opposite orientation. We prove below that |S3|C = (dim(C))−1 and|S1×S2|C = 1.
The invariant|M|C can be viewed as a state sum (or a partition function) on t
as follows. Provide all symmetrized multiplicity modules in C with distinguished
bases. By states on t, we mean pairs consisting of a map c : Reg(t)→ I and a
choice of a basis vector bc(e)∈ Hc(e) for every oriented edge e of t. Let b⋆
c(e)
be the corresponding vector in the basis of Hc(e)⋆ dual to the distinguished basis
ofHc(e). The Boltzmann weight associated with such a state is the product of the
factors FC(Γ x)(⊗e∈txbc(e)),∗e(b⋆
c (eop),b ⋆
c (e)) = ∗eop(b⋆
c (e),b ⋆
c (eop)), dim c(r), and
(dim(C))−1 contributed respectively by the vertices, edges, faces, and tet rahedra
oft. The invariant |M|C is the sum of these Boltzmann weights over all states on t.
This state sum diﬀers from the one in [TV, BW1], where the states are labelings of
the edges of t with elements of I and the key factor in the Boltzmann weight is a
6j-symbol contributed by every tetrahedron. It is non-obvious bu t true that these
two state sums are equal, see Section 6. In particular, our invarian t|M|C is equal
to the invariant of M deﬁned by Barrett and Westbury [BW1].
5.3. Remark. We say that a triangulated surface Σ is I-colored if every edge of Σ
is oriented and endowed with an element of I. In other words, Σ is I-colored if its 1-
skeleton Σ (1) is aC-colored graph in Σ with colors of all edges being in I. For such Σ,
we can consider the k-module HC(Σ) = H(Σ (1)) =⊗xHx(Σ (1)), where x runs over
all vertices of Σ. The state sum (8) extends to compact oriented 3 -manifolds M
with I-colored triangulated boundary and gives a vector |M|C∈HC(∂M )⋆. These
vectors can be used to deﬁne a 3-dimensional TQFT. We will discuss a more general
construction in Section 9.
