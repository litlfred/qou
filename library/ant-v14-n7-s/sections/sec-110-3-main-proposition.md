---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-110-3-main-proposition
section_title: "Main proposition"
section_number: 3
pages: 197-206
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
For N|1∞, let
SE1,E2(N, X, Y;α,β):=
∑
D∈H∗
2g+1
∑
f∈M≤X
h∈M≤Y
λ1( f)λ2(h)χD(N f h)
| f|1/2+α|h|1/2+β , (3-1)
whereλi are the Dirichlet coefﬁcients of L(Ei, s) as in (1-1).
Proposition 3.1. Assume X≥ Y . We have
SE(N, X, Y)
:= SE,E(N, X, Y; 0, 0)
=| H2g+1|CE(N; 1, 1, 1)L(Sym2 E, 1)3Y+ O(q2g)+ O(q2g−Y/5g2)+ O(qg/2+3(X+Y)/8g30),
and if E 1⁄= E2, then
SE1,E2(N, X, Y;α,β)
=| H2g+1|CE1,E2(N; 1, 1, 1,α,β) L(Sym2 E1, 1+ 2α)L(Sym2 E2, 1+ 2β) L(E1⊗ E2, 1+α+β)
+ O(q2g−Y/5g2)+ O(qg/2+3(X+Y)/8g30)
uniformly for|α|,|β|≤ 1/g, where the values CE(N; 1, 1, 1) and CE1,E2(N; 1, 1, 1,α,β) are deﬁned in
(3-8), (3-9) and (3-10).
We begin the proof of the proposition by applying Lemma 2.4 and rewriting SE1,E2(N, X, Y;α,β) as
∑
f∈M≤X
h∈M≤Y
λ1( f)λ2(h)
| f|1/2+α|h|1/2+β
∑
C1|1
µ(C1)χC1(N f h)
∑
C2|(1f h)∞
∑
R∈M2g+1−deg(C1)−2 deg(C2)
χR(N f h)
− q
∑
f∈M≤X
h∈M≤Y
λ1( f)λ2(h)
| f|1/2+α|h|1/2+β
∑
C1|1
µ(C1)χC1(N f h)
∑
C2|(1f h)∞
∑
R∈M2g−1−deg(C1)−2 deg(C2)
χR(N f h)
= SE1,E2(N, X, Y, Z;α,β)+ TE1,E2(N, X, Y, Z;α,β), (3-2)
where SE1,E2(N, X, Y, Z;α,β) denotes the contribution of the terms with deg(C2)≤ Z and where
TE1,E2(N, X, Y, Z;α,β) denotes that with deg(C2) > Z for some Z ≤ g. We ﬁrst estimate
TE1,E2(N, X, Y, Z;α,β) , which is easier.
3A. The term T E1,E2(N, X, Y, Z;α,β) .
Lemma 3.2. We have
TE1,E2(N, X, Y, Z;α,β)≪ε q2g−3Z/2g6+ε
uniformly for|α|,|β|≤ 1/g.
1864 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
Proof. It sufﬁces to prove the bound for T
′
E1,E2, which is
∑
f∈M≤X
h∈M≤Y
λ1( f)λ2(h)
| f|1/2+α|h|1/2+β
∑
C1|1
µ(C1)χC1(N f h)
∑
C2|(1f h)∞
deg(C2)>Z
∑
R∈M2g+1−deg(C1)−2 deg(C2)
χR(N f h).
We use the Perron formula for the sum over f and h. We write g(C2)/(rad(C2),1)= C= AB , and
replace f, h by A f and Bh, respectively, where g( f) is deﬁned to be g( f)=∏
P| f P. Then
T
′
E1,E2=
∑
c2>Z
c1+2c2≤2g+1
∑
C1∈Mc1
C2∈Mc2
C1|1,C=AB
µ(C1)χC1(N AB)
|A|1/2+α|B|1/2+β
∑
R∈M2g+1−c1−2c2
χR(N AB)
× 1
(2πi)2
∮
|u|=r
∮
|v|=r
∑
f,h∈M
χC1 R( f h)λ1(A f)λ2(Bh)udeg( f)vdeg(h)
| f|1/2+α|h|1/2+β
× dudv
u X−deg(A)+1vY−deg(B)+1(1− u)(1−v)
for any r< 1. The sum over f and h may be written as
D1(A, B, C1 R; u,v,α,β) L
(
E1⊗χC1 R, u
q1/2+α
)
L
(
E2⊗χC1 R, v
q1/2+β
)
,
where D1(A, B, C1 R; u,v,α,β) is some Euler product which is uniformly convergent provided that
|u|,|v|≤ q−1/g, and satisﬁes
D1(A, B, C1 R; u,v,α,β) ≪τ( AB)
uniformly in this region. Moving the u andv contours to|u|=| v|= q−1/g and using the bound
⏐⏐⏐⏐L
(
E1⊗χC1 R, u
q1/2+α
)
L
(
E2⊗χC1 R, v
q1/2+β
)⏐⏐⏐⏐
≪
⏐⏐⏐⏐L
(
E1⊗χC1 R, u
q1/2+α
)⏐⏐⏐⏐
2
+
⏐⏐⏐⏐L
(
E2⊗χC1 R, v
q1/2+β
)⏐⏐⏐⏐
2
we get
T
′
E1,E2≪ g2 ∑
c2>Z
c1+2c2≤2g+1
∑
C1∈Mc1
C2∈Mc2
C1|1
τ(C)2
√|C|
∮
|u|=q−1/g
∮
|v|=q−1/g
∑
R∈M2g+1−c1−2c2
(⏐⏐⏐⏐L
(
E1⊗χC1 R, u
q1/2+α
)⏐⏐⏐⏐
2
+
⏐⏐⏐⏐L
(
E2⊗χC1 R, v
q1/2+β
)⏐⏐⏐⏐
2)
dudv.
Now let D=(C1, R). Write R= D R1= DE H 2, where E is square-free, and let C1= DC3. Then
⏐⏐⏐⏐L
(
E1⊗χC1 R, u
q1/2+α
)⏐⏐⏐⏐≪ε|DH|ε
⏐⏐⏐⏐L
(
E1⊗χC3 E, u
q1/2+α
)⏐⏐⏐⏐.
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1865
Using upper bounds for moments (see Remark 4.2 after Theorem 4.1), we get that
T
′
E1,E2≪ε q2gg3+ε ∑
C2∈M
Z<deg(C2)≤g
τ(C2)2
√|g(C2)|C2
2
≪ε q2g−3Z/2g6+ε,
and this ﬁnishes the proof of Lemma 3.2. □
3B. The term S E1,E2(N, X, Y, Z;α,β) . Deﬁne S
′
E1,E2(N, X, Y, Z;α,β) to be
∑
f∈M≤X
h∈M≤Y
λ1( f)λ2(h)
| f|1/2+α|h|1/2+β
∑
C1|1
µ(C1)χC1(N f h)
∑
C2|(1f h)∞
deg(C2)≤Z
∑
R∈M2g+1−deg(C1)−2 deg(C2)
χR(N f h),
and S
′′
E1,E2(N, X, Y, Z;α,β) to be the same sum with g being replaced by(g− 1). Then
SE1,E2(N, X, Y, Z;α,β)= S
′
E1,E2(N, X, Y, Z;α,β)− q S
′′
E1,E2(N, X, Y, Z;α,β).
Using Lemma 2.6 on the sum over R, it follows that S
′
E1,E2(N, X, Y, Z;α,β) equals
q2g+1 ∑
f∈M≤X
h∈M≤Y
deg(N f h) even
λ1( f)λ2(h)
|N|| f|3/2+α|h|3/2+β
∑
C1|1
C2|(1f h)∞
deg(C2)≤Z
deg(C1)+2 deg(C2)≤2g+1
µ(C1)χC1(N f h)
|C1||C2|2
×
(
G(0, N f h)+(q− 1)
∑
V∈M≤deg(N f h)+deg(C1)+2 deg(C2)−2g−3
G(V, N f h)−
∑
V∈Mdeg(N f h)+deg(C1)+2 deg(C2)−2g−2
G(V, N f h)
)
+ q2g+1τ(q)
∑
f∈M≤X
h∈M≤Y
deg(N f h) odd
λ1( f)λ2(h)
|N|| f|3/2+α|h|3/2+β
∑
C1|1
C2|(1f h)∞
deg(C2)≤Z
deg(C1)+2 deg(C2)≤2g+1
µ(C1)χC1(N f h)
|C1||C2|2
×
∑
V∈Mdeg(N f h)+deg(C1)+2 deg(C2)−2g−2
G(V, N f h).
Let S
′
E1,E2(V= 0) denote the terms with V= 0 above and S
′
E1,E2(V⁄= 0) be the terms with nonzero V .
The terms S
′′
E1,E2(V= 0) and S
′′
E1,E2(V⁄= 0) are similarly deﬁned. Let
SE1,E2(N, X, Y, Z;α,β; V= 0)= S
′
E1,E2(V= 0)− q S
′′
E1,E2(V= 0)
and
SE1,E2(N, X, Y, Z;α,β; V⁄= 0)= S
′
E1,E2(V⁄= 0)− q S
′′
E1,E2(V⁄= 0)
so that we have
SE1,E2(N, X, Y, Z;α,β)= SE1,E2(N, X, Y, Z;α,β; V= 0)+ SE1,E2(N, X, Y, Z;α,β; V⁄= 0). (3-3)
1866 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
We shall evaluateSE1,E2(N, X, Y, Z;α,β;V=0) in Section 3C and boundSE1,E2(N, X, Y, Z;α,β;V⁄= 0)
in Section 3D.
3C. The V = 0 terms.
Lemma 3.3. We have
SE(N, X, Y, Z; V= 0):= SE,E(N, X, Y, Z; 0, 0; V= 0)
=| H2g+1|CE(N; 1, 1, 1)L(Sym2 E, 1)3Y+ O(q2g)+ O(q2g−Y/5g2),
and if E 1⁄= E2, then
SE1,E2(N, X, Y, Z;α,β; V= 0)
=| H2g+1|CE1,E2(N; 1, 1, 1,α,β) L(Sym2 E1, 1+ 2α)L(Sym2 E2, 1+ 2β) L(E1⊗ E2, 1+α+β)
+ O(q2g−Y/5g2)+ O(q2g−3Z/2)
uniformly for|α|,|β|≤ 1/g, where the values CE(N; 1, 1, 1) and CE1,E2(N; 1, 1, 1,α,β) are deﬁned in
(3-8), (3-9) and (3-10).
Proof. Note that G(0, N f h)⁄= 0 if and only if N f h is a square polynomial, and in this case G(0, N f h)=
φ( N f h). Hence
S
′
E1,E2(V= 0)= q2g+1 ∑
f∈M≤X
h∈M≤Y
N f h=□
λ1( f)λ2(h)φ( N f h)
|N|| f|3/2+α|h|3/2+β
∑
C2|(1f h)∞
deg(C2)≤Z
1
|C2|2
∑
C1|1
(C1,N f h)=1
deg(C1)≤2g+1−2 deg(C2)
µ(C1)
|C1| . (3-4)
We have
∑
C1|1
(C1,N f h)=1
deg(C1)≤2g+1−2 deg(C2)
µ(C1)
|C1| =
∑
C1|1
(C1,N f h)=1
µ(C1)
|C1| −
∑
C1|1
(C1,N f h)=1
deg(C1)>2g+1−2 deg(C2)
µ(C1)
|C1|
=
∏
P|1
P ∤ N f h
(
1− 1
|P|
)
+ O(q−2g|C2|2)
= |N f h|
φ( N f h)
∏
P|1f h
(
1− 1
|P|
)
+ O(q−2g|C2|2). (3-5)
Note that ∑
C2∈Mn
C2|(1f h)∞
1≪ε qεn. (3-6)
Let N= N 2
1 N2 with N2 being square-free. The condition N f h= □ is equivalent to f h= N2𝓁2 for some
polynomial𝓁. Then we can write f= N′
2 A and h= N′′
2 B, with N′
2N′′
2= N2 and AB=𝓁2. It follows
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1867
that the contribution of the error term in (3-5) to (3-4) will be
≪ε qεg ∑
𝓁∈M≤(X+Y)/2
1
|𝓁|
∑
AB=𝓁2
|λ1(N′
2 A)λ2(N′′
2 B)|≪ε qεg,
by using the bound|λi( f)|≤ τ( f)≪ε| f|ε. Thus we can rewrite (3-4) as
S
′
E1,E2(V= 0)= q2g+1 ∑
f∈M≤X
h∈M≤Y
N f h=□
λ1( f)λ2(h)
| f|1/2+α|h|1/2+β
∏
P|1f h
(
1− 1
|P|
) ∑
C2|(1f h)∞
deg(C2)≤Z
1
|C2|2+ Oε(qεg).
We obtain a similar estimate for S
′′
E1,E2(V= 0) with g being replaced by(g− 1), and hence
SE1,E2(N, X, Y, Z;α,β; V= 0)
=| H2g+1|
∑
f∈M≤X
h∈M≤Y
N f h=□
λ1( f)λ2(h)
| f|1/2+α|h|1/2+β
∏
P|1f h
(
1− 1
|P|
) ∑
C2|(1f h)∞
deg(C2)≤Z
1
|C2|2+ Oε(qεg). (3-7)
From the Perron formula for the sum over C2,
∑
C2|(1f h)∞
deg(C2)≤Z
1
|C2|2= 1
2πi
∮
|w|=r
∏
P|1f h
(
1−wdeg(P)
|P|2
)−1 dw
wZ+1(1−w)
for any r< 1, it follows that
SE1,E2(N, X, Y, Z;α,β; V= 0)
=|H2g+1|
(2πi)3
∮
|u|=r
∮
|v|=r
∮
|w|=r
AE1,E2(N; u,v,w,α,β) dudvdw
u X+1vY+1wZ+1(1− u)(1−v)(1−w)+ Oε(qεg),
where
AE1,E2(N; u,v,w,α,β) =
∑
f,h∈M
N f h=□
λ1( f)λ2(h)udeg( f)vdeg(h)
| f|1/2+α|h|1/2+β
∏
P|1f h
(
1− 1
|P|
)(
1−wdeg(P)
|P|2
)−1
.
We can write down an Euler product for AE1,E2(N; u,v,w,α,β) as follows.
AE1,E2(N; u,v,w,α,β)
=
∏
P ∤1
(
1+
(
1− 1
|P|
)(
1−wdeg(P)
|P|2
)−1 ∑
i+ j even≥2
λ1(Pi)λ2(P j)ui deg(P)v j deg(P)
|P|(1/2+α)i+(1/2+β) j
)
×
∏
P|1
((
1− 1
|P|
)(
1−wdeg(P)
|P|2
)−1 ∑
i, j
i+ j+ordP(N) even
λ1(Pi)λ2(P j)ui deg(P)v j deg(P)
|P|(1/2+α)i+(1/2+β) j
)
. (3-8)
1868 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
Then
AE(N; u,v,w, 0, 0)
:= AE,E(N; u,v,w, 0, 0)
= CE(N; u,v,w) L
(
Sym2 E, u2
q
)
L
(
Sym2 E,v2
q
)
× L
(
Sym2 E, uv
q
)
Z
(uv
q
)
, (3-9)
and
AE1,E2(N; u,v,w,α,β)
= CE1,E2(N; u,v,w,α,β) L
(
Sym2 E1, u2
q1+2α
)
L
(
Sym2 E2, v2
q1+2β
)
L
(
E1⊗ E2, uv
q1+α+β
)
, (3-10)
if E1⁄= E2, where CE(N; u,v,w) and CE1,E2(N; u,v,w,α,β) are some Euler products which are
uniformly bounded for example when|u|,|v|≤ q1/5,|w|≤ q3/2.
Consider the case E1= E2= E. We have
SE(N, X, Y, Z; V= 0)
=|H2g+1|
(2πi)3
∮
|u|=r
∮
|v|=r
∮
|w|=r
CE(N; u,v,w) L
(
Sym2 E, u2
q
)
×L
(
Sym2 E,v2
q
)
L
(
Sym2 E, uv
q
) dudvdw
u X+1vY+1wZ+1(1−u)(1−v)(1−w)(1−uv)+Oε(qεg) (3-11)
for any r< 1. We choose r= q−1/g and move the u contour to|u|= q1/5, encountering two simple poles
at u= 1 and u= 1/v. The new integral is trivially bounded by O(q2g−X/5g2).
Furthermore, the contribution from the residue at u= 1/v is
−|H2g+1|L(Sym2 E, 1) 1
(2πi)2
∮
|v|=q−1/g
∮
|w|=q−1/g
CE(N; 1/v,v,w)
× L
(
Sym2 E, 1
v2q
)
L
(
Sym2 E,v2
q
) dvdw
vY−XwZ+1(1−v)2(1−w),
which is O(q2g). This can be seen by ﬁrst moving the v contour to|v|= q−1/5, creating no poles, and
then moving thew contour to|w|= q3/2, crossing a simple pole at w= 1. Both the new integral and the
residue atw= 1 are O(q2g) as X≥ Y . So
SE(N, X, Y, Z; V= 0)=| H2g+1|L(Sym2 E, 1) 1
(2πi)2
∮
|v|=q−1/g
∮
|w|=q−1/g
CE(N; 1,v,w)
× L
(
Sym2 E,v2
q
)
L
(
Sym2 E,v
q
) dvdw
vY+1wZ+1(1−v)2(1−w)
+ O(q2g)+ O(q2g−X/5g2).
We now move thev contour to|v|= q1/5, encountering a double pole at v= 1. The new integral is
bounded by O(q2g−Y/5g), and an argument similar to the above implies that the residue at v= 1 is
|H2g+1|L(Sym2 E, 1)3Y 1
2πi
∮
|w|=q−1/g
CE(N; 1, 1,w) dw
wZ+1(1−w)+ O(q2g).
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1869
Hence
SE(N, X, Y, Z; V= 0)=| H2g+1|CE(N; 1, 1, 1)L(Sym2 E, 1)3Y+ O(q2g)+ O(q2g−Y/5g2).
For E1⁄= E2, we have that
SE1,E2(N, X, Y, Z;α,β; V= 0)
=|H2g+1|
(2πi)3
∮
|u|=r
∮
|v|=r
∮
|w|=r
CE1,E2(N; u,v,w,α,β) L
(
Sym2 E1, u2
q1+2α
)
L
(
Sym2 E2, v2
q1+2β
)
× L
(
E1⊗ E2, uv
q1+α+β
) dudvdw
u X+1vY+1wZ+1(1− u)(1−v)(1−w)+ Oε(qεg)
for any r< 1. We choose r= q−1/g and ﬁrst shift the u contour to|u|= q1/5, encountering a pole at
u= 1. The new integral over|u|= q1/5,|v|=| w|= q−1/g is bounded by q2g−X/5g2. To calculate the
residue at u= 1, we move the v contour to|v|= q1/5, crossing a pole at v= 1. The new integral is
O(q2g−Y/5g). For the residue at u=v= 1, we move thew contour to|w|= q3/2. In doing so we obtain
SE1,E2(N, X, Y, Z;α,β; V= 0)=| H2g+1|CE1,E2(N; 1, 1, 1,α,β) L(Sym2 E1, 1+ 2α)
× L(Sym2 E2, 1+ 2β) L(E1⊗ E2, 1+α+β)
+ O(q2g−Y/5g2)+ O(q2g−3Z/2),
and this concludes the proof of the lemma. □
3D. The V ⁄= 0 terms.
Lemma 3.4. We have
SE1,E2(N, X, Y, Z;α,β; V⁄= 0)≪ q(X+Y+Z)/2g30
uniformly for|α|,|β|≤ 1/g.
Proof. We will prove the bound for the term
S(V⁄= 0)= q2g+1τ(q)
∑
f∈M≤X
h∈M≤Y
deg(N f h) odd
λ1( f)λ2(h)
|N|| f|3/2+α|h|3/2+β
∑
C1|1
C2|(1f h)∞
deg(C2)≤Z
deg(C1)+2 deg(C2)≤2g+1
µ(C1)χC1(N f h)
|C1||C2|2
×
∑
V∈Mdeg(N f h)+deg(C1)+2 deg(C2)−2g−2
G(V, N f h), (3-12)
the treatment of the other terms being similar. We also assume for simplicity that deg(N), X and Y are
all odd. The other cases can be done similarly.
1870 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
We use the Perron formula in the forms
∑
f∈M≤X
deg( f) odd
a( f)= 1
2πi
∮
|u|=r
(∑
f∈M
a( f)udeg( f)
) du
u X+1(1− u2)
and
∑
f∈M≤X
deg( f) even
a( f)= 1
2πi
∮
|u|=r
(∑
f∈M
a( f)udeg( f)
) du
u X(1− u2)
for the sums over f and h. We write V= V1V 2
2 with V1 being a square-free polynomial and V2∈ M,
g(C2)/(rad(C2),1)= C= AB , and replace f, h by A f and Bh, respectively. We then see that
S(V⁄= 0)= q2g+1τ(q)
∑
c2≤Z
c1+2c2≤2g+1
∑
C1∈Mc1
C2∈Mc2
C1|1,C=AB
µ(C1)χC1(N AB)
|N||A|3/2+α|B|3/2+β|C1||C2|2
× 1
(2πi)3
∮
|u|=r
∮
|v|=r
∮
|w|=r
∑
V1∈H
B(N, A, B, C1, V1; u/w,v/w,w,α,β)
× (1+ uv)dudvdw
u X−deg(A)+1vY−deg(B)+1wdeg(N AB)−deg(V1)+c1+2c2−2g−1(1− u2)(1−v2) (3-13)
for any r< 1, where B(N, A, B, C1, V1; u,v,w,α,β) equals
∑
f,h,V2∈M
χC1( f h)λ1(A f)λ2(Bh)udeg( f)vdeg(h)w2 deg(V2)G(V1V 2
2, N AB f h)
| f|3/2+α|h|3/2+β .
To proceed we need to study the function B(N, A, B, C1, V1; u,v,w,α,β) .
Lemma 3.5. The function B(N, A, B, C1, V1; u,v,w,α,β) deﬁned above may be written as
D2(N, A, B, C1, V1; u,v,w,α,β) L
(
E1⊗χC1V1, u
q1+α
)
L
(
E2⊗χC1V1, v
q1+β
)
,
where D2(N, A, B, C1, V1; u,v,w,α,β) is some Euler product which is uniformly convergent provided
that|u|,|v|≤ q1/2−2/g,|w|≤ q−1/2−ε, and satisﬁes
D2(N, A, B, C1, V1; u,v,w,α,β) ≪ g10τ10(AB)
√
AB
uniformly in this region.
Proof. It is easy to see that B(N, A, B, C1, V1; u,v,w,α,β) converges absolutely if|u|,|v|≤ q−ε and
|w|≤ q−1/2−ε. We claim that the sum over f, h and V2 is triply multiplicative. Indeed, one can easily see
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1871
that the double sum over f, h is multiplicative, so
∑
f,h∈M
χC1( f h)λ1(A f)λ2(Bh)udeg( f)vdeg(h)G(V1V 2
2, N AB f h)
| f|3/2+α|h|3/2+β
=
∏
P
(∑
i, j
χC1(Pi+ j)λ1(Pi+aP)λ2(P j+bP)ui deg(P)v j deg(P)G(V1V 2
2, Pi+ j+aP+bP+n P)
|P|(3/2+α)i+(3/2+β) j
)
,
where aP, bP and n P denote the orders of A, B and N with respect to P respectively. Let AP(V2) denote
the Euler product above. Note that when P ∤V2, we have AP(V2)= AP(1). Then we rewrite the double
sum over f, h as ∏
P
AP(1)
∏
P| V2
AP(V2)
AP(1) .
We introduce the sum over V2 and use the observation that for (V2, V3)= 1 and P ∤V3 we have
AP(V2V3)= AP(V2). Then
∏
P
AP(1)
∑
V2∈M
w2 deg(V2) ∏
P| V2
AP(V2)
AP(1)
=
∏
P
AP(1)
∏
P
(
1+ 1
AP(1)
∑
k
AP(Pk)w2k deg(P)
)
=
∏
P
(∑
i, j,k
χC1(Pi+ j)λ1(Pi+aP)λ2(P j+bP)ui deg(P)v j deg(P)w2k deg(P)G(V1 P2k, Pi+ j+aP+bP+n P)
|P|(3/2+α)i+(3/2+β) j
)
,
and hence the generating series for f, h, V2 is indeed triply multiplicative.
Now we rewrite B(N, A, B, C1, V1; u,v,w,α,β) as
∏
P ∤C1
(∑
i, j,k
χC1(Pi+ j)λ1(Pi+aP)λ2(P j+bP)ui deg(P)v j deg(P)w2k deg(P)G(V1 P2k, Pi+ j+aP+bP+n P)
|P|(3/2+α)i+(3/2+β) j
)
×
∏
P| C1
(∑
k
λ1(PaP)λ2(PbP)w2k deg(P)G(V1 P2k, PaP+bP+n P)
)
.
We next compute the Euler factors at an irreducible P in the region|u|,|v|≤ q1/2−2/g,|w|≤ q−1/2−ε.
Note that in this region, w2k deg(P)≪ε|P|−1−ε if k≥ 1.
Consider ﬁrst the case when P ∤ N ABC 1V1. The contribution of such an Euler factor is
∑
i, j,k
χC1(Pi+ j)λ1(Pi)λ2(P j)ui deg(P)v j deg(P)w2k deg(P)G(V1 P2k, Pi+ j)
|P|(3/2+α)i+(3/2+β) j .
In view of Lemma 2.5, this is equal to
1+χC1V1(P)λ1(P)udeg(P)
|P|1+α +χC1V1(P)λ2(P)vdeg(P)
|P|1+β + O
( 1
|P|1+ε
)
,
which justiﬁes the two L-functions.
1872 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
In the case P| V1 but P ∤ N ABC 1, the Euler factor equals
∑
i, j
χC1(Pi+ j)λ1(Pi)λ2(P j)ui deg(P)v j deg(P)G(V1, Pi+ j)
|P|(3/2+α)i+(3/2+beta) j + O
( 1
|P|1+ε
)
= 1−λ1(P2)u2 deg(P)
|P|2+2α −λ1(P)λ2(P)(uv)deg(P)
|P|2+α+β −λ2(P2)v2 deg(P)
|P|2+2β + O
( 1
|P|1+ε
)
= 1+ O
( 1
|P|1+2/g
)
.
Similarly, the corresponding Euler factor is
=



O(|P|1/2) if P| AB and P ∤ NC 1V1,
O(1) if P| AB, P| V1 and P ∤ NC 1,
1+ O(1/|P|1+ε) if P| C1 and P ∤ N AB,
O(|P|1/2) if P| C1, P| AB and P ∤ N V1,
0 if P| C1, P| AB, P| V1 and P ∤ N,
and is
≪ε
∑
i+ j≤2k
|P|1−(1+ε)k−(i+ j)/2≪ε|P|,
if P| N.
The lemma easily follows by combining these estimates. □
We now return to (3-13). In view of Lemma 3.5, we take r≤ q−1/2−ε and move the u andv contours
to|u|=| v|= rq 1/2−2/g. This creates no poles. Then, by the above result,
B(N, A, B, C1, V1; u/w,v/w,w,α,β)
≪ g10τ10(AB)
√
AB
⏐⏐⏐⏐L
(
E1⊗χC1V1, u/w
q1+α
)
L
(
E2⊗χC1V1, v/w
q1+β
)⏐⏐⏐⏐
≪ g10τ10(AB)
√
AB
(⏐⏐⏐⏐L
(
E1⊗χC1V1, u/w
q1+α
)⏐⏐⏐⏐
2
+
⏐⏐⏐⏐L
(
E2⊗χC1V1, v/w
q1+β
)⏐⏐⏐⏐
2)
.
So
S(V⁄= 0)
≪ q2g−(X+Y)/2g10 ∑
c2≤Z
c1+2c2≤2g+1
∑
C1∈Mc1
C2∈Mc2
C1|1
τ(C)τ10(C)τ(C1)√|C||C1||C2|2
×
∮
|u|=q1/2−1/g
∮
|v|=q1/2−1/g
∮
|w|=r
∑
V1∈H
⏐⏐⏐⏐L
(
E1⊗χC1V1, u
q1+α
)⏐⏐⏐⏐
2 dudvdw
|w|X+Y+deg(N)−deg(V1)+c1+2c2−2g+1.
If deg(V1)≤ X+ Y+ c1+ 2c2− 2g, then we move thew contour to|w|= q−3/4, otherwise we move the
