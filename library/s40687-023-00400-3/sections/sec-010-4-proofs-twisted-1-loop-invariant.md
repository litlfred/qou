---
doc_id: s40687-023-00400-3
doc_title: "bonn.mpg.de/stavros 2MaxPlanckInstitutefor Mathematics,Bonn,Germany Fulllistofauthorinformationis availableattheendofthearticle DedicatedtoWalterNeumann andDonZagier,withadmiration"
section_id: sec-010-4-proofs-twisted-1-loop-invariant
section_title: "Proofs: twisted 1-loop invariant"
section_number: 4
pages: 16-21
source_pdf: s40687-023-00400-3.pdf
source_sha256: fd7638a8cf512a99
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
duplicate_of: "arxiv-2109.00379v1"
---
Inthissection,wegiveproofsofthepropertiesofthetwisted1-loopinvariant.
Proof Theorem 1.6 WewillusethenotationofTheorem 1.5whichrelatestheNZmatrices
oftwotriangulations T and T obtainedbya2–3PachnermoveshowninFig. 2.Recallthat
a 2–3 Pachner move onT is determined by two tetrahedra/Delta1α and /Delta1β with a common
face in T . Dividing the bipyramid/Delta1α ∪ /Delta1β into three tetrahedra/Delta1a,/Delta1b, and /Delta1c as in
S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37 Page 17 of 23 37
Fig.2, we obtain a new ideal triangulationT with one additional edgee0.N o t et h a to n e
canreadoﬀrelationsofshapeparametersbetween T and T directlyfromFig. 2:
z′
a = zα zβ ,z ′
b = 1 −1/zβ
1 − zα
,z ′
c = 1 −1/zα
1 − zβ
and zα = 1 −1/z′
b
1 − z′c
,z β = 1 −1/z′
c
1 − z′
b
(46)
withthegluingequation z′
az′
bz′
c = 1fortheedge e0.
Weﬁrstconsidertheﬂatteningpartofthedeﬁnition( 22).Acombinatorialﬂatteningof
T satisﬁestheequation f ′
a + f ′
b + f ′
c = 2(comingfromtheedge e0)anddeterminesoneof
T by
fα = fb + f ′′
c ,f ′
α = f ′′
a + fc f ′′
α = fa + f ′′
b ,
fβ = f ′′
b + fc,f ′
β = f ′′
a + fb,f ′′
β = fa + f ′′
c .
(47)
Thenastraightforwardcomputationshowsthat
∏
□
ζ□ f □
a
a ζ
□ f □
b
b ζ□ f □
c
c =± zα(1 − zα)zβ(1 − zβ)
1 − zα zβ
∏
□
ζ□ f □
α
α ζ
□ f □
β
β . (48)
Moreover,combiningEquation( 37)with( 46),onechecksthat
( ∑
□
G
□
(t)aζ□
a
∑
□
G
□
(t)bζ□
b
∑
□
G
□
(t)cζ□
c
)
⎛
⎜⎜⎝
1
zα zβ
1
zα zβ −1 1
zα zβ −1
0 zβ(1−zα)(1−zα zβ)
1−zβ 0
00 zα(1−zβ)(1−zα zβ)
1−zα
⎞
⎟⎟⎠
= Q
⎛
⎝
10 0
∗
∑
□
G□ (t)αζ□
α
∑
□
G□ (t)βζ□
β
⎞
⎠
⎛
⎝
10 0
0 zα zβ(1 − zα) zα(1 − zα)
0 zβ(1 − zβ) zα zβ(1 − zβ)
⎞
⎠ ,
wherethedeterminantofthe3 ×3matrixintheleft(resp.,right)handsideis(1 − zα zβ)2
(resp., zα(zα −1)zβ(zβ −1)(1− zα zβ)).Combiningthisfactwiththeequation( 48)andthe
factthatdet Q = 1,weconcludethat τCS(T ,t) =± τCS(T ,t). ⊓⊔
Proof of Theorem 1.7 Using Equation (28) and the fact that a combinatorial ﬂattening of
T (n) issimplygivenby ncopiesofthatof T ,itfollowsthat
τCS(T (n),t n) = det
( ∑
k∈Z
( ∑
□
G(n)□
k diag(ζ□ ,... ,ζ□ )
)
tnk
)
·
⎛
⎝
N∏
j=1
ζ
fj
j ζ
′f ′
j
j ζ
′′f ′′
j
j
⎞
⎠
−n
(49)
= det
⎛
⎜⎜⎜⎜
⎜⎜⎜⎝
W
0 W1 ··· Wn−2 Wn−1
tnWn−1 W0 ··· Wn−3 Wn−2
...
... ... ...
tnW2 tnW3 ··· W0 W1
tnW1 tnW2 ··· tnWn−1 W0
⎞
⎟⎟⎟⎟
⎟⎟⎟⎠
·
⎛
⎝
N∏
j=1
ζ
fj
j ζ
′f ′
j
j ζ
′′f ′′
j
j
⎞
⎠
−n
(50)
where Wr = ∑
k∈Z
∑
□ G□
nk+r diag(ζ□ ) tnk for0 ≤ r ≤ n −1.
The block matrix in the equation (50) is called afactor block circulant matrix where
the factor is diag(tn,... ,t n). It is known that a factor block circulant matrix admits a
37 Page 18 of 23 S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37
block-diagonalizationintermsofthe representer P(z) = W0 + W1z +···+ Wn−1zn−1:
⎛
⎜⎜⎜
⎜⎜⎜
⎜⎝
W
0 W1 ··· Wn−2 Wn−1
tnWn−1 W0 ··· Wn−3 Wn−2
..
.
..
. ... ..
.
t
nW2 tnW3 ··· W0 W1
tnW1 tnW2 ··· tnWn−1 W0
⎞
⎟⎟⎟
⎟⎟⎟
⎟⎠
= V
⎛
⎜⎜⎜
⎜⎝
P(t)
P(ω t)
...
P(ω
n−1 t)
⎞
⎟⎟⎟
⎟⎠
V
−1 (51)
where ω isaprimitive n-throotofunityand V isablockVandermondematrix
V =
⎛
⎜⎜
⎜⎜⎜
⎜⎜⎝
II ··· I
H
0 H1 ··· Hn−1
H2
0 H2
1 ··· H2
n−1
...
...
...
Hn−1
0 Hn−1
1 ··· Hn−1
n−1
⎞
⎟⎟
⎟⎟⎟
⎟⎟⎠
,H
i = ωi diag(t,... ,t). (52)
Wereferto[ 24]fordetails.Inparticular,wehave
det
⎛
⎜⎜
⎜⎜⎜
⎜⎜⎝
W
0 W1 ··· Wn−2 Wn−1
tnWn−1 W0 ··· Wn−3 Wn−2
...
... ... ...
tnW2 tnW3 ··· W0 W1
tnW1 tnW2 ··· tnWn−1 W0
⎞
⎟⎟
⎟⎟⎟
⎟⎟⎠
=
∏
ωn=1
det P(ω t) (53)
where,bydeﬁnition,
P(ω t) =
n−1∑
r=0
Wr(ω t)r
=
n−1∑
r=0
( ∑
k∈Z
∑
□
G□
nk+rdiag(ζ□ )(ωt)nk
)
(ωt)r
=
n−1∑
r=0
∑
k∈Z
( ∑
□
G□
nk+rdiag(ζ□ )
)
tnk+rωnk+r
=
∑
k∈Z
( ∑
□
G□
k diag(ζ□ )
)
(ω t)k (since ωn = 1).
Combiningtheabovecalculations,weobtain
τCS(T (n),t n) =
∏
ωn=1
det
( ∑
k∈Z
∑
□ G□
k diag(ζ□ )(ω t)k
)
∏ N
j=1 ζ
fj
j ζ
′f ′
j
j ζ
′′f ′′
j
j
=
∏
ωn=1
τCS(T ,ω t). (54)
⊓⊔
Proof of Theorem 1.8 Let R(t) = ∑
□ G□ (t)diag( ζ□ )a n dRi(t)d e n o t ei t si-th row. Since
the sum of all rows ofG□ (1) = G□ is (2,... ,2) andζj + ζ′
j + ζ′′
j = 0, the sumR1(1) +
···+ RN(1)isazerovector.Itfollowsthatdet R(1) = 0andthus τCS(T ,1) = 0.
S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37 Page 19 of 23 37
Sincethedeterminantisamultilinearmap,wehave
∂
∂t
⏐⏐⏐⏐
t=1
det R(t) =
N∑
i=1
det
⎛
⎜⎜⎜⎜
⎜⎜⎜⎝
R
1(1)
...
∂
∂t
⏐⏐
t=1 Ri(t)
..
.
R
N(1)
⎞
⎟⎟⎟⎟
⎟⎟⎟⎠
. (55)
For i ⁄= N, we exchange thei-th row
∂
∂t
⏐⏐
t=1 Ri(t)w i t ht h eN-th rowRN(1) and replace
RN(1)by −R1(1) −···− RN−1(1).Thenaftersomeelementaryrowoperations,weobtain
∂
∂t
⏐⏐⏐⏐
t=1
det R(t) =
N∑
i=1
det
⎛
⎜⎜⎜⎜⎝
R1(1)
..
.
R
N−1(1)
∂
∂t
⏐⏐
t=1 Ri(t)
⎞
⎟⎟⎟⎟⎠
= det
⎛
⎜⎜⎜⎜⎝
R1(1)
..
.
R
N−1(1)
∂
∂t
⏐⏐
t=1
∑ N
i=1 Ri(t)
⎞
⎟⎟⎟⎟⎠
. (56)
Comparing the deﬁnitions of equation ( 20)a n d( 22), it suﬃces to show that
∂
∂t
⏐⏐
t=1
∑ N
i=1 Ri(t) agrees with 1
2
∑
□ C□
λ diag(ζ□ ) up to linear combination of
R1(1),... ,R N(1).
Let ~/Sigma1be the pre-image of the peripheral torus/Sigma1under the covering map~M → M.
Note that T induces a triangulation of~/Sigma1where vertices and triangles of~/Sigma1correspond
toedgesandtetrahedraof ~T ,respectively.Foreachtriangle /Delta1of ~/Sigma1correspondingtothe
tetrahedron μk · ~/Delta1j,weassigna corner parameter t k log z□
j toeachcornerof /Delta1according
to the quad type of/Delta1j. Then the sumri(t) of corner parameters around a vertex of~/Sigma1
correspondingtotheedge ~ei is
ri(t) =
N∑
j=1
∑
□
(G□ (t))ij log z□
j . (57)
Itfollowsthat(seeEquation( 6))
Ri(t) =
(
∂
∂z1 ri(t) ··· ∂
∂zN
ri(t)
)
. (58)
We choose any lift~λ of λ to ~/Sigma1.S i n c eα(λ) = 0, ~λ is still a loop in~/Sigma1. Up to homotopy,
we may assume that~λ is an edge-path in~/Sigma1so that the surfaceS bounded by~λ and μ ·~λ
istriangulated.Hereweview S asaclosedcylinderwhoseboundaryisconsistedof ~λand
μ ·~λ.Let cλ(t)(resp., ˇcλ(t))bethesumofcornerparametersin S thatareadjacent(resp.,
not adjacent) to~λ. By deﬁnition, the equationcλ(1) = 0 represents the completeness
equationof λ.Hence,
∑
□
C□
λ diag(ζ□ ) =
(
∂
∂z1 cλ(1) ··· ∂
∂zN
cλ(1)
)
. (59)
Also,since S consistsoftrianglesand ζj + ζ′
j + ζ′′
j = 0forall j,wehave
∂
∂zj
(cλ(t) +ˇcλ(t)) = 0. (60)
Ontheotherhand, tcλ(t)isthesumofcornerparametersadjacentto μ·~λandnotin S.It
followsthatthesumofcornerparametersaroundverticesin S\~λisgivenby tcλ(t)+ˇcλ(t).
Since S\~λisafundamentaldomainof /Sigma1,exactlytwoverticesin S \~λcorrespondtoalift
37 Page 20 of 23 S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37
of ei foreach1 ≤ i ≤ N.Itfollowsthat
tcλ(t) +ˇcλ(t) =
N∑
i=1
(tai + tbi) ri(t). (61)
forsome ai and bi ∈ Zandthus
∂
∂t
⏐⏐
⏐⏐
t=1
(tcλ(t) +ˇcλ(t)) =
N∑
i=1
(ai + bi)ri(1) +2 ∂
∂t
⏐⏐
⏐⏐
t=1
N∑
i=1
ri(t). (62)
Takingthepartialderivativewithrespectto zj,weobtain
∂
∂t
⏐⏐
⏐⏐
t=1
∂
∂zj
N∑
i=1
ri(t) = 1
2
∂
∂zj
∂
∂t
⏐⏐
⏐⏐
t=1
(tcλ(t) +ˇcλ(t)) − 1
2
N∑
i=1
(ai + bi) ∂
∂zj
ri(1) (63)
= 1
2
∂
∂zj
cλ(1) − 1
2
N∑
i=1
(ai + bi) ∂
∂zj
ri(1) , (64)
where the second equation is followed from the equation (60)w i t ht h ef a c ttcλ(t) +
ˇcλ(t) = (t − 1)cλ(t) + cλ(t) + ˇcλ(t). Combining the equations (58), (59), and (64), we
obtainthedesiredresultthat ∂
∂t
⏐⏐
t=1
∑ N
i=1 Ri(t)agreeswith 1
2
∑
□ C□
λ diag(ζ□ )uptolinear
combinationof R1(1),... ,R N(1):
∂
∂t
⏐⏐⏐⏐
t=1
N∑
i=1
Ri(t) = 1
2
∑
□
C□
λ diag(ζ□ ) + 1
2
N∑
i=1
(ai + bi)Ri(1). (65)
⊓⊔
Remark 4.1 RewritingEquation( 65)intermsofNZmatrices,wehave
Xλ =
⎛
⎜⎜
⎜⎜⎜⎝
x
1(1)
..
.
x
N−1(1)
2 d
dt
⏐⏐⏐
t=1
(x1(t) +···+ xN(t))
⎞
⎟⎟
⎟⎟⎟⎠
for X = A and Bwhere x
1(t),... ,x N(t)aretherowsof X(t).
Proof of Corollary 1.9 Thestatementisequivalentto
det
(
A(t)diag( ζ) + B(t)diag( ζ′′)
)
= εtr det
(
A(1/t)diag( ζ) + B(1/t)diag( ζ′′)
)
(66)
forsome ε =± 1andsomeinteger randsomechoiceofquadsof T .Wemakesuchachoice
such thatB is non-singular. This is always possible; see [6, App.A]. Then, detB(t) ⁄= 0,
since B(1) = B.Conjecture 1.4impliesthatdet B(t) = εtr det B(1/t) ⁄= 0.This,combined
withTheorem 1.2gives
det
(
A(t)diag( ζ) + B(t)diag( ζ′′)
)
= det B(t)det
(
B(t)−1A(t) +diag(ζ′′/ζ)
)
det(diag(ζ))
= εtr det B(1/t)det
(
B(1/t)−1A(1/t) +diag(ζ′′/ζ)
)
det(diag(ζ))
= εtr det
(
A(1/t)diag( ζ) + B(1/t)diag( ζ′′)
)
NotethatTheorem 1.2impliesthat B(t)−1A(t) = (B(1/t)−1A(1/t))T whichisusedinthe
secondequalityabove. ⊓⊔
S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37 Page 21 of 23 37
We end this section by giving a proof of Equation (26). Taking the derivative of Equa-
tion(25)at t = 1andthensimplifyingtheresultbyTheorem 1.8,weobtain
τCS
λ (T (n))
τCS
λ (T ) = 1
n
∏
ωn=1
ω⁄=1
τCS(T ,w) (67)
which is equivalent to Equation (26) due to Theorem 4.1 of [23] (explicitly, the ratio
τCS
λ (T )/τCS
μ (T )isthecuspshapeof M and τCS
λ (T (n))/τCS
μ (T (n))is ntimesofthat).
