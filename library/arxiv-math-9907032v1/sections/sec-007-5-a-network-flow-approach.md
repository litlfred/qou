---
doc_id: arxiv-math-9907032v1
doc_title: "Mathematics Department, California Institute of Technolog y"
section_id: sec-007-5-a-network-flow-approach
section_title: "A NETWORK FLOW APPROACH"
section_number: 5
pages: 13-16
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
There is an alternative way to prove Theorem 3.3 which uses the Max F low-Min Cut
theorem of network ﬂow instead of the duality theorem of linear pro gramming. It
should be noted that the diﬀerence between the two arguments is la rgely superﬁcial,
since the proof of Theorem 3.3 can be seen to essentially prove the M ax Flow-Min
Cut theorem. There are two reasons to set up the question as a re sult on network
ﬂow. The ﬁrst is that the proof (hopefully) becomes clearer and mo re intuitive.
The second is that the special sorts of linear programs that arise in the theory of
network ﬂow have been heavily analyzed from the viewpoint of comple xity, which
will allow us to give a very satisfactory estimate (section 8) for the r unning time
of an algorithm to determine whether a structure with prescribed d ihedral angles
actually exists.
· 14
A network is a directed (multi)graph N , with two distinguished vertices – s (the
source), and S (the sink). Each edge of N has a certain capacity, which is a real
number, which is an upper bound on the amount of the commodity whic h can ﬂow
from the tail to the head of the edge. A cutset C of N is a collection of edges, the
removal of which leavess andS in two diﬀerent connected components of N \C. The
capacity of the cutset C is simply the sum of the capacities of the edges comprising
C. The capacity of an empty collection of edges is, of course, 0.
The Max Flow-Min Cut theorem of network ﬂow (see, for example, [26 , Chapter
7]) says the following:
Theorem 5.1 ( Max Flow – Min Cut ). The maximal amount of a commod-
ity that can ﬂow from the source s to the sink S of a network N is equal to the
capacity of the smallest cutset in N .
This theorem can be proved in a number of ways. The interested rea der can
adapt the proof of Theorem 3.3 to show Theorem 5.1.
To use Theorem 5.1 for our purposes, we need to set up a network o f a special
sort, starting with a triangulation T .
The vertices of this network are divided into four classes: {s},F (T ), E(T ), and
{S}.
The source s is connected to all of the vertices corresponding to the faces of T
with edges of capacity 1. We call them edges of level 1. Every vertex corresponding
to a face t is connected to the three vertices, corresponding to the three e dges of
t by edges of capacity 1. These are edges of level 2. Finally, each e ∈ E(T ) is
connected to the sink S by an edge of capacity δ(e). These are edges of level 3 .
The following statement is self-evident:
Observation 5.2. There exists a solution of the linear program L1 if and only
if the maximal ﬂow through the above-constructed network N1 is equal to |F (T )|.
Proof of theorem 3.1. Consider a cut C ofN1. This will have some edges at
level 1, removing which which will disconnect a subset F0 of the faces of T from the
source. It is then not necessary to remove any edges of level 2 em anating from F0.
Let F (T )\F0 =F1. Let F2 ⊆F1 be those faces f for which the cutset contains all
three edges of level 2 emanating from f . Finally, F3 =F1\F2. All of the edges of
level 3 (indirectly) emanating from F3 must be in the cutset C. These are precisely
the edges corresponding to the edges of the subcomplex of T whose faces are in F3.
What is the capacity of C? Evidently, it is equal to
F0 + 3F2 +
∑
e∈E(F3)
δ(e).
If we want the ﬂow through N1 to be F , we must have
F0 + 3F2 +
∑
e∈E(F3)
δ(e) ≥F,
Or, noting that F1 =F −F0,
3F2 +
∑
e∈E(F3)
δ(e) ≥F1.
· 15
In the special case where F2 = 0, it follows that
∑
e∈E(F3)
δ(e) ≥F. (20)
SinceF3 could have been any subset of F , it follows that condition 2.2 is necessary
(this is, in any event, self evident).
On the other hand, if condition 2.2 holds for any subcomplex of T , substituting
the inequality 2.2 into 5, we see that
c(C) ≥F0 + 3F2 +F3 =F + 2F2 ≥F.
The above result is not quite what is required: the non-strict inequa lity 20 implies
the existence of a consistent assignment of angles to the faces of T , but some of
these angles may be equal to 0. In order to have the angles strictly positive, we
must modify the weights in the network N1 as follows:
Modify the capacity of level 1 edges to be 1 − 3ǫ; those of level 2 to be 1 −ǫ,
and those of level 3 to be 1 − 2ǫ. Call the resulting network N2. The existence
of a consistent assignment of angles to the faces of T where all the angles are no
smaller than ǫ is obviously equivalent to the maximal ﬂow in N2 being equal to
F (T )(1 − 3ǫ).
Consider now a cut C inN2, with notation as before. The capacity of C will be:
(1 − 3ǫ)F0 + 3(1 −ǫ)F2 +
∑
e∈E(F3
δ(e) − 2ǫE(F3). (21)
Assume that F2 = 0. The MinCut condition together with expression 21 gives:
(1 − 3ǫ)F0 +
∑
e∈E(F3
δ(e) − 2ǫE(F3) ≥ (1 − 3ǫ)F,
or ∑
e∈E(F3
δ(e) ≥ (1 − 3ǫ)F3 + 2ǫE(F3).
If ∅ ⊂ F3 ⊂F , then E(F3)> 3
2F3, and so ∑
e∈E(F3δ(e)>F 3.
Suppose now that δ(F ′) −F ′ ≥ψ >0, for all proper non-empty subsets F ′ ofF .
Then the expression 21 is no smaller than
(1 − 3ǫ)F0 + 3(1 −ǫ)F2 +F3 +ψ − 2ǫE(F3). (22)
The edges of F3 can be divided into two classes: interior edges (those incident
to two triangles of F3) – these number Ei(F3), and boundary edges of F3 – those
incident to only one triangle. These number E∂ (F3). Since F3 is a proper subset
of F ,E∂ (F3)> 0. Clearly,
2E(F3) = 3F3 +E∂ (F3). (23)
The lower bound 22 can thus be rewritten as
c(C) ≥ (1 − 3ǫ)F0 + 3(1 −ǫ)F2 + (1 − 3ǫ)F3 +ψ −ǫE∂ (F3) (24)
= (1 − 3ǫ)F +ψ + (1 − 3ǫ)F2 −ǫE∂ (F3). (25)
· 16
Since ǫ ≤ 1
