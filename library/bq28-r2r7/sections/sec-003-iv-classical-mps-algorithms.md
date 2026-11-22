---
doc_id: bq28-r2r7
doc_title: "Classical and Quantum Algorithms for Characters of the Symmetric Group"
section_id: sec-003-iv-classical-mps-algorithms
section_title: "IV.. CLASSICAL MPS ALGORITHMS"
section_number: null
pages: 5-7
source_pdf: bq28-r2r7.pdf
source_sha256: 38419a88531ebce7
toc_source: outline
doc_brief: "Classical and Quantum Algorithms for Characters of the Symmetric Group — 12 sections: Front matter; I.. INTRODUCTION; II.. GROUP THEORY REFRESHER"
---
Consider a permutation g ∈Sn. Let c(g) be the number
of cycles in g and νj be the length of the j th cycle. Our
strategy is to represent the 2n-qubit state
|ψg⟩=
c(g)

j =1
Jνj |1n0n⟩
(15)
by an MPS. To this end, we need the following lemma.
Lemma 2. The current operator Jℓis an MPO with bond
dimension ℓ+ 2.
Proof. Figure 1 deﬁnes a tensor T ∈C2 ⊗Cℓ+2 ⊗
Cℓ+2 ⊗C2, where C2 represents physical indices and Cℓ+2
represents virtual indices of the MPO. Taking 2n copies of
T and contracting all virtual indices (horizontal lines) as
shown in Fig. 1 gives an operator
2n−1−ℓ

j =0

0
1
0
0

j
Zj +1 · · · Zj +ℓ−1

0
0
1
0

j +ℓ
.
This is the current operator deﬁned in Eqs. (7) and (8).
■
The initial state |1n0n⟩is clearly an MPS with bond
dimension 1. Deﬁne a sequence of MPSs |φ0⟩= |1n0n⟩and
|φj ⟩= Compress(Jνj |φj −1⟩, ϵ)
(16)
for j = 1, . . . , c(g). Here Compress(|φ⟩, ϵ) is a function
that computes the canonical form of an MPS |φ⟩and trun-
cates the singular values (Schmidt coeﬃcients) at each site,
as discussed in Sec. 4.5.1 of Ref. [30]. The error toler-
ance ϵ ≥0 deﬁnes the maximum relative error incurred
while truncating singular values. More precisely, suppose
that s1 ≥s2 ≥· · · ≥sN are singular values of some MPS
FIG. 1.
MPO representation of the current operator Jℓ. Hor-
izontal lines represent virtual indices of dimension ℓ+ 2. We
label basis vectors of Cℓ+2 by integers {0, 1, . . . , ℓ+ 1}. The
MPO consists of 2n copies of T. We list all nonzero components
of tensor T.
|φj ⟩for some bipartite cut of the chain. We discard singu-
lar values si with i ≥d, where d is the smallest index such
that
N

i=d+1
si ≤ϵ
N

i=1
si.
We chose to impose a bound on the relative truncation error
since the considered states are unnormalized and some sin-
gular values si can be exponentially large. Let D = D(ϵ)
be the maximum bond dimension of all states |φj ⟩with
j ≤c(g). Lemma 2 ensures that
D ≤
c(g)

j =1
(νj + 2).
(17)
We do not expect this bound to be tight, even for lossless
compression, ϵ = 0. For example, one can easily check
that a state Jν1|1n0n⟩has a bond dimension of only ν1
instead of ν1 + 2 predicted by Eq. (17). We empirically
observed that the MPS bond dimension D at the compres-
sion error ϵ = 10−10 can be smaller than the upper bound
(17) by several orders of magnitude; see Fig. 3 below.
Since the cost of MPO-MPS multiplication and MPS
compression scales as O(nD3), an MPS representation of
|ψg⟩can be computed in time O(nc(g)D3) = O(n2D3). Let
|mpsg⟩= |φc(g)⟩
be the ﬁnal MPS approximating |ψg⟩. The character of any
irrep λ ⊢n can then be extracted by computing a single
amplitude of the ﬁnal MPS,
χλ(g) = ⟨xλ+τ|ψg⟩≈⟨xλ+τ|mpsg⟩.
(18)
This takes time O(nD3).
Suppose that one needs to compute MPS amplitudes
⟨xλ+τ|ψg⟩for all irreps λ. To speedup this computation,
we divided the spin chain into four blocks of length n/2
and cached products of the MPS tensors associated with
each block. As one iterates over irreps λ, a product of the
MPS tensors is retrieved from the cache, if available. We
observed that the runtime for computing MPS amplitudes
with the caching strategy described above is comparable or
smaller than the runtime for computing the MPS tensors.
Recall that Sn characters are integer valued. Thus, the
exact value of χλ(g) can be recovered by rounding the ﬁnal
MPS amplitude to the nearest integer as long as
|χλ(g) −⟨xλ+τ|mpsg⟩| < 1
2.
(19)
An error introduced by the compression can be estimated
by comparing the norm of the exact state |ψg⟩and the
approximating MPS. The orthogonality theorem for char-
acters [28] gives
∥ψg∥2 =

λ⊢n
χλ(g)2 = |Eg|,
(20)
where Eg = {h ∈Sn : hg = gh} is the centralizer of g.
Denoting the number of length-ℓcycles in g by aℓ, one
gets
|Eg| =
n

ℓ=1
(aℓ!)ℓaℓ.
(21)
We used the mpnum software [17] for numerical exper-
iments and set the compression error to ϵ = 10−10. The
runtime of the MPS algorithm is compared with the run-
time of two widely used computer algebra systems: GAP
[31] and the symmetrica library included in SAGE [32];
see Fig. 2.
For numerical experiments, we selected permutations
with a large number of short cycles that tend to be most
expensive for all considered algorithms. Namely, for each
n, we consider a single permutation g ∈Sn composed of
n/2 length-2 cycles. Figure 2 shows the measured runtime
for 10 ≤n ≤30. The reported runtimes include compu-
tation of the characters χλ(g) for all irreps λ ⊢n. In the
FIG. 2.
Runtime for computing the characters χλ(g) for per-
mutations g ∈Sn composed of n/2 length-2 cycles and all irreps
λ ⊢n. The MPS compression error is set to ϵ = 10−10 for all the
data.
case of the MPS the runtime additionally includes comput-
ing state |mpsg⟩. As one can see from the plot, the MPS
algorithm shows a competitive performance for large val-
ues of n. We note that our implementation is in PYTHON,
while SAGE and GAP have a kernel written in C, which
tends to be much faster than PYTHON.
Recall that our MPS algorithm computes character
χλ(g) with the zero error as long as the MPS amplitude
⟨xλ+τ|mpsg⟩obeys Eq. (19). We found that
|χλ(g) −⟨xλ+τ|mpsg⟩| ≤10−6
FIG. 3.
Comparison between the observed maximum MPS
bond dimension for the problem instances reported in Fig. 2
(blue) and the upper bound (17) (green).
for all problem instances reported at Fig. 2 [the exact value
of χλ(g) was computed using the SAGE library]. This
is many orders of magnitude smaller than the required
precision 1/2, suggesting that the MPS runtime may be
improved further by truncating more singular values. Our
PYTHON implementation of the MPS algorithm is avail-
able from GitHub [33]. We provide two versions of the
algorithm that use the mpnum or quimb libraries for
MPO-MPS manipulations.
Finally, for each problem instance presented in Fig. 2,
we computed the maximum MPS bond dimension and
compared it with the upper bound (17). This comparison
is reported in Fig. 3.
