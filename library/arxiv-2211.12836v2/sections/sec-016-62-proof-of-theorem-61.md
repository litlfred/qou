---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION"
section_id: sec-016-62-proof-of-theorem-61
section_title: "Proof of Theorem 6.1"
section_number: 6.2
pages: 50-56
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION — We study a class of commuting Markov kernels whose simplest element describes the movement ofk particles on a discrete"
---
folds U(k) and SU (k). In particular, we will need the following bound which is a straightforward
deduction of the parabolic Harnack estimates of Li and Yau [40, Thm 2.3].
Lemma 6.5. Let Kt be the heat kernel either on SU (k) or U(k). Then, for all x∈SU (k) (resp.
U(k)) and 0<t 1<t 2
Kt(x,x )≤
(t2
t1
)(k2−ϵ)/2
exp
( kπ2
4(t2−t1)
)
,
whereϵ = 1 (resp. ϵ = 0).
Proof. Let G be a compact Lie group and Kt the heat kernel on G corresponding to a translation
invariant distancedG onG. Since G has positive curvature, taking the limitα→ 1 in [40, Theorem
2.3] yields that for all y∈G,
Kt(x,x )≤ Kt(x,y )
(t2
t1
)dimG/2
exp
(dG(x,y )2
4(t2−t2)
)
.
Hence, averaging y on all G and using that
∫
G Kt(x,y )dg = 1, we deduce that
Kt(x,x )≤
(t2
t1
)dimG/2
exp
(diam(G)2
4(t2−t2)
)
.
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 51
Since the diameter ofU(k) andSU (k) with respect todU(k) are smaller than
√
kπ and dimU(k) =k2
and dimSU (k) =k2− 1, the result is deduced. □
Proof of Theorem 6.1. Set µ = Bα,γ
ξn(I) (t0) and ν = Rm⟨m⟩
kn
(ξn [∗m∗δI]), and recall that α =
1
2Var (m) and γ = k
2(k2−1)K(m). By Proposition 6.4, for any t> 0
W1,Tk(µ,ν )≤ 2
√
2tk +
vuuu√
∑
J∈Bk
J⁄=I0
exp(−2κ(J)t)
κ(J) |Φ[µ](J)− Φ[ν](J)|2.(53)
By (23),
(54) Φ[ µ](J) = exp
(
−t0
γ
kK( ˜J)−t0
α
k2⟨λJ⟩2
)
SJ(ξn(I)),
and by Proposition 4.9, when ‖ ˜J‖∞ < n
2 we have Φ[ν](J) = SJ(ξn(I0))Φn[∗m∗δI](J(n)), where
J(n) is the unique element of Bk,n such that{J(n)
i [n]}1≤i≤k ={Ji[n]}1≤i≤k. By (18) and (19) with
Lemma 4.4, we then have
Φ[ν](J) =e−2iπm⟨m⟩·⟨λJ⟩
kn SJ(ξn(I0))Φn[∗m∗δI](J(n))
=e−2iπm⟨m⟩·⟨λJ⟩
kn SJ(ξn(I0))Φn[∗m](J(n))SJ (n)(ξn(I0))
SJ (n)(ξn(I0))
=e−2iπm⟨m⟩·⟨λJ⟩
kn Φn[∗m](J(n))SJ(ξn(I)),(55)
where we used that SJ (n)(ξn(I)) = SJ(ξn(I)) on the last equality. Let us split the latter sum as
follows: introduce the thresholds θγ = min( c1
k3√γM, 1
4,θα) = c2√αM for some numeric constants c1,c 2
to choose later and setνγ = 2c
km1/3M 1/3√γ andνα = 2c k
m1/3M 1/3√α, wherec is the numerical constant
given in Proposition 5.3. Then, deﬁne
RA =


J∈Bk\{I0},
√
K( ˜J)
νγ
∨|⟨λJ⟩|
να
≤n


,
RB =


J∈Bk\{I0},
√
K( ˜J)
νγ
∨|⟨λJ⟩|
να
≥n,
√
K( ˜J)
θγ
∨|⟨λJ⟩|
θα
≤n


,
and
RC =


J∈Bk\{I0},
√
K( ˜J)
θγ
∨|⟨λJ⟩|
θα
≥n


.
We then have
∑
J∈Bk
J⁄=I0
exp(−2κ(J)t)
κ(J) |Φ[µ](J)− Φ[ν](J)|2≤
∑
i∈{A,B,C}
∑
J∈Ri
exp(−2κ(J)t)
κ(J) |Φ[µ](J)− Φ[ν](J)|2
:=SA +SB +SC.
52 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
Bound of SC: Let us split SC as
SC =
∑
J∈RC√
K( ˜J)>θγn
exp(−2κ(J)t)
κ(J) |Φ[µ](J)− Φ[ν](J)|2
+
∑
J∈RC√
K( ˜J)≤θγn
exp(−2κ(J)t)
κ(J) |Φ[µ](J)− Φ[ν](J)|2
=S1
C +S2
C.
By deﬁnition of the Fourier transform on M1(Tk) from (19) and the bound SJ(⃗ u)≤ SJ(0,..., 0)
for⃗ u∈Tk, for any J∈Bk we have
|Φ[µ](J)− Φ[ν](J)|2≤ 2SJ(0,..., 0)2.
Hence, by the fact that κ(J) =K( ˜J) +|λJ|2/k for J∈Bk and (24), we get the ﬁrst bound
S1
C≤4
∑
J∈Bk\{I0}√
K( ˜J)>θγn
exp(−2κ(J)t)
κ(J) SJ(0,..., 0)2
≤4 exp(−tθ2
γn2)
∑
J∈Bk\{I0}
K( ˜J)>θγn
exp(−κ(J)t)SJ(0,..., 0)2≤ 4 exp
(
−tθ2
γn2)
KU(k)
t (0, 0).
By Lemma 6.5 for t1 =t and t2 =t + 1, when t≤ 1 we have
KU(k)
t (0, 0)≤
(t + 1
t
)k2/2
exp
(kπ2
4
)
≤
(2
t
)k2/2
exp
(π2
4k
)k2
,
so that
(56) S1
C≤ 4 exp(−tθ2
γn2−k2/2(logt−c))
for some numeric constant c∈ R.
By Proposition 5.3, when K( ˜J)≤θ2
γn2 with c1 small enough, we have
⏐⏐⏐Φn[∗m](J(n))
⏐⏐⏐≤ exp
(
−m(2π)2
2n2
K( ˜J)K(m)
k2− 1 + mM
n3 O
([
kK( ˜J)K(m)
]3/2))
≤ exp
(
−1
2· m(2π)2
2n2
K( ˜J)K(m)
k2− 1
)
= exp
(
−1
2·t0
γ
kK( ˜J)
)
.
Hence, by (54) and (55),
S2
C≤ 4
∑
J∈Bk\{I0}√
K( ˜J)≤θγn,|⟨λJ⟩|>θαn
exp(−2κ(J)t)
κ(J) exp
(
−1
2·t0
γ
kK( ˜J)
)
SJ(0,..., 0)2.
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 53
Since, exp(−2κ(J)t)≤ exp(−2t⟨J⟩2/k), decomposing J ∈ BK as J = ˆJ +𝓁1k with 𝓁∈ Z and
summing on 𝓁∈ Z such that|⟨λJ +kl⟩|>θ αn yields
S2
C≤4
∑
𝓁∈Z,J∈Bk\{I0},Jk=0√
K( ˜J)≤θγn,|⟨λJ+kl⟩|>θαn
k exp(−2tθ2
αn2/k)
⟨J +𝓁k⟩2 exp
(
−t0
γ
kK( ˜J)
)
SJ(0,..., 0)2
≤c k
nθα
exp(−2tθ2
αn2/k)
∑
J∈Bk\{I0},Jk=0
exp
(
−t0
γ
kK( ˜J)
)
SJ(0,..., 0)2
for some numeric constant c> 0. By (25), we have KSU (k)
t0 (0, 0), so that when t≤t0,
(57) S2
C≤ck exp(−2tθ2
αn2/k)
nθα
KSU (k)
t (0, 0).
When θγ≥n−1, set
(58) t = 2 +k2(logn + logθγ +c0)
θ2γn2 + k logn
θ2αn2 ,
with c0 a numeric constant. Then, combining (56) and (57) yields for c0 large enough
(59) SC≤ c
n2 + ck
θ3αn3.
Bound of SB: The pattern to bound SB is similar to the one concerning SC. Split SB as
SB =
∑
J∈RB√
K( ˜J)>νγn
exp(−2κ(J)t)
κ(J) |Φ[µ](J)− Φ[ν](J)|2
+
∑
J∈RB√
K( ˜J)≤νγ
exp(−2κ(J)t)
κ(J) |Φ[µ](J)− Φ[ν](J)|2
=S1
B +S2
B.
The condition
√
K( ˜J)
θγ ∨|⟨λJ⟩|
θα ≤n for c small enough yields by Proposition 5.3
⏐⏐⏐Φn[∗m](J(n))
⏐⏐⏐≤ exp
(
− m(2π)2
2n2
(
K( ˜J)K(m)
k2− 1 + Var (m)⟨λJ⟩2
k2
)
+ mM
n3 O
([
kK( ˜J)K(m)
]3/2
+ Var (m)3/2·|⟨λJ⟩|3
k3
))
≤ exp
(
−m(2π)2
4n2
(
K( ˜J)K(m)
k2− 1 + Var (m)⟨λJ⟩2
k2
))
≤ exp
(
−t0
2
(
γK( ˜J)
k + α⟨λJ⟩2
k2
))
.
54 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
Remark that νγ = 2c
km1/3M 1/3√γ = c′
kn2/3t1/3
0 M 1/3√γ
for some numeric constant c′. Hence,
√
K( ˜J)≥
νγn implies that
√
K( ˜J)≥ c′n1/3
kt1/3
0 M 1/3√γ
.
Similarly,|⟨λJ⟩|≥ να implies that
|⟨λJ⟩|2≥ ckn1/3
(t0M)1/3√α.
Decomposing J∈BK as J = ˆJ +𝓁1k with 𝓁∈ Z and summing on 𝓁∈ Z yields then
S1
B≤4
∑
𝓁∈Z,J∈Bk\{I0},Jk=0√
K( ˜J)≥νγn
1
κ(J) exp
(
−t0
γK( ˜J)
k
)
|SJ(ξn(I))|2
≤
∑
𝓁∈Z,J∈Bk\{I0},Jk=0√
K( ˜J)≥νγn
exp
(
−ccn2/3t1/3
0
k3M 2/3
)
n2/3
k2(t0M)2/3γ +|⟨J +𝓁k⟩|2/k
exp
(
−t0/2γK( ˜J)
k
)
|SJ(ξn(I))|2
≤
k2(t0M)1/3√γ exp
(
−ccn2/3t1/3
0
k3M 2/3
)
n1/3 KSU (k)
t0/2 (ξn(I),ξn(I)).
for some numeric constant c> 0. Similarly,
S2
B≤4
∑
𝓁∈Z,J∈Bk\{I0},Jk=0
|⟨J+𝓁1k⟩|≥ναn
1
κ(J) exp
(
−t0
(
γK( ˜J)
k + α⟨λJ⟩|2
k2
))
|SJ(ξn(I))|2
≤
∑
𝓁∈Z,J∈Bk\{I0},Jk=0
|⟨J+𝓁1k⟩|≥ναn
exp
(
−ccn2/3t1/3
0
M 2/3
)
|⟨J +𝓁k⟩|2/k exp
(
−t0
γK( ˜J)
k
)
|SJ(ξn(I))|2
≤
k2(t0M)1/3√α exp
(
−ccn2/3t1/3
0
M 2/3
)
n1/3 KSU (k)
t0 (ξn(I),ξn(I)).
Hence, we ﬁnally have
SB =S1
B +S2
B≤
ck2(t0M)1/3(√γ +√α) exp
(
−ccn2/3t1/3
0
k3M 2/3
)
n1/3 KSU (k)
t0/2 (ξn(I),ξn(I))
for some numeric constant c> 0, where we used that the heat kernel KSU (k)
t (0, 0) is decreasing in
t.
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 55
Bound of SA : By Lemma 5.4,
√
K( ˜J)≤ νγn implies that‖ ˜J‖∞≤ cn
m1/3M 1/3K(m)1/3 . Hence,
when
√
K( ˜J)
νγ ∨|⟨λJ⟩|
να ≤n, Proposition 5.3 yields that
e−2iπm⟨m⟩·⟨λJ⟩
kn Φn[∗m](J(n)) = exp
[
− m(2π)2
2n2
[
K(m)K( ˜J)
k2− 1 + Var (m)⟨λJ⟩2
k2
]
+ mM
n3 O
(
Var (m)3/2·|⟨λJ⟩|3
k3 +
[
k·K(m)·K( ˜J)
]3/2
)]
.
By (54) and (55), we thus have
|Φ[µ](J)− Φ[ν](J)| = exp
(
−m(2π)2
2n2
[
K(m)K( ˜J)
k2− 1 + Var (m)⟨λJ⟩2
k2
])
|SJ(ξn(I))|
·
⏐⏐⏐⏐⏐exp
(
mM
n3 O
(
Var (m)3/2·|⟨λJ⟩|3
k3 +
[
k·K(m)·K( ˜J)
]3/2
))
− 1
⏐⏐⏐⏐⏐
≤t0M
n exp
(
−t0
(γ
kK( ˜J) + α
k2|⟨λJ⟩|2
))
|SJ(ξn(I))|
O
(
α3/2·|⟨λJ⟩|3
k3 +
[
k2·γ·K( ˜J)
]3/2
)
,
where we used on the last inequality that mM
n3 O
(
Var (m)3/2·|⟨λJ⟩|3
k3 +
[
k·K(m)·K( ˜J)
]3/2)
=O(1)
when
√
K( ˜J)
νγ ∨|⟨λJ⟩|
να ≤n and the bound|eu− 1| =O(u) when u =O(1). Hence,
SA≤ t2
0M 2
n2
∑
J∈RA
e−2t0
(
γ
kK( ˜J)+ α
k2|⟨λJ⟩|2
)
κ(J) |SJ(ξn(I))|2·O
(α3·|⟨λJ⟩|6
k3 +
[
k2·γ·K( ˜J)
]3)
.
Setting g(u) =u3e−u for u≥ 0, we have
exp
(
−t0
(γ
kK( ˜J) + α
k2|⟨λJ⟩|2
))
O
(α3·|⟨λJ⟩|6
k3 +
[
k2·γ·K( ˜J)
]3)
≤ ck9‖g‖∞
t3
0
,
so that
SA≤ ck9M 2
t0n2
∑
J∈RA
exp
(
−t0
γ
kK( ˜J)
)
κ(J) |SJ(ξn(I))|2.
Decomposing J∈BK as J = ˆJ +𝓁1k and using that ∑
𝓁∈Z
1
κ(J+𝓁1k) =∑
𝓁∈Z
1
‖J+𝓁1k− ˜I0‖2−‖˜I0‖2≤c
for some numeric constant c independent of J⁄=I0, we get
SA≤ ck9M 2
t0n2
∑
J∈Bk,Jk=0
exp
(
−t0
γ
kK( ˜J)
)
|SJ(ξn(I))|2≤ ck9M 2
t0n2 KSU (k)
t0 (ξn(I),ξn(I)).
56 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
Putting all previous bounds together yields with (53)
WTk
1 (µ,ν )≤ck
√
t + c
n + c
√
k
(θαn)3/2
+


ck2(t0M)1/3(√γ +√α) exp
(
−ccn2/3t1/3
0
k3M 2/3
)
n1/3 + ck9M 2
t0n2


1/2
KSU (k)
t0/2 (ξn(I),ξn(I))1/2.(60)
Using the deﬁnition of θα and the choice of t from (58) yields for n large enough, after simplifying,
WTk
1 (µ,ν )≤ M
n
(
c1(k8γ +kα) logn + c2k9/2
√t0
KSU (k)
t0/2 (ξn(I),ξn(I))1/2
)
,
for some numeric constants c1,c 2> 0. □
