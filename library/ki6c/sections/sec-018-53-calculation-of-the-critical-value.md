---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-018-53-calculation-of-the-critical-value
section_title: "Calculation of the critical value"
section_number: 5.3
pages: 50-52
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
ˆV (t, s, u) = −2 log(1 −x) + log
(
1 −x
y
)
+ 2π
√
−1
(
t −1
2
)
,
(83)
∂
∂s
ˆV (t, s, u) = 2 log(1 −y) −log
(
1 −x
y
)
−log
(
1 −y
z
)
−2π
√
−1
(
s −1
2
)
,
(84)
∂
∂u
ˆV (t, s, u) = −2 log(1 −z) + log
(
1 −y
z
)
+ 2π
√
−1
(
u −1
2
)
,
(85)
where x = e2π√−1 t, y = e2π√−1 s and z = e2π√−1 u.
Lemma 5.1. ˆV has a unique critical point (t0, s0, u0) in P −1(∆′), where P : C3 →R3 is
the projection to the real parts of the entries.
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
1 −x
y
)
,
(1 −y)2 = −y
(
1 −x
y
)(
1 −y
z
)
,
(1 −z)2 = −z
(
1 −y
z
)
.
From the ﬁrst formula, we have that y = x2/(x2 −x+1). Hence, from the second formula,
we have that z = x3/
(
(x −1)(x2 + 1)
)
. By substituting these into the third formula, we
obtain
x6 −2x5 + 5x4 −6x3 + 5x2 −3x + 1 = 0.
Its solutions are given by
x = 0.108378... ± √−1 · 0.818891... ,
0.23185... ± √−1 · 1.65564... ,
0.659772... ± √−1 · 0.298454... .
50
Since x = e2π√−1 t,
t = 0.229058... + √−1 · 0.030418... ,
0.770942... + √−1 · 0.030418... ,
0.227856... −√−1 · 0.081789... ,
0.772144... −√−1 · 0.081789... ,
0.067611... + √−1 · 0.051371... ,
0.932389... + √−1 · 0.051371... .
Among these, the ﬁrst and third solutions are in the range of t in ∆′. Further, as for the
third solution, u = 0.932389... −√−1 · 0.0513713... , and this is not in ∆′. From the ﬁrst
solution, we have that
x0 = 0.108378... + √−1 · 0.818891... ,
t0 = 0.229058... + √−1 · 0.030418... ,
y0 = −0.57395... −√−1 · 0.818891... ,
s0 = 0.652705... ,
z0 = 0.158836... + √−1 · 1.20014... ,
u0 = 0.229058... −√−1 · 0.030418... ,
where x0 = e2π√−1 t0, y0 = e2π√−1 s0 and z0 = e2π√−1 u0. These give a unique critical point
of ˆV in P −1(∆′).
The critical value of ˆV at the critical point of Lemma 5.1 is presented by
ς = ˆV (t0, s0, u0)
=
1
2π√−1
(
2 Li2(x0) −Li2
(x0
y0
)
−2 Li2(y0) + Li2
(y0
z0
)
+ 2 Li2(z0)
)
+ 2π
√
−1 · 1
2
(
t2
0 −s2
0 + u2
0 −t0 + s0 −u0 + 1
6
)
(86)
= 0.906072... ,
noting that this value is real, since the 63 knot is amphicheiral and the above value is
invariant under the symmetry
(t, s, u) 7−→(u, s, t),
(x, y, z) 7−→(1/z, 1/y, 1/x).
(87)
We calculate the Hesse matrix of ˆV . Since x = e2π√−1 t,
d
dt = 2π√−1 x d
dx. Hence, from
(83), we have that
∂2
∂t2 ˆV
= 2π
√
−1
(
x
(
2
1 −x −
1
y
1 −x
y
)
+ 1
)
= 2π
√
−1
(1 + x
1 −x −
x
y
1 −x
y
)
.
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


1 + x0
1 −x0
−
x0
y0
1 −x0
y0
x0
y0
1 −x0
y0
0
x0
y0
1 −x0
y0
−1 + y0
1 −y0
−
x0
y0
1 −x0
y0
+
y0
z0
1 −y0
z0
−
y0
z0
1 −y0
z0
0
−
y0
z0
1 −y0
z0
1 + z0
1 −z0
+
y0
z0
1 −y0
z0









. (88)
51
