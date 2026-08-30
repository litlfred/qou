---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-016-51-some-estimates
section_title: "Some estimates"
section_number: 5.1
pages: 12-14
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
Lemma 5.1. Suppose |α| < 1.
(a) For 1 ≤ k ≤ n, 0 ≤ l, and y on the interval from 0 to α/n we have
⏐
⏐
⏐
⏐
∂l
∂y l ck(α, y)
⏐
⏐
⏐
⏐ < (A3)k|α|k−l k2l.
(b) For any y ∈ C, |y| < 1/n and 1 ≤ k ≤ n we have
⏐
⏐
⏐
⏐
∂l
∂y l HK,k (ey)
⏐
⏐
⏐
⏐ < (A2)k (A0)l k2l.
Proof. (a) We have ck(α, y) =∏ k
j=1 gj, where
gj = eα + e−α − ejy − e−jy .
By the Leibniz rule, the l-th derivative (with respect to y) of ck is the sum
(17) ∂l
∂y l ck(α, y) =
∑
|l|=l
( l
l1, . . . , lk
)
t(l), where t(l) =
k∏
j=1
g(lj)
j .
Here l = ( l1, . . . , lk), |l| := ∑ k
j=1 lj, lj ≥ 0. We will estimate each term t(l). Fix l = ( l1, . . . , lk). We
consider two cases, lj = 0 and lj > 0.
Suppose lj = 0. Then g(lj )
j = gj = eα + e−α − ejy − e−jy . Since j ≤ k ≤ n, the interval connecting α and
jy lies totally in the disk of radius |α| (remember that |y| ≤ | α|/n). As in the proof of Lemma
4.3, we have
(18) |gj| = |(eα + e−α ) − (ejy + e−jy )| ≤ (2e)|α|.
Now suppose lj > 0. Then
g(lj)
j = −ejy jlj − e−jy (−j)lj .
It is clear |e±α | < e. Since |j| ≤ | k| and |jy| < |α|, we have |e±jy (±j)lj | < ek lj . Hence
(19)
⏐
⏐
⏐g(lj )
j
⏐
⏐
⏐ < (2e) klj .
Taking the product over j, using (
18), ( 19) and ∑ lj = l, we get
|t(l)| < (2e)k kl |α|#{lj =0}
< (2e)k kl |α|k−l because |α| < 1 and # {lj = 0} ≥ k − l
Since∑
|l|=l
( l
l1,...,l k
)
= kl, from ( 17) and the above estimate for t(l), we get the result with A3 = 2e.
(b) By Theorem 4.2(a),
∂l
∂y l HK,k (ey) =
A0k2
∑
j=−A0k2
bj,k ejy jl.
From the bounds for j and k ≤ n one has |ejy | ≤ exp(A0k) and |jl| ≤ (A0k2)l. From the above equation
one has
⏐
⏐
⏐
⏐
∂l
∂y l HK,k (ey)
⏐
⏐
⏐
⏐ ≤ ||HK,k ||1 (exp A0)k(A0k2)l.
Using Theorem
4.2, it is enough to take A2 = A1 exp(A0). □
Corollary 5.2. For every knot K there are positive constants A4, A5 such that
ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT 13
(a) for 0 ≤ k, 0 ≤ N , and |α| < 1 and y on the interval from 0 to α/k, we have
⏐
⏐
⏐
⏐
∂N
∂y N hK,k (α, y)
⏐
⏐
⏐
⏐ < |αA4|k−N (A5k2)N .
(b) for 0 ≤ k, 0 ≤ N , and |α| < 1 and every positive integer n, we have
⏐
⏐
⏐
⏐
⏐hK,k (α, α/n) −
N −1∑
p=0
dk,p (α) (α/n)p
⏐
⏐
⏐
⏐
⏐ < 1
N !
(α
n
) N
|αA4|k−N (A5k2)N .
Proof. (a) The N -th derivative of hK,k (α, y), which is the product of ck(α, y) and HK,k (ey), is the sum of
2N terms, each of the form
∂l
∂y l ck(α, y) ∂N −l
∂y N −l HK,k (ey).
Using Lemma 5.1, the absolute value of the above term is bounded by |α|k−l(A2A3)k(A0)N −lk2N , which,
in turn, is less than |α|k−N (A2A3)k(A0)N k2N . Hence, multiplied by 2 N we get
⏐
⏐
⏐
⏐
∂l
∂y l hK,k (α, y)
⏐
⏐
⏐
⏐ < 2N × |α|k−N (A2A3)k(A0)N k2N = (αA2A3)k−N (2A0A2A3k2)N .
It is enough to take A4 = A2A3 and A5 = 2A0A2A3.
(b) By Taylor’s Theorem,
⏐
⏐
⏐
⏐
⏐hK,k (α, α/n) −
N −1∑
p=0
dk,p (α) (α/n)p
⏐
⏐
⏐
⏐
⏐ < 1
N !
(α
n
) N
max
⏐
⏐
⏐
⏐
∂N
∂y N hK,k (α, y)
⏐
⏐
⏐
⏐,
where max is taken when y is on the interval connecting 0 and α/n. Using the estimate of part (a), we get
the result. □
5.2. Theorem
4.2 implies Theorem 1.6. To simplify notation, let us deﬁne, for a knot K,
(20) f [N ]
K,n (z) := JK,n (ez/n ) −
N −1∑
k=0
PK,k (ez)
∆ K(ez)2k+1
(z
n
) k
.
Theorem 1.6 follows from Theorem 1.5, Lemma 2.1 and the following uniform bound.
Theorem 5.3. For every knot K there exists an open neighborhood ˜UK of 0 ∈ C such that for every N ≥ 0
there exists a positive number MN such that for α ∈ ˜UK, and all n ≥ 0, we have:
⏐
⏐
⏐
⏐
(n
α
) N
f (N )
K,n (α)
⏐
⏐
⏐
⏐ < M N .
Proof. (of Theorem
5.3, assuming Theorem 4.2) We have the following identities, where the second follows
from ( 14) and ( 15):
f [N ]
K,n (α) = fK,n (α) −
N −1∑
p=0
RK,p (α)
(α
n
) p
=
∞∑
k=0
hK,k (α, α
n ) −
N −1∑
p=0
( ∞∑
k=0
dk,p (α)
) (α
n
) p
=
∞∑
k=0
[
hK,k (α, α
n ) −
N −1∑
p=0
dk,p (α)
(α
n
) p
]
Using the estimate in Corollary 5.2, we see that
14 STA VROS GAROUF ALIDIS AND THANG TQ L ˆE
⏐
⏐
⏐
⏐
(n
α
) N
f [N ]
K,n (α)
⏐
⏐
⏐
⏐ < 1
N !
∞∑
k=0
|αA4|k−N (A5k2)N .
If |αA4| < 1, the series of the right hand side is absolutely convergent. It is en ough to take ˜UK to be the
disk centered at 0 with radius 1 /(2A4 + 1). This proves Theorem
5.3, assuming Theorem 4.2. □
