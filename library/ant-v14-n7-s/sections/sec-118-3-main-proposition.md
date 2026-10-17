---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory"
section_id: sec-118-3-main-proposition
section_title: "Main proposition"
section_number: 3
pages: 197-200
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
toc_source: outline
---
For N | 1∞, let
SE1,E2(N, X, Y; α, β) :=
X
D∈H∗
2g+1
X
f ∈M≤X
h∈M≤Y
λ1( f )λ2(h)χD(N f h)
| f |1/2+α|h|1/2+β
,
(3-1)
where λi are the Dirichlet coefﬁcients of L(Ei, s) as in (1-1).
Proposition 3.1. Assume X ≥Y. We have
SE(N, X, Y)
: = SE,E(N, X, Y; 0, 0)
= |H2g+1|CE(N; 1, 1, 1)L(Sym2 E, 1)3Y + O(q2g) + O(q2g−Y/5g2) + O(qg/2+3(X+Y)/8g30),
and if E1̸ = E2, then
SE1,E2(N, X, Y; α, β)
= |H2g+1|CE1,E2(N; 1, 1, 1, α, β)L(Sym2 E1, 1 + 2α)L(Sym2 E2, 1 + 2β)L(E1 ⊗E2, 1 + α + β)
+ O(q2g−Y/5g2) + O(qg/2+3(X+Y)/8g30)
uniformly for |α|, |β| ≤1/g, where the values CE(N; 1, 1, 1) and CE1,E2(N; 1, 1, 1, α, β) are deﬁned in
(3-8), (3-9) and (3-10).
We begin the proof of the proposition by applying Lemma 2.4 and rewriting SE1,E2(N, X, Y; α, β) as
X
f ∈M≤X
h∈M≤Y
λ1( f )λ2(h)
| f |1/2+α|h|1/2+β
X
C1 | 1
µ(C1)χC1(N f h)
X
C2 | (1f h)∞
X
R∈M2g+1−deg(C1)−2 deg(C2)
χR(N f h)
−q
X
f ∈M≤X
h∈M≤Y
λ1( f )λ2(h)
| f |1/2+α|h|1/2+β
X
C1 | 1
µ(C1)χC1(N f h)
X
C2 | (1f h)∞
X
R∈M2g−1−deg(C1)−2 deg(C2)
χR(N f h)
= SE1,E2(N, X, Y, Z; α, β) + TE1,E2(N, X, Y, Z; α, β),
(3-2)
where SE1,E2(N, X, Y, Z; α, β) denotes the contribution of the terms with deg(C2) ≤Z and where
TE1,E2(N, X, Y, Z; α, β) denotes that with deg(C2) > Z for some Z ≤g.
We ﬁrst estimate
TE1,E2(N, X, Y, Z; α, β), which is easier.
3A. The term TE1,E2(N, X, Y, Z; α, β).
Lemma 3.2. We have
TE1,E2(N, X, Y, Z; α, β) ≪ε q2g−3Z/2g6+ε
uniformly for |α|, |β| ≤1/g.
1864
Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
Proof. It sufﬁces to prove the bound for T
′
E1,E2, which is
X
f ∈M≤X
h∈M≤Y
λ1( f )λ2(h)
| f |1/2+α|h|1/2+β
X
C1 | 1
µ(C1)χC1(N f h)
X
C2 | (1f h)∞
deg(C2)>Z
X
R∈M2g+1−deg(C1)−2 deg(C2)
χR(N f h).
We use the Perron formula for the sum over f and h. We write g(C2)/(rad(C2), 1) = C = AB, and
replace f, h by Af and Bh, respectively, where g( f ) is deﬁned to be g( f ) = Q
P | f P. Then
T
′
E1,E2 =
X
c2>Z
c1+2c2≤2g+1
X
C1∈Mc1
C2∈Mc2
C1 | 1,C=AB
µ(C1)χC1(N AB)
|A|1/2+α|B|1/2+β
X
R∈M2g+1−c1−2c2
χR(N AB)
×
1
(2πi)2
I
|u|=r
I
|v|=r
X
f,h∈M
χC1R( f h)λ1(Af )λ2(Bh)udeg( f )vdeg(h)
| f |1/2+α|h|1/2+β
×
dudv
uX−deg(A)+1vY−deg(B)+1(1 −u)(1 −v)
for any r < 1. The sum over f and h may be written as
D1(A, B, C1R; u, v, α, β)L

E1 ⊗χC1R,
u
q1/2+α

L

E2 ⊗χC1R,
v
q1/2+β

,
where D1(A, B, C1R; u, v, α, β) is some Euler product which is uniformly convergent provided that
|u|, |v| ≤q−1/g, and satisﬁes
D1(A, B, C1R; u, v, α, β) ≪τ(AB)
uniformly in this region. Moving the u and v contours to |u| = |v| = q−1/g and using the bound

L

E1 ⊗χC1R,
u
q1/2+α

L

E2 ⊗χC1R,
v
q1/2+β


≪

L

E1 ⊗χC1R,
u
q1/2+α


2
+

L

E2 ⊗χC1R,
v
q1/2+β


2
we get
T
′
E1,E2 ≪g2
X
c2>Z
c1+2c2≤2g+1
X
C1∈Mc1
C2∈Mc2
C1 | 1
τ(C)2
√|C|
I
|u|=q−1/g
I
|v|=q−1/g
X
R∈M2g+1−c1−2c2


L

E1 ⊗χC1R,
u
q1/2+α


2
+

L

E2 ⊗χC1R,
v
q1/2+β


2
dudv.
Now let D = (C1, R). Write R = DR1 = DE H2, where E is square-free, and let C1 = DC3. Then

L

E1 ⊗χC1R,
u
q1/2+α


 ≪ε |DH|ε

L

E1 ⊗χC3E,
u
q1/2+α


.
Moments of quadratic twists of elliptic curve L-functions over function ﬁelds
1865
Using upper bounds for moments (see Remark 4.2 after Theorem 4.1), we get that
T
′
E1,E2 ≪ε q2gg3+ε
X
C2∈M
Z<deg(C2)≤g
τ(C2)2
√|g(C2)|C2
2
≪ε q2g−3Z/2g6+ε,
and this ﬁnishes the proof of Lemma 3.2.
□
3B. The term SE1,E2(N, X, Y, Z; α, β). Deﬁne S
′
E1,E2(N, X, Y, Z; α, β) to be
X
f ∈M≤X
h∈M≤Y
λ1( f )λ2(h)
| f |1/2+α|h|1/2+β
X
C1 | 1
µ(C1)χC1(N f h)
X
C2 | (1f h)∞
deg(C2)≤Z
X
R∈M2g+1−deg(C1)−2 deg(C2)
χR(N f h),
and S
′′
E1,E2(N, X, Y, Z; α, β) to be the same sum with g being replaced by (g −1). Then
SE1,E2(N, X, Y, Z; α, β) = S
′
E1,E2(N, X, Y, Z; α, β) −qS
′′
E1,E2(N, X, Y, Z; α, β).
Using Lemma 2.6 on the sum over R, it follows that S
′
E1,E2(N, X, Y, Z; α, β) equals
q2g+1
X
f ∈M≤X
h∈M≤Y
deg(N f h) even
λ1( f )λ2(h)
|N|| f |3/2+α|h|3/2+β
X
C1 | 1
C2 | (1f h)∞
deg(C2)≤Z
deg(C1)+2 deg(C2)≤2g+1
µ(C1)χC1(N f h)
|C1||C2|2
×

G(0, N f h) + (q −1)
X
V ∈M≤deg(N f h)+deg(C1)+2 deg(C2)−2g−3
G(V, N f h) −
X
V ∈Mdeg(N f h)+deg(C1)+2 deg(C2)−2g−2
G(V, N f h)

+ q2g+1τ(q)
X
f ∈M≤X
h∈M≤Y
deg(N f h) odd
λ1( f )λ2(h)
|N|| f |3/2+α|h|3/2+β
X
C1 | 1
C2 | (1f h)∞
deg(C2)≤Z
deg(C1)+2 deg(C2)≤2g+1
µ(C1)χC1(N f h)
|C1||C2|2
×
X
V ∈Mdeg(N f h)+deg(C1)+2 deg(C2)−2g−2
G(V, N f h).
Let S
′
E1,E2(V = 0) denote the terms with V = 0 above and S
′
E1,E2(V̸ = 0) be the terms with nonzero V .
The terms S
′′
E1,E2(V = 0) and S
′′
E1,E2(V̸ = 0) are similarly deﬁned. Let
SE1,E2(N, X, Y, Z; α, β; V = 0) = S
′
E1,E2(V = 0) −qS
′′
E1,E2(V = 0)
and
SE1,E2(N, X, Y, Z; α, β; V̸ = 0) = S
′
E1,E2(V̸ = 0) −qS
′′
E1,E2(V̸ = 0)
so that we have
SE1,E2(N, X, Y, Z; α, β) = SE1,E2(N, X, Y, Z; α, β; V = 0) + SE1,E2(N, X, Y, Z; α, β; V̸ = 0). (3-3)
1866
Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
We shall evaluate SE1,E2(N, X, Y, Z; α, β;V =0) in Section 3C and bound SE1,E2(N, X, Y, Z; α, β;V̸ =0)
in Section 3D.
