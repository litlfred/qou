---
doc_id: arxiv-2607.29018v1
doc_title: "The Aldous property for normal Cayley graphs on symmetric groups"
section_id: sec-005-4-proofs-of-theorem-and-corollary
section_title: "Proofs of Theorem and Corollary"
section_number: 4
pages: 11-12
source_pdf: 2607.29018v1.pdf
source_sha256: 789faa122dd32290
toc_source: inferred
doc_brief: "The Aldous property for normal Cayley graphs on symmetric groups — Aldous’ spectral gap conjecture states that the random walk and the interchange process on any connected graph have the same"
---
Proof of Theorem 1.3. Let N0 be the positive integer in Lemma 2.1. Let N = max{N0, 5}
and n ≥N. Let S be a nonempty normal set in Sn such that 2 ≤|supp(σ)| ≤n −2 for all
σ ∈S. Since S is normal, ⟨S⟩is a nontrivial normal subgroup of Sn and hence is either Sn
or An. Since Cay(Sn, S) is normal, by (6), its eigenvalue corresponding to a partition β ⊢n
is
λβ =
X
σ∈S
˜χβ(σ).
(a) Assume first that O(S) = ∅. Then S ⊆An and hence ⟨S⟩= An. Thus Cay(Sn, S) is
disconnected with two isomorphic connected components. Consequently, the largest eigen-
value |S| of Cay(Sn, S) has multiplicity 2 and is attained by both ρ(n) and ρ(1n). Therefore,
the strictly second largest eigenvalue of Cay(Sn, S) can be expressed as
max
β⊢n
β /∈{(n),(1n)}
λβ =
max
β⊢n
β /∈{(n),(1n)}
 X
σ∈S
˜χβ(σ)
!
.
(8)
By Lemma 2.1, the maximum on the right-hand side of (8) is attained by β = (n −1, 1).
Therefore, Cay(Sn, S) has the Aldous property.
Now assume that E(S) = ∅. Then every permutation in S is odd, and hence ⟨S⟩= Sn.
Therefore, Cay(Sn, S) is connected, and its largest eigenvalue |S| has multiplicity 1 and
is attained by the trivial representation ρ(n).
Furthermore, the eigenvalue of Cay(Sn, S)
corresponding to the sign representation ρ(1n) is −|S|. So, by the Perron–Frobenius theorem
[15, Theorem 8.4.4], −|S| is the smallest eigenvalue of Cay(Sn, S). Therefore, the strictly
second largest eigenvalue of Cay(Sn, S) is again given by (8). Again, by Lemma 2.1, the
maximum on the right-hand side of (8) is attained by β = (n−1, 1) and therefore Cay(Sn, S)
has the Aldous property.
(b) Assume that E(S)̸ = ∅and O(S)̸ = ∅.
Then ⟨S⟩= Sn and hence Cay(Sn, S)
is connected. The largest eigenvalue |S| of Cay(Sn, S) has multiplicity 1 and is attained
by the trivial representation ρ(n). The eigenvalue of Cay(Sn, S) corresponding to the sign
representation ρ(1n) is
λ(1n) =
X
σ∈E(S)
˜χ(1n)(σ) +
X
σ∈O(S)
˜χ(1n)(σ) = |E(S)| −|O(S)|.
(9)
We have
max
β⊢n
β /∈{(n),(1n)}
λβ =
max
β⊢n
β /∈{(n),(1n)}
 X
σ∈S
˜χβ(σ)
!
.
(10)
By Lemma 2.1, the maximum on the right-hand side of (10) is attained by β = (n −1, 1).
Thus,
λ2(Cay(Sn, S)) = max{λ(n−1,1), λ(1n)}.
(11)
11
It follows that Cay(Sn, S) has the Aldous property if and only if λ(n−1,1) ≥λ(1n). Since
λ(1n) = |E(S)| −|O(S)| and
λ(n−1,1) =
X
σ∈S
˜χ(n−1,1)(σ) =
X
σ∈S
|fix(σ)| −1
n −1
,
we obtain that Cay(Sn, S) has the Aldous property if and only if
X
σ∈S
|fix(σ)| −1
n −1
≥|E(S)| −|O(S)|,
or, equivalently,
X
σ∈S
|fix(σ)| ≥n|E(S)| −(n −2)|O(S)|.
Moreover, by (11), if Cay(Sn, S) does not have the Aldous property, then its strictly second
largest eigenvalue is attained by the sign representation ρ(1n) of Sn.
Proof of Corollary 1.5. Let N ≥5 be the positive integer in Theorem 1.3. Let n ≥N, and
let S be a nonempty normal set in Sn such that S ⊆An and 2 ≤|supp(σ)| ≤n −2 for every
σ ∈S.
Since S ⊆An, part (a) of Theorem 1.3 implies that Cay(Sn, S) has the Aldous property.
Hence its strictly second largest eigenvalue is attained by ρ(n−1,1). As Cay(Sn, S) is normal,
(6) and Table 1 show that this eigenvalue is
λ(n−1,1) =
X
σ∈S
˜χ(n−1,1)(σ) =
X
σ∈S
|fix(σ)| −1
n −1
=
1
n −1
 X
σ∈S
|fix(σ)| −|S|
!
.
Since S is a nonempty normal set consisting of nonidentity elements, ⟨S⟩is a nontrivial
normal subgroup of Sn. Moreover, ⟨S⟩⊆An. As n ≥5, it follows that ⟨S⟩= An. Therefore,
Cay(Sn, S) has exactly two connected components, induced on An and Sn \ An, respectively,
and each component is isomorphic to Cay(An, S).
