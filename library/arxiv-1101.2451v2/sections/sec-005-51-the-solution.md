---
doc_id: arxiv-1101.2451v2
doc_title: "From Navier-Stokes To Einstein"
section_id: sec-005-51-the-solution
section_title: "The solution"
section_number: 5.1
pages: 7-8
source_pdf: 1101.2451v2.pdf
source_sha256: 33a74704382d3589
toc_source: outline
doc_brief: "From Navier-Stokes To Einstein — We show by explicit construction that for every solution of the incompressible Navier-Stokes equation in p + 1 dimensions, there is a uniquely associated “dual”"
---
Consider the metric
ds2
p+2 =−rdτ 2 + 2dτdr +dxidxi
− 2
(
1− r
rc
)
vidxidτ− 2vi
rc
dxidr (14)
+
(
1− r
rc
)[
(v2 + 2P )dτ 2 + vivj
rc
dxidxj
]
+
(v2
rc
+ 2P
rc
)
dτdr
− (r2−r2
c)
rc
∂2vidxidτ + ...
wherevi =vi(xi,τ ) and P (xi,τ ) are independent of r. Here and henceforth i,j = 1,..p indices are raised
and lowered with δij and we take
vi∼O (ϵ), P ∼O (ϵ2), ∂ i∼O (ϵ), ∂ τ∼O (ϵ2) (15)
as in the hydrodynamic scaling of section 3. It follows that the ﬁrst line on the right hand side of (14) is
O(ϵ0) and each subsequent line is one higher order in ϵ. The linearization of this expression in vi agrees
with the linearized solution studied in [28].
On the cutoﬀ surface Σc, r =rc and the induced metric is ﬂat:
γabdxadxb =−rcdτ 2 +dxidxi, (16)
and hence satisﬁes the desired boundary condition. Here and henceforth xa∼ (xi,τ ). The extrinsic
curvature and unit normal on Σc are
Kab = 1
2LNγab =−1
2
[
Tab− 1
pγabγcdTcd
]
, N µ∂µ = 1√rc
∂τ +√rc
(
1− P
rc
)
∂r + vi
√rc
∂i +O(ϵ3). (17)
The Brown-York stress tensor is
Tabdxadxb = dx2
i√rc
+ v2
√rc
dτ 2− 2 vi
√rc
dxidτ + (vivj +Pδij)
r3/2
c
dxidxj− 2∂ivj
√rc
dxidxj +O(ϵ3). (18)
We wish to solve the Einstein equations as a power series in ϵ. We ﬁrst consider the necessary but
not suﬃcient condition that the constraints be satisﬁed on Σ c. At order ϵ0 the metric is ﬂat and Tab
is constant so they are trivially satisﬁed. The only way to get an order ϵ term is with one power of vi
and no derivatives. Such a linear term cannot appear because the constant vi terms in (14) can, through
quadratic order, be obtained from a boost of ﬂat space. The ﬁrst nontrivial equation is encountered at
order ϵ2:
r3/2
c ∂aTaτ =∂ivi = 0. (19)
This equation is satisﬁed if and only if vi is the velocity ﬁeld of an incompressible ﬂuid. Taking this to
be the case, one ﬁnds at order ϵ3:
r3/2
c ∂aTai =∂τvi−η∂ 2vi +∂iP +vj∂jvi = 0. (20)
This is satisﬁed if and only if vi solves the Navier-Stokes equation with pressure P and viscosity η =rc.
Once the constraints are satisﬁed it is ordinarily possible to evolve the solution oﬀ the hypersurface,
in this case in the radial direction, at least for a ﬁnite distance. Here we have the danger of singularities
at the horizon H+ near r = 0, or equivalently waves coming up from I−. We know from [28] that such
singularities are absent in the linearized analysis provided the ﬂuid viscosity takes the required value
(12). We have checked by direct computation that this absence of singularities extends to the nonlinear
case as well. That is all components obey
Gra,Gab,Grr =O(ϵ4) (21)
and are nonsingular for ﬁnite values of r. Presumably the order ϵ4 and higher terms in the metric can
be chosen so that the Einstein equations are solved exactly.
It turns out that it is still possible to solve the Einstein equations analytically through order ϵ3 with
the “wrong” value of the viscosity (i.e. η⁄=rc ) even in the nonlinear case. As expected these solutions
develop a singularity at r = 0 nearH+, and are presented in Appendix A .
