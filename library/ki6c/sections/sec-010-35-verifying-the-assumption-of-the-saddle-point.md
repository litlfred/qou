---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-010-35-verifying-the-assumption-of-the-saddle-point
section_title: "Verifying the assumption of the saddle point method"
section_number: 3.5
pages: 22-26
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
Verifying the assumption of the saddle point method
In this section, we verify the assumption of the saddle point method in Lemma 3.9. In
order to show this lemma, we show Lemmas 3.5–3.8 in advance. As we mentioned in
Remark 2.7, we verify the assumption for ˆV (t, s, u) instead of V (t, s, u), since V (t, s, u)
converges uniformly to ˆV (t, s, u) on ∆′ in the form mentioned in Remark 2.7.
In the proof of Lemma 3.9, by (43), it is suﬃcient to decrease Re ˆV (t, s, u) by 0.142571...
by pushing t, s, u into the imaginary directions.
In order to calculate this concretely,
putting
f(X, Y, Z) = Re ˆV (t + X
√
−1, s + Y
√
−1, u + Z
√
−1) −ςR ,
we consider the behavior of f at each ﬁber of the projection C3 →R3.
Lemma 3.5 ([34]). Fixing X and Y , we regard f as a function of Z.
(1) If t + s + u ≥1
2, then f is monotonically decreasing.
(2) If t + s + u < 1
2, then f has a unique minimal point at Z = g3(t, s, u), where
g3(t, s, u) =
1
2π log
sin 2π(t + s)
sin 2π(1
2 −t −s −u) .
In particular, g3(t, s, u) goes to ∞as t + s + u →1
2 −0.
22
Proof. As a function of Z, the diﬀerential of f is presented by
∂f
∂Z = Arg (1 −z) −2π
(
t + s + u −1
2
)
,
where z = e2π√−1 (u+Z√−1). Since 0 < u < 1
2,
−2π
(1
2 −u
)
< Arg (1 −z) < 0,
and Arg (1 −z) is monotonically increasing as a function of Z. Further,
∂f
∂Z

Z→∞= 2π
(1
2 −t −s −u
)
,
∂f
∂Z

Z→−∞= −2π
(1
2 −u
)
−2π
(
t + s + u −1
2
)
= −2π(t + s) < 0.
If t + s + u ≥1
2, then ∂f
∂Z is always negative, and (1) holds.
If t + s + u < 1
2, then there is a unique zero of ∂f
∂Z, which gives a unique minimal point
of f. When ∂f
∂Z = 0, we have that −Arg (1 −z) = 2π(1
2 −t −s −u), and t, s, u and Z are
related as shown in the following picture.
0
2πu
e−2πZ
1
1
z
2π( 1
2 −t−s−u)
Hence,
e−2πZ
sin 2π(1
2 −t −s −u) =
1
sin 2π(t + s) .
Therefore,
Z =
1
2π log
sin 2π(t + s)
sin 2π(1
2 −t −s −u) ,
and this gives the minimal point of the lemma. Hence, (2) holds.
Lemma 3.6 ([34]). Fixing X and Z, we regard f as a function of Y .
(1) If 2t + 2s + u ≥1, then f is monotonically decreasing.
(2) If 2t + 2s + u < 1 and 2t + s + u >
1
2, then f has a unique minimal point at
Y = g2(t, s, u), where
g2(t, s, u) =
1
2π log sin 2π(2t + s + u −1
2)
sin 2π(1 −2t −2s −u) .
In particular, g2(t, s, u) goes to ∞as 2t+2s+u →1−0, and goes to −∞as 2t+s+u →
1
2 + 0.
(3) If 2t + s + u ≤1
2, then f is monotonically increasing.
23
Proof. As a function of Y , the diﬀerential of f is presented by
∂f
∂Y
= Arg (1 −y) −2π
(
2t + 2s + u −1
)
,
where y = e2π√−1 (s+Y √−1). Since 0 < s < 1
2,
−2π
(1
2 −s
)
< Arg (1 −y) < 0,
and Arg (1 −y) is monotonically increasing as a function of Y . Further,
∂f
∂Y

Y →∞= 2π
(
1 −2t −2s −u
)
,
∂f
∂Y

Y →−∞= −2π
(1
2 −s
)
−2π
(
2t + 2s + u −1
)
= −2π
(
2t + s + u −1
2
)
.
If 2t + 2s + u ≥1, then ∂f
∂Y is always negative, and (1) holds.
If 2t + s + u ≤1
2, then ∂f
∂Y is always positive, and (3) holds.
If 2t + 2s + u < 1 and 2t + s + u > 1
2, then there is a unique zero of ∂f
∂Y , which gives
a unique minimal point of f. We can obtain the value of the minimal point in the same
way as in the proof of Lemma 3.5.
Lemma 3.7 ([34]). Fixing Y and Z, we regard f as a function of X.
(1) If 3t + 2s + u ≥3
2, then f is monotonically decreasing.
(2) If 3t + 2s + u <
3
2 and t + 2s + u >
1
2, then f has a unique minimal point at
X = g1(t, s, u), where
g1(t, s, u) =
1
2π log sin 2π(t + 2s + u −1
2)
sin 2π(3
2 −3t −2s −u) .
In particular, g1(t, s, u) goes to ∞as 3t+2s+u →3
2 −0, and goes to −∞as t+2s+u →
1
2 + 0.
(3) If t + 2s + u ≤1
2, then f is monotonically increasing.
Proof. As a function of X, the diﬀerential of f is presented by
∂f
∂X = 2 Arg (1 −x) −2π
(
3t + 2s + u −3
2
)
,
where x = e2π√−1 (t+X√−1). Since 0 < t < 1
2,
−2π
(1
2 −t
)
< Arg (1 −x) < 0,
and Arg (1 −x) is monotonically increasing as a function of X. Further,
∂f
∂X

X→∞= 2π
(3
2 −3t −2s −u
)
,
24
∂f
∂X

X→−∞= −2π
(
1 −2t
)
−2π
(
3t + 2s + u −3
2
)
= −2π
(
t + 2s + u −1
2
)
.
If 3t + 2s + u ≥3
2, then
∂f
∂X is always negative, and (1) holds.
If t + 2s + u ≤1
2, then
∂f
∂X is always positive, and (3) holds.
If 3t + 2s + u < 3
2 and t + 2s + u > 1
2, then there is a unique zero of
∂f
∂X , which gives
a unique minimal point of f. We can obtain the value of the minimal point in the same
way as in the proof of Lemma 3.5.
Lemma 3.8 ([34]). For each (t, s, u) ∈∆′ satisfying that 2t + 2s + u < 1, t + s + u < 1
2,
t + 2s + u > 1
2 and 2t + s + u > 1
2, f has a unique minimal point and no other critical
points.
Proof. From the deﬁnition of f,
f(X, Y, Z) = Re
(
1
2π√−1 · 2 Li2(e2π√−1 (t+X√−1))
)
+ 2π
(3
2 −3t −2s −u
)
X
+ Re
(
1
2π√−1 · Li2(e2π√−1 (s+Y √−1))
)
+ 2π
(
1 −2t −2s −u
)
Y
+ Re
(
1
2π√−1 · Li2(e2π√−1 (u+Z√−1))
)
+ 2π
(1
2 −t −s −u
)
Z.
By Lemma 3.7, ﬁxing Y and Z, f has a unique minimal point at X = g1(t, s, u). By
Lemma 3.6, ﬁxing X and Z, f has a unique minimal point at Y = g2(t, s, u).
By
Lemma 3.5, ﬁxing X and Y , f has a unique minimal point at Z = g3(t, s, u). Since the
contribution to f from X, Y and Z are independent, f has a unique minimal point at
(X, Y, Z) =
(
g1(t, s, u), g2(t, s, u), g3(t, s, u)
)
.
Lemma 3.9 ([34]). When we apply Proposition 2.6 to (33), the assumption of Proposition
2.6 holds.
Proof. We show that there exists a homotopy ∆′
δ (0 ≤δ ≤1) between ∆′
0 = ∆′ and ∆′
1
such that
(t0, s0, u0) ∈∆′
1,
(48)
∆′
1 −{(t0, s0, u0)} ⊂
{
(t, s, u) ∈C3 

 Re ˆV (t, s, u) < ςR
}
,
(49)
∂∆′
δ ⊂
{
(t, s, u) ∈C3 

 Re ˆV (t, s, u) < ςR
}
.
(50)
For a suﬃciently large R > 0, we put
ˆg1(t, s, u) =





R
if 3t + 2s + u ≥3
2,
max
{
−R, min {R, g1(t, s, u)}
}
if 3t + 2s + u < 3
2 and t + 2s + u > 1
2,
−R
if t + 2s + u ≤1
2,
ˆg2(t, s, u) =





R
if 2t + 2s + u ≥1,
max
{
−R, min {R, g2(t, s, u)}
}
if 2t + 2s + u < 1 and 2t + s + u > 1
2,
−R
if 2t + s + u ≤1
2,
25
ˆg3(t, s, u) =
{
R
if t + s + u ≥1
2,
min {R, g3(t, s, u)}
if t + s + u < 1
2.
We note that, since g3(t, s, u) →∞as t+s+u →1
2, ˆg3(t, s, u) is continuous, and similarly,
we can check that ˆg1(t, s, u) and ˆg2(t, s, u) are also continuous. We set the ending of the
homotopy by
∆′
1 =
{(
t + ˆg1(t, s, u)
√
−1, s + ˆg2(t, s, u)
√
−1, u + ˆg3(t, s, u)
√
−1
)
∈C3 

 (t, s, u) ∈∆′}
.
Further, we deﬁne the internal part ∆′
δ (0 < δ < 1) of the homotopy by setting it along
the ﬂow from
(
t, s, u
)
determined by the vector ﬁeld
(
−∂f
∂X , −∂f
∂Y , −∂f
∂Z
)
.
We show (50), as follows. From the deﬁnition of ∆′,
∂∆′ ⊂
{
(t, s, u) ∈C3 

 Re ˆV (t, s, u) < ςR
}
.
Further, by the construction of the homotopy, Re ˆV monotonically decreases by the ho-
motopy. Hence, (50) holds.
We show (48) and (49), as follows. Consider the following functions
F(t, s, u, X, Y, Z) = Re ˆV
(
t + X
√
−1, s + Y
√
−1, u + Z
√
−1
)
,
h(t, s, u) = F
(
t, s, u, ˆg1(t, s, u), ˆg2(t, s, u), ˆg3(t, s, u)
)
.
When 3t+2s+u ≥3
2, −h(t, s, u) is suﬃciently large (because we let R be suﬃciently large),
and (49) holds in this case. Similarly, we can check that (49) holds when ˆgi(t, s, u) = ±R.
The remaining case is the case where ˆgi(t, s, u) = gi(t, s, u) for i = 1, 2, 3. In this case,
we show (49), as follows.
It is shown from the deﬁnitions of gi(t, s, u) that
∂F
∂X = 0
at X = g1(t, s, u) and ∂F
∂Y = 0 at Y = g2(t, s, u) and ∂F
∂Z = 0 at Z = g3(t, s, u). Hence,
Im ∂ˆV
∂t = Im ∂ˆV
∂s = Im ∂ˆV
∂u = 0 at
(
t+g1(t, s, u)√−1, s+g2(t, s, u)√−1, u+g3(t, s, u)√−1
)
.
Further,
∂h
∂t = Re ∂ˆV
∂t and
∂h
∂s = Re ∂ˆV
∂s and
∂h
∂u = Re ∂ˆV
∂u at
(
t + g1(t, s, u)√−1, s +
g2(t, s, u)√−1, u + g3(t, s, u)√−1
)
. Therefore, when (t, s, u) is a critial point of h(t, s, u),
(
t + g1(t, s, u)√−1, s + g2(t, s, u)√−1, u + g3(t, s, u)√−1
)
is a critical point of ˆV . Hence,
by Lemma 3.3, h(t, s, u) has a unique maximal point at (t, s, u) = (Re t0, Re s0, Re u0).
Therefore, (48) and (49) hold.
4
The 62 knot
In this section, we show Theorem 1.1 for the 62 knot. We give a proof of the theorem in
Section 4.1, using lemmas shown in Section 4.2–4.5.
