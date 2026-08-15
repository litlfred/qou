---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-021-72-the-bound-for-the-l1-norm-of-hkn
section_title: "The bound for the l1-norm of HK,n"
section_number: 7.2
pages: 17-18
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
Theorem 6.3, we see that there is a constant A7 such that
(29) ||{2n + 2}!HK,n (q)||1 ≤ (A7)n.
The polynomials
˜HK,n (q) := qA0n2
HK,n (q) and g(q) := ˜HK,n (q)
2n+2∏
j=1
(1 − qj )
have only non-negative degrees in q, with deg +( ˜HK,n ) ≤ 2A0n2:
(30) ˜HK,n (q) =
2A0n2
∑
k=0
akqk
Since g(q) is the product of the polynomial on the left hand side of (
29) and a power of q, we have
(31) ||g(q)||1 ≤ (A7)n.
There are estimates of l1-norm using Mahler measure [ Mah60]. However, the estimate ( 31) is weak: the
inequalities of Mahler imply an exponential upper bound on the Mahler m easure of HK,n (q), and a doubly
exponential upper bound on the l1-norm of HK,n (q). The following estimate, which does not follow from
Mahler measure considerations, was communicated to us by D. Boyd . Since
˜HK,n (q) = g(q) 1∏ 2n+2
k=j (1 − qj)
,
we have that
ak =
k∑
i=0
bick−i, where g(q) =
∑
k
bkqk and 1∏ 2n+2
k=1 (1 − qk)
=
∞∑
k=0
ckqk.
Note that ck is the number of partitions of k of length ≤ 2n + 2. Hence 0 ≤ ck−1 ≤ ck, and ck ≤ pk, where
pk is the number of partitions of k. Using the growth rate of pk (see [
And98]), we see that there is a constant
A8 such that
(32) pk < (A8)
√
k.
The crucial part of the above inequality is the exponent
√
k. Now we can easily obtain the desired upper
bounds for || ˜HK,n ||1. Since ak =∑ k
i=0 bick−i we have
|ak| ≤
k∑
i=0
|bi|ck−i ≤
( k∑
i=0
|bi|
)
ck ≤ ||g(q)||1ck
≤ (A7)n(A8)n√
2A0 by ( 31), ( 32) and k ≤ 2A0n2
It follows that, for n ≥ 1,
|| ˜HK,n ||1 ≤
2A0n2
∑
k=0
|ak| ≤ 2A0n2(A7)n(A8)n√2A0 ≤ (A1)n,
for appropriate A1. This completes the proof of Theorem 4.2.
18 STA VROS GAROUF ALIDIS AND THANG TQ L ˆE
