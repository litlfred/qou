---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-014-polygon-diagrams
section_title: "Polygon diagrams"
section_number: null
pages: 19-24
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
Polygon diagrams
By definition, the evaluation of a bordered diagram is an endomorphism of the object labeling the left-hand
side of the diagram. For bordered diagrams that involve data from the pivotal 2-category Bimodθ(C, D) one
can take the bimodule trace of this morphism to obtain a complex number.
19
Definition 2.11. Let D be a bordered diagram labeled with data from Bimod?(C, D). The cyclic evaluation
of D is the trace of its evaluation.

The cyclic evaluation of a bordered diagram has better invariance properties than the evaluation of a bordered
diagram. This is most easily seen by using a diagrammatic calculus for bimodule traces, which is essentially
the calculus from [S13]. If a finite semisimple category M is equipped with a trace @ as in Definition 1.13, we
denote the associated morphisms 6, : Endy4(m) — C by horizontal lines at the upper and lower ends of the
lines representing endomorphisms of m. The cyclicity condition from Definition 1.13 then takes the form

m m’

m m (48)

and the compatibility conditions between the trace and the C-module or D-right module structure read

en “Tm Tm —™m
a = c a a = dh a
cf |m 1 ag jm an (49)

For a spherical fusion category C as a module or right module category over itself, we use both, the diagrams
from (29) and the diagrams for module traces. In the latter we draw thin black or grey lines instead of thick
coloured lines for edges labeled by C.

By Theorem 1.17 and Corollaries 1.18 to 1.20, (bi)module traces induce the pivotal 2-category structures
on the 2-categories Mod®(C) and Bimod®(C,D). The defining condition (23) on the component morphisms
w? ; F" = F of the pivots and identity (25) are expressed diagrammatically as

1
M iN n m™ Fwy M [m
Fi} Qa Qa nN aan
ae f ‘ ‘
. (23) ’ ' ‘\
mS " m N ’ a (25) FA N @a
ae N M4 B v t /
van ’ \ ’
4 n ‘In v Sou
Pe ae [mn 2 (50)

By definition, the evaluation of a bordered diagram D’ for a 2-category diagram D depends on the natural
transformation represented by D and on the data labeling the boundary of D’. In contrast, the cyclic
evaluation of a bordered diagram for Bimod®(C,D) depends only on the cyclic equivalence class of the
morphism represented by D, if the data at the boundary of D’ is transformed accordingly.

Cyclic transformations of diagrams induce cyclic transformations of bordered diagrams. These modify the
underlying natural transformation, move the object labels at the boundary and modify the morphisms at the
boundary by moving them and composing them with the (co)evaluations from (32):

Qa m m
Pp vee” —_ m ' *. (51)
HY AF HY
nr L__4___¢___
B at P B

20
f
Pp Qa m ' A
——. fe ——— ( a
' a” D at m ae
YF ” -
F m m
a:p—> F(m) at =F o F'(a): F'(p) 3m
oo m oon 2,
VK y 1
so! K aG
Vou — ys 3h ! 52
eid n Sap p (52)
YG ee
f
a p
' Gon n
YG *S ues
p ' n ‘ n x" P voN
—.— 7 ao
H
AG iy
Pp ' GP
7: G(n) > p = Gq) ome n> G'(p)

Identity (33) ensures that moving an endpoint from the upper (lower) to the lower (upper) side of a diagram
and then up (down) again yields its original morphism label: (a“)¢ = a and (y“)4 = y. The pivotal structure
depicted in (34) ensures that this does not change the bimodule natural transformation labeling a vertex.
Transforming the boundary morphisms in this way extends cyclic transformations of diagrams to cyclic
transformations of bordered diagrams, as shown in Figure 1.

Lemma 2.12. Let C,D be spherical fusion categories and D, D’ bordered diagrams for Bimod®(C, D) that

are related by cyclic transformations. Then the cyclic evaluations of D and D' are equal.

Proof. For the cyclic transformation in (51) this follows from the cyclic invariance of the trace in (48) and its
compatibility conditions with the pivotal 2-category structure of Bimod’(C,D) from (23), (25) and (50):

Pp m

a

Py’ m

ae

veer . n
oe B
H‘ |” Pp
‘43 a
p m

21
p
m
n
F
G
H
ν
α
β
γ
P
M
N
m
p
n
F
G
H
ν
αd
β
γ
P
M
N
m
n
p
F
G
H
ν
αd
βu
γ
P
M
N
n
m
p
F
G
H
ν
αd
β
γ
P
M
N
p
m
F
G
H
n
ν
αd
β
γu
P
M
N
p
m
n
F
G
H
ν
αd
β
γ
P
M
N
Figure 1: Some cyclic transformations of a bordered diagram.
For the cyclic transformation in (52) it is a direct consequence of identity (33):
m
n
p
K
G
δ
γ
ν
(33)
=
m
n
p
K
G
δ
γ
ν
Lemma 2.12 shows that the cyclic evaluation of a bordered diagram depends only on its cyclic equivalence
class. We therefore represent cyclic equivalence classes of bordered diagrams by discs with diagrams for
Bimodθ(C, D) in their interior and endpoints of lines at the boundary. Interior lines are oriented, and the
object labels at the boundary are assigned to the segments between their endpoints. Vertices in the interior
are labeled with cyclic equivalence classes of bimodule natural transformations. To the line endpoints at the
boundary we assign elements of the corresponding morphism spaces at the top of a bordered diagram, if the
line is incoming at the boundary, and the one for the bottom of a bordered diagram, if it is outgoing. In the
following, we often represent these diagrams by polygons and hence call them polygon diagrams.
Definition 2.13.
1. A polygon diagram for Bimodθ(C, D) is a cyclic equivalence class of bordered diagrams, represented
by a polygon with a diagram for Bimodθ(C, D) in the interior such that all diagram lines are oriented
and end in internal vertices or at the sides of the polygon.
2. The evaluation ev(D) of a polygon diagram D is the cyclic evaluation of the associated equivalence
class of bordered diagrams.
It is clear from Lemma 2.12 that the labeling and the evaluation of a polygon diagram is invariant under
rotations of the polygon. Also, one may add additional sides without line endpoints and move endpoints
22
of lines from a side to an adjacent side, if the labels are adjusted accordingly. For instance, some polygon
diagrams for the diagram from Figure 1 are given by

Pp

and also by
m B n m B n m B n
1 1 1
M HA N M Ha HA N
1 _ 1 _ 1
Qa es ee ean Qa po ern 4 N M vere y
P P GY Pa P
Pp Pp Pp Y nom a Pp

Note that any diagram for a spherical fusion category C that describes the trace of an endomorphism ¢ : c > c
is a polygon diagram for Bimod?(C,C) with cyclic evaluation tr(@). In this case, all regions of the diagram
are labeled with C and all lines and vertices by data from C.

We also consider mirror images of polygon diagrams. If the orientation of the lines is kept fixed, there is
no canonical data labeling such a mirror image. This would reverse the direction of a bimodule natural
transformation labeling a vertex, which is feasible only if it is an isomorphism. However, taking a mirror
image of a polygon diagram D for Bimod? (C,D) and reversing the orientation of all lines yields a polygon
diagram D* for Bimod®(D,C). This is obtained by replacing bimodule categories, functors and natural
transformations with their opposites from Examples 1.7 and 1.10, 7. Objects and morphisms at the boundary
of D are kept fixed, but a morphism a: a > b in M is interpreted as a morphism a: b > a in M*#.

Definition 2.14. Let D be a polygon diagram labeled by Bimod’ (C, D). The opposite polygon diagram
D* is the polygon diagram by Bimod’(D,C) obtained as follows:

« taking the mirror image of D,

« reversing the orientation of each line in D,

¢ replacing each (C,D)-bimodule category M in D by the (D,C)-bimodule category M*,
¢ replacing each bimodule functor F: M— N in D by F# : M# 4 N#,

¢ replacing each bimodule natural transformation v : F > G in D by v#: G# > F#,

« keeping the boundary data fixed.

Geometrically, D# is the polygon diagram obtained by looking at D from the back, behind the plane of
the drawing. The orientation reversal for lines is necessary, because a functor labeling a line goes from the
category on the left of the line to the category on the right, viewed in the direction of its orientation. Looking
at the diagram from the back exchanges left and right and hence reverses the orientation of the line.

Corollary 2.15. For any polygon diagram D one has ev(D) = ev(D*).

Proof. Taking the mirror image, reversing each line and replacing line labels F : M > N by F# : M#  N#
replaces a functor F,---F, : M— N by the functor (F#)!..-(F#)! = (F#... FP): N# = M#. A bi-
module natural transformation v : F\---F, = Gi---Gm in D is replaced by a natural transformation
from (Ff... F#)! to (G#---G#)! in D’, which is a cyclic transform of v# : G#...G# = Fi... F#.
Each morphism a € Homy(n,F(m)) in D is replaced by a morphism a € Hompye(m,(F*)!(n)) =
Hom ((F#)!(n),m) which is related to a via the (co)unit of the adjunction (F#)! 4 F#. Identities
(33) and (34) and the induced bimodule trace on the opposite category (cf. Example 1.15) then ensure that
the evaluations of D and D* are equal. O

23
