---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-016-82-circuit-augmentation-algorithms
section_title: "Circuit augmentation algorithms"
section_number: 8.2
pages: 29-31
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
The generic circuit augmentation algorithm is a circuit walk x(1),x (2),...,x (k+1)∈P as deﬁned
above, such that an initial feasible x(0) is given, and
⟨
c,x (t+1)⟩
<
⟨
c,x (t)⟩
, i.e., the objective
29
value decreases in every iteration. The elementary vector g is an augmenting direction for the
solution x(t) if and only if ⟨c,g⟩< 0, gi≥ 0 for every x(t)
i = 0 and gi≤ 0 for every x(t)
i = ui.
By LP duality, x(t) is optimal if and only if no augmenting direction exists. Oth erwise, the
algorithm proceeds to the next iterate x(t+1) by a maximal augmentation in an augmenting
direction.
The simplex algorithm can be seen as a circuit augmentation a lgorithm that is restricted
to using special elementary vectors corresponding to edges of the polyhedron. 2 For the general
framework, the iterates x(k) may not be vertices. However, in case of maximal augmentatio ns,
they must all lie on the boundary of the polyhedron.
In unpublished work, Bland [ Bla76] extended the Edmonds–Karp–Dinic algorithm [ Din70,
EK72] algorithm for general LP, see also [ Lee89, Proposition 3.1]. Circuit augmentation algo-
rithms were revisited by De Loera, Hemmecke, and Lee in 2015 [ DLHL15], analyzing diﬀerent
augmentation rules and extending them to integer programmi ng. We give an overview of their
results ﬁrst for linear programming. In particular, they st udied three augmentation rules that
use maximal augmentation. Let x(t) be the current feasible solution, and we aim to select an
augmenting direction g as follows.
• Dantzig-descent direction: Select g such that −⟨c,g⟩ is maximized, where g = gC is the
elementary vector with lcm( gC ) = 1 for a circuit C∈C W .
• Deepest-descent direction: Select g such that−α⟨c,g⟩ is maximized, where α is the max-
imal stepsize for x(t) and g.
• Steepest-descent direction: Select g such that−⟨c,g⟩/‖g‖1 is maximized.
Computing Dantzig- and deepest-descent directions is in ge neral NP-hard, see [ DLKS19] and
as detailed below. The steepest-descent direction can be fo rmulated by an LP; but without any
restrictions on the input problem, this may not be simpler th an the original one. However, it
could be easier to solve in practice; Borgwardt and Viss [ BV20] exhibits an implementation of
a steepest-descent circuit augmentation algorithm with en couraging computational results.
8.2.1 Augmenting directions for ﬂow problems
It is instructive to consider these algorithms for the speci al case of minimum-cost ﬂows . Given
a directed graph D = (V,E ) with capacities u∈ RE, costs c∈ RE, and node demands b∈ RV
with b(V ) = ∑
i∈V bi = 0. The objective is to ﬁnd the minimum cost ﬂow x that satisﬁes the
capacity constraints: 0 ≤x≤u, and the node demands: for each node i∈V , the total incoming
minus the total outgoing ﬂow equals bi. This can be written in the form LP(A,b,c,u ) withA as
the node-arc incidence matrix of D, a TU matrix. Let us deﬁne the residual graph Dx = (V,Ex),
where for (i,j )∈Ex we let (i,j )∈E if xij <u ij and (j,i )∈E if xij > 0. The cost of a reverse
arc will be deﬁned as cji =−cij. We will also refer to the residual capacities of arcs; these are
uij−xij in the ﬁrst case and xij in the second.
Let us observe that the augmenting directions correspond to directed cycles in the residual
graph. Circuit augmentation algorithms for the primal and d ual problems yield the rich classes
of cycle cancelling and cut cancelling algorithms, see the s urvey [ SIM00].
The maximum ﬂow problem between a source s and sink t can be formulated as a special
case as follows. We add a new arc ( t,s ) with capacity ∞, set the demands b≡ 0, and costs
as cts =−1 and cij = 0 otherwise. Bland’s [ Bla76] observation was that the steepest-descent
direction for this problem corresponds to ﬁnding a shortest residual s-t path, as chosen in the
Edmonds–Karp–Dinic algorithm.
2Simplex may contain degenerate pivots when the basic soluti on remains the same; we do not count these as
augmentation steps.
30
More generally, a steepest-descent direction amounts to ﬁn ding a residual cycle C⊆Ex that
minimizes the mean cycle cost c(C)/|C|. Thus, the steepest descent algorithm for minimum-cost
ﬂows corresponds to the classical Goldberg–Tarjan algorit hm [GT89] that is strongly polynomial
with running time O(|V|·| E|2) [ RG94].
Let us now consider the other two variants. A Dantzig-descen t direction in this context asks
for the most negative cycle, i.e., a cycle maximizing −c(C). A deepest-descent direction asks for
a cycleC of arcs that maximizes−αc(C), where α is the residual capacity of C. Computing both
these directions exactly is NP-complete, since they genera lize the Hamiltonian-cycle problem:
for every directed graph, we can set up a ﬂow problem where Ex coincides with the input graph,
all residual capacities are equal to 1, and all costs are −1. We note that De Loera, Kafer, and
Sanit` a [DLKS19] showed that computing the Dantzig- and deepest-descent di rections is also
NP-hard for the fractional matching polytope.
Nevertheless, the deepest-descent direction can be suitab ly approximated. Wallacher [ Wal89]
proposed selecting a minimum ratio cycle in the residual graph. This is a cycle in Ex that
minimizes c(C)/d(C), where de = 1/ue for every residual arc e ∈ Ex; such a cycle can be
found in strongly polynomial time. It is easy to show that thi s cycle approximates the deepest
descent direction within a factor |Ex|. Wallacher’s algorithm can be naturally extended to linear
programming [MS00], and has found several combinatorial applications, e.g. [ WZ99,Way02], and
has also been used in the context of integer programming [ SW99]. We discuss an improved new
variant in Section 8.3. A diﬀerent relaxation of the deepest-descent algorithm was given by
Barahona and Tardos [ BT89], based on Weintraub’s algorithm [ Wei74].
