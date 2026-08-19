---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Bonn, November 2018"
section_id: sec-044-bosons-in-one-dimension
section_title: "Bosons in one dimension"
section_number: null
pages: 76-78
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-Body Systems in Lattice Effective Field Theory Dissertation Erlangung des Doktorgrades (Dr. rer. nat.) Mathematisch-Naturwissenschaftlichen Fakultät Rheinischen Friedrich-Wilhelms-Universität Bonn"
---
We consider a one-dimensional system of bosons with attractive zero-range interactions [62]. The
Hamiltonian is given by
H =− 1
2m
N∑
i=1
d2
dx2
i
+ C0
N∑
i> j=1
δ(xi− x j), (6.2)
where m is the boson mass, N is the number of particles and C0 < 0 is the two-boson contact interaction
coeﬃcient. From either the Bethe ansatz [155] or by direct inspection, the ground state of this Hamiltonian
is a bound state with energy
ENb
B =− m
24C2
0N(N2− 1), (6.3)
and wave function
ΨN
(x1, x2,..., xN
) =N exp
[ mC0
2
(⏐⏐⏐x1− x2
⏐⏐⏐ +
⏐⏐⏐x1− x3
⏐⏐⏐ +...
)]
, (6.4)
with normalization constantN [62]. We note that no regularization or renormalization is needed, and all
quantities are ﬁnite.
Here, we consider several di ﬀerent bound state and scattering observables. We will consider the
binding energies of the N-boson bound state for up to ﬁve bosons and the root-mean-square radii of their
corresponding wave functions. The root-mean-square radii for all the particle positions will be the same
due to Bose symmetry and can be calculated as
r2
rms =
∫
dx1··· dxN
⏐⏐⏐⏐⏐x1− x1 +··· + xN
N
⏐⏐⏐⏐⏐
2 ⏐⏐⏐ΨN
(x1, x2,..., xN
)⏐⏐⏐2
. (6.5)
For the scattering observables, we compute coeﬃcients of the eﬀective range expansion for the boson-
boson and dimer-boson even-parity scattering phase shifts, which we denote asδ2 andδ3, respectively.
We use the conventions
p tanδ2 = 1
a2
+ r2
2 p2 +... , (6.6)
p tanδ3 = 1
a3
+ r3
2 p2 +..., (6.7)
where ai is the scattering length, ri is the eﬀective range, and p is the relative momentum. From the
70
6.2 Bosons in one dimension
1
2
1′
2′
Figure 6.1: One-loop diagramI2 involving two bosons in the initial and the ﬁnal state.
Bethe ansatz, these eﬀective range functions are known exactly [156],
p tanδ2 =
√
−mE2b
B , (6.8)
p tanδ3 =−4 a2 p2
3
2 a2
2 p2− 2
, (6.9)
where E2b
B is the two-boson bound state energy and a2 =−2/(mC0) is the two-boson scattering length.
When implemented on a spatial lattice, this theory will be modiﬁed by the lattice momentum cutoﬀ scale
Λ =π/a. In order to study the size of the lattice errors, we must know the dependence of the Green’s
functions upon the cutoﬀ momentum. For this analysis we use perturbation theory and determine the
cutoﬀ dependence of individual Feynman diagrams. In some cases there can be non-perturbative eﬀects
that arise from correlations that modify the ultraviolet properties of the Green’s functions. However,
perturbation theory is still a good starting point, and the cutoﬀ error estimates can then be veriﬁed by
numerical calculations. For our one-dimensional system of bosons, all diagrams are ultraviolet ﬁnite and
so all of the cutoﬀ eﬀects will be of residual dependences that vanish in the continuum limit.⋆
The Feynman diagram with the highest degree of divergence (albeit negative) is the one-loop diagram
I2 involving two bosons as shown in Fig. 6.1. Let the energies and momenta of the incoming particles be
(E1, p1) and (E2, p2), and the energies and momenta of the outgoing particles be (E′
1, p′
1) and (E′
2, p′
2).
We write ∆I2 for the diﬀerence between the continuum-limit amplitudes and the lattice amplitudes at
lattice spacing a. We expand in powers of momenta and energies and get
∆I2 = A2(a) + (p1 + p2)2B2(a) + m(E1 + E2)C2(a) +O(p4), (6.10)
whereO(p4) is shorthand for terms with more powers of momentum or energy. From dimensional
analysis we ﬁnd that A2(a)∼O (a1), while B2(a)∼O (a3) and C2(a)∼O (a3). All even expansion terms
vanish in the integral calculation, and thus terms with higher powers of momentum or energy start at
O(a5). The dependence on the total momentum, p1 + p2, is a result of the fact that the lattice regulator
breaks Galilean invariance and so the residual amplitude ∆I2 can depend on the frame of reference.
The diagram with the next highest degree of divergence is the one-loop diagramI3 involving three
bosons as shown in Fig. 6.2. Let the energies and momenta of the incoming particles be(E1, p1), (E2, p2),
(E3, p3) and the energies and momenta of the outgoing particles be(E′
1, p′
1), (E′
2, p′
2), (E′
3, p′
3). We let ∆I3
be the diﬀerence between the continuum-limit and lattice amplitudes. Expanding in powers of momenta
and energies gives
∆I3 = A3(a) +O(p2). (6.11)
From dimensional analysis we conclude that A3(a) ∼ O(a3) and the terms with higher powers of
momentum or energy start atO(a5). Our analysis thus far might give the false impression that all other
⋆ The case of non-perturbative regularization in the two-body sector is given in App. E.
71
Chapter 6 Lattice Improvement in Lattice E ﬀective Field Theory
1
2
1′
2′
3 3′
Figure 6.2: One-loop diagramI3 involving three bosons in the initial and the ﬁnal state.
1
2
1′
2′
3
Figure 6.3: One-loop form factor diagramI′
2 involving two bosons in the initial and the ﬁnal state and one external
insertion.
errors start atO(a5). However, we should note that there are two-loop diagrams involving three bosons
that give a cutoﬀ dependence that isO(a4). Furthermore, there will be O(a4) errors in the two-boson
system when we iterate the improved energy-independent interactions that we use to cancel theO(a1)
andO(a3) errors. We give further details for the expressions appearing in Eq. (6.10) and Eq. (6.11) in the
Appendix D.
Since we are computing the root-mean-square radius, we also need to consider form factor diagrams
associated with the boson density. The form factor diagram with the highest degree of divergence is the
one-loop diagramI′
2 shown in Fig. 6.3. Structurally this diagram is the same asI3, and so the residual
amplitude will have a similar form,
∆I′
2 = A′
2(a) +O(p2). (6.12)
From dimensional analysis A′
2(a) will beO(a3). In this case, however, the momentum-independent part
of the form factor just counts the number of bosons. So A′
2(a) will vanish if number conservation is
properly implemented on the lattice, and we assume this is the case. The root-mean-square radius is
proportional to the derivative of the form factor with respect to the squared momentum transfer, and so
the correction to the root-mean-square radius from this diagram will beO(a5).
