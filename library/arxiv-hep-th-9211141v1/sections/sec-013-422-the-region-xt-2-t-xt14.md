---
doc_id: arxiv-hep-th-9211141v1
doc_title: "arXiv:hep-th/9211141v1 1 Dec 1992"
section_id: sec-013-422-the-region-xt-2-t-xt14
section_title: "The region $x>>t^{-2}$, $t-x>>t^{1/4}$"
section_number: 4.2.2
pages: 22-23
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
toc_source: inferred
doc_brief: "arXiv:hep-th/9211141v1 1 Dec 1992 — 17 sections: Front matter; INTRODUCTION AND SUMMARY OF RESULT; The System of Partial Differential"
---
If in equation (4.8) we set
α(x) = (t −x)2 −µ
x
,
y =
Z x
0
q
α(z) dz ,
h(y) = α(x)1/4g(x)
then the equation for h(y) is
h′′(y) −h(y) =
"1
4
α′′
α2 −5
16
α′2
α3 −
1
4x2α
#
h(y) ,
where on the right side ′ =
d
dx. Since dy = α(x)1/2 dx, the integral with respect to y (of the
factor of h(y) on the right side of the equation) over any interval equals
Z 1
4
α′′
α3/2 −5
16
α′2
α5/2 −
1
4x2α1/2
!
dx
over the corresponding x interval. This will be o(1) as long as, in this interval, x >> t−2
and t −x >> t1/4.
In this same region y >> 1 and so
h(y) ∼aey
(4.10)
for some constant a = a(t). In case x << 1 we have y = 2t√x + o(1) and so
f(x) = x−1/2g(x) ∼at−1/2x−1/4e2t√x ,
(t−2 << x << 1).
Comparing this result with (4.9) in the overlapping region t−2 << x << t−1/2 and using the
known asymptotics of I0(z) as z →∞shows that a ∼1/2√π. Hence from (4.10)
f(x) ∼
1
2√π
(t −x)−1/2
x1/4
exp



Z x
0
s
(t −z)2 −µ
z
dz


,
(x >> t−2, t −x >> t1/4) .
We also used here once again the estimate µ = O(t1/2). Because of this same estimate we
can write the integral in the exponential as
Z x
0
t −z
√z
(
1 −1
2
µ
(t −z)2 + O
 
µ2
(t −z)4
!)
dz .
Because t −x >> t1/4 the last term in brackets contributes o(1) to the integral, and so we
obtain
2tx1/2 −2
3x3/2 −µ
2
Z x
0
dz
√z(t −z) .
Replacing z by tz2 shows that the integral here equals
t−1/2 log
√
t + √x
2
t −x
.
Thus
f(x) ∼
1
2√π
(t −x)
1
2 t−1/2µ−1
2
x1/4
√
t + √x
t−1/2 µ exp

2tx1/2 −2
3x3/2

(4.11)
(x >> t−2, t −x >> t1/4).
Let us see what happens if x is not far from t, if
t1/4 << t −x << t1/2 .
Then since
2tx1/2 −2
3x3/2 = 4
3t4/3 −1
2(x −t)2 + o(1)
in this region, we ﬁnd
f(x) ∼
1
2√π2−t−1/2µt−3/4

t
t −x
−1
2 t−1/2µ+ 1
2 exp
4
3t4/3 −1
2(x −t)2

(4.12)
(t1/4 << t −x << t1/2)
