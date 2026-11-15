---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-011-41-proof-of-theorem-11-for-the-62-knot
section_title: "Proof of Theorem 1.1 for the 62 knot"
section_number: 4.1
pages: 26-30
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
Proof of Theorem 1.1 for the 62 knot
In this section, we show a proof of Theorem 1.1 for the 62 knot.
26
The 62 knot is the closure of the following tangle.
0
0
0
i
n
0
j
0
1
N −1
k
0
l
0
0
As shown in [33], we can put the labelings of edges adjacent to the unbounded regions as
shown above. Hence, from the deﬁnition of the Kashaev invariant, the Kashaev invariant
of the 62 knot is presented by
⟨62 ⟩N =
∑
N q−1
2
(q)N−n(q)n−1
×
N q
1
2 −i
(q)N−i(q)i−j−1(q)j
×
N q−1
2 +i
(q)i−n(q)n−1(q)N−i
×
N q
1
2
(q)j(q)N−k−1(q)k−j
×
N q
1
2
(q)k(q)N−l−1(q)l−k
×
N q
1
2
(q)l(q)N−l−1
=
∑
0≤j<i≤N
j≤k<N
N 4 q
(q)N−i(q)N−i(q)i−j−1(q)j(q)j(q)k−j(q)k(q)N−k−1
=
∑
0≤j≤i<N
0≤k<N−j
N 4 q
(q)N−i−1(q)N−i−1(q)i−j(q)j(q)j(q)k(q)j+k(q)N−j−k−1
(51)
where the second equality is obtained by (4) and (5), and the last equality is obtained by
replacing i with i + 1 and replacing k with j + k.
Proof of Theorem 1.1 for the 62 knot. By (6), the above presentation of ⟨62 ⟩N is rewritten
⟨62 ⟩N = N 4 q
∑
0≤j≤i<N
0≤k<N−j
exp
(
N ˜V
(2i + 1
2N , 2j + 1
2N
, 2k + 1
2N
))
,
where we put
˜V (t, s, u) =
1
N
(
φ(1 −t) −φ(t) −φ
(
1 −t + s −1
2N
)
+ φ(s) −φ(1 −s) + φ(u)
−φ
(
1 −s −u + 1
2N
)
−φ
(
s + u −1
2N
)
−3 φ
( 1
2N
)
+ 5 φ
(
1 −1
2N
))
27
=
1
N
(
−2 φ(t) −φ
(
1 −t + s −1
2N
)
+ 2 φ(s) + φ(u)
)
−4
N log N
+
1
2π√−1 · π2
3 + π√−1
2N
−π√−1
6N 2
+ 2π
√
−1 · 1
2
(
−t2 + s2 +
(
s + u −1
2N
)2 + t −2s −u + 1
6 + 1
2N −
1
12N 2
)
.
Here, we obtain the last equality by (10) and (11). Hence, by putting
V (t, s, u) = ˜V (t, s, u) + 4
N log N
=
1
N
(
−2 φ(t) −φ
(
1 −t + s −1
2N
)
+ 2 φ(s) + φ(u)
)
+
1
2π√−1 · π2
3 + π√−1
2N
−π√−1
6N 2
+ 2π
√
−1 · 1
2
(
−t2 + s2 +
(
s + u −1
2N
)2 + t −2s −u + 1
6 + 1
2N −
1
12N 2
)
,
the presentation of ⟨62 ⟩N is rewritten
⟨62 ⟩N = q
∑
0≤j≤i<N
0≤k<N−j
exp
(
N · V
(2i + 1
2N , 2j + 1
2N
, 2k + 1
2N
))
= q
∑
i,j,k ∈Z
( 2i+1
2N , 2j+1
2N , 2k+1
2N )∈∆
exp
(
N · V
(2i + 1
2N , 2j + 1
2N
, 2k + 1
2N
))
,
where the range ∆of (2i+1
2N , 2j+1
2N , 2k+1
2N ) of the above sum is given by the following domain,
∆=
{
(t, s, u) ∈R3 

 0 ≤s ≤t ≤1,
0 ≤u ≤1 −s
}
.
By Proposition 2.1, as N →∞, V (t, s, u) converges to the following ˆV (t, s, u) in the
interior of ∆,
ˆV (t, s, u) =
1
2π√−1
(
−2 Li2(e2π√−1 t) −Li2(e2π√−1 (s−t))
+ 2 Li2(e2π√−1 s) + Li2(e2π√−1 u) + π2
3
)
+ 2π
√
−1 · 1
2
(
−t2 + s2 + (s + u)2 + t −s −(s + u) + 1
6
)
.
By concrete computation, we can check that the boundary of ∆is included in the domain
{
(t, s, u) ∈∆

 Re ˆV (t, s, u) < ςR −ε
}
(52)
for some suﬃciently small ε > 0, where we put ςR = 0.700414... as in (63); we will know
later that this value is equal to the real part of the critical value of ˆV at the critical point
28
of Lemma 4.2. Hence, similarly as in Section 3.1, we choose a new domain ∆′, which
satisﬁes that ∆−∆′ ⊂(52), as
∆′ =
{
(t, s, u) ∈∆

0.6 ≤t ≤0.86,
0.14 ≤s ≤0.4,
0.05 ≤u ≤0.4,
0.3 ≤t −s ≤0.67,
2s + u ≤0.97
}
,
(53)
where we calculate the concrete values of the bounds of these inequalities in Section 4.2.
Then, similarly as in Section 3.1, we can restrict ∆to ∆′ as
⟨62 ⟩N = eNς
(
q
∑
i,j,k ∈Z
( 2i+1
2N , 2j+1
2N , 2k+1
2N )∈∆′
exp
(
N · V
(2i + 1
2N , 2j + 1
2N
, 2k + 1
2N
)
−Nς
)
+ O(e−Nε)
)
, (54)
for some ε > 0.
Further, by Proposition 2.3 (Poisson summation formula, see also Remark 2.5), the
above sum is presented by
⟨62 ⟩N = eNς
(
N 3q
∫
∆′ exp
(
N · V (t, s, u) −Nς
)
dt ds du + O(e−Nε)
)
,
(55)
noting that we verify the assumption of Proposition 2.3 in Lemma 4.3. Furthermore, by
Proposition 2.6 (saddle point method, see also Remark 2.7), there exist some κ′
i’s such
that
⟨62 ⟩N = N 3q exp
(
N · V (tc, sc, uc)
)
· (2π)3/2
N 3/2
(
det(−H)
)−1/2(
1 +
d
∑
i=1
κ′
iℏi + O(ℏd+1)
)
,
for any d > 0, noting that we verify the assumption of Proposition 2.6 in Lemma 4.9.
Here, (tc, sc, uc) is the critical point of V which corresponds to the critical point (t0, s0, u0)
of ˆV of Lemma 4.2, and H is the Hesse matrix of V at (tc, sc, uc).
We calculate the right-hand side of the above formula. Similarly as in Section 3.1, we
have that V (tc, sc, uc) = V (t0, s0, u0) + O(ℏ2). Further,
φ
(
1 −t0 + s0 −1
2N
)
= φ
(
1 −t0 + s0
)
−φ′(
1 −t0 + s0
)
· 1
2N + O(ℏ2)
= φ
(
1 −t0 + s0
)
+ 1
2 log
(
1 −y0
x0
)
+ O(ℏ2),
where we put x0 = e2π√−1 t0 and y0 = e2π√−1 s0. Hence, by comparing V (t0, s0, u0) and
ˆV (t0, s0, u0) = ς, we have that
V (t0, s0, u0) = ς + π√−1
2N
−1
2N log
(
1 −y0
x0
)
−2π√−1
2N
(
s0 + u0 −1
2
)
+ O(ℏ2).
Therefore, there exist some κi’s such that
⟨62 ⟩N = eNςN 3/2 ω ·
(
1 +
d
∑
i=1
κiℏi + O(ℏd+1)
)
,
29
for any d > 0. Here, we put
ω = (2π)3/2√
−1
(
1 −y0
x0
)−1/2(
−y0z0
)−1/2(
det(−H0)
)−1/2
= −0.42920... + √−1 · 0.20337... ,
where we put z0 = e2π√−1 u0, and H0 is the Hesse matrix of ˆV at (t0, s0, u0) whose concrete
presentation is given in (64); see also [22] for a relation of this value and the twisted
Reidemeister torsion. Hence, we obtain the theorem for the 62 knot.
