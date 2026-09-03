---
doc_id: arxiv-hep-th-9211141v1
doc_title: "ITD 92/93–9"
section_id: sec-006-3-the-region-x-t-t14
section_title: "The region x −t >> t1/4"
section_number: 3
pages: 23-24
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
doc_brief: "ITD 92/93–9 — 13 sections: INTRODUCTION AND SUMMARY OF RESULT; The Ordinary Diﬀerential Equations; THE SYSTEM OF PARTIAL DIFFERENTIAL"
---
This is quite similar to the preceding. The main diﬀerence is that instead of making the
variable change y =
R α(x)1/2 dx in (4.8) we now set
y = 2
3x3/2 −2tx1/2 −
Z ∞
x
q
α(z) −z1/2 + tz−1/2

dz .
23
Since an eigenfunction cannot grow exponentially at ∞only the negative exponential e−y
can appear in the asymptotics and we ﬁnd that
f(x) ∼b(x −t)−1/2
x1/4
exp


2tx1/2 −2
3x3/2 +
Z ∞
x


s
(z −t)2 −µ
z
−z1/2 + tz−1/2

dz



for some constant b = b(t). Now the integral in the exponential is
−µ
2 t−1/2 log
√x +
√
t
2
x −t
+ o(1)
and so
f(x) ∼b
(x −t)
1
2t−1/2µ−1
2
x1/4
√x +
√
t
t−1/2µ exp

2tx1/2 −2
3x3/2

(x −t >> t1/4)
(4.13)
and specializing to the region t1/4 << x −t << t1/2 gives
f(x) ∼b 2−t−1/2µt−3/4

t
x −t
−1
2 t−1/2µ+ 1
2 exp
4
3t3/2 −1
2(x −t)2

(4.14)
(t1/4 << x −t << t1/2)
