---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-027-triangulation-independence
section_title: "Triangulation independence"
section_number: null
pages: 48-51
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
In this section we show that any two generic transversal triangulations of a 3-manifold with defect data yield
the same state sum if they agree at its boundary. Note that this does not follow directly from Corollary
5.13, because it is not guaranteed a priori that such triangulations are related bygeneric transversalbistellar
moves. As a first step, we derive a counterpart of Proposition 5.11 for general defect surfaces.
We again consider 3-manifoldsM that shell to fine neighbourhoods of a defect surfaceD and project the
dual of the boundary triangulation on∂M to D as in Definition 5.9 with an orientation preserving PL
homeomorphismϕ :M→ [0, 1]×D. The only difference to Proposition 5.11 is thatD is no longer a disc and
the resulting diagram onD must be cut along the triangulation to obtain a polygon diagram.
Proposition 5.14. LetM be a triangulated 3-manifold with defect data that shells to a fine neighbourhood
of a defect surfaceD by shellings of tetrahedra that do not intersectD. LetP be a polygon diagram obtained
by projecting the dual of the triangulation on∂M to D and cuttingD along the triangulation to a disc. Then
Z′(M,l∂M,b∂M ) =
∑
l
∑
b∆i
ev(P )
∏
e∈Ei
diml(e),
where
• Ei and ∆i are the sets of internal edges and triangles ofM that correspond to boundary vertices and
edges inP,
• the sum is over all assignments of simple objects to edges inEi and bases of the morphism spaces of
triangles in ∆i.
Proof. The claim follows by induction over the numbern of tetrahedra inM that do not intersectD.
1. Forn = 0, M is a fine neighbourhood ofD. CuttingD along the triangulation to a disc corresponds to
cutting M to a 3-ballB that is a fine neighbourhood of a defect disc. Edges inEi correspond to boundary
edges ofB and elements of∆i to boundary triangles inB. Every labeling of internal edges inM defines a
labeling l of Ei and a labelingl′ of the internal edges ofB.
The state sum forM is given by formula(81). By Proposition 5.11, summing over the labelingl′ and the
labelings of internal triangles ofB yields the state sum forB, which is the evaluation ofP. As every edge in
Ei is internal inM, but in the boundary ofB, the state sum forM is obtained by multiplying this expression
with Πe∈Ei diml(e) and summing over the labelings of edges inEi and morphism spaces for triangles in∆i.
2. Suppose thatM containsn + 1 tetrahedra that do not intersectD. AsM shells to a fine neighbourhood
ofD, it is obtained by gluing a tetrahedront that does not intersectD to triangulated manifoldM′ that also
satisfies the assumptions and hasn tetrahedra that do not intersectD. Ift is contained in the region labeled
by a spherical fusion categoryC, then by the induction hypothesis and Corollary 4.10 the state sum ofM is
given by formula (89) in the proof of Proposition 5.11.
It remains to show that(89) yields ev(P ). Ift is glued toM′ along a single face, this follows as in 2.(i) in
the proof of Proposition 5.11. Ift is glued toM′ along two facesf,f′ that share an edgee =f∩f′′ or along
three facesf,f′,f′′ that share edgese =f∩f′, e′ =f∩f′′ and e′′ =f′∩f′′, we can assume without loss of
generality that the edges in the polygon diagramP′ for M′ that correspond toe, e′, e′′ do not intersect∂P′.
This is possible, because the assumptions imply that they do not intersect a side ofP′ that is contained in
∂D. If they intersect sides ofP′ that are in the interior ofD, we can apply identity(66) to cutP′, glue it
back together in such a way that these edges do not intersect∂P′ and reverse this transformation after the
gluing oft. The claim then follows as in 2.(ii) and 2.(iii) in the proof of Proposition 5.11.
After summation over the objects and morphisms at its boundary, the evaluation of the polygon diagram
in Proposition 5.14 is again independent of the choice of the PL homeomorphismϕ :M→ [0, 1]×D that
defines the projection of the boundary graph onD. Lemma 5.10 ensures that different choices forϕ yield
PL isotopic projection maps and hence diagrams for spherical fusion categories with the same evaluations.
48
Together with identities(39) to (43) and identities(66) and (67) this ensures the polygon evaluations for
different choice ofϕ are equal. As the latter are precisely the cutting and gluing identities that relate different
polygon presentations of surfaces, see for instance [L, Ch. 6] and [ST, Ch. 6.38 and 6.40], it also follows that
all ways of cutting the surface in Proposition 5.14 yield the same value for the state sum.
Note also that Proposition 5.14 allows one to drop the requirement that a fine triangulation is generic in
the interior ofM. For a triangulation that is non-generic in the interior ofM, a small displacement of the
defect surfaces, defect lines and defect vertices yields a generic triangulation. As the cyclic evaluations of the
associated polygon diagrams coincide, all such displacements have the same state sum.
It remains to show that the state sum from Proposition 5.14 does not depend on the choice of the triangulation
in the interior ofM. This follows again from identities (66) and (67).
Lemma 5.15. LetM,M′ be triangulated 3-manifolds with defect data that shell to fine neighbourhoods of
a defect surfaceD with shellings by tetrahedra that do not intersectD. Suppose that the triangulations of
M,M′ coincide on the boundary. Then for all labelingsl∂M and b∂M
Z(M,l∂M,b∂M ) =Z(M′,l∂M,b∂M ).
Proof. By Proposition 5.14 the rescaled state sums forM,M′ are obtained by projecting the dual graph
of the boundary triangulation on∂M to D, cuttingD along the triangulations to discs and evaluating the
resulting polygon diagramsP,P′. With identities(66) and (67) we can cut the polygon diagramsP,P′ into
smaller pieces that are the intersections ofP,P′ with the tetrahedra in the two triangulations.
More precisely, one obtains embedded graphsΓ, Γ′ onD, whose vertices, edges and faces are the intersections
of D with the edges, triangles and tetrahedra in the triangulations. We denote by the same letters the
associated graphs onP,P′ and call vertices or edges ofΓ, Γ′ internal, if they are not contained in∂D and
boundary otherwise. By adjusting the triangulations, we can assume thatΓ, Γ′ are generic, meaning that (i)
defect vertices and vertices labeled by spherical fusion categories are in the interior of faces ofΓ, Γ′, (ii) defect
edges and edges labeled by spherical fusion categories intersect the edges ofΓ, Γ′ transversally in the interior.
With the labelings of the defects and the triangulations every face ofΓ and Γ′ becomes a polygon diagram. By
Proposition 5.14,(66) and (67), the rescaled state sums forM,M′ are obtained by multiplying the evaluations
of these polygon diagrams forΓ, Γ′, rescaling with the dimensions of the simple objects at internal vertices
and summing over all labelings of internal vertices and over bases of the morphism spaces at internal edges.
Using again identities(66) and (67), we cut these polygon diagrams into smaller pieces that correspond to a
common subdivision ofΓ and Γ′. By slightly displacing the vertices ofM,M′ one can achieve that the graphs
Γ, Γ′ remain generic and that every pointv′′∈ (Γ∩ Γ′)\∂D is a transversal intersection point of an edgee of
Γ and an edgee′ of Γ′, while all boundary edges and vertices ofΓ, Γ′ remain fixed. If the displacements of
vertices are sufficiently small, this does not change the evaluations of the polygon diagrams forΓ, Γ′ and
hence preserves the state sums.
Let Γ′′ be the embedded graph onD obtained by superimposingΓ and Γ′ and inserting a new four-valent
vertex at each intersection pointv′′ =e∩e′. Then every edge ofΓ′′ is either on an edge ofΓ or of Γ′. Every
vertex ofΓ′′ is either a vertex ofΓ, of Γ′ or an intersection point of an edge ofΓ and an edge ofΓ′. Summing
the product of polygon evaluations forΓ′′ over the labelings at those internal edges and vertices that lie on
Γ′ yields the corresponding product of polygon evaluations forΓ. Summing it instead over the labelings at
the internal edges and vertices that lie onΓ gives the corresponding product of polygon evaluations forΓ′.
By combining these two summations one obtains that the state sums are equal.
By combining Lemma 5.15 with the triangulation independence of Turaev-Viro-Barrett-Westbury state sums
for spherical fusion categories, we can now show that the state sums for two generic transversal triangulations
of a 3-manifoldM with defect data coincide, whenever their triangulations coincide at the boundary.
Theorem 5.16. Let T,T′ be generic transversal triangulations of a 3-manifoldM with defect data that
coincide on∂M. Then for all boundary labelingsl∂M and b∂M the state sums forT and T′ are equal:
Z(M,l∂M,b∂M,T ) =Z(M,l∂M,b∂M,T′).
Proof. By Lemma 5.7 there are finite sequences of bistellar moves between generic transversal tetrahedra that
transform the triangulationsT,T′ into triangulationsS,S′ that satisfy (i)-(iii) in Lemma 5.7. By Corollary
49
5.13 one hasZ(M,l∂M,b∂M,T ) = Z(M,l∂M,b∂M,S ) andZ(M,l∂M,b∂M,T′) = Z(M,l∂M,b∂M,S′). To
show thatZ(M,l∂M,b∂M,S ) =Z(M,l∂M,b∂M,S′), we denote byΣi the connected components of the defect
manifold D =⨿n
i=1Σi and byrk the regions ofM, which are the connected components ofM\D =⨿m
k=1rk.
By Lemma 5.7 (ii) gluing all tetrahedra inS,S′ that are contained in a regionrk yields triangulated 3-
manifolds Rk,R′
k that are PL homeomorphic to¯rk. By Lemma 5.7 (ii) gluing all tetrahedra inS,S′ that
intersect Σi yields fine neighbourhoodsDi,D′
i of Σi. This implies that all boundary triangles inDi,D′
i that
are internal triangles ofM are glued to boundary triangles in one of the 3-manifoldsRk,R′
k. More specifically,
each connected component of∂Di\∂M coincides with a unique boundary component of someRk, up to the
fact that they have opposite orientations. As∂D⊂∂M, all boundary triangles ofDi and D′
i that intersect
Σi are contained in∂M and hence coincide.
As Di and D′
i are both PL homeomorphic to[0, 1]× Σi, their boundaries are PL homeomorphic. As their
boundary triangulations agree on∂D⊂ ∂M, this allows one to transform each connected component of
∂D′
i\∂M into the corresponding connected component of∂Di\∂M by a finite number shellings or inverse
shellings with tetrahedra that do not intersect any defect surface. Performing the same shellings on the
associated boundary component ofR′
k transforms it into the corresponding boundary component ofRk.
For each labeling of the edges and triangles, performing such a simultaneous shelling or inverse shelling at
D′
i and R′
k amounts to multiplying or dividing the state sum ofM′ by the 6j symbol of a tetrahedront
labeled by a spherical fusion category, with the 6j symbol of the tetrahedron¯t with the same labeling, but
the opposite orientation, and with dimension factors associated to their edges. The orthogonality relation
(87) and identity (55) ensure that this does not change the state sum.
Hence, we can assume without loss of generality that the triangulations of all 3-manifoldsD′
i and Di coincide
on the boundary and that the same holds for all triangulated 3-manifoldsRk andR′
k. Under this assumption,
the state sums ofDi and D′
i agree by Lemma 5.15 for all labelings. The state sums ofRk and R′
k are the
usual Turaev-Viro-Barrett-Westbury state sums for a spherical fusion category and are equal by Theorem 5.5.
With Corollary 4.10 this yields
Z(M,l∂M,b∂M,S ) =
∑
l∂
∑
b∂
n∏
i=1
Z(Di,l∂Di,b∂Di)
m∏
k=1
Z(Rk,l∂Rk,b∂Rk)
=
∑
l∂
∑
b∂
n∏
i=1
Z(D′
i,l∂D′
i
,b∂D′
i
)
m∏
k=1
Z(R′
k,l∂R′
k
,b∂R′
k
) =Z(M,l∂M,b∂M,S′),
where the sums are over all labelingsl∂ of internal edges inM that are boundary edges ofDi, D′
i and over
dual bases of the morphism spaces for internal triangles inM that are boundary triangles ofDi, D′
i.
Theorem 5.16 extends the definition of the state sum for a defect manifold to triangulations that are
non-generic or non-transversal in the interior ofM. Together with Proposition 5.14 it shows that slightly
perturbing the defect surface, defect lines or defect vertices in the interior ofM does not change the value of
the state sum. This allows one to define the state sum of a non-generic triangulation as the state sum of a
small generic deformation. Similarly, any triangulation ofM with non-transversal tetrahedra in the interior
can be refined by stellar subdivisions to a triangulation that is transversal. One can then perturb the defect
surfaces, lines and vertices to make it generic. By Theorem 5.16 all ways of doing so yield the same state sum.
Definition 5.17. Let M be a 3-manifold with defect data andT a triangulation ofM whose boundary
triangles are transversal and generic. Then for all boundary labelingsl∂M, b the state sum ofM is defined as
Z(M,l∂M,b∂M,T ) :=Z(M,l∂M,b∂M,T′), (91)
for any generic transversal triangulationT′ that coincides withT on ∂M.
Corollary 5.18. LetM be a 3-manifold with defect data andT,T′ triangulations ofM that coincide on
∂M and whose boundary triangles are transversal and generic. Then their state sums coincide for all
boundary labelingsl∂M, b∂M. In particular, ifM is closed, its state sum does not depend on the choice of the
triangulation.
In principle the dependence of the state sum on boundary triangulations and their labeling could be removed
in the same way as for Turaev-Viro-Barrett-Westbury state sums without defects. To obtain a topological
50
quantum field theory from the latter one considers the vector spacesV∂M (t,l ) = ⊗f∈∆tHom(f,l ) for a
given triangulationt of ∂M and a labelingl with simple objects. The state sum of a triangulated cyclinder
∂M× [0, 1] then defines a linear mapZ(∂M× [0, 1],l ) :V∂M (t0,l 0)→V∂M (t1,l 1), whereti is the boundary
triangulation of∂M×{i} and li its labeling. By taking the projective limit of the system of all such state
sums, one obtains the vector space that the associated TQFT assigns to∂M, see [TV17, Sec. 13.3.2].
It is clear that an analogous procedure could be applied to state sum models with defects and seems plausible
that this would result in a defect TQFT in the sense of [CMS20, CRS18] by Carqueville et al. For the
spherical fusion categoriesVecG from Example 1.1 and oriented surfaces of genusg≥ 1 cylinders with defects
are considered in Example 6.2.
