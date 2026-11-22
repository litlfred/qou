---
doc_id: arxiv-2607.29018v1
doc_title: "The Aldous property for normal Cayley graphs on symmetric groups"
section_id: sec-004-3-proof-of-theorem
section_title: "Proof of Theorem"
section_number: 3
pages: 8-11
source_pdf: 2607.29018v1.pdf
source_sha256: 789faa122dd32290
toc_source: inferred
doc_brief: "The Aldous property for normal Cayley graphs on symmetric groups — Aldous’ spectral gap conjecture states that the random walk and the interchange process on any connected graph have the same"
---
Lemma 2.1 (cf. [27, Proposition 2.3]). There exists a positive integer N0 such that for every
n ≥N0 and any γ ⊢n with |fix(γ)| ≥2, we have
max
ζ⊢n
ζ /∈{(n),(1n)}
˜χζ(γ) = ˜χ(n−1,1)(γ).
3
Proof of Theorem 1.2
Proof of Theorem 1.2. Let n ≥5, and let S be a nonempty normal set in Sn with S̸ = Sn\{e}.
Assume first that either S or Sc is equal to An \ {e}. Without loss of generality, we may
assume that S = An \ {e}. Then Cay(Sn, S) ∼= 2Kn!/2 has spectrum

n!
2 −1
2 , (−1)n!−2

.
The eigenvalue n!
2 −1 is attained by both ρ(n) and ρ(1n), while the strictly second largest
eigenvalue −1 is attained by ρ(n−1,1). Since Sc = Sn \ An, we have Cay(Sn, Sc) ∼= Kn!/2,n!/2,
and its spectrum is

n!
2
1 , 0n!−2,

−n!
2
1
, with the largest eigenvalue n!
2 and the smallest
eigenvalue −n!
2 attained by ρ(n) and ρ(1n), respectively. The strictly second largest eigenvalue
of Cay(Sn, Sc) is 0, which is attained by ρ(n−1,1). Therefore, both Cay(Sn, S) and Cay(Sn, Sc)
have the Aldous property.
From now on, assume that neither S nor Sc is equal to An \ {e}. We aim to show that at
most one of Cay(Sn, S) and Cay(Sn, Sc) has the Aldous property. Without loss of generality,
8
assume that Cay(Sn, S) has the Aldous property.
We prove under this assumption that
Cay(Sn, Sc) does not have the Aldous property.
The union of Cay(Sn, S) and Cay(Sn, Sc) is the complete graph Cay(Sn, Sn \ {e}) ∼= Kn!,
which has eigenvalue n!−1 with multiplicity 1 attained by the trivial representation ρ(n), and
eigenvalue −1 with multiplicity n! −1 attained by all nontrivial irreducible representations
of Sn. Therefore, by (6), for each (n)̸ = ζ ⊢n,
λζ(Cay(Sn, S))+λζ(Cay(Sn, Sc)) =
X
σ∈S
˜χζ(σ)+
X
σ∈Sc
˜χζ(σ) = λζ(Cay(Sn, Sn\{e})) = −1. (7)
Since n ≥5, the alternating group An is the only non-trivial proper normal subgroup of
Sn. Since S and Sc are nonempty normal sets, the subgroups ⟨S⟩and ⟨Sc⟩are normal in
Sn, leaving An and Sn as the only possibilities. However, ⟨S⟩and ⟨Sc⟩cannot both be An,
for otherwise we would have S ∪Sc ⊆An, which contradicts S ∪Sc = Sn \ {e}. Therefore,
exactly one of the following three cases must occur.
Case 1. ⟨S⟩= Sn and ⟨Sc⟩= Sn.
In this case, both Cay(Sn, S) and Cay(Sn, Sc) are connected, and their largest eigenvalues
are attained by the trivial representation ρ(n). Since both graphs have diameter at least 2,
it follows from [14, Lemma 8.12.1] that each has at least three distinct eigenvalues. Since
Cay(Sn, S) has the Aldous property by our assumption, its strictly second largest eigenvalue
is λ(n−1,1)(Cay(Sn, S)). Let λβ(Cay(Sn, S)) be the smallest eigenvalue of Cay(Sn, S), where
β ⊢n satisfies β /∈{(n), (n −1, 1)}. Then
λ(n−1,1)(Cay(Sn, S)) > λβ(Cay(Sn, S)).
This together with (7) yields
λβ(Cay(Sn, Sc)) = −λβ(Cay(Sn, S)) −1
> −λ(n−1,1)(Cay(Sn, S)) −1
= λ(n−1,1)(Cay(Sn, Sc)).
Therefore, Cay(Sn, Sc) does not have the Aldous property.
Case 2. ⟨S⟩= Sn and ⟨Sc⟩= An.
In this case, Cay(Sn, S) is connected, and Cay(Sn, Sc) is disconnected with two isomorphic
connected components. The largest eigenvalue |S| of Cay(Sn, S) has multiplicity 1 and is
attained by ρ(n). The largest eigenvalue |Sc| of Cay(Sn, Sc) has multiplicity 2 and is attained
by both ρ(n) and ρ(1n).
Since S̸ = Sn \ {e}, Cay(Sn, S) has diameter at least 2.
So, by [14, Lemma 8.12.1],
Cay(Sn, S) has at least three distinct eigenvalues. Since Cay(Sn, S) has the Aldous property
by our assumption, its strictly second largest eigenvalue is λ(n−1,1)(Cay(Sn, S)).
By (7), among all partitions ζ ⊢n with ζ̸ = (n), any representation attaining the largest
eigenvalue of Cay(Sn, Sc) also attains the smallest eigenvalue of Cay(Sn, S). Since the largest
9
eigenvalue |Sc| of Cay(Sn, Sc) is attained by ρ(1n), it follows that the smallest eigenvalue of
Cay(Sn, S) is attained by the sign representation ρ(1n).
If Cay(Sn, S) has at least four distinct eigenvalues, then there exists β ⊢n with β /∈
{(n), (n −1, 1), (1n)} such that
λ(n−1,1)(Cay(Sn, S)) > λβ(Cay(Sn, S)) > λ(1n)(Cay(Sn, S)).
This together with (7) implies that
λβ(Cay(Sn, Sc)) = −λβ(Cay(Sn, S)) −1
> −λ(n−1,1)(Cay(Sn, S)) −1
= λ(n−1,1)(Cay(Sn, Sc)).
Hence Cay(Sn, Sc) does not have the Aldous property.
If Cay(Sn, S) has exactly three distinct eigenvalues, then by (7) there are exactly two
distinct values among the eigenvalues λβ(Cay(Sn, Sc)) with β̸ = (n). As mentioned above,
λ(n)(Cay(Sn, Sc)) = λ(1n)(Cay(Sn, Sc)). Therefore, Cay(Sn, Sc) has exactly two distinct eigen-
values. Thus Cay(Sn, Sc) is the disjoint union of two cliques, which forces Sc = An \ {e},
contradicting our assumption.
Case 3. ⟨S⟩= An and ⟨Sc⟩= Sn.
In this case, Cay(Sn, S) is disconnected with two isomorphic connected components, and
Cay(Sn, Sc) is connected. The largest eigenvalue |S| of Cay(Sn, S) has multiplicity 2 and is
attained by both ρ(n) and ρ(1n). The largest eigenvalue |Sc| of Cay(Sn, Sc) has multiplicity 1
and is attained by ρ(n).
Since S̸ = An \ {e}, Cay(Sn, S) is not the disjoint union of two cliques. Hence each
connected component of Cay(Sn, S) has diameter at least 2. Again, by [14, Lemma 8.12.1],
Cay(Sn, S) has at least three distinct eigenvalues. Since Cay(Sn, S) has the Aldous prop-
erty by our assumption, its strictly second largest eigenvalue is λ(n−1,1)(Cay(Sn, S)). Let
λβ(Cay(Sn, S)) be the smallest eigenvalue of Cay(Sn, S), where β ⊢n satisfies β /∈{(n), (n −
1, 1), (1n)}. Then
λ(n−1,1)(Cay(Sn, S)) > λβ(Cay(Sn, S)).
Combining this with (7), we obtain that
λβ(Cay(Sn, Sc)) = −λβ(Cay(Sn, S)) −1
> −λ(n−1,1)(Cay(Sn, S)) −1
= λ(n−1,1)(Cay(Sn, Sc)).
Hence Cay(Sn, Sc) does not have the Aldous property.
This proves Theorem 1.2.
10
4
