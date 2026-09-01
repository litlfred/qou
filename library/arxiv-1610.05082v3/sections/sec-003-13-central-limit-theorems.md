---
doc_id: arxiv-1610.05082v3
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-003-13-central-limit-theorems
section_title: "Central limit theorems"
section_number: 1.3
pages: 2-4
source_pdf: 1610.05082v3.pdf
source_sha256: 90c8089953ff2d97
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
patterns in the Ising model. In order to make the article more self-contained, we give a simpler
and more uniﬁed approach of the decays of joint cumulants in regimes, where the cluster expansion
converges. The result is stated as follows.
Theorem 1.1. We consider the Ising model on Zd with parameters (β,h ). There exist positive con-
stants ε(d) < 1, β1(d), β2(d) and h1(d) depending on the dimension d with the following property.
Assume we are in one of three following regimes:
very low temperature: β >β2(d) and h = 0;
very high temperature: β <β1(d) and h = 0;
strong magnetic ﬁeld: h>h 1(d).
Then for any r≥ 1, there exists a constant Dr such that for all A ={i1,...,i r}⊂ Zd, we have
⏐⏐κβ,h(σi1,...,σ ir)
⏐⏐≤Drε(d)𝓁T (A).
That the tree-length appears as exponent is important to make the connection with weighted de-
pendency graphs, which we discuss now.
1.2. Weighted dependency graphs. The theory of weighted dependency graphs, recently intro-
duced in [8], is a toolbox to prove central limit theorems. It extends the well-known concept of
dependency graphs; see [1, 16].
Throughout the article, a weighted graph is a graph such that a weightwe in [0, 1] is associated with
each edge e, where a weight 0 is the same as no edge. Informally, that a family of random variables
{Ya,a∈A} admits a weighted graph G as weighted dependency graph means the following:
• G has vertex-set A, i.e. we have one vertex in G per variable in{Ya,a∈A};
• the smaller the weight of an edge {a,b} is, the closer to independent Ya and Yb should be. In
particular, an edge of weight 0, or equivalently no edge between a and b, means that Ya and
Yb are independent.
Formally, this closeness to independence is not only measured by a bound on the covariance (as could be
expected), but also involves bounds on higher order cumulants (see Deﬁnition 2.3 for more precision).
Suppose now that, for each n, the family of random variables {Ya,n,a ∈ An} has a weighted
dependency graph Gn. Consider the renormalised sum ~Xn = 1
an
(∑
a∈AnYa,n
)
. Under some easy-to-
check conditions on the renormalising factor an, the variance of ~Xn and the maximal weighted degree
of Gn, ~Xn tends in distribution towards a Gaussian law (see Theorem 2.4). In short, the theory of
weighted dependency graph is a black box to prove central limit theorems.
A nice feature of weighted dependency graphs is the following stability property: a weighted depen-
dency graph for a family{Ya,a∈A} automatically gives a weighted dependency graph for monomials
YI =∏
a∈IYa in the Ya’s with a ﬁxed bound on the degree (here, I is a multiset of elements of A). As
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 3
a consequence, we can potentially prove central limit theorems for sums of such monomials. We refer
the reader to [8] for a detailed presentation of the theory of weighted dependency graphs.
Let us come back to the Ising model. The bounds on joint cumulants of Theorem 1.1 can be
naturally translated in terms of weighted dependency graphs for the random variables {σi :i∈ Zd}.
Theorem 1.2. Letω = (σi(ω))i∈Zd be a spin conﬁguration distributed according to µβ,h, where either
h > h1(d) or (h = 0; β < β1(d)) or (h = 0; β > β2(d)). Let G be the complete weighted graph with
vertex set Zd, such that every edge e = (i,j ) has weight we = ε(d)
‖i−j‖1
2 , where ε(d) comes from
Theorem 1.1.
Then G is a C-weighted dependency graph for the family {σi : i∈ Zd}, for some sequence C =
(Cr)r≥1.
Theorem 1.2 is proved in Section 4.1.1. The proof uses Theorem 1.1, some general results of [8]
and elementary considerations. As explained above, this automatically yields a weighted dependency
graph for products of a ﬁnite number of spins, which will be presented in Theorem 4.7 below.
We conclude Section 1.2 with the motivation behind Theorem 1.2. The Ising model is the prototyp-
ical example of a Markov random ﬁeld. (Recall that a Markov random ﬁeld on a graph G with vertex
set A is a family of random variables {Ya,a∈A} such that, for subsets A1, A2 and A3,{Ya,a∈A1}
and{Ya,a∈A2} are independent conditionally on {Ya,a∈A3} as soon as every path going from A1
to A2 in G goes through A3; this is also sometimes called global Markov property [18]).
Informally, in a Markov random ﬁeld, a variable interacts directly only with its neighbours. We
can thus expect that the dependency between variables is weaker when their distance in the graph G
increases (since such variables only interact through all variables lying between them in the graph).
In other terms, we expect to have a weighted dependency graph that is complete (because there is
no reason to have unconditionally independent variables), but whose weights decrease with the graph
distance. This was observed in the case of Markov chains (one-dimensional Markov random ﬁeld) in
[8, Section 10] and the present paper gives such a statement for the d-dimensional Ising model. In
both cases, weights decrease exponentially with the graph distance.
1.3. Central limit theorems. Central limit theorems (CLTs) play a key role in probability theory
and have also been a subject of interest in the study of the Ising model. We refer to the second edition
of Georgii’s classical book [11, Bibliographic Notes on Section 8.2, p469] for an overview of the diﬀerent
methods used to get such results.
The theory of weighted dependency graphs gives access to CLTs for the number of occurrences of
patterns of spins in a growing box Λn := [−n,n ]d. To illustrate this, we consider two kinds of patterns:
local and global patterns.
We deﬁne a local pattern P to be a pair ( D, s), where D is a ﬁnite subset of Zd containing 0
and s is a function D −→ {+,−}. The cardinality of D is called the size of the pattern P. An
example of local pattern is a positive spin surrounded by negative ones. In that case the subset is
D ={j∈ Zd :‖j‖1≤ 1}, while the sign function is given by s(0) = + and s(j) =− for all j∈D\{ 0}.
This pattern has size 2d + 1. An occurrence of a local patternP = (D, s) is a set{(i +j, s(j)) :j∈D} ,
where i∈ Zd is the position of the occurrence.
While in local patterns we consider spins that are at a ﬁxed distance from one another, in global
patterns they can be as far as we want, as long as they have a certain global shape. Formally, we deﬁne
a global pattern ˜P of size m to be a pair (O, s), whereO = (≤1,..., ≤d) is a d-tuple of total orders
over{1,...,m }, and s is a function{1,...,m }−→{ +,−}. An occurrence of ˜P in a spin conﬁguration
ω is a set{x(1),...,x (m)} ofm elements of Zd such that there exists some ordering (x(1),...,x (m)) of
these elements such that
(1) for all i∈{ 1,...,m }, σx(i)(ω) = s(i),
(2) for all i,j ∈{ 1,...,m }, for all k∈{ 1,...d }, x(i)
k ≤x(j)
k if and only if i≤k j.
4 JEHANNE DOUSSE AND VALENTIN F ´ERAY
For example, if d = 2, ≤1,≤2 are both the natural ordering and s(i) = + for all i, then the global
pattern (O, s) is a North-East chain of m positive spins.
