---
doc_id: ant-v14-n7-s-p06
doc_title: "Moments of quadratic twists of elliptic curve L-functions over function ﬁelds"
section_id: sec-014-8-proof-of-theorem-14
section_title: "Proof of Theorem 1.4"
section_number: 8
pages: 34-36
source_pdf: ant-v14-n7-s-p06.pdf
source_sha256: 4881141ef679dd5a
doc_brief: "Moments of quadratic twists of elliptic curve L-functions over function fields — 24 sections: Introduction and statement of resu; L′(; Some useful lemmas"
---
Following Lemma 2.3, for X< 2g and ﬁxed n∈ N, we deﬁne
M2,E(X, n):=(1−ϵ)
∑
f∈M≤X
(n+ deg(D)− deg( f))λ( f)χD( f)√| f| ,
so that
ϵ−L′(
E⊗χD, 1
2
)
=(log q)M2,E(X,[n/2])+(log q)(E2,E(1, X,[n/2])−ϵ2g+1ϵ(E)E2,E(M, X,[n/2])), (8-1)
where recall that E2,E(M, X, n) is given in (4-14). Then we get that
ϵ−L′(
E⊗χD, 1
2
)2= 2(log q)ϵ−L′(
E⊗χD, 1
2
)
M2,E(X,[n/2])−(log q)2M2
2,E(X,[n/2])
+(log q)2(E2,E(1, X,[n/2])−ϵ2g+1ϵ(E)E2,E(M, X,[n/2]))2.
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1887
By Cauchy’s inequality and Proposition 4.7 we get that
∑
D∈H∗
2g+1
ϵ−L′(
E⊗χD, 1
2
)2= 2(log q)
∑
D∈H∗
2g+1
ϵ−L′(
E⊗χD, 1
2
)
M2,E(X,[n/2])
−(log q)2 ∑
D∈H∗
2g+1
M2,E(X,[n/2])2+ Oε(q2gg1/2+ϵ(2g− X)4).
Now by Lemma 2.3 we have
∑
D∈H∗
2g+1
ϵ−L′(
E⊗χD, 1
2
)
M2,E(X,[n/2])
= 2(log q)([n/2]+2g+1)2(SE(1,[n/2]+2g+1, X)−ϵ2g+1ϵ(E)SE(M,[n/2]+2g+1, X))
+2([n/2]+2g+1) ∂
∂β(SE(1,[n/2]+2g+1, X; 0,β)−ϵ2g+1ϵ(E)SE(M,[n/2]+2g+1, X; 0,β))
⏐⏐
β=0
+2([n/2]+2g+1) ∂
∂α(SE(1,[n/2]+2g+1, X;α, 0)−ϵ2g+1ϵ(E)SE(M,[n/2]+2g+1, X;α, 0))
⏐⏐
α=0
+ 2
log q
∂2
∂α∂β(SE(1,[n/2]+2g+1, X;α,β)−ϵ2g+1ϵ(E)SE(M,[n/2]+2g+1, X;α,β))
⏐⏐
α=β=0,
and similarly
∑
D∈H∗
2g+1
M2,E(X,[n/2])2
= 2([n/2]+ 2g+ 1)2(SE(1, X, X)−ϵ2g+1ϵ(E)SE(M, X, X))
+ 2
log q([n/2]+ 2g+ 1) ∂
∂β(SE(1, X, X; 0,β)−ϵ2g+1ϵ(E)SE(M, X, X; 0,β))
⏐⏐
β=0
+ 2
log q([n/2]+ 2g+ 1) ∂
∂α(SE(1, X, X;α, 0)−ϵ2g+1ϵ(E)SE(M, X, X;α, 0))
⏐⏐
α=0
+ 2
(log q)2
∂2
∂α∂β(SE(1, X, X;α,β)−ϵ2g+1ϵ(E)SE(M, X, X;α,β))
⏐⏐
α=β=0.
Choosing X= 2g− 100 logg and using Proposition 3.1, we obtain that
1
|H∗
2g+1|
∑
D∈H∗
2g+1
ϵ−L′(
E⊗χD, 1
2
)2= c5(M)L(Sym2 E, 1)3g3+ Oε(g2+ϵ),
where
c5(M)= 16(log q)2(CE(1; 1, 1, 1)−ϵ2g+1ϵ(E)CE(M; 1, 1, 1))
∏
P|1
|P|+ 1
|P| . (8-2)
1888 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
