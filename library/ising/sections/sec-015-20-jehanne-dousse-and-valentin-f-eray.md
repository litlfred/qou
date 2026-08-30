---
doc_id: ising
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-015-20-jehanne-dousse-and-valentin-f-eray
section_title: "JEHANNE DOUSSE AND VALENTIN F ´ERAY"
section_number: 20
pages: 20-21
source_pdf: ising.pdf
source_sha256: 9f84d7209731d299
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
the number of occurrences of P whose position is in Λn. In the example of isolated + spins, we have
Sn,P :=
∑
i∈Λn

Xi
∏
j:‖i−j‖1=1
(1−Xj)

.
It is also easy to encode in this framework the number of + connected components of any given shape.
Let v2
n,P denote the variance of Sn,P. We have a lemma analogous to Lemma 4.2.
Lemma 4.7. As n tends to inﬁnity, the quantity
v2
n,P
|Λn| tends to v2
P :=∑
k∈Zd⟨ZP
0 ;ZP
k⟩β,h <∞.
Proof: That GP is a weighted dependency graph for the family ZP
i implies that
⟨ZP
0 ;ZP
k⟩β,h≤D2ε
1
2 (k−maxα,β∈D‖α−β‖1).
This proves that v2
P is ﬁnite as claimed.
Let ε> 0 be ﬁxed. We want to show that for n large enough,⏐⏐⏐⏐⏐⏐
v2
n,P
|Λn|−
∑
k∈Zd
⟨ZP
0 ;ZP
k⟩β,h
⏐⏐⏐⏐⏐⏐
≤ε.
We have
v2
n,P
|Λn| = 1
|Λn|
∑
i∈Λn
∑
j∈Λn
⟨ZP
i ;ZP
j⟩β,h
= 1
|Λn|
∑
i∈Λn
∑
j∈Zd
⟨ZP
i ;ZP
j⟩β,h− 1
|Λn|
∑
i∈Λn
∑
j∈Zd\Λn
⟨ZP
i ;ZP
j⟩β,h.
By translation invariance of⟨ZP
i ;ZP
j⟩β,h, the ﬁrst sum equals∑
k∈Zd⟨ZP
0 ;ZP
k⟩β,h. Thus the only thing
left to do is to show that for n large enough, the absolute value of the second term is bounded by ε.
We cut the sum oni into two parts : the points that are far from the boundary of Λ n and those which
are not. Recall that the boundary ∂Λn consists of points j not in Λ, which have a neighbour in Λ n.
We denoteδ(i,∂ Λn) = minj∈∂Λn‖i−j‖1, which is the distance between i and∂Λn. For R a positive
integer, let us consider the points i∈ Λn at distance more than R from the boundary of Λn. We have,
again by translation invariance
1
|Λn|
∑
i∈Λn
δ(i,∂Λn)>R
∑
j∈Zd\Λn
|⟨ZP
i ;ZP
j⟩β,h|≤
∑
k∈Zd
|k|>R
|⟨ZP
0 ;ZP
k⟩β,h|.
But the series ∑
k∈Zd|⟨ZP
0 ;ZP
k⟩β,h| is absolutely convergent so the sum above tends to 0 as R tends
to inﬁnity. Therefore, there exists some integer R0 such that
(4.5) 1
|Λn|
∑
i∈Λn
δ(i,∂Λn)>R0
∑
j∈Zd\Λn
|⟨ZP
i ;ZP
j⟩β,h|≤ ε
2.
Now let us consider the points of Λ n that are at distance at most R0 of ∂Λn. There are at most
C|∂Λn|Rd
0 such points. Therefore
1
|Λn|
∑
i∈Λn
δ(i,∂Λn)≤R0
∑
j∈Zd\Λn
|⟨ZP
i ;ZP
j⟩β,h|≤ 1
|Λn|
∑
i∈Λn
δ(i,∂Λn)≤R0
∑
k∈Zd
|⟨ZP
0 ;ZP
k⟩β,h|≤ C′|∂Λn|
|Λn| Rd
0.
But as n tends to∞, |∂Λn|
|Λn| tends to 0. Therefore for n large enough,
(4.6) 1
|Λn|
∑
i∈Λn
δ(i,∂Λn)≤R0
∑
j∈Zd\Λn
|⟨ZP
i ;ZP
j⟩β,h|≤ ε
2.
Adding (4.5) and (4.6) completes the proof. □
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 21
We are now ready to prove the central limit theorem.
Proof of Theorem 1.8: We proceed as in the proof of Theorem 4.1. We consider GP[Λn].
The number of vertices is Nn =|Λ′
n| =|Λn| and, from (4.4), its maximal weighted degree ∆n− 1 is
bounded as follows:
∆n− 1≤ max
i∈Λn
∑
j∈Λn
ε
1
