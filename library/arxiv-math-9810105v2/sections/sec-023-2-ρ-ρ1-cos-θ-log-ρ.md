---
doc_id: arxiv-math-9810105v2
doc_title: "ON THE DISTRIBUTION OF THE LENGTH OF THE LONGEST INCREASING SUBSEQUENCE OF RANDOM PERMUTATIONS"
section_id: sec-023-2-ρ-ρ1-cos-θ-log-ρ
section_title: "(ρ −ρ−1) cos θ + log ρ,"
section_number: 2
pages: 24-26
source_pdf: 9810105v2.pdf
source_sha256: 0a432946234949c1
doc_brief: "ON THE DISTRIBUTION OF THE LENGTH OF THE LONGEST INCREASING SUBSEQUENCE OF RANDOM PERMUTATIONS — The authors consider the length, lN, of the length of the longest increasing subsequence of a random"
---
(5.4)
LONGEST INCREASING SUBSEQUENCE
25
where z = ρeiθ, 0 < ρ ≤1, has the minimum at
ρ = ρθ ≡1 −
p
1 −γ2 cos2 θ
−γ cos θ
(5.5)
and F(ρθ) < 0. ( Note that ρθ < 0 for |θ| < π/2. ) For 1
2 ≤γ ≤1, we take
Σ(3)
in = {ρθeiθ : 3π/4 ≤|θ| ≤π} ∪{ρ3π/4eiθ : |θ| ≤3π/4},
Σ(3)
out = {ρ−1
θ eiθ : 3π/4 ≤|θ| ≤π} ∪{ρ−1
3π/4eiθ : |θ| ≤3π/4}.
(5.6)
Orient Σ(3) as in Figure 8. And ﬁnally, for 0 ≤γ ≤1
2, set Σ(3)(γ) = Σ(3)( 1
2).
Of course, Σ(3) varies with γ ∈[0, 1]. However, using estimates from [GK], it
is not diﬃcult to show that the Cauchy operators C± on L2(Σ(3)) are uniformly
bounded,
∥C±∥L2(Σ(3))→L2(Σ(3)) ≤C < ∞
(5.7)
for all 0 ≤γ ≤1. Observe also that in the limit γ →1, Σ(3) takes the form of the
cross
y = ±|x + 1|
for z = x + iy near −1.
(5.8)
Apart from the neighborhood of z = −1, there is considerable freedom in the
choice of Σ(3). For example, 3π/4 could be replaced by any angle between π/2 and
π. Also the form of the contour for |θ| < 3π/4 is not critical, as long as it has the
general shape drawn in Figure 8 : all that we really need is that the jump matrix
v(3) below has the property sup{z∈Σ(3):| arg(z)|<3π/4} |v(3) −I| →0 exponentially as
q →∞.
Using the factorization
v(2) =

1
0
(−1)qz−qe
−qγ
2
(z−z−1)
1
 
1
−(−1)qzqe
qγ
2 (z−z−1)
0
1

≡(b(2)
−)−1b(2)
+ ,
we deﬁne





m(3) = m(2)(b(2)
+ )−1
in
Ω(3)
2 ,
m(3) = m(2)(b(2)
−)−1
in
Ω(3)
3 ,
m(3) = m(2)
in
Ω(3)
1 , Ω(3)
4 .
Then m(3) solves the RHP (Σ(3), v(3)) where











v(3) =
 
1
−(−1)qzqe
qγ
2 (z−z−1)
0
1
!
on
Σ(3)
in ,
v(3) =
 
1
0
(−1)qz−qe
−qγ
2
(z−z−1)
1
!
on
Σ(3)
out,
(5.9)
and
κ2
q−1 = m(3)
22 (0).
(5.10)
As q →∞, v(3)(z) →I. Set Σ∞= Σ(3). The RHP
(
m∞
+ = m∞
−I
on
Σ∞,
m∞= I + O( 1
z)
as
z →∞
(5.11)
26
JINHO BAIK, PERCY DEIFT, AND KURT JOHANSSON
has, of course, the unique solution, m∞(z) ≡I.
Let 0 ≤γ ≤1 −δ1 for some 0 < δ1 < 1. From the choice of Σ(3),
∥v(3) −I∥L∞(Σ(3)) =
sup
3π/4≤θ≤5π/4
|eF (ρθ,θ)| ≤
sup
3π/4≤θ≤5π/4
|eF (ρπ,θ)|
≤eF (ρπ,π) = eq(√
1−γ2+log 1−√
1−γ2
γ
).
(5.12)
But, for 0 < γ ≤1, a straightforward estimate shows that
p
1 −γ2 + log(1 −
p
1 −γ2) −log γ ≤−2
√
2
