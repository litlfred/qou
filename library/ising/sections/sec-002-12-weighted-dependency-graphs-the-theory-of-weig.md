---
doc_id: ising
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-002-12-weighted-dependency-graphs-the-theory-of-weig
section_title: "Weighted dependency graphs. The theory of weighted dependency graphs, recently intro-"
section_number: 1.2
pages: 3-4
source_pdf: ising.pdf
source_sha256: 9f84d7209731d299
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
duced by the second author in [10], is a toolbox to prove central limit theorems. It extends the
well-known concept of dependency graphs; see [1, 20].
Throughout the article, a weighted graph is a graph such that a weight we in [0, 1] is associated to
each edge e, where an edge of weight 0 is the same as no edge.
A spanning tree of a graph G = (V,E ) is a subset E′ of E such that (V,E′) is a tree. If G is an
edge-weighted graph, we deﬁne the weightw(T ) of a spanning treeT ofG as the product of the weights
of the edges in T . The maximum weight of a spanning tree of G is denotedM
(
G
)
. By convention, if
G is disconnected, we setM
(
G
)
= 0.
We are now ready to deﬁne weighted dependency graphs:
Deﬁnition 1.3. Let{Yα,α∈A} be a family of random variables with ﬁnite moments, deﬁned on the
same probability space; and let C = (C1,C 2,··· ) be a sequence of positive real numbers.
A weighted graph G is a C-weighted dependency graph for {Yα,α ∈ A} if, for any multiset
B ={α1,...,α r} of elements of A, one has
(1.1)
⏐⏐⏐⏐κ
(
Yα;α∈B
)⏐⏐⏐⏐≤CrM
(
G[B]
)
,
where G[B] denotes the graph induced by G on the vertex set B.
Remark 1.4. This is actually a simpliﬁed deﬁnition, suﬃcient for the purpose of this paper. It corre-
sponds to the case Ψ ≡ 1 of the general deﬁnition given in [10].
Informally, that a family of random variables {Ya,a∈A} admits a weighted graph G as weighted
dependency graph means the following:
• G has vertex-set A, i.e. we have one vertex in G per variable in{Ya,a∈A}.
• The smaller the weight of an edge {a,b} is, the closer to independent Ya andYb should be. In
particular, an edge of weight 0 – or equivalently no edge – between a andb means that Ya and
Yb are independent. This closeness to independence is not only measured, as one could expect,
by a bound on the covariance, but also involves bounds on higher order cumulants.
As we will see in Section 1.3, weighted dependency graphs allows one to easily obtain central limit
theorems. Another nice feature of weighted dependency graphs is the following stability property: a
weighted dependency graph for a family{Ya,a∈A} automatically gives a weighted dependency graph
for monomials YI =∏
a∈IYa in the Ya’s with a ﬁxed bound m on the degree (i.e. I runs over multiset
of elements ofA of size at most m). As a consequence, we can potentially prove central limit theorems
for sums of such monomials. We refer the reader to [10] for a detailed presentation of the theory of
weighted dependency graphs.
Let us come back to the Ising model. The bounds on joint cumulants of Theorem 1.1 can be
naturally translated in terms of weighted dependency graphs for the random variables {σi : i∈ Zd}.
In the next statement, and throughout the paper, we let ‖i−j‖1 denote the graph distance in Zd
between two points i and j.
Theorem 1.5. Letω = (σi(ω))i∈Zd be a spin conﬁguration distributed according toµβ,h, where (β,h )∈
R(β1,β 2,h 1). Let G be the complete weighted graph with vertex set Zd, such that every edge e ={i,j}
has weight we =ε(d)
‖i−j‖1
2 , where ε(d) comes from Theorem 1.1.
Then G is a C-weighted dependency graph for the family {σi : i∈ Zd}, for some sequence C =
(Cr)r≥1, depending only on d.
Theorem 1.5 is proved in Section 4.1.1. The proof uses Theorem 1.1, some general results of [10]
and elementary considerations. As explained above, this automatically yields a weighted dependency
graph for products of a ﬁnite number of spins, which will be presented in Theorem 4.6 below.
We conclude this subsection with the motivation behind Theorem 1.5. The Ising model is the
prototypical example of a Markov random ﬁeld. Recall that a Markov random ﬁeld on a graph G
