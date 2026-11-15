---
doc_id: arxiv-1101.3374v1
doc_title: "Pontryagin invariants and integral formulas for Milnor's triple linking number"
section_id: sec-009-appendix-whiteheads-integral-formula-for-the-hop
section_title: "Appendix. Whitehead's integral formula for the Hopf invariant"
section_number: null
pages: 56-57
source_pdf: 1101.3374v1.pdf
source_sha256: 01d76c1d259c1d51
toc_source: outline
doc_brief: "Pontryagin invariants and integral formulas for Milnor's triple linking number — To each three-component link in the 3-sphere, we associate a geometrically natural characteristic map from the 3-torus"
---
We take this opportunity to make J. H. C. Whitehead’s integral formula for the Hopf
invariant of a map f : S3 →S2 explicit, and have relegated it to an appendix because we
do not use the result in this paper.
Recall from Section 8 Whitehead’s formula,
Hopf(f) =
Z
S3 α ∧ωf,
where ωf = f∗ω is the pullback to S3 of the normalized area form ω on S2, and α is any
1-form on S3 such that dα = ωf. To make this formula explicit requires a way to produce
such an α.
To do this, we ﬁrst write Whitehead’s formula in the language of vector ﬁelds,
Hopf(f) =
Z
S3
⇀a·
⇀vf d vol,
where the 2-form ωf on S3 has been converted to the vector ﬁeld
⇀vf in the usual way,
and where
⇀a is any vector ﬁeld on S3 such that ∇×
⇀a =
⇀vf.
An explicit recipe for
⇀a was given by DeTurck and Gluck [2008a]:
⇀a(y) = BS(
⇀vf)(y) =
Z
S3 Pyx
⇀vf(x) × ∇y ϕ(x, y) dx.
Here BS is the Biot–Savart operator for vector ﬁelds on the 3-sphere. In the last integral,
Pyx indicates parallel transport in S3 along the geodesic segment from x to y, and the
function ϕ is given by
ϕ(α) = −1
4π2 (π −α) csc α,
and ϕ(x, y) is an abbreviation for ϕ(α(x, y)), with α(x, y) the geodesic distance on S3
between x and y.
The signiﬁcance of the above function ϕ is that it is the fundamental solution of a
shifted Laplacian on S3:
−∆ϕ −ϕ = δ,
where δ is the Dirac delta function.
The above formula for BS(
⇀vf) is the analogue on S3 of the classical Biot–Savart formula
from electrodynamics in R3, expressing the magnetic ﬁeld BS(
⇀vf) in terms of the current
ﬂow
⇀vf. The equation ∇× BS(
⇀vf) =
⇀vf is just one of Maxwell’s equations, transplanted
to S3.
Inserting this formula for BS(
⇀v) into the previous formula for the Hopf invariant and
performing simple manipulations, we get
Hopf(f) = −
Z
S3×S3 Pyx
⇀vf(x) ×
⇀vf(y)· ∇y ϕ(x, y) dx dy,
the explicit version of Whitehead’s integral formula on the 3-sphere S3.
56
Pontryagin invariants and Integral formulas for Milnor’s triple linking number
