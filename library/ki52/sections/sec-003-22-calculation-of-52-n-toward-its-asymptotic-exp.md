---
doc_id: ki52
doc_title: "On the asymptotic expansion of the Kashaev invariant of the 5 2 knot Tomotada Ohtsuki Introduction"
section_id: sec-003-22-calculation-of-52-n-toward-its-asymptotic-exp
section_title: "Calculation of ⟨52 ⟩N toward its asymptotic expansion"
section_number: 2.2
pages: 7-10
source_pdf: ki52.pdf
source_sha256: 35ad4ee5a00d4a18
toc_source: inferred
doc_brief: "On the asymptotic expansion of the Kashaev invariant of the 5_2 knot — We give a presentation of the asymptotic expansion of the Kas haev invariant of the52 knot."
duplicate_of: "104171-qt-83"
---
Calculation of ⟨52 ⟩N toward its asymptotic expansion
In this section, we continue to calculate the value of the Kashaev invariant ⟨52 ⟩N of the
52 knot toward its asymptotic expansion.
To calculate the asymptotic expansion of ⟨52 ⟩N, we review an integral expression of
(q)n. It is known [8, 40] that
(q)n = exp
(
φ
( 1
2N
)
−φ
(2n + 1
2N
))
,
(q)n = exp
(
φ
(
1 −2n + 1
2N
)
−φ
(
1 −1
2N
))
.
(8)
Here, following Faddeev [6], we deﬁne a holomorphic function φ(t) on {t ∈C | 0 < Re t <
1} by
φ(t) =
∫∞
−∞
e(2t−1)xdx
4x sinh x sinh(x/N) ,
noting that this integrand has poles at nπ√−1 (n ∈Z), where, to avoid the pole at 0, we
choose the following contour of the integral,
γ = (−∞, −1 ] ∪
{
z ∈C

 |z| = 1, Im z ≥0
}
∪[ 1, ∞).
We review some properties of φ(t) in Appendix A.
7
By using φ(t), we rewrite the presentation (7) of ⟨52 ⟩N by (8) as
⟨52 ⟩N = N 3q
∑
0 ≤i,j
i+j < N
exp
(
N · ˜V
(2i + 1
2N , 2j + 1
2N
))
,
where we put
˜V (t, s) =
1
N
(
φ
(
t + s −1
2N
)
+ φ
(
1 −t −s + 1
2N
)
+ φ(s) −φ(1 −s)
−φ(1 −t) −3 φ
( 1
2N
)
+ 2 φ
(
1 −1
2N
))
=
1
N
(
−φ(1 −t) −2 φ(1 −s)
)
−
1
2π√−1
π2
6
−2π
√
−1
(1
2
(
t + s −1
2N
)2 + 1
2s2 −1
2t −s + 1
6
)
−5
2N log N −3π√−1
4N
+ π√−1
4N 2 .
Here, we obtain the second equality by Lemmas A.2 and A.3. Hence, by putting
V (t, s) = ˜V (t, s) + 5
2N log N
=
1
N
(
−φ(1 −t) −2 φ(1 −s)
)
−
1
2π√−1
π2
6
−2π
√
−1
(1
2
(
t + s −1
2N
)2 + 1
2s2 −1
2t −s + 1
6
)
−3π√−1
4N
+ π√−1
4N 2 ,
the presentation of ⟨52 ⟩N is rewritten
⟨52 ⟩N = N 1/2 q
∑
0 ≤i,j
i+j < N
exp
(
N · V
(2i + 1
2N , 2j + 1
2N
))
.
(9)
The range of (i/N, j/N) in this sum is given by the following domain,
∆=
{
(t, s) ∈R2 

 0 ≤t,
0 ≤s,
t + s ≤1
}
.
Further, it follows from Proposition A.1 that V (t, s) converges to the following function
as N →∞,
ˆV (t, s) =
1
2π√−1
(
−Li2(e−2π√−1 t) −2 Li2(e−2π√−1 s) −π2
6
)
−2π
√
−1
(1
2t2 + s2 + ts −1
2t −s + 1
6
)
.
(10)
We will show that the asymptotic expansion of (9) is of order eNςR times polynomial
order in N, where ςR is the real part of ς which is given in the introduction,
ςR = Re ς = 0.4501096100... .
8
Hence, we can ignore summands of (9) in the domain where Re ˆV (t, s) ≤ςR −ε, since
they do not contribute to the resulting expansion. Further, as we can see in Figure 1,
Re ˆV (t, s) −ςR is positive only for (t, s) in a particular subdomain of ∆. In the following
lemma, we consider to restrict ∆to a smaller domain ∆′ which includes this subdomain;
this restriction will be used to verify the assumptions of the Poisson summation formula
and the saddle point method later.
0.2
0.4
0.6
0.8
1.0
0.2
0.4
0.6
0.8
1.0
∆
∆′
Figure 1: The domain
{
(t, s)

 Re ˆV (t, s) ≥ςR
}
Lemma 2.1. We put
∆′ =
{
(t, s) ∈∆

 0.04 ≤t ≤0.4, 0.05 ≤s ≤0.4, t + s ≤0.6
}
.
Then, the following domain
{
(t, s) ∈R2 

 Re ˆV (t, s) ≥ςR −ε
}
(11)
is included in ∆′ for some suﬃciently small ε > 0.
We give a proof of the lemma in Appendix D. we can graphically observe the inclusion of
the lemma in Figure 1.
We put
∆′′ =
{
(t, s) ∈∆

 0.04 ≤t ≤0.9, 0.05 ≤s ≤0.9
}
.
(12)
By Lemma B.1, V (t, s) uniformly converges to ˆV (t, s) as N →∞in this domain. By this
uniform convergence, we can restrict ∆′′ to ∆′ later. Before this restriction, we consider
to restrict ∆to ∆′′ in the following calculation of ⟨52 ⟩N.
We consider the value of ⟨52 ⟩N given in (7). The summand of the sum (7) is estimated
by

N 3q
(q)i+j(q)N−i−j−1(q)j(q)j(q)i

 =

N 2
(q)i(q)2
j

 ,
(13)
where we obtain the equality by (3). Since (q)n = (1−qn)(q)n−1 from the deﬁnition of (q)n,
the value of 1/|(q)n| is monotonically increasing with respect to n for 0 ≤n ≤N
6 . Hence,
9
for 0 ≤i ≤0.04 · N and 0 ≤j ≤0.05 · N, the value of (13) is monotonically increasing
with respect to i and j. Further, we can similarly show that, for 0.9 · N ≤i < N and
0.9 · N ≤j < N, the value of (13) is monotonically decreasing with respect to i and j.
Furthermore, since V (t, s) uniformly converges to ˆV (t, s) as N →∞on ∆′′ by Lemma
B.1, Re V (t, s) is bounded by eN(ςR−ε1) for some ε1 > 0 on ∂∆′′ by Lemma 2.1. Hence,
(13) is bounded by the order eN(ςR−ε2) for some ε2 > 0. Therefore, by (7),
⟨52 ⟩N =
∑
i,j∈Z
(i/N,j/N)∈∆′′
N 3q
(q)i+j(q)N−i−j−1(q)j(q)j(q)i
+ O(N 2eN(ςR−ε2)).
Hence, similarly as (9), we have that
⟨52 ⟩N = N 1/2 q
∑
i,j∈Z
(i/N,j/N)∈∆′′
exp
(
N · V
(2i + 1
2N , 2j + 1
2N
))
+ O
(
N 2eN(ςR−ε2))
= eNςN 1/2 q
∑
i,j∈Z
(i/N,j/N)∈∆′′
exp
(
N · V
(2i + 1
2N , 2j + 1
2N
)
−Nς
)
+ O
(
N 2eN(ςR−ε2))
.
By Lemma 2.1, we can restrict ∆′′ to ∆′, where the error term of the sum is estimated
by the order N 2e−Nε. Hence,
⟨52 ⟩N = eNςN 1/2 q
(
∑
i,j∈Z
(i/N,j/N)∈∆′
exp
(
N · V
(2i + 1
2N , 2j + 1
2N
)
−Nς
)
+ O(e−Nε3)
)
, (14)
for some ε3 > 0. Further, by the Poisson summation formula, we will see that the above
sum is expressed by an integral,
⟨52 ⟩N = eNςN 5/2 q
( ∫
∆′ exp
(
N · V (t, s) −Nς
)
dt ds + O(e−Nε4)
)
for some ε4 > 0.
We will analyse this integral in Section 5 using the saddle point method and give the
proof our main Theorem 1.1 there. We will therefore devote the following two sections to
recalling the saddle point method and the Poisson summation formula.
