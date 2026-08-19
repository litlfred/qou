---
doc_id: arxiv-2104.06067v1
doc_title: "ON IRREDUCIBLE CHARACTERS OF THE IW AHORI-HECKE ALGEBRA IN TYPE A"
section_id: sec-003-5-the-bitrace-of-the-regular-representation
section_title: "The bitrace of the regular representation"
section_number: 5
pages: 17-20
source_pdf: 2104.06067v1.pdf
source_sha256: 750303181ca019ba
doc_brief: "ON IRREDUCIBLE CHARACTERS OF THE IWAHORI-HECKE ALGEBRA IN TYPE A — We use vertex operators to compute irreducible characters o f the Iwahori-Hecke algebra of type A."
---
The Hecke algebra Hn(q) is a ( Hn(q), Hn(q))-bimodule under the left and right regular actions, and
the two actions mutually commute with each other. As a result
(5.1) Hn(q) =
⨁
λ ⊢n
Vλ ⊗ V λ
where Vλ (resp. V λ ) is the irreducible left (resp. right) Hn(q)-module labeled by λ.
Following [6], we introduce the bitrace of the regular repre sentation of Hn(q) by deﬁning for any
compositions λ, µ |= n
btr(λ, µ) =
∑
ρ⊢n
χρ
λ (q)χρ
µ (q).(5.2)
This is a q-deformation of the second orthogonality relation between irreducible characters of the
symmetric group. It is known that btr(λ, µ)|q=1 = δλ,µ zλ .
Halverson, Luduc and Ram [6] proved the following result by u sing Roichman’s formula [19] for the
Hecke algebra. We will give an elementary proof using the tec hnique developed in this paper.
17
Theorem 5.1. Let λ = (λ1, λ2, . . . , λr) and µ = (µ1, µ2, . . . , µs) be two compositions of n. Then
btr(λ, µ) = ( q − 1)−r−s∑
M
wt(M ),(5.3)
where M = (mij) run through all r×s nonnegative integral matrices such that ∑
a mia = λi (1 ≤ i ≤ r)
and∑
b mbj = µj (1 ≤ j ≤ s) and
wt(M ) =
∏
mij ⁄=0
(q − 1)2[mij]q2.
By the Frobenius formula of the Hecke algebra Hn(q) it is readily seen that
btr(λ, µ) = ⟨˜qλ (q), ˜qµ (q)⟩.
Let H λ
µ (t) = ⟨qλ (t), qµ (t)⟩, then brt(λ, µ)(q) = q2n
(q−1)l(λ )+l(µ ) H λ
µ (q−1).
Using vertex operators and (2.8)-(2.9), we have the followi ng relation:
Q∗(z)Q(w) z − t2w
z − tw = Q(w)Q∗(z) z − tw
z − w ,(5.4)
where the rational functions are power series in negative po wers of z. Comparing coeﬃcients of z−nwm
we immediately obtain the following commutation relation.
Proposition 5.2. For any m, n ∈ Z+, as operators on Λ C[t,t −1]
q∗
nqm = qmq∗
n + (1 − t)
min(m,n )∑
k=1
qm−kq∗
n−k + (t − 1)
min(m,n )∑
k=1
q∗
n−kqm−ktk.(5.5)
For simplicity we denote for integer k > 0
(k)t = (t − 1) t2k − 1
t + 1 = (t − 1)2[k]t2
and make the convention that ( k)t = 0 for k < 0 and (0) t = 1. The following result is easily shown by
induction, and also can be used as an inductive deﬁnition of ( k)t.
Lemma 5.3. Let k be a positive integer, then we have
1 − t + (t − 1)
k∑
i=1
(k − i)tti = (k)t.(5.6)
Theorem 5.4. Let k ∈ Z+ and µ ⊨ n a composition, then
q∗
kqµ =
∑
τ|=k
∏
τa>0
(τa)tqµ −τ .(5.7)
18
Proof. Use induction on k + n. The initial step is clear. Assume the identity holds for q∗
k′qµ such that
k′ + |µ| < k + n, then
q∗
kqµ 1qµ 2 · · ·qµ l
=qµ 1q∗
kqµ 2 · · ·qµ l + (1 − t)
∑
i≥1
qµ 1−iq∗
k−iqµ 2 · · · qµ l + (t − 1)
∑
i≥1
q∗
k−iqµ 1−iqµ 2 · · ·qµ lti
=qµ 1
∑
τ|=k
∏
τa≥1
(τa)tqµ [1]−τ + (1 − t)
∑
i≥1
∑
τ|=k−i
∏
τa≥1
(τa)tqµ 1−iqµ [1]−τ
+ (t − 1)
∑
i≥1
∑
τ|=k−i
∏
τa≥1
(τi)tqµ 1−i−τ1qµ [1]−τ [1]ti.
The ﬁrst summand is ∑
τ|=k
∏
τa≥1
(τa)tqµ −τ with τ1 = 0. Replacing i + τ1 by j in the third summand and
pulling ( τ1)t = (j − i)t forward, we simplify the second and the third summands as fol lows:
(1 − t)
∑
i≥1
∑
τ|=k−i
∏
τa≥1
(τa)tqµ 1−iqµ [1]−τ + (t − 1)
∑
i≥1
∑
j≥i
(j − i)tti ∑
τ|=k−j
∏
τa≥1
(τa)tqµ 1−jqµ [1]−τ
=(1 − t)
∑
i≥1
∑
τ|=k−i
∏
τa≥1
(τa)tqµ 1−iqµ [1]−τ +
∑
j≥1
(t − 1)
j∑
i=1
(j − i)tti ∑
τ|=k−j
∏
τa≥1
(τa)tqµ 1−jqµ [1]−τ
=
∑
j≥1
(j)t
∑
τ|=k−j
∏
τa≥1
(τa)tqµ 1−jqµ [1]−τ (by Lemma 5.3) .
Combining this with the ﬁrst summand, we see the total sum is ∑
τ|=k
∏
τa≥1
(τa)tqµ −τ . □
The following is an immediate consequence of Theorem 5.4.
Corollary 5.5. Let λ, µ |= n with l(λ) = r and l(µ) = s. Then
H λ
µ (t) =
∑
M
r∏
i=1
∏
a≥1
(τ (i)
a )t.(5.8)
where the sum is over all r × s nonnegative integer matrices M = (τ (i)
a )1≤i≤r, 1≤a≤s such that the row
sums are λ1, . . . , λr and the column sums are µ1, . . . , µs
This provides a simple proof of Theorem 5.1 due the fact that t2k(k)t−1 = (k)t, and qi = 0 for i < 0.
Acknowledgments
The work is partially supported by Simons Foundation grant N o. 523868 and NSFC grant No.
11531004.
19
