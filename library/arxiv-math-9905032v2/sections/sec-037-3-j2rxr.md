---
doc_id: arxiv-math-9905032v2
doc_title: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS"
section_id: sec-037-3-j2rxr
section_title: "J2r+xr"
section_number: 3
pages: 28-30
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
doc_brief: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
1
3
(2r) − A(x)
⏐
⏐
⏐ = O(r− 1
3 ) , r → ∞ ,(4.6)
moreover, the constant in O(r− 1
3 ) is uniform in x on compact subsets
of R.
Proof. Assume ﬁrst that x ≥ 0. We denote
ν = 2r + xr
1
3 , α = arccosh
(
1 + xr− 2
3 /2
)
≥ 0.
It will be convenient to use the following notation
P = ν(tanh α − α), Q = ν
3 tanh3 α.
The formula 8.43(4) in [39] reads
Jν (2r) = tanh α
π
√
3 eP +QK 1
3
(Q) + 3γ1
ν eP(4.7)
where |γ1| < 1. We have the following estimates as r → +∞
α = x
1
2 r− 1
3 + O(r−1),
tanh α = α + O(α3) = x
1
2 r− 1
3 + O(r−1),
P + Q = ν · O(α5) = O(r− 2
3 ), e P +Q = 1 + O(r− 2
3 ),
Q = 1
3
(
2r + xr
1
3
)(
x
3
2 r−1 + O(r− 4
3 )
)
= 2x
3
2
3 + O(r− 1
3 ),
K 1
3
(Q) = K 1
3
(
2x
3
2
3
)
+ O(r− 1
3 ),
P ≤ 0, 3γ1
ν eP = O(r−1).
Substituting this into (4.7), we obtain the claim (4.6) for x ≥ 0.
ASYMPTOTICS OF PLANCHEREL MEASURES 29
Assume now that x ≤ 0. Denote
ν = 2r + xr
1
3 , β = arccos
(
1 + xr− 2
3 /2
)
≥ 0, y = |x|.
Introduce the notation
~P = ν(tan β − β), ~Q = ν
3 tan3 β .
The formula 8.43 (5) in [39] reads
(4.8) Jν (r) = 1
3 tan β cos
(
~P − ~Q
)[
J− 1
3
(
~Q
)
+ J 1
3
(
~Q
)]
+ 1√
3
tan β sin
(
~P − ~Q
)[
J− 1
3
(
~Q
)
− J 1
3
(
~Q
)]
+ 24γ2
ν
where |γ2| < 1. Again we have the estimates as r → +∞
β = y
1
2 r− 1
3 + O(r−1),
tan β = β + O(β3) = y
1
2 r− 1
3 + O(r−1),
~P − ~Q = ν · O(β5) = O(r− 2
3 ),
cos
(
~P − ~Q
)
= 1 + O(r− 4
3 ), sin
(
~P − ~Q
)
= O(r− 2
3 ),
~Q = 1
3
(
2r − yr
1
3
)(
y
3
2 r−1 + O(r− 4
3 )
)
= 2y
3
2
3 + O(r− 1
3 ),
J± 1
3
(
~Q
)
= J± 1
3
(
2y
3
2
3
)
+ O(r− 1
3 ).
These estimates after substituting into (4.8) produce (4.6 ) for x ≤
0.
Lemma 4.5. There exist C1, C2, C3, ε > 0 such that for any A > 0
and s > 0 we have⏐
⏐
⏐Jr+Ar
1
3 +s(r)
⏐
⏐
⏐ ≤ C1 r− 1
3 exp
(
−C2
(
A
3
2 + sA
1
2 r− 1
3
))
, s ≤ εr ,(4.9)
⏐
⏐
⏐Jr+Ar
1
3 +s(r)
⏐
⏐
⏐ ≤ exp (−C3(r + s)) , s ≥ εr ,(4.10)
for all r ≫ 0.
Proof. First suppose that s ≤ εr. Set ν = r + Ar
1
3 + s. We shall use
(4.7) with α = arccosh( ν/r). Provided ε is chosen small enough and
r is suﬃciently large, α will be close to 0 and we will be able to use
Taylor expansions. For r ≫ 0 we have
α = arccosh(1 + Ar− 2
3 + sr−1) ≥ const (Ar− 2
3 + sr−1)
1
2 ,
