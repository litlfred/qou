---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-014-polygon-diagrams
section_title: "Polygon diagrams"
section_number: null
pages: 19-24
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
By definition, the evaluation of a bordered diagram is an endomorphism of the object labeling the left-hand
side of the diagram. For bordered diagrams that involve data from the pivotal 2-categoryBimodθ(C,D) one
can take the bimodule trace of this morphism to obtain a complex number.
19
Definition 2.11. LetD be a bordered diagram labeled with data fromBimodθ(C,D). The cyclic evaluation
of D is the trace of its evaluation.
The cyclic evaluation of a bordered diagram has better invariance properties than the evaluation of a bordered
diagram. This is most easily seen by using a diagrammatic calculus for bimodule traces, which is essentially
the calculus from [S13]. If a finite semisimple categoryM is equipped with a traceθ as in Definition 1.13, we
denote the associated morphismsθm : EndM(m)→ C by horizontal lines at the upper and lower ends of the
lines representing endomorphisms ofm. The cyclicity condition from Definition 1.13 then takes the form
m
m
α
β
m′ =
m′
m′
β
α
m
(48)
and the compatibility conditions between the trace and theC-module orD-right module structure read
m
m
c
c
α =
m
m
c α
m
m
d
d
α =
m
m
d α
(49)
For a spherical fusion categoryC as a module or right module category over itself, we use both, the diagrams
from (29) and the diagrams for module traces. In the latter we draw thin black or grey lines instead of thick
coloured lines for edges labeled byC.
By Theorem 1.17 and Corollaries 1.18 to 1.20, (bi)module traces induce the pivotal 2-category structures
on the 2-categoriesModθ(C) and Bimodθ(C,D). The defining condition(23) on the component morphisms
ωF :Fll⇒F of the pivots and identity (25) are expressed diagrammatically as
n
n
m
F α
β
NM
F
(23)
=
n
n
m
α
β
F
MN
m
m
F
F
α
M
N (25)
=
m
m
F αN
M
(50)
By definition, the evaluation of a bordered diagramD′ for a 2-category diagramD depends on the natural
transformation represented byD and on the data labeling the boundary ofD′. In contrast, the cyclic
evaluation of a bordered diagram for Bimodθ(C,D) depends only on the cyclic equivalence class of the
morphism represented byD, if the data at the boundary ofD′ is transformed accordingly.
Cyclic transformations of diagrams induce cyclic transformations of bordered diagrams. These modify the
underlying natural transformation, move the object labels at the boundary and modify the morphisms at the
boundary by moving them and composing them with the (co)evaluations from (32):
m
n
F
H
α
β
νp −→
m
n
F H
αd β
νm
p
(51)
20
p m
F
α
p
mF
α
p m
F
αd
p
m
F
α
α :p→F (m) αd =ϵF
m◦Fl(α) :Fl(p)→m
m
p
K
G
δ
γ
ν n −→
m
p
K G
δ γu
ν p
n
(52)
p n
G
γ
n
p
G
γ n p
G
γu
n
pG
γ
γ :G(n)→p γ u =Gl(γ)◦η′G
n :n→Gl(p).
Identity (33) ensures that moving an endpoint from the upper (lower) to the lower (upper) side of a diagram
and then up (down) again yields its original morphism label:(αu)d =α and (γu)d =γ. The pivotal structure
depicted in(34) ensures that this does not change the bimodule natural transformation labeling a vertex.
Transforming the boundary morphisms in this way extends cyclic transformations of diagrams to cyclic
transformations of bordered diagrams, as shown in Figure 1.
Lemma 2.12. LetC,D be spherical fusion categories andD, D′ bordered diagrams forBimodθ(C,D) that
are related by cyclic transformations. Then the cyclic evaluations ofD and D′ are equal.
Proof. For the cyclic transformation in(51) this follows from the cyclic invariance of the trace in(48) and its
compatibility conditions with the pivotal 2-category structure ofBimodθ(C,D) from (23), (25) and (50):
p
p
m
n
F
H
...
α
β
ν (48)
=
m
m
n
p
F
F
H
...
β
α
ν
(50)
=
m
m
n
p
F H
...
β
α
ν
21
p m
n
F
G H
ν
α
βγ
P M
N
m
p n
F
G H
ν
αd βγ
P
M
N
m n
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
m p
F
GH
ν
αdβ γ
P
M
N
pm
F
G
H
n
ν
αdβ
γu
PM
N
pmn
F
G
H
ν
αdβγ
PM
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
ν (33)
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
Bimodθ(C,D) in their interior and endpoints of lines at the boundary. Interior lines are oriented, and the
object labels at the boundary are assigned to the segments between their endpoints. Vertices in the interior
are labeled with cyclic equivalence classes of bimodule natural transformations. To the line endpoints at the
boundary we assign elements of the corresponding morphism spaces at the top of a bordered diagram, if the
line is incoming at the boundary, and the one for the bottom of a bordered diagram, if it is outgoing. In the
following, we often represent these diagrams by polygons and hence call them polygon diagrams.
Definition 2.13.
1. A polygon diagramfor Bimodθ(C,D) is a cyclic equivalence class of bordered diagrams, represented
by a polygon with a diagram forBimodθ(C,D) in the interior such that all diagram lines are oriented
and end in internal vertices or at the sides of the polygon.
2. The evaluation ev(D) of a polygon diagramD is the cyclic evaluation of the associated equivalence
class of bordered diagrams.
It is clear from Lemma 2.12 that the labeling and the evaluation of a polygon diagram is invariant under
rotations of the polygon. Also, one may add additional sides without line endpoints and move endpoints
22
of lines from a side to an adjacent side, if the labels are adjusted accordingly. For instance, some polygon
diagrams for the diagram from Figure 1 are given by
F
G H
n
p m
ν
P M
N
α
βγ
=
G
H F
m
n p
ν
N P
M
γ
αβ
=
H
F G
p
m n
ν
M N
P
β
γα
and also by
H
GF ν
m n
pp
M N
P
α γ
β
=
H
G
F
ν
m n
np
M
N
P
α
γ
β
=
H
G
F
ν
m
m n
p
M
N
P
α
γ
β
Note that any diagram for a spherical fusion categoryC that describes the trace of an endomorphismϕ :c→c
is a polygon diagram forBimodθ(C,C) with cyclic evaluationtr(ϕ). In this case, all regions of the diagram
are labeled withC and all lines and vertices by data fromC.
We also consider mirror images of polygon diagrams. If the orientation of the lines is kept fixed, there is
no canonical data labeling such a mirror image. This would reverse the direction of a bimodule natural
transformation labeling a vertex, which is feasible only if it is an isomorphism. However, taking a mirror
image of a polygon diagramD for Bimodθ(C,D) and reversing the orientation of all lines yields a polygon
diagram D# for Bimodθ(D,C). This is obtained by replacing bimodule categories, functors and natural
transformations with their opposites from Examples 1.7 and 1.10, 7. Objects and morphisms at the boundary
of D are kept fixed, but a morphismα :a→b inM is interpreted as a morphismα :b→a inM#.
Definition 2.14. LetD be a polygon diagram labeled byBimodθ(C,D). The opposite polygon diagram
D# is the polygon diagram byBimodθ(D,C) obtained as follows:
• taking the mirror image ofD,
• reversing the orientation of each line inD,
• replacing each(C,D)-bimodule categoryM in D by the (D,C)-bimodule categoryM#,
• replacing each bimodule functorF :M→N in D by F # :M#→N #,
• replacing each bimodule natural transformationν :F⇒G in D by ν# :G#⇒F #,
• keeping the boundary data fixed.
Geometrically,D# is the polygon diagram obtained by looking atD from the back, behind the plane of
the drawing. The orientation reversal for lines is necessary, because a functor labeling a line goes from the
category on the left of the line to the category on the right, viewed in the direction of its orientation. Looking
at the diagram from the back exchanges left and right and hence reverses the orientation of the line.
Corollary 2.15. For any polygon diagramD one has ev(D) = ev(D#).
Proof. Taking the mirror image, reversing each line and replacing line labelsF :M→N byF # :M#→N #
replaces a functorF1··· Fn :M→N by the functor(F #
n )l··· (F #
1 )l = (F #
1 ··· F #
n )l :N #→M #. A bi-
module natural transformationν : F1··· Fn⇒ G1··· Gm in D is replaced by a natural transformation
from (F #
1 ··· F #
n )l to (G#
1··· G#
n )l in D′, which is a cyclic transform ofν# : G#
1··· G#
m ⇒ F #
1 ··· F #
n .
Each morphism α ∈ HomN (n,F (m)) in D is replaced by a morphism α ∈ HomM#(m, (F #)l(n)) =
HomM((F #)l(n),m ) which is related toα via the (co)unit of the adjunction (F #)l ⊣ F #. Identities
(33) and (34) and the induced bimodule trace on the opposite category (cf. Example 1.15) then ensure that
the evaluations ofD and D# are equal.
23
