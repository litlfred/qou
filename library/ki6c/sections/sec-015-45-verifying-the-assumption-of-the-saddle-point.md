---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-015-45-verifying-the-assumption-of-the-saddle-point
section_title: "Verifying the assumption of the saddle point method"
section_number: 4.5
pages: 37-44
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
Verifying the assumption of the saddle point method
In this section, we verify the assumption of the saddle point method in Lemma 4.9. In
order to show this lemma, we show Lemmas 4.4–4.8 in advance. As we mentioned in
Remark 2.7, we verify the assumption for ˆV (t, s, u) instead of V (t, s, u), since V (t, s, u)
converges uniformly to ˆV (t, s, u) on ∆′ in the form mentioned in Remark 2.7.
−
−
0
0
5
5
−5
5
10
10
−10
10
Figure 3: Contour lines of Re ˆV (0.8 + X√−1, 0.18 + Y √−1, 0.1) −ςR
In the proof of Lemma 4.9, as mentioned at the beginning of Section 4.4, it is suﬃcient
to decrease Re ˆV (t, s, u) by 0.06, by pushing t, s, u into the imaginary directions. In order
to calculate this concretely, putting
f(X, Y, Z) = Re ˆV (t + X
√
−1, s + Y
√
−1, u + Z
√
−1) −ςR
as in Section 3.5, we consider the behavior of f at each ﬁber of the projection C3 →R3.
Then, unlike Section 3.5, there are some (t, s, u) ∈R3 such that, ﬁxing X and Z, f has
a maximal point as a function of Y ; for example, see Figure 3. We also note that the
37
Hessian of f is not positive where the contour lines are not convex, though we like to
show that the Hesse matrix of f is positive deﬁnite at any critical point of f.
Lemma 4.4. Fixing X and Y , we regard f as a function of Z.
(1) If s + u ≥1
2, then f is monotonically decreasing.
(2) If s + u < 1
2, then f has a unique minimal point at Z = g3(t, s, u), where
g3(t, s, u) =
1
2π log
sin 2πs
sin 2π
( 1
2 −s −u
) .
In particular, this minimal point goes to ∞as s + u →1
2 −0.
Proof. As a function of Z, the diﬀerential of f is presented by
∂f
∂Z = Arg (1 −z) −2π
(
s + u −1
2
)
,
where z = e2π√−1 (u+Z√−1). Hence, we can show the lemma in a similar way as the proof
of Lemma 3.5.
When we regard f as a function of Z ﬁxing X and Y , by Lemma 4.4, f has a unique
minimal point at Z = g3(t, s, u); we note that this minimal point does not depend on X
and Y . In order to consider the behavior of f, putting
ˇf(X, Y ) = f
(
X, Y, g3(t, s, u)
)
,
(68)
we consider the behavior of ˇf in each ﬁber of the projection C3 →R3 at (t, s, u) ∈∆′ ⊂R3.
Lemma 4.5. For each (t, s, u) ∈∆′ satisfying that t−1
2 < s+u < 1
2,
ˇf has a unique
minimal point and no other critical points.
Proof. The diﬀerentials of ˇf are presented by
∂ˇf
∂X =
∂f
∂X = Im
(
−2 log(1 −x) + log
(
1 −y
x
))
+ 2π
(
t −1
2
)
,
∂ˇf
∂Y
=
∂f
∂Y
= Im
(
2 log(1 −y) −log
(
1 −y
x
))
−2π
(
2s + u −1
)
,
where x = e2π√−1 (t+X√−1) and y = e2π√−1 (s+Y √−1). Hence, since
dx
dX = −2πx,
∂2 ˇf
∂X2 = Im
((
2
1 −x +
y
x2
1 −y
x
) dx
dX
)
= 2π Im
(
−
2x
1 −x −
y
x
1 −y
x
)
= 2π Im
(
−
2
1 −x −
1
1 −y
x
)
,
where we obtain the last equality by changing the content of the parentheses by a real
number, which does not change its imaginary part. Similarly, we have that
∂2 ˇf
∂X∂Y
= 2π Im
1
1 −y
x
,
∂2 ˇf
∂Y 2
= 2π Im
(
2
1 −y −
1
1 −y
x
)
.
38
Therefore, the Hesse matrix of ˇf is presented by
2π
(
2a1 + b
−b
−b
2a2 + b
)
,
(69)
where we put
a1 = −Im
1
1 −x ,
a2 = Im
1
1 −y ,
b = −Im
1
1 −y
x
.
Since 0.6 ≤t ≤0.9, Im (1 −x) > 0, and hence, a1 > 0. Similarly, since 0.14 ≤s ≤0.4,
we have that a2 > 0.
When t −s ≤1
2, we have that Im
(
1 −y
x
)
≥0, and hence, b ≥0. Then, we can verify
that the trace and the determinant of the Hesse matrix (69) are positive. Hence, the
Hesse matrix (69) is positive deﬁnite. Therefore, by Lemma 4.7, ˇf has a unique minimal
point and no other critical points, as required.
When t −s > 1
2, putting b′ = −b, we have that b′ > 0. Since any critical point of ˇf is
in the domain (72) by Lemma 4.6 below, it is suﬃcient (by Lemma 4.7) to show that the
Hesse matrix (69) is positive deﬁnite in the domain (72). Hence, it is suﬃcient to show
that
(
the trace of (69)
)
= 4π(a1 + a2 −b′) > 0,
(70)
(
the determinant of (69)
)
= 4π2(
(2a1 −b′)(2a2 −b′) −b′2)
= 8π2a1a2b′( 2
b′ −1
a1
−1
a2
)
> 0.
(71)
We show that (71) ⇒(70), as follows. Suppose that (71) holds. Then, 1
b′ > 1
2
( 1
a1 + 1
a2
)
.
Since a1, a2 and b′ are positive, 1
b′ >
1
a1 or 1
b′ >
1
a2. Hence, b′ < a1 or b′ < a2. Therefore,
(70) holds.
We show (71), as follows. Since x = e2π√−1 (t+X√−1), a1 is presented by
a1 = −Im
1
1 −x = −Im 1 −x

1 −x

2 = −
e−2πX sin 2πt
(1 −e2π√−1 te−2πX)(1 −e−2π√−1 te−2πX)
= −
sin 2πt
e2πX + e−2πX −2 cos 2πt =
sin 2π(1 −t)
e2πX + e−2πX −2 cos 2π(1 −t) .
Hence,
1
a1
= e2πX + e−2πX −2 cos 2π(1 −t)
sin 2π(1 −t)
.
Similarly, we have that
1
a2
= e2πY + e−2πY −2 cos 2πs
sin 2πs
,
1
b′ = e2π(X−Y ) + e2π(Y −X) −2 cos 2π(1 −t + s)
sin 2π(1 −t + s)
.
39
Therefore, the diﬀerential of 2
b′ −1
a1 −1
a2 with respect to X is given by
1
2π · ∂
∂X
( 2
b′ −1
a1
−1
a2
)
= 2 · e2π(X−Y ) −e2π(Y −X)
sin 2π(1 −t + s)
−e2πX −e−2πX
sin 2π(1 −t) .
Since X > 0, Y < 0, 0.33 ≤1 −t + s < 0.5 and 0.1 ≤1 −t ≤0.4,
1
2π · ∂
∂X
( 2
b′ −1
a1
−1
a2
)
>
(
e2πX −e−2πX)(
2
sin 2π(1 −t + s) −
1
sin 2π(1 −t)
)
>
(
e2πX −e−2πX)(
2
sin 2π · 0.33 −max
{
1
sin 2π · 0.1 ,
1
sin 2π · 0.4
})
>
(
e2πX −e−2πX)(
2
0.876307... −max
{
1
0.587785... ,
1
0.587785...
})
>
(
e2πX −e−2πX)
· 0.581004... > 0.
Hence, it is suﬃcient to show the required inequality when X = 0. Similarly, since X > 0,
Y < 0, 0.33 ≤1 −t + s < 0.5 and 0.14 ≤s ≤0.4,
−1
2π · ∂
∂Y
( 2
b′ −1
a1
−1
a2
)
= 2 · e2π(X−Y ) −e2π(Y −X)
sin 2π(1 −t + s)
−e−2πY −e2πY
sin 2πs
>
(
e−2πY −e2πY )(
2
sin 2π(1 −t + s) −
1
sin 2πs
)
>
(
e−2πY −e2πY )(
2
sin 2π · 0.33 −max
{
1
sin 2π · 0.14 ,
1
sin 2π · 0.4
})
>
(
e−2πY −e2πY )(
2
0.876307... −max
{
1
0.770513... ,
1
0.587785...
})
>
(
e−2πY −e2πY )
· 0.581004... > 0.
Hence, it is suﬃcient to show the required inequality when Y = 0. When X = Y = 0,
1
2
( 2
b′ −1
a1
−1
a2
)
= 2 · 1 −cos 2π(1 −t + s)
sin 2π(1 −t + s)
−1 −cos 2π(1 −t)
sin 2π(1 −t)
−1 −cos 2πs
sin 2πs
.
Further, since 1−cos 2πα
sin 2πα
=
2 sin2 πα
2 sin πα cos πα = tan πα,
1
2
( 2
b′ −1
a1
−1
a2
)
= 2 tan π(1 −t + s) −tan π(1 −t) −tan πs > 0.
Hence, we obtain (71), as required.
The following two lemmas are used in the proof of Lemma 4.5.
Lemma 4.6. Let ˇf be as deﬁned in (68). If s < t−1
2 < s+u < 1
2, then any critical point
of ˇf is in the following domain,
{
(X, Y ) ∈R2 

 X > 0,
Y < 0
}
.
(72)
40
Proof. Let (X, Y ) be a critical point of ˇf.
We show that X > 0, as follows. Since
∂ˇf
∂X = 0,
−2 Arg (1 −x) + 2π
(
t −1
2
)
= −Arg
(
1 −y
x
)
,
where x = e2π√−1 (t+X√−1) and y/x = e−2π√−1 (t−s)e2π(X−Y ). Since
1
2 < t −s ≤0.67,
the right-hand side of the above formula is positive. Further, since 0.6 ≤t ≤0.9, the
left-hand side is monotonically increasing with respect to X, and is equal to 0 at X = 0.
Therefore, X > 0.
We show that Y < 0, as follows. Since ∂ˇf
∂Y = 0,
2 Arg (1 −y) = Arg
(
1 −y
x
)
+ 2π
(
2s + u −1
)
,
where y = e2π√−1 (s+Y √−1) and y/x = e−2π√−1 (t−s)e2π(X−Y ). Since Arg
(
1 −y
x
)
< 0 as
mentioned above,
2 Arg (1 −y) < 2π
(
2s + u −1
)
.
Hence,
2 Arg (1 −y) + 2π
(1
2 −s
)
< 2π
(
s + u −1
2
)
.
From the assumption of the lemma, the right-hand side of the above formula is negative.
Further, since 0.14 ≤s ≤0.4, the left-hand side is monotonically increasing with respect
to Y , and is equal to 0 at Y = 0. Therefore, Y < 0.
Lemma 4.7. For each (t, s, u) ∈∆′ satisfying that t −1
2 < s + u,
ˇf(X, Y ) →∞as
X2 + Y 2 →∞.
Proof. From the deﬁnition of ˆV , we have that
Re ˆV
(
t + X
√
−1, s + Y
√
−1, u + Z
√
−1
)
= Re
1
2π√−1
(
−2 Li2(e2π√−1 (t+X√−1)) −Li2(e2π√−1 (s−t+Y √−1−X√−1))
+ 2 Li2(e2π√−1 (s+Y √−1)) + Li2(e2π√−1 (u+Z√−1))
)
+ 2π
(
t −1
2
)
X −2π
(
s −1
2
)
Y −2π
(
s + u −1
2
)
(Y + Z).
Since ˇf is deﬁned from the above formula by ﬁxing Z, it is suﬃcient to show that
Re
1
2π√−1
(
−2 Li2(e2π√−1 (t+X√−1)) + 2 Li2(e2π√−1 (s+Y √−1))
−Li2(e2π√−1 (s−t+Y √−1−X√−1))
)
+ 2π
(
t −1
2
)
X + 2π
(
1 −2s −u
)
Y
41
goes to ∞as X2 + Y 2 →∞. Hence, putting
F(X, Y ) =
( {(
t −1
2
)
X
if X ≥0
−
(
t −1
2
)
X if X < 0
)
+
( {
(1 −2s −u)Y
if Y ≥0
−uY
if Y < 0
)
+
( {(
t −s + 1
2
)
(X −Y ) if X ≥Y
0
if X < Y
)
,
(73)
by Lemma 2.2, it is suﬃcient to show that F(X, Y ) →∞as X2 + Y 2 →∞.
We show that F(X, Y ) →∞as X2 + Y 2 →∞, as follows. As for the ﬁrst summand
of (73), since t > 0.5, this summand goes to ∞as |X| →∞. As for the second summand
of (73), since 1 −2s −u > 0 and u > 0, this summand goes to ∞as |Y | →∞. As for
the third summand of (73), since t −s + 1
2 > 0, this summand is non-negative. Hence,
F(X, Y ) →∞as X2 + Y 2 →∞, as required.
Lemma 4.8. Suppose that t−1
2 ≥s+u, and consider the ﬂow from (X, Y ) = (0, 0) along
the vector ﬁeld
(
−∂ˇf
∂X , −∂ˇf
∂Y
)
. Then, Y →−∞.
Proof. The diﬀerential of ˇf with respect to X is presented by
∂ˇf
∂X =
∂f
∂X = −2 Arg (1 −x) + Arg
(
1 −y
x
)
+ 2π
(
t −1
2
)
,
where x = e2π√−1 (t+X√−1) and y
x = e−2π√−1 (t−s)e2π(X−Y ). In particular, when X = 0,
noting that Arg (1 −x) = π
(
t −1
2
)
,
∂ˇf
∂X

X=0 = Arg
(
1 −y
x
)
< 0,
since 1
2 < t −s ≤0.7. Hence, the ﬂow of the lemma goes in the domain {X > 0}. We
suppose that X > 0 in the following of this proof.
The diﬀerential of ˇf with respect to Y is presented by
∂ˇf
∂Y
=
∂f
∂Y
= 2 Arg (1 −y) −Arg
(
1 −y
x
)
−2π(2s + u −1),
where y = e2π√−1 (s+Y √−1) and y
x = e−2π√−1 (t−s)e2π(X−Y ). Hence,
∂ˇf
∂Y

Y →−∞= −2 · 2π
(1
2 −s
)
+ 2π
(
t −s −1
2
)
−2π(2s + u −1) = 2π
(
t −s −u −1
2
)
≥0.
Further, when Y ≤0, similarly as in the proof of Lemma 4.5, we have that
1
2π · ∂2 ˇf
∂Y 2
= Im
(
2
1 −y −
1
1 −y
x
)
=
2 sin 2πs
e2πY + e−2πY −cos 2πs −
sin 2π(1 −t + s)
e2π(X−Y ) + e2π(Y −X) −cos 2π(1 −t + s)
42
> 2 sin 2πs −sin 2π(1 −t + s)
e2πY + e−2πY −cos 2πs
,
where we obtain the last inequality since 0.14 ≤s ≤1 −t + s < 1
2. Further, since
sin 2πs ≥max
{
sin 2π · 0.14, sin 2π(1 −t + s)
}
= max
{
0.770513... , sin 2π(1 −t + s)
}
> 1
2 sin 2π(1 −t + s),
we have that ∂2 ˇf
∂Y 2 > 0. Hence, ∂ˇf
∂Y is monotonically increasing. Therefore, since ∂ˇf
∂Y

Y →−∞≥
0 as shown above, we have that ∂ˇf
∂Y ≥0. Hence, by the ﬂow of the lemma, Y →−∞.
Lemma 4.9. When we apply Proposition 2.6 to (55), the assumption of Proposition 2.6
holds.
Proof. We show that there exists a homotopy ∆′
δ (0 ≤δ ≤2) between ∆′
0 = ∆′ and ∆′
2
such that
(t0, s0, u0) ∈∆′
2,
(74)
∆′
2 −{(t0, s0, u0)} ⊂
{
(t, s, u) ∈C3 

 Re ˆV (t, s, u) < ςR
}
,
(75)
∂∆′
δ ⊂
{
(t, s, u) ∈C3 

 Re ˆV (t, s, u) < ςR
}
.
(76)
For a suﬃciently large R > 0, we put
ˆg3(t, s, u) =
{
min {R, g3(t, s, u)}
if s + u < 1
2,
R
if s + u ≥1
2,
where g3(t, s, u) is given in Lemma 4.4. We note that, since g3(t, s, u) →∞as s+u →1
2−0,
ˆg3(t, s, u) is continuous. We set the middle part ∆′
1 of the homotopy by
∆′
1 =
{(
t, s, u + ˆg3(t, s, u)
√
−1
)
∈C3 

 (t, s, u) ∈∆′}
.
Further, we deﬁne the internal part ∆′
δ (0 < δ < 1) of the homotopy by setting it along
the ﬂow from (t, s, u) determined by the vector ﬁeld
(
0, 0, −∂f
∂Z
)
. By Lemma 4.4, such a
ﬂow goes to ∆′
1. We note that, when s + u ≥1
2, Re ˆV is suﬃciently small on ∆′
1. It is a
problem how to move ∆′
1 further to make Re ˆV smaller, when s + u < 1
2.
We consider the behavior of the ﬂow from each point of ∆′
1 determined by the vector
ﬁeld
(
−∂ˇf
∂X , −∂ˇf
∂Y , 0
)
. When t −1
2 < s + u, by Lemma 4.5, ˇf has a unique minimal point,
and the ﬂow goes to it; we put this minimal point to be
(
g1(t, s, u), g2(t, s, u)
)
. When
t −1
2 ≥s + u, by Lemma 4.8, Y goes to −∞by the ﬂow. We put
ˆg2(t, s, u) =
{
max {−R, g2(t, s, u)}
if t −1
2 < s + u,
−R
if t −1
2 ≥s + u.
43
We note that, since g2(t, s, u) →−∞as t−s−u →1
2 −0, ˆg2(t, s, u) is continuous. We put
ˆg1(t, s, u) so that
(
ˆg1(t, s, u), ˆg2(t, s, u)
)
is on the ﬂow. We set the ending of the homotopy
by
∆′
2 =
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
δ (1 < δ < 2) of the homotopy by setting it along
the ﬂow from
(
t, s, u + ˆg3(t, s, u)√−1
)
determined by the vector ﬁeld
(
−∂ˇf
∂X , −∂ˇf
∂Y , 0
)
.
We show (76), as follows. From the deﬁnition of ∆′,
∂∆′ ⊂
{
(t, s, u) ∈C3 

 Re ˆV (t, s, u) < ςR
}
.
Further, by the construction of the homotopy, Re ˆV monotonically decreases by the ho-
motopy. Hence, (76) holds.
We show (74) and (75), as follows. Consider the following functions
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
When t −1
2 ≥s + u or s + u ≥1
2, −h(t, s, u) is suﬃciently large (because we let R be
suﬃciently large), and (75) holds in this case. When t −1
2 < s + u < 1
2, similarly as
in the proof of Lemma 3.9, we can show that, if (t, s, u) is a critical point of h(t, s, u),
(
t + g1(t, s, u)√−1, s + g2(t, s, u)√−1, u + g3(t, s, u)√−1
)
is a critical point of ˆV . Hence,
by Lemma 4.2, h(t, s, u) has a unique maximal point at (t, s, u) = (Re t0, Re s0, Re u0).
Therefore, (74) and (75) hold.
5
The 63 knot
In this section, we show Theorem 1.1 for the 63 knot. We give a proof of the theorem in
Section 5.1, using lemmas shown in Section 5.2–5.5.
