---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-008-diagrams-for-2-categories
section_title: "Diagrams for 2-categories"
section_number: null
pages: 12-13
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
A 2-category diagramfor a 2-categoryC is a direct generalisation of a diagram for a monoidal category. It
is a PL stratification∅⊂ X0⊂X1⊂X2 = [0, 1]2 of the unit square. Elements ofX0 are calledvertices,
connected components ofX1\X0 lines and connected components ofX2\X1 regions of the diagram.
Lines may end at the top and bottom of the square only and all vertices are in the interior. A diagram is
called progressive, if its horizontal projection is regular, i.e. its restriction to each line is a PL isomorphism
onto the image. It is calledgeneric, if no two vertices are at the same height. In pictures, we often omit the
unit square that borders the diagram for better legibility.
Regions in the diagram are labeled by objects ofC, lines by 1-morphisms and vertices by 2-morphisms.
Diagrams are read from top to bottom, and can be composed horizontally if the top of one diagram matches
the bottom of the other. This corresponds to the vertical composition of 2-morphisms. Horizontal composition
is from the right to the left. This is analogous to the usual calculus for monoidal categories, up to the fact
that regions of the diagrams are labeled with objects, lines with 1-morphisms and vertices with 2-morphisms.
A diagram whose right-hand side is labeled by an objectA, whose left-hand side by an objectB and with
lines at its upper and lower boundary labeled with 1-morphismsF1,...,F n and G1,...,G m, from the right
to the left, describes a 2-morphismν :Fn··· F1⇒Gm··· G1 between 1-morphismsFn··· F1 :A→B and
Gm··· G1 :A→B . This 2-morphism is obtained by first horizontally composing the 2-morphisms at the
vertices in the diagram with the 1-morphisms on the lines to the left and right and then composing the
resulting 2-morphisms in their vertical order.
Example 2.1. The diagram
F
G H
K
L
ρ
σ
MP
Q
N (30)
12
for the 2-category Cat with functorsK,L :M→P , F :P→N , H :P→Q and G :Q→N and natural
transformationsσ :K⇒L and ρ :F⇒GH describes the natural transformation(ρL)◦ (Fσ ) :FK⇒GHL
with component morphismsρL(m)◦F (σm) :FK (m)→FL (m)→GHL(m).
It is shown in [JS91, Th. 1.12] in the smooth context, see also [BMS12, Th. 2.12] for the PL setting, that
2-category diagrams represent the same 2-morphisms if they are related by PL isotopies that start at the
identity and define a one-parameter family of isomorphisms of diagrams. An isomorphism of diagrams is a
PL homeomorphism that is the identity on the boundary of the diagram and such that the homeomorphism
and its inverse preserve all skeleta of the diagram. This invariance is a consequence of the identity
F
G
H
K
ν
µ ABC =
F
G
H
K
ν
µ
ABC
(Gµ)◦ (νH ) = (νK)◦ (Fµ ).
(31)
for all 1-morphismsF,G :B→C and H,K :A→B and 2-morphismsν :F⇒G and µ :H⇒K. It allows
one to associate 2-morphisms to non-generic diagrams by perturbing them to generic ones. In the 2-category
Cat this identity expresses the naturality of natural transformations.
