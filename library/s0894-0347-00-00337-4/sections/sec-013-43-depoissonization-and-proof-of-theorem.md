---
doc_id: s0894-0347-00-00337-4
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4"
section_id: sec-013-43-depoissonization-and-proof-of-theorem
section_title: "Depoissonization and proof of Theorem ??"
section_number: 4.3
pages: 26-28
source_pdf: S0894-0347-00-00337-4.pdf
source_sha256: 1c6848281fc2804c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4 — 22 sections: Front matter; Plancherel measures; Introduction"
---
denote by Fn the distribution function of λ1, . . . , λm under the Plancherel measure
Mn,
Fn(x1, . . . , xm) = Mn ({λ | λi < xi , 1 ≤i ≤m}) .
ASYMPTOTICS OF PLANCHEREL MEASURES
507
Also, set
F(θ, x) = e−θ
∞
X
k=0
θk
k! Fk(x).
This is the distribution function corresponding to the measure M θ.
The measures Mn can be obtained as distribution at time n of a certain random
growth process of a Young diagram; see e.g. [42]. This implies that
Fn+1(x) ≤Fn(x) ,
x ∈Rm .
Also, by construction, Fn is monotone in x and similarly
F(θ, x) ≤F(θ, y) ,
xi ≤yi ,
i = 1, . . . , m .
(4.17)
We shall use these monotonicity properties together with the following lemma.
Lemma 4.7 (Johansson, [16]). There exist constants C > 0 and n0 > 0 such that
for any nonincreasing sequence {bn}∞
n=0 ⊂[0, 1],
1 ≥b0 ≥b1 ≥b2 ≥b3 ≥· · · ≥0,
and its exponential generating function
B(θ) = e−θ
∞
X
k=0
θk
k! · bk
we have for all n > n0 the following inequalities:
B(n + 4
√
n ln n) −C
n2 ≤bn ≤B(n −4
√
n ln n) + C
n2 .
This lemma implies that for all x ∈Rm
F(n + 4
√
n ln n, x) −C
n2 ≤Fn(x) ≤F(n −4
√
n ln n, x) + C
n2 .
(4.18)
Set
¯1 = (1, . . . , 1) .
Theorem 5 asserts that
F

θ, 2θ
1
2 ¯1 + θ
1
6 x

→F(x),
θ →+∞,
x ∈Rm,
(4.19)
where F(x) is the corresponding distribution function for the Airy ensemble. Note
that F(x) is continuous.
Denote n± = n ± 4
√
n ln n. Then for i = 1, . . . , m
2n
1
2
± + n
1
6
± xi = 2n
1
2 + n
1
6 xi + O((ln n)1/2) .
Hence, for any ε > 0 and all suﬃciently large n we have
2n
1
2
+ + n
1
6
+ (xi −ε) ≤2n
1
2 + n
1
6 xi ≤2n
1
2
−+ n
1
6
−(xi + ε) ,
for i = 1, . . . , m. By (4.17) this implies that
F

n+, 2n
1
2 ¯1 + n
1
6 x

≥F

n+, 2n
1
2
+ ¯1 + n
1
6
+ (x −ε ¯1)

,
F

n−, 2n
1
2 ¯1 + n
1
6 x

≤F

n−, 2n
1
2
−¯1 + n
1
6
−(x + ε ¯1)

.
508
A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI
From this and (4.18) we obtain
F

n+, 2n
1
2
+ ¯1 + n
1
6
+ (x −ε ¯1)

−C
n2
≤Fn

2n
1
2 ¯1 + n
1
6 x

≤F

n−, 2n
1
2
−¯1 + n
1
6
−(x + ε ¯1)

+ C
n2 .
From this and (4.19) we conclude that
F (x −ε ¯1) + o(1) ≤Fn

2n
1
2 ¯1 + n
1
6 x

≤F (x + ε ¯1) + o(1)
as n →∞. Since ε > 0 is arbitrary and F(x) is continuous we obtain
Fn

2n
1
2 ¯1 + n
1
6 x

→F(x),
n →∞,
x ∈Rm,
which is the statement of Theorem 4.
