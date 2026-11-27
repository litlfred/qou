---
doc_id: arxiv-1508.01166v2
doc_title: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes"
section_id: sec-013-46-taylor-vortices-on-a-spherical-surface
section_title: "Taylor vortices on a spherical surface"
section_number: 4.6
pages: 26-27
source_pdf: 1508.01166v2.pdf
source_sha256: 0abff3bfd7d3d3e4
toc_source: outline
doc_brief: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes — A conservative discretization of incompressible Navier-Stokes equations is de"
---
The ability of the current discretization to simulate ﬂows over curved surfaces
is explored for an inviscid ﬂow test case over a spherical surface. The spherical
surface, with radius equal to 1.0, is approximated by a simplicial mesh consisting
of ﬂat triangles connecting the primal nodes, where the primal nodes are posi-
tioned on the smooth spherical surface (at radius = 1.0). For each primal edge,
its dual is the kinked line connecting the circumcenters of the two neighboring
triangles through the primal edge’s midpoint. During the discrete Hodge star op-
erator calculations, the length of a dual edge is its length as a kinked line. On the
other hand, for each primal node, its dual is the non-planar polygon consisting of
26
sector contributions from all the ﬂat triangles sharing the primal node, and its area
is calculated accordingly as a non-planar surface area.
The test case investigated in this section is for two Taylor vortices initially
positioned on a spherical surface and their evolution with time is simulated. The
spherical surface domain is initialized with two vortices each have the distribution
given in Eq. (25), with G = 0.5, a = 0.1. When calculating the vorticity at any
mesh node via Eq. (25), the distance r is measured along the sphere surface; i.e.
geographical distance. The centers of the two vortices are separated by a distance
of 0.4. The simulation is carried out using a mesh containing 327680 triangular
elements.
In order to recover the velocity 1-forms from the vorticity distribution, the
Poisson equation (26) is solved. During the Poisson equation solution, the stream
function at one primal node need to be ﬁxed in order to obtain a unique solution.
Using the resulting velocity 1-forms as an initial condition, the evolution of the
two vortices is then simulated using various time steps in the range [1.0− 0.05].
Fig. 7 shows the evolution of the vorticity contour plot with time. Again, the
two vortices move apart with a thin vortex sheet connecting them. The conver-
gence of the kinetic energy relative error with the time step is investigated after
simulation time T = 10.0, as shown in ﬁgure 7d. Similar to the ﬂow over a ﬂat
surface, a second order rate, on average, is observed for the convergence of the ki-
netic energy relative error with the time step. This again can be due to the two-step
time stepping scheme implemented during the current discretization.
