---
doc_id: ant-v14-n7-s-p06
doc_title: "Moments of quadratic twists of elliptic curve L-functions over function ﬁelds"
section_id: sec-017-2-m1e1xl
section_title: "M1,E1(X)L′("
section_number: 2
pages: 36-37
source_pdf: ant-v14-n7-s-p06.pdf
source_sha256: 4881141ef679dd5a
doc_brief: "Moments of quadratic twists of elliptic curve L-functions over function fields — 24 sections: Introduction and statement of resu; L′(; Some useful lemmas"
---
E2⊗χD, 1
2
)
+(log q)L
(
E1⊗χD, 1
2
)
M2,E2(X,[n2/2])
−(log q)M1,E1(X)M2,E2(X,[n2/2])
+(log q)(E1,E1(1, X,[n1/2])+ϵ2g+1ϵ(E1)E1,E1(M1, X,[(n1− 1)/2]))
×(E2,E2(1, X,[n2/2])−ϵ2g+1ϵ(E2)E2,E2(M2, X,[n2/2])).
We bound the last term above using Cauchy’s inequality and Proposition 4.7. In doing so we get
∑
D∈H∗
2g+1
ϵ−
2 L
(
E1⊗χD, 1
2
)
L′(
E2⊗χD, 1
2
)
=
∑
D∈H∗
2g+1
ϵ−
2 M1,E1(X)L′(
E2⊗χD, 1
2
)
+(log q)
∑
D∈H∗
2g+1
L
(
E1⊗χD, 1
2
)
M2,E2(X,[n2/2])
−(log q)
∑
D∈H∗
2g+1
M1,E1(X)M2,E2(X,[n2/2])+ Oε(q2gg1/2+ε(2g− X)3). (9-1)
We shall estimate the remaining three terms using Proposition 3.1. They all have similar forms. For the
ﬁrst term, by Lemma 2.3 again we have
∑
D∈H∗
2g+1
ϵ−
2 M1,E1(X)L′(
E2⊗χD, 1
2
)
=(log q)
∑
D∈H∗
2g+1
(1+ϵ1)(1−ϵ2)
∑
f∈M≤X
h∈M≤[n2/2]+2g+1
([n2/2]+ 2g+ 1− deg(h))λ1( f)λ2(h)χD( f h)√| f h| .
By expanding out, this equals
(log q)([n2/2]+ 2g+ 1)
(
SE1,E2(1,[n2/2]+ 2g+ 1, X; 0, 0)
+ϵ2g+1ϵ(E1)SE1,E2(M1,[n2/2]+ 2g+ 1, X; 0, 0)
−ϵ2g+1ϵ(E2)SE1,E2(M2,[n2/2]+ 2g+ 1, X; 0, 0)
−ϵ(E1)ϵ(E2)SE1,E2(M1M2,[n2/2]+ 2g+ 1, X; 0, 0)
)
+ ∂
∂β
(
SE1,E2(1,[n2/2]+ 2g+ 1, X; 0,β)
+ϵ2g+1ϵ(E1)SE1,E2(M1,[n2/2]+ 2g+ 1, X; 0,β)
−ϵ2g+1ϵ(E2)SE1,E2(M2,[n2/2]+ 2g+ 1, X; 0,β)
−ϵ(E1)ϵ(E2)SE1,E2(M1M2,[n2/2]+ 2g+ 1, X; 0,β)
)⏐⏐
β=0,
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1889
which is, by Proposition 3.1 and Cauchy’s residue theorem,
|H∗
2g+1|c6(M1, M2)L(Sym2 E1, 1)L(Sym2 E2, 1)L(E1⊗ E2, 1)g+ O(q2g)+ O(q5g/4+3X/8g31),
where
c6(M1, M2)= 2(logq)
(
CE1,E2(1;1,1,1,0,0)+ϵ2g+1ϵ(E1)CE1,E2(M1;1,1,1,0,0)
−ϵ2g+1ϵ(E2)CE1,E2(M2;1,1,1,0,0)
−ϵ(E1)ϵ(E2)CE1,E2(M1M2;1,1,1,0,0)
)∏
P|1
|P|+1
|P| . (9-2)
The other two terms in (9-1) have the same asymptotics so we obtain
1
|H∗
2g+1|
∑
D∈H∗
2g+1
ϵ−
2 L
(
E1⊗χD, 1
2
)
L′(
E2⊗χD, 1
2
)
=c6(M1, M2)L(Sym2 E1, 1)L(Sym2 E2, 1)L(E1⊗E2, 1)g+O(q−3g/4+3X/8g31)+Oε(g1/2+ε(2g−X)3).
Choosing X= 2g− 100 logg we obtain the theorem.
