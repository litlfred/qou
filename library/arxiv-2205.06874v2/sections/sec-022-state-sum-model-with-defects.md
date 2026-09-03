---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-022-state-sum-model-with-defects
section_title: "State sum model with defects"
section_number: null
pages: 37-39
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
In this section we show how the generalised 6j symbols for generic transversal defect tetrahedra combine to
state sums for a generic transversal triangulated 3-manifolds with defect data.
Let M be a generic transversal triangulated 3-manifold with defect data,R its set of regions andA its set of
oriented defect areas. We denote byCr the spherical fusion category assigned to the regionr and byMa
the bimodule category assigned to the defect areaa. A vertex, edge or triangle of the triangulation is called
boundary if its is contained in∂M and internal otherwise. We use the following notation:
• Tet for the set of tetrahedra of the triangulation,
• ∆ for its set of triangles,∆∂M for its set of boundary triangles and∆i for its set of internal triangles,
• E for its set of edges,E∂M for its set of boundary edges andEi for its set of internal edges,Er for its
set of edges in the regionr and Ea for its set of edges that intersect a defect areaa,
• V for its set of vertices,V∂M for its set of boundary vertices,Vi for its set of internal vertices andVr
for its set of vertices in the regionr.
We fix for each spherical fusion categoryC and each bimodule categoryM sets IC and IM of representatives
of the isomorphism classes of simple objects and associated projection and inclusion morphisms as in Section 3.
37
For each labelingl ofM as in Definition 4.2 we denote byl(e)∈ICr orl(e′)∈IMa the simple object assigned
to e∈Er or e′∈Ea. For an oriented trianglef labeled with simple objects in the sets of representatives and
associated projection or inclusion morphisms, we writeHom(f) for the associated morphism space from(70).
Each tetrahedront∈ Tet is equipped with the orientation induced byM. For the tetrahedra that intersect
defect surfaces, this is already encoded in their labeling with defect data. For tetrahedra that do not intersect
defect surfaces, we always assume this orientation choice without emphasising it notationally.
Definition 4.7. Let M be a generic transversal triangulated 3-manifold with defect data,l∂M a labeling
of its boundary edges with simple objects in the chosen sets of representatives andb∂M an assignment of
morphisms from the morphism spaces(70) to its boundary triangles. The state sum of(M,l∂M,b∂M ) is
Z(M,l∂M,b∂M ) =
∏
r∈R
dim(Cr)−(Σv∈Vrϵ(v))∑
l
∑
bi
∏
t∈Tet
6j(t,l,b )
∏
e∈E
diml(e)ϵ(e), (81)
where
• ϵ(v) = 1 for v∈Vi, ϵ(e) = 1 for e∈Ei and ϵ(v) = 1/2 for v∈V∂M, ϵ(e) = 1/2 for e∈E∂M,
• Σl is the sum over all labelingsl of edges ofM with simple objects inICr and IMa that coincide with
l∂M on the boundary,
• Σbi is the sum over all labelingsbi of internal triangles ofM with the projection and inclusion morphisms
in the morphism spaces(70),
• Πt∈Tet 6j(t,l,b ) stands for the product of the generalised 6j symbols6j(t,l,b )∈ C of all tetrahedra given
by the labelingl and the assignmentb = (bi,b∂M ) of morphisms to the triangles.
We denote byZ(M,l∂M ) the associated linear map
Z(M,l∂M ) :
⨂
f∈∆∂M
Hom(f)→ C, b ∂M↦→Z(M,l∂M,b∂M ) (82)
and byZ′(M,l∂M,b∂M ) the rescaled state sum without the dimension factors of boundary edges and vertices
Z(M,l∂M,b∂M ) =
( ∏
e∈E∂M
diml(e)∏
r∈R
∏
v∈Vr∩V∂M
dimCr
)1/2
Z′(M,l∂M,b∂M ). (83)
The product Πt∈Tet6j(t,l,b ) in formula(81) can also be viewed as the evaluation of the (unordered) tensor
product⊗t∈Tet6j(t) of the linear forms 6j(t) in Definition 4.3 on a vector in the tensor product of the
morphism spaces for the triangles. This vector is defined by the labelingsl,bi,b∂M, and the sums overl and
bi eliminate the dependence on the labeling in the interior ofM.
It is clear that the linear mapZ(M,l∂M ) does not depend on the choice of projection and inclusion morphisms
for the interior triangles. If the simple objects assigned to the edges of the triangulation are fixed, then the
projection and inclusion morphisms assigned to the interior triangles are fixed by(53) up to simultaneous
rescalingpα
xm→λpα
xm andjα
xm→λ−1jα
xm forλ =λ(x,m,α )∈ C×. As each interior triangle arises in exactly
two tetrahedra with opposite orientations, the state sum is invariant under such rescalings.
To determine the dependence of the state sum on the choice of representatives of simple objects, letM be
a triangulated 3-manifold with defect data. Fix two sets of representativesI,I′ for each category labeling
a region or defect area and an isomorphismϕxx′ : x→ x′ for each pair of isomorphic objectsx∈ I,
x′∈I′. Note that this isomorphism is unique up to rescaling withC× and that it induces an isomorphism
ϕf : Hom(f)→ Hom(f)′ between the morphism spaces for a trianglef labeled by isomorphic objects inI
and I′. More explicitly, these isomorphisms are given by
ϕf : Hom(m,F (j▷n))→ Hom(m′,F (j′▷n′)), α ↦→F (ϕjj′▷ϕnn′)◦α◦ϕ−1
mm′
ϕf : Hom(F (j▷n),n )→ Hom(F (j′▷n′),m′), β ↦→ϕmm′◦β◦F (ϕ−1
jj′▷ϕ−1
nn′).
Definition 4.3 and the cyclic invariance of the trace imply that the 6j symbols are invariant under these
isomorphisms, if they are applied to all morphism spaces simultaneously. This yields
Corollary 4.8. LetM be a generic transversal triangulated 3-manifold with defect data. Letl∂M and l′
∂M be
labelings of the boundary triangles with simple objects in two sets of representativesI,I′. Then
Z(M,l∂M ) =Z(M,l′
∂M )◦ (⊗f∈∆∂Mϕf) :
⨂
f∈∆∂M
Hom(f)→ C.
38
In particular, it follows that the state sum for aclosed generic transversal triangulated 3-manifold with defect
data does not depend on the choice of representatives of simple objects.
It is also apparent from Definition 4.7 that the state sum(81) is a direct generalisation of the usual Turaev-
Viro-Barrett-Westbury state sum from [BW96, TV92] and coincides with it if all defect areas, defect lines and
defect vertices are trivial. This amounts to replacing all bimodule categories in(81) by a single spherical fusion
categoryC, viewed as a(C,C)-bimodule category, and all bimodule functors and natural transformations by
identity functors and natural transformations.
Corollary 4.9. For any triangulated 3-manifold without defects and any generic transversal triangulated
3-manifold with trivial defect data, labeled by a spherical fusion categoryC, the state sum from Definition 4.7
reduces to the Turaev-Viro-Barrett-Westbury state sum
Z(M,l∂M,b∂M ) = 1
dimC|Vi|+|V∂M|/2
∑
l
∑
bi
∏
t∈Tet
6j(t,l,b )
∏
e∈E
diml(e)ϵ(e). (84)
Another direct consequence of Definition 4.7 is that the state sum can be computed by gluing triangulated
3-manifolds along boundary components. As in the case without defects, this allows one to compute state
sums by cutting 3-manifolds into simpler pieces. The only additional restriction is that the defect surfaces
must meet the cut transversally and all pieces must be generic and transversal.
Corollary 4.10. LetM1 and M2 be generic transversal triangulated 3-manifolds with defect data andM
obtained by gluingM1 and M2 along a boundary componentΣ⊂∂Mi. Then
Z(M,l∂M,b∂M ) =
∑
lΣ
Z(M1,l∂M1,b∂M1)·Z (M2,l∂M2,b∂M2), (85)
where the labelingsl∂M and b∂M of ∂M are induced by the labelingsl∂Mi and b∂Mi of ∂Mi and the sum is
over the labelings of edges inΣ with simple objects and over dual bases of the morphism spaces for triangles
in Σ.
