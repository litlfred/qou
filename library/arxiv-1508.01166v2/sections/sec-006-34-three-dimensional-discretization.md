---
doc_id: arxiv-1508.01166v2
doc_title: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes"
section_id: sec-006-34-three-dimensional-discretization
section_title: "Three dimensional discretization"
section_number: 3.4
pages: 16-18
source_pdf: 1508.01166v2.pdf
source_sha256: 0abff3bfd7d3d3e4
toc_source: outline
doc_brief: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes — A conservative discretization of incompressible Navier-Stokes equations is de"
---
The three-dimensional DEC discretization of NS equations is brieﬂy presented
in this subsection. In the 3D situation, the primal mesh consists of 3-simplices
(tetrahedra), 2-simplices (triangles), 1-simplices (edges) and 0-simplices (nodes).
The duals to these primal mesh entities consist of 0-cells (dual nodes), 1-cells
(dual edges), 2-cells (polygons) and 3-cells (polyhedra), respectively. The space
of the discrete k-forms deﬁned on primal/dual mesh complexes is deﬁned accord-
ing to the diagram in Eq. (13).
Following the same methodology in Section 3.3, we start the discretization
of Eq. (11) by choosing to deﬁne the 2-forms d u♭, in the time derivative term,
on the dual 2-cells (polygons). It then follows that the velocity 1-forms u♭ in
this term are deﬁned on the dual 1-cells (i.e. dual edges). The velocity 1-forms
deﬁned on the dual edges are denoted by u. It also follows, based on the diagram
in Eq. (13), that the velocity 1-forms in the viscous term are also deﬁned on the
dual edges. In regards to the convective term, since d ∗ (u♭∧∗ du♭) is deﬁned
on the dual 2-cells, then ∗(u♭∧∗ du♭) has to be deﬁned on the dual 1-cells (dual
edges), and therefore (u♭∧∗ du♭) is deﬁned on the primal 2-simplices (triangles).
Since u♭ is a 1-form, then ∗du♭ is also 1-form (in the 3D case), and therefore
the wedge product is carried out between two 1-forms, where the outcome of this
wedge product is deﬁned on the primal triangles. This implies that both the wedge
product portions are deﬁned on the primal edges. Accordingly, the 1-form∗du♭ is
deﬁned on the primal edges, which makes u♭ in this portion to be deﬁned on the
dual edges. Finally, the ﬁrst velocity 1-form in the wedge product term is deﬁned
on the primal edges. We denote the velocity 1-forms deﬁned on the primal edges
by v.
Substituting with the appropriate discrete operators, with N = 3 for the 3D
case, the discretization of Eq. (11) then takes the form
dT
1
Un+1− Un
∆t +µdT
1∗2 d1∗−1
1 dT
1 U− dT
1∗2 Wv∗−1
1 dT
1 U = 0, (20)
where U is a vector containing the dual (normal) velocity 1-forms u for all mesh
dual edges, and Wv is a sparse matrix representing the action of the discrete wedge
product operator. It is worth noting that similar to Eq (15), the operator d T
1 needs
16
to be complemented by another operator that closes some of the dual 2-cells on
the domain boundary. Such a complementary matrix is omitted in Eq. (20) for
simplicity, but its existence should always be considered during numerical imple-
mentations.
According to the deﬁnition in [15] (pg. 74 Eq. (7.2.1)), the wedge product of
a discrete primal 1-form α and a discrete primal 1-form β deﬁned over a primal
2-simplex (triangle) [i, j, k] is
⟨α∧β, [i, j, k]⟩ = 1
6(⟨α, [i, j]⟩⟨β, [ j, k]⟩−⟨ α, [i, k]⟩⟨β, [k, j]⟩
−⟨α, [ j, i]⟩⟨β, [i, k]⟩ +⟨α, [ j, k]⟩⟨β, [k, i]⟩
+⟨α, [k, i]⟩⟨β, [i, j]⟩−⟨ α, [k, j]⟩⟨β, [ j, i]⟩),
(21)
with the property ⟨α, [i, j]⟩ =−⟨α, [ j, i]⟩. Recalling that ∗−1
1 dT
1 U is a vector of
N1 rows, Wv is then a sparse N2× N1 matrix. For each row in Wv correspond-
ing to a primal triangle, the only non-zero entries in this row are for the primal
edges belonging to this triangle. For a primal triangle [ i, j, k], the matrix entry
corresponding to the edge [i, j] is 1
6(⟨v, [k, i]⟩−⟨ v, [ j, k]⟩).
Following the procedure in section 3.3, the velocity 1-forms are substituted
by their deﬁnition in terms of a stream function; i.e. U =∗2d1Ψ. According to
the diagram in Eq. (13), the vector Ψ includes the stream functions ψ deﬁned as
1-forms on the primal mesh edges ( ψ∈ C1(K)). Substituting in Eq. (20), the
resulting linear system is
dT
1
1
∆t∗2 d1Ψn+1 +µdT
1∗2 d1∗−1
1 dT
1∗2 d1Ψ− dT
1∗2 Wv∗−1
1 dT
1∗2 d1Ψ = dT
1
1
∆tUn. (22)
The degrees of freedom in the above linear system are the stream function
1-forms (scalars) deﬁned on the primal edges. Therefore, the resulting system is
a sparse N1× N1 linear system. The time discretization of Eq. (22) can then be
implemented similar to the 2D case.
The presented 3D discretization of the viscous term in Eq. (22) is similar
to previous DEC-based [13, 14] and covolume method [7, 11] discretizations.
However, using the interior product deﬁnition in Eq. (9) and the discrete wedge
product deﬁnition in Eq. (21) makes the present discretization di ﬀerent from all
previously developed 3D DEC-based/covolume discretizations.
17
