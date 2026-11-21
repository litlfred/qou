---
doc_id: bq28-r2r7
doc_title: "Classical and Quantum Algorithms for Characters of the Symmetric Group"
section_id: sec-000-i-introduction
section_title: "I.. INTRODUCTION"
section_number: null
pages: 1-3
source_pdf: bq28-r2r7.pdf
source_sha256: 38419a88531ebce7
toc_source: outline
doc_brief: "Classical and Quantum Algorithms for Characters of the Symmetric Group — 12 sections: Front matter; I.. INTRODUCTION; II.. GROUP THEORY REFRESHER"
---
Representation theory provides a powerful set of tools
for analyzing systems invariant under the action of some
group such as a molecular symmetry group in chemistry or
a gauge group in quantum ﬁeld theory. For example, the
eigenvalue spectrum of a quantum system is usually com-
puted by decomposing the Hilbert space into a direct sum
of irreducible representations of the symmetry group and
diagonalizing each irreducible block of the Hamiltonian
separately.
The character of an irreducible representation (irrep) can
be viewed as a ﬁngerprint that uniquely identiﬁes the irrep
and facilitates many computational tasks. In the case of
Abelian groups such as the symmetry group of a periodic
lattice, characters are basis functions of the Fourier trans-
form associated with a given frequency or momentum. In
general, the character of a group element g is deﬁned as
the trace of a matrix describing the action of g for a given
irrep.
*Contact author: dgosset@uwaterloo.ca
Published by the American Physical Society under the terms of
the Creative Commons Attribution 4.0 International license. Fur-
ther distribution of this work must maintain attribution to the
author(s) and the published article’s title, journal citation, and
DOI.
Here we address the problem of computing charac-
ters of the symmetric group Sn, that is, the group of all
possible permutations of n objects. Symmetric groups Sn
with small values of n often emerge as molecular sym-
metries in chemistry. For example, S4 and S5 describe
molecules with tetrahedral and icosahedral symmetries
such as methane and fullerene. Group S6 is isomorphic
to the symplectic group describing the action of two-qubit
Cliﬀord gates commonly used in quantum computation [1].
Moreover, Cayley’s theorem asserts that any ﬁnite group is
isomorphic to a subgroup of Sn [2].
Unfortunately, the irreducible characters of Sn lack a
simple analytic formula. In fact, it was shown [3,4] that
the problem of computing the character of a given permu-
tation g ∈Sn for a given irrep of Sn is #P-hard, that is, at
least as hard as counting the number of solutions of an NP-
hard problem. While this leaves little hope for an eﬃcient
algorithm with runtime scaling polynomially with n, one
may ask how well can we do in practice and whether it
is possible to compute the characters of Sn for moderately
large values of n, say n ≤100.
To motivate this problem, we note that the characters of
Sn with large values of n describe amplitudes of Laughlin
states in the fractional quantum Hall eﬀect [5–8]. Hav-
ing access to the characters of Sn enabled computation of
the electron density and correlation functions of Laughlin
states [5]. Another application is computing integrals of
high-degree polynomials over the unitary group [9]. Such
2691-3399/25/6(3)/030323(15)
Published by the American Physical Society
integrals can be computed using Weingarten functions that
depend on the Sn characters [9]. Algorithms for Sn charac-
ters may also facilitate evaluation of kernel functions for
solving ranking problems in machine learning [10,11].
Our ﬁrst contribution is an algorithm for computing the
characters of Sn based on matrix product states (MPSs).
These are tensor networks commonly used for simulat-
ing ground-state properties of quantum spin chains [12].
A deep connection between the characters of Sn and quan-
tum spin chains was recently established by Crichigno and
Prakash [13]. These authors showed that the characters of
a given permutation g ∈Sn associated with all possible
irreps of Sn can be read oﬀas amplitudes of a certain quan-
tum state |ψg⟩describing 2n fermionic modes. State |ψg⟩
is deﬁned in terms of current operators
Jℓ=
2n−ℓ

i=1
a†
i+ℓai,
where ℓis an integer and the a†
i (ai) are fermionic creation
(annihilation) operators. Speciﬁcally,
|ψg⟩=
c(g)

j =1
Jνj |1n0n⟩,
where c(g) is the number of cycles in g, νj is the length
of the j th cycle, and |1n0n⟩is the Fock basis state with the
ﬁrst n modes occupied and remaining modes empty. The
order in the product does not matter since the current oper-
ators pairwise commute [13]. For each irrep λ of Sn, the
Crichigno and Prakash mapping gives a Fock basis vec-
tor xλ ∈{0, 1}2n such that the amplitude ⟨xλ|ψg⟩coincides
with the character of g associated with λ. Section III pro-
vides a simpliﬁed derivation of the Crichigno and Prakash
mapping. Our derivation may be slightly more accessible
to physicists as it avoids the heavy machinery of non-
commutative symmetric polynomials used in the original
work [13,14]. Instead, we apply an elegant formula derived
by Frobenius in 1900 [15] to express the characters in
terms of fermionic Slater determinants. Rewriting this for-
mula using the fermionic second quantization formalism
reproduces the result of Ref. [13].
The standard Jordan Wigner transformation maps 2n
fermionic modes to 2n qubits. We show that the image of
the current operator Jℓunder this mapping is a matrix prod-
uct operator (MPO) with bond dimension ℓ+ 2. Applying
a sequence of MPOs to an initial product state is a common
subroutine in quantum spin chain simulations and a variety
of highly optimized software libraries for this task is avail-
able such as quimb [16] or mpnum [17]. Our problem is
particularly well suited for MPO-MPS simulation because
the characters of Sn are integer valued. Accordingly, a
small error introduced by truncating singular values in the
intermediate MPS can be tolerated. A detailed description
of our algorithm and numerical experiments can be found
in Sec. IV.
As mentioned above, computing Sn characters is a #P-
hard problem. Thus, neither classical nor quantum algo-
rithms for this problem are expected to run in time poly(n).
The main obstacle for the classical MPS algorithm is a
rapid growth of entanglement that results in an exponen-
tially large MPS bond dimension. A natural question to ask
is whether a quantum computer can eﬃciently prepare state
|ψg⟩. Surprisingly, we show that the answer is yes. To this
end, we construct a quantum circuit of size poly(n) that
prepares the uniform superposition of all permutations in
the conjugacy class of g. We show that applying the quan-
tum Fourier transform (QFT) over Sn to this superposition
gives the desired state |ψg⟩, with a suitable normalization
coeﬃcient. Importantly, the QFT over Sn can be realized
by a quantum circuit of size poly(n), as was shown by
Beals [18].
Using a similar technique, we describe a poly(n)-sized
quantum circuit that, for a given irrep λ of Sn, prepares a
quantum state |ωλ⟩that is a superposition of all permuta-
tions g ∈Sn with amplitudes proportional to the character
of g for irrep λ. By preparing and then measuring either
|ψg⟩or |ωλ⟩, a quantum computer can eﬃciently sample
either irreps or permutations with probability proportional
to the character squared.
Finally, we ask whether or not these sampling problems
admit eﬃcient classical algorithms. To this end, we give
a reduction from weak simulation (sampling with a small
statistical error) to strong simulation (exact computation
of probabilities) for a broad class of sampling problems
that posses a certain granularity structure. Namely, if P is
a probability distribution on some set , we say that P is
granular if || · P(x) is integer for all x ∈. Our weak-to-
strong reduction applies to any granular (or approximately
granular) distribution and does not require the anticoncen-
tration property that is commonly used in reductions from
weak-to-strong simulation [19–21]. Sampling problems
based on characters of Sn are shown to be (approximately)
granular due to the fact that Sn characters are integer val-
ued. Using our reduction, we show that classical hardness
of sampling from the measured distribution of |ψg⟩for
permutations g with O(√n/ log(n)) cycles follows from
a conjecture concerning average-case hardness of comput-
ing the group characters associated with g. Establishing or
refuting this conjecture is left for future work.
Similarly to characters of the symmetric group, we give
an MPS algorithm for Kostka numbers. The ﬁrst step of
mapping Kostka numbers onto quantum spin chains was
shown in Ref. [13]. We give a corresponding MPO con-
struction and code for running this algorithm in the ﬁnal
section of this paper.
Most of the existing classical algorithms for computing
Sn characters use variants of a recursive formula known as
the Murnaghan-Nakayama rule [22,23]. Algorithmic ver-
sions of this formula can be found in, e.g., Refs. [3,24]. An
eﬃcient classical algorithm that computes a small addi-
tive error approximation of Sn characters normalized by
the irrep dimension is described by Jordan [25]. Classical
and quantum algorithms for computing multiplicity coeﬃ-
cients closely related to Sn characters were studied in Refs.
[26,27].
The paper is organized as follows. Section II provides
a necessary background on group representation theory.
Section III gives a simpliﬁed derivation of the Crichigno
and Prakash mapping from characters of Sn to quan-
tum spin chains. Sections IV and V contain our main
results—an MPS algorithm for characters of Sn and a quan-
tum circuit that prepares the corresponding MPS. Sampling
problems for granular probability distributions and reduc-
tions from weak-to-strong simulation are discussed in Sec.
VI. An extension of our MPS algorithm to computing
Kostka numbers is given in Sec. VII.
