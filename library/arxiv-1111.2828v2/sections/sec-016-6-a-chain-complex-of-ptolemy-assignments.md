---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-016-6-a-chain-complex-of-ptolemy-assignments
section_title: "A chain complex of Ptolemy assignments"
section_number: 6
pages: 18-19
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
---
Let P tn
k be the free abelian group on Ptolemy assignments on ∆ k
n. The usual boundary map
induces a boundary map P tn
k → P tn
k−1 and the natural map C gen
∗ (G/N) → P tn
∗ taking a tuple
(g0N, . . . , gkN ) to its Ptolemy assignment is a chain map. The result below is p roved in Section 9.
Proposition 6.1. A generic tuple is determined up to the diagonal G-action by its Ptolemy coor-
dinates. □
Corollary 6.2. The natural map induces an isomorphism
(6.1) C gen
∗ (G/N) ⊗Z[G] Z ∼= P tn
∗ .
In particular, H∗(G, N) = H∗(P tn
∗ ). □
Lemma 6.3. Let c ∈ P tn
k be a Ptolemy assignment, and let α ∈ ∆ k
n−2(Z). The Ptolemy coordinates
cαij , i ⁄= j are the Ptolemy coordinates of a unique Ptolemy assignment cα on the subsimplex ∆ k(α).
Proof. For 1 ≤ k ≤ 3, this follows from Proposition 5.8. For k > 3, the result follows by induction,
using the fact that 5 Ptolemy coordinates on ∆ 3
2 determines the last. □
A Ptolemy assignment c on ∆ k
n thus induces a Ptolemy assignment cα on each subsimplex. We
thus have maps
(6.2) J n
k : P tn
k → P t2
k, c ↦→
∑
α∈∆ k
n− 2(Z)
cα.
For a Ptolemy assignment c ∈ P tn
k let ci ∈ P tn
k−1 be the induced Ptolemy assignment on the ith
face of ∆ k
n, i.e. we have ∂(c) =∑ k
i=0(−1)ici. Note that
(6.3) (ci)(a0,...,ak− 1) = c(a0,...,ai− 1,0,ai,...ak− 1)i ∈ P t2
k−1.
For β ∈ ∆ k
n−3(Z), let cβi = c(β+ei)i ∈ P t2
k−1, and deﬁne ∂β(c) ∈ P t2
k−1 by
(6.4) ∂β(c) =
k∑
i=0
(−1)icβi ∈ P t2
k−1.
The geometry is explained in Figure 3.
Proposition 6.4. Let c ∈ P tn
k . We have
(6.5) ∂(J n
k (c)) − J n
k−1(∂(c)) =
∑
β∈∆ k
n− 3(Z)
∂β(c) ∈ P t2
k−1.
THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS 19
0
1
2 0
1
2
3
Figure 3. The dotted lines in the left ﬁgure indicate cβ 0, cβ 1 and cβ 2 for k = 2 . The
triangle in the right ﬁgure indicates cβ 0 for k = 3. Here, n = 3 and β = 0.
Proof. By ( 6.3), we have
(6.6)
∂(J n
k (c)) − J n
k−1(∂(c)) =
k∑
i=0
(−1)i ∑
α∈∆ k
n− 2(Z)
cαi −
k∑
i=0
(−1)i ∑
α∈∆ k
n− 2(Z)
ai=0
cαi
=
k∑
i=0
(−1)i ∑
α∈∆ k
n− 2(Z)
ai>0
cαi
=
∑
β∈∆ k
n− 3(Z)
k∑
i=0
(−1)ic(β+ei)i
=
∑
β∈∆ k
n− 3(Z)
∂β(c)
as desired □
