---
doc_id: arxiv-1508.01166v2
doc_title: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes"
section_id: sec-008-41-driven-cavity
section_title: "Driven cavity"
section_number: 4.1
pages: 18-18
source_pdf: 1508.01166v2.pdf
source_sha256: 0abff3bfd7d3d3e4
toc_source: outline
doc_brief: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes — A conservative discretization of incompressible Navier-Stokes equations is de"
---
Driven cavity simulations are carried out on a unit square domain at Reynolds
number (Re) of 1000. Solid wall boundary conditions are imposed on the left,
right and bottom boundaries. The top boundary has zero ﬂux (i.e. u), and a unit
tangential velocity (i.e. v) boundary conditions. Therefore, the stream functions
on all boundary nodes are set to an arbitrary constant value. The ﬂuid dynamic
viscosity (µ = 1/Re in our normalized units) is set to 0.001, and the time step is
∆t = 0.1. The simulations are carried out on a Delaunay mesh and a structured-
triangular mesh (consisting of isosceles right triangles) with 32482 and 32258 ele-
ments, respectively, which has almost the same resolution as a 128×128 Cartesian
mesh.
Fig. 2 shows cross-sections at the domain center lines for the steady state
velocity proﬁle at simulation time T = 100. The results are compared with well-
established simulations by Ghia et al. [25] for Re = 1000 using a 128 × 128
Cartesian mesh. The comparison shows an agreement with Ghia’s results for both
mesh types, which reﬂects the numerical solution ﬁdelity.
