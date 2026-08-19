---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-035-b1-preliminary-estimates
section_title: "B.1. Preliminary estimates"
section_number: null
pages: 27-28
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
Lemma B.1. (a) The xj, as a function of j, is increasing for j ∈ [0, n/2] and decreasing for j ∈ [n/2, n]. In
particular, for j ≤ l ≤ n − j we have xj ≤ xl.
(b) For every 1 ≤ j ≤ n − 1, one has 2 ≥ xj. For n/4 ≤ j ≤ 3n/4, one has 2 ≤ (xj)2.
Lemma B.2. For a ﬁxed k, 1 ≤ k ≤ n − 1, the value of yb(k) :=∏ b+k
j=b+1 xj achieves maximum at
(50) b = β(k) := ⌊(n − k)/2⌋.
Proof. We will prove that if b < β (k), then yb(k) ≤ yb+1(k), while if b > β (k) then yb(k) ≤ yb−1(k). This
will prove the lemma.
Suppose b < β (k). Then b ≤ ⌊(n− k)/2⌋ −1 ≤ (n− k)/2 − 1. It follows that ( b + 1) ≤ b + k + 1 ≤ n− (b + 1).
From Lemma B.1(a) we get xb+1 ≤ xb+k+1. Hence yb+1(k)/yb(k) = xb+k+1/xb+1 ≥ 1, or yb+1(k) ≥ yb(k).
Suppose now b ≥ 1 + β(k). If b ≥ n/2, then xb ≥ xb+k since yj is deceasing on [ n/2, n]. If b < n/ 2, then
from b ≥ 1 +⌊(n − k)/2⌋ one can easily show that b + k ≥ n − b ≥ n/2. Hence we also have xb = xn−b ≥ xb+k.
Thus yb−1(k)/yb(k) = xb/xb+k ≥ 1. □
Using ( 39), with |evn({j})| = xj, we have
(51) |evnR+(n; a, b, k)| = yb(k) ya−k(k)
y0(k) , |evnR−(n; a, b, k)| = ya(k) yb−k(k)
y0(k) .
By Lemma B.2, both yb(k) and ya−k(k) achieve maximum when b = a − k = β(k). Hence
(52) max |evnR+(n; a, b, k)| = max
0≤k≤n
s(k), where s(k) =
(
yβ (k)(k)
) 2
y0(k) .
Lemma B.3. One has
(53) s(k + 1)
s(k) = (xβ (k))2
xk+1
with the denominator satisfying
(54) xk+1 =
{
x2β (k)−1 if n − k is even
x2β (k) if n − k is odd
Proof. By deﬁnition
(55) s(k) =
(
yβ (k)(k)
) 2
y0(k) =
(∏ k
j=1 xβ (k)+j
) 2
∏ k
j=1 xj
.
Note that, with β(k) = ⌊(n − k)/2⌋, we have
(56) β(k + 1) =
{
β(k) − 1 if n − k is even
β(k) if n − k is odd
We consider two cases: n − k is even and n − k odd.
(a) n − k is even. Replacing k with k + 1 in (
55), then using β(k + 1) = β(k) − 1, we get
s(k + 1) =
(∏ k+1
j=1 xβ (k+1)+j
) 2
∏ k+1
j=1 xj
=
(∏ k+1
j=1 xbk−1+j
) 2
∏ k+1
j=1 xj
=
(xβ (k))2
(∏ k
j=1 xβ (k)+j
) 2
xk+1
∏ k
j=1 xj
.
Dividing by s(k), we get (
53). As for the denominator, using xj = xn−j and n − k = 2β(k),
xk+1 = xn−k−1 = x2β (k)−1.
28 STA VROS GAROUF ALIDIS AND THANG TQ L ˆE
This proves the lemma when n − k is even.
(b) n − k is odd. Replacing k with k + 1 in ( 55), then using β(k + 1) = β(k), we get
(57) s(k + 1) =
(∏ k+1
j=1 xbk+j
) 2
∏ k+1
j=1 xj
=
(xβ (k)+k+1)2
(∏ k
j=1 xβ (k)+j
) 2
xk+1
∏ k
j=1 xj
= (xβ (k)+k+1)2
xk+1
s(k).
Using xj = xn−j and n − β(k) − k − 1 = β(k), we have
xβ (k)+k+1 = xn−β (k)−k−1 = xβ (k),
which, together with Equation ( 57), proves Equation ( 53). As for the denominator, using n − k − 1 = 2 β(k),
xk+1 = xn−k−1 = x2β (k).
This completes the proof of the lemma. □
As k increases from 0 to n, β(k) = ⌊(n − k)/2⌋ decreases and covers all integers from ⌊n/2⌋ to 0.
Lemma B.4. (a) If n ≥ 7 then s(k) achieves maximum at an integer k such that β(k) = ⌊(n − 1)/4⌋.
(b) s(k) achieves maximum at k which is the smallest integer such that β(k) = ⌊(n − 1)/4⌋.
Proof. (a) We will show that
(a1) if β(k) > (n − 1)/4 then s(k + 1) ≥ s(k), and
(a2) if β(k) ≤ (n − 1)/4 − 1 then s(k − 1) > s(k).
This will show that the maximum can be achieved for a k such that β(k) = ⌊(n − 1)/4⌋.
Proof of (a1). Suppose β(k) > n−1
4 . There is no integer in the interval ( n−1
4 , n
4 ), because otherwise (by
multiplying by 4) there would be an integer in ( n − 1, n). It follows that β(k) ≥ n/4.
Besides, β(k) = ⌊(n − k)/2⌋ ≤ n/2. Thus β(k) ∈ [n/4, n/2]. By Lemma B.1(b), ( xβ (k))2 ≥ 2 ≥ xj for any
1 ≤ j ≤ n. It follows that the right hand side of ( 53) is bigger than or equal to 1, or s(k + 1)/s(k) ≥ 1.
Proof of (a2). Suppose β(k) ≤ n−1
4 − 1. Then β(k − 1) ≤ n−1
4 since by ( 56), either β(k − 1) = β(k) or
β(k − 1) = β(k) + 1.
Since 2 β(k − 1) < n/ 2, by Lemma B.1(a), x2β (k−1) ≥ x2β (k−1)−1. It follows that xk, either equal to
x2β (k−1) or x2β (k−1)−1 by ( 54), satisﬁes
xk ≥ x2β (k−1)−1.
By Lemma B.3 and the above inequality,
s(k)
s(k − 1) = (xβ (k−1))2
xk
≤ (xβ (k−1))2
x2β (k−1)−1
< 1
where the last inequality follows from Lemma B.5 below. This completes the proof of the part (a).
(b) When n < 7 the statement is checked by explicit calculation. We will assume n ≥ 7.
There are two values of k such that β(k) = ⌊(n − 1)/4⌋. Let κ be the smaller one, then the other one is
κ + 1. Then n − κ is odd since otherwise β(κ − 1) = β(k).
Since n − κ is odd, by Lemma B.3, we have
s(κ + 1)
s(κ) = (xβ (κ ))2
x2β (κ )−1
,
which is less than 1 by Lemma B.5. This means s(k) achieves maximum at k = κ. □
