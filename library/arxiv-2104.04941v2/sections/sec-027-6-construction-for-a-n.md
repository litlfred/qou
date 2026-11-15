---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-027-6-construction-for-a-n
section_title: "Construction for A_n"
section_number: 6
pages: 32-33
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
The An case was studied in detail in [GTZ15]. We merely restate the conclusions in language consistent
with the above.
Remark 6.1. That the algorithm of Section 5 does not work for A2n can be seen in a few diﬀerent ways,
which are interconnected.
• There is no general formula for a Coxeter element c that yields a longest-word presentation w0 =
cc · · · c.
• The Coxeter number for A2n is odd.
• The action of σG for A2n preserves no simple roots, therefore there can be no tree partitioning with
a unique root node.
Proposition 6.2. For G of type An, Theorem 4.19 holds.
Proof. For the construction of Q, take the quiver consisting of mutable vertices { vij : 1 ≤j ≤n, 1 ≤i ≤n −j }
and frozen vertices { Ai, Bi, Ci : 1 ≤i ≤n }, all of weight 1. We consider
Ai = v0,i,
Bi = vi,n+1−j,
Ci = vi,0.
The edges are given by
σ(a, b) =





c(a, b)
a = vi,j, b = vi+1,j or a = vi,j, b = vi−1,j+1 or a = vi,j, b = vi,j−1
−c(a, b)
a = vi+1,j, b = vi,j or a = vi−1,j+1, b = vi,j or a = vi,j−1, b = vi,j
0
else,
and c(a, b) is 1
2 if a and b are both Ais, both Bis, or both Cis, and is 1 otherwise.
The mutation µrot = µ { } is trivial.
Since the mutable portion of QAn is not rectangular, we need another convention for describing coordinates
of Q0–2 in order to describe µﬂip. We present this by example in Figure 28.
□
Mechanically, the inclusion of the left QAn into Q0–2 is the following:
Ai 7→Di,
Bi 7→Ei,
Ci 7→wi,n,
vi,j 7→wi,j+n,
and for the right QAn into Q0–2, the following:
Ai 7→wi,n,
Bi 7→Fi,
Ci 7→Gi,
vi,j 7→wj,n+1−i,
32
A1
A2
A3
C1
C2
C3
B1
B2
B3
v11
v12
v21
A1
A2
A3
C1
C2
C3
B1
B2
B3
v11
v12
v21
D1
D2
D3
E1
E2
E3
F1
F2
F3
G1
G2
G3
w15
w14
w24
w13
w23
w33
w11
w12
w22
Ψ−1
02
Figure 28. Quivers for type A3, also showing naming convention for Q0–2.
The mutation µﬂip is then the “diamond sequence”:
t(ℓ, j) = ℓ+ 1
2
−

j −ℓ+ 1
2

eµRect(ℓ) =
ℓ
Y
k=1
n−ℓ
Y
j=0
µ

wt(ℓ,k)+j,2k+n−(ℓ+1)
	
µﬂip =
n
Y
ℓ=1
eµRect(ℓ)
The map M is constructed as in Deﬁnition 5.18. Where needed, the presentation of the longest word is
given by
i = (1, 2, . . . , n,
1, 2, . . ., n −1,
. . . ,
1, 2,
1).
7. Proof of Theorem 4.19 for simple G
