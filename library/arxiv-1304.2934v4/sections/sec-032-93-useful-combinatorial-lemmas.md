---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-032-93-useful-combinatorial-lemmas
section_title: "Useful combinatorial lemmas"
section_number: 9.3
pages: 73-76
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
lemmas on graphs and spanning trees.
9.3.1. A functional on graphs. In this section, we consider graphsH with multiple edges
and loops. We use the standard notationV(H) and E(H) for their vertex and edge sets.
For a graph H and a set partition π of V(H), we denote π⊥ H when the following
holds: for any edge{i, j}∈ E(H), the elements i and j lie in different parts of π (in this
case we use the notation i≁π j). We introduce the following functional on graphs H:
FH = (−1)|V(H)|−1
∑
π⊥H
µ(π).
Lemma 9.12. For any graph H, one has
FH = ∑
E⊂E(H)
(V(H),E) connected
(−1)|E|−|V(H)|+1.
Proof. To simplify notation, suppose V(H) = [ r]. We denote 1 (P) the characteristic
function of the property (P). By inclusion-exclusion,
(−1)|V(H)|−1 FH = ∑
π∈Q(r)

 ∏
(i,j)∈E(H)
1 i≁π j

 µ(π) = ∑
π∈Q(r)

 ∏
(i,j)∈E(H)
(1− 1 i∼π j)

 µ(π)
= ∑
E⊂E(H)
∑
π∈Q(r)
(−1)|E|

 ∏
(i,j)∈E
1 i∼π j

 µ(π)
= ∑
E⊂E(H)
(−1)|E|

 ∑
π such that
∀(i,j)∈E, i∼π j
µ(π)

 .
74 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
But the quantity in the bracket is 0 unless the only partition in the sum is the maximal
partition
{
[r]
}
, in which case it is 1. This corresponds to the case where the edges in E
form a connected subgraph of H. □
Corollary 9.13. The functional FH fulﬁlls the deletion-contraction induction, i.e., if e is an
edge of H which is not a loop, then
FH = FH/e + FH\e,
where H\ e (respectively H/e) are the graphs obtained from H by deleting (resp. contracting)
the edge e.
Proof. The ﬁrst term corresponds to sets of edges containing e, and the second to those
that do not contain e. □
This induction (over-)determines FH together with the initial conditions:



F
MOD-GAUSSIAN CONVERGENCE OF POL YNOMIAL FUNCTIONS UNDER CE NTRAL MEASURES3
Proof. Each spanning tree of HA can be lifted (non necessarily in a unique way) to
ap s e u d o - t r e ec o n t a i n e di nGA.S o t h e n u m b e ro f c o u p l e s(A,T ) of the statement
is bounded by the number of couples (A,G ),w h e r eG is a pseudo-tree contained
in GA.B yL e m m a1 . 1a n d1 . 2 ,t h i sn u m b e ri sg i v e nb yt h ef o r m u l aa b o ve.
The second assertion comes from the fact that a connected gra ph has at least one
spanning tree. □
Let H be a graph on vertex set [𝓁] (eventually with some multiple edges and/or
loops). We consider the following quantity
AH =( −1)V (H)−1 ∑
Π⊥E(H)
µ(Π),
where Π⊥E(H) means: (i, j) ∈ E(H) implies that i and j lie in different parts of
Π (notation: i ≁Π j).
Lemma 1.4. Fo r a n y g ra p hH,o n eh a s
AH =
∑
E⊂ E(H)
(V (H),E) connected
(−1)|E|−V (H)+1.
Proof. By inclusion-exclusion,
AH =( −1)V (H)−1 ∑
E⊂ E(H)
E⁄=∅
(−1)|E|


∑
Πsuch that
∀(i,j)∈E,i∼ Πj
µ(Π)

.
But the quantity in the bracket is 0 unless the only partition in the sum is the
maximal partition
{
{1,..., 𝓁}
}
,i nw h i c hc a s ei ti s1.T h i sc o r r e s p o n d st ot h ec a s e
where the edges in E form a connected subgraph of H. □
Corollary 1.5. AH fulﬁlls the deletion-contraction induction: if e is an edge of H,
then
AH = AH\e + AH/e,
where H∩e (resp. H/e)a r et h eg r a p h so b t a i n e df r o mH by contracting (resp.
deleting) the edge e.
Proof. The ﬁrst term correspond to sets of edges containing e,t h es e c o n dt ot h o s e
who do not contain e. □
This induction detemines AH together with the initial conditions:



A =1
A =0
AH =0 if H is disconnected.
Corollary 1.6. Fo r a n y g ra p hH,t h eq u a n t i t yAH is positive and smaller than the
number STH of spanning trees in H. = 1,
F = F =··· = 0,
FH = 0 if H is disconnected.
Corollary 9.14. For any graph H, the quantity FH is nonnegative and less or equal than the
number STH of spanning trees in H.
Proof. The quantity STH fulﬁlls the same induction as F H with initial conditions:



ST
MOD-GAUSSIAN CONVERGENCE OF POL YNOMIAL FUNCTIONS UNDER CE NTRAL MEASURES3
Proof. Each spanning tree of HA can be lifted (non necessarily in a unique way) to
ap s e u d o - t r e ec o n t a i n e di nGA.S o t h e n u m b e ro f c o u p l e s(A,T ) of the statement
is bounded by the number of couples (A,G ),w h e r eG is a pseudo-tree contained
in GA.B yL e m m a1 . 1a n d1 . 2 ,t h i sn u m b e ri sg i v e nb yt h ef o r m u l aa b o ve.
The second assertion comes from the fact that a connected gra ph has at least one
spanning tree. □
Let H be a graph on vertex set [𝓁] (eventually with some multiple edges and/or
loops). We consider the following quantity
AH =( −1)V (H)−1 ∑
Π⊥E(H)
µ(Π),
where Π⊥E(H) means: (i, j) ∈ E(H) implies that i and j lie in different parts of
Π (notation: i ≁Π j).
Lemma 1.4. Fo r a n y g ra p hH,o n eh a s
AH =
∑
E⊂ E(H)
(V (H),E) connected
(−1)|E|−V (H)+1.
Proof. By inclusion-exclusion,
AH =( −1)V (H)−1 ∑
E⊂ E(H)
E⁄=∅
(−1)|E|


∑
Πsuch that
∀(i,j)∈E,i∼ Πj
µ(Π)

.
But the quantity in the bracket is 0 unless the only partition in the sum is the
maximal partition
{
{1,..., 𝓁}
}
,i nw h i c hc a s ei ti s1.T h i sc o r r e s p o n d st ot h ec a s e
where the edges in E form a connected subgraph of H. □
Corollary 1.5. AH fulﬁlls the deletion-contraction induction: if e is an edge of H,
then
AH = AH\e + AH/e,
where H∩e (resp. H/e)a r et h eg r a p h so b t a i n e df r o mH by contracting (resp.
deleting) the edge e.
Proof. The ﬁrst term correspond to sets of edges containing e,t h es e c o n dt ot h o s e
who do not contain e. □
This induction detemines AH together with the initial conditions:



A =1
A =0
AH =0 if H is disconnected.
Corollary 1.6. Fo r a n y g ra p hH,t h eq u a n t i t yAH is positive and smaller than the
number STH of spanning trees in H. = 1,
ST = ST =··· = 1,
STH = 0 if H is disconnected. □
Remark 9.15. If H is connected, both F H and ST H are actually specializations of the
bivariate Tutte polynomial TH(x, y) of H (cf. [Bol98, Chapter X]):
FH = TH(1, 0) ; ST H = TH(1, 1).
This explains the deletion-contraction relation. As the bivariate Tutte polynomials has
non-negative coefﬁcients, it also explains the inequality 0≤ FH≤ STH.
9.3.2. Induced graphs containing spanning trees. Fix a graph G (typically the dependency
graphs of our family of variables). For a list (v1, . . . ,vr) of r vertices of G, we deﬁne the
induced graph G[v1, . . . ,vr] as follows:
• its vertex set is [r];
• there is an edge between i and j if and only if vi = vj or vi and vj are linked in
G.
MOD-φ CONVERGENCE, I 75
We will be interested in spanning trees of induced graphs. As the vertex set is[r], these
spanning trees may be seen as Cayley trees. Recall that a Cayley tree of size r is by def-
inition a tree with vertex set [r] (Cayley trees are neither rooted, nor embedded in the
plane, they are only speciﬁed by an adjacency matrix). These objects are enumerated
by the well-known Cayley formula established by C. Borchardt in [Bor60]: there are
exactly rr−2 Cayley trees of size r.
Lemma 9.16. Fix a Cayley tree T of size r and a graph G with N vertices and maximal degree
D. Fix a vertex v 1 of G. The number of lists (v1, . . . ,vr) of r vertices of G such that T is
contained in the induced subgraph G[v1, . . . ,vr] is bounded from above by
(D + 1)r−1.
Proof. Lists (v1, . . . ,vr) as in the lemma are constructed as follows. First consider a
neighbor j of 1 in T. As we require G[v1, . . . ,vr] to contain T, the vertices 1 and j must
also be neighbors in G[v1, . . . ,vr], i.e. v j = v1 or vj is a neighbor of v1 in T. Thus,
once v1 is ﬁxed, there are at most D + 1 possible values for vj. The same is true for all
neighbors of 1 and then for all neighbors of neighbors of 1 and so on. □
We have the following immediate consequence.
Corollary 9.17. Let G be a graph with n vertices and maximal degree D and r ≥ 1. Fix a
vertex v1 of G. The number of couples
(
(v1, . . . ,vr), T
)
where each vi is a vertex of V and T a
spanning tree of the induced subgraph G[v1, . . . ,vr] is bounded above by
rr−2 (D + 1)r−1.
9.3.3. Spanning trees and set partitions of vertices. Recall that ST H denotes the number
of spanning trees of a graph H. Consider now a graph H with vertex set [r] and a set
partition π = ( π1, . . . ,πt) of [r]. For each i, we denote ST πi (H) = STH[πi] the number
of spanning trees of the graph induced by H on the vertex set πi. We also use the
multiplicative notation
STπ(H) =
t
∏
j=1
STπj(H).
We can also consider the contraction H/π of H with respect to π. By deﬁnition, it
is the multigraph ( i.e. graph with multiple edges, but no loops) deﬁned as follows.
Its vertex set is the index set [t] of the parts of π and, for i⁄= j, there are as many
edges between i and j as edges between a vertex of πi and a vertex of πj in H. Denote
STπ(H) = STH/π the number of spanning trees of this contracted graph (multiple
edges are here important). This should not be confused with STπ(H): in the latter, π is
placed as an exponent because the quantity is multiplicative with respect to the part of
π.
Note that the union of a spanning tree T of H/π and of spanning trees Ti of H[πi]
(one for each 1≤ i≤ t) gives a spanning tree T of H. Conversely, take a spanning tree
T on H and a bicoloration of its edges. Edges of color 1 can be seen as a subgraph of H
with the same vertex set [r]. This graph is of course acyclic. Its connected components
deﬁne a partition π ={π1, . . . ,πt} of [r] and edges of color 1 correspond to a collection
of spanning trees Ti of H[πi] (for 1≤ i≤ t). Besides, edges of color 2 deﬁne a spanning
tree T on H/π.
76 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
Therefore, we have described a bijection between spanning trees T0 of H with a bi-
coloration of their edges and triples (π, T, (Ti)1≤i≤t) where:
• π is a set partition of the vertex set [r] of H (we denote t its number of parts);
• T is a spanning tree of the contracted graph H/π;
• for each 1≤ i≤ t, Ti is a spanning tree of the induced graph H[πi].
Before giving a detailed example, let us state the numerical corollary of this bijection:
2r−1 STH = ∑
π
STπ(H) STπ(H), (43)
where the sum runs over all set partitions π of [r].
T = 1
23
4
5 6
↔



π ={π1, π2} with π1 ={1, 2, 3}, π2 ={4, 5, 6};
T1 =
1
23
, T2 =
4
5 6
;
T =
π1
π2
.
FIGURE 9. Bijection explaining Identity (43).
Our bijection is illustrated on Figure 9, with the following conventions.
• On the left, blue plain edges are edges of color 1 in the treeT0; on the right, these
blue plain edges are the edges of the spanning trees Ti.
• On the left, green dashed edges are edges of color 2 in the tree T0; on the right,
these green dashed edges are edges of the spanning tree T.
• Red dotted edges belong to the graphs H, H/π, H[πi] but not to their spanning
tree T0, T, Ti.
Note that in this example the graph H/π has two vertices linked by four edges. These
four edges correspond to the edges (1, 4), (1, 6), (2, 6) and (3, 5) of H. In the example,
the spanning tree T is the edge{(3, 5)}. If we had chosen another edge, the tree T on
the left-hand side would have been different. Hence, in the Equality (43), the multiple
edges of H/π must be taken into account: in our example, STπ(H) = 4.
