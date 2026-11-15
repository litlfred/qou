---
doc_id: ant-v14-n7-s-p06
doc_title: "Moments of quadratic twists of elliptic curve L-functions over function fields"
section_id: sec-003-2-n-ab-f-h
section_title: ", N AB f h)"
section_number: 2
pages: 18-21
source_pdf: ant-v14-n7-s-p06.pdf
source_sha256: 4881141ef679dd5a
toc_source: inferred
doc_brief: "Moments of quadratic twists of elliptic curve L-functions over function fields — 15 sections: Front matter; Introduction and statement of resu; Some useful lemmas"
---
| f |3/2+α|h|3/2+β
.
To proceed we need to study the function B(N, A, B, C1, V1; u, v, w, α, β).
Lemma 3.5. The function B(N, A, B, C1, V1; u, v, w, α, β) deﬁned above may be written as
D2(N, A, B, C1, V1; u, v, w, α, β)L

E1 ⊗χC1V1,
u
q1+α

L

E2 ⊗χC1V1,
v
q1+β

,
where D2(N, A, B, C1, V1; u, v, w, α, β) is some Euler product which is uniformly convergent provided
that |u|, |v| ≤q1/2−2/g, |w| ≤q−1/2−ε, and satisﬁes
D2(N, A, B, C1, V1; u, v, w, α, β) ≪g10τ10(AB)
√
AB
uniformly in this region.
Proof. It is easy to see that B(N, A, B, C1, V1; u, v, w, α, β) converges absolutely if |u|, |v| ≤q−ε and
|w| ≤q−1/2−ε. We claim that the sum over f, h and V2 is triply multiplicative. Indeed, one can easily see
Moments of quadratic twists of elliptic curve L-functions over function ﬁelds
1871
that the double sum over f, h is multiplicative, so
X
f,h∈M
χC1( f h)λ1(Af )λ2(Bh)udeg( f )vdeg(h)G(V1V 2
2 , N AB f h)
| f |3/2+α|h|3/2+β
=
Y
P
X
i, j
χC1(Pi+ j)λ1(Pi+aP)λ2(P j+bP)ui deg(P)v j deg(P)G(V1V 2
2 , Pi+ j+aP+bP+nP)
|P|(3/2+α)i+(3/2+β) j

,
where aP, bP and nP denote the orders of A, B and N with respect to P respectively. Let AP(V2) denote
the Euler product above. Note that when P ∤V2, we have AP(V2) = AP(1). Then we rewrite the double
sum over f, h as
Y
P
AP(1)
Y
P | V2
AP(V2)
AP(1) .
We introduce the sum over V2 and use the observation that for (V2, V3) = 1 and P ∤V3 we have
AP(V2V3) = AP(V2). Then
Y
P
AP(1)
X
V2∈M
w2 deg(V2) Y
P | V2
AP(V2)
AP(1)
=
Y
P
AP(1)
Y
P

1 +
1
AP(1)
X
k
AP(Pk)w2k deg(P)

=
Y
P
X
i, j,k
χC1(Pi+ j)λ1(Pi+aP)λ2(P j+bP)ui deg(P)v j deg(P)w2k deg(P)G(V1P2k, Pi+ j+aP+bP+nP)
|P|(3/2+α)i+(3/2+β) j

,
and hence the generating series for f, h, V2 is indeed triply multiplicative.
Now we rewrite B(N, A, B, C1, V1; u, v, w, α, β) as
Y
P ∤C1
X
i, j,k
χC1(Pi+ j)λ1(Pi+aP)λ2(P j+bP)ui deg(P)v j deg(P)w2k deg(P)G(V1P2k, Pi+ j+aP+bP+nP)
|P|(3/2+α)i+(3/2+β) j

×
Y
P | C1
X
k
λ1(PaP)λ2(PbP)w2k deg(P)G(V1P2k, PaP+bP+nP)

.
We next compute the Euler factors at an irreducible P in the region |u|, |v| ≤q1/2−2/g, |w| ≤q−1/2−ε.
Note that in this region, w2k deg(P) ≪ε |P|−1−ε if k ≥1.
Consider ﬁrst the case when P ∤N ABC1V1. The contribution of such an Euler factor is
X
i, j,k
χC1(Pi+ j)λ1(Pi)λ2(P j)ui deg(P)v j deg(P)w2k deg(P)G(V1P2k, Pi+ j)
|P|(3/2+α)i+(3/2+β) j
.
In view of Lemma 2.5, this is equal to
1 + χC1V1(P)λ1(P)udeg(P)
|P|1+α
+ χC1V1(P)λ2(P)vdeg(P)
|P|1+β
+ O

1
|P|1+ε

,
which justiﬁes the two L-functions.
1872
Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
In the case P | V1 but P ∤N ABC1, the Euler factor equals
X
i, j
χC1(Pi+ j)λ1(Pi)λ2(P j)ui deg(P)v j deg(P)G(V1, Pi+ j)
|P|(3/2+α)i+(3/2+beta) j
+ O

1
|P|1+ε

= 1 −λ1(P2)u2 deg(P)
|P|2+2α
−λ1(P)λ2(P)(uv)deg(P)
|P|2+α+β
−λ2(P2)v2 deg(P)
|P|2+2β
+ O

1
|P|1+ε

= 1 + O

1
|P|1+2/g

.
Similarly, the corresponding Euler factor is
=



O(|P|1/2)
if P | AB and P ∤NC1V1,
O(1)
if P | AB, P | V1 and P ∤NC1,
1 + O(1/|P|1+ε)
if P | C1 and P ∤N AB,
O(|P|1/2)
if P | C1, P | AB and P ∤NV1,
0
if P | C1, P | AB, P | V1 and P ∤N,
and is
≪ε
X
i+ j≤2k
|P|1−(1+ε)k−(i+ j)/2 ≪ε |P|,
if P | N.
The lemma easily follows by combining these estimates.
□
We now return to (3-13). In view of Lemma 3.5, we take r ≤q−1/2−ε and move the u and v contours
to |u| = |v| = rq1/2−2/g. This creates no poles. Then, by the above result,
B(N, A, B, C1, V1; u/w, v/w, w, α, β)
≪g10τ10(AB)
√
AB

L

E1 ⊗χC1V1, u/w
q1+α

L

E2 ⊗χC1V1, v/w
q1+β


≪g10τ10(AB)
√
AB


L

E1 ⊗χC1V1, u/w
q1+α


2
+

L

E2 ⊗χC1V1, v/w
q1+β


2
.
So
S(V̸ = 0)
≪q2g−(X+Y)/2g10
X
c2≤Z
c1+2c2≤2g+1
X
C1∈Mc1
C2∈Mc2
C1 | 1
τ(C)τ10(C)τ(C1)
√|C||C1||C2|2
×
I
|u|=q1/2−1/g
I
|v|=q1/2−1/g
I
|w|=r
X
V1∈H

L

E1 ⊗χC1V1,
u
q1+α


2
dudvdw
|w|X+Y+deg(N)−deg(V1)+c1+2c2−2g+1 .
If deg(V1) ≤X +Y +c1 +2c2 −2g, then we move the w contour to |w| = q−3/4, otherwise we move the
w contour to |w| = q−5/4. Using the upper bounds for moments as in Theorem 4.1 (see Remark 4.2) we
Moments of quadratic twists of elliptic curve L-functions over function ﬁelds
1873
ﬁnd that
S(V̸ = 0) ≪q(X+Y)/2g11
X
c2≤Z
c1+2c2≤2g+1
X
C1∈Mc1
C2∈Mc2
C1 | 1
τ(C)τ10(C)
√|C|
≪q(X+Y)/2g11
X
C2∈M≤Z
τ(C2)τ10(C2)
√|g(C2)|
≪q(X+Y+Z)/2g30,
which ﬁnishes the proof of Lemma 3.4.
□
Proposition 3.1 follows upon combining the estimates and choosing Z = g −(X + Y)/4.
