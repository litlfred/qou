---
doc_id: ising
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-013-41-weighted-dependency-graph-for-the-σis-and-cen
section_title: "Weighted dependency graph for the σi’s and central limit theorem for the magneti-"
section_number: 4.1
pages: 16-18
source_pdf: ising.pdf
source_sha256: 9f84d7209731d299
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
zation.
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 17
4.1.1. The weighted dependency graph. We start by proving Theorem 1.5, which gives a weighted
dependency graph for{σi :i∈ Zd}.
Proof of Theorem 1.5: LetB ={i1,...,i r} be a multiset of elements of Zd and consider the induced
subgraph G[B]. Then the maximum weightM(G[B]) of a spanning tree in G[B] satisﬁes
M(G[B]) =ε
𝓁′
T (B)
2 .
Thus by Proposition 2.1,
(4.1) ε𝓁T (B)≤M (G[B])≤ε
𝓁T (B)
2 .
By Proposition 5.2 of [10], it is suﬃcient to show that
⏐⏐⏐⏐⏐κβ,h
(∏
α∈B1
σα,...,
∏
α∈Bk
σα
)⏐⏐⏐⏐⏐≤DrM(G[B]),
for some sequence D = (Dr)r≥1, where B1,...,B k are the vertex-sets of the connected components of
G1[B], which is the graph induced by edges of weight 1 of G on B.
The verticesi andj are connected in G1 if and only if i =j, because of the deﬁnition of the weights
we in G. Consequently, each multiset in the list B1,...,B k consists of a single spin σi, possibly
repeated several times. The random variables σi taking value +1 or−1, we have
σj
i =
{
σi if j odd,
1 if j even.
Therefore it is suﬃcient to prove that for any set B′ of distinct i1,...,i r,
(4.2) |κβ,h (σi1,...,σ ir)|≤ DrM(G[B′]).
But by Theorem 1.1,
|κβ,h (σi1,...,σ ir)|≤ Drε𝓁T (B′),
for some sequence D depending only onr. Thus using (4.1), Equation (4.2) is proved, which completes
the proof of the theorem. □
4.1.2. The central limit theorem for the magnetization. As a ﬁrst application, we use the weighted de-
pendency graph from last section to obtain the well-known central limit theorem for the magnetization
(for an early reference, see [30]), in the regime ( β,h )∈R(β1,β 2,h 1).
We consider the Ising model on Zd, with inverse temperature β and magnetic ﬁeld h. For any
positive integer n, we deﬁne Λn := [−n,n ]d the d-dimensional cube centred at 0 of side 2 n. We deﬁne
the magnetization
Sn :=
∑
i∈Λn
σi,
and let v2
n denote the variance of Sn. Let us further deﬁne the covariance
⟨σi;σj⟩β,h :=⟨σiσj⟩β,h−⟨σi⟩β,h⟨σj⟩β,h.
Theorem 4.1. Consider the Ising model on Zd, with inverse temperatureβ and magnetic ﬁeld h, such
that (β,h )∈R(β1,β 2,h 1). Then there exists v =v(β,h,d ) such that
Sn− E(Sn)√
|Λn|
d
−−−−→
n→∞
N (0,v 2).
Moreoverv2 > 0 so the Gaussian law is non-degenerate.
We start by a lemma of [8] on the asymptotics of the variance of Sn.
