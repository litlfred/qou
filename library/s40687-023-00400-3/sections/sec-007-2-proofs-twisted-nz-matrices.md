---
doc_id: s40687-023-00400-3
doc_title: "bonn.mpg.de/stavros 2MaxPlanckInstitutefor Mathematics,Bonn,Germany Fulllistofauthorinformationis availableattheendofthearticle DedicatedtoWalterNeumann andDonZagier,withadmiration"
section_id: sec-007-2-proofs-twisted-nz-matrices
section_title: "Proofs: twisted NZ matrices"
section_number: 2
pages: 9-12
source_pdf: s40687-023-00400-3.pdf
source_sha256: fd7638a8cf512a99
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
duplicate_of: "arxiv-2109.00379v1"
---
In this section, we give proofs of the properties of the twisted NZ matrices, namely the
relation to the NZ matrices of cyclic covers (Theorem1.1), the symplectic properties
(Theorem1.2),andthebehaviorunder2–3Pachnermoves(Theorem 1.5).
Proof of Theorem 1.1 It is clear thatT (n) has nN tetrahedra, as T has N tetrahedra /Delta1j,
j = 1,... ,N . Fixing a lift~/Delta1j of each/Delta1j to the inﬁnite cyclic cover, we choose lifts of the
tetrahedraof T (n) by μk · ~/Delta1j for k = 0,... ,n −1.Similarly,wechooseliftsoftheedgesof
T (n).Thenitisclearfromtheconstructionofthe n-foldcycliccoverthat
G(n)□
k =
⎛
⎜⎜
⎜⎜⎝
G
□
nk G□
nk+1
··· G□
nk+n−1
G□
nk−1 G□
nk ··· G□
nk+n−2
..
.
..
. ... ..
.
G
□
nk−n+1 G□
nk−n+2 ··· G□
nk
⎞
⎟⎟
⎟⎟⎠
(28)
forall k ∈
Z,whichimplies
G(n)□ =
⎛
⎜⎜
⎜⎜⎝
∑
r≡0 G□
r
∑
r≡1 G□
r ··· ∑
r≡n−1 G□
r∑
r≡n−1 G□
r
∑
r≡0 G□
r ··· ∑
r≡n−2 G□
r
..
.
..
. ... ..
.∑
r≡1 G□
r
∑
r≡2 G□
r ··· ∑
r≡0 G□
r
⎞
⎟⎟
⎟⎟⎠
(29)
ThiscompletestheproofofTheorem 1.1. ⊓⊔
Proof of Theorem 1.2 FollowingNeumann[ 21],weconsiderthe
Z[t±1]-module V gener-
atedbyvariables Zj ,Z ′
j ,Z ′′
j subjecttolinearrelations Zj + Z′
j + Z′′
j = 0for1 ≤ j ≤ N.We
deﬁneasymplecticformon V as
⟨Zi,Z ′′
j ⟩=⟨Z′
i ,Z j⟩=⟨Z′′
i ,Z ′
j⟩= δij (30)
and
⟨cZj ,Z ′′
j ⟩=⟨Zj ,¯cZ′′
j ⟩= c, c ∈ Z[t±1]
where δij is the Kronecker delta and ¯ :Z[t±1] → Z[t±1] is the involution induced
from the inversiont ↦→ t−1. Note that⟨Z′′
i ,Z j⟩=⟨Z′′
i ,−Z′
j − Z′′
j ⟩=− δij and similarly,
⟨Zi,Z ′
j⟩=⟨Z′
i ,Z ′′
j ⟩=− δij.
Weassociateanelement Ei ∈ V toeachedge ei of T as
Ei =
N∑
j=1
(
G(t)ij Zj + G′(t)ij Z′
j + G′′(t)ij Z′′
j
)
. (31)
Inwhatfollows,weusethesameargumentgivenintheproofof[ 3,Thm.3.6]toshowthat
⟨Ea,E b⟩= 0 forall1 ≤ a, b ≤ N. (32)
Consideringthelinearexpansionof ⟨Ea,E b⟩usingtheequation( 31),wehaveanon-trivial
termwhentheedges ea and eb appearinsome /Delta1j withdiﬀerentshapeparameters.Without
loss of generality, suppose thatea and eb have parameters Zj and Z′′
j , respectively. It is
clear that~/Delta1j contains μα ·~ea and μβ ·~eb for someα and β ∈ Z. Equivalently,μ−α · ~/Delta1j
and μ−β · ~/Delta1j areattachedto ~ea and~eb,respectively.Wethusgetanon-trivialterm
⟨t−α Zj ,t −β Z′′
j ⟩= tβ−α (33)
37 Page 10 of 23 S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37
inthelinearexpansionfromthetriple( ~/Delta1j ,μα ·~ea,μβ ·~eb).Ontheotherhand,considering
the face-pairing of the face of/Delta1j containing ea and eb, there is another tetrahedron/Delta1i
(possibly i = j), which also contains bothea and eb. It follows that~/Delta1i contains μα+γ ·~ea
and μβ+γ ·~eb for someγ ∈ Z. From this triple (~/Delta1i,μα+γ ·~ea,μβ+γ ·~eb), we get another
non-trivial term−t(β+γ)−(α+γ) =− tβ−α which we can pair with the term (33) to cancel
out.Notethatwehavetheminussignhere,sincetheface-pairingisorientation-reversing:
theshapeparametersof e
a and eb for /Delta1i areeither( Zi,Z ′
i),( Z′
i ,Z ′′
i ),or( Z′′
i ,Z i).Inthisway,
every non-trivial term that appears in the expansion of⟨Ea,E b⟩is paired to cancel out.
Thisprovestheequation( 32).Wethendirectlyobtainthedesiredequation( 17),sincewe
have
⟨Ea,E b⟩=
N∑
j=1
⟨
G(t)aj Zj + G′(t)aj Z′
j + G′′(t)aj Z′′
j , G(t)bj Zj + G′(t)bj Z′
j + G′′(t)bj Z′′
j
⟩
=
N∑
j=1
(
G(t)aj
(
G′′(1/t)bj − G′(1/t)bj
)
+ G′(t)aj
(
G(1/t)bj − G′′(1/t)bj
)
+ G′′(t)aj
(
G′(1/t)bj − G(1/t)bj
))
=
N∑
j=1
( (
G(t)aj − G′(t)aj
)(
G′′(1/t)bj − G′(1/t)bj
)
−
(
G′′(t)aj − G′(t)aj
)(
G(1/t)bj − G′(1/t)bj
))
=
N∑
j=1
(
A(t)aj B(1/t)bj − B(t)aj A(1/t)bj
)
.
⊓⊔
Proof of Theorem 1.5 Recall that a 2–3 Pachner move onT is determined by two tetra-
hedra /Delta1α and /Delta1β with a common face inT . Dividing the bipyramid/Delta1α ∪ /Delta1β into three
tetrahedra /Delta1a,/Delta1b, and /Delta1c as in Fig.2, we obtain a new ideal triangulationT with one
additional edge e0. We choose lifts of the ﬁve tetrahedra/Delta1α, /Delta1β, /Delta1a, /Delta1b, /Delta1c and the
edge e0 (to the inﬁnite cyclic cover) such that~/Delta1α ∪ ~/Delta1β and ~/Delta1a ∪ ~/Delta1b ∪ ~/Delta1c are the same
bipyramidcontaining ~e0.Notethatthe(twisted)gluingequationof e0 is
log z′
a +log z′
b +log z′
c = 2π
√
−1. (34)
There are nine edges on the bipyramid whose gluing equations are aﬀected by the
Pachner move: three at the triangle of the base pyramid and six others on the bipyramid
butnotonitsbase.Thesixedgesgive
log z
α = log zb +log z′′
c log z′
α = log z′′
a +log zc log z′′
α = log za +log z′′
b
log zβ = log z′′
b +log zc log z′
β = log z′′
a +log zb log z′′
β = log za +log z′′
c , (35)
andthethreeedgesgive
log zα +log zβ = log z′
a log z′
α +log z′′
β = log z′
b log z′′
α +log z′
β = log z′
c. (36)
The relations (36) are obtained from the relations (35) up to the gluing equation (34)o f
e0 andtherelationlog z +log z′+log z′′= π√−1.Forinstance,
log zα +log zβ = log zb +log z′′
c +log z′′
b +log zc
S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37 Page 11 of 23 37
Fig. 2 2-3Pachnermove
= 2π
√
−1 −log z′
b −log z′
c
= log z′
a.
Therefore, we can obtain the twisted gluing equation matricesG
□
(t) for T from the
twisted gluing equation matrices forT by substituting logz□
α and logz□
β in terms of the
right hand side of equation (35) and the substitution is correct up to the gluing equation
of e0 and the relation logz + log z′+ log z′′= π√−1. In matrix form, this implies that
forsomelowertriangularmatrix Q =
(
10
∗ IN
)
andanintegermatrix C,wehave
(
G(t)a G(t)b G(t)c
)
= Q
( 00 0
G′′(t)α + G′′(t)β G(t)α + G′(t)β G′(t)α + G(t)β
)
+ C,
(
G
′
(t)a G
′
(t)b G
′
(t)c
)
= Q
( 111
000
)
+ C,
(
G
′′
(t)a G
′′
(t)b G
′′
(t)c
)
= Q
( 000
G′(t)α + G′(t)β G′′(t)α + G(t)β G(t)α + G′′(t)β
)
+ C.
(37)
Here IN istheidentitymatrixofsize N and Xj isthe j-thcolumnofamatrix X.Multiplying
P =
(
10
G′(t)α + G′(t)β IN
)
Q−1 onbothsidesofEquation( 37),weobtain
P
(
G(t)a G(t)b G(t)c
)
=
( 00 0
G′′(t)α + G′′(t)β G(t)α + G′(t)β G′(t)α + G(t)β
)
+ PC,
P
(
G
′
(t)a G
′
(t)b G
′
(t)c
)
=
( 111
G′(t)α + G′(t)β G′(t)α + G′(t)β G′(t)α + G′(t)β
)
+ PC,
P
(
G
′′
(t)a G
′′
(t)b G
′′
(t)c
)
=
( 000
G′(t)α + G′(t)β G′′(t)α + G(t)β G(t)α + G′′(t)β
)
+ PC .
(38)
Itfollowsthat
P
(
A(t)a A(t)b A(t)c
)
=
(
−1 −1 −1
B(t)α + B(t)β A(t)α A(t)β
)
,
P
(
B(t)a B(t)b B(t)c
)
=
(
−1 −1 −1
0A (t)β + B(t)α A(t)α + B(t)β
)
,
where P isalowertriangularmatrixwith1’sonthediagonal. ⊓⊔
37 Page 12 of 23 S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37
Fig. 3 Thetriangulationoftheperipheraltorusof4 1
