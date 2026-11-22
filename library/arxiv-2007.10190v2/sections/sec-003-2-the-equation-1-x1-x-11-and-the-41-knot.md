---
doc_id: arxiv-2007.10190v2
doc_title: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS"
section_id: sec-003-2-the-equation-1-x1-x-11-and-the-41-knot
section_title: "The equation (1-x)(1-x-1)=1 and the 41 knot"
section_number: 2
pages: 4-5
source_pdf: 2007.10190v2.pdf
source_sha256: 37bcbd3a343bb21a
toc_source: outline
doc_brief: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS — The asymptotic expansion of quantum knot invariants in complex Chern-Simons theory gives rise to factorially divergent formal power series."
---
The state integral of the 41 knot is given by Equation (39) below with (A, B) = (1, 2) and
µ = λ = 0. The critical points of the integrand are solutions of the algebraic equation
(1 −x)(1 −x−1) = 1.
(7)
The latter has two solutions ξ1 = e2πi/6 and ξ2 = e−2πi/6 which lie in the number ﬁeld
Q(√−3), the trace ﬁeld of the 41 knot. The corresponding series Φσj(τ) satisfy the relation
Φσ2(τ) = iΦσ1(−τ) and the ﬁrst few terms of ϕσ1(τ/(2πi)) ∈3−1/4Q(√−3)[[τ]] are given by
ϕσ1
 τ
2πi

=
1
4√
3

1 +
11τ
72√−3 +
697τ 2
2 (72√−3)2 +
724351τ 3
30 (72√−3)3 + · · ·

.
(8)
The exponent in (3) involves the hyperbolic volume of the 41 knot complement
V (σ1) = V = 2Im Li2(eiπ/3) = 2.029883 . . . .
(9)
The two series Φσj(τ) for j = 1, 2 form a vector
Φ(τ) =

Φσ1(τ)
Φσ2(τ)

(10)
that also appears in the reﬁned quantum modularity conjecture [GZc]. Φ(τ) is the vector of
series whose description in Borel plane we wish to give.
Consider the linear q-diﬀerence equation
ym+1(q) −(2 −qm)ym(q) + ym−1(q) = 0
(m ∈Z) .
(11)
THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS
5
It has a fundamental solution set given by the columns of the following matrix
Wm(q) =

G0
m(q)
G1
m(q)
G0
m+1(q)
G1
m+1(q)

,
(12)
where G0
m(q) and G1
m(q) are deﬁned by
G0
m(q) =
∞
X
n=0
(−1)nqn(n+1)/2+mn
(q; q)2
n
(13a)
G1
m(q) =
∞
X
n=0
(−1)nqn(n+1)/2+mn
(q; q)2
n
 
2m + E1(q) + 2
n
X
j=1
1 + qj
1 −qj
!
,
(13b)
and E1(q) = 1 −4 P∞
n=1 qn/(1 −qn) is the Eisenstein series.
It is easy to see that G0
m satisﬁes (11). Indeed, G0
m(q) = P∞
n=0 an,−m(q)−1 where an,m(q)
is given in (34) below. Equations (35a)-(35c), applied to an,−m(q)−1 conclude the result. A
similar proof applies for G1
m. Another way to do so is to use the state integral (39) (with
(A, B) = (1, 2)) and show that the latter satisﬁes the linear q-diﬀerence equation (11) in two
ways, one with respect to the variable λ and another with respect to the variable µ.
The fundamental solution Wm(q) satisﬁes
det(Wm(q)) = 2
(14)
and the symmetry
Wm(q−1) = W−m(q)

1
0
0
−1

,
(15)
and the orthogonality
1
2Wm(q)

0
1
−1
0

Wm(q)T =

0
1
−1
0

.
(16)
for all integers m, as well as
1
2Wm(q)

0
1
−1
0

Wℓ(q)T ∈SL(2, Z[q, 1/q])
(17)
for all integers m, ℓ. The S matrix is given by
S+(q) = 1
2

0
1
1
1

W−1(q)

0
1
1
0

W−1(q)T

0
−1
1
2

,
(18a)
S−(q) = 1
2

−1
−1
0
1

W−1(q)

0
1
1
0

W−1(q)T

1
0
−2
1

.
(18b)
The above matrix S satisﬁes Equation (4).
