---
doc_id: arxiv-1508.01166v2
doc_title: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes"
section_id: sec-010-43-poiseuille-flow
section_title: "Poiseuille flow"
section_number: 4.3
pages: 19-21
source_pdf: 1508.01166v2.pdf
source_sha256: 0abff3bfd7d3d3e4
toc_source: outline
doc_brief: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes — A conservative discretization of incompressible Navier-Stokes equations is de"
---
Poiseuille ﬂow simulations are carried out to investigate the numerical con-
vergence rate of the developed discretization. The simulations are conducted on
a unit square domain. Solid wall boundary conditions are imposed on the top
and bottom boundaries, while parabolic in/out ﬂow conditions are imposed on the
left/right boundaries. Therefore, by ﬁxing the stream function at one boundary
node, the stream functions at the rest of the boundary nodes can be directly cal-
culated based on the in /out ﬂux (i.e. u) boundary conditions. The simulation is
19
(a)
 (b)
Figure 3: (a) The vorticity contour plot for Taylor-Green vortices at time T = 10.
(b) Cross-section of the velocity y-component proﬁle at the horizontal center line
for Taylor-Green vortices at time T = 10.
carried out for structured-triangular, Delaunay and well-centered meshes of dif-
ferent resolutions. The well-centered mesh is a Delaunay mesh that is optimized
to make the circumcenter of each triangle to reside inside the triangle itself [28].
The exact solution of the velocity vector ﬁeld is given by u = [y(1− y), 0].
The L2-norm of the velocity 1-form ( u) error (see Hall et al. [4]) is calculated
as‖uexact− u‖ =
[∑
σ1
(
uexact−u
|σ1|
)2
|σ1|| ⋆σ 1|
]1/2
, and its convergence with the mesh
elements size is shown in Fig. 4. It is observed that the velocity 1-form (ﬂux)
error converges with a second order rate for the structured-triangular mesh case,
and with a ﬁrst order rate otherwise. This is in agreement with previous theoret-
ical analysis by Nicolaides [5] for the covolume method. Such analyses showed
that a necessary condition to obtain a second order convergence rate is to have
the midpoint of each primal edge to coincide with the midpoint of its dual edge,
which is satisﬁed only for a structured-triangular mesh or a mesh consisting of
equilateral triangles. The observed convergence rates are therefore in agreement
with theory. Regarding the unstructured meshes, the well-centered mesh error is
slightly smaller than the Delaunay mesh error, where both the well-centered and
Delaunay mesh implementations converge in a ﬁrst order fashion.
The convergence of the interpolated velocity vector ﬁeld is also investigated.
The velocity vector ﬁeld is calculated inside each triangle through the interpola-
20
Figure 4: The numerical convergence of the velocity 1-form (ﬂux) and the inter-
polated velocity vector for the Poiseuille ﬂow test case. The dashed lines represent
the 1-st and 2-nd order slopes.
tion of the velocity 1-forms ∗−1
1 u deﬁned on the triangle’s faces using Whitney
maps [17]. As pointed out earlier in section 3.3, such interpolation results in a
constant velocity vector ﬁeld over each triangle, implying a ﬁrst order interpola-
tion scheme. The velocity ﬁeld is interpolated over all triangles and the L2-norm
of the velocity vector error is calculated. The convergence of the velocity vector
error with the mesh size is shown in Fig. 4. A ﬁrst order convergence rate is
observed for all considered mesh types. Although the structured-triangular mesh
exhibited a second order convergence for the ﬂux 1-forms, the interpolated veloc-
ity vector converges with a ﬁrst order rate. This can be attributed to the ﬁrst order
velocity interpolation scheme, which seems to dominate the velocity vector error.
This is conﬁrmed by calculating the velocity vector through the interpolation of
the exact ﬂux 1-forms (calculated by integrating the velocity analytical solution
over the dual edges), which also converges with a ﬁrst order rate, as shown in Fig.
