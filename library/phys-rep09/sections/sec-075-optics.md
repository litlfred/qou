---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-075-optics
section_title: "Optics"
section_number: null
pages: 82-83
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
In the review paper [228] one can find references to some early applications of ME to Optics. For example, to Hamiltonians
involving the generators of SU(2), SU(1, 1) and Heisenberg—Weyl groups, with applications to laser-plasma scattering and
pulse propagation in free-electron lasers. Here, as representatives of the more modern interest of ME in Optics, we quote
two applications referring to Helmholtz equation, and to the study of Stokes parameters.

Helmholtz equation in one spatial dimension with a variable refractive index n(x) reads

W(x) + Pr? (x) W(x) = 0, (358)
where k is the wavenumber in vacuum.
S. Blanes et al. / Physics Reports 470 (2009) 151-238 233

Recently, this time-honored wave equation has been treated in two different ways, both using ME. From a more formal
point of view, in [229] Helmholtz equation is analyzed following the well known procedure followed by Feshbach and Villars
to convert the second order relativistic quantum Klein-Gordon differential equation for spin-0 particles in a first order
differential equation involving two components wave functions (the original wave function and its time derivative). The
evolution operator for Helmholtz equation is then a 2 x 2 matrix which evolves according to the fundamental equation (4),
with the only difference that now the evolution parameter is x instead of t. In [229] the whole procedure is explained and
the main physical consequence, which amounts to the addition of correcting terms to the Hamiltonian, is discussed in the
case of an axially symmetric graded-index medium, i.e. one in which the refractive index is a polynomial.

Helmholtz equation has also been investigated with the help of ME in [227,230,231]. Here, the propagation in a slowly
varying waveguide is considered, and the boundary value problem is converted into an initial value problem by the
introduction of appropriate operators which are shown to satisfy Eq. (4). Numerical methods to fourth order borrowed
from [37] are then used.

Since the mid 19th century, the polarization state of light, and in general electromagnetic radiation or any other
transverse waves, is described by the so-called Stokes parameters, which constitute a four-dimensional vector S(w)
depending on the frequency w. When the light traverses an optical element which acts on its polarization state, the in
and out Stokes vectors are related by

Sour(@) = M(@)Sin(@), (359)
where the 4 x 4 matrix M(w) is called the Mueller matrix. It can be proved [232,233] that it satisfies the equation
M'(w) = H(@)M(), ~~ M(wo) = Mo, (360)

where, now, the prime denotes derivative with respect to the real independent variable w. For systems with zero
polarization-dependent loss (PDL) and no polarization mode dispersion (PMD), H(w) is constant, whereas with PDL and
PDM, the previous equation is just our Eq. (4) and the appropriateness of ME is apparent. The matrix H(@) in this application
has a Hermitian and a non-Hermitian component. ME has allowed a recursive calculation of successive orders of the
frequency variation of the Mueller matrix. This yields PMD and PDL compensators that counteract the effects of PMD and
PDL with increased accuracy.

Also related to the use of Stokes vector, one can mention the so-called radiative transfer equation for polarized light. It is
relevant in Astrophysics to measure the magnetic fields in the Sun and stars. That equation gives the variation of $(z) with
the light path z

d
—S(z) = —K(z)S(z) + J,
dz

where S is the Stokes vector, K is a 4 x 4 matrix which describes absorption in the presence of Zeeman effect and J stands
for the emission term. In [234-236] ME is used to obtain an exponential solution.
