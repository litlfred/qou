---
doc_id: arxiv-1101.2451v2
doc_title: "From Navier-Stokes To Einstein"
section_id: sec-006-52-forcing-the-fluid
section_title: "Forcing the fluid"
section_number: 5.2
pages: 8-9
source_pdf: 1101.2451v2.pdf
source_sha256: 33a74704382d3589
toc_source: outline
doc_brief: "From Navier-Stokes To Einstein — We show by explicit construction that for every solution of the incompressible Navier-Stokes equation in p + 1 dimensions, there is a uniquely associated “dual”"
---
Solutions of the linearized Navier-Stokes equation decay exponentially in the future. There is some
expectation - although no proof - that nonlinear solutions eventually decay as well. Therefore the extrinsic
curvature on Σc in our examples is expected to become constant.
On the other hand, already at the linear level, Navier-Stokes solutions grow exponentially in the far
past and typically are singular at τ =−∞ . Therefore we expect that the dual geometry is also singular
atτ =−∞, which is the past horizonH− of Σc. This singularity is not problematic for real ﬂuids, as we
are typically interested in cases where forcing terms correct the Navier-Stokes equation. For example we
might consider a ﬂuid which is initially at rest, stirred at time τ =τ∗ , and then left to evolve according
to the unforced Navier-Stokes equation.
In fact this kind of situation is also very natural to consider on the gravity side. Consider ﬂat
Minkowski spacetime with a ﬂat metric and constant extrinsic curvature on the boundary Σ c forτ <τ∗.
We then stir it at τ = τ∗ by momentarily perturbing the boundary condition that the induced metric
on Σc be ﬂat. This will send out a gravitational shock wave along τ = τ∗ and excite the geometry for
τ > τ∗. The result should be an appropriate gluing of (14) along a null hypersurface to ﬂat Minkowski
space. This is depicted in Figure 2.
At the linear level, it is possible to explicitly construct the glued geometry describing this situation
through order ϵ3. The metric is
ds2 =−rdτ 2 + 2dτdr +dxidxi
−
[
2(1−r/rc)vidxidτ + (1−r/rc) (∂jvi +∂ivj)dxidxj− 2
(
r− r2
2rc
−rc/2
)
∂2vidxidτ
]
−δ(τ−τ∗)
[(
4(1−r/rc)Fi + 2
rc
αi
)
dxidτ− 2
rc
βijdxidxj
]
+... (22)
Sc
I-
I-
t=-¥
t=t*
Figure 2: On the Σ c surface, prior to τ =τ∗, all initial data is trivial. At τ =τ∗, a gravitational shock wave arrives. The
shock forces the ﬂuid on Σ c, and consequently the vi is nontrivial on Σ c after τ∗.
where Fi is an arbitrary function of xi obeying ∂iFi = 0. βij and αi (which is divergence free) are both
functions of xi and related to Fi by
∂j∂jαi =Fi, β ij =∂iαj +∂jαi. (23)
Since the metric on Σc is no longer ﬂat, the constraint equations become linearized Navier-Stokes with a
forcing term similar to that described in [28]. For this conﬁguration we have
∂τvi−η∂ 2vi =Fi(x)δ(τ−τ∗). (24)
Clearly, since vi(x,τ ) is taken to vanish for τ < τ∗, the forcing term will cause it to jump to Fi(xi)
at τ = τ∗, after which it will evolve according to Navier-Stokes. Given (24) this geometry solves the
linearized Einstein equations everywhere, and is characterized by an arbitrary divergence-free vector ﬁeld
Fi(x). Before τ =τ∗ it is ﬂat, while afterward it is, up to a coordinate transformation, the linearization
of (14).
At the nonlinear level, the equations are cumbersome and we have been unable to explicitly construct
the analog of (22) away from Σ c. However it seems plausible that qualitatively similar solutions persist
at the nonlinear level.
