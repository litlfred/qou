---
doc_id: arxiv-1508.01166v2
doc_title: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes"
section_id: sec-009-42-taylor-green-vortices
section_title: "Taylor-Green vortices"
section_number: 4.2
pages: 18-19
source_pdf: 1508.01166v2.pdf
source_sha256: 0abff3bfd7d3d3e4
toc_source: outline
doc_brief: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes — A conservative discretization of incompressible Navier-Stokes equations is de"
---
The simulation of Taylor-Green vortices is carried out on a square domain of
dimension [−π,π ] in both x and y directions. The decay of Taylor-Green vortices
with time has an analytical solution that for the 2D case is expressed as [26, 27]
ux =− cos(x) sin(y)e−2νt
uy = sin(x) cos(y)e−2νt (23)
18
(a)
 (b)
Figure 2: Cross-section of the velocity proﬁle at the two domain center lines for
driven cavity test case at Reynolds number = 1000.
withν to be the kinematic viscosity. The simulation is conducted using a Delaunay
mesh consisting of 50852 elements with periodic boundary conditions applied on
all domain boundaries. This requires only to ﬁx the stream function at one primal
node to an arbitrary value in order to get a unique solution. The simulation is
carried out using a time step ∆t = 0.1 and kinematic viscosityν = 0.01.
Fig. 3a shows the vorticity contour plot for Taylor-Green vortices at simulation
time T = 10. A cross section of the velocity y-component uy along the horizontal
domain center line is shown in Fig. 3b. The simulation velocity proﬁle is in good
agreement with the analytical solution, as shown in Fig. 3b. This represents a
qualitative indication of the reliability of the current numerical implementation to
reproduce the evolution of such unsteady ﬂow with time.
