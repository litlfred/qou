---
doc_id: arxiv-2607.29018v1
doc_title: "The Aldous property for normal Cayley graphs on symmetric groups"
section_id: sec-005-3-proof-of-theorem-12
section_title: "Proof of Theorem 1.2"
section_number: 3
pages: 8-11
source_pdf: 2607.29018v1.pdf
source_sha256: 789faa122dd32290
doc_brief: "The Aldous property for normal Cayley graphs on symmetric groups — Aldous’ spectral gap conjecture states that the random walk and the interchange process on any connected graph have the same"
---
Proof of Theorem 1.2.Letn≥5, and letSbe a nonempty normal set inS n withS̸=S n\{e}.
Assume first that eitherSorS c is equal toA n\{e}. Without loss of generality, we may
assume thatS=A n\{e}. Then Cay(S n,S) ∼= 2Kn!/2 has spectrum
{(
n!
2−1
)2
,(−1)n!−2
}
.
The eigenvalue n!
2 −1 is attained by bothρ (n) andρ (1n), while the strictly second largest
eigenvalue−1 is attained byρ (n−1,1). SinceS c =S n\A n, we have Cay(Sn,Sc)∼= Kn!/2,n!/2,
and its spectrum is
{(
n!
2
)1
,0n!−2,
(
−n!
2
)1}
,with the largest eigenvalue n!
2 and the smallest
eigenvalue− n!
2 attained byρ (n) andρ (1n), respectively. The strictly second largest eigenvalue
of Cay(Sn,Sc) is 0, which is attained byρ (n−1,1). Therefore, both Cay(Sn,S) and Cay(Sn,Sc)
have the Aldous property.
From now on, assume that neitherSnorS c is equal toA n\{e}. We aim to show that at
most one of Cay(Sn,S) and Cay(S n,Sc) has the Aldous property. Without loss of generality,
8
assume that Cay(S n,S) has the Aldous property. We prove under this assumption that
Cay(Sn,Sc) does not have the Aldous property.
The union of Cay(Sn,S) and Cay(S n,Sc) is the complete graph Cay(Sn,Sn\{e})∼=Kn!,
which has eigenvaluen!−1 with multiplicity 1 attained by the trivial representationρ (n), and
eigenvalue−1 with multiplicityn!−1 attained by all nontrivial irreducible representations
ofS n. Therefore, by (6), for each (n)̸=ζ⊢n,
λζ(Cay(Sn,S))+λ ζ(Cay(Sn,Sc)) =
∑
σ∈S
˜χζ(σ)+
∑
σ∈S c
˜χζ(σ) =λ ζ(Cay(Sn,Sn\{e})) =−1.(7)
Sincen≥5, the alternating groupA n is the only non-trivial proper normal subgroup of
Sn. SinceSandS c are nonempty normal sets, the subgroups⟨S⟩and⟨S c⟩are normal in
Sn, leavingA n andS n as the only possibilities. However,⟨S⟩and⟨S c⟩cannot both beA n,
for otherwise we would haveS∪S c⊆A n, which contradictsS∪S c =S n\{e}. Therefore,
exactly one of the following three cases must occur.
Case 1.⟨S⟩=S n and⟨S c⟩=S n.
In this case, both Cay(Sn,S) and Cay(Sn,Sc) are connected, and their largest eigenvalues
are attained by the trivial representationρ (n). Since both graphs have diameter at least 2,
it follows from [14, Lemma 8.12.1] that each has at least three distinct eigenvalues. Since
Cay(Sn,S) has the Aldous property by our assumption, its strictly second largest eigenvalue
isλ (n−1,1)(Cay(Sn,S)). Letλ β(Cay(Sn,S)) be the smallest eigenvalue of Cay(S n,S), where
β⊢nsatisfiesβ /∈{(n),(n−1,1)}. Then
λ(n−1,1)(Cay(Sn,S))>λ β(Cay(Sn,S)).
This together with (7) yields
λβ(Cay(Sn,Sc)) =−λ β(Cay(Sn,S))−1
>−λ (n−1,1)(Cay(Sn,S))−1
=λ (n−1,1)(Cay(Sn,Sc)).
Therefore, Cay(Sn,Sc) does not have the Aldous property.
Case 2.⟨S⟩=S n and⟨S c⟩=A n.
In this case, Cay(Sn,S) is connected, and Cay(Sn,Sc) is disconnected with two isomorphic
connected components. The largest eigenvalue|S|of Cay(S n,S) has multiplicity 1 and is
attained byρ (n). The largest eigenvalue|S c|of Cay(S n,Sc) has multiplicity 2 and is attained
by bothρ (n) andρ (1n).
SinceS̸=S n\{e}, Cay(S n,S) has diameter at least 2. So, by [14, Lemma 8.12.1],
Cay(Sn,S) has at least three distinct eigenvalues. Since Cay(S n,S) has the Aldous property
by our assumption, its strictly second largest eigenvalue isλ (n−1,1)(Cay(Sn,S)).
By (7), among all partitionsζ⊢nwithζ̸= (n), any representation attaining the largest
eigenvalue of Cay(Sn,Sc) also attains the smallest eigenvalue of Cay(Sn,S). Since the largest
9
eigenvalue|S c|of Cay(S n,Sc) is attained byρ (1n), it follows that the smallest eigenvalue of
Cay(Sn,S) is attained by the sign representationρ (1n).
If Cay(Sn,S) has at least four distinct eigenvalues, then there existsβ⊢nwithβ /∈
{(n),(n−1,1),(1 n)}such that
λ(n−1,1)(Cay(Sn,S))>λ β(Cay(Sn,S))>λ (1n)(Cay(Sn,S)).
This together with (7) implies that
λβ(Cay(Sn,Sc)) =−λ β(Cay(Sn,S))−1
>−λ (n−1,1)(Cay(Sn,S))−1
=λ (n−1,1)(Cay(Sn,Sc)).
Hence Cay(Sn,Sc) does not have the Aldous property.
If Cay(Sn,S) has exactly three distinct eigenvalues, then by (7) there are exactly two
distinct values among the eigenvaluesλ β(Cay(Sn,Sc)) withβ̸= (n). As mentioned above,
λ(n)(Cay(Sn,Sc)) =λ (1n)(Cay(Sn,Sc)).Therefore, Cay(Sn,Sc) has exactly two distinct eigen-
values. Thus Cay(S n,Sc) is the disjoint union of two cliques, which forcesS c =A n\{e},
contradicting our assumption.
Case 3.⟨S⟩=A n and⟨S c⟩=S n.
In this case, Cay(Sn,S) is disconnected with two isomorphic connected components, and
Cay(Sn,Sc) is connected. The largest eigenvalue|S|of Cay(S n,S) has multiplicity 2 and is
attained by bothρ (n) andρ (1n). The largest eigenvalue|S c|of Cay(S n,Sc) has multiplicity 1
and is attained byρ (n).
SinceS̸=A n\{e}, Cay(S n,S) is not the disjoint union of two cliques. Hence each
connected component of Cay(Sn,S) has diameter at least 2. Again, by [14, Lemma 8.12.1],
Cay(Sn,S) has at least three distinct eigenvalues. Since Cay(S n,S) has the Aldous prop-
erty by our assumption, its strictly second largest eigenvalue isλ (n−1,1)(Cay(Sn,S)). Let
λβ(Cay(Sn,S)) be the smallest eigenvalue of Cay(S n,S), whereβ⊢nsatisfiesβ /∈{(n),(n−
1,1),(1 n)}. Then
λ(n−1,1)(Cay(Sn,S))>λ β(Cay(Sn,S)).
Combining this with (7), we obtain that
λβ(Cay(Sn,Sc)) =−λ β(Cay(Sn,S))−1
>−λ (n−1,1)(Cay(Sn,S))−1
=λ (n−1,1)(Cay(Sn,Sc)).
Hence Cay(Sn,Sc) does not have the Aldous property.
This proves Theorem 1.2.
10
