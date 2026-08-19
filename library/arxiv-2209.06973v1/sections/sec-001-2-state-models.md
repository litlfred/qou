---
doc_id: arxiv-2209.06973v1
doc_title: "On the geometry of two state models for the colored Jones polynomial"
section_id: sec-001-2-state-models
section_title: "State models"
section_number: 2
pages: 2-5
source_pdf: On_the_geometry_of_two_state_models_for_the_colore.pdf
source_sha256: cc3393a17c48b9df
doc_brief: "On the geometry of two state models for the colored Jones polynomial — Using the ﬂow property of the R-matrix deﬁning the colored Jones polynomial, we establish a natural bijection between the set of"
---
are isomorphic to each other in a well-deﬁned sense, even though the state
models are deﬁned on diﬀerent graphs.
Garoufalidis and Loebl also use their formula to deﬁne a non-commutative
(this means that the sum is calculated using non-commutative algebra, not
that the actual sum is non-commutative in some way) state-sum for the col-
ored Jones polynomial [7]. Independently Huynh and Le [10], see also [1],
deﬁned a non-commutative formula directly from the R-matrix deﬁned by
Rozansky [23]. There is recent work on the noncommutative approach, see
[2] and [9]. The relation between those two formulas is brieﬂy mentioned
in [10], Remark 0.1, but a detailed discussion of the relation of this is still
missing in the literature. The results of our article indicate that the two
noncommutative state models are also equivalent if there is a natural state-
sum deﬁned for the noncommutative formula of [7]. The states of [10] are
described in [1] in terms of walks on braids, with state-sum contributions
deﬁned by the actions of sequences of operators on a certain ring of polyno-
mials deﬁned from the walks. Algebraically the walks result from computing
the expansion of a quantum determinant of a matrix over a ring of operators
deﬁned through an analogy to the Burau representation, see [1] for more de-
tails. Here walks are deﬁned by sequences of overcrossings, undercrossings
and jump-down transitions.
In the literature there are often restrictions of formulas for the colored
Jones polynomial to the case of knots. This often seems in order to avoid
a discussion of which states are contributing (see Deﬁnition 2.1). We think
that this is in fact an interesting question, in particular when it comes to a
discussion of computational complexity. We will show that the formula [7]
2
based on the arc graph of knots extends to links.
In sections 2 and 3 we deﬁne state models and how to compare them.
We deﬁne the sets of decorated graphs we will be using. In section 4 we
deﬁne the bijections of states, which is used in the following sections to
show that the usual state model deﬁned from the ribbon functor (R-matrix)
is equivalent to the state model in [7]. In section 5 we review the ribbon
function deﬁnition, and in section 6 we give a direct proof of the state-sum
formula [7], which also shows the equivalence of the models and extends
the formula to link projections. In section 7 we show how the states in
both cases are determined by potentials, a notion introduced in section
4, and we show the contributing states are parametrized. Our approach
shows that the state-sums are determined without using any order of the
vertex set of the part arc-graph or arc-graph. In section 8 we we discuss the
computation when we choose the cyclic order of vertices, deﬁned by running
along components from chosen base points. In section 9 we explicitly give
the evaluation of the colored Jones polynomial for all weaving links on three
strings from the [7]. In section 10 we show how the state-sum of is computed
algorithmically from the braid word for all−-strand braid closures. We give
explicit examples of state-sum computations throughout the article.
2 State models
We will consider vertex models as deﬁned in [12], see also [24].
Deﬁnition 2.1. Let G be a set of (possibly in some way decorated) ﬁnite
graphs and let R be an integral domain (usually R = Z[t± 1
D ] for some
natural numberD). A state model on G assigns to each graphG = (V,E )∈
G (V is the vertex set, E is the edge set) a state-sum
Z(G) =
∑
f∈St(G)
Z(f) =
∑
f∈st(G)
Z(f)∈R
with Z(f) = ∆ ·β(f) ∈ R. The factor ∆ ⁄= 0 is a global contribution
deﬁned from the geometry and possible decorations of the graph but does
not depend on the coloring. The set St( G)⊂{ f : E→ Z} (Z could be
replaced by any countable set) is a set of edge-colorings, the states of the
state model. The factors β(f) :=∏
v∈V βv(f)∈R , are deﬁned locally. This
means that βv(f) depends only on edge-colorings of edges incident with v
or with adjacent vertices. The set of contributing states or admissible states
(see [24]) st(G) :={f∈ St|β(f)⁄= 0}⊂ St(G) is always ﬁnite so that Z(G)
3
is deﬁned. The condition f∈ st(G) is determined by local conditions on f,
conditions on the colorings at vertices. Note that β(f)⁄= 0 ⇐⇒βv(f)⁄=
0 for all v.
Remark. (a) Decoration on a graph includes direction, signs or numbers
attached to vertices and/or edges. Those decorations are not to be confused
with the edge-colorings.
(b) The above deﬁnition focuses on vertex contributions and is adapted to
state sums on braid projections. In the link projection case, additionally
colorings at extrema are included in the deﬁnition ofβ(f). This is necessary
so that the state sums deﬁne isotopy invariants.
Deﬁnition 2.2. Let G1, G2 be two sets of ﬁnite decorated graphs and
corresponding state models Z1,Z 2. Let Φ : G1 → G2. Suppose that
for each G ∈ G1 there is a surjective map of corresponding state sets
φG : St1(G)→ St2(Φ(G)) such that for each f∈ St2(Φ(G)) we have
Z2(f) =
∑
g∈st1(G):φG(g)=f
Z1(g)
Then we will say that the state modelZ1 dominates the state modelZ2 over
(Φ,φ = (φG)). If all maps φG are all bijections (so in particular restrict to
bijections st 1(G)→ st2(Φ(G)) then we call the two state models equivalent
over Φ.
Remark. Equivalence of the state-sum models can be stronger than equality
of the state-sums in R. Note that it follows that the sets of admissible
states for a graph G and its image Φ(G) correspond to each other under the
bijection φG.
Deﬁnition 2.3. An edge-coloring on a digraph G is a Z-ﬂow if
∑
e ingoing v
f(e) =
∑
e outgoing v
f(e) =:f(v).
LetF(G) denote the set of all Z-ﬂows onG. It is called a ﬂow if the image of
f is in N0 :={0, 1, 2,,... }. An n-ﬂow is a ﬂow withf(v)≤n for all vertices
v, i. e. f(v)∈{ 0, 1,...,n } =:n. The set of ﬂows respectively n-ﬂows on a
digraph G is denoted by F(G) respectivelyFn(G). Let Fn(G) denote the
set of ﬂows f on G with f(e)∈ n for all n, the n-bounded ﬂows. Note:
F(G)⊃F n(G)⊃F n(G).
Example. The ﬂow setF1(G) is in bijective correspondence with the set of
unions of vertex-disjoint directed cycles of G.
4
