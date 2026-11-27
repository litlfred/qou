---
doc_id: arxiv-1101.2451v2
doc_title: "From Navier-Stokes To Einstein"
section_id: sec-003-4-characterizing-the-dual-geometries
section_title: "Characterizing the dual geometries"
section_number: 4
pages: 5-7
source_pdf: 1101.2451v2.pdf
source_sha256: 33a74704382d3589
toc_source: outline
doc_brief: "From Navier-Stokes To Einstein — We show by explicit construction that for every solution of the incompressible Navier-Stokes equation in p + 1 dimensions, there is a uniquely associated “dual”"
---
We seek a relation between the (p+2)-dimensional Einstein and (p+1)-dimensional Navier-Stokes equa-
tions. Of course, the former has a much larger solution space than the latter so only a special type of
Einstein geometry is relevant. Roughly speaking, the relevant geometries are non-singular perturbations
of a horizon. Let us now make this more precise.
We consider geometries of the type depicted in Figure 1 with an outer “cutoﬀ” boundary denoted
Σc. The boundary hypersurface Σ c is taken to be asymptotically null in both the far future and far past.
In the Minkowskian coordinates ds2
p+2 =−dudv +dxidxi, past null inﬁnity I− is the union of the null
surfaces v→−∞ together with u→−∞ and Σc is the timelike hypersurface uv =−4rc with v >0.
Past (future) event horizons H− (H+) are deﬁned by the boundaries of the causal future (past) of Σ c.
The dual geometries will be constructed in two a priori diﬀerent expansions about Minkowski space: the
near-horizon and the hydrodynamic ϵ-expansion. Ultimately the two expansions will be shown to be
equivalent.
Initial data can be speciﬁed on the union of Σ c andI−. We consider initial data which is asymp-
totically Minkowskian and ﬂat (no incoming waves) on I− (or equivalentlyH−). On Σ c we generally
demand that the intrinsic metric γab be ﬂat,
γab =ηab, a,b = 0,...p (8)
H+
H-
I- I-
r=0
r=-¥
Sc
r=rc
t=-¥
Figure 1: This ﬁgure depicts the Einstein geometry holographically dual to a ﬂuid. The accelerated boundary hypersurface
Σc at radiusr =rc is intrinsically ﬂat but the extrinsic curvature is given by the ﬂuid stress tensor. This extrinsic curvature
leads to gravity waves which propagate radially inward. The leading-order condition that these waves do not cross the past
horizonH− of Σ c at τ =−∞ or produce singularities on the future horizon H+ at r = 0 is the non-linear incompressible
Navier-Stokes equation for the ﬂuid.
although we will later consider “forcing” the system by perturbing γab.
We wish to consider the general solution of the Einstein equations consistent with this initial data
and smooth on H+.1 In particular, so far we have not speciﬁed the extrinsic curvature Kab on Σc or
equivalently (and more conveniently) the Brown-York stress tensor on Σc2
Tab≡ 2(γabK−Kab). (9)
If no initial data were prescribed on I−, anyTab on Σc consistent with the constraint equations could be
chosen. This data could then in general be evolved radially inwards to produce a spacetime everywhere
inside of Σc. In general, such a spacetime will have gravitational ﬂux (if not singularities) going up to
v =∞ (I +) as well as down to I−. Hence we have a “shooting problem” to ﬁnd those special allowed
choices of Tab which produce a spacetime smooth on H+ with no ﬂux coming up from I−.
We solved this problem in [28] to leading order in a double expansion in long wavelengths and weak
ﬁelds.3 Ingoing Rindler coordinates were used for which the leading order ﬂat metric is
ds2
p+2 =−rdτ 2 + 2dτdr +dxidxi. (10)
Σc is the accelerated surface r = rc,H− is τ =−∞ andH+ is r = 0. These coordinates are conve-
nient for analyzing smoothness on H+. It was found that the allowed choices of Tab are precisely those
corresponding to the linearized ﬂuid:
r3/2
c Tτi =vi, r 3/2
c Tij =−η∂ (ivj), (11)
where the (kinematic) viscosity here is given by the formula
η =rc, (12)
1Here we allow for incoming ﬂux where I− meets Σc at u =−∞, v = 0.
2Our normalization here agrees with the conventional one for G = 1/16π.
3Our conventions here diﬀer from [28].
while vi obeys the linearized incompressible Navier-Stokes equation
∂ivi = 0, ∂ τvi−η∂ 2vi = 0. (13)
If we choose any value for the viscosity other than (12), the constraint equations on Σ c are still obeyed,
but gravitational waves are propagated down to I− and there is a singularity at r = 0.
In this paper we go one step further and solve the problem in certain hydrodynamic and near-horizon
limits without making a linearized approximation, enabling us to see a direct connection between the
nonlinear structures of the Navier-Stokes and Einstein equations.
