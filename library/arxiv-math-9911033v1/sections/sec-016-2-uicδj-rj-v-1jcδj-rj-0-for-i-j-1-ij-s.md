---
doc_id: arxiv-math-9911033v1
doc_title: "ON THE LOWER BOUND ESTIMA TES OF SECTIONS OF THE CANONICAL BUNDLES OVER A RIEMANN SURF ACE ZHIQIN LU Contents 1. Introductions 1 2. A lower bound estimate 4 3. A counterexample 11 "
section_id: sec-016-2-uicδj-rj-v-1jcδj-rj-0-for-i-j-1-ij-s
section_title: "(Ui|Cδj (Rj ),v 1j)Cδj (Rj ) = 0 for i ⁄=j, 1 ≤i,j ≤s;"
section_number: 2
pages: 29-34
source_pdf: 9911033v1.pdf
source_sha256: 196c05d2e3419565
doc_brief: "ON THE LOWER BOUND ESTIMATES OF SECTIONS OF THE CANONICAL BUNDLES OVER A RIEMANN SURFACE ZHIQIN LU Contents 1. Introductions 1 2. A lower bound estimate 4 3. A counterexample 11 4. Partial uniform est"
---
3.
∫
M \Cδi (Ri) ||Ui||2 ≤∼δ2m0−1
i .
Proof. Let
βij = (U ′
i,v 1j)Cδj (Rj ), 1 ≤i,j ≤s.
Then if i ⁄=j we have
|βij| ≤∼ δ
m0− 1
2
i(5.26)
by (5.25) and the deﬁnition of v1j, (j = 1, · · ·,s ) in (5.23). We also have
1 ≥∼βii ≥∼ 1(5.27)
by (5.24).
LetB = (βij)s×s be the matrix of (βij) for 1 ≤i,j ≤s. Then by (5.26), (5.27),
B is an invertible matrix, when max δi is small enough. Let A = B−1 be
the inverse matrix and let A = (α ij)s×s. Deﬁne
Ui =
s∑
j=1
α ijU ′
j, 1 ≤i ≤s.
ThenUi(i = 1, · · ·,s ) satisﬁes all the requirements in the lemma by the fact
that
|α ij| ≤∼ δ
m0− 1
2
i i ⁄=j,
1 ≥∼α ij ≥∼ 1 i =j.
LetU ′
s+1, · · ·,U ′
d be an orthonormal basis of the space span{U1, · · ·.U s}⊥.
Assume that
(U ′
i,U j) = 0
for s<i ≤d, 1 ≤j ≤s. Let
Ui =U ′
i −
s∑
j=1
γijUj, s<i ≤d,(5.28)
29
where
γik = 1
(Uk,v 1k)Cδk (Rk)
(U ′
i,v 1k)Cδk (Rk), 1 ≤k ≤s,s<i ≤d.(5.29)
Then we have
(Ui|Cδj (Rj ),v 1j )Cδj (Rj ) = 0
for s<i ≤d and 1 ≤j ≤s.
We have the following lemma:
Lemma 5.4. If x /∈ ∪ s
j=1Cδj (Rj − 2), then
d∑
i=1
||Ui||2 ≥∼ 1.
Proof. Let
lij = (Ui,U j)
for 1 ≤i,j ≤d. If 1 ≤i,j ≤s, we have
(Ui,U j) ≤∼ maxδi i ⁄=j,
1 ≥∼ (Ui,U j) ≥∼ 1 i =j(5.30)
by (5.26), (5.27) and lemma 5.3.
If 1 ≤i ≤s,s<j ≤d, we have
(Ui,U j) = −
s∑
k=1
γjk (Ui,U k)
using (5.28). By the deﬁnition of γjk in (5.29), we have
|γjk | ≤∼ maxδj.(5.31)
Thus
|(Ui,U j)| ≤∼ maxδj(5.32)
for 1 ≤i ≤s and s<j ≤d. Finally, if s<i,j ≤d, then
|(Ui,U j)| ≤∼ maxδi i ⁄=j,
1 ≥∼ (Ui,U j) ≥∼ 1 i =j(5.33)
by (5.28) and (5.31). Using (5.30), (5.32) and (5.33), we hav e
|lij| ≤∼ maxδi i ⁄=j,
1 ≥∼ |lij| ≥∼ 1 i =j.
Let (mij)d×d be the matrix such that
d∑
i=1
d∑
t=1
mji
mtklit =δjk
30
for 1 ≤j,k ≤d. We can choose mij such that
|mij| ≤∼ maxδi i ⁄=j,
1 ≥∼mij ≥∼ 1 i =j.(5.34)
It is easy to check that ∑ d
j=1mijUj for 1 ≤i ≤d forms an orthonormal
basis of H 0(M,K m0
M ). Thus we have
d∑
i=1
||
d∑
j=1
mijUj||2 ≥∼ 1
by Theorem 1.3. The lemma thus follows from (5.34) and the fac t that
maxδi is small.
We summarize the results up to now in the following
Proposition 5.1. LetU1, · · ·,U d be sections ofH 0(M,K m0
M ) as above. Then
||Ui|| + ||∇Ui|| ≤∼ 1 x /∈ ∪ s
j=1Cδj (Rj − 2),(5.35)
||Ui|| + ||∇Ui|| ≤∼ e−(m0+1)(Rj −|ρj|) x ∈Cδj (Rj − 2), 1 ≤j ≤s,(5.36)
for i>s and
||Ui|| + ||∇Ui|| ≤∼ δim0− 1
2 x /∈ ∪ s
j=1Cδj (Rj − 2),(5.37)
||Ui|| + ||∇Ui|| ≤∼ 1
√
δiem0|ρi| x ∈Cδi(Ri − 2),(5.38)
||Ui|| + ||∇Ui|| ≤∼ δ
m0− 1
2
i e−(m0+1)(Rj −|ρj|) x ∈Cδj (Rj − 2),j ⁄=i.(5.39)
for 1 ≤i ≤s. Furthermore,
d∑
k=1
||Ui||2 ≥∼ 1(5.40)
for x /∈ ∪ s
i=1Cδi(Ri − 2).
Proof. Ifx /∈ ∪ s
j=1Cδj (Rj), thenδx has a uniform lower bound. (5.35) fol-
lows from the Cauchy integral formula. (5.36) is a corollary of Lemma 5.1. (5.37)
follows from (5.5) and the Cauchy integral formula. (5.38) f ollows from a
straightforward computation. (5.39) follows from Lemma 5. 1 and (5.25).
Finally, (5.40) is just a restatement of the conclusion of Le mma 5.4.
Deﬁne an inner product <, > in the coordinate ring ⊕∞
m=0H 0(M,K m
M ).
Let S1 ∈ H 0(M,K m
M ) and S2 ∈ H 0(M,K m1
M ). Suppose that m ≥ m1.
We deﬁne a section of K m−m1
M as follows: Let x ∈ M and Ux is a local
trivialization of KM . let S1|Ux = S′ ·S′′ for S′ ∈ Γ(Ux,K m−m1
M ) and S′′ ∈
Γ(Ux,K m1
M ). Then
S3|Ux =S′ <S ′′,S 2 >H m1,
where <, , >H m1 is the pointwise inner product.
31
Proof of Theorem 5.1. We modify the method of Wolﬀ’s [14] of solving
the corona problem on the unit disk. First we construct a C ∞ solution. Let
S ∈H 0(M,K m
M ) for a ﬁxed m>m 0. Let



bk =ηk S
Uk
+ (1 − ∑ s
j=1ηj) <S,U k>
∑ d
j=1 ||Uj||2 1 ≤k ≤s,
bk = (1 − ∑ s
j=1ηj) <S,U k>
∑ d
j=1 ||Uj||2 k >s.(5.41)
Here bk(1 ≤ k ≤ s) is well deﬁned because of Lemma 5.2. We can check
that
S =
d∑
k=1
Ukbk.
If x /∈ ∪ s
j=1Cδj (Rj − 2), then by Lemma 5.4,
{
||bk|| ≤∼ (
√
δk(coshρk)m0 + 1)||S|| 1 ≤k ≤s,
||bk|| ≤∼ ||S|| k>s.(5.42)
By (5.41), we have
∂b k =∂η k
S
Uk
−∂
s∑
j=1
ηj
<S,U k >∑ d
j=1 ||Uj||2 + (1 −
s∑
j=1
ηj)<S, ∇Uk >
∑ d
j=1 ||Uj||2
−(1 −
s∑
j=1
ηj)
<S,U k > ∑ d
j=1<U j, ∇Uj >
(∑ d
j=1 ||Uj||2)2 1 ≤k ≤s,
∂b k = −∂
s∑
j=1
ηj
<S,U k >∑ d
j=1 ||Uj||2 + (1 −
s∑
j=1
ηj)<S, ∇Uk >
∑ d
j=1 ||Uj||2
− (1 −
s∑
j=1
ηj)
<S,U k > ∑ d
j=1<U j, ∇Uj >
(∑ d
j=1 ||Uj||2)2 k>s.
(5.43)
Thus
{ ||
∂b k|| ≤∼ 1
δ
m0 − 1
2
k
||S|| 1 ≤k ≤s,
||∂b k|| ≤∼ ||S|| k >s.
(5.44)
Let
cik = <
∂b k,U i >∑ d
j=1 ||Uj||2.(5.45)
for i ⁄=k and 1 ≤i,k ≤d. Then by (5.42) and (5.44), we have
{ ||cik|| ≤∼ 1
δ
m0 − 1
2
k
||S|| 1 ≤k ≤s,
||cik|| ≤∼ ||S|| k>s.
(5.46)
Let’s consider the equations
∂b ik =cik
32
for i ⁄= k and 1 ≤ i,k ≤ d. By Proposition 2.1, the solutions exist and we
may assume that
||bik||L2 ≤ ||cik||L2
for i ⁄=k, 1 ≤i,k ≤d. Thus by (5.46), we have
{ ||bik||L2 ≤∼ 1
δ
m0 − 1
2
k
||S||L2 1 ≤k ≤s,
||bik||L2 ≤∼ ||S||L2 s<k ≤d.
(5.47)
Let
Ti =bi +
d∑
k=1
(bik −bki)Uk.
One can check that ∂T i = 0 and
S =
d∑
i=1
TiUi.
In order to prove the theorem, we need to estimate ||TiUi|| for 1 ≤i ≤d.
By (5.47) and Proposition 5.1, we have
||TiUi||L2(M \∪s
j=1Cδ (Rj )) ≤∼ ||S||L2.(5.48)
By the Cauchy integral formula and Proposition 4.1
||TiUi||(x) ≤∼ ||S||L2(5.49)
for 1 ≤i ≤d and x /∈ ∪ s
j=1Cδj (Rj).
Let
Ei(ρ) = {x ∈Cδi(Ri)||ρi(x)| ≥ ρ}, 1 ≤i ≤s
for positive number ρ> 0. By (5.47) and Proposition 5.1 again, we have
{
||TiUi −ηiS||L2(Ej (ρ)−Ej (ρ+2)) ≤∼e−(Ri−ρ)||S||L2 1 ≤i ≤s,
||TiUi||L2(Ej (ρ)−Ej (ρ+2)) ≤∼e−(Ri−ρ)||S||L2 i>s.(5.50)
By the Cauchy formula,{
||TiUi −ηiS||(x) ≤∼ 1
δxe−(Ri−ρ)||S||L2 1 ≤i ≤s,
||TiUi||(x) ≤∼ 1
δx
e−(Ri−ρ)||S||L2 i>s.(5.51)
for any x ∈Ej(ρ + 1
2 ) −Ej(ρ + 1). Since
δx ≥ε5δj(coshρj)
by (4.7), we have
{
||TiUi −ηiS||(x) ≤∼ ||S||L2 1 ≤i ≤s,
||TiUi||(x) ≤∼ ||S||L2 i>s(5.52)
for any x ∈Ej(ρ + 1
2 ) −Ej(ρ + 1) and any |ρj|<R j − 3, j = 1, · · ·s. Thus
if ||S||L2 = 1, then by (5.49) and (5.52)
||TiUi||L2 ≤∼ 1
33
for 1 ≤i ≤d. If ||S||L∞ = 1, then
||TiUi||L∞ ≤∼ 1
for 1 ≤i ≤d. These results give the inequality (5.2).
