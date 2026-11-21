---
doc_id: bq28-r2r7
doc_title: "Classical and Quantum Algorithms for Characters of the Symmetric Group"
section_id: sec-002-iii-building-the-character
section_title: "III.. BUILDING THE CHARACTER"
section_number: null
pages: 3-5
source_pdf: bq28-r2r7.pdf
source_sha256: 38419a88531ebce7
toc_source: outline
doc_brief: "Classical and Quantum Algorithms for Characters of the Symmetric Group — 12 sections: Front matter; I.. INTRODUCTION; II.. GROUP THEORY REFRESHER"
---
We begin by reproducing the result of Crichigno and
Prakash [13] that shows how to build a quantum spin
chain encoding all characters χλ(g) of a given permutation
g ∈Sn.
Let λ = (λ1, . . . , λm) and ν = (ν1, . . . , νc(g)) be the par-
titions of n describing the irrep λ and the conjugacy class
of g. Consider a complex vector z ∈Cm and a polynomial
Pν(z) =
c(g)

j =1

m

k=1
z
νj
k

.
(1)
The Frobenius character formula [15] (see, e.g., Theorem
4.47 of Ref. [28]) states that χλ(g) coincides with the
coeﬃcient of a monomial
z(λ) =
m

j =1
z
λj +m−j
j
(2)
in the polynomial
Q(z) = Pν(z)

1≤i<j ≤m
(zi −zj ).
(3)
Let S1 = {x ∈C: |x| = 1} be the unit circle in the complex
plane, and let F1 be a Hilbert space of functions f : S1 →
C with inner product
⟨f |g⟩= 1
2π
 2π
0
dθf (eiθ)∗g(eiθ)
and an orthonormal basis of functions {f (x) = xk}k∈Z.
Informally, F1 describes a particle moving on the cir-
cle and f (x) = xk is a state with angular momentum
k. Consider now a many-body system composed of m
indistinguishable particles moving on the circle that obey
fermionic statistics. The fermionic ﬁrst quantization prin-
ciple stipulates that the m-particle Hilbert space Fm is the
antisymmetric subspace of F⊗m
1
and its orthonormal basis
is formed by Slater determinants composed of m distinct
single-particle basis functions. Such Slater determinants
have the form |κ⟩= Dκ(z)/
√
m!, where
Dκ(z) = det
⎡
⎢⎢⎢⎢⎣
zκ1
1
zκ2
1
· · ·
zκm
1
zκ1
2
zκ2
2
· · ·
zκm
2
...
...
...
zκ1
m
zκ2
m
· · ·
zκm
m
⎤
⎥⎥⎥⎥⎦
,
and κ runs over strictly decreasing integer sequences of
length m that represent momenta of the occupied single-
particle states. The Vandermonde determinant formula
gives

1≤i<j ≤m
(zi −zj ) =
√
m! |τ⟩,
(4)
where
τ = (m −1, m −2, . . . , 1, 0).
Let Pν : Fm →Fm be a linear operator that maps a func-
tion (z) ∈Fm to Pν(z)(z). Note that Pν preserves Fm
since Pν(z) is a symmetric polynomial. We conclude that
polynomial Q(z) deﬁned in Eq. (3) describes a fermionic
m-particle (unnormalized) state
|Q⟩=
√
m! Pν|τ⟩.
(5)
The coeﬃcient of the monomial z(λ) in Q(z) coincides
with ⟨Dλ+τ|Q⟩/m!, where
λ + τ = (λ1 + τ1, . . . , λm + τm).
Indeed, Q(z) is antisymmetric under the exchange of any
pair of variables, while Dλ+τ(z)/m! is the antisymmetrized
version of the monomial z(λ) deﬁned in Eq. (2). Thus, the
Frobenius character formula can be expressed as
χλ(g) = ⟨Dλ+τ|Q⟩/m! = ⟨λ + τ|Pν|τ⟩.
(6)
The next step is to rewrite Eq. (6) using the fermionic
second quantization formalism. To this end, consider an
inﬁnite chain of qubits labeled by integers k ∈Z. Let
Xk, Yk, Zk be the Pauli operators acting on the kth qubit.
Deﬁne a fermionic annihilation operator
ak = 1
2(Xk + iYk)

j <k
Zj ,
(7)
and let a†
k be the corresponding creation operator. Here
we used the Jordan-Wigner fermion-to-qubit mapping. The
operators ak, a†
k obey the Fermi-Dirac commutation rules,
that is, aiaj = −aj ai and aia†
j + a†
j ai = δi,j I for all i, j . Let
H be the Hilbert space of the chain. It has basis vectors |x⟩,
where x ∈{0, 1}Z is a bit string with a ﬁnite support.
Given a ﬁnite strictly decreasing integer sequence κ,
let xκ ∈{0, 1}Z be a bit string with support κ. The Slater
determinant basis state |κ⟩= Dκ(z)/
√
m! in the ﬁrst quan-
tization is represented by state |xκ⟩∈H in the second
quantization.
Multiplication of a wave function by the polynomial
m
j =1 zℓ
j in the ﬁrst quantization picture shifts the momen-
tum of each particle by ℓ. Such a shift is described by an
operator
Jℓ=

k∈Z
a†
k+ℓak
(8)
in the second quantization picture. Following Ref. [13],
we refer to Jℓas the current operator. Now the Frobenius
character formula can be expressed as
χλ(g) = ⟨xλ+τ|
c(g)

j =1
Jνj |xτ⟩.
(9)
The order in the product does not matter since the cur-
rent operators pairwise commute. At this point we have
mapped Sn characters to an inﬁnite spin chain. We can trun-
cate the chain to a block of 2n consecutive qubits using the
following lemma.
Lemma 1. Suppose that x, y ∈{0, 1}Z are bit strings and
that i∗is an integer such that xi = yi for i ≤i∗. Let x′, y′
be bit strings obtained from x, y, respectively, by setting to
zero all bits i ≤i∗. Then
⟨y|
c(g)

j =1
Jνj |x⟩= ⟨y′|
c(g)

j =1
Jνj |x′⟩.
(10)
Proof. Let ˜Jℓ= 
k>i∗a†
k+ℓak. One can easily check
that
c(g)

j =1
Jνj |x⟩=
c(g)

j =1
˜Jνj |x⟩+ |φ⟩,
where |φ⟩∈H is a superposition of basis vectors |z⟩such
that zi = 0 and xi = 1 for at least one qubit i ≤i∗(in the
case that no sites i ≤i∗are occupied, |φ⟩is 0). By assump-
tion, xi = yi for all i ≤i∗. Thus, |φ⟩is orthogonal to |y⟩,
that is,
⟨y|
c(g)

j =1
Jνj |x⟩= ⟨y|
c(g)

j =1
˜Jνj |x⟩.
(11)
Since ˜Jνj acts trivially on qubits i ≤i∗, we also have
⟨y|
c(g)

j =1
˜Jνj |x⟩= ⟨y′|
c(g)

j =1
˜Jνj |x′⟩.
(12)
Applying Eq. (11) again with x′, y′ instead of x, y proves
Eq. (10).
■
As a consequence of Lemma 1, the matrix element in
Eq. (9) does not change if we set m = n and pad λ with
n −m zeros on the right. Accordingly, we can set
τ = (n −1, n −2, . . . , 1, 0).
It is immediate that any qubit i < 0 or i ≥2n is set
to |0⟩in the initial state |xτ⟩. Note that c(g)
j =1 Jνj can
only move a fermion at most n sites to the right. Thus,
qubits i < 0 and i ≥2n are unchanged in the simulation
and can be removed. This leaves only 2n active qubits
i = 0, 1, . . . , 2n −1. After this truncation the initial basis
state |xτ⟩is mapped to |1n0n⟩, while the ﬁnal basis state
xλ+τ is mapped to a weight-n bit string with support
{λ1 + n −1, λ2 + n −2, . . . , 0} [29]. Now the Frobenius
character formula becomes
χλ(g) = ⟨xλ+τ|
c(g)

j =1
Jνj |1n0n⟩,
(13)
where
Jℓ=
2n−1−ℓ

k=0
a†
k+ℓak.
(14)
This concludes the derivation of the Crichigno and Prakash
mapping from characters of Sn to a quantum spin chain.
As pointed out in Ref. [13], state |ψg⟩= c(g)
j =1 Jνj |1n0n⟩
has support only on bit strings encoding partitions of n.
This can be seen as follows. Let x = (x0, x1, . . . , x2n−1)
be a bit string of length 2n. Let |x| = 2n−1
j =0 xj be the
weight of x and m(x) = 2n−1
j =0 jxj be the momentum
of x. For example, m(1n0n) = n−1
j =0 j = n(n −1)/2. We
claim that x encodes a partition of n if and only if x has
weight n and momentum n(n + 1)/2. Indeed, suppose that
x = xλ+τ for some partition λ ⊢n. Then x has weight
n since we agreed that λ has n parts (including the
padded zero parts). By deﬁnition, x has support {λj + n −
j }j =1,...,n. From n
j =1 λj = n one gets
m(x) =
n

j =1
(λj + n −j ) = n(n + 1)/2.
Conversely, suppose that x has weight n and momentum
n(n + 1)/2. Let 2n −1 ≥d1 > d2 > · · · > dn ≥0 be the
indices of nonzero bits of x. Set λj = j + dj −n for j =
1, . . . , n. From dj > dj −1 one gets n ≥λ1 ≥· · · ≥λn ≥0.
Also, we have n
j =1 dj = m(x), that is,
n

j =1
λj = m(x) −n(n −1)/2 = n.
Thus, λ is a partition of n.
Clearly, the current operators Jνj preserve the weight of
bit strings. Each application of Jνj increases the momen-
tum by νj . Since the c(g)
j =1 νj = n and the initial bit
string 1n0n has momentum n(n −1)/2, the ﬁnal state is a
superposition of bit strings with weight n and momentum
n(n −1)/2 + n = n(n + 1)/2. As shown above, these are
exactly the bit strings encoding partitions of n.
