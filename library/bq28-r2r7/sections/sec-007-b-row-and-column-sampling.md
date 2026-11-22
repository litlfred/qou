---
doc_id: bq28-r2r7
doc_title: "Classical and Quantum Algorithms for Characters of the Symmetric Group"
section_id: sec-007-b-row-and-column-sampling
section_title: "B.. Row and column sampling"
section_number: null
pages: 11-12
source_pdf: bq28-r2r7.pdf
source_sha256: 38419a88531ebce7
toc_source: outline
doc_brief: "Classical and Quantum Algorithms for Characters of the Symmetric Group — 12 sections: Front matter; I.. INTRODUCTION; II.. GROUP THEORY REFRESHER"
---
We have already seen that the column sampling prob-
lem obeys properties (1) and (2). Furthermore, computing
the probability Pλ(g) = |χλ(g)|2/n! is #P-hard in the worst
case [4]. Moreover, this problem is not contained in #P
unless the polynomial hierarchy collapses to the second
level [4]. However, it seems unlikely that average-case
hardness property (3) holds for this problem. In particu-
lar, the following lemma gives a classical quasipolynomial
time algorithm for computing Pλ(g) that succeeds with
high probability if g ∈Sn is a random permutation.
Lemma 5. There exists a classical algorithm that takes
as input an irrep λ of the symmetric group Sn, a permuta-
tion g ∈Sn, and outputs an integer k(g) such that k(g) =
χλ(g) for at least a 1 −1/n100 fraction of permutations
g ∈Sn. The algorithm has runtime nO(log n).
Proof. The proof combines the MPS algorithm of Sec.
IV for computing characters of Sn with tail bounds for the
number of cycles in a random permutation. We use the
algorithm from Sec. IV with zero truncation error (ϵ = 0).
With input λ ⊢n and g ∈Sn, this algorithm computes
an MPS |ψg⟩of bond dimension (17) that can be upped
bounded as D ≤(n + 2)c(g), where c(g) is the number of
cycles in g. Recall that computing this MPS and extracting
the amplitude χλ(g) uses a runtime upper bounded as
O(n2D3) = nO[c(g)].
This runtime is exponential in n in the worst case since
the number of cycles c(g) can be linear in n. However,
we are only interested in the average case, that is, ran-
dom permutations. Furthermore, random permutations are
known to have only a few cycles with high probability. The
following fact is a special case of Theorem 1.7 of Ref. [41].
Fact 1. Suppose that g ∈Sn is picked uniformly at ran-
dom. Let c(g) be the number of cycles in g. Then, for all
ℓ≥1, one has
Pr[c(g) ≥1 + ℓHn] ≤2e1−[ℓlog (ℓ)−ℓ+1]Hn,
(39)
where Hn = n
j =1 1/j = log (n) + O(1) is the nth har-
monic number and e = 2.718 28 . . ..
Corollary 1. There exists a constant B > 0 such that
the fraction of permutations g ∈Sn with c(g) > B log (n)
cycles is at most 1/n100 for all large enough n.
If c(g) ≤B log n, use the MPS algorithm to compute
χλ(g), which takes time nO(log n). Otherwise, if c(g) >
B log n, output some ﬁxed integer (say zero). This gives
the desired algorithm.
■
Next let us consider the row sampling problem.
Lemma 5 suggests that classically hard instances of the
problem can be constructed by choosing the input permu-
tation g ∈Sn with a large number of cycles, for example,
c(g) ∼√n. In this case best-known classical algorithms
for computing the characters χλ(g) appear to require an
exponential time. However, we need to check whether per-
mutations g with a large number of cycles give rise to
instances of the row sampling problem with a granular
distribution. This is addressed in the following lemma.
Lemma 6 (Granularity for row sampling). There exist a
universal constant A > 0 such that the probability distribu-
tion Pg(λ) over partitions λ ⊢n from Eq. (28) is granular
whenever g ∈Sn is a permutation with at most A√n/ log n
cycles.
Proof. Let n be the set of partitions λ ⊢n (our sample
space). We can write
Pg(λ) = γ |χλ(g)|2
|n|
,
γ = |n|
|Eg| ,
(40)
where Eg is the centralizer of g. Since χλ(g) is integer for
all λ ∈n, distribution Pg(λ) is granular whenever γ ≥1.
Suppose that g consists of aℓcycles of length ℓ. Then
|Eg| is given by Eq. (21). Also, it is known [42] that
|n| ≥eA√n for some universal constant A > 0 (one can
choose A = π√2/3 −ϵ for any constant ϵ > 0) and all
suﬃciently large n. Thus,
γ >
eA√n
n
ℓ=1 ℓaℓaℓ!.
(41)
Since aℓ! ≤(aℓ)aℓ, one gets
γ ≥exp

A√n −
n

ℓ=1
aℓlog (ℓaℓ)

.
(42)
From Eq. (32) one gets ℓaℓ≤n. Using this along with
c(g) = n
ℓ=1 aℓgives
γ ≥exp [A√n −c(g) log n].
(43)
Thus, γ ≥1 whenever A√n −c(g) log n ≥0.
■
We conclude that the row sampling problem for per-
mutations g with A√n/ log n or less cycles obeys proper-
ties (1) and (2). Proving or disproving property (3)—the
average-case hardness of computing Pg(λ) for random
partitions λ ⊢n—is left as a challenge for future work.
The proposed reduction from strong-to-weak simulation
may apply to sampling tasks unrelated to the symmetric
group. As a concrete example, consider a sampling ver-
sion of the commuting local Hamiltonian problem [43].
Suppose that m ≥n are integers and that H1, . . . , Hm are
pairwise commuting n-qubit projectors such that each pro-
jector acts nontrivially only on a few qubits. Hamiltonians
composed of few-qubit commuting projectors are often
used as toy models of the topological quantum order [44].
Given a bit string x ∈{0, 1}m, let Lx be the subspace
spanned by n-qubit states ψ such that Ha|ψ⟩= xa|ψ⟩for
all a = 1, . . . , m. Let dx be the dimension of Lx. Consider a
normalized probability distribution P(x) = dx/2n describ-
ing the joint eigenvalue measurement for the projectors
H1, . . . , Hm on the maximally mixed state of n qubits.
Since the sample space has size 2m, distribution P(x) has
granularity γ = 2m−n ≥1. A quantum computer can eﬃ-
ciently sample P(x) by measuring the projectors one by
one in some ﬁxed order. Assuming that the task of comput-
ing dimension dx for a random uniform x ∈{0, 1}m is not
contained in the class BPPNP, our strong-to-weak reduc-
tion implies that no BPP algorithm can sample distribution
P(x) with a small error. We note that a closely related task
of deciding whether dx > 0 for a given bit string x is a vari-
ant of the commuting local Hamiltonian problem that has
been studied by many authors [43,45–50].
