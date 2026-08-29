---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-036-102-polynomiality-of-cumulants
section_title: "Polynomiality of cumulants"
section_number: 10.2
pages: 83-85
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
10.2.1. Dealing with several arrangements. Consider a list (A1, . . . ,Ar) of arrangements.
We associate to this data two graphs (unless said explicitly, we always consider loop-
less simple graphs, and V(G) and E(G) denote respectively the edge and vertex sets
of a graph G):
• the graph GA has vertex set
Vk = V(GA) ={(t, i)| 1≤ i≤ r, 1≤ t≤ ki}
and an edge between (t, i) and (s, j) if and only if ai
t = aj
s. It is always a disjoint
union of cliques. If the Ai’s are arrangements, then the graph GA is endowed
with a natural proper r-coloring, (t, i) being of color i.
• the graph Hm
A has vertex set [r] and an edge between i and j if|Ai∩ Aj|≥ m.
Notice that H1
A is the contraction of the graph GA by the map ϕ : (t, i)↦→ i from the
vertex set of GA to the vertex of H1
A. Indeed,
(i, j)∈ E(H1
A) ⇔ ∃vi∈ ϕ−1(i), vj∈ ϕ−1(j) such that (vi, vj)∈ E(GA).
An example of a graph GA and of its 1- and 2-contractions H1
A and H2
A is drawn on
Figure 12. For m≥ 2, the deﬁnition of Hm
A is less common. We call it the m-contraction
of GA. The 2-contraction is interesting for us. It corresponds exactly to the graph
induced by the dependency graph B on the list of arrangement A, considered in the
proof of Theorem 9.7.
Remark 10.4. Graphs associated to families of arrangements are a practical way to en-
code some information and should not be confused with the random graphs or their
induced subgraphs. Therefore we used greek letters for the latter and latin letter for
graphs GA and their contractions. The dependency graph will always be called B to
avoid confusions.
10.2.2. Exploiting symmetries. The dependency graph of our model has much more
structure than a general dependency graph. In particular, all variables δγ(A) are iden-
tically distributed. More generally, the joint distribution of
(
δγ(A1), . . . ,δγ(Ar)
)
depends only on GA. Here, we state a few consequences of this invariance property
that will be useful in the next Section.
84 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
2794
41 63
25641
81 05
15 13 14 11 12
GA
H1
A H2
A
10
FIGURE 12. The graphs GA, H1
A and H2
A corresponding to the family of
arrangements (15, 13, 14, 11, 12), (2, 5, 6, 4, 1), (2, 7, 9, 4), (4, 16, 3), and
(8, 10, 5).
Lemma 10.5. Fix a graph γ of size k, the quantity
E
[
δγ(A1)··· δγ(Ar)
]
depends only on the graph G A associated to the family of arrangements (A1, . . . ,Ar). The
same is true for the joint cumulant κ
(
δγ(A1), . . . ,δγ(Ar)
)
.
Proof. The ﬁrst statement follows immediately from the invariance of the modelΓ(n, p)
by relabelling of the vertices. The second is a corollary, using the moment-cumulant
relation (42). □
Corollary 10.6. Fix some graph γ. Then the joint cumulant κ(X(n)
γ , . . . ,X(n)
γ ) is a polynomial
in n.
Proof. Using Lemma 10.5, we can rewrite the expansion (44) as
κ(X(n)
γ , . . . ,X(n)
γ ) = ∑
G
κ(G)NG, (50)
where:
• the sum runs over graphs G of vertex set Vk that correspond to some arrange-
ments (that is G is a disjoint union of cliques and, for any s, t and i, there is no
edge between (s, i) and (t, i));
• κ(G) is the common value of κ
(
δγ(A1), . . . ,δγ(Ar)
)
, where (A1, . . . ,Ar) is any
list of arrangements with associated graph G;
• NG is the number of lists of arrangements with associated graph G.
But it is clear that the sum index is ﬁnite and that neither the summation index nor
the quantity κ(G) depend on n. Besides, the number NG is simply the falling factorial
n(n− 1) . . .(n− cG + 1), where cG is the number of connected components of G. The
corollary follows from these observations. □
MOD-φ CONVERGENCE, I 85
