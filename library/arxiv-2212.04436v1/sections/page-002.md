---
doc_id: arxiv-2212.04436v1
doc_title: "Dilute neutron star matter from neural-network quantum states"
section_id: page-002
section_title: "Page 2"
section_number: null
pages: 2-2
source_pdf: 2212.04436v1.pdf
source_sha256: 0f98a851d030ec05
toc_source: undetermined
doc_brief: "Dilute neutron star matter from neural-network quantum states — 6 sections: Page 1; Page 2; Page 3"
---
slightly larger than the experimental value of −18.9(4)
fm, see [41] and references therein, while the eﬀective
range is well reproduced. The Hamiltonian also contains
a repulsive three-body force that ensures the stability of
nuclei.
We approximate the ground-state solution of the nu-
clear many-body problem with an NQS ansatz that be-
longs to the hidden-fermion family [42], recently general-
ized to continuum Hilbert spaces and applied to atomic
nuclei in Ref. [29]. In addition to the visible spatial and
spin coordinates of the A neutrons, R = {r1 . . . rA} and
S = {sz
1 . . . sz
A}, the Hilbert space contains ﬁctitious Ah
hidden-nucleon degrees of freedom. In this work we use
Ah = A = 14 so that the system is as ﬂexible as possi-
ble, but in practice we have also found using as few as
8 hidden nucleons gives very similar results. The wave
function can be conveniently expressed in a block matrix
form as
ΨHN(R, S) ≡det
φv(R, S) φv(Rh, Sh)
χh(R, S) χh(Rh, Sh)

.
(1)
As in Ref. [29], φv(R, S) is the A × A matrix represent-
ing visible single-particle orbitals computed on the visible
coordinates while the Ah × Ah matrix χh(Rh, Sh) yields
the amplitudes of hidden orbitals evaluated on the co-
ordinates of the Ah hidden nucleons. Finally, χh(R, S)
and φv(Rh, Sh) are Ah × A and A × Ah matrices giving
the amplitudes of hidden orbitals on visible coordinates
and visible orbitals on hidden coordinates, respectively.
All the above matrices are expressed in terms of deep
neural networks with diﬀerentiable activation functions
— see Ref. [29] for additional details.
To respect the
Pauli principle, the coordinates of the hidden nucleons
must be permutation-invariant functions of the visible
ones. We enforce this symmetry by using a Deep-Sets
architecture [43, 44] with logsumexp pooling.
Inspired by the success of quantum-chemistry NQS [32,
33], we augment the ﬂexibility of the ansatz by perform-
ing a generalized backﬂow transformation to the visible
coordinates entering the upper-left block of the hidden-
nucleon matrix: φv(R, S) →φv( ˜R, ˜S). We use the Deep-
Sets architecture again to enforce fermion anti-symmetry
(˜ri, ˜sz
i ) = ρbf

ri, sz
i , log
 X
j
exp(φbf(rj, sz
j)

.
(2)
To further augment the expressivity, each visible single-
particle orbital uses its own ρbf and φbf neural networks.
We simulate inﬁnite neutron matter using 14 particles
in a box with periodic boundary conditions. Following
Ref. [45], the latter are imposed by mapping the spatial
coordinates onto periodic functions by
ri →

sin
2πri
L

, cos
2πri
L

(3)
which ensures the wave function is continuous and diﬀer-
entiable at the box boundary. Here L is the size of the
simulation periodic box, and the sin and cos functions
are applied element-wise to ri.
Finite-size eﬀects due
to the tail corrections of two- and three-body potentials
are accounted for by summing the contributions given by
neighboring cells to the simulation box [46].
Evaluating the expectation values of quantum mechan-
ical operators, including the Hamiltonian, requires car-
rying out multi-dimensional integration over the spatial
and spin coordinates of the neutrons. To this aim, we
exploit Monte Carlo quadrature and sample R and S
from |ΨHN(R, S)|2 using the Metropolis-Hastings algo-
rithm [47] — additional details can be found in the sup-
plemental material of Ref. [27].
The best variational
parameters deﬁning the NQS are found by minimiz-
ing the system’s energy, which we carry out using the
R(oot)M(ean)S(quared)Prop(agation)-enhanced version
of the stochastic-reconﬁguration optimization method in-
troduced in Ref. [29].
Results and discussion.
We ﬁrst benchmark the ex-
pressivity of the hidden-nucleon NQS for periodic sys-
tems by comparing the energy per particle of inﬁnite
neutron matter against “conventional” variational Monte
Carlo (VMC), and both constrained-path and AFDMC
results. The variational wave function used in state-of-
the-art neutron-matter studies, see for example [7, 21],
contains a spin-independent Jastrow factor that multi-
plies a Slater determinant augmented by spin-dependent
backﬂow correlations.
The constrained-path approxi-
mation, commonly employed to alleviate the AFDMC
fermion-sign problem [19], brings about a bias in the
ground-state energy estimate [6, 21]. Exact results can be
obtained by performing unconstrained propagations, but
the statistical error grows exponentially with the imagi-
nary time.
0
1000
2000
3000
4000
Optimization Steps
6.4
6.5
6.6
6.7
6.8
6.9
7.0
Energy per Particle (MeV)
NQS
DMC (unconstrained)
DMC (constrained)
VMC
Hartree-Fock
FIG. 1. NQS training data in neutron matter at ρ = 0.04
fm−3 (data points) compared with Hartree-Fock (dotted line),
conventional VMC (dashed line), constrained-path ADMC
(dash-dotted line) and unconstrained-path ADMC results
(solid line).
