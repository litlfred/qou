---
doc_id: arxiv-math-9810105v2
doc_title: "ON THE DISTRIBUTION OF THE LENGTH OF THE LONGEST INCREASING SUBSEQUENCE OF RANDOM PERMUTATIONS"
section_id: sec-034-21-0eql-1qeqγlog-γ1m1
section_title: "(0)eql = −(−1)qeq(−γ+log γ+1)m(1)"
section_number: 21
pages: 32-34
source_pdf: 9810105v2.pdf
source_sha256: 0a432946234949c1
doc_brief: "ON THE DISTRIBUTION OF THE LENGTH OF THE LONGEST INCREASING SUBSEQUENCE OF RANDOM PERMUTATIONS — The authors consider the length, lN, of the length of the longest increasing subsequence of a random"
---
21 (0) by (4.10) and (4.14).
We use the same conjugation (5.2) for m(1) as in the case γ ≤1. Then our new
jump matrices for m(2) are
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
v(2) =
 
1
−e−2qα
e2qα
0
!
on C2
v(2) =
 
e−2qα−
−1
1
0
!
on C1
(6.2)
and κ2
q−1 = eq(−γ+log γ+1)m(2)
22 (0).
Set Σ(3) = C1 ∪eCinside ∪eCoutside where eCinside and eCoutside are open arcs as
chosen below. Note the factorization v(2) =
 1
0
e2qα
1
 1
−e−2qα
0
1

on C2. Set
Reα = R, Imα = I so that α = R + iI. Recall the Cauchy-Riemann equations in
polar coordinates (r, θ),
r∂R
∂r = ∂I
∂θ,
r∂I
∂r = −∂R
∂θ .
LONGEST INCREASING SUBSEQUENCE
33
For z = eiθ ∈C2, α(z) = −πi
R θ
θc dµV (θ′) is pure imaginary and
∂I
∂θ = ∂
∂θ(−iα) = −π γ
π cos(θ
2)
s
1
γ −sin2(θ
2) < 0.
Hence
R = 0
and
∂R
∂r = ∂I
∂θ < 0
on
C2.
Therefore for ﬁxed θ, eiθ ∈C2, there is ǫ1 = ǫ1(θ) > 0 such that R = Reα > 0
(resp. < 0) for z = reiθ with 1 −ǫ1 < r < 1 (resp. 1 < r < 1 + ǫ1). We take eCinside
(resp, eCoutside) such that |e−2α| < 1 (resp, |e2α| < 1) on eCinside (resp, eCoutside).
Clearly there exist 0 < ρ1, ρ2 < 1 such that |e−2α| < ρ1 (resp, |e2α| < ρ2), for all
z ∈eCinside (resp, z ∈eCoutside), apart from a small neighborhood of the endpoints.
Introduce the regions Ω(3)
k , k = 1, 2, 3, 4 as in Figure 10. Deﬁne m(3) as follows,















m(3) = m(2)
 
1
−e−2qα
0
1
!−1
in
Ω(3)
2 ,
m(3) = m(2)
 
1
0
e2qα
1
!
in
Ω(3)
3 ,
m(3) = m(2)
in
Ω(3)
1 , Ω(3)
4 .
Then v(3) is given by





















 
1
−e−2qα
0
1
!
on
eCinside,
 
1
0
e2qα
1
!
on
eCoutside,
 
e−2qα−
−1
1
0
!
on
C1,
and
κ2
q−1 = eq(−γ+log γ+1)m(3)
22 (0).
(6.3)
From Lemma 6.1 (iii) and the second variational condition in (4.7), we have, for
any z ∈C1,
e−2qα−→0
as
q →∞.
(Recall that the inequality in (4.7) is strict from Lemma 4.3 (ii)). Also from the
choice of eCinside and eCoutside,
e−2qα →0,
e2qα →0
as
q →∞
on eCinside, eCoutside, respectively. Therefore v(3) →v∞as q →∞,
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
v∞=
 
1
0
0
1
!
on
eCinside ∪eCoutside,
v∞=
 
0
−1
1
0
!
on C1.
(6.4)
The following result can be veriﬁed by direct calculation.
34
JINHO BAIK, PERCY DEIFT, AND KURT JOHANSSON
Lemma 6.2. RHP (C1, v∞) can be solved explicitly.
m∞=

1
2(β + β−1)
1
2i(β −β−1)
−1
2i(β −β−1)
1
2(β + β−1)

(6.5)
where β(z) ≡(
z−ξ
z−ξ−1 )1/4,
is analytic in C −¯C1 such that β ∼+1 as z →∞
Hence we expect from (6.3), κ2
q−1 ∼eq(−γ+log γ+1) 1
√γ , because m∞
22(0) =
1
√γ .
Our goal now is to show that indeed m(3) →m∞as q →∞. As in Section 5, we
must control the behavior of the solution of the RHP for m(3) near the endpoints,
where the rate of exponential convergence v(3) →v∞, becomes smaller and smaller.
Let δ3, M4 > 0 be ﬁxed numbers, let 0 < δ4 < 1 be a ﬁxed, suﬃciently small
number satisfying (6.35) below, and let M3 > 0 be a ﬁxed, suﬃciently large number
satisfying (6.32) and (6.39) below. We consider 3 cases for γ :
1. 1 + δ3 ≤γ
2. 1 +
M3
21/3q2/3 ≤γ ≤1 + δ4
3. 1 ≤γ ≤1 +
M4
21/3q2/3
Calculations similar to those that are needed for the asymptotics of the orthog-
onal polynomial on the real line (see, [DKMVZ1]), show that for γ > 1 + δ3,
κ2
q−1 = eq(−γ+log γ+1) 1
√γ (1 + O(1
q )).
(6.6)
The error is uniform for 1 + δ3 ≤γ ≤L for any ﬁxed L < ∞. However, we will not
use this result, utilizing instead (stronger) estimates from [Jo1] (see next section).
ξ
ξ
−1
−1
u0
-u 0
0
Σ
,
5
Σ2
,
Σ1
,
Σ4
,
3
,
Σ
