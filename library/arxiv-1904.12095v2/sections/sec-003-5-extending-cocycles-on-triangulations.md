---
doc_id: arxiv-1904.12095v2
doc_title: "Verified computations for closed hyperbolic 3-manifolds Matthias Goerner"
section_id: sec-003-5-extending-cocycles-on-triangulations
section_title: "Extending cocycles on triangulations"
section_number: 5
pages: 12-14
source_pdf: 1904.12095v2.pdf
source_sha256: 7006b250f0d3c991
doc_brief: "Verified computations for closed hyperbolic 3-manifolds Matthias Goerner — Extending methods ﬁrst used by Casson, we show how to verify a hyper- bolic structure on a ﬁnite triangulation of a closed"
---
Let T be a triangulation with an assignment of edge parameters νe < −1 such that each
G∆ is realized (i.e., fulﬁlls the conditions of Lemma 2.2). Let E ∼ ∪ E = = E(T ) be a parti-
tion of the edges into two disjoint sets where |E ∼| = 3o with o = |V (T )| being the num-
ber of vertices of T . Assume that we know that Θe = 2π for every edge e ∈ E =, but we
13
 
e ∼
j
γ012
∆i
β013
∆i
β021
∆i
γ023
∆i
γ031
∆i
α012
∆i γ103
∆iβ102
∆i
γ120
∆i β123
∆i
γ132
∆i
γ302
∆i ′
β301
∆i ′
γ310
∆i ′
γ321
∆i ′
Figure 9. Gimbal loops for two “vertex links” (only some part of each is shown). The thick
line is the edge in the triangulation.
only know that Θe is close to 2 π for e ∈ E ∼. Thus, the PGL 2(C)-cocycle in Theorem 3.5
might only extend to ˆT = = ˆT \ Prisms(E ∼), the complex where the prisms (including
the top and bottom face) about the edges in E ∼ have been removed. The goal of this
section is to give a criterion that forces Θe = 2π for all e ∈ E(T ), so that the conclusions
of Theorem 3.5 apply and the edge parameters νe yield a hyperbolic structure for T .
Let V (T ) = {v1,. .. ,vo} be the vertices of T . If we drop all all α-edges and all 2- and
3-cells adjacent to any α-edge from ˆT , the remaining complex has a connected com-
ponent for each vertex vk. We call such a connected component the “vertex link” of
vk and denote it by Lk. Starting with ˆT = instead of ˆT , we similarly obtain a subcom-
plex L=
k ⊂ Lk for each vk. Note that (Lk,L=
k ) is a punctured topological polyhedron as in
Deﬁnition 4.1 and the SO 3-cocycle on ˆT = descends to a (SO3,SO 2)-cocycle on each L=
k
formed by the β- and γ-edges. Let us ﬁx a gimbal loop Γk for each ( Lk,L=
k ), giving us
gimbal functions g1,. .. ,go as in Deﬁnition 4.6.
Let us label the edges in E ∼ = {e∼
1 , .. .,e∼
3o} and E = = {e=
1 , .. .,e=
m−3o}. We again want to
construct a gimbal function, but this time in one variable T j per edge e∼
j ∈ E ∼ instead
of a variable dk,l per removed polygon as in Section 4. Note that each edge e∼
j ∈ E ∼
corresponds to two polygons Pk,l and Pk′,l ′ that have been removed (from the “vertex
links” Lk and Lk′ in ˆT ) to obtain L=
k and L=
k′ (with k and k ′ not necessarily distinct), see
Figure 9. We obtain a gimbal function in ( T1, .. .,T3o) for each vertex by setting dk,l =
dk′,l ′ = T j in Deﬁnition 4.6. We combine these gimbal functions into a single one:
Deﬁnition 5.1. Let T be a triangulation with an assignment of edge parameters νe <
−1 such that each G∆ fulﬁlls the conditions of Lemma 2.2. Let E ∼ = {e∼
1 , ... ,e∼
3o} and
E = = {e=
1 , ... ,e=
m−3o} be a partition of E(T ) and ﬁx gimbal loops Γ1, .. .,Γo. The gimbal
function is given by
g : R3o → R3o, ( T1,. .. ,T3o) 7→
(
g1(d1,1,. .. ,d1,p1), .. .,go(do,1, .. .,do,po )
)
.
A box K ⊂ Rq avoids gimbal lock if [Dg (K )] is invertible.
14
Note that the orientation on (Lk,L=
k ) in the above deﬁnitions must be chosen such that
the boundary of a small hexagon in (Lk,L=
k ) contains a γσ(0)σ(1)σ(2) for σ ∈ A4.
Example 5.2. Figure 9 shows examples of gimbal loops for two “vertex links” of ˆT =. The
corresponding gimbal matrices would be given by
· · ·γ031
∆i · β013
∆i · RT j · γ012
∆i · β021
∆i · · · and · · ·γ103
∆i · γ310
∆i ′ · RT j · β301
∆i ′ · γ302
∆i ′ · · ·.
The gimbal function g for the triangulation is obtained by taking the upper triangular
entries of the gimbal matrix for each vertex.
Theorem 5.3. Let T , νe, E ∼ and E =, Γ1, .. .,Γo and g be as in Deﬁnition 5.1. Let K ⊂ R3o
be a box avoiding gimbal lock such that (2π, .. ., 2π) ∈ K . If
(a) (Θe∼
1 ,. .. ,Θe∼
3o ) ∈ K and
(b) Θe=
1 = · · · =Θe=
m−3o = 2π
then Θe = 2π for all e ∈ E(T ), so the edge parameters νe yield a hyperbolic structure
on T .
Proof. By applying Lemma 4.7 to each vertex v1,. .. ,vo, we see that
g (2π,. .. ,2π) = g (0, .. ., 0)= (0, .. ., 0).
Hence, the proof from Lemma 4.10 applies here as well and we have Θe∼
1 = · · · =Θe∼
3o =
2π. Therefore, all conditions of Theorem 3.5 are fulﬁlled.
