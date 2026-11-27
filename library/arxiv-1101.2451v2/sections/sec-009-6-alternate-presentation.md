---
doc_id: arxiv-1101.2451v2
doc_title: "From Navier-Stokes To Einstein"
section_id: sec-009-6-alternate-presentation
section_title: "Alternate presentation"
section_number: 6
pages: 10-11
source_pdf: 1101.2451v2.pdf
source_sha256: 33a74704382d3589
toc_source: outline
doc_brief: "From Navier-Stokes To Einstein — We show by explicit construction that for every solution of the incompressible Navier-Stokes equation in p + 1 dimensions, there is a uniquely associated “dual”"
---
In this section we give an alternate presentation of the metric (14) in which all the factors of ϵ appear
explicitly, without being hidden in the functional dependence on the coordinates. This is accomplished
by ﬁrst transforming to hatted coordinates
xi = rcˆxi
ϵ , τ = rcˆτ
ϵ2 , r =rcˆr (26)
so that ∂ˆτ =O(ϵ0) and we denote ˆ∂i = ∂
∂ ˆxi =O(ϵ0). In the new coordinates
ds2
p+2 =− ˆrr3
c
ϵ4 dˆτ 2 + 2r2
c
ϵ2 dˆτd ˆr + r2
c
ϵ2dˆxidˆxi
− 2r2
c
1− ˆr
ϵ2 ˆvidˆxidˆτ− 2rcˆvidˆxidˆr (27)
+ (1− ˆr)
[
r2
c
ˆv2 + 2 ˆP
ϵ2 dˆτ 2 +rcˆviˆvjdˆxidˆxj
]
+rc(ˆv2 + 2 ˆP )dˆτd ˆr
− (ˆr2− 1)rc ˆ∂2ˆvidˆxidˆτ + ..., (28)
where ˆP (ˆx, ˆτ) = 1
ϵ2P (x(ˆx),τ (ˆτ)), ˆvi(ˆx, ˆτ) = 1
ϵvi(x(ˆx),τ (ˆτ)), ˆv2≡ ˆviδijˆvj and i,j indices are raised and
lowered with δij. The usual Navier-Stokes equation for v, P with η =rc implies
∂ˆτ ˆvj− ˆ∂2ˆvj + ˆvk ˆ∂kˆvj + ˆ∂j ˆP = 0. (29)
This is the Navier-Stokes equation with η = 1 and no factors of ϵ or rc.
Finally let us consider the rescaled metric dˆs2
p+2 = ϵ2
r2c
ds2
p+2. The Einstein tensor is invariant under
such constant metric rescalings. Rearranging terms and deﬁning
λ≡ ϵ2
rc
(30)
one ﬁnds
dˆs2
p+2 =− ˆr
λdˆτ 2
+
[
2dˆτd ˆr +dˆxidˆxi− 2(1− ˆr)ˆvidˆxidˆτ + (1− ˆr)(ˆv2 + 2 ˆP )dˆτ 2]
(31)
+λ
[
(1− ˆr)ˆviˆvjdˆxidˆxj− 2ˆvidˆxidˆr + (ˆv2 + 2 ˆP )dˆτd ˆr + (1− ˆr2)ˆ∂2ˆvidˆxidˆτ
]
+....
The Brown-York stress tensor is
{
ˆT ˆτ
ˆτ =−
√
λˆv2, ˆT ˆτ
i =−
√
λˆvi, ˆTi
j = 1√
λ
δi
j +
√
λ
[
ˆviˆvj + ˆPδi
j− 2ˆ∂iˆvj
]}
+O(λ3/2). (32)
The important point here is that the geometry depends only on the ratioλ = ϵ2
rc
and notϵ orrc separately.
Given that the rescaled geometry depends only on λ and the ϵ-dependence (21) of the unrescaled
geometry (14) we conclude that in the hatted coordinates
Gˆτ ˆτ = r2
c
ϵ4Gττ∼O (λ0), G ˆiˆj = r2
c
ϵ2Gij∼O (λ),
Gˆrˆτ = r2
c
ϵ2Grr∼O (λ), G ˆrˆr =r2
cGrr∼O (λ2)
Gˆτˆi = r2
c
ϵ3Gτi∼O (λ1/2), G ˆrˆi = r2
c
ϵ Gri∼O (λ3/2). (33)
Given the explicit factor of λ−1 ingˆτ ˆτ, it is not immediately obvious in this presentation that in a direct
computation the Einstein tensor will even have a good Taylor expansion in λ. What happens is that,
because gˆrˆr = 0, there are only a limited number of powers of gˆτ ˆτ that can appear in the Einstein tensor,
and one may thereby directly recover (33). In fact, direct computation reveals we do slightly better; the
last line may be replaced by
Gˆτˆi = r2
c
ϵ3Gτi∼O (λ1), G ˆrˆi = r2
c
ϵ Gri∼O (λ2). (34)
Notice thatGˆτ ˆτ in (33) is of order λ0 rather thanλ1. We can improve this by computing a few higher
order pieces of the metric. Speciﬁcally, we add to (31)
−2λ(1− ˆr)ˆqidˆxidˆτ + 2λ2g(2)
ˆri dˆrdˆxi +λ2g(2)
ij dˆxidˆxj + ... (35)
Demanding that the r-independent pieces of Gˆτ ˆτ = 0 be solved through order λ0 then ﬁxes ˆqi(ˆτ, ˆx):
ˆ∂iˆqi = ˆ∂2ˆv2− 1
2 ˆvi ˆ∂iˆv2− 3
2∂ˆτ ˆv2− 1
2
(
ˆ∂iˆvj + ˆ∂jˆvi
)2
. (36)
Apparently ˆqi is a kind of heat current. Demanding that the entire Gˆτ ˆτ = 0 through order λ0 gives us a
diﬀerential equation for the combination ˆQ(ˆr, ˆτ, ˆx)≡− 2ˆ∂ig(2)
ˆri +∂ˆrgi (2)
i :
ˆQ+2ˆr∂ˆr ˆQ = 2ˆ∂iˆqi−2ˆviˆqi+3ˆr ˆ∂2ˆv2− ˆr
2
(
ˆ∂iˆvj + ˆ∂jˆvi
)2
+2 ˆ∂iˆvj ˆ∂jˆvi−ˆvj ˆ∂jˆv2+
(
ˆv2)2
−2ˆvi ˆ∂i ˆP +2 ˆP ˆv2. (37)
Choosing ˆqi, ˆQ accordingly, we ﬁnd that as desired all components of the Einstein equations vanish for
λ→ 0:
Gˆrˆa,G ˆaˆb,G ˆrˆr =O(λ). (38)
