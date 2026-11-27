---
doc_id: arxiv-0712.2456v4
doc_title: "Nonlinear Fluid Dynamics from Gravity"
section_id: sec-026-53-solution-in-the-tensor-sector
section_title: "Solution in the tensor sector"
section_number: 5.3
pages: 31-32
source_pdf: 0712.2456v4.pdf
source_sha256: c5fb02c494169403
toc_source: inferred
doc_brief: "Nonlinear Fluid Dynamics from Gravity — Black branes in AdS 5 appear in a four parameter family labeled by their velocity and temperature."
---
Finally, we turn to the tensor modes at second order where we s hall recover the explicit
form of the second order contributions to the stress tensor. Our task is now to determine
the functions α(2)
ij (r) in (5.1). As in § 4.3, in the symmetric traceless sector of SO(3) one
has only the dynamical equation given by
1
2 r
d
dr
[
r5
(
1 − 1
r4
) d
dr α(2)
ij (r)
]
= Aij(r) (5.19)
where
Aij(r) = a1(r)
(
Tij + 1
3Tij + tij
)
+ a5(r) Tij + a6(r) Tij − 1
4 a7(r) Tij
with the coeﬃcient functions
a1(r) = 3 p(r) + 11
p(r) + 5 − 3 r F (r)
a5(r) = 1
2
(
1 + 1
r4
)
a6(r) = 4
r2
r2 p(r) + 3 r2 − r − 1
p(r) + 5 − 6 r F (r)
a7(r) = 2 p(r) + 1
p(r) + 5 − 6 r F (r) .
(5.20)
The functions F (r) and p(r) are deﬁned in (4.20) and (5.17), respectively.
The desired solution to (5.19) can be found by intergrating t he right hand side of the
equation twice and choosing the solution to the homogenous s olution such that we retain
regularity21 at r = 1 and appropriate normalizability at inﬁnity. The solutio n with these
21We have imposed the requirement that all metric functions ar e well behaved in its neighbourhood of
properties is
α(2)
ij (r) = −
∫ ∞
r
dx
x (x4 − 1)
∫ x
1
dy 2 y Aij(y)
The quantity of prime interest to us is the leading large r behaviour of α(2)
ij . This can
be inferred from the expressions for the coeﬃcient function s given in (5.20) and evaluates
to
α(2)
ij (r) = 1
r2
(
−1
2 Tij + Tij − 1
4 Tij
)
+ 1
2r4
[(
1 − ln 2
2
) ( 1
3 Tij + Tij + tij
)
+ ln 2
4 Tij + Tij
] (5.21)
The leading term here will give a divergent contribution to t he stress tensor, which is
necessary to cancel the divergence arising from the expansi on of g(0) + g(1) to second order.
The subleading piece in (5.21) is the term that will provide u s with the second order stress
tensor. Before proceeding to evaluate the stress tensor we p resent the full solution to
second order, appropriately covariantized.
