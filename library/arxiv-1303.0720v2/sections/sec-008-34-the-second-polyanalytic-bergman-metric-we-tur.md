---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-008-34-the-second-polyanalytic-bergman-metric-we-tur
section_title: "The second polyanalytic Bergman metric. We turn to Bergman’s second metric. The"
section_number: 3.4
pages: 6-6
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
function
(3.4.1)
Lq(z, z′) := log E⊗2[Kq](z, z′; z, z′)
is basic to the analysis, where the expression on the right-hand side is as in (3.3.1). We think of
(z, ¯z′) as holomorphic coordinates, and form the corresponding Bergman metric:
∂z ¯∂zLq(z, z′)|dz|2 + ∂z∂z′Lq(z, z′)dzdz′ + ¯∂z ¯∂z′Lq(z, z′)d¯zd¯z′ + ∂z′ ¯∂z′Lq(z, z′)|dz′|2
Next, we write z′ = z + ǫ, so that dz′ = dz + dǫ; to simplify as much as possible, we restrict to
dǫ = 0, so that dz′ = dz. Then the above metric becomes
(∆z + ∆z′)Lq(z, z′)|dz|2 + 2 Re[∂z∂z′Lq(z, z′)(dz)2],
which after full implementation of the coordinate change becomes
(3.4.2)
ds④
q,ω,ǫ(z)2 := (∆z + ∆z′)Lq(z, z′)|dz|2 + 2 Re[∂z∂z′Lq(z, z′)(dz)2]

z′=:z+ǫ
= (∆z + 2∆ǫ −¯∂z∂ǫ −∂z ¯∂ǫ)[Lq(z, z + ǫ)]|dz|2 + 2 Re
n
(∂z∂ǫ −∂2
ǫ)[Lq(z, z + ǫ)](dz)2o
.
This gives us a metric parametrized by ǫ, for ǫ close to 0, which we may think of as Bergman’s
second polyanalytic metric. This metric (3.4.2) is, generally speaking, not isothermal. We
note here that to a given C∞-smooth non-isothermal metric we may associate an appropriate
quasiconformal mapping which maps the non-isothermal metric to an isothermal one.
