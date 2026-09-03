---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-021-generalised-6j-symbols
section_title: "Generalised 6j symbols"
section_number: null
pages: 31-37
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
We now associate a generalised 6j symbol to each labeled generic transversal tetrahedront with a defect
surface. Note that such a defect tetrahedron is more than a combinatorial tetrahedron with categorical data
assigned to each oriented edge. It consists of a combinatorial tetrahedront, an oriented defect polygonP, an
assignment of certain edges oft to the vertices ofP and an assignment of the vertices oft to the two regions
labeled byC andD. In particular, a labeled generic transversal tetrahedron inherits an orientation, because
the defect surface is oriented and assigningC andD to the two sides of the surface specifies a positive normal
vector to the surface
The orientation oft induces an orientation of all of its triangles. To each oriented triangle we assign a
morphism in the associated morphism space from(70). To a tetrahedron with these assignments, we associate
a polygon diagramD as follows:
1. The defect surface int is a polygonP. The defect data inP, viewed from the region labeledC towards
the region labeledD, defines a cyclic equivalence class of diagrams forBimodθ(C,D).
2. Pushing the endpoints of defect lines on each side ofP to the middle without creating crossings does
not change the cyclic equivalence class of the diagram. We thus assume that each side ofP is the
endpoint of exactly one defect line as in Figure 2, possibly labeled with a composite of functors.
3. Drawt such that edges and triangles labeled by data fromC andD lie on the corresponding sides of
the polygonP and that edges intersectingP are oriented by the positive normal vector ofP.
31
4. For each edgee of t that does not intersectP, draw the dual edge¯e, starting and ending on the
boundary ∂P and with its endpoints are displaced slightly from the endpoints of defect lines. They
are displaced towards the starting and target end ofe, ife is contained in the region forC andD,
respectively. Orient ¯e by duality, as shown in Figure 3, and project it onP.
5. Label the vertices ofP with the simple objects of the associated edges oft and the projected edges with
the simple objects of their duals int. Label the endpoints of defect lines and the projected vertices in
P with the morphisms assigned to the corresponding triangles int. The result is a polygon diagramD.
The diagrams for the tetrahedra in Figures 2 and 3 are shown in (71).
Note that the wordproject in 3. is used informally here. For the tetrahedron in Figure 3 (a) it means drawing
a trivalent vertex onP whose incident edges are connected with the endpoints on∂P. For the tetrahedron in
Figure 3 (b) it amounts to drawing two edges that connect endpoints on opposite sides ofP. The properties
of diagrams for spherical fusion categories and identities(39) to (43) ensure that all ways of doing so yield
polygon diagrams with the same evaluation.
Note also that tetrahedra that do not intersect defect surfaces can be viewed as special cases of Figure 2
(a) and (b). Each such tetrahedron has one vertex with only outgoing edges, which can be taken as the
lower vertex in Figure 2 (a) or as the left vertex in Figure 2 (b). Up to orientation reversal the tetrahedron
then coincides with the one in Figure 2 (a) or (b), if the defect surfaces are labeled with the spherical fusion
categoryC as a (C,C)-bimodule category, with identity functors and with identity natural transformations.
Interpreting a combinatorial tetrahedron as a tetrahedron with trivial defects amounts to a choice of orientation:
one needs to specify an orientation for the trivial defect surface and to specify its normal vector. We therefore
treat oriented tetrahedra labeled by a spherical fusion categoryC as generic transversal tetrahedra with
trivial defect data. In the following, we assume that all tetrahedra are equipped with an orientation.
Definition 4.3. Let (t,l ) be a labeled generic transversal tetrahedron with an assignmentb of morphisms
in the spaces(70) to its triangles. The generalised 6j symbol 6j(t,l,b ) is the cyclic evaluation of the
associated polygon diagramD. This defines a linear map
6j(t) :
⨂
f∈∆
Hom(f,l )→ C, b ↦→6j(t,l,b ),
where ∆ denotes the set of triangles oft, Hom(f,l ) the morphism space from(70) for a trianglef∈ ∆ and
the tensor product stands for the unordered tensor product of these morphism spaces for all triangles.
Example 4.4. The generalised 6j symbols for the tetrahedra in Figure 2 are the cyclic evaluations of
m
p n
H
F G
i
k
jν
α
γ
β δ
p q
nm
d
F
GH
Kc
ν
α
β
γ
δ
(71)
32
and given by the diagrams
m
m
p
n
F i
H
k
G
j
β
γ
δ
αν
p
p
q
n
m
d
F
G
K
H
c
α
β
γ
δ
ν (72)
Definition 4.3 also defines the usual 6j symbols of tetrahedra labeled by a spherical fusion categoryC that
occur in the Turaev-Viro-Barrett-Westbury state sum. However, they are not defined as 6j symbols of
combinatorial tetrahedra, as in [BW96], but as 6j symbols oforiented combinatorial tetrahedra.
The 6j symbols from Definition 4.3 encode the natural transformations on the defect polygon and the
coherence isomorphisms for the defect data. If the former are trivial, we obtain the following cases:
• IfP =N =M,F =G =H = idM andν = ididM for the tetrahedron in Figure 2 (a) and the associated
6j symbol in(72), we obtain a number that characterises the isomorphismcj,k,p : (j⊗k)▷p→j▷(k▷p)
from Definition 1.2. It follows from (53) that it is given by
cj,k,p =∑
i,m,n
α,β,γ,δ
dim(i)
dim(m)
dim(n)
m
m
p
n
i
k
j
β
γ
δ
α
j k
i
j k
p
p
m
n
α
β
δ
γ
(73)
where the sum runs over simple objectsi∈IC, m,p∈IM and bases of the associated morphism spaces.
There is an analogous generalised 6j symbol forD-right module categories, which arises from a
tetrahedron analogous to Figure 2 (a), but with a vertex in the region labeled byD and with the
orientations of the coloured edges reversed.
• In particular, ifM is a spherical fusion categoryC as a left module category over itself, we obtain the
usual 6j symbol for the spherical fusion categoryC that encodes the associator on simple objects:
aj,k,p =∑
i,m,n
α,β,γ,δ
dim(i)
dim(m)
dim(n)
m
m
p
n
i
k
j
β
γ
δ
α
j k
i
j k
p
p
m
n
α
β
δ
γ
(74)
33
• SettingQ =P =N =M, F =G =H =K = idM and ν = ididM in Figure 2 (b) and(72) yields the
6j symbol that characterises the isomorphismbc,n,d : (c▷n)◁d→c▷ (n◁d) from Definition 1.2:
bc,n,d =∑
m,p,q
α,β,γ,δ
dim(m)
dim(p)
dim(q)
p
p
d
c
q
n
m
α
β
γ
δ
d c n
n
q
p
m
c d
β
α
δ
γ
(75)
• In particular, forM =C =D identity (75) yields the usual 6j symbol for a spherical fusion categoryC
that encodes its associator, but in a diagrammatic representation different from (74)
ac,n,d =∑
m,p,q
α,β,γ,δ
dim(m)
dim(p)
dim(q)
p
p
d
c
q
n
m
α
β
γ
δ
d c n
n
q
p
m
c d
β
α
δ
γ
(76)
• If we setQ =P,N =M, G =H :M→P , F = idP, K = idM, ν = idG and c =e in Figures 2 (b)
and (72), we obtain the 6j symbol for the isomorphismtG
n,d :G(n)◁d→G(n◁d) from Definition 1.8:
tG
n,d =∑
m,p,q
α,β,γ,δ
dim(m)
dim(p)
dim(q)
p
p
d
G
q
n
m
α
β
γ
δ
d G n
n
q
p
m
G d
β
α
δ
γ
(77)
• Setting insteadP =M,Q =N, F =K :N→M , G = idN, H = idM, ν = idF and d =e in Figures
2 (b) and(72) yields the 6j symbol for the isomorphismsF
c,n :F (c▷n)→c▷F (n) from Definition 1.8:
sF
c,n =∑
m,p,q
α,β,γ,δ
dim(m)
dim(p)
dim(q)
p
p
F
c
q
n
m
α
β
γ
δ
F c n
n
q
p
m
c F
β
α
δ
γ
(78)
34
In all cases the diagrammatic expressions for the inverses of the coherence isomorphisms are obtained by
reflecting the diagrams on a horizontal axis. This corresponds to evaluating the associated polygon diagrams
counterclockwise and to an orientation reversal of the associated defect surface. This is possible, because all
of the bimodule natural transformations in these tetrahedra are bimodule natural isomorphisms and hence
their directions can be reversed, see the discussion before Definition 2.14.
We now investigate how the 6j symbols depend on the orientations of edges labeled by objects in spherical
fusion categories. Recall that reversing the orientation of such an edge does not affect the orientations of the
adjacent triangles and tetrahedra. Although it induces an odd permutation of the vertex numbers, which
may be viewed as an orientation reversal for the associatedcombinatorial tetrahedron, the orientations in our
formalism are fixed as part of the data.
Reversing the orientation of such an edge and replacing its label by its dual induces natural isomorphisms
between the morphism spaces for the adjacent triangles.
For aC-module functor F :M→N and the first morphism space from(70), we obtain the following
isomorphism that is natural inc∈ ObC, m∈ ObM and n∈ ObN
nm
c
F
HomN (F (c▷m),n )
m
n
cF
α −→
nm
c∗
F
HomN (F (m),c∗▷n)
m
n
F
c
α (79)
nm
c
F
HomN (F (c▷m),n )
m
n
F c
β ←−
nm
c∗
F
HomN (F (m),c∗▷n)
m
n
F
c
β
For aC-module functorG :N→M and the third morphism space from (70) we have the isomorphism
nm
c
G
HomN (c▷m,G (n))
m
n
c
G
α −→
nm
c∗
G
HomN (m,G (c∗▷n))
m
nG c
α (80)
nm
c
G
HomN (c▷m,G (n))
m
nG
c
β ←−
nm
c∗
G
HomN (m,G (c∗▷n))
m
nG c
β .
The isomorphisms for the other morphism spaces from(70) are analogous, just that the black line labeledc
may be replaced by a grey line labeledd that crosses under the dashed lines for the functors.
With these transformations of the morphism spaces one finds that reversing the orientation of an edge labeled
by a spherical fusion category does not affect the generalised 6j symbols of defect tetrahedra.
Lemma 4.5. The 6j symbol of a labeled generic transversal tetrahedron is invariant under reversing an edge
labeled with an objectc∈IC or d∈ID, replacing its label with the dual and transforming the morphisms at
its triangles according to(79) and (80).
Proof. This follows by a direct diagrammatic computation from(79) and (80), together with identity(27)
and the second identity in(50) for the trace, applied to the black and grey lines of the diagram. It also uses
35
identities (39) to (43) that encode the Reidemeister moves and the naturality conditions for the over- and
undercrossings. For the first diagram in (72) this yields
m
m
p
n
F i
H
k
G
j
β
γ
δ
αν (27)
=
m
m
p
n
F i
H
G
j
k
β
γ
δ
αν (27),(50)
=
m
m
p
n
F
i
H
k
G
j
j
β
γ
δ
αν
(27)
=
m
m
p
n
F
H
k
G
j
j
i
β
γ
δ
αν (27),(50)
=
m
m
p
n
F
H
G
j
j
k
k
i
β
γ
δ
αν (27)
=
m
m
p
n
F
H
G
j
j
k
k
i
β
γ
δ
αν
and for the second diagram in (72)
p
p
q
n
m
d
F
G
K
H
c
α
β
γ
δ
ν
(27),(50)
=
p
p
q
n
m
d
d
F
G
K
H
c
α
β
γ
δ
ν
36
(27),(50)
=
p
p
q
n
m
d
d
F
G
K
H
c
c α
β
γ
δ
ν
(27),(50)
=
p
p
q
n
m
dF
G
K
H
c
c α
β
γ
δ
ν
The generalised 6j symbols are also invariant under a simultaneous orientation reversal of the defect surface
and all defect lines on the surface, if the defect data is transformed accordingly.
Lemma 4.6. The 6j symbol of a labeled generic transversal tetrahedron is invariant under
• reversing the orientation of all defect areas and all defect lines,
• replacing each(C,D)-bimodule categoryM by the (D,C)-bimodule categoryM#,
• replacing each bimodule functorF :M→N by F # :M#→N #,
• replacing each bimodule natural transformationν :F⇒G by ν# :G#⇒F #.
Proof. By Lemma 4.5, one may additionally reverse the orientation of all edges labeled with objects in
spherical fusion categories and replace those objects by their duals without changing the associated 6j symbol.
Lett be a generic transversal tetrahedron andt′ the tetrahedron obtained fromt by reversing the orientations
of all defect areas, defect lines and edges oft and transforming their labels accordingly. For each triangle oft
the corresponding triangle oft′ has the same morphism space assigned to it by(70), but interpreted as a
morphism space in the opposite category. For instance,HomM(F (c▷m),n )is viewed asHomM#(n,F (m◁c∗))
and HomM(m◁d,G (n)) is viewed asHomM#(G(n),d∗▷m).
Projecting the data from the spherical fusion categories on the defect plane oft′ then yields a mirror image
of the polygon diagram fort, in which the orientation of all interior lines is reversed, each bimodule category
M is replaced by its oppositeM#, each bimodule functorF byF #, each bimodule natural transformation
ν by ν# and each object in a spherical fusion category by its dual. As the left action ofc∈ ObC or the
right action ofd∈ ObD onM corresponds to the right action ofc∗ and the left action ofd∗ onM#, the
evaluations of the polygon diagrams fort′ and t are equal by Corollary 2.15.
