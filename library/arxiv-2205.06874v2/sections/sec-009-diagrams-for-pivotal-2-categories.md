---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-009-diagrams-for-pivotal-2-categories
section_title: "Diagrams for pivotal 2-categories"
section_number: null
pages: 13-14
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
If the 2-category under consideration is a pivotal 2-category in the sense [S15, Def. A.12] or, more strictly, a
planar 2-category in the sense of [BMS12, Def. 3.2.1], we use the diagrams for planar 2-categories introduced
in [BMS12, Def. 3.5]. The main examples areModθ(C) and Bimodθ(C,D) from Theorem 1.17.
The diagrams for pivotal 2-categories are essentially the diagrams for a pivotal monoidal category. The only
difference is that regions of the diagram are labeled with objects, lines with 1-morphisms and vertices with
2-morphisms. As for a pivotal category, the pivotal structure implies that left duals are also right duals and
that double duals of a 1-morphismF are 2-isomorphic toF. We thus denote the duals of a 1-morphismF by
a dashed line labeledF with an arrow that points upwards. Lines without arrows are assumed to be oriented
downwards. The (co)evaluations of the duals, which generalise (1) and (3), are then given by the diagrams
F
A B
F
AB
F
AB
F
A B
(32)
ηF : idB⇒FF l ϵF :FlF⇒ idA η′F : idA⇒FlF ϵ ′F :FF l⇒ idB
that generalise (26). The defining conditions on the left (co)evaluations, which generalise (2), read
F
AB
=
F
AB
F
A B
=
F
A B (33)
and the pivotality condition that generalises (28) is expressed in the diagrammatic identity
F
G
ν
A
B
=
F
G
ν
B A
(34)
13
In the diagrammatic calculus the pivotal structure allows one to drop the requirement that the diagrams
are progressive, i.e. that the horizontal projection of the diagram is regular. Instead, singular points of the
projection are labeled with (co)evaluations. Although we draw them as smooth maxima and minima for
diagrammatic convenience, they represent vertices in a PL diagram. While a diagram with maxima and
minima is never progressive itself, it stands for the progressive diagram obtained by replacing maxima and
minima with vertices labeled by (co)evaluations, see [BMS12, Sec. 3.2].
This enlarges the class of diagrams that represent the same 2-morphism. It is shown in [BMS12, Th. 3.9]
that planar 2-category diagrams related by orientation preserving PL homeomorphisms that preserve the
unit square represent the same 2-morphism if their labels are transformed accordingly. This means that the
objects labeling the regions and the 1-morphisms labeling lines of the diagrams must coincide, while the
2-morphisms at the vertices are composed with the (co)evaluations of the 1-morphisms at the incident lines.
Composing a 2-morphism ν : Fn··· F1 ⇒ Gm··· G1 with the (co)evaluations forFn and G1 from (32)
transforms it into 2-morphismsν′ :Fn−1··· F1⇒Fl
nGm··· G1 and ν′′ :Fn··· F1Gl
1⇒Gm··· G2.
Fn Fn−1
...
F1
Gm
...
G2 G1
ν A
B
C
D
Fn
Fn−1
...
F1
Gm
...
G2 G1
ν AB
C D
Fn Fn−1
...
F1
Gm
...
G2 G1
ν A
B
C
D
Fn Fn−1
...
F1
Gm
...
G2
G1
ν
AB
C D
(35)
The pivotal 2-category structure ensures that all diagrams that are related by the two moves in(35) and
have the same edge labels represent the same 2-morphism.
Definition 2.2.LetC be a 2-category. Acyclic transformationof a 2-morphismν :Fn··· F1⇒Gm··· G1
is a 2-morphism obtained by applying a finite sequence of the moves in(35). Two 2-morphismsν and ν′ are
called cyclically equivalentif they are related by a cyclic transformation.
In pictures, we sometimes suppress the change in the labeling and the units and counits of the adjunctions
and use the labelν for a cyclic equivalence class of 2-morphisms.
