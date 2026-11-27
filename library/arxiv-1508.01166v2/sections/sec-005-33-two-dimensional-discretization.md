---
doc_id: arxiv-1508.01166v2
doc_title: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes"
section_id: sec-005-33-two-dimensional-discretization
section_title: "Two dimensional discretization"
section_number: 3.3
pages: 10-16
source_pdf: 1508.01166v2.pdf
source_sha256: 0abff3bfd7d3d3e4
toc_source: outline
doc_brief: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes — A conservative discretization of incompressible Navier-Stokes equations is de"
---
The two-dimensional DEC discretization of Navier-Stokes equations is de-
rived in this subsection and the three-dimensional discretization in the next sub-
section. As pointed out by Hirani et al. [17], due to the intrinsic coordinate inde-
pendent nature of exterior calculus, the derivation below, for the 2D case, results
in a numerical method that works without change for both planar domains and
curved surfaces. The dimension of the embedding space does not matter, neither
do the details of the embedding. This characterizes a key distinction between the
DEC-based approach and the covolume method. In the latter, the discretization of
NS equations was commenced by taking the dot product of the momentum equa-
tion and the vectors perpendicular to the triangles’ faces. Such normal vectors
may not be unique for a simplicial mesh approximation of a curved surface.
The discretization of NS equations is carried out here following the exact frac-
tional step method [4, 22]. This consists mainly of two steps, the ﬁrst is to dis-
cretize the vorticity formulation of NS equations (Eq. (11)), and the second is
to substitute the velocity by its deﬁnition as the curl of a stream function, where
the latter in its discrete manifestation becomes the unknown degrees of freedom
in the resulting linear system. Su ﬃcient details are provided since the numerical
experiments presented in this paper are limited only to two-dimensional ﬂow test
cases.
Discrete exterior calculus discretization of Eq. (11) ﬁrst requires the location
on the mesh where one deﬁnes the discrete variables such that the smooth forms
are satisﬁed in an integrated sense. Then, the smooth forms are replaced with their
discrete counterparts, and the smooth operators are substituted by the appropriate
discrete operators. Starting with the time derivative term in Eq. (11), we choose
to deﬁne the 2-form d u♭ on the dual 2-cells. Accordingly, all the other terms of
Eq. (11) are constrained to be deﬁned on the dual 2-cells for consistency. Back
10
to the time derivative term, it then follows, according to the diagram in Eq. (12),
that the velocity 1-form u♭ in this term is deﬁned on the dual 1-cells (i.e. dual
edges). We denote the velocity 1-form u♭ deﬁned on the dual edges by u, which
represents the integration of the velocity vector ﬁeld along the dual edges; i.e.
u =
∫
⋆σ1 u.dl∈ D1(⋆K). The velocity 1-form u may be referred to as the normal
velocity form or the ﬂux, since it represents the velocity normal to the triangles’
faces (i.e. primal edges). Similarly for the viscous term in Eq. (11), it follows
from the diagram in Eq. (12) that the velocity 1-form in this term is also deﬁned
on the dual edges.
In regards to the convective term, because the term d∗ (u♭∧∗ du♭) is deﬁned
on the dual 2-cells, the term∗(u♭∧∗ du♭) has to be deﬁned on the dual edges, and
therefore (u♭∧∗ du♭) is deﬁned on the primal edges. Since u♭ is a 1-form, then
∗du♭ is a 0-form (in 2D), and therefore the wedge product is carried out between a
1-form and a 0-form, such that the outcome of this wedge product must be deﬁned
on the primal edges. This implies that both wedge product portions are deﬁned on
primal mesh objects. Accordingly, the velocity 1-form in the ﬁrst portion of the
wedge product term is deﬁned on the primal edges, whereas the velocity 1-form in
the second portion of the wedge product term is deﬁned on the dual edges, making
the 0-form∗du♭ to be deﬁned on the primal nodes. We denote the velocity 1-form
u♭ deﬁned on the primal edges byv; i.e. v =
∫
σ1 u.dl∈ C1(K). The velocity 1-form
v represents the velocity tangential to the triangles edges.
After substituting with the appropriate discrete operators, with N = 2 for the
2D case, the discretization of Eq. (11) takes the form
[−dT
0 ]Un+1− Un
∆t −µ[−dT
0 ]∗1 d0∗−1
0
[
[−dT
0 ]U + dbV
]
+ [−dT
0 ]∗1 Wv∗−1
0
[
[−dT
0 ]U + dbV
]
= 0, (15)
where U is the vector containing the dual (normal) velocity 1-formsu for all mesh
dual edges, and the discrete wedge product of the tangential velocity 1-formv with
the 0-form∗du is represented by the Wv matrix, where the matrix Wv contains the
values of the tangential velocity 1-formv. The superscripts n and n + 1 in the time
derivative term are due to time discretization and these subscripts are suppressed
for the convective and viscous terms, deferring the time discretization of the vis-
cous and convective terms until later in this subsection. The discrete operation
[−dT
0 U] evaluates the circulation of the velocity forms u along the dual 2-cells
boundaries. Since a portion of these dual 2-cells boundaries may consists of pri-
11
mal edges, as discussed in Section 3.2, [dbV] then complements the velocity circu-
lation, accounting for the part that depends on the velocity 1-formsv on the primal
boundary edges. The vector V contains the tangential velocity 1-forms v for all
mesh primal edges, and the matrix d b is then deﬁned as d b = 0.5|dT
0|diag(dT
1 12),
where|dT
0| is the matrix d T
0 with all entries made non-negative and 12 is a vector
of ones with N2 entries, and diag(.) to be a diagonal matrix composed of the en-
closed vector entries. The subscript b emphasizes the fact that db “closes” the dual
2-cells for the boundary vertices by traversing along the primal boundary edges
in the orientation direction of the dual 2-cells. Such a boundary contribution van-
ishes in the time derivative term due to the time discretization. It also vanishes for
the other d T
0 operators in both the viscous and the convective terms, as shown in
Appendix A.
A deﬁnition for the discrete primal-primal wedge product was developed in
[15] (pg. 74 Eq. (7.2.1)), according to which the wedge product between a discrete
primal 1-formα and a discrete primal 0-formβ deﬁned over a primal edge [i, j] is
⟨α∧β, [i, j]⟩ = 1
2 (⟨α, [i, j]⟩⟨β, [ j]⟩−⟨ α, [ j, i]⟩⟨β, [i]⟩)
= 1
2⟨α, [i, j]⟩(⟨β, [i]⟩ +⟨β, [ j]⟩),
(16)
where [i, j] is the edge formed by nodes [ i] and [ j],⟨α, [i, j]⟩ is the discrete form
α deﬁned on the simplex [i, j], with the property⟨α, [i, j]⟩ =−⟨α, [ j, i]⟩. Recalling
that∗−1
0 [−dT
0 ]U is a vector withN0 entries, Wv is a sparse N1×N0 matrix deﬁned as
Wv = 0.5 diag(V)|d0|. Accordingly, the action of this wedge product operation (in
2D) at each primal edge is to take the average of the vorticity∗−1
0 [−dT
0 ]U evaluated
at the edge’s nodes and multiply it by the edge’s tangential velocity 1-formv. It is
worth noting that the vector U in Eq. (15) includes the normal velocity 1-forms u
for all mesh edges, including those that might be given as boundary conditions.
In order to obtain a linear representation for the convective term, we con-
sider the tangential velocity 1-forms v to be given through an interpolation of
previously-known normal velocity 1-forms u. A velocity vector ﬁeld can be cal-
culated inside each triangle through the interpolation of the velocity 1-forms∗−1
1 u
deﬁned on the triangle’s faces. The interpolation is carried out here using Whitney
maps [17]. Since the velocity 1-forms ∗−1
1 u are closed forms; i.e. d 1∗−1
1 u = 0,
the interpolation will result in a constant velocity vector ﬁeld over each triangle
(see [23], theorem 5.4). The constant vector ﬁeld obtained by Whitney map in-
terpolation is the one that would result from requiring a constant vector ﬁeld with
the given ﬂuxes of an incompressible vector ﬁeld. It is worth noting that other in-
12
terpolation methods, like these in [4], can also be used to interpolate the velocity
vector on triangles, which would result in velocity vectors not signiﬁcantly diﬀer-
ent from these interpolated using Whitney maps. The tangential velocity 1-forms
v can be then calculated on each primal edge by averaging the velocity vector
ﬁelds on the triangles sharing the edge.
The second step in the exact fractional step method is to substitute for the ve-
locity 1-forms u (in Eq. (15)) by its deﬁnition as the curl of a stream function. The
incompressibility condition (Eq. (4b)) in DEC notation is expressed as∗2d1∗−1
1 U.
This implies that the vector U is in the null space of the matrix [∗2d1∗−1
1 ]. Since
[∗2d1∗−1
1 ][∗1d0] =∗2d1d0 = 0, the columns of the matrix [ ∗1d0] then contain a
basis of the null space of [∗2d1∗−1
1 ]. Therefore, the vector U can uniquely be ex-
pressed in terms of the basis [∗1d0]; i.e., U =∗1d0Ψ. In vector calculus notation,
this is equivalent to expressing a divergence-free velocity vector as the curl of a
stream function. According to the diagram in Eq. (12), the vector Ψ includes the
stream functionψ deﬁned as 0-forms on the primal mesh nodes (i.e. ψ∈ C0(K)).
Substituting with this representation of U, Eq. (15) becomes
1
∆t[−dT
0 ]∗1 d0Ψn+1−µ[−dT
0 ]∗1 d0∗−1
0 [−dT
0 ]∗1 d0Ψ
+ [−dT
0 ]∗1 Wv∗−1
0 [−dT
0 ]∗1 d0Ψ = F, (17)
with the vector F = 1
∆t[−dT
0 ]Un +µ[−dT
0 ]∗1 d0∗−1
0 dbV− [−dT
0 ]∗1 Wv∗−1
0 dbV. Eq.
(17) describes the resultant linear system to be solved. The degrees of freedom
in the above linear system are the stream function 0-forms (scalars) deﬁned on
the primal mesh nodes. Therefore, the resulting system is a sparse N0× N0 linear
system.
For the current 2D case, it is worth noting the correspondence between the
velocity 1-form u and the mass ﬂux across the primal edges. While the discrete
velocity form u is formally deﬁned as the integration of the velocity ﬁeld on the
dual edges ( u =
∫
⋆σ1 u.dl), it can be used to approximate the mass ﬂux normal
to the primal faces (edges) as u f =∗−1
1 u. The incompressibility condition then
implies a zero summation of the mass ﬂuxes across the faces (edges) of each
triangular element; i.e., d 1u f = d1[∗−1
1 u] = 0. On the other hand, if the mass ﬂux
across the primal edges is the known quantity, it can be used to approximate the
velocity 1-form u as u =∗1u f . Recalling that the actual degrees of freedom in
the present discretization are the stream functions ψ and the velocity 1-form u is
calculated as u =∗1d0ψ, the mass ﬂux across the primal edges is then u f = d0ψ.
13
This implies that it is the mass ﬂux u f that is calculated ﬁrst and is then used to
approximate the velocity 1-form u as u =∗1u f =∗1d0ψ. Such a correspondence
between the velocity 1-formu and the mass ﬂux u f provides some ﬂexibility in the
case that an initial analytical expression for the velocity vector ﬁeld deﬁned on a
smooth surface is available. In order then to set the initial solution on the discrete
triangulation objects, it is possible to calculate u f by integrating the mass ﬂux
normal to hypothetical curved primal edges and then approximate u as u =∗1u f .
Otherwise, the velocity 1-formu can be initialized by integrating the velocity ﬁeld
on hypothetical curved dual edges. It is worth noting that the integration of the
mass ﬂux might be preferred in order to accurately guarantee zero net mass ﬂux
across the domain boundaries.
We now elaborate on the time discretization wherein the linear system in Eq.
(17) is solved in two steps as a predictor-corrector method. First, we advance the
system explicitly by a half time step
[ 1
0.5∆t[−dT
0 ]∗1 d0
]
Ψn+ 1
2 = F +
[
µ[−dT
0 ]∗1 d0∗−1
0 [−dT
0 ]
−[−dT
0 ]∗1 Wn
v∗−1
0 [−dT
0 ]
]
∗1 d0Ψn, (18)
where the matrix Wn
v incorporates the tangential velocity forms v at time n. Af-
ter solving the linear system (18), the normal velocity 1-forms at time n + 1
2 are
calculated as Un+ 1
2 =∗1d0Ψn+ 1
2 . These normal velocity 1-forms are then used to
predict, at time stepn+ 1
2, the velocity vector ﬁeld at each triangle element through
Whitney map interpolation [17]. The tangential velocity 1-form v is then calcu-
lated at each primal edge as the average of the velocity vectors in the neighboring
triangles, in the direction of the primal edge, multiplied by the primal edge length.
This results in the tangential velocity 1-forms v at time n + 1
2, and then W
n+ 1
2
v . The
latter matrix is then used to calculate the new velocity 1-formsu at time n+1. The
evaluation of the tangential velocity 1-formsv at half time step (n + 1
2) is expected
to improve the kinetic energy conservation, as was shown before by Perot [10] for
the covolume method. The second linear system to solve is then
[ 1
∆t[−dT
0 ]∗1 d0−µ[−dT
0 ]∗1 d0∗−1
0 [−dT
0 ]∗1 d0
+[−dT
0 ]∗1 W
n+ 1
2
v ∗−1
0 [−dT
0 ]∗1 d0
]
Ψn+1 = F, (19)
14
where the right hand side vector F in both Eqs. (18) and (19) also contains the
contribution from any stream function Ψ boundary conditions.
The solution of the Navier-Stokes equations through the exact fractional step
method is known to signiﬁcantly reduce the size of the solved linear system
[4, 22]. While the discretization of the momentum equation (10) would result
in a number of degrees of freedom equals to the number of edges plus the number
of triangles; i.e. (N1 + N2), the presented discretization has a number of degrees of
freedom equals only to the number of primal nodesN0. In addition to reducing the
linear system size, the presented discretization always maintains the incompress-
ibility error at the machine precision. Recalling the discrete incompressibility
condition∗2d1∗−1
1 U =∗2d1∗−1
1 ∗1d0Ψ =∗2d1d0Ψ, and since d1d0 = 0, the result-
ing formulation guarantees the mass conservation up to the machine precision,
regardless of the error incurred during the linear system solution. On the other
hand, the solution of the Navier-Stokes equations in terms of a stream function
might simplify or complicate the implementation of some boundary conditions.
A discussion regarding the implementation of various boundary conditions, in-
cluding the boundary conditions for interior walls (domain boundaries with zero
in/out ﬂow), through the stream function can be found in [22]. For the case of
interior boundaries with nonzero in/out ﬂow, the boundary conditions can be im-
plemented through Hodge decomposition manipulation for the stream functions.
More details regarding the implementation of such boundary conditions might be
addressed in future publications.
The presented discretization of NS equations has similarities with previous
discretizations. The viscous term discretization is similar to that previously de-
veloped through the covolume method [4, 6, 8, 9, 10] and DEC-based [13, 14]
discretizations. However, the discretization of the convective term via the inte-
rior product deﬁnition in Eq. (9) and the wedge product deﬁnition in Eq. (16)
makes the present discretization di ﬀerent from previous DEC-based discretiza-
tions that adopted Lie derivative advection techniques [13] or a ﬁnite-volume-
based approach [14] in discretizing the advection term. It also distinguishes the
present discretization from most of the covolume method discretizations, with
some similarity with the covolume discretization developed by Perot [10] only in
the special case of structured-triangular meshes; i.e. when the center points of the
primal edges and their dual edges coincide. Nevertheless, unlike all covolume dis-
cretizations, the current discretization is capable of simulating ﬂows over both ﬂat
and curved surfaces. In addition, the current manipulation of the convective term,
through the discrete wedge product operator, gives insight into other important
research themes. For example, it paves the way to exploring the discretization
15
of Navier-Stokes equations through the ﬁnite element exterior calculus method
[23, 24]. Furthermore, it gives insight into the discretization of other convective
terms in di ﬀerent physics problems; e.g. the magnetohydrodynamics governing
equations.
