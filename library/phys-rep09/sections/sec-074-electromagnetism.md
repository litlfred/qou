---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-074-electromagnetism
section_title: "Electromagnetism"
section_number: null
pages: 82-82
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
The Maxwell equations govern the evolution of electromagnetic waves. The equations are linear in the usual form and,
although they have been extensively studied, the complexity of obtaining approximate solutions is rather significant. When
reformulating the equations for a given problem, where the geometry, the boundary conditions etc, are considered, and
appropriate discretizations are taken into account, it is common to end with linear non-autonomous equations, so the
Magnus expansion can be of interest here.

To illustrate some possible applications, let us consider the Maxwell equations

OH 1

a =--VxE

dE 1 1 (355)
—=-VxH-— -J(t)

ot € €

where H, E, J are the magnetic and electric field intensities, and the current density, respectively, jz is the permeability
and ¢ is the permittivity. After space discretization, these equations turn into a large linear system of non-homogeneous
equations and Magnus integrators can, in principle, be applied. Time dependent contributions can also appear from boundary
conditions or external interactions. In some cases J = o E [225,226], so that, if the conductivity o is not constant, Magnus
integrators can be useful.
Let us now consider the frequency domain Maxwell equations (with J = 0)
V x E=iwyH
{ x H= —iweE (356)
where w is the angular frequency. These equations are of interest for time-harmonic light waves, propagating in a wave-
guiding structure composed of linear isotropic materials. If one is interested in the x and y components of H and E, and how
they propagate in the z direction, the equations to solve, after appropriate discretization, take the form [227]

d d
—iwe =a@yv,  —iwn = B@u. (357)
dz dz

Here u, v are vectors and A, B matrices depending on z, which, in this case, play the role of evolution parameter. A fourth-
order Magnus integrator has been used in [227]. From Section 5 we observe that higher order Magnus integrators, combined
with splitting methods, could also lead to efficient algorithms to obtain accurate numerical results with preserved qualitative
properties of the exact solution.
