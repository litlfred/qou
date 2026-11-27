---
doc_id: arxiv-1508.01166v2
doc_title: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes"
section_id: sec-011-44-double-periodic-shear-layer
section_title: "Double periodic shear layer"
section_number: 4.4
pages: 21-24
source_pdf: 1508.01166v2.pdf
source_sha256: 0abff3bfd7d3d3e4
toc_source: outline
doc_brief: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes — A conservative discretization of incompressible Navier-Stokes equations is de"
---
4.4. Double periodic shear layer
The simulation of a double periodic shear layer is carried out for an inviscid
ﬂow (µ = 0) over a square domain of unit edge length. The initial ﬂow repre-
21
sents a shear layer of ﬁnite thickness with a small magnitude of vertical velocity
perturbation. The initial velocity vector ﬁeld is expressed as [29]
ux =

tanh((y− 0.25)/ρ), for y≤ 0.5,
tanh((0.75− y)/ρ), for y> 0.5,
uy =δ sin(2πx),
(24)
withρ = 1/30 and δ = 0.05. The initial velocity 1-forms u are approximated by
integrating mass ﬂux normal to the primal edges and then multiplying this ﬂux by
the discrete Hodge star operator∗1. Periodic boundary conditions are imposed on
all domain boundaries. Therefore, it is only required to ﬁx the stream function at
one primal node to an arbitrary value in order to get a unique solution.
Five simulations are conducted using a time step of ∆t = 0.001 on structured-
triangular meshes with number of elements equal to 3042, 12482, 32258, 50562
and 204800. Fig. 5 shows the evolution of the vorticity contour plot with time,
using the ﬁnest mesh. At time T = 0.8, two vortices appear to be well resolved.
The shear layer connecting the coherent vortices becomes thinner with time and
within a ﬁnite time interval reach the resolution of the mesh after which dispersion
error is manifested as mesh level oscillations. The vorticity contour plot in Fig. 5
exhibit similarities with previous simulations by Bell et al. [29].
The convergence of the kinetic energy error with the mesh size is investigated.
The kinetic energy is calculated as
∫
Ω u.u dΩ, where the integration is carried out
over the entire simulation domain. The velocity vector is calculated in each tri-
angular element via Whitney map interpolation, as described before. The kinetic
energy relative error ( KE (0)−KE (T)
KE (0) ) is then calculated at time T = 2.0 and plotted
versus the mesh characteristic length in Fig. 5d. Except for the coarsest mesh
case, the kinetic energy relative error converges in a second order fashion with the
mesh size, which is expected from a scheme that is second order for structured-
triangular meshes. Overall, the kinetic energy relative error is modest, with a
0.3% error for the coarsest mesh (equivalent to a 40 × 40 Cartesian mesh) and
only 0.01% error for the ﬁnest mesh (equivalent to a 320× 320 Cartesian mesh).
For the mesh with 50562 triangular elements (equivalent to a 128× 128 Cartesian
mesh), the kinetic energy relative error is 0.039%, almost one order of magnitude
lower than a second order collocated mesh scheme using almost the same mesh
size [29].
22
(a)
 (b)
(c)
 (d)
Figure 5: The vorticity contour plot for double periodic shear layer with a mesh
of 204800 elements at time: (a) T=0.0, (b) T=0.8 and (c) T=1.2. (d) The conver-
gence of the relative kinetic energy error (KE (0)−KE (T)
KE (0) ) with the characteristic mesh
length at simulation timeT = 2.0. The dashed red line represents the second order
slope.
23
