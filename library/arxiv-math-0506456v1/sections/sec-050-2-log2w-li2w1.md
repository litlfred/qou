---
doc_id: arxiv-math-0506456v1
doc_title: "Journal of Knot Theory and Its Ramiﬁcations c© W orld Scientiﬁc Publishing Company ASYMPTOTICS OF THE QUANTUM INV ARIANTS FOR SURGERIES ON THE FIGURE 8 KNOT JØRGEN ELLEGAARD ANDERS"
section_id: sec-050-2-log2w-li2w1
section_title: "Log2(−|w|) − Li2(|w|−1),"
section_number: 2
pages: 63-65
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
64 Asymptotics of the quantum invariants for the ﬁgure 8 knot
where Log( −|w|) = Log( |w|) +iπ, so
Li2(|w|) = π2
2 − π2
6 − 1
2 Log2(|w|) − Li2(|w|−1) −iπLog(|w|).
But then
Li2(|w|) − Li2(|w|−1) = π2
2 − π2
6 − 1
2 Log2(|w|) − 2Li2(|w|−1) −iπLog(|w|).
Here |w|−1 = 3−
√
5
2 by (C.7) so by (C.8) and (C.9) we get
Li2(|w|) − Li2(|w|−1) = π2
2 − π2
6 − 2π2
15 −iπLog(|w|) = π2
5 −iπLog(|w|).
By (C.7) we conclude that
Li2(|w±|) − Li2(|w±|−1) = ∓π2
5 −iπLog(|w±|). (C.10)
Forw =w± we therefore get
Ψ(x,y ) = ab ± 1
4 ∓ 1
20 =ab ± 1
5.
Note here that we use the identities (C.5) and (C.10) in the proof of T heorem 8 to
handle the cases θ = ±1/4, so we can not here refer to this theorem.
We have above shown that the set of values mod Z of Ψ a,b
0 in its critical points
is identical with the set (C.4) of Chern–Simons invariants of ﬂat SU(2 )–connections
onM0 for arbitrary a,b ∈ Z. The determinant of the Hessian H of Ψ a,b
0 in a critical
point (x,y ) is given by
det(H) = 1 − 2
(
z + 1
z
)
according to (4.49). Thus all the critical points are non-degenera te. It is interest-
ing to note that to obtain the leading order large r asymptotics of τr(M0) using
the saddle point method we have to use critical points correspondin g to SL(2,C )–
representations of π1(M0) which are not equivalent to SU(2)–representations in
order to get the part of that leading asymptotics being associated to the reducible
ﬂat SU(2)–connections on M0. By Conjecture 3 this phenomenon should only occur
for p/q = 0. Recall here that the case p/q = 0 is in any case special; only in that
case the moduli space of reducible ﬂat SU(2)–connections on Mp/q is not discrete.
For (z,w ) =
(
−1, −3±
√
5
2
)
we see that det( H) = 5. Moreover, z = e2πix = −1
implies that x ∈ 1
2 + Z, so sin( πx) = ±1. Thus we see that the right-hand side of
the formula (1.11) gives the part of the leading order large r asymptotics of τr(M0)
corresponding to the irreducible ﬂat SU(2)–connections on M0 if we let m ¯ρ = 4 for
both points in M′
0.
Asymptotics of the quantum invariants for the ﬁgure 8 knot 65
The identity (C.10) was proved by using the explicit value of the dilogar ithm in
(3 −
√
5)/2, cf. (C.8). We note that only very few explicit values of the dilogarit m
are known, see [21, Chap 1].
Appendix D Proof of Lemma 8
Let us begin by showing the identitites (5.83) and (5.85). Let θ ∈ I and let u =
u±(θ), Qi =Q±
i (θ) and t =e4πiθ and get
Q1Q2 =
(
1 − (1 +u)−1t
)
(1 − (1 +u)t) = 1 −t
(
1 +u + (1 +u)−1)
+t2
= −t(1 +u)−1(
(1 +u)2 − (t +t−1)(u + 1) + 1
)
=t,
where the last equality follows by the fact that φ(t,u ) = 0, where φ is given by
(5.61).
To show (5.85) we observe that
Q1Q3
Q2
= Q3Q2
1
Q1Q2
=t−1Q3Q2
1
= t−1(1 +u)
(
1 −t(1 +u)−1) 2
=t−1(1 +u) +t(1 +u)−1 − 2
by (5.83). Now φ(t,u ) = 0 implies that
t(1 +u)−1 =t2 + 1 −t −t(u + 1)
leading to the identity
Q1Q3
Q2
= −1 +t−1 − 2t +t2 +u(t−1 −t) = L±(θ).
To prove the identities (5.82) and (5.84) it is necessary to examine th e arguments
of the functions Q±
i (θ), i = 1, 2. By Lemma 9 we note that
Q±
