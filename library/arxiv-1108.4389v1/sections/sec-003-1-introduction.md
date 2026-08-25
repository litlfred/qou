---
doc_id: arxiv-1108.4389v1
doc_title: "b partition functions of two mirror 3d N = 2 gauge theories are equal. Three-dimensional N = 2 ﬁeld theories associated to 3-manifolds can be thought of as theories that describe b"
section_id: sec-003-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-8
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
2. Geometry of 3-manifolds 7
2.1 Building blocks 8
2.2 Gluing 10
2.3 Geodesic boundaries 12
2.4 Torus cusps 16
2.5 Changing the triangulation 18
3. Operations on 3d abelian theories 19
3.1 An Sp(2N, Z) action on 3d CFTs with U(1)N ﬂavor symmetry 20
3.1.1 Generalities 20
3.1.2 Adding supersymmetry 22
3.2 A Z2 action on 3dN = 2 theories with a chiral operator 23
3.3 UsefulN = 2 mirror symmetries 24
4. Construction of TM 29
4.1 Deﬁnition 29
4.2 The bipyramid and the 2–3 move 32
4.3 The ﬂip 35
4.4 TM as a boundary condition 36
4.5 The octahedron 36
4.6 Figure-eight knot 38
5. Moduli space on R2×S1 40
5.1 The tetrahedron 41
5.2 The bipyramid 43
6. S3
b partition functions 44
6.1 Chirals and tetrahedra 46
6.2 Gluing and bipyramids 47
6.3 Figure-eight knot 49
6.4 Relation to moduli spaces on R2×S1 50
7. Line operators and q–diﬀerence equations 51
– 1 –
1. Introduction
One of the predictions of String Theory/M-Theory is the existence of a discrete family of
maximally symmetric six-dimensional conformal ﬁeld theories, labeled by a simply-laced Lie
algebra g. These theories lack a Lagrangian deﬁnition, but some of their properties are
known. The existence of such six-dimensional SCFT’s has a simple, but perhaps surprising,
consequence: it allows a geometric description of many lower-dimensional supersymmetric
ﬁeld theories. Indeed, one can deﬁne large families of 6 −d dimensional theories T [Md, g]
via compactiﬁcation of the six-dimensional theory labeled by g on a d-dimensional manifold
Md. If the compactiﬁcation is accompanied by an appropriate twist, it will lead to theories
with 6−d dimensional supersymmetry. In order to fully exploit this type of construction,
one should ideally give an alternative explicit deﬁnition of these “eﬀective” theories directly
in 6−d dimensions. If that can be accomplished, the result is a large family of theories
deﬁned in 6−d dimensions, whose properties are controlled by the geometry of d-dimensional
manifolds.
This program was pursued successfully for d = 2 [ 1, 2, 3]. The compactiﬁcation of
the six-dimensional theories on a Riemann surface C leads toN = 2 supersymmetric gauge
theories T [C, g] in four dimensions. The geometry of the Riemann surface controls a variety
of protected quantities in the four-dimensional gauge theories: the space of exactly marginal
deformations, the space of vacua in ﬂat space and upon compactiﬁcation on a circle, the
partition function of the Ω-deformed theory, the S4 partition function, the superconformal
index, etc.
It is natural to wonder if there is a similar d = 3 dictionary. A twisted compactiﬁcation
of a 6d theory on a three-manifold M3 will give an N = 2 ﬁeld theory T [M3, g] in three
dimensions. Some properties of these theories follow from the deﬁnition. For example, one of
the basic properties of the 6d theories is that they reduce to 5d SYM upon compactiﬁcation
on a circle. If we consider a 6d SCFT on S1×M3, we ﬁnd that the moduli space of vacua of
T [M3, g] is the same as the space of ﬂat complex g-connections on M3 [4].
One way to ﬁnd other properties of this d = 3 correspondence is to draw lessons from its
d = 2 version. Indeed, consider a three-dimensional cobordism, i.e. a 3-manifold M3 which
interpolates between two (or, more generally, several) Riemann surfaces, as in Figure 1. The
compactiﬁcation of the six-dimensional theory on the cobordism should give a domain wall
between the 4d theories associated to the Riemann surfaces. Note, in particular, that a half-
BPS domain wall ( cf. Figure 1) or a boundary condition ( cf. Figure 2) in a 4d N = 2
ﬁeld theory preserve the same amount of supersymmetry as a three-dimensional N = 2 ﬁeld
theory.
Therefore, one possible strategy for understanding T [M3, g] is to directly leverage the
d = 2 correspondence to construct the three-dimensional ﬁeld theories: take a closed manifold
M3, and stretch it to a conﬁguration of long tubes with a Riemann surface as cross sections,
joined by appropriate plumbing ﬁxtures, i.e. cobordisms. One could then reduce the six-
dimensional theory on the tubes of section C to give known four-dimensional gauge theories
– 2 –
& &
0 7
0
 7
&

7
&

D
 E

Figure 1: (a) A cobordism M betweenC andC′ gives rise to a domain wall ( b) between 4d N = 2
theories T (C) and T (C′).
T [C, g] on segments, cf. Figure 2. These theories would be coupled through the domain walls
associated to the plumbing ﬁxtures, and the whole setup taken to deﬁne a three-dimensional
gauge theory in the IR.
This strategy is hampered by the rapid proliferation of possible “elementary” plumbing
ﬁxtures: one would need to ﬁnd a way to construct the corresponding domain walls by hand,
and demonstrate a large set of mirror symmetries which relate diﬀerent ways to glue together
the same manifold. This should be contrasted with a similar approach in d = 2, where the
tubes are all cylinders with S1 cross-section, and the only plumbing ﬁxture is the pair of
pants.
We will follow an alternative, simpler strategy. Namely, we will abandon the restriction
to cut the manifold along tubes only, and instead propose a candidate N = 2 SCFT TM
for the theory T [M, su(2)] based on a decomposition (triangulation) of a 3-manifold M into
tetrahedra, glued together along the triangular faces. Note, here and in the rest of the paper
we focus (mainly for simplicity) on g = su(2). Moreover, since we are interested only in the
case d = 3, so here and in what follows we denote M3 simply by M.
We do not derive our construction of the N = 2 theory TM directly from properties of
the six-dimensional theory. Instead, we wish to associate a simple “building block” theory
T∆ to each tetrahedron ∆, and to deﬁne the ﬁeld theory analogue of the geometric gluing
with a simple constraint in mind: diﬀerent triangulations of the same manifold must give
equivalent deﬁnitions of the corresponding theory, in the sense that they ﬂow to the same
SCFT in the IR. In d = 2 diﬀerent decompositions of the same Riemann surface were related
by known S-dualities. In d = 3 we aim to relate diﬀerent triangulations of M through known
mirror symmetries, so that every 3-manifold M is associated to a well-deﬁned, triangulation-
independent 3dN = 2 SCFT.
We describe the theory TM as the IR ﬁxed point of an abelian Chern-Simons-matter
theory whose Lagrangian depends on the choice of triangulation of M (plus some extra
decoration Π that one encounters in SL(2) Chern-Simons theory on M). Intuitively, given a
– 3 –
&
7
&
 7
0
7
0

D
 E

 00 
Figure 2: (a) A 3-manifold M stretched along a ‘neck’ R×C becomes a 4d N = 2 superconformal
theory (b) on R3×I coupled to 3-dimensional theories T (M +) and T (M−) at the boundary. The 4d
N = 2 gauge theory in the bulk is determines by the cross-section C of the 3-manifold M.
triangulation M =⋃N
i=1 ∆i, we construct a theory for each tetrahedron ∆ i
∆i ↝ T∆i, (1.1)
and glue the tetrahedra together to build
M ↝ TM∼
⨂
i
T∆i. (1.2)
The gluing of theories T∆i involves a bit more than just taking a tensor product, and one of
the main technical aims of this paper is to develop a proper understanding of the sign ‘ ∼’
in (1.2). Loosely speaking, the gluing involves two steps, which require a careful explanation
and depend on a choice of the extra data Π (deﬁned below): gauging some ﬂavor symme-
tries, with carefully chosen Chern-Simons couplings, and adding a superpotential coupling
for each internal edge of the triangulation. The choice of the operators which enter the su-
perpotential couplings is the most subtle part of the construction. In general, they cannot be
simultaneously realized as products of elementary ﬁelds, but are deﬁned as ’t Hooft monopole
operators.
Regardless of the compactiﬁcation from six dimensions, the family of 3d N = 2 SCFTs
TM associated to 3-manifoldsM is an interesting object, and we hope it will lead to interesting
connections between three-dimensional SCFTs and three-dimensional geometry and topology.
For example, quantities like the superconformal index of TM or the partition function on S3
should map to interesting three-manifold invariants, as summarized in Table 1. In this paper
we specialize to a very simple building block theory for the tetrahedron, which is essentially the
theory of a single chiral multiplet. We believe our approach is much more general though, and
with an appropriate choice of tetrahedron building block one can produce natural candidates
for T [M, g].
– 4 –
3-manifold M 3dN = 2 theory TM
ideal tetrahedron theory T∆
change of triangulation mirror symmetry
change of polarization Π Sp(2N, Z) duality action
boundary ﬂip F transformation
gluing along superpotential
an internal edge coupling
Wilson lines line operators
boundaryC =∂M coupling to 4dN = 2 theory
ﬂat SL(2, C) connections SUSY moduli on R2×S1
Vol(M) +iCS(M) twisted superpotential ~Weﬀ
SL(2) Chern-Simons
partition function on S3
bpartition function
Seiberg-Witten invariants superconformal index
Table 1: The dictionary between geometry and physics.
We will be able to motivate our proposal for TM =T [M, su(2)] in a wide variety of ways,
and to check that it has expected properties. In particular, we take inspiration from two
related facts:
• The moduli space of vacua of the 3d theory must coincide (with some caveats) with the
space of ﬂat SL(2) connections on M.
• The partition function of T [M, g] on an ellipsoid S3
b , as in [ 5], should coincide with the
(analytically continued) g Chern-Simons partition function on M.
We engineer TM = T [M, su(2)] in such a way that these two properties are automatically
true.
One may wonder why the IR dynamics of the non-abelian six-dimensional theory on a
3-manifold M should admit a dual 3d description based on abelian gauge ﬁelds. A likely
answer is that in a generic vacuum of the 3d theory, the 6d theory is deep in its Coulomb
branch on most of M. Far on the Coulomb branch, the 6d theory reduces to an abelian
theory of self-dual forms. It is conceivable that the abelian gauge ﬁelds in our description
arise from these 6d abelian ﬁelds, and the matter ﬁelds arise from excitations localized in
the regions of M where the 6d theory is close to the origin of the Coulomb branch. Similar
ideas are useful for d = 2, but they give rise to IR-free, non-UV complete four-dimensional
abelian gauge theories. On the other hand, a three-dimensional abelian gauge theory is a UV
complete description of an IR ﬁxed point.
– 5 –
Finally, we should describe in more detail the class of 3-manifolds M to which our con-
struction applies. In the d = 2 case, it is useful to introduce codimension two defects of the
six-dimensional (2, 0) theory, which sit at points of the Riemann surface and ﬁll the entire 4d
space-time. These defects do not break any further supersymmetry, and greatly extend the
space of four-dimensional N = 2 theories which are amenable of a geometric construction.
The presence of even a single puncture allows one to use some interesting tools based on
“ideal” triangulations of Riemann surfaces, which have vertices at the defects only. Similarly,
ind = 3 one can add the very same kind of defects, which ﬁll the entire 3d space-time and are
supported on a line (or, better, on a knot/link) insideM. Again, our construction employs an
“ideal” triangulation: the tetrahedra have vertices at the defects. In particular, the manifold
should have at least one defect. In d = 2 a defect can represent a semi-inﬁnite tubular region
of the surface, and the same is true in d = 3.
Our construction does not actually force us to glue all the faces of the tetrahedra pairwise
together, to get a closed manifold with defects. We can also do a partial gluing, and obtain
theories associated to manifolds with boundaries made by faces of the tetrahedra. The defects
and boundaries both have an interpretation in terms of coupling to four-dimensional N = 2
theories. The diﬀerence is that defects represented by semi-inﬁnite tubular region with a cross
sectionC correspond to couplings of theories TM toN = 2 theories in the UV. In particular,
for our theories TM = T [M, su(2)] that come from compactiﬁcation of the (2 , 0) theory of
type g = su(2), the corresponding N = 2 theories associated to C in the UV typically have
SU (2) gauge groups. For example, closed cusps in M represented by semi-inﬁnite tubular
region with a 2-torus C = T 2 as a cross section correspond to coupling to four-dimensional
N = 4 super-Yang-Mills with gauge group SU (2).
On the other hand, a big, “geodesic” boundary of M (formed from unglued tetrahe-
dron faces) of topology C represents coupling of theory TM to the IR limit of the N = 2
four-dimensional theory T [C] ( cf. Figure 2). In contrast to its UV version, this IR theory
is usually abelian. Therefore, to summarize, each boundary of M corresponds to a possible
coupling of the 3d N = 2 theory TM to either IR or UV limit of the 4d N = 2 gauge theory
T [C], depending on whether the boundary C is big and “geodesic” or small and “defect-like.”
This is very natural because a typical example of a boundary condition for a weakly coupled
four-dimensionalN = 2 ﬁeld theory consists of a three-dimensional N = 2 ﬁeld theory living
at the boundary and coupled to the bulk degrees of freedom. Looking at the same boundary
condition or domain wall in diﬀerent weakly coupled regions of the bulk parameter space
leads to diﬀerent descriptions involving diﬀerent three-dimensional degrees of freedom.
The paper is organized as follows. In section 2 we will review the geometric properties of
triangulated three-manifolds that will inspire the construction of TM. In fact, we will need
to generalize the standard constructions a little bit in order to describe triangulations of 3-
manifolds that support irreducible ﬂat SL(2, C) connections. Section 3 reviews the physical
tools needed for the construction of TM, whereas the deﬁnition of the 3d N = 2 theory TM
is presented in section 4. Section 5 describes the match between the moduli space of ﬂat
– 6 –
connections on M and the moduli space of vacua of the theory TM on a circle. Section 6
describes a similar match between the SL(2) Chern-Simons partition function of M and the
ellipsoid partition function ofTM. Finally, section 7 extends the dictionary between geometry
of M and physics of TM to line operators.
