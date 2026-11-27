---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-036-b33-scalar-products-and-the-homogeneous-limit
section_title: "B.3.3 Scalar products and the homogeneous limit"
section_number: null
pages: 42-42
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
We give below the determinant representation for the scalar products Sn. Please note than when compared
to [58] we have taken the factors of r(λ) =a(λ)/d(λ) outside the matrix. This leads to an overall phase e−inφ
in front of the determinant from the modiﬁed eigenvalue d(λ)→eiφd(λ).
Sn({µ},{λ})≡⟨{µ}|{λ}⟩ = e−inφ det(H({µ},{λ}))∏
j>kϕ(µk−µj)∏
α<βϕ(λβ−λα), (170)
with
Hab({µ},{λ}) = ϕ(η)
ϕ(µa−λb)
(∏
k⁄=a
ϕ(µk−λb +η)−eiφd(λb)
∏
k⁄=a
ϕ(µk−λb−η)
)
. (171)
We shall need the scalar products Sn(η/2,η/ 2,... ), Sn(η/2,η/ 2,η/ 2,... ), and the derivative ∂xSn({µ}|η/2 +
x,η/ 2,{λ}ab)
)⏐⏐⏐
x=0
in the homogeneous limit, which must be taken carefully due to the denominator.
Subtracting the relevant columns ofH from each other before taking the limit, and taking factors of the type
1/ϕ(ξm−ξm+1) inside, we arrive at the replacement of the ﬁrst columns by their ﬁrst and second derivatives.
The second term in (171) disappears in these columns, thanks to d(ξm) = 0. Starting with Sn(η/2,η/ 2,... ), we
simply ﬁnd the ﬁrst column replaced by its derivative:
H′
a1({µ},{λ}) =−∂x
ϕ(η)
ϕ(µa−η/2−x)
∏
k⁄=a
ϕ(µk−x +η/2)
⏐⏐⏐⏐⏐
0
, (172)
and the product in the denominator of Sn is now taken for β >2. For Sn(η/2,η/ 2,η/ 2,... ) we arrive at the
following replacements for column 1 and 2:
H′
a2({µ},{λ}) = −∂x
ϕ(η)
ϕ(µa−η/2−x)
∏
k⁄=a
ϕ(µk−x +η/2)
⏐⏐⏐⏐⏐
0
, (173a)
H′′
a1({µ},{λ}) = 1
2∂2
x
ϕ(η)
ϕ(µa−η/2−x)
∏
k⁄=a
ϕ(µk−x +η/2)
⏐⏐⏐⏐⏐
0
. (173b)
The product in the denominator of Sn is now taken for β >3. Finally for ∂xSn({µ}|η/2 +x,η/ 2,{λ}) we can
take the derivative inside det( H) and let it act on the relevant column. Taking the homogeneous limit then
leads to further derivatives, so that in total we obtain
∂xSn({µ}|η/2 +x,η/ 2,{λ})
⏐⏐⏐⏐⏐
0
= −1
2
e−inφ det( ˜H′′({µ}|η/2,η/ 2,{λ}))∏
j>kϕ(µk−µj)∏
α<β,β>2ϕ(λβ−λα)
+
∑
2<β
ϕ′(λβ−η/2)
ϕ(λβ−η/2)Sn({µ}|η/2,η/ 2,{λ}), (174)
where ˜H′′ is obtained from H by diﬀerentiating the ﬁrst column twice:
˜H′′
a0 =∂2
x
ϕ(η)
ϕ(µa−η/2−x)
∏
k⁄=a
ϕ(µk−x +η/2)
⏐⏐⏐⏐⏐
x=0
. (175)
