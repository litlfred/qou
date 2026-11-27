---
doc_id: arxiv-1508.01166v2
doc_title: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes"
section_id: sec-012-45-taylor-vortices-on-flat-surfaces
section_title: "Taylor vortices on flat surfaces"
section_number: 4.5
pages: 24-26
source_pdf: 1508.01166v2.pdf
source_sha256: 0abff3bfd7d3d3e4
toc_source: outline
doc_brief: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes — A conservative discretization of incompressible Navier-Stokes equations is de"
---
Two Taylor vortices are simulated for an inviscid ﬂow ( µ = 0) over a ﬂat
square domain of dimension [−π,π ] in both directions. The vorticity distribution
for each vortex is expressed as [30]
ω(x, y) = G
a
(
2− r2
a2
)
exp
(
0.5
(
1− r2
a2
))
, (25)
with G = 1.0, a = 0.3 and r is the distance between any ﬁeld point and the vortex
center. The vorticity distribution in Eq. (25) ensures that the net circulation of
each Taylor vortex is zero.
The domain is initialized with a vorticity distribution for two vortices sep-
arated by a distance of 0 .8. Such a separation distance is just above the critical
bifurcation distance, below which the two vortices would merge [30, 31]. The vor-
ticity values are assigned to the primal nodes according to Eq. (25). The velocity
1-forms u are determined by solving the Poisson equation
∗−1
0 dT
0∗1 d0Ψ = X, (26)
where X is the vector containing the known vorticity values, and Ψ is the vector
containing the unknown stream functions on the primal nodes. No-ﬂux Dirichlet
boundary conditions are imposed on the domain boundaries during the Poisson
equation solution.
The Poisson equation is solved only once initially and the velocity 1-forms are
then calculated as U =∗1d0Ψ. Such velocity 1-forms are used as the initial state
for the simulations. When simulating the evolution of the two Taylor vortices,
periodic boundary conditions are imposed on all domain boundaries. Therefore,
it is only required to ﬁx the stream function at one primal node to an arbitrary
value in order to get a unique solution.
The simulations are carried out on a mesh consisting of 132204 equilateral
triangles, using various time steps in the range [1 .0− 0.002]. Fig. 6 shows the
vorticity contour plot evolution with time, using a time step of 0 .005. The two
vortices initially approach and turn over each other. The vortices then move apart,
as expected, with a thin vortex sheet connecting them that disappears at longer
simulation time.
The relative kinetic energy error is calculated at simulation timeT = 20.0 and
is plotted versus the time step in Fig. 6d. The ﬁgure shows a second order conver-
gence of the relative kinetic energy error over the entire range of time steps. Such
24
(a)
 (b)
(c)
 (d)
(e)
Figure 6: The vorticity contour plot for two Taylor vortices using a mesh consist-
ing of 132204 elements and a time step ∆t = 0.005 at time: (a) T =0.0, (b) T=3.0
and (c) T=5.0. (d) The convergence of the relative kinetic energy error with the
time step at simulation time T = 20.0. The dashed red line represents the second
order slope. (e) The evolution of the relative kinetic energy with time for two
Taylor vortices on a hexagonal domain.
25
time convergence rate can be due to the two-step time stepping scheme imple-
mented during the current discretization. For practical time steps that can resolve
the physics of the considered problem (e.g. ∆t < 0.01), trivial relative kinetic
energy error, below 0.01%, is observed.
Another simulation is carried out for two Taylor vortices on a hexagonal do-
main, aiming to compare with the Eulerian formulation developed by Pavlov et
al. [31]. The hexagonal domain has a side length of π and is meshed with 55296
equilateral triangular elements. The initial condition for the two Taylor vortices
is the same as in Eq. (25) (with G = 1.0 and a = 0.3), and periodic boundary
conditions are applied on all domain boundaries. Since the authors in [31] did
not state the time step they used, we choose to use a time step of 0.01 during this
test case. It is expected that the time step used in [31] will not be signiﬁcantly
larger than 0.01 since a simulation with a time step of 0 .02 was tested, however
the time step was not small enough to capture the expected behavior of the two
vortices, and the two vortices merged together when using the 0.02 time step. Fig.
6e shows the change in the relative kinetic energy for extended simulation time
up to T = 100. It is observed that the kinetic energy error is within the range of
0.003%, which is almost three orders of magnitude smaller than the error of 2.0%
reported in Pavlov et al. [31].
It is worth noting that the initial increase in the kinetic energy in Fig. 6e was
also observed for the previous test cases of Taylor vortices on a square domain, but
was comparable to the subsequent decrease in the kinetic energy only for the time
steps≤ 0.01. Therefore, for these time steps ≤ 0.01, the relative kinetic energy
error ( KE (0)−KE (T)
KE (0) ) in Fig. 6d was calculated by comparing with the kinetic energy
peak at time∼ 1.0 instead of the initial kinetic energy KE (0). This should better
represent how much kinetic energy loss the implemented scheme allows.
