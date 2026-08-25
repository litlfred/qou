---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-022-53-residues
section_title: "Residues"
section_number: 5.3
pages: 42-44
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
× ∪{∞}. In this subsection we compute
the residues of the meromorphic functions f (−1) = g(0,1) and f (1).
Lemma 5.2. The functions f (−1)(t, q) = g(0,1)(t, q) have simple poles at t = q
/CI
with residues
Rest=qnf (−1)(t, q) dt
2πit = Res t=qng(0,1)(t, q) dt
2πit = g(0,0)(qn, q) . (219)
Proof. We have
Rest=qk
θ′(t−1; q)
θ(t−1; q)
dt
2πit = −1 . (220)
To ﬁnish we note that the proof of the equality f (−1) = g(0,1) is independent of this Lemma
and follows from Equation ( 207). □
MODULAR q-HOLONOMIC MODULES 43
Lemma 5.3. (a) The function B1/2 ˆf (1)(ξ, q) has simple poles at ξ = ±q−1/4− /CI /2 with residue
Resξ=±q−1/ 4−n/ 2B1/2 ˆf (1)(ξ, q) dξ
2πiξ = −θ(±q−1/4; q1/2)
2(q; q)2
∞
k∑
ℓ=0
(±1)k q
k(k+2)
4
(q; q)ℓ(q; q)k−ℓ
. (221)
(b) The function f (1)(t, λ, q) has simple poles at t = ±q−1/4+/CI
λ−1 with residue
Rest=±q−1/ 4−nλ−1f (1)(t, λ, q) dt
2πit
= θ(±q3/4λ−1; q)θ(±q−1/4; q)θ(±q−3/4; q)θ(±q−3/4λ; q)
2(q; q)6
∞θ(q−1λ; q)θ(q−3/2λ; q) f (−1)(±q−1/4−nλ−1, q) .
(222)
Proof. For part (a), consider the following auxiliary function,
Hr(ξ, q) =
∑
k
ξ2k
(q; q)k(q; q)k+r
, (223)
which we analytically continue to ξ /∈ ±q
1
2
/CI
≤0. From the power series at ξ = 0, we see that
B1/2 ˆf (1)(q−1/4ξ, q) =
∑
r∈/CI
(−1)rqr2/4ξrHr(ξ, q). (224)
We have the relation
Hr−1(ξ, q) − ξHr(ξ, q) = −q1−r (Hr−2(ξ, q) − Hr−1(ξ, q)) (225)
and from this we can see that
Resξ=1 (Hr−1(ξ, q) − Hr(ξ, q)) dξ
2πiξ = (−1)rq−r(r−1)/2Resξ=1 (H−1(ξ, q) − H0(ξ, q)) dξ
2πiξ .
(226)
Since
lim
r→∞
Hr(ξ, q) = 1
(q; q)∞(ξ2; q)∞
, (227)
it follows that
Resξ=1Hr(ξ, q) dξ
2πiξ = Res ξ=1H0(ξ, q) dξ
2πiξ = Res ξ=1H∞(ξ, q) dξ
2πiξ = −1
2(q; q)2
∞
. (228)
Let
R±(n, q) = Res ξ=±q−1/ 4−n/ 2B1/2 ˆf (1)(ξ, q) dξ
2πiξ . (229)
Then,
R(0, q) = Res ξ=±1
∑
r∈/CI
(−1)rqr2/4ξrHr(ξ, q) dξ
2πiξ = −θ(±q−1/4; q1/2)
2(q; q)2
∞
. (230)
Now from the functional equation of B1/2 ˆf (1)(ξ, q), we deduce that
0 = Res ξ=±q−1/ 4−n/ 2(1 − q1/2ξ2)B1/2 ˆf (1)(ξ, q) + 2ξB1/2 ˆf (1)(q1/2ξ, q) − B1/2 ˆf (1)(qξ, q ) dξ
2πiξ
= (1 − q−n)R±(n, q) ± 2q−1/4−(n−1)/2R±(n − 1, q) − R±(n − 2, q).
(231)
44 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
Note that R±(n, q) = 0 for n < 0 and that when R±(−1, q) is zero we have a unique solution
determined by R±(0, q). One can then check that
R±(n, q) = −θ(±q−1/4; q1/2)
2(q; q)2
∞
n∑
ℓ=0
(±1)n q
n(n+2)
4
(q; q)ℓ(q; q)n−ℓ
. (232)
For part (b), we compute
Rest=±q−1/ 4−nλ−1f (1)(t, λ, q ) dt
2πit
= Res t=±q−1/ 4−nλ−1
θ(t; q)
(q; q)2
∞
L1/2B1/2 ˆf (1)(t, q ) dt
2πit
= θ(±q−1/4−nλ −1; q)
(q; q)2
∞θ(λ; q1/2)
∑
k∈
/CI
(−1)kq(k−2n)(k−2n−1)/4λ −k+2nR±(k, q )
= θ(±q−1/4−nλ −1; q)
(q; q)2
∞θ(λ; q1/2)
−θ(±q−1/4; q1/2)
2(q; q)2
∞
qn(2n+1)/2λ 2n
∞∑
k=0
k∑
ℓ=0
(−1)k q
k(k+1)
2
(q; q)ℓ(q; q)k−ℓ
(±q−1/4−nλ −1)k
= − θ(±q−1/4−nλ −1; q)θ(±q−1/4; q1/2)
2(q; q)4
∞θ(λ; q1/2) qn(2n+1)/2λ 2n ˆf (−1)(±q−1/4−n/2λ −1, q )
= − θ(±q−1/4−nλ −1; q)θ(±q−1/4; q)θ(±q−3/4; q)θ(±q−5/4−nλ −1; q)
2(q; q)6
∞θ(λ; q)θ(q−1/2λ; q)q−n(2n+1)/2λ −2n f (−1)(±q−1/4−nλ −1, q )
= − θ(±q−1/4λ −1; q)θ(±q−1/4; q)θ(±q−3/4; q)θ(±q−5/4λ −1; q)
2(q; q)6
∞θ(λ; q)θ(q−1/2λ; q) f (−1)(±q−1/4−nλ −1, q )
= θ(±q3/4λ −1; q)θ(±q−1/4; q)θ(±q−3/4; q)θ(±q−3/4λ; q)
2(q; q)6
∞θ(q−1λ; q)θ(q−3/2λ; q) f (−1)(±q−1/4−nλ −1, q ) .
(233)
□
