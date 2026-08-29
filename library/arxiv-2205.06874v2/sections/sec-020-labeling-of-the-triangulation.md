---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-020-labeling-of-the-triangulation
section_title: "Labeling of the triangulation"
section_number: null
pages: 29-31
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
To define the state sum of a generic transversal triangulated 3-manifold with defect data, we assign objects
and morphisms of the associated categories to the edges and triangles of the triangulation. For this, we fix
sets I of representatives of the isomorphism classes of simple objects and associated projection and inclusion
morphisms pα
xi :x→i and jα
xi :i→x satisfying (53) for all spherical fusion categories at the regions ofM
and for all bimodule categories at the defect areas.
Definition 4.2. LetM be generic transversal triangulated 3-manifold with defect data. Alabeling of M is
an assignment of the following data to the edges of the triangulation:
(i) to each edgee contained in a region labeled byC, a simple objectl(e)∈IC,
(ii) to each edgee that intersects a defect area labeledM, a simple objectl(e)∈IM.
A pair (M,l ) of a generic transversal triangulated 3-manifoldM with defect data and a labelingl is called a
labeled defect 3-manifold.
Note that the orientation of the edges from Section 4.1 is arbitrary in (i), but fixed by the orientations of the
defect surfaces in (ii). In (i) we would assign to the edge with the opposite orientation the unique object in
IC that represents the isomorphism class of the dual objectl(e)∗. In (ii) orientation could only be reversed
simultaneously for all edges of a tetrahedron that intersect a defect surface. This would amount to reversing
the orientation of each defect area and replacing its bimodule categoryM byM#, as explained in Section
4.1. In this case, we would assign to the edge with the opposite orientation the same object as an object of
M#.
29
M
N
P
p
n
m
C
i
j k
F
G H
ν
D
 c
d
m
p
n
q
F
K
GH
P Q
M N
C
D
ν
(b)
(a)
Figure 2: Generic transversal tetrahedra that intersect a defect surface.
(a) labeling withF :P→M , G :N→M , H :P→N and ν :F⇒GH,
(b) labeling withF :Q→P , G :N→Q , H :M→P , K :N→M and ν :FG⇒HK.
A labeling of a triangulated manifold with defect data defines a labeling of each triangle in the triangulation.
To each labeled triangle, we associate two morphism spaces, one for each orientation. For a triangle labeled
by objects in(C,D)-bimodule categoriesM,N that intersects a defect line labeled by a bimodule functor
F :M→N or G :N→M , the associated morphisms spaces are
n∈INm∈IM
c∈IC
F
m∈IMn∈IN
c∈IC
F + : HomN (F (c▷m),n )
− : HomN (n,F (c▷m)) (70)
n∈INm∈IM
c∈IC
G
m∈IMn∈IN
c∈IC
G + : HomM(c▷m,G (n))
− : HomM(G(n),c▷m)
n∈INm∈IM
d∈ID
F
m∈IMn∈IN
d∈ID
F
+ : HomN (F (m◁d),n )
− : HomN (n,F (m◁d))
n∈INm∈IM
d∈ID
G
m∈IMn∈IN
d∈ID
G
+ : HomM(m◁d,G (n))
− : HomM(G(n),m◁d).
Here, the triangles are equipped with the orientation induced by their edge orientation and the embedding in
the plane, via the right-hand rule. The first triangle in each line has positive (+) and the second negative (-)
orientation. The arrows indicate the orientation of the defect line relative to the orientation of the triangle.
They agree, if the arrow points downwards, and are opposite, if it points upwards. As the orientation of the
defect lines is fixed, reversing the orientation of the triangle reverses the orientation of this arrow.
The morphism spaces are obtained from the triangles as follows: The objects inC andD act on the object of
30
M
N
P
p
n
m
C
i
j k
F
G H
ν
D
α
c
d
m
p
n
q
F
K
GH
P Q
M N
C
D
ν
(b)
(a)
Figure 3: Projecting the data from spherical categories on the polygon.
M orN with whom they share a vertex with one incoming and one outgoing edge. Arrows labeled withC
have this vertex as their starting vertex, arrows labeled byD as their target vertex. The morphisms go from
the object on the left to the one on the right. The functor is applied to the object on the left, if its arrow
points downwards, and to the one on the right, if it points upwards.
ForM =N and F =G = idM, the diagrams in the first and the second row and in the third and the fourth
row in(70) coincide. SettingM =N =C,▷ =⊗ =◁ and F = G = idC yields the usual assignment of
morphisms to triangles for the Turaev-Viro-Barrett-Westbury invariants of a spherical fusion category.
