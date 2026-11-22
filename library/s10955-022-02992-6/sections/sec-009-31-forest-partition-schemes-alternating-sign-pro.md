---
doc_id: s10955-022-02992-6
doc_title: "Cluster Expansions: Necessary and Sufficient Convergence Conditions"
section_id: sec-009-31-forest-partition-schemes-alternating-sign-pro
section_title: "Forest Partition Schemes: Alternating Sign Property"
section_number: 3.1
pages: 14-17
source_pdf: s10955-022-02992-6.pdf
source_sha256: aa73d797a89eaf06
toc_source: outline
doc_brief: "Cluster Expansions: Necessary and Sufficient Convergence Conditions — We prove a new convergence condition for the activity expansion of correlation functions in equilibrium statistical mechanics"
---
To obtain a better understanding of the series ρn given by the generating functions of multi-
rootedgraphs,wenowconsideraparticularwaytoconstructthelatter—bytakingadesignated
spanning forest and successively adding edges to it. This perspective onto multi-rooted graphs
leads to a forest-graph equality analogous to the familiar tree-graph identity for connected
graphs [8, Proposition 5] and allows for a direct proof of an alternating sign property for
the coefﬁcients ψn,n+k of ρn in the case of repulsive interactions (i.e., for non-negative
potentials).
The forest-graph equality builds on the notion of forest partition schemes—maps that
assign spanning forests to multi-rooted graphs in Dn,n+k and thereby in a speciﬁc manner
provide partitions of Dn,n+k.
In the following, we let Fn,n+k denote the set of forest graphs on the vertex set [n + k]
consisting of n rooted trees, where the vertices {1, . . . , n} are the roots of the trees (recall
that a forest is an acyclic graph and a tree is a connected acyclic graph).
Deﬁnition 3.1 (Forest partition scheme) A forest partition scheme is a family of maps πn,k :
Dn,n+k →Fn,n+k such that for all n ∈N, k ∈N0, and all F ∈Fn,n+k, there exists a graph
Rn,k(F) ∈Dn,n+k with
π−1
n,k

{F}

= {G ∈Dn,n+k | E(F) ⊂E(G) ⊂E

Rn,k(F)

} =: [F, Rn,k(F)].
Cluster Expansions: Necessary...
Page 15 of 47
33
To lighten the notation, we introduced partition schemes as families of maps on uncoloured
structures. Notice, however, that partition schemes may be deﬁned on coloured structures and
may be allowed to depend on the colouring of the vertex set. Therefore, one could introduce
families of maps πk,n(x[n]), indexed additionally by colourings x[n] ∈Xn of [n] = {1, ..., n}.
Same graphs on the vertex set [n] with different colourings x[n] of the vertices can be mapped
onto different forests under such partition schemes.
The existence of forest partition schemes is ensured by the existence of a large class of
tree partition schemes, e.g, the Penrose tree partition scheme (see [8, 33]; for coulouring-
dependent schemes see also [25, 31]).
Example 3.1 A particular forest partition scheme can be deﬁned as follows: For a given multi-
rooted graph, construct a connected graph from it by adding a ghost-vertex and connecting
it to every root directly by an edge. Then apply the Penrose partition scheme to the resulting
connected graph to obtain a spanning tree of this connected graph. Finally, by removing the
ghost vertex as well as every edge incident to it, one gets a spanning forest of the initial
multi-rooted graph. For the map given by this construction, the characterizing properties of a
forest partition scheme follow from the corresponding properties of the Penrose tree partition
scheme.
Naturally,thechoiceofthePenrosetreepartitionschemeintheexampleaboveissomewhat
arbitrary; any tree partition scheme which does not “delete” any edge incident to the ghost
vertex in the above construction yields a forest partition scheme via the same procedure.
Proposition 3.2 (Forest-graph equality) Let (πn,k)n∈N, k∈N0 be a forest partition scheme and
let (Rn,k)n∈N, k∈N0 provide the corresponding family of multi-rooted graphs as in Deﬁni-
tion 3.1. Then
ψn,n+k(x1, . . . , xn+k) =

F∈Fn,n+k

{i, j}∈E(F)
f (xi, x j)

{i, j}∈E(Rn,k(F))\E(F)

1 + f (xi, x j)

for all n ∈N, k ∈N0, and (x1, . . . , xn+k) ∈Xn+k.
Proof The proof is similar to the standard proof of the tree-graph equality [8, Proposition
5]. We have
ψn,n+k(x1, . . . , xn+k) =

G∈Dn,n+k
w

G, (x1, . . . , xn+k)

=

F∈Fn,n+k

G∈Dn,n+k:
πn,k(G)=F
w

G, (x1, . . . , xn+k)

=

F∈Fn,n+k

{i, j}∈E(F)
f (xi, x j)

{i, j}∈E(Rn,k(F))\E(F)

1 + f (xi, x j)

.
⊓⊔
In the case of repulsive interactions, the forest-graph equality allows for a direct proof of
the alternating sign property for the graph weights ψn,n+k. For n = 1, it reduces to the
well-known alternating sign property [8, Eq. (2.8)]
ϕT
n(x1, . . . , xn) = (−1)nϕT
n(x1, . . . , xn)

(3.1)
of the Ursell functions.
33
Page 16 of 47
S. Jansen, L. Kolesnikov
Corollary 3.3 For non-negative potentials, we have
ψn,n+k(x1, . . . , xn+k) = (−1)kψn,n+k(x1, . . . , xn+k)

for all n ∈N, all k ∈N0, and all (x1, . . . , xn+k) ∈Xn+k.
Proof Each forest F ∈Fn,n+k has exactly k edges. Indeed, the forest F consists of trees
T1, . . . , Tn. Let mi be the number of vertices of the tree Ti; thus m1 + · · · + mn = n + k.
Each tree Ti has exactly mi −1 edges, therefore the number of edges of the forest is given
by n
i=1(mi −1) = k. Since f ≤0 and 1 + f ≥0 for non-negative potentials, it follows
that
ψn,n+k(x1, . . . , xn+k) = (−1)k

F∈Fn,n+k

{i, j}∈E(F)
| f (xi, x j)|

{i, j}∈E(Rn,k(F))\E(F)

1 + f (xi, x j)

,
hence (−1)kψn,n+k(x1, . . . , xn+k) ≥0.
⊓⊔
We will use the alternating sign property to establish that—in the case of non-negative
potentials—condition (i) in Theorem 2.1 is not only sufﬁcient but also necessary for absolute
convergence of ρ.
We conclude this section with a lemma that is not needed for the proof of Theorem 2.1
but enters the analysis of hard-core models, see the proof of Lemma 3.8 below.
Lemma 3.4 For all n ∈N, all k ∈N0, and all (x1, . . . , xn+k) ∈Xn+k, we have
ψn,n+k(x1, . . . , xn+k) =

1≤i< j≤n

1 + f (xi, x j)

×

{V1,...,Vr}
r
ℓ=1
 
1≤i≤n,
j∈Vℓ

1 + f (xi, x j)

−1

ϕT
|Vℓ|

(x j) j∈Vℓ

,
(3.2)
where the sum runs over all set partitions {V1, . . . , Vr} of non-root vertices {n+1, . . . , n+k}.
Remark 3.1 The lemma allows for an alternative proof of the alternating sign property from
Corollary 3.3, starting from the well-known alternating sign property of the Ursell function
instead of the forest-graph equality. Indeed, the sign of every summand in the right-hand side
of (3.2) is
(−1)r+r
i=1(|Vi|−1) = (−1)k.
Proof of Lemma 3.4 For n = 1, the lemma reduces to a well-known equality for the Ursell
functions, see e.g. [11, Eq. (5.13)]. For n ≥2, the proof is similar, we provide the details for
the reader’s convenience. Every multi-rooted graph G ∈Dn,n+k can be constructed in the
following way. On the root set {1, . . . , n} pick an arbitrary graph G0. On the complement of
the root set do the following construction: Partition the set of the non-root vertices into r sets
V1, ..., Vr, r ≤k. For every block Vℓ, pick a connected graph Gℓwith vertex set Vℓ, and in
addition a non-empty set of edges Eℓ⊂

{i, j} | i ∈{1, . . . , n}, j ∈Vℓ}. Then the graph
Cluster Expansions: Necessary...
Page 17 of 47
33
G with vertices 1, . . . , n + k and edge set given by the union of E1, . . . , Eℓand of the edge
sets of G0, G1, . . . , Gr is in Dn,n+k, its graph weight is
w(G; x1, . . . , xn+k) = w(G0; x1, . . . , xn)
r
ℓ=1
 
{i, j}∈Eℓ
f (xi, x j)

w

Gℓ; (x j) j∈Vℓ

.
Summation over G0 yields the factor 
1≤i< j≤n(1 + f (xi, x j)). Summation over the con-
nected graphs Gℓyields ϕT
|Vℓ|(xVℓ). Finally, summation over the edge sets Eℓyields the factor

1≤i≤n, j∈Vℓ(1 + f (xi, x j)) −1.
⊓⊔
