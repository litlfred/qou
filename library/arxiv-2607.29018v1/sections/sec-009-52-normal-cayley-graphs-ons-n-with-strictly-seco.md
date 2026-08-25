---
doc_id: arxiv-2607.29018v1
doc_title: "The Aldous property for normal Cayley graphs on symmetric groups"
section_id: sec-009-52-normal-cayley-graphs-ons-n-with-strictly-seco
section_title: "Normal Cayley graphs onS n with strictly second largest eigen-"
section_number: 5.2
pages: 17-19
source_pdf: 2607.29018v1.pdf
source_sha256: 789faa122dd32290
doc_brief: "The Aldous property for normal Cayley graphs on symmetric groups — Aldous’ spectral gap conjecture states that the random walk and the interchange process on any connected graph have the same"
---
value at most1
Acocktail party graphis a graph obtained from a complete graph with even order by deleting
a perfect matching. In 2010, Stani´ c [31] obtained the following complete classification of
connected regular graphs with the second largest eigenvalue at most 1.
Theorem 5.4(cf. [31, Theorem 3.1]).Every connected regular graph with the second largest
eigenvalue at most1is the complement of a (not necessarily connected) regular graph, where
each connected component is either a connected regular line graph, a cocktail party graph, or
one of the 187 exceptional connected regular graphs with order from 8 to 28 and degree from
3 to 16 described in [10, pp. 213–227].
Using Theorems 5.4 and 5.1, we obtain the following classification of normal Cayley graphs
onS n with strictly second largest eigenvalue at most 1.
17
Theorem 5.5.Letn≥5, and letSbe a nonempty normal set inS n. Then the strictly
second largest eigenvalue ofCay(S n,S)is at most1if and only if one of the following holds:
(a)S=S n\{e}, and henceCay(S n,S) ∼=Kn!;
(b)S=S n\A n, and henceCay(S n,S) ∼=Kn!/2,n!/2;
(c)S=A n\{e}, and henceCay(S n,S) ∼= 2Kn!/2.
Proof.Letn≥5 andSbe a nonempty normal set inS n. IfS=S n\{e},S n\A n or
An\{e}, then Cay(Sn,S) ∼=Kn!,Kn!/2,n!/2 or 2Kn!/2, respectively. Note thatK n! has distinct
eigenvaluesn!−1 and−1,K n!/2,n!/2 has distinct eigenvaluesn!/2, 0 and−n!/2, and 2K n!/2 has
distinct eigenvaluesn!/2−1 and−1. In all three cases, the strictly second largest eigenvalue
of Cay(Sn,S) is at most 1. This proves the sufficiency.
We now prove the necessity. Suppose that the strictly second largest eigenvalue of
Cay(Sn,S) is at most 1.
Case 1.Cay(S n,S) is connected.
In this case, we have⟨S⟩=S n. SinceSis a normal set inS n, so isS c = (Sn\{e})\S,
and hence⟨S c⟩is a normal subgroup ofS n. Asn≥5, we have⟨S c⟩={e},A n orS n. If
⟨Sc⟩={e}, thenS c =∅, soS=S n\{e}and Cay(S n,S) ∼=Kn!.
Assume that⟨S c⟩is eitherA n orS n. Sincen≥5, every connected component of
Cay(Sn,Sc) has at least 5!/2 = 60 vertices. Sinceλ 2(Cay(Sn,S))≤1, by Theorem 5.4, each
connected component of Cay(Sn,Sc) is either a regular line graph, a cocktail party graph, or
one of the 187 exceptional connected regular graphs. But all these exceptional graphs have
at most 28 vertices, so none of them can be a connected component of Cay(S n,Sc).
Suppose that some connected component of Cay(S n,Sc) is a cocktail party graph. Then
the complement of the subgraph of Cay(Sn,Sc) induced by⟨S c⟩is 1-regular. HenceS c omits
exactly one nonidentity element of⟨S c⟩. SinceS c is a union of conjugacy classes ofS n, this
would give a conjugacy class of size 1 inS n other than{e}, contradicting the fact that the
center ofS n is trivial forn≥5. Therefore, no connected component of Cay(S n,Sc) is a
cocktail party graph.
Thus every connected component of Cay(S n,Sc) is a regular line graph. Since a disjoint
union of line graphs is again a line graph, Cay(S n,Sc) is itself a line graph. It follows from
Theorem 5.1 that eitherS c =S n\{e}orS c =A n\{e}. The former is impossible since it
would implyS=∅. Thus, the only possibility is thatS c =A n\{e}. HenceS=S n\An and
therefore Cay(Sn,S) ∼=Kn!/2,n!/2.
Case 2.Cay(S n,S) is disconnected.
In this case, we have⟨S⟩=A n. SetS ∗ = (A n\{e})\S.Then Cay(A n,S∗) is the
complement of Cay(An,S). IfS ∗ =∅, thenS=A n\{e}, and hence Cay(S n,S) ∼= 2Kn!/2.
Assume thatS ∗̸=∅. SinceSis a normal set inS n,S ∗ is a union of conjugacy classes
of bothS n andA n. SinceA n is simple forn≥5, the nonempty normal setS ∗ generates
An, and hence Cay(An,S∗) is connected. Asλ 2(Cay(An,S))≤1, Theorem 5.4 implies that
18
Cay(An,S∗) is either a regular line graph, a cocktail party graph, or one of the 187 exceptional
connected regular graphs. The same arguments as in Case 1 show that it is neither a cocktail
party graph nor an exceptional graph. Hence Cay(A n,S∗) must be a line graph. Therefore,
Cay(Sn,S∗), which is the disjoint union of two copies of Cay(A n,S∗), is also a line graph.
Moreover,S ∗ is a union of conjugacy classes ofS n. Therefore, by Theorem 5.1, we have
eitherS ∗ =S n\{e}orS ∗ =A n\{e}. SinceS ∗⊆A n, it follows thatS ∗ =A n\{e}. This
forcesS=∅, contradicting the fact that⟨S⟩=A n.
