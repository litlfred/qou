---
doc_id: arxiv-0712.2456v4
doc_title: "Nonlinear Fluid Dynamics from Gravity"
section_id: sec-024-51-solution-in-the-scalar-sector
section_title: "Solution in the scalar sector"
section_number: 5.1
pages: 28-30
source_pdf: 0712.2456v4.pdf
source_sha256: c5fb02c494169403
toc_source: inferred
doc_brief: "Nonlinear Fluid Dynamics from Gravity — Black branes in AdS 5 appear in a four parameter family labeled by their velocity and temperature."
---
Given the general second order ﬂuctuation (5.1), we paramet erize scalar components of
g(2) in terms of the functions h2(r) and k2(r) according to
g(2)
ii (r) = 3 r2 h2(r)
g(2)
vv (r) = k2(r)
r2
g(2)
vr (r) = −3
2 h2(r) .
(5.4)
As we have explained in the § 4.1, the constraint Einstein’s equations in this sector are
given by the r and v component of the one-form formed by contracting the Einstei n tensor
with the vector dual to the one-form dr. The v component of this constraint, i.e. the
second order expansion of (4.3), evaluates to
1
b(0) ∂vb(1) = 1
b(1) S . (5.5)
This equation enables us to solve for the ﬁrst v derivative of b(1) in terms of two derivative
terms made up of β(0)
i , but imposes no further constraints on b(0), β(0)
i . (5.5) has a simple
physical interpretation; it is simply the time component of the conservation equation for
the stress tensor (4.26), expanded to second order in deriva tives. Consequently (5.5) is the
Navier Stokes equation!
The r component of the constraint, i.e. (4.5), gives us one relation between the functions
h2(r) and k2(r) and their derivatives. As in § 4.1, to this constraint we must add one
dynamical equation. We obtain the following equations
5 h′
2(r) + r h′′
2(r) = Sh(r)
k′
2(r) = Sk(r)
= 12 r3 h2(r) + (3 r4 − 1) h′
2(r) + ˆSk(r) ,
(5.6)
where
Sh(r) ≡ 1
3 r3 S + 1
2 Wh(r) S
ˆSk(r) ≡ − 4 r
3 s + 2 r S − 2 r
9 S + 1 + 2 r4
6 r3 S + 1
2 Wk(r) S .
(5.7)
The functions Wh(r) and Wk(r) are given by
Wh(r) = 4
3
(r2 + r + 1)2 − 2 (3 r2 + 2r + 1) F (r)
r (r + 1)2 (r2 + 1)2 ,
Wk(r) = 2
3
4 ( r2 + r + 1) (3 r4 − 1) F (r) − (2r5 + 2r4 + 2r3 − r − 1)
r (r + 1) ( r2 + 1) .
As advertised, it is clear that the diﬀerential operator act ing on the functions h2(r) and
k2(r) is identical to the one encountered in the ﬁrst order comput ation in § 4.1. The
equation (5.6) can be explicitly integrated; to do so it is us eful to record the leading large
r behaviour of the source term Sh(r):
Sh(r) → 1
r3 S∞
h ≡ 1
r3
( 1
3 S + 2
3 S
)
. (5.8)
The ﬁrst equation in (5.6) can be integrated given this asymp totic value to obtain the
leading behaviour of the function h2(r). One ﬁnds
h2(r) = − 1
4 r2 S∞
h +
∫ ∞
r
dx
x5
∫ ∞
x
dy y 4
(
Sh(y) − 1
y3 S∞
h
)
. (5.9)
The integral expression above can be shown to be of O (r−5) and hence the asymptotic
behaviour of h2(r) is controlled by sh. Given h2(r), one can integrate up the second
equation of (5.6) for k2(r). The leading large r behaviour of the source term Sk(r) is given
by
Sk(r) → r S∞
k ≡ r
(
−4
3 s + 2 S − 2
9 S − 1
6 S + 7
3 S
)
, (5.10)
and hence we have
k2(r) = r2
2 S∞
k −
∫ ∞
r
dx (Sk(x) − x S∞
k ) . (5.11)
In this case the integral makes a subleading contribution st arting at O (r−1). As in § 4.1,
we have chosen the coeﬃcients of homogeneous solutions to th is diﬀerential equation so as
to ensure normalizability and vanishing scalar contributi on to the stress tensor (according
to our renormalization conditions).
