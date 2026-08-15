---
doc_id: arxiv-1711.08944v2
doc_title: "The second largest eigenvalues of some Cayley graphs on alternating groups ∗"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1711.08944v2.pdf
source_sha256: ad7a020e7e92b788
doc_brief: "The second largest eigenvalues of some Cayley graphs on alternating groups ∗ — Let An denote the alternating group of degree n with n ≥ 3."
---
Let G = ( V (G), E(G)) be a simple undirected graph of order n. The adjacency
matrix of G, denoted by A(G), is the n × n matrix with entries auv = 1 if {u, v} ∈
E(G) and auv = 0 otherwise. The eigenvalues of A(G) are denoted by λ1(G) ≥
λ2(G) ≥ · · · ≥ λn(G), which are also called the eigenvalues of G.
For v ∈ V (G), we denote by N(v) = {u ∈ V (G) | { u, v} ∈ E(G)} and d(v) =
|N(v)| the neighborhood and degree of v, respectively. Let D(G) = diag( d(v) |
v ∈ V (G)) denote the diagonal degree matrix of G. The Laplacian matrix of G is
deﬁned as L(G) = D(G) − A(G), which is positive semi-deﬁnite and always has 0 as
its eigenvalue. So the eigenvalues of L(G) can be arranged as µ1(G) ≥ µ2(G) ≥ · · · ≥
µn−1(G) ≥ µn(G) = 0. Furthermore, µn−1(G) > 0 if and only if G is connected, and
for connected non-complete graphs we know that 0 < µ n−1(G) ≤ κ(G) ≤ κ′(G) ≤
δ(G), where κ(G), κ′(G) and δ(G) denote the vertex connectivity, edge connectivity
and minimum degree of G, respectively (cf. [
9], Corollary 7.4.6). For this reason,
µn−1(G) is called the algebraic connectivity of G. Clearly, if G is r-regular then
µn−1(G) = r − λ2(G).
∗ This work is supported by the National Natural Science Foundation of China (Grant nos.
11531011, 11671344).
†Corresponding author.
E-mail address: huangxymath@gmail.com (X. Huang), huangqx@xju.edu.cn (Q. Huan g).
1
2
For a ﬁnite group Γ, and a subset T ⊆ Γ \ {e} (e is the identity element of Γ)
such that T = T −1, the Cayley graph Cay(Γ , T ) on Γ with respect to T is deﬁned
as the undirected graph with vertex set Γ and edge set {{γ, tγ} | γ ∈ Γ , t ∈ T }.
Clearly, Cay(Γ , T ) is a |T |-regular graph which is connected if and only if T is a
generating subset of Γ.
Let Sn be the symmetric group of degree n ≥ 3 (for σ, τ ∈ Sn, the product
στ means that we ﬁrst apply permutation σ and then apply permutation τ , and τi
represents the image of i under the permuation τ ), and let T be a set of transpositions
in Sn. The transposition graph Tra(T ) of T is deﬁned as the graph with vertex
set {1, 2, . . . , n} and with an edge connecting two vertices i and j if and only if
(i, j) ∈ T . It is known that T can generate Sn if and only if Tra( T ) is connected [ 13].
Around 1992, Aldous [ 1] (see also [ 4, 12]) conjectured that if Tra( T ) is connected
then the second largest eigenvalue of Cay( Sn, T ) is equal to |T | − µn−1(Tra(T )),
that is, Cay( Sn, T ) and Tra( T ) share the same algebraic connectivity. Before 1992,
Flatto et al. [ 11] and Diaconis and Shahshahani [ 10] had conﬁrmed the conjecture for
Tra(T ) = K1,n−1 and Tra(T ) = Kn, respectively. In 2000, Friedman [ 12] proved that
if Tra( T ) is a tree ( |T | = n − 1) then the second largest eigenvalue of Cay( Sn, T )
is at least n − 2, and exactly equal to n − 2 if and only if Tra( T ) = K1,n−1. In
2010, Cesi [ 4] conﬁrmed Aldous’ conjecture when Tra( T ) is a complete multipartite
graph. Almost at the same time, Caputo et al. [ 2] completely solved the conjecture
for all connected Tra( T ). For other Cayley graphs on symmetric groups, Cesi [ 3]
proved that the second largest eigenvalue of the pancake graph Pn = Cay( Sn, S)
(S = {(1, i)(2, i − 1) · · · | 2 ≤ i ≤ n}) is equal to n − 2; and very recently, Chung
and Tobin [ 8] determined the second largest eigenvalues of the reversal grap h Rn =
Cay(Sn, S) (S = {(i, j)(i + 1, j − 1) · · · | 1 ≤ i < j ≤ n}) and a family of graphs that
generalize the pancake graph. Their method is very imaginative, whic h depends on
ﬁnding enough equitable partitions of Rn and decomposing the edge set E(Rn) to
that of Pn and n copies of Rn−1.
Now we consider the Cayley graphs on alternating group An (n ≥ 3). Let
T1 = {(1, 2, i), (1, i, 2) | 3 ≤ i ≤ n}, T2 = {(1, i, j), (1, j, i) | 2 ≤ i < j ≤ n}
and T3 = {(i, j, k), (i, k, j) | 1 ≤ i < j < k ≤ n}. The alternating group graph
AGn, extended alternating group graph EAGn and complete alternating group graph
CAG n are deﬁned as the Cayley graphs Cay( An, T1), Cay( An, T2) and Cay( An, T3),
respectively. Since T1 ⊆ T2 ⊆ T3, AGn is a spanning subgraph of EAGn while
EAGn is also a spanning subgraph of CAG n, and all these graphs are connected
because T1 can generate An (cf. [ 16], p. 298). In [ 15], Jwo et al. introduced the
alternating group graph AGn as an interconnection network topology for computing
systems, and they also showed that AGn is 2-transitive, Hamiltonian and of diame-
ter ⌊3(n − 2)/2⌋. Following this paper, AGn was extensively studied over decades.
For example, Chang and Yang [ 5, 6] investigated the panconnectivity, Hamiltonian-
connectivity and fault-tolerant Hamiltonicity of AGn. Zhou [ 17] determined the full
automorphism group of AGn. In addition, the complete alternating group graph
CAG n can be viewed as one of the two isomorphic connected components o f the
(n − 3)-point ﬁxing graph F (n, n − 3) deﬁned in [ 7], which has only integral eigen-
values (cf. [ 7], Corollary 1.2). Recently, the full automorphism group of CAG n was
determined by Huang and Huang [ 14].
3
Inspired by the work of Chung and Tobin [ 8], in the present paper, we determine
the second largest eigenvalues of AGn, EAGn and CAG n, which are equal to 2 n − 6
(for n ≥ 4), n2 − 5n + 5 and 1
3n(n − 2)(n − 4), respectively.
The paper is organized as follows. In Section 2, we obtain the second largest
eigenvalue of AGn by induction on n. In Section 3, we focus on determining the
second largest eigenvalue of CAG n. In order to achieve this goal by induction on n,
we decompose the edge set of CAG n into that of EAGn and n copies of CAG n−1,
and use λ2(EAGn) + λ2(CAG n−1) to bound λ2(CAG n). Thus we have to determine
λ2(EAGn), and for this reason, we also decompose the edge set of EAGn into that of
AGn and n copies of EAGn−1, and use λ2(AGn) +λ2(EAGn−1) to bound λ2(EAGn)
as λ2(AGn) has been determined in Section 2.
