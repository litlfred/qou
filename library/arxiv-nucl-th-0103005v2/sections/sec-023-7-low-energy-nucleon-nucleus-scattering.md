---
doc_id: arxiv-nucl-th-0103005v2
doc_title: "Quantum Monte Carlo Calculations of Light Nuclei"
section_id: sec-023-7-low-energy-nucleon-nucleus-scattering
section_title: "LOW-ENERGY NUCLEON-NUCLEUS SCATTERING"
section_number: 7
pages: 35-36
source_pdf: 0103005v2.pdf
source_sha256: c2aaa21b51d7bc10
doc_brief: "Quantum Monte Carlo Calculations of Light Nuclei — Accurate quantum Monte Carlo calculations of ground and low-lying excited states of light p-shell nuclei are now possible for realistic nuclear"
---
The calculations presented so far have treated resonant nuc lear states as if they
were particle stable; that is the VMC trial wave functions de cay exponentially
at large distances and the GFMC propagation does not impose a scattering-state
boundary condition. As was shown in Fig. 3, this GFMC propaga tion converges
for unstable states that are narrow, but for wide states, suc h as 8Be(4+), the
E(τ ) keeps decreasing for increasing τ . Such states should be computed using
scattering-wave boundary conditions.
The 5He( 1
2
−, 3
2
−) states have been studied in VMC (82) and GFMC (83) using
scattering-wave boundary conditions. The VMC calculation s use a trial function
that is a straight-forward generalization of the Ψ V given in Sec. 3. In it the Ψ J
contains one p-wave single-particle function that goes to z ero at a speciﬁed (large)
radius,Rn. The variational energy is minimized subject to this bounda ry condition.
The phase shift at the resulting scattering energy, Es = E(5He(Rn)) −E(4He) is
then obtained from
tan(δl) = jl(kRn)
nl(kRn), (56)
36 Steven C. Pieper and R. B. Wiringa
wherek = (2µEs)1/2/¯h,µ is the α+n reduced mass, and jl andnl are the spherical
Bessel functions (in this case l = 1). It is possible to generalize this formulation
by specifying a logarithmic-derivative at Rn, rather than having the wave function
go to zero there. This method requires the computation of the energy diﬀerence,
Es. If this is done with two diﬀerent VMC calculations, one for 5He with the
speciﬁed boundary condition, and one for 4He, then the statistical errors of these
two calculations must be added in quadrature. Instead one ca n directly evaluate
the energy diﬀerence in a VMC random walk that is controlled by the 5He wave
function. In practice this gives Es with a smaller statistical error than either of the
separate statistical errors (82). The GFMC calculations st art with the scattering-
state trial function and use a modiﬁed propagator that prese rves the boundary
condition (83). Both methods result in a phase shift and ener gy corresponding to
a given boundary condition. By repeating the calculations f or diﬀerent boundary
conditions, the phase shift as a function of energy can be map ped out.
The VMC calculations of Ref. (82) used older two- and three-n ucleon potentials
than have been used for the other calculations reported in th is review. They repro-
duced the qualitative features of the experimental α+n 1
2
− and 3
2
− phase shifts,
but, in particular, gave a spin-orbit splitting about 1 MeV t oo small. The GFMC
calculations (83) used a diﬀerent, but still somewhat old Ham iltonian and obtained
values that are closer to experiment. These calculations ne ed to be repeated with
the modern Hamiltonians described in this review, and for ot her systems such as
α+d, 6He+n, and α+α.
