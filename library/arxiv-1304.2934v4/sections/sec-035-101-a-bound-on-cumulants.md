---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-035-101-a-bound-on-cumulants
section_title: "A bound on cumulants"
section_number: 10.1
pages: 81-83
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
10.1.1. Subgraph count statistics. In the following we denote A(n, k) the set of arrange-
ments in [n] of length k, i.e., lists of k distinct elements in [n]. The cardinality of A(n, k)
is the falling factorial n↓k = n(n− 1)··· (n− k + 1). Let A = ( a1, . . . ,ak) be an ar-
rangement in [n] of length k, and γ be a ﬁxed graph with vertex set [k]. Recall that
Γ = Γ(n, pn) is a random Erdös-Rényi graph on [n]. We denote δγ(A) the following
random variable:
δγ(A) =
{
1 if γ⊆ Γ[a1, . . . ,ak];
0 else. (49)
Here Γ[a1, . . . ,ak] denotes the graph induced by Γ on vertex set {a1, . . . ,ak}. As our
data is an ordered list (a1, . . . ,ak), this graph can canonically be seen as a graph on
82 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
vertex set [k], that is the same vertex set as γ. Then the inclusion should be understood
as inclusion of edge sets.
For any graph γ with k vertices and any integer n≥ 1, we then deﬁne the random
variable X(n)
γ by
X(n)
γ = ∑
A∈A(n,k)
δγ(A).
Remark 10.2. It would also be natural to replace in Deﬁnition (49) the inclusion by an
equality γ = Γ[a1, . . . ,ak]. This would lead to other random variables Y(n)
γ , called
induced subgraph count statistics. Their asymptotic behavior is harder to study (in
particular, ﬂuctuations are not always Gaussian; see [JŁR00, Theorem 6.52]). Notice
that if γ is a complete graph, then both deﬁnitions coincide.
10.1.2. A dependency graph of the subgraph count statistics. Fix some graph γ with vertex
set [k]. By deﬁnition, the variable we are interested in writes as a sum
X(n)
γ = ∑
A∈A(n,k)
δγ(A).
We shall describe a dependency graph for the variables{δγ(A)}A∈A(n,k).
For each pair e ={v, v′}⊂ [n], denote Ie the indicator function of the event: e is
in the graph Γ(n, p). By deﬁnition of the model Γ(n, p), the random variables Ie are
independent Bernouilli variables of parameter p. Then, for an arrangement A, denote
E(A) the set of pairs{v, v′} where v and v′ appear in the arrangement A. One has
δγ(A) = ∏
e∈E′(A)
Ie,
where E′(A) is a subset of E(A) determined by the graph γ. In particular, if, for two
arrangements A and A′, one has|E(A)∩ E(A′)| = ∅ (equivalently,|A∩ A′|≤ 1), then
the variables δγ(A) and δγ(A′) are deﬁned using different variables Ie (and, hence, are
independent). This implies that the following graph denoted B is a dependency graph
for the family of variables{δγ(A)}A∈A(n,k):
• its vertex set is A(n, k);
• there is an edge between A and A′ if|A∩ A′|≥ 2.
Considering this dependency graph is quite classical — see, e.g., [JŁR00, Example 1.6].
All variables in this graph are Bernoulli variables and, hence, bounded by 1. Besides
the graph B has N = n↓k vertices, and is regular of degree D smaller than
(k
2
)2
2 (n− 2)(n− 3)··· (n− k + 1) < k4 nk−2.
Indeed, a neighbour A′ of a ﬁxed arrangement A∈ A(n, k) is given as follows:
• choose a pair{ai, aj} in A that will appear in A′;
• choose indices i′ and j′ such that a′
i′ = ai and a′
j′ = aj (these indices are different
but their order matters);
MOD-φ CONVERGENCE, I 83
• choose the other values in the arrangement A′.
So, we may apply Theorem 9.7 and we get:
Proposition 10.3. Fix a graph γ of vertex set [k]. For any r≤ 1, one has
⏐⏐κ(r)(X(n)
γ )
⏐⏐≤ 2r−1rr−2 nk (k4 nk−2)r−1.
