---
doc_id: arxiv-0712.2456v4
doc_title: "Nonlinear Fluid Dynamics from Gravity"
section_id: sec-025-52-solution-in-the-vector-sector
section_title: "Solution in the vector sector"
section_number: 5.2
pages: 30-31
source_pdf: 0712.2456v4.pdf
source_sha256: c5fb02c494169403
toc_source: inferred
doc_brief: "Nonlinear Fluid Dynamics from Gravity — Black branes in AdS 5 appear in a four parameter family labeled by their velocity and temperature."
---
The analysis of the vector ﬂuctuations at second order mimic s the computation described
in § 4.2. The vector ﬂuctuation in g(2) is chosen as described in (5.1) to be
g(2)
vi = j(2)
i
r2 . (5.12)
Once again, the analysis is easily done by looking at the cons traint equations which are
obtained by contracting the tensor EM N with the vector dual to dr. The ith constraint
equation evaluates to
18 ∂ib(1) = 5 vi + 5 vi + 15 Vi − 15
4 Vi − 33
2 Vi . (5.13)
This equation allows us to solve for the spatial derivatives of b(1) in terms of derivatives of
β(0)
i and b(0). (5.13) is simply the expansion to second order in derivativ es of the conserva-
tion of momentum of the stress tensor (4.26).
To complete the solution in the vector channel, we need to sol ve for j(2)(r), which can
be shown to satisfy a dynamical equation
d
dr
( 1
r3
d
dr j(2)
i (r)
)
= Bi(r). (5.14)
Note that the LHS of this expression has the vector part of the operator H acting on j(2).
Here Bi(r) is the source term which is built out of the second derivativ e terms transforming
in the 3 of SO(3) given in Table 1.
B(r) = p(r) B∞ + Bﬁn
18 r3 (r + 1) ( r2 + 1) (5.15)
with
B∞ = 4 (10 v + v + 3 V − 3 V − 6 V)
Bﬁn = 9 (20 v − 5 V − 6 V) , (5.16)
and we have introduced the polynomial:
p(r) = 2 r3 + 2r2 + 2 r − 3 . (5.17)
Clearly p(r) determines the large r behaviour of the vector perturbation; asymptotically
B(r) → 1
9 r3 B∞. Hence, integrating (5.14) we ﬁnd that j(2)(r) is given as
j(2)
i (r) = − r2
36 B∞
i +
∫ ∞
r
dx x 3
∫ ∞
x
dy
(
Bi(y) − 1
9 y3 B∞
i
)
, (5.18)
where once again we have chosen the coeﬃcients of homogeneou s modes in order to main-
tain normalizability and our renormalization condition. A s with the ﬁrst order computation
described in § 4.2, the solution (5.18) makes no contribution to the stress tensor of the ﬁeld
theory.
