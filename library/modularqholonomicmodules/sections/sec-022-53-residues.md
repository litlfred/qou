---
doc_id: modularqholonomicmodules
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-022-53-residues
section_title: "Residues"
section_number: 5.3
pages: 43-45
source_pdf: modular.qholonomic.modules.pdf
source_sha256: 640303a68dd75453
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
---
the residues of the meromorphic functions f (−1) =g(0,1) and f (1).
Lemma 5.2. The functionsf (−1)(t,q ) =g(0,1)(t,q ) have simple poles att =qZ with residues
Rest=qnf (−1)(t,q ) dt
2πit = Rest=qng(0,1)(t,q ) dt
2πit =g(0,0)(qn,q ). (222)
Proof. We have
Rest=qk
θ′(t−1;q)
θ(t−1;q)
dt
2πit =−1. (223)
To ﬁnish we note that the proof of the equality f (−1) =g(0,1) is independent of this Lemma
and follows from Equation (210). □
Lemma 5.3. (a) The functionB1/2 ˆf (1)(ξ,q ) has simple poles atξ =±q−1/4−Z /2 with residue
Resξ=±q−1/4−n/2B1/2 ˆf (1)(ξ,q ) dξ
2πiξ =−θ(±q−1/4;q1/2)
2(q;q)2
∞
k∑
𝓁=0
(±1)k q
k(k+2)
4
(q;q)𝓁(q;q)k−𝓁
. (224)
(b) The function f (1)(t,λ,q ) has simple poles at t =±q−1/4+Z λ−1 with residue
Rest=±q−1/4−nλ−1f (1)(t,λ,q ) dt
2πit
= θ(±q3/4λ−1;q)θ(±q−1/4;q)θ(±q−3/4;q)θ(±q−3/4λ;q)
2(q;q)6
∞θ(q−1λ;q)θ(q−3/2λ;q) f (−1)(±q−1/4−nλ−1,q ).
(225)
Proof. For part (a), consider the following auxiliary function,
Hr(ξ,q ) =
∑
k
ξ2k
(q;q)k(q;q)k+r
, (226)
which we analytically continue to ξ /∈±q
1
2 Z ≤0. From the power series at ξ = 0, we see that
B1/2 ˆf (1)(q−1/4ξ,q ) =
∑
r∈Z
(−1)rqr2/4ξrHr(ξ,q ). (227)
We have the relation
Hr−1(ξ,q )−ξHr(ξ,q ) =−q1−r (Hr−2(ξ,q )−Hr−1(ξ,q )) (228)
and from this we can see that
Resξ=1 (Hr−1(ξ,q )−Hr(ξ,q )) dξ
2πiξ = (−1)rq−r(r−1)/2Resξ=1 (H−1(ξ,q )−H0(ξ,q )) dξ
2πiξ.
(229)
Since
lim
r→∞
Hr(ξ,q ) = 1
(q;q)∞(ξ2;q)∞
, (230)
44 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
it follows that
Resξ=1Hr(ξ,q ) dξ
2πiξ = Resξ=1H0(ξ,q ) dξ
2πiξ = Resξ=1H∞(ξ,q ) dξ
2πiξ = −1
2(q;q)2
∞
. (231)
Let
R±(n,q ) = Resξ=±q−1/4−n/2B1/2 ˆf (1)(ξ,q ) dξ
2πiξ . (232)
Then,
R(0,q ) = Resξ=±1
∑
r∈Z
(−1)rqr2/4ξrHr(ξ,q ) dξ
2πiξ =−θ(±q−1/4;q1/2)
2(q;q)2
∞
. (233)
Now from the functional equation of B1/2 ˆf (1)(ξ,q ), we deduce that
0 = Resξ=±q−1/4−n/2(1−q1/2ξ2)B1/2 ˆf (1)(ξ,q ) + 2ξB1/2 ˆf (1)(q1/2ξ,q )−B 1/2 ˆf (1)(qξ,q ) dξ
2πiξ
= (1−q−n)R±(n,q )± 2q−1/4−(n−1)/2R±(n− 1,q )−R±(n− 2,q ).
(234)
Note thatR±(n,q ) = 0 forn< 0 and that when R±(−1,q ) is zero we have a unique solution
determined by R±(0,q ). One can then check that
R±(n,q ) =−θ(±q−1/4;q1/2)
2(q;q)2
∞
n∑
𝓁=0
(±1)n q
n(n+2)
4
(q;q)𝓁(q;q)n−𝓁
. (235)
For part (b), we compute
Rest=±q−1/4−nλ−1f (1)(t,λ,q ) dt
2πit
= Rest=±q−1/4−nλ−1
θ(t;q)
(q;q)2∞
L1/2B1/2 ˆf (1)(t,q ) dt
2πit
= θ(±q−1/4−nλ−1;q)
(q;q)2∞θ(λ;q1/2)
∑
k∈Z
(−1)kq(k−2n)(k−2n−1)/4λ−k+2nR±(k,q )
= θ(±q−1/4−nλ−1;q)
(q;q)2∞θ(λ;q1/2)
−θ(±q−1/4;q1/2)
2(q;q)2∞
qn(2n+1)/2λ2n
∞∑
k=0
k∑
𝓁=0
(−1)k q
k(k+1)
2
(q;q)𝓁(q;q)k−𝓁
(±q−1/4−nλ−1)k
=−θ(±q−1/4−nλ−1;q)θ(±q−1/4;q1/2)
2(q;q)4∞θ(λ;q1/2) qn(2n+1)/2λ2n ˆf (−1)(±q−1/4−n/2λ−1,q )
=−θ(±q−1/4−nλ−1;q)θ(±q−1/4;q)θ(±q−3/4;q)θ(±q−5/4−nλ−1;q)
2(q;q)6∞θ(λ;q)θ(q−1/2λ;q)q−n(2n+1)/2λ−2n f (−1)(±q−1/4−nλ−1,q )
=−θ(±q−1/4λ−1;q)θ(±q−1/4;q)θ(±q−3/4;q)θ(±q−5/4λ−1;q)
2(q;q)6∞θ(λ;q)θ(q−1/2λ;q) f (−1)(±q−1/4−nλ−1,q )
= θ(±q3/4λ−1;q)θ(±q−1/4;q)θ(±q−3/4;q)θ(±q−3/4λ;q)
2(q;q)6∞θ(q−1λ;q)θ(q−3/2λ;q) f (−1)(±q−1/4−nλ−1,q ).
(236)
□
MODULAR q-HOLONOMIC MODULES 45
