---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-142-7-conclusion-of-the-burgess-argument
section_title: "Conclusion of the Burgess argument"
section_number: 7
pages: 275-276
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
We now apply Proposition 6.2 to (5 -9) with K= 2H/P, recalling that we are working under the
assumption (5-1) that H1≤ H2≤···≤ Hn. (Also recall that Kn≤ Hn< q.) We conclude that
|S(F; N, H)|2r≪n,r,1, D(log q)2r(n+1) P2nr−1‖H‖−1
(‖H‖
Pn
)2r n∑
j=0
q(n+ j)/2~Bn,r( j; H/P)−1
=(log q)2r(n+1)‖H‖2r−1 P−1qn/2
n∑
j=0
q j/2~Bn,r( j; H/P)−1, (7-1)
in which we recall the deﬁnition of the function ~Bn,r(·,·) from (6-4).
At this stage of the Burgess argument in the one-dimensional setting n= 1, one knows thatθ0= 0 and
θ1= r, so that the sum over j∈{ 0, 1} contributes(1+ q1/2(H1/P)−r). To balance this, we would then
choose P to be an integer with
1
2 H1q−1/(2r)≤ P≤ H1q−1/(2r). (7-2)
Thus when n= 1, we recover
|S(F; N, H)|≪‖ H‖1−1/rq(r+1)/4r 2
(log q)2,
which agrees with Burgess’s statement (1-1) up to a logarithm. Now for n≥ 2, we observe:
Lemma 7.1. For 1≤ K1≤ K2≤···≤ Kn,
n∑
j=0
q j/2~Bn,r( j; K)−1≪n,r 1
precisely when
q1/2K−θ1
1 ≤ 1. (7-3)
Under this assumption, the sum over j is dominated by the terms with j = 0, 1.
In particular, this lemma (whose proof we defer to Section 7B) shows that the sum is ≫ 1 if the
relation (7-3) does not hold; hence it is advantageous to assume (7 -3). Under this assumption, we can
dominate the sum by the terms with j= 0, 1 and hence we conclude from (7-1) that
|S(F; N, H)|2r≪n,r,1, D(log q)2r(n+1)‖H‖2r−1 P−1qn/2(1+ q1/2(H1/P)−θ1).
To balance the last two terms within parentheses, we choose P to be an integer with
H1
2q1/(2θ1)≤ P≤ H1
q1/(2θ1), (7-4)
where we recall that θ1=⌊(r− 1)/(n− 1)⌋ if n≥ 2. We recall that earlier in (5 -2) and (5-8) we had the
requirements that P≤ Hi for all i and Hi P< q for all i. The ﬁrst is clearly true; the second we may
verify as long as we assume Hn H1< q1+1/(2θ1), as we do in our theorem statement.
1942 Lillian B. Pierce and Junyan Xu
With this choice for P, we have
|S(F; N, H)|2r≪n,r,1, D‖H‖2r−1H−1
1 qn/2+1/(2θ1)(log q)2r(n+1),
and hence we conclude that
|S(F; N, H)|≪ n,r,1, D‖H‖1−1/(2r)H−1/(2r)
1 q(nθ1+1)/4rθ1(log q)n+1.
This proves Theorem 1.1, upon recalling that we have reduced to the setting in which Hmin= H1,
Hmax= Hn, and we have set
2=θ1=
⌊ r−1
n−1
⌋
if n≥ 2.
