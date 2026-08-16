---
doc_id: ant-v14-n7-s-p06
doc_title: "Moments of quadratic twists of elliptic curve L-functions over function ﬁelds"
section_id: sec-013-7-proof-of-theorem-13
section_title: "Proof of Theorem 1.3"
section_number: 7
pages: 33-34
source_pdf: ant-v14-n7-s-p06.pdf
source_sha256: 4881141ef679dd5a
doc_brief: "Moments of quadratic twists of elliptic curve L-functions over function fields — 24 sections: Introduction and statement of resu; L′(; Some useful lemmas"
---
Following Lemma 2.2, for X< 2g, we deﬁne
M1,E(X):=(1+ϵ)
∑
f∈M≤X
λ( f)χD( f)√| f| ,
so that
L
(
E⊗χD, 1
2
)
= M1,E(X)+ E1,E(1, X,[n/2])+ϵ2g+1ϵ(E)E1,E(M, X,[(n− 1)/2]), (7-1)
where recall expression (4-13) for E1,E(N, X, n). Hence
L
(
E⊗χD, 1
2
)2
= 2L(E⊗χD, 1
2)M1,E(X)− M1,E(X)2+(E1,E(1, X,[n/2])+ϵ2g+1ϵ(E)E1,E(M, X,[(n− 1)/2]))2.
1886 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
By Cauchy’s inequality and Proposition 4.7 we get
∑
D∈H∗
2g+1
L
(
E⊗χD, 1
2
)2= 2
∑
D∈H∗
2g+1
L
(
E⊗χD, 1
2
)
M1,E(X)−
∑
D∈H∗
2g+1
M1,E(X)2
+ Oε(q2gg1/2+ε(2g− X)2).
Now using Lemma 2.2 again and expanding M1,E(X)2, the ﬁrst line of the equation above is
2(SE(1,[n/2]+ 2g+ 1, X)+ SE(1,[(n+ 1)/2]+ 2g, X)− SE(1, X, X))
+ 2ϵ2g+1ϵ(E)(SE(M,[n/2]+ 2g+ 1, X)+ SE(M,[(n+ 1)/2]+ 2g, X)− SE(M, X, X)),
where recall the deﬁnition of SE(M, X, Y) in Section 3. Using Proposition 3.1, this is equal to
|H∗
2g+1|c2(M)L(Sym2 E, 1)3X+ O(q2g)+ O(q2g−X/5g3)+ O(q5g/4+3X/8g30),
where
c2(M)= 2(CE(1; 1, 1, 1)+ϵ2g+1ϵ(E)CE(M; 1, 1, 1))
∏
P|1
|P|+ 1
|P| , (7-2)
and CE(N; 1, 1, 1) is deﬁned in (3-9). Thus
1
|H∗
2g+1|
∑
D∈H∗
2g+1
L
(
E⊗χD, 1
2
)2
= c4(M)L(Sym2 E, 1)3X+ O(q−X/5g3)+ O(q−3g/4+3X/8g30)+ Oε(g1/2+ε(2g− X)2).
Choosing X= 2g− 100 logg we obtain the theorem.
