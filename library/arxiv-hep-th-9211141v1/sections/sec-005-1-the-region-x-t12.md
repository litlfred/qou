---
doc_id: arxiv-hep-th-9211141v1
doc_title: "ITD 92/93–9"
section_id: sec-005-1-the-region-x-t12
section_title: "The region x << t−1/2"
section_number: 1
pages: 21-23
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
doc_brief: "ITD 92/93–9 — 13 sections: INTRODUCTION AND SUMMARY OF RESULT; The Ordinary Diﬀerential Equations; THE SYSTEM OF PARTIAL DIFFERENTIAL"
---
If we make the substitutions
f(x) = h(t2x) = h(y)
then (4.7) becomes
(yh′(y))′ −h(y) = t−2
 y2
t4 −2y
t −µ
!
h(y) .
The solution of the equation with the right hand side replaced by 0 which satisﬁes h(0) = 1
is I0(2√y) where I0 is the usual modiﬁed Bessel function. The actual solution h(y) will be
asymptotic to this in any interval over which the integral of the factor of h(y) on the right
hand side of the equation is o(1). Recalling that µ = O(t1/2) we see that y << t3/2 suﬃces.
Hence
f(x) ∼I0

2t√x

,
(x << t−1/2)
(4.9)
21
2.
The region x >> t−2, t −x >> t1/4
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
22
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
