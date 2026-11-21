---
doc_id: arxiv-math-0611504v1
doc_title: "QUANTUM HYPERBOLIC GEOMETRY"
section_id: sec-003-22-qhg-triangulated-pseudomanifolds
section_title: "QHG triangulated pseudomanifolds"
section_number: 2.2
pages: 7-9
source_pdf: 0611504v1.pdf
source_sha256: a33d2771c873a97e
toc_source: outline
doc_brief: "Quantum hyperbolic geometry — 25 sections: Front matter; Introduction; Universal QHG"
duplicate_of: "agt-v7-n2-p13-s"
---
plicity, but all what follows makes sense for arbitrary singular 3-cycles whose non manifold locus is
of codimension ≥2. By a pseudomanifold Z, possibly with non-empty boundary ∂Z, we mean a
compact oriented polyhedron with at most a ﬁnite set of non manifold points. The boundary is a
pseudo-surface.
A QHG triangulated pseudomanifold (Z, T ) is a pseudomanifold Z obtained as the quotient of a ﬁnite
family Z = {(∆i, bi, wi, f i, ci)} of ﬂat/charged I-tetrahedra, via a system of orientation reversing
simplicial identiﬁcations of pairs of 2-faces such that the branchings match. The resulting triangulation
T of Z is endowed with a global branching b, and is possibly singular (multiply adjacent as well as
self adjacent tetrahedra are allowed). The set of non manifold points of Z is contained in the set of
vertices of T . We do not impose for the moment any global constraint on the moduli, ﬂattening and
charges. Hence Z is equipped with a rough ﬂat/charged I-triangulation
T = (T, b, w, f, c), where
w = {wi} and so on.
Next we deﬁne the QHG triangulated pseudomanifold isomorphisms. Fix a QHG triangulated pseu-
domanifold (Z, T ), and let ǫT : E(Z) →E(T ) be the identiﬁcation map of edges. We deﬁne the total
8
ST´EPHANE BASEILHAC1 AND RICCARDO BENEDETTI2
modulus, log-branch and charge of an edge e, respectively, by:
WT (e) =
Y
h∈ǫ−1
T (e)
w(h)∗b
LT (e) =
X
h∈ǫ−1
T (e)
∗b l(h)
(7)
CT (e) =
X
h∈ǫ−1
T (e)
c(h)
where ∗b = ±1 according to the b-orientation of the tetrahedron in Z that contains h, w(h) is the
cross-ratio modulus at h, l(h) the log-branch at h, and c(h) the charge at h.
Remark 2.2. It is easily seen that WT (e) is a cross ratio for the four ‘extremal’ points on ∂H
3
determined by gluing oriented hyperbolic ideal tetrahedra with moduli w(h)∗b along a common edge
(by continuity WT (e) = 1 for a degenerate quadrilateral with three distinct vertices).
It is well-known that any two arbitrary naked triangulations T , T ′ of Z with the same boundary
triangulation can be connected (keeping the boundary triangulation ﬁxed) by a ﬁnite sequence of the
local moves shown in Figure 4, the 2 ↔3 move (top) and the bubble move (bottom).
Figure 4.
The moves on naked singular triangulations.
For any such a local move T ↔T ′ we have two triangulations of a same portion of a polyhedron Q.
Assume that both T and T ′ extend to portions (Q, T ) and (Q, T ′) of QHG triangulated pseudoman-
ifolds. We have to specify the admissible QHG transits T ↔T ′. In any case we require that they
are local (that is, the portions complements remain unchanged), and that the branchings coincide at
every common edge of T and T ′.
For the 2 ↔3 move we also require that at every common edge e as above the total modulus,
log-branch and charge coincide
(8)
WT (e) = WT ′(e),
LT (e) = LT ′(e),
CT (e) = CT ′(e).
The same rule restricted to the total modulus and total log-branch holds also for the bubble move;
however, the total charge behaves in a diﬀerent way: any bubble transit T ↔T ′ includes a marked
edge e common to T and T ′. Referring to the bottom of Figure 4 we require that CT (e) = CT ′(e)−2,
while for the other two common edges the total charges are unchanged.
Remark 2.3. For every QHG transit supported by a 2 ↔3 move (top of Figure 4), if E0 denotes
the new edge in T ′ then
WT ′(E0) = 1, LT ′(E0) = 0, CT ′(E0) = 2.
QUANTUM HYPERBOLIC GEOMETRY
9
For every QHG bubble transit, let f ′ be the unique new 2-simplex of T ′ that contains the marked
edge e. Denote by E1 and E2 the other edges of f ′, and by E3 the further new edge of T ′. Then we
have
WT ′(Ej) = 1,
LT ′(Ej) = 0,
j = 1, 2, 3
(10)
CT ′(E1) = CT ′(E2) = 0,
CT ′(E3) = 2.
Deﬁnition 2.4. A QHG isomorphism between QHG triangulated pseudomanifolds is any ﬁnite com-
position of QHG transit conﬁgurations and oriented simplicial homeomorphisms that preserve the
whole decoration.
