---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-013-43-calculation-of-the-critical-value
section_title: "Calculation of the critical value"
section_number: 4.3
pages: 33-35
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
Calculation of the critical value
In this section, we calculate the concrete values of a critical point and the Hesse matrix
of ˆV .
The diﬀerentials of ˆV are presented by
∂
∂t
ˆV (t, s, u) = 2 log(1 −x) −log
(
1 −y
x
)
−2π
√
−1
(
t −1
2
)
,
(59)
∂
∂s
ˆV (t, s, u) = −2 log(1 −y) + log
(
1 −y
x
)
+ 2π
√
−1
(
2s + u −1
)
,
(60)
∂
∂u
ˆV (t, s, u) = −log(1 −z) + 2π
√
−1
(
s + u −1
2
)
,
(61)
where x = e2π√−1 t, y = e2π√−1 s and z = e2π√−1 u.
Lemma 4.2. ˆV has a unique critical point (t0, s0, u0) in P −1(∆′), where P : C3 →R3 is
the projection to the real parts of the entries.
33
Proof. Any critical point of ˆV is given by a solution of
∂
∂t ˆV =
∂
∂s ˆV =
∂
∂u ˆV = 0, and these
equations are rewritten,
(1 −x)2 = −x
(
1 −y
x
)
,
(1 −y)2 = y2 z
(
1 −y
x
)
,
1 −z = −y z.
By using the ﬁrst and third formula, we remove y and z from the second formula, to
obtain
x5 −2x4 + 2x3 −3x2 + 2x −1 = 0.
Its solutions are given by
x = −0.232705... ± √−1 · 1.09381... ,
0.438694... ± √−1 · 0.557752... ,
1.58802... .
Since x = e2π√−1 t,
t = 0.283362... −√−1 · 0.0177936... ,
0.716638... −√−1 · 0.0177936... ,
0.143927... + √−1 · 0.0545975... ,
0.856073... + √−1 · 0.0545975... ,
−√−1 · 0.0736072... .
Among these, the second and fourth solutions are in the range of t in ∆′. Further, as for
the fourth solution, s = 0.0243944... + √−1 · 0.127823... , and this is not in ∆′. From the
second solution, we have that
x0 = −0.232705... −√−1 · 1.09381... ,
t0 = 0.716638... −√−1 · 0.0177936... ,
y0 = 0.0904327... + √−1 · 1.60288... ,
s0 = 0.24103... −√−1 · 0.0753425... ,
z0 = 0.267792... + √−1 · 0.471915... ,
u0 = 0.167853... + √−1 · 0.0973042... ,
where x0 = e2π√−1 t0, y0 = e2π√−1 s0 and z0 = e2π√−1 u0. These give a unique critical point
in P −1(∆′).
The critical value of ˆV at the critical point of Lemma 4.2 is presented by
ς = ˆV (t0, s0, u0)
=
1
2π√−1
(
−2 Li2(x0) −Li2
(y0
x0
)
+ 2 Li2(y0) + Li2(z0) + π2
3
)
+ 2π
√
−1 · 1
2
(
−t2
0 + s2
0 + (s0 + u0)2 + t0 −s0 −(s0 + u0) + 1
6
)
(62)
= 0.700414... −√−1 · 0.934648... .
Further, we put its real part to be ςR ,
ςR = Re ς = 0.700414... .
(63)
We calculate the Hesse matrix of ˆV . Since x = e2π√−1 t,
d
dt = 2π√−1 x d
dx. Hence, from
(59), we have that
∂2
∂t2 ˆV = 2π
√
−1 x ∂
∂x
(
2 log(1−x)−log
(
1−y
x
))
−2π
√
−1 = 2π
√
−1
(
−1 + x
1 −x −
y
x
1 −y
x
)
.
34
By calculating other entries similarly, the Hesse matrix of ˆV at (t0, s0, u0) is presented by
H0 = 2π
√
−1








−1 + x0
1 −x0
−
y0
x0
1 −y0
x0
y0
x0
1 −y0
x0
0
y0
x0
1 −y0
x0
2
1 −y0
−
y0
x0
1 −y0
x0
1
0
1
1
1 −z0








.
(64)
