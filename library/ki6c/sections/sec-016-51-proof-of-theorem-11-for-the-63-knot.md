---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-016-51-proof-of-theorem-11-for-the-63-knot
section_title: "Proof of Theorem 1.1 for the 63 knot"
section_number: 5.1
pages: 44-48
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
Proof of Theorem 1.1 for the 63 knot
In this section, we show a proof of Theorem 1.1 for the 63 knot.
44
The 63 knot is the closure of the following tangle.
0
0
n
0
i
0
0
N −1
j
0
k
1
l
0
0
As shown in [33], we can put the labelings of edges adjacent to the unbounded regions as
shown above. Hence, from the deﬁnition of the Kashaev invariant, the Kashaev invariant
of the 63 knot is presented by
⟨63 ⟩N =
∑
N q
1
2 −n
(q)N−n(q)n−1
×
N q
1
2 +n−i
(q)N−n(q)n−i(q)i−1
×
N q−1
2 −k
(q)N−j(q)j−k−1(q)k
×
N q
1
2 +i−1
(q)j−i(q)i−1(q)N−j
×
N q−1
2 +k−l
(q)k(q)N−l−1(q)l−k
× N q−1
2 +l+1
(q)l(q)N−l−1
=
∑
0<i≤j≤N
0≤k<j
N 4
(q)i−1(q)i−1(q)j−i(q)N−j(q)N−j(q)j−k−1(q)k(q)k
=
∑
0≤i≤j<N
0≤k≤j
N 4
(q)i(q)i(q)j−i(q)N−j−1(q)N−j−1(q)j−k(q)k(q)k
(77)
where the second equality is obtained by (4) and (5), and the last equality is obtained by
replacing i with i + 1 and replacing j with j + 1.
Proof of Theorem 1.1 for the 63 knot. By (6), the above presentation of ⟨63 ⟩N is rewritten
⟨63 ⟩N = N 4
∑
0≤i≤j<N
0≤k≤j
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
φ(t) −φ(1 −t) −φ
(
1 −s + t −1
2N
)
−φ(s) + φ(1 −s)
+ φ
(
s −u + 1
2N
)
+ φ(u) −φ(1 −u) −4 φ
( 1
2N
)
+ 4 φ
(
1 −1
2N
))
45
=
1
N
(
2 φ(t) −φ
(
1 −s + t −1
2N
)
−2 φ(s) + φ
(
s −u + 1
2N
)
+ 2 φ(u)
)
+ 2π
√
−1 · 1
2
(
t2 −s2 + u2 −t + s −u + 1
6
)
−4
N log N.
Here, we obtain the last equality by (10) and (11). Hence, by putting
V (t, s, u) = ˜V (t, s, u) + 4
N log N
=
1
N
(
2 φ(t) −φ
(
1 −s + t −1
2N
)
−2 φ(s) + φ
(
s −u + 1
2N
)
+ 2 φ(u)
)
+ 2π
√
−1 · 1
2
(
t2 −s2 + u2 −t + s −u + 1
6
)
,
the presentation of ⟨63 ⟩N is rewritten
⟨63 ⟩N =
∑
0≤i≤j<N
0≤k≤j
exp
(
N · V
(2i + 1
2N , 2j + 1
2N
, 2k + 1
2N
))
=
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

 0 ≤t ≤s ≤1,
0 ≤u ≤s
}
.
By Proposition 2.1, as N →∞, V (t, s, u) converges to the following ˆV (t, s, u) in the
interior of ∆,
ˆV (t, s, u) =
1
2π√−1
(
2 Li2(e2π√−1 t) −Li2(e−2π√−1 (s−t)) −2 Li2(e2π√−1 s)
+ Li2(e2π√−1 (s−u)) + 2 Li2(e2π√−1 u)
)
+ 2π
√
−1 · 1
2
(
t2 −s2 + u2 −t + s −u + 1
6
)
.
By concrete computation, we can check that the boundary of ∆is included in the domain
{
(t, s, u) ∈∆

 Re ˆV (t, s, u) < ς −ε
}
(78)
for some suﬃciently small ε > 0, where ς is given by (86), noting that ς is real unlike the
cases of the 61 and 62 knots. Hence, similarly as in Section 3.1, we choose a new domain
∆′, which satisﬁes that ∆−∆′ ⊂(78), as
∆′ =
{
(t, s, u) ∈∆

0.18 ≤t ≤0.3,
0.54 ≤s ≤0.7,
0.18 ≤u ≤0.3
0.3 ≤s −t ≤0.47,
0.3 ≤s −u ≤0.47
}
,
(79)
where we calculate the concrete values of the bounds of these inequalities in Section 5.2.
Then, similarly as in Section 3.1, we can restrict ∆to ∆′ as
⟨63 ⟩N = eNς
(
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
, (80)
46
for some ε > 0.
Further, by Proposition 2.3 (Poisson summation formula, see also Remark 2.5), the
above sum is presented by
⟨63 ⟩N = eNς
(
N 3
∫
∆′ exp
(
N · V (t, s, u) −Nς
)
dt ds du + O(e−Nε)
)
,
(81)
noting that we verify the assumption of Proposition 2.3 in Lemma 5.2. Furthermore, by
Proposition 2.6 (saddle point method, see also Remark 2.7), there exist some κ′
i’s such
that
⟨63 ⟩N = N 3 exp
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
for any d > 0, noting that we verify the assumption of Proposition 2.6 in Lemma 5.5.
Here, (tc, sc, uc) is the critical point of V which corresponds to the critical point (t0, s0, u0)
of ˆV of Lemma 5.1, and H is the Hesse matrix of V at (tc, sc, uc).
We calculate the right-hand side of the above formula. Similarly as in Section 3.1, we
have that V (tc, sc, uc) = V (t0, s0, u0)+O(ℏ2). Further, similarly as in Section 4.1, we have
that
φ
(
1 −s0 + t0 −1
2N
)
= φ
(
1 −s0 + t0
)
+ 1
2 log
(
1 −x0
y0
)
+ O(ℏ2),
φ
(
s0 −u0 + 1
2N
)
= φ
(
s0 −u0
)
−1
2 log
(
1 −y0
z0
)
+ O(ℏ2),
where we put x0 = e2π√−1 t0,
y0 = e2π√−1 s0 and z0 = e2π√−1 u0. Hence, by comparing
V (t0, s0, u0) and ˆV (t0, s0, u0) = ς, we have that
V (t0, s0, u0) = ς −1
2N log
(
1 −x0
y0
)
−1
2N log
(
1 −y0
z0
)
+ O(ℏ2).
Therefore, there exist some κi’s such that
⟨63 ⟩N = eNςN 3/2 ω ·
(
1 +
d
∑
i=1
κiℏi + O(ℏd+1)
)
for any d > 0. Here, we put
ω = (2π)3/2(
1 −x0
y0
)−1/2(
1 −y0
z0
)−1/2(
det(−H0)
)−1/2 = 0.416927...
where H0 is the Hesse matrix of ˆV at (t0, s0, u0) whose concrete presentation is given in
(88); see also [22] for a relation of this value and the twisted Reidemeister torsion. Hence,
we obtain the theorem for the 63 knot.
47
