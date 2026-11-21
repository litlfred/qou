---
doc_id: 4geo-dedi-rev
doc_title: "On the quantum Teichmüller invariants of fibred cusped 3-manifolds"
section_id: sec-007-on-the-quantum-teichm-uller-invariants-of-fibred
section_title: "ON THE QUANTUM TEICHM ¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS (page 9)"
section_number: null
pages: 9-9
source_pdf: 4GEO-DEDI-REV.pdf
source_sha256: e4d52947b71a3f37
toc_source: inferred
doc_brief: "On the quantum Teichmüller invariants of fibred cusped 3-manifolds — 26 sections: Front matter; ON THE QUANTUM TEICHM ¨ULLER INVAR; ON THE QUANTUM TEICHM ¨ULLER INVAR"
---
8
ST´EPHANE BASEILHAC1, RICCARDO BENEDETTI2
Recall that π1(Mφ) is a HNN-extension of π1(S). That is, given a generating set γ1, . . . , γu of π1(S)
satisfying the relations r1, . . . , rv, there is an isomorphism between π1(Mφ) and the group generated
by γ1, . . . , γu and an element t satisfying the relations r1, . . . , rv and tαt−1 = φ∗(α) for all α ∈
π1(S), where φ∗: π1(S) →π1(S) is the isomorphism induced by φ. Therefore, every representation
r: π1(S) →PSL(2, C) that may be extended to Mφ is such that r(π1(S)) and r ◦φ∗(π1(S)) are
conjugate subgroups of PSL(2, C). Any augmented character of S that may be extended to Mφ is
thus a ﬁxed point of the map Φ∗: X(S) →X(S) induced by the map r 7→r ◦φ∗on representations,
and i∗(X(Mφ)) is a subvariety of Fix(Φ∗).
Again in the setting of Section 2, let (T,˜b) be a weakly branched layered triangulation of the
ﬁbred cusped manifold Mφ. Let us recall a few facts about the gluing variety G(T,˜b), that is, the
set of solutions of the Thurston gluing equations supported by (T,˜b). It is a complex aﬃne algebraic
set of dimension greater than or equal to r. The points of G(T,˜b) are classically called systems of
shape parameters. Their coordinates, the shape parameters, are scalars in C \ {0, 1} associated to
the abstract edges of T. The shape parameters of opposite edges of a tetrahedron are equal, and the
cyclically ordered triple of shape parameters of a tetrahedron encodes an isometry class of hyperbolic
ideal tetrahedra.
The set G(T,˜b) is deﬁned by the following two sets of equations. For every branched tetrahedron,
set wj := w(Ej), j = 0, 1, 2 (see before Figure 1 for the ordering of the edge Ej). For every edge e of
T, deﬁne the total shape parameter W(e) as the product of the shape parameters w(E), where E →e.
Then we have:
• (Tetrahedral equation) For every tetrahedron and j ∈{0, 1, 2}, wj+1 = (1 −wj)−1 cyclically;
hence w0w1w2 = −1.
• (Edge equation) For every edge e of T, W(e) = 1.
A point w ∈G(T,˜b) determines a pseudo-developing map Fw :
˜
Mφ →H3, where
˜
Mφ is the
universal cover of Mφ, and Fw is well-deﬁned up to post-composition with an orientation-preserving
isometry of H3. The map Fw sends homeomorphically the edges of ˜T to complete geodesics, and
it satisﬁes Fw(g˜x) = rw(g)Fw(˜x) for all ˜x ∈˜
Mφ, g ∈π1(Mφ), where rw : π1(Mφ) →PSL(2, C) is
a homomorphism. So w encodes the conjugacy class of rw. In fact, Fw determines also some rw-
equivariant set {ξΓ}Γ∈Π as above, so that eventually the map w 7→rw can be lifted to a regular
“holonomy” map
hol: G(T,˜b) →X(Mφ).
We have (see Proposition 4.6 of [5] when Mφ has a single cusp, and Remark 1.4 of [6] for the general
case):
Proposition 3.1. There is a subvariety A of G(T,˜b) of dimension equal to the number of cusps
of M, and a point wh ∈A, such that hol(wh) is the hyperbolic holonomy of Mφ, and hol|A is a
homeomorphism from a Zariski open subset of A containing wh onto its image.
In particular, every point w ∈A encodes an augmented character of Mφ; the algebraic closure of
hol(A) is the eigenvalue subvariety E(Mφ) of X0(Mφ), the irreducible component of X(Mφ) containing
the discrete faithful holonomy rh (see [12]). If Mφ has a single cusp, then E(Mφ) = X0(Mφ); in general
E(Mφ) contains rh and has complex dimension equal to the number of cusps of Mφ.
It follows from Proposition 3.1 that a point of i∗(X0(Mφ)) ⊂X(S) close enough to i∗(rh) is encoded
by a point w ∈A.
From now on, we consider only systems of shape parameters w lying in the subvariety A of G(T,˜b).
Denote by (T,˜b, w) the layered triangulation T of Mφ endowed with the weak branching ˜b and the
labelling of the abstract edges of T by a system of shape parameters w.
For every j = 0, . . . , k,
consider the ideally triangulated surfaces (S, λj) embedded into (T,˜b, w) as in Section 2. For every
edge e of λj, deﬁne the lateral shape parameter W +
j (e) as the product of the shape parameters of the
abstract edges E →e carried by the tetrahedra lying on the positive side of (S, λj).
