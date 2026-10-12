---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-063-electromagnetism
section_title: "Electromagnetism"
section_number: null
pages: 82-82
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
The Maxwell equations govern the evolution of electromagnetic waves. The equations are linear in the usual form and,
although they have been extensively studied, the complexity of obtaining approximate solutions is rather significant. When
reformulating the equations for a given problem, where the geometry, the boundary conditions etc, are considered, and
appropriate discretizations are taken into account, it is common to end with linear non-autonomous equations, so the
Magnus expansion can be of interest here.
To illustrate some possible applications, let us consider the Maxwell equations



∂H
∂t = −
1
µ ∇× E
∂E
∂t =
1
ε ∇× H −
1
ε
J(t)
(355)
where H, E, J are the magnetic and electric field intensities, and the current density, respectively, µ is the permeability
and ε is the permittivity. After space discretization, these equations turn into a large linear system of non-homogeneous
equations and Magnus integrators can, in principle, be applied. Time dependent contributions can also appear from boundary
conditions or external interactions. In some cases J = σ E [225,226], so that, if the conductivity σ is not constant, Magnus
integrators can be useful.
Let us now consider the frequency domain Maxwell equations (with J = 0)

∇× E = iwµH
∇× H = −iwεE
(356)
where w is the angular frequency. These equations are of interest for time-harmonic light waves, propagating in a wave-
guiding structure composed of linear isotropic materials. If one is interested in the x and y components of H and E, and how
they propagate in the z direction, the equations to solve, after appropriate discretization, take the form [227]
−iwε
du
dz = A(z)v,
−iwµ
dv
dz = B(z)u.
(357)
Here u, v are vectors and A, B matrices depending on z, which, in this case, play the role of evolution parameter. A fourth-
order Magnus integrator has been used in [227]. From Section 5 we observe that higher order Magnus integrators, combined
with splitting methods, could also lead to efficient algorithms to obtain accurate numerical results with preserved qualitative
properties of the exact solution.
