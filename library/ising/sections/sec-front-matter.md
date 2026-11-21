---
doc_id: ising
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-8
source_pdf: ising.pdf
source_sha256: 9f84d7209731d299
toc_source: inferred
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL
JEHANNE DOUSSE AND VALENTIN F´ERAY
Abstract. Weighted dependency graphs have been recently introduced by the second author, as a
toolbox to prove central limit theorems. In this paper, we prove that spins in the d-dimensional Ising
model display such a weighted dependency structure. We use this to obtain various central limit
theorems for the number of occurrences of local and global patterns in a growing box.
1. Introduction and statement of results
1.1. Cumulants in the Ising model. The Ising model is a mathematical model of ferro-magnetism
in statistical physics. It was introduced in 1920 by Wilhelm Lenz who gave it as a problem to his
Ph.D. student Ernst Ising [19]. It can be deﬁned on any ﬁnite graph, but we restrict ourselves to ﬁnite
subsets Λ of Zd. For any lattice site i ∈Λ, there is a random variable σi which is equal to either 1 or
−1 and represents the spin at site i. A spin conﬁguration ω = (σi(ω))i∈Λ is an assignment of spins to
every site of Λ.
The distribution of spins depends on the magnetic ﬁeld h and the inverse temperature β in a way
that is detailed in Section 2.1. In particular, spins corresponding to neighbour sites i and j are more
likely to be equal. The bigger β is, i.e. the lower the temperature is, the more important is this
phenomenon.
In his Ph.D. thesis [19], Ising solved the model for the one-dimensional case d = 1, and showed
that there is no phase transition. But in 1936, Peierls [33] showed that, in dimensions 2 and 3, when
h = 0, the Ising model undergoes a phase transition at a critical inverse temperature βc. He used
a combinatorial argument now known as Peierls’ argument. The two-dimensional model for h = 0
was then exactly solved by Onsager [32] in 1944, using analytic techniques and the transfer matrix
method. It turns out that in higher dimensions, there is also a phase transition for h = 0 (see [33], or
[13] for a more modern treatment). However, there is no phase transition when there is a magnetic
ﬁeld h̸ = 0 [25, 36].
The Ising model is a priori deﬁned on a ﬁnite subset Λ ⊂Zd, but it is well-known that we can
take the thermodynamic limit Λ ↑Zd (see eg. [13]). This deﬁnes, for each pair of parameters (β, h),
a measure µβ,h on the set {−1, 1}Zd of spin conﬁgurations on the whole d-dimensional lattice Zd. In
low temperature without magnetic ﬁeld, i.e. β large and h = 0, this measure is not unique; we will
consider the one corresponding to + boundary conditions, see Section 2.1 for details.
The Ising model has been studied in thousands of research articles, under various aspects. Among
many others, a subject of interest has been the decay of joint cumulants of the spins (also called
truncated k-point functions or Ursell functions in the physics literature). Consider random variables
X1, . . . , Xr with ﬁnite moments deﬁned on the same probability space Their joint cumulant of order
r is deﬁned as
κ(X1, . . . , Xr) = [t1 . . . tr] log

exp(t1X1 + · · · + trXr)

,
where ⟨Y ⟩denotes the expectation of Y and the notation [t1 . . . tr]F stands for the coeﬃcient of t1 . . . tr
in the series expansion of F. The ﬁnite moments assumption ensures that this series expansion exists,
at least formally. The joint cumulant of order 2 is simply the covariance. If all random variables
2010 Mathematics Subject Classiﬁcation. 82B20,60F05.
Key words and phrases. Ising model, cumulants, central limit theorems, cluster expansions, weighted dependency
graphs.
Both authors are partially supported by grant SNF-149461 from Swiss National Science Fundation.
1
2
JEHANNE DOUSSE AND VALENTIN F´ERAY
X1, · · · , Xr are equal to the same variable X, then κr(X) := κ(X, . . . , X) is the usual cumulant of a
single random variable.
Joint cumulants have a long history in statistics and theoretical physics, see e.g. [35]. In the case
where the Xi’s are indicator functions of the presence of particles or + spins for example, they are often
referred to as truncated correlation functions or Ursell functions in the statistical physics literature.
In this paper, we will denote by κβ,h(σi1, . . . , σir) the joint cumulant of order r of spins σi1, . . . , σir,
with inverse temperature β and magnetic ﬁeld h.
Bounds on cumulants in the physics literature are often called cluster properties. There is in fact a
hierarchy of cluster properties, corresponding to sharper or weaker bounds on cumulants; we refer to
[5] or [26, Chapter 6, §1] for deﬁnitions of various kinds of cluster properties.
In the case of the Ising model, a ﬁrst bound on cumulants was obtained by Martin-L¨of [27, Eq. (20)]
— see also [24, Section 1] —: he proved that the joint cumulant κβ,h(σi; i ∈A) decreases exponentially
in diam(A)/r, where diam(A) is the the diameter of A and r the order of the cumulants.
In [6],
Duneau, Iagolnitzer and Souillard sharpened this bound in presence of a magnetic ﬁeld (h̸ = 0), or for
h = 0 and very high temperature: κβ,h(σi; i ∈A) decays exponentially in ℓT (A). Here ℓT (A) denotes
the tree-length of A, i.e. the minimal size of a connected set of edges of the lattice Zd such that each
vertex of A is incident to at least one edge in the set. In [26], Malyshev and Minlos have a similar result
in the case h = 0 and very low temperature. Both their approaches use cluster expansion, a powerful
tool introduced by Mayer and Montroll [28], which is now standard in the study of the Ising model.
Both proofs use additional ingredients of diﬀerent nature: Duneau, Iagolnitzer and Souillard use the
Lee-Yang circle theorem and complex analysis arguments, while Malyshev’s and Minlos’ approach
relies on combinatorial developments and bounds on joint cumulants for contours as an intermediate
step.
These bounds on cumulants will be our starting point to prove central limit theorems for patterns in
the Ising model. In order to make the article more self-contained, we give a simpler and more uniﬁed
approach of the decays of joint cumulants in several regimes where the cluster expansion converges.
To do so, for β1, β2, h1 > 0, let us introduce the three diﬀerent regimes
RHT (β1, h1) := {(β, h) : 0 ≤β < β1, |h| ≤h1}
(very high temperature),
RLT (β2) := {(β, h) : β > β2, h = 0}
(very low temperature),
RSF (h1) := {(β, h) : |h| > h1}
(strong magnetic ﬁeld),
and their union
R(β1, β2, h1) = RHT (β1, h1) ∪RLT (β2) ∪RSF (h1).
The result is stated as follows.
Theorem 1.1. We consider the Ising model on Zd with parameters (β, h). There exist positive con-
stants ε(d) < 1, β1 = β1(d), β2 = β2(d) and h1 = h1(d) depending on the dimension d, and for any
integer r ≥1 a constant Dr such that for all A = {i1, . . . , ir} ⊂Zd, we have

κβ,h(σi1, . . . , σir)

 ≤Drε(d)ℓT (A),
for any (β, h) ∈R(β1, β2, h1).
The notion of tree-length ℓT (A) is important to make the connection with weighted dependency
graphs, which we discuss now.
Remark 1.2. In the very high temperature and strong magnetic ﬁeld regimes, one can chose ε(d)
independent of the dimension and Dr = 1 for all r ≥1 (see the end of Section 3.1). This choice of Dr
is important to study the speed of convergence in the central limit theorem for the magnetization (see
[11, Section 5.3]), but is irrelevant for the purpose of the present article.
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL
3
1.2. Weighted dependency graphs. The theory of weighted dependency graphs, recently intro-
duced by the second author in [10], is a toolbox to prove central limit theorems.
It extends the
well-known concept of dependency graphs; see [1, 20].
Throughout the article, a weighted graph is a graph such that a weight we in [0, 1] is associated to
each edge e, where an edge of weight 0 is the same as no edge.
A spanning tree of a graph G = (V, E) is a subset E′ of E such that (V, E′) is a tree. If G is an
edge-weighted graph, we deﬁne the weight w(T) of a spanning tree T of G as the product of the weights
of the edges in T. The maximum weight of a spanning tree of G is denoted M
 G

. By convention, if
G is disconnected, we set M
 G

= 0.
We are now ready to deﬁne weighted dependency graphs:
Deﬁnition 1.3. Let {Yα, α ∈A} be a family of random variables with ﬁnite moments, deﬁned on the
same probability space; and let C = (C1, C2, · · · ) be a sequence of positive real numbers.
A weighted graph G is a C-weighted dependency graph for {Yα, α ∈A} if, for any multiset
B = {α1, . . . , αr} of elements of A, one has
(1.1)

κ
 Yα; α ∈B


 ≤Cr M
 G[B]

,
where G[B] denotes the graph induced by G on the vertex set B.
Remark 1.4. This is actually a simpliﬁed deﬁnition, suﬃcient for the purpose of this paper. It corre-
sponds to the case Ψ ≡1 of the general deﬁnition given in [10].
Informally, that a family of random variables {Ya, a ∈A} admits a weighted graph G as weighted
dependency graph means the following:
• G has vertex-set A, i.e. we have one vertex in G per variable in {Ya, a ∈A}.
• The smaller the weight of an edge {a, b} is, the closer to independent Ya and Yb should be. In
particular, an edge of weight 0 – or equivalently no edge – between a and b means that Ya and
Yb are independent. This closeness to independence is not only measured, as one could expect,
by a bound on the covariance, but also involves bounds on higher order cumulants.
As we will see in Section 1.3, weighted dependency graphs allows one to easily obtain central limit
theorems. Another nice feature of weighted dependency graphs is the following stability property: a
weighted dependency graph for a family {Ya, a ∈A} automatically gives a weighted dependency graph
for monomials YI = Q
a∈I Ya in the Ya’s with a ﬁxed bound m on the degree (i.e. I runs over multiset
of elements of A of size at most m). As a consequence, we can potentially prove central limit theorems
for sums of such monomials. We refer the reader to [10] for a detailed presentation of the theory of
weighted dependency graphs.
Let us come back to the Ising model.
The bounds on joint cumulants of Theorem 1.1 can be
naturally translated in terms of weighted dependency graphs for the random variables {σi : i ∈Zd}.
In the next statement, and throughout the paper, we let ∥i −j∥1 denote the graph distance in Zd
between two points i and j.
Theorem 1.5. Let ω = (σi(ω))i∈Zd be a spin conﬁguration distributed according to µβ,h, where (β, h) ∈
R(β1, β2, h1). Let G be the complete weighted graph with vertex set Zd, such that every edge e = {i, j}
has weight we = ε(d)
∥i−j∥1
2
, where ε(d) comes from Theorem 1.1.
Then G is a C-weighted dependency graph for the family {σi : i ∈Zd}, for some sequence C =
(Cr)r≥1, depending only on d.
Theorem 1.5 is proved in Section 4.1.1. The proof uses Theorem 1.1, some general results of [10]
and elementary considerations. As explained above, this automatically yields a weighted dependency
graph for products of a ﬁnite number of spins, which will be presented in Theorem 4.6 below.
We conclude this subsection with the motivation behind Theorem 1.5.
The Ising model is the
prototypical example of a Markov random ﬁeld. Recall that a Markov random ﬁeld on a graph G
4
JEHANNE DOUSSE AND VALENTIN F´ERAY
with vertex set A is a family of random variables {Ya, a ∈A} such that, for subsets B, B′, B′′ ⊂A,
{Ya, a ∈B} and {Ya, a ∈B′} are independent conditionally on {Ya, a ∈B′′} as soon as every path
going from B to B′ in G goes through B′′; this is also sometimes called global Markov property [23].
Informally, in a Markov random ﬁeld, a variable interacts directly only with its neighbours. We
can thus expect that the dependency between variables is weaker when their distance in the graph G
increases. Indeed, such variables only interact through all variables lying between them in the graph.
In other terms, we expect to have a weighted dependency graph which is complete (because there is
no reason to have unconditionally independent variables), but whose weights decrease with the graph
distance. This was observed in the case of Markov chains, which are one-dimensional Markov random
ﬁelds, in [10, Section 10]. The present paper gives such a statement for the d-dimensional Ising model.
In both cases, weights decrease exponentially with the graph distance.
1.3. Central limit theorems. Central limit theorems (CLTs) play a key role in probability theory
and have also been a subject of interest in the study of the Ising model.
We refer to the second
edition of Georgii’s classical book [14, Bibliographic Notes on Section 8.2, p.469] for an overview of
the diﬀerent methods used to obtain such results. The goal of this paper is to prove new central limit
theorems, using the weighted dependency graph technique. To this end, we shall use the following
normality criterion, which is a slightly modiﬁed version of the main theorem in [10].
Theorem 1.6. Suppose that, for each n, {Yn,i, 1 ≤i ≤Nn} is a family of random variables with ﬁnite
moments deﬁned on the same probability space. Let C = (Cr)r≥1 be a ﬁxed sequence that does not
depend on n.
Assume that, for each n, one has a C-weighted dependency graph Gn for {Yn,i, 1 ≤j ≤Nn} and
denote ∆n −1 its maximal weighted degree.
Let Xn = PNn
i=1 Yn,i and v2
n = V ar(Xn). Assume that there exists a sequence (an), an integer s ≥3
and a real number v such that
(1) v2
n
a2n
−−−−→
n→∞v2,
(2) for all n, a2
n ≤C2Nn∆n,
(3)
Nn
∆n
 1
s ∆n
an
−−−−→
n→∞0.
Then in distribution,
Xn −E(Xn)
an
d
−−−−→
n→∞N(0, v2).
Remark 1.7. The proof of Theorem 1.6 is almost identical to the proof of the normality criterion in
[10, Section 4.3] replacing σn by an. Indeed, as noticed in [10, Section 4.3], in the special case Ψ ≡1
to which we restrict ourselves in this article, the quantities Rn and Qn deﬁned there can be replaced
respectively by Nn (the number of vertices) and ∆n (the maximal weighted degree plus one).
Recall from the previous section that spins, and therefore products of spins, admit a weighted
dependency graph. The normality criterion above can thus be used to ﬁnd CLTs for polynomials of
spins in a growing box Λn := [−n, n]d. To illustrate this, we consider number of occurrences of two
kinds of spin patterns: local and global patterns.
We deﬁne a local pattern P to be a pair (D, s), where D is a ﬁnite subset of Zd containing 0
and s is a function D −→{+, −}. The cardinality of D is called the size of the pattern P. An
example of local pattern is a positive spin surrounded by negative ones. In that case the subset is
D = {j ∈Zd : ∥j∥1 ≤1}, while the sign function is given by s(0) = + and s(j) = −for all j ∈D \ {0}.
This pattern has size 2d+1. An occurrence of a local pattern P = (D, s) is a set {(i+j, s(j)) : j ∈D},
where i ∈Zd is the position of the occurrence.
While in local patterns we consider spins that are at a ﬁxed distance from one another, in global
patterns they can be as far as we want, as long as they have a certain global shape. Formally, we deﬁne
a global pattern ˜P of size m to be a pair (O, s), where O = (≤1, . . . , ≤d) is a d-tuple of total orders
over {1, . . . , m}, and s is a function {1, . . . , m} −→{+, −}. An occurrence of ˜P in a spin conﬁguration
ω is a set {x(1), . . . , x(m)} of m elements of Zd such that there exists some ordering (x(1), . . . , x(m)) of
these elements such that
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL
5
(1) for all i ∈{1, . . . , m}, σx(i)(ω) = s(i),
(2) for all i, j ∈{1, . . . , m}, for all k ∈{1, . . . d}, x(i)
k
≤x(j)
k
if and only if i ≤k j.
For example, if d = 2, ≤1, ≤2 are both the natural ordering and s(i) = + for all i, then an occurrence of
the global pattern (O, s) is a set of m positive spins such that each of them is located to the North-East
of the previous one.
CLTs for local and global patterns in other structures than the Ising model have attracted attention
in the literature. We mention Markov chains (see [34, 12, 10] and references therein), patterns in ran-
dom permutations (see [2, 21] for global patterns and [16, 2, 7] for local patterns) and arc conﬁgurations
in random set-partitions (CLTs for the number of arcs of size 1, which is a local pattern, and the num-
ber of crossings, which is a global pattern, were given in [4]). Note that Markov chains are (discrete)
one-dimensional Markov random ﬁelds, while the random permutation model is a non-Markovian two-
dimensional model (when considering patterns, we think of permutations as permutation matrices).
Finding such CLT results in Markov random ﬁelds of dimension two or more, and in particular in the
Ising model, is therefore a natural problem.
We ﬁrst prove a CLT for local patterns. Let Sn,P denote the number of occurrences of a given local
pattern P in Λn.
Theorem 1.8. Consider the Ising model on Zd, with inverse temperature β and magnetic ﬁeld h, such
that (β, h) ∈R(β1, β2, h1). Let P be a local pattern. Then
Sn,P −E(Sn,P)
p
|Λn|
d
−−−−→
n→∞N(0, v2
P),
where
v2
P = lim
n→∞
Var(Sn,P)
|Λn|
.
Similarly, if Sn, ˜
P denotes the number of occurrences of a global pattern ˜P in Λn, we have the
following result.
Theorem 1.9. Consider the Ising model on Zd, with inverse temperature β and magnetic ﬁeld h, such
that (β, h) ∈R(β1, β2, h1). Let ˜P be a global pattern of size m. We assume that, for some positive
constants A and η
(1.2)
Var(Sn, ˜
P) ≥A|Λn|2m−2+η.
Then
Sn, ˜
P −E(Sn, ˜
P)
q
Var(Sn, ˜
P)
d
−−−−→
n→∞N(0, 1).
We do not have in general an estimate for the variance Var(Sn, ˜
P). However, when the pattern
consists of positive spins only, we can prove that (1.2) is satisﬁed (with η = 1) — see Proposition 4.10
below. The reverse inequality Var(Sn, ˜
P) ≤B|Λn|2m−1 is always fulﬁlled (see the proof of Theorem 1.9).
We ﬁnish this introduction with a comparison with other methods. Standard methods to get CLT
in random ﬁelds are mixing properties [29] or FKG inequalities [30, 31]. It seems that the CLT for
local patterns can be easily obtained with these methods. Indeed, in an exponentially mixing ﬁeld
such as the Ising model, if we denote ZP
i the characteristic function of the occurrence of P in position
i (see (4.3)), then the ﬁeld (ZP
i )i∈Zd is also exponentially mixing and we can use the criterion given by
Neaderhouser [29, Section 3]. CLT for functions of neighbouring spins are also accessible with methods
based on FKG inequalities, see [31] for a general result in this direction.
On the contrary, we do not know how to adapt these methods to global patterns. Obtaining a CLT
for subword occurrences in Markov chains (the analogue problem in one-dimensional Markov ﬁeld) is
already a diﬃcult problem, see [3, 12] for some history on this problem. The technique of dependency
graphs gives access to CLTs for such global patterns, as shown in Theorem 1.9.
6
JEHANNE DOUSSE AND VALENTIN F´ERAY
In principle, it would also be feasible to mix local and global conditions (as in vincular patterns for
permutations [18]) or to consider more generally polynomials in X+
i
= 1+σi
2
and X−
i
= 1−σi
2
, in the
spirit of [15]; a major diﬃculty is then to get general estimates for the variance.
1.4. Outline of the paper. The remainder of the paper is organised as follows. In Section 2, we give
some preliminary deﬁnitions and basic results about the Ising model and tree lengths. In Section 3,
we discuss the cluster expansion for the Ising model in the three diﬀerent regimes we consider (very
high temperature, very low temperature, high magnetic ﬁeld), and deduce bounds on joint cumulants.
In Section 4, we use the theory of weighted dependency graphs to prove our central limit theorems.
Note: all constants throughout the paper depend on the dimension d of the space and we shall not
make it explicit from now on.
2. Preliminaries
2.1. The Ising model. We consider the Ising model on a ﬁnite subset Λ of Zd. We use the notation
of [13], that we present now.
Let EΛ := {{i, j} ⊂Λ : ∥i −j∥1 = 1} be the set of nearest neighbour pairs in Λ.
To each spin
conﬁguration ω, we associate its Hamiltonian
HΛ;β,h(ω) := −β
X
{i,j}∈EΛ
σi(ω)σj(ω) −h
X
i∈Λ
σi(ω),
where β ≥0 and h are two real parameters, respectively called inverse temperature and magnetic ﬁeld.
The probability of a spin conﬁguration ω is given by the Gibbs distribution
µΛ;β,h(ω) :=
1
ZΛ;β,h
e−HΛ;β,h(ω),
where
ZΛ;β,h :=
X
ω∈{−1,1}Λ
e−HΛ;β,h(ω)
is called the partition function.
The quantities deﬁned so far are with “free boundary conditions”, which means that the value of
the spins outside of Λ is not taken into consideration. We can also deﬁne the same quantities with
boundary condition, by considering the Ising model on the full lattice Zd, but where the values of the
spins outside of Λ are ﬁxed. Fixing a spin conﬁguration η ∈{−1, 1}Zd, we deﬁne a spin conﬁguration
in Λ with boundary condition η as an element of the set
Ωη
Λ :=
n
ω ∈{−1, 1}Zd : ωi = ηi, ∀i /∈Λ
o
.
We now deﬁne the Hamiltonian as
Hη
Λ;β,h(ω) := −β
X
{i,j}∈Eb
Λ
σi(ω)σj(ω) −h
X
i∈Λ
σi(ω),
where Eb
Λ :=

{i, j} ⊂Zd : ∥i −j∥1 = 1 and {i, j} ∩Λ̸ = ∅
	
.
The Gibbs distribution of the Ising model in Λ with boundary condition η and parameters β and h
is the probability distribution deﬁned on Ωη
Λ by
µη
Λ;β,h(ω) :=
1
Zη
Λ;β,h
e−Hη
Λ;β,h(ω),
where
Zη
Λ;β,h :=
X
ω∈Ωη
Λ
e−Hη
Λ;β,h(ω)
is the partition function with boundary condition η.
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL
7
The most classical boundary conditions are the + boundary condition, where ηi = +1 for all i ∈Zd,
and the −boundary condition, where ηi = −1 for all i ∈Zd. When considering quantities with +
(resp. −) boundary condition, we write them with superscript + (resp. −), e.g. µ+
Λ;β,h(ω).
We now take an increasing sequence Λn of ﬁnite subsets of Zd with S
n≥1 Λn = Zd. It is a well-
known fact (see, e.g., [13, Chapter 3]) that the sequence of measures µ+
Λn;β,h converges in the weak
sense towards a measure denoted µ+
β,h as n →∞. In the high temperature case (β < βc(d), h = 0)
or in the presence of a magnetic ﬁeld (h̸ = 0), the limiting measure is independent of the choice of
boundary conditions. At low temperature (β > βc(d), h = 0), the limiting measure depends on the
boundary conditions; in this article, we restrict ourselves to + boundary conditions to have a well-
deﬁned limiting measure in all cases. Also, we drop the superscript + and denote the limiting measure
by µβ,h.
In this article, we work with this limiting measure µβ,h and prove our central limit theorem under
this measure. In comparison with the measure µ+
Λn;β,h, it has the advantage to be translation invariant,
which simpliﬁes in particular the variance estimates.
2.2. Spanning trees of maximal weight and tree lengths. We recall from the introduction that,
if G is an edge-weighted graph, we denote by M
 G

the maximum weight of a spanning tree of G.
We will be mainly interested in the case where V is a ﬁnite subset A of Zd, E consists of all pairs
of vertices of A (i.e. we have a complete graph), and the weights are of the form w(i, j) = ε∥i−j∥1 for
some positive constant ε < 1. We denote this weighted graph by G[A]. Then, for a spanning tree T of
G[A],
w(T) = ε
P
(i,j)∈T ∥i−j∥1,
and the maximal such weight M
 G[A]

is obtained by minimizing the quantity P
(i,j)∈T ∥i −j∥1.
Therefore we deﬁne
ℓ′
T (A) = min
T
X
(i,j)∈T
∥i −j∥1,
where the minimum is taken over all spanning trees T of G[A], i.e. of the complete graph on A. Then
we have M
 G[A]

= εℓ′
T (A).
The quantity ℓ′
T (A) is sometimes referred to as the tree-length of A. There is another closely related
notion of tree-length, used in the introduction, which is deﬁned as ℓT (A) = minB ℓ′
T (A ∪B), where
the minimum is taken over all ﬁnite subsets B of Zd. In other words, this is the minimum length of a
tree connecting vertices of A and possibly other vertices of Zd. Equivalently, this is the minimal size
of a connected set of edges of the lattice Zd such that each vertex of A is incident to at least one edge
in the set. These two notions of tree-length are illustrated on Fig. 1.
x1 = (0, 1)
x2 = (1, 0)
x3 = (0, −1)
x4 = (−1, 0)
1
ℓT(A) = 4
ℓ′
T(A) = 6
1
1
1
2
2
2
x1 = (0, 1)
x2 = (1, 0)
x3 = (0, −1)
x4 = (−1, 0)
Figure 1. The two notions of tree-length on an example
In [5, page 197], Duneau, Iagolnitzer and Souillard proved the following bound, which will be useful
later in our computations.
8
JEHANNE DOUSSE AND VALENTIN F´ERAY
Proposition 2.1. For all A = {x1, . . . , xn} ﬁnite subset of Zd, we have
ℓT (A) ≤ℓ′
T (A) ≤2ℓT (A).
3. Cluster expansions and bounds on joint cumulants
The cluster expansion is a powerful tool in statistical mechanics, which consists in studying a system
in terms of macroscopic geometrical objects instead of considering its original microscopic components.
It was introduced in a work of Mayer and Montroll [28] studying molecular distribution and has since
been used in several other topics; for the Ising model, see for example [9] or Chapter 5 of [13]. In this
section, we will use the cluster expansion in three diﬀerent regimes of the Ising model to prove the
bounds on joint cumulants of Theorem 1.1. This will later be useful to apply the theory of weighted
dependency graphs. Theorem 1.1 is proved in Sections 3.1.2, 3.2.2 and 3.3, depending on the considered
regime.
Remark 3.1. In each section below, we use some classical notation for cluster expansion, such as Ξ, W,
X, . . . Note however that these quantities may have diﬀerent meanings in diﬀerent regimes. Since they
are only used for the proof of Theorem 1.1 and since the proofs in the diﬀerent regimes are independent
from each other, this should not create any diﬃculty.
