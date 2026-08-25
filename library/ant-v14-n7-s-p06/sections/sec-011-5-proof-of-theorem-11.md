---
doc_id: ant-v14-n7-s-p06
doc_title: "Moments of quadratic twists of elliptic curve L-functions over function ﬁelds"
section_id: sec-011-5-proof-of-theorem-11
section_title: "Proof of Theorem 1.1"
section_number: 5
pages: 29-33
source_pdf: ant-v14-n7-s-p06.pdf
source_sha256: 4881141ef679dd5a
doc_brief: "Moments of quadratic twists of elliptic curve L-functions over function fields — 24 sections: Introduction and statement of resu; L′(; Some useful lemmas"
---
For N|1∞, let
RE(N, X):=
∑
D∈H∗
2g+1
∑
f∈M≤X
λ( f)χD(N f)√| f| .
We will prove the following lemma.
Lemma 5.1. We have
RE(N, X)=| H2g+1|CE(N; 1)L(Sym2 E, 1)+ Oε(q2g−X/2+εg)+ Oε(q X/2+ϵg),
where the value CE(N; 1) is deﬁned in (5-2).
Proof. Note that
RE(N, X)= SE,E(N, X, 0; 0, 0),
where SE1,E2(N, X, Y;α,β) is deﬁned as in (3 -1). We proceed as in Section 3, see (3 -2), (3-3) and (3-7),
and write
RE(N, X)= SE,E(N, X, 0, g; 0, 0)= RE(N, X; V= 0)+ RE(N, X; V⁄= 0),
where RE(N, X; V⁄= 0)= SE,E(N, X, 0, g; 0, 0; V⁄= 0) and
RE(N, X; V= 0)= SE,E(N, X, 0, g; 0, 0; V= 0)
=| H2g+1|
∑
f∈M≤X
N f=□
λ( f)√| f|
∏
P|1f
(
1− 1
|P|
) ∑
C2|(1f)∞
deg(C2)≤g
1
|C2|2+ Oε(qεg).
1882 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
We ﬁrst evaluate RE(N, X; V= 0). From (3-6) we have
∑
C2|(1f)∞
deg(C2)≤g
1
|C2|2=
∏
P|1f
(
1− 1
|P|2
)−1
+ Oε(q−2g+εg).
The contribution of the error term to RE(N, X; V= 0) is
≪ε qεg ∑
l∈M≤X/2
|λ(Nl 2)|
|l| ≪ε qεg.
Hence
RE(N, X; V= 0)=| H2g+1|
∑
f∈M≤X
N f=□
λ( f)√| f|
∏
P|1f
(
1+ 1
|P|
)−1
+ Oε(qεg).
Applying the Perron formula to the sum over f yields
RE(N, X; V= 0)=|H2g+1|
2πi
∮
|u|=r
BE(N; u) du
u X+1(1− u)+ Oε(qεg) (5-1)
for any r< 1, where
BE(N; u)=
∑
f∈M
N f=□
λ( f)udeg( f)
√| f|
∏
P|1f
(
1+ 1
|P|
)−1
.
We can write BE(N; u) in terms of its Euler product,
BE(N; u)=
∏
P ∤1
(
1+
(
1+ 1
|P|
)−1∑
i≥1
λ(P2i)u2i deg(P)
|P|i
)∏
P|1
((
1+ 1
|P|
)−1 ∑
i+ordP(N) even
λ(Pi)ui deg(P)
|P|i/2
)
= CE(N; u)L
(
Sym2 E, u2
q
)
, (5-2)
where CE(N; u) is some Euler product which is uniformly bounded for|u|≤ q1/2−ε. We shift the contour
in (5-1) to|u|= q1/2−ε, encountering a simple pole at u= 1. Then
RE(N, X; V= 0)=| H2g+1|CE(N; 1)L(Sym2 E, 1)+ Oε(q2g−X/2+εg). (5-3)
Now we will bound RE(N, X; V⁄= 0). As in Section 3D, see (3-12), it sufﬁces to bound the term
R(V⁄= 0)=q2g+1τ(q)
∑
f∈M≤X
deg(N f) odd
λ( f)
|N|| f|3/2
∑
C1|1
C2|(1f)∞
deg(C1)+2 deg(C2)≤2g+1
µ(C1)χC1(N f)
|C1||C2|2
∑
V∈Mdeg(N f)+deg(C1)+2 deg(C2)−2g−2
G(V, N f).
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1883
Using the fact that
∑
C2∈Mc2
C2|(1f)∞
1
|C2|2= q−2c2
2πi
∮
|w|=r
∏
P|1f
(1−wdeg(P))−1 dw
wc2+1
for r< 1, and writing V= V1V 2
2 with V1 a square-free polynomial, we have
R(V⁄= 0)= q2g+1τ(q)
|N|
∑
c1+2c2≤2g+1
q−2c2
∑
C1∈Mc1
C1|1
µ(C1)χC1(N)
|C1|
×
∑
n≤X
n+deg(N) odd
∑
j≤n+deg(N)+c1+2c2−2g−2
j+c1 odd
∑
V1∈H j
∑
V2∈M(n+deg(N)+c1− j)/2+c2−g−1
× 1
2πi
∮
|w|=r
∑
f∈Mn
χC1( f)λ( f)G(V1V 2
2, N f)
| f|3/2
∏
P|1f
(1−wdeg(P))−1 dw
wc2+1.
Now
∑
f∈M
χC1( f)λ( f)G(V1V 2
2, N f)
| f|3/2
∏
P|1f
(1−wdeg(P))−1udeg( f)
= H(V1; u,w) I(V1V 2
2, N; u,w) J(V1V 2
2; u,w),
where
H(V1; u,w)=
∏
P ∤V1
(
1+χC1V1(P)λ(P)udeg(P)
|P| (1−wdeg(P))−1
)
,
I(V1V 2
2, N; u,w)=
∏
P|1
(∑
j
χC1(P j)λ(P j)G(V1V 2
2, P j+n P)u j deg(P)
|P|3 j/2
)
(1−wdeg(P))−1
and
J(V1V 2
2; u,w)=
∏
P| V1V2
P ∤1
(
1+
∑
j≥1
χC1(P j)λ(P j)G(V1V 2
2, P j)u j deg(P)
|P|3 j/2 (1−wdeg(P))−1
)
×
∏
P ∤V1
P|1V2
(
1+χC1V1(P)λ(P)udeg(P)
|P| (1−wdeg(P))−1
)−1
.
1884 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
We use the Perron formula for the sum over f and obtain
R(V⁄= 0)= q2g+1τ(q)
|N|
∑
c1+2c2≤2g+1
q−2c2
∑
C1∈Mc1
C1|1
µ(C1)χC1(N)
|C1|
×
∑
n≤X
n+deg(N) odd
∑
j≤n+deg(N)+c1+2c2−2g−2
j+c1 odd
∑
V1∈H j
∑
V2∈M(n+deg(N)+c1− j)/2+c2−g−1
× 1
(2πi)2
∮
|u|=r
∮
|w|=r
H(V1; u,w) I(V1V 2
2, N; u,w) J(V1V 2
2; u,w) du
un+1
dw
wc2+1. (5-4)
Let r1= q1/2−ε, r2= q−ε, and let k0 be minimal such that|r1r k0
2|< 1. Then we can write
H(V1; u,w)= L
(
E⊗χC1V1, u
q
)
L
(
E⊗χC1V1, uw
q
)
··· L
(
E⊗χC1V1, uwk0−1
q
)
K(V1; u,w), (5-5)
where
K(V1; u,w)≪ε|C1|ε
uniformly for|u|≤ r1 and|w|≤ r2. We also have
I(V1V 2
2, N; u,w)≪ε|V1V2|ε and J(V1V 2
2; u,w)≪ε|V2|ε
in this region. We now move the contours in (5 -4) to|u|= r1 and|w|= r2. We then use the Lindelöf
bound for each L-function and trivially bound the rest of the expression to obtain that
R(V⁄= 0)≪ε q X/2+εg.
Combining this with (5-3) ﬁnishes the proof of Lemma 5.1. □
To prove Theorem 1.1, note that from Lemma 2.2 we have
∑
D∈H∗
2g+1
L
(
E⊗χD, 1
2
)
= RE(1,[n/2]+ 2g+ 1)+ϵ2g+1ϵ(E)RE(M,[(n+ 1)/2]+ 2g).
Using Lemma 5.1 and choosing X= g we have that
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
)
= c1(M)L(Sym2 E, 1)+ Oε(q−g+εg),
where
c1(M)=(CE(1; 1)+ϵ2g+1ϵ(E)CE(M; 1))
∏
P|1
|P|+ 1
|P| . (5-6)
This ﬁnishes the proof of the theorem.
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1885
