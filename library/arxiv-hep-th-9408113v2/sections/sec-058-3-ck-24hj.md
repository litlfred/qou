---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-058-3-ck-24hj
section_title: "(ck− 24h(j)"
section_number: 3
pages: 58-60
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
k −k)π2 (mod π2), (2.23)
where ck = 3k
k + 2 is the central charge and h(j)
k = j(j + 2)
4(k + 2) is the conformal dimension of
the primary ﬁeld of spin j/2. From (2.23) we deduce
L(∆ (j1)
k+2− ∆ (j2)
k+2) = 8(h(j2)
k −h(j1)
k )π2 (mod π2).
Dilogarithm identities 59
Finally we are going to construct the elements ∆ n,r in B(Q(ζn+r)+) using the diloga-
rithm identity (1.28). For this purpose let us denote
g(k)
m :=g(k)
m (j) = sinkϕ sin(n−k)ϕ
sin(m +k)ϕ sin(m +n−k)ϕ, 1≤k≤n− 1,
whereϕ = (j + 1)π
n +r , 0≤j≤n+r−2 and g.c.d.(j +1,n +r) = 1. Clearly, g(k)
m ∈ Q(ζn+r)+.
Let us introduce elements ~∆ n,r = 2
n−1∑
k=1
r−1∑
m=1
[g(k)
m (0)].
Lemma 5. ~∆ n,r∈C(Q(ζn+r)+).
Proof. We have to check λ(~∆ n,r) = 0. First of all, one can easily prove that for any ϕ
(1≤k≤n− 1)
(1−g(k)
m )2
(1−g(k−1)
m )(1−g(k+1)
m )
= (g(k)
m )2
g(k)
m−1g(k)
m+1
, g (k)
0 := 1, g(n)
m := 0. (2.24).
If now ϕ = (j + 1)π
r +n , then g(k)
r = 1, 1 ≤ k≤ n− 1, and it follows from (2.24) that the
elementsga :=g(k)
m , a := (k,m ), satisfy the Bethe-ansatz-like equations
ga =
∏
b
(1−gb)2Ba,b , (2.25)
where B = (Ba,b) = An⊗A−1
r .
Consequently,λ(~∆ n,r) =
∑
a
Ba,aga⊗ga +
∑
a<b
Ba,b(ga⊗gb +gb⊗ga) = 0.
Let ∆ n,r be an element of B(Q(ζn+r)+) corresponding to ~∆ n,r ∈ C(Q(ζn+r)+). It
follows from (1.28) that
L(∆ n,r) =− (n− 1)r(r− 1)
3(n +r) π2 (mod π2), and (2 .26)
L(∆ n,r + ∆ r,n) =− (r− 1)(n− 1)
3 π2 (mod π2) (level − rank duality) . (2.27)
Furthermore, (2.27) admits a generalization. Namely, let u s consider an automorphism
σj∈ Gal(Q(ζn+r)+/Q), which is given by
σj(ζ +ζ −1) = ζ j+1 +ζ −(j+1), where
ζ :=ζn+r, 0≤j≤
[ n +r
2
]
and g .c.d.(j + 1,n +r) = 1.
60 Anatol N. Kirillov
Let us introduce the elements
∆ (j)
n,r :=σj(∆ n,r) = 2
n−1∑
k=1
r−1∑
m=1
g(k)
m (j),
which also belong to the Bloch group B(Q(ζn+r)+). Then it follows from (1.28) that
i) L(∆ (j)
n,r) = 1
