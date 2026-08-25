---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-010-322-simple-examples
section_title: "Simple examples"
section_number: 3.2.2
pages: 21-23
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
doc_brief: "Quantum Field Theory and the Volume Conjecture — 14 sections: Preliminaries; The many dimensions of the volume ; Parametrized VC"
---
Let us now adapt the general statements here to some speciﬁc examples.
Harmonic oscillator
The quintessential simplest nontrivial problem of quantization is the harmonic oscil-
lator. Consider a classical system that consists of a particle moving on a line (with
coordinate x = x(t)) with a potential energy V = 1
2x2. This is depicted in Figure 6.
The total (potential + kinetic) energy of the particle at any moment of time is given
by the Hamiltonian
H = 1
2x2 + 1
2p2, (3.22)
where classically p = ˙x = dx
dt is the momentum. This total energy H is conserved. The
classical phase space M is just R2 ={(x,p )}, endowed with a symplectic structure
ω =dp∧dx. A classical trajectory with energy H =E is just a circle of radius
√
2E
in phase space. This deﬁnes a Lagrangian submanifold L(E)≃S1.
Figure 6: The harmonic oscillator: potential V (x) = 1
2x2 in physical space, phase
spaceM, a classical trajectory L(E) in phase space, and the ground state quantum
wavefunctionZ(x).
Now let us quantize the system. Since H2(M; Z) = 0, there is no restriction or
quantization of ℏ−1. On the other hand, there is a restriction on L which quantizes
the energy. Namely, according to (3.11), for a Liouville 1-form θ such thatω =dθ, the
integral ∮
L
θ =
∮
S1
θ = 2πE (3.23)
20
must be an element of 2 πℏ Z, implying that E = nℏ for positive n∈ Z. In fact,
this equation is corrected by quantum eﬀects — a Maslov correction in geometric
quantization — to
E = ℏ
(
n + 1
2
)
. (3.24)
This leads to the famous result that the lowest possible energy of a quantum harmonic
oscillator (at n = 0) is nonzero.
Suppose we choose a polarization ∂/∂p = 0, and a corresponding Liouville 1-form
θ = pdx . The Hilbert space H can simply be identiﬁed as L2(R)∼{ functions of x},
on which the functions x and p act as operators
ˆx :=Ox =x, ˆp :=Op =−iℏ d
dx. (3.25)
In this case, the exact quantum expression for the Hamiltonian is
OH = 1
2(ˆx2 + ˆp2). (3.26)
It is then easy to ﬁnd the quantum wavefunctions corresponding to classical states
L(E). From (3.12), we ﬁnd a leading contribution
Z(x)≃ exp
(i
ℏ
∫ x
0
θ
)
= exp
(i
ℏ
∫ x
0
√
2E−x2dx
)
≃ exp
(
− 1
2ℏx2 +...
)
. (3.27)
Since the LagrangianL(E) is deﬁned classically byH−E = 0, the complete expression
for Z(x) can be obtained by solving the operator equation ( OH−E)Z = 0. This
eigenvalue equation has square-integrable solutions only for the quantized energies
(3.24); for example, at the ground state energy E = ℏ/2, the exact solution is Z(x) =
exp
(
− 1
2ℏx2)
.
Representations of Lie groups
Another famous application of quantization is the construction of unitary representa-
tions of Lie groups by quantization of coadjoint orbits. A basic premise of this approach,
also known as the orbit method, is that coadjoint orbits come equipped with a natu-
ral symplectic structure (the Kostant-Kirillov-Souriau symplectic structure), therefore
providing interesting examples for quantization.
Continuing with our default notations in these notes, we use G for a compact Lie
group (that we usually assume to be simple), GC for its complexiﬁcation, and GR for
some real form of the complex group GC (that may be equal to G). We denote by
gR the Lie algebra of GR, and similarly for G and GC. Given an element λ∈ g∗
R (the
highest weight of the desired unitary representation Rλ) one constructsM =GR·λ as
the coadjoint orbit of GR in g∗
R passing through λ.
In the case of compact groups, the phase space M is compact and its quantization
leads to a ﬁnite-dimensional Hilbert spaceH as the space of the unitary representation
21
Rλ. This is the statement of the Borel-Bott-Weil theorem. Moreover, the condition
1
2πℏω∈ H2(M; Z) that ensures the existence of a prequantum line bundle becomes
equivalent to the condition that λ be an element of the weight lattice Λ w⊂ g∗.
As a very simple illustration, consider the group SU (2). In this case, a non-trivial
coadjoint orbit is topologically equivalent to the ﬂag manifold
SU (2)/U(1)≃ P1. (3.28)
Letting ω be the unit volume form on P1, we see that (M,ω ) is quantizable for
ℏ−1 = 2πλ, λ ∈ Z(+). (3.29)
The prequantum line bundle with curvature ℏ−1ω is simplyO(λ)→ P1. Choosing a
holomorphic polarization, so that H is deﬁned as the space of holomorphic sections
ofO(λ), we see that dim H = λ + 1. The Hilbert space is precisely the space of the
(λ + 1)-dimensional representation of SU (2).
Similarly, some inﬁnite-dimensional representations, such as unitary principal series
representations of SL(n, C) or SL(n, R), can be described as quantized orbits. Nev-
ertheless, there remain some outstanding puzzles: there exist unitary representations
that don’t appear to correspond to orbits, and, conversely, there are real orbits that
don’t seem to correspond to unitary representations. An example of ﬁrst kind occurs
even in the basic case of the real group GR =SL(2, R) and the complementary series
representations. To illustrate the second phenomenon, one can take GR to be a real
group of Cartan type BN, i.e. GR =SO(p,q ) with p +q = 2N + 1. The minimal orbit
Omin of BN is a nice symplectic manifold of (real) dimension 4 N− 4, for any values
of p and q. On the other hand, the minimal representation of SO(p,q ) exists only if
p≤ 3 or q≤ 3 [37]. Both of these issues can be resolved in the brane quantization
approach [34], at the cost of replacing classical geometric objects (namely, coadjoint
orbits) with their quantum or “stringy” analogs (branes). In particular, in the case
of BN one ﬁnds that, while the minimal orbit exists for any values of p and q, the
corresponding brane exists only if p≤ 3 or q≤ 3. (In general, the condition is that
the second Stieﬀel-Whitney class w2(M)∈H2(M; Z2) must be a mod 2 reduction of
a torsion class in the integral cohomology of M.)
