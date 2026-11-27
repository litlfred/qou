---
doc_id: arxiv-0712.2456v4
doc_title: "Nonlinear Fluid Dynamics from Gravity"
section_id: sec-020-43-the-symmetric-tensors-of-so3
section_title: "The symmetric tensors of $SO(3)$"
section_number: 4.3
pages: 21-23
source_pdf: 0712.2456v4.pdf
source_sha256: c5fb02c494169403
toc_source: inferred
doc_brief: "Nonlinear Fluid Dynamics from Gravity — Black branes in AdS 5 appear in a four parameter family labeled by their velocity and temperature."
---
We now turn to g(1)
T , the part of g(1) that transforms in the 5, the symmetric traceless two
tensor representation, of SO(3). Let us parameterize our metric ﬂuctuation by
(
g(1)
T
)
αβ
dxα dxβ = r2 α(1)
ij (r) dxi dxj, (4.15)
where αij is traceless and symmetric. The Einstein’s equation Eij = 0 yield
d
dr
(
r5 f (r) d
dr α(1)
ij
)
= −6 r2 σ(0)
ij , (4.16)
where we have deﬁned a symmetric traceless matrix
σ(0)
ij = ∂(iβ(0)
j) − 1
3 δij ∂mβ(0)
m . (4.17)
The LHS of (4.16) is the restriction of the operator H of (3.4) to the tensor sector, and
the RHS of this equation is the tensor part of the source term s1. Note that H is a ﬁrst
order operator in the variable α(1)′
ij (r) and so may be integrated for an arbitrary source
term. The solution to this equation with arbitrary source te rm s(r) is given by (dropping
the tensor indices):
α(1) = −
∫ ∞
r
dx
f (x) x5
∫ x
1
s(y) dy . (4.18)
Note that the lower limit of the inner integral in (4.18) has b een chosen to be unity.
Provided that s(x) is regular at x = 1 (this is true of (4.16) and will be true at every order
in perturbation theory),
∫ x
1 s(x) has a zero at x = 1. It follows that the outer integrand
in (4.18) is regular at nonzero x (and in particular at x = 1) despite the explicit zero in
the factor f (x) in the denominator. The solution for α(1) is also normalizable provided the
source is regular and grows at inﬁnity slower than r3. This condition is obeyed in (4.16)
and is expected to continue to be obeyed at arbitrary order in perturbation theory (see the
next section).
Applying (4.18) to the source term in (4.16) we ﬁnd that the so lution for α(1)
ij is given
by
(g(1)
T )αβ dxα dxβ = 2 r2 F (r) σ(0)
ij dxidxj. (4.19)
with
F (r) =
∫ ∞
r
dx x2 + x + 1
x(x + 1) (x2 + 1) = 1
4
[
ln
( (1 + r)2(1 + r2)
r4
)
− 2 arctan( r) + π
]
(4.20)
At large r it evaluates to
(g(1)
T )αβ dxα dxβ = 2
(
r − 1
4 r2
)
σ(0)
ij dxidxj. (4.21)
As in the previous subsections, the ﬁrst term in (4.21) yield s a contribution to the stress
tensor that diverges like r3, but precisely cancels the corresponding divergence from ﬁ rst
derivative terms in the expansion of g(0). However the second term in this expansion yields
an important ﬁnite contribution to the stress tensor, as we w ill see below.
Summary of the ﬁrst order calculation: In summary, our ﬁnal answer for g(0) + g(1),
expanded to ﬁrst order in boundary derivatives about yµ = 0, is given explicitly as
ds2 = 2 dv dr − r2f (r) dv2 + r2 dxi dxi
− 2 xµ ∂µ β(0)
i dr dxi − 2 xµ ∂µ β(0)
i r2(1 − f (r)) dv dxi − 4 xµ ∂µ b(0)
r2 dv2
+ 2 r2 F (r) σ(0)
ij dxi dxj + 2
3 r ∂iβ(0)
i dv2 + 2 r ∂vβ(0)
i dv dxi.
(4.22)
This metric solves Einstein’s equations to ﬁrst order in the neighbourhood of xµ = 0
provided the functions b(0) and β(0)
i satisfy
∂vb(0) = ∂iβ(0)
i
3
∂ib(0) = ∂vβ(0)
i .
(4.23)
