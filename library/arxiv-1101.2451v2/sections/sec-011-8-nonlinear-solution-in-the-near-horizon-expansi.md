---
doc_id: arxiv-1101.2451v2
doc_title: "From Navier-Stokes To Einstein"
section_id: sec-011-8-nonlinear-solution-in-the-near-horizon-expansi
section_title: "Nonlinear solution in the near-horizon expansion"
section_number: 8
pages: 12-13
source_pdf: 1101.2451v2.pdf
source_sha256: 33a74704382d3589
toc_source: outline
doc_brief: "From Navier-Stokes To Einstein — We show by explicit construction that for every solution of the incompressible Navier-Stokes equation in p + 1 dimensions, there is a uniquely associated “dual”"
---
In section 4, the nonlinear Einstein equations with certain boundary conditions were solved in the non-
relativistic, long-wavelength hydrodynamic ϵ-expansion. This generalized the analysis given in [28] of
the ϵ-expansion for linearized modes. [28] also considered, for linearized modes, a second, near-horizon
expansion. Although physically inequivalent, the two expansions were found to be equivalent mathemat-
ically and reduce to the linearized dynamics of an incompressible ﬂuid. In this section, we consider the
nonlinear version of the near-horizon expansion and ﬁnd that it is again mathematically equivalent to
the nonlinear ϵ-expansion.
In the ϵ-expansion one solves the shooting problem for long-wavelength perturbations of Σ c with a
ﬁxed leading-order extrinsic curvature. The proper acceleration of a worldline at ﬁxed xi in Σc is to
leading order just proportional to Kττ , so we may also view this as ﬁxing the acceleration away from the
origin. In the near-horizon expansion, instead of expanding in the wavelength one expands in the inverse
acceleration. We begin with the ﬂat metric on the Rindler wedge
ds2
p+2 =−rdτ 2 + 2dτdr +dxidxi. (40)
To avoid confusion with the notation of the previous section we put the boundary on the accelerating
surface
r = ˜rc, (41)
so thatr≤ ˜rc. The near-horizon, large acceleration, limit is ˜rc→ 0. In order to exhibit the ˜rc-dependence
explicitly in the metric we transform to r = ˜rcˆr, τ = ˆτ
˜rc
so that r≤ 1 and
ds2
p+2 =− ˆr
˜rc
dˆτ 2 + 2dˆτd ˆr +dxidxi. (42)
In these coordinates the near-horizon limit rescales to inﬁnity the coeﬃcient of dˆτ 2 at any ﬁnite ˆr.
We now wish to consider perturbations of this metric solving the Einstein equations order by order
in the near-horizon expansion parameter ˜rc that are consistent with a ﬂat induced metric at ˆr = 1. At
the level of linear perturbations, the most general solution was found in [28] (characterized in terms of
the data at r = ˜rc). This solution is (for all r)
dˆs2
p+2 =− ˆr
˜rc
dˆτ 2 + 2dˆτd ˆr +dxidxi− 2(1− ˆr)vidxidˆτ + ˜rc
[
(1− ˆr2)∂2vidxidˆτ− 2vidxidˆr
]
+O(˜r2
c) (43)
where ∂ivi = 0 and ∂ˆτvi−∂2vi = 0. That is, vi is an incompressible ﬂuid ﬂow obeying the linearized
Navier-Stokes equation with unit kinematic viscosity.
The nonlinear generalization of (43) which solves the nonlinear Einstein equations to O(˜rc) is
dˆs2
p+2 =− ˆr
˜rc
dˆτ 2
+
[
2dˆτd ˆr +dxidxi− 2(1− ˆr)vidxidˆτ + (1− ˆr)(v2 + 2 ˆP )dˆτ 2]
+ ˜rc
[
(1− ˆr)vivjdxidxj− 2vidxidˆr + (v2 + 2 ˆP )dˆτd ˆr + (1− ˆr2)∂2vidxidˆτ− 2(1− ˆr)ˆqi(ˆτ, ˆr,x )dxidˆτ
]
+ ˜r2
c
[
2g(2)
ˆri (ˆτ, ˆr,x )dxidˆr +g(2)
ij (ˆτ, ˆr,x )dxidxj
]
+O(˜r2
c) (44)
provided∂ivi = 0, ∂ˆτvj−∂2vj +vk∂kvj +∂j ˆP = 0. ˆqi, g(2)
ˆri , g(2)
ij are solutions of ﬁrst order diﬀerential
equations of the type (36) and (37). Further O(˜r2
c) pieces do not aﬀect the equations of motion to this
order.
We can now see explicitly that making the notation change v→ ˆv, xi→ ˆxi and ˜rc→ λ in (44)
gives us the rescaled solution (31) in section 6. Hence the near-horizon and hydrodynamic expansions
are mathematically equivalent.
Since we are identifying ˜rc = λ = ϵ2
rc
, rc→∞ in the metric (14) is actually equivalent to the near-
horizon limit ˜rc→ 0 in (44). This may at ﬁrst seem odd, but the near-horizon-hydrodynamic equivalence
involves a constant rescaling of (14) by a factor of 1
r2c
, the proper distance to the cutoﬀ surface in the
rescaled metric (44) indeed behaves as 1√rc
.
