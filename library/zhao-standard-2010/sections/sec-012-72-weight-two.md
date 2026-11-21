---
doc_id: zhao-standard-2010
doc_title: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity"
section_id: sec-012-72-weight-two
section_title: "Weight two"
section_number: 7.2
pages: 18-19
source_pdf: Zhao_standard_2010.pdf
source_sha256: 94a70847c2937ba7
toc_source: inferred
doc_brief: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity — Let N be a positive integer."
---
Weight two
There are N 2 MPVs of weight two and level N:
LN(1, 1|i, j),
LN(2|j),
1 ≤i ≤N −1, 0 ≤j ≤N −1.
For 1 ≤i, j < N the FDS Z∗(y1,i ∗y1,j) = Zx(y1,ixy1,j) yields
LN(2|i + j) + LN(1, 1|i, j) + LN(1, 1|j, i) = LN(1, 1|i, j −i) + LN(1, 1|j, i −j).
(21)
Now from RDS ρ(Z∗(y1,0 ∗y1,i)) = Zx(y1,0xy1,i) we get for 1 ≤i < N
LN(1, 1|i, 0) + LN(2|i) = LN(1, 1|i, −i).
(22)
The FDT in (14) yields: for every divisor d of N, and 1 ≤a, b < d′ := N/d
LN(2|ad) =d
d−1
X
j=0
LN(2|a + jd′),
(23)
LN(1, 1|ad, bd) =
d−1
X
j,k=0
LN(1, 1|a + jd′, b + kd′).
(24)
To derive the RDT we can compare the coeﬃcients of x1xµad in (18) and use
Prop. 4.3 to get: for every divisor d of N, and 1 ≤a < d′
LN(1|ad)
d−1
X
j=1
LN(1|jd′) =
d−1
X
j=1
d−1
X
k=0
LN(1, 1|jd′, a + kd′)
−
d−1
X
k=0
LN(1, 1|a + kd′, −a −kd′) −LN(1, 1|ad, −ad).
(25)
By deﬁnition, the weight one relations are obtained from (11) and (12). For
example, if N = p is a prime then (12) is trivial and (11) is equivalent to the
following: for all 1 ≤j < h (h := (p −1)/2)
LN(1|j) −LN(1| −j) = (p −2j)(LN(1|h) −LN(1|h + 1)).
(26)
Thus multiplying by LN(1|i) (1 ≤i < p) and applying the shuﬄe relation
LN(1|a)LN(1|b) = LN(12|a, b −a) + LN(12|b, a −b) (here we put LN(12|−) =
LN(1, 1|−) to save space) we get:
LN(12|i, j −i) + LN(12|j, i −j) −LN(12|i, −j −i) −LN(12| −j, i + j)
= (p−2j)
`
LN(12|i, h−i)+LN(12|h, i−h)−LN(12|i, −i−h)−LN(12|−h, i+h)
´
.
(27)
Documenta Mathematica 15 (2010) 1–34
Relations of Multiple Polylogarithm Values
19
Computation shows that the following conjecture should hold.
Conjecture 7.1. The RDT (25) follows from the combination of the following
relations: the weight one relations, the RDS (21) and (22), and the FDT (23)
and (24).
