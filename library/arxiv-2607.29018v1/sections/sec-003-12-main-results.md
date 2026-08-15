---
doc_id: arxiv-2607.29018v1
doc_title: "The Aldous property for normal Cayley graphs on symmetric groups"
section_id: sec-003-12-main-results
section_title: "Main results"
section_number: 1.2
pages: 4-7
source_pdf: 2607.29018v1.pdf
source_sha256: 789faa122dd32290
doc_brief: "The Aldous property for normal Cayley graphs on symmetric groups — Aldous’ spectral gap conjecture states that the random walk and the interchange process on any connected graph have the same"
---
states that for any 2≤k≤n−2, Cay(S n,C(n,k)) has the Aldous property, thereby proving
a conjecture in [26, Conjecture 1.4] and solving an open problem in [30]. (See [11, 16, 17, 26]
for the proof of this conjecture whenk= 2,3,4,5 respectively.)
In [30], Siemons and Zalesski conjectured that forn≥5 and 1≤r <k <nthe nonnormal
Cayley graph Cay(Sn,C(n,k;r)) has the Aldous property. They proved in the same paper
that this is true whenr=k−1, and the case whenk= 2,3 was established earlier in
[12] and [16], respectively. In [24, Theorem 1.3], Li, Xia and Zhou settled this conjecture
by showing that forn≥5,k≥4 and 1≤r < k < n, Cay(S n,C(n,k;r)) has the Aldous
property except for (i) (n,k,r) = (6,5,1), or (ii)nis odd,k=n−1 and 1≤r < n
2 . In [17],
Huang, Huang and Cioab˘ a proved that most connected normal Cayley graphs onS n with
n≥7 whose connection sets consist of permutations moving at most five points have the
Aldous property. In [5], Cesi showed that the pancake graphP n has the Aldous property,
and Chung and Tobin [9] generalized this result to a family of graphs containing all pancake
graphs. The reader is referred to [25, Section 8] for more results on the Aldous property and
the second largest eigenvalue of Cayley graphs.
4
1.2 Main results
A subsetSofS n\{e}is called [27] anormal setinS n if it is the union of some conjugacy
classes ofS n. Since inS n every element is conjugate to its inverse element, a Cayley graph
Cay(Sn,S) onS n is normal if and only ifSis a normal set inS n. Clearly, for a normal set
SinS n, the set
Sc = (Sn\{e})\S
is also a normal set inS n, and moreover Cay(Sn,S) and Cay(Sn,Sc) are complements of each
other. Throughout the paper, we denote byK n the complete graph of ordern, byK m,n the
complete bipartite graph withmandnvertices in the two partite sets respectively, and by
tΓ the vertex-disjoint union oftcopies of a graph Γ. The first main result in this paper is as
follows.
Theorem 1.2.Letn≥5, and letSbe a nonempty normal set inS n withS̸=S n\{e}.
(a)If neitherSnorS c is equal toA n\{e}, then at most one ofCay(S n,S)andCay(S n,Sc)
has the Aldous property.
(b)If eitherSorS c is equal toAn\{e}, then one ofCay(S n,S)andCay(S n,Sc)is isomorphic
to2K n!/2 and the other toK n!/2,n!/2, and moreover both graphs have the Aldous property.
Theorem 1.2 implies that at most half of all normal Cayley graphs onSn exhibit the Aldous
property. This is true no matter whether isomorphism is taken into consideration because
two normal Cayley graphs are isomorphic if and only if their complements are isomorphic.
The second main result in this paper, Theorem 1.3 below, settles Problem 1.1 for suffi-
ciently largenand normal Cayley graphs whose connection sets consist of permutations with
support size between 2 andn−2. For a subsetS⊆S n, denote byO(S) andE(S) the sets
of odd and even permutations inS, respectively.
Theorem 1.3.There exists a positive integerN≥5such that, for everyn≥Nand every
nonempty normal setSinS n satisfying2≤|supp(σ)|≤n−2for allσ∈S, the following
statements hold:
(a)ifE(S) =∅orO(S) =∅, thenCay(S n,S)has the Aldous property;
(b)ifE(S)̸=∅andO(S)̸=∅, thenCay(S n,S)has the Aldous property if and only if
∑
σ∈S
|fix(σ)|≥n|E(S)|−(n−2)|O(S)|; (2)
moreover, ifCay(S n,S)does not have the Aldous property, then its strictly second largest
eigenvalue is attained by the sign representation ofS n.
If 2≤|supp(σ)|≤n−2 for allσ∈S, then ∑
σ∈S|fix(σ)|≥2|S|= 2|E(S)|+ 2|O(S)|, and
hence (2) is satisfied whenn|O(S)|≥(n−2)|E(S)|. So we obtain the following corollary of
Theorem 1.3 immediately.
5
Corollary 1.4.There exists a positive integerN≥5such that, for everyn≥Nand
every nonempty normal setSinS n satisfying2≤ |supp(σ)| ≤n−2for allσ∈S, if
n|O(S)|≥(n−2)|E(S)|, thenCay(S n,S)has the Aldous property.
Another corollary of Theorem 1.3 is the following explicit formula for the second largest
eigenvalue of normal Cayley graphs on the alternating groupA n.
Corollary 1.5.There exists a positive integerN≥5such that, for everyn≥Nand every
nonempty normal setSinS n, ifS⊆A n and2≤|supp(σ)|≤n−2for allσ∈S, then the
strictly second largest eigenvalue ofCay(S n,S)is given by
1
n−1
(∑
σ∈S
|fix(σ)|−|S|
)
,
and moreoverCay(Sn,S)is disconnected with two components each isomorphic toCay(A n,S).
For a subsetS⊆S n, let
AS =S∩Supp n({2,3,...,n−2}), B S =S∩Supp n(n−1), C S =S∩Supp n(n) (3)
and
AS = Suppn({2,3,...,n−2})\A S, BS = Suppn(n−1)\B S, CS = Suppn(n)\C S.(4)
The following theorem classifies all normal Cayley graphs Cay(S n,S) that have the Aldous
property under an easy-to-check condition.
Theorem 1.6.Letn≥5, and letSbe a nonempty normal set inS n. If
∑
σ∈AS
|fix(σ)|≤|A S|+|C S|+n−1,(5)
thenCay(S n,S)has the Aldous property if and only ifS=S n\{e},S n\An orA n\{e}, or,
equivalently,Cay(S n,S) ∼=Kn!,Kn!/2,n!/2 or2K n!/2, respectively.
Note that condition (5) holds only if eitherA S is empty orC S is nonempty. Theorem 1.6
implies the following corollary.
Corollary 1.7.Letn≥5, and letSbe a nonempty normal set inS n. ThenCay(S n,S)does
not have the Aldous property if one of the following conditions holds:
(a)S⊆Supp n({n−1,n});
(b)| AS|−| CS|+ 2(n−1)≥0andS /∈{S n\{e},S n\An,An\{e}};
(c) Suppn(n)⊆SandS̸=S n\{e}.
6
In [22, Problem 1.2], Li, Xia and Zhou ask for a necessary and sufficient condition for
Cay(Sn,Suppn(I)) with{n} ⊂I⊆ {2,3,...,n−2,n}to have the Aldous property for
sufficiently largen. Solving this problem, part (c) of Corollary 1.7 implies that such a graph
Cay(Sn,Suppn(I)) does not have the Aldous property for anyn≥5.
Theorem 1.3 and Corollary 1.7 together resolve Problem 1.1 for all normal Cayley graphs
Cay(Sn,S) with sufficiently largenexcept whenS∩Supp n({2,3,...,n−2})̸=∅,S∩
Suppn({n−1,n})̸=∅, and Supp n(n)̸⊆S.
The rest of the paper is organized as follows. The next section is a quick review of repre-
