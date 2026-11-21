---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-008-33-calculation-of-the-critical-value
section_title: "Calculation of the critical value"
section_number: 3.3
pages: 18-20
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
ˆV (t, s, u) = −2 log(1 −x) + 2π
√
−1
(
3t + 2s + u −3
2
)
,
(37)
∂
∂s
ˆV (t, s, u) = −log(1 −y) + 2π
√
−1 (2t + 2s + u −1),
(38)
∂
∂u
ˆV (t, s, u) = −log(1 −z) + 2π
√
−1
(
t + s + u −1
2
)
,
(39)
where x = e2π√−1 t, y = e2π√−1 s and z = e2π√−1 u.
Lemma 3.3. ˆV has a unique critical point (t0, s0, u0) in P −1(∆′), where P : C3 →R3 is
the projection to the real parts of the entries.
Proof. Any critical point of ˆV is given by a solution of
∂
∂t ˆV =
∂
∂s ˆV =
∂
∂u ˆV = 0, and these
equations are rewritten,
(1 −x)2 = −x3 y2 z,
1 −y = x2 y2 z,
1 −z = −x y z.
Putting y′ = xy and z′ = xyz, they are rewritten,
(1 −x)2 = −x y′z′,
1 −y′
x = y′z′,
1 −z′
y′ = −z′.
From the third formula, we have that y′ = z′/(1+z′). Hence, from the second formula, we
have that x = −z′/(z′2 −z′ −1). By substituting them into the ﬁrst formula, we obtain
that
2z′4 −z′3 −2z′2 + z′ + 1 = 0.
Its solutions are given by
z′ = −0.677958... ± √−1 · 0.15778... ,
0.927958... ± √−1 · 0.413327... .
18
Further, their corresponding values of (t, s) are given by
(t, s) = (0.16676... −√−1 · 0.0928453... ,
0.224343... −√−1 · 0.0127069...),
(0.83324... −√−1 · 0.0928453... ,
0.775657... −√−1 · 0.0127069...),
(0.111002... + √−1 · 0.0376865... ,
0.922078... + √−1 · 0.0678661...),
(0.888998... + √−1 · 0.0376865... ,
0.0779221... + √−1 · 0.0678661...).
Among these, the ﬁrst solution is in ∆′, from which we have that
x0 = 0.895123... + √−1 · 1.55249... ,
t0 = 0.16676... −√−1 · 0.0928453... ,
y0 = 0.17385... + √−1 · 1.06907... ,
s0 = 0.224343... −√−1 · 0.0127069... ,
z0 = 0.322042... + √−1 · 0.15778... ,
u0 = 0.0725053... + √−1 · 0.163214... ,
where x0 = e2π√−1 t0, y0 = e2π√−1 s0 and z0 = e2π√−1 u0. These give a unique critical point
of ˆV in P −1(∆′).
The critical value of ˆV at the critical point of Lemma 3.3 is presented by
ς = ˆV (t0, s0, u0)
=
1
2π√−1
(
2 Li2(x0) + Li2(y0) + Li2(z0) + π2
3
)
+ 2π
√
−1 · 1
2
(
(t0 + s0 + u0)2 + (t0 + s0)2 + t2
0 −3t0 −2s0 −u0 + 1
2
)
(40)
= 0.5035603... −√−1 · 1.08078... .
Further, we put its real part to be ςR ,
ςR = Re ς = 0.5035603... .
(41)
We calculate the Hesse matrix of ˆV . Since x = e2π√−1 t,
d
dt = 2π√−1 x d
dx. Hence, from
(37), we have that
∂2
∂t2 ˆV
= 2π
√
−1 x ∂
∂x
(
−2 log(1 −x)
)
+ 2π
√
−1 · 3 = 2π
√
−1 · 3 −x
1 −x .
Similarly, we have that
∂2
∂t∂s
ˆV
= 2π
√
−1 · 2,
∂2
∂t∂u
ˆV
= 2π
√
−1,
∂2
∂s2 ˆV
= 2 −y
1 −y ,
∂2
∂s∂u
ˆV
= 2π
√
−1,
∂2
∂u2 ˆV
=
1
1 −z .
Hence, the Hesse matrix of ˆV at (t0, s0, u0) is presented by
H0 = 2π
√
−1







3 −x0
1 −x0
2
1
2
2 −y0
1 −y0
1
1
1
1
1 −z0







.
(42)
19
