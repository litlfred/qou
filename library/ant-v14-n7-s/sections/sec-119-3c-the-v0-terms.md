---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory"
section_id: sec-119-3c-the-v0-terms
section_title: "3C. The V=0 terms"
section_number: null
pages: 200-203
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
toc_source: outline
---
Lemma 3.3. We have
SE(N, X, Y, Z; V = 0) : = SE,E(N, X, Y, Z; 0, 0; V = 0)
= |H2g+1|CE(N; 1, 1, 1)L(Sym2 E, 1)3Y + O(q2g) + O(q2g−Y/5g2),
and if E1̸ = E2, then
SE1,E2(N, X, Y, Z; α, β; V = 0)
= |H2g+1|CE1,E2(N; 1, 1, 1, α, β)L(Sym2 E1, 1 + 2α)L(Sym2 E2, 1 + 2β)L(E1 ⊗E2, 1 + α + β)
+ O(q2g−Y/5g2) + O(q2g−3Z/2)
uniformly for |α|, |β| ≤1/g, where the values CE(N; 1, 1, 1) and CE1,E2(N; 1, 1, 1, α, β) are deﬁned in
(3-8), (3-9) and (3-10).
Proof. Note that G(0, N f h)̸ = 0 if and only if N f h is a square polynomial, and in this case G(0, N f h) =
φ(N f h). Hence
S
′
E1,E2(V = 0) = q2g+1
X
f ∈M≤X
h∈M≤Y
N f h=□
λ1( f )λ2(h)φ(N f h)
|N|| f |3/2+α|h|3/2+β
X
C2 | (1f h)∞
deg(C2)≤Z
1
|C2|2
X
C1 | 1
(C1,N f h)=1
deg(C1)≤2g+1−2 deg(C2)
µ(C1)
|C1| .
(3-4)
We have
X
C1 | 1
(C1,N f h)=1
deg(C1)≤2g+1−2 deg(C2)
µ(C1)
|C1| =
X
C1 | 1
(C1,N f h)=1
µ(C1)
|C1| −
X
C1 | 1
(C1,N f h)=1
deg(C1)>2g+1−2 deg(C2)
µ(C1)
|C1|
=
Y
P | 1
P ∤N f h

1 −1
|P|

+ O(q−2g|C2|2)
= |N f h|
φ(N f h)
Y
P | 1f h

1 −1
|P|

+ O(q−2g|C2|2).
(3-5)
Note that
X
C2∈Mn
C2 | (1f h)∞
1 ≪ε qεn.
(3-6)
Let N = N 2
1 N2 with N2 being square-free. The condition N f h = □is equivalent to f h = N2ℓ2 for some
polynomial ℓ. Then we can write f = N ′
2A and h = N ′′
2 B, with N ′
2N ′′
2 = N2 and AB = ℓ2. It follows
Moments of quadratic twists of elliptic curve L-functions over function ﬁelds
1867
that the contribution of the error term in (3-5) to (3-4) will be
≪ε qεg
X
ℓ∈M≤(X+Y)/2
1
|ℓ|
X
AB=ℓ2
|λ1(N ′
2A)λ2(N ′′
2 B)| ≪ε qεg,
by using the bound |λi( f )| ≤τ( f ) ≪ε | f |ε. Thus we can rewrite (3-4) as
S
′
E1,E2(V = 0) = q2g+1
X
f ∈M≤X
h∈M≤Y
N f h=□
λ1( f )λ2(h)
| f |1/2+α|h|1/2+β
Y
P | 1f h

1 −1
|P|

X
C2 | (1f h)∞
deg(C2)≤Z
1
|C2|2 + Oε(qεg).
We obtain a similar estimate for S
′′
E1,E2(V = 0) with g being replaced by (g −1), and hence
SE1,E2(N, X, Y, Z; α, β; V = 0)
= |H2g+1|
X
f ∈M≤X
h∈M≤Y
N f h=□
λ1( f )λ2(h)
| f |1/2+α|h|1/2+β
Y
P | 1f h

1 −1
|P|

X
C2 | (1f h)∞
deg(C2)≤Z
1
|C2|2 + Oε(qεg).
(3-7)
From the Perron formula for the sum over C2,
X
C2 | (1f h)∞
deg(C2)≤Z
1
|C2|2 =
1
2πi
I
|w|=r
Y
P | 1f h

1 −wdeg(P)
|P|2
−1
dw
wZ+1(1 −w)
for any r < 1, it follows that
SE1,E2(N, X, Y, Z; α, β; V = 0)
= |H2g+1|
(2πi)3
I
|u|=r
I
|v|=r
I
|w|=r
AE1,E2(N; u, v, w, α, β)
dudvdw
uX+1vY+1wZ+1(1 −u)(1 −v)(1 −w) + Oε(qεg),
where
AE1,E2(N; u, v, w, α, β) =
X
f,h∈M
N f h=□
λ1( f )λ2(h)udeg( f )vdeg(h)
| f |1/2+α|h|1/2+β
Y
P | 1f h

1 −1
|P|

1 −wdeg(P)
|P|2
−1
.
We can write down an Euler product for AE1,E2(N; u, v, w, α, β) as follows.
AE1,E2(N; u, v, w, α, β)
=
Y
P ∤1

1 +

1 −1
|P|

1 −wdeg(P)
|P|2
−1
X
i+ j even≥2
λ1(Pi)λ2(P j)ui deg(P)v j deg(P)
|P|(1/2+α)i+(1/2+β) j

×
Y
P | 1

1 −1
|P|

1 −wdeg(P)
|P|2
−1
X
i, j
i+ j+ordP(N) even
λ1(Pi)λ2(P j)ui deg(P)v j deg(P)
|P|(1/2+α)i+(1/2+β) j

.
(3-8)
1868
Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
Then
AE(N; u, v, w, 0, 0)
:= AE,E(N; u, v, w, 0, 0)
= CE(N; u, v, w)L

Sym2 E, u2
q

L

Sym2 E, v2
q

× L

Sym2 E, uv
q

Z
uv
q

,
(3-9)
and
AE1,E2(N; u, v, w, α, β)
= CE1,E2(N; u, v, w, α, β)L

Sym2 E1,
u2
q1+2α

L

Sym2 E2,
v2
q1+2β

L

E1 ⊗E2,
uv
q1+α+β

,
(3-10)
if E1̸ = E2, where CE(N; u, v, w) and CE1,E2(N; u, v, w, α, β) are some Euler products which are
uniformly bounded for example when |u|, |v| ≤q1/5, |w| ≤q3/2.
Consider the case E1 = E2 = E. We have
SE(N, X, Y, Z; V = 0)
= |H2g+1|
(2πi)3
I
|u|=r
I
|v|=r
I
|w|=r
CE(N; u, v, w)L

Sym2 E, u2
q

×L

Sym2 E, v2
q

L

Sym2 E, uv
q

dudvdw
uX+1vY+1wZ+1(1−u)(1−v)(1−w)(1−uv)+Oε(qεg)
(3-11)
for any r < 1. We choose r = q−1/g and move the u contour to |u| = q1/5, encountering two simple poles
at u = 1 and u = 1/v. The new integral is trivially bounded by O(q2g−X/5g2).
Furthermore, the contribution from the residue at u = 1/v is
−|H2g+1|L(Sym2 E, 1)
1
(2πi)2
I
|v|=q−1/g
I
|w|=q−1/g CE(N; 1/v, v, w)
× L

Sym2 E, 1
v2q

L

Sym2 E, v2
q

dvdw
vY−XwZ+1(1 −v)2(1 −w),
which is O(q2g). This can be seen by ﬁrst moving the v contour to |v| = q−1/5, creating no poles, and
then moving the w contour to |w| = q3/2, crossing a simple pole at w = 1. Both the new integral and the
residue at w = 1 are O(q2g) as X ≥Y. So
SE(N, X, Y, Z; V = 0) = |H2g+1|L(Sym2 E, 1)
1
(2πi)2
I
|v|=q−1/g
I
|w|=q−1/g CE(N; 1, v, w)
× L

Sym2 E, v2
q

L

Sym2 E, v
q

dvdw
vY+1wZ+1(1 −v)2(1 −w)
+ O(q2g) + O(q2g−X/5g2).
We now move the v contour to |v| = q1/5, encountering a double pole at v = 1. The new integral is
bounded by O(q2g−Y/5g), and an argument similar to the above implies that the residue at v = 1 is
|H2g+1|L(Sym2 E, 1)3Y 1
2πi
I
|w|=q−1/gCE(N; 1, 1, w)
dw
wZ+1(1 −w) + O(q2g).
Moments of quadratic twists of elliptic curve L-functions over function ﬁelds
1869
Hence
SE(N, X, Y, Z; V = 0) = |H2g+1|CE(N; 1, 1, 1)L(Sym2 E, 1)3Y + O(q2g) + O(q2g−Y/5g2).
For E1̸ = E2, we have that
SE1,E2(N, X, Y, Z; α, β; V = 0)
= |H2g+1|
(2πi)3
I
|u|=r
I
|v|=r
I
|w|=r
CE1,E2(N; u, v, w, α, β)L

Sym2 E1,
u2
q1+2α

L

Sym2 E2,
v2
q1+2β

× L

E1 ⊗E2,
uv
q1+α+β

dudvdw
uX+1vY+1wZ+1(1 −u)(1 −v)(1 −w) + Oε(qεg)
for any r < 1. We choose r = q−1/g and ﬁrst shift the u contour to |u| = q1/5, encountering a pole at
u = 1. The new integral over |u| = q1/5, |v| = |w| = q−1/g is bounded by q2g−X/5g2. To calculate the
residue at u = 1, we move the v contour to |v| = q1/5, crossing a pole at v = 1. The new integral is
O(q2g−Y/5g). For the residue at u = v = 1, we move the w contour to |w| = q3/2. In doing so we obtain
SE1,E2(N, X, Y, Z; α, β; V = 0) = |H2g+1|CE1,E2(N; 1, 1, 1, α, β)L(Sym2 E1, 1 + 2α)
× L(Sym2 E2, 1 + 2β)L(E1 ⊗E2, 1 + α + β)
+ O(q2g−Y/5g2) + O(q2g−3Z/2),
and this concludes the proof of the lemma.
□
