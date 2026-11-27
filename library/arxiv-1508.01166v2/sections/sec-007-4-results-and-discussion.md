---
doc_id: arxiv-1508.01166v2
doc_title: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes"
section_id: sec-007-4-results-and-discussion
section_title: "Results and Discussion"
section_number: 4
pages: 18-18
source_pdf: 1508.01166v2.pdf
source_sha256: 0abff3bfd7d3d3e4
toc_source: outline
doc_brief: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes — A conservative discretization of incompressible Navier-Stokes equations is de"
---
In order to benchmark the performance of the presented discretization, sev-
eral 2D simulation experiments are performed for ﬂows over both ﬂat and curved
surfaces. During all simulations, Eqs. (18) and (19) are solved consecutively at
each time step, where direct LU decomposition solver is used to solve the linear
systems. As pointed out earlier, the mass conservation is guaranteed by the dis-
cretization construction. V orticity is also locally conserved due to the discretiza-
tion construction, as shown earlier by Perot [10]. Global vorticity conservation up
to the machine precision was observed during all conducted simulations, where in
the presence of solid walls the vorticity ﬂux comes only from the no slip bound-
aries as it should be for incompressible ﬂows. Therefore, the results presented
below mainly quantify the numerical convergence rate of the discretization and
the conservation of the kinetic energy.
