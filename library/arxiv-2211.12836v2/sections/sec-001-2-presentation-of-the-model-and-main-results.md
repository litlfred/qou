---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION"
section_id: sec-001-2-presentation-of-the-model-and-main-results
section_title: "Presentation of the model and main results"
section_number: 2
pages: 3-4
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION — We study a class of commuting Markov kernels whose simplest element describes the movement ofk particles on a discrete"
---
2.1. k-conﬁguration on a circle and continuous counterpart. Fork,n∈ N∗ with k≤n, let
Bk,n denote the set of positions of k nonintersecting and indistinguishable particles on a discrete
circle of size n. Formally, Bk,n is the set of increasing sequences of J0,n− 1K of length k: such a
sequence gives the position of the k particles in the clockwise direction starting from the origin 0 of
the discrete circle, see Figure 1 and the correspondingk-subsets on Figure 2 in the casek = 2,n = 4.
4 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
The size⟨I⟩ of an elementI ={I1>...>I k}∈ Bk,n is the sum of its parts (remark that the size
is always positive when I∈Bk,n). The discrete set Bk,n is given a graph structure by saying there
is an oriented edge from I to J when⟨J⟩ =⟨I⟩ + 1 mod n and #{1≤l,l′≤k,Jl′ =Il} =k− 1.
We then write I ↗ J when there is such an oriented edge from I to J. The edges of Bk,n
encode the clockwise movement of the k particles around the circle conditioned to never intersect.
A distinguished vertex of Bk,n is given by the sequence I0 ={0,...,k − 1}, which represents k
particles stacked after the origin on the discrete circle. See Figure 2 for the graph structure of B2,4.
Figure 2. Graph B2,4 from a combinatorial perspective.
For ﬁxedk≥ 1, the family of graphs{Bk,n, n≥ 1} has a continuous counterpart embodied by the
setTk of positions of k indistinguishable particles on a continuous circle of radius 1. Identifying the
positions of the particles by their distance from a distinguished point of the circle in the clockwise
direction, we formally identify Tk with the subset of vectors ⃗ u= (u1,...,u k)∈ [0, 2π[k such that
2π >u1≥u2≥···≥ uk≥ 0.
Remark that we authorize particles to be at the same position in the continuous case, since this
situation may theoretically appear as a limit case of discrete conﬁgurations as n goes to inﬁnity
(although it will almost surely not be the case).
Forx∈ R, denote by x the unique element of [0, 2π[ such that x−x∈ 2πZ. Then, reﬂecting the
circular nature of the model, there is a shift action of R on Tk given by
Rt(⃗ u) =Sort(u1− 2tπ,..., uk− 2tπ),
where Sort(⃗ u) is the sequence obtained from ⃗ u∈ [0, 2π[k by sorting it in decreasing order. For
eachn≥ 1, the graph Bk,n can actually be embedded in Tk through the map
(1) ξn :



Bk,n → Tk
I ↦→Rk−1
2n
(2π
n I
).
Note that there is a shift of π(k−1)
n which seems at ﬁrst sight arbitrary: its role is mainly to simplify
later expressions.
