---
doc_id: arxiv-2104.04941v2
doc_title: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES"
section_id: sec-003-13-higher-teichmüller-spaces
section_title: "Higher Teichmüller spaces"
section_number: 1.3
pages: 5-6
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
doc_brief: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES — Fock and Goncharov [FG06b] introduced cluster ensembles, p roviding a framework for coordi- nates on varieties of surface"
---
{ρ :π1(Σ) →G discrete and faithful }/G,
where the standard Teichmüller space case is given by G = Isom +(H2) = PSL 2(R). In order to apply the
Fock–Goncharov program, we need the following conditions.
• The surface Σ must admit an ideal triangulation, so we demand that it be hyp erbolic with n ≥ 1
punctures.
• The groupG must be a split semisimple algebraic group over Q; for technical reasons the moduli space
AG,Σ is deﬁned when G is simply-connected, and XG,Σ is deﬁned when G is centerless. However,
the ﬁeld underlying G is not critical.
As another technical point, when G is simply connected we will parametrize boundary-unipoten t repre-
sentations, and when G is centerless the representations will be boundary-borel ( see Deﬁnition 4.2).
We now replay the program to create moduli spaces AG,Σ and XG,Σ for higher rank G.
1. The structure is determined by ideal points.
By restrictions on Σ , the representation is still deﬁned by ideal points of a fund amental domain.
2. We can identify ideal points with cosets of isometries in Isom+(H2) that deﬁne them
We replace Isom+(H2) with general G. By our restrictions on G, subgroups N+ andB+ are still available.
3. Choosing an ordered triangulation attaches a non-degener ate ordered triple of cosets to
each triangle.
Non-degenerate cosets are replaced by suﬃciently generic conﬁguration spaces (see Deﬁnition 4.1).
These ensure that a well-deﬁned element of H, the maximal torus of G, corresponding to translations along
geodesics in the PSL2(R) case, can be attached to each edge of each triangle.
4. Coordinates can be assigned to each triple (or pairs of triple s) of cosets.
To assign coordinates to conﬁguration spaces, Fock–Goncha rov use generalized minors (see Deﬁni-
tion 2.16). In the case of GLn, these correspond to shuﬄing rows and columns according to t wo permuta-
tions, then taking the upper i ×i minor. In the more general case, two words in the Weyl group of G are
invoked and a coordinate associated to the ith fundamental weight is used.
By work of Lusztig, conﬁguration spaces carry a positive str ucture via factorization coordinates (see
Deﬁnition 2.23). By work of Fomin–Zelevinsky, generalized minors inherit this positive structure.
5. We must describe how the coordinates change under (oriented ) reordering and retriangu-
lation
5
A major result of the Fock–Goncharov program is that reorder ing of triangles (we restrict to orientation-
preserving reorderings, which we refer to as rotation) and retriangulation of quadrilaterals (which we refer
to as a ﬂip of the diagonal) preserve this positive structure. All gene ral retriangulations and reorderings can
be obtained this way.
6. Hyperbolic structures are those for which all coordinates a re positive.
Instead of hyperbolic structures, we are interested in poin ts in higher Teichmüller spaces. Since the general
moduli spaces carry positive structures, the sets of positi ve points A+
G,Σ and X +
G,Σ are well-deﬁned when G is
over R. These do, in fact, correspond to higher Teichmüller spaces or decorations of them (see Section 4.3).
7. The representation ρ :π1(Σ) →G can be reconstructed.
The representation ρ(γ) can still be computed by A- or X -coordinates (again, see Section 4.3). Here our
restrictions on G being simply connected or centerless are necessary.
So the Fock–Goncharov program holds beyond PSL2(R). We now address the following question:
The positive structure on coordinates is preserved under retri angulation and reorientation,
but how are those two operations realized on coordinates?
In the A1 case, the cluster ensemble of Figure 5 provides the answer. I n [FG06b], Fock–Goncharov
produced cluster ensembles for all types An. The quivers appear as triangular lattices, see Section 6 fo r
an overview. Fock–Goncharov also provided descriptions fo r coordinate changes under the two key oper-
ations as sequences of mutations. The rotation describes reordering of a triangle, and the ﬂip describes
retriangulation of a quadrilateral.
Fock–Goncharov predicted that AG,Σ and XG,Σ would carry cluster ensemble structures as well. To realize
those structures, we need, we need
• A way to assign coordinates of Conf ∗
4(G/K) to a triangle. These coordinates will be encoded in a
cluster ensemble. We will call the coordinate assignment ma p M. When the group G is over R,
collections of coordinates will be (R∗)n. Seeds with all coordinates positive will be the positive
points.
• A way to realize (orientable) symmetries of a triangle on tho se coordinates (the rotation, see
Figure 6 a). The bottom map will be realized by a quiver mutation which w e call µrot.
• A way to realize changes of triangulation on those coordinat es (the ﬂip , see Figure 6 b). The bottom
map will be realized by a quiver mutation which we call µﬂip .
• The maps µrot and µﬂip should preserve the positive structure. That is, if a seed ha s positive
coordinates, applying the rotation or the ﬂip should not cha nge that. Using generalized minors for
coordinates is a way to preserve positivity.
g0N+g1N+
g2N+
g0N+
g1N+
g2N+
(R∗)n (R∗)n
rot
M M
µ∗
rot
(a) The rotation.
g0N+
g1N+
g2N+
g3N+ g1N+
g2N+
g3N+
g0N+
(R∗)n (R∗)n
ﬂip
M M
µ∗
flip
(b) The ﬂip.
Figure 6. Retriangulation and reordering (for a group over R).
