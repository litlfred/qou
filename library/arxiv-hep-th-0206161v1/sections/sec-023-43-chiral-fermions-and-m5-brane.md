---
doc_id: arxiv-hep-th-0206161v1
doc_title: "SEIBERG-WITTEN PREPOTENTIAL FROM INSTANTON COUNTING"
section_id: sec-023-43-chiral-fermions-and-m5-brane
section_title: "Chiral fermions and M5 brane"
section_number: 4.3
pages: 27-30
source_pdf: 0206161v1.pdf
source_sha256: 9530c40215baa02d
doc_brief: "SEIBERG-WITTEN PREPOTENTIAL FROM INSTANTON COUNTING — 26 sections: Introduction; (1 .3); (α±"
---
Another conjecture relates the expansion (1.6) to the dynam ics of the Seiberg-Witten
curve9. Denote, as before q = Λ 2N .
Consider the theory of a free complex chiral fermion ψ,ψ ∗,
S =
∫
Σ
ψ∗ ¯∂ψ (4.7)
living on the curve Σ:
w + Λ 2N
w = P(λ), P(λ) =
N∏
l=1
(λ −αl) (4 .8)
9 For simplicity we consider the case Nf = 0. The conjecture for Nf > 0 case is easy to guess.
26
embedded into the space C × C∗ with the coordinates ( λ,w ). This curve has two distin-
guished points w = 0 and w = ∞ which play a prominent role in the Toda integrable
hierarchy [39]. Let us cut out small disks D0 and D∞ around these two points.
The path integral on the surface Σ with two disks deleted will give a state in the tensor
product H0 ⊗ H∗
∞ of the Hilbert spaces H0, H∞ associated to ∂D0 and∂D∞ respectively.
It can also be viewed as an operator GΣ : H0 → H ∞.
Choose a vacuum state |0⟩ ∈ H0 and its dual ⟨0| ∈ H ∗
∞ (we use the global coordinate w
to identify H0 and H∞). Consider
τΣ =
⟨
0
⏐
⏐
⏐
⏐exp
( 1
¯h
∮
∂D∞
S J
)
GΣ exp
(
− 1
¯h
∮
∂D0
S J
) ⏐
⏐
⏐
⏐ 0
⟩
(4.9)
where:
J =:ψ∗ψ :
dS = 1
2πiλdw
w
(4.10)
and we choose the branch of S near w = 0, ∞ such that (cf. [40]) :
S = N
2πiw∓ 1
N +O(λ−1)
Let us represent Σ as a two-fold covering of the λ-plane. It has branch points at λ =α±
l
where
P(α±
l ) = ±2Λ N
Let us choose the cycles Al to encircle the cuts between α−
l andα+
l . Of course, in H1(Σ , Z Z),
∑
lAl = 0. Then, we deﬁne:
al =
∮
Al
dS .
Our ﬁnal conjecture states:
Z(a, ¯h, −¯h;q) = τΣ
(4.11)
Note that from this conjecture the fact that F0(a, 0, 0) coincides with the Seiberg-Witten
expression follows as a consequence of the Krichever univer sal formula [41]. The remaining
paragraph is devoted to the explanation of the motivation be hind (4.11).
Let us assume that we are in the domain where αl −αm ≫ Λ. Then the surface Σ
can be decomposed into two halves Σ ± byN smooth circles Cl which are the lifts to Σ of
the cuts connecting α−
l and α+
l . The path integral calculating the matrix element (4.9)
27
can be evaluated by the cutting and sewing along the Cl’s. The path integral on Σ ± gives
a state in
⊗N
l=1HCl
(its dual). If we ﬁrst pull the
∮
SJ as close to Cl as possible, we shall get the Hilbert space
obtained by quantization of the fermions which have al + 1
2modZ Zmoding:
ψ(w) ∼
∑
i∈Z Z
ψl,iwal+i
( dw
w
) 1
2
(4.12)
near Cl ⊂ Σ. In addition, the states in HCl of ﬁxed total U (1) charge are labelled by the
partitions kl,i. We conjecture, that
⟨
0
⏐
⏐
⏐
⏐
⏐
⏐
e
∮
SJ∏
l,i
ψl,kl,i −iψ∗
l,−i
⏐
⏐
⏐
⏐
⏐
⏐
0
⟩
l
∼
∏
(l,i)<(m,j)
(alm + ¯h(kl,i −km,j +j −i)) (4 .13)
It is clear that (4.13) implies (4.11). For N = 1 (4.13) is of course a well-known fact (with
the coeﬃcient given by ∏
i<j
1
j−i ), which leads to the following formula for (1.6) 10:
ZN=1(¯h, −¯h;q) = e− q
¯h2
conﬁrming the fact, that even though we worked with the resol ved moduli space ∪k~Mk,1 =
∪k(C2)[k] the “symplectic” volume we got is that of ∪k~Mk,1 = ∪kSym k(I R4).
The conjecture (4.11) should in some sense trivially follow from the M5/NS5 real-
ization of the four dimensional supersymmetric gauge theor y[43][44]. The ǫ-twisting of
the four dimensional part of the ﬁvebrane worldvolume reduc es the dynamical degrees of
freedom down to those of the chiral boson on the curve, which a fter fermionization should
lead to (4.11).
Finally, if (4.11) is true, it is natural to conjecture that t he analogous equivariant
generating functions for instantons on ALE spaces of the ADE type will be related to the
ADE WZW theories on the SW curves.
10 which can also be derived using Schur identities [42]
28
