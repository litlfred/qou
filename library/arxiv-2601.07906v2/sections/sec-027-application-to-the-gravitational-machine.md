---
doc_id: arxiv-2601.07906v2
doc_title: "March 2026 A universal sum over topologies in 3d gravity"
section_id: sec-027-application-to-the-gravitational-machine
section_title: "Application to the gravitational machine"
section_number: null
pages: 93-98
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
doc_brief: "March 2026 A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS 3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
The fundamental groups of the gravitational machine are changed by gluing opera-
tions along 2-punctured spheres (or cylinders). By repeatedly applying this gluing,
the fundamental group of the resulting manifolds can be precisely described using
– 93 –
graph of groups where all the vertex groups are free groups (since these correspond to
handlebodies) and all the edge groups areZ(since we are gluing along 2-punctured
spheres). By the condition a), all boundary monomorphisms∂ ±
e are injective, so the
graphs of groups are well defined. The main purpose of the theory introduced above
is now that we can construct the Bass-Serre covering tree and study the action of
the fundamental group acting on it. We use this technology to prove two results:
Result 1:Given the amalgamated productG=G 1∗H G2, ifHis malnormal
inG 1, then the centralizerC(g) ={h∈G|gh=hg}is either infinite cyclic or
conjugate to a subgroup ofG 1 orG 2. Namely,C(g) ∼= Zor there is an injective
homomorphism fromC(g) toG 1 orG 2.
Result 2:Given the HNN extensionG=G 1∗H∼K , ifHis malnormal inG 1,
andH∩g 1Kg−1
1 ={1}for allg 1∈G 1, thenC(g) is either infinite cyclic or
conjugate to a subgroup ofG 1.
These two results will follow from the following observation: for the groupGsatisfy-
ing the assumptions above, the action ofGon its Bass-Serre treeTis 2-acylindrical,
i.e. diam(Fix(g))⩽2 for everyg∈G,g̸= 1. The diameter defined here is the
maximum distance between any two vertices ˜v,˜wwhich are fixed by the action of
g∈GonT. Intuitively, this means that whenGacts onT, it only stabilizes a small
portion of the tree.
We present the proof of these results in three parts. First, we show thatGacting
onTis 2-acylindrical. Recall that for a giveng∈G, its action on the tree is either
hyperbolic or elliptic. In the second and third parts we show that, in either case,
C(g) is either infinite cyclic or conjugate toG 1 orG 2. The first result is not new and
appears in [97]. To the best of our knowledge, the second result has not been stated
in this form.
Part I: Fixed-point sets.ForGa group acting on a treeT, let Fix(g) the set
of vertices fixed byg. OnT, there is a natural metric given by the number of edges
between two vertices. Fix(g) is a subtree since for any two fixed vertices, the group
action necessarily has to fix the geodesic connecting the two vertices. Let
diam(Fix(g)) = sup{d(˜x,˜y)|˜x,˜y∈Fix(g)}(B.20)
the diameter of the fixed point set. The action of a group on a treeTis called
k-acylindrical if for allg̸= 1, diam(Fix(g))⩽k. Note that the centralizerC(g) maps
Fix(g) to Fix(g). Indeed, for ˜v∈Fix(g) andc∈C(g),gc˜v=cg˜v=c˜vand so
c˜v∈Fix(g).
Consider now the case of the amalgamated productG=G 1∗H G2 withH
malnormal inG 1. We show that the group action on the associated Bass-Serre tree
– 94 –
Tis 2-acylindrical. Suppose a portion of the tree of the form
gG2 gG1 =g′G1 g′G2
gH g′H
(B.21)
is fixed by some group element. For such a portion of the graph, we haveg −1g′∈
G1\H. The stabilizers of the edges are Stab(gH) =gHg −1, Stab(g′H) =g ′H(g′)−1.
Thus the group element has to live in the intersection of both edge stabilizers, but
this is impossible due to the malnormality ofHinG 1. Indeed, if ˜g∈Stab(gH)∩
Stab(g′H), there areh,h ′∈Hsuch that
ghg−1 = ˜g=g′h′(g′)−1,thush= (g −1g′)h′(g−1g′)−1,(B.22)
which by malnormality means thath= 1 =h ′ (sinceg−1g′∈G 1\H). Thus the fixed-
point set cannot contain any interior red vertex. Note that the opposite orientation,
with an interior blue vertex, could in principle be fixed byg, since we do not assume
His malnormal inG 2. However, since edges only connect red and blue vertices, we
conclude that diam(Fix(g))⩽2 for anyg∈G.
We can make a similar observation for the HNN case. There are three non-
equivalent configurations to consider. By the same argument as above, the fixed-
point set ofgcannot contain the corresponding portion
gtG1 gG1 =g′G1 g′tG1
gH g′H
(B.23)
sinceHis malnormal inG 1.
Consider now a portion of the form
gt−1G1 gG1 =g′G1 g′tG1
gt−1H g′H
,(B.24)
wheretis the stable letter. Elements ˜gthat stabilize this portion of the tree must
be in the stabilizers (gt−1)H(tg−1) andg ′H(g′)−1, which means that there existh,h ′
such that
gt−1htg−1 = ˜g=g′h′(g′)−1,hencet −1ht= (g−1g′)h(g−1g′)−1.(B.25)
Recall thatt −1ht∈K=∂ +(H) andg −1g′ ∈G 1. By the assumption thatH∩
g1Kg−1
1 ={1}for allg 1∈G 1, it follows thath= 1 =h ′.47 Thus, such a portion can
47Here, we are also using the fact that the homomorphismG 1→Ginduced by the inclusion of
G1 in its HNN extension is injective. ThusH∩g 1Kg−1
1 ={1}withg 1∈G 1 being trivial inG 1
means the intersection is also trivial inG.
– 95 –
also not be part of the fixed-point set. The largest possible fixed-point set is then of
the form
gt−1G1 gG1 =g′G1 gt−1G1
gt−1H g′t−1H
(B.26)
and thus also diam(Fix(g))⩽2 and the action onTis 2-acylindrical.
Part II: Centralizer of hyperbolic elements.We start with the case whereg
is a hyperbolic element of a groupGwhose action on the treeTisk-acylindrical.
We prove thatC(g) is infinite cyclic.
By definition,gtranslates along a unique geodesicL⊂T, that is,gL=L. Let
c∈C(g), then the geodesiccLis also fixed byg, sincegcL=cgL=cL. Since
the geodesic fixed bygis unique, it follows thatcL=L. Since the groupGacts
on the tree as an isometry (i.e. the action preserves distances) we have the following
homomorphism between the centralizer and the group of isometries of the integer
line
φ:C(g)−→Isom(L) (B.27)
wherecgets mapped to the isometry induced by the actioncL. The kernel of this
map corresponds to the elements ofcwhich fix the geodesicLpoint-wise. Thus, if
c∈kerφthencfixes infinitely many points, so diam(Fix(c)) =∞. This contradicts
thek-acylindricity of the action ofG. Thereforeφis injective.
The group Isom(L) consists of translations alongLand possibly reflections
around vertices (depending on the orientation of the edge arrows). Supposec∈C(g)
corresponds to a reflection. Butgtranslates along the geodesic andcgc −1 translates
along the geodesic in the other direction. Sinceg=cgc −1 this is impossible. Thus,
the image of the homomorphismφhas to lie in the translation subgroup alongL,
which is isomorphic to the integers. We conclude thatC(g) is an infinite cyclic group.
Part III: Centralizer of elliptic elements.Finally, we consider the case where
gis an elliptic element, and thus fixes a vertex ˜v. For this part we will need the
following fact aboutfinitetrees, we include a derivation of this result at the end of
the section. LetT ′ be a tree with finite diameter, i.e.
diam(T′) = sup
˜u,˜w∈T′
d(˜u,˜w)<∞,(B.28)
andG′ a group acting onT ′. Then there is one vertex ˜u∗∈T ′ that is fixed by every
elementg′∈G′. In particular all elements ofG ′ are elliptic.
Returning to the proof, we assume thatgis an elliptic element of a groupGwhose
action on the treeTisk-acylindrical. Thus, Fix(g) at least contains one vertex ˜v
and is a non-empty subtreeT ′⊂T. Since the action isk-acylindrical, Fix(g) has
finite diameter. Hence, the groupC(g) acts on the subtree of finite diameter Fix(g).
– 96 –
It follows that there is a vertex ˜v∗ in the subtree that is fixed by the action ofC(g).
Thus,
C(g)⊆Stab(˜v∗).(B.29)
IfTis the Bass-Serre tree ofG 1∗H G2 orG 1∗H, then ˜v∗ =gG i for someg∈G
andi∈{1,2}. It follows thatC(g)⊆Stab(v ∗) =gG ig−1; namely,C(g) is conjugate
to a subgroup of one of the vertex groups. This proves the theorems stated at the
beginning of the section.
Finite trees.For completeness, we include two proofs of the fact that any treeT
with a finite diameter and a groupGacting onThas a vertex ˜v ∗∈Tthat is fixed
by the group action. We suppress the tilde notation in this part of the section and
simply writev ∗ instead of ˜v∗.
The first proof follows from the observation that a nontrivial tree with finite
diameter must contain vertices of different degrees. The degree of a vertex is the
number of edges attached to it. In particular, the vertices at the end of the tree
must be of degree one. The only trees where all vertices have the same degree are
the single vertex with no edges, and two vertices joined by one edge.
The action of any elementg∈Gmust preserve the degree of the vertex, soG
permutes between vertices of the same degree. LetT ′ be the subtree obtained by
removing the vertices of degree one. It follows thatGpreservesT ′, and diam(T′)<
diam(T). Since the diameter decreases at each step, this process can occur only
finitely many times. The final tree is one of the trivial cases: either a single vertex or
a single edge with two vertices. In either case, sinceGpreserves edge orientations,
Geither fixes the single vertex or the two vertices joined by an edge.
The second proof we present identifies the fixed vertex with the the central vertex
of the graph. To explain the construction, let
e(v) = sup
w∈T
d(v,w) (B.30)
be the eccentricity of a vertex. By definition,e(v)⩽diam(T)<∞. We also let
ρ= min v∈T e(v) the minimal eccentricity. We define the center of the graph as the
set of vertices with minimal eccentricity,
C(T) ={v∈T|e(v) =ρ}.(B.31)
Since the group action preserves distances, it has to preserve the setC(T). We claim
thatC(T) consists of either one of two vertices connected with a single edge. In both
cases (since edge inversions are not allowed),GfixesC(T) elementwise and thus we
may choosev ∗∈C(T).
To see whyC(T) consists of at most two vertices, letγbe a path of maximal
length diam(T) throughTrealizing max v,w∈T d(v,w) (without backtracking). Denote
the two endpoints byγ − andγ +. Letv∈Tbe any vertex. We can find a unique
– 97 –
closest vertex onγwhich we denote byπ(v). This is also called the projection ofv
onγ. The geodesic path fromvtoγ ± then has to pass throughπ(v). Thus
e(v)⩾max(d(v,γ +),d(v,γ −)) (B.32)
=d(v,π(v)) + max(d(π(v),γ +),d(π(v),γ −)) (B.33)
⩾d(v,π(v)) +⌈ 1
2 diam(T)⌉.(B.34)
In the last step, we used thatd(π(v),γ +) +d(π(v),γ−) = diam(T). Thus we see that
ρ=⌈ 1
2 diam(T)⌉. It is precisely attained by the central or the two central vertices of
the pathγ. For a vertex outside ofγ,d(v,π(v))>0 and thus they are not part of
C(T). The claim follows.
