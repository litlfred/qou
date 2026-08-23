---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-026-57-the-x-deformation
section_title: "The x-deformation"
section_number: 5.7
pages: 52-62
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
the homogeneous equations
tq−1f (q−1t, x, q) + (1 − (x−1 + x)t)f (t, x, q) + tqf (qt, x, q) = 0 , (279a)
(1 − qx)(1 − q−1x2)f (t, qx, q)
−(x − 1)2(x + 1)(x2t − x − (q−1 + q)t − x−1 + x−2t)f (t, x, q)
+(1 − qx2)(1 − q−1x)f (t, q−1x, q) = 0 ,
(279b)
(1 − xq)(f (t, qx, q) − x−1f (qt, qx, q)) = (1 − x−1)(f (t, x, q) − qxf (qt, x, q)) . (279c)
This is not a random system of equations, instead they are the deﬁn ing equations of the t-
deformation of the homogeneous ˆA-polynomial of the 4 1 knot. This system appeared in [ 25,
Eqn.(10)] and [ 22, Eqn.(134)], and it is q-holonomic of rank 2 in the variables ( t, x). The
system is symmetric under the involution x ↔ x−1 (which corresponds to the Weyl symmetry
in the color of the Jones polynomial of the knot) and our solutions will also be invariant
under this involution. As a result the monodromy connecting x = 0 to x = ∞ is the identity.
To construct solutions, we will apply the Frobenius method to the Eq uation ( 279a). This
has Newton polygon depicted in Figure 4. Notice that the indicial polynomial ( ρ−1)2 for the
top edge of Equation ( 28) now becomes ( ρ − x)(ρ − x−1) for Equation ( 279a). We can then
normalise so that the solutions satisfy the full system of equations (279a), ( 279b), ( 279c).
The solutions to this homogeneous system are then given by
f (−1)(t, x, q) = θ(q−1x; q)
(1 − x)θ(q−1t; q)(q; q)∞
∞∑
k=0
k∑
ℓ=0
(−1)k qk(k+1)/2x2ℓ−k
(q; q)ℓ(q; q)k−ℓ
tk
f (1)(t, x, λ1, q) = θ(t; q)(q; q)∞
(1 − x)θ(x; q) L1/2B1/2 ˆf (1)(t, x, λ1, q)
g(0,x−1)(t, x, q) = θ(q−1x; q)θ(tx; q)(qx2; q)∞
θ(t; q)θ(x2; q)(1 − x)(q; q)∞
∞∑
k=0
(−1)k qk(k+1)/2xk
(q; q)k(qx2; q)k
t−k−1
g(0,x)(t, x, q) = θ(q−1x−1; q)θ(tx−1; q)(qx−2; q)∞
θ(t; q)θ(x−2; q)(1 − x−1)(q; q)∞
∞∑
k=0
(−1)k qk(k+1)/2x−k
(q; q)k(qx−2; q)k
t−k−1
(280)
MODULAR q-HOLONOMIC MODULES 53
where
ˆf (1)(t, x, q) =
∞∑
k=0
k∑
ℓ=0
qℓ2−kℓx2ℓ−k
(q; q)ℓ(q; q)k−ℓ
tk. (281)
Notice that we have
B1/2 ˆf (1)(t, x, q) =
∞∑
k=0
k∑
ℓ=0
(−1)k qk(k+1)/4+ℓ2−kℓx2ℓ−k
(q; q)ℓ(q; q)k−ℓ
tk (282)
which satisﬁes
(1 − q1/2ξ2)B1/2 ˆf (1)(ξ, q) + (x + x−1)ξB1/2 ˆf (1)(q1/2ξ, q) − B1/2 ˆf (1)(qξ, q ) = 0 . (283)
We can complete this to include the inhomogeneous solutions to the sy stem of Equations (39a),
(39b), ( 39c). Equations ( 39a) can be made third order homogenous which has Newton
polygon depicted in Figure 5. The indicial polynomial of the top edge now factors as
(ρ − x)(ρ − x−1)(ρ − 1). This gives two additional solutions as in Section 5.6. Firstly
we have
ˆf (0)(t, x, q) =
∞∑
k=0
(−1)kq−k(k+1)/2(qx; q)k(qx−1; q)ktk , (284)
a divergent formal power series solution at t = 0. Then
B1f (0)(ξ, x, q) =
∞∑
k=0
(qx; q)k(qx−1; q)ktk , (285)
which can be analytically continued away from ξ ∈ q
/CI
≤0 using the relation
(1 − ξ)B1 ˆf (0)(ξ, q) + (x + x−1)qξB1 ˆf (0)(qξ, q ) − q2ξB1 ˆf (0)(q2ξ, q) = 1 . (286)
So we deﬁne
f (0)(t, x, λ2, q) = ( L1B1 ˆf (0))(t, x, λ2, q) = 1
θ(λ2; q)
∑
k∈/CI
(−1)kqk(k+1)λk
2B1 ˆf (0)(qkλ2t, x, q).
(287)
The second solution is then given by
g(0)(t, x, q) =
∞∑
k=0
(−1)k qk(k+1)/2
(x; q)k+1(x−1; q)k+1
t−k−1. (288)
We then take
U(t, x, λ1, λ2, q) = W (f (1)(t, x, λ1, q), f (−1)(t, x, q), f (0)(t, x, λ2, q)) ,
V (t, q) = W (g(0,x−1)(t, x, q), g(0,x)(t, x, q), g(0,1)(t, x, q)) .
(289)
Before we give the proof note the immediate symmetries
g(0,x−1)(t, x−1, q) = g(0,x)(t, x, q), f (−1)(t, x−1, q) = f (−1)(t, x, q),
g(0,x)(t, x−1, q) = g(0,x−1)(t, x, q), f (−1)(t, x−1, q) = f (−1)(t, x, q),
g(0,1)(t, x−1, q) = g(0,1)(t, x, q), f (0)(t, x−1, q) = f (0)(t, x, q) .
(290)
54 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
Proof of Theorem
1.9. First we prove the existence of the elliptic function m2,1 with the
properties listed in Theorem 1.9. Note that the only restriction to an existence of an elliptic
function with prescribed poles and residues is the vanishing of the su m of the residues on a
fundamental domain. Here, there are six residues, and their sum v anishing is equivalent to
1 = θ(q3/4λ −1
1 ; q)θ(q−1/4x; q)θ(q−3/4x; q)θ(q−3/4λ 1; q)
2θ(x; q)θ(x−1; q)θ(q−1λ 1; q)θ(q−3/2λ 1; q)
+ θ(−q3/4λ −1
1 ; q)θ(−q−1/4x; q)θ(−q−3/4x; q)θ(−q−3/4λ 1; q)
2θ(x; q)θ(x−1; q)θ(q−1λ 1; q)θ(q−3/2λ 1; q)
+ θ(q1/4λ −1
1 ; q)θ(q−1/4x; q)θ(q−3/4x; q)θ(q−1/4λ 1; q)
2θ(x; q)θ(x−1; q)θ(q−1/2λ 1; q)θ(q−1λ 1; q)
+ θ(−q1/4λ −1
1 ; q)θ(−q−1/4x; q)θ(−q−3/4x; q)θ(−q−1/4λ 1; q)
2θ(x; q)θ(x−1; q)θ(q−1/2λ 1; q)θ(q−1λ 1; q)
=
(
θ(q3/4λ −1
1 ; q)θ(q−3/4λ 1; q)
2θ(q−1λ 1; q)θ(q−3/2λ 1; q) + θ(q1/4λ −1
1 ; q)θ(q−1/4λ 1; q)
2θ(q−1/2λ 1; q)θ(q−1λ 1; q)
)
θ(q−1/4x; q)θ(q−3/4x; q)
θ(x; q)θ(x−1; q)
+
(
θ(−q3/4λ −1
1 ; q)θ(−q−3/4λ 1; q)
2θ(q−1λ 1; q)θ(q−3/2λ 1; q) + θ(−q1/4λ −1
1 ; q)θ(−q−1/4λ 1; q)
2θ(q−1/2λ 1; q)θ(q−1λ 1; q)
)
θ(−q−1/4x; q)θ(−q−3/4x; q)
θ(x; q)θ(x−1; q) .
(291)
To prove this identity, notice that the right hand side is elliptic in λ1 ↦→q1/2λ1 and x ↦→qx.
Moreover, λ1 has only one potential simple pole in its fundamental domain and there fore
this is constant in λ1. Then x has a potential double pole which cancels. Then specialising
the RHS to λ1 = q1/4 and x = −q1/4 gives
θ(q1/2; q)θ(q−1/2; q)
2θ(q−3/4; q)θ(q−5/4; q)
θ(−1; q)θ(−q−1/2; q)
θ(−q1/4; q)θ(−q−1/4; q). (292)
This can be proven to equal one by elementary means using the Jaco bi triple product identity.
Therefore, such an m2,1(t, x, λ1, q) exists. Explicitly, we have
m2, 1(t, x, λ1, q) = −1
2
θ′(tx; q)
θ(tx; q) + −1
2
θ′(tx−1; q)
θ(tx−1; q)
+ θ(q3/ 4λ−1
1 ; q)θ(q−1/ 4x; q)θ(q−3/ 4x; q)θ(q−3/ 4λ1; q)
2θ(x; q)θ(x−1; q)θ(q−1λ1; q)θ(q−3/ 2λ1; q)
θ′(tλ1q1/ 4)
θ(tλ1q1/ 4) + θ(−q3/ 4λ−1
1 ; q)θ(−q−1/ 4x; q)θ(−q−3/ 4x; q)θ(−q−3/ 4λ1; q)
2θ(x; q)θ(x−1; q)θ(q−1λ1; q)θ(q−3/ 2λ1; q)
θ′(−tλ1q1/ 4)
θ(−tλ1q1/ 4)
+ θ(q1/ 4λ−1
1 ; q)θ(q−1/ 4x; q)θ(q−3/ 4x; q)θ(q−1/ 4λ1; q)
2θ(x; q)θ(x−1; q)θ(q−1/ 2λ1; q)θ(q−1λ1; q)
θ′(tλ1q3/ 4)
θ(tλ1q3/ 4) + θ(−q1/ 4λ−1
1 ; q)θ(−q−1/ 4x; q)θ(−q−3/ 4x; q)θ(−q−1/ 4λ1; q)
2θ(x; q)θ(x−1; q)θ(q−1/ 2λ1; q)θ(q−1λ1; q)
θ′(−tλ1q3/ 4)
θ(−tλ1q3/ 4)
− −1
2
θ′(x; q)
θ(x; q) − −1
2
θ′(x−1; q)
θ(x−1; q) − θ(q3/ 4λ−1
1 ; q)θ(q−1/ 4x; q)θ(q−3/ 4x; q)θ(q−3/ 4λ1; q)
2θ(x; q)θ(x−1; q)θ(q−1λ1; q)θ(q−3/ 2λ1; q)
θ′(λ1q1/ 4)
θ(λ1q1/ 4)
− θ(−q3/ 4λ−1
1 ; q)θ(−q−1/ 4x; q)θ(−q−3/ 4x; q)θ(−q−3/ 4λ1; q)
2θ(x; q)θ(x−1; q)θ(q−1λ1; q)θ(q−3/ 2λ1; q)
θ′(−λ1q1/ 4)
θ(−λ1q1/ 4) − θ(q1/ 4λ−1
1 ; q)θ(q−1/ 4x; q)θ(q−3/ 4x; q)θ(q−1/ 4λ1; q)
2θ(x; q)θ(x−1; q)θ(q−1/ 2λ1; q)θ(q−1λ1; q)
θ′(λ1q3/ 4)
θ(λ1q3/ 4)
− θ(−q1/ 4λ−1
1 ; q)θ(−q−1/ 4x; q)θ(−q−3/ 4x; q)θ(−q−1/ 4λ1; q)
2θ(x; q)θ(x−1; q)θ(q−1/ 2λ1; q)θ(q−1λ1; q)
θ′(−λ1q3/ 4)
θ(−λ1q3/ 4) .
(293)
MODULAR q-HOLONOMIC MODULES 55
Next we calculate the second column of the monodromy matrix using t he same argument
as Equation ( 207) from [ 48].
ˆf (−1)(t, x ; q) =
∮
0
B−1(g)(ξ, x ; q)θ(t/ξ ; q) dξ
2πiξ =
∮
0
θ(t/ξ ; q)
(xξ; q)∞(x−1ξ; q)∞
dξ
2πiξ
= −
∞∑
k=0
(
Resξ=x±q−k
) θ(t/ξ ; q)
(xξ; q)∞(x−1ξ; q)∞
dξ
2πiξ
= −
∞∑
k=0
(Resε=0) θ(txqkeε; q)
(q−1e−ε; q−1)k(e−ε; q)∞(x−2q−1e−ε; q−1)k(x−2e−ε; q)∞
−dε
2πi
−
∞∑
k=0
(Resε=0) θ(tx−1qkeε; q)
(x2q−1e−ε; q−1)k(x2e−ε; q)∞(q−1e−ε; q−1)k(e−ε; q)∞
−dε
2πi
=
∞∑
k=0
θ(txqk; q)(qx2; q)∞
(q−1; q−1)k(x−2q−1; q−1)kθ(x2; q) +
∞∑
k=0
θ(tx−1qk; q)(qx−2; q)∞
(x2q−1; q−1)kθ(x−2; q)(q−1; q−1)k
= θ(tx; q)(qx2; q)∞
θ(x2; q)
∞∑
k=0
(−1)k qk(k+1)/2xkt−k
(q; q)k(x2q; q)k
+ θ(tx−1; q)(qx−2; q)∞
θ(x−2; q)
∞∑
k=0
(−1)k qk(k+1)/2x−kt−k
(q; q)k(qx−2; q)k
= − θ(q−1t; q)(1 − x)(q; q)∞
θ(q−1x; q) g(0,x−1)(t, x, q ) − θ(q−1t; q)(1 − x−1)(q; q)∞
θ(q−1x−1; q) g(0,x)(t, x, q ) .
(294)
Therefore, we see that
f (−1)(t, x, q) = −g(0,x−1)(t, x, q) − g(0,x)(t, x, q). (295)
Now note that the bottom row of
− →
M is given by (0 , 0, 1) simply from the fact the inho-
mogeneous module contains the homogeneous as a sub-module and t hen the inhomogeneity
normalises the last entry. Therefore, from Lemma 5.12, we see that


1 −1 0
−1 −1 0
0 0 1


−1
− →
M(t, x, λ, q) =


θ(x−2;q)θ(t;q)2(q;q)3
∞
2θ(q−1x;q)2θ(tx;q)θ(tx−1;q) 0 ∗
∗ 1 ∗
0 0 1

 . (296)
Consider the function
E4 := f (1)(t, x, λ1, q) − θ(x−2; q)θ(t; q)2(q; q)3
∞
2θ(q−1x; q)2θ(tx; q)θ(tx−1; q)
(
g(0,x−1)(t, x, q) − g(0,x)(t, x, q)
)
− m2,1(t, x, λ1, q)
(
−g(0,x−1)(t, x, q) − g(0,x)(t, x, q)
)
= f (1)(t, x, λ1, q) − θ(x−2; q)θ(t; q)2(q; q)3
∞
2θ(q−1x; q)2θ(tx; q)θ(tx−1; q)
(
g(0,x−1)(t, x, q) + g(0,x)(t, x, q)
)
− m2,1(t, x, λ1, q)f (−1)(t, x, q)
(297)
where is m2,1 has the properties stated in Theorem 1.9. Then by the deﬁnition of m2,1 along
with Lemma 5.9 and Lemma 5.10 we see that E4 is holomorphic and satisﬁes Equation ( 279a)
and therefore must be zero from Lemma 5.8. This proves the ﬁrst column. Now for the last
56 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
column consider the function
E5 := f (0)(t, λ2, x, q) − g(0,1)(t, x, q)
− θ(x−2; q)θ(t; q)2(q; q)3
∞
2θ(q−1x; q)2θ(tx; q)θ(tx−1; q)
(
g(0,x−1)(t, x, q) − g(0,x)(t, x, q)
)
−
( θ′(tλ2)
θ(tλ2) − θ′(tx)
2θ(tx) − θ′(tx−1)
2θ(tx−1) − θ′(λ2)
θ(λ2) − 1
2
)
×
(
−g(0,x−1)(t, x, q) − g(0,x)(t, x, q)
)
.
(298)
This is holomorphic from Lemma 5.9, Lemma 5.10 and Lemma 5.11. Moreover, E5 satisﬁes
Equation ( 279a) and therefore vanishes from Lemma 5.8.
The entries of the RHS of Equation ( 41) have the following transformation properties
under the S matrix
θ(x−2; ˜q)θ(t; ˜q)2(˜q; ˜q)3
∞
2θ(˜q−1x; ˜q)2θ(tx; ˜q)θ(tx−1; ˜q) = τ θ(x−2; q)θ(t; q)2(q; q)3
∞
2θ(q−1x; q)2θ(tx; q)θ(tx−1; q)(
θ′(~t~λ 2)
θ(~t~λ 2)
− θ′(~t~x)
2θ(~t~x) − θ′(~t~x−1)
2θ(~t~x−1) − θ′(~λ 2)
θ(~λ 2)
− 1
2
)
= τ
( θ′(tλ 2)
θ(tλ 2) − θ′(tx)
2θ(tx) − θ′(tx−1)
2θ(tx−1) − θ′(λ 2)
θ(λ 2) − 1
2
)
(299)
while m2,1 has three elements in it’s SL 2( /CI ) orbit m2,1, m2,1|1S, m2,1|1T . To see this notice
that m2,1|1T 2 simply permutes the terms in RHS of Equation ( 293). Then using Equa-
tions ( 49) ( 52) we can explicitly compute m2,1|1S and m2,1|1T S which can be used to show
that m2,1|1ST = m2,1|1S and m2,1|1T S = m2,1|1T . Altogether, this shows the monodromy
satisﬁes Equation ( 43).
Lemma 5.8. If h(t, x, q) is holomorphic for t ∈ /BV
× and satisﬁes Equation ( 279a) then it
vanishes.
Proof. If h(t, x, q) is holomorphic for t ∈
/BV
× then is has an Laurent series expansion
h(t, x, q) =
∑
k∈/CI
αk(x, q)tk. (300)
Therefore Equation ( 279a) determines the coeﬃcients αk(x, q) from two initial conditions
say α0 and α−1. However for any non-zero choice of ( α0, α−1) we ﬁnd that αk ∼ O(q−k2/2)
for k ∼ −∞ and therefore it is divergent unless α0 = α−1 = 0. Notice the diﬀerence here
with that of Corollary 5.5 comes from the fact that α−1 = 0 does not imply that αk = 0 for
k < 0. □
Lemma 5.9. We have
Rest=qmx
θ(t; q)2
θ(tx; q)θ(tx−1; q)g(0,x−1)(t, x, q) dt
2πit = −θ(x; q)2f (−1)(qmx, x, q)
θ(x2; q)(q; q)3
∞
Rest=qmx−1
θ(t; q)2
θ(tx; q)θ(tx−1; q) g(0,x)(t, x, q) dt
2πit = −θ(x−1; q)2f (−1)(qmx−1, x, q)
θ(x−2; q)(q; q)3
∞
(301)
while g(0,1)(t, x, q) is holomorphic for t ∈
/BV
× ∪ {∞}.
MODULAR q-HOLONOMIC MODULES 57
Proof. This follows from Equation ( 295) and the fact that
Rest=qmx±
θ(t; q)2
θ(tx; q)θ(tx−1; q)
dt
2πit = θ(x±; q)2
θ(x±2; q)(q; q)3
∞
. (302)
□
Lemma 5.10. (a) The function B1/2 ˆf (1)(ξ, x, q) has simple poles at ξ = ±q−1/4−
/CI
≥0/2 with
residue
Resξ=±q−1/ 4−n/ 2B1/2 ˆf (1)(ξ, x, q) dξ
2πiξ = −θ(±q−1/4x; q1/2)
2(q; q)2
∞
n∑
ℓ=0
(±1)n q
n(n+2)
4 x2ℓ−n
(q; q)ℓ(q; q)n−ℓ
. (303)
(b) The function f (1)(t, x, λ1, q) has simple poles at t = ±q−1/4+/CI
λ−1
1 with residue
Rest=±q−1/ 4−nλ−1
1
f (1)(t, x, λ1, q) dt
2πit
= θ(±q3/4λ−1
1 ; q)θ(±q−1/4x; q)θ(±q−3/4x; q)θ(±q−3/4λ1; q)
2θ(x; q)θ(x−1; q)θ(q−1λ1; q)θ(q−3/2λ1; q) f (−1)(±q−1/4−nλ−1
1 , x, q) .
(304)
Proof. Firstly note that the singularities are determined by the functional equation for
B1/2 ˆf (1)(ξ, x, q). For part (a), recall the auxiliary function Hr(ξ, q) deﬁned in Equation ( 223).
Note that from the power series at ξ = 0, we see that
B1/2 ˆf (1)(q−1/4ξ, x, q) =
∑
r∈/CI
(−1)rqr2/4xrξrHr(ξ, q). (305)
Let
R±(n, x, q) = Res ξ=±q−1/ 4−n/ 2B1/2 ˆf (1)(ξ, x, q) dξ
2πiξ . (306)
Then, from Equation ( 228),
R±(0, x, q) = Res ξ=±1
∑
r∈/CI
(−1)rqr2/4ξrxrHr(ξ, q) dξ
2πiξ = −θ(±q−1/4x; q1/2)
2(q; q)2
∞
. (307)
Now from the functional equation of B1/2 ˆf (1)(ξ, x, q), we can deduce that
Resξ=±q−1/ 4−n/ 2(1 − q1/2ξ2)B1/2 ˆf (1)(ξ, q) + (x + x−1)ξB1/2 ˆf (1)(q1/2ξ, q) − B1/2 ˆf (1)(qξ, q ) dξ
2πiξ
= (1 − q−n)R±(n, x, q) ± (x + x−1)q−1/4−(n−1)/2R±(n − 1, x, q) − R±(n − 2, x, q) = 0 .
(308)
Note that R±(n, x, q) = 0 for n < 0 and that when R±(−1, x, q) is zero we have a unique
solution determined by R±(0, x, q). One can then check that
R±(n, x, q) = −θ(±q−1/4x; q1/2)
2(q; q)2
∞
n∑
ℓ=0
(±1)n q
n(n+2)
4 x2ℓ−n
(q; q)ℓ(q; q)n−ℓ
. (309)
58 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
For part (b), we compute
Rest=±q−1/ 4−nλ−1
1
f (1)(t, x, λ 1, q ) dt
2πit
= Res t=±q−1/ 4−nλ−1
1
θ(t; q)(q; q)∞
(1 − x)θ(x; q) L1/2B1/2 ˆf (1)(t, x, λ 1, q ) dt
2πit
= θ(±q−1/4−nλ −1
1 ; q)(q; q)∞
(1 − x)θ(x; q)θ(λ 1; q1/2)
∑
k∈/CI
(−1)kq(k−2n)(k−2n−1)/4λ −k+2n
1 R±(k, x, q )
= θ(±q−1/4−nλ −1
1 ; q)(q; q)∞
(1 − x)θ(x; q)θ(λ 1; q1/2)
−θ(±q−1/4x; q1/2)
2(q; q)2
∞q−n(2n+1)/2λ −2n
1
∞∑
k=0
k∑
ℓ=0
(−1)k q
k(k+1)
2 x2ℓ−k
(q; q)ℓ(q; q)k−ℓ
(±q−1/4−nλ −1
1 )k
= − θ(±q−1/4−nλ −1
1 ; q)θ(±q−1/4x; q1/2)
2(q; q)∞(1 − x)θ(x; q)θ(λ 1; q1/2) qn(2n+1)/2λ 2n
1
(1 − x)
θ(q−1x; q)
ˆf (−1)(±q−1/4−n/2λ −1
1 , x, q )
= θ(±q−1/4−nλ −1
1 ; q)θ(±q−1/4x; q)θ(±q−3/4x; q)θ(±q−5/4−nλ −1
1 ; q)
2xθ(x; q)2θ(λ 1; q)θ(q−1/2λ 1; q)q−n(2n+1)/2λ −2n
1
f (−1)(±q−1/4−nλ −1
1 , x, q )
= θ(±q−1/4λ −1
1 ; q)θ(±q−1/4x; q)θ(±q−3/4x; q)θ(±q−5/4λ −1
1 ; q)
2xθ(x; q)2θ(λ 1; q)θ(q−1/2λ 1; q) f (−1)(±q−1/4−nλ −1
1 , x, q )
= θ(±q3/4λ −1
1 ; q)θ(±q−1/4x; q)θ(±q−3/4x; q)θ(±q−3/4λ 1; q)
2θ(x; q)θ(x−1; q)θ(q−1λ 1; q)θ(q−3/2λ 1; q) f (−1)(±q−1/4−nλ −1
1 , x, q ) .
(310)
□
Lemma 5.11. (a) The function B1 ˆf (0)(ξ, x, q) has simple poles at ξ ∈ q
/CI
with residue
R(m, x, q) := Res ξ=q−mB1 ˆf (0)(ξ, x, q) dξ
2πiξ = −(qx; q)∞(qx−1; q)∞
m∑
ℓ=0
qmx2ℓ−m
(q; q)ℓ(q; q)m−ℓ
.
(311)
(b) The function f (0)(t, x, λ2, q) has simple poles at t ∈ λ−1
2 q
/CI
with residue
Rest=q−mλ−1
2
f (0)(t, x, λ2, q) dt
2πit = f (−1)(q−mλ−1
2 , x, q) . (312)
Proof. For part (a), notice that
B1 ˆf (0)(ξ, x, q ) =
∞∑
k=0
(qx; q)k(qx−1; q)kξk = (qx; q)∞(qx−1; q)∞
∞∑
k=0
1
(qk+1x; q)∞(qk+1x−1; q)∞
ξk
= (qx; q)∞(qx−1; q)∞
∞∑
k=0
∞∑
n,ℓ=0
qkn+kℓ+n+ℓxℓ−n
(q; q)n(q; q)ℓ
ξk
= (qx; q)∞(qx−1; q)∞
∞∑
n,ℓ=0
qn+ℓxℓ−n
(q; q)n(q; q)ℓ(1 − qn+ℓξ)
= (qx; q)∞(qx−1; q)∞
∞∑
n=0
n∑
ℓ=0
qnx2ℓ−n
(q; q)ℓ(q; q)n−ℓ(1 − qnξ) .
(313)
MODULAR q-HOLONOMIC MODULES 59
The residue then follows. For part (b), the pole structure is clear n oting that Equation ( 287)
is convergent if all the terms are and that B1 ˆf (0)(qktλ2, x, q) has poles at t ∈ λ−1
2 q
/CI
≤−k. We
compute the residues ρm := Res t=q−mλ−1
2
f (0)(t, x, λ2, q) dt
2πit as follows:
ρm = Res t=q−mλ−1
2
(L1B1 ˆf (0))(t, x, λ2, q) dt
2πit
= Res t=q−mλ−1
2
1
θ(λ2, q)
∑
k∈/CI
(−1)kqk(k+1)/2λk
2B1 ˆf (0)(qkλ2t, x, q) dt
2πit
= 1
θ(λ2, q)
∑
k∈/CI
(−1)kqk(k+1)/2λk
2R(m − k, x, q)
= 1
θ(λ2, q) (−1)mqm(m+1)/2λm
2
∞∑
k=0
(−1)kqk(k−1)/2(q−mλ−1
2 )kR(k, x, q)
= −(qx; q)∞(qx−1; q)∞
θ(λ2, q) (−1)mqm(m+1)/2λm
2
∞∑
k,ℓ=0
(−1)k qk(k+1)/2x2ℓ−k
(q; q)ℓ(q; q)k−ℓ
(q−mλ−1
2 )k
= f (−1)(q−mλ−1
2 , x, q) .
(314)
□
The functional equation ( 279a) for U, V deﬁned in ( 289) can be written in the form
U(qt, x, λ1, λ2, q) = A(t, x, q)U(t, x, λ1, λ2, q) and V (qt, x, q) = A(t, x, q)V (t, x, q) (315)
where
A(t, x, q) =


0 1 0
0 0 1
q−3 q−3t−1 − (1 + x + x−1)q−2 (1 + x + x−1)q−1 − q−3t−1

 . (316)
Therefore, we see that
det(U(qt, x, λ1, λ2, q)) = det( U(t, x, λ1, λ2, q))q−3, det(V (qt, x, q)) = det( V (t, x, q))q−3 .
Lemma 5.12. We have:
det(U(t, x, λ1, λ2, q)) = − q−3x
(1 − x)2 t−3
det(V (t, x, q)) = θ(q−1x; q)2θ(tx; q)θ(tx−1; q)
θ(x−2; q)θ(t; q)2(q; q)3
∞
q−3x
(1 − x)2 t−3 .
(317)
Proof. Firstly notice that
U (t, x, λ1, λ2, q)
= W (f (1)(t, x, λ1, q), f (−1)(t, x, q), f (0)(t, x, λ2, q))
=


0 1 0
0 0 1
q−2t−1 −q−2 q−2t−1 − (x + x−1)q−1




0 0 1
f (1)(t, x, λ1, q) f (−1)(t, x, q) f (0)(t, x, λ2, q)
f (1)(qt, x, λ1, q) f (−1)(qt, x, λ1, q) f (0)(qt, x, λ2, q)


(318)
60 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
with a similar expression for V . Therefore,
det(U(t, x, λ1, λ2, q)) = q−2t−1(f (1)(t, x, λ1, q)f (−1)(qt, x, q) − f (1)(qt, x, λ1, q)f (−1)(t, x, q))
det(V (t, x, q)) = q−2t−1(g(0,x−1)(t, x, q)g(0,x)(qt, x, q) − g(0,x−1)(qt, x, q)g(0,x)(t, x, q)) .
(319)
Now notice that both det( U(t, x, λ1, λ2, q))t3 and det( V (t, x, q))t3 are elliptic functions in t.
Furthermore, det( U(t, x, λ1, q)) has potentially simple poles in t at t ∈ ± q−1/4−
/CI /2λ−1 and
t ∈ q
/CI
. However, note that the poles of f (−1) at t ∈ q
/CI
cancel with zeros of f (1). Lemma 5.10
implies that
Rest=±q−1/ 4−nλ−1 det(U(t, x, λ1, λ2, q)q2t) =
θ(±q3/4λ−1
1 ; q)θ(±q−1/4x; q)θ(±q−3/4x; q)θ(±q−3/4λ1; q)
2(q; q)2
∞θ(x; q)θ(x−1; q)θ(q−1λ1; q)θ(q−3/2λ1; q)
× f (−1)(±q−1/4−nλ−1
1 , x, q)f (−1)(±q3/4−nλ−1
1 , x, q)
− θ(±q3/4λ−1
1 ; q)θ(±q−1/4x; q)θ(±q−3/4x; q)θ(±q−3/4λ1; q)
2(q; q)2
∞θ(x; q)θ(x−1; q)θ(q−1λ1; q)θ(q−3/2λ1; q)
× f (−1)(±q3/4−nλ−1
1 , x, q)f (−1)(±q−1/4−nλ−1
1 , x, q) = 0 .
(320)
A similar calculation shows that
Rest=±q−3/ 4−nλ−1
1
det(U(t, x, λ1, λ2, q)) = 0 . (321)
Therefore, we see that U(t, x, λ1, q)t2 is elliptic and holomorphic in t ∈
/BV
×. Therefore,
it is constant in t. Now considering the limit as t → 0, using the deﬁnition of f (±1) and
their asymptotic expansions (given by their formal power series ex pansions, by a version of
Watson’s lemma), it follows that
det(U(t, x, λ1, λ2, q))q2t3 = lim
t→0
det(U(t, x, λ1, λ2, q))q2t3
= lim
t→0
θ(t; q)θ(q−1x; q)
θ(t; q)θ(x; q)(1 − x)2 t2 − lim
t→0
θ(qt; q)θ(q−1x; q)
θ(q−1t; q)θ(x; q)(1 − x)2 t2
= − lim
t→0
q−1 θ(t; q)θ(x; q)
θ(t; q)θ(x; q)(1 − x)2 = − q−1x
(1 − x)2 .
(322)
Now noting that θ(t; q)2/θ(tx; q)θ(tx−1; q) is elliptic we see that
det(V (t, x, q))t3 θ(t; q)2
θ(tx; q)θ(tx−1; q) (323)
MODULAR q-HOLONOMIC MODULES 61
is elliptic and holomorphic in t and therefore constant in t. Then we see that
lim
t→∞
det(V (t, x, q))q2t3 θ(t; q)2
θ(tx; q)θ(tx−1; q)
= lim
t→∞
(g(0,x−1)(t, x, q)g(0,x)(qt, x, q) − g(0,x−1)(qt, x, q)g(0,x)(t, x, q))t2 θ(t; q)2
θ(tx; q)θ(tx−1; q)
= q−1 (qx2; q)∞(qx−2; q)∞(1 − x2)θ(q−1x; q)θ(q−1x−1; q)
(1 − x)2θ(x2; q)θ(x−2; q)(q; q)2
∞
= −q−1x2 θ(x2; q)θ(q−1x; q)θ(q−1x−1; q)
θ(x2; q)θ(x−2; q)(1 − x)2(q; q)3
∞
.
(324)
□
To ﬁnish the proof of Theorem
1.9 we will use the state integrals introduced in [ 24,
Equ.(139)] for w in a neighbourhood of zero.
∫
/CA +iε
Φ b(x + ib−1u)Φ b(x − ib−1u) exp
(
−πix2 − 2π zx
b
)
1 + ˜q1/2 exp
(
− 2πx
b
) dx . (325)
The factorisation of this integral was done in [ 24, Equ.(149)]. This module is again not self
dual (see Proposition 2.6) and means that additional functions arise in the factorisation. It
was shown, using Equation ( 49), that Equation ( 325) factors as combinations of elementary
functions holomorphic in /BV
′ times
I(z, w, τ ) = g(0,1)(˜t,~x, ˜q) + τ g(0,x)(˜t,~x, ˜q)L(x−1)(t, x, q) − τ g(0,x−1)(˜t,~x, ˜q)L(x)(t, x, q) (326)
where
L(x∓)(t, x, q) = θ(t; q)(1 − x∓)(q; q)2
∞
θ(q−1x±; q)θ(tx∓; q) (qx±2; q)∞
∞∑
k=0
(−1)k qk(k+1)/2x±k
(q; q)k(qx±2; q)k(1 − qkx±) t−k.
(327)
These functions L(x∓) can then be shown to satisfy
L(x∓)(t, x, q) − L(x∓)(qt, x, q) = θ(x−2; q)θ(t; q)2(q; q)3
∞
θ(q−1x; q)2θ(tx; q)θ(tx−1; q)
(1 − x)2
x qtg (0,x±)(qt, x, q).
(328)
Again this determines L(x∓) up to the addition of an elliptic function so checking the principal
parts
V (t, x, q)−1
( 0 1 0
0 0 1
q−2t−1 −q−2 q−2t−1 − (x + x−1)q−1
)
=


−L(x)(t, x, q ) ∗ ∗
L(x−1)(t, x, q ) ∗ ∗
1 0 0

 . (329)
where the ∗ are given by ± det(V (t, x, q))−1g(0,x±)(qmt, x, q) where m = 0, 1. Finally, one can
use the functional equations to take w away from 0 which gives the analytic continuation or
can alter the contour depending on w. Noting that the entries of Ω V,S are combinations of
elementary functions times I(z +n+mτ, w, τ ), we see that Ω V,S extends for τ ∈
/BV
′ and using
the modularity of the monodromy and part (c) of Theorem 1.2 completes the proof. □
62 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
