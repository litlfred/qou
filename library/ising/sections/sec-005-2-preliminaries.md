---
doc_id: ising
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-005-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 6-8
source_pdf: ising.pdf
source_sha256: 9f84d7209731d299
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
2.1. The Ising model. We consider the Ising model on a ﬁnite subset Λ of Zd. We use the notation
of [13], that we present now.
LetEΛ :={{i,j}⊂ Λ :‖i−j‖1 = 1} be the set of nearest neighbour pairs in Λ. To each spin
conﬁguration ω, we associate its Hamiltonian
HΛ;β,h(ω) :=−β
∑
{i,j}∈EΛ
σi(ω)σj(ω)−h
∑
i∈Λ
σi(ω),
whereβ≥ 0 andh are two real parameters, respectively called inverse temperature and magnetic ﬁeld.
The probability of a spin conﬁguration ω is given by the Gibbs distribution
µΛ;β,h(ω) := 1
ZΛ;β,h
e−HΛ;β,h(ω),
where
ZΛ;β,h :=
∑
ω∈{−1,1}Λ
e−HΛ;β,h(ω)
is called the partition function.
The quantities deﬁned so far are with “free boundary conditions”, which means that the value of
the spins outside of Λ is not taken into consideration. We can also deﬁne the same quantities with
boundary condition, by considering the Ising model on the full lattice Zd, but where the values of the
spins outside of Λ are ﬁxed. Fixing a spin conﬁguration η∈{− 1, 1}Zd
, we deﬁne a spin conﬁguration
in Λ with boundary condition η as an element of the set
Ωη
Λ :=
{
ω∈{− 1, 1}Zd
:ωi =ηi,∀i /∈ Λ
}
.
We now deﬁne the Hamiltonian as
Hη
Λ;β,h(ω) :=−β
∑
{i,j}∈Eb
Λ
σi(ω)σj(ω)−h
∑
i∈Λ
σi(ω),
whereEb
Λ :=
{
{i,j}⊂ Zd :‖i−j‖1 = 1 and{i,j}∩ Λ⁄=∅
}
.
The Gibbs distribution of the Ising model in Λ with boundary condition η and parameters β andh
is the probability distribution deﬁned on Ω η
Λ by
µη
Λ;β,h(ω) := 1
Zη
Λ;β,h
e−Hη
Λ;β,h(ω),
where
Zη
Λ;β,h :=
∑
ω∈Ωη
Λ
e−Hη
Λ;β,h(ω)
is the partition function with boundary condition η.
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 7
The most classical boundary conditions are the + boundary condition, where ηi = +1 for alli∈ Zd,
and the − boundary condition, where ηi =−1 for all i∈ Zd. When considering quantities with +
(resp.−) boundary condition, we write them with superscript + (resp. −), e.g. µ+
Λ;β,h(ω).
We now take an increasing sequence Λ n of ﬁnite subsets of Zd with ⋃
n≥1 Λn = Zd. It is a well-
known fact (see, e.g., [13, Chapter 3]) that the sequence of measures µ+
Λn;β,h converges in the weak
sense towards a measure denoted µ+
β,h as n→∞ . In the high temperature case ( β < βc(d), h= 0)
or in the presence of a magnetic ﬁeld ( h⁄= 0), the limiting measure is independent of the choice of
boundary conditions. At low temperature ( β > βc(d), h= 0), the limiting measure depends on the
boundary conditions; in this article, we restrict ourselves to + boundary conditions to have a well-
deﬁned limiting measure in all cases. Also, we drop the superscript + and denote the limiting measure
byµβ,h.
In this article, we work with this limiting measure µβ,h and prove our central limit theorem under
this measure. In comparison with the measure µ+
Λn;β,h, it has the advantage to be translation invariant,
which simpliﬁes in particular the variance estimates.
2.2. Spanning trees of maximal weight and tree lengths. We recall from the introduction that,
if G is an edge-weighted graph, we denote by M
(
G
)
the maximum weight of a spanning tree of G.
We will be mainly interested in the case where V is a ﬁnite subset A of Zd, E consists of all pairs
of vertices of A (i.e. we have a complete graph), and the weights are of the form w(i,j ) =ε‖i−j‖1 for
some positive constant ε< 1. We denote this weighted graph by G[A]. Then, for a spanning tree T of
G[A],
w(T ) =ε
∑
(i,j)∈T‖i−j‖1,
and the maximal such weight M
(
G[A]
)
is obtained by minimizing the quantity ∑
(i,j)∈T‖i−j‖1.
Therefore we deﬁne
𝓁′
T (A) = min
T
∑
(i,j)∈T
‖i−j‖1,
where the minimum is taken over all spanning trees T ofG[A], i.e. of the complete graph on A. Then
we haveM
(
G[A]
)
=ε𝓁′
T (A).
The quantity𝓁′
T (A) is sometimes referred to as the tree-length ofA. There is another closely related
notion of tree-length, used in the introduction, which is deﬁned as 𝓁T (A) = minB 𝓁′
T (A∪B), where
the minimum is taken over all ﬁnite subsets B of Zd. In other words, this is the minimum length of a
tree connecting vertices of A and possibly other vertices of Zd. Equivalently, this is the minimal size
of a connected set of edges of the lattice Zd such that each vertex of A is incident to at least one edge
in the set. These two notions of tree-length are illustrated on Fig. 1.
x1 = (0, 1)
x2 = (1, 0)
x3 = (0, −1)
x4 = (−1, 0)
1
𝓁T (A) = 4 𝓁′
T (A) = 6
1 1
1
2 2
2
x1 = (0, 1)
x2 = (1, 0)
x3 = (0, −1)
x4 = (−1, 0)
Figure 1. The two notions of tree-length on an example
In [5, page 197], Duneau, Iagolnitzer and Souillard proved the following bound, which will be useful
later in our computations.
