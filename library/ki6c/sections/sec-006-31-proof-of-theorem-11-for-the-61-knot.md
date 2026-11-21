---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-006-31-proof-of-theorem-11-for-the-61-knot
section_title: "Proof of Theorem 1.1 for the 61 knot"
section_number: 3.1
pages: 12-16
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
Proof of Theorem 1.1 for the 61 knot
In this section, we show a proof of Theorem 1.1 for the 61 knot.
Since the Kashaev invariant of the mirror image of a knot is equal to the complex
conjugate of the Kashaev invariant of the original knot, it is suﬃcient to show the theorem
for the mirror image 61 of the 61 knot. The 61 knot is the closure of the following tangle.
0
0
0
N −1
n
i
j
0
1
k
k−1
0
0
l
0
1
0
(28)
12
As shown in [33], we can put the labelings of edges adjacent to the unbounded regions as
shown above. Hence, from the deﬁnition of the Kashaev invariant, the Kashaev invariant
of the 61 knot is presented by
⟨61 ⟩N =
∑
N q
1
2
(q)N−n−1(q)n
×
N q
1
2 +i
(q)n−i(q)i(q)N−n−1
×
N q−1
2−i
(q)N−j(q)j−i−1(q)i
×
N q−1
2+k
(q)k−j(q)j−1(q)N−k
×
N q−1
2 −k+1
(q)N−l(q)l−k(q)k−1
×
N q−1
2
(q)N−l(q)l−1
=
∑
0≤i<j≤k≤N
N 4 q−1
(q)i(q)i(q)j−i−1(q)j−1(q)N−j(q)k−j(q)k−1(q)N−k
=
∑
0≤i≤j≤k<N
N 4 q−1
(q)i(q)i(q)j−i(q)j(q)N−j−1(q)k−j(q)k(q)N−k−1
=
∑
0 ≤i,j,k
i+j+k<N
N 4 q−1
(q)i(q)i(q)j(q)i+j(q)N−i−j−1(q)k(q)i+j+k(q)N−i−j−k−1
,
(29)
where the second equality is obtained by (4) and (5), the third equality is obtained by
replacing j and k with j + 1 and k + 1 respectively, and the last equality is obtained by
replacing j and k with i + j and i + j + k respectively.
Proof of Theorem 1.1 for the 61 knot. By (6), the above presentation of ⟨61 ⟩N is rewrit-
ten
⟨61 ⟩N = N 4q−1
∑
0 ≤i,j,k
i+j+k<N
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
φ(t) −φ(1 −t) + φ(s) −φ
(
t + s −1
2N
)
−φ
(
1 −t −s + 1
2N
)
+ φ(u) −φ
(
t + s + u −1
N
)
−φ(1 −t −s −u + 1
N
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
=
1
N
(
2 φ(t) + φ(s) + φ(u)
)
+
1
2π√−1 · π2
3 −4
N log N + π√−1
2N
−π√−1
6N 2
+ 2π
√
−1 · 1
2
((
t+s+u−1
N
)2 +
(
t+s−1
2N
)2 + t2 −3t −2s −u + 1
2 + 3
2N −
1
4N 2
)
.
Here, we obtain the last equality by (10) and (11). Hence, by putting
V (t, s, u) = ˜V (t, s, u) + 4
N log N
13
=
1
N
(
2 φ(t) + φ(s) + φ(u)
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
((
t+s+u−1
N
)2 +
(
t+s−1
2N
)2 + t2 −3t −2s −u + 1
2 + 3
2N −
1
4N 2
)
,
the presentation of ⟨61 ⟩N is rewritten
⟨61 ⟩N = q−1
∑
0 ≤i,j,k
i+j+k<N
exp
(
N · V
(2i + 1
2N , 2j + 1
2N
, 2k + 1
2N
))
= q−1 ∑
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

 0 ≤t, s, u ≤1,
t + s + u ≤1 + 1
N
}
.
By Proposition 2.1, as N →∞, V (t, s, u) converges to the following ˆV (t, s, u) in the
interior of ∆,
ˆV (t, s, u) =
1
2π√−1
(
2 Li2(e2π√−1 t) + Li2(e2π√−1 s) + Li2(e2π√−1 u) + π2
3
)
+ 2π
√
−1 · 1
2
(
(t + s + u)2 + (t + s)2 + t2 −3t −2s −u + 1
2
)
.
By concrete computation, we can check that the boundary of ∆is included in the domain
{
(t, s, u) ∈∆

 Re ˆV (t, s, u) < ςR −ε
}
(30)
for some suﬃciently small ε > 0, where we put ςR = 0.5035603... as in (41); we will know
later that this value is equal to the real part of the critical value of ˆV at the critical point of
Lemma 3.3. Since we will know later that the sum of the problem is of the order O(eNςR),
we can ignore the sum of the problem restricted in the above domain, and hence, we can
remove this domain from ∆; see Appendix D for concrete procedure of this argument.
Therefore, we can choose a new domain ∆′ in the interior of ∆such that ∆−∆′ ⊂(30);
more concretely, we can choose ∆′ as
∆′ =
{
(t, s, u) ∈∆

 0.03 ≤t ≤0.4,
0.001 ≤s ≤0.5,
0.001 ≤u ≤0.5,
t+s+u ≤0.94
}
,
(31)
where we calculate the concrete values of the bounds of these inequalities in Section 3.2.
14
Hence, since ∆−∆′ ⊂(30), we obtain the second equality of the following formula,
⟨61 ⟩N = eNςq−1 ∑
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
)
−Nς
)
= eNς
(
q−1
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
,
(32)
for some ε > 0. To be precise, in order to obtain the second equality, we need to estimate
of the summand of the above sum in terms of ˆV (2i+1
2N , 2j+1
2N , 2k+1
2N ); see Appendix D for the
proof of the equality of (32).
Further, by Proposition 2.3 (Poisson summation formula, see also Remark 2.5), the
above sum is presented by
⟨61 ⟩N = eNς
(
N 3q−1
∫
∆′ exp
(
N · V (t, s, u) −Nς
)
dt ds du + O(e−Nε)
)
,
(33)
noting that we verify the assumption of Proposition 2.3 in Lemma 3.4. Furthermore, by
Proposition 2.6 (saddle point method, see also Remark 2.7), there exist some κ′
i’s such
that
⟨61 ⟩N = N 3q−1 exp
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
for any d > 0, noting that we verify the assumption of Proposition 2.6 in Lemma 3.9.
Here, (tc, sc, uc) is the critical point of V which corresponds to the critical point (t0, s0, u0)
of ˆV of Lemma 3.3, and H is the Hesse matrix of V at (tc, sc, uc).
We calculate the right-hand side of the above formula. Since tc = t0 + O(ℏ), sc =
s0 + O(ℏ) and uc = u0 + O(ℏ), we have that V (tc, sc, uc) = V (t0, s0, u0) + O(ℏ2). Further,
by comparing V (t0, s0, u0) and ˆV (t0, s0, u0) = ς, we have that
V (t0, s0, u0) = ς + π√−1
2N
−2π√−1
N
(
t0 + s0 + u0 −1
2
)
−2π√−1
2N
(
t0 + s0 −1
2
)
+ O(ℏ2).
Therefore, there exist some κi’s such that
⟨61 ⟩N = eNςN 3/2 ω ·
(
1 +
d
∑
i=1
κiℏi + O(ℏd+1)
)
,
for any d > 0. Here, we put
ω = (2π)3/2√
−1
(
−x0y0z0
)−1(
−x0y0
)−1/2(
det(−H0)
)−1/2
= −0.52139... + √−1 · 0.071732... ,
where we put x0 = e2π√−1 t0, y0 = e2π√−1 s0, z0 = e2π√−1 u0, and H0 is the Hesse matrix of
ˆV at (t0, s0, u0) whose concrete presentation is given in (42); see also [22] for a relation of
this value and the twisted Reidemeister torsion. Hence, we obtain the theorem for the 61
knot.
15
