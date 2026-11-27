---
doc_id: arxiv-0712.2456v4
doc_title: "Nonlinear Fluid Dynamics from Gravity"
section_id: sec-019-42-vectors-of-so3
section_title: "Vectors of $SO(3)$"
section_number: 4.2
pages: 20-21
source_pdf: 0712.2456v4.pdf
source_sha256: c5fb02c494169403
toc_source: inferred
doc_brief: "Nonlinear Fluid Dynamics from Gravity — Black branes in AdS 5 appear in a four parameter family labeled by their velocity and temperature."
---
In the vector channel the relevant Einstein’s equations are the constraint r2 f (r) Eri +Evi =
0 and a dynamical equation which can be chosen to be any linear combination of the
Einstein’s equations Eri = 0 and Evi = 0. The constraint evaluates to
∂ib(0) = ∂vβ(0)
i , (4.10)
which we will later interpret as a consequence of the conserv ation of boundary momentum.
In order to explore the content of the dynamical equation (we choose Eri = 0), it is
convenient to parameterize the vector part of the ﬂuctuatio n metric by the functions j(1)
i ,
as (
g(1)
V
)
αβ
dxα dxβ = 2 r2 (1 − f (r)) j(1)
i (r) dv dxi. (4.11)
The dynamical equation for ji(r) turns out to be
d
dr
( 1
r3
d
dr j(1)
i (r)
)
= − 3
r2 ∂vβ(0)
i . (4.12)
The LHS of (4.12) is the restriction of the operator H of (3.4) to the vector sector, and
the RHS of this equation is the projection of s1 to the vector sector. H is of ﬁrst order in
the variable j(1)′
(r) and so may be integrated for an arbitrary source term. The re sulting
solution is regular and normalizable provided the source is regular and decays at inﬁnity
faster than 1/r. This condition is obeyed in (4.12); it seems rather clear th at it will continue
to be obeyed at arbitrary order in perturbation theory (see t he next section).
Returning to (4.12), the general solution of this equation i s
j(1)
i (r) = ∂vβ(0)
i r3 + ai r4 + ci (4.13)
for arbitrary constants ai, ci. The coeﬃcient ai multiplies a non-normalizable metric defor-
mation, and so is forced to zero by our choice of boundary cond itions. The other integration
constant ci multiplies an inﬁnitesimal shift in the velocity of the bran e. It turns out (see
below) that a nonzero value for ci leads to a nonzero value for T0i which violates our
‘renormalization’ condition, consequently ci must be set to zero. In summary,
(
g(1)
V
)
αβ
dxα dxβ = 2 r ∂vβ(0)
i dv dxi. (4.14)
As in the scalar sector above, this solution grows by a factor of r3 faster at the boundary
than the shear zero mode. This slow fall oﬀ leads to a divergen t contribution to the stress
tensor which precisely cancels an equal and opposite diverg ence from terms in the expansion
of g(0) to ﬁrst order in derivatives. As we will see below, the full co ntribution of g(0) + g(1)
to the vector part of the boundary stress tensor is just zero, again in agreement with our
renormalization conditions.
