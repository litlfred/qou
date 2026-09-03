---
doc_id: arxiv-1804.03926v3
doc_title: "Weighted Poincaré inequalities, concentration inequalities and tail bounds related to Stein kernels in dimension one"
section_id: sec-004-33-asymmetric-brascamp-lieb-type-inequalities
section_title: "Asymmetric Brascamp-Lieb-type inequalities"
section_number: 3.3
pages: 18-20
source_pdf: 1804.03926v3.pdf
source_sha256: 8ad8e2d5a8881a5b
---
The celebrated Brascamp-Lieb inequality [BL76] states tha t if a measure π on Rd, d ≥ 1, is strictly
log-concave - that is ϕ = − lnp is convex and Hess (ϕ ) (x) is a positive deﬁnite symmetric matrix for
anyx ∈ Supp (π) - then for any smooth function h,
Varπ (h) ≤
∫
∇hT (Hess (ϕ ))−1∇hdπ .
Considering the one dimensional case d = 1, Menz and Otto [MO13] proved that for any smooth
g ∈L1 (π),h ∈L∞ (π),
|Covπ (g,h )| ≤
‖‖‖‖
h′
ϕ ′′
‖‖‖‖
∞
‖‖g′‖‖
1 . (36)
18
The authors call the later inequality an asymmetric Brascam p-Lieb inequality. This inequality has
been then generalized to higher dimension ([CCEL13]) and be yond the log-concave case ([ABJ16]).
Considering the covariance of two smooth functions, we will derive in the next proposition in-
equalities involving the derivative of these functions and as well as quantities related to the Stein
kernel.
Proposition 11 Assume that τν > 0 on the support of ν. Then for any p,q ∈ [1, +∞],p−1+q−1 = 1,
|Cov (g,h )| ≤
‖‖g′τν
‖‖
p
‖‖‖‖
¯L (h)
τν
‖‖‖‖
q
(37)
Furthermore, if p = 1 and q = +∞, we have
|Cov (g,h )| ≤
‖‖h′‖‖
∞
‖‖g′τν
‖‖
1 . (38)
If p,q ∈ (1, +∞), we also have
|Cov (g,h )| ≤
‖‖g′τν
‖‖
p
‖‖‖h′m1/q
‖‖‖
q
, (39)
where m (x) = p (x)−1∫
k (x,y )τ−1
ν (y)dy on the support of ν. If in addition, τν ≥ σ 2
min > 0 a.s. ,
then
|Cov (g,h )| ≤ σ −2
min
‖‖g′τν
‖‖
p
‖‖‖h′τ1/q
ν
‖‖‖
q
. (40)
Note that if ν is strongly log-concave, meaning that ϕ ′′ ≥ c > 0 for ϕ = − lnp, then the
asymmetric Brascamp-Lieb inequality (36) and covariance i dentity (38) both induce the following
inequality,
|Cov (g,h )| ≤ c−1‖‖h′‖‖
∞
‖‖g′‖‖
1 .
Proof. By (14) and H¨ older’s inequality, we have
|Cov (g,h )| =
∫
R
g′τν
¯Lh
τν
dν
≤
‖‖g′τν
‖‖
p
‖‖‖‖
¯L (h)
τν
‖‖‖‖
q
.
So Inequality (37) is proved. To prove (38) it suﬃces to apply (37) with p = 1 and q = + ∞ and
remark that ‖‖‖‖
¯L (h)
τν
‖‖‖‖
∞
=
‖‖‖‖
∫
h′ (y) kν (x,y )dy∫
kν (x,z )dz
‖‖‖‖
∞
≤
‖‖h′‖‖
∞ .
Now, to prove (39) simply note that
‖‖‖‖
¯L (h)
τν
‖‖‖‖
q
=
‖‖‖‖
∫
h′ (y) kν (x,y )dy∫
kν (x,z )dz
‖‖‖‖
q
≤
∫ ∫ (
h′ (y)
) q kν (x,y )∫
kν (x,z )dzdxdy =
‖‖‖h′m1/q
‖‖‖
q
.
To deduce (40) from (39), just remark that
m (x) = 1
p (x)
∫ kν (x,y )
τν (y) dy ≤ 1
σ 2
minp (x)
∫
kν (x,y )dy = τν (x)
σ 2
min
.
19
