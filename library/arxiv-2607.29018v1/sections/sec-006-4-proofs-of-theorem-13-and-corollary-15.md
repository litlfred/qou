---
doc_id: arxiv-2607.29018v1
doc_title: "The Aldous property for normal Cayley graphs on symmetric groups"
section_id: sec-006-4-proofs-of-theorem-13-and-corollary-15
section_title: "Proofs of Theorem 1.3 and Corollary 1.5"
section_number: 4
pages: 11-12
source_pdf: 2607.29018v1.pdf
source_sha256: 789faa122dd32290
doc_brief: "The Aldous property for normal Cayley graphs on symmetric groups — Aldous’ spectral gap conjecture states that the random walk and the interchange process on any connected graph have the same"
---
Proof of Theorem 1.3.LetN 0 be the positive integer in Lemma 2.1. LetN= max{N 0,5}
andn≥N. LetSbe a nonempty normal set inS n such that 2≤|supp(σ)|≤n−2 for all
σ∈S. SinceSis normal,⟨S⟩is a nontrivial normal subgroup ofS n and hence is eitherS n
orA n. Since Cay(S n,S) is normal, by (6), its eigenvalue corresponding to a partitionβ⊢n
is
λβ =
∑
σ∈S
˜χβ(σ).
(a) Assume first thatO(S) =∅. ThenS⊆A n and hence⟨S⟩=A n. Thus Cay(Sn,S) is
disconnected with two isomorphic connected components. Consequently, the largest eigen-
value|S|of Cay(S n,S) has multiplicity 2 and is attained by bothρ (n) andρ (1n). Therefore,
the strictly second largest eigenvalue of Cay(S n,S) can be expressed as
max
β⊢n
β/∈{(n),(1n)}
λβ = max
β⊢n
β/∈{(n),(1n)}
(∑
σ∈S
˜χβ(σ)
)
.(8)
By Lemma 2.1, the maximum on the right-hand side of (8) is attained byβ= (n−1,1).
Therefore, Cay(Sn,S) has the Aldous property.
Now assume thatE(S) =∅. Then every permutation inSis odd, and hence⟨S⟩=S n.
Therefore, Cay(Sn,S) is connected, and its largest eigenvalue|S|has multiplicity 1 and
is attained by the trivial representationρ (n). Furthermore, the eigenvalue of Cay(S n,S)
corresponding to the sign representationρ (1n) is−|S|. So, by the Perron–Frobenius theorem
[15, Theorem 8.4.4],−|S|is the smallest eigenvalue of Cay(S n,S). Therefore, the strictly
second largest eigenvalue of Cay(S n,S) is again given by (8). Again, by Lemma 2.1, the
maximum on the right-hand side of (8) is attained byβ= (n−1,1) and therefore Cay(S n,S)
has the Aldous property.
(b) Assume thatE(S)̸=∅andO(S)̸=∅. Then⟨S⟩=S n and hence Cay(S n,S)
is connected. The largest eigenvalue|S|of Cay(S n,S) has multiplicity 1 and is attained
by the trivial representationρ (n). The eigenvalue of Cay(S n,S) corresponding to the sign
representationρ (1n) is
λ(1n) =
∑
σ∈E(S)
˜χ(1n)(σ) +
∑
σ∈O(S)
˜χ(1n)(σ) =|E(S)|−|O(S)|.(9)
We have
max
β⊢n
β/∈{(n),(1n)}
λβ = max
β⊢n
β/∈{(n),(1n)}
(∑
σ∈S
˜χβ(σ)
)
.(10)
By Lemma 2.1, the maximum on the right-hand side of (10) is attained byβ= (n−1,1).
Thus,
λ2(Cay(Sn,S)) = max{λ (n−1,1),λ (1n)}.(11)
11
It follows that Cay(S n,S) has the Aldous property if and only ifλ (n−1,1) ≥λ (1n). Since
λ(1n) =|E(S)|−|O(S)|and
λ(n−1,1) =
∑
σ∈S
˜χ(n−1,1)(σ) =
∑
σ∈S
|fix(σ)|−1
n−1 ,
we obtain that Cay(Sn,S) has the Aldous property if and only if
∑
σ∈S
|fix(σ)|−1
n−1 ≥|E(S)|−|O(S)|,
or, equivalently, ∑
σ∈S
|fix(σ)|≥n|E(S)|−(n−2)|O(S)|.
Moreover, by (11), if Cay(Sn,S) does not have the Aldous property, then its strictly second
largest eigenvalue is attained by the sign representationρ (1n) ofS n.
Proof of Corollary 1.5.LetN≥5 be the positive integer in Theorem 1.3. Letn≥N, and
letSbe a nonempty normal set inS n such thatS⊆A n and 2≤|supp(σ)|≤n−2 for every
σ∈S.
SinceS⊆A n, part (a) of Theorem 1.3 implies that Cay(S n,S) has the Aldous property.
Hence its strictly second largest eigenvalue is attained byρ (n−1,1). As Cay(S n,S) is normal,
(6) and Table 1 show that this eigenvalue is
λ(n−1,1) =
∑
σ∈S
˜χ(n−1,1)(σ) =
∑
σ∈S
|fix(σ)|−1
n−1 = 1
n−1
(∑
σ∈S
|fix(σ)|−|S|
)
.
SinceSis a nonempty normal set consisting of nonidentity elements,⟨S⟩is a nontrivial
normal subgroup ofS n. Moreover,⟨S⟩⊆A n. Asn≥5, it follows that⟨S⟩=A n. Therefore,
Cay(Sn,S) has exactly two connected components, induced onA n andS n\An, respectively,
and each component is isomorphic to Cay(A n,S).
