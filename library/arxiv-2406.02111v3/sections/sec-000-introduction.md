---
doc_id: arxiv-2406.02111v3
doc_title: "Categorical Quantum Volume Operator"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-2
source_pdf: 2406.02111v3.pdf
source_sha256: d7be0c3f08b4d42a
doc_brief: "Categorical Quantum Volume Operator — 10 sections: Introduction; Quantum tetrahedron; Volume operator"
---
II. The V olume Operator in Loop Quantum Gravity 3
II.1. Spin networks and graph states 3
II.2. Quantum tetrahedron 3
II.3. V olume operator 4
II.4. Chakrabarti’s derivation of the volume
operator 5
III. Categorification of the V olume Operator 5
III.1. String diagrams 5
III.2. Derivation of the categorical volume operator 6
III.3. Beyond ribbon fusion categories 9
III.4. Hermiticity of the categorical volume operator 11
IV . Recovering the StandardSU(2) V olume Operator 12
V . Spectrum of theSU(2)k V olume Operator 13
VI. Discussion and Conclusions 14
References 15
Appendix: Basic Concepts in Category Theory 16
I. INTRODUCTION
In the search for an all-encompassing theory of quan-
tum gravity that successfully reconciles general relativity and
quantum field theory, background-independent theories such
as loop quantum gravity (LQG) [1–3] and causal dynamical
∗ alexander.hahn@students.mq.edu.au
† sebastian.murk@oist.jp
‡ qsukhi@gmail.com
§ gavin.brennen@mq.edu.au
triangulations [4, 5] are widely regarded as the main con-
tenders to string theory/M-theory. Arguably the most salient
property of background-independent theories is the prediction
of a granular structure of space in which lengths, areas, and
volumes are fundamentally discrete [6–12]. In the context of
LQG, the discrete structure of spacetime has been instrumen-
tal in derivations of thermodynamic properties of black holes
with possible observational consequences [13–16]. It has also
been proposed that a granular quantum spacetime might have
observable imprints on the power spectrum of the cosmic mi-
crowave background radiation [17, 18].
Due to the absence of a fixed background spacetime struc-
ture, states in background-independent theories are described
by graphs, i.e. a collection of nodes (also referred to as “ver-
tices”) that are connected by weighted and in general directed
links (also referred to as “edges”).1 The dual of the graph has
a geometric interpretation according to which each v-valent
node (i.e. a node with v links attached to it) is associated with
a v-polyhedron representing an elementary building block of
the quantum spacetime geometry. Matter fields can only ex-
ist where this quantum geometry is excited, namely on the
nodes (corresponding to fermionic degrees of freedom) and
on the links (corresponding to bosonic degrees of freedom).
Four-valent graphs whose duals are described by tetrahedra
play a special role: as the smallest polyhedron with a nonzero
volume they allow us to model the simplest physically rele-
vant settings. The quantum volume operator is a fundamental
observable in LQG. It was initially introduced for quantum
spacetime states described by graphs whose edges carry rep-
resentations of the group SU(2) and whose vertices carry lin-
ear maps that intertwine the representations on the incident
edges. Our aim in this article is to generalize the notion of the
quantum volume operator to a large class of fusion categories
beyond the representation category of SU(2).
The “categorification” of spin models has generated signif-
icant activity recently within the condensed matter and quan-
tum information communities. The Levin–Wen string net
1 In this article, we describe graphs using the language of string diagrams,
see Sec. III.1.
arXiv:2406.02111v3  [gr-qc]  29 Aug 2024
2
model [19] is a prime example where a Hamiltonian constraint
on a lattice with quantum degrees of freedom on the edges —
described by objects of a category C — is constructed such
that the ground states exhibit topological order through the
mechanism of string net condensation. It was shown [20]
that the string net space for a category C is equal to the state
space of the 3D Turaev–Viro topological quantum field the-
ory (TQFT) forC, or a 4D TQFT in the case of Walker–Wang
models [21]. A microscopic construction of the Hamiltonian
for general unitary fusion categories is given in Refs. [22, 23]
and has been further generalized to pivotal fusion categories
in Ref. [24].
The string net model was motivated by categorifying lat-
tice gauge theory where the gauge degrees of freedom located
on the edges — usually labeled by irreducible representations
of a (gauge) group — are supplanted by objects in a more
general category. Other well-known examples of categori-
fication are anyonic spin chains [25], which generalize the
quantum Heisenberg spin chain to anyonic degrees of free-
dom, such as the Golden Chain model of Fibonacci Anyons
(objects of the category SU (2)3). (Unlike String-net mod-
els which categorify gauge degrees of freedom, anyonic spin
chains are obtained by categorifying the physical degrees of
freedoms, namely, the lattice of spin 1/2s in the Heisenberg
model.) Similar and more general anyonic lattice models have
since been shown to realize rich phase diagrams, see e.g.,
Refs. [26, 27].
Motivated by these developments, one could ask whether
the volume operator — originally derived with isotropy of
space in mind using irreducible representations from the
group SU(2) — could be generalized using objects from a
category. Indeed, categorical extensions of loop quantum
gravity are implied by the presence of a cosmological con-
stant [28]. For 3D spacetime, one can write general rela-
tivity as a Chern–Simons gauge theory (see e.g. [3]). The
spin-foam approach to 3D gravity is obtained from combina-
torial optimization of Chern–Simons theory with the quantum
groupD(Uq(su(2))), the Drinfeld double ofUq(su(2)) which
is theq-deformation of the gauge group SU(2). In a 3D met-
ric with Euclidean signature and with a positive cosmological
constant Λ, the deformation parameter for the Chern–Simons
theory isq = eiℓp/R, whereℓp denotes the Planck length and
R−1 =
√
Λ the cosmological radius. The irreducible repre-
sentations ofD(Uq(su(2))), also known as objects from the
categoryC = SU(2) k, are non-negative half-integers with
an upper bound k/2 where the deformation is related to k by
q = ei 2π
k+2 .
Earlier work [29, 30] computed a quantum volume for triva-
lent spin networks labeled by the objects inSU(2)k. However,
such graphs have zero volume in the undeformedk→∞ limit
and therefore do not correspond to the usual notion of volume
in the classical limit with a classical symmetry group and la-
bels with large spins. More recently, Livine showed [31] how
to compute the action of the volume operator on an elementary
tetrahedron in a Ponzano–Regge state sum model of 3D grav-
ity. In that formulation, introduced in [32], one defines the
partition function from the action for a 2+1 dimensional BF
theory with a cosmological term, where the three-dimensional
manifold is triangulated by tetrahedra whose edges are labeled
by objects from SU(2)k. The volume is computed by taking
the derivative of the log of the Tureav-Viro transition ampli-
tude, i.e. the partition function of the BF theory with a factor
of i in the action, with respect to−iΛ, and then settingΛ→ 0.
It is important to note that Regge geometry is not the same as
spin-network geometry since in the latter the shapes of faces
of glued polyhedra do not have to match [33].
The main reason for the interest in categorical formulations
and extensions of LQG is to circumvent the infrared diver-
gences that appear using SU(2) with an infinite number of
irreducible representations [34]. Additionally, other authors
have recently pursued a categorical description of LQG for
various reasons. Dittrich and Geiller [35] formulated a cate-
gorical description of the LQG kinematics, which clarifies the
discreteness and finiteness of several quantum geometric op-
erators [35]. However, they derive a categorical area operator,
but not a volume operator. In a related work, Ref. [36], Dit-
trich speculates about defining grasping operators based on
fusion category F -moves to define a categorical volume op-
erator, which is closely related to the approach that we have
developed in the present paper. Also, Ref. [37] shows how
the categorical description of the kinematical Hilbert space for
LQG provides a simple explanation of large-scale Gauß con-
straint violations, which is not apparent in the standard spin-
network picture.
In this work, we compute the volume operator for an ele-
mentary four-valent node of a spin-network state, which has a
