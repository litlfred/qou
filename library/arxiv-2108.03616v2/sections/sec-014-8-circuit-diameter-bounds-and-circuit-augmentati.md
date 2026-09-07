---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-014-8-circuit-diameter-bounds-and-circuit-augmentati
section_title: "Circuit diameter bounds and circuit augmentation algorithms"
section_number: 8
pages: 28-29
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
Consider an LP in standard equality form with upper bounds, w hereA∈ Rm×n,b∈ Rm,u∈ Rn:
min⟨c,x⟩
Ax =b
0≤x≤u
(LP(A,b,c,u ))
In Section 4.2 we brieﬂy mentioned the Hirsch conjecture and some progress towards the
polynomial Hirsch conjecture; in Theorem 4.8 shows a bound O((n−m)3mκA log(κA +n)) on
the diameter of {x∈ Rn : Ax =b,x≥ 0} for A∈ Rm×n.
Circuit diameter bounds were introduced by Borgwardt, Finhold, and Hemmecke [ BFH15] as
a relaxation of diameter bounds. Let P denote the feasible region of LP(A,b,c,u ). A circuit walk
is a set of consecutive feasible points x(1),x (2),...,x (k+1)∈ P such that for each t = 1,...,k ,
x(t+1) = x(t) +g(t) for g(t)∈F (A), and further, x(t) + (1 + ε)g(t) /∈ P for any ε >0, i.e., each
28
consecutive circuit step is maximal. The circuit diameter ofP is the minimum length of a circuit
walk between any two vertices x,y∈P .
In contrast to walks in the vertex-edge graph, circuit walks are non-reversible and the mini-
mum length from x toy may be diﬀerent from the one from y tox; this is due to the maximality
requirement. The circuit-analogue of the Hirsch conjectur e, formulated in [ BFH15], asserts that
the circuit diameter of a polytope in d dimensions with n facets is at most n−d; this may be
true even for unbounded polyhedra, see [ BSY18].
In this section we begin by showing a recent, improved bound o n the circuit diameter with
logκA dependence. Section 8.2 gives an overview of circuit augmentations algorithms. We
review existing algorithms for diﬀerent augmentation rules (Theorem 8.2 and Theorem 8.5),
and also show a new bound for the steepest-descent direction (Theorem 8.4). The bounds in
these three theorems also translate directly to circuit dia meter bounds, since they all consider
algorithms with maximal augmentation sequences.
