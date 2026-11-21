---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-020-55-verifying-the-assumption-of-the-saddle-point
section_title: "Verifying the assumption of the saddle point method"
section_number: 5.5
pages: 53-55
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
Verifying the assumption of the saddle point method
In this section, we verify the assumption of the saddle point method in Lemma 5.5. In
order to show this lemma, we show Lemmas 5.3 and 5.4 in advance. As we mentioned in
Remark 2.7, we verify the assumption for ˆV (t, s, u) instead of V (t, s, u), since V (t, s, u)
converges uniformly to ˆV (t, s, u) on ∆′ in the form mentioned in Remark 2.7.
In the proof of Lemma 5.5, as mentioned at the beginning of Section 5.4, it is suﬃcient
to decrease Re ˆV (t, s, u) by 0.02, by pushing t, s, u into the imaginary directions. In order
to calculate this concretely, putting
f(X, Y, Z) = Re ˆV (t + X
√
−1, s + Y
√
−1, u + Z
√
−1) −ς,
as in Section 3.5, we consider the behavior of f at each ﬁber of the projection C3 →R3.
Lemma 5.3. For each (t, s, u) ∈∆′, f has a unique minimal point and no other critical
points.
53
Proof. By Lemma 5.4, it is suﬃcient to show that the Hesse matrix of f is positive deﬁnite
at any (X, Y, Z) ∈R3. Similarly as in the proof of Lemma 4.5, we have that
∂2f
∂X2 = 2π Im
(
2
1 −x −
1
1 −x
y
)
,
∂2f
∂X ∂Y
= 2π Im
1
1 −x
y
,
∂2f
∂Y 2
= 2π Im
(
−
2
1 −y −
1
1 −x
y
+
1
1 −y
z
)
,
∂2f
∂Y ∂Z = −2π Im
1
1 −y
z
,
∂2f
∂Z2
= 2π Im
(
2
1 −z +
1
1 −y
z
)
,
where x = e2π√−1 (t+X√−1), y = e2π√−1 (s+Y √−1) and z = e2π√−1 (u+Z√−1). Hence, the Hesse
matrix is presented by
2π


a1 + b1
−b1
0
−b1
a2 + b1 + b2
−b2
0
−b2
a3 + b2

,
where we put
a1 = Im
2
1 −x ,
a2 = Im −2
1 −y ,
a3 = Im
2
1 −z ,
b1 = Im −1
1 −x
y
,
b2 = Im
1
1 −y
z
,
noting that these numbers are positive since (t, s, u) ∈∆′. Since the above matrix is
equivalent as a quadratic form to the following matrix,
2π


a1 + b1
0
0
0
a2 +
a1b1
a1+b1 +
a3b2
a3+b2
0
0
0
a3 + b2

,
the Hesse matrix of f is positive deﬁnite, as required.
The following lemma is used in the proof of Lemma 5.3.
Lemma 5.4. For each (t, s, u) ∈∆′, f(X, Y, Z) →∞as X2 + Y 2 + Z2 →∞.
Proof. From the deﬁnition of f, we have that
f(X, Y, Z) = Re
1
2π√−1
(
2 Li2(e2π√−1 (t+X√−1)) −Li2(e2π√−1 (1+t−s)+2π(Y −X))
−2 Li2(e2π√−1 (s+Y √−1)) + Li2(e2π√−1 (s−u)+2π(Z−Y )) + 2 Li2(e2π√−1 (u+Z√−1))
)
−2π
(
t −1
2
)
X + 2π
(
s −1
2
)
Y −2π
(
u −1
2
)
Z −ς.
54
Hence, by Lemma 2.2, putting
F(X, Y, Z) =
( {(1
2 −t
)
X
if X ≥0
−
(1
2 −t
)
X if X < 0
)
+
( {
0
if X ≥Y
(1
2 −s + t
)
(Y −X) if X < Y
)
+
( {(
s −1
2
)
Y
if Y ≥0
−
(
s −1
2
)
Y
if Y < 0
)
+
( {
0
if Y ≥Z
(1
2 −s + u
)
(Z −Y ) if Y < Z
)
+
( {(1
2 −u
)
Z
if X ≥0
−
( 1
2 −u
)
Z if X < 0
)
,
it is suﬃcient to show that F(X, Y, Z) →∞as X2+Y 2+Z2 →∞. Since F(c X, c Y, c Z) =
c F(X, Y, Z) for any c > 0, it is suﬃcient to show that F(X, Y, Z) is positive on the unit
sphere {(X, Y, Z) ∈R3 | X2 + Y 2 + Z2 = 1}.
Note that all of the ﬁve summands in the right-hand side of the formula of F(X, Y, Z)
are non-negative. Further, the ﬁrst summand is positive if X̸ = 0, the third summand
is positive if Y̸ = 0, and the last summand is positive if Z̸ = 0. Hence, F(X, Y, Z) is
positive on the unit sphere, as required.
Lemma 5.5. When we apply Proposition 2.6 to (81), the assumption of Proposition 2.6
holds.
Proof. We show that there exists a homotopy ∆′
δ (0 ≤δ ≤1) between ∆′
0 = ∆′ and ∆′
1
such that
(t0, s0, u0) ∈∆′
1,
(91)
∆′
1 −{(t0, s0, u0)} ⊂
{
(t, s, u) ∈C3 

 Re ˆV (t, s, u) < ς
}
,
(92)
∂∆′
δ ⊂
{
(t, s, u) ∈C3 

 Re ˆV (t, s, u) < ς
}
.
(93)
At each ﬁber of the projection C3 →R3, we consider the behavior of f(X, Y, Z) =
Re ˆV (t + X√−1, s + Y √−1, u + Z√−1) −ς. By Lemma 5.3, f has a unique minimal
point. We put this minimal point to be (X, Y, Z) =
(
g1(t, s, u), g2(t, s, u), g3(t, s, u)
)
. We
deﬁne the ending of the homotopy to be the set of these minimal points,
∆′
1 =
{(
t + g1(t, s, u)
√
−1, s + g2(t, s, u)
√
−1, u + g3(t, s, u)
√
−1
)
∈C3 

 (t, s, u) ∈∆′}
.
Further, we deﬁne the internal part of the homotopy by setting it along the ﬂow from
(t, s, u) determined by the vector ﬁeld
(
−∂f
∂X , −∂f
∂Y , −∂f
∂Z
)
.
We can show (91), (92) and (93) by Lemma 5.1 in a similar way as the proof of Lemma
3.9.
