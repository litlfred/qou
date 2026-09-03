---
doc_id: bq28-r2r7
doc_title: "Classical and Quantum Algorithms for Characters of the Symmetric Group"
section_id: sec-000-full-text
section_title: "Full text"
section_number: None
pages: 1-15
source_pdf: bq28-r2r7.pdf
source_sha256: 38419a88531ebce7
doc_brief: "Classical and Quantum Algorithms for Characters of the Symmetric Group — 1 sections: Full text"
---
PRX QUANTUM 6, 030323 (2025)

Classical and Quantum Algorithms for Characters of the Symmetric Group
Sergey Bravyi,1 David Gosset,2,3,* Vojtech Havlicek ,1 and Louis Schatzki

4

1

2

IBM Quantum, IBM T.J. Watson Research Center, Yorktown Heights, New York 10598, USA
Department of Combinatorics and Optimization and Institute for Quantum Computing, University of Waterloo
3
Perimeter Institute for Theoretical Physics
4
University of Illinois Urbana Champaign, Urbana, Illinois 61801, USA
(Received 20 March 2025; accepted 25 June 2025; published 7 August 2025)
Characters of irreducible representations are ubiquitous in group theory. However, computing characters of some groups such as the symmetric group Sn is a challenging problem known to be #P-hard in the
worst case. Here we describe a matrix product state (MPS) algorithm for characters of Sn . The algorithm
computes an MPS encoding all irreducible characters of a given permutation. It relies on a mapping from
characters of Sn to quantum spin chains proposed by Crichigno and Prakash. We also provide a simpler
derivation of this mapping. We complement this result by presenting a poly(n) size quantum circuit that
prepares the corresponding MPS obtaining an eﬃcient quantum algorithm for certain sampling problems
based on characters of Sn . To assess classical hardness of these problems, we present a general reduction from strong simulation (computing a given probability) to weak simulation (sampling with a small
error). This reduction applies to any sampling problem with a certain granularity structure and may be of
independent interest.
DOI: 10.1103/bq28-r2r7

I. INTRODUCTION
Representation theory provides a powerful set of tools
for analyzing systems invariant under the action of some
group such as a molecular symmetry group in chemistry or
a gauge group in quantum ﬁeld theory. For example, the
eigenvalue spectrum of a quantum system is usually computed by decomposing the Hilbert space into a direct sum
of irreducible representations of the symmetry group and
diagonalizing each irreducible block of the Hamiltonian
separately.
The character of an irreducible representation (irrep) can
be viewed as a ﬁngerprint that uniquely identiﬁes the irrep
and facilitates many computational tasks. In the case of
Abelian groups such as the symmetry group of a periodic
lattice, characters are basis functions of the Fourier transform associated with a given frequency or momentum. In
general, the character of a group element g is deﬁned as
the trace of a matrix describing the action of g for a given
irrep.

*

Contact author: dgosset@uwaterloo.ca

Published by the American Physical Society under the terms of
the Creative Commons Attribution 4.0 International license. Further distribution of this work must maintain attribution to the
author(s) and the published article’s title, journal citation, and
DOI.

2691-3399/25/6(3)/030323(15)

Here we address the problem of computing characters of the symmetric group Sn , that is, the group of all
possible permutations of n objects. Symmetric groups Sn
with small values of n often emerge as molecular symmetries in chemistry. For example, S4 and S5 describe
molecules with tetrahedral and icosahedral symmetries
such as methane and fullerene. Group S6 is isomorphic
to the symplectic group describing the action of two-qubit
Cliﬀord gates commonly used in quantum computation [1].
Moreover, Cayley’s theorem asserts that any ﬁnite group is
isomorphic to a subgroup of Sn [2].
Unfortunately, the irreducible characters of Sn lack a
simple analytic formula. In fact, it was shown [3,4] that
the problem of computing the character of a given permutation g ∈ Sn for a given irrep of Sn is #P-hard, that is, at
least as hard as counting the number of solutions of an NPhard problem. While this leaves little hope for an eﬃcient
algorithm with runtime scaling polynomially with n, one
may ask how well can we do in practice and whether it
is possible to compute the characters of Sn for moderately
large values of n, say n ≤ 100.
To motivate this problem, we note that the characters of
Sn with large values of n describe amplitudes of Laughlin
states in the fractional quantum Hall eﬀect [5–8]. Having access to the characters of Sn enabled computation of
the electron density and correlation functions of Laughlin
states [5]. Another application is computing integrals of
high-degree polynomials over the unitary group [9]. Such

030323-1

Published by the American Physical Society


SERGEY BRAVYI et al.

PRX QUANTUM 6, 030323 (2025)

integrals can be computed using Weingarten functions that
depend on the Sn characters [9]. Algorithms for Sn characters may also facilitate evaluation of kernel functions for
solving ranking problems in machine learning [10,11].
Our ﬁrst contribution is an algorithm for computing the
characters of Sn based on matrix product states (MPSs).
These are tensor networks commonly used for simulating ground-state properties of quantum spin chains [12].
A deep connection between the characters of Sn and quantum spin chains was recently established by Crichigno and
Prakash [13]. These authors showed that the characters of
a given permutation g ∈ Sn associated with all possible
irreps of Sn can be read oﬀ as amplitudes of a certain quantum state |ψg  describing 2n fermionic modes. State |ψg 
is deﬁned in terms of current operators
J =

2n−


†

ai+ ai ,

i=1
†

where  is an integer and the ai (ai ) are fermionic creation
(annihilation) operators. Speciﬁcally,
|ψg  =

c(g)


Jνj |1n 0n ,

j =1

where c(g) is the number of cycles in g, νj is the length
of the j th cycle, and |1n 0n  is the Fock basis state with the
ﬁrst n modes occupied and remaining modes empty. The
order in the product does not matter since the current operators pairwise commute [13]. For each irrep λ of Sn , the
Crichigno and Prakash mapping gives a Fock basis vector xλ ∈ {0, 1}2n such that the amplitude xλ |ψg  coincides
with the character of g associated with λ. Section III provides a simpliﬁed derivation of the Crichigno and Prakash
mapping. Our derivation may be slightly more accessible
to physicists as it avoids the heavy machinery of noncommutative symmetric polynomials used in the original
work [13,14]. Instead, we apply an elegant formula derived
by Frobenius in 1900 [15] to express the characters in
terms of fermionic Slater determinants. Rewriting this formula using the fermionic second quantization formalism
reproduces the result of Ref. [13].
The standard Jordan Wigner transformation maps 2n
fermionic modes to 2n qubits. We show that the image of
the current operator J under this mapping is a matrix product operator (MPO) with bond dimension  + 2. Applying
a sequence of MPOs to an initial product state is a common
subroutine in quantum spin chain simulations and a variety
of highly optimized software libraries for this task is available such as quimb [16] or mpnum [17]. Our problem is
particularly well suited for MPO-MPS simulation because
the characters of Sn are integer valued. Accordingly, a
small error introduced by truncating singular values in the

intermediate MPS can be tolerated. A detailed description
of our algorithm and numerical experiments can be found
in Sec. IV.
As mentioned above, computing Sn characters is a #Phard problem. Thus, neither classical nor quantum algorithms for this problem are expected to run in time poly(n).
The main obstacle for the classical MPS algorithm is a
rapid growth of entanglement that results in an exponentially large MPS bond dimension. A natural question to ask
is whether a quantum computer can eﬃciently prepare state
|ψg . Surprisingly, we show that the answer is yes. To this
end, we construct a quantum circuit of size poly(n) that
prepares the uniform superposition of all permutations in
the conjugacy class of g. We show that applying the quantum Fourier transform (QFT) over Sn to this superposition
gives the desired state |ψg , with a suitable normalization
coeﬃcient. Importantly, the QFT over Sn can be realized
by a quantum circuit of size poly(n), as was shown by
Beals [18].
Using a similar technique, we describe a poly(n)-sized
quantum circuit that, for a given irrep λ of Sn , prepares a
quantum state |ωλ  that is a superposition of all permutations g ∈ Sn with amplitudes proportional to the character
of g for irrep λ. By preparing and then measuring either
|ψg  or |ωλ , a quantum computer can eﬃciently sample
either irreps or permutations with probability proportional
to the character squared.
Finally, we ask whether or not these sampling problems
admit eﬃcient classical algorithms. To this end, we give
a reduction from weak simulation (sampling with a small
statistical error) to strong simulation (exact computation
of probabilities) for a broad class of sampling problems
that posses a certain granularity structure. Namely, if P is
a probability distribution on some set , we say that P is
granular if || · P(x) is integer for all x ∈ . Our weak-tostrong reduction applies to any granular (or approximately
granular) distribution and does not require the anticoncentration property that is commonly used in reductions from
weak-to-strong simulation [19–21]. Sampling problems
based on characters of Sn are shown to be (approximately)
granular due to the fact that Sn characters are integer valued. Using our reduction, we show that classical hardness
of sampling from the measured
distribution of |ψg  for
√
permutations g with O( n/ log(n)) cycles follows from
a conjecture concerning average-case hardness of computing the group characters associated with g. Establishing or
refuting this conjecture is left for future work.
Similarly to characters of the symmetric group, we give
an MPS algorithm for Kostka numbers. The ﬁrst step of
mapping Kostka numbers onto quantum spin chains was
shown in Ref. [13]. We give a corresponding MPO construction and code for running this algorithm in the ﬁnal
section of this paper.
Most of the existing classical algorithms for computing
Sn characters use variants of a recursive formula known as

030323-2


CLASSICAL AND QUANTUM ALGORITHMS. . .

PRX QUANTUM 6, 030323 (2025)

the Murnaghan-Nakayama rule [22,23]. Algorithmic versions of this formula can be found in, e.g., Refs. [3,24]. An
eﬃcient classical algorithm that computes a small additive error approximation of Sn characters normalized by
the irrep dimension is described by Jordan [25]. Classical
and quantum algorithms for computing multiplicity coeﬃcients closely related to Sn characters were studied in Refs.
[26,27].
The paper is organized as follows. Section II provides
a necessary background on group representation theory.
Section III gives a simpliﬁed derivation of the Crichigno
and Prakash mapping from characters of Sn to quantum spin chains. Sections IV and V contain our main
results—an MPS algorithm for characters of Sn and a quantum circuit that prepares the corresponding MPS. Sampling
problems for granular probability distributions and reductions from weak-to-strong simulation are discussed in Sec.
VI. An extension of our MPS algorithm to computing
Kostka numbers is given in Sec. VII.

partition λ = (n) with a single part labels the trivial representation, while a partition λ = (1, 1, . . . , 1) with n parts
labels the sign representation. The general recipe for constructing the unitary action ρλ for a given partition λ can
be found in Ref. [28]. The explicit forms of matrices ρλ (g)
are irrelevant for our purposes since we are only interested
in the characters χλ (g) = Tr(ρλ (g)).
III. BUILDING THE CHARACTER
We begin by reproducing the result of Crichigno and
Prakash [13] that shows how to build a quantum spin
chain encoding all characters χλ (g) of a given permutation
g ∈ Sn .
Let λ = (λ1 , . . . , λm ) and ν = (ν1 , . . . , νc(g) ) be the partitions of n describing the irrep λ and the conjugacy class
of g. Consider a complex vector z ∈ Cm and a polynomial
c(g)  m

 νj 
zk .
Pν (z) =
j =1

(1)

k=1

II. GROUP THEORY REFRESHER
Suppose that G is a ﬁnite group. A d-dimensional representation of G is a group homomorphism from G to
the unitary group U(d). A representation is irreducible if
the ambient Hilbert space Cd contains no proper subspace
invariant under the action of all group elements. It is standard to identify irreps that diﬀer only by a basis change
in the ambient Hilbert space. Then any ﬁnite group has a
ﬁnite set of irreps. Given a group element g ∈ G and an
irrep λ, let ρλ (g) be the unitary matrix corresponding to g.
The character of g associated with an irrep λ is deﬁned as
a complex number χλ (g) = Tr[ρλ (g)]. The fact that ρλ is
a group homomorphism implies that χλ (g) depends only
on the conjugacy class of g, that is, χλ (g) = χλ (hgh−1 ) for
all g, h ∈ G. Organizing all characters into a matrix with
rows labeled by irreps and columns labeled by conjugacy
classes of G gives the character table of G.
The symmetric group Sn is the group of permutations of
n objects, say integers [n] = {1, 2, . . . , n}. Irreps and conjugacy classes of Sn are labeled by partitions of n, that is,
sorted sequences of positive integers
 λ = (λ1 , λ2 , . . . , λm )
such that λ1 ≥ λ2 ≥ · · · ≥ λm and m
j =1 λj = n. Here m is
the number of parts in λ. We write λ  n to indicate that λ
is a partition of n. A permutation g ∈ Sn is said to be a cycle
of length  if there exists a subset J ⊆ [n] such that |J | = 
and g cyclically shifts elements of J while acting trivially
on [n] \ J . Any permutation g ∈ Sn can be uniquely written
as a composition of cycles with pairwise disjoint supports.
Denoting the number of cycles by c(g) and the length of
the j th longest cycle by νj one obtains a partition of n with
c(g) parts, namely, ν = (ν1 , ν2 , . . . , νc(g) ). The partition ν
speciﬁes the conjugacy class of Sn that contains g. Irreps
of Sn are also labeled by partitions of n. For example, a

The Frobenius character formula [15] (see, e.g., Theorem
4.47 of Ref. [28]) states that χλ (g) coincides with the
coeﬃcient of a monomial
z(λ) =

m

λ +m−j
zj j

(2)

j =1

in the polynomial


Q(z) = Pν (z)

(zi − zj ).

(3)

1≤i<j ≤m

Let S1 = {x ∈ C : |x| = 1} be the unit circle in the complex
plane, and let F1 be a Hilbert space of functions f : S1 →
C with inner product
1
f |g =
2π

 2π

dθ f (eiθ )∗ g(eiθ )

0

and an orthonormal basis of functions {f (x) = xk }k∈Z .
Informally, F1 describes a particle moving on the circle and f (x) = xk is a state with angular momentum
k. Consider now a many-body system composed of m
indistinguishable particles moving on the circle that obey
fermionic statistics. The fermionic ﬁrst quantization principle stipulates that the m-particle Hilbert space Fm is the
antisymmetric subspace of F1⊗m and its orthonormal basis
is formed by Slater determinants composed of m distinct
single-particle basis functions. Such Slater determinants

030323-3


SERGEY BRAVYI et al.

PRX QUANTUM 6, 030323 (2025)

√
have the form |κ = Dκ (z)/ m!, where
⎡ κ1
z1
⎢z κ1
⎢2
Dκ (z) = det ⎢
⎢ ..
⎣ .
κ
zm1

κ

z1 2
κ
z2 2
..
.
κ2
zm

···
···
···

⎤
z1κm
z2κm ⎥
⎥
.. ⎥
⎥,
. ⎦
zmκm

and κ runs over strictly decreasing integer sequences of
length m that represent momenta of the occupied singleparticle states. The Vandermonde determinant formula
gives


(zi − zj ) =

√
m! |τ ,

(4)

1≤i<j ≤m

Given a ﬁnite strictly decreasing integer sequence κ,
κ. The Slater
let xκ ∈ {0, 1}Z be a bit string with support
√
determinant basis state |κ = Dκ (z)/ m! in the ﬁrst quantization is represented by state |xκ  ∈ H in the second
quantization.
of a wave function by the polynomial
Multiplication
m

z
in
the
ﬁrst
quantization picture shifts the momenj =1 j
tum of each particle by . Such a shift is described by an
operator
 †
J =
ak+ ak
(8)
k∈Z

in the second quantization picture. Following Ref. [13],
we refer to J as the current operator. Now the Frobenius
character formula can be expressed as

where

χλ (g) = xλ+τ |

τ = (m − 1, m − 2, . . . , 1, 0).
Let Pν : Fm → Fm be a linear operator that maps a function (z) ∈ Fm to Pν (z)(z). Note that Pν preserves Fm
since Pν (z) is a symmetric polynomial. We conclude that
polynomial Q(z) deﬁned in Eq. (3) describes a fermionic
m-particle (unnormalized) state
|Q =

√
m! Pν |τ .

(5)

The coeﬃcient of the monomial z(λ) in Q(z) coincides
with Dλ+τ |Q/m!, where

χλ (g) = Dλ+τ |Q/m! = λ + τ |Pν |τ .

(6)

The next step is to rewrite Eq. (6) using the fermionic
second quantization formalism. To this end, consider an
inﬁnite chain of qubits labeled by integers k ∈ Z. Let
Xk , Yk , Zk be the Pauli operators acting on the kth qubit.
Deﬁne a fermionic annihilation operator
ak =


1
Zj ,
(Xk + iYk )
2
j <k

(9)

The order in the product does not matter since the current operators pairwise commute. At this point we have
mapped Sn characters to an inﬁnite spin chain. We can truncate the chain to a block of 2n consecutive qubits using the
following lemma.
Lemma 1. Suppose that x, y ∈ {0, 1}Z are bit strings and
that i∗ is an integer such that xi = yi for i ≤ i∗ . Let x , y
be bit strings obtained from x, y, respectively, by setting to
zero all bits i ≤ i∗ . Then
y|

c(g)


Jνj |x = y |

j =1

c(g)


Jνj |x .

(10)

j =1


†
Proof. Let J̃ = k>i∗ ak+ ak . One can easily check
that
c(g)
c(g)


Jνj |x =
J̃νj |x + |φ,
j =1

j =1

where |φ ∈ H is a superposition of basis vectors |z such
that zi = 0 and xi = 1 for at least one qubit i ≤ i∗ (in the
case that no sites i ≤ i∗ are occupied, |φ is 0). By assumption, xi = yi for all i ≤ i∗ . Thus, |φ is orthogonal to |y,
that is,

(7)
y|

c(g)


Jνj |x = y|

j =1

†

and let ak be the corresponding creation operator. Here
we used the Jordan-Wigner fermion-to-qubit mapping. The
†
operators ak , ak obey the Fermi-Dirac commutation rules,
†
†
that is, ai aj = −aj ai and ai aj + aj ai = δi,j I for all i, j . Let
H be the Hilbert space of the chain. It has basis vectors |x,
where x ∈ {0, 1}Z is a bit string with a ﬁnite support.

Jνj |xτ .

j =1

λ + τ = (λ1 + τ1 , . . . , λm + τm ).
Indeed, Q(z) is antisymmetric under the exchange of any
pair of variables, while Dλ+τ (z)/m! is the antisymmetrized
version of the monomial z(λ) deﬁned in Eq. (2). Thus, the
Frobenius character formula can be expressed as

c(g)


c(g)


J̃νj |x.

(11)

j =1

Since J̃νj acts trivially on qubits i ≤ i∗ , we also have

030323-4

y|

c(g)

j =1

J̃νj |x = y |

c(g)

j =1

J̃νj |x .

(12)


CLASSICAL AND QUANTUM ALGORITHMS. . .

PRX QUANTUM 6, 030323 (2025)

Applying Eq. (11) again with x , y instead of x, y proves
Eq. (10).


Also, we have

n

j =1 dj = m(x), that is,

n


As a consequence of Lemma 1, the matrix element in
Eq. (9) does not change if we set m = n and pad λ with
n − m zeros on the right. Accordingly, we can set
τ = (n − 1, n − 2, . . . , 1, 0).
It is immediate that any qubit i < 0 or i ≥ 2n is set
c(g)
to |0 in the initial state |xτ . Note that j =1 Jνj can
only move a fermion at most n sites to the right. Thus,
qubits i < 0 and i ≥ 2n are unchanged in the simulation
and can be removed. This leaves only 2n active qubits
i = 0, 1, . . . , 2n − 1. After this truncation the initial basis
state |xτ  is mapped to |1n 0n , while the ﬁnal basis state
xλ+τ is mapped to a weight-n bit string with support
{λ1 + n − 1, λ2 + n − 2, . . . , 0} [29]. Now the Frobenius
character formula becomes
χλ (g) = xλ+τ |

c(g)


Jνj |1 0 ,
n n

λj = m(x) − n(n − 1)/2 = n.

j =1

Thus, λ is a partition of n.
Clearly, the current operators Jνj preserve the weight of
bit strings. Each application of Jνj increases the momenc(g)
tum by νj . Since the
j =1 νj = n and the initial bit
string 1n 0n has momentum n(n − 1)/2, the ﬁnal state is a
superposition of bit strings with weight n and momentum
n(n − 1)/2 + n = n(n + 1)/2. As shown above, these are
exactly the bit strings encoding partitions of n.
IV. CLASSICAL MPS ALGORITHMS
Consider a permutation g ∈ Sn . Let c(g) be the number
of cycles in g and νj be the length of the j th cycle. Our
strategy is to represent the 2n-qubit state
|ψg  =

(13)

j =1

c(g)


Jνj |1n 0n 

(15)

j =1

by an MPS. To this end, we need the following lemma.

where
J =

2n−1−


†

ak+ ak .

(14)

Lemma 2. The current operator J is an MPO with bond
dimension  + 2.

k=0

This concludes the derivation of the Crichigno and Prakash
mapping from characters of Sn to a quantum spin chain.
c(g)
As pointed out in Ref. [13], state |ψg  = j =1 Jνj |1n 0n 
has support only on bit strings encoding partitions of n.
This can be seen as follows. Let x = (x0 , x1 , . . . , x2n−1 )

be a bit string of length 2n. Let |x| = 2n−1
j =0 xj be the
2n−1
weight of x and m(x) = j =0 jxj be the momentum

of x. For example, m(1n 0n ) = n−1
j =0 j = n(n − 1)/2. We
claim that x encodes a partition of n if and only if x has
weight n and momentum n(n + 1)/2. Indeed, suppose that
x = xλ+τ for some partition λ  n. Then x has weight
n since we agreed that λ has n parts (including the
padded zero parts).
 By deﬁnition, x has support {λj + n −
j }j =1,...,n . From nj=1 λj = n one gets
n

(λj + n − j ) = n(n + 1)/2.
m(x) =
j =1

Conversely, suppose that x has weight n and momentum
n(n + 1)/2. Let 2n − 1 ≥ d1 > d2 > · · · > dn ≥ 0 be the
indices of nonzero bits of x. Set λj = j + dj − n for j =
1, . . . , n. From dj > dj −1 one gets n ≥ λ1 ≥ · · · ≥ λn ≥ 0.

Proof. Figure 1 deﬁnes a tensor T ∈ C2 ⊗ C+2 ⊗
C ⊗ C2 , where C2 represents physical indices and C+2
represents virtual indices of the MPO. Taking 2n copies of
T and contracting all virtual indices (horizontal lines) as
shown in Fig. 1 gives an operator
+2

2n−1−
 
j =0

0
0



1
0
Zj +1 · · · Zj +−1
0 j
1


0
.
0 j +

This is the current operator deﬁned in Eqs. (7) and (8).



The initial state |1n 0n  is clearly an MPS with bond
dimension 1. Deﬁne a sequence of MPSs |φ0  = |1n 0n  and
|φj  = Compress(Jνj |φj −1 , )

(16)

for j = 1, . . . , c(g). Here Compress(|φ, ) is a function
that computes the canonical form of an MPS |φ and truncates the singular values (Schmidt coeﬃcients) at each site,
as discussed in Sec. 4.5.1 of Ref. [30]. The error tolerance  ≥ 0 deﬁnes the maximum relative error incurred
while truncating singular values. More precisely, suppose
that s1 ≥ s2 ≥ · · · ≥ sN are singular values of some MPS

030323-5


SERGEY BRAVYI et al.

PRX QUANTUM 6, 030323 (2025)
|ψg  can be computed in time O(nc(g)D3 ) = O(n2 D3 ). Let
|mpsg  = |φc(g) 
be the ﬁnal MPS approximating |ψg . The character of any
irrep λ  n can then be extracted by computing a single
amplitude of the ﬁnal MPS,
χλ (g) = xλ+τ |ψg  ≈ xλ+τ |mpsg .

(18)

This takes time O(nD3 ).
Suppose that one needs to compute MPS amplitudes
xλ+τ |ψg  for all irreps λ. To speedup this computation,
we divided the spin chain into four blocks of length n/2
and cached products of the MPS tensors associated with
each block. As one iterates over irreps λ, a product of the
MPS tensors is retrieved from the cache, if available. We
observed that the runtime for computing MPS amplitudes
with the caching strategy described above is comparable or
smaller than the runtime for computing the MPS tensors.
Recall that Sn characters are integer valued. Thus, the
exact value of χλ (g) can be recovered by rounding the ﬁnal
MPS amplitude to the nearest integer as long as
FIG. 1. MPO representation of the current operator J . Horizontal lines represent virtual indices of dimension  + 2. We
label basis vectors of C+2 by integers {0, 1, . . . ,  + 1}. The
MPO consists of 2n copies of T. We list all nonzero components
of tensor T.

|φj  for some bipartite cut of the chain. We discard singular values si with i ≥ d, where d is the smallest index such
that
N
N


si ≤ 
si .
i=d+1

i=1

We chose to impose a bound on the relative truncation error
since the considered states are unnormalized and some singular values si can be exponentially large. Let D = D()
be the maximum bond dimension of all states |φj  with
j ≤ c(g). Lemma 2 ensures that
D≤

c(g)


(νj + 2).

(17)

j =1

We do not expect this bound to be tight, even for lossless
compression,  = 0. For example, one can easily check
that a state Jν1 |1n 0n  has a bond dimension of only ν1
instead of ν1 + 2 predicted by Eq. (17). We empirically
observed that the MPS bond dimension D at the compression error  = 10−10 can be smaller than the upper bound
(17) by several orders of magnitude; see Fig. 3 below.
Since the cost of MPO-MPS multiplication and MPS
compression scales as O(nD3 ), an MPS representation of

|χλ (g) − xλ+τ |mpsg | < 12 .

(19)

An error introduced by the compression can be estimated
by comparing the norm of the exact state |ψg  and the
approximating MPS. The orthogonality theorem for characters [28] gives
ψg 2 =



χλ (g)2 = |Eg |,

(20)

λn

where Eg = {h ∈ Sn : hg = gh} is the centralizer of g.
Denoting the number of length- cycles in g by a , one
gets
|Eg | =

n


(a !)a .

(21)

=1

We used the mpnum software [17] for numerical experiments and set the compression error to  = 10−10 . The
runtime of the MPS algorithm is compared with the runtime of two widely used computer algebra systems: GAP
[31] and the symmetrica library included in SAGE [32];
see Fig. 2.
For numerical experiments, we selected permutations
with a large number of short cycles that tend to be most
expensive for all considered algorithms. Namely, for each
n, we consider a single permutation g ∈ Sn composed of
n/2 length-2 cycles. Figure 2 shows the measured runtime
for 10 ≤ n ≤ 30. The reported runtimes include computation of the characters χλ (g) for all irreps λ  n. In the

030323-6


CLASSICAL AND QUANTUM ALGORITHMS. . .

PRX QUANTUM 6, 030323 (2025)
for all problem instances reported at Fig. 2 [the exact value
of χλ (g) was computed using the SAGE library]. This
is many orders of magnitude smaller than the required
precision 1/2, suggesting that the MPS runtime may be
improved further by truncating more singular values. Our
PYTHON implementation of the MPS algorithm is available from GitHub [33]. We provide two versions of the
algorithm that use the mpnum or quimb libraries for
MPO-MPS manipulations.
Finally, for each problem instance presented in Fig. 2,
we computed the maximum MPS bond dimension and
compared it with the upper bound (17). This comparison
is reported in Fig. 3.
V. QUANTUM ALGORITHM

FIG. 2. Runtime for computing the characters χλ (g) for permutations g ∈ Sn composed of n/2 length-2 cycles and all irreps
λ  n. The MPS compression error is set to  = 10−10 for all the
data.

case of the MPS the runtime additionally includes computing state |mpsg . As one can see from the plot, the MPS
algorithm shows a competitive performance for large values of n. We note that our implementation is in PYTHON,
while SAGE and GAP have a kernel written in C, which
tends to be much faster than PYTHON.
Recall that our MPS algorithm computes character
χλ (g) with the zero error as long as the MPS amplitude
xλ+τ |mpsg  obeys Eq. (19). We found that
|χλ (g) − xλ+τ |mpsg | ≤ 10−6

Here we describe a quantum circuit of size poly(n)
that prepares a state |ψg /ψg ; see Eq. (15). Our circuit
applies the quantum Fourier transform over group Sn to a
certain subset state constructed in the following lemma.
Lemma 3. Let g ∈ Sn be a permutation and Cg ⊆ Sn be
the conjugacy class of g. There exists a quantum circuit of
size poly(n) that prepares a subset state
1 
|Cg  = 
|h.
|Cg | h∈C

(22)

g

We defer the proof till the end of this section. Recall
that a QFT over the symmetric group Sn is deﬁned as a
unitary operator QFTn with input Hilbert space
 C[Sdn ] =
λ
span(|g : g ∈ Sn ) and output Hilbert space
λn C ⊗
Cdλ such that
QFTn |g =


λn



λ
dλ 
i|ρλ (g)|j |λ, i, j 
n! i,j =1

d

(23)

for all permutations g ∈ Sn .
Here dλ is the dimension of λ. The inverse QFT acts as

QFT†n |λ, i, j  =

dλ 
i|ρλ (g)|j ∗ |g.
n! g∈S

(24)

n

It is known [18] that QFTn can be implemented by a quantum circuit of size poly(n). Applying QFTn to the subset
state |Cg  gives a state

FIG. 3. Comparison between the observed maximum MPS
bond dimension for the problem instances reported in Fig. 2
(blue) and the upper bound (17) (green).

|θg  = QFTn |Cg 

dλ
 dλ 
1 

=
i|ρλ (h)|j |λ, i, j . (25)
n! i,j =1 |Cg | h∈C
λn

030323-7

g


SERGEY BRAVYI et al.

PRX QUANTUM 6, 030323 (2025)


Since h∈Cg h is a central element of the group algebra
C[Sn ], we infer that


ρλ (h) = bIdλ

a given irrep λ  n. Indeed, apply QFT†n to an initial state
dλ
1 
|λ, i, i.
|θλ  = √
dλ i=1

(26)

h∈Cg

This gives a state
for some complex number b ∈ C. Here Idλ is the identity
matrix of size dλ . Taking the trace of Eq. (26) gives
b=

|Cg |χλ (g)
.
dλ

(27)

Substituting Eqs. (26) and (27) into Eq. (25) and using the
identity |λ, i, j  = |λ ⊗ |i, j  shows that

|θg  =

|Cg | 
χλ (g)|λ ⊗ |φλ ,
n! λn

dλ
1 
|φλ  = √
|i, i.
dλ i=1

Let U be a unitary operator that maps |λ ⊗ |0 to |λ ⊗
|φλ . One can realize U by a quantum circuit of size
poly(n), for example using the techniques of Ref. [34],
since the dimension dλ can be computed in time poly(n)
using the well-known hook length formula [35].
Applying U −1 to state |θg  and tracing out the second
register gives a state

|ωg  =

(the complex conjugate can be omitted since Sn characters are real). By measuring state |ωλ  in the standard basis
one can sample a permutation g ∈ Sn from a probability
distribution
Pλ (g) =

where



1 
|ωλ  = QFT†n |θλ  = √
χλ (g)∗ |g
n! g∈Sn

|Cg | 
1 
χλ (g)|λ = 
χλ (g)|λ,
n! λn
|Eg | λn

where Eg is the centralizer of g; see Eq. (21). This a normalized version of the desired state |ψg  if one encodes a
partition λ  n by a bit string xλ+τ , as discussed in Sec.
III. By measuring state |ωg  in the standard basis one can
sample an irrep λ  n from a probability distribution
(χλ (g))2
Pg (λ) =
|Eg |

(row sampling).

(28)

(χλ (g))2
n!

(column sampling).

This is equivalent to sampling a column of the character
table of Sn with the probability proportional to the character squared (here we assume that columns are labeled by
permutations rather than conjugacy classes). We discuss
the classical hardness of these sampling problems in the
next section.
It is tempting to use our access to row and column sampling to estimate the characters themselves via repeated
sampling. However, column sampling fails to yield eﬃcient√ algorithms. To see this, note that χλ (g)2 ≤ dλ2 ≤
e−C n n! (C > 0 is a constant), where the second inequality
follows from known asymptotics [36]. Thus, the probabilities in Eq. (29) are always superpolynomially small in n
and diﬃcult to estimate. Could row sampling yield eﬃcient
estimates of characters? All characters could be estimated
when |Eg | is polynomial in n. This holds, for example,
when c(g) = O(1). But, in this case, the MPS algorithm
of Sec. IV computes all characters in time polynomial in n.
One could look for cases where both |Eg | and χλ (g)2 are
large; a task we leave to future work. We note that similar
approaches were considered for computing multiplicities
in tensor product representations [27,37].
Proof. Let k = |Cg | and
Cg = {h1 , h2 , . . . , hk }.
Suppose that one can construct permutations f1 , f2 , . . . , fk ∈
Sn such that
hj = fj gfj −1

This is equivalent to sampling a row of the character table
of Sn with the probability proportional to the character
squared.
A similar method can prepare a superposition of all permutations g ∈ Sn with amplitudes proportional to χλ (g) for

(29)

(30)

for all j = 1, . . . , k and that there exists a quantum circuit
Q of size poly(n) such that

030323-8

Q|hj  ⊗ |0 = |hj  ⊗ |fj 

(31)


CLASSICAL AND QUANTUM ALGORITHMS. . .

PRX QUANTUM 6, 030323 (2025)

for all j = 1, . . . , k. Then the desired state |Cg  can be
prepared as follows. First prepare a state
1 
|ψ1  = √
|e ⊗ |g.
n! e∈Sn
Apply a classical reversible circuit that maps |e ⊗ |g to
|e ⊗ |ege−1 . This gives a state
1 
|ψ2  = √
|e ⊗ |ege−1 .
n! e∈Sn

Here the second equality makes use of Eq. (30) and the
equality Cg = {h1 , h2 , . . . , hk }.
It remains to construct permutations f1 , . . . , fk and a
quantum circuit Q satisfying Eqs. (30) and (31). Suppose
that g consists of a cycles of length , where a is an
integer in the range [0, n] and
n=

Eg = {b ∈ Sn : gb = bg}.
Since left cosets of Eg in Sn can be identiﬁed with elements
of Cg , any permutation e ∈ Sn can be uniquely decomposed
as e = fb for some f ∈ {f1 , . . . , fk } and some b ∈ Eg . Thus,
k
1 
|fj b ⊗ |fj gfj −1 .
|ψ2  = 
k|Eg | j =1 b∈E
g

Here we noted that n! = k|Eg |. Tensoring in the third register prepared in the |0 state and applying circuit (31) to
the second and third registers gives a state

T=

g

Next apply a classical reversible circuit that maps |fj b ⊗
|fj  to |b ⊗ |fj  to the ﬁrst and third registers of |ψ3 . This
gives a state
k
1 
|b ⊗ |fj gfj −1  ⊗ |fj .
k|Eg | j =1 b∈E


Now the ﬁrst register is left in a pure state (1/ |Eg |)

b∈Eg |b. Tracing out the ﬁrst register gives a state

1 
|ψ6  = √
|fj gfj −1  ⊗ |0.
k j =1
k

such that |T,j | =  and the boxes in each subset T,j span
a length- cycle in h. Let b,j ∈ T,j be a box contained
in T,j with the smallest integer label (recall that each box
of T is labeled by an integer between 1 and n). Order the
subsets T,j with a ﬁxed  such that

Let B,j be the ﬁrst (leftmost) box of T in the j th length-
row (rows are counted starting from the top). Let f ∈ Sn
be a permutation such that
f [g p (B,j )] = hp (b,j )

for all p = 0, 1, . . . ,  − 1 (33)

and all , j . Here g p ∈ Sn denotes the pth power of g. Since
any box of T can be obtained from some box B,j by applying powers of g, permutation f is uniquely determined by
h. Also, it is clear that the map h → f is computable in
time poly(n). Next we claim that h = fgf −1 . Since h cyclically shifts boxes in each subset T,j , it suﬃces to check
that
hp (b,j ) = (fgf −1 )p (b,j )

Finally, tracing out the second register we obtain a state
k
1 
1 
|ψ7  = √
|fj gfj −1  = 
|h = |Cg .
|Cg | h∈C
k j =1
g

T,j

b,1 < b,2 < · · · < b,a .

g

Applying the inverse of circuit (31) gives a state

a
n 

=1 j =1

1
|ψ3  = 
|fj b ⊗ |fj gfj −1  ⊗ |fj .
k|Eg | j =1 b∈E

1
|ψ5  = √
|fj gfj −1  ⊗ |fj .
k j =1

(32)

Clearly, the conjugacy class Cg depends only on a1 , . . . , an .
Let T be a Young tableau with n boxes and a rows of
length  for  = 1, . . . , n. We ﬁll T with integers 1, 2, . . . , n
in the row major order starting from the leftmost box in the
ﬁrst (top) row. Now integers 1, 2, . . . , n can be identiﬁed
with boxes of T. We can assume without loss of generality
that g cyclically shifts boxes in each row of T such that the
ith box in a row j goes to the (i + 1)th box in the same row
and the last box in a row j goes to the ﬁrst box in the same
row.
Consider a permutation h ∈ Cg . Clearly, h has the same
cyclic type as g although boxes spanning each cycle of h
may be scattered over many rows of T. This determines a
partition of T into a disjoint union of subsets

k 


k


a .

=1

Let Eg be the centralizer of g,

|ψ4  = 

n


(34)

for all , j , p. The above is equivalent to
hp (b,j ) = f [g p f −1 (b,j )] = f [g p (B,j )],

030323-9

(35)


SERGEY BRAVYI et al.

PRX QUANTUM 6, 030323 (2025)

which follows from Eq. (33). A classical circuit of size
poly(n) computing the map h → f can be converted to a
polynomial-sized quantum circuit Q1 computing a map

Q1 |h ⊗ |0 ⊗ |0 = |h ⊗ |garbage(h) ⊗ |f .
Here garbage(h) represents auxiliary bits used to make all
gates reversible. Making a copy of the third register in
the standard basis and applying the inverse of Q1 gives
a polynomial-sized circuit Q computing a map

Q|h ⊗ |0 = |h ⊗ |f ,
where h = fgf −1 . This is the circuit deﬁned in Eq. (31).

We note that the problem of preparing conjugacy class
states |Cg  for more general groups is considered in Ref.
[38]. Our proof of Lemma 3 closely follows the strategy
outlined in Appendix D of Ref. [38].
VI. CLASSICAL COMPLEXITY OF SAMPLING
In Sec. V we showed that a quantum computer can
eﬃciently sample from probability distributions (28) and
(29) associated with a given column or row of the character table of the symmetric group Sn . Are these sampling
problems hard for classical computers?
A. Granularity and quantum advantage
Let us ﬁrst consider a general setting in which a sampling problem is deﬁned by a probability distribution P
over some ﬁnite set  called the sample space and an
error tolerance . We consider inﬁnite families of problem instances labeled by an integer n called the problem
size. It is required that each point x ∈  can be speciﬁed by poly(n) bits. Likewise, the probability distribution
P should admit a succinct classical description of size
poly(n). We also assume that the error tolerance obeys
 ≥ poly(1/n). A classical or quantum algorithm solves
the sampling problem if it outputs a sample x ∈  from
some probability distribution P that is  close to P
in
 the total variation distance, such that P − P 1 ≡
x∈ |P(x) − P (x)| ≤ . Such an algorithm is eﬃcient if
its runtime is at most poly(n).
We are speciﬁcally interested in sampling problems
that can be solved eﬃciently by a quantum computer. To
provide evidence for classical hardness of such a sampling problem, one can follow the complexity-theoretic
argument pioneered in Refs. [19,39]. Roughly speaking,
this argument gives a reduction from average-case strong
simulation—computing output probabilities of a quantum
circuit in the average case over a suitable ensemble—to
the sampling problem of interest. Here the reduction uses
polynomial time classical resources as well as access to an

NP oracle (i.e., it is a BPPNP algorithm). If the averagecase strong simulation problem is so hard that it cannot
be solved using resources within the polynomial hierarchy
then this implies that no eﬃcient classical algorithm can
solve the sampling problem of interest.
Here we describe a variant of this argument for sampling
problems with a certain granularity structure, described
below.
Definition 1 (Granularity). A probability distribution P
over a ﬁnite set  is called granular if there exists a real
number γ ≥ 1 such that P(x) is an integer multiple of
γ /|| for all points x ∈ . We refer to the number γ as
the granularity of P.
For example, distribution (29) deﬁned by columns of
the character table has granularity γ = 1 since the sample
space has size || = |Sn | = n! and characters of the symmetric group are integer valued. Distribution (28) deﬁned
by rows of the character table may or may not be granular depending on the choice of the permutation g ∈ Sn ,
as detailed below. If the input of a sampling problem is a
granular distribution P, the granularity γ and the size of
the sample space || have to be included in the classical
description of P.
Lemma 4. Suppose that P0 and P1 are probability distributions over a ﬁnite set  such that P0 is granular, P1 can
be sampled by a BPP algorithm and P0 − P1 1 ≤  for a
given  that is at least inverse polynomial in n. Let γ ≥ 1
be the granularity of P0 . There exists a BPPNP algorithm
that takes as input a point x ∈  and outputs an integer
k(x) such that
P0 (x) =

γ k(x)
||

(36)

for at least a max {0, 1 − 20} fraction of points x ∈ .
Proof. Let N = ||. Deﬁne the sets


1
S = x ∈  : P0 (x) ≤
10N 
and


T = x ∈  : |P0 (x) − P1 (x)| ≤


1
.
10N

Markov’s inequality gives |S| ≥ (1 − 10)N and |T| ≥
(1 − 10)N . By the union bound,
|S ∩ T| ≥ (1 − 20)N .

(37)

The assumption that P1 can be sampled by a BPP algorithm
and Stockmeyer’s approximate counting theorem [40]
imply that there exists a BPPNP algorithm that takes as

030323-10


CLASSICAL AND QUANTUM ALGORITHMS. . .

PRX QUANTUM 6, 030323 (2025)

input a point x ∈  and outputs a real number P2 (x) such
that
|P2 (x) − P1 (x)| ≤ P1 (x).
For any x ∈ S ∩ T, one has P1 (x) ≤ P0 (x) + 1/(10N ) ≤
1/(10N ) + 1/(10N ) ≤ 1/(5N ), which implies that
|P2 (x) − P1 (x)| ≤ 1/(5N ). Thus, for any x ∈ S ∩ T, one
has

least 1 − 1/γ . Indeed, the dummy algorithm succeeds
with probability |S|/||, where S = {x ∈  : P(x) = 0}.
Granularity gives P(x) ≥ γ /|| for x ∈
/ S. Thus, 1 =

P(x)
≥
γ
(||
−
|S|)/||,
that
is,
|S|/|| ≥ 1 −
x∈
1/γ , as claimed. This shows that the average-case hardness property (3) can only be achieved if the granularity γ
is at most polynomial in n.
B. Row and column sampling

|P2 (x) − P0 (x)| ≤ |P2 (x) − P1 (x)| + |P0 (x) − P1 (x)|
≤

1
1
1
+
≤
.
5N
10N
3N

(38)

By assumption, P0 (x) is an integer multiple of γ /N for
a given γ ≥ 1. Let P3 (x) be an integer multiple of γ /N
closest to P2 (x). Using Eq. (38), one gets P3 (x) = P0 (x)
whenever x ∈ S ∩ T. The above shows that P3 (x) can be
computed by a BPPNP algorithm and Eq. (37) implies that
P3 (x) = P0 (x) for at least a 1 − 20 fraction of points x ∈
. Finally, set k(x) = (N /γ )P3 (x).

A central challenge in quantum complexity theory is
to prove the quantum advantage conjecture [19] in the
following form.
Conjecture 1. Assume that the polynomial hierarchy
does not collapse. Then there exists a sampling problem
that can be solved eﬃciently on a quantum computer and
that is provably hard for classical randomized algorithms.
Lemma 4 implies that the conjecture is true if there
exists a sampling problem satisfying the following properties.
(1) Granularity: the sampling problem is based on a
family of granular probability distributions P.
(2) Quantum algorithm: the sampling problem can be
solved eﬃciently on a quantum computer.
(3) Average-case hardness: the problem of computing
P(x) exactly on a point x ∈  picked uniformly at
random with a suﬃciently high success probability is not contained in the polynomial hierarchy.
Here the success probability must be at least 1 −
poly(1/n) for problem instances of size n.
We see that, for granular distributions, the hardness of
classical sampling follows from the average-case hardness property (3) and the assumption that the polynomial
hierarchy does not collapse. This diﬀers from the usual
argument in that we do not need to establish the so-called
anticoncentration property for the family of distributions
P; moreover, the average-case hardness property (3) concerns exact computation of output probabilities rather than
approximate computation.
Note that a dummy algorithm for computing P(x) that
outputs zero for all x ∈  has success probability at

We have already seen that the column sampling problem obeys properties (1) and (2). Furthermore, computing
the probability Pλ (g) = |χλ (g)|2 /n! is #P-hard in the worst
case [4]. Moreover, this problem is not contained in #P
unless the polynomial hierarchy collapses to the second
level [4]. However, it seems unlikely that average-case
hardness property (3) holds for this problem. In particular, the following lemma gives a classical quasipolynomial
time algorithm for computing Pλ (g) that succeeds with
high probability if g ∈ Sn is a random permutation.
Lemma 5. There exists a classical algorithm that takes
as input an irrep λ of the symmetric group Sn , a permutation g ∈ Sn , and outputs an integer k(g) such that k(g) =
χλ (g) for at least a 1 − 1/n100 fraction of permutations
g ∈ Sn . The algorithm has runtime nO(log n) .
Proof. The proof combines the MPS algorithm of Sec.
IV for computing characters of Sn with tail bounds for the
number of cycles in a random permutation. We use the
algorithm from Sec. IV with zero truncation error ( = 0).
With input λ  n and g ∈ Sn , this algorithm computes
an MPS |ψg  of bond dimension (17) that can be upped
bounded as D ≤ (n + 2)c(g) , where c(g) is the number of
cycles in g. Recall that computing this MPS and extracting
the amplitude χλ (g) uses a runtime upper bounded as
O(n2 D3 ) = nO[c(g)] .
This runtime is exponential in n in the worst case since
the number of cycles c(g) can be linear in n. However,
we are only interested in the average case, that is, random permutations. Furthermore, random permutations are
known to have only a few cycles with high probability. The
following fact is a special case of Theorem 1.7 of Ref. [41].
Fact 1. Suppose that g ∈ Sn is picked uniformly at random. Let c(g) be the number of cycles in g. Then, for all
 ≥ 1, one has
Pr[c(g) ≥ 1 + Hn ] ≤ 2e1−[ log ()−+1]Hn ,

(39)


where Hn = nj=1 1/j = log (n) + O(1) is the nth harmonic number and e = 2.718 28 . . ..

030323-11


SERGEY BRAVYI et al.

PRX QUANTUM 6, 030323 (2025)

Corollary 1. There exists a constant B > 0 such that
the fraction of permutations g ∈ Sn with c(g) > B log (n)
cycles is at most 1/n100 for all large enough n.
If c(g) ≤ B log n, use the MPS algorithm to compute
χλ (g), which takes time nO(log n) . Otherwise, if c(g) >
B log n, output some ﬁxed integer (say zero). This gives
the desired algorithm.

Next let us consider the row sampling problem.
Lemma 5 suggests that classically hard instances of the
problem can be constructed by choosing the input permutation g√
∈ Sn with a large number of cycles, for example,
c(g) ∼ n. In this case best-known classical algorithms
for computing the characters χλ (g) appear to require an
exponential time. However, we need to check whether permutations g with a large number of cycles give rise to
instances of the row sampling problem with a granular
distribution. This is addressed in the following lemma.
Lemma 6 (Granularity for row sampling). There exist a
universal constant A > 0 such that the probability distribution Pg (λ) over partitions λ  n from Eq. (28) is√granular
whenever g ∈ Sn is a permutation with at most A n/ log n
cycles.
Proof. Let n be the set of partitions λ  n (our sample
space). We can write
Pg (λ) = γ

|χλ (g)|2
,
|n |

γ =

|n |
,
|Eg |

(40)

where Eg is the centralizer of g. Since χλ (g) is integer for
all λ ∈ n , distribution Pg (λ) is granular whenever γ ≥ 1.
Suppose that g consists of a cycles of length . Then
|Eg | is given
by Eq. (21). Also, it is known [42] that
√
|n | ≥ eA n for
√ some universal constant A > 0 (one can
choose A = π 2/3 −  for any constant  > 0) and all
suﬃciently large n. Thus,
√

eA n
γ > n
.
a
=1  a !

(41)

Since a ! ≤ (a )a , one gets


√

γ ≥ exp A n −

n



a log (a ) .

(42)

=1

From Eq.
 (32) one gets a ≤ n. Using this along with
c(g) = n=1 a gives
√
γ ≥ exp [A n − c(g) log n].
√
Thus, γ ≥ 1 whenever A n − c(g) log n ≥ 0.

(43)



We conclude that√ the row sampling problem for permutations g with A n/ log n or less cycles obeys properties (1) and (2). Proving or disproving property (3)—the
average-case hardness of computing Pg (λ) for random
partitions λ  n—is left as a challenge for future work.
The proposed reduction from strong-to-weak simulation
may apply to sampling tasks unrelated to the symmetric
group. As a concrete example, consider a sampling version of the commuting local Hamiltonian problem [43].
Suppose that m ≥ n are integers and that H1 , . . . , Hm are
pairwise commuting n-qubit projectors such that each projector acts nontrivially only on a few qubits. Hamiltonians
composed of few-qubit commuting projectors are often
used as toy models of the topological quantum order [44].
Given a bit string x ∈ {0, 1}m , let Lx be the subspace
spanned by n-qubit states ψ such that Ha |ψ = xa |ψ for
all a = 1, . . . , m. Let dx be the dimension of Lx . Consider a
normalized probability distribution P(x) = dx /2n describing the joint eigenvalue measurement for the projectors
H1 , . . . , Hm on the maximally mixed state of n qubits.
Since the sample space has size 2m , distribution P(x) has
granularity γ = 2m−n ≥ 1. A quantum computer can eﬃciently sample P(x) by measuring the projectors one by
one in some ﬁxed order. Assuming that the task of computing dimension dx for a random uniform x ∈ {0, 1}m is not
contained in the class BPPNP , our strong-to-weak reduction implies that no BPP algorithm can sample distribution
P(x) with a small error. We note that a closely related task
of deciding whether dx > 0 for a given bit string x is a variant of the commuting local Hamiltonian problem that has
been studied by many authors [43,45–50].
VII. CLASSICAL MPS ALGORITHM FOR
KOSTKA NUMBERS
In Sec. IV we showed that Crichigno and Prakash’s connection between quantum spin chains and characters of the
symmetric group can be leveraged in an MPS algorithm
for characters. In Ref. [13] they also proved mappings
between spin chains and Kostka numbers and LittlewoodRichardson coeﬃcients. Using similar ideas to characters,
we show that this correspondence can be used to give an
MPS algorithm for Kostka numbers.
Kostka numbers appear frequently in combinatorics and
representation theory. Let λ  n. A semistandard Young
tableau of shape λ is a ﬁlling of the boxes in the Young
diagram corresponding to λ with positive integers between
1 and n such that the labels are nondecreasing across rows
and strictly increasing down columns. The weight of such
a tableau is an integer-valued vector of length n such that
the ith entry is the number of occurrences of i. The Kostka
number Kλ,μ is the number of semistandard Young tableaus
of shape λ and weight μ. Note that Kλ,μ is independent of
the order of the entries in μ and thus we assume that μ
is a partition of n. A notable special case is Kλ,(1n ) , which

030323-12


CLASSICAL AND QUANTUM ALGORITHMS. . .

PRX QUANTUM 6, 030323 (2025)

is the dimension of the irrep labeled by λ. More generally, Kλ,μ appears in the representation theory of Sn as
the multiplicity of the irrep λ in the permutation module
indexed by μ. In the language of symmetric polynomials,
the Kostka numbers encode the change of basis from Schur
polynomials to complete symmetric polynomials.
Crichigno and Prakash used this latter characterization
to demonstrate that quantum spin chains encode Kostka
numbers as well [13]. We brieﬂy review their construction here. Again, let the initial state |xτ  correspond to the
integer sequences (n − 1, n − 2, . . . , 0) in the second quantization picture. For commuting variables, the complete
symmetric polynomial hk is given by


hk =

xi1 xi2 · · · xik .

(44)

1≤i1 ≤···≤ik

For example, in three variables h2 = x12 + x22 + x32 +
x1 x2 + x1 x3 + x2 x3 . In Crichigno and Prakaksh’s construction the commutative variables are replaced with oper†
ators x̂i := ai+1 ai , where a (a† ) is again an annihilation
(creation) operator. Then, the noncommutative complete
symmetric polynomials take the form
ĥk =



x̂i1 x̂i2 · · · x̂k .

(45)

i1 >···>ik

Note that the indices are required to be strictly decreasing,
which follows from x̂i2 = 0 for any index i. Say that μ  n

is a partition of length m. We deﬁne ĥμ = m
j =1 ĥμj (the
operators commute and thus the order of the product does
not matter [13]). The authors showed that
Kλ,μ = xλ+τ |ĥμ |xτ .

(46)

Note that ĥμ moves fermions at most n sites to the right and
we can again truncate the chain to 2n sites with the initial
state |xτ  = |1n 0n .
Similarly to the MPS algorithm for characters, we represent the 2n-qubit state
|ψμ  =

m


ĥμi |1n 0n 

(47)

i=1

by an MPS. We do so via the following lemma.
Lemma 7. The noncommuting complete symmetric
polynomial ĥk is an MPO with bond dimension 2k + 1.
Proof. Figure 4 deﬁnes a tensor T ∈ C2 ⊗ C2k+1 ⊗
C
⊗ C2 , where C2 represents physical indices and
2k+1
C
represents virtual indices of the MPO. Taking 2n
2k+1

FIG. 4. MPO representation of the noncommuting complete
symmetric polynomial ĥk . Horizontal lines represent virtual
indices of dimension 2k + 1. We label basis vectors of C2k+1 by
integers {0, 1, . . . , 2k}. The MPO consists of 2n copies of T. We
list all nonzero components of tensor T.

copies of T and contracting the virtual indices gives an
operator

x̂i1 x̂i2 · · · x̂ik .
(48)
i1 >i2 >···>ik

This is exactly ĥk as deﬁned in Eq. (45).



From the bond dimension of this MPO, we can upper
bound the maximum bond dimension of all states during
compression as
D≤

m


(2μj + 1).

(49)

j =1

In running numerics, however, bond dimensions appeared
to be signiﬁcantly lower.
Denote the compressed MPS state as |mpsμ . Similarly
to characters, Kostka numbers take integer values and thus
the correct value is recovered as long as
|Kλ,μ − λ|mpsμ | < 12 .

(50)

We again used the mpnum software for numerical simulations with an error rate ε = 10−11 . We compared the MPS
algorithm to the symmetrica library of SAGE; see Fig. 5.
For numerical experiments, we selected random partitions μ with a smaller number of parts, fewer than

030323-13


SERGEY BRAVYI et al.

PRX QUANTUM 6, 030323 (2025)
and Economic Development, and by the Province of
Ontario through the Ministry of Colleges and Universities. D.G. acknowledges support as a Canadian Institute
for Advanced Research fellow, in the quantum information science program. L.S. was supported by IBM through
the Illinois-IBM Discovery Accelerator Institute.
DATA AVAILABILITY
The data supporting the ﬁndings of this article and a
Python package to implement the MPS algorithms for
characters and Kostka numbers are openly available [33].

FIG. 5. Runtime for computing Kostka numbers Kλ,μ . Each
runtime is, ﬁxing a random μ, for computing the set {Kλ,μ }λ .
One hundred random μ’s of length less than n/3 were sampled
for each n. The MPS compression error is set to ε = 10−12 for
all the data. Boxes indicate the ﬁrst and third quartiles and the
whiskers denote 1.5 times the interquartile range.

n/3. On longer partitions the MPS algorithm appears to
require smaller ε and longer run times. For example,
μ = (1, . . . , 1) proved diﬃcult to compute via the MPS
algorithm yet can be quickly computed via the hook length
formula. However, in the regime of shorter partitions, our
numerics oﬀer evidence that the MPS is competitive and
often faster than Sage for large n. It is further worth noting
that√most partitions are relatively short, the average being
[ n log(n)] [51]. Our implementation, as well as that for
skew Kostka numbers (a generalization), is available from
GitHub [33].
An interesting question, which we leave for future work,
is if Littlewood-Richardson coeﬃcients can be recovered
by a nontrivial MPS algorithm. Doing so via a mapping to
spin chains would require MPO constructions for noncommutative Schur polynomials [13]. Schur polynomials do
c(g)
not admit an obvious modular construction unlike j =1 Jηj

and m
j =1 ĥμj (from the commuting products). This would
seem to complicate MPO constructions.
We also leave open the question of sampling from distributions with probabilities deﬁned by normalized Kostka
numbers, in analogy to the results in Sec. V. A related task
was studied in Refs. [27,37], but there the distributions
contained just a single probability that was a normalized
Kostka number. It would be interesting to ﬁnd quantum
circuits that prepare a quantum state that corresponds to
the MPS we derive here.
ACKNOWLEDGMENTS
This research was supported in part by the Perimeter Institute for Theoretical Physics. Research at the
Perimeter Institute is supported by the Government of
Canada through the Department of Innovation, Science,

[1] Daniel Grier and Luke Schaeﬀer, in Proceedings of the
52nd Annual ACM SIGACT Symposium on Theory of Computing (Association for Computing Machinery, Chicago,
USA, 2020), p. 875.
[2] David Lawrence Johnson, Minimal permutation representations of ﬁnite groups, Am. J. Math. 93, 857 (1971).
[3] Charles Thomas Hepler, On the complexity of computing characters of ﬁnite groups. Master’s thesis.
https://prism.ucalgary.ca/items/0d83d63a-ec3b-47bdb5ca-18bf532eb49a, (1996).
[4] Christian Ikenmeyer, Igor Pak, and Greta Panova, Positivity of the symmetric group characters is as hard as the
polynomial time hierarchy, Int. Math. Res. Not. 2024, 8442
(2023).
[5] Gerald V. Dunne, Slater decomposition of Laughlin states,
Int. J. Mod. Phys. B 7, 4783 (1993).
[6] Andrea Di Gioacchino, Luca Guido Molinari, Vittorio
Erba, and Pietro Rotondo, Uniﬁed Fock space representation of fractional quantum Hall states, Phys. Rev. B 95,
245123 (2017).
[7] Di Gioacchino, Fock-space operator construction of Laughlin fractional quantum Hall eﬀect states: http://pcteserver.mi.
infn.it/caraccio/Lauree/DiGioacchino_m.pdf, (2015).
[8] P. Di Francesco, M. Gaudin, C. Itzykson, and F. Lesage,
Laughlin’s wave functions, Coulomb gases and expansions
of the discriminant, Int. J. Mod. Phys. A 9, 4257 (1994).
[9] Benoît Collins and Piotr Śniady, Integration with respect
to the Haar measure on unitary, orthogonal and symplectic
group, Commun. Math. Phys. 264, 773 (2006).
[10] Imre Risi Kondor, Group Theoretical Methods in Machine
Learning (Columbia University, New York City, USA,
2008).
[11] Risi Kondor and Marconi S. Barbosa, in COLT (Association for Computing Machinery, Haifa, Israel, 2010),
p. 451.
[12] Guifré Vidal, Eﬃcient classical simulation of slightly
entangled quantum computations, Phys. Rev. Lett. 91,
147902 (2003).
[13] Marcos Crichigno and Anupam Prakash, Quantum spin
chains and symmetric functions, ArXiv:2404.04322.
[14] Sergey Fomin and Curtis Greene, Noncommutative Schur
functions and their applications, Discrete Math. 193, 179
(1998).
[15] F. G. Frobenius, in Sitz. Ber. Preuss. Akad. (Prussian
Academy of Sciences, Berlin, Germany, 1900), p. 516.

030323-14


CLASSICAL AND QUANTUM ALGORITHMS. . .

PRX QUANTUM 6, 030323 (2025)

[16] Johnnie Gray, quimb: A python package for quantum information and many-body calculations, J. Open Source Softw.
3, 819 (2018).
[17] Daniel Suess and Milan Holzäpfel, mpnum: A matrix product representation library for python, J. Open Source Softw.
2, 465 (2017).
[18] Robert Beals, in Proceedings of the twenty-ninth annual
ACM symposium on Theory of computing (Association for Computing Machinery, El Paso, USA, 1997),
p. 48.
[19] Scott Aaronson and Alex Arkhipov, in Proceedings of the
forty-third annual ACM symposium on Theory of computing, (Association for Computing Machinery, San Jose,
USA, 2011), p. 333.
[20] Michael J. Bremner, Ashley Montanaro, and Dan J. Shepherd, Average-case complexity versus approximate simulation of commuting quantum computations, Phys. Rev. Lett.
117, 080501 (2016).
[21] Dominik Hangleiter and Jens Eisert, Computational advantage of quantum random sampling, Rev. Mod. Phys. 95,
035001 (2023).
[22] Francis D. Murnaghan, The characters of the symmetric
group, Am. J. Math. 59, 739 (1937).
[23] Tadasi Nakayama, in Japanese journal of mathematics:
transactions and abstracts (The Mathematical Society of
Japan, Tokyo, 1940), Vol. 17, p. 411.
[24] Ömer Eğecioğlu, in European Conference on Computer
Algebra, (Springer, Linz, Austria, 1985), p. 206.
[25] Stephen P. Jordan, Fast quantum algorithms for approximating some irreducible representations of groups,
(2009).
[26] Sergey Bravyi, Anirban Chowdhury, David Gosset, Vojtěch
Havlíček, and Guanyu Zhu, Quantum complexity of
the Kronecker coeﬃcients, PRX Quantum 5, 010329
(2024).
[27] Martin Larocca and Vojtech Havlicek, Quantum algorithms
for representation-theoretic multiplicities, Phys. Rev. Lett.
135, 010602 (2025).
[28] Pavel I. Etingof, Oleg Golberg, Sebastian Hensel, Tiankai
Liu, Alex Schwendner, Dmitry Vaintrob, and Elena Yudovina, Introduction to Representation Theory (American
Mathematical Soc., Providence, USA, 2011), Vol. 59.
[29] It may be helpful to understand this binary encoding of a
partition as follows. If we start with the bit string xτ +λ and
then interpret each 1 as “up by one” and each 0 as “to the
right by one” and then trace out a picture according to these
instructions, we get a picture of the partition λ within a
bounding box of size n × n.
[30] Ulrich Schollwöck, The density-matrix renormalization
group in the age of matrix product states, Ann. Phys. 326,
96 (2011).
[31] The GAP Group, GAP – Groups, Algorithms, and Programming, version 4.12.2, 2022.
[32] W. A. Stein et al., Sage Mathematics Software, version 9.8,
The Sage Development Team, 2023, http://www.sagemath.
org

[33] Sergey Bravyi, David Gosset, Vojtech Havlicek, and Louis
Schatzki,
https://github.com/sbravyi/symmetric_group_
characters.
[34] Alok Shukla and Prakash Vedula, An eﬃcient quantum
algorithm for preparation of uniform quantum superposition states, Quantum Inf. Process. 23, 38 (2024).
[35] Richard P. Stanley, Enumerative Combinatorics: Volume 2
(Cambridge University Press, 1999), Vol. 62.
[36] A Vershik and S Kerov, Asymptotics of the maximal and
typical dimension of irreducible representations of symmetric group, Func. Anal. Appl. 19, 25 (1985).
[37] Greta Panova, Polynomial time classical versus quantum algorithms for representation theoretic multiplicities,
ArXiv:2502.20253.
[38] Juan Bermejo-Vega and Kevin C. Zatloukal, Abelian
hypergroups and quantum computation, ArXiv:1509.05806.
[39] Michael J. Bremner, Richard Jozsa, and Dan J. Shepherd,
Classical simulation of commuting quantum computations
implies collapse of the polynomial hierarchy, Proc. R. Soc.
A: Math. Phys. Eng. Sci. 467, 459 (2011).
[40] Larry Stockmeyer, in Proceedings of the fifteenth annual
ACM symposium on Theory of computing (Association
for Computing Machinery, New York City, USA, 1983),
p. 118.
[41] Kevin Ford, Cycle type of random permutations: A toolkit,
Discrete Analysis (2022).
[42] G. H. Hardy and S. Ramanujan, Asymptotic formulaæ in
combinatory analysis, Proc. London Math. Soc. s2-17, 75
(1918).
[43] Sergey Bravyi and Mikhail Vyalyi, Commutative version of
the k-local Hamiltonian problem and common eigenspace
problem, Quantum Inf. Comput. 5, 187 (2005).
[44] A. Yu Kitaev, Fault-tolerant quantum computation by
anyons, Ann. Phys. 303, 2 (2003).
[45] Norbert Schuch, Complexity of commuting Hamiltonians
on a square lattice of qubits, Quantum Inf. Comput. 11, 901
(2011).
[46] Dorit Aharonov and Lior Eldar, in 2011 IEEE 52nd Annual
Symposium on Foundations of Computer Science (IEEE,
Palm Springs, USA, 2011), p. 334.
[47] Matthew B. Hastings, Matrix product operators and central
elements: Classical description of a quantum state, Geom.
Topol. Monogr. 18, 276 (2012).
[48] Dorit Aharonov, Oded Kenneth, and Itamar Vigdorovich,
in Proceedings of the thirteenth conference on the Theory
of Quantum Computation, Communication and Cryptography (Schloss Dagstuhl – Leibniz-Zentrum fur Informatik,
Sydney, Australia, 2018), p. 2.
[49] Dorit Aharonov and Lior Eldar, The commuting local
Hamiltonian problem on locally expanding graphs is
approximable in NP, Quantum Inf. Process. 14, 1 (2015).
[50] Sandy Irani and Jiaqing Jiang, Commuting local Hamiltonian problem on 2D beyond qubits, ArXiv:2309.04910.
[51] Paul Erdös and Joseph Lehner, The distribution of the number of summands in the partitions of a positive integer,
Duke Math. J. 8, 335 (1941).

030323-15
