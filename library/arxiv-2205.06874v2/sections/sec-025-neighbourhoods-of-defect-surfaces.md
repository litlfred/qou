---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-025-neighbourhoods-of-defect-surfaces
section_title: "Neighbourhoods of defect surfaces"
section_number: null
pages: 41-44
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
In the presence of defects, applying a bistellar move to a generic transversal triangulation may yield a
triangulation that is no longer transversal or generic. For this reason, it is not straightforward to establish
41
invariance of the state sums via bistellar moves. Instead, we refine the triangulations and decompose the
underlying defect 3-manifold into certain neighbourhoods of defect surfaces and components contained in the
regions between them. Their state sums are computed separately and then glued with Corollary 4.10. This
also gives a geometrical interpretation to the state sums and facilitates the computation of examples.
The neighbourhoods of the defect surfaces we consider are similar to regular neighbourhoods, see [RS, Ch. 3],
but our defect surfaces are not realised as subcomplexes of the triangulation.
Definition 5.6.A fine neighbourhoodof a defect surfaceD is a connected generic transversal triangulated
3-manifold M with defect surfaceD⊂M such thatD∩∂M =∂D, every vertex ofM is contained in∂M
and every triangle or edge inM that does not intersectD is contained in∂M.
By applying a finite number of bistellar moves between generic transversal triangulations, any generic
transversal triangulation of a defect 3-manifoldM can be subdivided in such a way that the tetrahedra
intersecting a given defect surface form a fine neighbourhood of the defect surface. A bistellar move between
two generic transversal triangulations is calledgeneric transversal bistellar movein the following.
Lemma 5.7. Let (M,D ) be a defect 3-manifold andT a generic transversal triangulation ofM. Then
there is a finite sequence of generic transversal bistellar moves that transformsT into a generic transversal
triangulation S such that:
(i) S coincides withT on ∂M,
(ii) the tetrahedra inS contained in any regionr⊂M form a 3-manifoldR homeomorphic to ¯r,
(iii) the tetrahedra inS that intersect any defect surfaceΣ⊂D form a fine neighbourhood ofΣ.
Proof. Let D =⨿n
j=1Σj be the defect manifold, whose connected components are the defect surfacesΣj, and
M\D =⨿m
k=1rk with the regionsrk as connected components.
For each oriented edge inT that intersectsD and hence is oriented byD, denote byrf the region that
contains its target vertex and byri the region that contains its starting vertex. Analogously, for each triangle
and tetrahedron inT that intersectsD, denote byrf and ri the regions that contain the target vertices and
starting vertices of its edges that intersectD.
The triangulationS is constructed by a finite sequence of stellar subdivisions from Section 5.1, which are
finite sequences of bistellar moves. We show that this can be achieved with generic transversal bistellar moves.
1. In the first step, for each tetrahedront inT that intersectsD, choose a pointtf∈rf∩˚t and perform a 1-4
move withtf as the new vertex. This subdividest into four transversal tetrahedra. By adjusting the position
of tf one can achieve that none of the new triangles contains a defect vertex and none of the new edges
intersect defect lines. Hence, all four tetrahedra are generic. This yields a generic transversal triangulation
T′ related toT by generic transversal bistellar moves.
2. In the second step, for each triangle∆ in T′ that intersectsD and is not contained in∂M, choose a point
∆f∈rf∩ ˚∆ and perform the stellar subdivision on∆ with ∆f as the new vertex. The two bistellar moves
that combine to this stellar subdivision involve only transversal tetrahedra. By adjusting the position of
∆f one can achieve that none of the triangles arising in these moves contains a defect vertex and none of
the edges intersect a defect line. With this, all of the tetrahedra become generic and we obtain a generic
transversal triangulationT′′ related toT′ by generic transversal bistellar moves.
3. In the third step, for each edgee in T′′ that intersectsD and is not contained in∂M, choose a point
ef∈rf∩˚e and perform a stellar subdivision one with ef as the new vertex. All tetrahedra arising in the
bistellar moves that combine to this stellar subdivision are transversal. By adjusting the position ofef, one
can achieve that none of their triangles contains a defect vertex and none of their edges intersects a defect
line. Hence, all tetrahedra in this sequence of bistellar moves are generic.
This yields a generic transversal triangulationT′′′ related toT by generic transversal bistellar moves. The
associated subdivisions of defect tetrahedra are shown in Figure 7. We equip each new edge inT′′′ that
intersectsD with the induced orientation and choose an arbitrary orientation for the other new edges.
4. We then apply steps 1 to 3 to the triangulationT′′′, but now with additional verticesti∈ri∩˚t, ∆i∈ri∩ ˚∆,
ei∈ri∩˚e in the regionri instead ofrf. The positions of these new vertices can again be chosen in such a
way that this defines a finite sequence of bistellar moves between generic transversal tetrahedra.
The result is a generic transversal triangulationS that coincides withT on ∂M by construction. We denote
42
D
Ef
ef
Ei
ei
D
Ef
Eief
ei
tf ∆f
tf
∆f
Figure 7: Subdivisions of tetrahedra intersecting the defect manifoldD with new verticestf, ∆f and ef that
span the surfaceEf. Edges in the subdivision that intersectD are drawn in blue, edges that lie in the region
rf in black and edges in the regionri in grey.
by Sj the triangulated 3-manifold formed by all tetrahedra inS that intersect a defect surfaceΣj. By
construction, every vertex ofSj and every edge or triangle ofSj that does not intersectΣj is contained in
∂Sj, and henceSj is a fine neighbourhood ofΣj. For each tetrahedront in the triangulationT that intersects
Σj, the union of the tetrahedra in its subdivision that are contained in a regionrk is PL homeomorphic to
the closure of(t\D)∩rk. These PL homeomorphisms and the identity maps for tetrahedra inT that do not
intersectD glue to a PL homeomorphism from the union of all tetrahedra inS in rk to ¯rk.
A fine neighbourhood of a defect surfaceD is shown in Example 6.2 and Figure 9. Generic transversal
triangulations that do not form fine neighbourhoods of their defect surfaces are given in Examples 6.1, 6.3
and 6.4, see also Figures 11 and 12. In particular, any fine neighbourhood ofD must have topology[0, 1]×D.
Lemma 5.8. LetM be a triangulated 3-manifold that shells to a fine neighbourhood of a defect surfaceD by
elementary shellings with tetrahedra that do not intersectD. ThenM is PL homeomorphic to[0, 1]×D.
Proof. If M is a fine neighbourhood ofD, this follows by applying the same subdivision procedure as in the
proof of Lemma 5.7, but to every edge and triangle that intersects the defect surfaceD, including the ones
in ∂M. Denote byEf the 2d PL surface spanned by the verticestf, ∆f and ef, byEi the 2d PL surface
spanned by the new verticesti, ∆i and ei, as shown in Figure 7. For each tetrahedront in the original
triangulation witht∩D̸=∅ the tetrahedra in its subdivision that intersectD form the region between
the surfacesEt∩t and Ei∩t in Figure 7 This region is PL homeomorphic to[0, 1]× (t∩D). The PL
homeomorphisms for the tetrahedrat with t∩D̸=∅ glue to a PL homeomorphism that sends the union of
all tetrahedra in the subdivision that intersectD to [0, 1]×D. AsM is related to it by elementary shellings,
it is PL homeomorphic to[0, 1]×D by Theorem 5.4. For a 3-manifoldM that shells to a fine neighbourhood
ofD with elementary shellings by tetrahedra that do not intersectD the claim follows with Theorem 5.4.
In the following, we will often project graphs on the boundary of a manifoldM with a defect surfaceD⊂M
to the defect surfaceD. This is achieved via orientation preserving PL homeomorphismsϕ :M→ [0, 1]×D.
43
We denote bypD : [0, 1]×D→D, (t,d )↦→d and pt : [0, 1]×D→ [0, 1], (t,d )↦→t the projection maps for
the product, which are PL maps by construction.
Definition 5.9. LetM be a triangulated 3-manifold with a defect surfaceD⊂M and ϕ :M→ [0, 1]×D an
orientation preserving PL homeomorphism withpD◦ϕ|D = idD. The projections induced byϕ are the PL
homeomorphismsPi(ϕ) :ϕ−1({i}× D)→D, m↦→pD◦ϕ(m) for i = 0, 1.
The diagrams obtained by projecting graphs on∂M to a defect surfaceD⊂M depend on the choice of the
underlying PL homeomorphism. That theirevaluations are independent of this choice follows from the fact
that different choices of PL homeomorphisms yield PL isotopic projection maps.
Lemma 5.10. Letϕ1,ϕ 2 :M→ [0, 1]×D be orientation preserving PL homeomorphisms withpD◦ϕ1|D =
pD◦ϕ2|D = idD. Then the projection mapsPi(ϕ1) and Pi(ϕ2) are PL isotopic fori = 0, 1.
Proof. By a well-known result of Epstein [E66, Th. 6.4], an orientation preserving PL homeomorphism from
a 2-manifold with compact boundary components to itself is PL isotopic to the identity iff it is homotopic to
the identity. It is therefore sufficient to show thatPi(ϕ2) and Pi(ϕ1) are homotopic. For this, we construct
homeomorphisms ϕ′
i :M→ [0, 1]×D that coincide withϕi on ∂Mi :=ϕ−1
1 ({i}× D) =ϕ−1
2 ({i}× D) and
homotopies fromϕ′
2|∂Mi to ϕ′
1|∂Mi. Fori = 0 and j = 1, 2, we consider the continuous maps
Fj : [0, 1]×D→ [0, 1], (t,d )↦→
{ t
2pt(ϕj(d)) t∈ [0,pt(ϕj(d))]
1−t
2(1−pt(ϕj(d))) + t−pt(ϕj(d))
1−pt(ϕj(d)) t∈ [pt(ϕj(d)), 1]
and the homeomorphismsϕ′
j :M→ [0, 1]×D, m↦→(Fj(ϕj(m)),pD(ϕj(m))) that satisfyϕ′
j(m) =ϕj(m) for
all m∈∂M0∪∂M1, pD◦ϕ′(d) =d and pt◦ϕ′
j(d) = 1
2 for alld∈D. Then the continuous map
h : [0, 1]×∂M0→D, (t,m )↦→pD◦ϕ′
2◦ϕ′−1
1 (t
2,pD(ϕ′
1(m)))
satisfies h(0,m ) =P0(ϕ2)(m) and h(1,m ) =P0(ϕ1)(m) for allm∈∂M0 and is a homotopy fromP0(ϕ1) to
P0(ϕ2). The proof thatP1(ϕ1) and P1(ϕ2) are homotopic is analogous.
