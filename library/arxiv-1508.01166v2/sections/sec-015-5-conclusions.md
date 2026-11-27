---
doc_id: arxiv-1508.01166v2
doc_title: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes"
section_id: sec-015-5-conclusions
section_title: "Conclusions"
section_number: 5
pages: 29-32
source_pdf: 1508.01166v2.pdf
source_sha256: 0abff3bfd7d3d3e4
toc_source: outline
doc_brief: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes — A conservative discretization of incompressible Navier-Stokes equations is de"
---
A conservative discrete exterior calculus discretization of Navier-Stokes equa-
tions was developed. The Navier-Stokes equations were ﬁrst rewritten using the
exterior calculus notation. The expression of Navier-Stokes equations using the
exterior calculus notation was derived from the standard vector calculus formu-
lation and veriﬁed against the coordinate invariant form in terms the exterior and
29
(a)
 (b)
(c)
 (d)
Figure 8: The vorticity contour plot for 6 vortices on a spherical surface at latitude
θ = 0.4 at time: (a) T =0.0 and (b) T =36.0. (c) The relative solution change
(||U(t)−U(0)||
||U(0)|| ) versus the simulation time. (d) The vorticity strength along a circle at
latitudeθ = 0.4.
30
Lie derivatives.
The discretization was carried out through the substitution by the discrete exte-
rior calculus operators deﬁned on simplicial meshes. Both 2D and 3D discretiza-
tions were developed, but with numerical implementations only for ﬂows over
surfaces. The main distinction between the developed discretization and previ-
ous unstructured conservative discretizations was in the convective term. In the
2D case, the current convective term discretization is di ﬀerent from all previous
DEC-based discretizations and most of the covolume method discretizations. The
developed discretization has similarities with the covolume discretization by Perot
[10] only for the special case of a structured-triangular mesh. Nevertheless, unlike
all covolume discretizations, the presented discretization is capable of simulating
ﬂows over both ﬂat and curved surfaces. In regards to the 3D case, the current
convective term discretization is diﬀerent from all previous unstructured conser-
vative discretizations. An additional merit of the presented methodology is the
manipulation of the convective term through algebraic discretization of the in-
terior product operator and a combinatorial discretization of the wedge product.
Such approach paves the way to explore the application of the ﬁnite element ex-
terior calculus method to discretize Navier-Stokes equations. Moreover, it gives
insight into the discretization of similar convective terms in other physics prob-
lems; e.g. the magnetohydrodynamics governing equations.
Several 2D simulation experiments were carried out to benchmark the dis-
cretization performance. The convergence of the velocity 1-forms (i.e. ﬂuxes)
was found to be of second order for structured-triangular meshes and of ﬁrst order
otherwise. This is in agreement with previous theoretical estimations developed
for the covolume method. In regards to the conservation properties, due to the dis-
cretization construction, both the mass and the vorticity are conserved locally and
globally up to the machine precision. The kinetic energy relative error converged
in a second order fashion with the mesh size for ﬂows over ﬂat surfaces. The
convergence of the kinetic energy relative error with the time step was also found
to be of a second order for ﬂows over both ﬂat and curved surfaces. Such conser-
vation properties, the ability to simulate ﬂows over both ﬂat and curved surfaces
and the relatively small size of the linear system make the presented discretization
attractive for both physics and engineering applications.
Acknowledgments
This research was supported by the KAUST O ﬃce of Competitive Research
Funds under Award No. URF/1/1401-01.
31
