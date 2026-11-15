---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-6
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
toc_source: inferred
doc_brief: "Reidemeister torsion on character varieties — 52 sections: Front matter; Introduction; Character varieties and Reidemeist"
---
HAL Id: tel-02108892
https://theses.hal.science/tel-02108892v1
Submitted on 24 Apr 2019
HAL is a multi-disciplinary open access archive
for the deposit and dissemination of scientific re-
search documents, whether they are published or not.
The documents may come from teaching and research
institutions in France or abroad, or from public or pri-
vate research centers.
L’archive ouverte pluridisciplinaire HAL, est des-
tinée au dépôt et à la diffusion de documents scien-
tifiques de niveau recherche, publiés ou non, émanant
des établissements d’enseignement et de recherche
français ou étrangers, des laboratoires publics ou
privés.
HAL Authorization
Reidemeister torsion on character varieties
Léo Bénard
To cite this version:
Léo Bénard. Reidemeister torsion on character varieties. Algebraic Topology [math.AT]. Sorbonne Université,
2018. English. ⟨NNT : 2018SORUS020⟩. ⟨tel-02108892⟩
Université Pierre et Marie Curie
École doctorale de sciences mathématiques de Paris
centre
Thèse de doctorat
Discipline : Mathématiques
présentée par
BENARD Léo
Reidemeister torsion on character varieties
dirigée par Julien MARCHE
Institut
de
mathématiques
de
Jussieu-Paris Rive gauche.
UMR
7586.
Boîte courrier 247
4 place Jussieu
75 252 Paris Cedex 05
Université Pierre et Marie Curie.
École doctorale de sciences
mathématiques de Paris centre.
Boîte courrier 290
4 place Jussieu
75 252 Paris Cedex 05
2
Table des matières
0
Introduction
5
1
Character varieties and Reidemeister torsion
15
1.1
Character varieties
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
15
1.1.1
Representation variety . . . . . . . . . . . . . . . . . . . . . .
15
1.1.2
Algebro-geometric quotient . . . . . . . . . . . . . . . . . . . .
16
1.1.3
Traces and skein algebra . . . . . . . . . . . . . . . . . . . . .
18
1.1.4
Characters, reducibility and irreducibility . . . . . . . . . . . .
20
1.1.5
Saito’s Theorem and some consequences
. . . . . . . . . . . .
22
1.1.6
The augmented variety . . . . . . . . . . . . . . . . . . . . . .
23
1.1.7
The tautological representation
. . . . . . . . . . . . . . . . .
24
1.1.8
Examples
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
1.2
Twisted cohomology
. . . . . . . . . . . . . . . . . . . . . . . . . . .
26
1.3
Culler-Shalen theory, group acting on trees and incompressible surfaces 29
1.3.1
The tree . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
1.3.2
Link of a vertex and ends of the tree
. . . . . . . . . . . . . .
30
1.3.3
The SL2 action : stabilizers of vertices, ﬁxed points and trans-
lation length . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30
1.3.4
Curves and valuations
. . . . . . . . . . . . . . . . . . . . . .
32
1.3.5
Group acting on a tree and splitting
. . . . . . . . . . . . . .
33
1.3.6
The split case. . . . . . . . . . . . . . . . . . . . . . . . . . . .
35
1.3.7
The non-split case
. . . . . . . . . . . . . . . . . . . . . . . .
36
1.4
Alexander module and character varieties . . . . . . . . . . . . . . . .
38
1.4.1
Reducible character in components of irreducible type of the
character variety
. . . . . . . . . . . . . . . . . . . . . . . . .
38
1.4.2
Alexander module . . . . . . . . . . . . . . . . . . . . . . . . .
39
1.5
The Reidemeister torsion . . . . . . . . . . . . . . . . . . . . . . . . .
42
3
1.5.1
First deﬁnition
. . . . . . . . . . . . . . . . . . . . . . . . . .
42
1.5.2
Second deﬁnition : the Euler isomorphism
. . . . . . . . . . .
43
1.5.3
Third deﬁnition : torsion of an exact complex (Cayley formula) 44
2
The adjoint torsion
45
2.1
The twisted complex with adjoint action . . . . . . . . . . . . . . . .
47
2.1.1
Tangent space, diﬀerential forms and twisted cohomology . . .
47
2.1.2
Computation of the twisted cohomology
. . . . . . . . . . . .
49
2.2
The adjoint torsion as a diﬀerential form . . . . . . . . . . . . . . . .
49
2.2.1
The torsion of an Ad ◦ρ-twisted cellular complex . . . . . . . .
49
2.2.2
The Reidemeister torsion form . . . . . . . . . . . . . . . . . .
50
2.2.3
Examples and computations . . . . . . . . . . . . . . . . . . .
50
2.3
The torsion at a ﬁnite point . . . . . . . . . . . . . . . . . . . . . . .
53
2.3.1
Proof of Main Theorem 1
. . . . . . . . . . . . . . . . . . . .
54
2.3.2
Interpretation of the Theorem : singularities and Alexander
module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
57
2.4
The torsion at an ideal point . . . . . . . . . . . . . . . . . . . . . . .
64
2.4.1
An example : a direct computation of the torsion of the trefoil
knot using its incompressible non-Seifert surface . . . . . . . .
65
2.4.2
Proof of theorem 2.0.2, the case when ρΣ is not residually abelian 72
2.4.3
The case when ρΣ is residually abelian
. . . . . . . . . . . . .
78
2.4.4
Back to Examples . . . . . . . . . . . . . . . . . . . . . . . . .
81
3
The standard torsion
83
3.1
The torsion function
. . . . . . . . . . . . . . . . . . . . . . . . . . .
85
3.2
The case of a ﬁnite character . . . . . . . . . . . . . . . . . . . . . . .
86
3.2.1
Proof of Theorem 3.0.1 . . . . . . . . . . . . . . . . . . . . . .
86
3.2.2
Some computations and examples . . . . . . . . . . . . . . . .
87
3.3
The torsion at ideal points . . . . . . . . . . . . . . . . . . . . . . . .
90
3.3.1
The split case . . . . . . . . . . . . . . . . . . . . . . . . . . .
90
3.3.2
The non-split case
. . . . . . . . . . . . . . . . . . . . . . . .
95
A Proof of Saito’s theorem
99
4
Chapitre 0
