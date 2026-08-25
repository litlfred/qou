---
doc_id: arxiv-1108.4389v1
doc_title: "b partition functions of two mirror 3d N = 2 gauge theories are equal. Three-dimensional N = 2 ﬁeld theories associated to 3-manifolds can be thought of as theories that describe b"
section_id: sec-025-42-the-bipyramid-and-the-23-move
section_title: "The bipyramid and the 2–3 move"
section_number: 4.2
pages: 33-36
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
Let’s consider the theory of the bipyramid, as constructed from two diﬀerent triangulations.
To keep things simple, we will focus on the “equatorial” polarization Π = Π eq for the bipyra-
mid, as deﬁned in ( 2.22) or (2.34). In particular, the three equatorial edges of the bipyramid
are position coordinates in Π. We keep the same notation as in Section 2, and repeat Figure
15 here as a visual reference.
If we decompose the bipyramid into three tetrahedra, then according to our rules T{∆i},Π
is a theory of three free chiral multiplets, coupled to a backgroundU(1)3, with some extra CS
couplings determined by our choice of momenta in Π. The operator associated to the unique
internal edge is simply the product of the three chiral ﬁelds. Hence TM,Π is simply the XYZ
model, with appropriate coupling to the unbroken U(1)2 ﬂavor symmetry. The operators
associated to the external edges are the three chiral multiplets themselves.
– 32 –
z
z￿z￿￿
z
z￿
z￿￿
w
w￿
w￿￿
w
w￿
w￿￿
y
y￿
y￿￿
y
y￿
y￿￿
r
r￿
r￿￿
r
r￿
r￿￿
s
s￿
s￿￿
s
s￿ s￿￿
Figure 19: Decompositions of the bipyramid, with labelled edge coordinates (Figure 15).
Being more explicit, we can start with a product polarization{Πi} ={ΠZ, ΠW, ΠY}, such
thatZ,W,Y are coordinates andZ′′,W′′,Y ′′ are momenta. In the equatorial polarization Πeq,
we know that X1 = Z and X2 = W are positions while P1 = Z′′ +Y′ and P2 = W′′ +Y′
are momenta; we therefore choose a compatible polarization ˜Π on P{∂∆i} with positions
X1,X 2,C and momentaP1,P 2, Γ, whereC =X +Y +Z and Γ =−Y′. The aﬃne symplectic
transformation g from{Πi} to ˜Π is encoded as


X1
X2
C
P1
P2
Γ


=


1 0 0 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 1 0 −1
0 0 0 0 1 −1
0 0 0 0 0 1




1 0 0 0 0 0
0 1 0 0 0 0
0 0 1 0 0 0
0 0 0 1 0 0
0 0 0 0 1 0
0 0 1 0 0 1




Z
W
Y
Z′′
W′′
Y′′


+


0
0
0
iπ
iπ
−iπ


, (4.7)
which involves a T -type transformation, a GL-type transformation, and a shift that will not
be visible at the level of Lagrangians. Thus, starting with a Lagrangian description
L{Πi}[VZ,VW,VY ] = 1
4π
∫
d4θ
(
− 1
2ΣZVZ− 1
2ΣWVW− 1
2ΣYVY
)
+
∫
d4θ
(
φ†
ZeVZφZ +φ†
WeVWφW +φ†
YeVYφY
)
(4.8)
for T{∆i},{Πi}, we construct the Lagrangian for T{∆i},˜Π =g◦T{∆i},{Πi} simply as
L˜Π[VX1,VX2,VC] =L{Πi}[VX1,VX2,VC−VX1−VX2]+ 1
4π
∫
d4θ(ΣC−ΣX1−ΣX2) (VC−VX1−VX2),
(4.9)
in other words by adding a level 1 Chern-Simons term forVY , and redeﬁningVZ =VX1, VW =
VX2, and VY =VC−VX1−VX2. It is trivial to see that the elementary operator
OC≡φZφWφY (4.10)
exists in T{∆i},˜Π, as do the individual operators φZ,φW,φY associated to the equatorial
external edges. The bipyramid theory TM,Πeq is then deﬁned by adding the superpotential
– 33 –
W =OC to (4.9), which forces VC =θ¯θmC = 0; direct calculation then shows
LM,Πeq[VX1,VX2] = 1
4π
∫
d4θ ΣX1VX2 +
∫
d4θ
(
φ†
ZeVX1φZ +φ†
WeVX2φW +φ†
Ye−VX1−VX2φY
)
+
∫ (
d2θφZφWφY +c.c.
)
. (4.11)
This is the promised XYZ model, with slightly redeﬁned U(1)2 symmetries, and a mixed
Chern-Simons term.
If we decompose the bipyramid into two tetrahedra instead of three, we need no superpo-
tential. On the other hand, the transformation g from the polarization{ΠR, ΠS′′} for the two
tetrahedra to Πeq is non-trivial: as the positions are X1 =R +S′′,X2 =R′′ +S, and R′ +S′,
it is easy to see that g involves gauging (with no CS coupling) the U(1) under which the two
chiral multiplets have opposite charge. Hence with this deﬁnition TM,Π is simply Nf = 1
SQED, with appropriate coupling to the U(1)2 ﬂavor symmetry. The operator associated to
the edge coordinate X1 =R +S′′ is simply the meson operator.
Again, one can go through explicit Lagrangian manipulations as above. Starting from a
polarization{Πi} ={ΠR, ΠS′′}∼ (R,S′′;R′′,S′) we reach the equatorial polarization Π eq∼
(X1,X 2;P1,P 2) via a symplectic transformation g =gSgTgU, with
gS =


1 0 0 0
0 0 0 −1
0 0 1 0
0 1 0 0

, g T =


1 0 0 0
0 1 0 0
0 0 1 0
0 1 0 1

, g U =


1 1 0 0
0 1 0 0
0 0 1 0
0 0−1 1

 . (4.12)
Therefore, we obtainLM,Πeq[VX1,VX2] by starting with
L{∆i},{Πi}[VR,VS′′] = 1
4π
∫
d4θ
(
− 1
2ΣRVR− 1
2ΣS′′VS′′
)
+
∫
d4θ
(
φ†
ReVRφR +φ†
S′′eVS′′φS′′
)
,
(4.13)
redeﬁning theU(1)2 symmetry, adding a Chern-Simons term, and gauging aU(1). A straight-
forward calculation produces 13
LM,Πeq[VX1,VX2] = 1
4π
∫
d4θ
(
ΣX1VX2 + (ΣX1 + 2ΣX2)V
)
+
∫
d4θ
(
φ†
ReV + 1
2VX1φR +φ†
S′′e−V + 1
2VX1φS′′
)
, (4.14)
with the U(1) gauge multiplet V dynamical. This is precisely Nf = 1 SQED, with a mixed
Chern-Simons coupling, and slightly redeﬁned U(1)2 symmetry. The meson operator OX1≡
φRφS′′ is obviously charged underVX1. We know that SQED also has two monopole operators
13In the last step of the derivation of ( 4.14), we shifted the dynamical gauge multiplet V → V + 1
2VX1,
thereby adding to the ‘X1’ ﬂavor current a half-integral multiplet of the gauge current. This non-integral shift
is not necessary, but can be made sense of because the multiplet VX1 =θ¯θmX1 is nondynamical. In the form
(4.14) of the Lagrangian, the identiﬁcation of 1
2VX1 with an axial ﬂavor multiplet becomes immediate.
– 34 –
v+ and v−, and from the form of the FI term in ( 4.14) we see that they must be charged
under the combinations VX2 and−VX1−VX2, respectively. Thus, they correspond to the
remaining two equatorial edges.
Thanks to the basicN = 2 mirror symmetry statement (3.19), our construction gives the
same theoryTM,Π for the bipyramid, no matter how we triangulate it . By carefully comparing
the Lagrangian descriptions (4.11) and (4.14), we see that the three equatorial edge operators
— elementary ﬁelds in the XYZ model and a meson/monopoles in SQED — are mapped to
each other by mirror symmetry, and their coupling to the background U(1) gauge multiplets
VX1 and VX2 coincide perfectly.
One can also repeat the exercise for the longitudinal polarization. The two triangulations
give respectivelyN = 4 SQED with Nf = 1 and the theory of a free hypermultiplet, i.e. the
basicN = 4 mirror pair. This is a useful exercise in order to show that the operators
associated to longitudinal edges by the two polarizations are also mapped into each other by
mirror symmetry.
With this result, we are in position to argue that the theories TM,Π deﬁned by diﬀerent
triangulations of the same three-manifoldM are mirror to each other. Diﬀerent triangulations
are related by a sequence of 2 − 3 moves.14 Two triangulations that diﬀer by a 2 − 3 move
give two deﬁnitions of the theory TM,Π that diﬀer only by a basic mirror symmetry relation.
The mirror symmetry acts on the degrees of freedom associated to the particular bipyramid
that is decomposed in two diﬀerent ways in the course of a 2 − 3 move.
